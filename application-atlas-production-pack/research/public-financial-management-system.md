# Research Notes — Public Financial Management System

## Research Goal

Understand the Public Financial Management System (PFM / IFMIS / GRP / government ERP) software Type: what the government's financial system of record actually is, what fiscal machinery it holds (chart of accounts, funds, appropriations, commitments, ledger), how the budget-execution loop works, what money operations run inside it (expenditure, receipts, treasury), who operates it, and where its boundaries sit against the neighboring Types.

This pass also discharges (from this side) one pre-hung joint-review flag:

1. public-budgeting-platform (2026-09-09): "FreeBalance demonstrates budgeting machinery as one pillar of a PFM/GRP suite — seam = budget-cycle center vs whole-fiscal-architecture center, overlap zone = budget execution controls (appropriations/commitments); ratify when public-financial-management-system is processed."

## Initial Boundary

Working hypothesis before research:

- A Public Financial Management System is the government's whole-of-finance system of record: a unified financial ledger organized in the government's own fiscal framework (chart of accounts / budget classification, funds, organizational units, fiscal periods), carrying budget execution control (appropriations, allotments, commitments), and operating the government's money flows (expenditure, receipts, treasury), commonly with civil service/payroll alongside.
- Market names for the same Type: PFM software, IFMIS (Integrated Financial Management Information System), GRP (Government Resource Planning), government ERP / public sector ERP, government financials / fund accounting suites.
- Nearest neighbors: Public Budgeting Platform (§24, processed — budget-cycle center), Accounting Software / General Ledger System (§08 — ledger engine), Enterprise Resource Planning / ERP (§10 — private-sector analog), Government Revenue Management (§24, processed — money-in operationalization), Tax Administration System (§24), Treasury Management System (§08 — corporate analog), Government Procurement Platform (§24, processed), Government Grants Management (§24, processed), Payroll System (§09).
- Unknowns: whether budget formulation is definitional or common; whether receipts and treasury are definitional or common; how the US local-government fund-accounting pole maps onto the international IFMIS pole; whether the "single unified system" framing is definitional or an ideal-type.

## Research Questions

1. What is the unit of record — the ledger, the budget, or the fiscal framework?
2. What exactly is the government's fiscal framework (chart of accounts / budget classification, funds, organizational units, fiscal periods)?
3. How does budget execution control work (appropriations, allotments, commitments/obligations, real-time availability)?
4. What money operations run inside the system (expenditure cycle, receipts, treasury/cash/debt)?
5. Who are the users (ministry of finance, budget office, accountant-general, line ministries, local finance departments, auditors)?
6. What is in-scope vs out-of-scope (payroll/civil service, procurement, revenue collection, assets, projects/grants)?
7. Where are the boundaries vs Public Budgeting Platform, Accounting/GL, ERP, Government Revenue Management, Treasury Management, Government Procurement, Government Grants Management?
8. Would older / regional / differently-positioned realizations (paper-era treasury bookkeeping, US municipal fund accounting, 1990s IFMIS) still fit the definition?

## Representative Products

Selected for market coverage, product-philosophy diversity, and customer-level diversity:

1. **FreeBalance Accountability Suite™** — the pure-play PFM/GRP pole: national governments across 25+ countries; the vendor whose own definition of PFM software anchors the category ("integrated financial management system used by governments to manage the entire budget cycle… all ministries, departments and spending agencies of a government are connected to a single, unified system"). Six-pillar suite with deep module documentation. Also the specimen named by the public-budgeting-platform pass.
2. **Springbrook (Cirrus Finance Platform)** — the US small/mid-sized local-government ERP pole (2,800+ agencies claimed): cloud fund accounting suite with GL, AP, payroll/HR, budgeting, utility billing, property-tax collection, payments. Shows the Type at municipal scale under US fund-accounting machinery.
3. **Infor CloudSuite Public Sector** — the enterprise government-ERP pole (state, local, municipal, federal, tribal governments, utilities, K-12, special districts, transportation authorities; FedRAMP-authorized platform): finance + procurement + workforce in one ERP. Positioning-level evidence.
4. **Workday (Public Sector)** — the modern cloud ERP pole (state & local, US federal, special districts; financial management + HR): shows the Type realized by a cross-industry ERP vendor entering government. Positioning-level evidence.

Market anchors, unreachable and therefore used only for market structure (no product-specific claims drawn):

- **Tyler Technologies (Munis / Enterprise ERP)** — tylertech.com returned 403 in this pass and in the public-budgeting-platform pass; the largest US local-government ERP brand, market anchor only.
- **OpenGov** — opengov.com returned 403 in three prior passes (government-performance-management, government-transparency-portal, public-budgeting-platform); not retried; market anchor only.
- **SAP / Oracle public-sector editions** — sap.com public-sector URLs returned 404; enterprise-ERP pole evidenced via Infor/Workday instead.
- **Unit4** (public-sector ERP, UK/EU pole) — unit4.com 403. **CGI** — cgi.com URLs 404.

Domain authorities:

- **FreeBalance's own PFM definition** (vendor, but the cleanest reachable statement of the discipline and the budget cycle: formulation → execution → accounting/reporting → audit).
- **NASBO — Budget Processes in the States & Territories** (from the public-budgeting-platform pass): funds subject to appropriation, monitoring and control of expenditures, transfers of appropriated funds, use of "integrated financial management systems" by states.
- IMF / World Bank / OECD / GFOA PFM pages — all unreachable (403 or redirect) in this pass; discipline-level framing rests on the vendor definition and prior-pass domain sources.

## Sources

All fetched 2026-09-09:

- FreeBalance — Products (Accountability Suite overview): https://www.freebalance.com/en/products/
- FreeBalance — Public Financials Management (pillar page): https://www.freebalance.com/en/products/public-financials-management/
- FreeBalance — Public Expenditure Management (pillar page): https://www.freebalance.com/en/products/public-expenditure-management/
- FreeBalance — Government Treasury Management (pillar page): https://www.freebalance.com/en/products/government-treasury-management/
- Springbrook — home: https://springbrooksoftware.com/
- Springbrook — Cirrus Finance (fund accounting page): https://springbrooksoftware.com/solutions/finance/
- Infor — Public Sector (CloudSuite Public Sector): https://www.infor.com/industries/public-sector
- Workday — Public Sector: https://www.workday.com/en-us/industries/government.html

Prior-pass observations reused (recorded in earlier passes, cited here):

- public-budgeting-platform pass (2026-09-09): FreeBalance budget machinery (PFPF Core Public Financials, PFBC Budget Controls, PFBR Budget Transfer Requests, PFBM Budget Management; budgetary control, multi-level allotments, soft/hard commitments, real-time ledger); NASBO domain map.
- government-revenue-management pass (2026-09-09): seam note — PFM owns budget execution, expenditure, treasury-wide financials; revenue management feeds receipts in.
- government-grants-management pass (2026-09-07): seam note — PFM manages government-wide budgets/ledger; grants management runs the per-award lifecycle.
- nonprofit-fund-accounting pass (2026-09-08): adjacency note — government fund accounting shares the fund-ledger core under public-sector standards.

**Source-access limitation (load-bearing for assertion calibration):**

- No Tier-1 operational documentation (help center / user guide) was reachable for ANY sampled product in this pass. All evidence is Tier-2 official product pages (positioning + feature level). Workflow mechanics are therefore described at capability level, never step level.
- The US market-leader pole (Tyler Munis, OpenGov) and the enterprise ERP editions (SAP, Oracle, Unit4, CGI) were unreachable (403/404). Their existence and market role are market-structure anchors only.
- IMF, World Bank topic page, OECD, and GFOA were unreachable (403/redirect). The discipline-level framing rests on FreeBalance's published definition plus prior-pass domain sources (NASBO).
- No precise operational facts (allotment levels, commitment thresholds, fiscal-year defaults, approval-chain depths, report formats) are asserted anywhere; the sampled pages do not state them.

## Product Observations

### FreeBalance Accountability Suite™ [Evidence layer A — Tier 2 product pages, 4 pages]

**Suite overview (products page):**

- Positioning: "a commercial off-the-shelf, Government Resource Planning (GRP) solution that covers the entire budget cycle and manages all critical government fiscal systems." 40 years alongside the public sector; 25+ countries; six base configurations.
- Canonical definition (vendor's own "What is Public Financial Management (PFM) Software?"): "an integrated financial management system used by governments to manage the entire budget cycle. This includes **budget formulation, budget execution, accounting and reporting, and audit**. Typically, **all ministries, departments and spending agencies of a government are connected to a single, unified system**. PFM software is also known as GRP or government resource planning software."
- Six pillars, each with a one-line scope statement:
  - **Government Performance Management** — "Tying performance directly to budgeting."
  - **Public Financials Management** — "Commitment accounting and budget management are unique to the public sector, enabling budgetary and commitment controls. This includes budget and commitment accounting, assets and inventory."
  - **Public Expenditure Management** — "manages all functions related to government spending… exceeds typical accounts payable functionality and includes expenditures, purchasing, procurement, grants and social programs."
  - **Government Treasury Management** — "manage debt and investments… bank reconciliation and cash management."
  - **Government Receipts Management** — "Governments raise revenue and collect receipts through a number of means. This includes non-tax revenue, taxation, and billing and receipts."
  - **Civil Service Management** — "manage the civil service cycle from recruitment through retirement. This includes human resources and workforce, payroll, pensions, benefits, and self-service."
- Standards frame: UN, IMF, World Bank, IFRS, MCC. Platform: progressive activation, modular approach, centralized/decentralized/hybrid deployment.

**Public Financials Management pillar (PFM page):**

- Discipline definition: "Public Financial Management (PFM) covers the legal and regulatory framework, IT systems and processes used by governments to raise revenue, undertake public spending, account for funds and audit results."
- "Critical to this process is the need to have a **unified and integrated financial management information system** that provides for budget controls, appropriations, commitment accounting, and the Chart of Accounts."
- Serves "unitary governments, national governments, line ministries, sub-national and local governments, and projects."
- Modules: (PFPF) Core Public Financials — "budget controls, appropriations, commitment accounting and Chart of Accounts"; (PFBC) Budget Controls — "controls for budget, appropriations and commitments"; (PFBR) Budget Transfer Requests — "requesting budget transfers… workflow approvals"; (PFCB) Cash Books; (PFFA) Fixed Assets — "fixed asset accounting, depreciation, custody transactions and asset transfer management"; (PFFM) Fleet Management; (PFSI) Stores and Inventory; (PFSL) Sub-Ledger; (PFAA) Accountable Advances — "control of advance payments… automatic control over recuperating advances."
- Benefits: **Budgetary Control** — "Budgetary funds are mapped to the Chart of Accounts at a predetermined hierarchy level for aggregate fiscal control"; **Multi-Level Allotment Controls** — "appropriations, warrants or allocations, mapped to… the Chart of Accounts and to fiscal periods"; **Commitment and Obligation Control** — "a soft commitment to spend or hard commitments to contractual obligations"; **Real-Time Ledger** — "Balances ledgers in real-time to ensure budgets are not overspent"; **Reform and Modernization** — "migrating to accrual accounting."
- Chart-of-accounts framing (vendor blog teaser): "The Chart of Accounts (COA) or 'budget classification' is arguably the most critical part of effective PFM reform and IFMIS design. The COA for government is more complicated than in the private sector."

**Public Expenditure Management pillar (PEM page):**

- "manages all functions related to government spending and public expenditure control. Due to the unique needs of government – including budget and commitment controls – this exceeds typical accounts payable functionality common in the private sector."
- Modules: (PEPR) Purchasing and Expenditure — "the core government purchase and commitment cycle – requisitions, purchase orders, goods receipt, goods returned, expenses and payment vouchers"; (PEPM) Payment Management; (PECM) Contract Management; (PECT) Catalogue Management; (PEEP) eProcurement Site — "transparency on procurement process, suppliers, pricing and terms"; (PEGP) Electronic Government Procurement — "tendering, eProcurement, contract and spend management."
- Benefits: **Budget and Commitment Controls** — "Ensure that all expenditures are approved and do not exceed budget or allocations established in the system"; purchasing instruments (local purchase orders, petty cash, open contracts, standing offers, special contracts); vendor management (authorizations, certifications, ratings); **Social Benefits** — "government healthcare programs, pensions, welfare payments and employment insurance"; **Grant Management** — "grants, loans and contributions to individuals, educational institutions, NGOs and businesses"; **Intergovernmental Transfers** — "transfer payments between governments."

**Government Treasury Management pillar (GTM page):**

- "supports bank reconciliation and manages cash, debt and investments… harmonizes treasury operations across all levels of government, mitigates fiscal risk and maximizes government funds through effective forecasting."
- Modules: (GTBR) Bank Reconciliation — "automatic multi-currency bank reconciliation"; (GTBT) Bank Account Transfers; (GTDM) Debt Management — "models and plans for short-term and long-term debt instruments"; (GTLN) Loans Management; (GTCM) Cash Management — "forecasting of cash availability… based on the commitment cycle"; (GTIM) Investment Management; (GTLM) Liquidity Management.
- Benefits: **Treasury Single Account** — "Migrates bank accounts to a single account to effectively manage reserves, investments and debt"; cash and liquidity management predicting cash-flow requirements; debt management of "all government debt commitments."

### Springbrook (Cirrus Finance Platform) [Evidence layer A — Tier 2 product pages]

- Positioning: "the cloud finance and ERP Software thousands of local governments rely on"; "Enterprise class Finance Platform software for local government agencies"; 2,800+ small and mid-sized agencies (vendor claim, not asserted); 35 years serving government; customers include townships, cities, water districts, tribes.
- Finance page: "cloud-based **fund accounting** software for government — a fully integrated finance suite with **general ledger, accounts payable automation and AI invoice matching**."
- "Under the hood" module list: General Ledger; Accounts Payable; Automated Clearing House; Inventory Control; Fixed Assets; Project Management; Advanced Reporting Tools; **Bank & Fund Reconciliation**; Payment solution integration; Advanced Budgeting.
- Control posture: "Internal control and audit trails to track and protect your valuable data"; "Real time data access for stakeholders."
- Suite scope (home page): Finance, Payroll/HR, Budgeting (Advanced Budgeting), Utility Billing, Property Tax Collection (tax management, treasurer tax collection, CAMA, auditor), Payments, Reporting & Analytics, Asset Management, Permitting & Land Management, Meeting Management.
- Fund-accounting quote from a customer (accountant, PA township): "Cirrus powerful **fund accounting** capabilities designed to standardize financial data, reduce reliance on manual data entry, and expedite everyday financial processes."

### Infor CloudSuite Public Sector [Evidence layer A — Tier 2 positioning page]

- Positioning: "Public sector software to modernize government operations… Infor CloudSuite Public Sector, available on a **FedRAMP-authorized platform**. Industry-specific solutions and AI agents that work across **finance, procurement, and human resources**."
- Audience: "Hundreds of public organizations – including state, local, municipal, federal, and tribal governments, as well as utilities, K-12 education, special districts, and transportation authorities."
- Public sector ERP: "Access all financial, procurement, and workforce data in one cloud-based ERP solution… Streamline government processes… maintain full visibility and control with built-in governance." "Maintain compliance with built-in controls and transparent, auditable decisions."
- Benefits framing: "Smarter regulatory compliance — automated rules and controls ensure regulatory compliance"; "Stronger financial oversight — Integrated reporting, automation, and real-time insights improve accuracy and transparency for better financial control."
- Customer stories: City of Greensboro "completes year-end close in 3 days"; State of Idaho centralized on "Infor CloudSuite Public Sector in AWS GovCloud"; Elsinore Valley MWD "modernize financial operations and strengthen audit readiness."
- Sub-industry pages: state and local government ("manage your workforce, finances, and procurement"), federal government, tribal and sovereign nations ("financial accounting, community services, and regulatory compliance"), utilities, special districts, transportation authorities, K-12 ("HR, payroll, budgeting, and school operations… state and federal funding rules"), public safety.

### Workday (Public Sector) [Evidence layer A — Tier 2 positioning page]

- Positioning: "Public Sector Software & Solutions — Better serve your citizens with **next-generation ERP**. Promote financial stewardship, engage a diverse workforce…"
- "ERP purpose-built for the public sector" across three sub-industries: **State and local** ("Optimize your workforce, operate more strategically"), **U.S. federal** ("next-generation ERP that drives a mission-ready workforce"), **Special districts** ("Simplify HR and finance").
- Product spine: Financial Management, Spend Management, Payroll, Planning (Adaptive Planning), HCM — the cross-industry ERP suite sold into government; "Workday Government Cloud" named as the industry product.
- Market anchor: "A Leader in ERP for US Local Government" (Gartner Magic Quadrant claim — vendor-cited, not asserted).
- Customers shown: State of Oklahoma, City of Arlington, City of Olympia, State of Vermont, Metropolitan Washington Airports Authority, LADWP, U.S. Department of Energy.

### Prior-pass observations reused

- **public-budgeting-platform pass (FreeBalance budget machinery):** (PFPF) Core Public Financials — "budget controls, appropriations management, commitment accounting, and a robust Chart of Accounts… double-entry bookkeeping, real-time ledger updates"; (PFBC) Budget Controls — "multiple aggregate budget controls… equal and unequal allotments… soft and hard commitments/obligations… de-commitment and de-obligation functions. Providing real-time 'free balance' status"; (PFBR) Budget Transfer Requests; (PFBM) Budget Management — "budget appropriations, streamline budget transfers… budget amendments… budget control update vouchers… mid-term reviews." Suite context: six pillars; budgeting machinery is one pillar of the whole fiscal architecture.
- **government-revenue-management pass:** "PFM owns budget execution, expenditure, treasury-wide financials; budgeting owns revenue estimation. This Type [revenue management] feeds receipts in (deposits, GL export) and consumes levy/fee authority."
- **government-grants-management pass:** "PFM manages government-wide budgets/ledger; grants management runs the per-award lifecycle and hands financial postings to it."
- **nonprofit-fund-accounting pass:** "Government fund accounting (GASB) is the closest external discipline — same fund structure, different regulatory frame and users (public agencies). MIP and Denali serve municipalities explicitly, showing the machinery is shared."
- **NASBO (domain):** funds subject to appropriation; balanced budget requirements, debt limits; "monitor and control expenditures, transfer appropriated funds"; states' "use of integrated financial management systems."

## Cross-product Comparison

| Dimension | FreeBalance (PFM/GRP pole) | Springbrook (US local ERP pole) | Infor CloudSuite Public Sector | Workday Public Sector |
|---|---|---|---|---|
| Center | whole-of-government fiscal architecture (six pillars) | municipal finance suite (fund accounting core) | government ERP (finance + procurement + workforce) | cross-industry ERP sold into government (finance + HR) |
| Unit of record | unified government ledger over Chart of Accounts / budget classification | fund accounting general ledger | "all financial… data in one cloud-based ERP" | financial management over the government's accounts |
| Fiscal framework | COA mapped to funds at hierarchy levels; fiscal periods; appropriations/warrants/allotments | funds (bank & fund reconciliation; fund accounting) | not detailed (positioning level) | not detailed (positioning level) |
| Budget execution control | explicit: appropriations, allotments, soft/hard commitments, real-time free balance, "budgets are not overspent" | Advanced Budgeting module; budget checking depth not stated on fetched pages | "built-in controls"; not detailed | not detailed |
| Expenditure operations | full purchase-and-commitment cycle (requisitions → POs → receipt → payment vouchers); procurement; contracts; grants; social benefits; intergovernmental transfers | accounts payable, ACH, AI invoice matching, payment solution | procurement in-ERP | spend management |
| Receipts | Government Receipts Management pillar (non-tax revenue, taxation, billing and receipts) | utility billing, property-tax collection, payments | not detailed | not detailed |
| Treasury | Government Treasury Management pillar (cash, bank reconciliation, TSA, debt, investments) | bank & fund reconciliation | not detailed | not detailed |
| Payroll / civil service | Civil Service Management pillar (recruitment → retirement, payroll, pensions, benefits) | Payroll/HR module | HCM pillar | HCM + payroll |
| Assets & projects | fixed assets, fleet, stores/inventory, projects & job costing, accountable advances | fixed assets, inventory control, project management | asset management (via operations line) | not detailed |
| Reporting | real-time ledger, dashboards, standards (UN/IMF/World Bank/IFRS/MCC) | advanced reporting tools, Tableau bundling, audit trails | "integrated reporting… better financial control"; year-end close story | analytics & reporting |
| Regional machinery | international PFM reform (COA design, PEFA, progressive activation, accrual migration, TSA) | US local-government machinery (fund accounting, utility billing, property tax) | US federal (FedRAMP/AWS GovCloud) + state/local | US federal + state/local (Government Cloud) |
| Product form | pure-play PFM/GRP suite, six base configurations | small/mid-market government ERP suite | enterprise government ERP suite | cross-industry cloud ERP, government edition |

Stable across the sampled products (cross-product commonality, evidence layer B):

1. **One unified financial system of record for the government** — a single integrated ledger (FreeBalance states it explicitly: "all ministries, departments and spending agencies… connected to a single, unified system"; Springbrook: "a fully integrated finance suite"; Infor: "all financial… data in one cloud-based ERP").
2. **The government's own fiscal framework organizes the record** — chart of accounts / budget classification, funds, organizational units, fiscal periods (FreeBalance explicit; Springbrook fund accounting; NASBO funds-subject-to-appropriation).
3. **Budget execution control is the public-sector-specific machinery** — spending checked against budget authority in-system (FreeBalance: appropriations/allotments/commitments, real-time free balance, "ensure budgets are not overspent"; NASBO: "monitor and control expenditures"; the discipline's own definition includes budget execution). Depth at the US local pole not directly evidenced on fetched pages — held common-mature, not asserted per-product.
4. **The expenditure cycle runs through the system** — purchasing/commitment → payment, producing the accounting record as it goes (FreeBalance PEPR cycle; Springbrook AP/ACH; Infor procurement-in-ERP).
5. **Money-in, treasury, payroll, and assets appear as standard companions** — receipts (FreeBalance pillar; Springbrook utility billing/tax), treasury/cash (FreeBalance pillar; Springbrook bank & fund reconciliation), payroll/HR (FreeBalance pillar; Springbrook module; Infor/Workday HCM), fixed assets/inventory (all).
6. **Statutory reporting and audit posture** — financial statements, audit trails, internal controls (FreeBalance real-time ledger + standards; Springbrook audit trails; Infor "auditable decisions"; Infor customer story: year-end close).
7. **Public-accountability framing** — transparency portals, dashboards, open data as outputs (FreeBalance transparency-portals solution; Infor "increase transparency").

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The government's unified financial system of record.** One integrated system holding the government's financial records — a ledger organized in the government's own fiscal framework: its chart of accounts / budget classification, its funds, its organizational units (ministries, departments, agencies), and its fiscal periods — serving the whole government rather than a single department. Remove → departmental accounting tools or a fund-accounting package serving one entity's books without the whole-of-government frame.
2. **Budget execution control over public money.** The adopted budget is loaded into the system as spending authority (appropriations, allotments/warrants) and spending is controlled against it in-system: commitments/obligations are checked against real-time budget availability before money is committed or paid, so expenditure cannot legally exceed the budget. Remove → an accounting system that records spending after the fact (no control), or a budgeting platform that plans the budget but does not execute it.
3. **The government's money operations executed in the system.** The spending cycle (commitment → purchase → payment) runs through the system and posts to the ledger as it goes; money-in (receipts) and cash/debt (treasury) are the standard companions, making the system the operational pipeline of public money, not merely a record of it. Remove → a control/monitoring layer over someone else's transactions, or a payment processor with no fiscal frame.

Joint-hold test: (1) alone = government fund accounting / GL; (2) without (1) = a budget-control module over foreign records; (3) without (1)+(2) = private-style AP/payments; (1)+(2) without (3) = a control ledger with no operations; (1)+(3) without (2) = a government ERP without the public-sector control model; (2)+(3) without (1) = transaction processing with no unified record.

Deliberately NOT in L0 (checked against cross-product variance and the historical sample):

- **Budget formulation** — the discipline's cycle includes formulation, and suites sell it, but the market realizes formulation both in-suite and in dedicated budgeting platforms integrated at the seam (the public-budgeting-platform pass documents the dedicated pole). Formulation is common-mature, not definitional.
- **Receipts and treasury as named pillars** — present in every sampled product in some form, but their depth varies (a small municipality's bank reconciliation vs a national treasury single account); the invariant is that money-in and cash are operated in the system, their depth is variant.
- **Payroll/civil service** — a pillar at the national pole, a module at the local pole, absent from finance-only deployments; packaging variable.
- **Fund accounting as the accounting basis** — the US local realization; international poles organize by COA/budget classification with cash-to-accrual migration. The invariant is "the government's fiscal framework," not any specific accounting basis.
- **Specific accounting standards (GASB, IPSAS, IFRS)** — regional/regime machinery.
- **Single-vendor unification** — FreeBalance states the ideal-type ("single, unified system"), but federated deployments (ERP core + integrated revenue/budgeting products) satisfy the Type; the invariant is the unified record, not the single vendor.

### L1 — Common Mature Structure

- Chart-of-accounts / budget-classification administration as the organizing spine (named by the discipline's own literature as the critical PFM design element).
- Commitment/obligation machinery: soft and hard commitments, de-commitment/de-obligation, real-time "free balance" / budget availability.
- Budget transfers and amendments as workflowed, auditable in-year changes.
- Accounts payable / payment management (vouchers, ACH-class payments, invoice processing).
- Purchasing/procurement cycle (requisitions, purchase orders, goods receipt/return) bound to commitment control.
- Receipts/receivables (non-tax revenue, billing) posting into the ledger.
- Bank reconciliation and cash management; debt and investment management at the treasury pole; treasury single account at the national pole.
- Payroll/HR (civil service cycle, pensions, benefits) as pillar or module.
- Fixed assets, inventory/stores, fleet; project/job costing for grants and capital work.
- Accountable advances (advance payments with recuperation control).
- Financial reporting to statutory/public-sector standards; audit trails and internal controls; year-end close.
- Budget preparation/formulation support (in-suite module or integration with a dedicated budgeting platform).
- Dashboards/analytics; transparency portals as publication outputs.
- Roles/permissions and workflow approvals throughout.

### L2 — Variant / Optional Structure

- **Level of government**: national/ministries (international IFMIS pole), state/provincial, county/municipal (US local pole), federal agencies, special districts and authorities, tribal/sovereign nations, public utilities.
- **Regional machinery**: international PFM reform (COA reform, PEFA assessment, donor frameworks, progressive activation, TSA migration, cash→accrual accounting migration) vs US local-government machinery (GASB fund accounting, encumbrance, ACFR-class reporting, GFOA programs) vs US federal appropriation vocabulary (PPBE-class).
- **Accounting basis**: cash, modified cash/modified accrual, full accrual — often a migration path driven by reform programs.
- **Deployment**: on-premises, private/public/community cloud, shared services; FedRAMP-class authorization for US federal; progressive activation for sequenced reform programs.
- **Product form**: pure-play PFM/GRP suite vs government ERP (finance+HR+procurement) vs cross-industry ERP government edition vs small-municipality fund-accounting suite.
- **Scope breadth**: finance-only vs finance+payroll+procurement+revenue+assets+permitting/meeting management (the small-municipality suite pole bundles adjacent government operations).
- **Donor/project-funded operations**: development-country poles carry donor funds, grants, and contribution management prominently.

### L3 — Vendor-specific Structure (Research Notes only)

- FreeBalance: Accountability Suite™/Platform™ naming; six pillars; module codes (PFPF, PFBC, PFBR, PFCB, PFFA, PFFM, PFSI, PFSL, PFAA; PEM: PECM, PECT, PEEP, PEPM, PEGP, PEPR; GTM: GTBR, GTBT, GTDM, GTLN, GTCM, GTIM, GTLM); six base configurations; progressive activation; PEFA results page; "25+ countries," "$425 billion in budget dollars," "40 years" claims (not asserted).
- Springbrook: Cirrus platform naming; KVS/SoftRight and SB Express (formerly BIAS) legacy platforms; Xpress Bill Pay; Tableau bundling; AI invoice matching; "2,800+ agencies" claim (not asserted).
- Infor: CloudSuite Public Sector; FedRAMP-authorized AWS GovCloud; Industry AI agents; Operations & Regulations (permitting/GIS) line; Talent Science; Velocity Suite.
- Workday: Workday Government Cloud; Gartner MQ "Leader in ERP for US Local Government" claim (vendor-cited); Adaptive Planning.
- Tyler (Munis), OpenGov, SAP PSM-class, Oracle, Unit4, CGI: unreachable; market anchors only.

### Historical / market-sample check

The paper-era treasury/finance ministry — ledger books over the government's chart of accounts and funds, appropriation ledgers, warrant and encumbrance registers, payment vouchers and check registers, receipt ledgers and cash books, annual financial statements rendered to the legislature — satisfies all three L0 structures with no software: unified books over the fiscal framework (1), spending controlled against appropriation authority before payment (2), and the money operations executed through the treasury's own machinery (3). The 1980s–2000s generations also fit: US municipal fund-accounting packages (fund GL + appropriations/encumbrance + AP/payroll/receipts) and early national IFMIS implementations (unified ledger + budget controls across ministries). The definition names no cloud, SaaS, AI, specific standard, or accounting basis. Check passes; the definition is not overfitted to the current cloud-ERP generation.

## Vendor-specific Findings

- FreeBalance is the only sampled vendor that publishes an explicit definition of the Type and the discipline; its six-pillar split (performance / financials / expenditure / treasury / receipts / civil service) is one vendor's articulation of the fiscal architecture. Springbrook's module split (finance / payroll / budgeting / utility billing / tax / payments / assets / permitting / meetings) is the US municipal articulation. The content classes recur (ledger, budget control, expenditure, receipts, treasury, payroll, assets, reporting); the module names do not.
- The US market-leader pole (Tyler Munis, OpenGov) could not be directly researched (403 across passes). The final document describes the US local-government realization generically (fund accounting, appropriations/encumbrance machinery) without product-specific claims.
- Infor and Workday evidence is positioning-level only; no fiscal-machinery detail was asserted from their pages.

## Boundary Findings

1. **vs Public Budgeting Platform (§24, processed) — pre-hung flag DISCHARGED, keep-both RATIFIED.** The seam holds exactly as the budgeting pass framed it: the budgeting platform centers the **budget cycle** (multi-participant formulation → review → adoption → publication; its unit of record is the fiscal-period budget as a whole); the PFM system centers the **whole fiscal architecture** (unified ledger + execution control + money operations; its unit of record is the government's financial record over the fiscal framework). The overlap zone is budget execution controls (appropriations/commitments) — FreeBalance demonstrates budget machinery as one pillar of the PFM suite, and budgeting suites integrate with ERP/GL for execution. Removal tests: strip the ledger, execution control, and money operations from a PFM suite → a budgeting platform; strip the formulation/publication cycle from a budgeting platform → it does not become a PFM system (no ledger, no operations). A PFM system without in-suite formulation (using an external budgeting platform) is still fully in-type; a budgeting platform with ERP integration for execution is still budgeting. No alias/duplicate.
2. **vs Accounting Software / General Ledger System (§08).** Government fund accounting shares the ledger engine (the nonprofit-fund-accounting pass recorded the same adjacency from the nonprofit side). The discriminators: PFM adds budget execution control (appropriations/commitments as first-class structures), the whole-of-government span, and the operated money flows (treasury, receipts, expenditure at government scale). One-way specialization: add the government fiscal framework + execution control + operations → PFM; remove them → accounting/GL. Keep-both.
3. **vs Enterprise Resource Planning / ERP (§10).** GRP is the government analog of ERP; several sampled products self-label "ERP" (Infor, Workday, Springbrook). The discriminator is the object and control model: ERP plans and records a company's resources around profit-oriented operations; PFM controls public money against legal spending authority (appropriations/commitments) and renders accounts to the public/legislature. Government-ERP products are this Type realized in ERP form, not members of the corporate ERP Type. The directory's ERP leaf should be read as the private-sector Type; cross-reference recommended when that leaf is processed.
4. **vs Government Revenue Management (§24, processed).** Confirms that pass's seam: revenue management operationalizes money-in (levying, billing, collecting, delinquency) for specific revenue classes; PFM holds receipts as one pillar and consumes the collections into the unified ledger (deposits, GL export). Interlock, not overlap.
5. **vs Tax Administration System (§24).** Tax administration centers the tax-law relationship (registration, filing, assessment, audit, enforcement); PFM consumes tax receipts as money-in. FreeBalance's receipts pillar names "taxation" as one receipt class — collection machinery depth belongs to the tax Type.
6. **vs Government Procurement Platform (§24, processed).** The procurement cycle (sourcing, tendering, contract award) is that Type's center; PFM holds purchasing/procurement as an expenditure pillar bound to commitment control (FreeBalance PEM includes eProcurement modules). Module-vs-whole-product seam, same shape as the CIP/budgeting seam: a procurement platform without the fiscal frame is still procurement; a PFM suite with procurement modules is still PFM.
7. **vs Treasury Management System (§08, corporate).** Same machinery family (cash, debt, investments, reconciliation), different subject and frame: corporate treasury manages a company's liquidity for commercial ends; government treasury operates public cash/debt under fiscal-authority constraints (TSA, appropriation-linked cash forecasting — FreeBalance's cash forecasting is "based on the commitment cycle"). Government treasury is a pillar of this Type, not the corporate Type.
8. **vs Government Grants Management (§24, processed).** Confirms that pass's seam: grants management runs the per-award lifecycle (program → application → award → disbursement → reporting); PFM holds grants as expenditure programs and donor receipts posting to the ledger. Interlock.
9. **vs Payroll System / HR (§09).** Civil service management (recruitment → retirement, payroll, pensions) is a pillar/module of PFM suites at some poles and absent at others; the standalone payroll Type serves any employer. Suite packaging, not identity.
10. **vs Government Performance Management (§24, processed) / Government Transparency Portal (§24, processed).** Performance linkage ("tying performance directly to budgeting") and transparency publication are pillars/outputs beside the fiscal core — consistent with both passes' findings that these recur as modules inside neighboring Types. Interlock.
11. **vs Public Benefits Management / Social Services (§24).** Social-benefit payments (pensions, welfare, employment insurance) appear as expenditure programs inside PFM (FreeBalance PEM social benefits); the benefits Types center the program/recipient relationship and eligibility machinery. Payment rail vs program machinery.

## Uncertainties

- No Tier-1 operational documentation was reachable for any sampled product; all workflow mechanics are capability-level. Exact control-check sequences (commitment vs payment-time checking), allotment-release mechanics, period-close procedures, and report formats are NOT asserted.
- The US local-government pole's budget-checking depth (encumbrance at transaction entry) is inferred from the fund-accounting frame and market structure, not directly evidenced on the fetched Springbrook pages — held common-mature, not asserted per-product.
- The US market-leader pole (Tyler Munis, OpenGov) and enterprise ERP editions (SAP, Oracle, Unit4, CGI) unverified (403/404); their feature realizations are market-structure anchors only.
- IMF / World Bank / OECD / GFOA domain pages unreachable (403/redirect); the discipline-level framing rests on FreeBalance's published definition plus prior-pass domain sources (NASBO). The canonical framing (budget cycle: formulation → execution → accounting/reporting → audit) is vendor-sourced and should be re-anchored if a domain source becomes reachable.
- Whether every PFM deployment includes receipts and treasury in-system (vs integrated external products) is unverified at the product level; held as common companions, not asserted as universal.
- Non-US, non-international-vendor regimes (e.g., EU national treasuries running SAP-class systems) were not directly sampled; the international realization is evidenced by one vendor.

## Final Synthesis

The Public Financial Management System is the government's whole-of-finance system of record — the software realization of what the discipline calls PFM and the market variously labels IFMIS, GRP, or government ERP. Its defining structure is threefold and jointly-held: (1) the government's unified financial system of record — one integrated ledger organized in the government's own fiscal framework (chart of accounts / budget classification, funds, organizational units, fiscal periods) serving the whole government; (2) budget execution control — the adopted budget loaded as spending authority (appropriations, allotments) with commitments and payments checked in-system against real-time budget availability, the machinery the discipline itself names as unique to the public sector; and (3) the government's money operations executed in the system — the expenditure cycle from commitment through payment posting to the ledger, with receipts (money-in) and treasury (cash, debt, investments) as the standard companions. Around this core, mature products add the purchasing/procurement cycle, payroll/civil service, fixed assets and inventory, project/grant costing, accountable advances, budget transfers and amendments, statutory financial reporting with audit trails, budget-formulation support or integration, dashboards, and transparency publication. The Type is distinct from the Public Budgeting Platform by its center (the whole fiscal architecture vs the budget cycle — the ratified seam), from accounting/GL by its control model and government span, from corporate ERP by its object (public money under appropriation authority), from revenue management and tax administration by its direction (the fiscal architecture that receives money-in vs the machinery that collects it), and from corporate treasury by its subject. The paper-era treasury — appropriation ledgers, warrant registers, payment vouchers, receipt ledgers, cash books, annual statements to the legislature — satisfies all three legs with no software, confirming the definition is not overfitted to the current cloud generation.
