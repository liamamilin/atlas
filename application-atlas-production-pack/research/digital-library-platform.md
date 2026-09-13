# Research Notes — Digital Library Platform

Research date: 2026-09-07
Slug: digital-library-platform
Directory leaf: Digital Library Platform (§23 Education, Research & Knowledge Institutions)

---

## Research Goal

Understand what a Digital Library Platform actually is as an Application Type: what objects exist inside it, how digital content enters it, how it is organized, discovered, and delivered to end users, and where its boundary lies against neighboring library/cultural-heritage Types (ILS, Library Discovery Platform, Institutional Repository, Archives Management System, E-book Library Application, CMS).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: institution-operated software that hosts a curated collection of digital items (metadata + content files), organizes items into collections, and provides search/browse and public delivery.
- Likely neighbors: ILS (physical circulation ops), Library Discovery Platform (search layer over external sources), Institutional Repository (scholarly-output subtype), Archives Management System (archival description/finding aids), E-book Library Application (consumer personal library), CMS (generic web publishing).
- Unknowns: how central preservation is; whether submission workflows are definitional; whether IIIF/OAI-PMH are definitional; whether "platform" implies hosted SaaS.

## Research Questions

1. What is the core object ("item") and its internal structure (metadata, files, media)?
2. How are items grouped (collections/communities/sets/sites)? Single vs multiple membership?
3. How does content enter (manual add, batch import, submission workflow, harvest, deposit)?
4. How do end users discover (search, browse, facets, full text) and access (viewers, downloads, transcripts)?
5. What access control exists (public/restricted, IP, authentication, embargoes, rights statements)?
6. Is digital preservation core or optional?
7. Which standards are load-bearing (Dublin Core, OAI-PMH, IIIF, METS/PREMIS, Handle)?
8. What interfaces exist (staff admin, public portal, item page, APIs)?
9. Relationship to ILS/discovery/IR/archives systems?

## Representative Products

Selected for market representation, documentation quality, and spread across product philosophies and customer tiers:

| Product | Vendor / Origin | Pole | Evidence tier reached |
|---|---|---|---|
| DSpace | DSpace/LYRASIS open-source community | open-source, self-hosted; institutional repository + digital collections hybrid | Tier 1 (official docs wiki) |
| CONTENTdm | OCLC | commercial hosted SaaS; library/cultural-heritage digital collections | Tier 1 (official help center) |
| Omeka S | Omeka / Digital Scholar (RRCHNM heritage) | open-source GLAM web-publication system; exhibit-oriented | Tier 1 (official user manual) |
| AM Quartex | Adam Matthew Digital (Sage) | commercial fully-hosted digital collections platform (DAM + website) | Tier 2 (official product pages; help center not reachable) |
| Rosetta | Ex Libris | enterprise preservation-and-delivery system for digital heritage | Tier 1 (official knowledge center; partial depth) |
| Greenstone | Univ. of Waikato / UNESCO / Human Info NGO | historical/regional check: open-source digital library suite, offline-media distribution | Tier 1 (official site) |

## Sources

- DSpace 7.x Documentation (LYRASIS wiki): https://wiki.lyrasis.org/display/DSDOC7x/DSpace+7.x+Documentation ; Functional Overview: https://wiki.lyrasis.org/display/DSDOC7x/Functional+Overview (fetched 2026-09-07)
- CONTENTdm Help Center (OCLC): https://help.oclc.org/Metadata_Services/CONTENTdm ; CONTENTdm Overview: https://help.oclc.org/Metadata_Services/CONTENTdm/Get_started/010CONTENTdm_Overview ; Collection building overview: https://help.oclc.org/Metadata_Services/CONTENTdm/Get_started/Collection_building_overview (fetched 2026-09-07)
- Omeka S User Manual: https://omeka.org/s/docs/user-manual/ ; Items: https://omeka.org/s/docs/user-manual/content/items/ ; Item Sets: https://omeka.org/s/docs/user-manual/content/item-sets/ (fetched 2026-09-07)
- AM Quartex product pages: https://www.amdigital.co.uk/products/quartex (fetched 2026-09-07); https://www.quartexsite.com/ (transport error — abandoned after 1 failure)
- Rosetta Knowledge Center: https://knowledge.exlibrisgroup.com/Rosetta ; Introducing the Rosetta System: https://knowledge.exlibrisgroup.com/Rosetta/Product_Documentation/Rosetta_Overview_Guide/001_Introducing_the_Rosetta_System (fetched 2026-09-07)
- Greenstone: https://www.greenstone.org/ (fetched 2026-09-07)

Source-access limitations:
- Quartex: no operational help documentation reachable; only official product/marketing pages. All Quartex-specific claims kept at positioning level; no workflow detail asserted.
- Rosetta: knowledge center reachable but deep guides (Staff Users, Preservation, Producer's) not individually fetched; model reconstructed from the intro page plus the documented guide/article structure. Claims about Rosetta internals kept coarse.
- No numeric limits, default values, or time windows from any product were promoted to the final document.

---

## Product Observations

### DSpace (Layer A — direct, official docs)

Positioning: open-source repository/digital-library platform; "online access to your digital assets" in "an organized tree of Communities and Collections".

Key observations:

- **Data model**: site → Communities (can nest as sub-communities) → Collections → Items → Bundles → Bitstreams. "Each item is owned by one collection"; an item may appear in additional collections but has exactly one owning collection. Bitstreams = uploaded files; bundles are named groupings (ORIGINAL, THUMBNAILS, TEXT, LICENSE, CC_LICENSE).
- **Item** = "metadata descriptions together with files available for download".
- **Metadata**: three sorts — descriptive (multiple flat schemas; qualified Dublin Core default), administrative (preservation, provenance, authorization policy), structural (how bitstreams present/order within an item; basic).
- **Bitstream Format Registry**: each bitstream has a format with a support level (Supported / Known / Unsupported) set by the hosting institution — a preservation-posture concept.
- **Discovery**: full-text search over extracted content plus metadata; faceted browsing; browse indexes (title, issue date, author, subject), scopeable to a collection/community; external reference via Handle.
- **Persistent identifiers**: CNRI Handle assigned to every community, collection, and item; bitstreams get weaker "persistent" sequence IDs. Rationale: preserve the item, not the bit encoding.
- **Ingest**: (a) manual web submission UI producing an "in-progress submission"; (b) configurable workflow with review steps (default up to three steps — review / edit / final edit — each optionally bound to an e-person group; task-pool semantics; reject returns to submitter); (c) batch import (directory + XML metadata; METS packages); (d) registration of externally hosted files; (e) SWORD / SWORDv2 remote deposit. On install: accession date, date.available, provenance message with checksums, Handle assignment, authorization policies, search/browse indexing.
- **Access control**: Resource Policies binding actions (READ/WRITE/ADD/REMOVE, collection DEFAULT_ITEM_READ / DEFAULT_BITSTREAM_READ) to objects for E-People/Groups; default deny; permissions do not commute; Anonymous group; IP/network-based group membership possible ("LocalUsers" pattern). Items/collections remain discoverable regardless of READ policy.
- **Licensing**: per-collection licenses; submitter distribution license at submission; Creative Commons support stored as metadata + RDF.
- **Item lifecycle**: withdrawn (hidden, tombstone shown) vs expunged (all traces removed).
- **Preservation**: Checksum Checker (verify content not corrupted/tampered; scheduled or ad hoc); AIP backup/restore (METS-based Archival Information Packages).
- **Delivery**: item pages, bitstream download URLs, thumbnails; Request-a-copy feature; Google/Google Scholar optimization; OpenURL support; OAI-PMH exposure of Dublin Core (public items; collection structure as OAI sets); Signposting (FAIR).
- **Users**: E-People and Groups; self-registration possible; LDAP/X509 authentication stacks; subscriptions to collections (not implemented in 7.x — documented as pending); usage statistics (page views, file downloads, countries).
- **Extras**: Researcher Profiles, Configurable Entities (persons/orgs as first-class objects), ORCID integration, curation tasks, supervision orders for theses.

### CONTENTdm (Layer A — direct, official help center)

Positioning: "Build, preserve, and showcase your unique digital collections"; OCLC's hosted digital collection management system; vendor implementation guide titled "Implementing your Digital Library with CONTENTdm".

Key observations:

- **Two-surface architecture**: Server URL (CONTENTdm Administration — staff) and Website URL (public front-end).
- **Project Client**: Windows desktop application for batch preparation — projects (each linked to a single server collection), add items (single file, folder-full import, PDFs, EAD finding aids, URLs for streaming media, metadata-only records, compound objects), enter metadata (item editing tab, metadata templates, tab-delimited text files), manage archival files and high-resolution images, generate display images, image rights (banding/branding/watermarking), then "Upload for Approval".
- **Approval queue**: uploaded items sit in a pending queue until reviewed/approved by an administrator; "Approve & Index" makes them public. Items tracked with uploading user.
- **Compound objects**: "two or more files bound together with an XML structure" — multi-page/multi-part items with node structure.
- **Administration**: server admin (create/delete collections, harvesting settings, stop list, user rights, reports), collection admin (field properties incl. full-text search flags, controlled vocabularies, display image settings, archival file management, image rights, PDF conversion, export), item admin (approve, build text index, edit, unlock; web editor for one-at-a-time items).
- **Website Configuration Tool**: branding/appearance, search & browse configuration, navigation, page types, localization, analytics/SEO; advanced customization via uploaded HTML/CSS/JS; API reference.
- **Metadata**: field-level configuration per collection; controlled vocabularies (shareable across fields/collections); full-text search fields; OCR (ABBYY engine, licensed add-on; CJK notes); transcripts; faceted search; custom queries (CQR).
- **Standards/integration**: OAI-PMH harvesting (deleted items appear in harvest; items can be restricted from harvest); WorldCat sync / Digital Collection Gateway; IIIF (manifests; troubleshooting articles); COUNTER usage question; EAD3 support question.
- **Access control**: item-level IP permission restrictions; restricted PDF downloads; user rights by job responsibility; embargo/timer FAQ exists (feature presence not confirmed in fetched pages).
- **Preservation archive**: separate module (activation required; ingest/reports/dissemination; volumes accessioned) — optional, not part of base flow.
- **Site management**: custom domains, SSL, collection aliases, Flex Loader, storage reports.
- **Limits observed in troubleshooting titles** (kept out of final doc): browse display cap (~10k items), facet term cap (100).

### Omeka S (Layer A — direct, official user manual)

Positioning: "a web publication system for universities, galleries, libraries, archives, and museums. It creates a local network of independently curated exhibits sharing a collaboratively built pool of items and their metadata."

Key observations:

- **Resources**: Items, Media, Item Sets, Vocabularies, Resource Templates.
- **Item** = "the building blocks"; need not represent physical objects nor have media — can be a node (person, place, thing); items link to items via properties (linked-data style); value annotations (reification) allow statements about statements (provenance, time, certainty).
- **Metadata**: RDF vocabulary-driven (Dublin Core, Bibliographic Ontology, etc.); properties added per item from any installed vocabulary; resource templates pre-load field sets per item type; classes from vocabularies; per-value public/private visibility; language tags per value.
- **Media**: attached to items; types include Upload, URL, HTML, oEmbed, IIIF image, IIIF presentation, YouTube; primary media drives thumbnails; media can be public/private independently of the item.
- **Item Sets**: aggregations of items ("similar to collections in Omeka Classic"); items may belong to any number of sets; sets have their own metadata; open/closed (who may add) independent of public/private (who may see); deleting a set does not delete items.
- **Sites**: public-facing exhibitions; independently curated; items must be added to a site (manually, by user default, or auto-assign); site pages built from blocks; themes; site-level user roles (Manager/Creator/Viewer); site setting to exclude resources not in the site.
- **Roles**: Global Admin, Supervisor, Editor, Reviewer, Author, Researcher — permission matrix over add/edit/delete, private-object visibility, batch actions; ownership model (creator owns; orphaning on user deletion).
- **Ingest**: manual add; CSV Import; connectors (Zotero Import, ArchivesSpace Connector, DSpace Connector, Fedora Connector, Omeka Classic Importer); File Sideload; Extract Metadata / Extract Text; Collecting module (public contribution); Web Archive module.
- **Discovery**: admin advanced search; public search; Faceted Browse module; Metadata Browse module; Hierarchy module (nested item sets).
- **Delivery**: public item pages (configurable layout), media rendering, IIIF Presentation module, Output Formats module, Static Site Export module.
- **Other modules**: Scripto + DataScribe (crowdsourced transcription), Persistent Identifiers, Value Suggest (authority vocabularies), Local Contexts (Indigenous data), Redact Values, Data Visualization, Mapping, Zotero Citations.

### AM Quartex (Layer A-lite — official product pages only; positioning-level)

Positioning: "digital collections platform for libraries and archives"; "a secure, accessible and feature-rich digital asset management (DAM) and website creation system in one"; "cloud-based and fully hosted"; "no specialist IT knowledge is required".

Key observations (positioning-level only):

- Capability pillars named on product pages: Access and discovery (OCR, HTR, audio transcription, full-site search, digital exhibits, interactive timelines); Digital asset management (customisable settings and workflows for metadata, controlled vocabularies, access controls); Build and migration (site creation, migration services from AM's teams).
- Audiences: academic libraries; galleries, museums, archives ("cultural heritage").
- Emphasis on accessibility (dedicated platform-accessibility page) and long-term stewardship.
- No operational help documentation reachable; no workflow detail asserted from this product.

### Rosetta (Layer A — official knowledge center, coarse depth)

Positioning: "designed to enable effective preservation of, and access to, digital heritage collections"; "large amounts of digital data, including audio, video, and text content, can be stored and managed"; content providers deposit content "and make it available to library staff, the public, or to specific content consumers"; retention: "storing material indefinitely or for a specified amount of time and then deleting it (tentatively or permanently)".

Key observations (from intro + documented guide/article structure):

- **OAIS-shaped pipeline**: Producers deposit SIPs (Submission Information Packages) → deposit area → validation/assessment → Permanent repository; IEs (Intellectual Entities) with Representations (including Derivative Copies); METS-based; DNX (preservation/technical metadata); fixity checks; Format Library / Format Registry (PUID); preservation reports (Formats Breakdown vs Formats at Risk); retention policies; rollback of IEs.
- **Collections**: Collections Management (tree); ingest enrichment assigns collections automatically (by DC value / by name).
- **Delivery**: viewers (IIIF Universal Viewer, METS/General IE Viewer, FlexPaper for PDF); delivery rules per institution/user group; access rights (IP ranges, SAML authentication profiles); OAI publishing (DC output customization); Handle publishing; integration with OPAC/Primo/Voyager/Alma for end-user access.
- **Staff machinery**: Staff Users Guide, Roles and Privileges, scheduled jobs/processes, work queues (deposit errors, TA validation), reports (BIRT/Metabase).
- **Producers**: Producer's Guide — external content-provider accounts, material flows, copyright boilerplate for deposit.

### Greenstone (Layer A — official site; historical/regional check)

Positioning: "a suite of software for building and distributing digital library collections"; "organizing information and publishing it on the web or on removable media such as DVD and USB flash drives"; open-source, multilingual, GNU GPL; produced by the New Zealand Digital Library Project with UNESCO and Human Info NGO; aim: "empower users, particularly in universities, libraries, and other public service institutions, to build their own digital libraries", with explicit developing-country focus.

Key observations:

- Confirms the Type's older/regional form: collection building + organization + distribution, with delivery not limited to the web (removable media).
- Confirms institutional (public-service) orientation of the Type.
- No cloud, no IIIF, no preservation certification — yet still recognizably a digital library platform.

---

## Cross-product Comparison

| Aspect | DSpace | CONTENTdm | Omeka S | Quartex | Rosetta | Greenstone |
|---|---|---|---|---|---|---|
| Self-positioning | repository / digital assets online | digital collection management ("implementing your digital library") | web publication system for GLAM | digital collections platform (DAM + website) | preservation of, and access to, digital heritage | building & distributing digital library collections |
| Core object | Item (metadata + bundles of bitstreams) | Item / compound object (files bound by XML) | Item (vocabulary values + media) | digital asset (positioning-level) | Intellectual Entity (IE) with representations | document in a collection |
| Collection container | Community → Collection tree (item: one owning collection + mapped extras) | Collection (flat; aliases) | Item Set (many-to-many) + Sites (publication layer) | collections (positioning-level) | Collections (managed tree; auto-assignment) | Collections |
| Ingest paths | submission UI + configurable workflow; batch import (XML/METS); registration of external files; SWORD | Project Client batch; web editor; Catcher (OAI-based batch edits); approval queue | manual add; CSV import; connectors (Zotero/ArchivesSpace/DSpace/Fedora); sideload; collecting | migration/build services (positioning-level) | producer SIP deposit; material flows; validation | collection build process |
| Review/approval | configurable workflow steps with task pools; reject returns to submitter | approval queue → approve & index | role-based (Reviewers); no mandatory gate | n/a (not verified) | validation/assessment stages | n/a |
| Discovery | metadata + full-text search; facets; browse indexes | search; browse; facets; custom queries | search; advanced search; faceted browse module | full-site search; OCR/HTR search | search (Solr); OPAC/Primo integration | search over collections |
| Delivery | item page; bitstream download; request-a-copy; Google Scholar optimization | public website; image viewer; PDF; video; transcripts | site pages; item pages; media render; IIIF module | collection sites; exhibits; timelines | IIIF Universal Viewer; METS viewer; OPAC integration | web or DVD/USB |
| Access control | resource policies; anonymous; groups; IP-based groups; licenses | item-level IP restrictions; restricted downloads; user rights | public/private per item/property/media; roles | access controls (positioning-level) | access rights (IP ranges, SAML); delivery rules | limited |
| Preservation | checksum checker; format support levels; AIP backup/restore | optional preservation archive module | not built-in (exports) | "long-term stewardship" (positioning) | core discipline (fixity, format library, retention, reports) | minimal |
| Standards | Dublin Core; OAI-PMH; SWORD; Handle; METS/AIP; Signposting | OAI-PMH; IIIF; EAD (finding aids); COUNTER (question) | RDF vocabularies; Dublin Core; IIIF; OAI (module) | IIIF-era features (positioning) | METS; DNX; OAI; IIIF; Handle; PUID | Dublin Core; OAI |
| Deployment | self-hosted open source | hosted SaaS | self-hosted open source | fully hosted SaaS | hosted/on-prem enterprise | self-hosted open source; offline media |
| Primary staff users | repository managers, librarians | collection staff, administrators | curators, editors, authors | archivists/librarians (services-assisted) | preservation/digital-collection staff, producers | library staff, NGOs |

## Canonical Model (four-level abstraction)

### L0 — Defining Invariant

An institution-operated platform that maintains a curated collection of digital items and makes them discoverable and accessible to an audience. Four properties; remove any one and the product stops being a digital library platform:

1. **Digital item as the unit of record** — an identified item binding descriptive metadata to one or more content files (or media references). Without metadata-bound items it is a file share / web CMS; without content it is a catalog.
2. **Collection-level organization** — items are grouped into named, curated collections (tree, flat, or many-to-many membership all qualify). Without organization it is an unstructured asset dump.
3. **Institutional curation machinery** — staff-side capability to add, describe, edit, approve, and maintain items over time. Without it, it is a personal library or a static publication.
4. **Discovery + delivery to an audience** — search and/or browse across the collection, and an access surface through which end users can view or obtain the content. Without discovery it is storage; without delivery it is a back-office asset store.

Historical check (§24): Greenstone (older, regional, UNESCO/developing-world deployments, offline DVD/USB distribution) satisfies all four properties without cloud, IIIF, OAI, or any preservation program. Pre-web CD-ROM digital collections and early thesis repositories satisfy it as well. The definition therefore does not depend on web delivery, hosted SaaS, any metadata standard, or any preservation discipline.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B), but not definitional:

- Staff metadata workbenches: templates/profiles per item type, controlled vocabularies, batch editing, per-field configuration
- Ingest machinery beyond manual add: batch import (CSV/tab-delimited/XML), media derivative generation (thumbnails, display images), OCR / full-text extraction
- Configurable review/approval of new items before publication
- Faceted search and browse indexes; full-text search over extracted content
- Public item page: metadata display + content viewer + download
- Access restriction: public vs restricted items; IP-range or authenticated access; item-level rights/licenses statements
- Persistent identifiers for items (Handle-class)
- Usage statistics (views, downloads)
- Metadata exposure/harvesting (OAI-PMH) and rich-media delivery (IIIF)
- Compound/multi-file items with internal ordering (structural metadata)
- Integration seams to the library ecosystem (ILS/discovery/catalog sync)

### L2 — Variant / Optional Structure

- **Preservation program depth**: from none (Omeka S base) through optional module (CONTENTdm preservation archive) to core discipline (Rosetta: fixity, format registries, retention, preservation reporting)
- **Publication/exhibit layer**: independently curated sites/exhibits/timelines over the item pool (Omeka S sites; Quartex exhibits; CONTENTdm website configuration)
- **Scholarly/IR flavor**: submission workflows, embargoes, request-a-copy, researcher profiles, ORCID (DSpace pole)
- **Crowdsourcing/transcription**: Scripto/DataScribe (Omeka), HTR/audio transcription (Quartex positioning)
- **Deployment posture**: self-hosted open source vs hosted SaaS vs enterprise hosted/on-prem
- **Audience flavor**: academic library vs cultural heritage (museum/archive) vs national-library scale
- **Delivery medium**: web portal (dominant) vs offline media (Greenstone)
- **Linked-data posture**: items as nodes with property links and value annotations (Omeka S)

### L3 — Vendor-specific (research notes only)

- DSpace: bundles (ORIGINAL/THUMBNAILS/TEXT/LICENSE/CC_LICENSE), Bitstream Format Registry support levels, Handle server, supervision orders, configurable entities, AIP tooling
- CONTENTdm: Windows Project Client, Catcher (OAI-based batch web service), Flex Loader, CQR, Website Configuration Tool, image rights (banding/branding/watermarking), WorldCat sync, ~10k browse display cap and 100-term facet cap (troubleshooting-documented; not promoted)
- Omeka S: module ecosystem (named above), role matrix labels, open/closed item sets, value annotations
- Rosetta: IE/Representation/DNX model, Material Flows, Producer accounts, Format Library (global/local, PUID), TA work queues, BIRT/Metabase reporting, Alma/Primo/Voyager integration
- Quartex: HTR/audio-transcription packaging, AM build/migration services

## Vendor-specific Findings

See L3. None of these were promoted to the canonical model. The closest call was DSpace's Community→Collection single-ownership tree: it is a strong implementation pattern but contradicted by Omeka S many-to-many item sets and CONTENTdm flat collections, so the canonical concept is "collection-level organization" with membership topology as a variant.

## Rejected Findings (considered, not canonical)

- "Preservation is definitional" — rejected: Omeka S ships none; CONTENTdm's is an activated add-on; Greenstone minimal. Preservation depth is a variant pole (Rosetta).
- "Submission workflow with approval is definitional" — rejected: DSpace collections can skip workflow entirely; Omeka/CONTENTdm allow direct adds; batch imports bypass UI submission. Common, not defining.
- "OAI-PMH / IIIF / Handle are definitional" — rejected: standards integrations common in the sector but absent in Greenstone-era and optional elsewhere.
- "Hosted SaaS is definitional" — rejected: DSpace/Omeka/Greenstone are self-hosted open source; Greenstone even distributes offline.
- "Full-text/OCR search is definitional" — rejected: metadata-only search satisfies discovery; OCR is licensed add-on in CONTENTdm.
- "Public web portal is definitional" — rejected: Greenstone distributes on removable media; delivery surface is a variant, the delivery function is not.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (and "remove what to become the other") |
|---|---|---|
| Integrated Library System / ILS | adjacent, ecosystem partner | ILS manages the physical collection's operations (cataloging, circulation, acquisitions, patrons). Remove digital-item delivery and add circulation/acquisitions → ILS. Rosetta integrates with Alma/Primo/Voyager; CONTENTdm syncs to WorldCat — integration seam, not same Type. |
| Library Discovery Platform | adjacent, complementary | Discovery layer searches across many external sources (catalog, subscriptions, digital collections); the digital library platform is the host of one institution's collection being discovered. Remove the hosted item store and search external indexes instead → discovery platform. |
| Institutional Repository | subtype/variant — flagged | IR is this Type deployed for institutional scholarly output (papers, theses, datasets) with submission workflows and open-access policy machinery. DSpace is the canonical product of both labels; the market does not cleanly separate them. Joint review recommended; possible variant/alias relationship rather than fully independent Type. |
| Archives Management System | adjacent | AMS manages archival description and finding aids (often back-office, EAD-centered) for physical+digital archives; the digital library platform publishes digital content to audiences. Remove public delivery and center finding-aid description → AMS. Overlap exists (CONTENTdm accepts EAD; Omeka has ArchivesSpace connector). |
| E-book Library Application (§02.09) | different actor | Consumer-side personal reading library (user's own books, reading experience first). Remove institutional curation and multi-user collection management → personal e-book library. |
| Digital Asset Management (enterprise DAM) | adjacent | DAM centers on brand/marketing asset lifecycles and rights for organizations; Quartex self-describes as "DAM and website creation system in one" for collections. DAM lacks the library collection/publication semantics (metadata schemas, harvesting, public scholarly delivery). |
| Content Management System / CMS | adjacent | Generic CMS publishes web pages; it lacks item-level collection semantics (descriptive metadata models, controlled vocabularies, content viewers, OAI/IIIF). Omeka S calls itself a "web publication system" but its core objects are collection resources. |
| Web Archive Viewer / preservation systems | adjacent | Capturing/replaying archived websites or pure preservation repositories lack the curated-collection + discovery + delivery loop as the primary job. |

## Uncertainties

- Quartex operational behavior (ingest steps, access-control granularity, standards support) unverified — product-page evidence only; final doc makes no Quartex-specific workflow claims.
- Rosetta deep workflows (validation stages, delivery rule configuration) reconstructed from intro + documented guide structure; kept coarse.
- Whether the market treats "Digital Library Platform" and "Institutional Repository" as one Type or two — evidence suggests heavy overlap (DSpace spans both); recorded as a boundary issue for joint review, not silently resolved.
- CONTENTdm embargo/timer feature: FAQ title exists but content not fetched; presence not asserted.
- No numeric limits from any product were promoted to the final document.

## Final Synthesis

A Digital Library Platform is institution-operated software for building and operating a curated digital collection: identified digital items (descriptive metadata bound to content files), organized into named collections, managed by staff through ingest/description/approval/maintenance machinery, and made discoverable (search/browse) and accessible (viewers/downloads) to an audience. Around this defining core, mature products add staff metadata workbenches, batch ingest with derivatives and OCR, review workflows, faceted discovery, access restriction, persistent identifiers, statistics, and standards-based exposure (OAI-PMH, IIIF). Product families differ mainly in where they put their center of gravity: repository/submission (DSpace), hosted collection management (CONTENTdm), publication/exhibition (Omeka S), hosted turnkey sites (Quartex), preservation discipline (Rosetta), and simple distribution incl. offline media (Greenstone). Preservation depth, submission workflows, exhibit layers, and standards integrations are variant structure, not definition.
