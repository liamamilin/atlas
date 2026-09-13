# Engineering Change Management

## Overview

An **Engineering Change Management** application governs how changes to a product's engineering definition are proposed, evaluated, approved, and put into effect. Its world is built around a change record — commonly realized as an engineering change request, change order, or change notice — that travels through a controlled lifecycle and, when approved, supersedes the released revisions of the engineering objects it affects: parts, bills of materials, drawings, documents, files, and specifications.

The defining structure is small:

```text
Change record (request / order / notice)
└── binds to affected revisioned engineering records
    │   (items, BOMs, drawings, documents, files, specifications)
└── governed progression
    │   (propose → assess → approve → implement → release)
└── recorded decisions and controlled release
        (who approved what, when, why — often with effectivity)
```

Everything else commonly associated with modern products — electronic signatures, impact dashboards, AI-assisted redlines, automated routing, cycle-time analytics — is widespread in current products but is not part of the defining core. Paper-era practice (change request forms, change board minutes, change orders, change notices, redlined drawings) satisfies the same structure without any of it.

When the center of gravity shifts to owning the whole product-record estate across the product's life, the product is a Product Lifecycle Management system; when it shifts to a commercial contract's scope, price, and time among contracting parties, it is construction change order management. The change process itself — not the estate, not the contract — is what this Type owns.

## Users & Context

The primary users are people who work on a product's engineering definition and the people who must agree before that definition changes:

- **engineers / requesters** — identify a need (design improvement, component obsolescence, quality event, cost reduction, customer or regulatory requirement) and raise a change request
- **responsible engineers / change owners** — prepare the change: identify affected records, make the design changes, assemble the implementation plan
- **approvers / change board members** — cross-functional reviewers (engineering, manufacturing, quality, procurement, sometimes regulatory, service, or external supply-chain partners) who evaluate impact and approve or reject
- **change administrators / document control** — configure the process, manage routings, set effectivity, and keep the audit trail

The work context is a manufacturing or product-development organization where a product's definition — what the part is, how it is drawn, how it is built — must stay controlled: an unapproved edit to a released drawing or BOM can send a supplier fabricating from the wrong revision. The characteristic tension the application manages is speed of change against control of the released record.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being recognizable as this Type.

**1. The change record — the unit of work.**

A persistent, identified record that carries what is changing, why it is changing, who must decide, and the outcome. Products realize it in one or more forms:

- a **request** (engineering change request) documenting the problem or opportunity and the justification
- an **order** (engineering change order) authorizing the change against an established baseline
- a **notice** (engineering change notice/notification) delivering the implemented change to the enterprise

Some products keep all three as separate record types; others merge them into a single change object with phases. Both realizations satisfy the same structure: a formal, tracked record moving from proposal to disposition. The record typically names the affected records, the reason (design improvement, obsolescence, quality event, cost, customer request, regulatory requirement), the approvers, and the outcome (approved, rejected, withdrawn).

**2. The revisioned engineering record base the change acts upon.**

The change record binds to the engineering objects it affects — parts/items, BOMs, drawings, documents, CAD files, specifications, procedures. These objects exist as sequences of identified revisions, and an approved change produces new released revisions of the affected objects. The record base is wider than BOMs alone: in mature products a change routinely touches documents, files, and specifications alongside items and structures. This binding is what makes the application engineering change management rather than a generic approval workflow — the change record is meaningless without the revisioned records it supersedes, and the records are uncontrolled without the change process.

**3. The governed progression with designated authority and traceability.**

The change record moves through a defined lifecycle — commonly propose → assess → approve → implement → release — and each decision is recorded: who approved what, when, and why. Approval authority is cross-functional and configurable: a standing change review board in process-heavy organizations, or a per-change approver list elsewhere. Release of the new revisions is controlled, commonly gated by an effectivity decision (when the change takes effect). Without the governed progression, the record base is just a version archive; without traceability, the process cannot support audits or quality investigations.

### Capabilities Shared by Mature Products

These are widespread in current products and make the process practical, but they do not define the Type:

- **impact / where-used analysis** — identifying what the change touches beyond the immediate item: parent assemblies, open purchase orders, existing inventory, tooling, work instructions, related documents, quality records
- **redlines and revision comparison** — showing what differs between revisions of an affected record (before/after highlighting, markup overlays, automated change summaries)
- **electronic signatures and audit trails** — recorded sign-offs attached to the change record and the affected data
- **change categories and process-depth tiers** — lightweight paths for documentation-only changes versus full board review for form/fit/function changes; separate types for engineering, manufacturing, and documentation changes
- **problem reports and quality links** — issues, nonconformances, and corrective actions feeding the change process (and changes feeding quality processes back)
- **downstream handoff** — publishing resolved changes to manufacturing systems, ERP, or supply-chain partners
- **validation before submission** — rule checks (missing data, status requirements, conflicting changes) that block or warn before review
- **cycle-time analytics** — measuring how long changes spend at each stage

### One Structure, Many Implementations

```text
Concept:   Change record
Realizations:  three-tier request/order/notice chains; single merged change object;
               typed variants (engineering / manufacturing / documentation)

Concept:   Record base
Realizations:  item/BOM registries; file vaults; ERP product records; document registers

Concept:   Authority
Realizations:  standing change review boards; per-change approver lists;
               configured routing roles with unanimous or majority decision rules

Concept:   Effectivity
Realizations:  effectivity dates set at release; revision snapshots at approval;
               automatic close on approval vs manual close after implementation
```

A reader who has only seen one implementation should still be able to recognize the others from the defining core.

## How It Works

### The change loop

The defining workflow is one governed loop from recognized need to released change:

```text
Recognize the need
  (design improvement, obsolescence, quality event, customer/regulatory requirement)
→ raise a change request
  (what is changing, why, affected records, proposed resolution)
→ assess impact
  (where-used, affected assemblies/documents/inventory, cost and schedule where tracked)
→ review and approve
  (designated authority evaluates; decision recorded; rejection sends it back for revision)
→ implement
  (make the design changes; prepare new revisions of affected records)
→ release with effectivity
  (new revisions become the released definition; downstream systems and
   stakeholders are notified of when the change takes effect)
```

Two properties of this loop matter more than any individual step:

- **Approval is a gate on release, not on editing.** Engineers can typically work on proposed changes freely; the released revision only advances when the change record is approved and the implementation is complete. A rejected change returns to its owner for revision and resubmission — the record persists rather than restarting.
- **The change record is the traceability spine.** The reason for the change, the records it affected, the people who approved it, and the implementation work all link back to the change record, so "why is this part at revision D?" is answerable from the record.

### Supporting loops

- **Problem → change**: issues, nonconformances, or corrective actions raise change requests; some products automate the handoff (a corrective action generating a change order).
- **Change → downstream**: on release, updated definitions are published to manufacturing/ERP systems, and supply-chain partners can be notified or involved in review before release.
- **Change → change**: one change can trigger subsequent changes (a design change generating a documentation change or a manufacturing-process change).

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- change record as the unit of work
- binding to a revisioned engineering record base
- governed progression with designated authority, recorded decisions, and controlled release

**Common mature structure** — present in most modern products:

- impact/where-used analysis
- redlines / revision comparison
- e-signatures and audit trails
- change types and process-depth tiers
- problem/quality links
- downstream handoff to manufacturing/ERP
- validation before submission
- cycle-time analytics

**Variant / optional** — depends on industry, regulation, and packaging:

- regulated change control (design-history and audit framing for medical and other regulated products)
- manufacturing change orders as a sibling process
- file-centric vs item-centric record base
- parallel-version diff/merge editing
- standalone, suite-module, ERP-module, or PDM add-on packaging

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Change record workspace

The center of work for any single change.

- what is changing (affected records with their current revisions), why, description and attachments
- approver list, notifications, comments, decision history
- primary actions: create, add/remove affected records, submit for approval, approve/reject, withdraw, close

### Change list / board view

The queue and portfolio surface.

- lists change records with status, age, owner, type
- surfaces what is waiting on whom; overdue or stalled changes
- primary actions: filter, open a change, reassign, escalate

### Affected-records view / where-used

The impact surface.

- for a change: the records it will supersede, with their revision and release state
- for a record: the change history that produced each revision
- primary actions: add affected records, inspect a record's where-used, jump to a revision

### Revision history / comparison

The record's memory.

- per record: the sequence of changes that produced each revision (who, when, what type, resulting revision and status)
- comparison between any two revisions with differences highlighted
- primary actions: compare revisions, open the change record behind a revision

### Administration / process configuration

The governance surface.

- change types, process tiers, routing definitions, approver roles, numbering schemes, validation rules, notification templates
- primary actions: configure routings and roles, define change types, set validation and effectivity rules

## Important Rules / Behaviors

### A record is in one active change at a time

Several products enforce that a given item or file can appear in only one open change order at a time, preventing conflicting edits from being approved out of sequence. This makes the change process an access-control surface as well as a governance one.

### Approval gates release, not editing

Working on a proposed change is generally unrestricted; what is restricted is advancing the released revision. In some products the restriction is strict — lifecycle state changes of released records are only permitted through a change order — making the change record the sole gate to production.

### Effectivity decides when a change takes effect

Approval alone does not complete the change. Release commonly requires setting effectivity — the date (or condition) from which the new revision is the released definition — and the implementation work being complete. Some products close the change automatically on approval; others keep it open until implementation is confirmed.

### Rejection is a revision, not a dead end

A rejected change record returns to its owner, is edited (affected records may be added or removed), and is resubmitted. The record and its history persist.

### Validation runs before review

Rule checks (required data, status requirements, parent/child consistency, missing documents) run during preparation; errors block submission, warnings do not. Strictness commonly increases with the release status of the affected records.

### The audit trail is the product

Every decision — who approved, when, what changed, why — is recorded against the change record and commonly against the affected data. This is what makes the process usable in quality audits and investigations, and it is why traceability belongs to the defining core rather than to a feature list.

## Variants

- **suite-embedded enterprise change management** — the change process as one governed capability of a full PLM estate, with boards, process tiers, and cross-discipline scope (the largest deployments)
- **cloud PLM with change at the center** — mid-market and startup products where the change order is the primary object and the record base is a lean item/document registry
- **ERP-module change management** — change orders as a module over ERP-owned product/BOM records, handing off to manufacturing through the same suite
- **PDM add-on change management** — change orders layered over a CAD file vault, operating on files and items either together or separately
- **regulated change control** — the same machinery carrying regulatory content: design-history linkage, compliance-driven review, audit-ready trails
- **manufacturing change management** — a sibling process over process/equipment records, often generated from an engineering change

A variant remains a variant unless it changes the core objects or rules; regulated change control, for example, keeps the same record world and only adds compliance content.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Product Lifecycle Management / PLM | broader sibling | PLM owns the product-record estate and the whole-life span (items, structure, documents, quality, requirements, portfolio); this Type owns the governed change progression over such records. Remove the estate → change machinery still functions; remove the change process → the estate is a static revision archive |
| Bill of Materials Management | adjacent sibling | BOM management centers the item/BOM/revision structure and its controlled release; a change workflow scoped to items/BOMs is a standard capability there, not the center. This Type's record base spans documents, files, and specifications as well |
| PDM / Engineering Document Management | adjacent | vaults and document registers manage versions, check-in/out, and release states; this Type adds the governed change process that supersedes versions. One product can carry both (vault as base, change orders as a governed layer) |
| IT Change Management | same grammar, different world | identical governance loop (request → assess → authorize → implement → review) over IT infrastructure and services with service-impact semantics; this Type operates over engineering product definition data with revision-advancement semantics |
| Change Order Management (construction) | same word, different world | construction change orders modify a commercial contract's scope/price/time among contracting parties with payment consequences and a counterparty approval gate; here there is no commercial counterparty and the changed object is design/product data |
| Product Configuration Management | adjacent | configuration management owns the variant space (rules and resolution sessions producing buildable variants); a change may alter the configuration model, but that is one affected object among many |
| Quality Management System / CAPA | feeder and regulator | quality events and corrective actions feed changes, and regulated change control is a compliance-carrying variant; the QMS's center is the quality system, not the change process |

The most important boundary is with PLM, because every sampled PLM embeds this machinery. The structural difference is the center of gravity: the product-record estate versus the change process that moves its records from one released revision to the next.

## Representative Products

- PTC Windchill (enterprise PLM suite; change process with request/order/notice tiers and change review boards)
- Arena, a PTC business (cloud PLM/QMS with automated change routings over a connected product record)
- Odoo PLM (open-source ERP module centered on engineering change orders)
- Duro (cloud PLM for hardware teams with the change order at the center of revision management)
- Autodesk Vault Professional (PDM file vault with change orders as a governed add-on layer)

The defining core was checked against the file-vault pole and the ERP-module pole to avoid over-fitting to the modern cloud-PLM implementation, and against paper-era practice (forms, boards, notices, redlines) for the historical check.

## Sources

Research date: **2026-09-10**

- PTC — Engineering Change Management: https://www.ptc.com/en/technologies/plm/engineering-change-management
- Arena — Engineering Change Management: https://www.arenasolutions.com/solutions/engineering-change-management/
- Arena — The Essential Guide to Engineering and Manufacturing Change Orders: https://www.arenasolutions.com/resources/articles/guide-manufacturing-engineering-change-orders/
- Arena — How Automated Engineering Change Management Helps Manufacturers Move Faster With Less Risk: https://www.arenasolutions.com/blog/how-automated-engineering-change-management-helps-manufacturers-move-faster-with-less-risk/
- Arena — No-code & Low-code Workflow Customization: https://www.arenasolutions.com/knowledge-hub/arena-plm-qms-questions/no-code-workflow/
- Odoo — PLM: https://www.odoo.com/app/plm
- Duro — Change Orders (help center): https://duro.zendesk.com/hc/en-us/articles/360029600032-Change-Orders
- Duro — FAQ: Change Orders: https://duro.zendesk.com/hc/en-us/articles/6893351333652-FAQ-Change-Orders
- Duro — Lifecycle Validations and Updates: https://duro.zendesk.com/hc/en-us/articles/360044348651-Lifecycle-Validations-and-Updates
- Duro — Revision History Table: https://duro.zendesk.com/hc/en-us/articles/360050079871-Revision-History-Table
- Duro — Change Orders (API documentation): https://docs.durohub.com/core-concepts/change-orders
- Autodesk — Vault help, Change Orders: https://help.autodesk.com/cloudhelp/2026/ENU/Vault-General/files/GUID-967A669D-028F-4E7B-AD66-86780FDAC4E9.htm
- Autodesk — Vault help, Change Order Routings and Routing Roles: https://help.autodesk.com/cloudhelp/Help/ENU/Vault/files/GUID-AC999E67-546E-4690-8A3D-95BA93519CCD.htm
- Autodesk — Vault help, Rules and Best Practices for Using Change Orders with Files: https://help.autodesk.com/cloudhelp/2026/ENU/Vault-General/files/GUID-2BEA1B49-D4EF-4C45-9AFE-26588BA998A7.htm
- Autodesk — Vault help, Change Order Administration: https://help.autodesk.com/cloudhelp/2025/ENU/Vault-Admin/files/GUID-1425F5FA-80E5-4D32-BAD5-01A44A6CD529.htm

> Sourcing limitation: Odoo's PLM application has no dedicated user-documentation page reachable from the research environment (two attempts returned not-found); Odoo evidence is limited to its official product page, and no Odoo-specific operational details are asserted. Exact state names, numeric limits, and default settings are stated only where directly observed in the sampled products' documentation; such details otherwise remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
