# Research Notes — Royalty Management Platform

Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (update-v1)
Slug: royalty-management-platform (DIRECTORY.md §27 Media, Entertainment, Creator & Culture)

---

## Research Goal

Understand what a Royalty Management Platform actually is as an Application Type: what system of record it maintains, who operates it, what its core computational loop is, and where its boundaries sit against the heavily adjacent music/publishing/media siblings already processed in §27 (record-label-management, music-publishing-management, performing-rights-management, media-rights-management, music-distribution-platform, book-publishing-management, author-management-platform).

## Initial Boundary (hypothesis before research)

- Hypothesis: a royalty management platform is the system that computes and settles contractual royalty obligations — it holds agreements as computable money terms, ingests sales/usage from outside, calculates per contract per period, and produces statements and payments.
- Likely confusions:
  - Record Label Management / Music Publishing Management (same money loop, different subject)
  - Performing Rights Management (society-side collective distribution)
  - Media Rights Management (rights grants vs royalty money)
  - Music Distribution Platform (earnings pass-back vs contractual computation)
  - Author Management Platform (flagged joint review from that pass)
  - Accounting software / ERP royalty modules
  - Franchise management systems (royalty collection as a module)
- Direction-of-money question: does the Type cover only "we owe royalties out" (publisher→author, label→artist) or also "royalties owed to us" (licensor←licensee, franchisor←franchisee)?

## Research Questions

1. What is the unit of record — contract, payee account, product, or period?
2. What exactly does the calculation consume (sales files? usage reports? licensee statements?) and how does matching work?
3. What money-term machinery is definitional vs optional (rates, splits, escalators, advances, recoupment, reserves, cross-collateralization, minimum guarantees, deductions)?
4. What is the settlement loop's shape (periods, balances, statements, payments, locking)?
5. Is the money direction (payable out vs receivable in) part of the Type or a variant?
6. Is the Type industry-specific or industry-agnostic? Which industries realize it?
7. Where do music-specialized royalty-only systems (Curve-class) sit — this Type or the label-tool family (delegated decision from record-label-management pass)?
8. Where do licensor-side licensing platforms (FADEL-class) sit — this Type or a licensing-lifecycle Type?
9. What are the interfaces (back office, recipient portal, analytics)?
10. What are the important rules (period locking, matching failures, reserves, audit trail)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers + different industries + different money directions:

| Product | Vendor | Industry focus | Direction | Tier | Philosophy |
|---|---|---|---|---|---|
| Royalty Tracker® | MetaComet Systems | book publishing first, generalized (biotech, tech transfer, franchise, games, entertainment) | payable (out) | mid-market | royalty-only specialist, ERP-integrated |
| Curve | Curve Royalty Systems | music (labels + publishers, dual-side) | payable (out) | indie labels to majors' departments | royalty-only specialist, music-native, managed-service option |
| Reprtoir | Reprtoir | music (labels + publishers), generalizing to video/MCN | both (money-in and money-out contracts) | SMB/mid | all-in-one workspace suite with royalty accounting module |
| IPM Suite / LicenSee | FADEL | brand licensing, consumer goods, publishing | both (licensor receivable + licensee payable) | enterprise | licensing-lifecycle platform with royalty engine |
| EasyRoyaltiesPlus (+ROL Portal) | Book Matters LLC (RIGHTS 20/20) | book publishing (independent publishers) | payable (out) | small/SMB | self-hostable royalty accounting, modular rights add-ons |

## Sources

All fetched 2026-09-09 unless noted.

- MetaComet — homepage (https://metacomet.com/), Royalty Tracker product page (https://metacomet.com/solutions/royalty-tracking-software/), "Royalty Calculation and the Royalty Management Lifecycle™" (https://metacomet.com/resources/royalty-calculation-lifecycle/)
- Curve — homepage (https://www.curveroyaltysystems.com/), Knowledge Base (https://help.curveroyaltysystems.com/), Artist Contracts category (https://help.curveroyaltysystems.com/category/43-contracts), "Adding Sales Terms to Your Contracts" (https://help.curveroyaltysystems.com/article/47-adding-sales-terms-to-your-contracts)
- Reprtoir — homepage (https://www.reprtoir.com/), Royalty Accounting page (https://www.reprtoir.com/royalty-accounting), Documentation (https://docs.reprtoir.com/), "About Royalty Accounting" (https://docs.reprtoir.com/docs/about-royalty-accounting.md), "Processing a Royalty Statement" (https://docs.reprtoir.com/docs/processing-a-royalty-statement.md)
- FADEL — homepage (https://fadel.com/), IPM Suite page (https://fadel.com/ipm-suite/)
- Book Matters — EasyRoyaltiesPlus/That's Rights! page (https://www.easyroyalties.com/ → bookmatters.us)

Sibling research notes consulted for pre-drawn seams (no re-fetch needed):
- research/record-label-management.md (Boundary Findings; delegated Curve-class placement decision)
- research/music-publishing-management.md (Boundary Findings; works/entitlement wall)
- research/media-rights-management.md (joint-review request vs this leaf)
- research/author-management-platform.md (joint-review request vs this leaf)
- research/performing-rights-management.md (generic-vs-society seam)
- research/music-distribution-platform.md (supply-chain statements vs contractual computation)

Source-access limitations:
- FADEL operational documentation (support.fadel.com) is login-gated; FADEL evidence is product pages + case studies + FAQ (Tier 2), so FADEL-specific workflow detail is held at moderate strength.
- MetaComet's detailed help center was not sampled beyond the lifecycle article; MetaComet workflow claims rest on product pages + the lifecycle article (Tier 1/2 mix).
- Enterprise publishing royalty systems (Klopotek-class) and franchise-management royalty modules were not directly documented this pass; those variants are held at lineage strength.
- Reprtoir's statement-provider count varies across its own pages (120+ / 180+ / "more than 70 sources") — marketing variance; no precise count promoted.

---

## Product A — MetaComet Systems (Royalty Tracker®)

### Key observations (Layer A unless noted)

- Self-label: "Royalty Management Software: Tracking & Reporting"; "Make Rights & Royalties Easy with MetaComet's Rights & Royalty Management Software". Positioning: "purpose-built for rights and royalties — not adapted from generic accounting or ERP software."
- Own definition of the category (homepage FAQ): "Royalty management software is a critical tool for finance teams that license intellectual property." / "Royalty software drives efficiency in any industry where businesses license intellectual property... If your business pays royalties, MetaComet was built for you."
- Own explanation of how it works: "Royalty software processes large amounts of sales and contract data to generate accurate statements, reports, and payment files... It allows users to record or import contract terms or royalty rules and receive sales reports in all formats and currencies. It then calculates royalty payments instantly, so users can generate statements, reports, and payment files with the click of a button."
- Product suite: Royalty Tracker® (calculation core), Sales Aggregator (sales ingestion), Royalty Portal (recipient self-service), MetaComet® Rights (licensing/rights module), free implementation service.
- The "magic button" workflow (product page): "Set up your contract terms, enter the personal information for each royalty recipient, upload your sales data, then push literally one button and Royalty Tracker will handle everything automatically" → "Calculate all royalty payouts. Generate professional royalty statements. Send the statement to each recipient and post it to your company's secure Royalty Portal."
- Contract machinery: "Handle an unlimited number of different contracts"; "Support sales-based royalties, patent licenses, milestone payments, revenue-share agreements, franchise fees, and more"; "Handle even the most sophisticated rules, including cross collateralization, kit explosion, minimum guarantees, etc."; FAQ: different rates by format/channel/territory within a single contract; escalators, tiers, split royalties as "core contract logic"; co-author/agent/contributor splits defined in contract setup; kit explosion for bundles/subscriptions; multi-currency sales and payouts; payout schedules (quarterly, semiannual).
- Reports: Sales Reconciliation Report ("every sales transaction and royalty calculation by product or recipient"), Adjustments Reconciliation Report, Statement Balances Report ("rolls up everything... for easy management, accounting, and accrual reporting"). Forecasting from sales history + contract terms at company/business-unit/agreement/title level.
- Scale claim: "processes sales across companies with over 40,000 products, patents, titles, or SKUs, and millions of sales transactions" (marketing-scale claim, single-source).
- Integration: "Virtually any ERP or Accounting System" (Oracle, NetSuite, SAP, Great Plains, MS Dynamics, QuickBooks); product databases (Firebrand Title Management), fulfillment systems, BI suites. Payment files "directly uploaded to the user's accounting and/or payment software."
- Industries: book publishing, biotechnology/life sciences, pharmaceuticals, medical device, technology transfer, online learning, video games, entertainment, consumer product licensing.
- Royalty Management Lifecycle™ (vendor's own process model, 4 phases):
  1. **Acquisition** — sign agreement with author/inventor/recipient; create, share, revise, execute, store, record contract details; onboard the recipient.
  2. **Sales** — product released; "Combining multiple sales files into a single sales database. Mapping sale types (e.g., foreign, domestic, paperback, and ebooks) from sales reports to those described in your contract terms. Converting multiple foreign currencies."
  3. **Royalty Calculation & Reporting** — "the company figures out what it owes to its recipients... generate royalty statements, month-end reports, advance roll-forwards, outstanding reserves, and other necessary records."
  4. **Royalty Distribution** — "the company shares royalty statements and payments with its recipients."
- Calculation factors (publishing example, educational content): list price by format, sales by format, retail vs net royalty basis, rate + escalator triggers, discounts, returns, reserves, advance earn-out.
- Audit rationale: "business partners, investors, tax agencies, and your royalty recipients all need to see proof of accurate, honest, and legal financial calculations and record-keeping."
- Data access claims: "product level accruals, net payables, unearned advances."
- Marketing metrics ("cut royalty management time by 90%") — vendor claim, not promoted.

## Product B — Curve Royalty Systems

### Key observations (Layer A)

- Self-label: "Music Royalty Software"; "Curve is a Complete Royalty System for Record Labels and Music Publishers"; "Complicated deal terms, contract rate escalations, black box revenue distribution and more - for music publishing & masters."
- Dual-side packaging: separate product lines and pricing for Publishing Royalties and Recording Royalties; "Manage your mechanical royalty accounting to publishers" (label→publisher mirror flow).
- Core loop in vendor's words: "From ingestion of sales data, through calculation on contract terms, to providing clear and readable Statements, Reports and Analytics."
- Scale/performance claim: "ingesting millions of lines of data & producing statements in minutes & hours versus days & weeks."
- Contract database flexibility: "The contract database can be configured to match your royalty reporting needs. You decide which channels, formats, price tiers, territories etc. to target & make available in your contract terms. You can break out any income stream or cost & set specific rates."
- Knowledge-base structure (Tier 1) — the object world:
  - Labels side: Getting Started, Settings, **Payees**, **Artist Contracts**, **Catalogue**, **Sales**, Sales Templates, **Costs**, **Period & Artist Statements**, **Mechanicals**, Reports & Data
  - Publishers side: Getting Started, Settings, **Payees**, **Writer Contracts**, **Catalogue**, **Deliveries**, **Income**, Income Templates, **Period & Writer Statements**, Reports & Data
  - **Payments** (separate collection: getting started, requirements & coverage) — Curve operates actual outbound payments (payment services via a regulated e-money institution per footer)
  - Curve For Creators — artist-facing dashboard ("grant your artists access to retrieve their statements, data & analytics"; "no longer stuck emailing 100-page PDFs")
- Sales-term structure ("Adding Sales Terms to Your Contracts", Tier 1): a term is an if/then rule —
  - IF variables: catalogue type (track vs release), catalogue group, territory (with territory groups), channel (defaults Digital/Physical/Licensing), configuration (defaults Premium Stream, Ad-Funded Stream, Download, CD, LP), price category (Full/Mid/Budget), source (free text).
  - THEN variables: deal type (Gross Receipts, Net Receipts, PPD [published price to dealer], Unit Price, Retail Price, Sale Price, Unit Rate, Fixed Unit Rate), Rate % ("the payee's share"), Multiplier, Reduction %, Reserve % ("typically used on physical products to protect against potential future returns", released on a schedule).
  - "You can add as many income terms to your Contracts as needed"; 0%-rate terms exclude revenue from statements; a documented hierarchy decides which term applies when several match.
  - Worked example: £10 gross → 50% rate → ×1.3 multiplier → 75% reduction → 10% reserve = £4.875 payable + £0.4875 reserved.
- Artist Contracts category (Tier 1) — contract machinery: create contracts; sales terms; cost terms; deductions; escalations ("increase or decrease royalty rates"); reserves ("delay royalties"); advances/payments/adjustments as transactions; opening balances (migration); cross-contracts ("transfer or subtract artist royalties"); catalogue groups (different rates for different parts of catalogue); auto-matching contracts to catalogue; custom accounting period types; contract duration/end date; self-bill invoices; fees invoices for commission/distribution fee; auto-payments; custom statement design per company.
- Royalty vs profit-share deals distinction documented (help article title).
- Managed-service option: "Curve offers fully managed royalty services - our team handles processing, accounting, and reporting on your behalf."
- Acquisition: Jamen Capital and Merlin completed acquisition (Aug 2026) — market-consolidation signal, not structural.
- Client base: "800+ labels, publishers and rights holders" (marketing claim).

## Product C — Reprtoir

### Key observations (Layer A)

- Self-label: "The workspace for labels and publishers"; Royalty Accounting = "The supercharged all-in-one music industry royalty accounting solution"; "built for record labels and music publishers"; also: "Not only for record labels. If you are a movie or TV production firm, a video creation team, a YouTube MCN, or any entity that needs to... split royalties between rights holders."
- Suite packaging: Catalog Management, Music Sharing, Release Builder, Royalty Accounting as separate solution pages; royalty accounting is one module of a workspace.
- Own definition (docs, Tier 1): "'Royalty Accounting' is a specialized accounting practice used by Record Labels, Music Publishers, and Rights Administrators to manage, calculate, and distribute royalties generated by the exploitation of music rights. Unlike standard accounting, Royalty Accounting relies on contractual logic rather than simple invoices or sales records. It must account for advances, royalty splits, recoupments, cross-collateralization, deductions, escalations, minimum guarantees, and territory or usage specific rules."
- Positioning vs accounting: "It operates as a structured layer on top of general accounting, producing accurate royalty balances and statements while remaining compatible with standard financial bookkeeping." / "not a replacement for general accounting software."
- The canonical workflow (docs, Tier 1, quoted structure):
  1. "Revenues and Costs are recorded... always associated with Contracts. These Contracts define how money flows, how it is split between Rights-Holders, and how advances or costs are recouped over time."
  2. "Each financial movement generates internal Operations that reflect debit and credit entries. These Operations are the foundation of automated recoupments and cross-collateralization across multiple Contracts involving the same Rights-Holder."
  3. "At any time, the financial position of a Contract is visible through its Contract Balance."
  4. "When a reporting period ends, Contract Balances are closed. Their totals are transferred to the Rights-Holder Balance, and Contract Balances are reset to zero so that a new period can begin without affecting past results."
  5. "Statements are then generated from the Rights-Holder Balance. Once a Statement is issued and sent, the corresponding reporting period is permanently locked and made available to the Rights-Holder through their portal."
  6. "Payments can then be created to track the actual cash flow."
  7. "This workflow ensures full traceability from raw revenues to final payouts."
- Prerequisites (docs, Tier 1): assets in catalog with identifiers (UPC, ISRC, ISWC, provider-specific codes) — "Without these identifiers, reliable matching is not possible"; parties present (statement providers, clients, rights-holders as companies/contacts); contracts configured (Money In and Money Out); contracts linked to assets; organization currency set; optional opening balances for migration.
- Contracts: "Create incoming and outgoing contracts with royalty sharing percentages in net or gross amounts for digital, physical, licensing, mechanical, performance, sync, and direct revenues"; contract groups for cross-collateralization; recoupable/semi-recoupable/non-recoupable fees and advances; custom royalty periods, minimum payout, VAT rate per contract; opening balances; bulk-assign contracts to thousands of tracks/works; split adjustments per track and work.
- Statement ingestion pipeline (docs, Tier 1, "Processing a Royalty Statement"): add income (provider, template, contract money-in, payment date, currency, net/gross amounts) → upload file (CSV/TXT/TSV/XLSX/CRD — Common Royalty Distribution) → map columns to the standard data model → handle amount errors (totals discrepancy pauses processing) → handle data errors (missing asset → create with identifiers; missing royalty split → link contract; missing dates/classification; corrections generate reusable Rules; **quarantined errors do not block the workflow**) → review (totals, lines, quarantined) → confirm → **calculation** → final summary. "Processed data cannot be modified. If errors exist, the Income must be deleted or reprocessed." Reprocessing and Revert Accounting documented as separate capabilities.
- Matching prerequisite: "Royalty statements primarily reference assets using identifiers. If identifiers present in the statement do not exist in the catalog, lines cannot be matched and remain unprocessed."
- Statement providers: dozens of named providers — retailers (Spotify, Apple, Deezer, YouTube), distributors/aggregators (Believe, FUGA, Ingrooves, The Orchard, DistroKid, TuneCore), societies (BMI, GEMA, HFA, PRS, PPL, The MLC, SACEM), major labels (UMG, WMG). Count varies by page (120+/180+/70+) — marketing variance.
- Other incomes: sync (track/work), license (track/album/video/work), sale product, direct incomes.
- Outputs: "Generate royalty statement summaries and detailed breakdown spreadsheets by contracts"; "Send customized statements to your Rights-Holders by email in bulk"; "Record and track all payments to never forget to pay anyone"; real-time balances ("opening, overall, or closing balances for all Rights-Holders"); "Close balances manually or automatically by using automated rules based on custom sales periods."
- Rights-Holders Portal: "secure and private accounts (isolated from the Workspace), in which the Organization's Rights-Holders access their lists of Statements, Operations, and Payments, as well as Analytics."
- Multi-organization, 150+ currencies claim, error rules, sales analytics.

## Product D — FADEL (IPM Suite / LicenSee)

### Key observations (Layer A; operational docs login-gated — moderate strength)

- Self-label: "Leading Rights and Royalty Management Software"; IPM Suite = "Rights & Royalty Management for Midmarket to Enterprise Licensors, Licensees & Publishers"; LicenSee = "Royalty Operations for Small to Midmarket Licensees."
- Both money directions in one vendor:
  - **Licensors** (IPM Suite): "Manage outbound licensing of characters, brands, and products. Check conflicts, collisions, and compliance. Manage rights and royalties across licensees. Integrate with your ERP."
  - **Licensees** (IPM Suite/LicenSee): "Manage inbound licensing of content and product parts along with the associated payout of royalties. Automate royalty processing. Generate licensor-specific royalty reports. Manage audits and track violations."
  - Publishers: "manage rights and permissioning of content, calculate royalty payments & generate statements."
- Feature set (product page): Deal Management ("Negotiate deals, capture even the most complex agreement terms... complete audit trail"), Rights Management ("Structure rights hierarchies, advances, guarantees, payment schedules, and royalty rates... check for collisions and clearance"), **Royalty Management** ("Automate sales and usage processing, royalty calculation and validation, statement generation, minimum guarantee recoupment, and analytics"), Accounting Engine ("Integrate with your ERP's AP, AR, and General Ledger"), Product Approval, Forecasting ("View licensee business plans, align budgets, true up forecasts to actuals, and manage accruals"), AI Analytics, **Licensee Portal** ("portal for royalty statement upload, document sharing, electronic payments, and online account history"), DAM, **Statement Portal** ("electronic document delivery and personalized notifications"), Contract Ingestion (AI agent reads contracts, extracts rights/obligations, creates parties/agreements).
- Own FAQ definition: "IP management software automates the tracking, administration, and compliance of intellectual property rights based on licensing agreements. It pulls in usage or sales data, applies contract terms, and generates accurate reports—reducing manual work and ensuring audit readiness." / "IPM Suite manages the full lifecycle—from contracts to payments."
- Licensee-side evidence (Tervis case study): "Achieved accurate royalty calculations for over 100 licensors; Automated the creation of 50 unique royalty reports; Significantly reduced lengthy and costly audits." Licensee-side visuals: "Royalty statement and product performance chart showing minimum guarantees."
- Licensor-side evidence (homepage visual): "Character artwork applied to merchandise with global royalty earnings displayed."
- Industries: consumer goods, sports, publishing, toys/games, fashion/apparel/beauty. Enterprise customers: Disney, Marvel, Hasbro, Coca-Cola, Pearson, etc.
- Marketing metrics (20% savings in royalty overpayments, 50% reduction in processing time, 68% reduction in audit efforts) — vendor claims, not promoted.
- The licensing lifecycle (deal → product approval → royalty reporting → audit) is prominent: FADEL's center of gravity is the licensing relationship lifecycle with royalty processing as one leg (see Boundary Findings).

## Product E — EasyRoyaltiesPlus / That's Rights! (Book Matters, RIGHTS 20/20)

### Key observations (Layer A)

- Self-label: "Software for Author Royalties and Foreign Rights"; "Comprehensive royalties, rights management, and author portals for publishers"; EasyRoyaltiesPlus = "advanced royalty-accounting software... accurate calculations and clear, transparent reporting for even the most intricate royalty structures."
- Setup flow (vendor's own 3 steps): "1. Import authors, titles, contracts, and sales data. 2. Configure your royalty runs and calculation rules. 3. Generate verified royalty statements and reports."
- Distribution: "Statements can be distributed via automated email (MS Outlook or Gmail) or securely uploaded to the ROL Royalty Portal, providing guaranteed 24/7 access for authors and agents."
- Complexity machinery: "Escalating rates based on performance or price. Multi-layered splits for sub-rights income. Customized reserves, cross-collateralization, tax withholdings." "Royalty rules functionalities allow you to configure a wide range of publishing agreements — from the simplest to the most complex — with multiple formats, with one or multiple beneficiaries."
- Modular packaging: Foreign/Subsidiary Rights modules ("Interests, Foreign/subsidiary rights licenses, Incoming rights revenues (with AI-enhanced optical reading of incoming statements)") — the rights/relationship side ships as a separate product (That's Rights!) or add-on modules, confirming the royalty core is separable from the relationship surface.
- ROL Portal: "Downloadable, verifiable royalty statements, Detailed sales activity, Custom notifications and alerts"; "no limit on the number of authors, agents or other portal users."
- Data custody: "contract terms, distributor sales data, and royalty calculations remain securely on your local infrastructure. Only the finished, author-facing royalty information is published to the ROL Royalty Portal."
- Deployment: self-hostable (local PC/Windows server) or vendor cloud — the self-hosting pole for this Type.
- Target: "small to medium independent publishers"; 750+ companies claim (marketing).
- Incoming rights revenue with AI optical reading of statements — the money-in direction exists here too (sub-rights income), inside a payable-oriented product.

---

## Cross-product Comparison

| Structure | MetaComet | Curve | Reprtoir | FADEL | EasyRoyaltiesPlus | Strength |
|---|---|---|---|---|---|---|
| Contract/agreement as computable money terms | ✓ (contract terms/rules; escalators, tiers, splits, cross-collat, kit explosion, minimum guarantees) | ✓ (artist/writer contracts: sales terms if/then, cost terms, deductions, escalations, reserves, advances, opening balances, cross-contracts) | ✓ (contracts money-in/out: splits, rates, deduction rules, escalation rules, contract groups, recoupment) | ✓ (deal management + rights mgmt: advances, guarantees, payment schedules, royalty rates) | ✓ (royalty rules: escalating rates, multi-layered splits, reserves, cross-collat, tax withholding) | Universal (5/5) |
| Identified royalty recipients (payees/rights-holders) | ✓ ("personal information for each royalty recipient") | ✓ (Payees category) | ✓ (rights-holders as companies/contacts) | ✓ (licensees/licensors as parties) | ✓ (authors, agents, beneficiaries) | Universal (5/5) |
| Royalty base: products/properties bound to contracts | ✓ (products/titles/SKUs/patents) | ✓ (catalogue: tracks/releases/works; catalogue groups; auto-matching) | ✓ (assets: albums/tracks/videos/works; contracts linked to assets) | ✓ (properties/products licensed) | ✓ (titles, formats) | Universal (5/5) |
| Sales/usage ingestion from heterogeneous external sources | ✓ (Sales Aggregator; "all formats and currencies"; combine/map/convert) | ✓ (Sales + Sales Templates; "ingest sales files from anywhere"; millions of lines) | ✓ (statement pipeline: upload→map→errors→quarantine→calculate; dozens of named providers) | ✓ ("Automate sales and usage processing"; licensee statement upload portal) | ✓ (import sales data; AI optical reading of incoming statements) | Universal (5/5) |
| Matching/normalization machinery | ✓ (map sale types to contract terms) | ✓ (sales templates; mapping sales to contracts; term hierarchy) | ✓ (identifier-based matching; mapping; error/quarantine classes) | ✓ (usage/sales processing + validation) | ✓ (import + validation) | Universal (5/5) |
| Periodic calculation per contract terms | ✓ ("calculates royalty payments instantly"; payout schedules) | ✓ (period processing) | ✓ (calculation step; review before calculation) | ✓ (royalty calculation and validation) | ✓ (royalty runs; calculation rules) | Universal (5/5) |
| Balances with advances/recoupment/reserves carried | ✓ (advance roll-forwards, outstanding reserves, unearned advances, accruals) | ✓ (reserves with release schedules; opening balances; cross-contracts) | ✓ (contract balances → rights-holder balances; recoupment logic; closing) | ✓ (minimum guarantee recoupment; accruals) | ✓ (reserves carried forward) | Universal (5/5) |
| Statements per recipient | ✓ (generate + send + portal) | ✓ (period & artist/writer statements; automated sending; custom design) | ✓ (summaries + breakdowns; bulk email; portal) | ✓ (statement generation; statement portal) | ✓ (verified statements; email or portal) | Universal (5/5) |
| Payment records/files | ✓ (payment files for accounting/payment software) | ✓ (Payments collection; auto-payments; self-bill invoices; actual payout rails) | ✓ (payments to track cash flow) | ✓ (electronic payments via portal; ERP AP/AR) | ✓ (payment tracking) | Universal (5/5) |
| Recipient self-service portal | ✓ (Royalty Portal) | ✓ (Creator Dashboard) | ✓ (Rights-Holders Portal) | ✓ (Licensee Portal + Statement Portal) | ✓ (ROL Portal) | Universal (5/5) |
| Period close / locking | ✓ (period reports; accrual reporting) | ✓ (custom accounting period types) | ✓ (period close → balances transferred → statement issued → period permanently locked) | ✓ (period processing implied) | ✓ (royalty runs per period) | Strong (5/5, explicit mechanics documented in 2) |
| Audit trail / audit-readiness | ✓ ("make auditing a breeze"; audit rationale) | ✓ (statement design; csv statements) | ✓ ("full traceability from raw revenues to final payouts") | ✓ ("audit-ready tools"; "Manage audits and track violations"; audit-reduction case study) | ✓ ("fully auditable") | Universal (5/5) |
| ERP/accounting integration | ✓ (Oracle/NetSuite/SAP/QuickBooks...) | ✓ (payment rails; integration claims) | ✓ ("structured layer on top of general accounting") | ✓ (ERP AP/AR/GL) | ✓ (implied; local data custody) | Strong (5/5) |
| Money-IN direction (royalties receivable) | partial (revenue-share agreements; rights income via Rights module) | partial (publisher side ingests society income; mechanicals out) | ✓ (incoming AND outgoing contracts) | ✓ (licensor side: collect from licensees; guarantee recoupment) | partial (incoming rights revenues module) | Variant (direction NOT definitional) |
| Recipient analytics/forecasting | ✓ (forecasts at any level; forecast methods) | ✓ (creator analytics) | ✓ (sales analytics; portal analytics) | ✓ (AI analytics; forecasting; true-up) | — (not observed) | Common |
| Rights/licensing module (grants, availability) | ✓ (MetaComet Rights) | ✗ (none — pure royalty) | partial (Rights section for publishing use cases) | ✓ (Rights Management with collision/clearance) | ✓ (That's Rights! as separate product) | Optional |
| Managed/outsourced operation option | — (implementation service) | ✓ (fully managed royalty services) | — | — | — | Optional (single-product) |
| Self-hostable deployment | ✗ (cloud since 2007) | ✗ (web-based) | ✗ (SaaS) | ✗ (enterprise) | ✓ (local PC/server or cloud) | Variant |
| AI assistance (contract ingestion, optical reading, analytics) | ✓ (AI page) | — | — | ✓ (AIVA agents) | ✓ (AI optical reading) | Era-current, optional |

### What repeats everywhere (Layer B → candidate core)

1. **Agreements held as structured, computable money terms** — never just documents. Rates conditioned on dimensions (format/channel/territory/price tier/source), splits among multiple payees, advances with recoupment, escalators, reserves, deductions, minimum guarantees, cross-collateralization.
2. **A royalty base**: the products/properties/works the terms attach to, identified so external data can be matched to them.
3. **Ingestion of external sales/usage reports** from many heterogeneous sources, normalized (mapping, currencies, sale types) and matched to the royalty base — with explicit failure handling (unmatched lines, quarantines, error rules).
4. **The settlement loop**: periodic calculation per terms → balances (advances/recoupment/reserves carried forward) → statements per recipient → payment records/files → period close/locking → audit trail.
5. **A recipient-facing portal** — 5/5 products ship one; the statement is delivered and consumed digitally.
6. **Integration outward**: ERP/accounting consumes payment files and accruals; the royalty system is a specialized layer, not the general ledger.

### What varies (candidate L2/L3)

- Money direction (payable vs receivable vs both)
- Industry vocabulary (titles/tracks vs properties/products; authors/artists vs licensees)
- Suite packaging (royalty-only vs workspace suite vs licensing-lifecycle platform)
- Deployment (SaaS vs self-hostable), managed-service option
- Rights/availability machinery presence
- Payment execution depth (payment files vs actual payout rails)
- AI assistance, forecasting depth, analytics

---

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

The system of record for contractual royalty obligations, built on three jointly-held structures:

1. **The royalty agreement as the computable unit of record** — a persistent, identified agreement binding identified royalty counterparties to a royalty base (products, properties, works, licenses) under structured money terms (rates, splits, advances/recoupment, escalators, reserves, guarantees) that the system can execute. Remove → contract repository / CLM / sales-report tracker.
2. **Usage/sales ingestion attributed to the royalty base** — external sales or usage data from heterogeneous sources is normalized (mapped, converted) and matched to the contracted items, because royalty obligations are computed from what happened outside, not from invoices the operator issues. Remove → contract database with no computation input.
3. **The settlement loop** — periodic calculation per contract terms over the attributed usage, producing balances (with advances/recoupment/reserves carried forward), statements per counterparty, and payment records/files, with period close and an audit trail. Remove → a calculator, or a pass-through earnings pipeline.

Jointly-held load-bearing:
- 1 alone = contract store / CLM
- 2 alone = sales data aggregation (MetaComet ships Sales Aggregator as a standalone product — proof of separability)
- 3 without 1+2 = accounting shell
- 1+2 without 3 = royalty calculator without settlement
- 1+3 without 2 = statements computed from nothing
- 2+3 without 1 = flat payout pipeline (distribution-earnings pass-back territory)

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Recipient self-service portal (5/5 — but a paper statement mailed to recipients satisfies the settlement loop; the portal is the modern delivery surface)
- Recipient registry with roles/splits (payees, agents, co-holders)
- Multi-currency handling and conversion
- ERP/accounting integration (payment files, accruals)
- Reporting/analytics (reconciliation reports, balances reports, sales analytics)
- Forecasting from sales history + contract terms
- Rights/licensing modules (grants, availability) — present in some, absent in pure-royalty products (Curve)
- Statement design/branding; automated statement delivery
- Error-handling machinery as first-class workflow (quarantine, error rules, reprocessing)

### L2 — Variant / Optional Structure

- Money direction: payable-out (publisher/label/licensee side) vs receivable-in (licensor/franchisor side) vs both — NOT definitional
- Industry instantiation: book publishing, music (labels/publishers, dual-side), brand licensing, biotech/tech-transfer/patents, franchise, games, entertainment — NOT definitional
- Suite packaging: royalty-only specialist vs all-in-one workspace vs licensing-lifecycle platform
- Deployment: SaaS vs self-hostable; managed/outsourced royalty operation as a service
- Payment execution depth: payment files vs operating actual payout rails
- Industry-standard identifier/format machinery (UPC/ISRC/ISWC, CWR, CRD) — era/industry machinery
- AI assistance (contract ingestion, optical reading of statements, analytics)

### L3 — Vendor-specific (research notes only)

- MetaComet's "Royalty Management Lifecycle™" branding and "magic button" framing; named forecast methods (linear trend, moving average, Holt-Winters); named ERP list; 40,000-product scale claim; 90% time-reduction claim.
- Curve's specific if/then term variables (Cat Type, Cat Group, PPD deal type, Multiplier/Reduction % as Pro-tier "Complex Sales Terms" add-on); self-bill invoices; fees invoices for distribution commission; cross-contracts; custom statement design per company; CurrencyCloud/Visa payment-rail disclosures; Curve Lite tier; Jamen Capital/Merlin acquisition.
- Reprtoir's Operations (debit/credit entries) model; quarantine semantics; CRD format support; named statement-provider list; 150+ currencies claim; Organization Portal isolation; Revert Accounting; Audio AI.
- FADEL's AIVA agents (Contract Ingestion, Reviewer); Brand Vision / PictureDesk sibling products; marketing metrics (20/50/68); named enterprise customers.
- Book Matters' ROL portal data-custody split (only finished author-facing data published); MS Outlook/Gmail automated statement email; XX-Small plans.

---

## Vendor-specific Findings

See L3 above. None of these entered the canonical core.

## Boundary Findings

1. **vs Record Label Management** (flag delegated to this pass by that pass): the money loop (ingest→calculate→statements→payments) is shared machinery; the discriminator is the subject. Record Label Management holds the label's catalog + roster + deals + release operations as its center; a royalty platform computes over a royalty base with no release operations. **DECISION (this pass): music-specialized royalty-only systems (Curve) belong to THIS Type** as industry-scoped variants — Curve's own object world (payees, contracts, catalogue, sales, periods, statements, payments) is the generic royalty machinery in music vocabulary; it has no release operations, no destination network, no roster/campaign objects; its publisher line is the same machinery over works. Reprtoir is suite packaging: a label/publisher workspace whose royalty-accounting module is this Type's machinery. The record-label pass's "money-leg pole of the label-tool family" reading is ratified but the pole is placed on this side of the seam. Remove the royalty engine from Curve → nothing label-like remains; add release operations → it becomes a label system.
2. **vs Music Publishing Management** (flag from that pass): ratified — the works/entitlement core (writer/publisher shares, society deliveries) is the wall. Music royalty platforms serve masters and works sides in one product (Curve's two product lines; Reprtoir's publishing use cases) = dual-side packaging, not Type merger. Remove the works/entitlement structure → generic royalty software (this Type); add it → publishing management.
3. **vs Performing Rights Management** (ratified from that pass): society-side collective administration (usage attribution under published distribution rules, money pooled per source) vs contractual computation over one operator's agreements. Confirmed from this side: societies appear as statement providers / pay sources (Reprtoir documents SACEM/BMI/PRS/MLC statements as income sources; Curve's publisher side ingests society income). The PRO is inside this Type's ingestion, not a competing Type.
4. **vs Media Rights Management** (joint-review request from that pass): **keep-both RATIFIED.** Adopted seam holds: grant-of-record + availability/conflict/expiry resolution is the center there; royalty computation over reported usage is the center here. Tests from this side: remove royalty computation → MetaComet Rights and FADEL Rights Management remain as rights systems of record; Curve (no rights module at all) remains a pure royalty platform. Remove the rights/grant core → the royalty engine remains (Curve proves it). Suites bundle both as separately named modules (FADEL IPM Suite lists Rights Management and Royalty Management as distinct features; MetaComet sells Rights beside Royalty Tracker) — bundling is packaging, not identity.
5. **vs Author Management Platform** (joint-review request from that pass): **keep-both RATIFIED** on that pass's structural test. From this side: the recipient population of this Type is generic (payees/rights-holders/royalty recipients — MetaComet's industries span inventors, licensors, franchisees; Curve's payees are generic; EasyRoyaltiesPlus ships the author-relationship surface as a separate product, That's Rights!). Royalty-specialist products scoped to publishing do implement the settlement spine of author management (the gradient is real), but the defining population here is any royalty recipient, with no author-relationship surface (attribution display, correspondence) as core.
6. **vs Music Distribution Platform** (seam pre-drawn by that pass): ratified — supply-chain-derived earnings pass-back (store-reported earnings credited to the rights-holder account, platform share deducted) vs contractual royalty computation (terms with recoupment/escalators/reserves applied to ingested data). This Type ingests distributor statements as *input* (Reprtoir's provider list includes distributors); the seam is what the system does with the money: pass through a fixed arrangement vs compute obligations under each agreement.
7. **vs Book Publishing Management** (that pass holds this leaf downstream): confirmed — publishing management is the publisher's whole system of record (titles, production, editorial, rights, sales); royalty settlement is one module there (that pass lists "royalty settlement from ingested sales" as L1). MetaComet lists title-management systems (Firebrand) as integration targets — the royalty platform sits beside, not inside, the title system of record.
8. **vs Accounting Software / ERP**: royalty accounting is contractual logic (splits, recoupment, cross-collateralization), not general bookkeeping — Reprtoir's own positioning ("a structured layer on top of general accounting... not a replacement") and MetaComet's ("not adapted from generic accounting or ERP software"; ERP royalty modules criticized as limiting). Outputs (payment files, accruals) integrate into standard systems.
9. **vs CLM (§11)**: the agreement here is the source of structured money terms consumed by the engine, not the end artifact of a legal document lifecycle. Contract ingestion/creation exists (MetaComet's Acquisition phase; FADEL's Contract Ingestion) but is onboarding-adjacent, not the center.
10. **vs Franchise Management systems**: franchise royalty collection is a module of whole-business franchise systems; in this Type, franchise fees appear as a supported contract type (MetaComet: "franchise fees"). Held as a variant/contract-type observation; no franchise-management leaf was processed to joint-review it — noted for that pass if processed.
11. **"Remove what to become another Type" test**: remove the contract terms → sales reporting/aggregation; remove ingestion → contract repository; remove the settlement loop → calculator or aggregator; make the subject a label's catalog+roster+releases → Record Label Management; make it works+writer/publisher entitlements → Music Publishing Management; make it collective usage attribution under published rules → Performing Rights Management; make it grants+availability → Media Rights Management; make it pass-through earnings → Music Distribution Platform; add the author-relationship surface → Author Management Platform territory.
12. **Historical / market-sample check (per v1.1 §24)**: passed. A paper-era publisher's royalty desk — contract folder with recorded terms (rates, advances), sales figures transcribed from distributors' statements, clerk-calculated royalties per terms each period, handwritten statements, issued checks, reserves and advance balances carried forward — satisfies all three L0 legs with no software. A licensor's paper practice (licensee sales statements in, royalty invoices out, guarantee ledger) satisfies the receivable direction. The definition names no digital formats, identifiers, portals, clouds, or AI.

## Uncertainties

1. **FADEL operational depth**: support docs login-gated; workflow detail (how licensee statements are validated, how guarantee recoupment executes) held at product-page strength. Assertions about FADEL kept moderate.
2. **Enterprise publishing royalty systems** (Klopotek-class) not directly documented; the enterprise on-premise variant is held at lineage strength.
3. **Franchise-management royalty modules** not sampled; the franchise direction rests on MetaComet's contract-type claim.
4. **Reprtoir provider-count variance** (70+/120+/180+ across pages) — treated as marketing variance; no count promoted.
5. **Curve's payment rails** (CurrencyCloud/Visa disclosures) confirm payment execution exists, but per-territory coverage details were not researched; no precision promoted.
6. **MetaComet help center** not broadly sampled; workflow claims rest on product pages + lifecycle article (both official).
7. **Society-side royalty software** (the CMO's own distribution engines) was not sampled; the performing-rights pass covers that territory — seam assumed clean but only from the society side's evidence.

## Final Synthesis

A Royalty Management Platform is the **system of record for contractual royalty obligations**. Its world has three load-bearing structures held jointly:

1. **The royalty agreement as computable money terms** — identified counterparties bound to a royalty base under structured terms (rates conditioned on format/channel/territory/price tiers, splits among payees, advances with recoupment, escalators, reserves, deductions, minimum guarantees, cross-collateralization).
2. **Attributed usage/sales** — external sales/usage reports from heterogeneous sources (distributors, retailers, societies, licensees), normalized and matched to the contracted items by identifiers or mapping, with unmatched/erroneous data handled as a managed class.
3. **The settlement loop** — periodic calculation per terms → balances with advances/recoupment/reserves carried forward → statements per counterparty → payment records/files → period close/locking → audit trail, with a recipient-facing portal as the modern delivery surface and ERP/accounting integration as the standard outward edge.

The Type is industry-agnostic (publishing, music, brand licensing, biotech, franchise, games all realize it), direction-agnostic (payable out, receivable in, or both), and packaging-diverse (royalty-only specialists, workspace suites, licensing-lifecycle platforms). What makes it a Type is the jointly-held trio: terms + attributed usage + settlement. Remove any one and the product collapses into a neighboring kind of software (contract store, sales aggregator, calculator, pass-through pipeline, or — when the subject becomes a specific industry's catalog/entitlement world — one of the §27 sibling Types).
