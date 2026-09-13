# Research Notes — Research Information Management / CRIS

Research date: 2026-09-09
Slug: research-information-management-cris
Directory leaf: Research Information Management / CRIS (§23 Education, Research & Knowledge Institutions)

## Research Goal

Understand, from real products, what a Research Information Management system (RIM/RIMS, also called a Current Research Information System, CRIS) is: its core objects, how records enter and are maintained, what the system is consumed for, and where its boundary lies against neighboring Types (Institutional Repository, Research Administration Platform / Research Grant Management, Bibliometrics Platform, Reference Manager, Academic Search Engine, Research Data Management).

## Initial Boundary

Initial hypothesis before research:

- A CRIS is the research institution's system of record for its research activity: researchers, outputs (publications and other research products), projects, funding, organizational units — linked, maintained through a combination of external-source ingestion and institutional curation, and consumed as profiles, portals, reports, and compliance outputs.
- Nearest neighbors: Institutional Repository (open-access archive), Research Administration Platform (grant lifecycle), Bibliometrics Platform, Reference Manager, Academic Search Engine.
- Open questions: whether harvesting is definitional; whether the repository is part of the Type; whether funding is a linked record or a grants-administration object; whether the public portal is definitional.

## Research Questions

1. What are the core objects? (person/researcher, output, project, funding, organizational unit, and extended types)
2. How do records enter the system? (external databases, institutional systems, researcher deposits, manual entry)
3. How are records attributed to researchers? (identifiers, name matching, claiming, approval)
4. What validation/curation workflows exist before records become authoritative?
5. What consumption surfaces exist? (profiles, public portal, reporting, assessment exercises, OA compliance, CVs, exports)
6. How does funding appear — as linked records or as grants administration?
7. What is the relationship to the institutional repository?
8. Who are the users and how do their roles differ?
9. Where is the boundary against Institutional Repository, Research Administration, Bibliometrics, Reference Manager, Academic Search Engine?
10. Do older/regional/open-source products fit the same definition (historical/market-sample check)?

## Representative Products

| Product | Vendor | Why selected |
|---|---|---|
| Pure | Elsevier | Market-leading commercial RIMS/CRIS; self-labels both terms; broadest module set |
| Symplectic Elements | Digital Science (Symplectic) | UK-origin strong second; assessment/OA-heavy philosophy; deep public support documentation |
| Esploro | Ex Libris (Clarivate) | Library-vendor lineage; repository-adjacent philosophy ("beyond the repository"); full online help accessible |
| VIVO | open-source community (LYRASIS) | Open-source pole; profiles/networking-first philosophy; semantic-web data model |

Worktribe was initially considered as a smaller-institution all-in-one pole but its site returned 403 on two attempts; it was dropped per the source-access limitation rule and replaced by VIVO.

## Sources

Tier 2 (official product pages):

- Elsevier — Pure product page: https://www.elsevier.com/products/pure (fetched 2026-09-09)
- Elsevier — Pure "How it works": https://www.elsevier.com/products/pure/how-it-works (fetched 2026-09-09)
- Symplectic — Elements product page: https://www.symplectic.co.uk/products/elements (fetched 2026-09-09)
- Symplectic — "What is Research Information Management?": https://www.symplectic.co.uk/research-management-using-the-elements-platform/ (fetched 2026-09-09)
- Ex Libris — Esploro product page: https://www.exlibrisgroup.com/products/esploro/ (fetched 2026-09-09)

Tier 1 (official operational documentation):

- Ex Libris Knowledge Center — Esploro Online Help (English), index + Esploro Overview + Claiming Outputs from Smart Harvesting: https://knowledge.exlibrisgroup.com/Esploro/Product_Documentation/Esploro_Online_Help_(English) (fetched 2026-09-09)
- Symplectic Support — Elements category index + Getting Started + "Automatic claiming in Elements": https://support.symplectic.co.uk/en/articles/11299457 (fetched 2026-09-09)

Type-level / community sources:

- euroCRIS — Main features of CERIF: https://eurocris.org/services/main-features-cerif/ (fetched 2026-09-09)
- euroCRIS home (DRIS, CRIS conference): https://www.eurocris.org/ (fetched 2026-09-09)
- VIVO — home: https://vivoweb.org/ (fetched 2026-09-09)
- OCLC Research + euroCRIS RIM definition and survey, as quoted on the Symplectic RIM page (secondary quotation; original report not fetched)

Failed sources (recorded per source-access limitation):

- https://www.worktribe.com/ and /products — 403 twice; dropped
- https://www.exlibrisgroup.com/products/esploro-research-services/ — 404; succeeded via /products/esploro/
- https://www.vivow.org/ — unpublished Dynadot error page; succeeded via vivoweb.org
- Pure's operational help center was not reached; Pure evidence is Tier-2 (product/how-it-works pages) plus its own FAQ definitions

## Product Observations

### Pure (Elsevier) — evidence layer A unless noted

- Self-labels: "a Research Information Management System (RIMS) also known as a CRIS"; FAQ defines a RIMS as "a centralized platform that helps universities and research institutions collect, manage, and make use of their research data… aggregates information from multiple sources — HR, finance, publication databases, and more — into a single authoritative system."
- Centralized objects named: "publications, funding, people, projects, and impact — into a single source of truth."
- Synchronizes automatically with Scopus, ORCID, national CRIS registers, and institutional HR and finance systems.
- Data quality machinery (how-it-works FAQ): "automated de-duplication, source prioritization and workflow-driven validation"; duplicate records identified and merged "using persistent identifiers such as DOI, ORCID and Scopus Author ID"; institutions "configure trusted sources and quality thresholds to determine what is accepted automatically versus routed for human review"; "Role-based validation workflows then allow editors and administrators to review, approve and enrich records before they are published or included in reports."
- Standards: "Built on international standards such as CERIF and Dublin Core"; ISO 27001 mentioned.
- Modules (how-it-works): Core ("research outputs, funding, researchers and organizational data"), Portal ("showcase validated research publicly"), Community (cross-institution sharing), Award Management ("full grant lifecycle… from application to award"), CV (auto-generate standardized CVs from validated data), Reporting, National Assessment (REF, SEP/KUOZ).
- Users named: research offices, librarians, leaders. Institutions named: research-intensive universities, national research institutes, government research bodies, funders; also a hospital network and a federal agency program (product-page examples).
- Compliance framing: open access mandates, national assessments (REF UK, SEP/KUOZ Netherlands), funder reporting.
- Pure Portal: "ready-made, search-optimized showcase."

### Symplectic Elements (Digital Science) — evidence layer A unless noted

- Self-labels: "a highly-configurable research management system which ingests data from multiple sources to build a truly comprehensive picture of your organizational data"; footer: "A research information management system that builds a comprehensive picture of scholarly activity."
- "Goes beyond traditional RIM": research funding and awards management, equipment and technology profiles, assessment exercises.
- Data sources table (product page): publications from arXiv, CiNii, Crossref, DBLP, Europe-PMC, Figshare, Google Books, MLA, ORCID, RePEc, SSRN, Scopus, Web of Science, PubMed; publications & grants from Dimensions; plus Altmetric (metrics); capabilities per source: automated search, automatic claiming, auto-link publications & grants, research metrics, full-text links.
- Support-site structure (Tier-1): Awards Management (11 categories / 98 articles), Repository Tools and OA Monitor (39), Discovery Module (public profiles, 14), Evaluation and Review (37), Reporting Database (15), Reporting Hub (19), REF (11 categories / 52 articles), Elements API, On-Premises Hosting, AI features.
- "Automatic claiming in Elements" (Tier-1 article): researcher identifiers include arXiv Author ID, Dimensions Researcher ID, figshare accounts, ORCID iD, Web of Science ResearcherID, Scopus ID, SSRN Author ID, email addresses. Identifier dispositions: auto claim items / auto suggest items (→ Pending) / auto reject items / ignore. Name-based search settings (name variants, addresses) as the complementary matching mechanism; false-positive management (name collisions, diacritics) documented in FAQ; ORCID claiming vs authenticated connection distinguished; curators process pending publications and grants.
- Public profiles (Discovery Module): biographies, publications, grants, teaching activities, patents, equipment, facilities, research groups; branded, mobile-friendly, searchable.
- Assessment: out-of-the-box workflows for REF and PBRF; internal workflows: publication approvals, conference attendance requests, promotion rounds; Annual Collection module for faculty annual reviews with data reuse ("Where Elements already knows key information about the individual… it will not ask the faculty member to supply this information").
- Open access: deposit prompts guiding researchers "to deposit the right version", compliance dashboards, repository integration (DSpace, EPrints, Figshare named on the RIM page), exceptions recording.
- Impact tracking: qualitative/quantitative impact records linked to outputs, grants, engagement activities ("Records of Impact" quick-start guide).
- Reporting Hub: configurable dashboards; "specialist SQL-based reporting database, enabling direct querying, integration with BI tools like Tableau or Power BI."
- Privacy: "item-by-item control of information held within the platform" by administrators or researchers.
- Users named: research officers and librarians.

### Esploro (Ex Libris / Clarivate) — evidence layer A unless noted

- Self-labels: "The Esploro research information management solution"; page title "Research Management System : Esploro"; positions itself as "move beyond the traditional repository."
- Research Information Hub: "Capturing multiple types of scholarly information, activities and entities in one place, and linking everything." Showcases "publications, preprints, datasets, creative works, awarded grants, projects, and media mentions."
- Acquisition: "Data is captured automatically from various virtual sources or semi-automatically via deposits by researchers, librarians, or assistants." Smart Harvesting AI "matches scholars with their research work."
- Researcher profiles: "Auto-generating and updating researcher profiles with publications, expertise, affiliations, awarded grants, identifiers and media mentions"; share to Google Scholar and ORCID; SEO emphasis.
- Online Help structure (Tier-1): Research Hub back-office objects — Research Assets, Research Deposits, Researchers, Grant Information, Media Mentions, Projects, Activities, User Identifiers, Collections, Organizational Units; Portal & Profiles — claiming outputs, file access requests, CV management; Smart Harvesting Framework — author matching approval task list, asset matching rules, record importing configuration; Publishing — OAI, FTP export, Google Search/Scholar/Datasets, Primo, ORCID, SEO; Integration — SIS, SWORD, Web of Science, InCites, DataCite/Crossref mapping, ETD Administrator; Analytics — subject areas, reports; Appendices — ANZ Fields of Research and Socio-Economic codes.
- "Claiming Outputs from Smart Harvesting" (Tier-1): Smart Harvesting "bring[s] in assets that are potential matches for a set of pre-selected researchers. Administrators can mark outputs from Smart Harvesting for approval by researchers." Researcher sees claim notifications in the profile; claims or rejects; a claimed output "if approved… will display with the rest of the publications. If the asset was not yet approved, it will display in the In Process tab. If an output was rejected it will not display in the portal."
- Funding: holds awarded grants information; integrates Pivot-RP for funding-opportunity discovery (adjacent capability, explicitly an integration).
- Users: librarians named throughout (library-systems lineage); research office use cases (activity reporting, tenure processes, national assessment projects).

### VIVO (open source, LYRASIS) — evidence layer A unless noted

- Self-positioning: "VIVO creates an actionable map of the scholarly work of your organization"; "a connected, integrated record of the scholarly work of your institution, ready for reporting, visualization, and analysis."
- "Automatically connect data from your institution with external sources of data on researchers, scholarly activities, funding and impact."
- Semantic technologies and open standards for representing scholarly work; community-developed open source; 150+ instances in 25+ countries claimed on site.
- Features shown: scholar/researcher pages (expertise, production, outcomes), network visualizations (co-authorship, mentoring/thesis networks), topic word visualizations.
- Disambiguation/deduplication specification published as a community RFC (2026) — direct evidence that entity dedup/disambiguation is a first-class concern of the Type, worked on even at the open-source pole.
- No evidence fetched of assessment-exercise tooling, OA compliance machinery, or awards administration — consistent with a profiles/networking-first realization.

### Type-level sources — evidence layer B/C

- euroCRIS CERIF: "the comprehensive information model for the domain of scientific research… intended to support interchange of research information between and with CRISs." euroCRIS also maintains the DRIS (Directory of Research Information Systems) and runs the annual CRIS conference — evidence of a distinct, internationally organized product category.
- OCLC Research + euroCRIS definition (quoted by Symplectic): RIM is "the aggregation, curation, and utilization of information and research." Their joint survey (381 responses, 44 countries) found commercial and open-source platforms "coexisting with a large number of region-specific solutions as well as locally developed systems" — evidence that the Type spans commercial, open-source, regional, and locally built realizations.
- Acronym equivalence (Symplectic page): "RIM Systems – also known as Current Research Information Systems (CRIS), or sometimes as Faculty Information Systems (FIS) or Expert Finder Systems (EFS)." Pure independently: "RIMS, also known as a CRIS." → RIM/RIMS/CRIS/FIS/EFS are one market family behind several names; the directory leaf "Research Information Management / CRIS" is one Type, not an alias problem.

## Cross-product Comparison

| Dimension | Pure | Elements | Esploro | VIVO |
|---|---|---|---|---|
| Self-label | RIMS / CRIS | research management system / RIM | research information management solution | research networking / "map of scholarly work" |
| Person record | researchers (Core) | users/faculty | Researchers | persons/scholars (semantic) |
| Output record | research outputs | publications + scholarly activities | research assets (articles, datasets, creative works, preprints…) | publications (semantic) |
| Project / funding | projects + funding (Core); Award Management module | grants/awards (Awards Management, deep) | awarded grants + projects (records) | funding/grants (records) |
| Org unit | organizational data (Core) | groups | Organizational Units | organizations (semantic) |
| Extended types | impact | equipment/technology, teaching, patents, impact records | media mentions, activities, collections | courses, thesis/mentoring links |
| Ingestion channels | internal systems (HR, finance, grant mgmt) + external DBs (Scopus, WoS, ORCID, national CRIS registers) | widest-source harvesting (13+ publication sources, Dimensions grants) + internal | Smart Harvesting + deposits by researchers/librarians/assistants + import profiles | harvest from external sources + internal data |
| Attribution machinery | dedup/merge via DOI/ORCID/Scopus ID; source prioritization; role-based validation | identifier-based auto claim/suggest/reject/ignore + name-based search settings; curator pending queues | Smart Harvesting author matching + admin-marked approval + researcher claim/reject | identifier harvesting + community dedup/disambiguation spec |
| Validation gate | editors/admins review/approve/enrich before publish/report | claim → Mine; curator processing; item-level privacy | claim → approved → portal; unapproved → In Process; rejected → hidden | (weaker; community-managed) |
| Consumption | Portal, dashboards, CVs, national assessment modules, reporting | public profiles (Discovery), Reporting Hub + SQL DB + BI, REF/PBRF workflows, OA monitor, impact records | Research Portal + profiles, Analytics, publishing to ORCID/OAI/Google/Primo | scholar pages, network/topic visualizations, reporting |
| OA / repository | compliance tracking; (repository module per marketing) | repository integrations + OA Monitor + deposit prompts | repository functions inside ("beyond the repository") | not evidenced |
| Assessment exercises | National Assessment module (REF, SEP/KUOZ) | REF (52-article category), PBRF, internal reviews | "national assessment projects" named as use case | not evidenced |
| Deployment | SaaS | SaaS or on-premises | cloud (Ex Libris platform) | self-hosted open source |
| Standards | CERIF, Dublin Core | ORCID, ROR, GRID, REST API, SQL DB | OAI, SWORD, DataCite/Crossref, ORCID | semantic web / VIVO ISF |

Layer-B findings (cross-product commonality, 4/4 unless noted):

- The linked record corpus: person + output + project/funding + organizational unit, held as one institutional corpus (4/4).
- Multi-channel acquisition: external sources + institutional systems + human entry/deposits (4/4).
- Attribution/matching of records to the institution's people as a distinct, user-visible step (4/4; machinery differs).
- A validation/curation gate between acquisition and authoritative/public status (3/4 direct evidence: Pure, Elements, Esploro; VIVO weaker but dedup spec shows the concern).
- Researcher profiles as a first-class consumption surface (4/4).
- Institutional reporting/analytics from the corpus (4/4).
- Public-facing showcase (portal/profiles) (4/4 present, but modular in Pure/Elements — see anti-overfit).
- OA compliance machinery (3/4: Pure, Elements, Esploro; absent from VIVO evidence) — policy-dependent, layer L2.
- Assessment-exercise tooling (3/4: Pure, Elements, Esploro names it as use case; regional — UK/NZ/NL) — layer L2.
- Funding/awards administration depth (2/4 deep: Elements Awards Management, Pure Award Management module; Esploro/VIVO hold funding records only) — bundling, not identity.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **The institution's research record corpus as system of record** — persistent linked records for the institution's researchers, research outputs, projects/funding, and organizational units, held in one system as the institution's authoritative picture of its research activity.
   - remove → disconnected lists: a publication spreadsheet, a staff directory, a grant tracker.
2. **Multi-channel acquisition reconciled to attribution** — records flow in from multiple channels (external databases/sources, institutional systems, researcher deposits, manual entry) and are matched to the institution's people and reconciled (deduplicated, merged, claimed/rejected, validated) into authoritative attributed records, as an ongoing operation.
   - remove → a read-only bibliography or an uncurated dump; the "current" in CRIS dies.
3. **The institutional research picture served out** — the corpus is consumed for the institution's purposes: researcher profiles/expertise discovery, institutional reporting/analytics, and commonly a public showcase.
   - remove → a private archive nobody uses; the "management" in RIM dies.

Jointly-held load-bearing tests:

- 1 alone = a static research database (archive).
- 2 without 1 = an ingestion pipeline with no system of record.
- 3 without 1+2 = a showcase built on nothing (brochure site).
- 1+2 without 3 = a curated archive with no institutional consumption.
- 1+3 without 2 = a manually typed showcase that decays — not "current" research information.
- 2+3 without 1 = an aggregation/discovery surface over external data — Academic Search Engine / expert-finder-over-the-world territory, not the institution's own records.

### L1 — Common Mature Structure

Present across the modern sample, expected by the market, but not required to recognize the Type:

- External-source harvesting from publication databases (Scopus, Web of Science, PubMed, Crossref, arXiv…) and grants databases (Dimensions).
- Researcher identifiers (ORCID, Scopus ID, email) driving automatic claiming/suggestion.
- Deduplication/merge machinery over persistent identifiers (DOI, ORCID, author IDs).
- Claim/reject + approval workflows (researcher self-service + curator queues).
- Public research portal / branded public profiles.
- Reporting dashboards, BI integration, SQL reporting database.
- CV generation from validated records.
- Open-access compliance tracking and repository deposit integration.
- Assessment-exercise workflows (REF, PBRF, internal reviews, annual collections).
- Identifier synchronization and publishing out (ORCID, OAI, Google Scholar, search engines).
- Role model: researcher / curator (librarian, research office) / administrator / leadership.

### L2 — Variant / Optional Structure

- National assessment modules tied to specific regional exercises (REF UK, PBRF NZ, SEP/KUOZ NL) — regional.
- Open-access compliance depth — policy-regime dependent (strong UK/EU; weaker elsewhere).
- Awards/grant-lifecycle administration (proposal → award → post-award) — bundled in some products (Elements, Pure module); absent as administration in others (Esploro, VIVO hold records only).
- Repository functions (full-text hosting, file requests, access levels) — merged in Esploro, integrated in Elements, modular in Pure.
- Extended record types: equipment/facilities, media mentions, impact records, teaching activities, patents, tech-transfer objects.
- Deployment: SaaS vs on-premises vs self-hosted open source.
- Data-model standardization: CERIF-based vs semantic-web (VIVO ISF) vs proprietary.
- Locally built / region-specific systems (OCLC/euroCRIS survey) — the Type has a long tail of homegrown realizations.
- AI-assisted curation (CV-to-records, smart matching) — era-current.

### L3 — Vendor-specific Structure (research notes only)

- Pure: module names (Core/Portal/Community/Award Management/CV/Reporting/National Assessment); Scopus-integration positioning; implementation-duration claims; named customer deployments (CityU "CityU Scholars", NSF translational-impacts map, MEDERI hospital network).
- Elements: Discovery Module name; Annual Collection module; Records of Impact; identifier-disposition button semantics ("Yes/No/Ignore" with auto claim/suggest/reject/ignore); identifier-suggestion threshold behavior (found in three items before suggestion — FAQ); version-specific UI paths (v6.x vs v7.5+).
- Esploro: Smart Harvesting/Smart Expansion names; "In Process" tab semantics; Many Authors Handling Policy; file-access requests; letters configuration; ANZ code appendices; Primo/SIS/ETD integrations.
- VIVO: Vitro platform; VIVO Integrated Semantic Framework; LYRASIS membership/governance; POSI self-assessment; workshop series.

## Vendor-specific / Rejected Findings

Rejected from the canonical core (with reasons):

- **Harvesting from commercial databases as definitional** — rejected: Esploro documents deposits-by-humans as a first-class channel; VIVO and historical/regional CRIS run on manual/local ingestion; the invariant is multi-channel acquisition + reconciliation, not any specific source.
- **ORCID/identifier machinery as definitional** — rejected: modern-dominant implementation of attribution; historical CRIS used internal person records; the invariant is attribution/matching itself.
- **Public portal as definitional** — rejected: portal is a separately licensed module in Pure and a module in Elements; the invariant consumption floor is profiles + reporting; public showcase is the dominant realization, not the definition.
- **REF/national assessment as definitional** — rejected: regional (UK/NZ/NL); US and most non-Commonwealth institutions run without it.
- **OA compliance as definitional** — rejected: policy-regime dependent; VIVO pole lacks it entirely.
- **Grant-lifecycle administration as definitional** — rejected: only 2/4 products administer the lifecycle; the rest hold funding as linked records; lifecycle administration is Research Administration territory bundled into some CRIS products.
- **Repository as definitional** — rejected: Esploro's own positioning is "beyond the traditional repository"; Elements integrates with external repositories; the OA item (file + access level) is the IR's defining object, not the CRIS's.
- **CERIF as definitional** — rejected: it is an interchange standard, not a structure every product implements (VIVO is semantic-web based; Esploro/Elements proprietary models).
- **AI/ML curation as definitional** — rejected: era-current marketing layer.
- **Specific object vocabulary** (e.g., "research asset" vs "output" vs "publication") — rejected as vendor terminology; conceptually the same slot.

## Boundary Findings

- **vs Institutional Repository**: IR's defining object is the open-access item — a deposited file with an access level, preserved and exposed via OAI-PMH. CRIS's defining object is the linked research record corpus. The two interlock (CRIS feeds the IR; OA status is a CRIS record attribute) and products bundle them (Esploro merges; Elements integrates; Pure modular). Test: remove the linked corpus and keep OA item management → you have an IR; remove OA file management and keep the corpus → you have a CRIS.
- **vs Research Administration Platform / Research Grant Management**: those Types own the grant as the institution's unit of financial/compliance work (proposal routing, budgets, effort, subawards, closeout). CRIS holds funding as linked records that give the research picture its funding dimension. Elements' Awards Management and Pure's Award Management module are bundling — the CRIS core (corpus + attribution + consumption) stands without them.
- **vs Bibliometrics Platform**: bibliometrics analyzes publication/citation corpora (often world-scale, licensed) for insight; CRIS maintains the institution's own records and reports on them. CRIS analytics modules consume the CRIS corpus; they do not define it.
- **vs Reference Manager**: individual-scale personal bibliography/citation tool; CRIS is institution-scale, multi-role, with institutional reporting and compliance duties.
- **vs Academic Search Engine / Research Funding Discovery Platform**: discovery over the world's literature/funding opportunities (Esploro's Pivot-RP integration is exactly this, as an adjacent integration); CRIS is the institution's own record corpus. Test (L0 leg 2+3 without 1): an expert-finder over harvested world data with no institutional system of record is not a CRIS.
- **vs Research Data Management**: RDM handles active research data (plans, storage, sharing controls); CRIS records datasets as outputs within the corpus. Adjacent, increasingly linked.
- **vs HR systems**: CRIS ingests staff/affiliation data from HR (Pure documents HR/finance synchronization); it does not own employment records.
- **Naming**: RIM/RIMS, CRIS, FIS, EFS are one Type (both vendor self-labels and the OCLC/euroCRIS framing agree). No taxonomy change needed; the leaf's dual name is accurate.

## Uncertainties

- Pure's operational help center was not reached; Pure validation-workflow detail comes from its own how-it-works FAQ (Tier-2). Assertion strength for Pure-specific workflow mechanics is correspondingly reduced.
- Worktribe dropped (403 ×2); the smaller-institution all-in-one pole is under-sampled. The sample's smallest pole is VIVO (open source), which is profiles-first rather than administration-first.
- VIVO's validation/curation depth is under-evidenced (only the dedup/disambiguation RFC was fetched); claims about VIVO workflows are correspondingly weak.
- Whether any product exists that holds the corpus + consumption but has *no* attribution step (i.e., L0 leg 2 falsification) was not found in the sample; the historical manual-entry CRIS still required attribution (linking publications to staff records), so leg 2 stands, but the evidence is inference for the historical case rather than direct observation.
- Esploro's grants objects: the help structure shows "Working with Grant Information" and "Configuring Grants" but the depth of grant administration (budgets/effort) was not fetched; treated as record-level funding, not administration, per available evidence.
- National CRIS registers (national-level aggregations of institutional CRIS data) were observed only as integration targets (Pure FAQ, euroCRIS DRIS, PeruCRIS reference); whether a national register is the same Type or a supra-institutional variant was not resolved — recorded as a possible boundary issue.

## Final Synthesis

A Research Information Management system (RIM/RIMS, CRIS, FIS, EFS) is the research institution's system of record for its research activity. Its world is a linked corpus — researchers, outputs, projects/funding, organizational units — continuously fed from multiple channels (external databases, institutional systems, researcher deposits, manual entry), reconciled to the institution's people through matching/claiming/validation, and served out as researcher profiles, institutional reporting/analytics, and commonly a public showcase, with OA compliance and assessment-exercise tooling as policy-dependent extensions and grants administration as optional bundling. The Type is realized across commercial suites, open-source platforms, and locally built systems, and its defining core survives both the modern harvesting-heavy implementation and the older manually maintained institutional research database.
