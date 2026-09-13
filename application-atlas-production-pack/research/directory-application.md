# Research Notes — Directory Application

## Research Goal

Identify the smallest stable invariant that defines the **Directory Application** Type (DIRECTORY.md §02.11 Directories & Listings), and place every other observed feature at the correct abstraction level.

This document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

and evidence layers:

```text
A Direct Product Observation
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Directory Application

Nearest confusing Types (per DIRECTORY.md):

- Listings Platform (§02.11 sibling)
- Information Portal (§02.11 sibling)
- Review Platform / Comparison Platform (§02.10)
- General Web Search Engine / Vertical Search Engine (§02.02)
- General Reference Database (§02.05)
- Social Profile Network (§01.05)
- Member Directory (§25 — separate leaf)
- Contact Discovery / Sales Data Enrichment Platforms (§07), Master Data Management (§13) — data-platform drift

Working hypothesis:

> A Directory Application is a lookup-oriented application: a maintained catalog of standing, structured entries about entities of one defined class (businesses, people, companies, agencies…), organized for browsing and searching, where each entry presents the entity's identity plus attributes sufficient to identify, evaluate, and contact it.

## Research Questions

- What is the smallest structure that makes a product recognizable as a directory, independent of era and business model?
- How do entries enter the catalog (editorial curation, self-service claiming, paid inclusion, statutory filing, aggregation of official records)?
- What lookup organizations do directories expose (category browse, alphabetical browse, geographic browse, keyword search, reverse lookup by phone/address/number)?
- What does an entry carry, and what does the entry detail surface show?
- How do monetization and verification postures vary, and which of them are definitional?
- Where are the boundaries with Listings Platform, Information Portal, Review Platform, Search Engines, and entity-data platforms?
- Does the definition survive print-era directories and non-commercial registers? (historical / market-sample check)

## Representative Products

| Product | Why selected |
|---|---|
| Whitepages | largest US people/residential directory; freemium commercial model; reverse-lookup pattern |
| Yellow Pages Australia (Thryv Australia) | archetypal category-organized business directory; advertiser-funded; print-book heritage still visible |
| Companies House "Find and update company information" (UK) | statutory public register of companies; filing-sourced entries; state-tracked records; free public service |
| USA.gov A–Z index of U.S. government departments and agencies | institutional/official directory; editorially maintained; pure free public service |
| OpenCorporates | cross-jurisdiction legal-entity aggregator; provenance-trust philosophy; API/data-drift pole |

The sample spans: entity classes (people / businesses / companies / agencies), business models (freemium, advertising, free public service, data licensing), and entry-sourcing models (aggregated public records, self-service listing signup, statutory filing, official editorial curation, multi-registry aggregation).

## Sources

Research date: **2026-09-07**

Sources successfully fetched on the research date (all Layer A below):

- Whitepages — https://www.whitepages.com/
- Yellow Pages Australia — https://www.yellowpages.com.au/
- Companies House — https://find-and-update.company-information.service.gov.uk/
- USA.gov — https://www.usa.gov/federal-agencies
- OpenCorporates — https://opencorporates.com/

Source-access limitation (recorded per evidence rules): the following vendor surfaces were attempted and could not be fetched — yelp.com and yelp-support.com (403 / transport error), yp.com and yell.com (403), bbb.org (403), thomasnet.com (403, incl. /about), manta.com (403), yellowpages.ca and canada411.ca (403), capterra.com (403), hotfrog.com (403), yalwa.com (403), kompass.com (403), europages.com / europages.co.uk (empty responses), pingboard.com (403), support.google.com (timeout ×2), gethelp.wildapricot.com (JS-only shell, no content), en.wikipedia.org (timeout ×2), directory.stanford.edu (transport error ×2). Consequently: no Tier-1 help-center article for any commercial directory was reachable; evidence is concentrated on official home / landing / service pages, plus one full statutory service. All claims below are calibrated to that evidence: no numeric limits, no pricing details, no review-mechanics details, and no help-center-only workflows are asserted.

## Product Observations

### Whitepages (people/residential directory) — Layer A

- Self-describes as "the largest U.S. directory and trusted source for contact info and property data" and, in its own FAQ, as "the largest online phone book and directory in the United States" offering "free access to limited landline and listed phone numbers, home addresses, and resident information for adults across the U.S."
- Three lookup modes on the home surface: **People Search** (last name + city/state/ZIP required), **Reverse Phone**, **Reverse Address** — i.e. the entity can be looked up by identity or by attribute keys.
- Browse structure: an A–Z "Last Names Directory" (alphabetical browse over the entity class).
- Entry attributes (its own "What can I find" list): cell/landline numbers, addresses, relatives, maiden names, age; property details; public-records/safety attributes (background checks, licenses, fraud ratings).
- Business model: free search with limited results; **Whitepages Premium** subscription unlocks fuller contact data, address histories, background reports; **Whitepages for Business** for identity verification/contact enrichment; **Whitepages Pro API** to "plug contact information and property data into fraud prevention workflows, CRMs, and other platforms."
- Family vocabulary, in its own FAQ: "white pages list residential phone numbers and addresses for individuals. Yellow pages list business phone numbers and advertisements organized by category." And on business listings: "services like Google Business Profile, Yelp, and the Better Business Bureau are more current options" — direct attestation that the business-directory family is recognized as a family.
- Historical anchor, in its own FAQ: the printed residential phone book "the kind that used to show up on your doorstep"; Whitepages positions itself as going "beyond a traditional printed phone book."
- Drift note: the same company now sells identity verification, property intelligence (deed feeds), and data APIs — a directory origin with a data-platform orbit.

### Yellow Pages Australia (business directory) — Layer A

- Self-titled "Your Local Australian Business Directory."
- Two-field search pattern: "What are you looking for?" + "Where?" (with "Use My Location") — the what × where lookup.
- Browse structure: head-of-term shortcuts (Lawyers, Dentists, Restaurants, Plumbers, Electricians, Mechanics, Hairdressers, Builders, Doctors) and a **category × city grid** ("Popular categories" for Sydney / Melbourne / Brisbane / …, with URLs of the form /sydney-nsw-2000/plumbers-gasfitters) — geography and category are the two browse axes.
- Entry-sourcing and monetization: "Get a free listing" (self-service signup at my.yellow.com.au), and an advertiser-funded model — "Connect with more customers… online ad on Australia's favourite business directory, SEM, social marketing or more"; "Digital marketing solutions"; "Business hub."
- Print heritage still a live product: footer link "Order or cancel your book" (directoryselect.com.au) — the print directory remains opt-in.
- Adjacent content layer: "Recent articles" and per-category "Cost guides" — content marketing attached to the directory, clearly secondary to the entity catalog.

### Companies House — "Find and update company information" (statutory register) — Layer A

- Single search box: "Enter company name, number or officer name" — identity-key and attribute-key lookup in one surface; plus **Advanced company search** (faceted) and an **Alphabetical company search** (a browse structure, listed as a feature).
- Entity-class-internal state dimension: **Dissolved company search** exists alongside active companies — records carry lifecycle states.
- Related entity class: **Search for disqualified directors** — a second directory over officers, derived from the same filings.
- Entry → underlying records: "View company data and document images"; "Order certificates and certified documents"; "File abridged or full accounts"; "Change a registered office address" — the register is both a lookup surface and the filing surface of record.
- Provenance posture, stated on the surface: "Companies House does not check the accuracy of the information filed" — the operator disclaims verification of self-reported entry data.
- Free public service; **Follow companies** (watchlist); developer API linked ("Developers").
- Entry sourcing: statutory filing obligations — the catalog is created and maintained by the entities' own legally required submissions, not by claiming or editorial curation.

### USA.gov — A–Z index of U.S. government departments and agencies — Layer A

- Self-description: "Get contact information for U.S. federal government agencies, departments, corporations, instrumentalities, and government-sponsored enterprises. Find websites, email, phone numbers, addresses, and more."
- Browse structure: A–Z letter index (A–W shown) plus an on-page search ("Search agencies and departments").
- Entry shape (repeated across all entries): entity name + one-paragraph description + **Website** + **Phone number** + **Contact** link + optional "Find an office near you" sub-locators + "More information about X >" detail page.
- Editorial/official sourcing: maintained by USAGov as "the official guide to government information and services" — no claiming, no advertising, no paid placement.
- Sub-directory pattern: several entries link onward to narrower official directories (e.g. USDA "farmers market directory", USAID "mission directory") — directories nested by scope.

### OpenCorporates (cross-jurisdiction legal-entity aggregator) — Layer A

- Self-description: "the world's largest open legal-entity database, providing a single unified set of company records from over 140 government registries and other official sources"; "fresh, standardized, auditable information direct from official primary sources."
- Two entity classes toggled on one surface: **Companies / Officers**.
- Retrieval organization: jurisdiction selector ("Browse all jurisdictions"), **Advanced search**, and register-level browsing; "Over 5 million searches made every month" (own claim) — lookup-primary usage.
- Provenance-trust philosophy: "sourced direct from primary sources, curated with clear decision-making and no hidden bias… defined by open not proprietary identifiers"; published **Legal-Entity Data Principles**; data-coverage and data-dictionary documentation.
- Use-case framing: entity verification, third-party risk, investigations, data management, business discovery — sold as data supply (API, bulk delivery, pricing page), i.e. a directory origin with an enterprise data-platform orbit.

## Cross-product Comparison

| Finding | Whitepages | Yellow Pages AU | Companies House | USA.gov | OpenCorporates | Abstraction level |
|---|---|---|---|---|---|---|
| defined entity class | US residents/people | Australian businesses | UK companies | US federal agencies | companies (+ officers) worldwide | L0 |
| standing entry per entity (persists across sessions; record of the entity itself) | yes | yes | yes | yes | yes | L0 |
| attribute profile incl. contact/reach attributes (phone, address, website, contact links) | yes | yes | yes | yes | yes (registry attributes) | L0 |
| organized for retrieval: search | People/Reverse Phone/Reverse Address | what × where | name/number/officer + advanced | search box | Companies/Officers + advanced | L0 |
| organized for retrieval: browse structure | A–Z last names | category × city grid | alphabetical search; (jurisdiction at OC) | A–Z letters | A–Z via registers | L0 |
| entry detail surface (dedicated page per entity) | person page | business pages | company page + filings | agency page | company page | L1 |
| multiple/reverse lookup keys (look up by phone/address/number/officer) | reverse phone/address | — | officer name, company number | — | officers toggle | L1 |
| geographic dimension in retrieval | city/state/ZIP required | "Where?" + city pages | registered office | offices near you | jurisdictions | L1 |
| filters / advanced / faceted search | — | — | advanced search | — | advanced search | L1 |
| entry lifecycle states (active/dissolved…) | — | — | dissolved search | — | (status per registry) | L1 |
| related/derived directories (officers, offices, sub-locators) | relatives/associates | — | disqualified directors | office finders | officers | L1 |
| contribution: self-service entry creation/claiming | — | free listing signup | (statutory filings, not claiming) | no | no | L2 |
| paid visibility / advertising | premium paywall | advertiser-funded | no | no | no | L2 |
| freemium/paywall on attributes | yes (Premium) | — | free | free | free tier + paid API | L2 |
| API / bulk data supply | Pro API | — | developers | — | API + bulk | L2 |
| provenance/verification posture | premium gating | — | accuracy disclaimer | official editorial | data principles | L2 |
| content layer (articles/guides) | — | articles + cost guides | guidance | — | blog/insights | L2 |
| print companion | phone-book heritage | "order or cancel your book" | — | — | — | L2 |
| platform drift toward identity/KYC/fraud data services | yes (Business/API) | marketing agency (Thryv) | — | — | yes (verification use-cases) | L2 / adjacent Type |

Layer B (cross-product commonality, observed across ≥3 of the 5 sampled products): standing per-entity entries with contact attributes; search + browse as twin retrieval organizations; a dedicated entry detail surface; a geographic axis; derived/related directories; API data supply.

Layer C (canonical inference): the retrieval organization (search + browse over a standing entity catalog) and the attribute profile (identity + reach attributes) are the load-bearing structure; everything commercial (ads, claiming, paywalls) and everything infrastructural (APIs, provenance frameworks) varies without changing the Type.

## L0 — Defining Invariant

```text
Defined entity class (fixed by the directory's scope)
└── Standing entry — one structured record per entity of the class
    └── Attribute profile — identity + reach attributes (name, contact, location …)
    └── Catalog retrieval organization — browse structures and search keys over the catalog
```

Three properties. Removal tests:

- remove the **defined entity class with a maintained standing catalog** → it becomes a general search engine or an unbounded index, not a directory
- remove the **attribute profile** (entries degrade to bare name lists) → it no longer routes the user to the entity; it stops doing a directory's job
- remove the **retrieval organization** (no browse, no search) → it becomes a raw record store, not a lookup application

Deliberately NOT in L0 (all pass the historical check — a print-era yellow pages, a printed residential phone book, and a paper membership roster satisfy L0 without them): reviews/ratings, claiming/self-service submission, paid visibility, maps, images/media, verification badges, APIs, websites-as-attributes, cloud delivery.

## L1 — Common Mature Structure

Common across the sampled products; makes a directory practical, not definitional:

```text
Entry detail surface (dedicated profile page per entity)
Multiple / reverse lookup keys (by phone, address, registration number, officer…)
Geographic axis in retrieval (location field, city pages, jurisdictions, office finders)
Faceted / advanced search over catalog attributes
Entry lifecycle states (active / dissolved / historical records)
Related or derived directories (officers, offices, relatives, sub-locators)
API / bulk data supply over the same catalog
```

## L2 — Variant / Optional Structure

```text
Entity class: people (residential), businesses, legal companies, government agencies,
              member/staff populations (bounded-population directories)
Sourcing model: editorial/official curation · self-service listing signup / claiming ·
              statutory filings · aggregation of official registers · (paid inclusion, attested
              as a family phenomenon but not directly observed in the reachable sample)
Business model: free public service · advertising-funded · freemium paywall ·
              subscription/data licensing
Verification posture: accuracy disclaimers · provenance principles · premium gating ·
              official editorial trust
Geographic scope: local → national → cross-jurisdiction
Adjacent layers: content marketing (articles/cost guides), review/rating surfaces,
              accreditation/trust markers, print companion products
Drift orbits: identity verification / fraud data (Whitepages), SMB marketing services
              (Yellow Pages/Thryv), entity-verification data supply (OpenCorporates)
```

## L3 — Vendor-specific Structure

Stays in Research Notes only:

- Whitepages: Identity Graph statistics, Property Intel deed feeds, background-check products, 411.com / PeopleSearch.com / Switchboard / Address.com brand family, best-time-to-call indicators
- Yellow Pages Australia: the category × city SEO URL grid (/sydney-nsw-2000/plumbers-gasfitters), cost-guide content engine, Thryv marketing-services bundle, directoryselect.com.au book ordering
- Companies House: abridged/full accounts filing, company name availability checker, disqualified directors search, certificate ordering, follow-companies feature, planned "other document filings"
- OpenCorporates: Legal-Entity Data Principles, 140+ register coverage list, KYC/B / AML use-case packaging, bulk-delivery guides
- USA.gov: agency-index letter anchor pages, Spanish-language mirror, embedded recruiter/office locators

## Boundary Findings

### vs Listings Platform (§02.11)

The decisive variable is what the record represents. A directory record is a **standing description of an entity** that persists as long as the entity exists; a listing is a **current offer** (a job, a rental, an item for sale) that is created, consummated, or expires. Test: strip the standing entity records and keep point-in-time offers with statuses → Listings Platform. (Directory Application is in the Directories & Listings family precisely because both organize retrievable records; the record's temporal nature separates them.)

### vs Information Portal (§02.11)

A portal organizes **content** (news, links, resources, services) around a topic or audience; a directory organizes **entity records**. Yellow Pages Australia carries articles and cost guides, but removing its entity catalog would leave a content site — at which point it has become a portal. Test: entries describe entities (directory) vs pages describe topics/content (portal).

### vs Review Platform / Comparison Platform (§02.10)

Reviews, ratings, and comparisons are **opinions about entities**; directory entries are the **entities' own records**. Consumer directories commonly attach rating surfaces, and the family relationship is attested (Whitepages' own FAQ names Google Business Profile, Yelp, and BBB as business-directory services). When opinion content becomes the primary object and the entity record is merely its carrier, the product is a Review Platform.

### vs General / Vertical Search Engine (§02.02)

A search engine indexes an unbounded, unstructured corpus and returns links; a directory maintains a **bounded, structured, curated** catalog whose entries are first-class records. OpenCorporates reports millions of searches monthly — search-like usage — but the object searched is a defined entity catalog with structured attributes.

### vs General Reference Database (§02.05)

Reference databases hold **facts and knowledge about things** (definitions, statistics, topics); directories hold **entity records for reaching entities**. Overlap arises when the entity class is "concepts" rather than contactable actors; the directory's signature output is contact/evaluation routing, not explanation.

### vs Social Profile Network (§01.05)

Profile networks center on self-authored presentation and a social graph/feed; people directories center on lookup of identity/contact records that the subject may not have authored. When feed, following, and social discovery become primary, the product is a Social Profile Network.

### vs Member Directory (§25) and internal staff directories

Bounded-population directories (association members, employees) reuse the same structure — entries, lookup, contact attributes — scoped to a closed roster. **Taxonomy flag**: Member Directory is a separate DIRECTORY leaf; the research here suggests it is most plausibly a domain-scoped instance of Directory Application rather than a structurally independent Type. No member-directory product was reachable for direct evidence in this pass; joint review recommended.

### vs entity-data platforms (§07 Contact Discovery / Sales Data Enrichment; §13 MDM; §15 identity data)

Two of five sampled products sell the same underlying catalog as API/bulk data for CRM enrichment, KYC/AML, or fraud prevention. The **lookup application** (a human-facing retrieval surface) remains the Type; the **data supply business** over the same records belongs to the data-platform Types. Several sample products live on both sides simultaneously — the seam is the surface, not the data.

### vs CRM (§07)

CRM manages an organization's own relationship records and workflows (deals, activities, owners). A directory's entries are not relationships and carry no commercial workflow; the user's job is lookup, not progression.

## Uncertainties

- No Tier-1 help-center documentation was reachable for any commercial directory (see Source-access limitation). Common capabilities observed on only one sampled product (e.g. watchlist/follow at Companies House) are held at L1/L2 with hedged wording; none are promoted into the defining core.
- Review/rating integration, claiming mechanics, verification/accreditation machinery, and paid-placement rules are asserted only as family-level possibilities, not as observed mechanics of specific sampled products (Yelp/BBB/Google Business Profile were unreachable).
- Whether Member Directory (§25) should merge into this Type is an open taxonomy question requiring its own evidence pass.
- The exact upstream data flows for aggregated directories (e.g. Whitepages' identity graph construction) were not researched and are not needed for the Type definition.

## Final Synthesis

Canonical Directory Application:

```text
L0 (defining invariant)
- defined entity class
- standing entry per entity of the class
- attribute profile with identity + reach attributes
- catalog retrieval organization (browse + search, incl. attribute/reverse keys)

L1 (common mature structure)
- entry detail surface
- reverse/multiple lookup keys
- geographic axis
- faceted/advanced search
- entry lifecycle states
- derived/related directories
- API data supply

L2 (variant / optional)
- entity class (people / business / company / agency / bounded population)
- sourcing model (editorial / claimed / statutory / aggregated)
- business model (free / ads / freemium / data licensing)
- verification posture; content layers; review layers; print companion
- drift orbits (marketing services, identity/fraud data, entity verification)
```

The Application Document presents the defining core and the common structure in natural language; vendor specifics remain here.
