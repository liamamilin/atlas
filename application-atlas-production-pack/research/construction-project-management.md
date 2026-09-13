# Research Notes — Construction Project Management

Research date: 2026-09-07

## Research Goal

Understand what "Construction Project Management" software actually is as an Application Type: what objects it manages, who uses it, how the core coordination work flows through it, how it differs from generic project management software, and how it relates to the many sibling construction leaves in the directory (field management, cost management, scheduling, contract administration, document management, point-tool leaves).

## Initial Boundary

- **What it likely is**: the project-scoped system of record that manages a construction project end-to-end across the participating organizations — the coordination, document, schedule, and money spine of project delivery (as opposed to the site day-record).
- **Nearest neighbors**: generic Project Management Application (§03.07); Construction Field Management (§17, processed); Construction Cost Management (§17, processed); Construction Scheduling; Project Controls Platform; Construction Contract Administration; Change Order Management; Progress Billing; Construction Document Management (§17, processed); Construction Bidding Platform; Preconstruction Management; RFI Management; Submittal Management; Real Estate Development Management.
- **Known taxonomy pressure (from the construction-field-management pass)**: this Type is the suite umbrella of construction software — many directory point-leaves are realized as modules inside PM platforms. The field pass drew the split on objects: "PM owns schedule, cost, contracts, and the document register; field management owns the day record, field work items, inspections, safety, and time capture."
- **Known seam (from the construction-cost-management pass)**: "PM platforms span schedule, RFIs, submittals, field tools; cost tools are one tool family inside them."
- **Open questions going in**: Is the schedule definitional? Is cost definitional? Is the RFI as a named instrument definitional? Is multi-organization participation definitional (vs a GC-internal tool)? What is the boundary vs generic PM and vs the owner-side capital-program pole?

## Research Questions

1. What is the central container/object world of a construction PM product (project, parties, items, documents, schedule, money)?
2. How does the multi-party structure work — organizations vs users, roles, permissions, data visibility, data ownership?
3. What are the canonical coordination workflows (RFI, submittal, transmittal/correspondence, change, meetings) and their lifecycles?
4. How do documents (drawings, specs) participate — version control, distribution, linking to items?
5. How do schedule and cost participate — native depth vs integration, and where does that machinery belong relative to sibling leaves?
6. What differs between the GC-first pole, the owner-side capital-program pole, the neutral multi-org collaboration pole, and the residential SMB pole?
7. What is the boundary against generic Project Management Application, and which findings would be vendor-specific?
8. Historical check: would pre-cloud and pre-digital construction project administration still fit the definition?

## Representative Products

Chosen for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Evidence quality |
|---|---|---|
| Procore | GC-first all-in-one platform; mid-market–enterprise | Tier 1 — full support site reachable (tool inventory, WBS guide, complete RFI user-guide lifecycle + permissions tables) |
| Oracle Aconex | Neutral multi-organization project collaboration; large enterprise/infrastructure | Tier 2 — official product page with unusually detailed FAQ (official self-description; process model documented in the vendor's own words) |
| Trimble Unity Construct (formerly e-Builder Enterprise) | Owner-side capital program & construction project management | Tier 2 — official product page positioning only (capabilities cards JS-rendered; help center not reachable) |
| Buildertrend / CoConstruct | Residential home-builder & remodeler SMB pole | Tier 2-limited — official migration page listing the feature set; main site and help center unreachable (403/timeout) |

Rejected/abandoned samples: Autodesk Construction Cloud (autodesk.com 403 ×2; help.autodesk.com JS shell), Buildertrend main site + help center (403/timeout ×3) — recorded per source-access limitation rules.

## Sources

- Procore Support (support.procore.com) — Support Home tool inventory; Work Breakdown Structure tool page; RFIs user-guide landing (tutorials, FAQ, workflow, permissions matrix); [fetched 2026-09-07]
- Oracle Aconex product page (oracle.com/aconex) — features, FAQ, product tours; [fetched 2026-09-07]
- Trimble Unity Construct product page (trimble.com/en/products/trimble-unity-construct; e-builder.net redirects there) — positioning; [fetched 2026-09-07]
- CoConstruct migration site (coconstruct.com — "The next chapter starts with Buildertrend") — residential pole feature set; [fetched 2026-09-07]
- Prior sibling passes for boundary consistency: research/construction-field-management.md, research/construction-cost-management.md, research/construction-estimating.md (§Boundary Findings)

## Product Observations

### Procore (evidence layer: A — direct observation of official Tier-1 docs)

**Positioning & structure.** The support site organizes the product into **Project Tools** and **Company Tools** — the project is the container; the company (contractor organization) sits above it. Project tool list (verbatim from the support home): Admin, Bidding, Budget, Action Plans, Change Events, Change Orders, Client Contracts, Commitments, Coordination Issues, Correspondence, Crews, Daily Log, Direct Costs, Directory, Documents, Drawings, Emails, Estimating, Forms, Funding, Home, Incidents, Inspections, Invoicing, Meetings, Models, Observations, Photos, Prime Contracts, Progress Billings, Punch List, 360 Reporting, RFIs, Schedule, Specifications, Submittals, Tasks, Timesheets, T&M Tickets, Transmittals. Company tools include Admin, Analytics, Bid Board, Cost Catalog, Directory, ERP Integrations, Payments, Permissions, Planroom, Portfolio, Prequalification Portal, Programs, Resource Planning, Workflows. This is the fullest single evidence of the category's object world.

**Multi-party model.** WBS guide: "With WBS, Owners, General Contractors, and Specialty Contractors can create a customized framework… for tagging, tracking, and reporting with Procore's Financial Management tools." A **Directory** tool holds project participants across organizations; **Permissions** are company/project-level with None/Read Only/Standard/Admin tiers plus granular permissions. RFI role videos name the party roles directly: Owner, Architect, Superintendent, Field Worker, Specialty Contractor, Subcontractor — the project community is contractual, not just a team.

**WBS / coding.** Work Breakdown Structure = segments (cost codes, cost types, sub jobs, custom segments) arranged into a **budget code structure** at company level, overridable at project level; budget codes tag financial line items "across change objects." Segments/items are governed by admin permissions and can be imported/deactivated.

**RFI lifecycle (Tier 1, fully documented).**
- States: Draft → Open → Closed (a "Closed-Draft" status exists; RFIs can be reopened; revisions exist).
- Responsibility: **RFI Manager** role; **Assignees** (optional required responders); **Distribution List**; the "**Ball In Court**" concept — one person holds the next action and can be shifted.
- Responses: multiple responses possible; one is chosen as the "**Official Response**"; respondents can answer **by email without logging in**; notifications at defined steps.
- Linkage/conversions (documented tutorial titles): add Related Item; link RFI to a **drawing** (and specify a **Specification Section**); multi-tiered **Locations**; create **Change Event** from an RFI; create **Potential Change Order** from an RFI (prime contract must be 'Approved'; change-order tiering configured); create an **Instruction** or **Correspondence** item from an RFI; RFI numbering with configurable prefix/starting number; change history; export to CSV/PDF; recycle bin with recover (RFIs maintain status in recycle bin).
- Permissions matrix gates each action by None/Read Only/Standard/Admin + granular permissions (e.g. "Act as RFI Manager", "Mark Official Responses"); offline mobile create/close.

**Money spine present but modular.** Budget, Commitments (downstream subcontracts/POs), Client Contracts and Funding (upstream), Prime Contracts, Change Events → Change Orders, Progress Billings, Invoicing, Direct Costs, T&M Tickets, plus a separate "Portfolio Financials and Capital Planning" product area (Bid Room, Contract Room, Cost Tracker, Project Page, Milestones, Vendor resources) for the owner side. Integrations list includes ERP connectors (Sage, Viewpoint, CMiC, QuickBooks, Yardi, MRI, NetSuite, Acumatica…) and **Oracle Primavera** / Asta Powerproject / Microsoft Project for scheduling — i.e., deep scheduling lives in dedicated tools.

**Field/quality inside the same platform.** Daily Log, Crews, Timesheets, Timecard, Punch List, Inspections, Incidents, Observations, Action Plans — the field-management module family sits inside the same project container (consistent with the field pass's "Procore's tool grid shows vendors drawing the same line").

### Oracle Aconex (evidence layer: A — official product page + FAQ, vendor self-description)

**Positioning.** "Oracle Aconex is a cloud-based project collaboration system built for construction, infrastructure, and engineering projects… helps owners, contractors, engineers, designers, suppliers, and other project participants collaborate in one system throughout the project lifecycle." The page is titled "Aconex Construction Project Management Software." Critically: "Unlike traditional project management solutions designed for a single organization, Oracle Aconex is purpose-built for **contractual collaboration across multiple independent organizations**."

**Data ownership model (the neutral platform).** "Every organization on the project has their own private workspace… and controls the data in their workspace, including who they share that data with and when"; "one organization cannot alter another organization's data or restrict access to it"; the purchaser does not control the project system. This is the strongest formulation of the multi-org governance structure in the sample.

**The project record.** "Unalterable audit trail — nothing can be deleted or edited"; "designed to serve as the **contractual system of record**"; correspondence replaces traditional email — messages "cannot be deleted or altered after the fact"; threading connects related correspondence; archive options (online/project/scheduled) preserve the record post-completion "to meet regulatory and legal requirements… and to help prevent or resolve claims and disputes."

**Processes managed (FAQ list, verbatim).** Document and drawing management; project correspondence and contractual communications; review and approval of design documents; workflow automation; BIM model coordination; work packaging; RFIs; inspection and test plans (ITPs); quality inspections and safety processes; cost, contract, and change management; bid and tender management; supplier document management; reporting, project closeout, and project archiving.

**Document register.** "A single document register with strict version control… revisions automatically supersede earlier versions"; metadata-driven search (not folders); documents/drawings/models linked to reviews, workflows, RFIs, work packages, quality inspections, contracts.

**Workflows.** Configurable workflow engine ("highly configurable process management engine"); automated Review Matrix routes review documents by metadata; comment management consolidates review comments for 2D/3D; cross-organization workflows customizable to "review cycle needs… reducing approval delays."

**Money.** "Integrated cost control" module: "collaboratively manage contracts across the supply chain and streamline change management… track the schedule of values for payment management"; "manage upstream and downstream contracts… report on both the budget and cost sides of contract changes."

**Field & tender.** Aconex Field: safety walks, quality checks, issue tracking, punch lists, daily reports; ITPs as first-class; bid/tender distribution to "Aconex or guest users with direct and secure access," tracked view/receipt status, addenda and clarifications.

**Roles.** "Project directors, project managers, document controllers, design managers, project controls teams, site managers, quality and safety teams, supervisors"; organizations: asset owners, general contractors, EPC firms, owners' representatives/PM firms, architects, consultants, suppliers, subcontractors.

### Trimble Unity Construct / e-Builder Enterprise (evidence layer: A for positioning only)

Official page (product page + navigation): "Enterprise solution for capital program and construction project management… industry-leading, cloud based digital project delivery software **for owners**." Trimble's own navigation labels it "Enterprise software for digital project delivery" and lists it under "Project Management" alongside ProjectSight ("Construction project management software"). The e-Builder heritage is owner-side capital programs (owner as the system-of-record operator). Capabilities cards did not render; help center not reachable — detailed feature claims NOT asserted beyond positioning. This product anchors the owner-side pole: the same Type operated by the funding party rather than the builder.

### Buildertrend / CoConstruct — residential SMB pole (evidence layer: A-limited)

CoConstruct's site is now a migration page: "CoConstruct's mission is to simplify the business for busy builders… focus on financial management"; the product family is "construction management software for home builders and remodelers." Buildertrend feature set listed on the page: **Specs, Selections, Task management, Client Updates, Plans, Signatures and annotations, Better budgeting**; testimonials reference cost-plus contracts, budgets, scheduling, client communication. Notably absent from the named feature set: formal RFIs and submittals — the residential pole realizes the coordination loop as **client-facing approvals** (selections, signatures, client updates) rather than contract-form instruments. Main site and help center were unreachable, so this pole is documented at reduced strength (feature names only, no workflow detail).

## Cross-product Comparison

| Structure | Procore | Oracle Aconex | Unity Construct (e-Builder) | Buildertrend/CoConstruct | Verdict |
|---|---|---|---|---|---|
| Project as container of all records | Yes (Project tools) | Yes ("every organization on the project") | Yes (capital program → projects) | Yes (projects per build/remodel) | **Defining** |
| Multi-organization project community | Yes (Directory; Owner/Architect/GC/Specialty roles; permission tiers) | Yes — the product's raison d'être (private workspace per org, neutral ownership) | Yes (owner + delivery teams; "digital project delivery") | Yes (builder + clients + trade partners) | **Defining** |
| Formal cross-party coordination items with tracked state + durable record | Yes (RFIs, Submittals, Transmittals, Correspondence, Meetings, Change Events/Orders; ball-in-court; official response; change history) | Yes (correspondence replacing email, workflows, reviews, RFIs, unalterable audit trail) | Implied by positioning (owner approval/change workflows); not directly observed | Partial — approvals/signatures/selections (client approvals), no formal RFI/submittal observed | **Defining** (the instrument names vary by segment; the structured approval/change flow + record is constant) |
| Version-controlled drawing/document register | Yes (Drawings, Specifications, Documents) | Yes (single document register, revisions supersede) | Not directly observed | Yes (Plans; "latest plans from anywhere") | Common mature (universal in sample) |
| Native schedule | Yes (Schedule tool + P6/MSP/Powerproject integrations) | **No native CPM** — integrates Primavera; packages link to schedule dates | Not directly observed | Yes (scheduling for residential) | Common, NOT defining (a flagship category product lacks native scheduling) |
| Budget/commitment/change-order machinery | Yes (Budget, Commitments, Client Contracts, Change Events→Change Orders, Progress Billings) | Yes (integrated cost control; upstream/downstream contracts; schedule of values) | Yes by positioning (owner capital program management) | Yes (budgeting, job costing) | Common (deep version = Construction Cost Management sibling) |
| Bid/procurement to subcontractors | Yes (Bidding, Planroom, Bid Board, Prequalification) | Yes (bid/tender management, supplier documents) | Not directly observed | Partial (bids/estimates named in heritage features) | Common |
| Field records (daily log, punch, inspections) | Yes (Daily Log, Punch List, Inspections, Incidents…) | Yes (Aconex Field: punch lists, daily reports, safety walks) | Not directly observed | Partial (client updates, to-dos) | Common (deep version = Construction Field Management sibling) |
| Mobile/offline capture | Yes (iOS/Android user guides; offline noted) | Yes (Aconex Mobile) | Not directly observed | Not directly observed | Common, era-typical |
| Owner/client visibility surface | Yes (Portfolio Financials for owners; owner role videos) | Yes (owner as participant org) | Yes (owner IS the operator) | Yes (client portal, client updates) | Common |
| AI assistance | Yes (Draft RFI Agent beta; Assist drafting) | Not observed | Not observed | Yes (AI-powered client updates) | Era-typical, optional |
| Neutral per-org data ownership | No (purchaser/company-controlled with permission tiers) | **Yes** (defining product philosophy) | Not observed | No | Vendor-specific (pole) |
| Ball-in-court / official response vocabulary | Yes (Procore-native terms) | Equivalent mechanics via workflow routing | Not observed | Not observed | Vendor-specific naming of a common pattern |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

1. **The construction project as the managed container.** A defined construction undertaking (building, infrastructure, facility work) that all records — items, documents, schedule, money — attach to, persisting from award/set-up through closeout. Remove it → disconnected point tools, not a management system.
2. **A multi-organization project community.** The project's participants come from multiple independent organizations (owner/client, designers/engineers, general contractor, subcontractors, suppliers), each with its own people working under governed, organization-aware access. Remove it → an internal team tool (generic Project Management Application), not this Type.
3. **Formal cross-organization coordination workflows held as the durable project record.** Structured, numbered, attributable items (information requests, submittals/approvals, formal correspondence, change actions, meeting minutes) routed between parties through tracked states (draft → open/routed → responded/official decision → closed), each with an action owner and retained history, linked to the project's documents. Remove it → a document store or a Gantt tool, not this Type.

Removal tests:
- Remove (1): RFI/approval records float free of any undertaking → form tracker. Still this Type? No.
- Remove (2): one org's team runs tasks in a Gantt tool → generic Project Management Application. No.
- Remove (3): project + parties + files but no routed, stateful, recorded coordination → cloud storage with sharing. No.
- Historical check (pre-cloud / pre-digital): paper-era construction project administration — numbered RFI logs, submittal registers, drawing registers, change-order files, signed meeting minutes routed between owner/architect/contractor — satisfies all three invariants without cloud, mobile, AI, or native CPM. Historical check **passes**; L0 survives §22 anti-overfitting review.

### L1 — Common Mature Structure

- **Project directory + org-scoped permissions** (parties, roles, contact data; None/Read Only/Standard/Admin-class tiers; granular permissions).
- **Project document record**: drawings with revision control (later revisions supersede), specifications, photos, general documents; distribution to the parties; plan/markup viewers; items link to drawings/spec sections/locations.
- **Coordination item machinery**: numbering registers with prefixes, distribution groups, due dates, notifications, email-in/email-out, related-item linking, change history, exports, recycle bin, revisions.
- **Change management seam**: coordination items convert into change records that update contracts/budgets (the cost pass's change chain; two-tier/three-tier change-order configurations).
- **Budget/commitment/claim machinery** (deep version = Construction Cost Management): budget codes over a cost breakdown, commitments, progress claims against the owner contract.
- **Schedule dimension**: milestones/activities tracked or integrated from dedicated scheduling tools; coordination items reference schedule impact.
- **Meetings & minutes with action items**; correspondence logs.
- **Field record surfaces**: daily log, punch list, inspections/quality, safety (deep version = Construction Field Management).
- **Bid/procurement to the supply chain**: bid packages, tender distribution/tracking, vendor prequalification, supplier document collection.
- **Mobile field apps** with offline capture and quick-create from photos.
- **Owner/client visibility** surfaces (portals, update feeds, read-only access).
- **Reporting/dashboards, search, audit trail, archive/closeout record** (handover packages; retention "for regulatory and legal requirements… and disputes").
- **AI assistance** (era-typical: drafting, summarizing) — optional.

### L2 — Variant / Optional Structure

- **Operator side**: GC/subcontractor-first platforms (builder operates) vs owner-side capital-program platforms (owner operates, "digital project delivery") vs neutral collaboration platforms (no single owner-org controls the record).
- **Segment flavor**: vertical commercial (RFI/submittal-heavy, spec sections), heavy civil/infrastructure (EPC, long-horizon programs), residential SMB (client approvals — selections/signatures — instead of contract-form instruments).
- **Native scheduling depth**: none (integration-first) vs lightweight native vs deep (deep = Construction Scheduling sibling).
- **Financial depth**: none → budget tracking → full commitment/claim/retainage machinery → ERP-integrated.
- **Data-governance model**: purchaser-controlled (permission tiers) vs per-organization ownership.
- **Deployment**: SaaS standard today; regional/localized products; module/edition laddering.

### L3 — Vendor-specific (research notes only)

- Procore: "Ball In Court" responsibility shifting; "Official Response"; WBS segments (cost codes/cost types/sub jobs/custom) and budget codes; Change Events as a distinct pre-change object; Project vs Company tool split; "Portfolio Financials" capital-planning area; Draft RFI Agent (AI).
- Aconex: the data-ownership model ("every organization owns its workspace"); mail replacing email as contractual correspondence; Review Matrix; work packages; Online/Project/Scheduled Archive products.
- Unity Construct/e-Builder: capital-program framing; program/portfolio layer above projects.
- Buildertrend/CoConstruct: Selections, Client Updates, Specs; CoConstruct's financial-management emphasis; CoConstruct folded into Buildertrend (2024–2026 migration).
- Procore/Autodesk/Trimble integration catalogs (P6, MSP, Sage, Viewpoint, CMiC…).

## Vendor-specific Findings

- Ball-in-court, official responses, and WBS budget codes are Procore vocabulary for mechanics that Aconex realizes differently (workflow routing, review matrices) — do not promote the terms; promote the pattern (tracked action ownership; one official decision per item; coded cost structure).
- The neutral per-org data-ownership model is Aconex-specific product philosophy; other products use purchaser-controlled permission tiers. Both realize the same L0 invariant (multi-org community with governed access).
- Residential client-approval machinery (selections, signatures) is the residential pole's realization of the approval flow — segment variant, not a separate Type.

## Boundary Findings

1. **vs generic Project Management Application (§03.07)** — the sharpest seam. Generic PM centers tasks/boards/timelines for a team inside one organization. This Type centers a **contractual multi-organization community** plus construction-specific machinery (document registers, approval/change flows, commitments). Test: strip multi-org participation and the formal cross-party workflow machinery → generic PM; add them → this Type. Procore's own FAQ-adjacent framing ("traditional project management solutions designed for a single organization") and Aconex's positioning both draw this line.
2. **vs Construction Field Management (§17, processed)** — consistent with that pass: field owns the day record + field work items; PM owns the project container, coordination workflows, schedule/cost/contract/document spine. Field modules are hosted inside PM platforms (Procore tool grid shows both). Subtraction test (from the field pass): keep schedule/cost/contracts and drop the day record + field work items → Construction Project Management.
3. **vs Construction Cost Management (§17, processed)** — cost owns the money loop (budget baseline → commitments → actuals → forecast → change chain); PM hosts it as one tool family among the coordination spine. The change-order/payment vocabulary is shared; the center differs.
4. **vs Construction Scheduling (§17, unprocessed)** — deep CPM scheduling (logic networks, resource/cost loading, updating cycles) is its own Type; PM platforms integrate scheduling products rather than replace them (Aconex has no native schedule; Procore integrates P6/MSP/Powerproject). Flag for joint review when that leaf is processed.
5. **vs Project Controls Platform (§17, unprocessed)** — project controls = the measurement/analysis layer (performance indices, earned value, portfolio roll-up, dashboards) over schedule/cost data; PM = the management system of record where the data originates. Flag for joint review.
6. **vs Construction Contract Administration (§17, unprocessed)** — contract lifecycle management (procurement→execution→claims→closeout) vs project coordination; PM products carry commitment/claim surfaces but the contract-administration center (contract registers, insurance/security, claims escalation) is distinct. Flag for joint review.
7. **vs Construction Document Management (§17, processed)** — the document register is a contained module of PM; the document-management Type owns deep document control (transmittal-level governance, ISO 19650-style CDE workflows). Subtraction test: keep only the register → that Type.
8. **vs Construction Bidding Platform (§17, unprocessed)** — bid packages/tender distribution is one PM capability; the bidding Type owns multi-bidder bid-day machinery (per the estimating pass's note). Flag for that leaf.
9. **vs Real Estate Development Management (§17, unprocessed)** — owner-side development business management (acquisition→pro formas→assets) vs project delivery execution; Unity Construct's owner pole is delivery-focused, adjacent to but distinct from development management.
10. **Umbrella structure note (echoing the field pass)** — RFI Management, Submittal Management, Change Order Management, Progress Billing, Daily Log, Punch List Management, Construction Quality/Safety Management are all realized as modules of PM platforms; they remain legitimate point-leaf Types (standalone and specialist products exist), but this pass confirms the PM platform is the container product on the market. Recommend cross-reference handling when those leaves are processed.

## Uncertainties

- Trimble Unity Construct detail: only positioning evidence reachable (JS-rendered capability cards; help center unreachable). The owner-side pole's feature detail is asserted only as "capital program + construction project management for owners" per the vendor's own page; nothing more specific.
- Buildertrend/CoConstruct detail: main site 403, help center timeouts; evidence limited to the migration page's named features. The residential pole is documented at reduced strength; no workflow-level claims.
- Autodesk Construction Cloud: unreachable; excluded from the sample; the design-authoring-to-construction continuum is therefore documented only via Aconex's model coordination and Procore's BIM plugins.
- e-Builder help center: no response; no Tier-1 owner-pole workflow evidence.
- The exact tiering of Procore's Portfolio Financials vs core platform is product-specific and left in notes.
- No claim is made about pricing, market share, or usage scale.

## Final Synthesis

A Construction Project Management application is the project-scoped system of record for delivering construction work across the organizations contracted to deliver it. Its defining structure is threefold and minimal: (1) the construction project as the container to which everything attaches; (2) the project's multi-organization community — owner, designers, contractors, suppliers — working under governed, organization-aware access; (3) formal cross-organization coordination workflows — information requests, submittals/approvals, contractual correspondence, change actions, minutes — carried as numbered, stateful, attributable records linked to the project's documents, forming the durable contractual project record. Around that core, mature products add the document register with revision control, the schedule dimension (often via integration with dedicated scheduling tools), the budget/commitment/change/claim machinery, field record surfaces, bid/tender distribution to the supply chain, mobile capture, owner/client visibility, reporting, and a preserved closeout/archive record. The market realizes the Type in poles: GC-first platforms, owner-side capital-program platforms, neutral multi-org collaboration platforms, and residential SMB tools where the approval flow runs through the client. The Type's edges are held by subtraction: strip multi-org participation and formal workflows → generic project management; strip coordination and keep the day record → construction field management; strip coordination and keep the money loop → construction cost management; strip coordination and keep deep CPM → construction scheduling; keep only the register → construction document management.
