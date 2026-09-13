# Research Information Management / CRIS

## Overview

A **Research Information Management system** — historically called a **Current Research Information System (CRIS)**, and also marketed as a Faculty Information System or Expert Finder System — is a research institution's system of record for its own research activity. It holds the institution's researchers, research outputs, projects and funding, and organizational units as one linked corpus of records; it continuously pulls candidate records in from external sources and institutional systems and reconciles them to the institution's people; and it serves the resulting picture out as researcher profiles, institutional reporting, and commonly a public research showcase.

The problem it solves is fragmentation: research information naturally scatters across HR systems, finance systems, publisher databases, funder portals, and individual CVs, none of which gives the institution a consistent, current, attributable picture of what its people produce. A CRIS unifies that picture in one place and keeps it current with minimal manual re-entry.

Its boundary: a CRIS is about the institution's *records* of research — not the open-access archive itself (Institutional Repository), not the money pipeline of grant administration (Research Administration Platform), and not discovery over the world's literature (Academic Search Engine). It sits at the center of these, feeding and being fed by them.

## Users & Context

The context is a university, research institute, government research body, funder, or (in some deployments) a hospital network — any organization that needs a standing, institution-wide picture of its research.

Primary users:

- **Research office / research administrators** — run the system as the institution's research data stewards: configure ingestion, validate and enrich records, produce reports, run assessment and compliance exercises.
- **Library research-support staff** — a second stewarding role, strongest in library-lineage products: metadata quality, harvesting configuration, open-access support, repository integration.
- **Researchers / faculty** — the population the records describe. They claim or reject records matched to them, maintain their profiles, complete annual activity collections, and generate CVs from validated data.

Secondary users:

- **Institutional leadership** — consume dashboards and analytics over the corpus for strategy and external reporting.
- **IT / integration staff** — maintain the feeds to and from HR, finance, student systems, and external services.

The researcher's experience is deliberately low-effort: the system's recurring promise across products is that records arrive pre-populated from external sources and the researcher only confirms, corrects, or rejects them — then reuses the validated data for every downstream form (annual review, promotion, CV, funder report) instead of retyping it.

## Core Model

### The defining core

The system's world is a **linked corpus of research records** held as the institution's single authoritative picture:

```text
Researcher (person)
└── affiliated to → Organizational Unit (department / institute / school)
├── authors / performs → Research Output (publication, dataset, creative work, …)
├── participates in → Project
├── holds / is funded by → Funding (grant / award record)
└── extended record types (activities, equipment, impact, media mentions, …)
```

Three properties together make the Type what it is. Remove any one and the product stops being a CRIS:

- **The linked record corpus as system of record.** Persistent records for people, outputs, projects/funding, and organizational units, connected by explicit links (authorship, affiliation, funding acknowledgment, participation). This is what separates a CRIS from a pile of disconnected lists — a publication spreadsheet, a staff directory, a grant tracker. The corpus is the institution's *own* records, not an aggregation of the world's metadata.
- **Multi-channel acquisition reconciled to attribution.** Records enter from several channels at once — external databases and publisher sources, institutional systems (HR, finance), researcher deposits, manual entry — and each candidate record must be *matched to the institution's people* and reconciled (deduplicated, merged, claimed, validated) before it becomes authoritative. Without this ongoing reconcile loop the corpus is a static archive, and the "current" in Current Research Information System dies.
- **The institutional research picture served out.** The corpus exists to be consumed: researcher profiles and expertise discovery, institutional reporting and analytics, and commonly a public showcase. A corpus nobody serves is a private archive, not research information *management*.

### Standard capabilities

Mature products add a common layer of capabilities on top of this core. They are what make the system practical, not what make it a CRIS:

- **External-source harvesting** — automated retrieval of publication candidates from scholarly databases (abstract-and-citation databases, PubMed-class bibliographic sources, preprint servers, publisher metadata) and of grant candidates from funding databases.
- **Researcher identifiers** — ORCID and publisher author identifiers, plus institutional email addresses, used to attribute harvested records to the right person automatically or semi-automatically.
- **Deduplication and merge** — duplicate records arriving from different sources are detected and merged, commonly keyed on persistent identifiers (DOI, ORCID, author IDs).
- **Claim / reject and validation workflows** — researchers see pending candidate records and claim or reject them; administrators and curators review, approve, and enrich records before they become authoritative or public.
- **Public research portal and profiles** — a branded, searchable public surface presenting the institution's researchers, outputs, and projects; per-researcher profile pages with biography, outputs, grants, and expertise.
- **Reporting and analytics** — dashboards and report builders over the corpus, commonly with a direct-query reporting database and BI-tool integration.
- **CV generation** — standardized CVs produced from validated records rather than hand-maintained documents.
- **Open-access compliance support** — tracking outputs against funder and institutional OA policies, prompting researchers to deposit the accepted version, and monitoring compliance.
- **Assessment-exercise support** — workflows that gather, review, and submit outputs and metadata for national research assessment exercises and internal reviews (annual activity collections, promotion rounds).
- **Publishing out** — synchronization of validated records to external services and standards-based exports (researcher identifier registries, OAI harvest endpoints, search engines, library discovery systems).

### Concept vs implementation

The core is conceptual; products implement each concept differently, and a reader who knows only one implementation should still recognize the others:

```text
Concept:   attribution of records to people
Realized as:  researcher identifiers (ORCID, publisher author IDs, email),
              name-variant matching, administrator-assisted matching,
              researcher claim/reject with curator approval

Concept:   acquisition channels
Realized as:  automated harvesting from licensed databases,
              synchronization with institutional HR/finance systems,
              deposits by researchers/librarians,
              manual entry, bulk import

Concept:   the research output record
Realized as:  "research output", "publication", "research asset",
              "scholarly activity" — one slot with vendor-specific vocabulary
              and a product-specific type list (publications, datasets,
              creative works, preprints, media mentions, …)
```

## How It Works

The system runs as a continuous loop rather than a single transaction. Its canonical cycle:

### 1. Ingest candidate records

```text
configure sources (external databases, institutional systems, deposit forms)
→ candidates arrive continuously (harvested metadata, HR/finance sync,
  researcher deposits, manual entries)
```

No single channel is the definition; mature products combine several. The candidate record is *not yet* part of the institution's picture — it is a proposal.

### 2. Match candidates to the institution's people

```text
candidate arrives with author names / identifiers
→ system matches against researcher records
  (identifier match, name-variant match, or algorithmic suggestion)
→ matched candidates queue for the researcher and/or curator
```

This is the step that makes the corpus *attributable* — the institution's picture is built by binding external records to its own people. Name collisions and near-identical names are a documented, engineered-for problem: mature products expose matching controls — per-identifier dispositions, name-variant settings, review queues — precisely to keep the wrong person's publications out.

### 3. Claim, validate, reconcile

```text
researcher reviews pending candidates → claim or reject
→ administrator/curator validation (dedup, merge, metadata enrichment)
→ record becomes authoritative
```

The gate matters: a claimed record may still wait for approval before it appears publicly; a rejected record disappears from the researcher's surfaces. Validation is role-based — researchers confirm *their* records; curators guard the institution's picture.

### 4. Enrich and link

```text
link outputs ↔ funding (acknowledged grants)
link outputs ↔ projects, datasets, impact evidence
attach metrics, open-access status, full-text links
```

The links are the point: a publication list becomes research information when each output is connected to the people, funding, and organizational context that produced it.

### 5. Serve the picture out

```text
researcher profiles (auto-generated, researcher-maintained)
→ institutional portal / public showcase
→ reports, dashboards, CVs
→ compliance and assessment workflows (OA monitoring, exercise submissions)
→ exports and synchronization to external services
```

Consumption is continuous, not a final step: profiles update as records are validated; reports re-run against the live corpus; assessment workspaces reuse the same records researchers already confirmed.

### The recurring interaction patterns

- **Researcher loop** — check notifications → claim/reject candidates → curate own profile → complete an annual collection by selecting already-validated records → generate a CV.
- **Curator loop** — monitor ingestion reports and validation queues → resolve duplicates and mismatches → enrich records → approve for publication.
- **Administrator loop** — configure sources, matching rules, and visibility; define reporting and exercise workflows; manage roles and privacy.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Back-office research hub (curator / administrator console)

The stewarding surface over the corpus.

- lists of records by type (people, outputs, grants, projects, organizational units) with search and filtering
- validation and matching queues (pending candidates, deduplication tasks, approval task lists)
- record detail views with edit/enrich forms and link management
- primary actions: validate, merge, reject, enrich, link, configure

### Researcher workspace

The researcher's personal surface, usually reached through the profile.

- claim/reject notifications for matched candidate records
- profile editor (biography, expertise, affiliations, identifiers)
- personal record lists with visibility controls
- annual-collection / activity-report forms that reuse validated data
- primary actions: claim, reject, edit, set visibility, submit, export CV

### Public research portal

The institution's outward-facing showcase, typically search-engine optimized.

- search across people, outputs, and projects
- researcher profile pages (biography, outputs, grants, expertise, metrics)
- output and project detail pages, commonly with links to full text or deposit services
- primary actions: search, browse, follow links out; file requests for restricted files where supported

### Reporting / analytics surface

- dashboards over outputs, funding, collaborations, and compliance
- report builders and scheduled reports; direct-query reporting database and BI export in mature products
- primary actions: build report, filter, export, schedule

### Compliance and assessment workspaces

- open-access monitors (compliance state per output against defined policies)
- assessment-exercise workspaces (gather candidate outputs, select, review, track, submit)
- primary actions: check compliance, prompt deposit, record exceptions, assemble and submit exercise data

### Integration and export surfaces

- administrative configuration of source connections and export targets
- standards-based endpoints (identifier registries, OAI harvest, search-engine submission)

## Important Rules / Behaviors

### Attribution is gated, not automatic

Harvested records do not silently become the institution's records. A candidate must pass matching and a claim/validation gate before it is authoritative — and a further visibility step before it is public. This two-sided gate (researcher confirmation + curator approval) is the system's core quality mechanism, and products differ mainly in how much is automated versus routed to human review.

### Rejected and unapproved records have distinct fates

A record a researcher rejects disappears from their surfaces; a claimed-but-unapproved record typically remains visible internally in a pending/in-process state but not on public surfaces. The public picture is always a curated subset of the corpus.

### Deduplication is a first-class operation

The same publication arrives from multiple sources; the same person appears under name variants. Products merge on persistent identifiers where possible and expose manual merge/review where automation is uncertain. Wrong attribution is treated as a serious defect, and the tooling (identifier dispositions, name-variant settings, rejection memory) exists to suppress it.

### Visibility is item-level and privacy-sensitive

Records carry per-item visibility controls — researcher-controlled and administrator-controlled — because public exposure of a researcher's work is a professional concern, not just a display setting. Restricted files (e.g., the accepted version of a paper) may be requestable rather than openly downloadable.

### The corpus feeds other systems; it does not own their data

Employment data is synchronized from HR, not maintained here; money is administered in finance/grant systems (where administration exists at all); full texts may live in a repository. The CRIS holds the *linked picture* and publishes out to identifier registries, discovery services, and harvest endpoints.

### Reporting reuses validated records

The recurring efficiency rule: any downstream form (annual review, CV, funder report, exercise submission) draws on records already claimed and validated, and known attributes (rank, affiliation) are filled automatically rather than re-asked.

## Variants

- **Commercial suite** — the dominant shape: modular platforms where the core corpus is sold alongside optional portal, reporting, awards-administration, and assessment modules.
- **Open-source community platform** — self-hosted, standards-and-semantic-web oriented, strongest at profiles, expertise discovery, and network visualization; institutions own their data and operate the system themselves.
- **Repository-merged** — products from library-vendor lineage that fold repository functions (deposit, file hosting, access levels) into the research information hub, positioning themselves as "beyond the traditional repository."
- **Profiles-first / expertise discovery** — deployments (often labeled Faculty Information System or Expert Finder System) whose center of gravity is researcher profiles and collaboration discovery rather than compliance machinery.
- **Compliance-first** — deployments in jurisdictions with national assessment exercises or strong open-access mandates, where exercise tooling and OA monitoring dominate configuration effort.
- **Regional and locally built systems** — the Type has a long tail of homegrown and region-specific systems coexisting with commercial and open-source platforms, per the field's own surveys.
- **Funder and government deployments** — the same record model applied by funders and agencies to track and showcase the projects they support, rather than by a single institution.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Institutional Repository | interlocked neighbor | the IR's defining object is the open-access item (deposited file + access level + preservation); the CRIS's defining object is the linked record corpus; CRIS feeds the IR and tracks OA status, products often bundle both |
| Research Administration Platform / Research Grant Management | adjacent, often bundled | those Types own the grant lifecycle as financial/compliance work (proposal routing, budgets, effort, closeout); a CRIS holds funding as linked records that give the research picture its funding dimension |
| Bibliometrics Platform | adjacent consumer/producer | bibliometrics analyzes publication/citation corpora (often world-scale) for insight; a CRIS maintains the institution's own records and reports on them |
| Reference Manager | individual-scale neighbor | a personal bibliography/citation tool for one researcher; a CRIS is institution-scale, multi-role, with reporting and compliance duties |
| Academic Search Engine | discovery over the world | searches the world's literature/funding; a CRIS is the institution's own record corpus — an expert-finder over harvested world data with no institutional system of record is not a CRIS |
| Research Data Management | adjacent | RDM handles active research data (plans, storage, sharing controls); a CRIS records datasets as outputs within the corpus |
| Research Funding Discovery Platform | adjacent integration | matches researchers to funding opportunities; commonly integrated into CRIS products as a feed, not part of the record corpus |
| HR / HCM systems | upstream source | supplies staff and affiliation data by synchronization; the CRIS never owns employment records |

The two most consequential boundaries: against the **Institutional Repository** (OA item vs linked corpus) and against **Research Administration** (funding-as-record vs grant-as-financial-workflow). Both pairs interlock and are frequently bundled in one vendor's portfolio, which is why they are confused — but each defining object stands alone.

## Representative Products

- **Pure** (Elsevier) — market-leading commercial RIMS/CRIS; broad modular suite (core corpus, portal, reporting, CV, awards administration, national assessment modules).
- **Symplectic Elements** (Digital Science) — UK-origin commercial system; strong at harvesting breadth, open-access workflows, and assessment exercises (REF/PBRF-class); deep awards-management module.
- **Esploro** (Ex Libris / Clarivate) — library-vendor lineage; repository-merged philosophy ("beyond the traditional repository"); smart-harvesting-driven profiles and portal.
- **VIVO** (open source, LYRASIS community) — open-source, semantic-web pole; profiles, expertise discovery, and network visualization; institution-owned data.

The defining core was checked against the open-source pole and against the field's own accounts of older, regional, and locally built systems (manually maintained institutional research databases, national CRIS registers) to avoid defining the Type by the current harvesting-heavy implementation.

## Sources

Research date: **2026-09-09**

- Elsevier — Pure product page: https://www.elsevier.com/products/pure
- Elsevier — Pure, How it works: https://www.elsevier.com/products/pure/how-it-works
- Symplectic — Elements product page: https://www.symplectic.co.uk/products/elements
- Symplectic — What is Research Information Management? (quoting the OCLC Research / euroCRIS definition): https://www.symplectic.co.uk/research-management-using-the-elements-platform/
- Symplectic Support — Elements documentation, incl. "Automatic claiming in Elements": https://support.symplectic.co.uk/en/articles/11299457
- Ex Libris — Esploro product page: https://www.exlibrisgroup.com/products/esploro/
- Ex Libris Knowledge Center — Esploro Online Help (English), incl. Esploro Overview and Claiming Outputs from Smart Harvesting: https://knowledge.exlibrisgroup.com/Esploro/Product_Documentation/Esploro_Online_Help_(English)
- VIVO — https://vivoweb.org/
- euroCRIS — Main features of CERIF: https://eurocris.org/services/main-features-cerif/

> Sourcing limitations: one candidate product (Worktribe) was dropped after repeated access failures and the smaller-institution pole is under-sampled; Pure's operational help center was not reachable, so Pure-specific workflow mechanics rest on its product/how-it-works documentation rather than help-center articles. Precise operational parameters (source counts, thresholds, timing) are intentionally not stated; product-specific mechanics live in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
