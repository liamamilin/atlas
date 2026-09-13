# Vertical Search Engine

## Overview

A **Vertical Search Engine** is a search application whose retrieval corpus is narrowed to a single domain — job openings, classified ads, properties, products, scholarly literature, images — and whose results present the items of that domain in the domain's own vocabulary, pointing the user to the source that holds each item.

The general-purpose web search engine answers "what is out there, anywhere". A vertical search engine answers "what is out there **in this domain**, expressed in this domain's terms". Its query structures, result records, and ordering all speak the language of the vertical: a job search engine queries by keywords, location, contract type, and salary; a property search engine by place, price, and layout; a classifieds search engine across cars, homes, and jobs under one roof.

The defining core is small:

```text
Query-first entry
└── A corpus narrowed to one domain, held and operated by the engine itself
    └── The engine's own ordering over that corpus
        └── Domain-shaped results that are references to the items' sources
```

Remove the narrowing and the product is a general web search engine. Remove the corpus it operates and the product is a metasearch relay. Remove its own ordering and it is an unranked aggregator or a directory. Make the engine hold and fulfill the items themselves and it has become a marketplace, board, or venue of a different Application Type.

## Users & Context

**Demand side — consumers seeking one kind of item within one domain.** Job seekers, home hunters, car buyers, bargain hunters, students, and researchers open the product to run a query against the domain's pooled supply and see what exists across many sources at once. Sessions are typically short and query-shaped: enter what and where, scan the results, open the promising items at their sources, leave. Little persists on this side beyond saved searches and alerts.

**Supply side — the parties whose items fill the corpus.** Operators of job boards, agency sites, classifieds portals, and merchant sites want their items found. They submit or feed their sites for indexing, monitor which of their items appear, and buy promotion — better placement, per-click or per-outcome campaigns — to move ahead in the ordering. The search engine is, from their side, a traffic channel into their own properties.

**Third-party publishers** embed the search machinery itself — a search box and result feed — on their own sites, extending the engine's reach beyond its own surface.

The typical deployment is a public web or app surface scoped to one or more markets (usually organized per country or language), with the supply-side machinery behind a separate, business-facing entry.

## Core Model

### The Defining Core

Four structures, jointly held, define the Type:

**1. Query-first entry.** The primary act of use is a user-composed query against the vertical — free-text terms, structured domain attributes, or both — not browsing a catalog, posting content, or maintaining a list. The query, not the hierarchy, is the front door. Without this, the product is a directory or a browse-first listing site.

**2. A narrowed corpus, operated by the engine as its own.** The engine collects the items of one domain into a database or index it holds and refreshes — job listings from job boards and agency sites, ads from classifieds portals, records from domain sources. Two separations are packed into this structure. First, the corpus is **narrowed**: bounded to one domain rather than the open web — this is the Type's defining difference from the general web search engine. Second, the corpus is **its own**: collected and held by the engine, not fetched from other search services at the moment of search — this separates it from metasearch. How the corpus is acquired (crawling the web, ingesting feeds, taking source submissions) varies by product and era; that the engine holds and operates the corpus does not.

**3. The engine's own ordering.** Results come out in an order the engine computes — relevance ranking is commonly the default, with domain sorts such as newest-first or salary-first offered to the user. Without its own ordering, the product is a raw feed or a hand-curated directory.

**4. Domain-shaped results that are references, not the items themselves.** Each result presents the item in the vertical's own vocabulary — salary and contract type, price and location, attributes specific to the domain — usually with only an excerpt of the item's content, and hands off to the source where the item actually lives: the original listing, the advertiser's site, the seller. The engine points; the source holds and fulfills. This is what keeps the product a search engine rather than a venue: if the engine begins holding the items and completing the transaction itself as its defining work, it has drifted into marketplace or board territory.

### Standard Capabilities of Mature Products

Most of what users associate with these products is layered capability, not definition:

- **Domain-shaped query filters** — the vertical's own attributes exposed as structured search controls: contract type and working hours and salary range for jobs, price and attributes for property and classifieds, category restrictions, exclusion terms, distance radius around a location.
- **Attribute-rich result records** — each result carries the fields that matter in the domain (salary with currency and pay period, structured location, company or seller, category, posting date) rather than a bare page title and URL; the item's content appears as a short excerpt only.
- **Per-market scoping** — the product operates as a set of country- or language-scoped interfaces, with the corpus, defaults, and vocabulary localized per market.
- **Location handling as first-class behavior** — places are matched, structured hierarchically, and disambiguated explicitly when a query's location is ambiguous or unmatched.
- **Tracked outbound handoff** — the link out to the source passes through the engine, carrying attribution, so the engine can measure and monetize the referral.
- **A domain taxonomy applied by the engine** — items classified into the engine's own category system, with browsable entry points (by keyword, by place, by company) alongside free query.
- **Search machinery syndication** — the retrieval surface published to third-party publishers through partner programs and APIs, with per-publisher attribution.

### One Structure, Several Realizations

```text
Corpus acquisition:   web crawling   ·   feed ingestion from sources   ·   source submission and review
Query form:           free-text terms   ·   structured domain attributes   ·   both combined
Result unit:          the domain item's record (job, ad, property, product, record)
Handoff:              tracked link out to the source holding the item
Market structure:     per-country sites   ·   multi-country single interface   ·   API-only
```

A reader who has only met one kind of vertical search engine — say, job search — should be able to recognize the property, product, or scholarly variants from the same core: the domain changes, the four structures do not.

## How It Works

### The retrieval loop

```text
Enter a query (terms + domain attributes + place)
→ the engine matches against its narrowed corpus
→ results are ordered by the engine's own ranking
→ results are presented as domain-shaped records
→ the user opens an item → tracked handoff to the source
→ done: the engine's work ends at the reference
```

### Collecting and maintaining the corpus

Before any query, the engine accumulates its domain: it crawls the web for the domain's items, or ingests feeds and submissions from the sites that publish them — commonly a mix, with one method dominant. Collection is continuous, because the corpus is time-sensitive: listings expire, prices change, postings close. The engine rescans sources on a cycle, adds newly found items to the index, and drops stale ones. This corpus maintenance — not content hosting — is the engine's ongoing work on the supply side.

### The supply-side loop

```text
Source submits its site / feed for inclusion
→ the engine reviews and admits it
→ the source's items enter the corpus
→ the source monitors its listings' presence and performance
→ optionally buys promotion (placement, per-click, per-outcome)
→ the engine's referral links track what came from whom
```

Inclusion is typically free but **reviewed** — the engine admits sources that genuinely publish domain items, and removal paths exist for sources that leave. Promotion is where monetization concentrates: the supply side pays to compete within the ordering, not for basic inclusion, and consumers are not charged for searching.

### Standing queries

Many products let a user convert a search into a watch: the query is saved, and when new corpus items match, the user is notified through alerts or a digest. The standing query is the same retrieval loop fired over time.

## Interfaces

**Query surface (home/search).** The entry surface: a prominent query box over the domain's vocabulary, accompanied by the domain's structured filters (place, salary or price, type, category) and entry points into browsable views (by category, by location, by company).

**Results list.** The product's central surface: an ordered list of domain-shaped records — title, key attributes (salary, price, place, date, type), source, content excerpt — with sort controls (relevance, date, domain metrics) and filter refinement alongside. Each record is a doorway, not a destination.

**Item handoff.** Leaving the product: the user opens a result and is taken to the source's own page for the item — the listing, the advertiser, the seller — through the engine's tracked link. Any application, purchase, or booking that follows happens on the source's surface, not the engine's.

**Alerts management.** The user's persistent surface: saved searches with their criteria, notification settings, and unsubscribe controls.

**Supply-side console.** The business-facing surface: submit a site or feed for indexing, check the status of inclusion, view which items are listed and how they perform, configure promotion campaigns (duration, budget, bid level), and see referral statistics.

**Publisher / API surface.** Programmatic access to the retrieval machinery itself: authenticated query endpoints returning domain-shaped result records for embedding in third-party sites and applications, with per-publisher attribution built into the outbound links.

**Market entry.** A per-country or per-language switch that moves the user into a separately scoped interface with its own corpus slice and localized defaults.

## Important Rules / Behaviors

- **Results are references, not custody.** The canonical product does not host the items it finds; it redirects to the source. This is structural, not incidental — it is what keeps fulfillment, liability, and the transaction loop on the source's side.
- **The corpus is perishable.** Items have lives of their own (a posting closes, a car sells, an ad expires); the engine's collection cycle and staleness handling are part of its core operation, and stale results are a real failure mode users encounter.
- **The ordering is the product.** Relevance is the default; the user can usually re-sort by domain metrics (date, salary, price). The engine does not promise neutrality or explain its signals; what promotion does and does not affect is a product policy, not a given.
- **Outbound links are engine-mediated.** The handoff passes through the engine's own link domain for attribution and monetization; the destination is still the original item.
- **Inclusion is reviewed, not automatic.** A source's request to be indexed is subject to review; feeds may ease collection but are usually not required for a crawlable site.
- **Ambiguous locations are surfaced, not silently resolved.** A query location that matches nothing or several places produces an explicit disambiguation step before any search runs.
- **The consumer side is not the revenue side.** In the researched products, searching is free to the end user; the economics run through the supply side and the tracked referral.

## Variants

- **Single-vertical vs multi-vertical.** The common shape concentrates on one domain (jobs is the classic); some products run several verticals — properties, cars, jobs, general products — under one brand and one machinery, with the vertical as a switchable corpus slice.
- **Corpus acquisition mix.** Crawl-led products that scan the web for items; feed-led products built on managed source agreements; submission-plus-review products; and undocumented mixes.
- **Monetization architecture.** Supply-side promotion (fixed placement boosts, per-click on the apply/visit action, per-outcome per application), paid posting for sources, publisher revenue share; some verticals in the wider family run with no visible monetization.
- **Data products over the corpus.** Some engines compute and sell domain intelligence from their own index — salary or price distributions, regional supply, top sources — turning the corpus into an analytics asset beyond retrieval.
- **Adjacent supply-side layers.** Recruiter or seller tooling (paid posting, résumé or inventory search, integrations) packaged alongside the engine; present in some products without changing the retrieval center of gravity.
- **Surface shape.** Consumer web and app fronts, publisher-embedded widgets, and programmatic APIs are peer realizations of the same machinery.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| General Web Search Engine | family sibling | corpus is the open web, unbounded by design; a vertical narrows the corpus to one domain and shapes query and results in the domain's vocabulary. An engine offering both is assigned by its default surface — vertical tabs on a general engine are scoped views, not separate products |
| Metasearch Engine | family sibling | fetches and merges result lists from other search services at query time and holds no corpus of its own; a vertical holds and orders its own corpus. The two dimensions are independent — a metasearch can be domain-narrowed (travel) |
| Answer Engine | family sibling | primary output is a synthesized answer; a vertical's primary output is a ranked reference list |
| Shopping Search Engine | domain instance (commerce) | the commerce vertical, defined by its commerce supply chain — merchant feeds, product-identity normalization, purchase handoff — not by corpus narrowing alone |
| Academic Search Engine | domain instance (scholarly) | the scholarly vertical, defined additionally by bibliographic record structure (identity, citation graph, access rights) and its researcher population |
| Listings Platform | adjacent, straddles | both pool domain items; the listings platform's defining act is managed pooling of current offers (feed agreements, inclusion and expiry lifecycle), while retrieval over a collected corpus defines this Type. Aggregator products can sit on this seam and are assigned by center of gravity |
| Job Board | adjacent (jobs domain) | a posting venue: employers post, applications run on the platform; a job search engine retrieves across many sources and hands off to them. Posting packages sold by search engines are additive layers, not a change of center |
| Directory Application / Information Portal | adjacent | standing, hand-curated records vs transient ranked retrieval over a live collected corpus |
| Enterprise Search / Search Platform | adjacent | operates on an organization's internal, permissioned corpus with member identity; a vertical's corpus is a public domain corpus with open access |
| Content Aggregator | adjacent | syndicates content into a consumption surface (streams, readers); a vertical search retrieves references out on demand, query-first |
| Web Browser | adjacent | the client surface that routes queries to the engine; distribution integration is common, not definitional |

## Representative Products

- **Careerjet** — worldwide job search engine; the pure retrieval pole: crawls and re-scans tens of thousands of source sites, hosts nothing, redirects every result to the original listing, and syndicates its search machinery to publishers via API.
- **Trovit** — multi-vertical classifieds search engine (properties, cars, jobs, products) across dozens of country markets; the multi-vertical pole of the same machinery over pooled classified ads.
- **Adzuna** — jobs search with an API-first posture; documents its job-ad database, structured search parameters, tracked outbound links, and data products computed from its own corpus.

*(Indeed, the category's largest job search product, was unreachable during research and makes no evidentiary contribution to this document; it is noted only as market context.)*

## Sources

Research date: **2026-09-09**

Primary vendor surfaces (official product documentation):

- Careerjet — About us: https://www.careerjet.com/about-us · FAQs: https://www.careerjet.com/faqs · Recruiter indexing & promotion: https://www.careerjet.com/recruiter/indexing · Partner API: https://www.careerjet.com/partners/api
- Trovit (LIFULL Connect) — brand page: https://about.trovit.com
- Adzuna — API documentation: https://developer.adzuna.com/ · Overview: https://developer.adzuna.com/overview · Search endpoint: https://developer.adzuna.com/docs/search

Boundary framework cross-references (research notes of processed sibling types): general-web-search-engine, metasearch-engine, shopping-search-engine, academic-search-engine, listings-platform.

> Sourcing limitations: the largest job search product (Indeed) returned access denials on both its About and Help Center surfaces, and image-search verticals attempted for domain diversity timed out; no claims in this document depend on those sources. Adzuna's consumer-facing surfaces and self-description were not directly observed — its evidence is limited to its official API documentation. Vendor-displayed scale figures and prices are recorded as claims, not verified facts. Detailed evidence, cross-product comparison, and boundary analysis are in the paired Research Notes.
