# Research Notes — Institutional Repository

Research date: 2026-09-08
Leaf: Institutional Repository (DIRECTORY §23 Education, Research & Knowledge Institutions)
Slug: institutional-repository

---

## Research Goal

Understand what an Institutional Repository (IR) actually is as an Application Type: what objects exist inside it, whose works it holds, how works enter it, how access and delivery are governed, who operates it, and where its boundary lies against neighboring Types — above all the **Digital Library Platform** (processed 2026-09-07, which left a pending joint-review question about this leaf), plus CRIS / Research Information Management, Integrated Library System, Library Discovery Platform, Archives Management System, Academic Journal Management, Research Data Management, and ePortfolio Platform.

## Initial Boundary

- Hypothesis entering research: an IR is an institution's self-archive of its own research output, with submission/deposit workflows and open-access delivery.
- The digital-library-platform pass (2026-09-07) recorded: "the market does not cleanly separate the two labels — DSpace, the canonical institutional-repository product, is equally the canonical digital-collections platform"; it treated IR as a deployment/variant of DLP and flagged this leaf for joint review to ratify **keep-both-with-seam vs variant presentation**.
- This pass must therefore produce an independent IR definition and explicitly ratify or reject the keep-both-with-seam reading.

## Research Questions

1. What is the unit of record — is it metadata-only or metadata + held content files?
2. What is the corpus — whose works, and of what types?
3. How do works enter the record — author self-deposit, staff mediation, automated feeds? What review gates exist?
4. What access machinery exists — embargoes, restricted files, security tiers?
5. How is the corpus delivered — item pages, portals, harvesting, search engines?
6. What persistent-identity/citation machinery exists — handles, DOIs, URIs?
7. What curation and maintenance loops exist — withdrawal, dedupe, corrections, versioning?
8. Where exactly is the IR vs Digital Library Platform seam, and the IR vs CRIS seam?
9. Historical check: would the founding-generation products (EPrints 2000, DSpace 2002) satisfy the definition? Would a paper-era ancestor?

## Representative Products

| Product | Steward | Philosophy / posture | Customer tier | Evidence quality |
|---|---|---|---|---|
| DSpace | LYRASIS + open-source community | open-source repository platform; self-hosted or partner-hosted; the dominant IR software | universities worldwide, consortia | A — official functional documentation (fetched) |
| EPrints | University of Southampton / EPrints Services | open-source; the original IR software (early 2000s); services-backed hosting; strong UK/AU footprint | 760+ registered installations; universities, journals | A — official wiki glossary + introduction (fetched) |
| Digital Commons (bepress / Elsevier) | Elsevier | turnkey hosted SaaS IR; consulting-mediated configuration | broad: small colleges through large universities | A — official help center (fetched, multiple articles) |
| Esploro | Ex Libris | commercial research-services platform; repository integrated with researcher profiles, portal, library ecosystem | research universities | A — official online help (fetched, multiple pages) |
| Pure | Elsevier | CRIS/RIMS first, repository capability as one module | 500+ research-intensive institutions | A for positioning (product page fetched); operational docs not fetched — boundary anchor only |

Selection rationale: market representation (DSpace/EPrints dominate open-source IR; Digital Commons and Esploro lead the hosted/commercial poles), documentation completeness, different product philosophies (community open-source vs services-backed open-source vs turnkey SaaS vs suite-integrated), different customer tiers. Pure is deliberately included as a **boundary anchor** (see Product Mismatch note below).

## Sources

All fetched 2026-09-08:

- DSpace 7.x Documentation — Functional Overview (LYRASIS wiki): https://wiki.lyrasis.org/display/DSDOC7x/Functional+Overview
- EPrints — What is EPrints?: https://www.eprints.org/what-is-eprints/
- EPrints — main site (positioning, testimonials): https://www.eprints.org/
- EPrints — The EPrints Platform: https://www.eprints.org/the-eprints-platform/
- EPrints Documentation wiki — Main Page: https://wiki.eprints.org/w/
- EPrints Documentation wiki — EPrints Glossary: https://wiki.eprints.org/w/EPrints_Glossary
- EPrints Documentation wiki — Introduction: https://wiki.eprints.org/w/Introduction
- Digital Commons Help Center — Digital Commons IR category: https://digitalcommons.elsevier.com/en_US/digital-commons-ir
- Digital Commons — Author Submission Steps in Digital Commons: https://digitalcommons.elsevier.com/en_US/managing-submissions-publishing/author-submission-steps-in-digital-commons
- Digital Commons — Access Control and Embargoes: https://digitalcommons.elsevier.com/en_US/managing-submissions-publishing/access-control-and-embargoes-options-for-restricting-content
- Digital Commons — Harvesting Tool (Populating the IR with Faculty Records): https://digitalcommons.elsevier.com/en_US/integration-preservation/digital-commons-harvesting-tool
- Esploro Online Help (English) — top page: https://knowledge.exlibrisgroup.com/Esploro/Product_Documentation/Esploro_Online_Help_(English)
- Esploro — Adding and Working with Research Deposits: https://knowledge.exlibrisgroup.com/Esploro/Product_Documentation/Esploro_Online_Help_(English)/Working_with_the_Esploro_Research_Hub/020_Working_with_Research_Deposits
- Pure — product page (Elsevier): https://www.elsevier.com/products/pure

---

## Product Observations

### DSpace (evidence layer A — official functional documentation)

- **Data model**: each site is divided into *communities* (mirroring college/department/center structure) containing *collections*; collections contain *items*; items are subdivided into named *bundles* of *bitstreams* (files). Bundles in practice: ORIGINAL (deposited files), THUMBNAILS, TEXT (extracted full text for indexing), LICENSE (the deposit license), CC_LICENSE.
- **Item** = descriptive metadata (qualified Dublin Core by default; multiple schemas configurable) + administrative metadata (provenance, policies) + structural metadata (bundle/bitstream ordering).
- **Ingest is a process, not a form**: the Web submission UI or batch importer assembles an "in progress submission"; depending on collection policy a **workflow** starts — up to three steps (review / edit / finaledit), each with an associated e-person group; tasks go to a group's *task pool*, one member claims the task; actions are accept / reject (steps 1–2) / commit-to-archive (step 3). Rejection emails the submitter and returns the item to their workspace for correction and resubmission.
- **Item installer** (after workflow acceptance): assigns accession date, adds date.available, records provenance (filenames + checksums), assigns a **Handle persistent identifier** (CNRI Handle System; each site has a unique prefix), adds the item to the target collection with authorization policies, and adds it to search and browse indexes.
- **Deposit license**: at the end of submission the submitter grants the repository a distribution license (commonly non-exclusive); customizable per collection. Creative Commons license selection supported per item.
- **Authorization**: resource policies bind actions (READ/WRITE/ADD/REMOVE…) on objects (community/collection/item/bundle/bitstream) to e-people/groups; 'Anonymous' READ is the public posture; permissions are explicit, default deny. Collections carry DEFAULT_ITEM_READ / DEFAULT_BITSTREAM_READ policies inherited at submission.
- **Withdrawal vs expunge**: withdrawn items remain in the archive but hidden, presented to end users as a **tombstone**; expunged items are removed entirely.
- **Discovery**: full-text search over metadata + extracted document text; faceted browsing; browse indexes (title, issue date, author, subject); OpenURL support; deliberate **Google / Google Scholar indexing optimization** (metadata in page head tags; popular repositories reportedly draw the majority of visits from Google).
- **Getting content in/out**: batch item import/export (XML metadata + files), package importers (METS etc.), AIP backup/restore, **registration** of externally hosted files (metadata in DSpace, bitstreams elsewhere), **SWORD / SWORDv2** remote-deposit protocols, **OAI-PMH** metadata exposure (with sets = collection structure; deletion information for withdrawn items), FAIR Signposting profile.
- **Preservation**: bitstream format registry with per-format **support levels** (supported / known / unsupported); checksum checker for corruption/tamper verification.
- **Users**: e-people + groups; self-registration possible; LDAP/authentication stacks; **supervision orders** bind thesis supervisors to a student's pre-submission workspace with defined policy levels.
- **Usage statistics**: SolR-based page views and file downloads per item/collection/community, monthly breakdowns, country/city views.

### EPrints (evidence layer A — official wiki glossary + introduction; positioning pages)

- **Positioning**: "Open Source digital repository platform… used primarily as an Open Access repository for promoting and sharing academic outputs by way of an easily discoverable Web presence"; also used for research data, educational resources, theses, and even single journals/conferences. Series began early 2000; 760+ registered installations; 25 years. Testimonials emphasize green open access, funder compliance for publications, grey literature (theses, working papers), and integration with institutional systems including REF-adjacent systems (UK).
- **Data model**: *eprint* (first-class data object — the publication record) → *document* (second-class; must belong to an eprint; carries files) → *file* (third-class; filename, size, MIME, MD5 hash for integrity). Plus *user*, *subject*, *history* objects. A repository can host multiple *archives*.
- **Status lifecycle** (the depositing lifecycle): **user workarea** (depositing user still editing) → **review buffer** (submitted for review) → **live archive** (reviewed by an *editor* user and made publicly accessible) → **retired** (removed from live archive; no longer public). Editors can amend records in the review buffer and either push to live archive or return to the user's workarea.
- **EPrint types** (publication flavour defaults): article, book_section, monograph, conference_item, book, thesis, patent, artefact, exhibition, composition, performance, image, video, audio, dataset, experiment, teaching_resource, other. Type chosen at workflow stage 1 and drives later fields.
- **Document security**: per-document access value — *public* / *validuser* (registered users) / *staffonly* (editors + admins); combinable with an **embargo** until a set date, after which security auto-updates to public (lift script). Embargo reasons from a configurable named set.
- **Version semantics**: *document content* field describes the version — draft / submitted / accepted / published (explicitly mapped to Author's Original Manuscript / Accepted Manuscript / Version of Record).
- **Public delivery**: *abstract pages* (cached public item pages: metadata, abstract, download links, summary table); *browse views* over metadata fields (defaults: year, subjects, divisions, creators); simple + advanced search; full-text indexing of uploaded documents; latest-additions tool.
- **Organization**: no curated collection containers in the core model — the archive is organized through metadata fields; *divisions* (hierarchical org units: faculty/school/department/group) is a default eprint field with its own browse view.
- **Integrity/quality machinery**: eprint revisions (numbered, exported as XML revision files) with history tab; **issues audit** (scheduled) flags duplicate titles, similar titles, old-but-unpublished items, malformed creator names; edit locking.
- **Metadata exposure**: OAI-PMH interface; export plugins in many formats; import plugins; REST/CRUD API.
- **Licensing**: Creative Commons v4 license set as default options for documents.
- **Extensibility**: flavours (publication / data / education), ingredients, Bazaar plugin packages; per-archive configuration overrides.
- **Review posture is a policy choice**: the introduction explicitly frames day-to-day operation as the institution's choice — "a very light touch on the data submitted or a formal review process on each item".

### Digital Commons (evidence layer A — official help center)

- **Product family**: Digital Commons IR + Digital Commons Exhibits + Digital Commons Journals + Digital Commons Data — the IR is one product in a suite; the IR documentation is explicitly "for DC Institutional Repository administrators".
- **Structures**: the IR is organized into *publications* (series, journals, event communities, book/image galleries) and *communities*, with a *group tool* for hierarchies and a *collection tool* that can display one submission in multiple publications. A three-tiered taxonomy of academic disciplines is available.
- **Author submission flow** (documented step-by-step): from a publication page the author clicks **Submit Research** → logs in / creates account → (journals: submission instructions) → **submission agreement** checkbox → submission form (metadata + file upload; supplemental files optional) → submit → confirmation screen → **pending administrator approval** → posted by administrator/editor. Authors get a **My Account** page listing their submissions with status; they can revise, withdraw, add supplemental files, email the administrator — these options lock once published/rejected/withdrawn/locked. Email address enables correspondence, publication notifications, and periodic usage reports (download activity).
- **Access control** (per publication, enabled via consulting services): authenticate approved visitors by **IP address / email domain / account email list**; administrators and authors always have access. Open-access exceptions within a restricted publication: by document type, by a "force open access" field (optionally admin-only), by time frame (fixed date or moving wall).
- **Embargoes** (per item): embargo field on the submission form (expiration date or time-period dropdown); metadata page shows "Available for download on <date>"; download button stays active and serves the file automatically after expiry; administrators/authors see the full text throughout. Past dates = no embargo.
- **Restricted-download semantics**: access control and embargoes apply to the **primary full-text file only**; metadata and supplemental content remain public; metadata stays visible in repository search and is indexed by search engines (the restricted file itself is not; full-text indexing of restricted files available on request). "While restricting materials is not typical in open access repositories, some institutions need to provide certain documents only to designated visitors."
- **Intake at scale — Harvesting Tool**: populates the IR from **Scopus, Pure, ORCID, PubMed** APIs plus **Jisc Open Policy Finder** (formerly Sherpa/RoMEO) for journal permissions: find the institution's works, identify OA content, map/prepopulate metadata (import full texts from Pure), dedupe against existing records, check publisher permissions; export to prepopulated batch-upload spreadsheets → batch import. Explicitly supports both postures: "regardless of whether your IR hosts metadata-only records or requires a full-text file/copy with every record".
- **Other machinery**: batch upload/export/revise; ETD series publishing; DOIs; OAI-PMH outbound harvesting; bepress Archive (preservation); API; dashboards + author dashboards + PlumX metrics + readership map; SEO features; hiding/excluding/withdrawing content; author merge tool (combining author records).

### Esploro (evidence layer A — official online help)

- **Positioning**: Ex Libris "research information management solution"; the product spans a staff **Research Hub**, a public **Research Portal**, and **researcher profiles**. The repository function is integrated with profiles, grants, projects, media mentions, organizational units.
- **Deposit → asset lifecycle**: "The first time you add an asset to Esploro it is called a deposit. After approval, the deposit becomes an Esploro asset." Approval makes the asset "part of the repository and discoverable, depending on its access rights policy."
- **Four intake paths**: (1) **staff-mediated deposits** (wizard: researcher + creator/contributor role, mandatory organization academic unit, asset type driving type-specific fields e.g. DOI/ISBN/PMID, file upload; page 2 prefilled from Ex Libris' Summon central index by match on entered metadata or file metadata); (2) **researcher self-deposit** from their profile in the portal; (3) **non-researcher (student) deposit forms** — configurable per-profile forms exposed at a dedicated URL (default profile: Undergraduate ETD Submissions), with configurable fields, deposit policies, and automatic approval letters (advisors CC'd); (4) **Smart Harvesting** — automated building of the asset list for profiles and the repository, with author-matching approval task lists and researchers claiming outputs.
- **Deposit management**: Research Deposits page with assignment (assign to administrator / release), actions: approve, **return** (status → Returned, email with reason + optional note; researcher corrects and resubmits), contact researcher, save draft, change asset type, edit in generic form, view files, **register DOI** (Crossref/DataCite; locally generated DOI or handle used as permalink), delete. Duplicate indicator (same DOI/title) warns staff and depositors.
- **Roles**: Research Assets Curator, Research Assets Manager (delete + assign), Research Observer (view only).
- **Record anatomy**: tabs for Asset (multi-language abstract/subjects), Attachments (policy documents, correspondence), Internal Notes, Communications (researcher correspondence, visible on the researcher profile too), History (status-change notes), Assessment Profile (configurable, for reporting).
- **Publication constraints**: publication-category deposits cannot be approved without at least one date under Statuses and Dates.
- **Publishing/delivery**: publishing to OAI, FTP export, Google Search/Scholar/Datasets, **Primo** (library discovery), ORCID; SEO best-practice guide; portal asset display configuration; **file access requests** — a request workflow for restricted files; CV management from profiles.
- **Integration**: SIS, SWORD, Web of Science, InCites, DataCite/Crossref mapping, ETD Administrator, handle server, redirect of previous repository portal URLs.

### Pure (evidence layer A for positioning only — product page; operational docs not fetched)

- Pure is positioned as a **Research Information Management System (RIMS/CRIS)**: "aggregate, manage and showcase your research data in one secure platform"; 500+ institutions across 50+ countries.
- Scope spans publications, funding, people, projects, impact — a single source of truth synchronized automatically with **Scopus, ORCID, national CRIS registers, HR and finance systems**.
- The **Pure Portal** is the public showcase ("ready-made, search-optimized showcase"); open-access compliance workflows and funder/national-assessment reporting (e.g., REF in the UK) are first-class concerns.
- **Boundary note**: Pure's center of gravity is research information management (people/grants/projects/impact), not the open self-archive; its repository capability (holding and delivering output files) is one module of a broader system. Recorded as a Product Mismatch per the workflow: selected as a boundary anchor, not as a canonical IR sample.

---

## Cross-product Comparison

| Aspect | DSpace | EPrints | Digital Commons | Esploro | Pure (boundary) |
|---|---|---|---|---|---|
| Corpus | institution's own output: articles, ETDs, data, multimedia, learning objects | research publications primarily; data/education flavours exist | faculty publications, ETDs, journals, proceedings, galleries, data | research assets: publications, datasets, ETDs, creative works, patents, teaching | publications + funding + people + projects (CRIS span) |
| Unit of record | Item = metadata + bitstreams in bundles | Eprint = metadata + documents + files | submission/publication record with full-text file | research asset (deposit → asset) | research output record |
| Intake paths | submission UI → workflow steps; batch import; SWORD; registration of external files | deposit → review buffer → editor review; import plugins | author Submit Research form → admin approval; batch upload; harvesting tool | staff wizard; researcher self-deposit; student forms; smart harvesting | automated sync (Scopus/ORCID/HR) + validation |
| Review gate | up to 3 workflow steps with group task pools; configurable | editor review buffer; posture is institution's choice ("light touch … or formal review") | administrator approval before posting | approve / return-with-reason; assignment to curators | validation/compliance workflows (positioning-level) |
| Access machinery | resource policies; anonymous READ default; collection-level defaults | document security public/validuser/staffonly + embargo with auto-lift | per-publication access control (IP/email-domain/email-list) + per-item embargoes; metadata stays public | access rights policies; file requests for restricted files | portal visibility (positioning-level) |
| Persistent identity | Handles (CNRI) | eprint URI/URL | DOIs | DOI registration (Crossref/DataCite) + handles | (Scopus IDs etc.) |
| Public delivery | item pages; Google Scholar optimization; OAI-PMH; OpenURL | abstract pages; browse views; OAI-PMH | publication pages; OAI-PMH outbound; SEO | research portal + researcher profiles; publishing to Google/Scholar/Primo/OAI | Pure Portal |
| Organization of corpus | communities → collections tree | flat archive organized by metadata browse views (divisions/subjects/year/creator) | publications + communities + group/collection tools | organizational units + collections | org hierarchy |
| Version semantics | provenance messages; bitstream versioning implicit | document content: submitted/accepted/published (AOM/AM/VoR) | revise/withdraw before publication; version history | deposit → asset; history tab | (positioning-level) |
| Preservation | checksum checker; AIP backup/restore; format support levels | revision files; digital-preservation guidance | bepress Archive | (Ex Libris ecosystem) | — |
| Metrics | usage statistics (views/downloads, countries) | access statistics | dashboards, author dashboards, PlumX, readership map | analytics module | research analytics |
| Harvesting exposure | OAI-PMH (sets, deletion info) | OAI-PMH | OAI-PMH outbound | OAI publishing + FTP | (national CRIS registers) |

**Cross-product commonalities (evidence layer B):**

1. The corpus is **the institution's own research output** — works produced by the institution's researchers/students, not acquired or digitized heritage material. (All four IR-native products.)
2. The unit of record is a **persistent identified item binding bibliographic metadata to held content files**. (All four; metadata-only records exist as a documented posture in Digital Commons, but the file-holding function is the product family's center.)
3. Works enter through a **managed intake path** — deposit/ingest machinery with metadata capture and file upload — rather than by hand-editing a website. (All four.)
4. Intake is **commonly gated by review/approval** before publication, with a return-to-depositor path. (All four; EPrints documents the gate as an institution-level policy choice, DSpace allows collections with no workflow steps — so the gate is common-mature, not invariant.)
5. **Open access is the default delivery posture**, with restriction as the managed exception (embargo, security tiers, access control). (All four; Digital Commons states restriction "is not typical in open access repositories".)
6. **Metadata stays public even when files are restricted** (DSpace: "item metadata is always viewable"; Digital Commons: metadata visible and search-engine indexed while file restricted; EPrints: abstract page public, document security gates the file; Esploro: discoverable "depending on its access rights policy" + file-request workflow).
7. **Persistent identifiers** for items (handles, URIs, DOIs). (All four; scheme varies.)
8. **Metadata harvesting exposure** (OAI-PMH in all four IR-native products) and **search-engine/Google Scholar optimization** (DSpace, Digital Commons, Esploro documented).
9. **Withdrawal is deliberate and visible** (tombstone in DSpace; retired status in EPrints; hiding/excluding/withdrawing in Digital Commons).
10. **Usage statistics** (views/downloads) for administrators and often authors. (All four.)
11. **Duplicate detection** (EPrints issues audit; Digital Commons harvesting dedupe; Esploro duplicate indicator).
12. **Embargo with automatic expiry** (EPrints auto-lift; Digital Commons auto-expiry; Esploro access-rights dates; DSpace via policies).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

An Institutional Repository is the institution's system of record for **its own research output**, held as persistent identified items (bibliographic metadata + content files), filled through a **managed intake path**, and delivered on the **open web under an open-access posture**.

Three jointly-held structures:

1. **The institution's own output as the collection of record** — a persistent, individually identified record per scholarly work produced by the institution's researchers (and students), binding bibliographic metadata to held content files. Remove → a file store or a bibliographic database with no institutional self-archive.
2. **The managed intake path** — works enter through the system's deposit/ingest machinery (author self-deposit, staff-mediated deposit, or automated feed), with metadata capture, file upload, and (commonly) a review/approval gate before publication. Remove → a static publications website or showcase with no machinery of record.
3. **Open-access public delivery** — public item pages on the web where the deposited work is discoverable and downloadable; open access is the default posture, embargo/restriction the managed exception; the record is citable (persistent identifiers). Remove → an internal research-records system (CRIS territory) or a dark archive.

**Jointly-held is load-bearing:**

- 1 alone = file store / bibliographic database
- 2 without 1 = a submission form with nowhere to archive
- 3 without 1+2 = a website
- 1+2 without 3 = internal research records (CRIS without the open delivery)
- 1+3 without 2 = static showcase site (no intake machinery)

**Not in L0** (modern-market expectations held below the line): collection/community containers (EPrints organizes a flat archive by browse views — counter-sample), OAI-PMH, Google Scholar optimization, ORCID, DOIs specifically (handles/URIs equally valid), embargoes specifically, version semantics, preservation programs, metrics, funder-policy machinery, researcher profiles.

### L1 — Common Mature Structure

Present in most mature products; makes the Type practical but does not define it:

- deposit licenses / submission agreements accepted at deposit time
- review/approval gates with return-to-depositor loops (configurable depth)
- embargo machinery with automatic expiry; document security tiers (public / institution / staff)
- version semantics for deposited files (submitted / accepted / published)
- persistent identifiers (handles, DOIs, URIs) and citation support
- OAI-PMH metadata exposure; search-engine / Google Scholar optimization
- full-text search + browse indexes over metadata fields
- batch ingest/import; duplicate detection
- usage statistics (views/downloads), author-facing reports/notifications
- controlled vocabularies (subjects, organizational divisions)
- withdrawal with tombstone / retired status
- DOI registration (in addition to native identifiers)

### L2 — Variant / Optional Structure

- **Corpus scope**: publications + ETDs only; + datasets; + creative/performance works; + teaching materials (EPrints education flavour); + patents
- **Intake mix**: author self-deposit-first vs staff-mediated-first vs automated-harvest-first (the modern drift: smart harvesting, API feeds from Scopus/Pure/ORCID/PubMed)
- **Metadata-only vs full-text posture**: some IRs hold metadata-only records with links; others require a deposited file per record (both documented postures in Digital Commons)
- **Suite integration**: standalone IR vs IR as module of a research-information/library suite (Esploro, Pure); journal/conference publishing add-ons (Digital Commons Journals; EPrints used to run journals)
- **Hosting posture**: self-hosted open source vs vendor-hosted SaaS vs services-backed hosting
- **Preservation programs**: fixity checking, AIP backup/restore, format support levels (stronger in some products)
- **Policy-environment machinery**: funder/journal permission checking (Jisc Open Policy Finder), national assessment support (REF-adjacent), open-access compliance workflows
- **Showcase layers**: exhibits, researcher profiles, CV management

### L3 — Vendor-specific Structure (research notes only)

- DSpace: Communities/Collections/Bundles/Bitstreams vocabulary; CNRI Handle infrastructure; supervision orders; bitstream format registry with support levels; AIP backup/restore; stackable authentication
- EPrints: flavours (publication/data/education) + ingredients + Bazaar EPMs; review buffer / live archive / retired terminology; issues audit rules; citation style files; multi-archive repositories
- Digital Commons: publications/communities structures; group & collection tools; consulting-services-mediated configuration (access control enabled by request); PlumX metrics; readership map; bepress Archive; SelectedWorks lineage
- Esploro: Research Hub / Research Portal / researcher-profiles triad; Smart Harvesting framework with author-matching approval tasks; Summon CDI prefill; task lists; letters configuration; assessment profiles; Primo publishing
- Pure: Scopus synchronization; national assessment frameworks (REF, SEP/KUOZ); SciVal/InCites integrations

## Historical / Market-Sample Check

- **Founding generation**: EPrints (series began early 2000) and DSpace (2002-era design, Handle-based, Dublin Core, workflow gatekeepers) satisfy the three-part core with none of the modern machinery — no Google Scholar optimization, no ORCID, no harvesting frameworks, no DOI registration, no smart anything. The definition is not over-fitted to the current hosted/AI-assisted market.
- **Regional spread**: EPrints is strongest in UK/AU (REF-adjacent workflows in testimonials); DSpace is global; Digital Commons is US-centric; Esploro sells internationally. All fit the same core; regional policy machinery (REF, funder mandates) sits in L2.
- **Differently positioned products**: Pure (CRIS-first) still carries the three legs for its output records but its center of gravity is the wider research-information span — confirming the CRIS boundary rather than breaking the IR definition. Corporate/enterprise research repositories with fully restricted delivery would sit at the Type's edge (open posture weakened); the canonical IR is the academic/research-institution open-access form.
- **Paper-era ancestor**: the university theses shelf and the institutional publications list are the thin ancestors; they lack public web delivery, so the Type is **born-digital** with the open-access movement — the honest historical anchor is the founding software generation (2000–2002), not a paper practice. This is recorded rather than forced.

## Vendor-specific Findings

See L3 above. Additionally:

- Digital Commons enables access control and embargo fields **via its consulting services** rather than self-service configuration — a packaging choice, not a Type property.
- Esploro's deposit wizard prefills metadata from the vendor's central index (Summon CDI) — vendor-ecosystem detail.
- DSpace's "popular repositories reportedly draw over 60% of visits from Google pages" is a vendor-documented claim about typical traffic, not a Type property; not carried into the final document as a precise figure.

## Boundary Findings

### vs Digital Library Platform (the pending joint review) — RATIFY keep-both-with-seam

The two Types share: digital items (metadata + files), public discovery, delivery to an audience, staff-operated machinery. The seam is real and structural:

1. **Whose material**: DLP curates material the institution **acquires or digitizes** (heritage collections, archives, exhibits — material that exists independently of the platform). IR holds material the institution's own people **produced** (its research output). Provenance of the corpus is the first discriminator.
2. **What is at the center**: DLP's center is **curation of collections** (collection containers are definitional there). IR's center is **intake of works** (the deposit/ingest path is definitional here). EPrints is the counter-sample that proves collection containers are NOT definitional for IR: it organizes a flat archive through metadata browse views with no curated collection containers, and is still a canonical IR.
3. **Delivery posture**: DLP delivers curated collections to an audience (open or restricted per item). IR is defined by the **open-access posture** toward the institution's own output, with restriction as managed exception.
4. **Products span both**: DSpace serves both roles; this is why the market blurs the labels — but spanning does not merge the Types. The same product family serving two centers of gravity is the classic keep-both pattern (cf. CRM vs marketing-automation seams recorded in earlier passes).

**Ratification**: keep both leaves. Digital Library Platform = institution-operated platform for curated collections of any material, curation-centered. Institutional Repository = the institution's system of record for its own research output, intake-centered with open-access delivery. The final DLP document's "subtype/variant" framing is superseded by this seam statement; the DLP leaf needs no rewrite (its core model stands), but the relationship row should eventually be read as "sibling Type with a provenance/intake seam" rather than "subtype".

### vs Research Information Management / CRIS (Research Information Management leaf, §23)

CRIS manages the institution's research **information** — people, grants, projects, outputs — for reporting, assessment, and compliance; the IR holds and openly delivers the output **content**. Remove open-access content delivery and add people/grants/projects → CRIS. Pure is the boundary anchor: CRIS-first with repository capability. Esploro deliberately straddles (research services platform with a repository at its core) — evidence that the seam is integration-depth, not a hard wall.

### vs Integrated Library System (§23)

ILS runs the physical collection's operations (cataloging, circulation, acquisitions, patrons). The IR hosts the institution's scholarly output. Ecosystem partners: IR metadata is harvested into catalogs/discovery layers; ETD workflows may touch ILS. Neither replaces the other.

### vs Library Discovery Platform (§23)

A discovery layer searches across external sources (catalog, subscriptions, repositories). The IR is the **host** that discovery layers index (Esploro publishes to Primo; DSpace optimizes for discovery-layer and Google Scholar indexing). Remove the hosted item store and intake → discovery platform.

### vs Archives Management System (§23)

Archives systems manage archival description and finding aids (intellectual control of archives, often including undigitized material). The IR self-archives the institution's output for open delivery. Overlap exists (some IRs accept EAD finding aids as items — recorded by the DLP pass), but the centers differ.

### vs Academic Journal Management / Peer Review Platform (§23)

Journals run an editorial decision workflow that produces publications; the IR captures and delivers works **after** the editorial fact (published articles, accepted manuscripts, theses). The academic-journal-management pass already recorded: repositories "store and expose already-published works or preprints without an editorial decision workflow"; Janeway ships a separate repository framework alongside its journal workflow — same-vendor evidence the two are different structures. Digital Commons ships both (Journals + IR) as separate products in one suite — same pattern.

### vs Research Data Management (§23)

Datasets are one work type within IR scope (DSpace hosts data; EPrints has a data flavour; Esploro has dataset asset types; Digital Commons has a Data product). Dedicated research-data-management adds data-specific machinery (metadata standards like domain schemas, data management plans, embargo/licensing depth). Boundary flagged for that leaf's own pass.

### vs ePortfolio Platform (§23)

The ePortfolio pass recorded: IR = "organization-published scholarly record, not a personal learning record". The ePortfolio's subject is the person's learning/evidence record; the IR's subject is the work.

### vs Government Open Data Portal / Public Data Portal (§24/§02)

Different subject matter (civic/dataset publication vs scholarly output) and different intake semantics (dataset publication vs work deposit with bibliographic identity). No overlap in evidence.

## Uncertainties

1. **Pure operational detail**: only the product page was fetched; Pure's repository-module mechanics (file handling, embargo machinery) are not evidenced at page level. Claims about Pure are limited to positioning. (Source-access limitation recorded; no memory-filling.)
2. **DSpace documentation version**: the fetched Functional Overview is the 7.x documentation tree (current release is 10.x). The documented structures (communities/collections/items, workflow, handles, OAI) are stable across the doc tree, but version-specific details were not re-verified against 10.x.
3. **EPrints deposit-license detail**: the glossary excerpt fetched does not include a deposit-agreement entry (DSpace and Digital Commons document deposit licenses/agreements explicitly). EPrints' deposit agreement is not asserted in the final document.
4. **Esploro repository positioning**: Esploro is marketed as a research-services platform; how many customers run it purely as an IR vs as a CRIS-with-repository is not evidenced. Treated as the suite-integrated pole.
5. **Market-share numbers**: no independent market-share figures were fetched; "dominant", "760+ installations", "500+ institutions" are vendor-documented figures only and are not carried as precise claims into the final document.
6. **Corporate IRs**: whether fully restricted corporate research repositories count as IRs is a judgment call recorded in the historical check; the canonical form documented is the academic open-access IR.

## Final Synthesis

The Institutional Repository stands as an independent Application Type with a three-part defining core: **the institution's own research output as a collection of persistent identified item records (metadata + held files), a managed intake path that captures works into the record (commonly gated by review), and open-access public delivery with persistent citation**. The corpus provenance (own output, not acquired heritage), the intake-centered structure (not curation-centered), and the open-access posture jointly distinguish it from the Digital Library Platform; the open content-delivery leg distinguishes it from CRIS. The joint review with the digital-library-platform pass is **ratified as keep-both-with-seam**: both leaves stand, the seam is provenance + center of gravity + delivery posture, and product spanning (DSpace) is expected and documented rather than treated as label collapse. The founding-generation check (EPrints 2000, DSpace 2002) confirms the core is not an artifact of the current hosted market; the paper-era ancestor is thin and the Type is honestly born-digital.
