# Research Notes — Cultural Heritage Asset Management

Research date: 2026-09-07

## Research Goal

Understand what a Cultural Heritage Asset Management application is as a distinct Application Type: what its world consists of (objects of record), who uses it, what workflows it supports, what rules govern it, and where its boundaries lie against Museum/Archaeological Collection Management, Government GIS, Digital Collection Portals, Building Asset Management, and Archives Management.

## Initial Boundary

Initial hypothesis (pre-research):

- Software for inventorying and managing cultural heritage **assets** — historic buildings, monuments, archaeological sites, parks/gardens/battlefields, cultural landscapes, districts, marine/underwater heritage — as place-based resources, for heritage agencies, local-government historic environment records, and heritage organizations.
- Nearest Types: Museum Collections Management and Archaeological Collection Management (objects in custody), Archives Management System, Government GIS, Land Records/Cadastre, Digital Collection Portal, Building Condition Assessment / Building Asset Management (§17 family), Public Data Portal.
- Working boundary hypothesis (inherited from the prior archaeological-collection-management pass, recorded in STATUS.md Boundary Issues): heritage-inventory platforms (Arches) register places/monuments/sites with geospatial visualization but have **no per-object custody** (accession, storage locations, loans). This pass tests and deepens that split from the heritage side.

## Research Questions

1. What is a "heritage asset" as the object of record? What record classes exist around it?
2. How are assets identified and characterized (IDs, typologies, thesauri, data standards)?
3. What role does spatial data play — is the map an organizing surface, and is GIS-native structure definitional?
4. What designation / legal-protection machinery exists (registers, lists, status)?
5. What condition / monitoring / risk machinery exists?
6. What workflows exist beyond inventory: designation/nomination, consultation/casework, field survey, publication?
7. Who uses the system (agency officers, HER officers, site managers, contractors, public) and through which surfaces?
8. How does data enter (legacy migration, survey capture, mobile, public nomination, APIs)?
9. Where exactly is the boundary against collection management (custody), Government GIS, portals, and facility-asset management?
10. Historical check: do pre-digital monument inventories / national registers still fit the definition?

## Representative Products

Chosen for market representativeness, documentation access, product philosophy, and customer tier:

| Product | Kind | Philosophy / Tier |
|---|---|---|
| **Arches** (Getty Conservation Institute + World Monuments Fund) | open-source heritage data-management platform | configurable, standards-based (CIDOC CRM), GIS-native; community-governed; used by national agencies, cities, and research projects worldwide |
| **exeGesis HBSMR** (Historic Buildings, Sites and Monuments Records) | commercial UK HER specialist software (an Idox company) | deep UK public-sector domain fit; vendor claims 75% of UK historic environment records managed with its systems; desktop+GIS+web architecture |
| **New York State CRIS** (Cultural Resource Information System) | government-built heritage inventory + review portal | agency-specific realization by a US State Historic Preservation Office; GIS + digitized records + program/review portal |

Supporting domain evidence: **MIDAS Heritage** data standard (FISH) and **FISH vocabularies** — the published information framework for this Type in the UK, used to check record-class commonality independent of any product. exeGesis **Local Heritage List Platform (LHLP)** was also fetched as same-vendor module-level evidence for the nomination→designation workflow (not counted as an independent sample).

## Sources

Fetched 2026-09-07:

- Arches — https://www.archesproject.org/what-is-arches/ (positioning + capability summary)
- Arches — https://www.archesproject.org/features/ (feature documentation)
- Arches — https://www.archesproject.org/arches-for-hers/ (HER-specific product, standards, consultations module, deployments)
- Arches — https://www.archesproject.org/implementations-of-arches/ (deployment landscape, ~40 implementations described)
- exeGesis — https://esdm.co.uk/ (product portfolio; "75% of UK historic environment records" claim)
- exeGesis — https://esdm.co.uk/hbsmr-features (feature list)
- exeGesis — https://esdm.co.uk/hbsmr-consultations (module description)
- exeGesis — https://esdm.co.uk/local-heritage-list-platform (workflow description, LHLP)
- HBSMR documentation portal — https://hbsmrdocumentation.esdm.co.uk/ (public index only; content behind registration)
- NY State CRIS — https://cris.parks.ny.gov/ (official splash/description pages)
- FISH — http://www.heritage-standards.org.uk/midas-heritage/ (MIDAS Heritage standard description; six themes)

Unreachable / limited:

- Historic England — https://historicengland.org.uk/advice/planning/plan-making/her-history/ → HTTP 403 (bot protection). Abandoned after one failure per network rule; UK HER domain detail therefore rests on FISH/MIDAS + vendor pages instead.
- HBSMR full user/admin documentation — registered users only; module structure confirmed from the public index; no field-level operational claims made.
- exeGesis `esdm.co.uk/hbsmr-web/` → 404; superseded by `/hbsmr-web-api` references in the doc index.

## Product A — Arches

### Key observations

- Positioning: "an open-source data management platform… originally developed for the cultural heritage field by the Getty Conservation Institute and World Monuments Fund"; "at its inception, Arches was specifically designed as a generic heritage inventory management system for the international cultural heritage field" (A).
- Three top-level capability groups (A): **Data Management** (manage, define, structure data), **Data Discovery and Visualization** (search, report, visualize — "e.g. geospatial data"), **Project/Task Management** (workflows for "sophisticated data editing procedures").
- Search layer (A): semantic & thesauri-enhanced search, geospatial search, saved/advanced search, searchable annotations, export of results.
- GIS layer (A): "essential geospatial tools in order to visualize and query resource locations"; integration with external GIS (Esri — "Arches Esri Link… directly access and edit Arches data from their Esri desktop GIS"); changeable basemaps incl. historical maps, overlays, satellite imagery.
- Relationships layer (A): "documentation and visualization of data relationships… people, materials, activities, historic events, objects, iconography"; related-resources graph.
- Time layer (A): temporal search, fuzzy dates, "Timewheel" time-distribution visualization.
- Data structure (A): semantic, self-describing data; multiple ontologies "e.g. CIDOC CRM"; API & linked-data support; dynamic UI generation; bulk data manager (csv/json/shapefile import); mobile data collection (Arches Collector; "mobile data collection via responsive workflow template").
- Controlled vocabularies (A): thesauri management via Reference Data Manager (RDM) / Controlled Lists Manager (CLM).
- Access & review (A): user/group secure access; granular permission control (card-level and resource-level); detailed audit of changes; "provisional (unpublished) data; data review"; data entry logged by user account.
- Arches for HERs (A): purpose-built version for UK Historic Environment Records; conforms to FISH standards incl. **MIDAS Heritage** ("buildings, monuments, archaeological sites, shipwrecks and submerged landscapes, parks and gardens, battlefields, artefacts and ecofacts") and FISH vocabularies; British National Grid; "Consultations module streamlines the casework and consultation process and integrates fully with the inventory data"; deployed by Historic England (GLHER Online — "archaeological sites, historic buildings, parks and landscapes, and heritage features"), East Sussex (Portico), Lincoln; developed with Historic England and the City of Lincoln.
- Deployment landscape (A — official implementations page, used as a broad cross-deployment sample):
  - National/provincial registries: England's National Marine Heritage Record (offshore heritage assets); British Columbia Register of Historic Places ("over 5,000 registered sites… officially recognized… for their heritage value… supports the provincial government's land use decisions"); Barbados National Registry of Historic Places ("official repository… heritage designation, through its community-based nomination procedure"); Jamaica National Inventory of Historic Places (maintained by the Jamaica National Heritage Trust; "public nominations of significant sites"); Coflein/RCAHMW Wales ("manage the geographical site index of the National Monuments Record of Wales… records archaeological and historical sites, monuments, buildings, landscapes").
  - City/county inventories: West Hollywood ("centralized inventory and management system for its cultural resources", populated from historic resource surveys; notes a "growing trend among California cities"); SF Cultural Heritage ("San Francisco's living cultural resources inventory", citywide survey); East Sussex HER (35,000+ records; "manage the historic environment… enabling informed decisions on planning applications"); GLHER Online (87,000+ entries).
  - Risk/condition-oriented research programs: EAMENA / MarEA ("documenting and assessing risks", "sustainable management of endangered maritime heritage"); MAEASaM (site inventories with national heritage authorities); MAPSS (endangerment assessment).
  - Monitoring/maintenance-flavored: Cantón Nabón, Ecuador ("heritage monitoring of the assets is being carried out in compliance with the preventive conservation cycle", via Arches Collector mobile); Kinmen Qionglin Settlement, Taiwan ("basic designated registrations, surveys, management-and-maintenances" under a "Cultural Heritage Lifecycle" concept).
  - Designation-list platforms: Málaga MALAKA.net ("inventory, locate and assist in its management… heritage included in official lists and catalogues of protection").
  - Adjacent re-uses (do NOT define this Type): Getty Provenance Index (provenance research records); Antwerp museums (museum collections managed in Arches — platform reuse for collection management); Arches for Science (heritage-science research data); Getty archival collections viewer.
- Numbers on Arches pages are implementation-specific claims; kept in Research Notes only.

## Product B — exeGesis HBSMR

### Key observations

- Positioning (A): "Software for Historic Environment Records… 75% of UK historic environment records are managed with our systems" (A for positioning; market-share number treated as vendor claim, not asserted further).
- Record classes (A, features page): "Records **Monuments, Events, Sources, Finds, Historic Landscape Character, Designations, Casework & Synthesis**". The documentation portal's user-guide index confirms the same classes as first-class modules: Monuments; Events/Activities; Sources/Archives; Finds; Consultations; HLC; Designations; Themes (A).
- Standards (A): indexed using Historic England **FISH/INSCRIPTION** terminologies; compliant with the **MIDAS Heritage** data standard.
- GIS (A): "Integrated digital mapping (GIS) using ArcGIS, MapInfo or QGIS" — mapping provided by integrated third-party GIS.
- Publication (A): "Data, maps and images published on the web with HBSMR-web or the HBSMR Gateway"; HBSMR Web doc-index sections: Search, Record Details, Maps, Registration, CMS & Blog, Forms & Surveys; API: MapServer, OData, Data Services.
- Consultations module (A): "Historic Environment Record services act as consultees and advisors to the planning process… All formal consultations need to be managed, documented and archived. A Consultation record details the stages of the consultation process, the actions undertaken and the resulting outcomes." Records organizations/individuals/agents as source; consultation types; log/target/completion dates; location, proposals, "multiple recommendations and outcomes"; consultations can be grouped; "fully integrated spatial recording… powerful 'Get from GIS' function that instantly identifies all Monuments within the consultation area"; images/docs via LibraryLink; "Data entry logged as part of HBSMR Audit Trail". "Normally used by casework officers and HER officers."
- Productivity & admin (A): Tasks, History, Bookmarks; Themes module "for interpreting HER data for research and outreach"; powerful filtering incl. spatial searching with the GIS module; extensive report generation and data export; SQL Server backend; hosted/SaaS options; customizable forms/queries/reports; user group + governance (roadmap, change log, questionnaires).
- Local Heritage List Platform (same vendor, A): cloud platform for local heritage designation lists — public interactive map + searchable list of entries and candidate sites (with National Heritage List for England overlay); registered public **submit candidate sites** (map location where possible, justification, fit with criteria, supporting images/documents), comment on candidates, track status of their submissions, receive decision notifications; staff **review and adjudicate** pending candidates in a dashboard, give feedback, "record the determination decisions on candidate sites, with justification", full audit trail of changes, cross-references to existing HER records, user-account control; planning departments consume the data "live" within planning and GIS applications via APIs (WMS/WFS); HER side "automatically accession new and changed Local Heritage List entries into the HER" (the word "accession" used loosely for automated ingest into the inventory — not object custody).
- Sourcing limitation: full HBSMR operational documentation is behind registration; only module names + vendor descriptions verified. No precise field/status/limits asserted.

## Product C — New York State CRIS

### Key observations

- Positioning (A): "Cultural Resource Information System… an advanced Geographic Information System program that provides access to New York State's vast historic and cultural resource databases and now digitized paper records."
- Content (A): "more than 1.5 million pages of digital images including National Register documents, building and archaeological inventory forms and survey reports" (CRIS's own claim; number kept here only).
- Programs served (A): "interactive portal for agencies, municipalities and others who use historic preservation programs, such as the State and Federal Income Tax Credits for Historic Properties, the State and National Registers of Historic Places Programs, the Sections 14.09 (NYSPRHPL) and 106 (NHPA) review processes, the Certified Local Government Program and building and archaeological survey programs."
- Access (A): NY.gov ID sign-in for "full functionality"; public legal-disclaimer gate; explicit statement that viewing material "does not constitute 'consultation' with the SHPO under section 106… or Section 14.09" — the system supports the statutory review processes but viewing it is not itself the consultation.
- Built and operated by the New York State Historic Preservation Office (SHPO) / Division for Historic Preservation, with federal funding.
- Interpretation: an agency-side realization of the same Type — inventory (building & archaeological inventory forms, National Register documents, survey reports) + spatial access + program/review linkage. No custody machinery anywhere in the description.

## Domain Reference — MIDAS Heritage (FISH)

- "British cultural heritage standard for recording information on buildings, monuments, archaeological sites, shipwrecks and submerged landscapes, parks and gardens, battlefields, artefacts and ecofacts" (A).
- "The data standard suggests the minimum level of information needed for recording heritage assets and covers the procedures involved in understanding, protecting and managing these assets." Used by "national government organizations, local authorities, heritage sector organizations, amenity groups and societies, the research community and professional contractors" (A).
- Six themes (A): 1. **Heritage Assets** (Areas, Monuments, Artefacts and ecofacts; Watercraft and Aircraft annexe); 2. **Activities** (investigative activities, designation and protection, **heritage asset management activities**, casework and consultations, research and analysis, historical events); 3. **Information Sources** (archive and bibliography, narrative and synthesis, management activity documentation); 4. **Spatial Information** (location, map depiction); 5. **Temporal Information** (dates and periods); 6. **Actor Information** (actor and role).
- Explicit scope exclusion (A): the standard "does not cover… how to record archives and museum collections" — standards-level confirmation of the boundary against collection management / archives.
- Dictionary: most information units are optional "depending on the purpose of your inventory" — supports treating the documentation layer as common, not invariant.
- History: first edition 1998 (RCHME) as "A Manual and Data Standard for Monument Inventories"; expanded 2007 — the Type's paper-era ancestry is explicitly "monument inventories" (useful for the historical check).

## Cross-product Comparison

| Dimension | Arches | HBSMR | NY CRIS | MIDAS Heritage (domain) |
|---|---|---|---|---|
| Object of record | configurable "resources"; heritage-inventory origin | Monuments (+ Events, Sources, Finds, HLC, Designations) | building & archaeological inventory forms; National Register documents | Heritage Assets: Areas, Monuments, Artefacts/ecofacts |
| Location anchoring | GIS-native (maps, geospatial search, Esri link) | integrated GIS (ArcGIS/MapInfo/QGIS) | "advanced GIS program" | Spatial Information theme (location, map depiction) |
| Heritage characterization | ontology/thesaurus-driven (CIDOC CRM, RDM/CLM) | FISH/INSCRIPTION terminologies; MIDAS-compliant | SHPO inventory forms/registers | typologies + dictionary units |
| Designation / status | present in deployments (registries, "official lists and catalogues of protection") | Designations record class | State & National Registers programs | Activities theme: "designation and protection" |
| Documentation layer | resource relationships (people, events, objects); media/IIIF | Events/Activities + Sources/Archives + Finds | digitized paper records, survey reports | Activities + Information Sources + Actor themes |
| Consultation/casework | Consultations module (Arches for HERs) | Consultations module (stages, actions, outcomes, "Get from GIS") | Section 106/14.09 review processes (portal role; viewing ≠ consultation) | Activities theme: "casework and consultations" |
| Condition / monitoring | deployment-level: preventive conservation monitoring (Nabón), risk assessment (EAMENA/MarEA, MAPSS), state/use of monuments (NHDP) | not visible in public materials | not visible in public materials | "heritage asset management activities" as an activity class |
| Public surface | public deployments (GLHER Online, BC Register, West Hollywood…) | HBSMR-web / Gateway (registration, CMS, maps) | public disclaimer + NY.gov-gated full access | — |
| Nomination / community entry | Barbados/Jamaica public nominations | via LHLP (vendor sibling) | not observed | — |
| Custody machinery (accession / storage locations / loans) | none (Antwerp museum reuse is adjacent) | none observed (Finds are records, not accessioned holdings) | none | explicitly out of scope |
| Controlled access & audit | granular permissions, provisional data, audit | audit trail; user groups; registered access | NY.gov ID; disclaimer gate | — |
| Legacy data ingestion | Bulk Data Manager (csv/json/shapefile) | vendor services; automated LHLP ingest into HER | "digitized paper records" | — |
| APIs / interoperability | API, linked data, Esri link | OData, MapServer, WMS/WFS (LHLP), Data Services | not confirmed from public pages | UK Gemini (GIS metadata), Dublin Core lineage |

Reading of the table:

- The object of record — a heritage asset at a location, characterized in heritage vocabulary — is common to all four sources (B/C evidence).
- The documentation layer around the asset (activities/events, sources, actors) is common to all four (B).
- Designation/protection status is common (B), though survey-only inventories without statutory status also exist (e.g., SF survey inventory).
- Consultation/casework appears in all three products, but always as a module/portal function beside the inventory, not the inventory itself (B, with C-level note that it is workflow machinery, not the defining structure).
- Condition/monitoring appears at deployment level within Arches and as an activity class in MIDAS, but is not evidenced in HBSMR/CRIS public materials → common-in-some, not definitional.
- Public surfaces, community nomination, and program portals vary widely → variant layer.

## Canonical Model (abstraction result)

### L0 — Defining Invariant (minimal)

A Cultural Heritage Asset Management application is a **standing registry of cultural heritage assets**, maintained over time by a custodial organization, where:

1. **Heritage asset record** — each asset (a place-based cultural resource: monument, building, site, area, landscape, structure, or comparable resource) is an individually identified, persistent record. The record — not an accessioned object under custody — is the unit of the system.
2. **Heritage characterization** — each record documents the resource in heritage-domain terms (what it is: form/type, period, description, and how it is known), using the sector's vocabularies rather than generic database attributes.
3. **Location anchoring** — each asset is anchored to a position/extent in geographic space (however realized: coordinates, geometry, map depiction, or a textual location in paper-era inventories).

Remove the record persistence/registry nature → a survey report; remove heritage characterization → a generic place/GIS dataset; remove location anchoring → a non-spatial catalog (drifts toward other Type families). Add per-object custody (accession, storage locations, loans) → it becomes a collection-management system instead.

### L1 — Common Mature Structure

Very common in mature modern products; not required for recognition:

- **Documentation layer around assets** — activity/event records (investigations, designation actions, management actions, casework), information-source/bibliographic records, and actor (person/organization) records linked to assets (MIDAS themes 2/3/6; HBSMR Events/Sources; Arches relationship graphs; CRIS survey reports).
- **Spatial visualization and spatial search** — map-first browsing, geospatial query, map layers/overlays (Arches, HBSMR, CRIS all map-centric).
- **Controlled vocabularies / thesauri** — terminology management governing data entry and search (FISH/INSCRIPTION; Arches RDM/CLM).
- **Designation / protection status** — recording whether an asset is officially recognized/listed/registered, and linkage to statutory registers (HBSMR Designations; CRIS Registers programs; BC/Barbados/Jamaica registries; MIDAS "designation and protection").
- **Search, reporting, export** — text + spatial + temporal search; statistical/reporting output; data export.
- **Controlled access, audit, review** — user/group permissions; audit trail of changes; provisional/unpublished data and review steps (Arches, HBSMR, CRIS sign-in).
- **Media & document attachments** — photographs, drawings, documents as managed representations (LibraryLink; Arches IIIF/media; CRIS digital images).
- **Public access surface** — a web publication of (part of) the inventory: search/browse maps and records (HBSMR-web/Gateway; GLHER Online; BC Register; CRIS public tier).

### L2 — Variant / Optional Structure

Depends on segment, jurisdiction, workflow, deployment:

- **Consultation / casework machinery** — managing planning-related enquiries and formal consultations as records with stages, actions, recommendations, outcomes, spatial scoping (HBSMR Consultations; Arches for HERs Consultations; CRIS review-process portal role). Strong in planning-linked deployments; absent in pure registries.
- **Nomination / community entry** — public submission of candidate sites with justification and media, staff adjudication, determination with justification, notification (LHLP; Barbados/Jamaica public nominations).
- **Condition / monitoring / risk** — recording condition, state, damage, or endangerment observations over time, including mobile field capture (Arches deployments: Nabón preventive-conservation monitoring, EAMENA/MarEA risk documentation, NHDP "current state and use"; MIDAS "heritage asset management activities"). Not evidenced as a first-class module in HBSMR/CRIS public materials.
- **Scope variants** — national registers vs local/county HERs vs city surveys vs thematic/project inventories (routes, archaeology, marine, endangered-heritage research); marine/underwater sub-domain; landscape characterization (HBSMR HLC — regional UK/European tradition).
- **Legacy-data ingestion emphasis** — digitizing paper records, bulk migration (CRIS; Arches Bulk Data Manager; East Sussex migration).
- **Program/portal extensions** — tax-credit programs, certified local government programs, planning-data APIs (CRIS; LHLP WMS/WFS).
- **Interoperability depth** — linked open data, ontologies (CIDOC CRM), GIS interop, OData/WMS/WFS feeds.
- **Mobile field collection** — survey apps feeding the inventory (Arches Collector; FlyMapper is a different exeGesis domain — not counted).

### L3 — Vendor-specific Structure (kept out of the final document)

- Arches: branch/graph resource-model configuration, tile-based data model, RDM/CLM, Arches Collector, Arches Esri Link, Timewheel, Project Status plugin, report manager, specific deployment branding (Portico, ARCADE, GLHER Online), named funded programs (Arcadia-funded EAMENA/MAEASaM/MAHSA/MAPSS family).
- HBSMR: Microsoft SQL Server backend, MapLink/LibraryLink companion products, HBSMR Gateway cost model, Themes module, Tasks/History/Bookmarks, OASIS questionnaire governance, user-group governance structure, "75% of UK HERs" claim.
- CRIS: NY.gov ID authentication, specific program bundle (tax credits, CLP), SAFETEA-LU funding origin, splash-page legal disclaimer mechanics.
- MIDAS: Watercraft and Aircraft annexe, e-GMS/Dublin-Cor compliance history.

## Historical / Market-Sample Check

- The MIDAS standard's own lineage (1998 "Manual and Data Standard for **Monument Inventories**", RCHME) points at the paper-era predecessors: national monument records, county Sites & Monuments Records, printed national inventories, register cards + base maps. These satisfy L0 (identified persistent records of heritage resources, characterized by type/period, located, maintained over time) while lacking GIS-native mapping, digital media, public web portals, and consultation modules. Therefore none of those belong in the definition.
- Regional check: the UK HER tradition (Monuments + Events + Sources + Designations + HLC) is one regional elaboration; North American SHPO inventories + National Register documents (CRIS), Caribbean/Canadian national registries (Barbados, Jamaica, BC), and research-driven endangered-heritage databases (EAMENA family) all fit L0 without UK-specific machinery (HLC, HER officers, FISH standards). So UK vocabulary must not leak into the definition.
- Platform check: Arches is also used for museum collections (Antwerp) and provenance data (Getty Provenance Index). Those are platform re-uses for *other* Application Types — evidence that the platform is generic, and that this Type must be defined by the record semantics (heritage asset registry, no custody), not by the software package.

## Vendor-specific Findings

See L3 above. Additional cautions:

- The "75% of UK HERs" figure is a single-vendor marketing claim; not generalized.
- "Consultations" naming and workflow shape differ across products (HBSMR Consultation record stages vs CRIS statutory review processes vs Arches workflow tooling); the common denominator is only "recorded casework linked spatially to the inventory".
- The word "accession" appears in the LHLP page for automated ingestion of list entries into the HER — a false friend vs collection-management accession; do not carry it into the final document.

## Boundary Findings

1. **vs Museum Collections Management / Archaeological Collection Management** — the load-bearing boundary. Collection management centers on accessioned physical objects under custody: numbering policy per object, hierarchical storage locations, movement/loan events, deaccession. Heritage asset management centers on place-based resources held as records; there is no custody chain because the system does not hold the asset. MIDAS Heritage explicitly excludes "how to record archives and museum collections". Test: if the system must answer "which shelf/tray is this object in and who may borrow it", it is collection management; if it answers "what is this place, where is it, what do we know and what is its status", it is this Type. Confirmed empirically: Arches (this Type's flagship) exhibits no custody machinery; when Antwerp used Arches for museum objects, that deployment became a collections-management use of the platform.
2. **vs Government GIS / Land Records / Cadastre** — those systems make parcels/geometry/administrative data the object of record; heritage asset management attaches heritage characterization, protection status, and documentation to the location. Spatial is a property of the heritage record, not the record itself. Test: strip heritage semantics → generic GIS dataset; the heritage record must survive as the unit.
3. **vs Digital Collection Portal / Public Data Portal** — portals are publication surfaces fed by a registry of record; this Type owns and maintains the registry itself (with publication as one common layer). Test: no editorial/curation power over the underlying records → portal.
4. **vs Building Asset Management / Building Condition Assessment (§17 family)** — those manage buildings as operational/financial assets of an owning organization (maintenance regimes, costs, facility condition). Heritage asset management manages heritage resources for protection and knowledge, for the public trust; condition there (where present) is conservation state, not facility maintenance. Test: cost-of-ownership/maintenance-work-order semantics → §17 family; heritage status/significance/documentation semantics → this Type.
5. **vs Archives Management System** — archives manage document collections as custody objects with finding aids; heritage inventories *reference* sources (bibliographic/archive links are part of the documentation layer) without managing the archive. Same "custody vs reference" test as #1.
6. **vs Provenance Research Platform** — provenance documents ownership history of art objects; this Type documents heritage places. Arches powers a provenance database (Getty Provenance Index) — an adjacent reuse, not this Type.
7. **vs Permit Management / Planning & Zoning Management** — heritage consultations feed planning processes, but permits/plan-control machinery belongs to planning systems; the heritage system acts as consultee/advisor (HBSMR Consultations framing; CRIS disclaimer that viewing ≠ consultation).
8. **Taxonomy note** — the leaf is a coherent, structurally distinct Type: shared family context with the §27 collection-management siblings but a different center of gravity (registry of place-based assets without custody). Consistent with the boundary confirmation recorded by the archaeological-collection-management pass.

## Uncertainties

- HBSMR operational internals (field-level behavior, exact status machines) unverifiable without registration; only module structure asserted.
- Condition/monitoring machinery could not be confirmed as a first-class capability in HBSMR/CRIS from public materials; wording in the final document stays qualified ("some products / deployments").
- The commercial market beyond Arches/HBSMR (other national vendors, e.g., in continental Europe) was not directly sampled; the claim that this Type is realized by "specialist vendors + open-source platform + agency-built systems" is a canonical inference (C-layer), not an exhaustive market census.
- Historic England's own HER guidance pages were unreachable; HER-practice details (e.g., exact consultation workflows in UK practice) rest on vendor pages + FISH/MIDAS only.
- CRIS's internal record classes are inferred from program descriptions (inventory forms, National Register documents) rather than a data dictionary.

## Final Synthesis

A Cultural Heritage Asset Management application is the registry-of-record software for cultural heritage assets: individually identified, persistent records of place-based heritage resources, characterized in heritage vocabulary and anchored to geographic location, maintained over time by the agency or organization responsible for them. Around that core, mature products add a documentation layer (activities/events, sources, actors), spatial visualization and search, controlled vocabularies, designation/protection status, search/reporting/export, permissioned access with audit, media attachments, and a public access surface. Common extensions are consultation/casework machinery for planning, public nomination workflows, condition/risk monitoring, mobile field capture, and legacy-data ingestion. The Type's negative definition is as important as its positive one: it holds no custody chain for accessioned objects — that seam separates it from museum and archaeological collection management, whose shared family space it occupies.
