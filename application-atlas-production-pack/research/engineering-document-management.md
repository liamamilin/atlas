# Research Notes — Engineering Document Management

Research date: 2026-09-08
Leaf: Engineering Document Management (§16 Engineering, Manufacturing & Industrial)
Slug: engineering-document-management

---

## Research Goal

Understand how real software manages an engineering organization's controlled documents and drawings as records: registration/identity, revision discipline, review and approval, distribution, viewing/CAD integration, and handover into operations — and how this Type is bounded against Construction Document Management (the recorded joint-review obligation from the sibling pass), Product Data Management / PLM, Enterprise Content Management, Engineering Change Management, and generic file storage.

## Initial Boundary (pre-research hypothesis)

- Core guess: this is the design/EPC/owner-engineering organization's system of record for engineering documents (drawings, models, specs, datasheets, calculations, vendor docs) — a controlled vault with revision lineage and approval workflows, as opposed to:
  - Construction Document Management = the multi-party project's cross-organization issue/field-consumption register (sibling leaf, processed 2026-09-07, recorded a pending custody/consumption test against this leaf).
  - PDM/PLM = product/item-record-centric (CAD parts, BOMs, change orders), where documents are one object type among many.
  - ECM = generic enterprise content (office docs, email, records) without engineering-document semantics.
- Unknowns going in: whether transmittals are definitional or variant; whether CAD integration is definitional; how owner-operator (asset-anchored) vs EPC (project-anchored) deployments differ structurally; how much of the boundary with construction DM rests on document-control vs project-delivery semantics.

## Research Questions

1. What is the managed object — file, document record, or something else? What identity/numbering does it carry?
2. How do revisions/versions work — same record gaining revisions, one current/authoritative version, superseded history?
3. How does review/approval work — states, permissions per state, comments/audit, terminal states?
4. How are changes serialized (checkout/locks) and how does CAD authoring integrate (references/xrefs, title blocks, renditions)?
5. How are documents distributed to other organizations (transmittals/submittals) and does that machinery belong to this Type or to construction-side Types?
6. How do deployments anchor the document population — project/work-area (EPC/AEC) vs asset/facility (owner-operator) vs CAD vault (manufacturing)?
7. What distinguishes this Type from ECM, PDM/PLM, Engineering Change Management, and Construction DM — via the "remove X and it becomes the other Type" test?

## Representative Products

Selected for market structure, different product philosophies, different customer poles, and documentation accessibility:

1. **Bentley ProjectWise** (ProjectWise Explorer / Deliverables Management) — the archetypal AEC/infrastructure engineering document management platform; design-organization custody, CAD-integrated, project/work-area anchored. **Tier-1 evidence** (full operational help center reachable on docs.bentley.com).
2. **Accruent Meridian** — owner-operator / process-industry EDMS (oil & gas, chemical, pharma, utilities); lifecycle control of technical documents and drawings tied to operations and maintenance. **Tier-2 evidence** (official product page + FAQ; help center unreachable).
3. **AVEVA Asset Information Management** (with integrated Assai document control) — EPC/owner-operator information-management context; handover/commissioning emphasis; corroborates the market structure in which a dedicated document-control system handles "non-intelligent data" revision flows. **Tier-2 evidence** (official product page).

Considered but not sampled (source-access limitations, recorded per network rules):
- **Bentley ProjectWise marketing site** (bentley.com) — sign-in wall ×2; superseded by docs.bentley.com Tier-1 content.
- **Autodesk Vault** — help.autodesk.com renders a JS shell (no content); autodesk.com 403. CAD-vault/PDM pole therefore held by reasoning, not direct observation.
- **SOLIDWORKS PDM** — help.solidworks.com JS shell.
- **OpenText Engineering Document Management** — opentext.com 444; docs.opentext.com transport error.
- **AVEVA Document Management (classic product page)** — 404; product folded into AVEVA AIM position (sampled instead at Tier-2).
- **Siemens Teamcenter** — docs.sw.siemens.com 404.
- **Aras Innovator** — docs reachable but the Type there is PLM-platform; document management is a platform capability, not the defining purpose (boundary witness only).
- **Synergis Adept** — 404.
- **Assai** — transport error.

## Sources

- Bentley ProjectWise Explorer Help (2024): docs.bentley.com/LiveContent/web/ProjectWise Explorer-v2024/Help/en/index.html — full TOC + topic bodies: Creating Documents, Checking Out and Checking In Documents, Working with Document Properties, Working with Versions, Working with Workflows and States, Working with References and Sets, Working in Integrated Applications (MicroStation title blocks/attribute exchange, reference polling), Creating Renditions, PDF Markup Service, Audit Trail topics, Search topics, Spatial Tools.
- Bentley ProjectWise Deliverables Management Portal Help (2024): docs.bentley.com/.../ProjectWise Deliverables Management Portal-v2024/... — Sending Transmittals (body), Managing Incoming Submittals, PDF Review Workflow, RFIs, General Correspondences (TOC).
- Accruent Meridian product page + FAQ: accruent.com/products/meridian (positioning, capability bullets, EDMS-vs-ECM FAQ, compliance claims, integration list).
- AVEVA Asset Information Management product page + FAQ: aveva.com/en/products/asset-information-management/ (EPC/owner use cases, handover, Assai integration statement, standards CFIHOS/ISO 15926/ISO 14224).
- Sibling research: research/construction-document-management.md (§Boundary Findings — recorded joint-review obligation).
- Unreachable (limitations): Autodesk Vault, SOLIDWORKS PDM, OpenText EDM, Siemens Teamcenter, Assai, Synergis Adept, Accruent Meridian help center, Bentley marketing site.

**Source-access limitation**: no numeric limits, default values, exact state-name catalogs, or product-specific workflow configurations are asserted anywhere; the CAD-vault/PDM pole has no direct documentation evidence this pass and PDM/PLM boundary claims are held at reasoning strength.

---

## Product 1 — Bentley ProjectWise (ProjectWise Explorer + Deliverables Management)

Evidence layer: **A** (direct observation of official operational documentation)

### Key observations

**Organizational containers.** Documents live in a **datasource** (the repository), organized in **work areas** (project-like containers with types, custom attributes, participants/permissions) and **folders**; folders can be upgraded to work areas; custom folders can aggregate links to documents/folders/URLs. Work areas carry workflow assignments, rendition profiles, and per-participant permissions. (A)

**The managed object is a document record, not a file.** "Creating Documents" includes: drag files in; create a document and attach a file; **placeholder documents** (record with no file yet; multiple placeholders can be created at once — the register can be established before content exists); an **Advanced Document Creation Wizard** (multiple documents at once); and **Document Creation Conflicts** — when a created document matches an existing one, the system asks whether to skip, **create a new document**, or **create a new version of a document**. The system therefore adjudicates register identity: whether incoming material belongs to an existing record. Document properties include name, description, **file name (separate from document name)**, associated application, department, **environment attributes** (administrator-defined metadata sets per document class), permissions, workflow state. (A)

**Revision discipline.** "Working with Versions": documents have **versions** with **version labels** (default labeling rules exist; labels of the active version are editable); there is exactly one **active version**; **only the active version can be checked out** — opening a non-active version is read-only; versions can be copied/moved/deleted and have their own security. **Master documents and references**: a master document carries references; you can **lock a specific version of a reference to the master** or update to the active version — revision-lineage control over CAD-like dependency graphs. (A)

**Controlled change.** "Checking Out and Checking In Documents": check out = download to a **working directory** + **lock** (others see a lock icon; cannot check out or export); check in = commit to server + unlock; **check-in comments optional or required (configurable)**; **Update Server Copy** commits without checking in (others referencing the file can refresh their local copy); **Free** releases a lock without committing; **Copy Out** = read-only local copy; **unmanaged export** bypasses control (a documented escape hatch). Requires Checked In status and Read/File Read/File Write privileges. (A)

**Workflows and states.** A **workflow is an ordered group of states** through which a document passes; assigned to folders/work areas; **access control can be applied to each state** (only certain users can access a document in a given state); moving state requires Write + Change Workflow State permissions and (optionally) an **audit-trail comment**; **Final status** is a terminal, out-of-workflow state that makes the document **read-only regardless of permissions** (removable by privileged users); **workflow rules** (Rules Engine) can replace manual state changes with named operations — e.g., a "Revise" operation that places the document in a specific state **and creates a new version** — the vendor's own example couples revision creation to workflow progression; **email notifications** can be wired to state changes via a messaging agent. (A)

**CAD-native integration.** Working in Integrated Applications: MicroStation/AutoCAD integration — open/check in from the CAD application, **attach documents stored in the vault as references**, **reference polling/reloading** (periodic refresh prompts when references change), **attribute exchange and title blocks** (tag sets placed in drawings exchange values with document properties), **print sets**, **renditions** (generated renditions with rendition profiles per work area — PDF-class outputs from authoring formats), **PDF Markup Service** (marking up PDFs), **Dependency Viewer** (navigating document/model dependency maps), **Scan References and Link Sets** (discovering file references and registering them), **Components** (searchable objects inside files) and **spatial location** (documents placed geospatially; spatial views/search). (A)

**Search/visibility.** Quick search, advanced search by general properties, **environment attributes**, file properties, text; saved searches; export of document lists. Audit trail visible for documents and work areas. (A)

**Distribution to other parties.** The companion **Deliverables Management Portal** (separate product, connected to ProjectWise) sends **transmittal packages**: each package "describes the documents being sent, as well as the sender and the recipients; explains why the documents are being sent; specifies what is expected of the recipients in the way of acknowledgement or response." Transmittals move Draft → (review) → **Issue** (a permission: Issue package) → Outgoing; recipients respond; responses, response reports, and attachments are tracked; a transmittal can be recalled; **updated documents can be sent in a new version of the original transmittal**; due dates and reminders exist. Sibling package types: **submittals** (incoming, forwardable), **RFIs**, **general correspondences**, plus a **PDF review workflow**. (A)

### Reading of the vendor's model

```text
Datasource (repository)
└── Work Area / Folder (project container, participants, permissions, workflow)
    └── Document (record: name ≠ file, attributes, environment metadata, permissions)
        ├── Versions (labels; one active; non-active read-only)
        ├── Workflow states (ordered milestones; state-based access; Final = read-only)
        ├── References (master↔reference dependency graph; version locking)
        ├── Renditions / Components / Spatial location
        └── Audit trail (comments on state changes, check-ins)
Deliverables Management (companion): Transmittal / Submittal / RFI packages to external participants
```

## Product 2 — Accruent Meridian

Evidence layer: **A- (vendor's own positioning/FAQ) but Tier-2** — no operational help pages reachable.

### Key observations

- Positioning: "manage technical documents and drawings **throughout their lifecycle**, providing a centralized repository for storing, organizing, and controlling engineering documentation." Control = "version management, secure printing, up-to-date documentation, controlled data changes, and configurable workflows." (A-tier wording, Tier-2 source)
- **Concurrent engineering**: "real-time visibility into document revisions across projects and operations, automatically notifying teams of updates" — parallel changes tracked; revision awareness across projects/operations is a first-class selling point. (A-tier wording, Tier-2 source)
- **Compliance**: workflows + "comprehensive audit trails"; **electronic signatures** for formal approvals; named regimes FDA CFR Part 11, ISO 55000, GMP Annex 11; SOC 2 / ISO 27001 posture. (Tier-2)
- **Operations tie-in**: "single source of asset information"; up-to-date information **for work orders**; contractor documentation; integrations with **EAM, ERP, ECM, Office, and CAD applications**; a Meridian Cloud variant for Life Sciences (validated SaaS). (Tier-2)
- **Markup tools** for commenting/editing. (Tier-2)
- **EDMS vs ECM (vendor FAQ)**: "EDMS refers to engineering-specific organizations and associated documents **including drawings, mockups, environmental assessments, and technical data**. An ECM encompasses a broader range of content including emails, images, and other records, but is not specific to the engineering field." (A-tier wording, Tier-2 source — a vendor-drawn boundary consistent with this research's synthesis.)
- Customer base: TotalEnergies, Zurich Airport, AbbVie, Huntsman, mining/engineering firms — owner-operators and engineering companies; a case study titles "document exchange costs" (distribution machinery present in the product family).

### Reading

Same skeleton as ProjectWise at conceptual strength: document-of-record + revisions + workflows/audit + CAD/Office integration + operations-system integration; anchored to **assets/facilities** (owner-operator) rather than project work areas; compliance/e-signature depth is a distinguishing flavor.

## Product 3 — AVEVA Asset Information Management (with Assai document control)

Evidence layer: **B-** (market-structure witness; Tier-2 product page)

### Key observations

- Target context: EPCs aggregate "design data **P&IDs, 3D models, specs, and documents** into one single source of truth"; handover/commissioning ("efficient milestone handovers", "accelerate operational readiness"); owner-operators access historical engineering/asset data for maintenance. (Tier-2)
- The product manages the contextualized information core (documents, 3D models, laser scans) with data-quality/completeness reporting; for document control specifically: "integrated with the **Assai Document Control and Management System**, which proactively **controls document revision flows** to manage **non-intelligent data**," or customers keep their existing DMS. (Tier-2)
- Standards orientation: CFIHOS, ISO 15926, ISO 14224 (handover/information standards). (Tier-2)

### Reading

Corroborates: (1) engineering document populations are anchored to projects (EPC) and assets (owner); (2) **document revision-flow control** is a distinct, nameable function that even information-platform vendors package separately or integrate; (3) handover into operations is the terminal leg of the document lifecycle. AVEVA AIM itself sits adjacent (asset information), useful mainly for the boundary with asset/digital-twin platforms.

## Cross-product Comparison

| Dimension | ProjectWise (Tier-1) | Meridian (Tier-2) | AVEVA AIM+Assai (Tier-2) |
|---|---|---|---|
| Managed object | Document record (name ≠ file; placeholders; register-conflict adjudication) | Technical documents and drawings "throughout lifecycle" (version management) | Documents among information objects; revision flows via document-control system |
| Identity/attributes | Name, file, department, environment attributes, workflow state | version management, controlled data changes | contextualized by standards (CFIHOS/ISO) |
| Revision model | Versions with labels; one active; non-active read-only; reference version locking | revision visibility, parallel/concurrent changes | "proactively controls document revision flows" |
| Change control | Check-out/lock/check-in; configurable comments; Update Server Copy; Free | configurable workflows; controlled data changes | (via Assai; not operationally documented) |
| Approval workflow | Ordered states, state-based access control, Final status (read-only), rules engine, notifications, audit comments | configurable workflows, audit trails, e-signatures, CFR Part 11/GMP/ISO 55000 | data governance/completeness review before handover |
| CAD integration | Deep (in-CAD checkout, references, title-block attribute exchange, renditions, dependency maps, point clouds) | "integrations with … CAD applications" | documents + 3D models as information objects |
| Anchoring | Datasource → work areas/folders (project-anchored) | plant/asset operations context (asset-anchored) | project (EPC) and asset (owner) both |
| Distribution | Transmittal/submittal/RFI portal with issue permission, responses, recall, revision-linked re-issue | document exchange (case-study level) | milestone handover to owner |
| Operations tie-in | — (design side; AssetWise line covers operate) | work orders, EAM/ERP integration | maintenance/operations readiness, PI integration |
| Viewer/markup | Preview pane, PDF markup service, dependency viewer | markup tools | visualization on CONNECT |

Stable across all three (evidence B): controlled repository of engineering documents; revision discipline with a current version; governance of changes (workflow/audit; e-signature in compliance-heavy products); drawing/model content with CAD-adjacent handling; a terminal handover/publish leg into construction or operations.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (minimal)

The engineering-document record under revision-and-approval control, in engineering custody:

1. **The engineering document of record** — a persistent, individually identified record (register entry) for a piece of engineering deliverable material (drawing, model, specification, datasheet, calculation, vendor document…); files attach to the record, not vice versa; the record carries controlled attributes and lives in a structure the engineering organization owns (register/discipline/numbering). Remove → a file share/folder tree; files have no identity, no lineage.
2. **Revision lineage with one current authoritative version** — changes attach to the same record as new revisions/versions; prior versions are retained as superseded history; exactly one version is the current one that downstream consumers work from; superseded/current cannot be silently confused (identity conflict between incoming files and existing records is adjudicated — new record vs new revision). Remove → versionless or lineage-less storage; the "controlled drawing" concept (revision letters, supersede) — the essence of engineering document control — disappears; what remains is generic document/file management.
3. **Governed progression through controlled states** — documents move through named states (work-in-progress → review → approved/released, exact labels product-defined) under permission control (who may move, who may act in a state; approved/final states render read-only), with an attributable audit trail of the transitions. Remove → plain versioning (cloud-drive-class), not document management; the approval/audit spine that makes drawings contractually meaningful is gone.

Jointly-held is load-bearing:
- 1+2 without 3 = versioned file store (Dropbox-class) — no control.
- 1+3 without 2 = register with approval flags but no revision lineage — collapses toward generic QMS/DMS document control.
- 2+3 without 1 = versions and workflow with no document register — unrecognizable.
- Content scope (engineering deliverables, engineering-org custody) is part of the definition: remove it → ECM.

**Historical check (passed)**: pre-software engineering practice satisfies all three legs without any digital machinery — the drawing register (numbered records), title-block revision letters with superseded-status discipline (revision lineage, one current), the checker/approver signature block and distribution ledger (governed states, audit). No CAD integration, cloud, portals, or AI in the core.

### L1 — Common Mature Structure (very common, not definitional)

- **CAD application integration**: check in/out from within the authoring tool; management of **references/dependencies** (attach vault documents as references; lock or update reference versions); **title-block/attribute exchange** (drawing fields ↔ record metadata); **renditions** (publishing PDF-class outputs from authoring formats).
- **Viewing and markup** without authoring tools (preview, PDF markup, redlining).
- **Rich attribute search** over document metadata classes; saved searches; register reports/exports.
- **Per-document and per-container access control** (ownership, participants, state-gated access).
- **Audit trail surfaces** (who did what, when, with comments).
- **Document numbering/register helpers**: placeholders before content exists, bulk document creation, creation-conflict resolution.
- **Distribution packages to other parties** (transmittals/submittals with issue permission, acknowledgements, responses, revision-linked re-issue) — universal in project-facing deployments (and the signature surface of the construction-side sibling), but absent in vault-pole deployments that never leave the design org; therefore common-mature, not defining.
- **Integrations into operations systems** (EAM/ERP work orders; asset contexts) for owner-operator poles.
- **Model-content handling** (3D models as documents/items in the register; point clouds; spatial/geolocation of documents).

### L2 — Variant / Optional Structure

- Anchoring: **project/work-area** (EPC/AEC) vs **asset/facility** (owner-operator) vs **CAD-vault** (product/manufacturing design teams) vs enterprise-register (multi-project/multi-asset).
- Content emphasis: drawing/PDF-centric document control ("non-intelligent data") vs model-rich (BIM/CAD-native) registers.
- Deployment: on-prem enterprise vault vs SaaS portal/companion surfaces; compliance packaging (validated SaaS for regulated industries).
- Change-serialization posture: exclusive checkout/lock (CAD norm) vs co-authoring for office-type documents.
- Governance regimes: e-signature/validation-heavy (CFR Part 11, GMP Annex 11), records-retention formalism, standards-driven handover (CFIHOS/ISO 15926/ISO 14224), CDE/ISO 19650 framing in AEC.
- Extras: spatial location, components/classification searches, dependency visualization, AI-assisted search/classification (era-current).

### L3 — Vendor-specific (kept out of the final document)

ProjectWise: datasource/work-area/environment terminology, Rules Engine operations, InterPlot, Deliverables Management portal packaging, AssetWise operate-side sibling. Meridian: BlueCielo heritage modules, Meridian Cloud Life Sciences packaging, RedEye integration. AVEVA: CONNECT platform, Assai OEM relationship, Information Standards Manager. Numeric limits/defaults: none asserted (no operational evidence for Meridian/AVEVA; ProjectWise specifics like "state-based permission names" held in research notes only).

## Vendor-specific Findings

- ProjectWise's **"Final" status as an out-of-workflow terminal state** and **Update Server Copy** (commit-without-check-in so reference users can refresh) are product designs, not Type invariants — but they evidence the general rules (terminal read-only state; revision publishing while change stays open).
- Meridian's **secure printing** and **concurrent-engineering notifications** are vendor features evidencing L1 needs (controlled reproduction; revision awareness across concurrent work).
- AVEVA's **standards-driven data-quality/completeness reporting before handover** evidences the handover leg without defining it.

## Boundary Findings

- **vs Construction Document Management (sibling §17, joint-review obligation)** — *resolved from this side*. The custody/consumption test ratifies keep-both: Engineering Document Management is the **engineering organization's vault of record** — custody of documents it authors/controls through revision-and-approval; the working population is the design team and the document register is the object of record. Construction Document Management is the **project's cross-organization issue and field-consumption register** — the document register exists so that many independent organizations receive, view, and mark up issued revisions, and so the project has a record of what was issued to whom. Remove the design-org custody/authoring-side revision control → Construction DM; remove the multi-party issue/field consumption → EDM. Products straddle (an EDM grows an issue/transmittal face — ProjectWise Deliverables Management; a construction platform's document tool can serve an engineering org), so the boundary is drawn on primary custody/consumption, as the sibling pass proposed. The construction side's caveat that it "was not sampled against a ProjectWise-class product" is hereby discharged: this pass documented the ProjectWise-class product directly (Tier-1), and its core (register + checkout/lock + versions + state workflows) is design-org custody machinery, with the cross-org issue machinery present as a companion/portal surface. **Joint review discharged; keep-both ratified.**
- **vs PDM / PLM (Mechanical CAD vaults, e.g. Autodesk Vault / SOLIDWORKS PDM / Teamcenter-class)** — held at reasoning strength (vendor docs unreachable this pass; marked accordingly). Conceptual seam: PDM centers on **CAD item/part records and the CAD-file vault** bound to BOMs, items, and change orders; document records (drawings, specs, reports) are the center here, without item/BOM semantics. A pure CAD vault that only manages CAD files of parts sits at this Type's edge (vault-pole variant) or inside PDM depending on whether document-record semantics (register, transmittals, spec/revision-of-record for non-CAD deliverables) are present. No directory contradiction found; recorded as a boundary note, not an escalation.
- **vs Enterprise Content Management** — vendor-drawn (Meridian FAQ) and reasoning-consistent: ECM manages general enterprise content (email, images, records) without engineering-document semantics; remove engineering-document custody/revision-of-record semantics → ECM. Also confirms reverse: ECM is frequently *integrated with* EDM as the broader content layer.
- **vs Engineering Change Management (§16 sibling)** — ECM manages the change *process objects* (requests/orders driving change across items and documents); EDM manages the *documents* as records. A change order may trigger document revisions, but the register-of-record, revision lineage, and state workflow of the documents live here.
- **vs Product Lifecycle Management** — PLM's center of gravity is the product record (items/BOMs/changes/portfolio); document management appears as a module. EDM's center is the document register for engineered assets/projects regardless of BOM presence (AEC/owner deployments have no BOM).
- **vs Enterprise Records Management** — retention/disposition-centric, content-agnostic; EDM is revision/approval-centric and content-specific. Compliance packaging overlaps in regulated deployments.
- **vs generic file storage / cloud drives** — no register identity, no revision-of-record authority, no governed approval states; the remove-test collapses it to file storage (L0 leg 1 and 3 gone).
- **vs BIM Coordination / Construction Closeout** — coordination consumes issued models/documents in a federation/comparison process; closeout consumes the register to assemble the handover record; neither holds the document register as its object of record.

## Uncertainties

1. **CAD-vault pole (Autodesk Vault-class) left undocumented** — the claim that a pure CAD vault satisfies the L0 (and where exactly it crosses into PDM) rests on reasoning + market structure, not direct product documentation. Marked in Sources.
2. **Transmittal commonality strength** — directly evidenced (Tier-1) in the AEC pole only; Meridian evidence is case-study level ("document exchange costs"); owner-operator deployments may emphasize EAM-linked retrieval over formal transmittals. Held at L1 ("common in project-facing deployments"), not stronger.
3. **State-name catalogs, numeric limits, retention defaults** — not asserted anywhere (no operational evidence for Meridian/AVEVA; ProjectWise specifics not load-bearing for the Type).
4. **Whether some modern products replace exclusive checkout with co-editing for office-type documents** — asserted only as a posture variant (ProjectWise documents the lock model; Meridian claims "parallel changes" support at Tier-2; no product documented as fully co-editing CAD).
5. **AVEVA AIM/Assai inner workings** (revision-flow mechanics) — Tier-2 only; used as market-structure witness, not as a model source.

## Final Synthesis

An Engineering Document Management application is the engineering organization's system of record for its engineering documents and drawings as **registered records**: each record persists independently of its files, accumulates a revision lineage of which exactly one version is current and authoritative, and advances through permission-gated, audited states from authoring to approval — after which the approved revision is published (renditions, transmittals, handover) to the parties who consume it, without authoring rights. Around this core, mature products add CAD-integrated authoring (checkout within the design tool, reference management, title-block exchange), viewer/markup surfaces, metadata search, register reports, distribution packages, and operations-system integrations; deployments vary by anchor (project, asset, CAD vault), content emphasis (drawings/PDF vs models), and governance regime (e-signature/validated, standards-driven handover). The Type is bounded from Construction Document Management by custody/consumption (design-org vault vs cross-org issue register), from PDM/PLM by the center of record (documents vs items/BOMs), and from ECM by engineering-document semantics.
