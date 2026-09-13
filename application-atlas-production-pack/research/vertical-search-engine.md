# Research Notes — Vertical Search Engine

Research date: **2026-09-09** · Leaf: `vertical-search-engine` (DIRECTORY §02.02 Search) · Methodology v1.1

---

## Research Goal

Establish what a **Vertical Search Engine** is as an Application Type: how its defining act differs from its two processed §02.02 siblings (General Web Search Engine, Metasearch Engine), what its canonical core is, and how the four pre-registered boundary flags from sibling passes (general, metasearch, shopping, academic, listings) should be resolved.

## Initial Boundary (hypothesis before research)

The §02.02 family framework recorded by the general-web-search-engine pass proposes three defining acts: single-corpus algorithmic ranking (general), combining other engines' result lists (metasearch), and **narrowed corpus scope (vertical)**. The metasearch pass ratified "orthogonal discriminators — vertical is about corpus *scope*, metasearch about corpus *posture*". Working hypothesis: the vertical's core is the search-engine family core (query-first entry, own operated corpus, own ranking, ranked outbound results) plus corpus narrowing as the defining act — with center-of-gravity assignment for straddling products.

Adjacent leaves pre-identified: Shopping Search Engine (§05.05, commerce instance), Academic Search Engine (§23, scholarly instance), Listings Platform (§02.11, aggregator pole Trovit), Job Board (§09), Enterprise Search / Search Platform / Internal Knowledge Search (§10/§13), Directory Application / Information Portal (§02.11), Answer Engine (§02.03, unprocessed), Web Browser (§02.01).

## Research Questions

1. How do real products self-label? Does the market actually say "vertical search engine"?
2. What is the corpus — narrowed to what, and how is it built (crawl / feeds / submissions / licensed)?
3. What is the query surface — free text only, or domain-shaped structured filters?
4. What is the result unit and presentation — raw documents or domain-shaped records?
5. What ordering/ranking machinery is documented?
6. What is the handoff — do results stay in the product or point to the source?
7. What supply-side machinery exists (inclusion, removal, promotion, tracking)?
8. What separates a vertical from: general engine, metasearch, shopping search, academic search, listings platforms, directories, job boards?

## Representative Products

| Product | Domain | Why sampled |
|---|---|---|
| **Careerjet** | jobs, worldwide | Self-labeled "job search engine"; pure retrieval pole (does not host items); crawler-first supply; full partner API docs |
| **Trovit** | multi-vertical classifieds (homes, cars, jobs, products) | Self-labeled "vertical search engine" verbatim; multi-vertical pole; the listings-platform pass's flagged aggregator |
| **Adzuna** | jobs | API-first challenger; documents its job-ad database, search parameters, and derived data products |
| *(Indeed — jobs, global market anchor)* | — | Unreachable this pass (403 ×2). Listed for market context only; **no claims made from it** |

TinEye and Openverse (image/media verticals, attempted for domain diversity) timed out twice each and were abandoned per the retry rule. Domain diversity therefore rests on the multi-vertical sample (Trovit) plus the ratified family seams from the sibling passes.

## Sources

Tier 1/2 official surfaces, fetched 2026-09-09:

- Careerjet — About us ("What we are"): https://www.careerjet.com/about-us — self-label, corpus mechanics, handoff policy (A)
- Careerjet — Recruiter indexing / promotion: https://www.careerjet.com/recruiter/indexing — supply-side promotion tiers (A)
- Careerjet — FAQs: https://www.careerjet.com/faqs — indexing admission, feeds-optional, alerts, apply-on-original (A)
- Careerjet — Partner API: https://www.careerjet.com/partners/api — query parameters, sort modes, job record schema, location-disambiguation response (A)
- Trovit (LIFULL Connect) — brand page: https://about.trovit.com — verbatim self-label, verticals, history, scale claims (A)
- Adzuna — Developer API Welcome: https://developer.adzuna.com/ (A)
- Adzuna — API Overview: https://developer.adzuna.com/overview — endpoints, corpus reference, categories (A)
- Adzuna — API Search endpoint: https://developer.adzuna.com/docs/search — query parameters, result-record schema, redirect_url (A)

Unreachable / abandoned (recorded per evidence rules):

- Indeed — https://www.indeed.com/about (403), https://support.indeed.com/hc/en-us (403) — the category's largest jobs product; **no operational claims from memory**
- Adzuna — https://www.adzuna.co.uk/about (empty ×2), https://www.adzuna.com/about (405) — self-label not directly observed; positioning rests on developer docs only
- Careerjet — about.html (404 both ccTLDs; live page is /about-us)
- TinEye — https://tineye.com/how, https://tineye.com/ (timeouts ×2)
- Openverse — https://openverse.org/, https://docs.openverse.org/ (timeouts ×2)

Cross-pass evidence (layer B, from processed sibling research notes in this repo): research/general-web-search-engine.md, research/metasearch-engine.md, research/shopping-search-engine.md, research/academic-search-engine.md, research/listings-platform.md.

Evidence layers: **A** = directly observed on an official product surface this pass; **B** = cross-product commonality (two or more products, or one product + ratified sibling-pass observation); **C** = canonical inference from comparison and boundary reasoning.

---

## Product Observations

### Careerjet (jobs, worldwide) — evidence A

- Self-label: **"Careerjet is a job search engine designed to make the process of finding a job on the internet easier for the user."** Explicitly "not a recruitment agency".
- Corpus: "maps the huge selection of job offerings available on the internet **in one extensive database** by **referencing job listings originating from job boards, recruitment agency websites and large specialist recruitment sites**."
- Corpus building: "smart agents running on a cluster of networked computers that **scan the web and identify job listings**… Those listings are then **scanned daily and the jobs found are added to the job index**." Scale claim: over 58,000 websites scanned every day (vendor-displayed).
- Handoff: "The job offerings themselves are **not hosted by Careerjet** and users are **always redirected to the original job listing**. Essentially, Careerjet acts as traffic driver to those sites."
- Network shape: 90+ countries, separate interfaces, 28 languages (vendor-displayed).
- Supply side (FAQs + indexing page): sites are indexed after **free submission and review** ("Just submit your website for free. We will review it and confirm when your jobs are listed."); **feeds optional** ("Getting a feed may make things easier, but it is not necessary… We should be able to index your jobs even if you cannot provide one"); all feed types accepted.
- Supply-side promotion (indexed page): Easy Boost (campaign over listed jobs), **PPC** ("only pay when candidates click to apply directly on your site", vendor-displayed from $3.00/click), **PPL** (per application, vendor-displayed from $5.00), programmatic contact route. Precise figures are vendor-displayed claims.
- Consumer side (FAQs): job **alerts** exist (account-level, per-query alerts, unsubscribe flow); **apply happens on the job description page** via the apply button, i.e. handoff to the source; resumes can be uploaded (recruiter-side resume search is sold separately).
- Retrieval machinery (partner API, documents the same machinery publishers embed): endpoint `search.api.careerjet.net/v4/query`; parameters — `keywords`, `location`, `contract_type` (permanent/contract/temporary/internship/volunteering), `work_hours` (full/part), `radius` (default 5 km/miles), `sort` (**relevance** default; date; salary), `locale_code` per-country, paging; response carries `type: JOBS` with hits/pages, or `type: LOCATIONS` with candidate locations ("no matching location found" / "multiple locations found" — location disambiguation as a first-class response mode).
- Result record schema: title, company, date, description **excerpt**, locations, salary (min/max, currency, `salary_type` Y/M/W/D/H), and `url` on a **tracked outbound link** domain (`jobviewtrack.com`).

### Trovit (multi-vertical classifieds) — evidence A

- Verbatim self-label: **"Trovit is one of the world's leading vertical search engines for classifieds."** — the only in-sample product that uses the literal category name.
- Corpus: "**We centralize thousands of classified ads from thousands of Real Estate, Cars, and Jobs websites**, saving users the time it would take them to surf through all these pages individually."
- Verticals: Homes (2006) → Cars and Jobs (2007) → Products (2010). Per-country sites across 50+ countries; mobile apps listed.
- Scale claims: 63M users/month, 57 countries, 92M listings, publisher network (vendor-displayed numbers; the publisher figure rendered incompletely on the page — recorded as displayed, not asserted).
- History: founded Barcelona 2006; acquired by LIFULL (2014/2017); merged with Mitula Group into LIFULL Connect (2019).
- Consumer result surface and corpus-acquisition mechanics were **not on the fetched pages**; the listings-platform pass (2026-09-07) documents supply as partner feed inclusion with opt-out/removal — cross-pass observation, held as B-layer evidence.

### Adzuna (jobs) — evidence A (developer surfaces only; consumer surface unobserved)

- Positioning (developer docs only): "Search **Adzuna's full listings of job adverts** using keywords and locations"; "Adzuna's search function and **massive database of ads**". The literal self-label "search engine for jobs" was **not** directly observed (about page unreachable) — positioning statements kept at this strength.
- Corpus reference: "our database of job ads"; categories are a product-side structure: "the categories that **Adzuna applies** to jobs".
- Retrieval machinery (REST API, 9 endpoints): search endpoints with `what`, `what_exclude`, `where`, `salary_min`, `full_time`, `permanent`, `sort_by=salary`, `results_per_page`, per-country path (`/jobs/gb/search/1`), `app_id`/`app_key` auth.
- Result record schema: salary_min/max, `salary_is_predicted` flag, hierarchical `location.area` array (UK → South East England → Buckinghamshire → Marlow) with display_name, description **snippet** ("we currently only provide a snippet of the job description"), `created` timestamp, `title`, `category` (label + tag), `company.display_name`, `contract_type`, numeric `id`, and a **tracked `redirect_url`** (`adzuna.co.uk/jobs/land/ad/…` with per-publisher attribution parameters).
- Derived data products: salary data, historical salary series, salary histogram, regional vacancy counts, top companies — labour-market intelligence computed **from the corpus**; XLSX/JSON/JSONP/XML/HTML encodings.

---

## Cross-product Comparison

| Structure | Careerjet | Trovit | Adzuna | Layer |
|---|---|---|---|---|
| Self-label as a search engine over one domain | "job search engine" (A) | "vertical search engine for classifieds" (A) | "search function" over "database of ads" (A; full self-label unobserved) | B |
| Query-first entry (keywords + location) | A (consumer nav + API) | A (per-country sites; consumer page not fetched) | A (API `what`/`where`) | B |
| Corpus narrowed to one domain vertical | jobs (A) | homes/cars/jobs/products (A) | job ads (A) | B |
| Corpus held as the product's own database/index | "one extensive database… added to the job index" (A) | "centralize… ads" (A) | "our database of job ads" (A) | B |
| Corpus built by collecting third-party items | daily web scan, 58,000+ sites (A); feeds optional (A) | centralized from thousands of websites (A); feed inclusion per listings pass (B) | mechanism not documented in fetched pages | B (mechanism varies) |
| Domain-shaped query structures | contract type, work hours, radius, locale (A) | per-vertical attributes (not itemized in fetched pages) | salary bound, contract, category, exclusion terms (A) | B |
| Domain-shaped result record | title/company/date/salary+currency+period/locations/excerpt (A) | ad records per vertical (fetched page does not itemize) | salary min-max+prediction flag/location hierarchy/category/contract/company/created (A) | B |
| Own ordering, relevance default | `sort` relevance default; date; salary (A) | not documented in fetched pages | sort-by parameter incl. salary (A); relevance default unobserved | B |
| Results are outbound references to the source | "not hosted… always redirected to the original" (A) | aggregator pattern per listings pass (B) | tracked `redirect_url` (A) | B |
| Tracked outbound handoff links | jobviewtrack.com domain (A) | not observed this pass | `land/ad/…` + attribution params (A) | B |
| Per-country / market scoping | 90+ countries, 28 languages, `locale_code` (A) | 50+ countries, per-country sites (A) | per-country API path (A) | B |
| Location disambiguation as behavior | LOCATIONS response mode (A) | not observed | hierarchical location display (A) | B |
| Search alerts | A (FAQs) | not observed | not observed | single-product → optional |
| Supply-side admission review | submit + review + confirm (A) | feed inclusion w/ opt-out (B, cross-pass) | not observed | B |
| Supply-side promotion economy | boost / PPC / PPL / programmatic (A) | not observed this pass | not observed | single-product → variant |
| Search machinery syndicated to publishers | publisher program + partner API (A) | publisher network claim (A, undetailed) | API for third-party sites (A) | B |
| Multi-vertical product shape | no (single domain) | yes (4 verticals) | no | variant |
| Derived domain data products | no (resume search is recruiter-side) | no | yes (salary/histogram/regional/top-companies) | single-product → optional |
| Recruiter-side additive layers | posting packages, resume search, ATS integrations (A) | not observed | labour-market intelligence for organizations (A) | variant |

## Canonical Abstraction

### L0 — Defining Invariant

A Vertical Search Engine is a query-first retrieval application whose defining core is exactly four jointly-held structures:

1. **Query-first entry** — the primary act of use is the user-composed query over the vertical, not browsing or posting; query structures may be free text, structured domain attributes, or both. *(Remove → a directory/portal or browse-first listing surface.)*
2. **A retrieval corpus narrowed to one domain vertical, operated by the product as its own** — the product collects and holds the domain's items in its own database/index (however acquired: web crawling, feed ingestion, source submission); the narrowing to one domain is the defining act that separates this Type from the general engine, and the corpus ownership is what separates it from metasearch. *(Remove the narrowing → General Web Search Engine; remove the ownership → Metasearch relay.)*
3. **The product's own ordering over that corpus** — results are ordered by the product's ranking/sorting machinery (relevance ordering observed as default; user-selectable domain sorts such as date or salary observed). *(Remove → an unranked aggregator feed or a directory of hand-curated records.)*
4. **Domain-shaped results that are references, not the items themselves** — each result presents the item in the vertical's own vocabulary (salary, location, category, attributes…) and hands off to the source holding the item; the engine points rather than fulfills. *(Remove the handoff → a venue/board/marketplace that holds the item; remove the domain shaping → a generic link list, not a vertical.)*

Jointly-held is load-bearing:
- 1 alone = directory/browse portal; 2 alone = a domain database nobody queries; 3 alone = ranking over nothing; 4 alone = a bare link list.
- 1+2 without 3 = unranked aggregator feed; 1+3 without 2 = re-ranking relay (metasearch's degenerate pole); 2+3 without 1 = a browsable listing venue without a retrieval center; 1+2+3 without 4 = the drift toward a marketplace/board that holds and fulfills the item.

Anti-overfitting — explicitly NOT in L0:
- **The jobs/classifieds domain** — the sample is domain-heavy, but the family framework (general, metasearch, shopping, academic passes) and the multi-vertical sample establish the Type as domain-generic; the corpus may be jobs, products, homes, images, scholarly records, or any other domain.
- **Web crawling as the acquisition method** — crawl-first (Careerjet), feed/submission ingestion (Trovit per listings pass), and undocumented mixes all hold an own corpus; acquisition method is a variant axis.
- **Precise ranking signals** — nothing beyond "relevance ordering, with selectable domain sorts" is evidenced; signal families are kept qualitative.
- **Ads/monetization, accounts, alerts, apps** — none are required; an API-only or minimal consumer engine satisfies the core.
- **"Outbound link + ad economics" as a business model** — the handoff is structural; the *monetization of* the handoff is a variant.

### L1 — Common Mature Structure

- **Domain-shaped query filters/facets** over the vertical's attributes (contract type, work hours, salary bounds, radius, category, exclusions — observed directly at two jobs products; per-vertical attributes asserted for Trovit at existence level).
- **Domain-shaped result records** carrying the vertical's key attributes in the result itself (salary with currency and period, hierarchical location, category, contract, company, date) with only an excerpt of the item's content.
- **Per-market scoping** — separate per-country interfaces/locales as the product's market structure (three of three sampled products).
- **Location handling as a first-class behavior** — disambiguation modes and hierarchical location structures (observed at two products).
- **Tracked outbound handoff** — results pass through engine-controlled redirect URLs carrying attribution parameters.
- **A domain taxonomy applied by the product** (categories applied to items, browsable keyword/location/company entry points alongside free query).
- **Search machinery syndication** — the retrieval surface distributed to third-party publishers via partner APIs/widget programs (observed at all three sampled products at existence level; documented in detail at Careerjet).
- **Saved queries as alerts** — a standing query that re-fires as new items arrive (observed at one product; treated as optional pending more evidence).

### L2 — Variant / Optional Structure

- **Single-vertical vs multi-vertical product shape** (Trovit carries four verticals under one brand; Careerjet/Adzuna single-domain).
- **Corpus-acquisition mix** — crawl-first with feeds optional (Careerjet), feed/partner-centric inclusion with opt-out (Trovit, cross-pass), undocumented (Adzuna).
- **Supply-side admission posture** — open submission with review (Careerjet) vs managed feed agreements (Trovit cross-pass).
- **Monetization architecture** — employer-side promotion tiers (boost/PPC/PPL, posting packages), publisher-side revenue share, no visible consumer charges in-sample; monetization may also be absent (commons-style poles exist in the wider family, unobserved this pass).
- **Derived data products** computed from the corpus (labour-market statistics; single-product observation).
- **Recruiter/seller-side adjacent layers** — posting, resume search, ATS integrations; additive, not definitional.
- **Consumer app surfaces** (mobile apps listed by two sampled products).

### L3 — Vendor-specific (research notes only)

- Careerjet: displayed prices ($130/30 days posting; PPC from $3.00/click; PPL from $5.00/application; resume search from $200/10 days — vendor-displayed claims); `fragment_size` default 120; page bounds 1–10 / page_size 1–100 default 20; `user_ip`/`user_agent` required parameters; `jobviewtrack.com` link domain; 58,000 sites/day and 90+ countries/28 languages claims; "Easy Boost" brand; `contract_type`/`work_hours` letter codes.
- Adzuna: `app_id`/`app_key` auth; nine-endpoint API taxonomy; `salary_is_predicted` flag; JSON/JSONP/XML/HTML/XLSX response encodings; `Jobsworth`; response class names; example salary figures in docs.
- Trovit: LIFULL Connect corporate history (2006 founding, 2014 NEXT acquisition, 2017 LIFULL rename, 2019 Mitula merger); 63M users/57 countries/92M listings display figures; per-vertical per-country site matrix; app store listings.

## Vendor-specific / Rejected Findings

- **"A vertical search engine is a job aggregator"** — rejected. The sample is jobs-heavy for reachability reasons; the literal self-label (Trovit) is multi-vertical and the sibling passes ratify shopping (commerce) and academic (scholarly) as instances of the same corpus-narrowing act. The Type is domain-generic.
- **"Vertical tabs of a general engine are separate vertical search engines"** — rejected as separate Types; ratified as scoped views. A general engine offering a narrowed surface (the Google Images pattern, per the general pass) does not become a different product type by the tab; assignment is by center of gravity (default surface = open web → general; default surface = the vertical → this Type).
- **"Crawling is what makes it a search engine (vs an aggregator)"** — rejected as an L0 criterion. Careerjet crawls; Trovit's supply is feed agreements (cross-pass); both are retrieval-centered products. Acquisition is variant, corpus ownership is invariant.
- **"Paid inclusion means it is not a search engine"** — rejected. Supply-side promotion economics (PPC/PPL on the handoff) ride on top of the retrieval core; no evidence in-sample that payment is required for inclusion (Careerjet indexing submission is free with review).
- **"A vertical search engine hosts the items"** — rejected for the canonical pole. The sampled pole states the opposite (items not hosted, users redirected). Hosted copies are incidental in family instances (the academic pass observed incidental OA hosting) but custody is not the defining act; when holding/fulfilling the item becomes the product, the Type has drifted to venue/board/marketplace territory.
- **"Vertical search = metasearch over one domain"** — rejected (ratifies the metasearch pass): scope and posture are orthogonal. A metasearch over a narrowed domain exists (travel) and is assigned to the travel leaves when domain objects and booking/handoff paths dominate.

## Boundary Findings

**vs General Web Search Engine (§02.02) — the family's primary seam (DISCHARGES the general pass's family flag from this side).**
The discriminator is corpus scope. The general engine's corpus is the open web by default, unbounded by design; the vertical's corpus is bounded to one domain, and its query/result structures are shaped by that domain. Single-subtraction test: remove the narrowing → general engine; add the narrowing → vertical. **Center-of-gravity rule ratified from this side** (the general pass's own rule): a product offering both surfaces is assigned by its default surface; vertical tabs inside a general engine are scoped views of the general Type, not instances of this Type. With this pass, the §02.02 family is processed except Answer Engine: general (scope-unbounded), metasearch (posture-aggregating), vertical (scope-narrowed); the answer-engine pass completes the family with the primary-output discriminator.

**vs Metasearch Engine (§02.02) — echoes and ratifies the metasearch pass.**
Orthogonal discriminators: vertical = corpus *scope*; metasearch = corpus *posture* (no operated corpus; query-time fan-out and merge of upstream services). A vertical engine holds and orders its own corpus; a metasearch fetches result lists at the moment of search. The two can co-occur (a domain metasearch is vertical in scope, metasearch in posture); the directory assigns such products by center of gravity, and the metasearch pass assigned travel products with domain objects + handoff to §26. Single-subtraction test: give the product an operated corpus as primary source → this Type; make query-time aggregation the defining act → Metasearch.

**vs Shopping Search Engine (§05.05) — DISCHARGES that pass's flag (keep-both, center-of-gravity seam ratified as proposed).**
A shopping search engine is the **commerce instance** of vertical search: it satisfies this Type's core (narrowed commerce corpus, own ordering, domain-shaped results) and additionally carries the commerce supply chain as its defining act — merchant/provider feed ingestion, product-identity normalization, per-click economics, and the purchase handoff. This pass's generic core deliberately contains no commerce machinery; the shopping leaf remains the commerce instance. Assignment stays by center of gravity: retrieval over a narrowed corpus without the commerce supply chain → here; with it → shopping leaf. No sampled product this pass sits on that seam.

**vs Academic Search Engine (§23) — DISCHARGES that pass's flag (keep-both).**
The scholarly instance is structurally a vertical search over the scholarly corpus and satisfies this Type's core. The separation the academic pass recorded is ratified from this side: the scholarly corpus carries a record structure the generic vertical concept does not require (bibliographic identity, citation graph, access rights), plus a distinct user population and tool ecosystem. The tension is real but is the same family-instance pattern already resolved for shopping: the generic core is intentionally minimal so that domain instances satisfy it, while the domain leaves carry their additional defining structures. Single-subtraction test: remove the scholarly-corpus restriction and the bibliographic record structure → a generic vertical; restrict to scholarly records → academic leaf.

**vs Listings Platform (§02.11) — DISCHARGES that pass's Trovit flag (keep-both, this side ratifies the listings hold).**
Trovit satisfies this Type's core and self-labels a vertical search engine; the listings pass held it there because its supply is by managed partner agreement (feed inclusion with opt-out/removal) and its units are offer listings with lifecycle and expiry states, not transient retrieval results. This side ratifies: the seam is the center of gravity — when the product's defining act is the **managed pooling of current offers** (standing supply relationship, inclusion/removal lifecycle, pooled-listing container), it is listings territory even when the surface is a search engine; when retrieval machinery over a domain corpus is the center (open crawling or openly submitted sources, retrieval as the defining act), it is this Type. Trovit straddles and stays in listings; Careerjet (open submission-and-review of sources, daily rescans, retrieval-centered self-description) documents this Type's pole. Both passes now agree on the hold.

**vs Job Board (§09) — family note for that pass.**
A job board is an employer posting venue: jobs are posted on the platform and applications are the platform's loop. A job search engine is query-first retrieval over a pooled corpus with outbound apply. The sampled pole states explicitly it is not a recruitment agency and acts as a traffic driver; yet it sells posting packages and resume search — additive layers whose presence does not move the center of gravity. When employer posting + on-platform application becomes the defining loop, the product is the Job Board leaf. **Job search engines are the retrieval-pole neighbor of the Job Board Type; recorded for the job-board pass's boundary work.**

**vs Directory Application / Information Portal (§02.11).**
Directories hold standing, hand-curated records; verticals compute transient ranked retrievals over a live collected corpus per query. Same seam the general pass drew; the vertical inherits it. Removal test: replace the product's own ordering over a collected corpus with human curation over a fixed catalog → Directory.

**vs Enterprise Search Platform / Search Platform / Internal Knowledge Search (§10/§13).**
Those operate on an organization's internal, permissioned corpora with member identity; the vertical's corpus is a public (or public-aggregated) domain corpus with open access. Same seam the general pass drew; scope narrowing does not move a product across it. Removal test: replace the domain corpus with the organization's internal sources → sibling Type.

**vs Answer Engine (§02.03, unprocessed).**
The vertical's primary output remains a ranked reference list; synthesized answers layered on results are additive (the general pass's AI-summary rule). The answer-engine pass should assign by center of gravity.

**vs Web Browser (§02.01).**
Browsers are client surfaces that route input to a destination service; the vertical is the destination. Distribution integration (browser defaults, apps) is common, not definitional.

**"去掉什么就变成另一个 Type" summary**: remove the corpus narrowing → General Web Search Engine; remove corpus ownership (fetch upstreams at query time) → Metasearch; add the commerce supply chain as the defining act → Shopping Search Engine; add the scholarly record structure and researcher ecosystem → Academic Search Engine; make managed pooled-offer supply + offer lifecycle the center → Listings Platform; make employer posting + on-platform application the loop → Job Board; replace own ordering with hand curation → Directory; internalize the corpus → Enterprise Search; promote synthesized answers to primary output → Answer Engine; hold and fulfill the items → marketplace/board/venue territory.

## Historical / Market-Sample Check (§24)

- **Pre-web subject databases** (biomedical-literature retrieval, commercial subject databases, legal retrieval services): query-first entry over a narrowed domain corpus, held and ordered by the operator, returning references to the source documents — all four L0 legs satisfied decades before the web, with Boolean/fielded retrieval and per-field sorts as the ordering machinery of the era. The definition holds; ranking sophistication is era-dependent, not definitional. *(Reasoned, not cited — no pre-web source was fetchable this pass.)*
- **Early-web crawler aggregators for jobs** — Careerjet's own description (scan many sites daily, add to a job index, redirect to the original listing) is effectively the description of the early-2000s generation; no separate era machinery is in the core.
- **Print-era and regional analogues** (classified ad papers with their own indexes; regional recruitment papers): query-first and algorithmic ranking are absent — they are listings media, not search engines; consistent with holding the aggregator pole in Listings Platform rather than here.
- **A human-curated link directory for one domain** fails L0 legs 1–3 (curation, not retrieval) → Directory.
- **A browse-first national job/classified board** fails leg 1 (posting venue, not query-first) and partially leg 4 (holds the items) → Job Board / Listings territory.
- The check passes: the definition is not overfitted to the 2020s cloud/consumer implementation.

## Uncertainties

1. **Indeed** — the category's largest jobs product — was unreachable (403 ×2). No claims made from it. If a later pass reaches its help center, re-verify the standard-capabilities list (filters, alerts, apply flow) against it.
2. **Adzuna's consumer surface and self-label** were not directly observed (about pages unreachable); its evidence covers the corpus and API mechanics only. Claims about Adzuna are held at developer-doc strength.
3. **Trovit's consumer result page and acquisition mechanics** were not fetched this pass; its inclusion leans on the verbatim self-label plus the listings pass's cross-pass observations (feed inclusion with opt-out). Result-page structure for Trovit is asserted at existence level only.
4. **Ranking signals** are undocumented across the sample beyond default relevance + selectable sorts; the document deliberately makes no signal-level claims.
5. **Deduplication of the same item across sources** (the same job advertised on many sites) is a plausible corpus problem for this Type but was **not observed** in fetched sources; left unverified, not claimed.
6. **Domain breadth of the sample**: media/image verticals (TinEye, Openverse) were unreachable; the direct sample covers classifieds/jobs only. Domain-generality rests on the multi-vertical sample plus the ratified family seams (shopping, academic, travel). An image-vertical product fetch would strengthen the L0.
7. **Alerts, location disambiguation, and admission review** are evidenced at one or two products each; they are held as optional/common-mature respectively, not definitional.
8. **Pre-web historical check is reasoned, not cited** (no archived source fetched); same limitation the general pass recorded.

## Final Synthesis

A Vertical Search Engine is the **corpus-scope member of the search-engine family**: a query-first retrieval application that collects the items of one domain vertical into a corpus it operates as its own, orders that corpus with its own ranking machinery, and answers with domain-shaped results that remain references to the items' sources — the engine points, the source holds. The defining act separating it from the general engine is the narrowing; the corpus ownership separating it from metasearch; the own ordering separating it from directories and unranked aggregators; the reference-not-custody result separating it from venues that hold and fulfill the item. Everything the market associates with mature products — domain filters and facets, attribute-rich result records, per-market interfaces, tracked redirects, categories, alerts, publisher APIs, supply-side promotion economies, derived data products — is common mature structure or variant layered on that core, and the domain instances (commerce, scholarly, travel) are held by their own leaves wherever an additional defining act (supply chain, record structure, booking handoff) takes over as the center of gravity.
