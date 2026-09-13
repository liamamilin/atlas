# Research Notes — Research Data Management

## Research Goal

Understand, from real products, what a **Research Data Management (RDM)** application is: what unit it manages (dataset? plan? file? record?), what lifecycle it governs, who operates it, what governance machinery is definitional, and where its boundaries sit against the dense neighboring cluster — Institutional Repository (processed §23), Scientific Data Management System (processed §22), Research LIMS (processed §23), data management planning tools, generic data portals/catalogs, EDC, CRIS, and file storage.

This pass must discharge three inherited forward flags:

1. **institutional-repository** (§23, 2026-09-08): "Datasets are one work type within IR scope… Dedicated research-data-management adds data-specific machinery (metadata standards like domain schemas, data management plans, embargo/licensing depth). Boundary flagged for that leaf's own pass."
2. **scientific-data-management-system** (§22, 2026-09-09): "Seam = unit and scale of management: RDM governs an institution's research data at dataset/plan/repository grain (funder mandates, DMPs); SDMS operates lab/instrument-scale data files with capture machinery."
3. **research-lims** (§23, 2026-09-09): "institution-scale research data governance (datasets, data management plans, repositories, funder/mandate compliance) vs lab-scale specimen/workflow operations… A research LIMS feeds RDM; it does not govern institutional data compliance. Joint review recommended when processed."

## Initial Boundary

- Hypothesis: RDM is the **institution-scale stewardship layer** over research data — the dataset is the managed unit, moved through a governed lifecycle (plan → prepare/describe → preserve → make available under terms → reuse), with funder/policy compliance as the driving context.
- Nearest Types: Institutional Repository (output-publication posture; datasets one work type), SDMS (lab/instrument grain), Research LIMS (specimen/workflow grain), Data Catalog / data portals (catalog entries, no stewardship), DMP tools (planning fragment), EDC (trial capture instrument), CRIS (research information aggregation), file storage (substrate only).
- Unknowns: whether DMP machinery is definitional (historical check should decide); whether "repository/publication" is definitional or a posture variant (restricted data archives suggest variant); whether the Type is one market or a bundle of fragments (planning tools + repositories + catalogs).

## Research Questions

1. What is the unit of record in each product — dataset, item, record, plan?
2. What lifecycle states does the unit pass through, and which transitions are governed?
3. What planning machinery exists (DMP templates, funder requirements, guidance)?
4. What access/governance machinery exists (embargo, restriction, terms, licenses, request-access, guestbooks, retention)?
5. What identification/citation machinery (DOI, handles, versioned citations)?
6. What metadata machinery (required fields, domain schemas, export/harvesting)?
7. Who are the users and what are the interfaces (depositor, curator, admin, reuser)?
8. What rules are load-bearing (publish immutability, versioning semantics, no-deletion, tombstones)?
9. Where are the boundaries vs IR, SDMS, LIMS, DMP tools, data portals, EDC, CRIS, storage?
10. Does the definition survive the historical check (pre-web data archives)?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| **Figshare** (Digital Science) | Commercial SaaS institutional repository/RDM; "research outputs" generalist | Market-leading institutional pole; explicit RDM positioning; rich user guides |
| **Dataverse Project** (Harvard IQSS) | Open-source dataset-centric repository software | Deep official guides; dataset versioning/citation philosophy; self-hosted academic deployments |
| **Zenodo** (CERN, InvenioRDM) | Generalist open repository, community/self-serve pole | Record-centric counterweight; NIH DMS / Horizon Europe guidance; EU infrastructure |
| **DMPonline** (Digital Curation Centre) | Planning-only fragment (boundary probe) | Tests whether planning alone constitutes the Type |
| **CKAN** | Generic open-data portal (counter-sample) | Tests the catalog-vs-stewardship seam |
| **ICPSR** (Univ. of Michigan) | Historical anchor (social-science data archive consortium) | Historical/market-sample check |

## Sources

All fetched 2026-09-10 (evidence layer A unless noted):

- Figshare — https://info.figshare.com/ (root positioning); https://info.figshare.com/academic-institutions/ ; https://info.figshare.com/user-guides/ (guide index); https://info.figshare.com/user-guide/embargoes-and-restricted-access-publishing/ ; https://info.figshare.com/user-guide/how-to-write-a-data-management-plan-dmp-and-include-figshare-in-your-data-sharing-plans/ . Note: figshare.com root returned HTTP 403; info.figshare.com (official product site) used instead. support.figshare.com/support/solutions returned 404 — institutional admin operational detail not directly fetched.
- Dataverse — https://guides.dataverse.org/en/latest/user/ ; https://guides.dataverse.org/en/latest/quickstart/what-is-dataverse.html ; https://guides.dataverse.org/en/latest/user/dataset-management.html (full page incl. publish/review/embargo/retention/versions/deaccession sections).
- Zenodo — https://help.zenodo.org/ (help index); https://help.zenodo.org/docs/deposit/about-records/ .
- DMPonline — https://dmponline.dcc.ac.uk/ (home); https://dmponline.dcc.ac.uk/help .
- CKAN — https://ckan.org/ .
- ICPSR — https://www.icpsr.umich.edu/web/pages/about/index.html .

## Product Observations

### Figshare (evidence layer A)

- Positioning: "Figshare's repository solutions help researchers and organizations manage their research outputs in a discoverable, citable, reportable and transparent way." Four pillars: Share / Showcase / Manage / Track. "A Digital Science solution. FAIR-compliant repository infrastructure."
- Serves: academic institutions, government/funders/nonprofits, publishers, pharmaceutical organizations, individual researchers (free repository).
- Institutional page: "used by academic institutions all over the world both as an **institutional repository** and **data repository solution**." Store/manage research outputs of any type; comply with funder and publisher open access policies (OSTP, NIH, UKRI, ARC named); restricted access and embargo functionality; flexible license options (CC-BY, CC0, CC-BY-SA, CC-BY-NA…); 1200+ file types previewed in browser; configurable custom metadata per repository group; "powerful administration capabilities for managing submissions, users and storage allocations"; integrations with ELNs, CRIS/RIMS; CoreTrustSeal certification achieved by licensing institutions; metrics (views, downloads, Altmetric, Dimensions citations); persistent identifiers.
- Embargo article (operational): embargo = "publish your research in a controlled way. Typically, the files are embargoed and remain private to you, while the metadata is findable to the world." Reasons: ethically/commercially sensitive data; no permission yet (research unpublished); data stored elsewhere but want a DOI. Mechanics: embargo period selection (expires at a set date; "permanent embargo" available for files only); embargo type = files only or entire content; visibility options — Nobody / Administration (institution-authorized users) / Custom (institution groups and/or IP ranges); embargo title + optional public reason; institution-configurable **request access** option (requests emailed to owner + institutional admins; requester must log in). Best-practice warning: "Please don't embargo files by default!"
- DMP article (operational): DMP context — funders requiring DMPs (NSF, NIH DMS policy, ERC, CIHR, SNSF, UK MRC/ESRC, NHMRC, Wellcome, Gates…); "a DMP asks the researcher to consider how data and associated products of research such as code or other files, will be handled across the life span of a project and beyond… how the data will be stored, secured, accessed, documented, formatted, and versioned… where and when data will be shared… how it will be licensed for reuse, and how and for how long data will be archived"; human-subjects ethics/consent/de-identification; institutional support from data librarians; DMPTool and DMPonline named as planning tools; Re3data (2000+ repositories) for repository choice.
- Compliance/persistence claims: DataCite DOI per published item; "does not allow deletion of content"; backups via Chronopolis and Duracloud; "maintained… for the life of the repository and for a minimum of 10 years"; metadata per community standards incl. machine-readable license + funding sources; indexing (Google Dataset Search, Google Scholar by item type, Dimensions); views/downloads/Altmetric/citations tracked; 20GB storage/file on standard tier; FTP uploader + open API; Figshare Plus for TB-scale (up to 5TB/file, one-time cost); TRUST principles + FAIR + ISO27001.
- User-guide structure (index): Getting started (incl. DMP guide, retention FAQ); account management; uploading/managing files (non-logged-in institutional submit pages, FTPS/API bulk, file size limits); metadata (reserve a DOI, private links, choose a licence, item types, geospatial metadata); publishing (embargoes, versioning, unpublishing advice); projects and collections; discoverability/indexing; search/share/reuse; API + OAI-PMH; policies; integrations (GitHub/GitLab/Bitbucket, ORCID); **data sharing policy compliance** (OSTP/NIH desirable characteristics, US funder guide); Figshare Plus; FAQs (FAIR alignment, TRUST, metadata schema, usage metrics, categories, security/ISO27001).

### Dataverse (evidence layer A)

- Definition: "Dataverse is an open source web application for sharing, preserving, citing, exploring, and analyzing research data." A repository hosts **collections** ("dataverses") which organize **datasets**; a dataset = "a container for your data, documentation, code, and the metadata describing this Dataset."
- Core capabilities (quickstart): upload/manage/publish/download data files (directory structure retained; collaborators invited before publication); "Control access with permissions, configurations, licenses, file restrictions, and guestbooks"; publish with rich metadata, licensing, versioning "to make data FAIR"; download with clear terms of use and cite using provided citation options; rich metadata before publication with optional **domain-specific metadata blocks**; metadata harvesting/distribution (e.g., Google Dataset Search); standardized licenses or custom terms; versioning (major/minor, per-version access and citation, version-diff comparison).
- Dataset lifecycle (dataset-management guide): create dataset (required fields → data citation with DOI); file upload (HTTP/Dropbox/folder/DVUploader CLI; MD5 checksum per file; UNF for tabular); **Restricted Files** + Terms of Access; **Guestbook** (collects user info at download); dataset-level and file-level **roles & permissions**; **Submit for Review** (contributor → curator/admin; publish or "Return to Author"); **Publish** (public; "once a dataset is made public it can no longer be unpublished"; file validation before finalize); **Embargoes** (file-level, instance-configured; content inaccessible until end date, auto-expires; reason optional/required; "rolling" embargoes via successive versions; embargo immutable after publish except admin correction); **Retention Periods** (file content inaccessible after end date, for legal requirements; destruction not automatic); **Dataset Versions** (draft on edit; major/minor; version table + differences); **Dataset Deaccession** (serious action; reason required; tombstone landing page with citation metadata always remains at the persistent URL); dataset types (review datasets etc.).
- Metadata: three levels — citation metadata; domain-specific blocks (Social Science, Life Science, Geospatial, Astronomy); file-level metadata. Export formats: Dublin Core, DDI Codebook 2.5, DataCite 4, OAI_ORE, OpenAIRE, schema.org JSON-LD, Croissant (+ RO-Crate via external exporters). One persistent identifier (DOI or Handle) per dataset, not per version.
- Metrics: download counts aggregated dataset/file level; Make Data Count (views, downloads, citations via Crossref/DataCite).
- Admin surface: metadata customization, harvesting clients/servers, IP groups, mail-domain groups, storage quotas per collection, Solr search index, backups, rate limiting.
- Platform: self-hosted open-source (installation guide, containers, Shibboleth/OAuth/OIDC/ORCID, LocalContexts integration).

### Zenodo (evidence layer A)

- Positioning: generalist open repository built on **InvenioRDM**, funded by CERN/OpenAIRE/EU. "Records are the basic entities used to share and preserve a digital research object (datasets, publications, software, poster, presentations etc) on Zenodo. Any user… can create a new record."
- Record = metadata + files + persistent identifier (DOI registered with DataCite on publish; existing DOIs can be brought). Minimal required metadata (citation fields), export to many standards.
- Lifecycle: draft → publish → record. After publish: "Metadata CAN be modified; Files and the persistent identifier CANNOT be modified" — archiving best practice; citing researchers must be able to rely on immutability. **Versions**: "a completely new record with separate metadata, files and persistent identifier" — version citations are stable.
- Access: metadata always public; files can be restricted at deposit or later; share with specific people (user sharing, link sharing); **access requests**; restricted access rationale: "embargoed content, content under peer-review, content that cannot be made generally available (e.g. anonymized clinical trial data)".
- Communities: create/join; submit for review to community; community curators review submissions; curation surfaces.
- Policy guidance surfaces: NIH **Data Management and Sharing Plan** guidance (element-by-element pages), Horizon Europe guidance (EU Open Research Repository), GitHub integration for software archiving.
- Preservation: "we only guarantee bit-level preservation"; preservation-friendly format guidance.

### DMPonline (evidence layer A — planning fragment)

- Positioning: "DMPonline helps you to create, review, and share data management plans that meet institutional and funder requirements. It is provided by the Digital Curation Centre (DCC)." Scale claims: 184,041 users / 820 organisations / 209,508 plans / 89 countries (vendor stats).
- Structure: Public DMPs (published plans library); Funder requirements (public templates — UK research councils etc.; US counterparts via DMPTool); institutional sign-in via Shibboleth; open source (DMPRoadmap/roadmap).
- Help: "provides tailored guidance and example answers to help researchers develop data management plans"; separate user/administrator help; partner-enabled "basic and enhanced customisations" (institutional branding/guidance); DCC Checklist for a DMP (13 questions) as generic template; example DMPs; links to general RDM training (MANTRA, UK Data Service guides, DCC how-to guides on citing datasets, licensing data, appraising/selecting data for curation).
- **No dataset management whatsoever**: the managed object is the plan document. No repository, no files of record, no access machinery over data. → planning-only fragment.

### CKAN (evidence layer A — counter-sample)

- Positioning: "The world's leading open source data management system… an open-source DMS (data management system) for powering data hubs and data portals. CKAN makes it easy to publish, share and use data." Powers government open-data portals (data.gov, Canada, Australia, Singapore…) and enterprise internal data assets.
- Catalog-shaped: datasets as portal entries for publication/discovery; no research-data lifecycle machinery observed on the official site (no DMP linkage, no preservation commitments, no scholarly citation/versioning semantics, no funder-policy compliance surfaces). → generic data-portal Type, not RDM.

### ICPSR (evidence layer A — historical anchor)

- "ICPSR is an international consortium of 800+ academic and research bodies. We provide leadership and training in data access, curation, and analytical methods for social science." 400,000+ research files; 25+ specialized data collections; 120,000+ data-related publications (citation database linking publications to held data). Summer Program established 1963 (consortium dates to the founding generation of the social-science data archive movement).
- Operational structure on the live site: **Share & Manage Data** — Preparing for Deposit → Deposit Your Data → **Data Management Plans & Grant Support** → Support & Resources; Find Data (search, variable-level search & compare, data-related publications); membership model; policies & certifications; repository operations.
- Fits the stewardship model with pre-web machinery: accession-numbered holdings, curated deposits, membership-governed access incl. restricted-use data, long-term preservation, publication linkage. No DOI-era machinery required.

## Cross-product Comparison

| Aspect | Figshare | Dataverse | Zenodo | DMPonline | CKAN (counter) | ICPSR (historical) |
|---|---|---|---|---|---|---|
| Unit of record | item (dataset/figure/paper/any output) | dataset (files+docs+code+metadata) in collections | record (any research object) | plan (DMP document) | dataset (portal catalog entry) | curated study/files (accession-numbered) |
| Persistent identity | DataCite DOI per item | DOI/Handle per dataset (one per dataset, not per version) | DOI per record; version = new record/DOI | none | not verified | accession numbers (pre-DOI era) |
| Lifecycle | private → (institutional review) → published; versioning; embargo; restricted | draft → submit for review → publish (irreversible) → versions → deaccession (tombstone) | draft → publish (files immutable) → new version = new record | draft → complete → optionally public | publish to portal | deposit → curation → access/reuse |
| Access governance | embargo (period/permanent; nobody/admin/custom incl. IP ranges), restricted access, request access, private links | restricted files + terms of access, guestbook, file-level embargo (auto-expire), retention periods, dataset/file roles | restricted files, access requests, user/link sharing, community review | n/a (plans only) | portal permissions | membership + restricted-use contracts |
| Metadata | required fields per community standards; license mandatory; funding sources; categories; geospatial | citation + domain blocks (soc-sci/life-sci/geospatial/astronomy) + file-level; exports DDI/DataCite/DC/OAI-ORE/OpenAIRE/schema.org/Croissant | minimal citation metadata; many export standards | funder templates; DCC 13-question checklist; guidance/example answers | resource metadata | curated social-science documentation (DDI lineage) |
| Preservation | no deletion; Chronopolis/Duracloud backups; min 10 years claim | file validation at publish; versioning; deaccession tombstone | bit-level preservation guarantee; files immutable | n/a | n/a | long-term archive mandate |
| Policy/compliance | funder/publisher OA policy compliance; DMP guidance; US funder guide | FAIR; metadata exports for harvesters | NIH DMS element guidance; Horizon Europe guidance | funder requirement templates (UK/US) | government open-data policy | funder/grant support incl. DMPs (modern layer) |
| Users | researchers, institutional admins/library, funders, publishers, pharma | researchers, curators, collection admins, installation admins | any researcher (self-serve), community curators | researchers, institutional DMP admins, funders | data publishers, portal operators | members, depositors, researchers |
| Citation/metrics | DOI citable; views/downloads/Altmetric/citations | data citation w/ version; Make Data Count | DOI citation; usage statistics | n/a | n/a | data-related publications database |

**Cross-product commonalities (layer B):** across Figshare, Dataverse, Zenodo (and ICPSR historically): (1) a persistent, identified, described dataset/record as the managed unit; (2) a governed draft→published lifecycle with an irreversible publication commitment; (3) controlled availability — open by default, restricted/embargoed as managed exceptions; (4) versioning of published data; (5) preservation posture (immutability/no-deletion/bit preservation); (6) discovery machinery (search, metadata export/harvesting into scholarly discovery layers); (7) usage/citation tracking. DMP linkage appears in Figshare (guidance + compliance framing), Zenodo (NIH DMS guidance), ICPSR (DMP & grant support), and as the entire product in DMPonline — common mature machinery, not definitional (ICPSR predates it).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Two jointly-held structures:

1. **The research dataset as the managed unit of record** — a persistent, identified, described bundle of research data (data files + documentation + metadata) bound to a research context (project/study/depositor/funder), held as a record that outlives the project and remains addressable and citable. Remove → a file store, a document archive, or a catalog with no data of record.
2. **Stewardship governance over the dataset's availability lifecycle** — the dataset moves through managed states (prepared/deposited → described/curated → preserved → made available under defined terms or held under control → reused/reported), with access rules attached (who may access, under what license/terms, embargo/restriction), versioned changes, and accountable closure (deaccession with reason; tombstone). Remove → storage or a listing with no stewardship loop.

Jointly-held is load-bearing: 1 alone = file store/repository shell; 2 alone = a policy document with nothing governed; the pair = the institution's research-data system of record.

### L1 — Common Mature Structure

- Data management planning: DMP templates per funder, guidance/example answers, plan lifecycle, institutional customization (DMPonline as pure form; Figshare/Zenodo/ICPSR as guidance + compliance framing)
- Persistent identifiers (DOI/handle) + machine-actionable data citation
- Rich structured metadata with domain-specific schemas/blocks (DDI, DataCite, geospatial, astronomy…) and metadata export/harvesting (OAI-PMH, schema.org, OpenAIRE, Croissant)
- Versioning of published datasets (major/minor; or new-version records)
- Access machinery: embargo (time-based auto-expiry; permanent variant), restricted files + terms of access, request-access workflows, guestbooks/download terms
- Licensing (standard CC suite; custom terms)
- Review/approval workflow before publication (curator/institutional review)
- Discovery surfaces + indexing into scholarly discovery layers (Google Dataset Search, Dimensions, OpenAIRE)
- Usage metrics (views/downloads/citations; Make Data Count)
- Preservation commitments (bit preservation, backups, retention minimums, no-deletion)
- Administration: submissions/users/storage quotas; bulk upload (FTP/API); integrations (ORCID, GitHub, CRIS/RIM, ELN)

### L2 — Variant / Optional Structure

- Scope posture: data-only vs all research outputs (generalist repositories)
- Openness posture: open-by-default vs restricted-archive (ICPSR restricted-use; secure enclaves)
- Deployment: SaaS vs self-hosted open-source installations vs consortium-operated archives
- Community/collection organization (Dataverse collections, Zenodo communities, Figshare groups)
- Domain specialization depth (social science DDI, astronomy FITS, geospatial)
- Big-data support (TB-scale tiers, Globus/cloud compute)
- Planning-only fragment as standalone product (DMPonline/DMP Tool)
- Funder-policy guidance depth (NIH DMS element-by-element)

### L3 — Vendor-specific (research notes only)

- Figshare: Altmetric/Dimensions integration, Chronopolis/Duracloud backups, 20GB standard limits, Figshare Plus pricing (5TB/file), non-logged-in institutional submit pages, ISO27001, CoreTrustSeal via licensees, embargo expiry at 00:10 UTC, "minimum 10 years" retention claim.
- Dataverse: UNF fingerprints for tabular data, Solr index, guestbook mechanics, IP groups/mail-domain groups, DVUploader, BagIt support, deaccession reason dropdown, preview URLs (incl. anonymized), LocalContexts integration, storage via Swift/S3.
- Zenodo: GitHub integration, InvenioRDM base, EU/OpenAIRE funding, communities curation queues, quota management.
- DMPonline: DCC 13-question checklist, ED wiki help pages, partner customisation tiers, Shibboleth, DMPRoadmap codebase, vendor stats (184k users/820 orgs/209k plans/89 countries).
- ICPSR: membership consortium model, Summer Program, variable-level search, 400k+ files scale claims.

## Vendor-specific Findings

See L3. Nothing above promoted to the canonical core. Figshare's "institutional repository AND data repository solution" self-description is the clearest spanning-product evidence for the IR seam.

## Boundary Findings

**vs Institutional Repository (discharges flag from institutional-repository, 2026-09-08) — keep-both RATIFIED from this side.**
The IR pass held: datasets are one work type in IR; dedicated RDM adds data-specific machinery. Confirmed and sharpened with fresh evidence: Figshare — the market's flagship "RDM" product — self-describes as "institutional repository and data repository solution" (spanning product, like DSpace spanning IR/DLP). The seam is the center of gravity: IR is the institution's scholarly-output collection of record with an open-access delivery posture (works produced by the institution's people); RDM is stewardship over the dataset lifecycle — planning linkage, domain metadata schemas, embargo/licensing/retention depth, preservation commitments, versioned data citation. A dataset deposited in an IR is one output among papers/theses; a dataset in RDM is the primary governed object. Spanning products do not merge Types. Keep-both.

**vs Scientific Data Management System (discharges flag from scientific-data-management-system, 2026-09-09) — keep-both RATIFIED from this side.**
Seam = unit and scale of management, exactly as that pass predicted: SDMS operates lab/instrument-scale data files with capture machinery (watched instrument outputs, adaptors); RDM governs institution-scale datasets/plans/repositories under funder mandates. No capture machinery exists in any sampled RDM product; no funder-policy/DMP machinery exists in any sampled SDMS. The SDMS pass's own "structured file management, rich metadata, policy-driven retention" essay describes the lab grain. Keep-both.

**vs Research LIMS (discharges flag from research-lims, 2026-09-09) — keep-both RATIFIED from this side.**
Seam = unit of management: physical specimens and their processing (LIMS) vs datasets and data outputs (RDM). The LIMS pass's own line — "A research LIMS feeds RDM; it does not govern institutional data compliance" — is confirmed: none of the sampled RDM products manage specimens or lab workflows; the RDM products' integrations treat ELN/LIMS as upstream sources. Keep-both.

**vs Data Management Planning tools (DMPonline / DMP Tool) — capability-of-Type, not a separate Type.**
A planning-only tool manages plan documents, not datasets: no unit of data record, no availability lifecycle, no preservation. It is the planning fragment of the RDM lifecycle sold standalone (DMPonline: 209k plans, zero datasets). The RDM leaf absorbs it as a variant/fragment; no directory change proposed. If maintainers ever want a separate leaf for planning tools, the seam is clean (plan document vs dataset of record).

**vs generic data portals / Data Catalog (CKAN; §13 Data Catalog) — different Types.**
CKAN powers government open-data portals: datasets as catalog entries for publication/discovery, portal-level permissions, no research-data lifecycle (no DMP linkage, no preservation commitments, no scholarly citation/versioning semantics, no embargo/restriction machinery observed). A data catalog describes data that lives elsewhere; RDM holds and governs the data of record. The word "dataset" appears in both; the stewardship loop does not.

**vs Electronic Data Capture / Clinical Data Management (§22, processed) — clean.**
EDC is the trial-specific capture instrument (eCRFs, site entry, edit checks); CDM is the cleaning discipline over trial data. RDM is institution-wide stewardship of research data across projects. Zenodo's restricted-access rationale even names "anonymized clinical trial data" as content that lands in repositories after capture/cleaning — downstream of EDC/CDM.

**vs Research Information Management / CRIS — adjacent, aggregation vs stewardship.**
CRIS aggregates research information (publications, grants, datasets as metadata records); RDM holds and governs the data itself. Figshare's CRIS/RIM integrations (incl. Symplectic Elements pairing) show the handoff: CRIS feeds metadata/context; the repository holds the data of record.

**vs file storage / sync (§03.15) — substrate, not the Type.**
Storage is a configurable substrate in every sampled product (Dataverse local/Swift/S3; Figshare AWS; Zenodo CERN data centre). Remove the governance and only storage remains; remove storage and the stewardship model still describes the product (records can be metadata-only with external data links — Figshare explicitly supports "publish without uploading files" / "data stored somewhere else, but you want to link to it to get a DOI").

**vs Research Grant Management — planning linkage only.**
DMPs attach to grants and funder requirements, but the managed object differs (money/milestones vs data). No sampled RDM product manages grant finances.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit?

- **ICPSR** (founding generation of the social-science data archive movement; Summer Program since 1963): curated deposits, accession-numbered holdings, membership-governed access incl. restricted-use data, long-term preservation, publication linkage — satisfies both L0 legs with zero modern machinery (no DOI, no DMP, no web UI). ✓
- **UK Data Archive / DANS-class national archives** (regional poles): same archive shape — deposit, curation, controlled access, preservation. ✓ (positioning-level evidence; not product-fetched this pass)
- **DMP machinery is modern** (funder mandates of the 2000s–2010s; Figshare's own DMP article dates the NIH DMS policy to January 2023): therefore DMPs cannot be definitional — held at L1. ✓
- **DOI-era identification is an implementation**: ICPSR's accession numbers predate DOIs; the invariant is stable addressable identity, not the DOI specifically. ✓
- **Open-by-default is a posture, not the definition**: ICPSR runs restricted-use data; Dataverse/Figshare/Zenodo treat restriction/embargo as managed exceptions. The invariant is governed availability, not openness. ✓

The definition survives the historical check.

## Uncertainties

- Figshare's institutional admin approval workflow could not be fetched directly (support site 404; figshare.com root 403). The institutional page's "administration capabilities for managing submissions, users and storage allocations" is A-layer from the official product page, but queue-level mechanics are unverified — held at common-mature, not definitional.
- Whether every RDM product carries preservation commitments: DMPonline has none (fragment); among repository products all sampled carry some preservation posture. Held common-mature, not definitional.
- CKAN DOI/versioning plugins were not verified; no claims made about CKAN beyond its official positioning.
- The market uses "RDM" loosely (sometimes meaning the practice, sometimes planning tools, sometimes repositories). This pass defines the software Type by the stewardship system of record; vendor marketing that uses "RDM" for planning-only tools is recorded as the fragment reading.
- Dataverse embargo/retention are instance-configurable features; depth varies by installation — held as common machinery with configurable depth.
- ICPSR/UK Data Archive used as historical anchors from official about-pages only; no operational workflow detail fetched for UK Data Archive.

## Final Synthesis

A **Research Data Management application** is the research institution's research-data stewardship system of record. Its defining core is two jointly-held structures: the **research dataset as the managed unit of record** (a persistent, identified, described bundle of data files, documentation and metadata bound to a research context, held beyond the project's life) and **stewardship governance over the dataset's availability lifecycle** (plan → prepare/describe → review → preserve → make available under defined terms or hold under control → reuse/report, with embargo/restriction/licensing/versioning and accountable closure). Around this core, mature products add data management planning machinery, DOI-based citation, domain metadata schemas, review workflows, discovery/metrics, preservation commitments, and administrative machinery. The Type is deliberately defined above any single era's implementation: the pre-DOI data archive satisfies it with accession numbers and membership contracts; the modern SaaS repository satisfies it with DOIs, DMPs and Make Data Count metrics. The three inherited flags are discharged: keep-both vs Institutional Repository (output-collection vs data-stewardship center of gravity), keep-both vs SDMS (lab/instrument grain vs institution grain), keep-both vs Research LIMS (specimens vs datasets). Planning-only tools and generic data portals are recorded as fragment and counter-Type respectively.
