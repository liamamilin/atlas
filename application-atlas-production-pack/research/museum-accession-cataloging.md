# Research Notes — Museum Accession / Cataloging

Research date: 2026-09-08
Leaf: Museum Accession / Cataloging (§27 Media, Entertainment, Creator & Culture — museum/cultural-heritage cluster)
Slug: museum-accession-cataloging

## Research Goal

Understand what "Museum Accession / Cataloging" actually is in the real market: what the accessioning and cataloguing workflow consists of, what objects and records it creates and maintains, who performs it, how it is realized in software, and how it relates to the surrounding §27 museum-cluster leaves (Museum Collections Management, Archaeological Collection Management, Digital Collection Portal, Provenance Research Platform, object movement / loan / conservation / condition siblings) — including resolving (or refining) the pre-hung sibling flag that this leaf is "probable Capability" of a collections-management system.

## Initial Boundary

Hypothesis before research: accessioning = the formal, numbered intake of objects into a museum's permanent collection (source, method, title evidence); cataloguing = creating and continually enriching the descriptive record per object. Both are the **record-creating** layer of museum practice, realized as the core of collections-management systems rather than as standalone products. Nearest confusions:

- Museum Collections Management (the containing system; sibling flag anticipated a Capability relationship)
- Archaeological Collection Management (its L0 already contains an accession→cataloging lifecycle leg)
- Digital Collection Portal (publication of records vs creation of records)
- Integrated Library System (bibliographic cataloging — different object world)
- Auction Management System (its "cataloging" leg is units-of-sale, not permanent custody)

## Research Questions

1. What exactly does "accessioning" mean as a defined museum procedure? What does it require (records, numbers, legal evidence)?
2. What does "cataloguing" mean as a procedure, and how does it relate to inventory?
3. What is the object record — its identity, its required and optional content, its lifetime?
4. What is the accession lot / accession number, and how do object numbers relate to it?
5. Who performs this work (roles), and on which surfaces?
6. What rules govern the record (uniqueness, immutability, audit, backup, credit line, not-everything-accessioned)?
7. How do the sampled products realize the workflow, and where do they differ (segment, deployment, standards)?
8. Is there any standalone accession/cataloging product, or is the workflow always inside a CMS?
9. Does the paper-era form of this practice satisfy the definition (historical check)?

## Representative Products

Selected for market representation, documentation reachability, different product philosophy, and different customer tier:

| Product | Vendor | Pole | Evidence level reached |
|---|---|---|---|
| TMS Collections | Gallery Systems | enterprise museum incumbent (800+ clients, 23 countries) | product pages + Collections Trust software-directory entry (operational detail) |
| MuseumPlus | Zetcom | European museum incumbent (900+ museums) | product page (module/function level) |
| CatalogIt | It Unlimited, Inc. | SMB / cloud-native museum + private collectors | Tier-1 help center + vendor-authored educational article |
| CollectiveAccess (Providence) | Whirl-i-Gig | open-source, self-hosted | official documentation landing (positioning level) |

Also consulted: **Spectrum 5.1** (Collections Trust) — the UK museum collections-management standard, used internationally; defines "Acquisition and accessioning" and "Cataloguing" as primary procedures. Not a product, but the domain-standard backbone that products advertise compliance with (TMS is "Spectrum 5 compliant"; Gallery Systems a Spectrum Partner).

Not usable: PastPerfect (403, consistent with the archaeological-collection-management pass), Lucidea Argus (403 this pass), Vernon Systems (unreachable in sibling passes), Axiell (unreachable in sibling passes), Gallery Systems / Zetcom detailed help centers (login-gated).

## Sources

- Collections Trust — Spectrum: Acquisition and accessioning (primary procedure overview, scope, standard): https://collectionstrust.org.uk/spectrum/primary-procedures/acquisition-and-accessioning/ ; https://collectionstrust.org.uk/resource/acquisition-and-accessioning-scope/ ; https://collectionstrust.org.uk/resource/acquisition-and-accessioning-the-spectrum-standard/
- Collections Trust — Spectrum: Cataloguing (primary procedure overview, scope): https://collectionstrust.org.uk/spectrum/primary-procedures/cataloguing-spectrum-5-0-primary-procedures/ ; https://collectionstrust.org.uk/resource/cataloguing-scope/
- Collections Trust — Spectrum appendix: Object information groups: https://collectionstrust.org.uk/spectrum/information-requirements/object-information-groups/
- Collections Trust — software directory entry "TMS Collections and eMuseum": https://collectionstrust.org.uk/software/tms/
- Gallery Systems — Collections Management with TMS Collections: https://www.gallerysystems.com/solutions/collections-management/ ; Software for Registrars: https://www.gallerysystems.com/roles/software-for-registrars/
- Zetcom — MuseumPlus: https://www.zetcom.com/en/museumplus-en/
- CatalogIt — product page: https://www.catalogit.app/ ; help center: What is an Entry? https://support.catalogit.app/en_US/entries/what-is-an-entry ; Using the Museum Accession Profile https://support.catalogit.app/en_US/profiles/using-the-museum-accession-profile ; Creating The First Entry in Your Museum Account https://support.catalogit.app/en_US/museum-features/creating-the-first-entry-in-your-museum-account ; Museum Features category https://support.catalogit.app/en_US/museum-features ; blog "Acquisition v. Accession" https://www.catalogit.app/post/acquisition-v-accession
- CollectiveAccess — official documentation: https://manual.collectiveaccess.org/

Source-access limitations: doc.collectiveaccess.org/wiki and wiki.collectiveaccess.org (transport errors ×3 total) unreachable — CollectiveAccess evidence stays at its official manual landing page (positioning/standards claims), no operational workflow claims asserted for it. lucidea.com/argus 403. PastPerfect skipped after sibling 403s. Gallery Systems client community and Zetcom help center are login-gated (confirmed this pass via the community login link). Consequently: TMS/MuseumPlus observations are product-page and directory-entry level; CatalogIt provides the screen-level operational depth; Spectrum provides the procedure-level definitional backbone.

## Product / Standard Observations

### Spectrum 5.1 (Collections Trust) — domain standard [Evidence A for the standard's own content]

- Cataloguing primary procedure definition: "The ongoing process of recording and managing information about collections, often from multiple perspectives, to meet the needs of a range of users."
- Acquisition and accessioning primary procedure definition: "Taking legal ownership of objects… through the process of accessioning: the formal commitment by your governing body to care for objects over the long term."
- Acquisition scope: "In legal terms, acquisition involves a 'transfer of title' from the previous owner to you. The procedure gives you proof of ownership, and it assigns a unique number that will link each object to the information you hold about it."
- Not everything acquired is accessioned: objects acquired for handling/display-prop use follow part of the procedure but "do not formally accession the items"; accessioning "brings with [it] ethical responsibilities to preserve objects over the long term."
- Cataloguing scope: "Museums create a catalogue record for each object, or group of objects, either in a computerised system (eg using collections management software) or paper-based system (eg on cards)… They should be searchable…"
- Cataloguing builds on inventory minimum: "Catalogue records usually build on this bare minimum with more context and significance, eg which pots are Roman…"
- No fixed record depth: "Spectrum does not specify any level of information required beyond the minimum needed to meet the Inventory standard… there is no 'ideal' catalogue record."
- Never complete: "The aim of cataloguing is not to produce a definitive end product that cannot be shared until it is 'complete'. No museum has finished cataloguing because there is always more to learn."
- Acquisition/accessioning standard — minimum requirements include: acquire only per agreed policy and law; "written evidence that the undisputed owners… have transferred title"; donors aware of terms; "a unique number to each accessioned object and securely label or mark it with this number" ("You can link each physical object with the information you have about it"); keep all acquisition information accessible via the unique numbers; provenance documentation; "a tamperproof record of all accessioned objects, using their unique numbers"; "an up-to-date security copy of all accession records."
- Object information groups appendix: all object information "is linked to an object via the *Object number*"; groups include identification, description, production, history and association, collection, rights, condition, valuation, owner's contribution, user's contribution, etc.
- Numbering policy is an explicit policy question: "What is your format for numbering new accessions and the preferred labelling and marking methods…?"

### TMS Collections (Gallery Systems) — enterprise museum incumbent [Evidence A for its pages/directory entry]

- Positioning: "the world's leading collections management system for museums and institutions… handles every facet of your workflow."
- Collections Trust directory entry: "TMS Collections is comprised of 11 interrelated modules, with supporting functionality for entering and tracking all collections data and management activities."
- Spectrum procedures supported (directory entry, listed verbatim): Object Entry (primary), **Acquisition and accessioning (primary)**, Location and movement control (primary), Inventory (primary), **Cataloguing (primary)**, Object Exit (primary), Loans In, Loans Out, Condition checking, Collections care and conservation, Valuation, Insurance and indemnity, Damage and loss, Deaccessioning and disposal, Rights management, Use of collections, Audit. "Spectrum 5 compliant."
- Cataloguing machinery (directory entry): "Catalogue and cross-reference everything, from object data to constituents"; thesaurus for data entry and retrieval "as standard" (supplied with Getty AAT and TGN); "Create user-defined object data entry forms"; "Create object records via integrated Object Importer"; "Multilingual cataloguing"; data-cleaning tools including batch updates via authority control; alerts "triggered by user-defined events, e.g. the creation of an object record without a title being recorded."
- Audit trail (directory entry): built-in audit trail capturing date, login ID, table, column, old value, new value, with user-entered explanations/approvals; complete location-history audit trail per object; separate Audit Manager product for configurable field-level auditing.
- Rights and credit: Registration menu includes a Rights and Reproduction screen recording agreement send/receive/sign dates, rights granted, restrictions, "credit line for reproduction."
- Segments: 11 collecting-discipline pages (fine art, history, natural history, archives, corporate art, university museums…); localization into 24 languages; over 800 clients in 23 countries.

### MuseumPlus (Zetcom) — European museum incumbent [Evidence A for its product page]

- "Comprehensive cataloging, registration and management of all objects in your collection." (Core Functions)
- "Central register for internal and external contacts" (person/organization authority records beside objects).
- "Digital Assets — Images and other digital media can be linked to objects, artists, addresses and other entries."
- Modules beside cataloging: Contracts (exhibition/loan/object agreements), Exhibition Management, plus "additional modules such as event management, archiving."
- "High degree of flexibility in the definition of data fields, modules, forms and reporting" — configurable record structure.
- Deployment: in-house or SaaS. Clients: 900+ museums (Louvre, etc.).
- The word "registration" is used alongside cataloging — the registrar workflow is first-class in the incumbent segment.

### CatalogIt — SMB / cloud-native pole [Evidence A, Tier-1 help center + authored article]

- Entry definition: "An **Entry** in CatalogIt represents one individual item (or object record) in your collection. Each Entry counts as a single cataloged object, regardless of how many images, files, or related records (such as people, places, accessions, exhibitions, or documents) are attached to it. Your Entry is the central, living record of that item — capturing what it is, where it came from, why it matters, and how it's managed."
- Accession definition: "Accessions are an object or group of objects (lot) acquired at the same time by the same source that is added to a museum's permanent collection. This object or lot is assigned a unique number called an Accession Number."
- Numbering: "Most museums in the US follow a three-part numbering system with the first two parts referring to the Accession Number following a year and batch numbering pattern… The third-part… are sequential numbers assigned to each object from the lot. For example, the first object from the first accession of the year 2025 would be 2025.1.1."
- Numbering enforcement: "Strict Accessioning: This is a default setting in CatalogIt where Object / Entry IDs are automatically assigned to the next available number. If you are trying to use a numbering pattern aside from the default… you will encounter an error." Custom regular patterns supported via tokens (Y/M/D/N/a/A, prefix letters "L" loans, "Q" acquisitions, "FIC" found in collection, "D" deaccessioned); pattern enforcement per numbering system; can be turned off by support request.
- Acquisition vs accession (authored article by a museum-registration consultant): "An acquisition refers to items obtained by the museum. An accession is an acquisition that the museum formally adds to its collection to be held in public trust and administered through the collections management policy." Methods listed: "purchase, gift, bequest, or transfer." Non-accessioned property (education collection, props, sellable gifts) tracked in a separate Acquisition profile with its own numbering ("Q" prefix); if later accessioned, "you can create an 'Accession' profile… and then associate the related accession number to the Acquisition."
- Deaccession profile exists as the counterpart ("Learn how to deaccession an item from your collection").
- Museum plan: "Authoritative data fields", "Accession, exhibition, loan, and location documentation", "Workflow and multi-user capabilities"; personal collector plan tracks "acquisition, value, insurance, provenance."
- Forms: "Generate standardized forms directly from your CatalogIt records" (.docx template authoring); blog: "Creating Deed of Gift Agreements with CatalogIt."
- Authorities: "Adding Getty AAT Terms to Entries"; "CatalogIt works with museum professionals… to research classifications, making them relevant and easy to use."
- Capture and enrichment: photo capture "at a historic site, in a basement storage room, at an auction"; entries track "value, location, and condition… adding to their stories in real time"; AI "Describe Image" assistant; bulk editing.
- Permissions: "Users with Owner, Admin, Read/Write, and Editor permissions can create and edit Entries." Multi-user collaboration emphasized (staff + volunteers).
- Roles of users: historical societies, cultural institutions, preservation societies, museums, private collectors, consultants, conservators.

### CollectiveAccess / Providence — open-source pole [Evidence A for its manual landing page; positioning level only]

- "CollectiveAccess is collections management and presentation software… The project began in 2003 as a response to the complete lack of non-commercial, affordable, open-source solutions for digital collections management."
- "Providence is the core cataloguing application of CollectiveAccess where data, media and metadata is input, edited, and managed. Pawtucket is the optional, public web-access tool for digital publication and discovery." (Clean internal split: cataloguing core vs publication surface — matches the cataloging/portal boundary.)
- "Designed to handle large, heterogeneous collections that have complex cataloging requirements."
- Metadata standards: DACS, Dublin Core, VRA Core; authorities/vocabularies: LCSH, Getty AAT; relational links between records.
- Free/open-source (GPLv3), web-based, self-hosted or community-supported.

## Cross-product Comparison

| Dimension | TMS Collections | MuseumPlus | CatalogIt | CollectiveAccess | Spectrum (standard) |
|---|---|---|---|---|---|
| Object record as unit | "catalogue… everything, from object data to constituents"; object records via forms/importer | "cataloging, registration and management of all objects" | Entry = "one individual item (or object record)… central, living record" | "core cataloguing application… data, media and metadata is input, edited, and managed" | "a catalogue record for each object, or group of objects" |
| Accession as recorded event with number | Spectrum procedure "Acquisition and accessioning (primary)" supported | object management within registrar workflow (module level only) | Accession profile: lot acquired "at the same time by the same source", unique Accession Number, lot→object three-part numbers | (not operationally verified — doc hosts unreachable) | unique number per accessioned object; number links object ↔ information; title evidence |
| Acquisition vs accession distinction | Spectrum compliance implies it; not separately observed on reachable pages | not observed at reachable level | explicit: separate Acquisition profile for non-accessioned property | not verified | explicit in scope ("do not formally accession the items") |
| Numbering machinery | not observed at reachable level | not observed at reachable level | strict auto-numbering default, configurable patterns, error on deviation | not verified | numbering format is a required policy decision |
| Descriptive depth | user-defined forms; discipline schemas; multilingual cataloging | "flexibility in the definition of data fields, modules, forms" | "authoritative data fields"; classifications | "complex cataloging requirements"; DACS/DC/VRA Core | no 'ideal' record; builds beyond inventory minimum |
| Authorities/terminology | Getty AAT/TGN thesaurus as standard; batch authority updates | not observed at reachable level | Getty AAT terms; researched classifications | LCSH, Getty AAT | (controlled terminology guidance exists elsewhere in Spectrum resources — not fetched) |
| Person/constituent records | "from object data to constituents" | "central register for internal and external contacts" | Person profiles; people/places attachable to entries | relational links | owner's-contribution and history/association information groups |
| Media on record | link unlimited media; media metadata ingest | digital assets linked to objects | images/files central to Entry; AI describe | media and metadata managed | (media as object-linked documentation) |
| Audit/immutability | built-in audit trail old→new values; Audit Manager product | not observed at reachable level | not directly observed (plan copy implies multi-user tracking) | not verified | "tamperproof record… of all accessioned objects" + backup requirement |
| Acquisition paperwork | Rights & Reproduction screen records agreements/credit lines | Contracts module (exhibition/loan/object agreements) | deed-of-gift form generation from records | not verified | written evidence of title transfer; donors aware of terms |
| Counterpart exit workflow | Deaccession and disposal procedure supported | not observed at reachable level | Deaccession profile | not verified | Object exit / Deaccessioning procedures |
| Deployment | web-based; client-hosted or vendor cloud hosting | in-house or SaaS | cloud subscription only | self-hosted open source | (paper-based systems explicitly allowed) |
| Segment | large institutions, 800+ clients | 900+ museums, Europe-heavy | small museums, historical societies, collectors | resource-constrained institutions; projects on 5 continents | UK-accreditation frame, used internationally |

Reading of the matrix: every product pole realizes accession+cataloging as the **record-creating core of a collections-management system**; no sampled or reachable source offers a standalone accession/cataloging product. Segment determines everything around that core (deployment, standards depth, adjacent modules), not the core itself.

## Abstraction Hierarchy

### L0 — Defining Invariant (deliberately small)

The accession/cataloging workflow, as realized in museum software, is the museum's **object-documentation system of record**, held together by three jointly-loaded structures:

1. **The accessioned intake.** Objects enter the collection through a recorded acquisition event — source (donor/seller/originating person or institution), method (gift, purchase, bequest, transfer), date, with title-transfer evidence retained — that is formally accessioned into the permanent collection, and each accessioned object receives a unique number that is used to label/mark the object and to bind the physical object to its record and its acquisition documentation. (Remove → an object database with no acquisition/custody semantics: a generic catalog or asset inventory.)
2. **The object catalogue record.** A persistent, individually identified record per object (or defined object group) — the authoritative documentation of what the institution holds — carrying identification and description (object name, classification, maker/origin, date, materials, dimensions) at whatever depth the institution's policy sets, beyond bare inventory. (Remove → an acquisition register/log with nothing documented about the objects.)
3. **The ongoing cataloguing work loop.** Records are actively enriched and maintained over time — description, authority-controlled terminology, images/media, provenance and history, credit lines, links to related people/places/objects — kept searchable, with changes attributable and the accession record tamper-resistant and backed up; cataloguing is explicitly open-ended, never "complete." (Remove → a static numbered inventory.)

Jointly-held is load-bearing: 1 alone = acquisition paperwork log; 2 alone = descriptive catalog without custody/acquisition semantics (library-catalog/asset-inventory territory); 3 alone = knowledge management with no object spine; 1+2 without 3 = frozen inventory below the Type; 2+3 without 1 = undocumented-provenance catalog.

Anchor evidence: Spectrum's two primary procedures define exactly this pair (accession = formal numbered intake with title evidence and long-term care commitment; cataloguing = ongoing record building per object, from the object number outward), and every sampled product carries both as its core.

### L1 — Common Mature Structure (very common in mature products, not definitional)

- Configurable record structure (fields, forms, screens per institution/discipline) — TMS, MuseumPlus, CatalogIt, CA all advertise it
- Authority/terminology control — thesauri/vocabularies (Getty AAT/TGN, LCSH) for consistent description
- Person/constituent records (donors, makers, artists, contacts) linked to object records
- Images and other media attached to and referenced from the record
- Numbering-scheme configuration and enforcement (beyond the bare L0 numbering act) — documented as machinery in CatalogIt (strict accessioning, pattern tokens); presumed common but only single-product-verified at that depth
- Acquisition paperwork artifacts generated from records (deed of gift, receipts, credit lines)
- Counterpart exit workflow (deaccession/object exit) recorded in the same system
- Search over the whole catalogue; data import/migration and batch editing; data-cleaning/consistency tooling
- Multi-user roles and permissions over record creation/editing; audit trails of record changes
- Printed/printed-style registers and reports (the digital descendants of the accession register and card catalogue)
- Discipline-specific schemas and classification systems per collecting area

### L2 — Variant / Optional Structure

- Deployment: SaaS-only cloud (CatalogIt) vs on-prem/vendor-hosted enterprise (TMS, MuseumPlus) vs self-hosted open source (CollectiveAccess)
- Segment: national/large institutions vs mid-size vs historical societies/small museums vs **private collectors** (CatalogIt sells the same record-creating core to personal collections; Spectrum's custody/ethical framing is museum-specific but the record structure travels)
- Discipline breadth: art, history, natural history, archaeology, archives and library hybrids (TMS ships archive and bibliographic modules; CA targets heterogeneous collections)
- Standards regime: Spectrum (UK/international), CDWA/CCO/LIDO/CIDOC CRM/VRA Core/CHIN (TMS lists many); multilingual cataloguing (TMS 24 languages)
- Era machinery: AI image-description assistance (CatalogIt) — current implementations, not definitional
- Adjacent published surfaces (eMuseum, Pawtucket, CatalogIt HUB) and downstream workflows (locations, loans, exhibitions, conservation) — separate Types/modules, not this one

### L3 — Vendor-specific (kept here, not in the final document)

- CatalogIt: "Strict Accessioning" default with deviation errors; pattern tokens (Y/M/D/N/a/A, L/Q/FIC/D prefixes); Owner/Admin/Read-Write/Editor permission names; Entry/Folder/Profile terminology; plan limits (25,000 entries etc.)
- TMS Collections: 11-module composition; Registration menu with Rights and Reproduction screen; Audit Manager as separate product; eMuseum publishing companion; concurrent-user licensing
- MuseumPlus: named Core Functions (Customer Service register, Digital Assets, Contracts, Exhibition Management); Curator add-on for 3D planning (per sibling pass)
- CollectiveAccess: Providence/Pawtucket component split; 2003 origin story

## Vendor-specific vs Type Findings (explicit)

- The **three-part accession→object numbering pattern** (year.lot.object) is stated by CatalogIt as what "most museums in the US follow" — a vendor-authored generalization, not independently verified across the sample; recorded as common practice with attribution, NOT as a Type invariant. The invariant is: unique numbers assigned at accession, used to bind objects to records.
- **Strict numbering enforcement** is only CatalogIt-verified → L1/common-with-attribution, not core.
- **Acquisition vs accession separation as a named profile** is CatalogIt's implementation of a distinction Spectrum states normatively → the distinction is Type-level; the separate-profile mechanism is product-level.
- TMS/MuseumPlus module inventories (contracts, exhibitions, events) are suite packaging → not Type findings.

## Rejected Findings

- "Accession/cataloging is a standalone product category" — REJECTED: no standalone product in the reachable sample; every realization is inside a CMS (consistent with the archaeological pass's observation).
- "Cataloguing has a defined ideal record/minimum field set in software" — REJECTED: Spectrum explicitly denies an ideal record; depth is policy-driven; TMS's data-cleaning alerts show even required-ness is configurable.
- "Cataloging = digitization of collections" — REJECTED: cataloging is documentation of objects; digitized surrogates/media are one enrichment class among many.
- "AI-assisted description is part of the workflow definition" — REJECTED: single-product, current-era feature (CatalogIt AI Describe Image); era machinery.
- "Public web publishing belongs to this Type" — REJECTED: publishing is a separate surface (Digital Collection Portal; eMuseum/Pawtucket/HUB are companions), and CollectiveAccess's own split (Providence vs Pawtucket) shows the market draws this line.
- "US three-part numbering is the Type's numbering system" — REJECTED as invariant (see vendor-specific vs Type findings); regional/vendor-attributed common practice.

## Boundary Findings

**1. vs Museum Collections Management (§27 sibling, unprocessed at pass time) — the central one.**
All sampled products are collections-management systems; accession+cataloging is their record-creating core, sitting beside movement/location, loans, exhibitions, conservation, condition, rights, audit modules (TMS's own Spectrum-procedure list shows the whole family). Structural test: strip the downstream custody/ops workflows and the accession+catalog core still stands as the documentation system of record (small-museum and collector products nearly realize this bare form; Spectrum allows a paper version); strip the record-creating core and the remaining modules are workflows over records that no longer exist. Verdict: the leaf documents the record-creation workflow slice — probable Workflow-layer/Capability-of relationship with Museum Collections Management, consistent with the pre-hung archaeological-pass flag. Keep-both with containment framing (precedent: exhibition-planning/installation/logistics passes); final consolidation is a taxonomy-owner decision at joint review when museum-collections-management is processed.

**2. vs Archaeological Collection Management (processed 2026-09-06).** That leaf's L0 already contains an accession→cataloging lifecycle leg; its differentiator is the excavation-context (site→stratum→object) documentation layer. Remove the context layer → this Type's structure remains. Confirms the seam and discharges that pass's "flagged for joint review" expectation from this side: the shared spine is real, the context layer is the discriminator.

**3. vs Digital Collection Portal (processed 2026-09-07).** Portal = published public surface over records governed elsewhere; this Type = creation and maintenance of those authoritative records. That pass's note ("no custody or cataloging machinery of its own") is exactly the complement of this leaf. Clean, confirmed both directions.

**4. vs Provenance Research Platform (§27 sibling, unprocessed).** Catalogue records carry provenance/history fields (Spectrum object history-and-association group), but the research apparatus (structured investigation of an object's ownership history, evidence chains) is a different job over the same records. Adjacent; expected to hold as long as that leaf's core is investigation machinery rather than record creation. Left as a note for its pass.

**5. vs Integrated Library System / library cataloging (§23).** Bibliographic world: records describe editions/works held in copies, identified by call/copy numbers, with circulation; the museum world: unique objects under permanent custody, identified by accession-derived numbers, with credit lines and provenance rather than holdings and circulation. Different object worlds, different legal semantics (title transfer vs acquisition of copies). Distinct Types.

**6. vs Auction Management System (processed 2026-09-06).** Its cataloging leg builds lots as units of sale for a commercial close (buyer invoice, seller settlement). Museum accessioning builds records for permanent custody with an explicit no-sale disposition default (deaccessioning is a governed exception, not the terminus). Distinct.

**7. vs Enterprise Asset Registry (§10) / generic asset inventory.** An asset registry tracks what an organization owns and where it is. The accession/catalog Type adds: recorded acquisition events with source and method-of-acquisition semantics, permanent-collection commitment, provenance and scholarship as record content, authority-controlled description, and formalized exit (deaccession). Remove the acquisition-event/credit/provenance semantics → asset registry.

**8. Downstream §27 siblings (object movement, loan, conservation, condition).** All operate on the object records this Type creates (movement/loan/condition passes each observed themselves as modules over the object record). This leaf owns record creation and initial identification; they own custody state, agreements, care. Consistent with how those leaves documented their boundaries.

## Historical / Market-Sample Check

Paper-era form: the accession register (bound ledger; one numbered entry per acquisition/lot, columns for source, mode of acquisition, date, description, and later the object number) + the catalogue card per object + a deed-of-gift file + annual numbering — satisfies all three L0 legs at analog level. Spectrum itself states cataloguing may run "in a computerised system… or paper-based system (eg on cards)", and its accessioning standard's requirements (unique number, marked object, tamperproof record, backup copy, title evidence) are all satisfiable on paper (the "backup" being a security copy). The definition therefore names no software surface, no cloud, no standards list, no AI — older, regional, paper-based, and platform-native realizations all fit. Modern machinery (cloud, AI assistance, multilingual thesauri) is era layering, held outside the core.

## Uncertainties

- Operational screen-level detail for the enterprise incumbents (TMS Collections, MuseumPlus) is login-gated; their accession/cataloging module internals (exact fields, states, numbering enforcement behavior) are documented here only at product-page and Collections-Trust-directory level. No screen-level claims are made for them.
- CollectiveAccess operational workflow (how its lots/objects accessions behave in practice) unverified — doc hosts unreachable; positioning-level evidence only.
- Whether any market product positions itself as a standalone "accession & cataloging" tool (outside a CMS) could not be exhaustively excluded; nothing was found in the reachable sample.
- The US three-part numbering prevalence claim rests on one vendor-authored statement (CatalogIt consultant article + help page).
- Spectrum is UK-framed (accreditation) though used internationally; other regional standards frameworks (e.g., CHIN in Canada, Smithsonian vocabularies in the US) were not fetched and are not asserted.

## Final Synthesis

The leaf names the museum's **record-creating workflow**: the accession — a formal, numbered, evidenced intake of objects into the permanent collection (source, method, title, commitment to long-term care) — and the catalogue — the per-object authoritative record that starts at identification and is enriched indefinitely with description, terminology, media, provenance, and links, kept searchable, attributable, and tamper-resistant. In the current market this workflow is not sold separately; it is the core of every collections-management system, from enterprise incumbents to small-museum cloud products to open-source platforms, and it is defined normatively by the domain standard (Spectrum's two primary procedures). The Type stands as the record-creation layer over the collection, with Museum Collections Management as its containing system and the custody/loan/exhibition/conservation siblings as downstream consumers of the records it creates. Joint review with museum-collections-management is recommended; candidate outcomes consistent with sibling precedent are keep-both-with-containment or consolidation as the documentation layer of a single CMS Type.
