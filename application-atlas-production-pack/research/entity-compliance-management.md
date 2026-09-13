# Research Notes — Entity Compliance Management

Research date: 2026-09-06
Slug: `entity-compliance-management`
Directory location: §11 Legal, Risk, Compliance & Governance (sibling of Legal Entity Management in §10, Compliance Management Platform, Corporate Governance Platform)

---

## Research Goal

Understand what an Entity Compliance Management application actually is as a software category: what the managed unit is, what "compliance" concretely consists of for legal entities, how obligations are tracked and completed, who operates the system, and where the boundary lies against Legal Entity Management, generic Compliance Management Platforms, board governance platforms, and registered-agent / filing services.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the managed unit is the **legal entity** (subsidiary, corporation, LLC, LLP, SPV…). "Compliance" means the entity's statutory/regulatory obligations: periodic filings (annual reports / confirmation statements), registered agent & registered office maintenance, statutory registers (officers, directors, shareholders, beneficial owners), good standing, and the corporate records that evidence them.
- Likely confusion set:
  - **Legal Entity Management** (directory §10) — probably the same product category viewed from the record/structure side.
  - **Compliance Management Platform** (§11) — generic obligations (policies, controls, training), not entity-anchored.
  - **Corporate Governance Platform / Board portal** (§11) — board-centric, not entity-statutory-centric.
  - **Registered agent / incorporation services** — services, not software, but often bundled.
  - **Business License / Permit Management** — obligations attach to business activities/locations, not to the legal entity itself.
- Unknowns going in: how filings are executed (in-product e-filing vs managed service vs external agent); how much corporate-records (minute book) work belongs in this Type; whether ownership/cap-table data is core or adjacent.

## Research Questions

1. What is the central object — what does an "entity record" contain?
2. What are "compliance obligations" and how are they represented (deadline, recurrence, jurisdiction, owner, status)?
3. What is the compliance calendar / deadline workflow?
4. How do filings actually get done — direct registry e-filing, managed service, or external?
5. What corporate records / statutory registers are maintained (officers, directors, shareholders, PSC/UBO, minute books)?
6. What documents are stored and generated (resolutions, minutes, certificates, filing confirmations)?
7. Who uses it (corporate secretary, paralegal, legal ops, compliance, external providers) and what roles/permissions exist?
8. How does the Type relate to board governance, legal ops, and registered-agent services?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy / position | Segment |
|---|---|---|
| Diligent Entities | Enterprise GRC-suite module; AI-assisted entity & subsidiary governance | Large enterprise legal ops |
| CSC Entity Management | Service+software incumbent rooted in registered-agent business | Enterprise / mid-market legal & compliance |
| Athennian | Cloud-native "Governance Ops" platform; deep registry e-filing | Corporate groups, funds/PE, professional services |
| Harbor Compliance | Compliance-services provider with SaaS suite; multistate SMB/nonprofit focus | SMB / multistate operators, nonprofits |
| Klea | Entity compliance automation pure-play | (unreachable — see Sources) |

## Sources

| Source | URL | Status |
|---|---|---|
| Diligent Entities product page | https://www.diligent.com/products/entities/ | fetched 2026-09-06 |
| Diligent corporate secretary solution page | https://www.diligent.com/solutions/corporate-secretary/ | fetched 2026-09-06 |
| Athennian homepage | https://www.athennian.com/ | fetched 2026-09-06 |
| Athennian Help Center | https://help.athennian.com/hc/en-us | fetched 2026-09-06 |
| Athennian help: Navigate the New Task Experience | https://help.athennian.com/hc/en-us/articles/50989307354139 | fetched 2026-09-06 |
| Athennian help: Companies House Integration (UK E-Filing) | https://help.athennian.com/hc/en-us/articles/35026474948507 | fetched 2026-09-06 |
| CSC Entity Management page | https://www.cscglobal.com/service/entity-solutions/entity-management/ | fetched 2026-09-06 |
| Harbor Compliance homepage | https://www.harborcompliance.com/ | fetched 2026-09-06 |
| Harbor Compliance Entity Manager page | https://www.harborcompliance.com/entity-manager-software | fetched 2026-09-06 |
| Klea | https://klea.team/ , https://www.klea.team/ | **unreachable** (2× transport error; abandoned per network rule) |

Evidence layers used below: **A** = directly observed on an official source of one product; **B** = cross-product commonality (≥2 products); **C** = canonical inference from comparison + boundary reasoning.

---

## Product Observations

### Diligent Entities (Diligent)

Key observations (Layer A unless noted):

- Positioning: "Manage subsidiaries with a centralized corporate record that's always up to date"; "AI-enhanced entity management software for faster, sharper oversight."
- Central promise: "a fully digitized, fully connected corporate record"; AI "finds the right data, flags compliance issues, and builds reports and visualizations — across every step of your workflow."
- Compliance deadline machinery: "Never miss a compliance deadline" is a named capability block.
- Case study (Fortive): "centralize 300+ global records, stay audit-ready and visualize complex org structures in real-time"; "managing compliance across hundreds of jurisdictions."
- Corporate-secretary framing: "shouldering responsibility for statutory compliance, entity records and governance support, often across complex, multi-jurisdictional landscapes"; "Centralize & automate compliance — filings, calendars, and reminders in one audit-ready system"; "Keep every entity, filing, and board record organized and up to date in a single, audit-ready hub."
- Self-service distribution of entity data: "Empower your team with a self-service model using permissioned access via Microsoft Teams."
- Part of the Diligent One Platform (boards + GRC suite); subsidiary board management is adjacent.
- Users named: corporate secretaries, legal, tax and compliance teams; senior corporate paralegal quoted.

### Athennian

Key observations (Layer A):

- Positioning: "Governance Ops™ Software for Legal, Tax & Finance Teams"; "Modern Entity Management for Governance Ops."
- Capability set (product page): Entity & People Records ("entity details, appointment, addresses, KYC, registrations and compliance details in reportable and searchable profiles"); Equity & Debt Structures (cap tables, loans); Structure Charts; Controls & Governance ("granular permissions, audit trails and custom fields"); Document Management ("store, edit and automate templates, use electronic signatures, and control access"); Appointments/D&O ("director, officer, power of attorney or signing authority"); Tasks & Reports ("track compliance dates and significant events, and create custom task lists"); Athennian AI.
- Tasks (help center, Tier 1):
  - Global task list columns: Status, Name, Task Type, connected Entity, Priority, Created Date, Due Date (danger icon when Overdue); Table and Calendar views; actions Complete / Archive / Delete.
  - Filters: Status, Due Date, Type, Assignee, Issuer, Group; savable custom views.
  - Custom task statuses managed by administrators (with colors).
  - Full-page task: Name, Task Type, Status, Priority, Issuer, Assignee, Details, Tags, Checklist, Effective / Resolution / Reference dates, Reminders.
  - Document generation inside a task from templates; route to e-signature; task-level access restrictions; upload/download.
  - **Jurisdiction-specific tasks**: "The user interface dynamically changes based on the specific task type, entity type, and formation jurisdiction, revealing relevant fields and filing options… Click the final task filing button to submit directly to connected registries."
- Companies House e-filing (help center, Tier 1):
  - "Submit UK filings directly to Companies House with real-time tracking"; automated task updates; form previews mirroring official documents.
  - Requires a Companies House credit account; credentials entered as Presenter ID + Authentication Code.
  - Supported filings: incorporation (IN01), confirmation statement (CS01), director/secretary appointments (AP01–AP04), terminations (TM01–TM02), change of name (NM01), Person of Significant Control notices (PSC01/02/04/07), change of registered office (AD01). Filing statuses and notifications tracked; director identity-verification codes supported.
- Minute book: "virtual minute book… pull a folder, download everything and share" (customer quote); help center has "Navigate the New Minute Book Experience."
- Access governance: time-limited access grants for outside counsel (customer quote); PII flags on people addresses; global audit trail export (admin).
- UBO: publishes a "2026 Global UBO Guide" covering UBO regulations across 50 jurisdictions (positioning-level evidence of beneficial-ownership focus).
- Audiences: corporate groups, private equity & funds, private markets (funds, SPVs, portfolio entities), professional services, family offices; teams: legal, treasury, finance, tax.

### CSC Entity Management

Key observations (Layer A):

- Positioning: "Gain confidence and control over critical entity compliance"; "simplifies and centralizes the governance of your global entity portfolio. We combine award-winning software with expert support."
- Explicit feature list (product page):
  - Maintain sensitive officer and director data; transparency on officer/director changes via a Workday (HCM) integration.
  - Store, manage, and search minute book and governance documents electronically; AI document management (bulk imports, automated entity/folder routing, instant summaries).
  - Generate documents via guided workflow; route e-signature requests (DocuSign).
  - Track ownership, stock, and shareholder information; automated structure charts; structure-chart modeling of potential/pending ownership changes.
  - Custom fields; track DBA names, prior names, merger history.
  - **"Manage upcoming compliance due dates, including annual reports, and other critical filings."**
  - Reports "for auditing, entity tracking, and decision-making"; secure bi-directional APIs.
  - **"Submit electronic filings directly to Companies House and the SEC via prebuilt integrations."**
- "Automated Compliance Calendar — Built-in tools auto-manage U.S. and global deadlines like annual reports and key filings."
- Service integration: "Governance data and legal documents auto-sync with CSC services" (registered agent, annual report filing, etc. are sibling CSC services).
- FAQ definitions (Tier 1-adjacent, vendor-authored): "Entity management is the process of organizing and maintaining accurate records for a company's legal entities across jurisdictions. It includes tracking ownership structures, officer and director information, compliance deadlines, and governance documentation." And: entity management vs corporate governance — "Entity management focuses on the operational and administrative tasks required to maintain compliance for legal entities… Corporate governance… refers to the broader framework of rules, practices, and processes used to direct and control a company."
- Users: "legal departments, compliance professionals, corporate secretaries, and governance teams… especially those managing complex or multinational entity portfolios."
- Sibling services around the software: entity formation, global subsidiary management, SPV management, registered agent & SOP, annual report filing, business license solutions, transactional filings.

### Harbor Compliance (Entity Manager within the Compliance Suite)

Key observations (Layer A):

- Positioning: "State Licensing Compliance Platform"; "Multistate compliance made simple"; software suite = Entity Manager, License Manager, Records Manager, Tax Manager, Dynamic Disclosures, Registered Agent Service, Compliance Navigator AI.
- Entity Manager (product page):
  - "Provides complete visibility into entity and compliance status"; "Automates annual report and compliance tracking."
  - Value bullets: "Maintain good standing and avoid late fees and penalties"; "Save time submitting corporate filings and annual reports"; "Get instant clarity on where your entities are registered"; "Ensure continuity through staff and vendor changes."
  - Interactive map of state registrations (hover/click per state).
  - **Compliance Core™ database**: "automatically set annual report due dates and send notifications, wherever available… continually maintained."
  - **Agency integration**: "integrated with the secretary of state databases, wherever available. Registrations are automatically populated… along with their registration numbers and publicly available information" (addresses, registered agent on file).
- Homepage framing of the compliance domain (vendor-authored FAQ): every business must (1) register its legal entity in each state where it does business and maintain those registrations "generally by appointing a registered agent and filing annual reports," (2) maintain licenses, (3) register for taxes — "the requirements are interdependent."
- Centralized Company Profile used to complete filings across jurisdictions; onboarding audits legacy spreadsheets and verifies data against agencies.
- Engagement models: Managed Services (vendor files for you), SaaS (in-house staff), Hybrid.
- Services catalog: annual report, foreign qualification, registered agent, BOI reporting, reinstatement, dissolution/withdrawal, certificates of good standing, DBA, etc.
- Good standing is the recurring outcome concept ("Only organizations in good standing can do either [M&A]").

### Klea

- Both candidate URLs unreachable (transport error ×2). No observations recorded. Per source-access limitation rule, nothing is claimed from memory about Klea; the sample stands on the four reachable products.

---

## Cross-product Comparison

| Dimension | Diligent Entities | Athennian | CSC Entity Management | Harbor Entity Manager |
|---|---|---|---|---|
| Managed unit | legal entities / subsidiaries ("centralized corporate record") | entities (corporate groups, funds, SPVs) | legal entities across jurisdictions | entity registrations per state |
| Compliance deadlines | explicit ("never miss a compliance deadline"; calendars & reminders) | Tasks with due dates, calendar view, overdue flags | "Automated Compliance Calendar"; annual reports & critical filings | auto-set annual report due dates + notifications |
| Obligation completion tracking | filings tracked in audit-ready hub | task lifecycle (status/priority/assignee/checklist; complete/archive) | due-date management + reports | registration status & good-standing visibility |
| Filing execution | not detailed on fetched pages | direct e-filing to Companies House via API; "submit directly to connected registries" | direct e-filing to Companies House and SEC; sibling filing services | managed-service filing (vendor files) or in-house via suite |
| Entity profile data | entity records, org structures | entity details, addresses, registrations, KYC, custom fields | officers/directors, ownership/stock/shareholders, DBA/prior names, merger history | registration numbers, addresses, registered agent, status (from agency feeds) |
| People / appointments | entity records incl. directors (implied); Workday integration is CSC | Appointments/D&O (director, officer, POA, signatory) | officer & director data + change transparency | registered agent on file |
| Ownership / UBO | ownership answers via AI | securities/cap tables, debt; UBO guide | ownership, stock, shareholder info; structure-chart modeling | BOI reporting as a service |
| Corporate records / documents | "every entity, filing, and board record… audit-ready hub" | minute books, document automation, e-signature, access control | minute book & governance documents, AI summaries | Records Manager module |
| Structure charts | "visualize complex org structures" | real-time structure charts | automated charts + modeling of pending changes | map of registrations (geo, not ownership) |
| Agency/registry data feeds | not observed | Companies House API (outbound filing + status) | Companies House + SEC e-filing integrations | secretary-of-state inbound feeds |
| Roles & audit | granular permissions, audit trails | granular permissions, audit trail, custom statuses | enterprise security; unlimited users | unlimited users incl. accountants/counsel |
| Service component | platform (suite) | platform + partner network | software + expert support + sibling services | managed services / SaaS / hybrid |
| Segment | enterprise | corporate groups, funds, professional services | enterprise/mid-market legal & compliance | SMB/multistate, nonprofits |

Layer B (cross-product commonality, ≥3 of 4): entity register as system of record; deadline/compliance calendar with reminders; annual reports as the canonical recurring obligation; officer/director records; ownership/shareholder records; document/minute-book management; structure visualization; permissions + audit trail; integrations (HR, e-signature, registries, agency feeds).

Layer C (canonical inference): the Type is a **portfolio-scale compliance system of record over legal entities**, whose defining loop is obligation → deadline → tracked completion → recorded evidence, with the entity's standing (good standing / filings current) as the health state being protected.

---

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product stops being an Entity Compliance Management application:

1. **Legal-entity register** — the organization's legal entities as identified, jurisdiction-qualified managed records (name, jurisdiction, entity type, registration identifiers, status).
2. **Compliance obligations attached to entities** — jurisdiction-defined requirements (periodic filings, register maintenance, agent/office maintenance) each carrying a due date.
3. **Tracked obligation lifecycle with recorded outcome** — each obligation moves through preparation → filing/submission → confirmation, and the outcome (filed, confirmation, certificate) is recorded as evidence; missed deadlines are visible as a state (overdue / not in good standing).
4. **Portfolio-level oversight surface** — a cross-entity calendar/status view that lets a small governance team see and drive compliance for many entities at once.

Test: remove (1) → generic compliance management; remove (2)+(3) → a corporate-records repository (Legal Entity Management without the compliance loop); remove (4) → per-entity spreadsheets, not a management application.

### L1 — Common Mature Structure

Present in most mature products, not definitional:

- entity profile depth: registered office, registered agent, incorporation/registration dates, DBA/prior names, merger history, custom fields
- people layer: officers, directors, signatories, appointments (D&O), with change tracking (sometimes synced from HR systems)
- ownership layer: shareholders, share/stock records; beneficial-ownership (UBO/PSC/BOI) records where regimes require
- corporate records: minute books, resolutions, minutes, governance documents; document templates, generation, e-signature routing, access control
- task workflow: assignee, priority, status, checklist, reminders, calendar view, saved filters
- structure charts / org charts (incl. modeling of pending changes)
- compliance reporting and audit-ready exports
- roles & granular permissions, audit trails
- integrations: HR (officer changes), e-signature, government registries (e-filing), agency databases (inbound registration data), sibling services (registered agent, formation)
- data migration/onboarding from legacy spreadsheets with verification against agency records

### L2 — Variant / Optional Structure

- **Filing execution model**: direct registry e-filing from the product (observed: Athennian–Companies House; CSC–Companies House/SEC) vs managed-service filing (Harbor) vs tracking-only (user files through their own agents). This is the biggest philosophical split in the category.
- **Scope breadth**: entity-only vs entity+licenses+tax (Harbor suite) vs entity+board/subsidiary-boards (Diligent) vs entity+securities/debt (Athennian).
- **Regional regime**: US multistate (secretary-of-state registrations, foreign qualification, good standing, franchise/annual reports) vs UK (Companies House, confirmation statement, PSC) vs multi-jurisdiction global portfolios.
- **Customer segment**: SMB/multistate operator & nonprofit vs enterprise legal ops vs funds/PE/private markets (SPV-heavy) vs corporate service providers running entities for clients.
- **Service component**: software-only vs software+expert services vs managed-services-first.
- **Beneficial-ownership depth**: recording vs filing support vs advisory content.
- **AI depth**: document summarization, data extraction, Q&A over entity data, agentic workflows.
- **Deployment**: multi-tenant SaaS standard; security posture varies by customer (PII handling, time-limited external access).

### L3 — Vendor-specific (research notes only)

- Diligent: Microsoft Teams permissioned self-service access; Diligent One Platform bundling; marketing ROI figures (318% ROI, 70% time reduction — not used as evidence).
- CSC: Workday HCM integration for officer/director changes; DocuSign routing; flat-fee unlimited-users pricing; NYLJ/CLOC award claims.
- Athennian: "Governance Ops™" branding; virtual minute book; time-limited outside-counsel access; Companies House Presenter ID/Authentication Code credentialing; PwC UK collaboration; Debt/Loans module.
- Harbor: Compliance Core™, Harbor Compliance Score™, Air-Tight Onboarding™, "22,000+ regulatory filing requirements" and "150,000 licensing agencies" figures (vendor marketing numbers — not generalized), interactive registration map, Dynamic Disclosures® (fundraising), 4-step onboarding with "90%" discovery claim.

## Vendor-specific Findings

See L3 above. None of these were promoted into the canonical model. The Workday/DocuSign integrations (CSC) and Teams access (Diligent) are treated as instances of the generic L1 integration layer.

## Boundary Findings

1. **vs Legal Entity Management (directory §10)** — the market category is one ("entity management software"); the same products serve both directory leaves. Defensible split: **Entity Compliance Management centers on the obligation/deadline/filing loop and the entity's compliance state (good standing)**; **Legal Entity Management centers on the entity record corpus and structure** (org/ownership charts, minute books, entity lifecycle events) as the corporate system of record. In practice one product provides both; the leaves are two emphases of one category. → flagged for joint review in STATUS.md.
2. **vs Compliance Management Platform (§11)** — generic compliance obligations (policies, controls, training, frameworks) are not anchored to legal entities as the managed unit. Remove the legal-entity register and obligation set and the product becomes a generic compliance platform.
3. **vs Corporate Governance Platform / board portals (§11)** — board-centric surfaces (meetings, packs, director portals) vs entity-statutory surfaces. Diligent bundles both; CSC's own FAQ draws the line: entity management is "operational and administrative… to maintain compliance for legal entities," governance is "the broader framework… to direct and control a company."
4. **vs Registered Agent / incorporation / filing services** — services executed by humans/agents vs the software that tracks, prepares, and evidences. Several vendors bundle both (CSC, Harbor); the software Type remains distinct because its deliverable is the tracked record + calendar + evidence, not the filing act itself.
5. **vs Business License / Permit Management** — licenses attach to business activities/locations and are tracked in Harbor's separate License Manager module; entity compliance is the entity-registration slice. Adjacent, interdependent ("registering for taxes may trigger the need to register the entity…").
6. **vs Cap Table Management** — ownership records overlap, but cap-table products center on equity transactions/dilution of one company; here ownership is one attribute layer of portfolio compliance records.
7. **"Remove what to become another Type" test**: remove the entity register → Compliance Management Platform; remove the obligation/deadline machinery → Legal Entity Management (records/structure); remove the multi-entity portfolio view → single-company secretarial record-keeping (a Variant, not a separate Type — historical UK company-secretarial software fits L0 without portfolio dashboards).

## Historical / Market-Sample Check

Older and narrower products still fit L0: single-jurisdiction company-secretarial suites (e.g., UK company-secretarial software tracking statutory registers and annual returns long before cloud/AI era) satisfy entity register + obligations + tracked filing + (per-entity or small-portfolio) oversight without agency feeds, structure charts, or AI. Regional products (a Delaware registered agent's compliance tracker) also fit. Therefore the definition is not overfit to the current AI-era, multi-jurisdiction enterprise implementation. Modern expectations (agency data feeds, e-filing APIs, AI extraction) are L1/L2, not L0.

## Uncertainties

- Diligent's operational depth (task model, e-filing support) could not be verified from help-center documentation within this pass; its evidence is product/solution-page level (Layer A positioning + named capabilities, no Tier-1 workflow detail).
- Klea unreachable — a compliance-automation pure play is missing from the sample; the "automation-first" pole is represented only indirectly (Athennian AI workflows, Harbor managed services).
- Exact obligation catalogs (which filings per jurisdiction) are vendor-maintained databases (e.g., Harbor's Compliance Core); no neutral public registry of obligation types was consulted. Obligation examples used (annual reports, registered agent, confirmation statement, PSC) are directly evidenced per product but the universe of obligations is larger.
- Whether "good standing" is a first-class tracked state in every product is unclear (explicitly evidenced in Harbor; implied in CSC's certificate-of-good-standing service; not observed in Diligent/Athennian pages).
- US beneficial-ownership (BOI) regime is legally in flux; products support BOI recording/filing, but no claim is made about current mandatory scope.

## Final Synthesis

An Entity Compliance Management application is the governance team's system of record for keeping a portfolio of legal entities compliant. Its world is built from four inseparable parts: (1) a register of the organization's legal entities as identified, jurisdiction-qualified records; (2) the compliance obligations each jurisdiction attaches to those entities (periodic filings, register maintenance, agent/office requirements), each with a due date; (3) a tracked lifecycle that carries each obligation from preparation through filing to recorded confirmation, producing audit-ready evidence and exposing overdue/non-compliant state; and (4) a portfolio-level calendar and status surface through which a small corporate-secretary/legal-ops team drives compliance for many entities at once.

Around this core, mature products add the entity's full statutory profile (officers, directors, signatories, registered agent/office, ownership, beneficial owners), the corporate record (minute books, resolutions, generated documents, e-signature), structure visualization, reporting, permissions/audit, and integrations that keep the record current (HR feeds, agency databases, registry e-filing, e-signature, sibling services). Products diverge most on who executes filings (the software via registry APIs, a managed service, or the user's own agents), on scope breadth (entity-only vs entity+licenses+tax vs entity+board), and on segment (SMB multistate vs enterprise vs funds/SPVs).

The Type's boundary is held by the managed unit: if the records are not legal entities with jurisdiction-defined statutory obligations, it is not this Type; if the obligation/deadline machinery disappears and only the record corpus remains, it has become Legal Entity Management; if the obligations are generic (policies, controls, training), it is a Compliance Management Platform.
