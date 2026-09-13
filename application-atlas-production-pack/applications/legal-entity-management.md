# Legal Entity Management

## Overview

A **Legal Entity Management** application is the corporate system of record for an organization's portfolio of legal entities. It maintains, for each entity — subsidiary, holding company, joint venture, SPV, branch, or affiliated vehicle — an identified, jurisdiction-qualified record: its names (current, prior, and doing-business-as), entity type, jurisdictions of formation and qualification, registration identifiers, registered office and agent, and status. Around each record it holds the two things that make an entity governable: its **structure** (who owns and controls it, and which people hold which roles in it) and its **corporate record** (the official governance documents — bylaws, resolutions, minutes, certificates — that evidence its decisions). The record is maintained over time through recorded changes rather than treated as a static snapshot.

The problem it solves is concrete: organizations that operate many entities across jurisdictions accumulate entity truth in spreadsheets, shared drives, and individual memories. When a lender, auditor, regulator, or acquirer asks "who are the directors of this entity, who owns it, and where is its registered office?", no one can answer reliably. This application makes the answer a lookup, not a project, and makes every subsequent change — an appointment, a name change, a share transfer, a merger — a recorded event that keeps the record true.

Its boundary: it is a **record-and-structure** system, not a workflow-for-filings system (though most products also track filing deadlines), not a board-meeting product, and not a diagramming tool. The market mostly sells it under the category name "entity management software."

## Users & Context

Primary users are the people accountable for the correctness of the corporate record:

- **Corporate secretary / governance lead** — owns the record: ensures entity details, appointments, and the minute book are current and defensible.
- **Corporate paralegal / entity administrator** — does the day-to-day work: enters changes, generates resolutions and minutes, files with registries, assembles documents for requests.
- **Legal operations / counsel** — consumes the record: answers ownership and authority questions, prepares for transactions, manages outside counsel access to specific data.

Secondary users:

- **Tax, finance, and treasury teams** — need entity, ownership, and registration data for filings, bank account opening, and structuring work.
- **Compliance officers** — need officer, beneficial-ownership, and registration data for regulatory disclosures and know-your-customer responses.
- **Corporate service providers and fiduciary administrators** — run the same kind of record, but for many client companies at once.

The characteristic setting is an organization with more than a handful of entities — commonly dozens to hundreds across multiple jurisdictions — where a small team must keep every record current and produce evidence on demand: for audits, board meetings, financing, M&A due diligence, and regulatory inquiries.

## Core Model

### The defining core

```text
Legal Entity Record  (identified, jurisdiction-qualified, persistent)
├── Structure layer  (held as data)
│     ├── entity ↔ entity:  ownership / control / intercompany relationships
│     └── person ↔ entity:  appointments / roles / signing authority
├── Corporate record corpus  (documents bound to the entity)
│     └── minute book:  bylaws · resolutions · minutes · consents · certificates
└── Recorded changes  (the maintenance loop)
      └── appointment, termination, name/address change, ownership change,
          amendment, merger, dissolution — each a recorded, attributable event
```

Four properties. If any one is removed, the product stops being recognizable as this Type:

- **The entity record.** Each legal entity is a persistent, identified record carrying at minimum: name (with prior/DBA names where tracked), entity type, jurisdiction of formation (and foreign qualifications where applicable), registration and tax identifiers, registered office and agent, and status. The entity — not the document, not the filing, not the task — is the anchor object to which everything else attaches.
- **The structure layer as data.** Relationships are held as queryable records, not only as drawings: which entity owns or controls which (with percentages where applicable), and which person holds which role (director, officer, secretary, signatory, power of attorney) in which entity. This layer is what distinguishes an entity-management system from a records room: it can answer structural questions directly, and it is what structure charts render.
- **The corporate record corpus.** Each entity carries its official governance documents: constitutive documents, bylaws or operating agreements, director and shareholder resolutions, meeting minutes, written consents, share or membership certificates, and filing confirmations. These documents are organized under the entity, access-controlled, and increasingly generated from templates so that the document says what the data says.
- **Maintained over time through recorded changes.** The record is kept current through recorded, attributable events — an appointment with an effective date, a registered-office change, a share transfer, a dissolution — rather than silent overwrites. The value of the system lies precisely in this: the record reflects the entity as it is *now*, with a trail of how it got there.

### What mature products commonly add

These capabilities are widespread in current products but do not define the Type — older and narrower corporate-record systems manage entities without them:

- **Deeper profile data** — merger history, custom fields, principal places of business, global identifiers (e.g., LEI), jurisdiction-specific compliance details.
- **People and beneficial-ownership records** — person records linked across many entities; know-your-customer data; persons of significant control / ultimate beneficial owners where regimes require.
- **Ownership and securities views** — shareholders, share classes, holdings; some products extend to cap-table-like views, debt, and loans.
- **Structure charts** — diagrams generated from the live records, filterable by jurisdiction, ownership threshold, or entity type, exportable for boards and transactions, sometimes with modeling of proposed changes.
- **Compliance-date tracking** — annual report and similar periodic obligations tracked per entity, with reminders. This is the capability where the Type borders Entity Compliance Management (see Related Application Types).
- **Document tooling** — template-based generation, e-signature routing, bulk import with automated entity/folder routing, search across the corpus.
- **Search, reporting, exports** — cross-entity search and filtered reports for audits, filings, boards, and transactions.
- **Access governance** — granular permissions, audit trails, time-limited access for outside counsel or auditors.
- **Integrations that keep the record current** — HR systems (officer changes), e-signature, government registries (outbound e-filing), agency databases (inbound registration data), and sibling services (registered agent, formation).

### One structure, many implementations

The core is written conceptually. Implementations vary:

```text
Concept:      entity record
Realizations: structured profile forms per jurisdiction · agency-populated
              registration records · AI-extracted profiles from source documents

Concept:      structure layer
Realizations: relationship fields on records · dedicated ownership/registers
              modules · auto-generated charts as the visible surface

Concept:      corporate record corpus
Realizations: "minute book" as a virtual folder per entity · document libraries
              with entity routing · generated-and-e-signed document sets

Concept:      recorded changes
Realizations: in-product registry e-filing with status tracking · filings
              executed by a managed service and synced back · changes recorded
              manually with documents attached as evidence
```

A reader who has only seen one implementation — say, an AI-era SaaS platform with live charts — should still recognize a plain corporate-records system with statutory registers and a minute book as the same Type.

## How It Works

### Build the record

```text
Collect existing entity truth (spreadsheets, filing documents, agency data)
→ create a record per entity (type, jurisdiction, identifiers, people, structure)
→ verify against official sources where possible
→ attach founding documents to the record
→ the portfolio becomes a single source of truth
```

Onboarding is a first-class activity: vendors commonly assist with migration and verification, and some products populate registrations automatically from secretary-of-state databases or government-source data.

### Record a corporate change (the central loop)

```text
A corporate event occurs (appoint a director, change the name,
transfer shares, move the registered office, plan a merger)
→ record the change on the entity (with effective date and the people involved)
→ generate the required documentation (resolution, written consent, notice)
→ route for approval / e-signature
→ file with the registry — from within the product where e-filing is supported,
  or through the organization's agent or filing service
→ record the outcome (filing confirmation, updated certificate) on the record
→ charts, reports, and answers now reflect the change
```

This loop is the daily work of the application. Whether step five is executed by the software (direct registry e-filing with real-time status), by the vendor as a service, or by the user's own agents varies by product — but the record of the change and its evidence always lands on the entity.

### Answer questions and produce outputs

```text
A request arrives (audit, board meeting, financing, M&A diligence, KYC)
→ search or filter the register; open the entity record
→ read structure directly, or render/export a structure chart
→ pull the relevant documents from the minute book
→ produce a report or export scoped to the request
```

The defining promise of the Type shows here: answers come from maintained data rather than from document archaeology. Customer-facing evidence across the researched products repeats one theme — a transaction or audit request that previously required assembling facts from multiple document sets becomes a lookup plus an export.

### Keep the record current

Between deliberate changes, mature products keep records aligned through integrations: agency database feeds that surface registration facts, HR-system sync for officer changes in some products, and service sync (registered agent, annual report filing) that writes completed filings back onto the record. Where the product itself files electronically, submission statuses flow back automatically.

### Core vs common vs optional

- **Defining core** — entity register; structure held as data; corporate record corpus per entity; recorded changes maintaining the record over time.
- **Common mature capabilities** — profile depth (DBA/prior names, custom fields), people/beneficial-ownership records, ownership and securities views, derived structure charts, compliance-date tracking, document generation and e-signature, reporting/exports, permissions and audit trails, currency-keeping integrations.
- **Variant / optional** — who executes filings (in-product e-filing vs managed service vs external agents), scope extensions (equity and debt; board and subsidiary governance; licenses and tax), tenancy model (in-house team vs corporate service provider vs fund/SPV administrator), regional regime (US multistate vs UK vs global), AI assistance (extraction, Q&A over the record, staged document filing, agentic changes).

## Interfaces

The following surfaces are described conceptually; layouts and names vary by product.

### Entity register (portfolio home)

The entry surface for the whole portfolio.

- lists entities with type, jurisdiction, status, and key identifiers
- filter and search across the register (by name, jurisdiction, ownership, tags)
- primary actions: open an entity, add an entity, build filtered views

### Entity profile (the record)

The record for one entity — the heart of the application.

- identity block (names incl. prior/DBA, type, jurisdiction(s), registration and tax identifiers, formation date, status), registered office and agent
- structure panels: parent/owners, subsidiaries, appointments, shareholdings
- links into the entity's documents, filings, tasks, and compliance dates
- primary actions: edit details, record a change, generate a document, upload to the record

### Structure chart view

The rendered structure layer.

- ownership/hierarchy charts generated from the records (with percentages where applicable), sometimes including governance-role overlays and debt
- filter by jurisdiction, ownership threshold, entity type; export as image/PDF
- primary actions: generate, filter, export; in some products, model a proposed change before it happens

### People & appointments

The person-side of the structure layer.

- person records linked to appointments across many entities; roles incl. director, officer, secretary, signatory, power of attorney; beneficial-ownership records where tracked
- primary actions: record an appointment or termination (with effective date), view a person's entity footprint

### Minute book / documents

The corporate record corpus of one entity.

- organized folders or virtual minute books: constitutive documents, bylaws, resolutions, minutes, certificates, filing confirmations
- template-based document generation; e-signature routing; access control; full-corpus search
- primary actions: generate, upload, sign, download, restrict access (in some products, an entity's entire minute book can be downloaded as one bundle)

### Compliance dates view

Where periodic obligations are tracked (common capability).

- per-entity upcoming filings and due dates, calendar or list views, reminders and overdue indicators
- primary actions: review, assign, complete, record the filing outcome

### Reports & exports

- filtered reports of entities, appointments, and ownership for audits, filings, boards, and transactions; exportable bundles

### Administration

- roles and granular permissions, audit trail, custom fields, integration settings (registries, e-signature, HR), time-limited external access grants

## Important Rules / Behaviors

### The record is a system of record, not a snapshot

Changes are recorded as attributable events with effective dates — appointments, terminations, transfers — and the record's current state is derived from that history. This is what makes the data trustworthy enough to answer external questions, and what the audit trail protects.

### Charts are derived, never drawn

Structure charts are projections of the underlying records; a change to any record flows into every chart. The contrast with manually maintained org charts (slide decks that go stale) is a recurring selling point of the category — and the reason the structure layer must live as data.

### Jurisdiction drives the record

What an entity record must contain, which changes are possible, and which filings a change triggers are all determined by the entity's jurisdiction and type. Products encode this: forms and required fields adapt to jurisdiction, and registry filings follow jurisdiction-specific formats. An entity is never just a name — it is always an entity *of somewhere, of some type*.

### Documents and data are two layers of one record

A recorded change is normally evidenced by a document (the resolution authorizing it) and may produce another (the registry confirmation). Document generation from the record's own data keeps the two layers aligned; filing confirmations are attached back to the entity.

### Sensitive data is access-controlled

Officer and director details, personal addresses, and beneficial-ownership data are sensitive by nature. Granular permissions and careful handling of personal data are standard expectations, not extras, and some products add finer controls such as flags on personal data or time-limited access grants for outside counsel and auditors.

### The record ultimately answers to registries

The application's record is maintained in parallel with official registers. Where the product files electronically, the record and the register converge; where filings happen through agents, the record waits for confirmation. Either way, the register's version of the truth is the external benchmark the record aims to match.

### Good standing is the state the record protects

A current record is the precondition for demonstrating that an entity is validly existing, properly officered, and filig-current — the state usually summarized as good standing, and the one whose loss (missed filings, lapsed registrations) the discipline exists to prevent. How explicitly each product tracks standing as a first-class state varies.

## Variants

- **By filing execution model** — the biggest philosophical split: products that file directly to registries via APIs (with real-time status), products where a vendor service performs filings and syncs results back, and products that track only, leaving execution to the organization's agents.
- **By scope breadth** — entity-record-only tools; products adding equity, debt, and cap-table views; suite members adding board/subsidiary governance; compliance suites adding license and tax management alongside the entity module.
- **By tenancy and segment** — in-house legal teams of corporate groups; funds and private-market administrators running many SPVs and portfolio entities; corporate service providers running entities for many clients; small multistate operators and nonprofits tracking registrations in a few US states.
- **By regional regime** — US multistate practice (secretary-of-state registrations, foreign qualification, registered agents, annual reports, good standing); UK practice (Companies House filings, confirmation statements, persons of significant control); global multi-jurisdiction portfolios.
- **By service component** — software-only vs software-plus-expert-services vs managed-services-first offerings.
- **The single-entity tradition** — one company (or a small set) maintaining its statutory registers and minute book, with or without portfolio dashboards. This is the historically older and still widespread shape of the Type; the portfolio view is a scaling of the same core, not a different one.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Entity Compliance Management | closest neighbor; same market category. Its defining loop is the compliance obligation: deadline → preparation → filing → recorded evidence → compliance state. Here the defining structure is the record corpus and the maintained entity/structure data; deadline tracking is a common capability, not the spine. Remove either loop and the other product remains fully recognizable. |
| Cap Table Management | centers on one company's equity instruments, transactions, and dilution; here ownership is one attribute layer of a portfolio record, often surfaced as views rather than transaction machinery |
| Corporate Governance Platform / Board portal | board-centric: meetings, materials, director communication; entity management is the statutory record beneath the boards, and products that bundle both keep the surfaces distinct |
| Diagramming / Org Chart Application | lets users draw diagrams; here charts are generated from maintained records — remove the record and only a drawing tool remains |
| Enterprise Records Management | manages document corpora generically; here documents are bound to legally-qualified entities and follow the entity's statutory lifecycle |
| Master Data Management | governs golden records across domains generically; this Type is the domain-specific corporate record with statutory semantics |
| ERP | carries a legal-entity dimension of financial operations (company codes, ledgers); the corporate/statutory record and its governance documents are not ERP objects |
| Registered agent / formation / filing services | human-executed services (accepting service of process, forming entities, filing documents); frequently bundled with this software, but the software's deliverable is the maintained record |
| Legal Operations Platform | broader legal-department tooling (matters, spend, contracts); the entity record is one slice |

The boundary that matters most is with Entity Compliance Management: the market largely sells one product category, and the two leaves are best understood as two emphases of it — the record-and-structure emphasis (this Type) and the obligation-and-deadline emphasis. A buyer choosing between vendors is usually choosing one system that must do both; a taxonomy that keeps the leaves distinct should do so on the defining loops, not on feature checklists.

## Representative Products

- **Diligent Entities** — enterprise GRC-suite module; AI-assisted centralized corporate record
- **CSC Entity Management** — service+software incumbent rooted in registered-agent services; single source of truth for legal entities
- **Athennian** — cloud-native platform with deep registry e-filing and equity/debt structures; corporate groups, funds and SPVs
- **Harbor Compliance (Entity Manager)** — compliance-suite module over secretary-of-state data; SMB and multistate operators

The core model was checked against the category's breadth: the record-corpus core is shared by all four, while charts, e-filing, equity depth, and AI appear as differing implementations. The single-entity corporate-secretarial tradition (statutory registers + minute book, pre-cloud) fits the core without any modern additions.

## Sources

Research date: **2026-09-07**

Primary vendor sources:

- Diligent — Diligent Entities product page: https://www.diligent.com/products/entities/
- CSC — Entity Management page and FAQ: https://www.cscglobal.com/service/entity-solutions/entity-management/
- CSC — "15 Steps to Mastering Corporate Entity Management" (entity-lifecycle guide): https://blog.cscglobal.com/15-steps-to-mastering-corporate-entity-management/
- Athennian — homepage and capability pages (Entity & People Records; Structure Charts): https://www.athennian.com/ , https://www.athennian.com/capabilities/entity-people-records , https://www.athennian.com/capabilities/structure-charts
- Athennian Help Center — Companies House Integration (UK E-Filing): https://help.athennian.com/hc/en-us/articles/35026474948507
- Harbor Compliance — Entity Manager page: https://www.harborcompliance.com/entity-manager-software

> Sourcing limitations: a planned regional SMB sample (Inform Direct, UK) and the pure-play Klea were unreachable and are not characterized here. Diligent's evidence is product-page level; no Tier-1 help documentation for it was reachable. Per-entity registry field schemas are not publicly specified; field observations come from product pages. Precise operational parameters (exact field lists per jurisdiction, numeric limits, plan-gated capabilities) are intentionally not asserted in this document.
