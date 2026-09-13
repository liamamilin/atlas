# Research Notes — Author Management Platform

Research date: 2026-09-06
Status: leaf processed under v1.1 methodology
Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Book Distribution Management, Magazine / Periodical Management; nearby: Book Publishing Management, Publishing Editorial Workflow, Publishing Metadata Management, Royalty Management Platform, Creator CRM, Talent Agency Management)

---

## Research Goal

Understand what an "Author Management Platform" actually is as an Application Type: what object it centers on, who operates it and who is managed by it, what lifecycle governs the publisher–author relationship, and where it begins/ends relative to Royalty Management Platform, Book Publishing Management, Publishing Metadata Management, Publishing Editorial Workflow, Creator CRM, and Talent Agency Management.

## Initial Boundary

Hypothesis before research: the Type covers publisher-side software for managing the publisher's relationship with authors — author records, contract tracking (rights, royalties, advances), royalty statements and payments, contributor metadata, and correspondence/portals.

Risks identified up front:

1. **Word-sense ambiguity of "author"** — could mean (a) book authors managed by publishers/agents, (b) scholarly authors managed by journal submission systems, (c) content contributors managed by media outlets, (d) self-published writers as customers of author-service tools. These may be different Types with the same word.
2. **Author-side vs publisher-side** — author-facing writing/submission tools (word processors, query trackers) share the word "author" but are a different Type; this leaf sits in a publishing-operations cluster, suggesting publisher-side.
3. **Overlap with Royalty Management Platform** (sibling leaf) — royalty systems pay authors; overlap must be resolved.
4. **Standalone vs module** — publishing operations software tends to bundle; the leaf may be a Capability packaged inside suites rather than a standalone product market.

## Research Questions

- RQ1: What is an author record in publishing software — person or organisation, which attributes, which relationships (agent, estate, works)?
- RQ2: How are authors linked to works, and what role/metadata machinery exists?
- RQ3: What does the contract record capture (rights granted, remuneration basis, payees, splits, advances)?
- RQ4: What is the settlement lifecycle (sales intake → calculation → statements → payment → carry-forward)?
- RQ5: Do authors themselves interact with the system (portals, messaging, self-service)?
- RQ6: What remuneration mechanics are common (escalators, reserves, withholding, cross-collateralization)?
- RQ7: Which segments and packaging forms exist (suite vs royalty module vs title system; cloud vs self-hosted; publisher vs agency side)?
- RQ8: Boundary answers vs neighboring Types; does a standalone "author management" product exist?

## Representative Products

Selected for different packaging philosophies, geographies, and customer levels (publisher-side publishing-operations software; all official sources):

| Product | Packaging philosophy | Segment / Level | Evidence quality |
|---|---|---|---|
| Consonance (General Products Ltd, UK) | All-features-in-one publishing enterprise management SaaS ("features, not modules") | University presses, trade, academic, children's; from start-ups to multinationals (Tate, Liverpool UP, British Library Publishing, Taylor & Francis ONIX feeds) | A — official Tier-1 user documentation (docs site) |
| Stison (UK) | Modular suite: Title Manager + Royalties Manager + Rights Manager + Production Manager | Small/medium publishers (300+ publishers claimed), UK/Europe | A− — official product pages (Tier 2); help KB unreachable |
| MetaComet Systems (US) | Royalty-first specialist suite: Royalty Tracker® + Sales Aggregator + Rights + Royalty Portal | SMB-to-mid publishers; multi-industry (biotech, tech transfer, licensing, games) | A− — official product pages incl. FAQ section (Tier 2) |
| EasyRoyaltiesPlus / RIGHTS 20\|20 (Book Matters LLC, US) | Royalty accounting + rights modules + ROL portal; self-hostable | Small/medium independent publishers, packagers; agent-side configurations (That's Rights! Agents) | A− — official product pages (Tier 2) |

Attempted and rejected / unreachable:
- **Ingenta BiblioSuite** (ingenta.com) — HTTP 403 on both the root and product paths (2 attempts) → abandoned per source-access rule. The enterprise/legacy publishing-system tier therefore remains unverified in this sample; no claims made about it.
- **Stison Central Knowledge Base** (stison.zendesk.com) — transport error (1 attempt) → Tier-1 operational detail for Stison not available; Stison evidence stays at product-page depth.
- Products not fetched because the sample reached stop conditions (Workflow stop condition 4 — new products repeating existing evidence): Publishers Assistant, Firebrand Title Management (mentioned by MetaComet only as an integration target).

## Sources

- Consonance — https://consonance.app/ (positioning, feature list) — fetched 2026-09-06
- Consonance docs — https://consonance.app/docs/ (index), /docs/royalties-overview/ (About royalties), /docs/add-contributors-to-a-work/, /docs/1-edit-a-contract/ (Edit a contract), /docs/add-a-contact/ (Add a contact) — fetched 2026-09-06
- Stison — https://www.stison.com/ (home), /title-manager, /royalties-manager — fetched 2026-09-06
- MetaComet Systems — https://metacomet.com/ (home), /solutions/royalty-tracking-software/, /solutions/royalty-portal/ — fetched 2026-09-06
- Book Matters LLC (EasyRoyaltiesPlus / That's Rights! / RIGHTS 20|20) — https://www.easyroyalties.com/ → bookmatters.us (home/products) — fetched 2026-09-06

Source-access limitation: Ingenta BiblioSuite unreachable (403 ×2); Stison Zendesk KB unreachable (transport error ×1). For Stison, MetaComet, and Book Matters, evidence depth is official marketing/product pages (Tier 2), not operational help centers; Consonance supplies the Tier-1 operational depth. Precise numeric facts (default statement frequencies, exact rates, product counts, prices) are deliberately not asserted in the final document beyond what official pages state as product capability.

---

## Product Observations

### Consonance — Evidence layer A (Tier-1 docs)

Positioning: "Publishing enterprise management solution for the modern book publisher"; "features, not modules"; segments listed: scholarly & academic, educational & professional, children's, trade & illustrated, religious, licensing/content & distribution, hybrid & partnership.

Key observations:

- **People & organisations / Address book**: contacts are person or organisation records ("Add a contact" — choose person or company; address, phone, email, relationships; notes; de-duplication tool; tags; spreadsheet import).
  - Two structural association kinds to works: **contributors** ("contacts that need to be included in ONIX information") vs **non-contributing payees** ("contacts that need to be paid in association with a work, but not necessarily publicly attached to the work, such as an agent or literary estate").
  - **Pseudonyms** require two records: the credited (pseudonym) contact is attached to the work as contributor for ONIX/public surfaces; the legal-name contact is a non-contributing payee via contract payee splits.
  - Contact "types" are auto-derived from behavior: contributors (attached to works), data aggregators (receive ONIX feeds), POD printers, sellers.
- **Work ↔ contributor linkage** ("Add contributors to a work"): work page has a contributions section; each contribution has a **role** (e.g., "By (author)"), a contributor chosen from the shared address book (or created inline as person/organisation), optional regions/countries, product applicability, and a **display order** that is sent in ONIX (affects retail display order). Separate doc: add/edit contributor **biographical note**.
- **Contract** ("Edit a contract"): contractual data entered per work — term length, signatories, delivery dates, royalty rates, advance payments, reserves against returns — "can combine with a contract template in the system to generate a PDF contract… to form the agreement between you and your content licence holders." Data is worth entering even if the PDF is produced elsewhere because it drives to-dos (manuscript delivery dates) and royalty calculation.
  - Regions: Terms, Benefits, Rights ("the rights you are granted by the author / agent / IP holder, which can be sub-licensed"), Royalties, Sales rights (territories, with coverage checkers), Remittances (Payees, Royalty percentage splits, Advances, Payments), Deductions (Reserves against returns), Contract formatting/clauses, Files (signed scans, addenda).
  - **Royalty specifier**: total base rate (required), price basis (list price vs discount/net receipts, required), escalators by quantity / sale value / date / discount, guaranteed minimum/maximum. Specifiers are scoped: all sales on the work / a product / a product in a master channel / in a channel — a hierarchy where more specific specifiers override defaults.
  - **Payees & splits**: payees may differ from signatories ("contributors" and "non-contributing payees" such as agent or literary estate); percentage splits across payees must total 100%; splits can be set at work and/or product level.
  - **Advances**: entered as separate instalment records with trigger events (e.g., on signature / on delivery / on publication); entering a paid date creates a payment record; unpaid instalments must not carry a paid date.
  - **Payments**: money paid out must be recorded or the system would expect to pay it again at the next royalty period ("it would be a duplicate payment").
  - **Reserves against returns**: proportion of sales held back against retailer returns; rate can vary by statement number (e.g., descending schedule to 0%), releasing previously reserved amounts in later statements.
- **Royalty lifecycle** ("About royalties"): multi-step — (1) specify royalty rates in a contract, (2) load sales data, (3) create a **royalty run** (a batch of products through a calculation cycle, with an analysis step and review-before-approval), (4) create a **statement batch** (a group of contacts/payees for which statements are generated, review-before-approval). Factors considered: sales quantity/value per channel, base rate and its variations (sale date, price, cumulative quantity), advances and whether paid, months since publication, statement date vs publication date, reserve against returns. Rights sales can be included in statements as sales/payment items.
- **Rights & permissions**: record rights deals (acquired and sold); permissions in/out.
- Interfaces observed: product lists, work metadata page (summary cards), rights deals dashboard, contract edit page, Data Studio searches/reports, marketing-material generation, to-dos/pipelines; user permissions; GraphQL API; ONIX feeds outbound to supply chain.
- No author-facing portal observed on the fetched pages (not claimed either way).

### Stison — Evidence layer A− (Tier-2 product pages)

Positioning: "Seamless software for publishers of all sizes"; four products: Title Manager, Royalties Manager, Rights Manager, Production Manager; "over 300 publishers" (home) / "over 150 publishers" (product pages — inconsistent counts on vendor's own pages; treat as marketing, do not reuse).

- **Title Manager**: "a database to store your bibliographic data, as well as generating and distributing data feeds via Onix"; work-based views ("different editions of the same content can be grouped by work for more realistic P&L data"); asset management (store PDF/EPUB/covers/contracts/chapters against titles, content, or the work); **contact management** ("categorise by source, market, catalogue, mail or interest"); contributor details screen (screenshot); ONIX 2.1/3.0 feeds, pre-flight data checks; groups and permissions.
- **Royalties Manager**: "manage payments to your contributors, import sales and returns and store copies of the relevant contracts"; "Map any rule set — track and pay royalties across all contract variants… no limit to the number of breaks or escalators on a title"; **Payees**: "customise tax or withholding settings for individual payees or contributors"; **Payment management**: "manage advances, payments and balances with real time, and point in time reporting"; statements ("clear, concise statements in seconds"); import sales data in multiple currencies; customisable sales types; reporting; running from the same system as bibliographic data "can enable you to gain an understanding of the profitability of an individual title or **Author**".
- Cross-module observation: royalties, rights, production, and bibliographic modules share one data core; customer testimonial calls the royalties module "essential to our operations."

### MetaComet Systems — Evidence layer A− (Tier-2 product pages + FAQ)

Positioning: "Royalty Management Software… purpose-built for rights and royalties — not adapted from generic accounting or ERP software"; serves book publishing and other royalty industries (biotechnology, life sciences, technology transfer, online learning, video games, entertainment, consumer product licensing).

- **Royalty Tracker® workflow** (as stated): "Set up your contract terms, enter the personal information for each royalty recipient, upload your sales data, then push literally one button" → calculates payouts, generates statements, sends each statement to the recipient, posts it to the Royalty Portal.
- Recipient model: **"royalty recipients"** — "authors, inventors, artists, licensors, or distribution partners"; "enter the personal information for each royalty recipient".
- Contract logic: unlimited contracts; rates by format, channel, territory within a single contract; escalators, tiers, **splits** ("co-author, agent, and contributor splits… define each party's share directly in the contract setup"); advanced rules: cross-collateralization, kit explosion, minimum guarantees; sales-based royalties, milestone payments, revenue-share agreements.
- Sales intake: Sales Aggregator ("no matter how many sources and formats"); multi-currency.
- Reporting: named reports (Sales Reconciliation, Adjustments Reconciliation, Statement Balances); forecasting from sales history + contract terms.
- Integration: ERP/accounting (Oracle, NetSuite, SAP, QuickBooks…) and product databases (e.g., "Firebrand Title Management") — royalty data flows to accounting; product/title data comes from title systems.
- **Royalty Portal** (recipient-facing): 24/7 self-service for "authors, inventors, artists, licensors, or distribution partners" — view current and past statements; **contract storage** (deliver and store contracts); **document storage** (reports, documents, assets); **messaging** ("communicate directly with one or all of your recipients"); **self-service contact updates** ("Contacts can update their information immediately"). Publisher rationale: reduce support calls; transparency.

### EasyRoyaltiesPlus / RIGHTS 20|20 (Book Matters LLC) — Evidence layer A− (Tier-2 product pages)

Positioning: "Comprehensive royalties, rights management, and author portals for publishers"; ecosystem for "publishers, packagers, agents and other rights and royalties professionals"; small/medium independent publishers.

- Deployment: **local install (own PC/Windows server) or vendor cloud** — self-hosting as an explicit option; sensitive data (contract terms, distributor sales, calculations) stays local; "only the finished, author-facing royalty information is published to the ROL Royalty Portal."
- Onboarding sequence as advertised: "1. Import authors, titles, contracts, and sales data. 2. Configure your royalty runs and calculation rules. 3. Generate verified royalty statements and reports." — an explicit author/title/contract import triad.
- Remuneration mechanics: escalating rates (performance or price), multi-layered splits for sub-rights income, customized reserves, cross-collateralization, tax withholdings; one or multiple beneficiaries.
- Statement delivery: automated email (Outlook/Gmail) or **ROL Royalty Portal** — 24/7 access "for authors and agents"; downloadable verifiable statements; detailed sales activity; notifications; "no limit on the number of authors, agents or other portal users"; included in plans.
- Rights modules: That's Rights! (foreign/subsidiary rights: licenses, terms, territories, advances, royalty rates; submission tracking; receivables and royalty income tracking; AI-enhanced optical reading of incoming statements) — rights income connects to royalty data.
- **Agent-side configurations**: "That's Rights Agents" / "RIGHTS 20|20 Agents" for "rights and literary agencies" — manage multiple author clients, submission tracking and editorial feedback, incoming royalty revenue (with automated capture), comprehensive client reporting, **Agents Portal for clients**. The agency is the operator; authors are clients.

---

## Cross-product Comparison

| Structure | Consonance | Stison | MetaComet | EasyRoyaltiesPlus |
|---|---|---|---|---|
| Creator/recipient registry | Address book: person/org; contributors + non-contributing payees; pseudonyms; dedupe; auto-typed kinds; tags | Contact management with categories; contributor details on titles | "personal information for each royalty recipient" | "Import authors…"; authors/agents as portal users |
| Author ↔ work attribution | Contributions with roles, order → ONIX, product applicability | titles/works; contributor details; work grouping | recipients bound per contract/title; rates per format/channel/territory | authors × titles × contracts import |
| Contract record | Full structured contract editor + templates → PDF; signed scans stored | "store copies of the relevant contracts" | "set up your contract terms" (unlimited contracts) | "import… contracts"; configurable rules |
| Remuneration mechanics | base rate + price basis; quantity/value/date/discount escalators; min/max; splits=100%; advances w/ trigger instalments; reserves by statement no. | breaks/escalators unlimited; per-payee tax/withholding; advances/payments/balances | escalators/tiers/splits; cross-collateralization; kit explosion; minimum guarantees | escalating rates; multi-layered splits; reserves; cross-collateralization; withholding |
| Sales intake | Import sales; channel hierarchy | Import sales/returns; sales types; multi-currency | Sales Aggregator; all formats/currencies | Import sales data |
| Calculation lifecycle | Royalty run: analysis → calculate → review → approve | statements "in seconds" | one button → calculate → statements → deliver | configure runs → verified statements |
| Statement delivery | Statement batches (per payee/contact) | statements + reporting | send to recipients + Royalty Portal | email or ROL portal |
| Payment tracking | payments recorded; advance paid-date → payment record | advances, payments, balances (real-time/point-in-time) | payment files; balances report | statements + balances |
| Recipient portal | not observed | not observed | Royalty Portal (statements/contracts/documents/messaging/self-update) | ROL Portal (statements/sales activity/notifications) |
| Rights dimension | rights granted per contract; rights deals; sales rights territories | Rights Manager module | MetaComet Rights | That's Rights! modules; incoming rights revenue |
| Supply-chain metadata | ONIX contributor roles/bios/order | ONIX feeds | integrates from title systems (e.g., Firebrand) | — |
| Packaging | one system, all features | four named modules | royalty-first suite | royalty accounting + rights + portal |
| Deployment | SaaS | web-based | cloud-hosted | local/self-host or cloud |
| Operator scope | publisher | publisher | publisher/licensor across industries | publisher, packager; agency-side products |

Synthesis of the comparison:

- All four products maintain **identified records for the people who create the works** (and their representatives), **link those records to the publisher's works with attribution**, **record the commercial terms of each work's publication**, and **operate a recurring settlement cycle** from sales data to statements to payments. This four-part spine is the candidate defining core (Layer B cross-product commonality, with Consonance providing Layer A operational depth).
- The settlement loop is the center of gravity in all four; even the bibliographic-centric module line (Stison) sells royalties as its "essential" module, and MetaComet markets itself as settlement-first.
- **Payee ≠ credited contributor** appears in every product (agents/estates/agents-as-payees; splits; withholding per payee).
- Recipient self-service portals are common but not universal in the sample (2 of 4 observed) → common, not defining.
- Rights income and sales-rights/territory data orbit the same contract and payees in all four → common mature structure.
- Contributor metadata for the supply chain (ONIX roles/bios) appears where bibliographic management is in scope (Consonance, Stison; MetaComet imports title data instead) → common in publishing, structurally secondary.
- Packaging, deployment (incl. self-hosting), operator identity (publisher vs agency vs licensor), and industry generalization vary freely → variant layer.

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

```text
Publisher-side creator registry (identified authors/contributors — persons or organisations — plus their representatives)
└── Work attribution (creator ↔ the publisher's works, with attributed roles)
    └── Contract record (per work: rights granted, remuneration specification, payees and splits)
        └── Settlement loop (recurring: sales intake → amount-owed calculation per contract terms
            → statements → tracked payments → carried balances/reserves)
```

Four properties. Remove the registry → there are no authors to manage. Remove attribution → it is a generic address book / CRM, not author management. Remove the contract record → it is title/metadata management (Publishing Metadata Management). Remove the settlement loop → it is metadata plus documents, and the reason the Type exists (the publisher–author money relationship) disappears.

Evidence: settlement loop present in 4/4 products (Layer B); attribution in 4/4; registry in 4/4; contract record in 4/4 (structured editor in Consonance, stored copies + rules in Stison, terms setup in MetaComet, imported contracts in EasyRoyaltiesPlus).

### L1 — Common Mature Structure

Present in most mature products but not required for recognition:

- remuneration mechanics beyond a flat rate: escalators/tiered rates, reserves against returns, cross-collateralization, tax/withholding settings
- advances as instalment records with trigger events and paid-state tracking
- sales/returns import from distributors in multiple formats and currencies
- statement generation with review/approval before issue; payment recording and balances carried forward
- non-credited payees (agents, literary estates) and percentage splits between payees
- rights dimension: rights granted per contract; subsidiary/foreign-rights deals and income feeding the same payees
- contributor metadata for the public/supply chain (roles, order, biographical notes; ONIX in book publishing)
- recipient self-service portal (statements, contracts/documents, messaging, contact self-update) — 2/4 observed, market-expected
- deduplication, notes, tagging/categorization on person records
- auditability of calculations; integration toward accounting/ERP

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- packaging: all-in-one publishing suite vs modular suite vs royalty-specialist vs title-management-centric
- deployment: cloud SaaS vs self-hosted/local install
- operator identity: publisher vs packager vs literary/rights agency (agency-side configurations manage author *clients*)
- population generalization: recipients beyond authors (inventors, licensors, franchisees) in cross-industry royalty systems
- supply-chain metadata depth (ONIX, identifiers) and its coupling to contributor records
- segment calibration: trade vs academic/scholarly vs children's vs religious publishing; independent vs multinational scale
- regional/regulatory regimes (withholding, VAT/GPSR-style compliance surfaces)

### L3 — Vendor-specific (research notes only)

- Consonance: royalty specifier hierarchy (work → product → masterchannel → channel with override); contract template → PDF generation; "non-contributing payee" terminology; auto-derived contact kinds (data aggregators / POD printers / sellers); Data Studio; royalty importer; GraphQL API.
- Stison: four-product naming (Title/Royalties/Rights/Production Manager); "no limit to breaks or escalators" marketing claim.
- MetaComet: Royalty Tracker®/Sales Aggregator/Royalty Portal naming; named reports (Sales Reconciliation / Adjustments Reconciliation / Statement Balances); kit explosion, minimum guarantees; forecasting methods; "push one button" framing.
- Book Matters: ROL Royalty Portal naming; AI optical reading of incoming statements; That's Rights! / Agents configurations; XX-Small plan exclusion of portal.

## Vendor-specific Findings

See L3 above; none of these are promoted to the canonical model. Note also the vendor-page inconsistency (Stison "300+" vs "150+" publishers) — marketing numbers deliberately excluded from the final document.

## Boundary Findings

1. **vs Royalty Management Platform (sibling §27 leaf)** — closest neighbor; a gradient, not a wall. Royalty-only systems (MetaComet, EasyRoyaltiesPlus) implement the entire settlement spine and, when scoped to publishing, pay authors under author contracts — i.e., they function as author-management platforms for the money side. The distinguishing test: **author management = author/population registry + relationship surface (attribution, portal, correspondence) + contract, with settlement as the engine; pure royalty management = settlement engine whose population may be any royalty recipients (inventors, licensors) with no author-relationship surface**. Generalized (non-publishing) royalty systems fall on the royalty side. Flag for joint review when Royalty Management Platform is processed.
2. **vs Book Publishing Management** — in the reachable market, author management ships *inside* publishing management suites (Consonance features list; Stison modules). No standalone product marketed specifically as an "Author Management Platform" was identified. Probable **Capability / module-of-suite** packaging rather than a standalone product market; the Type description remains valid as the *function* those modules implement (same posture as the artwork-consignment-management flag).
3. **vs Publishing Metadata Management** — title/bibliographic systems also store contributor records (roles, bios) for the supply chain. Test: remove the contract + settlement loop → what remains is metadata management. Contributor metadata is L1 here, secondary to the money relationship.
4. **vs Publishing Editorial Workflow** — pre-contract acquisition (submissions, pipelines, P&Ls) touches prospective authors (Consonance pipelines), but editorial workflow centers on the work's production lifecycle, not the creator relationship; author management begins at identified-creator records + contract.
5. **vs Creator CRM** — different population (social creators/influencers vs published authors under contract) and different objects (sponsorships, audiences, media kits vs rights grants, royalties, statements). Naming proximity only.
6. **vs Talent Agency Management / literary-agency software** — the agency side exists inside this sample (That's Rights Agents: authors as clients, client portals, incoming revenue capture). Same author records, different operator and commercial logic (commission on inbound royalties vs publisher's payment obligation). Held as an operator variant here; the agency-suite Type belongs to its own leaf.
7. **vs scholarly "author management"** — journal submission/peer-review systems manage author *accounts* for manuscripts, without contracts/royalties. That habitat belongs to Academic Journal Management / Peer Review Platform, not this leaf.
8. **Word-sense guard** — author-facing writing tools (word processors, query trackers, self-publishing service portals) share the word "author" but are author-side products; excluded.

### Historical / market-sample check (per v1.1 §24)

- Older products: dedicated royalty/contract systems have existed since at least the 1980s–90s; before dedicated software, publishers ran the same function with card files, contract files, ledgers, and semi-annual statements. The four-part core (registry, attribution, terms, periodic settlement) predates every implementation detail. ONIX feeds, portals, cloud, AI statement-reading are modern additions → correctly L1/L2, not definition.
- Regional: continental-European publishing practice runs the same contract-and-statement structure (author contracts and periodic royalty/settlement statements are standard across markets); the definition does not depend on Anglo-American ONIX-era tooling.
- Platform-native: the spreadsheet is the acknowledged incumbent (MetaComet explicitly contrasts with spreadsheets/ERP modules) — the *workflow* is stable even where the tool is generic.

## Uncertainties

1. Enterprise/legacy publishing-system tier (Ingenta BiblioSuite and peers) unverified (403 ×2) — the sample's scale range tops out at multinational customers of SaaS products via testimonials, not at legacy on-prem suites. L2 statements about that tier are omitted.
2. Whether all-in-one suites universally offer recipient portals (Consonance not observed either way) — portal treated as common-but-not-universal.
3. Agency-side products' depth (contract terms per client, commission handling) known only from product-page summaries.
4. Precise operational facts (statement frequency defaults, exact escalation syntaxes, price/plan mechanics) not asserted — pages fetched were product pages, not full help centers (except Consonance).
5. Possible standalone "author management" products in markets not reachable by search during this pass (e.g., regional publishing software suites) — none identified; boundary issue #2 phrased as "no standalone product identified in the reachable market."

## Final Synthesis

An Author Management Platform is the publisher-side application that manages the publisher's standing relationship with the people who create its works: it keeps identified records for authors/contributors and their representatives, attributes them to works with roles, records the contractual terms under which each work is published (rights granted, remuneration, payees and splits, advances), and operates the recurring settlement loop — sales in, amounts owed computed per contract, statements issued, payments tracked — increasingly with a self-service portal as the author-facing surface. The function is real, evidence-rich, and stable across decades; in the reachable current market it ships as the author/contracts/royalties layer of publishing management suites and of royalty-specialist systems rather than as a standalone "author management" product, and it sits on a gradient with the Royalty Management Platform sibling leaf. Defining core kept minimal; supply-chain metadata, remuneration mechanics, portals, rights income, and agency-side configurations are standard capabilities; packaging, deployment, operator identity, industry generalization, and regional regimes are variants.
