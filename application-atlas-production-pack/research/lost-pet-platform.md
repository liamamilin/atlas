# Research Notes — Lost Pet Platform

## Research Goal

Understand what a Lost Pet Platform actually is as an Application Type: what records it holds, who files them, how the lost side connects with the found side, what the reunification loop looks like, and where its boundaries run against Pet Adoption Platform, Animal Shelter Management, Animal Control Management, Neighborhood Social Network, Classifieds Platform, and GPS-tracking pet apps.

## Initial Boundary

Working hypothesis before research:

- Core purpose: reunite a specific missing owned animal with its owner, by collecting lost-pet reports and found-pet reports in one venue and connecting the two.
- Likely users: pet owners (lost side), finders of stray animals (found side), volunteer/community subscribers who amplify alerts, shelter/vet professionals as partners.
- Nearest Types: Pet Adoption Platform (unowned animal → new owner), Animal Shelter Management (internal ops), Animal Control Management (licensing/enforcement), Neighborhood Social Network (lost-pet posts as generic content), Classifieds (generic listing venue).
- Known unknowns: Is the registry/microchip pole the same Type as the incident-report pole? Is matching machinery definitional or is a broadcast-alert model sufficient? Is community alerting definitional? Is a photo definitional?

## Research Questions

1. What is the core record structure — lost report, found report, pet profile, sighting, alert?
2. Who files what, and when (incident-first vs pre-registration)?
3. How do lost and found records connect — manual search, automated matching, pet-ID lookup?
4. What is the lifecycle of a report — filed → active → reunited? Is closure a first-class state?
5. What distribution surfaces exist — public listings, email/social/app alerts, flyers, vet/shelter notifications?
6. How does the registry-first pole (microchip/tag) differ structurally from the incident-first pole?
7. What community/professional roles exist (alert subscribers, volunteers, shelters, vets)?
8. What rules and exceptions matter (contact privacy, scam warnings, false-positive match alerts, deceased/sighting circumstances, ownership transfer)?
9. Business models: free nonprofit, freemium, registry fee, paid boost?
10. Where are the boundaries against adjacent Types?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

1. **PawBoost** — commercial freemium incident-first platform; community alerting network (Facebook local pages + email subscriber network + app); premium paid boost tier. Reachable, rich Tier-1/2 docs (homepage, /site/how-it-works).
2. **PetFBI** — nonprofit volunteer-run national database founded 1998 ("one of the first web-based lost and found pet databases"); free; minimal self-serve tooling; automatic matching added only 2026-03. Reachable, rich Tier-1 docs (homepage, /report.html wizard, FAQ).
3. **PetLink (Datamars)** — registry-first microchip-registry recovery service ("lifelong link… via a unique code registered in the PetLink database"); 24/7 human reunification team; professional network (vets/shelters/ACOs). Reachable, rich Tier-1/2 docs (homepage, FAQ, report flows).

Attempted but unreachable (recorded as source-access limitation):
- **Petco Love Lost** (lost.petcolove.org 403, petcolove.org/lost-pet 403) — known photo-matching reunification network across shelter partners; included only as market context, with B/C-grade evidence via sibling research files (animal-shelter-management.md observed shelter software publishing to "Petco Love/petcolove"; animal-control-management.md observed "Petco Love Lost integration" inside a licensing product). No first-hand product observation this pass.
- **AKC Reunite** (akcreunite.org 403) — microchip registry/recovery pole; same limitation. Registry pole is covered first-hand by PetLink instead.
- **24Petwatch** — root URL reachable but product redirected to the "PetPlace" adoption-first landing; only the header line "The 24Petwatch microchip registry is now on PetPlace! Report a lost or found pet" observed (A, minimal). Used only to note that registry products are expanding into adoption surfaces (span).

## Sources

- PawBoost homepage — https://www.pawboost.com/ (retrieved 2026-09-08)
- PawBoost "How Does PawBoost Work?" — https://www.pawboost.com/site/how-it-works (retrieved 2026-09-08)
- PetFBI homepage — https://petfbi.org/ (retrieved 2026-09-08)
- PetFBI report wizard — https://petfbi.org/report.html (retrieved 2026-09-08)
- PetFBI FAQ — https://petfbi.org/about-pet-fbi/frequently-asked-questions/ (retrieved 2026-09-08)
- PetLink homepage + FAQ + lost/found flows — https://www.petlink.net/ (retrieved 2026-09-08)
- 24Petwatch/PetPlace root — https://www.24petwatch.com/ (retrieved 2026-09-08, minimal)
- Sibling research (internal cross-reference, B-grade for boundary work): research/animal-shelter-management.md, research/animal-control-management.md, research/dog-walking-platform.md

## Product Observations

### PawBoost (evidence layer A throughout)

- Two-sided filing from the homepage form: "What Happened? I Lost My Pet / I Found A Stray Pet", with found-circumstance options "In my possession / Sighting (still roaming) / Deceased". Report fields observed: pet name, "Nearest Address Last Seen", contact email, account password; alert signup opt-in.
- Persistent public database: separate Lost Pets and Found Pets listings browsable by species (dog/cat/bird/all) and status; "Add your pet to the web's largest lost & found pets database. Search by location, gender, and pet type."
- Report lifecycle → reunion closure: "2,303,232 pets reported reunited"; Happy Tails success-story section; "Join 2.3M+ pet parents who have been reunited".
- Distribution machinery: post to "the PawBoost-powered Facebook page for your local area" (network of 843 local pages); email alerts to the Rescue Squad™ ("volunteers, rescue owners, shelter employees, veterinarians, and pet lovers… signed up for local lost & found pet alerts", 7.6M+ claimed); app push notification; printable "high-quality lost pet flyer" with QR code; premium tier = locally-targeted Facebook/Instagram ad campaign + Featured Pet spot.
- Shelter partnerships ("PawBoost for Shelters") and an embeddable widget for partner sites ("Add Local Lost Pets to Your Site").
- FAQ defines the alert as "like an amber alert for lost or found pets"; posting is free, premium services optional.
- Multi-country coverage claimed (US, CA, UK, AU, BR, MX, ZA); operating since 2014; mobile apps exist.

### PetFBI (evidence layer A throughout)

- Nonprofit, founded 1998, "one of the first web-based lost and found pet databases"; serves US/Canada/Puerto Rico/Virgin Islands; "services are always free of charge".
- Homepage presents exactly three core actions: Report a Lost or Found Pet ("Post to our National Database, Receive Alerts for Potential Matching Reports, and Notify our Special Agents at No Cost"); Search Reports ("Somebody may have already posted a report for the same pet. Search our national database for potential matches."); Update or Edit a Report ("Click here if your lost pet is back home, the pet you found has been reunited, or to make other changes.").
- Report wizard (A, full field list): Report Type and Location → Email Verification → Contact Info → Report Photo → Pet Info → Submit (preview). Fields: date lost/found; species; breed (filterable); colors; identifying markings; gender; approximate age/height/weight; coat type; hair length; collar description; comments; state + zip. Photo explicitly optional ("I Do Not Have a Picture").
- Contact layer: contact name; email kept private with messages auto-forwarded; phone with explicit "Make My Phone Number Public" toggle; "Send Me Email Alerts with Potential Matches — Send potential matching reports based on species and location".
- Matching = species + location alerts, manual search, and (new 2026-03) an "Automatic Report Matching Dashboard [that] instantly shows you lost and found pet reports that match yours by location, date, and animal type" — i.e., automated matching is a recent addition, not the historical form.
- Community layer: "Special Agents" = volunteers/shelter employees/rescue owners/pet lovers signed up for local area email alerts; a manual exists for them.
- Flyer machinery: report submission "create[s] a flyer automatically"; separate flyer template and flyer-posting tips.
- Closure: report editing to "back home"/reunited; Happy Tails reunion stories.
- Advisory knowledge base is prominent (lost dog/cat action plans, found pet checklists, whom to contact, flyer tips, scam warnings — "Please be aware of and protect yourself from lost pet scams" on the contact step, with a dedicated Google Voice scam-alert article). FAQ includes "Why am I receiving Potential Match Alert emails that don't look like my pet?" — loose species+location matching produces expected false positives.
- Species scope: "You can post a lost or found report for any species of pet in our database."
- Sighting flow exists in advice content ("I think I saw my lost pet on the Pet FBI website or on a Pet FBI flyer. What should I do?").

### PetLink (evidence layer A throughout; registry-first pole)

- Registry core: "Microchipping your pet creates a lifelong link from pet to owner via a unique code that is registered in the PetLink database." Owner keeps contact details current; "accurate pet and owner details are what make reunification possible." Lifetime registration, "no recurring fees for microchip registrations."
- Lost flow (documented 4 steps): 1. File a lost pet report (account login; "Takes under 2 minutes") → 2. "We alert your area": the 24/7 team "notifies local vets, shelters and rescue organisations near your pet's last known location" → 3. "Your pet goes public": listed in the public lost pet gallery, "searchable by anyone who may have found them" → 4. "You get connected": "When your pet is found or microchip scanned, we contact you immediately."
- Found flow (documented 4 steps): look for ID tag → have the pet scanned for a microchip at a vet/shelter → file a Found Pet report online (or call) → keep the pet safe.
- Owner notification on found report: "you will receive an email, text message and phone call immediately with details of the finder/rescue organization holding the pet."
- Human service layer: "24/7 access to our specialist pet reunification team"; "Unlimited 24/7 phone access to Lost Pet Professionals"; poster and social-media-post creation from the account; emergency contacts (up to 2).
- Public Lost Pet Gallery (browse pets currently reported missing); "Together Again" reunion stories.
- Professional side: register veterinary practice; register shelter/rescue/breeder; "ACO app for professionals" (animal-control officers); cross-registry lookup via PetMaxx search and AAHA petmicrochiplookup.org.
- Ownership transfer workflow between registry accounts (request, 14-day acceptance window, auto-removal) — registry-record lifecycle beyond the lost incident.
- Adjacent commerce in the same brand: GPS tracker (live tracking, geofence escape alerts), pet insurance affiliate, collars/ID tags — documented but clearly product-adjacent, not the reunification loop itself.

### 24Petwatch / PetPlace (evidence layer A, minimal — one observation)

- "The 24Petwatch microchip registry is now on PetPlace!" with a "Report a lost or found pet" header action and an adoption-search landing — registry products span into adoption surfaces; noted for the boundary discussion only.

## Cross-product Comparison

| Aspect | PawBoost | PetFBI | PetLink |
|---|---|---|---|
| Posture | incident-first community-alert platform (2014, commercial freemium) | incident-first nonprofit database (1998, free) | registry-first microchip recovery service (commercial) |
| Lost-pet report | yes — name, last-seen address, contact, circumstance | yes — full structured wizard, photo optional | yes — filed from account or via hotline/team; bound to registered pet |
| Found side | yes — "I Found A Stray Pet" with possession/sighting/deceased circumstances | yes — found reports + sightings through same database | yes — Found Pet report after tag/microchip scan; finder contacts platform |
| Pet identity substrate | free-form report content | free-form structured description; photo optional | permanent microchip code + owner-of-record contact |
| Connection mechanism | searchable lost/found database + alert-driven response | manual search + species/location match emails + (2026) auto-match dashboard | microchip-ID lookup + area alerts + public gallery |
| Distribution | local Facebook pages, email Rescue Squad, app push, QR flyers, paid boosts | email alerts to Special Agents, auto flyer, social sharing | 24/7 team notifies local vets/shelters/rescues; public gallery; posters |
| Owner-contact privacy | email-based account | private email w/ forwarding; public phone opt-in | contact details held by registry; owner contacted by platform |
| Closure state | "reported reunited" + Happy Tails | edit report: "pet is back home"/reunited | owner contacted; Together Again stories |
| Community role | Rescue Squad subscribers (volunteers/shelter staff/vets) | Special Agents volunteers | professional network: vets, shelters, rescues, ACOs |
| Shelter/vet integration | shelter partnership program, widget | partners list; shelter employees as agents | vet/shelter professional registration; scan-and-report workflow; cross-registry lookups |
| Advice content | blog tips | large knowledge base, action plans, scam warnings | lost pet guide |
| Business model | free alerts + premium boost | free/donations | registration fees; lifetime registration |
| Adjacent spans | shelter tools | ID tag shop, advice center | GPS tracker, insurance, tags, ownership transfer |

## L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Lost Pet Platform:

1. **The lost-pet report as the record of record.** A persistent, individually identified report of a specific missing owned companion animal, carrying the animal's identity/description, the last-seen circumstance (where and when), and a contact channel to the owner/representative. (Remove → a generic classified ad or social post.)
2. **The found/sighting side of the same system.** The same venue accepts found-pet and sighting reports from finders — as finder-submitted reports of a held/roaming animal, or as identifications made through a pet ID (tag/microchip) — so both halves of the reunion exist inside one system. (Remove → a one-way broadcast/poster service.)
3. **The reunification connection loop through recorded closure.** The platform's own machinery brings lost and found records together — searchable report databases, alert-driven matching by location/species, or pet-ID lookup — and the pair is carried to direct contact between finder and owner, with the report progressing to a recorded reunited/closed state. (Remove → two disconnected notice boards; a matching demo with no records; a poster service with no loop.)

Jointly-held is load-bearing:
- 1 alone = classifieds/social post
- 2 alone = found-animal directory
- 3 without 1+2 = matching algorithm with no records of record
- 1+2 without 3 = two adjacent listing boards with no connective machinery or closure
- 2+3 without 1 = a found-pet reporting channel (stray intake) — shelter intake territory
- 1+3 without 2 = a broadcast alert service with nothing to match against

Domain binding: the subject is a **specific owned companion animal** (species breadth varies — dog/cat dominate, any-pet allowed in the sample) and the goal is **reunion with the existing owner**, not placement with a new one. Remove the owned-animal binding → pet adoption; remove the reunion goal → generic classifieds.

Deliberately NOT definitional (checked against §24 historical/sample reasoning):
- photos on reports (PetFBI explicitly allows no-photo reports)
- automated/photo-AI matching (PetFBI ran on manual search + loose species/location alerts for ~28 years; auto-matching dashboard added 2026-03)
- social-media posting, apps, push notifications (none existed in 1998 form)
- community subscriber programs (PawBoost Rescue Squad / PetFBI Special Agents era post-dates the database itself)
- microchip/tag identity (incident-first pole works on description alone)
- flyers/posters, premium boosts, hotline teams, advice content, rewards

## L1 — Common Mature Structure (evidence B: present in 3/3 sample, A per product)

- Public, searchable listings of active lost and found reports (lost gallery / found gallery; search by location, species, and other attributes).
- A distribution/alerting layer that pushes reports to a local audience: email alerts to area subscribers (all 3), social posting (PawBoost, PetLink support), app push (PawBoost), vet/shelter/rescue notification (PetLink).
- Local/geographic scoping of everything: last-seen location, zip/state, "pets near you", area-defined alert audiences.
- Flyer/poster generation from the report (all 3).
- Report lifecycle management by the filer: edit, update, and mark reunited/back-home (all 3; dashboard surfaces).
- Reunion showcase (Happy Tails / Together Again; reunion counters).
- A community/participant layer beyond the two principals: alert subscribers, volunteers, shelter staff, vets.
- Shelter/vet/professional integration (partnership programs, scan-and-report, professional registration).
- Advice/guidance content around the report (action plans, tips, scam warnings).
- Contact-privacy controls on the report (private email with forwarding, public-phone opt-in, registry-held contacts).

## L2 — Variant / Optional Structure

- Identity model: incident-first (report created when the pet goes missing) vs registry-first (pre-enrolled pet profile with permanent ID; the lost report activates the recovery machinery). Also hybrids: shelters/licensing registries pre-register animals and attach lost-pet services.
- Human service layer: self-serve only (PetFBI) vs staffed 24/7 recovery team (PetLink) vs paid concierge/poster services (market context).
- Matching depth: manual search → rule-based match alerts (species+location) → automatic matching dashboards (location+date+animal type) → photo-similarity matching across shelter intakes (Petco Love Lost model — only B/C-grade evidence this pass, source unreachable).
- Promotion tiers: free base alert + paid boost (PawBoost premium); free-only (PetFBI); fee-funded registry (PetLink).
- Species breadth: dog/cat-focused surfaces vs "any species of pet"; circumstance taxonomy (possession/sighting/deceased).
- Geographic scope: national databases (US+CA+…) vs regional services (sibling research notes regional lost/found services in shelter ecosystem).
- Registry federation: cross-registry microchip lookups (PetLink → PetMaxx, AAHA lookup).
- Ownership-transfer workflows on pre-registered profiles (PetLink 14-day acceptance) — registry-side lifecycle beyond any incident.
- GPS/collar-device integration and device-commerce adjacency (PetLink GPS; boundary surface with Family Location/Safety apps).

## L3 — Vendor-specific Structure

- PawBoost: Rescue Squad™ trademark; per-area Facebook page network (843 pages); premium Facebook/Instagram ad campaign; QR-code flyer; featured-pet spots; reunion odometer counters; embeddable partner widget.
- PetFBI: Special Agent program + manual; Google Voice scam-alert article; donation-funded model; "pets found by internet" branding; the three-action homepage (report/search/update) as the entire product.
- PetLink: Lost Pet Professionals 24/7 phone team; emergency contacts (up to 2); ownership-transfer 14-day window; ACO app; PetMaxx/AAHA cross-lookups; Datamars branding; GPS/insurance cross-sell.
- 24Petwatch: PetPlace rebrand spanning registry + adoption search; consent-to-contact collected at adoption (sibling research).

## Boundary Findings

1. **vs Pet Adoption Platform** — different terminal transaction: reunification of an owned animal with its existing owner vs placement of an unowned animal with a new owner. Overlap is real: shelter software publishes to both lost/found databases and adoption portals; 24Petwatch/PetPlace spans both; some lost-pet platforms carry adoption content. Test: if the animal being processed is unowned and the outcome is a new-owner transaction with fees/applications, it is the Adoption Platform; if the record binds an owner's missing animal to a last-seen circumstance and the outcome is a recorded reunion, it is the Lost Pet Platform. Keep both leaves.
2. **vs Animal Shelter Management** — internal operations system (intake, kennel, medical, outcomes). Its lost/found matching is an optional module (sibling research: L2 variant "found-stray ↔ lost-report matching; regional services"); shelter systems publish TO lost/found databases and update microchip registries after adoption/reclaim. The shelter is a power user/partner of the Lost Pet Platform, not the same Type. If the found side degrades into stray intake and kenneling, it is shelter territory.
3. **vs Animal Control Management** — licensing/enforcement ops; lost-pet services attach to licensing registries (sibling research: tag-code lookup, Lost Pet Alerts, cross-jurisdiction pet profiles). The lost-pet service rides on the registry; the Type's center remains the reunification loop, not compliance operations.
4. **vs Neighborhood Social Network / Community Platform** — lost-pet posts are a frequent generic-content use case there, but there is no report-of-record structure, no found-side matching machinery, no closure state. A lost-pet post is a trigger that usually points back to a dedicated platform or offline process.
5. **vs Classifieds Platform** — generic listing venue; can host "lost dog" ads. The lost-pet Type differs by the two-sided report structure, the built-in connection machinery (matching/lookup/alerts), the reunification semantics (last-seen, circumstances, status), and recorded closure. The newspaper lost&found section is the below-Type thin ancestor: both sides post, but the venue holds no connection machinery and records no reunion.
6. **vs Family Location / Safety Application (GPS trackers)** — live location tracking of a device; the lost-pet Type is report-and-reunify machinery. PetLink sells a GPS tracker in the same brand: device commerce adjacent to, not part of, the reunification loop.
7. **vs Pet Health Application** — no reunification loop; shared "pet profile" vocabulary only (dog-walking-platform sibling research reached the same conclusion for its §29 neighbors).

## Uncertainties

- Petco Love Lost's photo-matching network (its defining mechanism per market reputation) could not be observed first-hand (403 on both domains). Its photo-matching posture is therefore recorded as market context with B/C-grade evidence only, sourced from sibling passes' observations of partner integrations; it did not influence the L0.
- AKC Reunite's exact lost-pet reporting workflow unobserved (403). Registry pole rests on PetLink alone for workflow detail; single-source workflow claims (e.g., multi-channel owner notification) are kept product-specific or L2.
- Reward offers as a report field: discussed in PetFBI advice content but not observed as a structured report field in any sampled product; not classified.
- Exact alert radii, match-rule parameters, retention periods, and pricing numbers: not asserted anywhere (precision not supported).
- Whether pure B2B "pet concierge" call services (posters/neighbor-calling) satisfy the L0 was not researched; noted as possible market variant.

## Final Synthesis

The market realizes ONE Type in two poles plus spans:

- **Incident-first community platform** (PawBoost, PetFBI): the lost report is created at the moment of loss; machinery = public database + local alerting + match alerts/search; closure = recorded reunion.
- **Registry-first recovery network** (PetLink): the pet profile with a permanent ID pre-exists; the lost report activates a staffed recovery process; the found side arrives mainly as tag/microchip identifications; closure = owner contacted and reunified.
- Both poles share the same three-part skeleton (lost report of record + found/sighting side + connection-to-closure loop), differ only in when the pet's identity record is created and who does the matching work (self-serve community vs staffed team).

Historical check passes: the shelter lost-and-found binder (owner files lost slip; public reports/brings found animals; staff match and call owner; animal marked returned) satisfies all three legs at analog level; PetFBI's 1998 form satisfies with none of the modern alerting/social/AI machinery; the pure newspaper lost&found classified section correctly fails the connection/closure leg (thin ancestor).

Definition (for STATUS.md): the reunification system of record for missing owned pets whose defining core is exactly three jointly-held structures: the lost-pet report of record (owner-filed persistent record: animal description, last-seen circumstance, contact channel — remove → classifieds/social post) + the found/sighting side of the same system (finder reports of held/roaming animals or pet-ID identifications entering the same venue — remove → one-way broadcast) + the reunification connection loop through recorded closure (the platform's own machinery — searchable database, location/species match alerts, or pet-ID lookup — carries lost and found records to direct contact and a recorded reunited state — remove → adjacent notice boards); jointly-held is load-bearing; standard-NOT-definitional: photos, automated/photo matching, social/app distribution, subscriber communities, flyers, registry IDs, staffed hotlines, advice content; historical check passed (shelter lost-and-found binder analog form satisfies; 1998 web database satisfies without modern machinery; newspaper lost&found section = thin ancestor); boundaries: adoption = unowned→new owner transaction; shelter management = internal ops with optional lost/found module; animal control = licensing registry with attached lost-pet services; neighborhood social/classifieds = generic content without the two-sided loop.
