# Engineering Document Management

## Overview

An **Engineering Document Management** application is an engineering organization's system of record for its engineering documents and drawings. It holds each document as a **registered record** — a persistent, individually identified entry that exists independently of any file — tracks a **revision lineage** in which exactly one version is current and authoritative while earlier revisions remain as superseded history, and moves documents through **governed, permission-controlled states** from authoring to review to approval, with an attributable audit trail. Approved revisions are then published to the parties who consume them — as renditions, distribution packages, or handover sets — without granting them authoring rights.

The defining core is deliberately small:

```text
Engineering document of record (registered identity; files attach to it)
└── Revision lineage with one current authoritative version
    └── Governed progression through controlled states (review → approval)
        └── Publication of approved revisions to consumers
```

Everything else commonly associated with the category — CAD-tool integration, reference management, title-block exchange, PDF renditions, viewers and markup, transmittal portals, EAM/ERP integrations, compliance e-signatures — is standard capability that mature products add, not what makes the product an engineering document management system. A pre-software drawing register with revision letters, checker/approver signatures, and a distribution ledger satisfies the same core without any of them.

When the center of gravity shifts from the engineering organization's vault to a construction project's cross-organization issue and field consumption, the product is drifting toward a different Application Type (Construction Document Management). When the center shifts to part/item records, BOMs, and change orders, it is drifting toward Product Data Management / PLM.

## Users & Context

The primary user is the **engineering organization** — an owner-operator's engineering department, an EPC or engineering consultancy, or a manufacturer's design office — that authors and controls engineering deliverables: drawings, 3D models, specifications, datasheets, calculations, P&IDs, vendor documents, reports.

Typical roles and their relationship to the system:

- **Design engineers / CAD authors** — create and revise documents, check them out for editing, attach references, keep title-block data consistent with the record.
- **Checkers / reviewers** — examine submitted revisions, comment or mark up, and move documents through review states.
- **Approvers / document controllers** — release revisions, manage the register (numbering, attributes, status), and control who may see or act on documents in each state.
- **Downstream consumers** — construction teams, operations and maintenance staff, other disciplines and contractors — who retrieve the current approved revision, view or mark it up, and receive notifications when it changes; they do not author.

The work context is long-lived and high-stakes: a drawing's revision is contractually meaningful, multiple people may work concurrently on related documents, and the population must remain trustworthy for years — through project delivery and into operations, where the same documents answer maintenance and safety questions. This is why the record, its lineage, and its approval state — not the file — are what the system manages.

## Core Model

### The Defining Core

**The engineering document of record.** The central object is a registered record for one document — a drawing, model, specification, datasheet, calculation, or vendor document. The record carries its own identity (a document number/name distinct from any file name), controlled attributes (type, discipline, status, revision, ownership), and its own access permissions. Files attach to the record; the record can exist before any file does (a register entry awaiting content), and replacing the attached file does not create a new record. The register is the organization's authoritative list of what engineering documents exist.

**Revision lineage with one current authoritative version.** Changes to a document attach to the same record as new revisions. Earlier revisions are retained — visible, retrievable, and marked as superseded — never silently overwritten. Exactly one revision is the **current** one: the version downstream consumers work from and the one that may be edited next. When new material arrives that might match an existing record, the system adjudicates: it is either a new revision of that record or a new record — the register stays unambiguous. Dependency relationships between documents (a drawing referencing other documents) are part of the lineage too: a master document can be pinned to specific revisions of its references or follow their current ones.

**Governed progression through controlled states.** A document advances through named states — work in progress, review, approved/released; exact labels are configured per organization — and the system enforces who may move it and who may act on it in each state. State-based access control means a document under review is visible or editable only to the parties the state allows. Reaching an approved or final state typically renders the document read-only for everyone, regardless of permissions. Every transition is attributable: who changed what, when, and (where configured) with a required comment. In compliance-heavy deployments, formal approvals carry electronic signatures.

**Publication to consumers.** The approved current revision is what leaves the vault: rendered renditions (PDF-class outputs of authoring formats), distribution packages to other organizations, or handover sets to the owner at project completion. Publication is a controlled act — recorded, attributable, and tied to specific revisions — not a file copy.

### Standard Capabilities of Mature Products

These are widespread and expected, but a product remains in this Type without any given one:

- **CAD application integration** — check documents out and in from within the authoring tool; manage **references** (documents referenced by a master drawing/model, with revision pinning or follow-current behavior); exchange **title-block/attribute data** between drawing fields and record metadata; generate **renditions** for publication.
- **Viewing and markup** — preview and annotate documents (especially PDF renditions) without owning the authoring application.
- **Metadata search and register reporting** — search by document attributes, saved searches, exports of the register and its revision/status state.
- **Change serialization** — exclusive check-out with a lock (the CAD norm), with read-only copies available to everyone else; some products allow committing work while keeping the change open, and co-authoring for office-type documents.
- **Distribution packages** — formal transmittals/submittals to external parties: what is being sent, to whom, why, what response is expected; tracked to acknowledgement and response, with updated documents re-issued as new revisions of the original package.
- **Operations-system integration** — linking documents to asset and work-order contexts (EAM/ERP) so maintenance staff always see the current approved revision.
- **Model-content handling** — 3D models, point clouds, and geospatial placement of documents as first-class register content.

### One Structure, Many Implementations

The core is written conceptually; deployments realize it differently:

```text
Concept:   Document of record
Realized:  register entry with number + attributes; placeholder entries before content exists;
           creation-conflict resolution (new record vs new revision)

Concept:   Revision lineage
Realized:  version labels with one active version; superseded history retained;
           reference-revision pinning for dependent documents

Concept:   Governed states
Realized:  administrator-defined state sequences per document class; state-based access;
           terminal read-only status; audit comments; e-signatures where regulated

Concept:   Publication
Realized:  renditions; transmittal packages with issue permission and tracked responses;
           milestone handover sets to the owner
```

## How It Works

### Register and author

```text
Create register entry (number, type, discipline, attributes)
→ attach or author content (often from within the CAD tool)
→ check out (lock) → edit → check in (commit, with change comment)
→ revision recorded on the same record; prior revision superseded
```

Authoring happens under control: only one person holds the edit lock on the current revision at a time; everyone else works from read-only copies. References pulled from the vault stay linked — when a referenced document changes, dependent authors are prompted to refresh.

### Review and approve

```text
Submit revision for review
→ reviewers comment / mark up
→ state advances (permission-gated, audited)
→ approved / released: revision becomes the current authoritative version
→ document locked read-only (until a new revision cycle opens)
```

The state sequence is organization-defined. Access follows the state: a document in review is visible to its reviewers; a released document is visible to its consumers. The audit trail records every transition.

### Publish and distribute

```text
Generate rendition of the approved revision
→ assemble distribution package (documents, recipients, purpose, expected response)
→ issue (permission-gated) → recipients acknowledge / respond
→ responses and their attachments tracked against the package
→ updated documents re-issued as a new revision of the package
```

In project delivery, this loop carries documents between owner, engineer, and contractors. At completion, the register's approved revisions assemble into the handover record the owner will operate from.

### Maintain in operations

For owner-operators, the register continues after construction: maintenance and modification work pulls the current approved revision (often through EAM/work-order integration), field changes drive new revision cycles, and the lineage preserves what was true at every point in the asset's life.

### Capability tiers

**Defining core** — document of record; revision lineage with one current version; governed states with audit; publication of approved revisions.

**Standard capabilities** — CAD integration, references, title-block exchange, renditions, viewers/markup, metadata search, check-out locking, transmittal packages, EAM/ERP integration, model handling.

**Optional / variant** — e-signature and validated compliance packaging; standards-driven handover data; geospatial placement; component-level search inside files; AI-assisted search and classification.

## Interfaces

Exact layouts vary by product; the surfaces below are described conceptually.

### Document register / explorer

The primary working surface: a navigable tree of containers (projects, work areas, folders, or asset/discipline structures) over a list of document records.

- Typical information: document number/name, type, discipline, revision, state, owner, last activity.
- Primary actions: create record, check out/in, open, view properties, change state, search.

### Document detail / properties

The record surface: identity, attributes, revision list with the current one flagged, references in and out, permissions, audit trail.

- Primary actions: edit attributes, manage revisions, manage references, set permissions, view history.

### Authoring-tool integration

The vault experienced from inside the CAD or office application: open/save against the register, check in/out, attach references from the vault, title-block data exchange.

### Viewer / markup

Read-and-annotate surface for renditions — for reviewers and downstream consumers who do not author.

### Distribution / transmittal surface

Package composition (documents, recipients, purpose, response expectations), issue with permission, and tracking of acknowledgements and responses. Often a web portal for external parties.

### Administration

Configuration of the register: document classes and their attribute sets, state sequences and their permissions, numbering conventions, container structures, integrations.

## Important Rules / Behaviors

- **The current revision is authoritative.** Consumers work from the current approved revision; superseded revisions remain readable but are never the working version. Only the current revision can be checked out for editing.
- **Changes are serialized.** The edit lock prevents concurrent modification of the current revision; read-only copies keep everyone else productive. Committing work and releasing the lock are separable acts in some products.
- **Approval is a gate, not a label.** Released/final states render the document read-only regardless of permissions; reopening requires a new revision cycle under the same governed rules.
- **State controls access.** Who can see and act on a document depends on its state; moving state requires specific permissions and leaves an attributable, often commented, audit entry.
- **Register integrity is adjudicated.** Incoming material that matches an existing record becomes either a new revision or a new record — the system forces the choice so the register never silently forks.
- **Publication is attributable.** What was sent, to whom, in which revision, and what came back is part of the record — distribution is a controlled transaction, not a file copy.
- **Lineage extends to references.** A master document's references are managed at the revision level (pinned or follow-current), so a published set is internally consistent.

## Variants

- **EPC / project-anchored** — the register is organized by project, work area, and discipline; distribution packages and milestone handovers to the owner are central; heavy CAD/BIM content.
- **Owner-operator / asset-anchored** — the register is organized by facility and asset; the emphasis is on keeping the as-operated document population current and linked to maintenance work; strong EAM integration; often PDF/drawing-centric ("non-intelligent data") document control.
- **CAD-vault pole** — design teams vaulting CAD files with revision and approval control, without formal external distribution; the thin edge toward Product Data Management.
- **Compliance-heavy** — validated environments with electronic signatures and audit formalism for regulated industries (pharma, energy, nuclear).
- **Deployment shapes** — on-premises enterprise vaults; SaaS platforms with web portals for external collaboration; companion portals layered on an existing vault for distribution.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Construction Document Management | closest sibling | the project's cross-organization issue and field-consumption register; here the engineering organization's vault of record is primary. Remove design-org custody and revision control → Construction DM; remove multi-party issue/field consumption → this Type. Products straddle the seam. |
| Product Data Management (PDM) | adjacent | centers on CAD part/item records and the CAD-file vault bound to BOMs; here document records (drawings, specs, reports) are the center, without item/BOM semantics |
| Product Lifecycle Management (PLM) | broader | centers on the product record (items, BOMs, change objects); document management appears as a module; this Type stands alone where no BOM exists (AEC, owner-operators) |
| Engineering Change Management | complementary | manages the change-process objects (requests/orders) that drive changes across items and documents; the documents' register, revisions, and states live here |
| Enterprise Content Management | adjacent | manages general enterprise content (email, records, policies) without engineering-document semantics; remove engineering-document custody and revision-of-record → ECM |
| Enterprise Records Management | adjacent | retention/disposition-centric and content-agnostic; here revision/approval-centric and content-specific |
| BIM Coordination | downstream consumer | consumes issued models/documents in a federation and coordination process; does not hold the register |
| File storage / cloud drives | not this Type | no register identity, no revision-of-record authority, no governed approval states |

## Representative Products

- Bentley ProjectWise
- Accruent Meridian
- AVEVA Asset Information Management (with integrated document control)

The core model was checked against the pre-software drawing-register practice (numbered records, revision letters, checker/approver signatures, distribution ledger) to avoid over-fitting to any current product shape.

## Sources

Research date: **2026-09-08**

- Bentley — ProjectWise Explorer Help (2024) and ProjectWise Deliverables Management Portal Help (2024), docs.bentley.com (operational documentation: document creation and conflicts, check-out/check-in, versions, workflows and states, references and sets, integrated applications, renditions, transmittals)
- Accruent — Meridian product page and FAQ, accruent.com/products/meridian
- AVEVA — Asset Information Management product page and FAQ, aveva.com/en/products/asset-information-management/
- Sibling research: research/construction-document-management.md (boundary seam)

> Sourcing limitation: operational help centers for several adjacent products (Autodesk Vault, SOLIDWORKS PDM, OpenText Engineering Document Management, Siemens Teamcenter, Accruent Meridian's help center) were not reachable from the research environment on 2026-09-08. Claims about the CAD-vault/PDM pole are held at reasoning strength rather than direct observation, and no numeric limits, default settings, or exact state-name catalogs are asserted anywhere in this document.
