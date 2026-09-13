# Research Notes — Legal Entity Management

Research date: 2026-09-07
Slug: `legal-entity-management`
Directory location: §10 Enterprise Operations & Administration (line 837). Cross-referenced sibling: Entity Compliance Management (§11), processed 2026-09-06 with a joint-review flag against this leaf.

---

## Research Goal

Understand what a Legal Entity Management application is as a software category: what the managed unit of record is, what "management" concretely consists of (record corpus, structure, people, ownership, lifecycle events), who operates the system, how the record stays current, and — critically — how to hold the boundary against Entity Compliance Management (§11), which shares the same market category ("entity management software") and which flagged a joint review against this leaf.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the managed unit is the **legal entity as a corporate record** — the entity's statutory profile (names, jurisdiction, type, identifiers, registered office/agent, status), its **structure** (entity↔entity ownership/control, person↔entity appointments), its **corporate record** (minute book, resolutions, governance documents), and its **lifecycle** (formation → changes → dissolution) — maintained as the corporate system of record.
- The market sells this under one category name: "entity management software." The sibling research pass recorded: "the market sells one product category serving both directory leaves; working split by emphasis — Entity Compliance Management centers on the obligation/deadline/filing loop and the entity's compliance state; Legal Entity Management on the entity record corpus and structure (org/ownership charts, minute books, entity lifecycle events)." This pass must ratify or revise that split from the record/structure side.
- Likely confusion set:
  - **Entity Compliance Management** (§11) — same products, obligation/deadline emphasis.
  - **Cap Table Management** (§07) — equity of one company vs ownership as one layer of a corporate record portfolio.
  - **Corporate Governance Platform / Board portals** (§11) — board-centric.
  - **Org Chart / Diagramming Application** (§03.05) — charts drawn vs charts derived from the record.
  - **Enterprise Records Management** (§10) — generic records vs legally-qualified entity records.
  - **Master Data Management** (§13) — generic golden records vs domain-specific statutory record.
  - **Registered agent / formation / filing services** — services, not software.
- Unknowns going in: how deep the ownership layer goes before it becomes a cap table; whether lifecycle events are first-class records or just field edits; how much of the compliance loop is core vs bundled.

## Research Questions

1. What does the entity record contain — which fields, identifiers, status concepts?
2. How is corporate structure represented — org/ownership relationships, structure charts? Are charts drawn or derived?
3. How are people handled — directors, officers, secretaries, signatories, PSC/UBO? Are appointments/terminations recorded as events?
4. How deep does the ownership layer go — shareholders, share classes, debt? Where is the line to Cap Table Management?
5. What is the corporate record (minute book) model — documents stored, generated, e-signed, access-controlled?
6. How are entity lifecycle events handled — incorporation, name/address changes, mergers, dissolution? Are they structured records or registry filings?
7. How does the record stay current — manual entry, agency feeds, e-filing integrations, AI extraction?
8. Where does the compliance/deadline machinery sit — core or adjacent? (Boundary vs Entity Compliance Management.)
9. Who uses it and what roles/permissions exist?
10. What would make this leaf an Alias/Variant rather than a distinct Type — or vice versa?

## Representative Products

The market is one category; sampling covers its poles rather than four unrelated categories. Selection: market representation + documentation quality + different philosophies + different customer tiers.

| Product | Philosophy / position | Segment |
|---|---|---|
| Diligent Entities | Enterprise GRC-suite module; AI-assisted "centralized corporate record" | Large enterprise legal ops |
| CSC Entity Management | Service+software incumbent rooted in registered-agent business; "single source of truth for your legal entities" | Enterprise / mid-market legal & compliance |
| Athennian | Cloud-native "Governance Ops™" platform; deep registry e-filing; equity/debt structures | Corporate groups, funds/PE/private markets, professional services |
| Harbor Compliance Entity Manager | Compliance-suite module over secretary-of-state data; SMB/multistate | SMB / multistate operators, nonprofits |

Planned regional SMB sample (Inform Direct, UK company secretarial) unreachable — see Sources. Klea unreachable in the sibling pass (2× transport error) and skipped here per the network rule.

## Sources

| Source | URL | Status |
|---|---|---|
| Diligent Entities product page | https://www.diligent.com/products/entities/ | fetched 2026-09-07 |
| CSC Entity Management page (incl. FAQ) | https://www.cscglobal.com/service/entity-solutions/entity-management/ | fetched 2026-09-07 |
| CSC: 15 Steps to Mastering Corporate Entity Management (blog guide) | https://blog.cscglobal.com/15-steps-to-mastering-corporate-entity-management/ | fetched 2026-09-07 |
| Athennian homepage | https://www.athennian.com/ | fetched 2026-09-07 |
| Athennian capability: Entity & People Records | https://www.athennian.com/capabilities/entity-people-records | fetched 2026-09-07 |
| Athennian capability: Structure Charts (incl. FAQ) | https://www.athennian.com/capabilities/structure-charts | fetched 2026-09-07 |
| Athennian Help Center: Companies House Integration (UK E-Filing) — Tier 1 | https://help.athennian.com/hc/en-us/articles/35026474948507 | fetched 2026-09-07 |
| Harbor Compliance Entity Manager page | https://www.harborcompliance.com/entity-manager-software | fetched 2026-09-07 |
| Inform Direct (planned UK regional sample) | https://www.informdirect.co.uk/ , https://informdirect.co.uk/ | **unreachable** (403 ×2; abandoned per network rule) |
| Klea | https://klea.team/ | unreachable in sibling pass 2026-09-06; not retried |

Evidence layers used below: **A** = directly observed on an official source of one product; **B** = cross-product commonality (≥2 products); **C** = canonical inference from comparison + boundary reasoning.

---

## Product Observations

### Diligent Entities (Diligent)

Key observations (Layer A, product/solution-page level — no Tier-1 help docs reached):

- Positioning: "Manage subsidiaries with a centralized corporate record that's always up to date"; "AI-enhanced entity management software for faster, sharper oversight."
- Central promise: "a fully digitized, fully connected corporate record"; AI "finds the right data, flags compliance issues, and builds reports and visualizations — across every step of your workflow."
- AI assistant over entity data: "Ask a question… and get immediate answers from an AI assistant on ownership, directors, filings and more."
- Self-service distribution of entity data: "Empower your team with a self-service model using permissioned access via Microsoft Teams."
- Compliance deadline block: "Never miss a compliance deadline."
- Case study (Fortive): "centralize 300+ global records, stay audit-ready and visualize complex org structures in real-time."
- Named users: corporate secretaries, legal, tax and compliance teams; senior corporate paralegal quoted.
- Part of Diligent One Platform (boards + GRC suite); nav labels it "Entity & Subsidiary Management."

### CSC Entity Management (CSC)

Key observations (Layer A):

- Positioning: "Gain confidence and control over critical entity compliance"; "simplifies and centralizes the governance of your global entity portfolio… award-winning software with expert support."
- Core record promise: "dynamically keep entity records accurate, complete, and up to date. The result is a single source of truth for your legal entities."
- Feature list (verbatim capabilities):
  - "Maintain sensitive officer and director data"; change transparency via Workday (HCM) integration.
  - "Store, manage, and search minute book and governance documents electronically"; AI document management (bulk imports, automated entity/folder routing, instant summaries).
  - "Generate documents via an intuitive guided workflow and route electronic signature requests with Docusign."
  - "Track ownership, stock, and shareholder information."
  - "Automate the creation of advanced structure charts"; "Visualize potential or pending changes to ownership structures via structure chart modeling."
  - "Establish an unlimited number of custom fields to track unique entity data."
  - "Track Doing Business As (DBA) names, prior names, and merger history."
  - "Manage upcoming compliance due dates, including annual reports, and other critical filings."
  - "Generate strategic reports for auditing, entity tracking, and decision-making purposes."
  - "Enable secure bi-directional integrations… via modern APIs."
  - "Submit electronic filings directly to Companies House and the SEC via prebuilt integrations."
- Automated Compliance Calendar: "Built-in tools auto-manage U.S. and global deadlines like annual reports and key filings."
- Service integration: "Governance data and legal documents auto-sync with CSC services" (registered agent, annual report filing, formation, SPV management are sibling services).
- FAQ (vendor-authored definitions):
  - "Entity management is the process of organizing and maintaining accurate records for a company's legal entities across jurisdictions. It includes tracking ownership structures, officer and director information, compliance deadlines, and governance documentation."
  - "Entity management software… helps legal and compliance teams manage entity data, automate annual compliance requirements, maintain organizational charts, and ensure regulatory filings are completed on time."
  - entity management vs corporate governance: "Entity management focuses on the operational and administrative tasks required to maintain compliance for legal entities—such as tracking filings, maintaining minute books, and updating officer and director information. Corporate governance, by contrast, refers to the broader framework of rules, practices, and processes used to direct and control a company."
  - Platform used for: "centralizing data, automating compliance tasks… integrated features like org chart generation, cap table management, compliance tracking, Workday and DocuSign integrations, and secure document storage."
  - Users: "legal departments, compliance professionals, corporate secretaries, and governance teams… especially those managing complex or multinational entity portfolios."
- 15 Steps guide (vendor discipline guide, describes the entity lifecycle the software serves):
  - Formation chain: define objectives → choose entity type & jurisdiction → registered agent → name availability/reservation → supporting documents (good standing certificates, apostilles) → file formation/qualification → EIN/tax IDs.
  - Foundational documents: "Drafting the entity bylaws and operating agreement; Creating stock and membership certificates; Drafting resolutions for corporate actions, banking resolutions, delegation of authority, and intercompany agreements; Naming officers and directors."
  - Ongoing: "Conduct periodic or annual shareholder and board meetings… Establish a system to record, distribute, and archive corporate activities and documents such as minutes, consents, capital contributions, and dividends"; "An entity management solution can be invaluable in helping you manage and maintain your corporate governance data."
  - Changes: "Changes to your entity's structure must be approved by the board. Decisions should be recorded using resolutions or written consent, and the appropriate filings, such as corporate amendments… should be filed in the entity's jurisdiction."
  - End of life: dissolution/withdrawal steps (tax clearance, voluntary dissolution or withdrawal documents).
  - Standing: "Proper entity management requires careful planning and continued diligence to ensure that entities remain in good standing from formation through dissolution."
  - Record posture: "receiving, indexing, and safeguarding all your corporate entity data… Every time you conduct a corporate transaction with CSC… your entity and jurisdiction data are automatically added to your online portfolio."

### Athennian

Key observations (Layer A; help-center article is Tier 1):

- Positioning: "Governance Ops™ Software for Legal, Tax & Finance Teams"; "Modern Entity Management for Governance Ops."
- Entity & People Records capability page:
  - "Maintain accurate, centralized records for every legal entity, individual and registration, creating a single source of truth across legal, finance, tax and compliance teams."
  - "Create and manage entities: Set up and update legal entities across jurisdictions, with structured data fields for consistent, reportable records."
  - "Track people and roles: Record individuals and link them to multiple appointments across entities, including directors, officers and signatories."
  - "Capture compliance details: Store registration numbers, tax IDs and jurisdiction-specific compliance information in a centralized profile."
  - "Manage addresses and identifiers: Track registered offices, principal places of business and global identifiers such as LEIs or DUNS."
  - "Link relationships across entities: Establish and visualize connections between people and entities across complex organizational structures."
  - "Store KYC and onboarding data… to support due diligence, onboarding and internal reviews."
  - "Search and filter records… using custom tags and filters, or full-text search across structured fields."
  - "Generate reports and exports: Produce filtered reports of entities, appointments and individuals for audits, filings or internal review."
- Structure Charts capability page (+ FAQ):
  - "Generate dynamic, real-time visualizations of ownership, governance and financing relationships across entities."
  - "Create dynamic org charts: Generate ownership and relationship charts that reflect the most up-to-date entity, equity and debt data."
  - "Visualize governance relationships: Map appointments, control roles and D&O relationships across subsidiaries and jurisdictions."
  - "Display equity and debt positions: Show layered capital structures, shareholder breakdowns and funding flows at a glance."
  - Filter by region, entity type, ownership percentage, custom tags; export as PDF/image for "board meetings, audits or transaction planning."
  - FAQ: charts are generated from live data — "Any changes to appointments, equity positions or entity records are automatically incorporated into the visualizations"; "Unlike static visuals built in PowerPoint or Visio, Athennian's charts are automatically generated from verified data and require no manual updates."
  - Deal use: "They support restructuring, M&A due diligence and financing scenarios."
- Other capabilities: Equity & Debt Structures ("Manage cap tables, equity and debt transactions, records and structure"); Controls & Governance ("granular permissions, audit trails and custom fields to ensure data integrity"); Document Management ("Store, edit and automate templates, use electronic signatures, and control access"); Appointments/D&O ("Record, link and automate any appointment such as director, officer, power of attorney or signing authority"); Tasks & Reports ("Track compliance dates and significant events"); Athennian AI ("automate entity lifecycle changes"; "Continuously reconcile records, validate ownership data, maintain minute books and support inbound KYC and audit requests").
- Customer evidence: virtual minute book ("pull a folder, download everything and share"); time-limited outside-counsel access grants; "all entity data into one platform… who's the authorized signatory or the parent entity… It's all in Athennian."
- Companies House Integration (UK E-Filing) — **Tier 1**:
  - "Submit UK filings directly to Companies House with real-time tracking"; "Automated Task Updates: The UI adapts dynamically to ensure all required fields are met"; "Form Previews: Pre-coded templates mirror official Companies House documents."
  - Requires a Companies House credit ("fee-bearing") account; credentials entered as Companies House Presenter ID + Authentication Code.
  - Supported filings (the lifecycle as structured, form-coded events): Incorporation IN01; Confirmation statement CS01; Appointments AP01–AP04 (director, corporate director, secretary, corporate secretary); Terminations TM01–TM02; Change of name NM01 (company and LLP); Person of Significant Control notices PSC01/02/04/07 (individual, relevant legal entity, change of details, ceasing); Change of registered office AD01. Filing statuses tracked; multiple Companies House credential sets supported; director identity-verification codes supported.
- Audiences: corporate groups, private equity & funds, private markets (funds, SPVs, portfolio entities), professional services, family offices; teams: legal, treasury, finance, tax.

### Harbor Compliance (Entity Manager within the Compliance Suite)

Key observations (Layer A):

- Positioning: "Instant clarity on your registrations nationwide"; "Provides complete visibility into entity and compliance status"; "Automates annual report and compliance tracking."
- Value bullets: "Maintain good standing and avoid late fees and penalties"; "Save time submitting corporate filings and annual reports"; "Get instant clarity on where your entities are registered"; "Ensure continuity through staff and vendor changes."
- Data visualization: interactive map of state registrations (per-state registration counts).
- Compliance Core™ database: "automatically set annual report due dates and send notifications, wherever available… continually maintained."
- Agency integration: "integrated with the secretary of state databases, wherever available. Registrations are automatically populated… along with their registration numbers and publicly available information" (addresses, registered agent on file).
- Suite siblings: License Manager, Records Manager, Tax Manager; services catalog: annual report, foreign qualification, registered agent, BOI reporting, reinstatement, dissolution/withdrawal, certificates of good standing, DBA, etc.
- Segment: SMB/multistate operators, nonprofits; engagement models SaaS / managed services / hybrid.

---

## Cross-product Comparison

| Dimension | Diligent Entities | CSC Entity Management | Athennian | Harbor Entity Manager |
|---|---|---|---|---|
| Managed unit | subsidiaries ("centralized corporate record") | legal entities across jurisdictions ("single source of truth") | entities, individuals, registrations (records per entity/person) | entity registrations per state |
| Entity record depth | entity records, org structures, AI Q&A over data | officers/directors, ownership/stock/shareholders, DBA/prior names, merger history, custom fields | entity details, addresses, identifiers (LEI/DUNS), registrations, tax IDs, KYC | registration numbers, addresses, registered agent, status (from agency feeds) |
| Structure representation | "visualize complex org structures in real-time" | automated structure charts + modeling of pending ownership changes | real-time structure charts derived from live entity/equity/debt data; filterable, exportable | interactive map of registrations (geo, not ownership) |
| People / appointments | directors via AI answers; permissioned access | officer/director data + change transparency (Workday feed) | person records linked across entities; appointments incl. POA/signing authority; D&O mapping | registered agent on file |
| Ownership layer | AI answers on ownership | ownership, stock, shareholder info; "cap table management" named in FAQ | cap tables, equity & debt transactions, shareholder breakdowns | not observed (BOI as sibling service) |
| Corporate record / documents | "every entity, filing, and board record… audit-ready hub" | minute book & governance documents; AI routing/summaries; guided generation; DocuSign | virtual minute book; templates, e-signature, access control; AI-staged document filing | Records Manager (suite sibling) |
| Lifecycle events | not detailed on fetched pages | amendments/changes described in lifecycle guide; e-filing to Companies House/SEC | structured lifecycle filings: incorporation, appointments, terminations, name change, PSC, registered office (UK e-filing, Tier 1) | registration lifecycle via services (formation, amendment, dissolution) |
| Record currency mechanism | AI extraction/automation | manual + CSC service auto-sync + APIs | manual + AI workflows + registry e-filing + government-source onboarding | secretary-of-state inbound feeds |
| Compliance machinery | "Never miss a compliance deadline" | compliance due dates + Automated Compliance Calendar | Tasks & Reports track compliance dates | auto-set annual report due dates + notifications |
| Roles & audit | permissioned self-service (Teams) | enterprise-grade security; unlimited users | granular permissions, audit trails, custom fields, time-limited external access | unlimited users incl. accountants/counsel |
| Portfolio surface | cross-entity reports/visualizations | global entity portfolio governance | multi-entity platform, portfolio views | nationwide registration map |
| Segment | enterprise | enterprise/mid-market | corporate groups, funds/SPVs, professional services | SMB/multistate, nonprofits |

Layer B (cross-product commonality, ≥3 of 4): the entity register as the corporate system of record ("single source of truth" language in 3 of 4); officer/director records; ownership/shareholder records; structure visualization; minute book / governance document management; document generation + e-signature; permissions + audit trail; compliance dates tracked per entity; integrations (HR, e-signature, registries, agency feeds); reporting/exports for audits and transactions.

Layer C (canonical inference): the Type is the **corporate system of record over a portfolio of legal entities** — entities as jurisdiction-qualified records, their ownership/control and people/role structure held as data, their official corporate record (minute book class) held as documents, all maintained over time through recorded changes — with structure charts as the signature derived surface and good standing as the state the record protects.

---

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product stops being a Legal Entity Management application:

1. **The legal entity record** — a persistent, identified record for each legally constituted entity in the portfolio: name (incl. prior/DBA names where tracked), entity type, jurisdiction(s) of formation/qualification, registration identifiers, registered office/agent, status. The entity — not the document, not the filing, not the task — is the anchor object. Remove → generic records/charting tooling.
2. **The structure layer as data** — relationships held as queryable records, not only as drawings: entity↔entity (ownership, control, intercompany) and person↔entity (appointments, roles, signing authority). This is what "management" adds over a records room; it is what structure charts render. Remove → a corporate document repository or a filing tracker.
3. **The corporate record corpus bound to the entity** — the entity's official governance documents (minute book class: bylaws/operating agreements, resolutions, minutes, consents, certificates) organized under the entity record, with controlled access. Remove → a bare org-chart tool over entity data.
4. **Maintained over time through recorded changes** — the record and structure are kept current through recorded, attributable changes/events (appointments/terminations with effective dates, name/address changes, ownership changes, status changes such as merger or dissolution) rather than silent overwrites or static snapshots. Remove → static org chart + file share; not a management system.

Test: remove (1) → not entity-anchored; remove (2) → document repository; remove (3) → diagramming tool; remove (4) → snapshot, not system of record. All four jointly are load-bearing; any three without the fourth collapse into an adjacent Type.

Not in L0 (deliberately): compliance/deadline calendars and obligation loops (the sibling Type's defining loop — common bundled capability here); structure-chart UIs (a rendering of the structure layer; historical products served it as statutory registers and typed schedules); e-filing/agency feeds; equity-transaction depth; AI; KYC/UBO modules; portfolio dashboards.

### L1 — Common Mature Structure

Present in most mature products, not definitional:

- entity profile depth: registered office/agent, formation dates, DBA/prior names, merger history, custom fields
- people layer: directors, officers, secretaries, signatories, POAs; appointment/termination tracking; person records linked across many entities; PSC/UBO and KYC records where regimes require
- ownership layer: shareholders/members, share classes, stock, holdings; cap-table-like views; sometimes debt/loans
- structure charts: auto-generated from live records, filterable (jurisdiction, ownership %, entity type), exportable, sometimes modeling pending/proposed changes
- document management: templates, guided generation, e-signature routing, entity/folder routing of uploaded documents, search over the corpus
- compliance dates tracked per entity (annual reports and similar periodic obligations) with reminders — common, and the point where this Type borders Entity Compliance Management
- search/filter across entities and people; reports and exports for audits, filings, boards, transactions
- roles/granular permissions, audit trails, time-limited external access (counsel, auditors)
- integrations: HR (officer changes), e-signature, government registries (outbound e-filing), agency databases (inbound registration data), sibling services (registered agent, formation)
- onboarding/migration from spreadsheets with verification (sometimes against government-source data)

### L2 — Variant / Optional Structure

- **Filing execution model**: in-product registry e-filing (Athennian–Companies House; CSC–Companies House/SEC) vs managed-service filing vs tracking-only with external agents. Biggest philosophical split in the category.
- **Scope breadth**: entity-only vs +equity/debt (Athennian) vs +board/subsidiary-boards (Diligent suite) vs +licenses/tax (Harbor suite).
- **Segment/tenancy**: single-organization in-house legal ops vs corporate service providers/fiduciaries running entities for many clients vs funds/SPV-heavy private markets.
- **Regional regime**: US multistate (secretary-of-state registrations, foreign qualification, good standing) vs UK (Companies House, PSC, confirmation statement) vs multi-jurisdiction global portfolios.
- **Service component**: software-only vs software+expert services vs managed-services-first.
- **AI depth**: extraction/data entry, document staging, Q&A over the record, agentic entity changes, AI chart generation.
- **Deployment**: multi-tenant SaaS standard; security posture (PII flags, encryption, SOC 2 claims) varies.

### L3 — Vendor-specific (research notes only)

- Diligent: Microsoft Teams permissioned self-service; Diligent One Platform bundling; ROI figures (318% ROI, 70% time, 90% cost — marketing, not used as evidence).
- CSC: Workday HCM integration; DocuSign routing; flat-fee unlimited users; NYLJ/CLOC award claims; "160,000+ licensing jurisdictions" figure in the blog (marketing context, not generalized).
- Athennian: "Governance Ops™" branding; virtual minute book; time-limited outside-counsel access; Companies House Presenter ID/Authentication Code credentialing; multiple credential sets; PwC UK collaboration; Loans/Debt module.
- Harbor: Compliance Core™ database; interactive registration map; Harbor Compliance Score; free-trial "entity status health check" offer.

## Vendor-specific Findings

See L3. None promoted into the canonical model. The Workday integration (CSC), Teams access (Diligent), and time-limited counsel access (Athennian) are treated as instances of the generic L1 integration/permission layers.

## Rejected Findings

- "Entity management = compliance calendar software" — rejected as the definition: the calendar is one bundled capability (present in all four samples but as a block, not the organizing structure); making it definitional would erase the record/structure corpus that all four products equally center, and would duplicate Entity Compliance Management exactly.
- "Structure charts are the core" — rejected: charts are the derived, rendered surface of the structure layer; older/regional realizations (statutory registers, typed schedules) satisfy the Type without chart UIs.
- "Ownership/cap-table depth is definitional" — rejected: CSC and Athennian carry it; Diligent evidences only AI answers on ownership; Harbor effectively none (BOI as a sibling service). Ownership is one attribute layer, not the spine.
- "This leaf is an Alias of Entity Compliance Management (same products, same category)" — rejected as pure alias, but recorded as the category's central tension: one market, two emphases. The two leaves are kept distinct by their defining loops (see Boundary Findings 1); residual near-duplicate risk flagged in STATUS.md.

## Boundary Findings

1. **vs Entity Compliance Management (§11) — the flagged joint review, resolved from this side.** The market category is one ("entity management software"); the same products (Diligent Entities, CSC, Athennian) serve both leaves, and CSC's own definition of entity management spans both ("tracking ownership structures, officer and director information, compliance deadlines, and governance documentation"). Ratified split by defining loop:
   - **Legal Entity Management** (this leaf): the defining core is the **entity record corpus + structure maintained over time** (L0 above). Remove the obligation/deadline/filing loop entirely and the product is still fully recognizable.
   - **Entity Compliance Management** (§11): the defining core is the **obligation → deadline → tracked completion → recorded evidence loop** and the entity's compliance state (good standing), per its research notes. Remove the record-corpus/structure depth and it is still fully recognizable.
   - Each side's L0 makes the other's defining loop a common (L1) capability, not a defining one. Verdict: keep both leaves as two emphases of one category; residual near-duplicate risk recorded in STATUS.md for taxonomy review.
2. **vs Cap Table Management (§07)** — cap-table products center on one company's equity transactions and dilution math; here ownership is one attribute layer of a portfolio record, and CSC's FAQ literally lists "cap table management" as an integrated feature — supporting "feature, not Type."
3. **vs Corporate Governance Platform / board portals (§11)** — board-centric surfaces (meetings, packs, director portals) vs entity-statutory surfaces. CSC's own FAQ draws the line: entity management is "operational and administrative… to maintain compliance for legal entities"; corporate governance is "the broader framework… to direct and control a company."
4. **vs Org Chart / Diagramming Application (§03.05)** — charting tools let users draw diagrams; here charts are derived projections of maintained records ("automatically generated from verified data and require no manual updates" — Athennian FAQ). Remove the record and structure layer and only a drawing tool remains.
5. **vs Enterprise Records Management (§10) / generic document management** — generic records corpora vs the legally-qualified entity record with jurisdiction-driven structure; here documents are bound to entities and follow the entity's lifecycle.
6. **vs Master Data Management (§13)** — MDM governs golden records generically; this Type is the domain-specific corporate/statutory record with legal semantics (entity types, registries, appointments, good standing).
7. **vs ERP (§10)** — ERP carries a legal-entity dimension of financial operations (company codes, ledgers); this Type's object is the statutory corporate record, not financial transactions.
8. **vs registered agent / formation / filing services** — human-executed services vs the software that tracks, prepares, evidences. Vendors bundle both (CSC, Harbor); the software Type's deliverable is the maintained record, not the filing act.
9. **"Remove what to become another Type" tests**: remove the entity anchor → generic diagramming/records/MDM; remove the structure layer → corporate document repository; remove the record corpus → org-chart tool; remove the maintained-over-time loop → static snapshot; center the obligation/deadline loop → Entity Compliance Management; remove portfolio scale → single-entity secretarial record-keeping (a Variant, not a separate Type — see historical check).

## Historical / Market-Sample Check

Asked: would older, regional, platform-native or differently positioned products still fit? Single-jurisdiction corporate-secretarial record-keeping as practiced long before cloud/AI — statutory registers of members/directors, share register and certificates, minute book, board resolutions, annual return tracking for one company or a small set — satisfies all four L0 properties: entity record (the company register), structure (registers of members and officers), record corpus (minute book), maintained over time (recorded changes: appointments, allotments, name/address changes). CSC's vendor discipline guide describes the same lifecycle discipline from formation through dissolution independent of any modern UI. What fails the historical filter as definitional: structure-chart canvases, agency data feeds, e-filing APIs, KYC/UBO modules, AI, portfolio dashboards — all L1/L2. The definition is not overfit to the current AI-era, multi-jurisdiction enterprise implementation. Caveat: the planned regional SMB software sample (Inform Direct) was unreachable, so the historical/regional check rests on the lifecycle guide plus canonical inference, not on a directly observed legacy product.

## Uncertainties

- Diligent's operational depth (record fields, task model, e-filing support) remains product-page-level only; no Tier-1 help documentation reached in either this pass or the sibling pass.
- Inform Direct unreachable (403 ×2) — the UK SMB/accountant-tier company-secretarial pole is unobserved first-hand; Klea also unreachable. Sample skews enterprise/mid-market.
- Exact per-jurisdiction record schemas (which fields each registry requires) are not published publicly; field lists above are inferred from product pages, not registry specifications.
- Whether "good standing" is a first-class tracked state in every product is unclear (explicit in Harbor; implied in CSC via certificates/reinstatement services; not observed in Diligent/Athennian pages).
- The boundary between "ownership records as attribute layer" and "cap table management" is drawn by emphasis; no neutral benchmark exists. Single-source observations (Athennian debt/loans module) kept product-specific.
- The SEC e-filing integration (CSC) was not further verified (which SEC form classes); kept as observed capability without detail.

## Final Synthesis

A Legal Entity Management application is the corporate/legal team's **system of record for a portfolio of legal entities**. Its world has four inseparable parts: (1) the **entity record** — each legal entity as an identified, jurisdiction-qualified record (names incl. prior/DBA, type, jurisdictions, registration identifiers, registered office/agent, status); (2) the **structure layer held as data** — ownership/control links between entities and appointment/role links between people and entities, queryable and renderable; (3) the **corporate record corpus** — the minute-book class of official governance documents bound to each entity, with controlled access, template-driven generation and e-signature; and (4) the **maintained-over-time loop** — changes recorded as attributable events (appointments, terminations, name/address changes, ownership changes, status changes such as merger or dissolution), many executed or evidenced through registry filings, so that structure charts, reports and audit answers are always projections of a current record.

Around this core, mature products add officer/director and PSC/UBO/KYC records, shareholder and securities views, auto-generated filterable structure charts, compliance-date tracking, search/reporting/exports, granular permissions and audit trails, and integrations that keep the record current (HR feeds, agency databases, registry e-filing, e-signature). Products diverge most on who executes filings (the software via registry APIs, a managed service, or the user's own agents), on scope breadth (entity-only vs +equity/debt vs +board vs +licenses/tax), on tenancy (in-house vs corporate service providers vs funds/SPVs), and on regional regime (US multistate vs UK vs global).

The Type's boundary is held by the managed unit and the defining loop: if the records are not legal entities with their statutory structure and corporate record, it is not this Type; if the obligation/deadline/filing loop is the center and the record corpus/structure depth recedes, it is Entity Compliance Management; if charts are drawn rather than derived, it is diagramming; if documents are unbound from entities, it is generic records management.
