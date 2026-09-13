# Research Notes — Pet Adoption Platform

Research date: 2026-09-09
Slug: pet-adoption-platform
Directory location: §29 Home, Family, Personal & Local Services (siblings: Animal Shelter Management, Lost Pet Platform, Dog Walking Platform, Pet Sitting Platform, Pet Health Application; cross-section neighbors: Classifieds Platform §05.03, Listings Platform §02.11, Online Marketplace §05.02, Directory Application §02.11)

---

## Research Goal

Understand what a "Pet Adoption Platform" actually is as an Application Type: what records it holds, who creates them, how adopters discover animals, how adopter interest connects to the organizations that hold the animals, where the adoption itself happens, and where the boundary sits against Animal Shelter Management (operator custody system — flagged for joint review from the sibling pass), Lost Pet Platform, Classifieds/Listings Platforms, and Online Marketplace.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: consumer-facing venue for discovering adoptable animals offered by shelters/rescues, plus the machinery that carries an adopter from a listing into that organization's adoption process. The platform holds no custody, no kennels, no medical records — it is the demand-side surface the shelter system feeds.
- Primary users: prospective adopters (consumers); shelter/rescue staff who maintain listings and respond to inquiries; the platform operator as venue runner.
- Most likely confusions:
  - Animal Shelter Management (operator custody system; its publishing output looks like an adoption platform)
  - Lost Pet Platform (reunification of owned animals vs placement of unowned animals)
  - Classifieds Platform / Listings Platform (generic listing venues that can host "pets for adoption")
  - Online Marketplace / E-commerce (transaction venue, but animals are not merchandise)
  - Owner-rehoming services (individuals rehoming their own animals — variant or different Type?)
- Unknowns going in: is multi-organization pooling definitional or is a single-org adoption site the same Type? Is the adoption transaction (fee/contract) ever completed on-platform? Is owner-rehoming inside the Type? How deep do platform-hosted applications go?

## Research Questions

1. What is the core record — the adoptable-animal listing — and what does it contain?
2. Who creates and maintains listings (organizations only, or individuals too), and how does listing data arrive (direct entry, syndication from shelter software)?
3. What does adopter-side discovery look like (search facets, filters, favorites, saved searches, alerts)?
4. How does adopter interest reach the offering organization (contact info, inquiry, platform-hosted application)?
5. Where does the adoption itself happen — does the platform ever complete it (fee, contract, custody transfer)?
6. What is the listing lifecycle (available → pending → adopted/removed)? Who controls availability?
7. What surrounds the core: org profile pages, guidance content, success stories, fostering, donations, sponsors?
8. What business models exist (free service, nonprofit, sponsor-funded, paid)?
9. Where exactly is the boundary with Animal Shelter Management (discharge the sibling pass's joint-review flag)?
10. What regional/structural variants exist (national platforms, syndication hubs, single-federation sites, open posting networks, retail adoption centres)?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer/geographic tiers:

| Product | Segment | Philosophy | Evidence quality |
|---|---|---|---|
| RescueGroups.org — Pet Adoption Portal | US small/medium rescues; free service tier | syndication hub: update once, populate many adoption sites; portal + org network | Strong (official user guide, fetched) |
| Rescue Me! | US since 1999; individuals + shelters/rescues; breed-organized | open posting network with human review, alerts, widgets, grants | Strong (official site + shelter/rescue help page, fetched) |
| RSPCA Find a Pet (rspca.org.uk) | UK; single charity federation (England & Wales centres) | charity's own adoption search + fully documented adoption process | Strong (official adoption-process pages, fetched) |
| RSPCA Adopt-a-Pet (adoptapet.com.au) | Australia; national RSPCA federation + retail adoption centres | national aggregation with advanced search; retail partner centres | Strong (official site, fetched) |
| PetPlace (served at petango.com) | US; 24Pet/PetPoint ecosystem's consumer adoption search engine | ecosystem surface fed by shelter software | Minimal (JS application; header/search chrome only) |

Note: the two RSPCA properties are one organization in two countries; they are treated as one sample with two regional realizations, with the other three products providing independent-vendor coverage.

Attempted but unreachable (recorded as source-access limitations):

- **Petfinder** — www.petfinder.com and /for-shelters-and-rescues/ return 403 (2 attempts); help center is a JavaScript application with no extractable content; Wayback Machine fetch timed out / transport error (2 attempts). Abandoned per network rules. The largest US adoption platform is therefore market context only; no product claims are made about it.
- **Adopt-a-Pet** — www.adoptapet.com and rehome.adoptapet.com return 403 (2 attempts); help subdomain transport error. Abandoned. Its well-known Rehome program is market context only.
- **PetRescue (AU)** — root and /about returned empty responses (2 attempts). Abandoned.
- **911fosterpets** — domain now serves unrelated spam content; not usable.
- **Get Your Pet** — direct owner-to-adopter rehoming platform; site states "Get Your Pet ceased operations on March 1, 2024" (direct observation of the closure notice). Used only as evidence that a dedicated rehoming pole existed and has thinned.

## Sources

Tier 1 (official operational documentation):

- RescueGroups.org — Pet Adoption Portal Guide (index, Getting Started, Features, About email messages, About partnerships) — https://userguide.rescuegroups.org/display/PORTAL/Pet+Adoption+Portal and child pages (fetched 2026-09-09)
- Rescue Me! — homepage — https://www.rescueme.org/ (fetched 2026-09-09)
- Rescue Me! — "Grants for Rescue Groups & Other Help" (shelter/rescue onboarding steps) — https://www.rescueme.org/RescueGroups (fetched 2026-09-09)
- RSPCA (England & Wales) — Find a Pet landing — https://www.rspca.org.uk/findapet (fetched 2026-09-09)
- RSPCA (England & Wales) — "How to adopt a pet" (adoption process, requirements, fees) — https://www.rspca.org.uk/findapet/adopt (fetched 2026-09-09)
- RSPCA Australia — Adopt-a-Pet national adoption site — https://www.adoptapet.com.au/ (fetched 2026-09-09)

Tier 2 (official product surfaces, limited extraction):

- PetPlace — https://www.petango.com/ and /pet-adoption (JavaScript application; navigation, search chrome, and registry banner extractable only) (fetched 2026-09-09)
- Get Your Pet — https://getyourpet.com/ (closure notice only) (fetched 2026-09-09)

Internal cross-references (sibling research passes, B-grade for boundary work):

- research/animal-shelter-management.md (operator custody system; publishing output; the flagged joint review)
- research/lost-pet-platform.md (reunification vs placement boundary)
- research/dog-walking-platform.md (§29 sibling vocabulary note)

---

## Product Observations

### RescueGroups.org — Pet Adoption Portal (evidence layer A throughout)

Free service for US nonprofit rescues; part of a service suite (Website Service, Data Management, Online Forms, Email Marketing, Voicemail, Fax, Domain Names, Android management app).

- Positioning (guide, verbatim): "helps organizations gain as much exposure for their adoptable animals as possible with as little overhead as possible by updating many of the national pet adoption websites at one time"; volunteers "update one site to populate many"; "completely free".
- Benefits list: single-site updating of "all the major adoption listing websites"; no forced advertisements in pet descriptions; no forced pet-list scroller; ease of setup ("we do most of the work for you, including getting set up with most of the adoption listing site AND adding your animals"); data and picture exports at any time; "we never delete your data".
- Setup flow: review organization contact info → add animals → enable exports → add volunteers (role-based users). A veterinarian reference letter may be requested of the organization (org vetting).
- Features tab: Email Messages (site messages with assignable templates — including "Online Form Applicant Contact", a template email used on the Contact Applicant page, editable before sending; Contacts/Registration Invitation), Locations, Partnerships, API Developer's Guide; FTP account; Reports.
- Partnerships (org-to-org network): request/approve/decline/block workflow; one-way sharing of animal information with partner organizations "to help find space for at-risk animals"; postal-code + radius search for partner organizations; shared animals immediately available on approval.
- Structural significance: the Portal is the consumer-facing/syndication service of an operator suite — the same vendor ships the operator-side Data Management service separately (sibling research). The Portal's own public surface plus exports to "the major adoption listing websites" is the platform layer.

### Rescue Me! (evidence layer A throughout)

US 501c3 public charity, copyright 1999–2026; "Rescue Me helps dogs, cats, horses, birds, and other animals find homes"; homepage counter "1,427,975 Animals Adopted on Rescue Me!" (vendor claim).

- Structure: breed-organized rescue listings (subdomain per breed: dog.rescueme.org, hundreds of breed pages; cat breeds; horse, rabbit, farm animal, small mammal, reptile, pet bird, wildlife sections).
- Two poster classes, explicitly separated: "Accounts for shelters/rescues are different than for individuals. Create a shelter account to qualify for grants and special rescue features. Any organization can create a posting account, whether or not a charity." Individuals have their own flow ("Find a Home for an Animal" nav action; "Log into Posting Account").
- Connection machinery: "Most groups receive adoption enquiries within hours of posting their first animal. Within two hours of posting, Rescue Me reviews each post to alert hundreds of potential adoption candidates." (human review + alerting to candidate adopters)
- Distribution: embeddable widgets ("Easily embed your adoptable animals within your own site using Rescue Me widgets. Many groups include a widget on every page of their site"); Rescue Alerts (subscribe by breed/area to be notified as new animals are posted); photo + YouTube/Facebook video encouraged in posts.
- Org support: quarterly rescue grants (require shelter posting account + Facebook page like); "Help for Shelters/Rescues" page; success stories blog.
- Species breadth: dogs, cats, horses, rabbits, farm animals, small mammals, reptiles, birds, wildlife.

### RSPCA Find a Pet — rspca.org.uk (evidence layer A throughout)

Single-charity federation platform (England & Wales; branches and centres).

- Search: "find a rescue pet" by Type of Pet (Dogs, Cats, Rabbits, Pet birds, Horses and ponies, Farm animals, Guinea pigs, Ferrets, Small furries, Fish, Reptiles, Mini beasts, Amphibians) + Location; "explore animals near you".
- Profile content promise: "Each profile shares what we know about the animal, including their personality, needs and the kind of home that will best support their welfare."
- Adoption process (documented step-by-step on /findapet/adopt):
  1. Find a pet — browse profiles on the search.
  2. Apply — "complete the application on their profile page. This helps our teams understand your home, lifestyle and experience… You should hear back from our team within 48 hours."
  3. Matchmaking and assessment — teams review applications, phone conversations, "Every adoption is considered individually, with the animal's welfare at the heart of every decision."
  4. Meet and get to know each other — arranged meeting, possibly multiple visits for complex needs.
  5. Final checks and taking your pet home — "paperwork, adoption fees and practical advice"; fees "vary depending on the type of animal and the centre. They help contribute to the cost of veterinary care, vaccinations, neutering and preparation"; key documents issued.
  6. Post-adoption — local centre remains available; "follow-up calls or home visits" possible.
- Adoption requirements: home environment safety, time available (how long the pet may be left alone), experience and reward-based training willingness, ability to meet ongoing costs, landlord permission if renting; framed against the Animal Welfare Act 2006 five welfare needs. "Rather than having fixed rules, our teams focus on whether you can meet the needs of a specific animal."
- Companion surfaces: Favourites (account feature); fostering track ("Become a foster carer"); Advice for Adopters; local-centre finder; "Recently rehomed" success stories; Rehoming policy PDF and Adoption terms and conditions PDF.
- Vendor-claimed volume: "70 animals a day found new homes" (marketing claim; not asserted as fact).

### RSPCA Adopt-a-Pet — adoptapet.com.au (evidence layer A throughout)

National Australian adoption site of the RSPCA federation.

- Search facets (all directly observed): Animal Type (Dog & Puppy, Cat & Kitten, Amphibian, Bird, Cattle, Crab/Fish, Farm, Ferret, Fowl, Goat, Guinea Pig, Horse, Pig, Rabbit, Reptile, Rodent, Sheep); State (ACT/NSW/NT/QLD/SA/TAS/VIC/WA); Location (specific centres — RSPCA shelters/centres AND retail adoption centres: dozens of Petbarn and PetStock stores, Best Friends stores, "Petbarn Adoption Centre" entries); Advanced search: Breed, Colour (very large value list), Sex, Size (Small/Medium/Large/Extra Large), plus attribute flags: Special Needs, Longterm resident, Senior Pet.
- Result retrieval: "Meet some of our pets" with pagination ("Show more", /search?load=40).
- Adoption steps (documented): Plan (lifestyle/cost readiness) → Search ("All animals have been health and behaviour assessed by the RSPCA") → Contact ("contact the shelter and make an appointment to stop by") → Visit (meet animals at the shelter).
- Supply structure: RSPCA state/territory organizations + retail partner adoption centres (animals physically hosted in retail stores) — a federation-plus-retail supply model.
- Surrounding surfaces: How to adopt; Why adopt; Caring for your pet (+ RSPCA Pet Insurance cross-sell); sponsors (Royal Canin, Bravecto/MSD, Bendigo Bank); RSPCA Adoption Centres contact page; knowledgebase link.

### PetPlace (served at petango.com) (evidence layer A, minimal — JavaScript application)

The 24Pet/Pethealth ecosystem's consumer surface; petango.com (the former Petango adoption search) now serves PetPlace. Sibling research (animal-shelter-management pass) independently documented PetPlace as PetPoint's "automatic publishing feature and our pet adoption search engine".

- Directly observed: adoption search chrome — "Dogs for adoption near 90210", Filter control, "Sorted by: Nearest", per-card favorite control (♡), placeholder cards ("Pet available for adoption"), Sign in; top-level sections Adopt / Protect / Care / About; "Report a lost or found pet" action; banner "The 24Petwatch microchip registry is now on PetPlace!"; support phone line.
- Interpretation (calibrated): a consumer adoption search over the shelter-software network's animals, location-sorted, with adopter accounts and favorites, bundled in a brand that also carries the microchip registry (Protect) and pet-care content (Care). Detail pages could not be extracted (JS app) — no deeper claims made.

### Market context (unreachable or dead; no product claims)

- Petfinder and Adopt-a-Pet: the two best-known North American adoption platforms; both unreachable from this environment (403). Their existence and general shape are common knowledge, but nothing in this research depends on their internal behavior.
- Get Your Pet: dedicated owner-to-adopter rehoming platform; closure notice observed ("ceased operations on March 1, 2024"). Evidence that the pure rehoming pole existed as a standalone Type-candidate and has thinned; rehoming persists as a flow inside open posting networks (Rescue Me!) and, per market reputation, inside Adopt-a-Pet's Rehome program (unreachable — not asserted).

---

## Cross-product Comparison

| Dimension | RescueGroups Portal | Rescue Me! | RSPCA UK Find a Pet | RSPCA AU Adopt-a-Pet | PetPlace |
|---|---|---|---|---|---|
| Per-animal adoptable listing (identity/description/media) | ✓ (animals entered by org; exports carry descriptions/photos) | ✓ (posting with photo/video encouraged) | ✓ (profiles with personality/needs/home-fit) | ✓ (search results; assessed animals) | ✓ (placeholder cards observed; detail JS-hidden) |
| Offering party identified on the listing | ✓ (organization account; org contact info) | ✓ (posting account — org or individual) | ✓ (RSPCA centres) | ✓ (centre/location per listing) | ✓ (network shelters; not directly observed) |
| Pooled multi-source inventory | ✓ (many orgs; exports to many sites) | ✓ (orgs + individuals, breed-organized) | ✓ (centres across England & Wales) | ✓ (states + retail centres) | ✓ (PetPoint shelter network) |
| Adopter-side search/filter | via destination sites (portal itself is syndication) | breed/area browse + alerts | type + location | type/state/location/breed/colour/sex/size/flags | location-sorted + filter |
| Favorites / saved state | not observed | not observed (alerts are the standing mechanism) | ✓ (Favourites) | not observed | ✓ (♡ per card) |
| New-listing alerts to adopters | not observed (alerts are org-side via destination sites) | ✓ (Rescue Alerts by breed/area) | not observed | not observed | not observed |
| Connection path | online form applicants + template contact emails; org contact | "adoption enquiries" to posting account; human review + candidate alerting | application on the profile page → team response → phone → meet | contact the shelter, make an appointment, visit | not directly observed (sign-in gated) |
| Platform-hosted application forms | ✓ (Online Forms service; applicant contact templates) | not observed (enquiry-based) | ✓ (application on profile page) | not observed (contact/appointment model) | unknown |
| Adoption completed on-platform (fee/contract) | not observed | not observed | no — paperwork/fees at the centre | no — visit the shelter | not observed |
| Listing lifecycle evidence | status managed by org (sibling research: animal status drives exports) | posts reviewed/removed by platform review | "Recently rehomed" showcase; animals leave search | availability maintained by centres | "available for adoption" state |
| Fostering surface | not observed in Portal guide | not observed | ✓ (foster track) | not observed | not observed |
| Org-to-org networking | ✓ (partnerships: share animals, find space for at-risk animals) | not observed | internal (branches) | internal (states) + retail | network-internal |
| Guidance content | minimal (support docs) | advice section | extensive (how to adopt, requirements, advice for adopters) | how to adopt / why adopt / caring for your pet | Care section |
| Success stories / counters | not observed | ✓ (adoption counter, success stories blog) | ✓ ("Recently rehomed" stories) | not observed | not observed |
| Who may list | organizations (vetted; vet reference letter possible) | organizations AND individuals | RSPCA only (single federation) | RSPCA states + retail partners | network shelters |
| Business model | free service (suite upsells) | free + grants + donations | charity | charity + sponsors + insurance cross-sell | ecosystem (registry/care bundle) |
| Syndication (update once → many sites) | ✓ (defining feature) | ✓ (widgets embed into own site) | n/a (own site) | n/a (own site) | ✓ (PetPoint publishing feeds it) |

Reading of the matrix:

- Present in all five samples: per-animal adoptable listing with an identified offering party; pooled multi-source inventory; a connection path from listing to offering party; the adoption itself completed by the offering party, not the platform.
- Present in most: adopter-side search/filtering; guidance content; success-story showcases; status-driven availability.
- Present in some: platform-hosted application forms; favorites; new-listing alerts; fostering surfaces; org-to-org networking; syndication machinery; retail adoption centres; individual (rehome) postings.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

A Pet Adoption Platform is a consumer-facing venue where adoptable animals are listed by the parties that hold them, and is built on three jointly-held structures:

```text
Adoptable-Animal Listing of Record
└── Pooled Multi-Party Adoption Inventory
    └── Adoption Connection Path
        (interest routed to the offering party,
         whose own adoption process takes over)
```

1. **The adoptable-animal listing of record.** A persistent, individually identified listing of one specific animal offered for adoption: identity and description (name, species/breed, age, sex, size), photos (commonly video), adoption-relevant attributes and narrative (health/behavior status, personality, the kind of home needed), and the offering party with its location. The listing's availability is maintained by the offering party — it is a stateful record tracking a real placement process, not a static ad. (Remove → generic pet content or a directory entry.)
2. **The pooled multi-party adoption inventory.** Listings from multiple independent offering parties — shelters, rescues, foster-based organizations, and in some products individual owners rehoming directly — aggregated into one browsable/searchable population on a venue operated separately from the animal-holding parties. (Remove → a single organization's own adoptable-pets page, which is the publishing output of shelter operations, not a platform.)
3. **The adoption connection path.** The platform's own machinery carries an interested adopter from a listing into the offering party's adoption process — as published contact/appointment details, an inquiry routed to the posting account, or a platform-hosted application form — after which the offering party screens, decides, and completes the adoption (meet-and-greet, paperwork, adoption fee) at its own facility or through its own process. The platform connects; it does not itself hold animals or transfer custody. (Remove → a read-only aggregator/directory.)

Jointly-held is load-bearing:

- 1 alone = a pet listing page / catalog entry
- 2 without 1 = an organization directory
- 3 without 1+2 = a contact form
- 1+2 without 3 = a read-only aggregator
- 1+3 without 2 = one organization's adoption page (shelter publishing output)
- 2+3 without 1 = a referral service with nothing per-animal to attach interest to

Domain binding: the animals are offered for **new-home placement under a welfare framing** — the offering party is accountable for the animal and gates the placement through screening; the terminal outcome is adoption (a new owner), not a sale of merchandise and not a reunion with an existing owner. Remove the welfare-placement binding → classifieds/marketplace; remove the new-owner outcome → lost-pet territory.

Historical/market-sample check: printed multi-shelter adoption directories and shelter-coalition listing books (listing cards from many organizations + contact routing) satisfy all three legs at analog level; late-1990s web adoption databases satisfy them without favorites, apps, alerts, or algorithmic matching. The single-shelter adoptable-pets webpage and the newspaper "free to good home" ad are thin ancestors (publishing output and classifieds respectively). The core therefore does not over-fit the current platform market.

Deliberately NOT in L0 (tested and demoted):

- **Adopter accounts, favorites, saved searches, new-listing alerts** — common (PetPlace ♡, RSPCA UK Favourites, Rescue Me! alerts) but absent from other mature samples and from the historical form.
- **Platform-hosted application forms** — one strong realization (RSPCA UK application-on-profile; RescueGroups online forms) but other mature platforms connect by contact/appointment only (RSPCA AU).
- **Rich profile narrative** (personality/home-fit text) — common in modern products; the historical form worked on photos + basic description.
- **Syndication machinery** (update once → many sites) — the RescueGroups Portal's defining feature and PetPlace's feed model, but federation platforms (RSPCA) need none.
- **Org-to-org transfer networking** — present (RescueGroups partnerships) but internal to federations elsewhere.
- **Fostering surfaces** — present (RSPCA UK) but not universal.
- **On-platform fee payment / contract signing** — not observed in any sampled platform; the fee/contract step belongs to the offering party's process.
- **Success stories, guidance content, sponsors, donations** — surrounding surfaces, not structure.

### L1 — Common Mature Structure

- Adopter-side search and filtering: species/type, location/geography, breed, age, sex, size, and attribute flags (special needs, senior, long-term resident).
- Per-animal profile pages: photos (commonly video), description, health/behavior/assessment notes, home-fit narrative, offering party and location.
- Organization/centre profile surfaces: the offering party's other animals, contact details, location.
- Connection surfaces: contact/appointment details, inquiry forms, or application forms routed to the offering party.
- Adoption guidance content: how adoption works, adoption requirements, why adopt, adopter advice.
- Success-story showcases and adoption counters ("recently rehomed", reunion-style stories).
- Status-driven availability: listings leave the search when adopted; pending/reserved states exist behind the scenes (operator-side).
- Adopter accounts with favorites/saved state (most modern platforms).
- New-listing alerting to subscribed adopters (open-network products).
- Syndication/export machinery feeding the platform from shelter software (portal-type products).

### L2 — Variant / Optional Structure

- Who may list: organization-only (vetted nonprofits/federations) vs organizations + individuals rehoming their own animals (open posting networks; dedicated rehoming services existed — one observed closure).
- Supply structure: open multi-org network vs single-federation (one charity's states/centres) vs ecosystem network (shelter-software vendor's customer base) vs retail adoption centres (animals hosted in retail stores).
- Connection depth: contact/appointment only → inquiry → structured application with screening questions → (rare) on-platform adoption workflow support.
- Regional scope: national platforms vs regional/single-country services; language/regime differences (welfare-law framing differs by jurisdiction).
- Species breadth: dog/cat-focused vs any-animal (horses, farm animals, birds, reptiles, small furries).
- Fostering surfaces alongside adoption (foster listings, foster-to-adopt pipelines).
- Business model: free nonprofit service, charity-operated, sponsor/advertising-funded, ecosystem-bundled (registry/insurance/pet-care cross-sell), or paid promotion.
- On-platform commerce adjacency: pet insurance, pet food, accessories cross-sell around the adoption moment.

### L3 — Vendor-specific Structure

- RescueGroups: free-suite bundling (voicemail/fax/email marketing), FTP exports, veterinarian reference letter vetting, partnership request/approve/decline/block mechanics with one-way sharing, "we never delete your data" data-retention promise, assignable site email templates (applicant contact, registration invitation).
- Rescue Me!: breed-subdomain information architecture (hundreds of breed sites), human post review within a stated short window with candidate alerting, quarterly rescue grants tied to shelter accounts + social engagement, embeddable widgets, "Find a Home for an Animal" individual flow, adoption counter.
- RSPCA UK: application-on-profile with a published response-time expectation (48 hours), Animal Welfare Act 2006 five-needs framing, published Rehoming policy and Adoption terms PDFs, fostering track, "Adoptober" campaign, local-centre finder.
- RSPCA AU: state-federation + retail adoption centre supply model (Petbarn/PetStock/Best Friends locations as adoption venues), very large colour/breed facet vocabularies, Plan→Search→Contact→Visit four-step framing, sponsor and insurance ecosystem.
- PetPlace/24Pet: 24Petwatch microchip registry integration ("Protect"), lost/found reporting inside the adoption brand, PetPoint publishing feed as the supply side.

## Vendor-specific Findings

See L3. The most consequential vendor pattern is the **ecosystem model** (shelter software vendor operating the consumer adoption surface — PetPlace fed by PetPoint; RescueGroups Portal feeding many sites): it demonstrates that the platform layer and the custody layer are separate products even inside one vendor, which is the strongest available corroboration for the Animal Shelter Management boundary.

## Rejected Findings

- "Adoption platform = shelter software with a public page": rejected — the consumer venue has no custody lifecycle, no kennel/medical structures, and no operator workflow; shelter products ship their listing output as a separate publishing function or a separate product (RescueGroups Portal vs Data Management; PetPlace vs PetPoint).
- "The platform completes the adoption transaction": rejected on current evidence — in every sampled product the screening decision, paperwork, and fee happen in the offering party's process (at the centre/shelter or via its own workflow); the platform's job ends at connection. On-platform payment/contract was not observed anywhere in the sample.
- "Owner rehoming is a different Type": rejected as a separate Type — individual postings appear inside a mature adoption platform (Rescue Me!) as a poster-class variant; dedicated rehoming platforms existed (Get Your Pet, now closed). Rehoming is a variant axis (who may list), not a separate structure.
- "Adoption platform = pet classifieds": rejected — classifieds is a generic venue with seller-set terms; the adoption platform carries welfare-placement semantics (organization accountability, screening gate, fee-as-contribution-to-care, no merchandise framing).
- "Matching algorithms are the core": rejected — no sampled platform matches adopters to animals algorithmically as its primary machinery; discovery is search/browse and the connection is routed interest. (Contrast with dating products' match-first model.)

## Boundary Findings

1. **vs Animal Shelter Management (§29 sibling — joint-review flag from that pass, discharged here)** — the sharpest boundary, and it holds. The shelter system is operator-facing custody software (animal records, intake→in-care→outcome, care events); the adoption platform is the consumer-facing venue with no custody structures at all. Evidence from this pass: RescueGroups ships the Pet Adoption Portal and Data Management as two separate services with separate guides; PetPlace is a separate consumer surface from PetPoint (same vendor family); RSPCA's platform aggregates across centres and retail partners rather than running shelter operations; the platform's listing availability is *fed by* the custody system's status but the platform holds no custody records. Structural test confirmed both ways: remove the custody lifecycle → an adoption platform remains (listings + adopter connection); remove public discovery → shelter management remains (impound/transfer-only operations still function). **Flag discharged; keep both leaves.**
2. **vs Lost Pet Platform (§29 sibling)** — different terminal transaction: new-owner placement of an unowned animal (applications, screening, fees) vs recorded reunion of an owned animal with its existing owner (sibling pass held the same test from its side). Products and organizations commonly span both (PetPlace carries both an adoption search and lost/found reporting; shelter software publishes to both).
3. **vs Classifieds Platform (§05.03) / Listings Platform (§02.11) / Directory Application (§02.11)** — generic venues list anything from anyone with seller-set terms and no placement process. The adoption platform's inventory is welfare-placement inventory: offering parties are accountable for their animals, adopters are screened rather than merely transacting, the fee is framed as contribution to care rather than price, and listings are stateful records tied to a real placement process. The newspaper "free to good home" ad is the thin ancestor on the classifieds side.
4. **vs Online Marketplace / E-commerce (§05.01/05.02)** — no cart, no product catalog, no seller ratings/reviews machinery, no shipping/fulfillment; the "transaction" is a custody transfer governed by welfare screening, completed off-platform. Animals are not merchandise; adoption fees are not market prices.
5. **vs Veterinary Practice Management / pet-service Types (§29)** — no service engagement, appointments-for-care, or client billing; the only appointment-like surface is the meet-and-greet at the shelter.
6. **vs Nonprofit fundraising Types (§25)** — donations/sponsors appear around the platform (charity platforms cross-sell insurance, display sponsors; org support includes grants), but donor cultivation is not the platform's structure.
7. **vs Dating Application (§01.07)** — the "matching" metaphor is superficial: discovery is search-based, the offering party holds the decision right, and there is no mutual-match gate. Recorded to preempt a false analogy; no real boundary risk.
8. **Internal taxonomy observation** — the leaf sits in §29 (pet services) next to its operator-side sibling; the consumer/operator pairing mirrors other §29 pairs. No taxonomy change proposed.

## Uncertainties

- Petfinder and Adopt-a-Pet — the two largest North American platforms — could not be observed first-hand (403; archive fetch failed). The sample therefore under-represents the biggest consumer platforms' adopter-side UX conventions (saved searches, application depth, on-platform messaging). Nothing in the synthesis depends on their internal behavior, but adopter-account features are calibrated as "common in modern products" rather than asserted as universal.
- PetPlace's detail pages are JavaScript-hidden; its application/connection flow is unobserved. Claims about it are limited to the observed search chrome and brand structure.
- On-platform payment for adoption fees: not observed in any sampled product; whether some modern platforms support it was not verifiable within this pass. Kept out of all definitional claims.
- The exact status vocabulary of listings (available/pending/on-hold/adopted) varies and is largely operator-side; the synthesis describes the lifecycle conceptually without asserting universal labels.
- Get Your Pet's closure suggests the standalone rehoming pole is thinning, but the rehoming-variant landscape (including Adopt-a-Pet's Rehome program) could not be verified first-hand.
- Retail adoption centres were observed only in the Australian sample; their prevalence elsewhere is unknown (kept as a variant, not a trend claim).

## Final Synthesis

The market realizes ONE Type in four supply-side shapes:

- **Open multi-org platform** (Rescue Me!): organizations and individuals post; the platform adds human review, alerting, widgets, and grants; connection is enquiry-based.
- **Syndication portal** (RescueGroups Pet Adoption Portal): the platform is primarily a distribution hub — organizations update once and populate many adoption sites, with its own public surface, form/applicant machinery, and org-to-org partnerships.
- **Federation platform** (RSPCA UK / RSPCA AU): one charity (or federation) operates the venue over its own centres — plus, in AU, retail adoption centres — with the deepest documented adoption process (application on profile → screening → meet → paperwork/fee at the centre).
- **Ecosystem search engine** (PetPlace): a shelter-software vendor's consumer surface fed by its publishing network, bundled with registry and care content.

All four share the same three-part skeleton: per-animal adoptable listings of record maintained by accountable offering parties; a pooled searchable inventory on a venue separate from the animal holders; and a connection path that routes adopter interest into the offering party's own screening-and-adoption process. The platform never holds custody and (in the observed sample) never completes the adoption transaction.

Definition (for STATUS.md): the consumer-facing adoption venue whose defining core is exactly three jointly-held structures: the adoptable-animal listing of record (persistent identified per-animal listing — identity/description/media, adoption-relevant attributes, offering party + location, availability maintained by the offering party; remove → generic pet content) + the pooled multi-party adoption inventory (listings from multiple independent offering parties aggregated into one browsable/searchable population on a venue operated separately from the animal holders; remove → a single shelter's own adoptable-pets page = shelter publishing output) + the adoption connection path (the platform's machinery routes adopter interest from a listing to the offering party — contact, inquiry, or application — and the offering party's screening/adoption process takes over, custody transfer and fee completing off-platform or at the facility; remove → read-only aggregator); jointly-held load-bearing (1 alone = pet listing page; 2 without 1 = org directory; 3 without 1+2 = contact form; 1+2 without 3 = read-only directory; 1+3 without 2 = one org's adoption page); historical check passed (printed multi-shelter adoption directories and shelter-coalition listing books satisfy all three legs with no web/apps/favorites/algorithmic matching; single-shelter adoptable-pets webpage and newspaper free-to-good-home ad are thin ancestors); standard capabilities NOT definitional: adopter accounts/favorites/saved-search alerts, rich profile narratives, org profile pages, platform-hosted application depth, guidance content, success-story showcases, syndication machinery, inter-org transfer networks, fostering surfaces, sponsor/insurance bundling; variant axes: who may list (org-only vs org+individual rehome), open network vs federation vs ecosystem vs syndication portal, retail adoption centres, species breadth, connection depth; boundaries held: vs animal-shelter-management (operator custody system vs consumer venue — joint-review flag discharged: RescueGroups ships Portal and Data Management as separate services, PetPlace separate from PetPoint), vs lost-pet-platform (new-owner placement vs recorded reunion), vs classifieds/listings/directory (welfare placement + screening + fee-as-contribution vs generic venue), vs marketplace/e-commerce (custody transfer with welfare gating, animals not merchandise, no on-platform transaction observed).
