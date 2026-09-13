# Research Notes — Construction Document Management

## Research Goal

Understand how real software manages **controlled documents on construction projects**: how drawings, specifications, reports, and files of record are registered, revised, distributed to the project's participating organizations, accessed in the office and the field, and preserved as the project's record — and how this Type differs from Engineering Document Management, Enterprise Content Management, Construction Project Management modules, RFI/Submittal Management, BIM Coordination, Construction Closeout Management, and generic file storage.

## Initial Boundary

Initial hypothesis: a Construction Document Management application is the **project-scoped controlled-document system of record** for construction delivery:

1. A **register** of the project's documents (drawings and general files), each identified by number/title/type/metadata.
2. **Revision management**: new revisions tracked against the same document record, with a current-version discipline (earlier revisions retained as history/superseded, not silently overwritten).
3. **Multi-party controlled distribution and access**: documents are issued to and consumed by the project's participating organizations and roles under permissions.

Nearest confusions:
- **Engineering Document Management** — same object family (controlled documents with revisions) but design-office/EPC custody and authoring-side consumption.
- **Enterprise Content Management** — organization-internal, retention-centric; not project-cross-organization.
- **Construction Project Management** — owns workflow objects (RFIs, submittals, tasks); document management is one tool family inside such platforms and the reference layer for those workflows.
- **RFI Management / Submittal Management** — workflow registers that reference documents; the submittal register is a specialized controlled register but the approval workflow belongs to its own leaf.
- **BIM Coordination** — model-centric clash/issue process; models may be stored as documents but coordination is a different Type.
- **Construction Closeout Management** — owns the end-of-project handover compilation; document management feeds it.
- **File Manager / Personal Cloud Drive** — personal or org-internal storage without register/revision/distribution semantics.

## Research Questions

1. What is the document object model? (register, document record, revision, status, folder/set organization)
2. How does revision control work — how does a new revision relate to the old, what does "current" mean, are superseded revisions retained?
3. How is distribution performed and controlled (permissions, invited parties, notifications, download tracking)?
4. How are documents consumed (viewing, markup, linking to project objects, mobile/offline)?
5. What status/lifecycle mechanics exist (draft/publish, review/confirm, obsolete)?
6. What accountability machinery exists (audit trail, download tracking, immutability claims)?
7. What organization philosophies exist (register/metadata-driven vs folder-driven; document-control-heavy vs field-light)?
8. Which capabilities are defining vs common vs optional vs vendor-specific?
9. Where are the boundaries vs the neighboring Types listed above?

## Representative Products

| Product | Pole | Segment | Docs fetched |
|---|---|---|---|
| Procore | GC-centric construction platform; Drawings tool (drawing register) + Documents tool (general file repository) as separate tools | mid-market to enterprise GCs, multi-party projects | Tier-1: Drawings tool landing page, Documents tool landing page, Upload Drawing Revisions tutorial (fetched 2026-09-07) |
| Oracle Aconex | Owner/EPC document-control heritage; "single document register" + data-ownership model + unalterable audit trail; contractual system of record | owners, EPC/contractors on large multi-organization projects | Tier-2: product page with extensive FAQ (fetched 2026-09-07) |
| Asite | UK-heritage CDE / information-manager pole; ISO 19650-framed common data environment | enterprise owners, contractors, supply chain (UK/global infrastructure) | Tier-2: home page + Common Data Environment product page (fetched 2026-09-07) |
| Fieldwire (by Hilti) | Field-first plan-viewer + lightweight document storage; SMB/subcontractor pole | specialty contractors, small-to-mid GCs, field crews | Tier-2: home page + Document Management product page + Blueprint App product page (fetched 2026-09-07) |

Attempted / not needed: Autodesk Construction Cloud was unreachable (403/404) in the sibling construction-cost-management run the same day; per the network rule it was not retried, and no Autodesk-specific claims are made. Bentley ProjectWise and Trimble 4Projects were not sampled (ProjectWise sits on the engineering-document-management seam; noted in Boundary Findings).

## Sources

- Procore Support — Drawings tool landing page: https://support.procore.com/products/online/user-guide/project-level/drawings (fetched 2026-09-07)
- Procore Support — Project Documents tool landing page: https://support.procore.com/products/online/user-guide/project-level/documents (fetched 2026-09-07)
- Procore Support — Upload Drawing Revisions tutorial: https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/upload-drawing-revisions (fetched 2026-09-07)
- Oracle — Aconex product page + FAQ: https://www.oracle.com/construction-engineering/aconex/ (fetched 2026-09-07)
- Asite — home page: https://www.asite.com/ (fetched 2026-09-07)
- Asite — Common Data Environment page: https://www.asite.com/project-portfolio-management-ppm/common-data-environment-cde (fetched 2026-09-07)
- Fieldwire — home page: https://www.fieldwire.com/ (fetched 2026-09-07)
- Fieldwire — Document Management page: https://www.fieldwire.com/document-management/ (fetched 2026-09-07)
- Fieldwire — Blueprint App page: https://www.fieldwire.com/blueprint-app/ (fetched 2026-09-07)
- Historical context (no fetch): paper plan rooms, drawing registers, and transmittal practice — used only for the historical-sample check.

## Product A — Procore

### Key observations (Layer A unless noted)

**Two complementary tools** (Tier-1): a **Drawings** tool ("manage and archive project drawings and revisions to ensure that team members always have access to the most current drawing set") and a **Documents** tool ("important files of any type can be stored and accessed by specified users"). The drawing register and the general file repository are distinct surfaces with distinct mechanics.

**Drawings tool** (Tier-1):
- **Drawing register/log**: Manage Drawing Log, export log to PDF/CSV, search/filter drawings, drawing sets (named sets with set date), disciplines (configurable defaults), drawing areas (location overlay), reorder within discipline.
- **Ingest**: upload with **OCR** filling Drawing Number/Title/Discipline; revision parsing from drawing numbers/filenames ("A203.01" → number A203, revision 01; decimal/underscore variants); multi-page PDFs; **Review and Confirm Drawings** step ("Items to Review" with progress indicator); **Publish Drawings** (draft/pending vs published); upload a Drawing Sketch.
- **Revisions**: upload drawing revisions — "Procore will recognize the drawing number as a duplicate … and mark it as a revision of the existing drawing. The drawing revision will automatically appear under the Revision History of the existing drawing"; same revision number allowed if Set Name/Drawing Date/Received Date unique; change a revision's number; reorder revisions; view deleted revisions; **Compare Drawing Revisions**; **Mark Drawings as Obsolete** / unmark.
- **Markup layers**: **personal vs published** markups ("personal and published drawing markups" distinction); private/published markup layers; markup activity feed; filter markups; markups on a previous revision "preserved and inherited by the new drawing revisions" (layer-specific; later edits to old revisions do not propagate).
- **Linkage**: create or link **RFIs** on a drawing, punch list items, observations, coordination issues, photos, 360 photos; link items on a drawing; measurements; generate locations hierarchy from drawings.
- **Distribution/awareness**: notification emails after revision upload processing; **subscribe to the Drawings Log**; email drawings; download/print; QR codes for drawings.
- **Consumption**: view drawings, view all revisions on mobile, **view drawings offline**, search **text within drawings**, rotate; web/iOS/Android.
- **Permissions**: granular permissions ('Upload Drawings', 'Upload and Review Drawings'); Read Only/Standard/Admin; role-based tutorials for Owner, Specialty Contractor (as collaborator), Field Worker.

**Documents tool** (Tier-1):
- Folder/subfolder tree; standard project folder structure templates; copy folder structure to a new project.
- "Set and manage permissions on folders and documents"; private-by-default files/folders; **publicly-viewable folders for invited bidders** (with Bidding tool).
- "Check out and lock a document"; **"Manage revisions and distribute updates to specified users"**; upload a new version, download a previous version, compare documents.
- **"Build accountability by tracking when and who downloaded each file"**; track file and folder changes; file/folder tracking management.
- Email files into the project; Office 365 view/edit; DocuSign signing; tags; related items; recycle bin; 3D models stored/published from the tool (IFC/DWG/NWD; BIM customers).

**Interpretation (Layer C)**: Procore realizes the Type as two registers — a structured drawing register with revision-discipline mechanics and a folder-based controlled file store — both sharing the same distribution/permission/audit posture and both feeding the platform's workflow tools (RFIs, punch, etc.) via linked items.

## Product B — Oracle Aconex

### Key observations (Layer A for page/FAQ content; positioning Tier-2)

- **"A single document register"**: "Create a single source of truth for the entire project team. A single document register with strict version control protocols eliminates the risk of multiple datastores and helps ensure that everyone uses the correct information."
- **Revision discipline**: "Documents, drawings, and models are managed within a single document register where **revisions automatically supersede earlier versions**. Teams always have access to the current version while maintaining full visibility into historical revisions and their associated activities."
- **Metadata-driven organization**: "metadata-driven search instead of traditional folder-based approaches. Documents, drawings, models … organized using configurable metadata"; "version control helps users confirm they are accessing the correct documents"; no limits on document volume or size (vendor claim).
- **Data ownership model**: "Every organization on the project has their own private workspace … and controls the data in their workspace, including who they share that data with and when"; "one organization cannot alter another organization's data"; designed for "contractual collaboration across multiple independent organizations."
- **Distribution**: "securely distribute information only with the organizations that need it"; automated notifications (tender context).
- **Review machinery**: "Document Processes provides a structured framework … automated Review Matrix" initiating "the correct approval flow … based on the metadata of the review document"; integrated Comment Management consolidating review comments "for 2D and 3D."
- **Accountability**: "unalterable audit trail"; "Nothing can be deleted or edited"; audit trail records "who performed each action, when, and how it relates to associated documents."
- **Work packaging**: group documents/drawings/correspondence into packages "for completion and sign-off"; documents can belong to multiple packages while maintaining version control; packages linked to schedule dates.
- **Mobile/field**: "View the latest set of drawings"; one app for documents, mail, models, inspections.
- **Archive/handover**: complete project record; three archive options (Online Archive / Project Archive on-prem / Scheduled Archive); record preserved "for knowledgebase and to meet regulatory and legal requirements during and after project completion."
- **Named user role**: "document controllers" listed among primary users; also project directors, PMs, design managers, project controls.
- **Adjacent modules**: Mail (contractual correspondence), Model Coordination, Bid/Tender, Supplier Documents, Cost/Contract, Field (quality/safety) — the document register is the platform's information spine, not the whole product.

**Interpretation (Layer C)**: Aconex is the document-control pole: the register is the system of record, cross-organization neutrality and immutability are first-class product principles, and review/approval workflows are built directly on document metadata.

## Product C — Asite

### Key observations (Layer A for page content)

- **CDE framing**: "Asite Common Data Environment (CDE) empowers Information Managers to control project information in a standards-based collaborative platform with powerful workflows"; "manage data according to **ISO 19650**-specified standard procedures and governance."
- **Single repository**: "Improve transparency by storing project documents in a single centralized repository."
- **Automatic version control**: "CDE uses **automatic version control to remove the confusion of different versions**. Teams can manage documents with accuracy — from drawings and specs, to submissions and meeting minutes."
- **Supply-chain collaboration**: "View and collaborate on 2D drawings, 3D models and hundreds of other file types"; "from the smallest teams to the world's largest" supply chain.
- **Publish/share**: "Drawings, photos, and files can be published and shared at any time and from any location … security controls to manage access appropriately."
- **Integration/field**: aMail (email connected to the CDE), Asite Field mobile app ("mobilize your 2D/3D models"), 3D Repo (model coordination add-on), dashboards/reports, schedule/cost/risk integration.
- **Named user role**: "Information Managers" / "Project Information Managers" (Playbook configures "information delivery processes and schedules").

**Interpretation (Layer C)**: Asite realizes the Type as a standards-framed common data environment governed by information managers: repository + automatic versioning + access control + supply-chain-wide publishing, with workflow and field surfaces attached.

## Product D — Fieldwire (by Hilti)

### Key observations (Layer A for page content; Tier-2 positioning)

- **Plan viewing core**: "Access, edit, and view as-built drawings from any device"; "work from the latest plans with **versions**, auto-hyperlinking, and real-time sync"; mobile-first (iPhone/iPad/Android), **works offline**, optimized high-resolution rendering on servers.
- **Sheet register**: "Robust sheet version control … import and manage large quantities of construction drawings"; "upload your blueprints as a multi-page PDF or sync your project directly with a posted set on Box, Dropbox, or OneDrive"; "Fieldwire **extracts the drawing numbers, version sheets automatically, and warns you of any conflicts**"; "version conflict" FAQ; unlimited sheets on paid plans (vendor pricing claim).
- **Auto-hyperlinking**: extracts sheet names, links navigation callouts to related drawings/elevations.
- **Markups & as-builts**: "add markups, annotations, and progress photos directly on your drawings while you're in the field"; "everyone from the foreman to the architect has access to the latest information"; "export your as-built drawings in one click"; "a historical record of all annotations, progress photos, and file links … at the end of each project"; "maintain a conformed set of drawings" (customer quote).
- **General documents**: Document Management page — "Store and access construction documents"; 2-way sync with cloud storage ("making version control effortless"); subfolders mirroring existing file systems; access from office or field; reports/RFIs/submittals/forms stored in one place.
- **Task linkage**: tasks/punch items attached on plans; messaging connected to tasks.

**Interpretation (Layer C)**: Fieldwire is the field-consumption pole: the drawing set and its revision discipline carried to the jobsite (offline, mobile, markups), with lightweight general document storage beside it and weaker (undocumented on fetched pages) permission machinery. Distribution is team-wide sync rather than formal per-organization issue.

## Cross-product Comparison

| Dimension | Procore | Oracle Aconex | Asite | Fieldwire |
|---|---|---|---|---|
| Register | Drawings log + sets/disciplines/areas; Documents folder tree | "single document register", metadata-driven (explicitly vs folders) | centralized repository, organized information | sheet list w/ extracted numbers; subfolders for files |
| Revision discipline | auto-recognized revisions → Revision History; compare; obsolete marking | revisions "automatically supersede earlier versions"; current + full history | "automatic version control" removes version confusion | auto-versioning of sheets; conflict warnings |
| Multi-party distribution | specified users; per-folder/file permissions; public bid folders; notifications; subscribe to log | per-organization private workspaces; "distribute information only with the organizations that need it" | publish/share to supply chain w/ security controls | team access/real-time sync (mechanics not detailed on fetched pages) |
| Status lifecycle | Review & Confirm → Publish; draft/pending vs published; Obsolete | review matrix/document processes; approval flows from metadata | powerful workflows over information management | version-conflict warnings (no formal review flow documented) |
| Viewing & markup | viewer; personal vs published markup layers carried across revisions; compare revisions; text search in drawings | comment management for 2D/3D reviews | view/collaborate 2D + 3D | offline viewer; markups/photos; auto-hyperlinks; as-built export |
| Accountability | download tracking ("who and when"); track file/folder changes | "unalterable audit trail; nothing can be deleted or edited" | digital tracking; security by design | historical record of annotations/photos |
| Linkage to workflows | RFIs/punch/observations/coordination issues/photos on drawings | documents linked to reviews/RFIs/packages/ITPs/contracts | field app, aMail, financials attached to CDE | tasks/punch/messaging on plans |
| Archive/handover | log exports; project folder copy | three archive products; preserved project record | handover phase in CDE framing | one-click as-built export |
| Organization philosophy | hybrid: structured drawing register + folders | register/metadata-first | standards/CDE-first (ISO 19650 framing) | drawing-set-first, field-first |
| Evidence strength | Tier-1 (support site ×3) | Tier-2 (product page + rich FAQ) | Tier-2 (×2 pages) | Tier-2 (×3 pages) |

**Cross-product commonality (Layer B):**

1. **A project-scoped register of controlled documents** — every product maintains an identified list of the project's documents/drawings (log, register, sheet list, repository), not an undifferentiated pile of files.
2. **Revision management with a current-version discipline** — new revisions attach to the same document record; the current revision is what the team works from; superseded/earlier revisions remain visible as history (Procore Revision History; Aconex automatic supersede; Asite automatic version control; Fieldwire auto-versioning). No product overwrites in place.
3. **Multi-party, permission-controlled access and distribution** — documents are issued/shared to the project's participating organizations and roles under access controls (Procore specified users + permissions; Aconex per-organization sharing; Asite security-controlled publishing; Fieldwire qualified — team access documented, granularity not).
4. **Awareness of change** — revision uploads generate notifications/subscriptions (Procore notifications + log subscription; Aconex automated notifications; Fieldwire real-time sync; Asite real-time visibility).
5. **Consumption where the work happens** — viewing and markup on drawings, on mobile, offline (Procore, Fieldwire directly; Asite field app; Aconex mobile app).
6. **Documents as the reference layer of project workflows** — RFIs, punch items, tasks, reviews, packages link back to document records (all four, different realizations).
7. **Accountability trail** — who accessed/downloaded/changed what (Procore download tracking; Aconex audit trail; Asite tracking; Fieldwire historical record — strength varies).
8. **Project record preservation** — export/archive/as-built outputs at completion (Procore log exports; Aconex archives; Asite handover framing; Fieldwire as-built export).

## Canonical Model (Layer C synthesis)

```text
Construction Project (multi-party delivery engagement)
└── Document Register (the project's controlled-document system of record)
    ├── Document record (number/title/type-discipline/metadata; drawing or general file)
    │   └── Revisions (versioned; current revision is the working set;
    │        earlier revisions retained as history / superseded / obsolete)
    ├── Organization structures: sets/disciplines/areas (drawing pole)
    │        or folders (file pole) — or metadata search instead of folders
    └── Distribution & access (participating organizations + roles,
         permission-controlled; notifications on change)
Consumption: view → mark up (personal vs shared layers) → link to workflow objects
             (RFIs, punch, tasks, reviews) → download/print (offline in the field)
Closing: as-built export / archive / handover record
```

## L0 — Defining Invariant (minimal)

1. **A project-scoped register of controlled documents** — identified records (number/title/type/metadata) for the project's documents. Without the register there is no management, only storage.
2. **Revision management with a current-version discipline** — new revisions tracked against the same document record; the current revision is what the team works from; earlier revisions retained as history. Without it, the product is a file share.
3. **Multi-party, permission-controlled distribution and access across the project's organizations** — documents are issued to and consumed by parties beyond the uploading organization, under access control. Without it, it is a personal or single-org archive.

Historical check: the paper drawing register + plan room + transmittal practice satisfies all three (a register of drawing numbers/rev letters; superseded sets stamped and retained; issued to named parties with receipts). Pre-digital document control passes; cloud collaboration, OCR, markups, mobile, ISO 19650 are deliberately excluded from the definition.

## L1 — Common Mature Structure

- **Document ingest with recognition** — OCR/metadata extraction of number/title/discipline from files; multi-page PDF import; review-and-confirm before publication.
- **Status lifecycle** — draft/pending → reviewed/published (some products: formal multi-party review/approval workflows driven by document metadata; document-control pole).
- **Viewing and markup** — in-product viewers (drawings, PDFs, 3D files); personal vs shared/published markup layers; markups persisting across revisions; revision comparison; text search within drawings.
- **Linkage to project workflow objects** — RFIs, punch items, tasks, observations, reviews, packages referencing document records.
- **Change awareness** — notifications/subscription on revision publication; real-time sync to all parties.
- **Search and retrieval** — metadata-driven search and/or folder navigation; content search within drawings.
- **Accountability machinery** — download/access tracking, change tracking, audit trails (strength varies; strongest in document-control pole).
- **Mobile/offline field access** — current document set on phones/tablets, offline-capable.
- **Organization structures** — drawing sets/disciplines/areas on the drawing pole; folder trees on the file pole.
- **Record preservation** — exports, as-built drawing compilation, project archives for handover.

## L2 — Variant / Optional Structure

- **Register/metadata-first vs folder-first organization** (Aconex explicitly contrasts metadata search with folder approaches; Procore/Fieldwire offer folders; hybrid common).
- **Drawing-centric vs general-file emphasis** (Fieldwire/blueprint pole vs general document repository; most mature products carry both).
- **Per-organization data ownership** (each party owns its workspace — Aconex pole; other products use project-level permissions instead).
- **Formal review/approval matrices** (document-control pole; lighter products ship without).
- **Work packages / transmittal bundles** (grouping documents for issue/sign-off).
- **Models as documents** (3D files stored/viewed/published in the register; full coordination belongs to BIM Coordination).
- **Bid/tender document distribution** (publicly-viewable folders for invited bidders — Procore; tender distribution — Aconex).
- **Standards framing** (ISO 19650 CDE governance — Asite; region/regime dependent).
- **Cloud-storage sync bridges** (Box/Dropbox/OneDrive two-way sync — Fieldwire; Office 365 editing — Procore).
- **Email integration** (email files into the register; correspondence tools beside it).
- **E-signature inside the document store** (DocuSign — Procore).
- **Archive depth** (read-only online/on-prem/scheduled archives — Aconex pole).

## L3 — Vendor-specific Structure (research notes only)

- Procore: OCR language selection; drawing-number revision parsing rules (decimal/underscore variants); 'Get From Filename'; private/personal/published markup layer names; markups-not-propagating rule for post-hoc edits to old revisions; Procore Drive desktop sync; recycle bin; publicly-viewable bid folders tied to the Bidding tool; QR codes for drawings; location heat maps generated from drawings; DocuSign banners; 3D model publishing (IFC/DWG/NWD viewpoints); Procore Connect for Drawings; granular permission names ('Upload and Review Drawings').
- Oracle Aconex: data-ownership/private-workspace model; "unalterable … nothing can be deleted or edited" immutability claim; Review Matrix; Comment Management; work packaging with schedule linkage; three named archive products; aMail/Mail module; Model Coordination Cloud Service; "no limits on document volume or size" claim.
- Asite: Playbook (information-delivery configuration), aMail, aDrive, 3D Repo/SafetiBase, Cognitive CDE, Virtual Coworkers; ISO 19650 self-framing; "84,000+ companies" claim.
- Fieldwire: two-way Box/Dropbox/OneDrive sync; auto-hyperlinking of navigation callouts; version-conflict warnings; unlimited sheets on paid plans; 4,000,000+ projectsites claim; "conformed set" customer framing.

## Boundary Findings

- **vs Engineering Document Management**: same object family (controlled documents + revisions), different custody and consumption. Engineering document management centers on the design/EPC organization's deliverable vault (authoring-side, CAD-adjacent, single-org custody); construction document management centers on the construction project's cross-organization issue and field consumption (owner/contractor/subcontractor parties, site access, markups). **Remove the multi-party project issue/field consumption and keep the design-org vault → Engineering Document Management.** Products straddle the seam (a construction platform's document tool can serve the engineering org), so the boundary is drawn on primary custody/consumption, not file type.
- **vs Enterprise Content Management**: ECM manages an organization's internal content/records over retention policy; construction document management manages a project's documents across independent organizations over revision/supersede discipline, dissolving at project completion into archive. **Remove the project scope and multi-organization issue → ECM.**
- **vs Construction Project Management**: document management is one tool family inside construction PM platforms (Procore's own structure shows Drawings/Documents as tools beside RFIs, submittals, budget, scheduling). PM owns the workflow objects and the schedule; document management owns the controlled documents those workflows reference. **Keep the workflow objects and drop the document register/revisions → Construction Project Management.**
- **vs RFI Management / Submittal Management**: those leaves own question/approval workflow registers. Documents are the referenced artifacts; an RFI links to a drawing; a submittal register is a specialized controlled register whose approval workflow belongs to Submittal Management. **Keep only the workflow and drop the general document register → RFI/Submittal Management.**
- **vs BIM Coordination**: storing and viewing model files in the register is document management; clash detection, model issue management, and federated coordination are BIM Coordination. **Keep only model viewing in the register → this Type; add the coordination process → BIM Coordination.**
- **vs Construction Closeout Management**: closeout owns the end-of-project handover process (deliverable completion, O&M/warranty compilation); document management supplies the records and the as-built export all along. **Keep only the handover compilation process → Closeout Management.**
- **vs File Manager / Personal Cloud Drive / File Sync**: personal or organization-internal storage without register, revision discipline, or project-party distribution. **Remove register + revisions + multi-party issue → file storage.**
- **vs PDF / Document Reader**: a reader opens one document; no register, no revisions, no distribution.
- **"去掉什么就变成另一个 Type" 判据**: remove revision/current-version discipline → project file share (cloud drive); remove the document register → file storage; remove multi-party distribution/access → personal archive; remove drawings-and-files breadth and keep only workflow registers → RFI/Submittal Management; keep only viewing/markup → plan viewer surface (a capability, not the Type).

## Uncertainties

- **Fieldwire's access-control granularity** is not documented on the fetched pages; its distribution mechanics are treated as "team access" with qualified strength. No permission-machinery claims are made for it.
- **Autodesk Construction Cloud / PlanGrid-class products** were not directly documented (unreachable in the sibling same-day run; not retried). Their structural role in this market is acknowledged but no product-specific claims are made.
- **Supersede semantics differ** in detail across products (automatic vs confirmed vs published); the canonical claim is the discipline (current + retained history), not any specific mechanism.
- **Engineering-document-management seam products** (ProjectWise, Bentley) were not sampled; the boundary judgment there rests on market structure reasoning, not direct evidence.
- Whether formal **review/approval workflow machinery** should be Core or Common: it is absent in the field-light pole (Fieldwire) and present in the document-control pole (Aconex, Asite, Procore's lighter Review/Confirm) — written as standard capability with variant depth, not as defining.

## Final Synthesis

Construction Document Management is the **project-scoped controlled-document system of record for construction delivery**: it holds a register of the project's documents (drawing register and general document store), attaches every new revision to the same document record while keeping the current revision as the working set and earlier revisions as retained history, and issues documents to the project's participating organizations and roles under permission-controlled access with change notifications. Around that core, mature products add ingest recognition (OCR), status/publish lifecycles and (at the document-control pole) formal review matrices, in-product viewing with layered markups that survive revisions, linkage from RFIs/punch/tasks/reviews to document records, accountability trails (download/access/audit), mobile offline field access, and end-of-project as-built export/archive. Two organization philosophies coexist — metadata-driven register versus folder tree — and two custodial philosophies — per-organization data ownership versus project-level permissions — without changing the defining structure.
