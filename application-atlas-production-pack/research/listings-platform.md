# Research Notes — Listings Platform (§02.11 Directories & Listings)

Research date: 2026-09-08
Slug: listings-platform
Methodology: v1.1 (update-v1/)

---

## Research Goal

Establish what the directory leaf **Listings Platform** (§02.11, Domain 02 "Content, Knowledge & Information") denotes as an Application Type, distinct from its in-family siblings **Directory Application** and **Information Portal** (§02.11), from the commerce-typed **Classifieds Platform** / **Listing Marketplace** (§05.03), and from vertical realizations typed elsewhere (**Property Listing Platform** §17, **Job Board** §09). This pass must also ratify the near-alias flag left by the listing-marketplace pass (§05.03, processed 2026-09-08).

## Initial Boundary (pre-research hypothesis)

- The §02.11 family organizes information surfaces. Sibling passes already propose the frame:
  - directory-application pass: "standing entity record vs expiring/consummable offer" is the in-family seam with Listings Platform.
  - information-portal pass: "offers with lifecycle vs ephemeral pointers".
  - job-board pass: Listings Platform = "the employment realization of the expiring-offer model" generalized (Job Board as vertical realization).
- Working hypothesis: Listings Platform = the generic offer-listings publication-and-discovery Type: pooled, structured, time-bound listings of things offered, published for search/browse discovery. Commerce machinery (connection/deal) is expected to be standard capability, not defining — which would ratify keep-both vs Listing Marketplace with a containment seam.
- Nearest confusions: Listing Marketplace (near-alias flag), Classifieds Platform (ad-centric sibling), Directory Application (standing records), Vertical Search Engine (aggregator pole), single-seller storefronts.

## Research Questions

1. What is the unit of record (the listing), and what does it carry?
2. How does the pooled inventory get built — who supplies listings and through what machinery?
3. What does seeker-side discovery look like (search/browse/filter/alerts/map)?
4. What lifecycle does a listing have (entry → update → retirement)?
5. What happens at the seeker→lister edge — is connection machinery defining or variable?
6. How is the platform monetized, and from which side?
7. What rules govern listings (accuracy, prohibited content, moderation, staleness)?
8. Where exactly are the seams vs Directory Application / Information Portal / Classifieds / Listing Marketplace / Vertical Search Engine / single-seller storefront?

## Representative Products

Selected for market representativeness, documentation completeness, differing product philosophy (professional-membership vs self-serve vs pure aggregation), differing lister admission policy, and geographic spread:

| Product | Market | Vertical | Lister admission | Evidence |
|---|---|---|---|---|
| Rightmove | UK #1 property portal | residential/commercial property | professional membership only (agents, developers, rental operators; overseas private sellers) | Tier-1 (help centre Freshdesk + advertise/professional pages) |
| realestate.com.au (REA) | AU #1 property portal | residential/commercial property | professional only (agents, developers, property managers) | Tier-1 (REA Support Zendesk: Agents & Developers + Renters categories) |
| OpenRent | UK rentals | residential lettings | private landlords only (no agents) | Tier-1 (FAQ page, detailed) |
| Trovit | multi-country, multi-vertical aggregator | homes/cars (also jobs per product title) | none direct — partner-portal feed inclusion | Tier-1 (help centre Zendesk) |

Unreachable this pass (recorded per source-access rules; 403s): Zoopla, AutoTrader UK, Zillow, Cars.com, Indeed. This matches the prior listing-marketplace pass's limitation (US/DE portals unreachable). No product claims are asserted for unreachable products.

## Sources (fetched 2026-09-08)

- Rightmove Help Centre — https://faq.rightmove.co.uk/support/home/ ; tools folder https://faq.rightmove.co.uk/support/solutions/folders/7000041938 (search, Keyword Sort, Property Alerts, Draw a Search, Sold Prices, valuation tool, School Checker)
- Rightmove professional/advertising — https://www.rightmove.co.uk/for-agents.html (membership classes incl. Estate & Letting Agency, New Homes Developers, Rental Operators/BTR, Commercial, Overseas incl. private sellers; membership T&Cs, Member Classification Guidelines, Agent & Developer Technical Guidelines, Data Quality Course of Action, Fraud Course of Action)
- REA Support — https://help.realestate.com.au/hc/en-us ; Agents & Developers category https://help.realestate.com.au/hc/en-us/categories/49055732021017 (Agent Admin; listing uploader/CRM/API partner incl. REAXML documentation and update-cadence article; downloadable documents on listings; agency branding incl. Suburb Sponsorship; agent/agency profiles & reviews; Ignite agent workspace incl. listing search, Upcoming Inspections, Notifications Hub, Centralised Reporting; Seller Leads incl. Enriched Seller Leads; subscriptions Premiere+/Essentials/Basic, Audience Maximiser packages; CMA/Market Insights/Property Profiles; Max Bid for auctions; Realtair Pitch/Sign+/Pay Now); Renters category https://help.realestate.com.au/hc/en-us/categories/49055849242265 (Renter Profile with employment/income/address history; rental application apply/status/withdraw/pets; Tenant Check; state rental-law compliance guides)
- OpenRent FAQ — https://www.openrent.co.uk/faq (free advertising, paid portal syndication to Rightmove/Zoopla, Rent Now tenancy creation, holding deposit flow, masked email, viewing arrangement + reminders, verified UK phone requirement, landlord ownership verification, "advertise until let" + fair-usage policy, listing propagation delays incl. portal syndication lag, alerts-notify-once-on-first-list, location-on-map correctness governs findability, private-landlords-only admission, rental valuation calculator from own listing data)
- Trovit — homepage https://www.trovit.co.uk/ ("A classified search engine for property, jobs, cars and products"; "Ads from thousands of websites in just one search"; Lifull Connect); Help Center https://help.trovit.com/hc/en-gb (categories incl. Issues with ads, Problems making contact, Report a problem, Trovit for businesses; promoted: contact the poster, found an expired ad, ad without contact info, advertise on Trovit); article "I want to advertise on Trovit" https://help.trovit.com/hc/en-gb/articles/211533489 (feed inclusion via partner product site for portal owners; otherwise publish on a site Trovit already shows; deletion/opt-out article present)

## Product Observations

### Rightmove (evidence layer A)

- Seeker surface: homepage search bar "area, postcode or station" with "For sale" / "To rent" buttons — the offer-type split is the top-level organization. Property Alerts (register with free account), Keyword Sort (personalize ranking by features), Draw a Search (map outline + schools/parks/transport overlays), Sold Prices, School Checker, mortgage/affordability calculators, valuation tool (routes seller to local agents — a lead path).
- Lister admission: professional membership classes only — Estate & Letting Agents, New Homes Developers, Rental Operators incl. Build to Rent, Commercial, Overseas (incl. Overseas Private Seller T&Cs). UK private sellers/landlords are explicitly routed to "choose any estate/letting agent that advertises on Rightmove" — they cannot list directly.
- Lister-side machinery: Rightmove Plus professional hub; Agent & Developer Technical Guidelines (feed-based listing supply); Data Quality Course of Action and Fraud Course of Action (governance of listing content); Member Classification Guidelines; display-advertising products (schools, home products/services).
- Data layers: Sold House Prices, House Price Index, Data Services (property data supply).
- Monetization: memberships + display advertising; not per-transaction.

### realestate.com.au / REA (evidence layer A)

- Audience split of the help centre mirrors the platform's two-sidedness: Agents & Developers / Property Managers / Renters.
- Listing supply: professional consoles (Agent Admin, Ignite) + "listing uploader (CRM) or API partner" — listings flow in from agency CRMs via a documented XML format (REAXML), with a documented update-cadence article ("How often does a listing uploader send updates to us?"); downloadable documents attachable to listings; "Listing Live" notifications to listers (being retired — lifecycle signal).
- Seeker surface: search incl. "AI search" (era-current), renter profiles (employment/income/address history), rental applications (apply, check status, withdraw, add pets), Upcoming Inspections surfaced from listings.
- Connection/commerce machinery: Seller Leads machinery (assignment, enrichment, reports, enquiry notifications) — managed lead path to listers; rental application pipeline; Tenant Check reports; Max Bid for auctions; Realtair transaction-adjacent services (Pitch/Sign+/Pay Now).
- Monetization: subscription tiers (Premiere+/Essentials/Basic), Audience Maximiser ad-hoc packages, Suburb Sponsorship banner products, agency/agent profile subscriptions (Elevate), reviews layer (agent ratings on listing pages; Google Business Profile syndication).
- Data layers: Comparative Market Analysis, Market Insights, Property Profiles.
- Regional regulatory machinery: state-by-state rental law change compliance guides (AU states).

### OpenRent (evidence layer A)

- Lister admission: private landlords only ("we can only accept listings from private landlords"; company/housing-association owners accepted; letting agents rejected) — the inverse policy of Rightmove/REA.
- Listing creation: self-serve ("Add Listing"; landlord-authored advert; fast to compose), free on OpenRent itself; paid upgrade syndicates the same advert to Rightmove/Zoopla — portal syndication as a paid layer, with the syndication lag documented (hours) and the note that only registered agents can list there.
- Lifecycle: "We will advertise your property until let" with a fair-usage policy; new-listing event triggers tenant alerts exactly once (on first listing); recommended lead time before vacancy documented on their blog; search indexing has caching delay.
- Discovery: location-based search ("a search works by the user entering a location... if your property is within this area, then your property will appear" — map-location correctness is the governing findability attribute, not the title); commute-time search; alerts.
- Seeker→lister contact: viewing booking on the listing page; enquiries via portals handled by OpenRent and relayed to the landlord through masked email; landlord records viewing date/time; reminders to tenants; "chase" control for unresponsive landlords; verified UK phone number required to advertise/book viewings/pass screening (anti-spam rationale).
- Trust machinery: landlord ownership verification ("systems in place to verify that a landlord owns the property"), verified-tenant product, verified-landlord badge via Rent Now, rogue-landlord defences (funds handling), deposit-protection compliance.
- Transaction-adjacent layer: "Rent Now" tenancy creation — tenant places a holding deposit on the listing page → landlord accepts/rejects → referencing → contracts → deposit protection → rent collection. The platform explicitly separates advertising ("use OpenRent for advertising and retain access to any of our other services") from tenancy creation — landlords who find tenants elsewhere can skip it.
- Monetization: free listings + paid upgrades (syndication, tenancy creation, referencing, insurance, certificates, photography...) — lister-side services on a free-advertising core; tenant side free.
- Data layer: rental valuation calculator derived from own accumulated listing data.

### Trovit (evidence layer A)

- Self-positioning: "A classified search engine for property, jobs, cars and products"; "Ads from thousands of websites in just one search". Operates many country editions (30+), part of Lifull Connect.
- Supply model: no direct lister self-service. Owners of classifieds portals include their ads via the partner product site (feed inclusion); individuals are told to publish on one of the sites Trovit already indexes — "even if your ad is hosted on a different website, it will appear on our search results". Opt-out/removal article ("I don't want my ad to appear on Trovit. How can I delete it?") — inclusion is managed, not open-web-crawled (explicitly distinguished from a general search engine's relationship to pages).
- Seeker surface: vertical search engines (Homes, Cars shown on UK homepage; title also claims jobs/products); accounts; email notifications for saved searches.
- Lifecycle: "Issues with ads" and "I found an expired ad" categories — ingested ads expire; expired-ad reporting is a user-facing state.
- Contact: "Problems making contact" and "The ad I'm interested in doesn't have contact information" — contact routes to the source site/poster; contact info may be absent on-site. The platform's job ends at discovery + routing.
- Monetization: partner/advertising products (Trovit for businesses).

---

## Cross-product Comparison

| Dimension | Rightmove | realestate.com.au | OpenRent | Trovit |
|---|---|---|---|---|
| Unit of record | property advert (for sale / to rent / commercial / overseas) | property listing (sale/rent/commercial) | rental advert | "ad" ingested from partner portals (homes/cars/jobs) |
| Pooled inventory | yes — agent-fed pool | yes — CRM/API-fed pool | yes — self-serve pool | yes — partner-feed pool |
| Lister admission | professionals only | professionals only | private landlords only | none (feed partners) |
| Supply machinery | membership + technical feed guidelines | uploader/CRM/API + consoles | self-serve advert builder + syndication | partner feed inclusion + opt-out |
| Offer-type split at top level | For sale / To rent (+commercial/overseas) | buy/rent/commercial | rentals (+rooms) | verticals (homes/cars/jobs) |
| Discovery | area/postcode/station search, map draw, keyword sort, alerts | search + AI search, inspections, alerts (renter side) | location search, commute-time search, once-only alerts | vertical search + saved-search notifications |
| Listing lifecycle | governed by membership + feed updates; data-quality/fraud policies | live via uploader; Listing Live notifications; inspections dates | until-let + fair use; new-listing alerts once; caching delay | ads expire; expired-ad states |
| Seeker→lister edge | enquiries/leads to agents; valuation-tool agent leads | Seller Leads machinery; rental applications; Tenant Check | masked email, viewing booking + reminders, chase | routed to source site; contact may be absent |
| Transaction machinery | none on surface (agents complete) | rental application pipeline; Max Bid; Realtair services | Rent Now tenancy creation (optional layer) | none |
| Monetization | memberships + display ads | subscriptions/packages/sponsorship/leads | free core + paid upgrades/syndication | partner products/advertising |
| Data layers | sold prices, index, data services | CMA, insights, property profiles | valuation calculator | — |
| Trust & safety | data quality + fraud courses of action | tenant check, listing content rules, law-change guides | ownership verification, UK phone verification, deposit compliance | report-a-problem, opt-out removal |

### B-layer (cross-product commonality) findings

1. **The listing as unit of record** — every sampled product's world is built from individually addressable offer records for ONE specific thing, carrying attributes, media, price/rent or terms, location, and an identified lister or source. (A×4)
2. **Pooled multi-lister inventory** — many listers' offerings aggregate into one venue the operator runs; the venue is not any single lister's catalog. (A×4)
3. **Offer-type / vertical organization at top level** — for-sale vs to-rent split (property portals) or vertical split (aggregator) organizes the pool before search. (A×4)
4. **Seeker-facing discovery machinery** — location/area search, filters/attributes, map views, saved searches + alerts. (A×4; alerts and saved searches universal in sample)
5. **Listing lifecycle with retirement** — listings enter, are updated (via feed/uploader/self-edit), and leave the pool when let/sold/expired/withdrawn; expiry/staleness is a managed state ("expired ad", "until let", "Listing Live" retirement, data-quality courses of action). (A×4)
6. **A lister-side supply surface distinct from the seeker surface** — consoles/advert builders/feeds; the two-sidedness is structural, its depth varies from thin (feed inclusion) to rich (full agency workspaces). (A×4)
7. **Seeker→lister contact handoff** — present in all sampled products; management depth varies enormously: link-out routing (Trovit) ↔ masked relay + viewing machinery (OpenRent) ↔ managed lead/application pipelines (REA). The handoff is standard; its machinery is variant. (A×4)
8. **Location as the organizing axis** (for location-bound verticals) — area/postcode search, map correctness governs findability, map-draw search, commute-time search. For non-local verticals the axis shifts to attributes/vertical categories (Trovit jobs/cars). (A×4, with the noted axis shift)
9. **Lister-side/audience-side monetization** — memberships, subscriptions, paid placement/sponsorship, syndication fees, lead products; seekers search free in the sample. (A×4)
10. **Trust & safety machinery over the inventory** — content/accuracy policies, fraud handling, verification (lister identity/ownership), reporting and opt-out/removal. (A×4)
11. **Derived data layers** — sold prices/indices/valuations/insights built on accumulated listing data. (A×3 — Rightmove, REA, OpenRent; not evidenced for Trovit)

### C-layer (canonical inference)

- The Type's defining job is **publication and discovery of a pooled inventory of current offers** — the platform is where many listers' time-bound offers become findable.
- The listing's **temporality** (entered → updated → retired when consummated/expired) is the in-family discriminator vs Directory Application (standing entity records).
- The **offer semantics** (something is currently offered on specific terms at a location) is the discriminator vs Information Portal (ephemeral pointers) and vs Review/Media content.
- The **connection/deal machinery is deliberately NOT definitional**: the minimal poles (feed-in/link-out aggregator; advertise-until-let with contact relayed) satisfy the Type without any managed connection or transaction machinery. This ratifies keep-both vs Listing Marketplace via a containment seam (below).

---

## Canonical Model — Four Abstraction Levels

### L0 — Defining Invariant (minimal)

A Listings Platform is a publication-and-discovery platform over a **pooled inventory of current-offer listings from many listers**. Three jointly-held structures:

1. **The pooled multi-lister offer inventory** — the operator aggregates offerings from many independent listers (or supply sources) into one venue. Remove → single-seller storefront / lister's own site.
2. **The listing of record as a structured, time-bound offer** — a persistent, individually addressable record of ONE specific thing currently offered (sale/rent/let/exchange), carrying attributes, media, price/terms, location, and an identified lister or source; it enters the pool, is updated, and is retired when the offer is consummated, expired, or withdrawn. Remove the time-bound offer semantics → Directory Application (standing entity record). Remove the structure → a pointer feed (Information Portal) or an unstructured ad wall (Classifieds).
3. **Seeker-facing discovery over the pool** — browse/search/filter across the whole pooled inventory is the platform's primary consumer-side job. Remove → a warehouse/syndication feed with no discovery surface (data supply), or a simple publication.

Jointly-held is load-bearing: (1+3 without 2) = a search/aggregation surface over documents, not an offer venue; (1+2 without 3) = a listings data store with no consumer discovery product; (2+3 without 1) = a single lister's own listing page.

### L1 — Common Mature Structure (very common, not defining)

- Seeker accounts, saved searches, email/push alerts (alerting typically fires on new listings entering the pool)
- Map-based search and location deepening (draw-a-search, commute/travel-time search)
- Structured attribute filters + keyword search; keyword-ranking controls
- Listing detail pages with media galleries, attributes, price/terms, lister identification
- Lister/agency profiles attached to listings; ratings/reviews of listers (sampled: REA, and OpenRent badges)
- Listing performance reporting for listers (views/enquiries); notifications hub
- Trust & safety: lister identity/ownership verification, prohibited-content rules, reporting channels, takedown/opt-out
- Derived data layers: sold/historical prices, price indices, valuation estimates, market insights
- Multi-surface delivery: web + mobile apps

### L2 — Variant / Optional Structure

- **Lister admission policy** — the most consequential variant: professional-membership-only (Rightmove, REA) vs private-lister-only (OpenRent) vs mixed vs none-direct/feed-only (Trovit).
- **Supply machinery depth** — self-serve advert builder ↔ professional consoles ↔ CRM/API feeds ↔ partner feeds.
- **Monetization shape** — memberships/subscriptions, per-listing or package fees, paid placement/sponsorship, syndication fees, lead products, free-core+paid-services.
- **Transaction-adjacent layers** — rental application pipelines, tenancy creation, holding deposits, auction bid registration; present in some products as optional layers above the advertising core (drift zone toward other Types when they become the defining job).
- **Portal syndication** — a lister-facing product (or platform policy) that bridges one venue's inventory into another venue's pool (agent-of-record bridging).
- **Vertical scope** — single-vertical deep platforms vs multi-vertical aggregators.
- **Regional regulatory machinery** — state/jurisdiction-specific compliance content and rules embedded in listing/application flows.
- **Search-era features** — AI/natural-language search (era-current, single-product observed).
- **Identity/verification regime** — phone verification, ownership checks, tenant/seeker verification products.

### L3 — Vendor-specific (research notes only)

- Rightmove: Rightmove Plus professional hub; Keyword Sort; Draw a Search; School Checker; Happy at Home Index; Member Classification Guidelines; "over 80% of time on property portals" self-claim; overseas private-seller T&Cs.
- REA: REAXML feed format; Ignite workspace; Agent Admin; Premiere+/Essentials/Basic subscription ladder; Audience Maximiser; Suburb Sponsorship; Enriched Seller Leads; Seller Leads assignment; Realtair (Pitch/Sign+/Pay Now); Max Bid; My Rental Profile; Tenant Check; Google Business Profile syndication of reviews.
- OpenRent: Rent Now (holding deposit → referencing → contracts → deposit protection → rent collection); masked email relay; 2-hour viewing reminders; "chase" button; £29 syndication / £79 Rent Now / £30-per-reference pricing; "advertise until let" + fair-usage policy; alerts-fire-once-on-first-list behavior; caching/propagation delays (1 hour own-site; 3–6 hours portals); rental valuation calculator; verified-UK-phone requirement; Property Ombudsman/ARLA/deposit-scheme memberships.
- Trovit: thribee partner product; Lifull Connect group; 30+ country editions; "Are you a classifieds portal?" self-positioning section.

## Vendor-specific Findings

(All L3 — none of these enter the final document.)

- Pricing points and service bundles (OpenRent's £29/£79/£30; REA's subscription names) are plan-specific facts.
- Timing/propagation specifics (OpenRent's alert-once rule, caching delays; REA uploader cadence article) are implementation behaviors, not Type rules.
- Self-reported market-share claims (Rightmove "80%") are marketing claims, recorded but not endorsed.

## Rejected Findings (considered and NOT promoted)

- "Listings are supplied by professional agents/CRMs" — rejected as defining: OpenRent (private self-serve) and Trovit (feed-only) are counter-samples. Admission policy is L2.
- "The platform manages the seeker→lister connection" — rejected as defining: Trovit's contact-at-source and absent-contact-info cases satisfy the Type with a bare handoff. Connection machinery is L1/L2.
- "The platform completes deals off-platform / connects parties to transact" — rejected as defining here (it IS definitional for the sibling Listing Marketplace leaf): OpenRent separates advertising from tenancy creation; Rightmove has no transaction surface. Containment seam chosen (see Boundary Findings).
- "Location/map search is defining" — rejected: true for location-bound verticals; Trovit's vertical organization shows the axis is domain-dependent (attributes/verticals for non-local goods).
- "Seeker accounts/alerts are defining" — rejected: publication-and-discovery precedes accounts; print-era antecedents satisfy the core without accounts (see historical check).
- "Ads vs listings vocabulary distinguishes the Type" — rejected: vocabulary is unreliable (Trovit calls its units "ads"; OpenRent calls them "adverts"; REA calls them "listings"). Structure, not vocabulary, carries the seams.

## Boundary Findings

### vs Directory Application (§02.11 sibling) — RATIFIED keep-both

Seam = record temporality, exactly as proposed by the directory-application pass: the directory holds a **standing entry per entity** (the entity persists; reach attributes are the point), the listings platform holds **expiring/consummable offer records** (each exists because something is currently offered; retirement is normal completion). Real products blend both surfaces (portals carry find-an-agent/agency directories — Rightmove "Find Agent", REA Agency Profiles); the blend does not merge the Types: strip the offer inventory and a property portal collapses into an agent directory (different Type); strip the entity directory and it remains a listings platform.

### vs Information Portal (§02.11 sibling) — consistent with that pass

Information Portal = ephemeral pointers (headlines/shortcuts) on a session-start gateway; Listings Platform = individually addressable offer records with detail pages and lifecycle. The information-portal pass's own removal test ("offers with lifecycle vs ephemeral pointers") is confirmed from this side.

### vs Classifieds Platform (§05.03) — keep-both, seam held structurally

Classifieds = self-published, ad-centric board: one ad = one item, minimal schema, category×locality filing, contact-first interaction, ephemeral ad lifecycle, poster account as the actor. Listings Platform = inventory-centric venue: a managed pooled inventory with structured schema, lifecycle governance (data quality, verification, syndication), and discovery as the product. The seam is genuinely blurry at the aggregator pole (Trovit ingests classifieds-portal ads and self-describes as a "classified search engine"); what keeps Trovit in this Type is that its product is the pooled searchable offer inventory with publication/discovery as the entire job — it hosts neither the ad-board interaction model (posting/renewing/messaging) nor any transaction machinery. **Flag for joint review with the classifieds side.**

### vs Listing Marketplace (§05.03) — the flagged near-alias. RESOLVED: keep-both RATIFIED with containment seam; alias candidate rejected

- Every Listing Marketplace contains a Listings Platform (its first two legs — listing of record + pooled searchable inventory — are exactly this Type's L0 1+2+3).
- Not every Listings Platform is a Listing Marketplace: the minimal poles documented here (partner-feed ingestion with contact routed to source — Trovit; advertise-until-let with enquiries relayed and transaction machinery strictly optional — OpenRent's advertising core; professional portals where the transaction completes entirely off-platform — Rightmove) satisfy Listings Platform but fail Listing Marketplace's defining legs (managed seeker→lister connection + off-platform deal-completion framing).
- Therefore: **Listing Marketplace = Listings Platform + connection machinery + deal-completion framing held as defining.** The seam is "what is the platform's defining job": publication/discovery of the offer inventory (this leaf) vs connection-to-deal as the managed product (that leaf).
- Products sit on a gradient: professional property portals with managed lead/application machinery (REA) drift toward the Listing Marketplace pole while remaining listings platforms at core. Variant language in the final document reflects this.
- Honest alternative recorded: if the directory were ever revised, folding Listing Marketplace into Listings Platform as the commerce-flavored pole is a defensible consolidation (the cores overlap ~80%); the directory currently types them in different domains (information vs commerce), and the minimal forms differ, so keep-both is the ratified outcome for v1.1.

### vs Property Listing Platform (§17) / Job Board (§09) — vertical instances

Both passes already treat the generic expiring-offer model as the underlying Type ("the employment realization of the expiring-offer model" — job-board pass). Listings Platform is the generic Type; Property Listing Platform and Job Board are its property/employment realizations typed elsewhere with their vertical machinery (agent/CRM integration; candidate machinery). Consistency confirmed from this side.

### vs Vertical Search Engine (§02.02) — aggregator-pole drift

The aggregator pole (Trovit) self-describes as a search engine and shares retrieval mechanics with vertical search. Held in this Type because supply is by partner agreement (feed inclusion with opt-out/removal — a managed relationship, not open-web crawling) and the units are offer listings with lifecycle and expiry states, not documents. **Flag for the vertical-search-engine pass.**

### vs Online Marketplace (§05.02) / storefront

No checkout, cart, or transaction of record on the platform surface; the offer is published, not sold on-platform. Transaction-adjacent layers (applications, tenancy creation) are optional add-ons; when mediated transactions become the defining product, the Type has drifted to marketplace territory. Single-seller catalog = storefront (no pooling).

### Historical / market-sample check (§24)

Passed. The print-era antecedents satisfy L0 without any digital implementation: newspaper property/autos/jobs listings sections, Trader-style classified magazines, newsagent window cards, and MLS-style broker listing books — pooled current offers from many listers, structured presentation (attributes, price, location, contact), browsable/organized discovery, listings retiring when sold/let/issue-expired. No accounts, alerts, maps, feeds, or web presence required. Modern aggregator and professional-portal forms are implementations, not the definition.

## Uncertainties

1. **US/global portal evidence gap**: Zillow, Realtor.com, Cars.com, CarGurus, Indeed, Zoopla, AutoTrader UK were unreachable this pass and in the prior listing-marketplace pass (403s). US-specific structures (MLS-fed inventory architecture, FSBO admission policies, ID-verification regimes) are therefore NOT asserted from product evidence; the final document's claims rest on the four directly sampled products and are worded structurally.
2. **Professional feed mechanics**: only the existence and configurability of listing-uploader/CRM/API supply is documented (REA REAXML article titles); field-level schema and cadence values are not asserted.
3. **Aggregator classification**: whether the market systematically classes Trovit-like products as listings platforms or as vertical search engines is genuinely ambiguous; both passes flag it.
4. **Trovit vertical breadth**: the UK homepage shows Homes and Cars engines; the product title claims jobs and products too. Treated as "multiple verticals including homes and cars".
5. **Monetization breadth**: sampled monetization is lister-side/audience-side; whether any mainstream listings platform charges seekers for core discovery is unverified (premium seeker tiers are known in adjacent job-board research but not evidenced here).
6. **Seeker-side data layers at aggregators**: derived-data layers evidenced only for inventory-owning platforms (Rightmove/REA/OpenRent); aggregator data-layer posture unknown.

## Final Synthesis

Listings Platform (§02.11) is the generic, information-domain Type: **a publication-and-discovery platform whose content is a pooled inventory of structured, time-bound offer listings from many listers, each individually addressable and lifecycle-managed, discovered by seekers through search/browse over the pool.** Its defining core is the trio: pooled multi-lister offer inventory + the structured time-bound listing of record + seeker-facing discovery. Everything else commonly seen — accounts, alerts, maps, profiles, verification, lead machinery, data layers, monetization shapes, admission policies, transaction-adjacent layers — is standard mature structure or variant, calibrated in the final document as core/common/optional.

The pass RATIFIES: (a) keep-both vs Directory Application (temporality seam), consistent with that pass; (b) keep-both vs Listing Marketplace (containment seam: connection+deal machinery defining there, not here), resolving that pass's near-alias flag; (c) consistency with Information Portal, Classifieds Platform, Job Board, and Property Listing Platform removal tests already on record. New flags for joint review: aggregator pole vs Vertical Search Engine; aggregator pole vs Classifieds Platform.
