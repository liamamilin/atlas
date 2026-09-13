# Construction Document Management

## Overview

A **Construction Document Management** application is the project-scoped controlled-document system of record for a construction project. It holds a **register** of the project's documents — drawings, specifications, reports, contracts, and general files of record — attaches every new revision to the same document record while keeping the **current revision** as the version the whole team works from, and **issues** documents to the project's participating organizations and roles under permission-controlled access.

Three properties define the Type. Remove any one and it stops being recognizable:

- a project document **register** (identified records, not an undifferentiated pile of files)
- **revision management with a current-version discipline** (earlier revisions retained as history, never silently overwritten)
- **multi-party, permission-controlled distribution** across the independent organizations on the project

Everything else commonly associated with it — OCR ingestion, in-drawing markups, mobile offline viewing, review-and-approval workflows, ISO-style information governance, cloud-storage sync — is standard or optional capability layered on that core. Historically, a paper drawing register in a plan room, with revision-stamped sets issued to named parties via transmittals, satisfies the same three properties; the software Type digitalizes and automates that practice.

When the register dissolves into a generic file share (no revisions, no controlled issue), the product has drifted toward plain cloud storage. When the emphasis shifts to the workflow objects that *reference* documents — RFIs, submittals, schedule — it has drifted toward Construction Project Management and its sibling Types.

## Users & Context

Construction projects are executed by many independent organizations — owner, architects and engineers, general contractor, specialty contractors, suppliers — that must all work from the same current documents while their contractual relationships demand controlled, attributable exchange.

Primary users and their relationship to the system:

- **document controllers / information managers**: maintain the register — upload, identify, revise, publish, and issue documents; the role is named explicitly by the document-control products in this market
- **project managers / design managers**: consume and distribute the current sets, decide what gets issued to whom, track what has been seen
- **architects and engineers**: publish design documents and revisions; review and respond on shared documents
- **superintendents and field crews**: use the current drawings on site — view, mark up, take photos, link field issues — often offline on tablets or phones
- **subcontractors and suppliers**: access the documents issued to them for their scope; in some products they contribute their own markups and scope documentation from their side of the contract

Secondary concerns fall to administrators: folder/register structure, permission templates, project templates copied between projects.

## Core Model

### The Defining Core

```text
Construction Project (multi-party delivery engagement)
└── Document Register — the project's controlled-document record
    ├── Document record (number, title, type/discipline, metadata)
    │   └── Revisions — versioned under the same record;
    │        the current revision is the working set;
    │        earlier revisions retained as history (superseded / obsolete)
    └── Distribution & Access — participating organizations and roles,
         permission-controlled, with change notifications
```

- **Document record** — the stable identity of a document across its whole life: drawing number, title, discipline or type, and project-specific metadata. One record per document, no matter how many times it is revised.
- **Revision** — a new file under an existing record. Uploading a file with the same document number creates a revision of that record rather than a duplicate; the newest revision becomes current and the team is understood to work from it; the previous revisions remain visible and retrievable. This current-version discipline is what "controlled" means in this Type.
- **Register** — the queryable list of all document records (a "drawing log" or "document register"). It is the system of record: what exists, what revision is current, who may see it, what has been issued when.
- **Distribution & access** — documents are not public to the world; they are issued to defined organizations and roles. Permissions decide who can see, download, upload, or publish; notifications tell the right people that a revision they hold has been superseded.

### Standard Capabilities

Mature products carry most of the following. They make the core practical but do not define the Type.

- **Ingest with recognition** — bulk upload of multi-page PDFs; automatic extraction of drawing numbers, titles, and disciplines (OCR or filename parsing); a review-and-confirm step before documents enter the register; publication gating so drafts and superseded material do not reach the field.
- **Organization structures** — two coexisting philosophies: structured register attributes (drawing sets, disciplines, drawing areas/locations, metadata tags, metadata-driven search instead of folders) and folder trees with subfolders for general files. Most products offer some of each.
- **Viewing and markup** — in-product viewers for drawings, PDFs, and often 3D model files; annotation layers separated into personal and shared/published markups; markups carried forward onto new revisions; side-by-side revision comparison; text search inside drawings.
- **Linkage to project workflows** — RFIs, punch list items, tasks, observations, review comments, and work packages attach to or originate from specific spots on specific document revisions. Documents are the reference layer of the project's activity records.
- **Change awareness** — revision uploads trigger notifications; users can subscribe to a document log; cloud-connected products sync the current set to every device in real time.
- **Accountability machinery** — tracking of who downloaded or changed what and when; in the document-control-heavy products, a strong (sometimes contractual-grade) audit trail over the entire document history.
- **Mobile and offline field access** — the current drawing set on phones and tablets, usable without connectivity, with field markups and photos syncing back.
- **Record preservation** — log exports, one-click as-built drawing compilation, and project archives; the register is expected to survive as the project's evidence base long after completion.

### One Structure, Many Implementations

The core is written conceptually. Implementations differ on every layer:

```text
Concept:      Register organization
Realizations: metadata-driven register search (no folders) ·
              drawing sets + disciplines + areas · folder trees

Concept:      Custody and sharing model
Realizations: every organization owns a private workspace and controls
              its own sharing · project-level permission templates ·
              simple team-wide access

Concept:      Publication discipline
Realizations: review-and-confirm → publish steps · formal multi-party
              review matrices driven by document metadata · immediate sync
```

## How It Works

### Register the documents

```text
Collect drawings / files from the design team
→ upload (multi-page PDF or cloud-storage sync)
→ the system extracts number / title / discipline and detects
  existing document numbers
→ review and confirm the detected records
→ publish to the register
→ the relevant parties are notified
```

Ingest is deliberately mechanical: the register's usefulness depends on correct identification, so mature products invest in OCR, revision parsing out of drawing numbers, and conflict warnings when an upload does not cleanly match the existing records.

### Revise a document

```text
A new version of a drawing arrives
→ upload it against the same document number
→ the system attaches it as a new revision of the existing record
→ the new revision becomes current; the old one is retained as history
→ markups and links carry over per the product's rules
→ subscribers and affected parties are notified
```

No user ever "overwrites" a document. The revision chain is the product: it lets anyone answer, months later, which revision was current on a given date — a question that decides rework claims and disputes.

### Access and consume in the field

```text
Open the register (web, tablet, phone)
→ find the document by search, folders, set, or a hyperlink from another sheet
→ view the current revision (offline copies available on mobile)
→ mark up personally or publish a shared annotation
→ create a linked RFI / punch item / task at a location on the sheet
→ the field record stays attached to that document revision
```

### Distribute and control

```text
Define the project parties and roles
→ grant access per organization, role, folder, or document
→ publish revisions; notifications reach the right parties
→ downloads and views are tracked for accountability
→ optional: open read-only folders to invited bidders or external reviewers
```

### Close out the record

```text
Compile the as-built set (markups + final revisions)
→ export logs and record packages
→ archive the register as the project's permanent, retrievable evidence
```

## Interfaces

The surfaces below are described conceptually; exact names and layouts vary by product.

### Document register / drawing log

The system-of-record list. Typical information: document number, title, discipline/type, current revision, revision date, set or folder, status. Primary actions: search and filter, open, upload or upload revision, export the log, subscribe to changes.

### Document / drawing viewer

The consumption surface for one document. Typical information: the rendered sheet or file, revision selector, markup tools, linked items (RFIs, punch items, photos) pinned to locations. Primary actions: navigate and zoom, compare revisions, annotate personally or publish an annotation, measure, create a linked item, print or download.

### Revision history view

The control surface for one document record: every revision with date, source, and status; compare any two; mark obsolete; restore visibility of deleted revisions in some products.

### Folder / set management

The organization surface: folder trees with per-folder permissions (general-file pole), or drawing sets, disciplines, and areas (drawing pole). Primary actions: create and nest structures, move documents, set permissions, copy a structure into a new project.

### Permission / distribution settings

The party-facing control surface: organizations and roles, per-folder or per-document grants, private-vs-shared defaults, bid-phase external access. Primary actions: grant/revoke, publish or restrict, review the access and download trail.

### Mobile field viewer

The site surface: the current set cached for offline use, camera-to-sheet photo attachment, quick markup, and fast handoff into field workflows (punch lists, observations, daily work).

## Important Rules / Behaviors

- **The current-revision discipline governs work.** The register's promise is that "the latest published revision" is unambiguous. Products enforce it mechanically — automatic supersede, version conflict warnings, publish gating — because ambiguity here is exactly what the Type exists to eliminate.
- **Superseded is not deleted.** Earlier revisions remain in the register as history. Deletion is exceptional, heavily permissioned, and in the strongest products impossible; the document history is the project's evidence.
- **Obsolete is a status, not a removal.** A drawing that is no longer valid is marked obsolete and stays visible as such, so nobody mistakes it for current while the record of its existence is preserved.
- **Markup layers are separated.** Personal markups stay private; published markups become part of the shared record. Shared markups typically survive into new revisions; what happens to later edits of superseded revisions varies by product.
- **Access follows the organization chart of the project.** Visibility between owner, contractor, and subcontractors is deliberately controlled; in some products each organization owns its workspace and decides what to share. Downloads and changes are attributed — "who had which document when" is a designed capability, not an accident.
- **Draft and published states are distinct.** What reviewers process and what the field works from are separated by an explicit publication step in most products; only published revisions generate the "work from this" notifications.
- **Documents anchor the project's other records.** An RFI, a punch item, or a review comment points at a specific document and usually a specific revision; the register therefore doubles as the spine for the project's information trail.

## Variants

- **Document-control pole** (owner / EPC / large infrastructure): metadata-driven register instead of folders, per-organization data ownership, formal review matrices and approval workflows, contractual-grade audit trail, long-term archives. The register is framed as the project's contractual system of record.
- **Standards-governed CDE pole**: the register organized explicitly around information-management standards (such as ISO 19650), with information managers configuring delivery processes and schedules.
- **Field-first pole** (subcontractors, SMB general contractors): the drawing set and its revision discipline carried to the jobsite — offline mobile viewing, markups, as-built export — with lighter general-document storage and simpler access control; cloud-storage sync bridges (Box/Dropbox/OneDrive) feed the register.
- **Platform-module realization**: document management as one tool family inside a broader construction management platform, drawing revision mechanics tightly coupled to RFIs, submittals, and field tools.
- **Drawing-centric vs general-file emphasis**: some products grow from plan viewing (sheet register, hyperlinked sets), others from project file storage (folder trees, versioned files); mature products cover both but visibly lean one way.
- **Models as documents**: 3D model files stored, viewed, and versioned in the register; where clash detection and federated coordination begin, the product has entered a neighboring Type.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Engineering Document Management | same object family, different custody | design/EPC organization's authoring-side deliverable vault vs the construction project's cross-organization issue and field consumption |
| Enterprise Content Management | adjacent | organization-internal content and retention policy vs project-scoped, multi-organization revision discipline that ends in a project archive |
| Construction Project Management | host platform | owns workflow objects (RFIs, submittals, schedule, budget); document management is one module inside it and the reference layer for its workflows |
| RFI Management | linked workflow | owns the question/answer workflow; the documents it references live in the document register |
| Submittal Management | linked workflow | a submittal register is a specialized controlled register, but the approval workflow — not the general document record — is its defining core |
| BIM Coordination | downstream consumer | stores/views models as documents; clash detection and model issue management belong to coordination |
| Construction Closeout Management | downstream phase | owns the end-of-project handover compilation process; document management supplies and preserves the records it compiles |
| Construction Field Management | sibling consumer | field issues, daily logs, and quality/safety workflows attach to documents; the controlled record remains in the register |
| File Manager / Personal Cloud Drive | not the Type | no register, no revision discipline, no project-party distribution |
| PDF / Document Reader | capability surface | views one document; no register, revisions, or distribution |

The most important seam is with **Engineering Document Management**: the object model (register + revisions) is nearly identical, and products straddle it. The distinction lies in who holds the record and where it is consumed — the design organization's vault versus the multi-party construction project's issue-and-field surface. The second seam is with generic **cloud storage**: once revisions and controlled distribution disappear, the product has left this Type, whatever it calls itself.

## Representative Products

- **Procore** — Drawings tool (drawing register with revision history, compare, obsolete marking) and Documents tool (folder-based controlled file store) inside a construction management platform
- **Oracle Aconex** — single document register with automatic revision supersede, per-organization data ownership, and a contractual-grade audit trail; the document-control pole
- **Asite** — ISO 19650-framed Common Data Environment governed by information managers; the standards-led CDE pole
- **Fieldwire (by Hilti)** — field-first plan viewer with automatic sheet versioning, offline mobile access, and as-built export; the field-consumption pole

The defining core was checked against the pre-digital practice it replaced — paper drawing registers, plan rooms, and transmittal-controlled issue — which satisfies the same three defining properties without any modern machinery.

## Sources

Research date: **2026-09-07**

- Procore Support — Drawings tool landing page: https://support.procore.com/products/online/user-guide/project-level/drawings
- Procore Support — Project Documents tool landing page: https://support.procore.com/products/online/user-guide/project-level/documents
- Procore Support — Upload Drawing Revisions tutorial: https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/upload-drawing-revisions
- Oracle — Aconex product page and FAQ: https://www.oracle.com/construction-engineering/aconex/
- Asite — home page: https://www.asite.com/
- Asite — Common Data Environment page: https://www.asite.com/project-portfolio-management-ppm/common-data-environment-cde
- Fieldwire by Hilti — home page, Document Management page, Blueprint App page: https://www.fieldwire.com/ , https://www.fieldwire.com/document-management/ , https://www.fieldwire.com/blueprint-app/

> Sourcing note: Procore was documented from its Tier-1 support site (tool landing pages plus an operations tutorial). Aconex, Asite, and Fieldwire were documented from official product pages and FAQs; their deep help centers were not reached, so claims about those products' internal mechanics are kept at the strength of their published pages, and no numeric limits, default settings, or internal state names are asserted for them. Detailed evidence and product-by-product observations are recorded in the paired Research Notes.
