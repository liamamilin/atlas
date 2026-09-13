# Research Notes — Engineering Change Management

## Research Goal

Understand what an Engineering Change Management application is as an Application Type: what objects exist in its world, what users do with them, how a change moves from proposal to released revision, which rules govern the process, and where the Type's boundary lies against Product Lifecycle Management (PLM), Bill of Materials Management, PDM/Engineering Document Management, IT Change Management, Construction Change Order Management, and Product Configuration Management.

This pass also carries four joint-review obligations recorded by previously processed sibling passes:

1. **bill-of-materials-management** — every sampled BOM product embeds a change workflow (CR/CO/approval) scoped to items/BOMs/revisions; the ECM leaf was reserved for change-centered products whose managed objects span wider engineering artifacts (documents, files, specifications). Partial-alias risk if defined broadly.
2. **product-lifecycle-management-plm** — change process embedded in every sampled PLM; test for a change-centered record world independent of the product-record estate.
3. **it-change-management** — identical governance grammar over a product/BOM record base; keep-both expected on domain binding.
4. **change-order-management (construction)** — same-word overlap; seam test = remove the commercial contract/counterparty/money structure (→ ECM territory) or the design-data/BOM structure (→ COM territory).
5. **product-configuration-management** — enterprise change process vs model-scoped versioning leg.

## Initial Boundary

Working hypothesis at start: Engineering Change Management is the governed process machinery for modifying engineering/product definition data — change requests are submitted, analyzed for impact, approved by a designated authority, then implemented as new released revisions of affected items/documents, with effectivity rules deciding when each change takes effect. Nearest neighbors: PLM (estate), BOM management (structure), PDM/EDM (files/documents), IT Change Management (IT services), Construction Change Order Management (contracts), QMS document control (regulated quality).

## Research Questions

- RQ1. What are the core objects of the change world? Is the request/order/notice triple universal or vendor-specific?
- RQ2. What record base do changes act upon — items, BOMs, documents, files, specs? (BOM-flag test: wider than items/BOMs?)
- RQ3. What is the change lifecycle (states, transitions, roles)?
- RQ4. How is approval organized (change board, routing, e-signature)?
- RQ5. How do approved changes alter the record base (new revisions, redlines, affected/affected-by links)?
- RQ6. What is effectivity and disposition (when does the change take effect)?
- RQ7. How does the change world hand off downstream (manufacturing/ERP, suppliers)?
- RQ8. What interfaces do users face (change workspace, impact analysis, revision history)?
- RQ9. Is there a change-centered record world independent of the product-record estate? (PLM-flag test)
- RQ10. Boundary tests vs IT change, construction change orders, QMS document control, configuration management.

## Representative Products

Five poles chosen for market representation, documentation quality, product philosophy, and customer level:

| Product | Pole | Customer level | Philosophy |
|---|---|---|---|
| PTC Windchill | enterprise PLM suite with change machinery | large enterprise | process depth (full/fast/basic tracks, boards) |
| Arena (a PTC business) | cloud PLM/QMS, change as foundational solution area | mid-market, regulated-heavy | automated routings + connected product record |
| Odoo PLM | open-source ERP module | SMB / global low end | ECO as the module's central object, social communication |
| Duro | modern cloud PLM for hardware teams | startups / SMB | Change Order as "the heart of revision management" |
| Autodesk Vault Professional | PDM file vault with change orders | mid-market engineering workgroups | file/item vault first; change process as governed add-on layer |

## Sources

| # | Source | Tier | Access |
|---|---|---|---|
| S1 | PTC — Engineering Change Management technology page (ptc.com/en/technologies/plm/engineering-change-management) | 2 | OK, fetched 2026-09-10 |
| S2 | Arena — Engineering Change Management solution page (arenasolutions.com/solutions/engineering-change-management/) | 2 | OK, fetched 2026-09-10 |
| S3 | Arena — "The Essential Guide to Engineering and Manufacturing Change Orders" (arenasolutions.com/resources/articles/guide-manufacturing-engineering-change-orders/) | 2 (official educational article) | OK via search excerpts |
| S4 | Arena — "How Automated Engineering Change Management Helps Manufacturers Move Faster With Less Risk" blog (arenasolutions.com/blog/how-automated-engineering-change-management-helps-manufacturers-move-faster-with-less-risk/) | 2 | OK via search excerpts |
| S5 | Arena — No-code & Low-code Workflow Customization knowledge-hub page (arenasolutions.com/knowledge-hub/arena-plm-qms-questions/no-code-workflow/) | 2 | OK via search excerpts |
| S6 | Odoo — PLM product page (odoo.com/app/plm) | 2 | OK, fetched 2026-09-10 |
| S7 | Duro — "Change Orders" help article (duro.zendesk.com/hc/en-us/articles/360029600032-Change-Orders) | 1 | OK via search excerpts |
| S8 | Duro — "FAQ: Change Orders" (duro.zendesk.com/hc/en-us/articles/6893351333652-FAQ-Change-Orders) | 1 | OK via search excerpts |
| S9 | Duro — "Lifecycle Validations and Updates" (duro.zendesk.com/hc/en-us/articles/360044348651-Lifecycle-Validations-and-Updates) | 1 | OK via search excerpts |
| S10 | Duro — "Revision History Table" (duro.zendesk.com/hc/en-us/articles/360050079871-Revision-History-Table) | 1 | OK via search excerpts |
| S11 | Duro — API docs "Change Orders" (docs.durohub.com/core-concepts/change-orders) | 1 | OK via search excerpts |
| S12 | Autodesk — Vault help "Change Orders" (help.autodesk.com/cloudhelp/.../GUID-967A669D-...) | 1 | OK via search excerpts |
| S13 | Autodesk — Vault help "Change Order Routings and Routing Roles" (GUID-AC999E67-...) | 1 | OK via search excerpts |
| S14 | Autodesk — Vault help "Rules and Best Practices for Using Change Orders with Files" (GUID-2BEA1B49-...) | 1 | OK via search excerpts |
| S15 | Autodesk — Vault help "Change Order Administration" (GUID-1425F5FA-...) | 1 | OK via search excerpts |
| S16 | KETIV (Autodesk partner) — "How to Use ECOs in Autodesk Vault—With or Without Items" | 3 | OK via search excerpts |

Source-access limitation: Odoo's PLM application has no dedicated user-documentation page reachable at the standard documentation paths (two attempts, 404). Odoo evidence is therefore Tier 2 (product page) only; no Odoo-specific state names or operational details are asserted. PTC's Windchill help center was not attempted beyond the technology page (the PLM pass had already established that support.ptc.com pages typically require login); Windchill evidence is Tier 2 but unusually detailed for a product page.

## Product Observations

### PTC Windchill (S1) — evidence layer A

- Definition (vendor's own): "Engineering change management is the process of creating, reviewing, and gaining formal approval for engineering change requests, engineering change orders, and engineering change notifications."
- Change processes include **full track (full CRB/CIB)** — Change Review Board / Change Inspection Board — **fast track (change admin)**, and **basic (lightweight CN only)**: the process depth itself is configurable.
- **Problem report**: capture issues or opportunities for products and processes, tie to both change and quality processes.
- **Deviation or waiver**: capture a "temporary" change as part of the standard change workflow.
- **ECN**: "create and execute the implementation plans for delivering the change to the enterprise. Allow for auditing and validation of the results prior to release of the data."
- **ECR**: "evaluate technical and business justifications and plan minor or major changes (fast track or full track) with the change review board."
- **ECO**: "notify, seek approval, and implement their proposed changes during the product development stage."
- **Electronic signatures**: change records, sign-offs, markups, comments connected to product data with audit trails.
- **Workflow**: repeatable processes delivering tasks automatically; configurable task templates.
- **Automatic synchronization with manufacturing systems**: publish updated information downstream when changes are resolved.
- **Business rules** to ensure product data meets corporate standards; **remote requirements** impact via OSLC traceability.
- Benefits framing: visibility (real-time view of requested changes to all stakeholders, cross-discipline involvement), traceability (single source of truth, compliance), governance (associativity so all changes are identified).

### Arena (S2, S3, S4, S5) — evidence layer A

- "Arena Engineering Change Management is a foundational part of our PLM and QMS solutions. Internal teams and supply chain partners review and collaborate effectively on formal engineering change requests (ECR) and engineering change order (ECO) processes with automated approvals."
- Changes connected to **items, BOMs, drawings, and SOPs**; later blog adds **specifications, software, procedures, quality records**.
- Roles on the review: engineering, supply chain partners (DFM feedback), procurement, quality, executive management, cross-functional teams.
- Automate approval routings based on change types, priorities, product lines; ECO cycle-time analytics; email notifications and dashboards; review changes "in context with all parts, BOMs, and documents linked to product and quality processes."
- Arena's own educational guide (S3) defines the industry vocabulary: **ECO** = "a formal review process of proposed engineering changes to an established baseline that will impact form, fit, or function… will list all the affected components and will provide the reasoning… Redlined drawings, inventory disposition instructions, and part effectiveness are other types of information that may be contained within an ECO." **ECR** = "document the initial request or suggestion(s) to address a design problem… It's possible to combine the ECO and ECR processes because the ECR may be considered redundant by some businesses." **DCO** (document change order) = smaller adjustments (typos, work-order instructions, document updates).
- Arena blog (S4) on ECO content: what is changing (affected parts, assemblies, BOMs, drawings, specifications, software, procedures, other documents); why (design improvement, component shortage/obsolescence, supplier recommendation, quality event/CAPA, customer request, cost reduction, manufacturing improvement, regulatory requirement); impact assessment beyond the item (related assemblies, open purchase orders, existing inventory, tooling, test equipment, work instructions, training records, supplier commitments, customer deliveries); who approves (team should reflect ECO type and impact — quality, regulatory, procurement, manufacturing, service, external suppliers); how implemented (approval "does not complete the change"; ECO defines implementation work).
- Automations (S5): generate an ECO from an ECR; generate an ECO from a CAPA; generate an MCO or DCO from an ECO; copy BOMs; link records; add approvers; initiate subsequent processes.
- AI capabilities: AI Item Redline (summarize ECO changes, before/after differences), AI File Insights (find references/dependencies across documents for change-impact analysis). Metrics: ECO cycle time, approval time, overdue changes, time per review stage, implementation time, rework count.

### Odoo PLM (S6) — evidence layer A (Tier 2 only)

- Positioning: "A collaborative platform to manage engineering changes, versions, documents and ECOs in real-time."
- The ECO list is the module's central artifact ("A list of Engineering Change Orders in Odoo PLM").
- Communication model: enterprise social network — followers, approvals "simple", discussions centralized on documents.
- Integrated document management: attach documents to BoMs, routings; multiple document versions.
- Smart versioning: diff and merge; "work on several versions of the same BoM in parallel and apply only the differences to manage multiple changes."
- Downstream: "Pass information to manufacturing with triggered alerts on worksheets or work center control panels."
- PLM sits beside Manufacturing, Purchase, Quality apps in the ERP suite.

### Duro (S7–S11) — evidence layer A

- "Change Orders are the heart of revision management. Duro's simplified Change Order workflow allows teams to quickly and efficiently highlight changes, review, and approve them."
- Creation surfaces: from a product/component page ("Add to change order"), from the Change Order library, from a dashboard tile.
- CO types: **Documentation Change Order (DCO)** — "used when simple documentation updates are required… DCOs do not impact the revision value or promote the lifecycle status"; Revision History table shows types "Engineering, Manufacturing, or Documentation".
- Anatomy: name, description, products-and-components tab, approver list tab, notification list, documents table.
- Requirements to submit: name, description, at least one product/component, approval type, error-free.
- Status lifecycle: **Draft → Open → (Finalizing) → Closed**; API adds **ON_HOLD** and resolutions **APPROVED / REJECTED / WITHDRAWN**. "By default, Duro's Change Orders automatically close upon approval… reconfigured to allow users to manually close."
- Finalizing stage: "the export package is generated, and a revision snapshot of components and products added to the Change Order is created. Finalizing is only used to ensure CAD changes have been completed in another tool (e.g., Onshape, SWX). Once any Change Order has been approved, no modifications to the contents of CO are allowed."
- Validation engine: items must be at Prototype/Production status to submit; "Nested child components must be at an equal or greater status value than their parent assembly"; **"This component is included in one or more existing open Change Orders"** — "products and components can only be submitted in one Change Order at a time" (race-condition prevention); errors block submission, warnings do not; validation strictness increases with lifecycle status.
- Revision History Table: author, timestamp, type (CO type + number, green approved / red rejected), resulting revision value, resulting status, details; red-triangle indicator for "modified but not yet approved for release" — "It must now be submitted through a Change Order for the new status and revision values to be ratified and the item revision to be considered released."
- Compare Revisions tool: diff between any two revisions — documents added/deleted, sourcing changes (MPN, manufacturer, price, lead time), assembly/BOM changes.
- New-generation workflow templates (S11): single-stage review template (auto-closes approved COs), dual-stage template (adds second review stage, **impact analysis fields**, requires manual closure), custom templates; stages with decision methods; custom fields; validations (system + custom JavaScript rules).
- Rejection handling: reject → edit (add/remove components) → re-submit "the original ECO".

### Autodesk Vault Professional (S12–S16) — evidence layer A

- "Change orders are a component of the change management process that describe why, how, and when changes are made to a design." Available only in Vault Professional. "Change orders provide a historical record of why, how, and when changes were made."
- CO states "help track the progression of the change order through the change management process. The state of the change order can determine which users can affect the change order, based on the user's role." Routing list controls who is notified per state.
- Pre-requisites: Administrator or Change Order Editor permission; routing list and numbering scheme predefined by an administrator.
- CO dialog six tabs: General (attributes), **Records (files and items associated with the change order — title, description, revision, state)**, Comments (decisions, attachments, markups), Files, Routing (participants), Status (graphical).
- Routing roles: **Change Requestor** (creator, automatically a Reviewer), **Reviewer** (markups, comments), **Responsible Engineer** (makes the requested design changes in Work state), **Change Administrator** (edits routing, sets effectivity, cancels/reopens), **Approver** (approve/reject); optional Checker role; **unanimous approval** configurable.
- States observed: Open → Work → Review → Ready For Final Review → Approved; closing rules: CO must be Approved, all associated files/items released, **effectivity dates set via the Set Effectivity dialog** ("The Change Administrator must set the effectivity date on the change order to release the items for production"). Cancelled and reopened states exist.
- Rules: "A file can only be associated with one active change order at a time"; "Change orders do not drive file state changes. However, a change order will prevent certain lifecycle state changes for the file depending on the change order's state" — admin option "Restrict File and Item Lifecycle state changes to change-orders" makes the CO the sole gate for release; item added to a CO in Work in Progress gets a new revision per the lifecycle's Bump-revision rule.
- Record base: files AND items — either or both ("ECOs can work in a Vault that's not item-based" — file-level approach supported; item-based adds automated state transitions on approval). Markups via DWF/Composer.

## Cross-product Comparison

| Aspect | PTC Windchill | Arena | Odoo PLM | Duro | Autodesk Vault Pro |
|---|---|---|---|---|---|
| Packaging | PLM suite capability | PLM/QMS suite solution area | ERP module | cloud PLM (CO at center) | PDM vault + change add-on (Pro tier) |
| Change record | ECR / ECO / ECN (three-tier: full CRB/CIB, fast track, basic CN) | ECR / ECO (+ DCO, MCO generated from ECO) | ECO (single object) | Change Order (Engineering/Manufacturing/Documentation types) | Change Order (ECO) |
| Record base | product data across disciplines (items, BOMs, docs, CAD; requirements via OSLC) | items, BOMs, drawings, SOPs, specs, software, quality records | products, BoMs, routings, documents | products, components, documents | files AND items (either or both) |
| Lifecycle | request → board review → order → notice/implementation → release | proposal → review → approval → release/implementation | ECO states (names unconfirmed) | Draft → Open → Finalizing → Closed (+ ON_HOLD) | Open → Work → Review → Ready For Final Review → Approved → Closed/Cancelled |
| Authority | change review board (CRB/CIB) or change admin | automated approval routings by type/priority/product line | simple approvals + followers | approver list; single/dual-stage review templates | routing roles (Requestor/Reviewer/Responsible Engineer/Change Administrator/Approver); unanimous option |
| Effectivity | ECN implementation plans; audit/validate before release | "part effectiveness" in ECO content (guide) | apply differences to BoM | revision snapshot at Finalizing; auto/manual close | Set Effectivity dialog; effectivity date required to release for production |
| Downstream | automatic synchronization with manufacturing systems | automations initiate subsequent processes; ERP integration | triggered alerts to manufacturing (worksheets/work centers) | export package; CAD tools (Onshape, SWX) | release to production |
| Traceability | e-signatures, audit trails | approval history, audit trails | version history | Revision History Table, Compare Revisions | historical record of why/how/when; markups |
| One-active-change rule | not observed | not observed | not observed | yes (component in one open CO) | yes (file in one active CO) |
| Validation | business rules | validation before submit | — | validation engine (errors/warnings) | lifecycle-state restrictions |

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The change record as the unit of work.** A persistent, identified record — realized as a request, an order, a notice, or a single merged object — that carries what is changing, why, who decides, and the outcome, and progresses through a governed lifecycle from proposal to disposition. Remove → version history without governance (PDM/document control) or a generic approval form.
2. **The revisioned engineering record base the change acts upon.** The change record binds to affected engineering objects (parts/items, BOMs, drawings/documents/files, specifications) whose released revisions the change will supersede; an approved change produces new released revisions of those objects. Remove → generic approval workflow with nothing to change.
3. **The governed progression with designated authority and traceability.** Review/approval by a designated authority (change board or configured approvers), recorded decisions (who approved what, when, why), and controlled release of the new revisions — commonly with effectivity (when the change takes effect). Remove → an uncontrolled edit log.

Jointly-held load-bearing tests:

- 1 alone = a ticket/approval form
- 2 without 1 = revision archive (PDM/document control)
- 3 without 1+2 = governance ritual over nothing
- 1+2 without 3 = change log with no authority
- 1+3 without 2 = approval workflow with no engineering objects
- 2+3 without 1 = version control with no change process

### L1 — Common Mature Structure (not definitional)

- Impact / where-used analysis (affected assemblies, open POs, inventory, tooling, documents — Arena blog enumerates; OSLC requirements impact at PTC)
- Affected/affected-by linkage and redlines/diffs (Arena AI redlines; Duro Compare Revisions; Vault markups)
- Electronic signatures and audit trails (PTC, Arena)
- Change categories/types and process-depth tiers (PTC full/fast/basic; Duro DCO vs ECO; Arena DCO/MCO)
- Problem reports / quality events feeding changes (PTC problem report; Arena CAPA→ECO automation)
- Downstream handoff: manufacturing/ERP synchronization (PTC, Odoo, Vault), supplier notification (Arena supply-chain partners)
- Cycle-time analytics and dashboards (Arena, PTC)
- Validation rules before submission (Duro, Vault, PTC business rules)
- One-active-change-per-object rule (Duro, Vault — observed in 2/5; treat as common, not definitional)
- Notifications, followers, email routing (Odoo, Arena, Vault, Duro)

### L2 — Variant / Optional Structure

- Regulated document/design change control (QMS/CAPA-driven; Arena QMS pole; DHF linkage)
- Manufacturing change orders (MCR/MCO) as sibling process over process/equipment records (Arena)
- File-centric (Vault) vs item-centric (Duro, Arena) record base
- ERP-module packaging (Odoo) vs suite packaging (PTC/Arena) vs PDM add-on (Vault) vs standalone-ish cloud (Duro)
- Parallel-version diff/merge editing model (Odoo)
- Paper-era lineage: change request forms → change board minutes → change order authorizing revision change → change notice distribution → redlined drawings + disposition instructions — satisfies the core without any digital machinery

### L3 — Vendor-specific Structure (Research Notes only)

- PTC: full/fast/basic track naming, CRB/CIB boards, deviation/waiver object, OSLC remote requirements, "up to 33% product development time reduction" marketing claim (McKinsey citation — marketing, not structure)
- Arena: AI Item Redline, AI File Insights, no-code Automations trigger/action catalog, ECO cycle-time metric set
- Odoo: enterprise-social-network communication model, parallel BoM version diff/merge, free-forever packaging
- Duro: DCO type semantics (no revision bump), Finalizing stage, auto-close default, validation error catalog, "Last Release" column
- Vault: six-tab CO dialog, routing role names (Change Administrator, Responsible Engineer, Checker), Set Effectivity dialog, DWF/Composer markups, Professional-tier gating

## Boundary Findings

1. **vs Product Lifecycle Management (JOINT REVIEW DISCHARGED — keep-both RATIFIED).** The PLM pass's test — "does a change-centered record world exist independent of the product-record estate?" — is CONFIRMED from this sample: Odoo PLM centers the ECO over records that live in the ERP (products/BoMs owned by other apps); Vault Professional layers change orders over a file/item vault that is PDM-class, not PLM; Duro centers the Change Order over a minimal item/document registry. In the PLM-branded poles (Windchill, Arena) the change process is embedded machinery over the full estate. The seam is center of gravity: PLM owns the product-record estate and the whole-life span; ECM owns the governed change progression that moves engineering records from one released revision to the next. Removal test: remove the estate (CAD vaulting, requirements, quality, portfolio) → the change machinery still functions over any revisioned engineering record base (Odoo/Vault/Duro prove it); remove the change machinery → the estate is a static revision archive. The leaf stands as an independent Type.
2. **vs Bill of Materials Management (JOINT REVIEW DISCHARGED — keep-both RATIFIED).** The BOM pass reserved this leaf for change-centered products spanning wider engineering artifacts. CONFIRMED: the change record base spans items + documents/files/specs/SOPs in every sampled product (Vault is file-first; Arena connects changes to drawings/SOPs/specifications; Duro has a Documentation CO type; Odoo attaches documents to BoMs/routings). The BOM pass's alias risk is mitigated by holding the center as the change process itself: the change workflow scoped to items/BOMs/revisions inside BOM products remains a standard capability of that Type, not this Type's center. Removal test: remove the change process → BOM management continues (structure authoring/release); remove the structure-centered world → ECM continues over documents/files (Vault proves it).
3. **vs IT Change Management (JOINT REVIEW DISCHARGED — keep-both CONFIRMED as the IT pass expected).** Identical governance grammar (request → assess → authorize → implement → review) over different record bases and semantics. ECM's binding: engineering product definition data (parts/BOMs/documents/files), revision-advancement semantics (approved change produces a new released revision), effectivity, manufacturing handoff. ITCM's binding: IT infrastructure/services, service-impact language, CAB, ITSM context. Remove the engineering record base → ITCM territory; remove the IT/service binding → ECM territory.
4. **vs Change Order Management (construction) (JOINT REVIEW DISCHARGED — keep-both CONFIRMED).** The construction pass's seam test holds: ECM has no commercial counterparty, no contract scope/price/time object, no payment consequences; approval is internal cross-functional authority (change board/approvers), and the changed object is design/product data. Remove the commercial contract/counterparty/money structure → ECM territory; remove the design-data/BOM structure → COM territory.
5. **vs Product Configuration Management.** PCM centers the variant space (rules + resolution sessions producing buildable variant definitions); ECM centers the change progression over the record base. A change may alter the configuration model, but that is one affected object among many. Keep-both; consistent with the PCM pass's forward flag.
6. **vs PDM / Engineering Document Management.** Document registers and file vaults manage versions, check-in/out, and release states; ECM adds the governed change process that supersedes versions. Vault shows the seam inside one product: base vaulting is the core; change orders are a Professional-tier governed layer. Remove the change process → document control with versions; add it → this Type's machinery over a document/file record base.
7. **vs QMS / CAPA change control (life sciences).** Regulated change control is a variant realization of the same machinery with regulatory content (Arena QMS pole; DHF/audit framing). Not a separate leaf here; life-sciences QMS is its own directory leaf elsewhere.
8. **vs Manufacturing change (MCR/MCO).** Sibling process over process/equipment records; Arena documents MCO generation from ECO. Variant/adjacent, not the center.

## Historical / Market-Sample Check (§24)

- **Paper-era lineage satisfies the core.** Engineering change request forms → change board review → change order authorizing a revision change → change notice distribution → redlined drawings and disposition instructions. All three L0 legs hold without digital workflow, e-signatures, dashboards, or AI. Therefore digital workflow tooling, e-signatures, impact dashboards, AI redlines, and SaaS delivery are NOT definitional.
- **Regional/ERP variants**: change management embedded in ERP (Odoo; SAP-style ECR/ECO/ECN held at reasoning strength — not fetched) satisfies the core over ERP-owned records.
- **The definition does not over-fit** to the modern cloud PLM implementation: the file-vault pole (Vault) and the ERP-module pole (Odoo) both satisfy the three legs with different record bases and packaging.

## Uncertainties

- Odoo's ECO state machine and operational details are unconfirmed (no Tier-1 docs reachable); only the product page's structural claims are used.
- Exact state names vary by product; states are asserted only where directly observed (Duro, Vault).
- Effectivity semantics beyond date-based effectivity (serial/lot effectivity) were not directly observed in the sample; not claimed.
- Whether a pure standalone ECM product with no record base of its own exists is not observed — and per the L0, the record base is load-bearing, so such a product would be an approval-workflow tool instead.
- The one-active-change-per-object rule was observed in 2/5 products (Duro, Vault); treated as common-mature, not definitional.

## Final Synthesis

Engineering Change Management is the governed change-process record world over a revisioned engineering record base. Its defining core is three jointly-held structures: the change record (request/order/notice, merged or tiered) as the unit of work carrying what/why/who/outcome through a governed lifecycle; the revisioned engineering record base (items, BOMs, documents, files, specifications) whose released revisions the approved change supersedes; and the governed progression with designated cross-functional authority, recorded decisions, and controlled release — commonly with effectivity. The Type appears both embedded in PLM estates (Windchill, Arena) and as a separable change-centered layer over PDM file vaults (Vault), ERP records (Odoo), and minimal item registries (Duro) — which discharges all four joint-review flags as keep-both. The defining core is era-independent: paper-era change forms, boards, notices, and redlines satisfy it.
