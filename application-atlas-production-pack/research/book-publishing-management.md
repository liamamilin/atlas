# Research Notes — Book Publishing Management

Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Publishing Editorial Workflow, Publishing Metadata Management; adjacent processed: Author Management Platform, Book Distribution Management, Academic Journal Management)

Research date: 2026-09-06

## Research Goal

Understand what a Book Publishing Management application actually is as an Application Type: what objects exist inside a publisher's management system, how a title moves from idea to publication and into the backlist, how people (authors/contributors), contracts, money, production, rights, and metadata relate to the title record, and where the boundary lies against Publishing Editorial Workflow, Publishing Metadata Management, Author Management Platform, Book Distribution Management, Royalty Management Platform, and generic ERP/project management.

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- Core use: the publisher's internal system of record for running the publishing business — the title (book as a commercial product) as the central managed object, moved through a planned lifecycle (acquisition → contract → editorial/production → publication) with the associated money (P&L, advances, royalties, rights income) and supply-chain data (metadata/ONIX).
- Likely users: acquisitions/editors, production, contracts & royalties, rights, marketing/publicity, sales, finance/management at book publishers of all sizes (trade, academic, children's, religious, educational).
- Nearest neighbors: Publishing Editorial Workflow (content process), Publishing Metadata Management (title data itself), Author Management Platform (people-and-money layer), Book Distribution Management (trade operation), Royalty Management Platform (settlement engine), generic ERP / Project Management.
- Likely confusion: "publishing" in the directory also means CMS/news publishing (web content) and desktop publishing (layout); this leaf means managing the *book publishing business*.
- Unknowns: whether the market realizes this as one suite or as modules; how deep money machinery (royalty settlement) sits inside such systems vs delegated to specialist products; whether the two unprocessed sibling leaves (Editorial Workflow, Metadata Management) will turn out to be partial aliases.

## Research Questions

1. What is the central managed object — the title? How do work/edition/product/ISBN/family/series/sets relate?
2. What does the title lifecycle look like (acquisition → publication → backlist)? What anchors it (publication date)? What states exist?
3. How are contributors attached, and how do contracts encode terms (rights, rates, advances)?
4. How does title-level financial planning work (P&L: forecasts, costs, margin) and what role does it play in the acquisition decision?
5. How is production managed (specs, purchase orders, suppliers, print runs, files)?
6. How are schedules and tasks handled (templates, dependencies, company-wide notification)?
7. How do rights & permissions work (acquired vs available to sell; permissions received)?
8. How does metadata (bibliographic data, classifications, ONIX) flow to the trade?
9. How do sales data, royalties, and reporting close the loop?
10. Which capabilities are defining vs common vs variant vs vendor-specific? Historical/regional check: do older (on-prem, pre-ONIX), regional, and differently positioned products fit the same core?

## Representative Products

Selected across market structure (enterprise suite / SMB modular suite / modern indie cloud / workflow-specialist), prioritizing reachable official documentation:

| Product | Segment / role | Why selected | Evidence quality |
|---|---|---|---|
| Klopotek (STREAM: TEP + CRR) | Enterprise publishing management suite; self-described "international market leader"; used by large multinational groups and SME cloud customers | Deepest evidence of the full publisher business model: title lifecycle, contracts, royalties, rights, production, scheduling, metadata | A (official product pages, fetched) |
| Stison (Title/Royalties/Rights/Production Manager) | SMB cloud publishing management (UK), 300+ publishers claimed | Modular suite shape; shows which modules are separable and how they bolt together | A (official site + product pages, fetched) |
| Consonance | Modern cloud "publishing enterprise management" for independent publishers (UK); all book segments incl. scholarly/hybrid | Best operational documentation of the core triad (work–contract–products), plans (title P&L), seasons, pipelines | A (official docs, fetched) |
| Firebrand Title Management Enterprise (TME) | Title-lifecycle workflow specialist (US), since 1994; enterprise + Lite tier | The "title lifecycle as system of record" archetype; strong acquisition→publication workflow evidence; historical depth (1994) | A (official product pages, fetched) |

Cross-reference: the processed sibling research (book-distribution-management, author-management-platform) independently sampled the same four vendors from the distribution and author/royalty angles; this pass sampled the title-lifecycle/business-management angle of the same products plus new Klopotek TEP/CRR pages, giving triangulated coverage.

Considered but not sampled this pass: Ingenta/BiblioSuite (403 in the author-management pass — not retried), Open Monograph Press (workflow-first scholarly tool, belongs primarily to the Publishing Editorial Workflow angle), Pressbooks/Booktype (book production/authoring, not publisher business management). Legacy/regional products (virtuos, Titleplay, CatS, Publishers Assistant, Broadland) were unreachable in sibling passes; not retried.

## Sources

- Klopotek — https://www.klopotek.com/ ; https://www.klopotek.com/title-management-editorial-and-production ; https://www.klopotek.com/contracts-rights-and-royalties (retrieved 2026-09-06)
- Stison — https://www.stison.com/ ; https://www.stison.com/production-manager (retrieved 2026-09-06); Title Manager page previously fetched by the book-distribution pass
- Consonance — https://consonance.app/docs/ (index) ; /docs/add-a-new-work-and-its-products/ ; /docs/about-plans/ ; /docs/about-seasons/ (retrieved 2026-09-06)
- Firebrand Technologies — https://firebrandtech.com/ ; https://firebrandtech.com/title-management-enterprise (retrieved 2026-09-06)
- Sibling research used for triangulation: research/book-distribution-management.md, research/author-management-platform.md (same vendors, different angles; both fetched 2026-09-06)

## Product Observations

### Klopotek (Title Management Editorial & Production + Contracts Rights & Royalties) — evidence layer A

Positioning:

- "Publishing Management Software for All Publishers"; "the international market leader in the area of publishing software"; "supports the entire value chain for print and digital publishing"; "suitable for large multi-national publishing groups as well as small and mid-sized publishers"; over 400 publishers (vendor claim). "Klopotek software is specifically designed for the publishing industry: unlike customized versions of generic ERP solutions."
- Delivery: on-premise "Classic Line" (30 years of experience) + cloud STREAM web apps ("Complete essential business tasks wherever you are… harmonized workflow of all of your publishing tasks").

Title Management, Editorial & Production (TEP):

- **Title Life Cycle Manager** — three apps in one: *Early Title Manager* ("editors can create first drafts without cluttering the system"; "Planning and budgeting tools for doing a first calculation can be used, even if only little information on a planned title is available"; workflow covers "entering first pieces of information… to preparing for getting the title approved at the Editorial Meeting"); *Title Structure Manager* (new titles from "title templates"; "'Title families' enable users to combine different version types and formats of the same intellectual property"; "Planning an audio book or e-variant to follow a book that has already been published… in a few clicks"); *Title Metadata Editor* (workflow-driven metadata entry, configurable scenarios). Unified dashboard with filters: "drafts", "forthcoming", "published" titles, series.
- **Title & Work Structure Management** — "Managing 'works' (intellectual property) and creating titles based on these works helps you to be more efficient"; Work Component Manager (agreements "for components of works" also appear in Contract Manager).
- **Product Dashboard Apps** — *Product 360°* (configurable widget dashboard; widgets include "Record Status and Publication Dates", "Print Sizes, Specification and Extent", "Prices Per Copy", "Product Sales and Returns", "Classifications" (BIC, BISAC, Thema), set/series relations tree; keyword search over large title databases; can pull stock info from a distributor); *Product Quality Manager* (metadata quality monitoring at title-list and single-product level; "workflow-based quality checks"; reference to German "VLB Gold Status"); *Inventory Manager* ("clearly determine when your publishing products should be reproduced"; forecast vs real sales; minimum stock auto-computed; "users can directly decide on production-related actions, e.g. reprinting").
- **Classification Manager** (BIC/BISAC/Thema), **Blurb Manager** ("texts… needed in the title approval process, for marketing activities as well as for providing bibliographic details"), **Sales Price Manager** (complex price structures; customer-specific price lists; per ISBN; multiple price types and currencies; per-country rounding; full price history), **Collective Revisions & Operations** (mass updates), **Metadata Export Manager & Content Delivery** (ONIX exports, flyers).
- **Project & Production Management** — *Scheduling* ("production schedules… including dependencies"; Gantt; recalculation when "priorities have changed"); *Notification Dashboard* ("schedules are created and modified by specialists, but many people's daily tasks at a publisher are affected by these plans… a configurable notification dashboard to all employees, so everybody in the company will always know what has to be done by when"); *Production Management*: Purchasing ("order and controlling processes of vendor services"; guided order-placement workflow) + Suppliers Online (suppliers "also get access to the tools").
- **Permission & Compliance Manager** — inbound rights: "You've acquired various rights, but for which types of traditional and digital publications, exactly, limited to which extent, and for how long?… handle every aspect of the metadata necessary to acquire licenses, track their use, and manage compliance."

Contracts, Rights & Royalties (CRR):

- **Contract Management** — Contract Manager ("clear overview of all active projects with status information on rights acquisition, negotiated terms, and monetary aspects of a deal"; supports acquisition "from authors, agencies, or other publishers"); Contract Wizard (basic info → parties → agency → "assigning works or product lists"; contracts "for components of works or products"); Contract Workflow Manager ("control, monitor, and document the contracting process from the first draft through approval and signature via defined workflows"); templates; multi-contract editing; terms tracked as data with change history.
- **Royalty Accounting** — Royalty Accounting Manager (archived statements and payment remittances; adjustments); Royalty Sales Data Editor; Royalty Forecast Manager; Royalty Recipient Manager ("all the details that are legally requested for calculating royalties according to the laws and rules of author associations in different countries").
- **Author Management** — Author 360°; Authors Online ("make royalty statements and data available to authors and their agents in a secure way").
- **Rights Sales Solution** — Rights Sales Manager ("clear overview of the rights which have been acquired from an author or agency, and the rights which remain available to sell"; tracking "registered interest and options to the point of contract negotiations and agreement"); Rights Sales Contract Manager (sales contract auto-generated from negotiated terms); Rights Accounting Manager ("managing sub right claims to handling incoming rights payments and generating the payment share for the authors"); **Intercompany / International Publishing Deals** (transactions between legal entities of a publishing group; "transmit rights flexibly through all legal entities and report on this to the author in one single royalty statement").
- O2C (Order to Cash) is the separate distribution/sales solution area (see sibling research); CRM and Analytics are further sibling areas.

### Stison — evidence layer A

- Positioning: "Seamless software for publishers of all sizes"; "publishing management system used by over 300 publishers" (homepage; the Production Manager page says "over 150 publishers" — vendor counts inconsistent across pages, treat as unverified); aim: "give small and medium sized book publishers the chance to run their systems with the same efficiency previously only available to the much larger companies."
- **Title Manager**: bibliographic database + ONIX feeds; pre-flight data checks; price profiles; marketing materials (advance information sheets, order forms, catalogues); contacts; groups & permissions; work-based views (editions grouped by work). (Details from sibling book-distribution pass.)
- **Royalties Manager**: "upload sales data, generate pay runs and manage statements"; "Effortlessly manage payments and contracts, customise the data as you need and remove unnecessary complexity."
- **Rights Manager**: "Simplify the rights management process and see rights bought, sold, royalties and licences at a glance."
- **Production Manager** (fetched this pass): "take full control of the production schedule"; *Custom tasks and schedules* ("Create and assign multiple tasks to product schedules with multiple dependencies"); *Workflow* ("very visual production schedule, see the complete picture at a glance to spot potential issues and opportunities ahead of time"); *Stop-go P&L analysis* ("Create a P&L for multiple outputs with varying costs to better inform decisions, and for future review"); *Notes* ("Keep communication flowing between team members at any point in pre-production or production"); *Costs and print runs* ("Track all estimated and actual details across production costs and print runs"); *Custom reports* ("Gantt charts, printer schedule report, grid reports"); *Pre-production* ("Track ideas, submissions and proposals to assist in editorial review meetings"); *Complete compatibility* ("Bolt this module onto others, such as Royalties Manager to link with sales data").
- Modular shape is the point: the four Managers are separately licensed modules over one title database.

### Consonance — evidence layer A

Positioning: "Publishing enterprise management solution for the modern book publisher"; "intuitive title management software written and supported by publishers, for publishers"; segment pages: scholarly & academic, educational & professional, children's & novelty, trade & illustrated, religious, licensing/content & distribution, hybrid & partnership. Documentation structure itself maps the domain.

- **Getting started — "Add a new work, its contract and its products"**: "Create a new work before you've made a decision about whether or not to publish. Enter as much data as possible, to make as sound a publishing decision as possible. Then, if you do decide to go ahead, you won't have to type in a lot of data – the hard work will already be done." Duplicate an existing (exemplar) work or create from scratch; creation "creates the work, editable on the metadata page, and a blank contract, editable on the contract page"; add products to the work. In-house editions and formats are internal reference data that "won't feed out via ONIX".
- **Works & products (metadata docs)**: works as intellectual property with contributors (roles, display order, biographical notes), subject classifications (Thema), translations, series, sets; products attached to works with ISBN-13, barcodes, prices, publication dates (including "alternative publication dates"), backlist products, duplication, per-product ONIX toggles.
- **Plans (title P&L)** — "A Plan is applied to a set of works and their products with the intention of working out the financial implications of choosing to publish them": sales forecasts per product across multiple channels and currencies; costs at work level ("origination gets paid once per work") and at product level ("print costs are at product level"); report "to show the expected margin contribution"; plan roles ("Planner, Plan sales estimater"); plan statuses ("Planning in progress, Planned, pending decision"); "If the plan is approved and publishing is to go ahead, then those works and products are in the system ready for further development." Default cost groups: Editorial origination (advances, indexing, copyediting, proofreading, cover design, typesetting, warehousing and fulfilment, marketing, overhead), Publishing fees (indexing, sponsorship, grants), Rights (co-edition, extract, film, first serial, second serial, translation, TV).
- **Seasons** — "a way of grouping works together based on their expected publication date… often ties in with catalogues or sales and marketing campaigns"; season page is "a readiness overview on the completion of the workflow and metadata completeness"; seasons usable as reporting conditions.
- **Project management** — Briefings, Discussions, Issues, Pipelines ("Create and use a pipeline"; "Pipelines: ten uses" — acquisition-side), Roles, To-dos (setup from spreadsheets), Tracked copies.
- **Production** — production files upload; "About production runs" (print, digital, audio production runs; print on demand — from feature list in sibling research); "Notes for production managers" guidance exists.
- **Contracts & royalties** — contract templates (add/duplicate); "Set up a complex contract"; escalators; offsetting fees against royalties; "Prepare a work for royalties" (royalty-specific contract data); royalty runs ("Calculate royalties", "Troubleshoot royalty problems"); statements ("Generate statements"); payments ("Add payments made"); implementation guides for new publishers and legacy-data migrations.
- **Rights & permissions** — "Record permission you've received" (inbound permissions); "Add a rights deal" (outbound).
- **Data exchange** — ONIX feed setup and transmission checks; data-quality checks; import sales, prices, products, contacts; CSV exports with change reports; import contract royalties.
- **People & organisations** — address book with deduplication; contacts as contributors/payees (see author-management sibling research for the royalty side).
- Inspiration docs: "Best practice publishing process"; "Notes for production managers".

### Firebrand Title Management Enterprise — evidence layer A

Positioning: "Comprehensive lifecycle management built to adapt to every publisher's unique workflows"; "The Publishing Industry's Single Source of Truth Since 1994"; "a comprehensive publishing workflow platform that serves as the central system of record for a publisher's titles, metadata, schedules, contracts, production, marketing, and sales activities… designed to manage the entire lifecycle of a publishing project—from acquisition through publication and beyond." Vendor scale claims (unverified): 3,200+ publishers served, 1M+ titles managed, 600+ trading partners, 40,000+ product updates imported monthly.

Feature areas (all from official page):

- **Acquisitions & Financial Planning** — "Track submissions and manage peer reviews from the initial idea phase. Build dynamic Profit & Loss statements to make strong business cases." FAQ: "calculate format-specific sales, royalties, prepress, and manufacturing costs at every critical stage—from initial acquisition through transmittal and publication."
- **Editorial & Metadata Management** — "Centralize your core bibliographic data and descriptive copy in one hub"; metadata delivery to the trade via Eloquence on Demand (separate product line).
- **Contracts & Rights** — "Securely capture trackable author contract details and complex royalty rates"; FAQ: contracts capture "territories, royalty rates, licensed content, and advance payment dates—at the exact point of acquisition"; executed files stored; "Monitor available and sold subrights deals instantly via a dedicated dashboard"; cash-flow impact visible to leadership.
- **Production & Manufacturing** — "Manage detailed, component-based printing specifications all in one place. Efficiently create purchase orders to eliminate the need for disconnected spreadsheets."
- **Scheduling & Task Tracking** — "highly customizable schedule templates"; tasks/deadlines auto-assigned "based on their roles"; "automated email alerts"; dashboards surface "active titles, overdue tasks, and critical approval deadlines."
- **Asset Management** — digital files stored within title records; connections to external DAM systems.
- **Marketing, Publicity, & Sales** — plan campaigns; "automatically generate professional Tip Sheets"; push data into InDesign catalogs (EasyCatalog plugin).
- **Reporting, Dashboards, & Integrations** — leadership dashboards; "Seamlessly integrate data from our title management system with ERPs and other essential internal systems."
- **Journals & Periodicals** — "Track volumes, issues, and individual articles through dedicated peer-review scheduling" (periodical extension).
- **Title Management Lite** — smaller-publisher tier: "Acquisition and contract management, Schedule and task tracking, Catalog creation, Seamless metadata distribution via Eloquence on Demand"; upgrade path to Enterprise.

## Cross-product Comparison

| Dimension | Klopotek (TEP/CRR) | Stison | Consonance | Firebrand TME |
|---|---|---|---|---|
| Title/work as central record | ✓ Title Life Cycle Manager; Title & Work Structure ("works (IP)" → titles) | ✓ Title Manager bibliographic database (work-based views) | ✓ works + products ("Add a new work, its contract and its products") | ✓ title records as "single source of truth" |
| Work/edition-product split | ✓ title families: version types & formats of same IP | ✓ editions grouped by work | ✓ works vs products; in-house editions/formats; ISBN per product | ✓ component-based specs; format-specific P&L |
| Pre-publication record (before decision) | ✓ Early Title Manager drafts, editorial-meeting approval | ✓ pre-production: ideas/submissions/proposals for editorial review | ✓ works created before the publish decision; pipelines | ✓ submissions + peer reviews from idea phase |
| Title P&L / budgeting | ✓ planning/budgeting "first calculation" with little data | ✓ stop-go P&L ("multiple outputs with varying costs") | ✓ Plans: channel forecasts + origination/print costs + margin report | ✓ dynamic P&L statements at every critical stage |
| Contract machinery | ✓ Contract Wizard; draft→approval→signature workflow; templates; terms as data | ✓ payments & contracts (Royalties Manager) | ✓ blank contract per work; templates; escalators | ✓ contract details at point of acquisition; executed files |
| Contributors/authors | ✓ Author Management: Author 360°, Authors Online portal | ✓ contacts module | ✓ contributors with roles/order/bios on works | ✓ author contract details |
| Royalty settlement | ✓ Royalty Accounting (runs, statements, forecasts) | ✓ Royalties Manager (pay runs, statements) | ✓ royalty runs, statements, payments | rates captured; computation not evidenced on fetched page |
| Rights | ✓ inbound Permission & Compliance + outbound Rights Sales + intercompany | ✓ Rights Manager (bought/sold/licences) | ✓ permissions received + rights deals | ✓ subrights dashboard (available vs sold) |
| Production | ✓ Purchasing + Suppliers Online (vendor portal) | ✓ Production Manager (tasks, costs, print runs) | ✓ production runs (print/digital/audio), files, POD | ✓ printing specs + purchase orders |
| Schedules & tasks | ✓ Scheduling (Gantt, dependencies) + Notification Dashboard | ✓ visual production schedule, dependencies | ✓ to-dos, pipelines, calendars; seasons as readiness view | ✓ schedule templates, role-based tasks, alerts |
| Metadata to industry standard | ✓ Metadata Export (ONIX), BIC/BISAC/Thema, Product Quality Manager (VLB) | ✓ ONIX 2.1/3.0 feeds, pre-flight | ✓ ONIX feeds + transmission checks, Thema, data-quality checks | ✓ via Eloquence on Demand |
| Marketing materials | ✓ Blurb Manager, flyers | ✓ AI sheets, order forms, catalogues | ✓ marketing materials templates (Data Studio) | ✓ tip sheets, InDesign catalogs |
| Sales data / reporting | ✓ Product Sales and Returns widgets; Analytics area | ✓ sales uploads into royalties | ✓ import sales; sales analysis; custom reports | ✓ integrations import product updates; ERP integration |
| Stock / reprints | ✓ Inventory Manager (forecast-driven reprint decisions) | — (delegated to distributors) | production runs/POD; no stock module evidenced | — |
| Seasons / publication waves | not directly evidenced | catalogs per season implied | ✓ seasons as first-class object | ✓ seasonal catalogs |
| Roles/permissions | ✓ (role-based dashboards; suite permissions) | ✓ groups & permissions | ✓ group management, plan roles | ✓ role-based task assignment |
| Segment focus | enterprise groups + SME cloud | SMB | indie/mid, all book segments | mid-to-enterprise (US); Lite for smaller |
| Deployment | on-prem Classic Line + STREAM cloud | SaaS | SaaS | hosted service (since 1994) |

Evidence: all rows layer A (directly observed on fetched official pages) for what the pages document; "—" means not evidenced on fetched pages (absence of evidence, not evidence of absence).

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as book publishing management:

```text
Title record (a work with its editions/products — the book as a
planned commercial product)
├── Contributors attached to the title under recorded contract terms
│   (attribution + rights granted + remuneration obligations)
└── Title lifecycle from pre-publication planning to publication
    (record exists before publication; advances through planned stages
    toward a planned publication date)
```

Four properties:

1. **Title as central managed record** — the system's world is organized around titles (works and their editions), not around generic projects, customers, or ledger entries. Remove → generic project management or ERP.
2. **Contributors under contract** — creators are attached to titles with attribution and recorded commercial terms; the money relationship is structural, not optional. Remove → bibliographic catalog or metadata manager.
3. **Pre-publication lifecycle** — the title record exists while the book is still a decision (acquisition/proposal stage) and is advanced through planned stages to publication. Remove → a book database or distribution system (both start from decided/published titles).
4. **Publication date as the organizing anchor** — schedules, metadata completeness, materials, and availability all hang off the planned publication date. Remove → task tracking without publishing semantics.

Historical check: a 1990s on-prem title-management system (TME, 1994) and pre-digital publisher practice (title files, contract folders, publication schedules — see author-management sibling research) satisfy exactly this core; nothing in L0 requires cloud, ONIX, P&L computation, or digital formats.

### L1 — Common Mature Structure

Present across the researched sample:

- **Title P&L / acquisition financial planning** — sales forecasts per channel/format against work-level origination costs and product-level manufacturing costs, producing an expected margin for the publish decision. All four products evidence some form. [A×4]
- **Production schedules and task machinery** — per-title schedules with task templates, dependencies, deadlines, and company-wide visibility. [A×4]
- **Production management** — printing/manufacturing specifications, purchase orders, supplier interaction, print runs, production files/assets. [A×4]
- **Contract machinery** — contracts recorded as structured data (parties, rights, terms, advances) with workflow (draft → approval → signature), templates, and document storage. [A×4 — Firebrand evidences data capture + storage; workflow machinery evidenced at Klopotek/Consonance]
- **Contributor/author management** — contributor records with roles; relationship maintenance; author-facing portals in some products. [A×4; portal A×1→common]
- **Rights & permissions tracking** — inbound (permissions received, rights acquired with scope/duration) and outbound (subrights available vs sold, rights deals, income shares). [A×4]
- **Royalty settlement** — sales data ingestion → calculation under contract terms → statements → payments. Evidenced directly in three of four; in the fourth, rates are captured and settlement presumably handled downstream/integrated. Treat as standard machinery of full suites, with specialist-module delegation as a known pattern. [A×3]
- **Bibliographic metadata management to industry standards** — classifications (BIC/BISAC/Thema), data-quality checks, ONIX (or equivalent) export to the trade. [A×4]
- **Marketing/publicity materials from title data** — tip sheets, advance information sheets, catalogs (some auto-generated into layout tools). [A×4]
- **Sales data ingestion and title-level reporting** — sales/returns flowing back from the trade for analysis and royalties; dashboards/reports per title, season, imprint. [A×4]
- **Roles/permissions and multi-department operation** — acquisitions, editorial, production, contracts/royalties, rights, marketing, sales share one record base with role-specific views. [A×4]

### L2 — Variant / Optional Structure

- **Packaging and deployment**: full enterprise suite vs modular SMB suites (modules separately licensed over one title database) vs workflow-specialist core with companion services; on-prem vs cloud.
- **Segment calibrations**: trade & illustrated, scholarly & academic (open-access products change the money model), educational & professional, children's & novelty, religious, hybrid/partnership publishing.
- **Periodicals extension**: journals/periodicals (volumes, issues, articles, peer-review scheduling) added to the book model in some products.
- **Group/intercompany structures**: multi-entity publishing groups, intercompany rights transfers, consolidated royalty statements.
- **Stock/reprint machinery**: inventory monitoring and reprint decisions inside the system (some products; others delegate to distributors).
- **Regional conventions**: national metadata registries and quality schemes (e.g., the German books-in-print register), regional classification standards, regional trade data formats.
- **Author-facing and supplier-facing portals**: authors/agents viewing statements; suppliers viewing orders.
- **Digital products and POD linkage**: e-book/audio editions as products; print-on-demand triggers.
- **ERP/accounting coupling**: integrate-with-ERP posture vs fuller in-system financials.
- **AI assistance**: AI drafting/assistance layered on title data (emerging; vendor-marketed).

### L3 — Vendor-specific (Research Notes only)

- Klopotek: STREAM platform and app family (Product 360°, Early Title Manager, Contract Wizard, Notification Dashboard, Authors Online, Rights Sales Solution, Intercompany/International Publishing Deals, Royalty Forecast Manager, AI Assistant "Kleo"); VLB Gold Status support; "over 400 publishers" (vendor claim); 30-year Classic Line heritage.
- Stison: separately licensed Manager modules; price profiles; Onix Pre-Flight; stop-go P&L; publisher counts inconsistent across own pages (300+ homepage vs 150+ production page — unverified).
- Consonance: Plans with named default cost groups; seasons as first-class objects; exemplar-work duplication; pipelines ("ten uses"); Data Studio; tracked copies; GraphQL API; "About Open Access and Free Products" scholarly posture.
- Firebrand: TME since 1994 ("industry standard"); TME Lite tier with upgrade path; EasyCatalog/InDesign catalog automation; Eloquence metadata services family (EOD/EOA/Flywheel); vendor metrics (3,200+ publishers, 1M+ titles, 40,000+ monthly updates — unverified).

## Boundary Findings

- **vs Publishing Editorial Workflow (sibling, unprocessed)**: the editorial-workflow leaf centers on the *content process* — submissions, peer review, editing rounds, production files — as manuscript-centric workflow. Book publishing management centers on the *title as a commercial product*: the same events appear, but as schedule tasks, decision gates (editorial meeting, plan approval), and money events, not as the editorial process itself. Observed overlap: Firebrand TME tracks "submissions and peer reviews" inside acquisitions; Consonance has pipelines/to-dos; Klopotek Editorial is a named area. Boundary test: remove contracts/money/metadata machinery and keep the content process → editorial workflow; remove the content-process depth and keep the business lifecycle → this leaf. **Flag for joint review** when the sibling is processed — acquisition-stage features sit exactly on the seam.
- **vs Publishing Metadata Management (sibling, unprocessed)**: metadata records, quality checks, and ONIX feeds are standard capabilities inside publishing management, but the metadata leaf would center on the title data itself (creation, quality, delivery to the supply chain) as the primary object. Boundary test: remove the lifecycle/contract/money machinery, keep title data → Publishing Metadata Management (see also book-distribution sibling research, which drew the same line from the other side). **Flag for joint review.**
- **vs Author Management Platform (processed)**: the people-and-money layer — creator registry, attribution, contracts, settlement loop. Publishing management *contains* it (Klopotek has an Author Management area; Consonance/Stison carry contributors+contracts+royalties inside). Boundary test: keep only people+contracts+settlement → author management.
- **vs Book Distribution Management (processed)**: the trade operation around published titles — accounts, orders, stock, dispatch, returns, sales records. Publishing management ends at making titles available and recording sales back; it does not run the trade operation. Boundary test: remove editorial/production/contracts and keep the trade operation → distribution management. (Klopotek ships both as separate solution areas: TEP/CRR vs O2C.)
- **vs Royalty Management Platform**: generalized settlement engine consuming sales records; inside publishing suites it is the royalty module. The author-management sibling already flagged the author-management/royalty seam; from this leaf the royalty engine is downstream machinery.
- **vs ERP / Accounting**: generic ledgers and finance lack the title object, contract-terms-as-data, rights scope semantics, and publication-date anchoring. Klopotek explicitly positions against "customized versions of generic ERP solutions"; TME positions as integrating *with* ERPs. Boundary test: strip publishing objects → finance/ERP.
- **vs Project Management Application**: production scheduling resembles project management, but the managed object is the title (with contract, ISBN, rights, royalty semantics), schedules are templates tied to publication dates, and the record persists into the backlist. Boundary test: strip title semantics → generic PM.
- **vs Desktop Publishing / Page Layout**: typesetting/layout is *tracked* (specs, tasks, files) not *performed*; catalogs are generated from title data into layout tools, not authored here.
- **vs News Publishing Platform / CMS / Magazine management**: "publishing" as web content delivery vs the book business. Different objects (articles/issues vs titles/editions), different money (subscriptions/ads vs rights/royalties), different supply chain (no ISBN/ONIX trade).
- **"去掉什么就变成另一个 Type" 判据**: remove the pre-publication lifecycle → book metadata/database or distribution; remove contract/money machinery → metadata management + task tracker; remove title/commercial semantics and keep the content process → Publishing Editorial Workflow; keep only people+contracts+settlement → Author Management Platform; keep only the trade operation → Book Distribution Management; strip industry objects → ERP/PM.

## Historical / Market-Sample Check

- **Era**: TME has run since 1994 as the "single source of truth"; Klopotek's Classic Line has 30 years of on-prem heritage. The 1994-era core — titles, contracts, schedules, P&L, production specs — matches the L0 with no ONIX/cloud/digital dependence. Pre-digital publisher practice (title files, contract folders, royalty ledgers; see author-management sibling research) maps to the same core.
- **Region**: the reachable sample is UK/US/Germany-heavy; regional products (virtuos/Germany, Titleplay/Denmark, CatS/US, Broadland/UK) were unreachable across sibling passes — recorded as limitation. Regional *conventions* (German VLB register; BIC/BISAC/Thema classifications; regional trade formats) appear as L2 configuration, not core. The L0 does not presume a specific market's metadata infrastructure.
- **Position**: scholarly presses, religious publishers, hybrid/partnership publishers (Consonance segment pages; Stison customer logos include a university press) fit the same core; open access changes the money model (L2), not the object structure. Periodicals (Firebrand journals module) extend rather than redefine the title model.
- The definition therefore holds against older, regional, and differently positioned products; nothing in the current cloud/SaaS/ONIX-dominant sample leaked into L0.

## Uncertainties

1. **Royalty settlement inside workflow-specialist products** — Firebrand TME captures rates and advance dates but the fetched page does not evidence in-system settlement runs; market knowledge suggests specialist royalty systems are a common pairing. Kept as "standard machinery of full suites, with specialist-module delegation as a known pattern" — no stronger claim.
2. **Stock/reprint depth** — only Klopotek evidences inventory monitoring directly; Consonance has production runs/POD; Stison delegates. Treated as common-to-optional, phrased conditionally in the final document.
3. **Seasons** — directly evidenced in Consonance; seasonal catalogs implied at Firebrand/Stison; not evidenced in fetched Klopotek pages. Kept in L1-adjacent as "common" with careful wording (publication-wave grouping), not as defining.
4. **Vendor counts** (Klopotek 400+, Stison 300/150, Firebrand 3,200+ publishers / 1M+ titles) — vendor marketing claims, unverified; not used in the final document.
5. **Acquisition-stage seam** — the exact split of submissions/peer-review machinery between this Type and Publishing Editorial Workflow is genuinely fuzzy in market products; both sibling leaves are unprocessed. Recorded as Boundary Issues for joint review rather than resolved unilaterally.
6. **Sample skew** — reachable products are vendors with strong web documentation (UK/US/Germany); smaller regional products and in-house systems could not be observed; claims calibrated accordingly (no precise numeric limits, state vocabularies, or defaults asserted in the final document).

## Final Synthesis

A Book Publishing Management application is the publisher-side system of record for the business of publishing books. Its defining core is small: the title (a work together with its editions/products) as the central managed record; contributors attached to that record under contract terms (attribution plus rights and remuneration obligations); and a pre-publication lifecycle that carries the title from first proposal through approval, contract, editorial and production, to a planned publication date. Around this core, mature products add the standard machinery of the publishing business: title P&L for the acquisition decision (channel forecasts against origination and manufacturing costs), contract workflow, production schedules with task templates and dependencies, printing specs and purchase orders, rights and permissions tracking in both directions, royalty settlement from ingested sales, bibliographic metadata to industry standards with ONIX export, marketing materials generated from title data, season/backlist organization, and role-based multi-department operation. The market realizes the Type in three postures — enterprise suite, modular SMB suite over one title database, and workflow-specialist core with companion services — plus segment calibrations (trade, academic/open-access, children's, religious, educational), periodical extensions, and group/intercompany structures. The Type is bounded from Publishing Editorial Workflow (content process vs title-as-commercial-product), Publishing Metadata Management (title data itself vs the business lifecycle around it), Author Management Platform (its people-and-money layer), Book Distribution Management (the trade operation it hands off to), Royalty Management Platform (its settlement engine), and generic ERP/PM (industry objects absent).
