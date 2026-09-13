# Research Notes — Pet Sitting Platform

Research date: 2026-09-09

## Research Goal

Understand what a Pet Sitting Platform actually is as a class of software: what objects exist inside it (sitter profiles, owner accounts, pet profiles, sit bookings, care instructions, sit updates, trust signals, payments), how pet owners and pet sitters find each other, how a sitting engagement flows from discovery through the sit itself to completion, how trust and payment are handled around custody care of an animal in a home, and where the Type's boundaries lie against the neighboring pet-care and marketplace Types — above all the mandatory joint review with Dog Walking Platform.

## Initial Boundary

Directory location: §29 Home, Family, Personal & Local Services (siblings: Home Services Marketplace, Babysitting Marketplace, Veterinary Practice Management, Pet Grooming Management, Pet Boarding Management, Pet Daycare Management, Pet Care Business Management, Dog Walking Platform, Pet Sitting Platform, Pet Training Management, Pet Adoption Platform, Animal Shelter Management, Lost Pet Platform, Pet Health Application).

Working hypothesis: a consumer-facing, two-sided platform connecting pet owners who need someone to care for their animals while away with individual pet sitters. Expected core: sitter profiles + discovery + booking of sitting engagements; expected service shapes: sitting in the owner's home, sitting in the sitter's home, drop-in visits; expected modern additions: in-app payments, photo updates, care instructions, protection plans.

Prior context carried into this pass:

- **dog-walking-platform pass (2026-09-07)** left a MANDATORY joint review: the reachable product population is shared (every deep-observed dog-walking product is a multi-service pet-care marketplace offering sitting/boarding/daycare alongside walking); adopted leaf boundary = service-unit discriminator walk (short daytime outdoor outing) vs custody (overnight/extended care); both Types stand as separate service lenses over one population. Rover/Wag were unobservable (HTTP 403) in that pass.
- **babysitting-marketplace pass (2026-09-06)**: same two-sided skeleton in the childcare domain; sibling Types, not aliases; child profiles unverified there (contrast noted for pet profiles).
- **pet-boarding-management pass (2026-09-09)**: held from its side that sitting = care without a facility accommodation inventory (in the pet's home or caregiver's home); "1+2 without 3 = sitting-style booking — Pet Sitting territory".
- **pet-care-business-management / pet-daycare-management / pet-grooming-management passes (2026-09-09)**: operator-side systems of record vs consumer-side two-sided marketplaces.

Potential confusions identified up front:

- Dog Walking Platform (§29 sibling — walk vs custody as the service unit; joint review mandatory)
- Pet Boarding Management (§29 sibling — operator-side facility administration with accommodation inventory)
- Pet Care Business Management (§29 sibling — operator-side software for pet-care companies)
- Babysitting Marketplace (§29 sibling — same skeleton, human child care)
- Home Services Marketplace / Local Service Marketplace (generic service brokering)
- Classifieds Platform (transient ads without structured profiles)
- Household Staff Management (live-in sitters vs domestic staff employment)
- Pet Adoption Platform / Lost Pet Platform / Pet Health Application (shared pet vocabulary, different purpose)

## Research Questions

1. What are the core objects: sitter profile, owner account, pet profile, sit booking, care instructions, sit updates, review, payment/payout?
2. What are the sitting service shapes: in-owner's-home sitting (house sitting), at-sitter's-home sitting, drop-in visits — and how do products materialize the differences?
3. How does discovery work: owner searches sitter profiles, owner posts a listing that sitters apply to, or request-and-quotes? Who holds selection agency?
4. What is the engagement lifecycle: request/application → accept → payment → meet & greet → the sit → updates → payout → review?
5. How is trust constructed: identity verification, background checks, references, reviews, platform protection?
6. What happens during the sit: care instructions, photo updates, home-care duties (plants, mail, security)?
7. How do payment and monetization work — and is payment to the sitter definitional (membership/exchange models exist)?
8. What rules govern contact, cancellation, payment release, home access?
9. Where are the boundaries against Dog Walking Platform (joint review), Pet Boarding Management, Pet Care Business Management, generic marketplaces, classifieds — and does the leaf stand as an independent Type?
10. Historical check: would older, directory-era, regional sitter-listing products still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different geography/monetization:

1. **TrustedHousesitters** (global: UK/US/AU/CA + more) — house-sitting-first platform with a membership/exchange philosophy: sitters are unpaid and care in exchange for homestays; the platform monetizes memberships on both sides. Radically different economics from commission marketplaces.
2. **Mad Paws** (Australia) — largest AU pet-care marketplace; commission monetization; explicit service taxonomy separating Sitting (in your home) / Hosting (at sitter's home) / House visiting; detailed guarantee terms public.
3. **PetBacker** (global, 50 countries) — quote-matching marketplace; drop-in visits vs overnight house sitting distinction; per-visit pricing; escrow payment; sitting report card.
4. **Holidog** (Europe; AT site observed) — request-based European pet-care marketplace; Hausbetreuung (house sitting) alongside Hundebetreuung (boarding at sitter's home) and Hausbesuche (visits); full booking-process documentation (carried from the walking pass, sitting-specific service definitions observed this pass).

**Rover** (the largest US sitting/walking platform) was desired as a representative but could not be observed: rover.com returned HTTP 403 (consistent with the dog-walking pass, where rover.com, wagwalking.com and their help subdomains were all blocked). Per the source-access limitation rule, no claims in this research rely on Rover observations; the US market pole and the on-demand-dispatch style remain unverified and deliberately uncharacterized.

## Sources

Observed directly (2026-09-09):

- TrustedHousesitters — homepage (trustedhousesitters.com); How it works — find a sitter (/how-it-works/find-a-sitter/); How it works — find a house sit (sitter side, /how-it-works/find-a-house-sit/); Trust and safety (/trust-and-safety/)
- Mad Paws — homepage (www.madpaws.com.au); Pet Sitting service page (/pet-sitters/house-pet-sitting)
- PetBacker — Pet Sitting service page (www.petbacker.com/pet-sitting)
- Holidog — Austrian homepage (www.holidog.com/at) with service definitions and live-activity feed

Failed / limited sources (abandoned per network rule):

- rover.com — HTTP 403 (1 attempt this pass; 2 attempts in the dog-walking pass)
- madpaws.com.au/pet-sitters/pet-sitting-services, /pet-sitters/pet-sitting — HTTP 404 (URL guesses; correct page found via homepage navigation)
- holidog.com/at/hausbetreuung — HTTP 404 (URL guess; service definitions observed on the homepage instead)
- madpaws.brainfi.sh help centre — JS-rendered (carried limitation from walking pass; article content not fetchable)
- petbacker.com/help-center — JS-rendered (carried limitation)
- support.trustedhousesitters.com — not fetched (time budget; homepage + how-it-works + trust pages sufficient)

## Product Observations

Evidence layer per observation: **A** = directly observed on an official source of that product; **B** = cross-product commonality across the observed sample.

### Product A — TrustedHousesitters (global)

Key observations (Layer A unless noted):

- Positioning: "Find Pet Sitters & House Sits Worldwide"; "16 years of happy pets, 280k+ happy members"; B Corp certified; community forum.
- **Membership/exchange economics**: two membership products — Pet Parent membership ("Sitters don't charge", "Verified sitters", "Home & Contents Plan") and Sitter membership ("Unlimited access to sits", "Worldwide sits", "Free verifications"); combined membership available. "It's a simple exchange – our experienced sitters don't charge. You give them a new place to stay on their travels and in return, they'll care for your home and pets." Sitters "exchange their time, care and expertise for interesting homestays and unique travel experiences."
- **In-home care**: "Connect with verified pet sitters for in-home care while you're away"; "Pets stay happy at home with a sitter who gives them loving care and companionship."
- **Owner flow (listing-based, sitters apply)**: "Our pet sitters reach out to you" — 1) Create your listing ("Tell sitters about you, your home, pets and their care requirements") → 2) Choose your sitter ("Review sitter applications and vet them before you commit") → 3) Travel worry free. The owner reviews applications and selects.
- **Sitter flow**: purchase annual sitter plan → create profile ("plenty of pictures, personality, and sitter verifications") → "Apply for unlimited sits — Explore, apply for, and confirm exciting sits" → "Experience life elsewhere — Stay in a home away from home with a new pet companion, keeping them safe while their parent's away."
- **Trust & safety**: third-party verification including ID and background checks; sitter vetting requires "Background checks, ID checks, External references, Email & phone verification" before sitters can apply; checks visible on profiles. Reviews run **both directions**: pet parents review sitters on sitter profiles, and sitters leave feedback "for pet parents" / on their listings ("Find honest feedback from sitters… reviews left by fellow sitters on their listing").
- **Protection**: Home & Contents Plan — "cover against property damage, theft, and sitter accidents, available on certain plans."
- **Vet support**: 24/7 Vet Advice Line sitters can call during a sit; year-round vet video calls for pet parents on certain plans.
- **Animal breadth**: dogs, cats, poultry, horses, fish, birds, reptiles, livestock, small pets.
- Sitter profile cards: "Experienced pet sitters", "Administers medication", "Verified", 5-star rating, review counts (e.g. 175 reviews). "98% of our sits result in a five-star review." "Over 100,000 experienced sitters."
- App ("Stay on top of your sit, wherever you go").

### Product B — Mad Paws (Australia)

Key observations (Layer A unless noted):

- Positioning: "Australia's largest online pet care marketplace"; "1,745,000+ bookings"; "300,000 reviews of pet sitters".
- **Search wizard is service- and pet-aware**: pet type (puppy under 6 months / dog / cat / other) + **Overnight services: Hosting ("At sitter's home") vs Sitting ("In your home")** + Daytime services (Daycare / House visits / Walking) + location + dates from–until + "Add your pets" (required input).
- **Service taxonomy** (homepage + sitting page): Hosting — overnight, "Your pet stays at your sitter's home"; **Sitting — overnight, "Your sitter stays with your pet in your home. Best in show care where your pet is most comfortable."**; Day care; **House visiting — "The sitter drops in to visit your pet, giving them food, water and a toilet break."**; Dog walking; Dog grooming; Dog training. Animal-specific sitting lines in navigation: dog, cat, bird, puppy, rabbit, guinea pig sitting; separate "House Sitting" line also exists in navigation (not fetched).
- **Sitting page value framing**: "2-in-1 solution — Your pet stays in their own familiar environment, with the bonus of having a house sitter too"; "Unlike a boarding kennel or cattery, your pet receives tailored care as unique as they are!"; "Constant contact — Stay in touch with your furry friend through regular photo updates while you're away"; FAQ "What's the difference between a Pet Sitter and a Boarding Kennel or Cattery?"
- **Sitting flow**: 1) Find a 5-star Sitter — "Confirm and pay to secure your booking ahead of time" → 2) "The staycay begins — Your pet is cared for in the comfort of their (your) home" → 3) "Receive updates — Get regular photo updates for your peace of mind."
- **Home-care adjunct** (editorial): house+pet sitting combo; "someone to look after your pet and maintain your home – after all, your plants need care and attention too!"; home security while on holiday; undivided attention "especially important if your furry friend requires constant supervision or medication."
- Trust: "All sitters are vetted", identity verified, optional police checks; every booking backed by the Mad Paws Guarantee ("up to $8,000 in vet care for eligible claims"); customer support 7 days a week. FAQ: "Can you meet a Pet Sitter before making a booking?"
- How it works (platform level): Search for a Sitter → Chat then book → Enjoy peace of mind.

### Product C — PetBacker (global, 50 countries)

Key observations (Layer A unless noted):

- Positioning: "world largest pet service platform"; services: pet boarding, pet sitting, dog walking, pet taxi, grooming, day care.
- **Sitting page**: "PET SITTING MADE EASY — Get 5 Prices from Pet sitters nearby. Choose the Best Profile or Price." Price framing "from $20/visit" with bullets: Personal Care, Feeding & walk, **Daily Photo Updates**.
- **Drop-in visits vs overnight house sitting** — explicit service-shape choice: "How do I know if Drop-in Visits or Overnight House Sittings is right for me?" with criteria: cats stressed in new environments; long-term bookings; low-maintenance pets; senior pet who prefers to stay at home; caged pocket pets (fishes, tortoises, rabbits, birds); "While I'm away, I want someone to drop by daily to check on my home"; "help in small house tasks like watering the plants and picking newspapers."
- **Quote-matching flow**: Click Book → "Get 5 Sitters to choose from instantly" → Deposit ("It's secure & no tips necessary") → Meet & Greet ("Meet your trusted sitters"). "We send your need to 30+ pet sitters instantly."
- **Trust & payment**: Reservation Guarantee (last-minute cancel → platform helps find a new one); Secure Payment ("Escrow Payment & Refundable before job starts"); Free Protection ("Every stay booked through PetBacker is covered by premium protection"); 24/7 support + SPOT checks; transparent verified reviews; Royalty Rewards (discount credits per spend).
- **Sitting report card** (app): "Visit time, Pee, poo, food, and water, Photos and a personalized note, Protect your home while you're away."
- **Editorial on sitting shapes**: two types — sitters who "come to the house at specified times to feed, bathe and taking it for a poop" (visit length "determined by both pet owners and pet sitters, averaging from fifteen to forty-five minutes") vs "live-in sitters" who "live at the pet owner's house so the pets have a constant companion, or at least a companion at night"; home-protection benefits (mail/newspaper collection removes 'away from home' signals; live-in sitters deter burglaries; plant care, phone messages); "priced lower than that of commercial boarding facilities"; "per-visit or a per-day basis" billing; extra charges for multiple pets, travel, special services.

### Product D — Holidog (Europe; Austrian site observed)

Key observations (Layer A unless noted):

- Positioning: "Vertrauensvolle Tierbetreuung in ganz Europa" (trusted pet care across Europe); 500k+ pets, 50k+ sitters, 4.9/5.
- **Service definitions** (homepage): Hundebetreuung (boarding_at_sitter — "Liebevolles Zuhause für dein Tier"); **Hausbetreuung (house_sitting — "Betreuung bei dir zu Hause" = care at your home)**; Gassi-Service (dog_walking — daily walks); **Hausbesuche (visits — "Füttern, Spielen & nach dem Rechten sehen" = feeding, playing & seeing to things)**.
- **Live-activity feed**: "Gerade passiert — Sieh aktuelle Anfragen von Tierhaltern in deiner Nähe" (current requests from owners nearby), e.g. "Jacqueline hat Hausbesuche bei Anna angefragt" — request-based discovery made visible.
- **Flow**: "Erzähl uns von deinem Haustier — Teile Persönlichkeit, Gewohnheiten" (tell us about your pet — personality, habits) → "Finde den perfekten Match — Verbinde dich mit fürsorglichen Sittern und vereinbare ein Kennenlernen" (find the match, arrange a meet & greet) → "Mit Vertrauen buchen — Sichere Buchung mit Schutz und regelmäßigen Foto-Updates" (book with trust: protection + regular photo updates).
- **Trust**: "Nur verifizierte Sitter — Background-Checks & Referenzen"; real reviews; "Premium-Schutz — Versicherung & sichere Zahlungen"; Holivet Protection "begrenzte kommerzielle Garantie" (limited commercial guarantee) included in every booking; 24/7 + emergency support; secure platform payments.
- Sitter profile cards with ratings, review counts, "TOP" badges; owner reviews quoted on cards ("regular updates and photos").
- Full booking-process documentation (help article, carried from the walking pass — same machinery serves sitting): request → sitter reviews (72h window) → accept with final price → pay on platform (held, released after completion) → meet & greet → service → payout → review; chat contact-info blocking; staged sitter-address reveal.

## Cross-product Comparison

| Dimension | TrustedHousesitters | Mad Paws | PetBacker | Holidog |
|---|---|---|---|---|
| Two-sided roles | Pet Parent / Sitter (A) | Owner / Sitter (A) | Pet Parent / Pet Sitter (A) | Tierhalter / Tiersitter (A) |
| Sitter profile as central object | Yes: profile cards (experience, medication capability, verified badge, reviews) (A) | Yes: 5-star sitter search, vetted profiles (A) | Yes: "Choose the Best Profile or Price" (A) | Yes: sitter cards with ratings, TOP badges (A) |
| Pet profile as first-class object | Yes: listing carries pets + care requirements (A) | Yes: "Add your pets" required in search (A) | Yes: pet-profile-aware requests (A) | Yes: "tell us about your pet" (personality, habits) (A) |
| Discovery mode | Owner posts listing → sitters apply → owner chooses (A); sitters also browse sits (A) | Owner searches sitters → chat → book (A) | Request → 5 quotes → deposit → meet & greet (A) | Search/browse + request; live activity feed (A) |
| Sitting service shapes | In-home house sitting (sitter stays in owner's home) (A) | Sitting (in your home, overnight) / Hosting (at sitter's home) / House visiting (A) | Drop-in visits (per-visit) / Overnight house sitting / live-in (A) | Hausbetreuung (at your home) / Hundebetreuung (at sitter's home) / Hausbesuche (A) |
| Duration envelope | Days to weeks; annual membership, unlimited sits (A) | Overnight, dated from–until (A) | Per-visit (15–45 min editorial) or overnight/per-day (A) | Day-rate × days (carried) (A) |
| Home-care adjunct | "care for your home and pets" (A) | "2-in-1… house sitter too", plants, home security (A) | "watering the plants and picking newspapers", daily home check (A) | implied in Hausbetreuung (A) |
| Updates during the sit | photo updates (A) | regular photo updates (A) | Daily Photo Updates + report card (visit time, pee/poo/food/water, photos, note) (A) | regular photo updates (A) |
| Meet & greet | not named on fetched pages; application/vetting step instead (A) | FAQ: "Can you meet a Pet Sitter before making a booking?" (A) | Deposited flow step "Meet & Greet" (A) | "Kennenlernen" flow step (A) |
| Payment posture | Sitters don't charge; membership fees both sides (A) | Pay ahead on platform; guarantee (A) | Escrow, refundable before start; deposit (A) | Pay on platform, held, released after service (carried) (A) |
| Reviews | Two-way: parents review sitters; sitters review parents/listings (A) | Owner→sitter (A) | Transparent verified reviews (A) | Owner→sitter (A) |
| Verification | Background checks, ID checks, external references, email/phone verification — required before applying (A) | Identity verified; optional police checks (A) | SPOT checks (A) | Background checks & references (A) |
| Protection | Home & Contents Plan (property damage, theft, sitter accidents; certain plans) (A) + Vet Advice Line (A) | Mad Paws Guarantee (up to $8,000 vet care) (A) | Premium Protection + Reservation Guarantee (A) | Holivet Protection (limited commercial guarantee) (A) |
| Monetization | Membership (both sides) (A) | Commission per booking (carried) (A) | Percentage of quoted amount (carried) (A) | Membership tier (carried) (A) |
| Multi-service scope | Sitting/house-sitting only (A) | 7+ services incl. walking, hosting, daycare (A) | 6+ services incl. boarding, walking (A) | 4 services incl. boarding, walking, visits (A) |
| Geography | Global (UK/US/AU/CA/…) (A) | Australia (A) | 50 countries (A) | Europe (A) |

Stable commonalities (Layer B, cross-product):

- Two differentiated participant roles with separate entry paths (owner/pet parent vs sitter).
- The **sitter profile** is the central persistent, searchable object: photo, bio/experience, services, capabilities (e.g. administers medication), availability, verification badges, reviews.
- The **pet profile is a first-class, account-attached object** used in search, listings/requests, and sitter vetting (all four products — consistent with the dog-walking pass finding).
- **Owner-driven selection** in every observed discovery mode: the owner chooses among candidates (searched profiles, applicants to a listing, or quotes).
- The **sitting engagement**: care responsibility for the animal over a bounded period while the owner is away — overnight/multi-day stays in the animal's own home or the sitter's home, or recurring in-home visits; never a commercial facility.
- **Photo updates to the owner during the sit** — universal in this sample ("regular photo updates" on three products; "Daily Photo Updates" + report card on the fourth).
- **Care requirements travel with the pet**: personality, habits, medication, routines are inputs to matching and the sit.
- **Trust layer**: identity verification at minimum; background checks/references in varying intensity; reviews; platform protection wrapping sits.
- **Meet & greet / Kennenlernen** normalized before the sit (three products explicitly; the fourth substitutes an application/vetting step).
- **Home-care adjunct** in in-home sitting: plants, mail, home security, "checking on my home" (three products explicitly).
- **Independent-provider posture**: sitters are not employees; the platform is a venue (membership, commission, or quote-percentage monetization).
- **Multi-service drift**: three of four products bundle sitting inside a broader pet-care marketplace (walking, boarding, daycare); one is sitting-only.

Key divergences: monetization architecture (commission vs quote-percentage vs membership-exchange with unpaid sitters), discovery direction (search vs listing-applications vs quotes), service-shape emphasis (in-owner's-home vs at-sitter's-home vs drop-in), protection depth, review directionality, geographic scope.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Minimal structure without which the product stops being a Pet Sitting Platform:

1. **Two-sided participation** — differentiated pet-owner (care-seeking) and sitter (care-providing) roles, each with its own account/registration.
2. **Sitter profiles** — persistent, structured, self-described identities of individual sitters carrying pet-care-relevant attributes (experience, services, capabilities, availability, verification, reviews).
3. **Owner-driven discovery and selection** — owners find, evaluate, and choose sitters (by browsing profiles, posting a sit listing that sitters apply to, or requesting quotes); the selection agency always stays with the owner.
4. **Platform-mediated sitting engagement** — the engagement arranged through the platform is a **sit**: the sitter assumes care responsibility for the owner's animal over a bounded period while the owner is away or unavailable, with care delivered in the animal's own home or the sitter's home — not in a commercial facility.

Historical check (§24): an older, directory-era, city- or country-specific pet-sitter listing site — structured sitter profiles, owner search, contact/messaging, no online payments, no booking engine, no app — satisfies all four (payment mechanics vary wildly across the sample, including a canonical member where sitters are unpaid; the skeleton stands without any of them). Conversely: a classifieds board of transient "pet sitter wanted" ads fails #1–2 (classifieds); an operator-side scheduling/billing tool used by a sitting company fails the two-sided stranger-matching core (Pet Care Business Management); a facility with managed kennel inventory fails #4's no-facility property (Pet Boarding Management); the same skeleton pointed at short outdoor outings is the Dog Walking sibling. L0 stands.

### L1 — Common Mature Structure (cross-product, not definitional)

- **Pet profile** as a first-class object on the owner's account (species/breed/age, temperament, habits, medication and care requirements), used at search, listing, request, and vetting time.
- **Care requirements/instructions** attached to the pet or the sit, consumed by the sitter during the engagement.
- In-platform messaging between owner and sitter, with contact-information blocking and staged information reveal before booking (documented in the sibling pass on the same machinery).
- **Booking lifecycle**: request/application → sitter review/accept → platform payment (held) → meet & greet → the sit period → payout/settlement → review.
- **Photo updates** from the sitter during the sit (universal in this sample); structured visit/sit report on one product (times, care events, photos, note).
- **Trust layer**: identity verification at minimum; background checks, external references, email/phone verification in varying intensity; reviews; platform protection (guarantee/insurance-like plans) wrapping sits.
- **Meet & greet** as a normalized pre-engagement step.
- Sitter-side workspace: profile editor, availability, applications/requests inbox, earnings or sit-dashboard.
- **Multi-service bundling** (walking, boarding, daycare, grooming) in most products — sitting is one service of a marketplace.

### L2 — Variant / Optional Structure

- **Service-shape mix**: in-owner's-home sitting (house sitting), at-sitter's-home sitting, drop-in visits; animal-specific lines (cat, bird, rabbit, puppy, guinea pig sitting); long-term sits.
- **Monetization architecture**: per-booking commission, percentage of quoted amount, membership tiers — and the **exchange model** where sitters are unpaid and the platform sells memberships to both sides (payment-to-provider is therefore NOT definitional).
- **Discovery direction**: owner-searches-sitter vs owner-posts-listing-and-sitters-apply vs request-and-quotes.
- **Protection depth**: capped commercial guarantee vs home & contents cover (property damage, theft, sitter accidents) vs insurance-like premium protection; caps and windows are product-specific numbers.
- **Home-care scope**: pet-only vs pet+home duties (plants, mail, security presence).
- **Review directionality**: owner→sitter universal in sample; sitter→owner explicit on one product.
- **Geographic scope**: single-country, regional, global footprints.
- **Duration envelope**: overnight weekends to multi-week/long-term sits; per-visit vs per-day vs per-sit pricing.

### L3 — Vendor-specific (research notes only)

- TrustedHousesitters: membership plan structure (Pet Parent / Sitter / combined); "sitters don't charge"; Home & Contents Plan; 24/7 Vet Advice Line + vet video calls on certain plans; external-references check; email/phone verification; 100k+ sitters / 280k+ members / 16 years claims; "98% of sits result in a five-star review"; B Corp; community forum; app.
- Mad Paws: search-wizard structure (pet type → overnight service → daytime service → dates); guarantee up to $8,000 vet care; police-check add-on; 1,745,000+ bookings / 300,000 reviews claims; animal-specific sitting lines; separate House Sitting navigation line; $25 referral program; 20% sitter fee + owner fee (carried from walking pass).
- PetBacker: "from $20/visit" framing; 5-quote matching; deposit-to-meet; escrow refundable before start; Reservation Guarantee; Premium Protection; SPOT checks; Royalty Rewards; report-card field set; "30+ pet sitters instantly" broadcast; 15–45 min visit average and live-in sitter editorial; per-visit/per-day billing; extra charges for multiple pets/travel.
- Holidog: 72-hour sitter response window; price formula (rate × days × pets + fees); Holivet Protection; live-activity feed of nearby requests; TOP badges; 500k-pets/50k-sitters claims; chat contact-info blocking + staged address reveal (carried).

## Rejected Findings

- "A pet sitting platform is defined by paid sitters / per-night rates" — **rejected as definitional**: TrustedHousesitters' sitters don't charge (membership-exchange model); PetBacker prices per visit. Payment-to-provider is common mature structure, not the core. The invariant is the care engagement, not the wage.
- "Sitting means only in the owner's home" — **rejected**: at-sitter's-home sitting (Hosting / Hundebetreuung) is a first-class shape on three of four products; the no-facility property, not the specific home, is the invariant.
- "Drop-in visits are a different Application Type" — **rejected**: they are an in-home care shape within the sitting family (feeding, toilet break, home check while the owner is away); the boundary vs walking is the venue/care character (home care vs outdoor outing), not duration.
- "House sitting makes this a property-care platform" — **rejected**: the home-care adjunct (plants, mail, security) exists in service of the pet-care engagement; the animal is the center in every product's model.
- "GPS tracking / structured sit reports are definitional" — **rejected** (carried from the walking pass): structured reporting observed on one product; photo updates are the broader common layer.
- "Two-way reviews are definitional" — **not established**: explicit on one product (sitters review owners/listings); owner→sitter direction universal; prevalence across the market unknown.
- "Sitters are licensed professionals" — **rejected**: registration is open to individuals with verification; platforms disclaim employer/agency status (consistent with sibling passes).

## Boundary Findings

1. **vs Dog Walking Platform (§29 sibling) — MANDATORY JOINT REVIEW, discharged from this side**: the two Types share one product population — three of this pass's four products also sell walking, and the walking pass observed the same population from the other side (Mad Paws, PetBacker, Holidog all bundle both). The adopted discriminator holds from this side: the service unit is **custody care** (the sitter assumes care responsibility for the animal in its home or the sitter's home over a bounded period while the owner is away) vs the **walk** (a short outdoor outing, dog collected and returned). Both Types stand as separate service lenses over one population; a product offering both participates in both Types. Removal tests: remove custody care, keep outings → Dog Walking Platform; remove outings, keep custody care → Pet Sitting Platform. RATIFIED — keep both leaves.
2. **vs Pet Boarding Management (§29 sibling)**: operator-side system of record for a boarding facility with a managed accommodation inventory (kennels/runs, capacity, occupancy) vs consumer-side two-sided marketplace of individual sitters caring in homes with **no facility inventory object** (a sitter's home capacity is just the sitter's own stated limit). The boarding pass held this from its side ("sitting-style booking = no facility inventory"); ratified here. Test: add a managed facility inventory → boarding management; remove it → sitting territory.
3. **vs Pet Care Business Management (§29 sibling)**: operator-side administration of a pet-care company's own clients and staff vs two-sided matching of strangers. Test: remove owner-facing discovery of independent sitters, keep business administration → Pet Care Business Management.
4. **vs Babysitting Marketplace (§29 sibling, processed 2026-09-06)**: identical two-sided skeleton (profiles → discovery → contact → booking → trust → review); different care domain and trust semantics — child-safety trust vs animal-care trust. Object-level contrast confirmed: the **pet profile is a verified first-class object in all four products of this sample**, while child profiles were unverified in the babysitting sample.
5. **vs Home Services Marketplace / Local Service Marketplace (§29 / §05.02)**: those broker generic services (often business providers, generic job objects); this Type's invariant is the individual sitter profile + animal-care trust + home-venue custody care. Test: remove the animal domain and sitter-profile structure → generic service marketplace.
6. **vs Classifieds Platform (§05.03)**: transient wanted/offered ads vs persistent profiled sitter identities and role-differentiated accounts. Test: remove sitter profiles + two-sided roles → classifieds.
7. **vs Household Staff Management (§29)**: live-in sitters resemble domestic staff, but the sitting platform's engagement is a dated animal-care arrangement between strangers, not employment placement of household staff; platforms explicitly disclaim employer status.
8. **vs Pet Adoption Platform / Lost Pet Platform / Pet Health Application (§29 siblings)**: shared "pet" vocabulary only; no service-engagement matching (pet-adoption pass already flagged this seam as "expected clean" — confirmed).

"去掉什么就变成另一个 Type" summary: remove custody care, keep outings → dog walking platform; add a managed facility inventory → pet boarding management; remove two-sided stranger matching → pet care business management; remove the animal domain → generic local-service marketplace; remove sitter profiles + roles → classifieds; replace the animal with a child → babysitting marketplace.

## Uncertainties

- **Rover unobserved** (HTTP 403 this pass; all domains blocked in the walking pass): the largest US sitting/walking platform could not confirm or challenge any pattern. US market structures, the on-demand instant-dispatch pole, and Rover-specific sitting mechanics (e.g., how its sitting shapes are packaged) are unverified; no product-level claims about Rover appear anywhere.
- **Key/home-access logistics** (keys, lockbox, handover rituals) are implied by in-home sitting but not explicitly documented in reachable pages; not asserted.
- **TrustedHousesitters help centre not fetched**: cancellation rules, sit-extension behavior, and verification depth beyond the trust page not detailed.
- **Two-way review prevalence** unknown beyond one product.
- **Mad Paws / PetBacker help centres JS-rendered** (carried limitation): sitting-specific operational articles (what a sitter does with keys, multi-pet households, medication rules) unobserved.
- **Mad Paws' separate "House Sitting" line** (navigation only, not fetched): relationship between "At Pet's Home" sitting and the standalone house-sitting line unverified.
- **Whether pure property-only house sitting** (no pets) is a first-class service on these platforms: observed in navigation (Mad Paws) but not studied; this leaf's center is pet care.

## Final Synthesis

A Pet Sitting Platform is a consumer-facing, two-sided platform on which pet owners and individual pet sitters meet through structured sitter profiles. Owners add their pets as first-class profiles carrying care requirements, discover and select a sitter — by searching profiles, posting a sit listing that sitters apply to, or requesting quotes — and book sitting engagements: the sitter assumes care responsibility for the animal over a bounded period while the owner is away, delivering care in the animal's own home (often alongside looking after the home) or in the sitter's home, or through recurring in-home drop-in visits — never in a commercial facility. The platform mediates first contact (with chat-safety controls), holds payment until the service completes — or, in the membership-exchange variant, charges memberships while sitters stay unpaid — accumulates trust signals (verification badges, reviews, protection plans) on sitter profiles, and expects a pre-engagement meet & greet. During the sit, owners receive photo updates; afterwards, reviews accumulate on profiles. Sitters are independent providers, and most current products bundle sitting inside a multi-service pet-care marketplace; the sitting lens isolates custody care. The Type separates from Dog Walking Platform on the unit of service (custody vs outing) over a shared product population, from Pet Boarding Management on the absence of a facility accommodation inventory, from Pet Care Business Management on being two-sided and consumer-facing, and from generic marketplaces and classifieds on the sitter-profile structure and animal-care trust semantics.
