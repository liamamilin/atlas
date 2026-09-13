# Product Lifecycle Management / PLM

## Overview

A **Product Lifecycle Management (PLM)** system is the manufacturer's system of record for the product's definition across its life. It holds the authoritative, revision-controlled definition of what a product is — its parts, its structure, its documents and design files — governs how that definition changes through formal change processes, and carries the record from development through release into production, serving not only engineering but manufacturing, quality, procurement, and the supply chain.

The defining core is deliberately small:

```text
Product Record (the product's system of record)
└── Definition data (items/parts + product structure + documents/design files, revision-controlled)
    └── Controlled change (request → review/approval → order → release)
        └── Whole-life, whole-organization span
            (beyond engineering design → release into production → commonly service/retirement;
             consumed by functions beyond engineering; released definition handed to ERP/production)
```

Everything else the market associates with PLM — CAD vaulting, requirements management, quality processes, manufacturing process planning, supplier collaboration, compliance content, cost management, digital-thread and AI vocabulary — is standard capability of mature products or industry/deployment packaging, not what makes the system a PLM. A design-team file vault with CAD versions (PDM) or a standalone bill-of-materials tool sits outside this core; so does the ERP that consumes the released definition.

## Users & Context

PLM is used by product-making organizations — discrete manufacturers (aerospace, automotive, industrial equipment, electronics, medical devices) and, in an industry variant, consumer-goods companies (fashion, food, home goods). The common context is a product whose definition is too complex and too consequential to hold in spreadsheets and shared drives: many parts, multiple design disciplines, suppliers and contract manufacturers, regulatory exposure, and a production process that must build exactly what engineering released.

Primary users and their relationship to the record:

- **Design and development engineers** (mechanical, electrical, software/firmware, and in industry variants garment technologists or food technologists) — create and revise the definition: items, structures, drawings, design files, specifications.
- **Component or parts engineers** — manage the part population: classify parts, document replacements for unavailable or end-of-life components, drive reuse instead of duplication.
- **Manufacturing and process engineers** — consume the released engineering definition and prepare manufacturing-ready structures and process documentation from it.
- **Procurement and supply chain teams** — review structures, approved manufacturer and vendor lists, and pending changes before placing orders.
- **Quality teams** — review designs and documentation for compliance, and link quality processes to the product record.
- **Supply chain partners, suppliers, and contract manufacturers** — review and approve the latest released designs inside the same record, under controlled access.

Secondary users:

- **Executives and program managers** — track product releases, milestones, and change activity against launch dates.
- **PLM administrators** — configure workflows, approval routings, data models, and access.

The work environment is cross-functional by construction: the defining promise of the Type, in vendors' own words, is that *everyone on the team — not just engineering — works from the same product record*. Some products additionally provide simplified, role-based views so that people who never author the definition can still consume it safely.

## Core Model

### The Defining Core

Four structures, held together. Remove any one and the system stops being a PLM:

**1. The product record.** A persistent, identified record of the product — the container to which the product's data attaches: its items, its structure, its documents, its changes, its quality history. Vendors across the market name this center directly: the "product record," the "single source of product information," the "system of record for product data." The product record is what makes PLM a *system of record* rather than a collection of tools.

**2. The definition as structured, revision-controlled data.** Inside the record, the product's definition is held as structured data, not files alone:

- **Items (parts)** — the individually identified building blocks of the product: purchased components, fabricated parts, assemblies, and in industry variants materials, styles, or recipe lines. Each item carries its identification, its attributes, and its revision.
- **Product structure (the bill of materials)** — the hierarchical arrangement of items that defines how the product is built, commonly with associated files, drawings, and specifications. The structure's form follows the industry: a parts BOM in discrete manufacturing, a materials BOM in fashion, a formula in food.
- **Documents and design files** — specifications, drawings, procedures, and the design files produced by CAD and other authoring tools, attached to the record and held under the same revision discipline.

Revision control is the load-bearing property: the definition exists as a sequence of identified revisions, so the organization can always answer "which version of the product is the released one?"

**3. Controlled evolution.** The definition does not change by editing in place. Changes enter through a formal process — a change request proposing and justifying the change, a review and approval step (often a change review board or named approvers, with electronic signatures), a change order or notice that authorizes and plans implementation, and a release that produces new revisions of the affected items, structures, and documents. The process leaves a traceable, auditable trail connecting every change to what it changed, who approved it, and when it took effect.

**4. The whole-life, whole-organization span.** The record's governance extends beyond the engineering design phase. At minimum it runs through release into production, with the released definition handed to downstream systems — ERP and manufacturing systems consume it for planning, procurement, and execution. Mature deployments commonly extend the span through service and end-of-life. And the system's audience is the whole organization: manufacturing, quality, procurement, supply chain partners, and executives work from the same record engineering created. This span is what separates PLM from its design-team ancestors — vendors themselves draw the line exactly here: product data management (PDM) serves engineering workgroups' design data; PLM manages the product's data and processes for the whole lifecycle and the whole team.

### Standard Capabilities of Mature Products

Mature PLM products commonly carry a wide estate around this core. These capabilities make PLM practical; they are not what makes a system a PLM:

- **CAD and design-tool integration** — connecting the authoring tools (mechanical CAD, electrical CAD) to the record: design files checked into the system, associated with items, and visualized (often in 3D, in a browser) by people who do not own the authoring tools. Depth varies widely across the market, from deep vaulting and multi-CAD management to integration-level connectivity.
- **Manufacturing process planning** — transforming the engineering structure into manufacturing-ready structures and process documentation (engineering BOM to manufacturing BOM, process plans, work instructions).
- **Parts classification and component engineering** — organizing the part population for search and reuse, flagging duplicates, and tracking supplier and manufacturer approvals (approved vendor / manufacturer lists).
- **Supplier and external collaboration** — controlled access for suppliers and contract manufacturers to review and approve designs inside the same record.
- **Quality management** — closed-loop quality processes (issues, corrective actions, audits) linked to the product record; in some market offerings a separately sold quality-management product shares the same record and change machinery.
- **Requirements management** — capturing requirements and linking them to the definition for traceability.
- **Project and program management** — tasks, milestones, and deliverables tracked against the product record.
- **Compliance content** — environmental (restricted substances), export-control, and industry-regulatory data attached to items and structures.
- **Cost management, simulation data management, analytics** — estate extensions at the high end.
- **Digital thread and digital twin framing, AI assistants** — the current era's vocabulary and tooling layered over the record; conceptually, the record's connectedness is what these marketing terms describe.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:            Product record
Realizations:       item-and-document record; multi-discipline product data; style/season record; formula record

Concept:            Definition data
Realizations:       parts BOM (discrete manufacturing); materials BOM (fashion); recipe/formula (food);
                    CAD files + drawings + specifications attached at any of these levels

Concept:            Controlled change
Realizations:       request/order/notice process chains with review boards and e-signatures;
                    lightweight change notices; automated approval routings by change type or product line

Concept:            Whole-life span
Realizations:       concept → production (mid-market cloud pole);
                    concept → manufacturing → service → end-of-life (enterprise pole);
                    pre-season → in-season → end of season (consumer-goods pole)
```

A reader who has only seen one implementation — say, a cloud PLM for a hardware startup — should still be able to recognize an enterprise deployment managing a multi-discipline aircraft definition, or a fashion PLM managing styles and seasons, from the same core.

## How It Works

PLM's work flows through a small number of defining loops.

### Build the product record

```text
Create the product
→ create or import items (parts, materials)
→ build the product structure (BOM)
→ attach documents, drawings, and design files
→ classify parts; link approved manufacturers and vendors
```

Items arrive by creation inside the system or by import from design tools and component databases; structures are assembled from items; documents and CAD files attach to the items and assemblies they describe. From this point the record — not a spreadsheet or a shared drive — is the product's definition.

### Release a design

```text
Assemble the definition at a working revision
→ route it for review (engineering, and commonly quality, manufacturing, procurement, supply chain partners)
→ approvals recorded (electronic signatures where required)
→ release: the revision becomes the authoritative definition
→ downstream systems can receive it
```

Release is the hinge of the whole Type. Before release, the definition is work-in-progress; after release, it is what the organization builds, buys, and sells against. Collaboration before release is the point of the shared record: dispersed teams and external partners review the *entire* design — mechanical, electrical, software, documentation — in one place.

### Change the product

```text
Problem, opportunity, or improvement identified
→ change request (justify: what and why)
→ review and approval (review board or routed approvers; e-signatures)
→ change order / notice (plan and authorize implementation)
→ affected items, structures, documents revised
→ new revisions released; traceability and audit trail retained
→ downstream systems synchronized with the resolved change
```

This loop is the operational heart of a mature deployment, because products change constantly after first release: components go end-of-life, suppliers change, defects surface, costs and regulations shift. The change process keeps those changes controlled — nothing silently edits the released definition — while keeping them fast enough to keep pace with production. Some products scale the process from lightweight notices to full review-board tracks depending on the change's risk; some capture temporary deviations through the same machinery.

### Hand off to manufacturing

```text
Released definition in PLM
→ transfer of validated, released data to ERP / manufacturing systems
→ planning, procurement, and production build against the released revision
→ changes re-sync the handoff when released revisions change
```

The direction of truth is one-way at the seam: PLM defines and releases; ERP consumes for planning, procurement, and execution. Vendors state this division explicitly — only validated, released product data crosses into the business systems.

### Collaborate across functions

Throughout all loops, the record is the shared surface: engineers see design context; procurement sees structures and pending changes before ordering; quality sees designs and links quality processes; supply chain partners review and approve inside controlled access; executives see release and milestone status. Role-based views for non-expert consumers of the data are a common maturity marker.

### Core vs Common vs Optional

**Defining core** — without these, not a PLM:

- product record as the system of record
- structured, revision-controlled definition data (items, structure, documents/design files)
- formal controlled change producing new revisions
- whole-life, whole-organization span with release into production and downstream handoff

**Standard mature capabilities** — present in most modern products:

- CAD/design-tool integration and visualization
- manufacturing process planning / BOM transformation
- parts classification and component engineering
- supplier/external collaboration
- quality processes linked to the record
- requirements management
- project/program management
- compliance content
- analytics and reporting

**Variant / optional** — depends on industry, scale, deployment, and regulatory posture:

- deployment substrate (on-premises, vendor cloud, multi-tenant SaaS, government cloud)
- packaging philosophy (broad suite vs packages vs platform-with-apps vs fixed cloud platform)
- industry record content (parts/CAD vs styles/seasons vs formulas)
- quality as bundled module vs separately sold product
- cost management, simulation data management, portfolio planning
- digital-thread/digital-twin tooling and AI assistants

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Product / item explorer

The record's backbone surface.

- lists and searches the item population and product structures
- typical information: item identification, revision and lifecycle state, structure hierarchy, attached documents and files, supplier/manufacturer links
- primary actions: create or import items, assemble structures, open an item's detail, compare revisions

### Structure (BOM) view

The definition's hierarchical surface.

- shows the product's structure as a navigable, often multi-level tree or table
- typical information: part numbers, quantities, revision states, effectivity context, attached drawings
- primary actions: add/remove/reorder lines, redline a pending change, compare revisions, export

### Change workspace

The controlled-evolution surface.

- lists change requests, orders, and notices with their states and approvers
- typical information: affected items and documents, justification, approval status, implementation plan, audit trail
- primary actions: create a change, route for approval, record sign-off, implement and release

### Document / file library

The record's document surface.

- holds specifications, drawings, procedures, and design files under revision control
- primary actions: check in / revise, review and approve, view (often including 3D visualization of CAD content without the authoring tool)

### Review and collaboration surface

Where cross-functional and external review happens.

- design reviews with comments and markups; supplier/partner access under controlled roles
- primary actions: review, comment, approve or reject, track decisions

### Dashboards and reporting

The management surface.

- release status, change activity and cycle times, program milestones
- primary actions: track, filter, report

Some products extend access to non-expert consumers through simplified role- or task-based views of the same record.

### Administration / configuration

The system-shaping surface.

- workflows, approval routings, data models, roles and permissions, integration configuration
- primary actions: configure processes, manage access, maintain integrations

## Important Rules / Behaviors

### Released revisions are the buildable truth

The organization builds, buys, and sells against released revisions. Working revisions in progress are not authoritative; the release step is what promotes a definition to truth. This is the discipline the whole record exists to enforce.

### The definition changes only through the change process

Editing a released item outside a change order is not how the system works: changes are proposed, approved, and implemented as tracked operations that produce new revisions. The audit trail — who changed what, who approved, when it took effect — is a first-class output, and in regulated deployments a compliance requirement.

### One record, controlled access

The same record serves internal functions and external partners, under role-based access: suppliers may review and approve what they are entitled to and nothing more. Intellectual-property protection is a structural concern, not an afterthought.

### The PLM→ERP seam passes released data only

Downstream business systems receive validated, released definitions. Unreleased work-in-progress does not flow to planning and procurement. When released revisions change, the handoff re-synchronizes.

### Traceability binds the estate

Changes link to the items, structures, documents, and quality processes they affect; requirements link to the definition; approvals link to the change records. The record's value — and the reason it replaces spreadsheets — is that these links are maintained by the system rather than by memory.

### Lifecycle states govern behavior

Items, structures, documents, and change objects carry lifecycle states (working → released → obsolete is the canonical conceptual pattern; exact labels vary by product). State determines what actions are legal: a released item generally cannot be edited in place; an obsolete item is retired from new designs but its history remains.

## Variants

- **Enterprise suite PLM** — the broadest estate (design data, manufacturing process planning, simulation data, compliance, cost) for large discrete manufacturers; typically deployable on-premises, in the customer's cloud, or as vendor-operated SaaS.
- **Packaged / role-based PLM** — the estate sold as packages and role- or task-based applications, including lightweight views for non-expert consumers of product data.
- **Platform-based PLM** — a configurable data platform with composable applications and low-code extension, positioned for organizations that tailor their lifecycle processes; open community editions exist at this pole.
- **Cloud-native mid-market PLM** — multi-tenant SaaS with fast onboarding, often paired with a separately sold quality-management product sharing the same record; serves startups through large companies.
- **Industry PLM (consumer goods)** — fashion, food, and consumer-goods realizations where the record's content is styles, seasons, colorways, materials BOMs, or formulas rather than parts and CAD; the lifecycle rhythm follows seasons and the compliance content follows consumer-goods regulation.
- **Regulated-industry deployments** — aerospace/defense, medical device, and similar regimes add traceability, document-control, and audit depth; the machinery remains the generic record core, with regime-specific record chains typically carried by companion quality or regulatory products.
- **Government cloud variants** — sovereign/federal deployment postures of the same Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Bill of Materials Management | closest sibling | the item/BOM/revision structure is the managed world; PLM's estate spans that structure plus documents, quality, suppliers, process planning, and the whole-life span — the BOM core is extractable and independently sellable |
| Mechanical CAD | upstream authoring tool | MCAD authors and maintains the model itself; PLM manages product data and processes above the model; CAD integration depth in PLM varies and is not identity |
| Engineering Document Management | adjacent register | EDM centers the document register for engineered assets/projects regardless of product structure; in PLM, documents are one record class beside items and structures |
| ERP / Manufacturing ERP | downstream consumer | ERP consumes the released definition for planning, procurement, execution; PLM defines and releases; the seam passes released data only |
| Manufacturing QMS | companion quality system | the quality-event/action loop (deviations, CAPA, audits) is the quality system's evidence of record; in PLM, quality is a linked capability or a separately sold product sharing the record |
| MBSE Platform | complementary model world | MBSE's system model is the system-of-record for architecture; PLM's record world is the product data estate; modeling appears inside PLM as one application, not the estate |
| Product Configuration Management | variant-space layer | PCM owns the rule-governed variant space that resolves into concrete buildable definitions; PLM hosts variant management as one capability inside the estate |
| Engineering Change Management | embedded process vs standalone center | every PLM embeds change management over its record; a standalone change-centered Type would own the change process across engineering objects without the product-record estate |
| Medical Device Lifecycle Management | regime-specific record chain | the device design-control/risk-file/submission chain is its own record world; enterprise PLM serves device makers with generic machinery plus industry packaging, and device-regime depth lives in companion products |
| Product Information Management / PIM | different record world | PIM manages commercial/catalog content for selling channels; PLM manages the engineering/manufacturing definition; vendors sell them as separate product lines |
| Digital Twin Platform | operational counterpart | the twin platform centers a persistent digital object standing for a specific physical asset in operation; PLM's record is the development-to-production definition; "digital twin" vocabulary over the record is era framing |

The most important boundary is with **Bill of Materials Management**: the two Types share the item/structure/revision spine, and the market's packaging blurs them (structure-centered tools brand themselves PLM; PLM products sell their BOM layer by name). The discriminator is the center of gravity — if the item/BOM/revision structure is the managed world, it is BOM management; if the record spans the definition estate, the change process over it, and the whole-life whole-organization span, it is PLM.

## Representative Products

- Siemens Teamcenter
- PTC Windchill
- Aras Innovator
- Arena PLM (Arena, a PTC business)
- Centric PLM (Centric Software)

The core was checked across enterprise suites, platform-based, cloud mid-market, and consumer-goods industry poles to avoid over-fitting the definition to any one deployment model, customer tier, or industry's record content.

## Sources

Research date: **2026-09-09**

- Siemens — Teamcenter product page: https://www.siemens.com/en-us/products/teamcenter/
- PTC — Windchill product page: https://www.ptc.com/en/products/windchill
- PTC — Engineering Change Management: https://www.ptc.com/en/technologies/plm/engineering-change-management
- Aras — home and PLM capability pages: https://www.aras.com/ , https://aras.com/en/capabilities/product-lifecycle-management
- Arena — PLM product page, Engineering Change Management, Item & BOM Management, and "What Is PLM?": https://www.arenasolutions.com/platform/plm/ , https://www.arenasolutions.com/solutions/engineering-change-management/ , https://www.arenasolutions.com/solutions/item-bom-management/ , https://www.arenasolutions.com/what-is-plm/
- Centric Software — home page: https://www.centricsoftware.com/

> Sourcing limitation: vendor help centers and product documentation portals were not reachable this pass (PTC help center 404; Siemens documentation gated; no public help center for Arena; one startup-tier cloud PLM vendor and one CAD-vendor-adjacent mid-market vendor unreachable after repeated attempts). All evidence is product/solution-page strength. Precise operational details — exact lifecycle state names, revision-number schemes, workflow step sequences, and numeric limits — are intentionally not stated in this document; conceptual patterns (working → released → obsolete; request → approval → order → release) are stated as the canonical pattern with exact labels varying by product.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against sibling Types are recorded in the paired Research Notes.
