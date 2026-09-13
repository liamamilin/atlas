# Research Notes — Archives Management System

Research date: 2026-09-10
Leaf: Archives Management System (DIRECTORY.md §23 Education, Research & Knowledge Institutions)
Slug: archives-management-system

## Research Goal

Understand what an Archives Management System (AMS) actually is as an Application Type: the system of record an archival institution uses to gain intellectual and physical control over archival holdings — unique, unpublished materials of enduring value — and to make them discoverable and retrievable. Produce a vendor-neutral canonical model and hold the boundaries against the many neighboring GLAM / records Types already processed in this directory.

## Initial Boundary (hypothesis before research)

- Core hypothesis: an AMS centers on **archival description** — multi-level, provenance-based description of aggregations (fonds/collections → series → files → items) — anchored to records creators, rendered as **finding aids**, with accessioning as the intake instrument.
- Nearest neighbors to test: Institutional Repository, Digital Library Platform, Museum Collections Management, Integrated Library System, Library Discovery Platform, Enterprise Records Management, Government Records Management, Cultural Heritage Asset Management.
- Prior recorded seams that constrain this pass:
  - institutional-repository (2026-09-08): "vs archives-management-system (output self-archiving vs finding-aid description)".
  - digital-library-platform (2026-09-07): curated digital collection delivery, digital item as unit of record.
  - museum-collections-management (2026-09-08): object-level custody accountability is the museum line.
  - enterprise-records-management (2026-09-06) / government-records-management (2026-09-08): retention/disposition governance of active records; GRM's disposition "transfer to archives" is the handoff point.

## Research Questions

1. What is the unit of record? Is it the archival description, and at what levels?
2. How is the description hierarchy structured, and what archival principles govern it (provenance, original order, multi-level description)?
3. What are authority records (creators) and how do they link to descriptions?
4. What is accessioning, and how does it relate to description (accruals, deaccessions, field inheritance)?
5. What is the finding aid, and how does the system produce/deliver it (generated documents, public UI, export)?
6. How do digital objects attach to descriptions — and where is the DAM boundary?
7. What access/request machinery exists (public search, browse, treeview, reading-room requests)?
8. What standards shape the data model (ISAD(G), ISAAR(CPF), ISDIAH, ISDF, DACS, RAD, EAD, EAC-CPF, PREMIS)?
9. What roles exist (archivist, contributor, editor, administrator, researcher/public)?
10. What physical storage / location management exists, and is it definitional?
11. Where exactly are the boundaries vs IR / DLP / museum CMS / ERM-GRM / ILS?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| ArchivesSpace | Open-source community-governed application (LYRASIS organizational home); dominant in US academic/special collections; DACS-centered; merged from Archivists' Toolkit + Archon (v1.0 2013) | The community-standard description-centered tool; exceptionally explicit boundary statements |
| AtoM (Access to Memory) | Open-source (Artefactual); ICA standards-native (ISAD(G), ISAAR(CPF), ISDIAH, ISDF); web-delivery-first; multilingual; multi-repository union-list capable | The international-standards pole; richest public documentation |
| Axiell CALM | Commercial, UK/Europe heritage sector; "designed by archivists, for archivists"; ISAD(G)/ISAAR(CPF)/EAD/EAC; companion public product (CalmView); transitioning to Axiell Collections | The commercial European heritage-suite pole |
| PastPerfect | Commercial, small institutions (museums, historical societies, small archives); combined collections tool where Archives is one of four catalogs (Objects/Photos/Archives/Library) | The small-shop / combined-collections pole; tests the museum-CMS boundary from inside a hybrid product |

## Sources

Tier 1/2 official surfaces fetched 2026-09-10:

- ArchivesSpace
  - https://archivesspace.org/ (positioning)
  - https://archivesspace.org/features (functional areas: accessioning, arrangement & description, assessment, location management, authority control, standards, staff/public UI)
  - https://archivesspace.org/application/specifications (module structure: main/supporting/sub-record specifications)
  - https://archivesspace.org/resources/user-resources/getting-started (training workflow; DACS as out-of-box standard)
  - https://archivesspace.atlassian.net/wiki/spaces/ADC/overview (wiki overview: core functions, reference service, metadata authoring)
- AtoM
  - https://www.accesstomemory.org/en/docs/2.10/ (documentation index)
  - .../user-manual/overview/intro/ (What is AtoM: positioning, standards, multi-repository)
  - .../user-manual/overview/entity-types/ (core entities and relationships)
  - .../user-manual/add-edit-content/archival-descriptions/ (hierarchy, draft/publish, calculate dates)
  - .../user-manual/add-edit-content/accessions/ (accession workflow, accruals, donors, events, rights)
  - .../user-manual/reports-printing/print-finding-aid/ (finding-aid generation/upload/download)
- Axiell
  - https://www.axiell.com/uk/solutions/product/calm/ (CALM product page)
  - https://www.axiell.com/solutions/product/axiell-collections/axiell-collections-packages/ (Archive package features/standards)
- PastPerfect
  - https://museumsoftware.com/ (positioning)
  - https://museumsoftware.com/pp5.html (catalogs incl. Archives; reports; online access)
  - https://museumsoftware.com/webedition.html (Web Edition: accessions/loans/exhibits; Public Access)

Access limitations: ArchivesSpace member Help Center is members-only (public wiki overview + features + specifications used instead). Axiell CALM detailed user documentation sits behind the support portal (documentation.axiell.com index reachable but per-topic pages not fetched); CALM claims rest on official product pages (Tier 2). PastPerfect archives-specific depth (e.g., finding-aid support) not directly documented on fetched pages; claims kept modest. Evidence strength calibrated accordingly.

## Product Observations

### ArchivesSpace (evidence layer A unless noted)

- Positioning: "open-source archives information management application for managing and providing access to archives, manuscripts and digital objects"; "supports a range of archival functions, including accessioning, arrangement, description, preservation, and access."
- Wiki overview: "designed to support core functions in archives administration such as accessioning; description and arrangement of processed materials including analog, hybrid, and born-digital content; management of authorities (agents and subjects) and rights; and reference service. The application supports collection management through collection management records, tracking of events, and a growing number of administrative reports. The application also functions as a metadata authoring tool, enabling the generation of EAD, MARCXML, MODS, Dublin Core, and METS formatted data."
- Accession records: "store information about the receipt of materials, whether it be a single item or an aggregation"; linkable to Resource, Digital Object, subject, name, collection management, and other accession records; data can be "spawned" to create other record types.
- Arrangement & description: Resource records (physical) / Digital Object records (digital) carry "the bulk of information about the intellectual and physical characteristics of archival materials"; a Resource "may be comprised of one item, or, most typically, it will be an aggregation of items that can be of any extent or complexity"; descriptive elements, notes, rights statements, linked repository records; supplemented with linked authority records.
- DAM boundary (explicit): "ArchivesSpace is not a digital asset management system. Digital Objects cannot be ingested into and do not reside within it. It can be used to create metadata about digital content, and to link to content stored on a web server or another system, serving a single point of access and system of record for both physical and digital materials."
- Circulation boundary (explicit): "ArchivesSpace can track the location of materials but is not a circulation management system."
- Location management: Location records describe shelving locations (shelves, drawers, file cases, bins, walls); web locations managed via URIs in Digital Object records.
- Authority control: Agent records "uniquely identify persons, families, corporate entities, or software that have a specified relationship to archival materials in the custody of a repository"; variant name forms; agent-to-agent relationships; Subject records for themes/contents/format; both linkable to accessions, resources, digital objects, and components.
- Assessment records: quantitative/qualitative condition, readiness for reformatting/housing/arrangement, research value; linkable to accessions, resources, components, digital objects.
- Standards: DACS is the underlying descriptive standard ("out of the box"); adaptable to others (e.g., ISAD(G) via customization); import/export EAD, EAC-CPF, MARCXML, METS, MODS, Dublin Core.
- Interfaces: staff UI with unlimited user accounts and granular permissions; **optional** public user interface (PUI) — "only those records deliberately published by a user will be made accessible in the public user interface."
- Module structure (specifications page): main modules = Archival Object, Accessions/Deaccessions, Resource, Digital Object; supporting modules = Agent, Repository, Staff User, Location, Subject, Event; sub-records = Date, Extent, External Document, Rights Management, Collection Management.
- Training workflow (getting-started): session 1 accession record + single-level resource; session 2 multi-level resource records + container management + rapid data entry; session 3 digital object, agent, subject records; session 4 location records, import/export, customization.
- History: integration of Archivists' Toolkit and Archon; v1.0 released 2013; Mellon-funded origins; 550+ member institutions (marketing figure — not used in final doc).

### AtoM (evidence layer A unless noted)

- Positioning: "web-based, open source application for standards-based archival description and access in a multilingual, multi-repository environment."
- Multi-repository: "can be used by a single institution for its own descriptions or ... set up as a multi-repository 'union list' accepting descriptions from any number of contributing institutions."
- Standards: built around ICA standards — ISAD(G) (descriptions), ISAAR(CPF) (authority records), ISDIAH (archival institutions), ISDF (functions); SKOS for vocabularies; additional templates DACS, RAD, Dublin Core, MODS; PREMIS rights elements.
- Entity types (user manual): accession record, archival description, authority record, archival institution, function, rights record, term (+ donors, deaccessions, physical storage).
- Archival description: "a body of information about an archival record or records ... arranged into hierarchical levels (fonds, series, files, items, and variations of these in accordance with institutional standards)." Also an activity: "the outcome of a process to gain intellectual control over a resource or collection of resources and provide end users (such as researchers) with a means of conceptualizing the organization of these resources and navigating to the specific content."
- Pitti quote (documentation cites): "Archival description represents a fonds, a complex body of materials ... sharing a common provenance. The description involves a complex hierarchical and progressive analysis. It begins by describing the whole, then proceeds to identify and describe sub-components of the whole ... The description emphasizes the intellectual structure and content of the material, rather than their physical characteristics."
- Hierarchy mechanics: parent/child records; "on the fly" child creation as stubs; treeview context menu for navigation; level-of-description field; move/duplicate/delete; modification history; alternative identifiers; identifier masks with auto-generation.
- Publication lifecycle: new descriptions default to DRAFT; drafts invisible to unauthenticated users; publishing grants public read access; publication status inheritable down the hierarchy ("Update descendants", asynchronous job); publish permission separate from edit permission (a user without publish permission causes a published record to revert to draft on save).
- Dates: "Calculate dates" task computes parent controlled date ranges from descendants; display date is free text (approximation/uncertainty typography), controlled ISO dates used for range search/sorting; warning when child dates exceed parent range.
- Accession record: "administrative and descriptive information that identifies the contents, provenance and disposition of the materials transferred to the archival institution ... designed to establish basic intellectual and physical control over a new accession at the time it is received." "Not aimed at end-user description" but can spawn an archival description with field inheritance (title, name of creator, archival/custodial history, scope & content, physical condition; name access points and rights also inherited).
- Accession mechanics: unique accession number (mask-generated, uniqueness enforced); alternative identifiers (legacy IDs, transfer IDs, barcodes) with type + note; donor records (contact, location); events (typed, dated, agented — audit trail of accession actions; CAAIS-derived event types); rights records; accruals (accrual cannot have accruals; unlimited accruals on the original); deaccession records (recommended over deletion); legacy accession import (CSV / mask alteration); physical storage container linking (many-to-many).
- Finding aid: "AtoM allows logged-in users to generate printer-friendly finding aids in either PDF or RTF format"; or upload locally created finding aids; one finding aid per archival unit (descriptive hierarchy), generatable from any level; downloadable by any user (public sees download link when description published); cover page (institution, title, generation date, source URL), TOC, headers/footers; "Inventory summary" vs "Full details" layouts; draft exclusion setting; physical-storage visibility interplay with Visible elements module; regeneration required after edits ("finding aids are not automatically updated when you make edits").
- Access surfaces: search, advanced search (incl. date-range), browse, navigate, clipboard; public users are read-only researchers.
- Roles: administrator, editor, contributor, translator, researcher (read-only) — per user-roles documentation.
- Admin: user accounts/groups, granular permissions, jobs (async scheduler), menus, plugins, themes, visible elements, settings; OAI repository; CSV/XML import-export; API (information objects CRUD, digital object download, physical object add).

### Axiell CALM (evidence layer A for product-page claims; Tier 2 source — strength reduced)

- Positioning: "Designed by archivists, for archivists. Calm archive management software is built on a foundation of international standards for archival and curatorial collections management."
- Functions: "cataloguing, managing locations and movements, or managing archive conditions"; "Create workflows that help your team manage reading room requests and requests for information from the public."
- One database for "physical records, born digital and digital copies" plus "a wide variety of multimedia files that relate to the collection within the system."
- Standards: "Built to SPECTRUM standards as well as ISAD(G), ISAAR(CPF), EAD, EAC."
- Authority: "Link to external thesauri and people databases through Linked Open Data."
- Structure: "Store, link and manage data using a sophisticated hierarchy-based data structure."
- Reporting: "monitor data entry and digitization statistics." Import/export XML incl. EAD. Open API.
- Companion products: CalmView ("Publish your collections online"); Axiell Move (item relocations with barcode scanning); hosting service.
- Axiell Collections Archive package (successor line): "Archive accessions and accruals • Indexing of names, subjects and locations • Define and manage retention schedules • Location management • Conservation management • Reading room • Acquisition • Basic library cataloguing"; standards ISAD(G), ISAAR(CPF), DACS, RAD, MAD, Australian Series System, RDA, FRBR, OAI-PMH; catalogue areas follow ISAD(G) groupings (Identity statement, Context, Content and structure, Conditions of access and use, Allied materials, Condition/Conservation, Reproductions, Notes & Description control); "on-screen 'tree structure' display enables you to readily browse through all the levels of the catalogue, however complex."

### PastPerfect (evidence layer A for product-page claims; archives depth limited — strength reduced)

- Positioning: museum collection and contact management software; desktop (5.0) and cloud (Web Edition).
- Catalogs: "Document collections of all types and sizes using the Objects, Photos, Archives, and Library catalogs, with fields specific to each type of collection based on common standards and practices." — Archives is one catalog inside a broader collections tool.
- Web Edition: "tools to manage your collection with ease, including accessions, loans, exhibits, and more. From archival, art, and archaeology to historic, ethnographic, and photographic collections..."
- Public Access: "Only the records, data, and images you choose are shared in a searchable database for web visitors."
- Inventory Manager upgrade: inventory lists, barcode labels, electronic collection tracking.
- Contacts side (membership, donations, mailings) is museum-association machinery, not archives-specific.

## Cross-product Comparison

| Dimension | ArchivesSpace | AtoM | Axiell CALM | PastPerfect |
|---|---|---|---|---|
| Unit of record | Resource (aggregation) + Archival Object components; Accession; Digital Object | Archival description (multi-level); Accession; Digital object | Hierarchical catalogue records (ISAD(G) areas); Accessions | Records in an "Archives" catalog (alongside Objects/Photos/Library) |
| Hierarchy | Resource → components (multi-level, any extent/complexity) | Parent/child levels of description (fonds → series → file → item), treeview | "Sophisticated hierarchy-based data structure", tree-structure display | Catalog-level; archival hierarchy depth not evidenced in fetched pages |
| Creator anchoring | Agent records (persons/families/corporate entities/software) linked to all record types | Authority records (ISAAR(CPF)) linked via dated events; many-to-many | ISAAR(CPF); linked open data to external thesauri/people databases | Names as access points (depth not evidenced) |
| Accessioning | Accession records; spawn to other records; deaccession spec | Accession records; accruals; deaccessions; donors; events; field inheritance into description | "Archive accessions and accruals" | Accessions among Web Edition tools |
| Digital objects | Digital Object records = metadata + links; explicitly NOT a DAM | Digital objects uploaded/attached; download API | "Physical records, born digital and digital copies within one database" | Multimedia attachments; online image sharing |
| Physical storage | Location records (shelves/drawers/cases/bins); "not a circulation management system" | Physical storage module; container linking; box-label reports; storage in finding aids toggleable | "Managing locations and movements"; location management | Inventory Manager (barcodes, tracking) as add-on |
| Standards | DACS out-of-box; EAD/EAC-CPF/MARCXML/METS/MODS/DC | ISAD(G)/ISAAR(CPF)/ISDIAH/ISDF native; DACS/RAD/DC/MODS; PREMIS rights; SKOS | ISAD(G), ISAAR(CPF), EAD, EAC (+ SPECTRUM); Archive package adds DACS/RAD/MAD/Australian Series System | "Common standards and practices" (unspecified) |
| Publication control | Deliberate publish to optional PUI | Draft/published with descendant inheritance; publish permission distinct | Not evidenced on fetched pages (CalmView companion publishes) | "Only the records ... you choose are shared" |
| Finding aid | EAD generation as metadata authoring; PUI display | Generated/uploaded PDF/RTF finding aid per archival unit, public download | Not evidenced as document generation on fetched pages; catalogue is the access vehicle | Not evidenced |
| Public access | Optional PUI | Built-in public UI (web-first) | CalmView companion product | Public Access add-on site |
| Roles | Staff accounts with granular permissions; public PUI users | Administrator/editor/contributor/translator/researcher | Not evidenced | Staff; public visitors |
| Deployment | Self-hosted open source; membership program | Self-hosted open source; hosted providers | Commercial; hosting service; transitioning to web-based Axiell Collections | Desktop or cloud commercial |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The multi-level archival description as the unit of record.** Persistent, individually identified descriptions of archival units — aggregations of unique, unpublished materials and their component parts — organized as a hierarchy from general to specific (whole described first, then sub-components). The description emphasizes intellectual structure and content over physical characteristics. Remove → a flat document catalog / bibliographic database; the Type collapses.
2. **Provenance anchoring.** Descriptions are bound to the records creators (persons, families, corporate bodies) held as authority records, and the hierarchy expresses arrangement by provenance — who created or accumulated the materials and how the parts relate. Remove → an inventory of documents with no creator context; retrieval by provenance — the archives' defining retrieval logic — disappears.
3. **Finding-aid production as the access instrument.** The system renders descriptions into navigable finding aids — on-screen hierarchical navigation, generated/downloadable finding-aid documents, or exported/published description data — through which staff and researchers discover holdings and request access to materials. Remove → an internal description store with no access function; the archives' central professional instrument disappears.

Jointly-held is load-bearing:
- 1 alone = a hierarchical catalog database (no creator context, no access instrument).
- 2 alone = an authority file / prosopography tool.
- 3 without 1+2 = a publishing surface with nothing archival behind it.
- 1+2 without 3 = a description database nobody can use to find materials.
- 1+3 without 2 = finding aids without provenance (inventories of anonymous documents).
- 2+3 without 1 = creator biographies with no holdings description.

### L1 — Common Mature Structure

Present across the sample (evidence layer B), expected in mature products but not definitional:

- **Accession records** documenting receipt/transfer (provenance, contents, legal/physical transfer, donor, rights), with **accruals** (additions to existing holdings) and **deaccessions** (documented removal), and field inheritance/spawning into descriptions.
- **Digital object records/metadata** attached to descriptions — with the explicit caveat (ArchivesSpace) that the AMS is metadata + links, not a digital asset management system; some products (CALM) hold digital copies in the same database.
- **Physical storage / location management** — shelving locations, containers, box labels, movement tracking; container-level, not object-circulation-level.
- **Controlled vocabularies / access points** — subject and place terms, thesauri, sometimes linked open data.
- **Standards-based templates and exchange** — ISAD(G)/DACS/RAD description templates, ISAAR(CPF) authority templates, EAD/EAC-CPF/MARCXML/MODS/DC/METS import-export, OAI harvesting.
- **Publication status machinery** — draft vs published, inheritance down the hierarchy, deliberate publication as the gate to public visibility.
- **Staff/public interface split** — staff cataloguing workbench with granular permissions and roles; public search/browse/treeview for researchers.
- **Search and navigation** — keyword/advanced search (incl. date ranges), browse, hierarchical treeview navigation.
- **Reports** — file/item lists, box labels, data-entry/digitization statistics.
- **Rights records** — access restrictions (copyright, license, statute, policy) with inheritance down the hierarchy.
- **Events / audit trail** on records (accession events, modification history).
- **Identifier machinery** — reference codes, accession-number masks, alternative identifiers.

### L2 — Variant / Optional Structure

- **Standards flavor**: ICA international (ISAD(G)/ISAAR(CPF)) vs US DACS vs Canadian RAD vs Australian series system; institution-configurable templates.
- **Public access posture**: built-in public UI (AtoM web-first) vs optional PUI (ArchivesSpace) vs companion publishing product (CalmView) vs add-on public site (PastPerfect Public Access) vs export-only (EAD published elsewhere).
- **Single repository vs multi-repository union list** (AtoM explicitly supports both).
- **Combined collections suites**: archives as one catalog inside a museum/library collections product (PastPerfect; Axiell Collections packages) vs archives-dedicated products (ArchivesSpace, AtoM, CALM).
- **Scale/deployment**: solo-archivist small shop (desktop or hosted) vs large multi-repository networks; self-hosted OSS vs commercial hosting.
- **Reference/reading-room workflows**: reading-room request management documented explicitly at CALM; "reference service" named in ArchivesSpace's overview; depth varies.
- **Multilingual content and interface** (AtoM).
- **Adjacent machinery**: assessment/condition surveying (ArchivesSpace), conservation management (CALM/Axiell Collections), retention schedules inside the archives product (Axiell Collections Archive package — note: this is records-management machinery embedded at the suite level), digitization statistics.

### L3 — Vendor-specific (research notes only)

- ArchivesSpace: "spawn" from accession to other record types; assessment records; collection management records; top-container/container model; optional PUI as a distinct interface; membership-governance model; Archivists' Toolkit + Archon lineage.
- AtoM: Gearman job scheduler; identifier masks with legacy-accession alteration; Visible elements module; clipboard; RAD-formatted finding-aid generation; donor dialog with geo fields; SKOS import/export; OAI repository; multi-repository union list; AGPL licensing.
- Axiell CALM: CalmView companion; Axiell Move barcode relocation companion; SPECTRUM compliance; linked-open-data thesauri; migration path to Axiell Collections.
- PastPerfect: four-catalog structure (Objects/Photos/Archives/Library); Inventory Manager upgrade; contacts/membership/donor machinery inherited from the museum-CMS side.

## Rejected Findings (not promoted to core)

- **Accessioning as definitional**: rejected. Descriptions can be created directly (legacy/backlog cataloguing); accessioning is the common intake instrument but not required to recognize the Type. (AtoM documents description creation independent of accessions; ArchivesSpace resources can exist without accessions.)
- **Digital objects as definitional**: rejected. ArchivesSpace explicitly states it is not a DAM and digital objects are metadata + links; the paper-era archive satisfies the core with zero digital objects.
- **Built-in public web UI as definitional**: rejected. ArchivesSpace PUI is optional; CALM publishes via a separate companion product; export-only publication satisfies the finding-aid leg.
- **Specific standards (ISAD(G) or DACS) as definitional**: rejected. Multiple standards across products and regions; the invariant is multi-level provenance-based description, not any one standard.
- **Location/barcode tracking as definitional**: rejected. Container-level tracking is common but the museum-style per-object custody accountability is not the archives line (museum-collections-management pass holds that).
- **Reading-room request workflows as definitional**: only explicitly documented at one product (CALM); ArchivesSpace names "reference service" without fetched detail. Held as common/variant.
- **Retention schedules inside the AMS**: rejected as core — that is records-management machinery appearing at the suite level (Axiell Collections Archive package); the AMS's materials are already appraised permanent holdings.

## Boundary Findings

| Neighbor Type | Seam | "Remove what → becomes the other Type" |
|---|---|---|
| Institutional Repository | IR holds the institution's **own scholarly output** via deposit, open-access delivery posture; AMS describes **archival materials** (transferred/acquired records of enduring value) via finding aids. Matches the seam recorded by the IR pass ("output self-archiving vs finding-aid description"). | Change the corpus to self-deposited scholarly works and the posture to open-access delivery → IR. |
| Digital Library Platform | DLP's unit is the **digital item** bound to content files, curated for delivery; AMS's unit is the **description** of holdings, often physical, digital objects optional. ArchivesSpace's own words: "not a digital asset management system." | Make the digital item + delivery the center and drop the provenance hierarchy → DLP. |
| Museum Collections Management | Museum = **object-level custody accountability** (per-object location, loans, exhibitions); archives = **aggregation-level description** by provenance; archives location tracking is container-level. PastPerfect shows the hybrid (Archives as one catalog beside Objects). | Shift to per-object custody events (loans/exhibits/condition) → museum CMS. |
| Enterprise / Government Records Management | ERM/GRM govern **active/semi-active business records** under retention/disposition schedules; AMS manages **permanent holdings of enduring value**. GRM's "transfer to archives" disposition is the handoff into accessioning. | Remove description/finding-aid core, keep retention/disposition governance → ERM/GRM. |
| Integrated Library System | ILS = **published** materials, item-level bibliographic records, **circulation**; AMS = unique materials, aggregation-level description, no circulation (ArchivesSpace: "not a circulation management system"). | Make items published copies circulating on loan rules → ILS. |
| Library Discovery Platform | LDP is a **search layer over** a resource universe (catalog + indexes + repositories); AMS is the archives' **own system of record**. An AMS public UI can feed a discovery layer but is not one. | Reduce to configured search over external sources with get-it paths → LDP. |
| Cultural Heritage Asset Management | CHAM registers **place-based heritage resources** (monuments/buildings/sites) with spatial anchoring; AMS describes **held archival materials**. | Shift the record unit to geographic heritage assets → CHAM. |

## Historical / Market-Sample Check

Paper-era archives office: accession register (documents legal/physical transfer), typed finding aids + card catalogs arranged by provenance (multi-level description: fonds → series → box → folder), reading-room card catalog (access instrument). All three L0 legs satisfied with zero software, web UI, EAD, digital objects, controlled vocabularies, or barcodes. Therefore none of those belong in L0.

Regional check: US DACS repositories, ICA-standard international archives, Canadian RAD institutions, and Australian series-system archives all satisfy the L0 — the hierarchy vocabulary differs (fonds-centered vs series-centered) but "multi-level description from general to specific, anchored to creators, rendered as finding aids" holds across all. L0 vocabulary is kept neutral accordingly ("levels of description", "records creators") rather than mandating fonds.

## Uncertainties

- CALM detailed behavior (finding-aid generation, publication control mechanics, role model) rests on product pages only; detailed docs behind support portal. Claims about CALM kept at product-page strength.
- PastPerfect's archival hierarchy depth (true multi-level description vs flat archives catalog) not verified from fetched pages; PastPerfect used only as the combined-collections/small-shop pole.
- ArchivesSpace member Help Center (detailed per-record workflows) is members-only; public features/specifications/wiki-overview used. The "spawn" and assessment details are from official public pages (layer A) but per-field workflows unverified.
- Whether reference/reading-room request machinery is universal could not be confirmed across the sample; held as common-to-variant.
- Precise numeric limits (description counts, hierarchy depth caps, file-size limits) deliberately not stated — not researched to that precision.

## Final Synthesis

An Archives Management System is the archival institution's description system of record. Its defining core is exactly three jointly-held structures: (1) the multi-level archival description as unit of record — persistent identified descriptions of aggregations of unique, unpublished materials, hierarchical from general to specific; (2) provenance anchoring — descriptions bound to records creators held as authority records, the hierarchy expressing arrangement; (3) finding-aid production as the access instrument — descriptions rendered into navigable, downloadable, or published finding aids through which holdings are discovered and requested. Accessioning, digital objects, storage/location tracking, controlled vocabularies, standards exchange, publication control, staff/public interface split, search, and reports are the common mature furniture. The Type is bounded against IR (own-output deposit vs holdings description), DLP (digital item delivery vs holdings description), museum CMS (object custody vs aggregation description), ERM/GRM (active-records governance vs permanent-holdings description), ILS (published circulation vs unique non-circulating), and LDP (search layer vs system of record).
