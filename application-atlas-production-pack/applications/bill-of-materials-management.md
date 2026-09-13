# Bill of Materials Management

## Overview

A **Bill of Materials Management** application is the system of record for what a product is made of, controlled over time. It holds, for each product or assembly, a structured definition of the items that go into it and in what quantities, and it manages how that definition evolves: every product has a current, released definition, earlier definitions remain retrievable, and every change is recorded.

Its purpose is to solve a coordination problem that spreadsheets and scattered files cannot: engineering, manufacturing, purchasing, and outside partners must all work from the same answer to "which revision of this product is real?" When the structural definition lives in disconnected CAD exports and spreadsheets, teams build from stale versions, purchasing buys the wrong parts, and no one can say what changed or why.

The boundary is drawn by the object of control. This Type manages the **structural definition of the product and its controlled evolution**. It does not primarily manage the CAD files the structure was derived from (that is PDM), does not plan or execute production from the structure (that is Manufacturing ERP / Production Planning), does not track stock on hand (that is Inventory Management), and does not manage commercial selling content (that is Product Information Management). In the market, the same core often ships inside broader PLM suites or ERP modules, but it also exists as a standalone product category.

## Users & Context

The system sits between design and the rest of the manufacturing organization, so its user base is deliberately cross-functional:

- **Design engineers** (mechanical, electrical/electronics) — create and evolve the product structure, usually by pushing it out of CAD tools or importing it; they care that the structure matches the design and that changes are captured.
- **Manufacturing / NPI engineers** — turn the engineering definition into something buildable; they reconcile the engineering structure with how the product is actually sourced and produced, and they consume released revisions.
- **Purchasing / sourcing** — consume the structure to know what to buy, from whom, at what cost; they maintain supplier and manufacturer-part-number information attached to items.
- **Operations / program managers** — check product status, cost roll-ups, and whether changes are in flight before making build or delivery commitments.
- **Contract manufacturers and suppliers** — external recipients of released BOMs, drawings, and specifications; in many products they access a shared or portal surface rather than full internal accounts.
- **Administrators** — manage the item-numbering scheme, categories, roles, and approval rules.

Typical context is a hardware-producing company — electronics, machinery, consumer products, medical devices, aerospace — that has outgrown spreadsheet BOMs. Adoption usually starts at the engineering boundary (replacing exported CAD BOM spreadsheets) and extends outward to procurement and contract-manufacturer handoff. A notable secondary context is process/formulation production (food, chemicals), where the "product structure" is a recipe and the same structural discipline applies.

## Core Model

The world of a BOM management application is built from four kinds of things, and their relationships.

```text
Item records (parts, materials, sub-assemblies)
        ▲ referenced by
Product Structure (BOM): parent item → child items × quantity
        └─ versioned as
Revisions (released snapshots of the definition)
        ▲ changed through
Change records (proposed → approved → released change)
```

### Item records

Every referenced thing — a purchased component, a raw material, a manufactured part, a sub-assembly — exists as an individually identified record: the **item master** (some products call the containers catalogs or part libraries). An item carries its identifying numbers (an internal part number, and typically the manufacturer's part number that identifies it in the wider component world), description, category, suppliers, cost, lifecycle state, documents, and product-specific parameters. Items are the shared vocabulary: the same item record can appear in many products' structures, and correcting or enriching it in one place propagates everywhere it is used. In electronics practice the manufacturer part number is the identity that pins down exactly one form-fit-function-equivalent component; the internal part number is the company's own handle on it.

### Product structure (the BOM itself)

The central object is the product-structure record: a parent product or assembly bound to a list of child items, each with a **quantity and unit of measure** ("each" for most parts; length or volume measures for wire, adhesives, formulations). Structures compose: an assembly's children can themselves be assemblies with their own structure, so the same data can be presented as an indented multi-level hierarchy or flattened into a single parts list for a specific use (purchasing, costing). A BOM line answers three questions — **what item, how much, and where it goes** — with the "where" expressed differently by industry (reference designators in electronics, position or callout conventions elsewhere). What a BOM line must contain is settled practice: item identification, quantity with unit; everything else is enrichment that lives on the item records and is joined at presentation or handoff time.

### Revisions

A structure changes constantly, so each product's definition is **versioned**. A revision is a snapshot of the structure (and of the item definitions it references) that is released for use — by manufacturing, by purchasing, by a contract manufacturer — and then holds still: released revisions do not mutate, changes produce new revisions. Earlier revisions remain accessible, which is what makes questions answerable like "what did we build in the previous production run?" and "exactly what changed between these two versions?" The current released revision is the unambiguous "real" definition of the product.

### Change records

Movement from one revision to the next passes through a change record — a documented proposal (what is changing and why), an approval step with named approvers, and a release that creates the new revision and notifies affected parties. In many products the machinery distinguishes a lightweight **change request** (documenting a proposed modification) from a **change order** (an approved, batched implementation, often bundling several related changes). The change record is where the *why* of product history lives, attached to the revisions it produced.

### One structure, many implementations

The core is conceptual, and products implement each piece differently:

```text
Concept:                  Common implementations:
Item identity             internal part-number scheme; manufacturer part number (MPN)
                          as world identity; vendor/distributor numbers linked to one item
Structure presentation    indented multi-level tree; flat/rolled-up list; spreadsheet-like grid
"Where it goes"           reference designators (electronics); position/callout numbers;
                          assembly-sequence context
Versioning                revision letters/numbers on items and BOMs; immutable baselines;
                          effective-dated definitions
Change machinery          change request → change order → release; single-record workflows;
                          batched orders bundling multiple requests
```

## How It Works

A BOM management application is used through one recurring lifecycle with several loops around it.

### Authoring: get the structure in

```text
Design in CAD (or decide by hand)
→ extract/import the assembly structure (CAD integration, spreadsheet import,
  or manual entry against the item master)
→ resolve each line to an item record (matching or creating part numbers)
→ enrich: suppliers, costs, documents, parameters
```

The dominant authoring path in modern products is CAD synchronization: the CAD assembly is the source of the initial structure, and the application matches its components to item records — reusing existing items wherever possible rather than minting duplicates. Non-modeled items (fasteners, labels, adhesives, packaging) are added by hand. Spreadsheet import is the common migration path from the state the system replaces.

### Stewardship: keep one definition healthy

While the structure is in development, users work on it collaboratively: adding and correcting items, checking whether a component is already used elsewhere (**where-used**), flagging alternates for hard-to-source parts, and discussing open questions attached to the records themselves. Because item data is shared, an engineer fixing one part record fixes it for every product that uses it. Cost is a live derived view: unit costs times quantities, rolled up through sub-assemblies to the finished product.

### Change: evolve the definition under control

```text
Something must change (part obsolescence, supplier switch, design fix)
→ raise a change record describing what and why
→ impact check: where-used across the product line, cost delta, affected builds
→ review and approval (named approvers, notifications)
→ release: new item and/or BOM revision created; prior revision frozen
→ affected parties notified (internal teams, contract manufacturers)
```

This is the loop that separates *management* from *listing*. The rules of the loop — nothing changes without a record, released things don't mutate, the current definition is always identifiable — are the point of the whole system. Comparison tooling supports it directly: any two revisions of a structure can be diffed item by item, and the diff feeds both the approval decision and audit needs.

### Handoff: give the definition to the people who build on it

The released definition flows outward in controlled form:

- **To contract manufacturers and suppliers** — as shared workspaces, vendor portals, or generated packages combining the BOM with drawings and specifications, always pulled from the current released data rather than emailed static files; recipients are notified when it changes.
- **To procurement and ERP** — item, quantity, and supplier data synchronized into purchasing and business systems, so what is bought matches what was designed. Some products create a distinct "order BOM" from a released revision for this purpose.
- **To production** — in products that go further, the BOM feeds material planning and build records; the build is pinned to a specific released revision, which is what makes "what exactly went into unit #441" answerable.

## Interfaces

The same handful of surfaces recur across products, presented in a utilitarian, data-dense style (frequently spreadsheet-like grids) because the primary content is tabular structure.

- **BOM workspace / structure editor** — the primary surface. Shows the product's structure as an expandable tree or grid; each line shows the item, quantity, unit, references, cost, and status. Primary actions: add/remove lines, change quantities, switch between multi-level and flat views, open an item, initiate a change.
- **Item / part detail** — one item record: identifiers, description, suppliers and manufacturer numbers, documents, cost history, lifecycle state, where-used across products. Primary actions: edit attributes (permission-gated), attach files, view usage, propose a change.
- **Where-used view** — reverse lookup from an item to every product and sub-assembly that consumes it. Primary actions: open a consuming BOM, assess change impact.
- **Revision history & compare** — the list of a structure's revisions with release metadata (who, when, why), and a side-by-side diff of any two revisions showing added, removed, and changed lines. Primary actions: compare, retrieve a prior revision, export the diff.
- **Change workspace** — the queue and detail for change records: proposed changes, approvals owed, recently released. Primary actions: create a change, review and approve, check impact, release.
- **Sharing / handoff surface** — generated exports or governed share links/portals for contract manufacturers and suppliers, and sync configuration for ERP/procurement targets. Primary actions: select scope, publish or sync, view what was sent and when.
- **Dashboards / status** — product-level status (draft vs released, changes in flight), cost roll-ups, and lead-time or shortage signals where the product includes sourcing data.

## Important Rules / Behaviors

- **Released revisions are immutable.** Once a definition is released for building, it does not change in place; a change produces a new revision. This is the rule that makes "which version is real" answerable and is enforced (not merely encouraged) in mature products.
- **Every change leaves a record.** Who changed what, when, and why is retained and attributable. Discussion and decision context stays attached to the BOM, item, or change record rather than living in email.
- **The structure references shared item records.** Editing item data in one place affects every structure that references it; duplicating an item instead of reusing the existing record is treated as a data-quality failure, and where-used exists precisely to catch it.
- **Identification completeness.** A BOM line without an unambiguous item identity, quantity, and unit is incomplete by the discipline's own standards; products validate for this. Whether a modification requires a *new item* or just a *new revision* hinges on interchangeability: if form, fit, function (or formulation) changes, it is a different item.
- **Change gating by role.** Who may edit draft structures, who may approve, and who may release are permission-controlled. Consumers (purchasing, operations, external partners) typically see released data read-only.
- **Handoff shows the released state, not the work-in-progress.** Partners and downstream systems receive released revisions; work-in-progress changes are visible internally (and surfaced as "changes in process") but not mistaken for the current buildable definition.
- **Builds pin to revisions.** Where production is traced, a build is executed against a named released revision, so the system can always answer what definition a given unit was built to.

## Variants

- **Electronics-centric** — manufacturer-part-number identity, distributor data, reference designators, approved alternates, and packaging-variant handling are first-class; deep CAD/ECAD integration.
- **Mechanical / machine design** — CAD-driven structure with drawing and document attachments; emphasis on engineering change discipline and release to manufacturing.
- **Process / formulation** — the structure is a recipe: materials with fractional or percentage quantities, intermediates, and batch context; the same revision and change discipline applies.
- **Contract-manufacturer-facing** — organized around producing clean, current, governed handoff packages to outside builders, with portal access and change notifications for the recipient.
- **Standalone vs suite module** — the same core is sold standalone (often bottom-up, low-administration, cloud) and as the structural module of enterprise PLM or ERP suites, where it gains formal multi-view disciplines (as-designed vs as-built structures), effectivity control, and deep estate integration.
- **MRP-flavored SMB editions** — at the small-manufacturer end, BOM management commonly expands to include inventory, purchasing, and material planning, blurring toward lightweight ERP; the structural core remains the anchor.
- **Regulated-industry deployments** — aerospace/defense and medical variants add security boundaries, audit emphasis, and compliance evidence around the same core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Product Lifecycle Management / PLM | broader; frequent packaging host | PLM manages the full lifecycle estate — CAD vaulting, documents, requirements, quality, portfolio workflows; BOM management is its structural spine, and stands alone when the item/BOM/revision world is the center of gravity |
| Engineering Change Management | sibling discipline, embedded here | change workflow is a standard capability inside BOM management scoped to items/BOMs/revisions; a change-management-centered Type spans wider engineering artifacts (documents, files) as its primary objects |
| Manufacturing ERP / Production Planning | downstream consumer | ERP consumes the BOM for planning, costing, and execution; BOM management owns authoring and controlled definition, then hands off. At the SMB end the two blur as BOM products grow planning features |
| Inventory Management System | adjacent, often bundled | inventory tracks quantities on hand in locations; BOM management tracks structure. Bundling is common but optional |
| CAD / PDM | upstream source | PDM vaults and versions CAD documents; BOM management versions the *structural definition* derived from them. A CAD assembly's BOM is an input here, not the managed object |
| Product Information Management / PIM | unrelated-looking, name-adjacent | PIM manages commercial catalog content for selling channels; BOM management manages engineering/manufacturing structure. Different vocabularies (selling attributes vs part numbers and quantities) |
| Product Configuration Management | adjacent for variant-heavy products | configurable BOMs (options, variants) appear here as an optional capability; a configuration-centered Type makes rule-driven variant definition its primary object |

## Representative Products

- **OpenBOM** — cloud-native collaborative product-data platform; catalogs + BOMs information model, real-time multi-user editing, CAD integrations, revision/change control, ERP sync.
- **Aligni** — standalone PLM+MRP for electronics; item-master discipline, where-used, BOM compare, cost sheets, vendor vaults; explicit minimal-BOM doctrine.
- **Duro** — hardware PLM with BOM as the digital-thread foundation; GitHub-inspired change management, CAD/MES/ERP integrations, aerospace/defense posture.

The same capabilities also ship as the structural module of enterprise PLM suites and ERP systems; those suite implementations were not directly researched for this document and are mentioned as market context only.

## Sources

Research date: **2026-09-06**

- OpenBOM — BOM Management capability: https://www.openbom.com/bom-management-capability
- OpenBOM — Revision Control: https://www.openbom.com/revision-control
- OpenBOM — product overview: https://www.openbom.com/
- Aligni — BOMs and Revisions: https://www.aligni.com/product/boms-revisions/
- Aligni — Documentation, "Mastering the BOM": https://docs.aligni.com/guides/mastering-the-bom/
- Aligni — product overview: https://www.aligni.com/
- Duro (Duro Labs) — Design PLM product page: https://durolabs.co/product-lifecycle-management/
- Duro — product overview: https://www.duroplm.com/

> Sourcing limitation: Arena (arena.io) was unreachable from the research environment (repeated transport errors) and contributes no direct evidence; a general-reference article on bills of materials timed out and was abandoned. Product claims in this document rest on the three sampled vendors' official pages and documentation. Enterprise PLM/ERP suite documentation was not fetched (gated); statements about suite-embedded implementations are kept generic. Precise operational details (numeric limits, exact workflow states, plan-specific features) are intentionally not asserted; detailed observations are recorded in the paired Research Notes.
