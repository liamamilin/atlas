# Research Notes — Property Listing Platform

Research date: **2026-09-09**
Leaf: Property Listing Platform (§17 Construction, Real Estate & Facilities)
Slug: `property-listing-platform`

---

## Research Goal

Establish what the directory leaf **Property Listing Platform** (§17) denotes as an Application Type: the venue where properties offered for sale or rent are published and discovered. The pass must:

1. define the property-vertical realization of the pooled-offer venue and separate it from the generic **Listings Platform** (§02.11, processed 2026-09-08);
2. draw seams against §17 siblings (Real Estate Brokerage CRM, Property Showing Platform, Rental Application Platform, Tenant Screening Platform, Residential/Commercial Property Management — all unprocessed), against Classifieds Platform (§05.03, processed), Directory Application (§02.11, processed), and Vacation Rental Marketplace (§26, unprocessed);
3. handle the North-American MLS question (listing-data supply institution) with calibrated evidence;
4. ratify or amend the structure the listings-platform pass anticipated: "Property Listing Platform and Job Board are [the generic Type's] property/employment realizations typed elsewhere with their vertical machinery (agent/CRM integration; candidate machinery). Consistency confirmed from that side."

## Initial Boundary

Working hypothesis before research:

- A Property Listing Platform is a two-sided market venue: listers (agents, landlords, developers, owners) publish structured offers of specific properties; seekers (buyers, renters) discover them through location- and attribute-based search; listings carry a market lifecycle; seeker interest is routed to the responsible party; the transaction completes off-platform.
- Nearest confusion risks:
  - **Listings Platform (§02.11)** — the generic expiring-offer Type; property portals were that pass's evidence base, so this leaf must be defined by what the property vertical *adds*.
  - **Real Estate Brokerage CRM (§17)** — the agent-side system of record vs the public venue; listings flow from the former to the latter.
  - **MLS (North America)** — a broker-cooperative listing-data institution feeding portals; not itself the consumer venue.
  - **Vacation Rental Marketplace (§26)** — bookable short-stay inventory vs housing-market offers.
  - **Classifieds Platform (§05.03)** — property sections inside general classifieds.
  - **Rental Application / Tenant Screening / Property Showing (§17)** — downstream machinery that some portals embed.

## Research Questions

1. What exactly is the unit of record (the listing)? What content does it carry (attributes, media, price/rent, location)?
2. Who lists? (agents, landlords, developers, private sellers, operators) What admission rules exist per product?
3. How does listing supply arrive? (direct entry, CRM/uploader feeds, cooperative/institutional feeds, syndication between portals)
4. How do seekers discover? What are the search axes, and what governs findability?
5. What is the listing lifecycle? What market states exist and who maintains them?
6. What connection machinery routes seeker interest (inquiries, leads, viewing requests)? Where does the platform's role end?
7. What place-level data layers exist beyond the transient listing (sold prices, estimates, area data)?
8. What business models do platforms run (membership, per-listing, free+premium, advertising)?
9. Where do rental-deep machinery (applications, screening, tenancy creation) sit — inside this Type or in sibling Types?
10. What are the boundaries vs the generic Listings Platform and the other neighbors?

## Representative Products

| Product | Market | Philosophy / tier | Why sampled | Evidence tier |
|---|---|---|---|---|
| Rightmove | UK #1 portal | professional-membership portal; UK landlords/sellers reach it only through an advertising agent | canonical professional-portal model; deep seeker tools + sold-price data layer | Tier-1 (Freshdesk help centre + for-agents page) |
| realestate.com.au (REA) | AU #1 portal | professional portal with deep agent-side tooling (Ignite) and CRM/uploader feed supply | deepest documented lister-side machinery; renter-side application machinery | Tier-1 (Zendesk help centre, multiple articles) |
| OpenRent | UK rental | private-landlord direct platform; no-agent philosophy; itself syndicates to portals | proves the private-lister pole and the portal-feed supply path | Tier-1 (FAQ + advertising page + homepage) |
| Zillow | US #1 consumer portal | consumer-first portal + landlord SaaS (Rental Manager); brand family (Trulia, HotPads, StreetEasy) | US market structure; FSBO/landlord-direct pole; estimate data layer | Tier-2 (homepage + Rental Manager surfaces; help centre JS-walled) |

Rejected/abandoned: Realtor.ca (403), Realtor.com (429), Redfin (405), idealista (403), Zoopla (403 in prior passes; not retried), Trovit (already covered by the listings-platform pass as the aggregator pole).

## Sources

Fetched 2026-09-09:

- Rightmove Help Centre — https://faq.rightmove.co.uk/support/home/ ; tools folder https://faq.rightmove.co.uk/support/solutions/folders/7000041938 ; Sold House Prices folder https://faq.rightmove.co.uk/support/solutions/folders/7000048633
- Rightmove for-agents — https://www.rightmove.co.uk/for-agents.html
- REA Support — https://help.realestate.com.au/hc/en-us ; Agents & Developers category https://help.realestate.com.au/hc/en-us/categories/49055732021017 ; Renters category https://help.realestate.com.au/hc/en-us/categories/49055849242265 ; listing-uploader article https://help.realestate.com.au/hc/en-us/articles/115002481503-Set-up-or-change-my-listing-uploader-CRM-or-API-partner
- OpenRent — homepage https://www.openrent.co.uk/ ; advertising https://www.openrent.co.uk/landlords-advertise-property-for-rent-on-rightmove-and-zoopla ; FAQ https://www.openrent.co.uk/faq
- Zillow — homepage https://www.zillow.com/ ; Rental Manager https://www.zillow.com/rental-manager/ ; post-a-listing https://www.zillow.com/rental-manager/post-a-listing/

Unreachable (recorded as sourcing limitation): realtor.ca (403), realtor.com (429), redfin.com (405), idealista.com (403), zillow.help (JS-rendered shell only). Same wall class as the listings-platform pass (Zillow/Zoopla 403s) and the lease-administration pass (Yardi 403).

---

## Product A — Rightmove (UK)

### Key observations (evidence layer A unless noted)

**Seeker side:**
- Search starts with "an area, postcode or station" + the "For sale" / "To rent" choice — the offer-type split is the top-level organization (help centre: "How to start your search on Rightmove").
- Seeker tools: Keyword Sort (personalized ranking by features), Property Alerts (free account; new-match notifications), Draw a Search (map outline + schools/parks/transport overlays), Sold Prices, School Checker (school data + admission criteria + performance), mortgage/affordability calculators, valuation tool (seller enters details, picks local agents to contact — a seller-lead path), Happy at Home Index.
- Site sections: Buy (for sale, new homes), Rent (to rent, student), House Prices (sold prices, valuations), Mortgages, Find Agent, Commercial (sale/rent + commercial advertising), Overseas, Retirement homes.
- Sold House Prices: data supplied monthly by HM Land Registry (England & Wales sales after 1995; Registers of Scotland for Scotland); records persist and are not removed on request ("we don't remove sold prices… we want to ensure the insight we provide home movers is accurate"); images matched automatically from estate-agent listing data to sold-address records; homeowners may request image removal with ID verification; registration lag up to ~3 months.

**Lister side (for-agents page):**
- Membership model by lister segment: UK Estate & Letting Agents; UK New Homes Developers ("Coming soon" to "Site sold"); UK Rental Operators incl. Build to Rent (Lease-Up to Stable Phase); UK Commercial (agents, surveyors, landlords); Overseas (agents, developers, **private sellers** — the direct-listing exception); Schools; Home Products & Services (display advertising).
- UK landlords/sellers: "You can choose any letting agent that advertises on Rightmove to advertise your property" — consumer access is mediated by an advertising agent; the portal's listers are professionals.
- Governance: Membership Terms, Membership Classification Guidelines, Self-Employed Agent Model Guidelines, Agent and Developer Technical Guidelines (feed specs), Data Quality Course of Action, Fraud Course of Action, Geographical Advertising Guidelines, per-vertical Product Guidelines.
- Professional hub: Rightmove Plus; Data Services (property data supply).

### Interpretation

Rightmove shows the professional-membership pole: the portal is the seeker-facing aggregation layer; supply arrives through member agents (and their CRM systems, per the Technical Guidelines); the platform monetizes memberships and advertising, not transactions. The sold-price layer is a **permanent place-anchored public record** maintained beside the transient listings — sourced from the state land registry, not from the listings.

---

## Product B — realestate.com.au / REA (Australia)

### Key observations

**Audience split of the help centre:** Agents & Developers / Property Managers / Renters — the two-sidedness is institutionalized in support itself.

**Lister side (Agents & Developers):**
- Agent Admin (agency accounts, switching between agency accounts, sign-in).
- Agency branding: Ownership Groups and Agency Profiles; Suburb Sponsorship and Rent Banner Ads (creative + business rules); Property spotlight on Agency Profiles.
- Agent & Agency profiles (41 articles): Agent Profile object, contact info updates, Elevate subscriptions, social links.
- Agent & Agency reviews: ratings shown on property listing pages; AI summaries of reviews; Google Business Profile syndication.
- **Ignite** (agent workspace): listing search bar, Upcoming Inspections, Notifications Hub, Centralised Reporting, Watchlists, email preferences.
- Agency reporting and insights: Market Insights (incl. for Project Profiles), Audience Insights, Audience Extension Reporting (New Homes), Ignite Reports permissions.
- **CRM integrations**: "Set up or change my listing uploader (CRM) or API partner" — agencies designate a third-party listing uploader; two permission scopes: "Loading Listings" (loading + listings management) and "Leads and Reporting" (buyer & seller leads, lead enrichment, campaign reporting; CRM read access via API Export Permission); XML Uploads section in Agent Admin; REAXML format documented; "How often does a listing uploader send updates to us?" cadence article; on uploader change, existing listing details are handed to the new uploader and agent email addresses must be updated so enquiries still arrive; transferring listings between agencies is a supported operation; data extract available.
- **Seller Leads**: leads assigned to agents in Ignite; Enriched Seller Leads; lead-enquiry notifications; seller-leads reports.
- Realtair: Pitch (proposal), Sign+ (e-signing), Pay Now — transaction-adjacent partner machinery.
- Subscriptions: Premiere+ / Essentials / Basic; Audience Maximiser ad-hoc packages; Subscription & Listing Contract page.
- **Comparative Market Analysis**: CMA report customization; Owner Details lookup; Statement of Information; Market Insights; Property Profiles.
- realcommercial.com.au — the commercial sibling venue; "How clients find your agency on realcommercial.com.au".

**Renter side (Renters):**
- My Rental Profile: renter profile with employment & income details, address history.
- My Rental application: apply for a rental on the platform, check application status, withdraw, add pets; data-protection article.
- Tenant Check: renter-pullable screening report with state restrictions and accepted IDs.
- Renting FAQs: state-by-state rental-law change guides (QLD/NSW/NT/SA compliance).

**Seeker-side search:** AI search on realestate.com.au (article "How does AI search work"); Max Bid for auctions (buyer-side auction tool).

### Interpretation

REA is the deepest professional-portal realization: listings flow in from agency CRMs via a documented XML format (REAXML) with managed uploader relationships; the portal returns leads and reporting to the agencies; the agent workspace (Ignite) is the lister-side operating surface. The renter side embeds application machinery (profile → application → status) inside the venue. The venue also sells market data and CMA tooling back to the professional side.

---

## Product C — OpenRent (UK, private landlords)

### Key observations

**Positioning:** "The destination for finding, advertising, and managing rental property"; self-described UK's biggest letting agent (by tenancies created); founded 2012.

**Admission:** "We can only accept listings from private landlords" — companies/housing associations that own the properties they let are accepted; **letting agents are excluded**. Ownership-based admission is the rule.

**Lister side:**
- Packages: Free advertising (OpenRent only); Portal Advertising £29 (OpenRent + Zoopla + "up to 100+ partner sites"); Rightmove upgrade £70 ("useful for properties that are hard to let"); Advertising + Rent Now £58.
- Portal partnership: "We partner with the most popular property sites in the UK… **Only registered agents can list [on Rightmove/Zoopla] so you won't be able to do this directly as a landlord**" — OpenRent intermediates: it holds the professional relationships with the portals and feeds private landlords' listings into them.
- Listing creation: "less than 5 minutes" with photos; rooms as well as whole properties supported.
- Advert lifecycle: "We will advertise your property until let, but please note we do have a fair usage policy"; alerts fire once (on first listing); recommended listing ~4 weeks before vacancy; caching delays (up to 1 hour on OpenRent, 3–6 hours on partner portals).
- Enquiry handling: enquiries arriving via partner portals are handled by OpenRent and relayed to the landlord through a **masked email service**; viewing dates recorded with 2-hour reminders; a "chase" button after 48 hours of landlord silence; unresponsive-landlord reporting path.
- Rental valuation calculator from "all our properties ever advertised" (postcode-based rent estimate).
- Verified UK phone number required to advertise (landlord side) — spam defence.

**Tenant side:**
- Search by area/postcode/current location; saved searches + alerts; commute-time search (office postcode + max travel time by train/tube/walking).
- "We take down listings as soon as they are let, so no more ghost adverts" — lifecycle discipline as a tenant promise.
- Verified Tenant product (identity + affordability confirmation before enquiring); verified UK phone required to book viewings or pass screening.
- Message-the-landlord-directly model; deposit and rent protection framing.

**Rent Now (tenancy creation, optional):** tenant clicks Rent Now on the listing page and places a holding deposit of one week's rent → landlord notified (email+SMS), 4-day decision window → referencing (£30/reference, landlord-paid per Tenant Fees Act 2019) → contract drafting + online signing (custom clauses possible at landlord's risk) → deposit registered with mydeposits → initial rent collected (10-day hold as rogue-landlord defence) → key handover; "Let Agreed" state stops promotion. Landlord gets a "verified" badge via Rent Now. Regulatory context embedded: Tenant Fees Act 2019 (no tenant admin fees), Renters' Rights Act 2025 (periodic tenancies in England), deposit-protection law, Rent Smart Wales / Scottish registration.

**Trust machinery:** "systems in place to verify that a landlord owns the property"; Client Money Protection (Propertymark); Property Ombudsman + ARLA memberships; segregated client accounts.

### Interpretation

OpenRent proves the private-lister pole AND the supply-chain layer: a listing platform can itself be a feed supplier into larger portals (the "registered agent" relationship). Its core is the same pooled-offer venue; the tenancy machinery (Rent Now) is optional and adjacent — the platform's defining surface remains advertising + discovery + enquiry routing. Regulatory machinery (deposit schemes, fee bans) is regional context, not structure.

---

## Product D — Zillow (US)

### Key observations (evidence layer A for fetched pages; help centre unreachable — see limitations)

**Seeker side (homepage):**
- Top-level: Buy / Rent / Sell / Get a mortgage / Find an agent; Manage rentals (landlord entry); Advertise (partner entry).
- Search: location-based with Buy/Rent modes; browse hierarchies by state/city; rental buildings; apartments/houses per city.
- Zestimates (estimate layer); region insights; research; mortgage rates by state.
- Brand family: Trulia, StreetEasy, HotPads, Out East — one listings network under multiple consumer brands.
- Canada listings carry CREA/MLS trademarks (footer) — MLS-governed listing data north of the border.
- Zillow holds real estate brokerage licenses in multiple states/provinces (footer) — the portal is also a licensed brokerage.

**Lister side (Rental Manager):**
- Post-a-listing flow: street address + property type (House / Condo-Apartment Unit / Townhouse / Entire Apartment Community / Room for rent) → property details + photos → set monthly rent → publish; "minutes to create"; republish saved listings ("Reuse your rental posting").
- Distribution: listing appears across the rentals network ("over 30 million monthly visitors"; "over 1 million daily visitors" claims).
- Rent Zestimate integrated into the listing; comparable-review pricing tools; "Price my rental".
- Applications: accept rental applications free; tenant screening with background checks, credit reports, eviction history; income verification built into applications.
- Leases: upload/send lease for signing; Payments: online rent collection (rent, utilities, move-in fees); tours coordination; Lead Management tab (conversations, applications, next steps in one place).
- Premium upgrade: increased exposure, pricing & market insights, listing recommendations, priority support.
- Professional supply paths: Rent Connect (subscription-based ads), Lease Connect (pay-per-lease), **Syndicate listings (listing feeds)** — feed-based supply for apartment operators.

### Interpretation

Zillow is the consumer-first pole: free landlord posting + paid promotion, estimate data layers (Zestimate/Rent Zestimate) computed from its own data, and a rentals network spanning multiple consumer brands. Rental-deep machinery (applications, screening, leases, payments) is embedded but optional. The MLS relationship is visible only indirectly (Canada trademarks; feed syndication paths) — US supply architecture could not be directly documented this pass.

---

## Cross-product Comparison

| Dimension | Rightmove | REA | OpenRent | Zillow |
|---|---|---|---|---|
| Unit of record | property advert (sale/rent/commercial/overseas/student/retirement) | property listing (sale/rent/commercial via realcommercial) | rental advert (whole property or room) | rental listing (house/condo/townhouse/community/room); sale listings on main site |
| Listers | member agents, developers, rental operators, commercial firms; overseas private sellers (exception) | member agencies via CRM uploaders/API partners; agents hold profiles | private landlords (+ owning companies); agents excluded | landlords/property managers direct (Rental Manager); professionals via feeds (Rent/Lease Connect, syndication); agents advertise |
| Seekers | buyers, renters, landlords researching, sellers valuing | buyers, renters (with profiles/applications), investors | renters | buyers, renters |
| Discovery axes | area/postcode/station + For sale/To rent; map draw; keyword sort; alerts | location + attributes; AI search; alerts (implied by category structure) | area/postcode/geolocation; saved searches + alerts; commute-time search | location + Buy/Rent mode; map; browse hierarchies; recommendations |
| Findability rule | location correctness governs (search = area translation) | listing data quality governed by uploader feeds + data-quality policy | "location on the map is correct" is the governing findability attribute; title irrelevant | address-keyed posting (street address is the entry key) |
| Lifecycle | advertised while marketed; sold-price record persists separately | listing states managed via uploader updates; sold/withdrawn via feed | "advertise until let" + fair-use policy; takedown on let; "Let Agreed" state | published until rented/removed; republish saved listings |
| Connection | enquiries to agents; valuation tool → agent leads | enquiries emailed to agent profiles; Seller Leads with assignment + enrichment | masked-email relay; viewing booking + reminders; chase button | messages in Rental Manager; Lead Management tab; applications |
| Supply path | member technical guidelines (feed specs) | REAXML XML uploads via designated uploader/API partner | direct entry + OpenRent-as-agent syndication to portals | direct entry + listing feeds (syndication) |
| Place data layer | Sold House Prices (land-registry sourced, permanent) | Property Profiles, Market Insights, CMA, price data | rental valuation calculator (own listing data) | Zestimate / Rent Zestimate; comparable tools |
| Business model | agent/developer/operator memberships + advertising | agency subscriptions (Premiere+/Essentials/Basic) + sponsorship + advertising | free tier + per-advert packages + optional services | free posting + Premium upgrades + professional ad products |
| Rental-deep machinery | (via landlord/tenant services entity) | Renter Profile + applications + Tenant Check | Rent Now (holding deposit → referencing → contract → deposit → rent) | applications, screening, leases, payments |
| Regulatory embedding | membership classification, data-quality/fraud policies | state rental-law compliance guides | deposit schemes, tenant-fee ban, Renters' Rights Act, CMP | fair-housing guide; brokerage licensing |

### Cross-product commonalities (evidence layer B)

1. **Pooled property offers from multiple independent listers** — all four.
2. **Location-organized discovery** — all four; two products explicitly document that map-location correctness (not title wording) governs findability (Rightmove help, OpenRent FAQ); Zillow keys posting on street address.
3. **Structured listing content** — attributes (type, beds, features), price/rent, photos; floorplans/documents common (REA downloadable documents; Rightmove/REA media norms).
4. **Market-state lifecycle** — advertised-while-marketed with retirement/marking on outcome (OpenRent "until let" + "Let Agreed"; REA feed-driven states; Zillow republish; Rightmove until-sold/let via agent).
5. **Interest routing to the responsible party** — enquiries/messages/leads in all four; contact masking and lead management appear in mature implementations.
6. **For-sale / for-rent top-level split** — all four carry both offer types (OpenRent rental-only as a pole; Rightmove/REA/Zillow dual).
7. **Lister profiles / branding** — agent & agency profiles (REA), find-an-agent (Rightmove), landlord profiles (OpenRent), professional advertising (Zillow).
8. **Alerts / saved searches** — Rightmove, OpenRent documented; REA/Zillow category structure implies (weaker).
9. **Paid visibility / tiered placement** — all four (memberships, subscriptions, premium, sponsorship).
10. **Feed-based supply for professional listers** — REA (REAXML), Zillow (syndication), Rightmove (technical guidelines), OpenRent (as feed supplier) — the professional supply chain is feed-shaped everywhere it is documented.
11. **Place-level data layers beyond the transient listing** — sold prices (Rightmove, registry-sourced), estimates (Zillow), CMA/property profiles (REA), rent calculator (OpenRent). Implementations differ; the layer exists in all mature samples.
12. **Optional rental-deep machinery** — applications/screening/tenancy/payments embedded at varying depth (REA, OpenRent, Zillow; Rightmove routes to services entities).

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The smallest structure without which the product stops being a Property Listing Platform:

```text
Pooled property offers
(structured listings of specific place-identified properties,
 offered for sale or rent, from multiple independent listers)
└── Location-organized discovery
    (seekers search the pool by area/map + property attributes;
     findability governed by the property's geographic placement)
    └── Market-state lifecycle
        (listings live while the property is on the market;
         retired or state-marked on sale/let/withdrawal)
        └── Interest routing with off-platform completion
            (seeker interest reaches the listing's responsible party
             as an enquiry/lead; the sale or tenancy itself
             completes off-platform)
```

Four properties, each load-bearing:

1. **Pooled property offers** — the inventory is many listers' offers of *specific real properties*, each identified by its location. Remove → a single-agency inventory, or a generic Listings Platform with no property constraint.
2. **Location-organized discovery** — the offer is a fixed place, so discovery is organized around geography (area/map) plus attributes; whether a listing appears for a search depends on its placement in that geography. Remove → a lister-side inventory tool or a generic vertical search.
3. **Market-state lifecycle** — the listing exists because the property is currently on the market; it is maintained while marketed and retired or state-marked (let agreed / sold / withdrawn) at outcome. Remove → a standing property directory (the temporality seam ratified by the directory-application and listings-platform passes).
4. **Interest routing with off-platform completion** — the platform's connection role ends in routing seeker interest to the responsible party; the transaction (conveyancing, lease signing) is completed off-platform or by adjacent machinery. Remove → market-data publication with no participant connection.

**Historical check (§24):** newspaper property-listings sections (region-organized structured ads, contact the advertiser, ads retire when sold/let), MLS-style broker listing books (pooled broker offers organized by area, retired when sold), and newsagent window cards all satisfy all four legs with no digital machinery — no accounts, maps, alerts, estimates, or feeds in the definition. The definition is not overfit to the modern portal.

### L1 — Common Mature Structure

Present across the mature sample; expected but not definitional:

- structured attribute schema per property (type, bedrooms, size, features; regional energy classes)
- media: photos, floorplans, downloadable documents; virtual tours at the modern pole
- map-based search with drawn boundaries; commute-time search
- saved searches + new-listing alerts
- for-sale / for-rent top-level organization; commercial, new-homes, student, retirement, overseas segments
- lister profiles (agent/agency profiles, landlord profiles) with branding and reviews
- enquiry routing with contact masking; lead management surfaces for listers
- viewing arrangement machinery (booking, reminders)
- price/rent estimate tools and comparables
- place-level data layers: sold-price history (registry-sourced where documented), area/school data, price indices
- lister-side listing management (create/edit/republish) and feed/uploader integration for professionals
- paid visibility tiers (memberships, subscriptions, premium placement, sponsorship)

### L2 — Variant / Optional Structure

- **Lister population**: professional-only membership (Rightmove UK; REA), private-landlord direct (OpenRent; Zillow Rental Manager), mixed; ownership-based admission rules (OpenRent excludes agents)
- **Supply architecture**: direct entry; CRM/uploader XML feeds (REAXML); cooperative/institutional feeds (MLS-class — indirectly evidenced this pass); platform-as-agent syndication (OpenRent → portals); multi-brand network distribution (Zillow family)
- **Business model**: membership/subscription (Rightmove, REA), per-advert packages (OpenRent), free+premium (Zillow), advertising/display products
- **Rental-deep machinery depth**: none → enquiry-only → applications + screening → full tenancy creation + rent collection (OpenRent Rent Now, Zillow Rental Manager); heavy standalone realizations belong to sibling Types (Rental Application Platform, Tenant Screening Platform)
- **Sales-side extras**: valuation tools routing seller leads to agents (Rightmove, REA Seller Leads/CMA)
- **Commercial property** as a separate vertical or sibling venue (realcommercial.com.au; Rightmove commercial)
- **Regional regulatory machinery**: tenant-fee bans, deposit-protection schemes, periodic-tenancy law, state rental-law guides (UK/AU documented)
- **Auction support** (REA Max Bid), **AI search** (REA), **data services/APIs** (Rightmove Data Services, REA data extract)

### L3 — Vendor-specific (research notes only)

- Rightmove: Keyword Sort, Draw a Search, School Checker, Happy at Home Index, Rightmove Plus hub, Membership Classification Guidelines, overseas-private-seller exception
- REA: Ignite workspace, REAXML format, Suburb Sponsorship, Premiere+/Essentials/Basic tiers, Enriched Seller Leads, Realtair Pitch/Sign+/Pay Now, Max Bid, Audience Maximiser
- OpenRent: Rent Now, masked-email relay, 2-hour viewing reminders, chase button, £29/£70/£79/£58 pricing, verified-UK-phone requirement, mydeposits registration, 10-day rent hold
- Zillow: Zestimate/Rent Zestimate, Rental Manager, Rent Connect/Lease Connect, Lead Management tab, brand family (Trulia/HotPads/StreetEasy/Out East), brokerage licensing

---

## Vendor-specific Findings

See L3. Additionally: OpenRent's self-description as the UK's biggest letting agent shows a platform can straddle venue + agency services; the venue core (advertising/discovery/enquiry) is what generalizes. Zillow's brokerage licensing shows the portal operator may itself be a transaction party at the pole — the venue core still dominates its surface.

## Boundary Findings

1. **vs Listings Platform (§02.11, processed)** — containment seam, RATIFIED from this side consistent with that pass's structure: Listings Platform is the generic expiring-offer Type (pooled structured time-bound offer inventory + discovery); Property Listing Platform is its property-vertical realization typed in §17, carrying the property machinery as definitional (place-identified offers, location-organized discovery, market-state lifecycle tied to sale/let outcomes, professional lister ecosystem with feed supply, place-level data layers). Strip the property vertical → Listings Platform; strip the generic-pool framing → a single-agency inventory. The listings-platform pass's "property-listing-platform instance note" is hereby discharged from this side.
2. **vs Real Estate Brokerage CRM (§17, unprocessed)** — system-of-record seam: the brokerage CRM holds the agency's clients, properties and deals; the listing platform is the public market venue. Listings originate in the agency's systems and flow to the venue via uploader feeds (REA evidence: uploader change hands existing listing details over; enquiries return to agent profiles). Remove the public seeker-facing pool → CRM territory. Flag for that pass.
3. **vs MLS-class cooperative listing data (North America)** — the MLS is a broker-cooperative listing-data institution; consumer portals are its public faces (Zillow's Canada footer names CREA/MLS governance). Not directly researchable this pass (Realtor.ca/Realtor.com unreachable); recorded as an adjacent data-supply layer, not a competing definition. No directory leaf exists for it; no flag raised.
4. **vs Vacation Rental Marketplace (§26, unprocessed)** — inventory-character seam: short-stay bookable inventory with platform-mediated booking vs housing-market offers (sale or tenancy) with enquiry routing and off-platform completion. The hotel-search pass already flagged vacation-rental-marketplace for joint review; this pass holds the housing-offer seam from this side.
5. **vs Classifieds Platform (§05.03, processed)** — that pass recorded "vs Job Board / Property Listing Platform (verticals add candidate/agent machinery)". Confirmed from this side: property sections inside general classifieds lack the professional lister ecosystem, feed supply chain, market-state discipline and place-data layers; the dedicated platform's defining machinery is vertical.
6. **vs Rental Application Platform / Tenant Screening Platform / Property Showing Platform (§17, unprocessed)** — machinery seam: portals embed applications (REA, Zillow), screening (REA Tenant Check, Zillow, OpenRent referencing) and viewing booking (OpenRent, Zillow tours) as venue-adjacent depth; the standalone Types are the machinery's system of record. Remove the pooled public venue → sibling-Type territory.
7. **vs Directory Application (§02.11, processed)** — temporality seam ratified (standing entity record vs expiring offer). Portals blend both surfaces (find-an-agent directories, agency profiles); the blend does not merge the Types (strip the offer inventory → agent directory).
8. **vs Residential/Commercial Property Management (§17)** — demand side vs operator side: the listing venue markets availability to seekers; property management operates occupied stock (leases, maintenance, rent collection). OpenRent's Management Plus and Zillow's Rental Manager tooling drift toward the operator side as optional depth.

## Uncertainties

- **US/Canada supply architecture under-evidenced**: Realtor.ca (403), Realtor.com (429), Redfin (405) unreachable; Zillow help centre JS-walled. The MLS-fed model is asserted only at structural-inference strength (Zillow's Canada MLS trademark notice; feed-syndication product paths). No precise US feed/refresh mechanics are claimed.
- **Zillow evidence is marketing-weighted**: homepage + Rental Manager surfaces are official but promotional; operational rules (posting requirements, takedown timing, FSBO sale-listing mechanics) not directly documented. Kept out of precise claims.
- **Sale-side private listing (FSBO) depth on US portals** not directly observed; Rightmove's overseas-private-seller exception is the only directly documented private-seller pole on a professional portal.
- **Alert semantics** directly documented only at Rightmove/OpenRent (fire-once-on-first-listing at OpenRent); generalized cautiously.
- **Whether a sale-only or rent-only platform at national scale changes the Type**: OpenRent (rental-only) and the historical MLS book (sale-only) both satisfy L0, so offer-type breadth is held variant, not definitional — but the modern national portals in-sample are all dual.

## Final Synthesis

A Property Listing Platform is the property market's public listing venue: listers publish structured offers of specific place-identified properties for sale or rent into a pooled, publicly searchable inventory; seekers discover through location- and attribute-organized search; each listing lives while its property is on the market and retires or state-marks at outcome; and seeker interest is routed to the listing's responsible party, with the sale or tenancy completing off-platform. Around this core, mature products add structured media-rich listing content, map/commute search, alerts, lister profiles, feed-based professional supply (CRM uploaders, syndication, cooperative data), place-level data layers (sold prices, estimates, area data), paid visibility tiers, and — at varying depth — rental-deep machinery (applications, screening, tenancy creation) and seller-lead machinery (valuations, CMA). The Type is the property-vertical realization of the generic Listings Platform, distinguished by the place-bound offer, the market-state lifecycle tied to sale/let outcomes, and the professional lister ecosystem that supplies it.
