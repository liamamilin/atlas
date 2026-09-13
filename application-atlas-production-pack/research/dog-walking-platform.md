# Research Notes — Dog Walking Platform

Research date: 2026-09-07

## Research Goal

Understand what a Dog Walking Platform actually is as a class of software: what objects exist inside it (walker profiles, owner accounts, dog profiles, walk bookings, walk reports, trust signals, payments), how dog owners and dog walkers find each other, how a walking engagement flows from discovery to completion, how trust and payment are handled around an outdoor service performed on the owner's dog, and where the Type's boundaries lie against neighboring pet-care and marketplace Types.

## Initial Boundary

Directory location: §29 Home, Family, Personal & Local Services (siblings include: Home Services Marketplace, Babysitting Marketplace, Veterinary Practice Management, Pet Grooming Management, Pet Boarding Management, Pet Daycare Management, Pet Care Business Management, Dog Walking Platform, Pet Sitting Platform, Local Service Marketplace).

Working hypothesis: a consumer-facing, two-sided platform connecting dog owners who want their dogs walked with individual dog walkers. Expected core: walker profiles + discovery + booking of walks; expected modern additions: in-app payments, GPS-tracked walks with reports, recurring schedules. Prior context from the babysitting-marketplace pass (§29 sibling, processed 2026-09-06) recorded that Pet Sitting Platform / Dog Walking Platform share the two-sided marketplace skeleton in a different care domain and are sibling Types, not aliases.

Potential confusions identified up front:

- Pet Sitting Platform (§29 sibling — custody vs walk as the service unit)
- Pet Care Business Management (§29 sibling — operator-side software for pet-care companies)
- Pet Boarding Management / Pet Daycare Management (§29 — operator-side facility administration)
- Local Service Marketplace / Home Services Marketplace (generic service brokering)
- Babysitting Marketplace (§29 sibling — same skeleton, human child care)
- Classifieds Platform (transient ads without structured profiles)
- Ride-hailing / on-demand dispatch platforms (§18 — similar request→dispatch mechanics, different object)
- Pet Adoption Platform / Lost Pet Platform (§29 — different purposes entirely)

## Research Questions

1. What are the core objects: walker profile, owner account, dog profile, walk booking, walk report, review, payment/payout?
2. Is the dog/pet profile a first-class object (in contrast to babysitting, where child profiles were not verifiable)?
3. How does discovery work: search/browse profiles, quote-request matching, on-demand dispatch?
4. What is the engagement lifecycle: request → accept → payment → meet & greet → walk → report → payout → review?
5. How is trust constructed: identity verification, background checks, reviews, platform protection/guarantees?
6. What happens during the walk itself and what is reported back (photos, GPS route, report card)?
7. How do recurring/regular walking arrangements work (weekly repeats, multi-visit)?
8. Who pays the platform and how (commission, percentage of quote, membership)?
9. What rules govern contact, cancellation, and payment release?
10. Where are the boundaries against Pet Sitting Platform, Pet Care Business Management, generic service marketplaces, and dispatch-style platforms — and does the leaf stand as an independent Type?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different geography:

1. **Mad Paws** (Australia) — largest AU pet-care marketplace; dog walking one of several services; commission monetization; detailed guarantee terms public.
2. **PetBacker** (global, 50 countries incl. Asia/EU/US) — quote-matching marketplace; walking service with documented walk report card; app-centric walker side.
3. **Holidog** (Europe, AT site observed) — European pet-care marketplace; Gassi-Service (dog walking) alongside boarding/sitting/visits; full booking-process documentation.
4. **Pawshake** (EU/global, 20+ regions) — partially observed only (region-selector root reachable; regional sites 403); evidences multi-country marketplace positioning and app-based booking, no walking-specific detail.

**Rover and Wag!** (the two largest US walking-first products) were originally desired as representatives but could not be observed: rover.com, wagwalking.com, and their help subdomains all returned HTTP 403 (Rover help additionally a transport error). Per the source-access limitation rule, no claims in this research rely on Rover/Wag observations; the on-demand-dispatch pole of the market is recorded as unverified, and the final document's assertion strength is calibrated to the three observed products.

## Sources

Observed directly (2026-09-07):

- Mad Paws — homepage (www.madpaws.com.au); Dog Walking service page (/pet-sitters/dog-walking-services); Become a Sitter page (/about/become-a-sitter); Mad Paws Guarantee terms (/about/mad-paws-guarantee)
- PetBacker — homepage (www.petbacker.com); Dog Walking page (/dog-walking); Dog Walker recruitment page (/dog-walking-job); Help Center index (/help-center, JS-rendered, index only)
- Holidog — Austrian homepage (www.holidog.com → /at); Help Centre (/at/hilfe); booking-process article (/at/hilfe/tierhalter/wie-funktioniert-der-buchungsprozess-auf-holidog)
- Pawshake — root region selector (www.pawshake.com) only

Failed / limited sources (abandoned per network rule):

- rover.com, help.rover.com — HTTP 403 / transport error (2 attempts)
- wagwalking.com, help.wagwalking.com — HTTP 403 (2 attempts)
- pawshake.com.au, pawshake.ie — HTTP 403 (regional sites; 2 attempts total)
- madpaws.brainfi.sh — JS-rendered help centre; category counts visible (339 sitter articles, 143 owner articles), article content not fetchable
- petbacker.com/help-center — JS-rendered; topic/question index visible, article bodies not fetchable

## Product Observations

Evidence layer per observation: **A** = directly observed on an official source of that product; **B** = cross-product commonality across the observed sample.

### Product A — Mad Paws (Australia)

Key observations (Layer A unless noted):

- Positioning: "Australia's largest online pet care marketplace"; services: pet hosting, pet sitting, day care, house visiting, **dog walking**, grooming, training.
- Homepage search wizard is service- and pet-aware: choose pet type (puppy under 6 months / dog / cat / other), overnight service (hosting at sitter's home vs sitting in your home), daytime service (daycare / house visits / **walking**), location, dates. Booking entry requires pet selection — pet is an input object.
- Dog Walking service page: "Your sitter will walk them in your local area"; flow: find a local walker → confirm and pay to secure booking ahead of time → walker takes the lead → peace of mind. "Easy to book … you can even set-up repeat weekly bookings for a regular exercise 'date'." Owner chooses "whether it's a 1-on-1 experience or with other dogs, for an added element of socialisation." Walker "sends photos" during/after walks (review text mentions photos + offered feeding). Meet & Greet recommended before booking ("organise a Meet & Greet with any potential Dog Walkers to make sure that it's a good fit").
- Distinction between walking and daycare is materialized as an FAQ ("What's the difference between Pet Day Care and Dog Walking?") — the two daytime services are separate bookable units.
- Trust: "All sitters have their identity verified, and can choose to add police checks"; every booking backed by the Mad Paws Guarantee; customer support 7 days a week.
- Become a Sitter (walker side): free profile with guided steps and **free safety training**; "set when and how you want to pet sit"; connected with owners; funds available **upon completion** of booking. FAQ: sitters may decline bookings but must respond to all requests in a timely manner; advised to update calendar, showcase skills on profile, always do a Meet & Greet; "consider this like your own small business" (own hours, pricing, booking choice; pause availability anytime); reading the **pet profile** and organizing Meet & Greet is the sitter's stated vetting method.
- Fees: "Mad Paws collects a 20% fee on each booking" (sitter side) + a separate owner fee; earnings claim "up to $1,600 a month" (marketing).
- Guarantee terms (full T&C page): a **commercial guarantee, explicitly "NOT INSURANCE"**; covers vet expenses (AU: up to $8,000 AUD per incident), pet-owner property damage (up to $25,000), third-party injury (up to $25,000); minimum contribution $350 AUD per incident; loss must occur during a paid, platform-processed Booking; **injuries during a pre-booking Meet & Greet are NOT covered**; 48h claim notification; 14-day documentation; treatment costs eligible only within 30 days of injury; sitters solely responsible for carrying legally required insurance; exclusions include automotive liability, ceding of care to third parties, pre-existing/breed-specific/chronic conditions.
- Help Centre exists (Brainfish-hosted; 339 sitter + 143 owner articles) but article content not fetchable.

### Product B — PetBacker (global, 50 countries)

Key observations (Layer A unless noted):

- Positioning: "world largest pet service platform", "Use Petbacker in 50 Countries"; services: pet boarding, pet sitting, **dog walking**, pet taxi, grooming, day care, training, house visits.
- Search is service + location + **pet-profile aware**: "For my pets — Add pet: Dog Cat Reptile Ferret Bird Guinea Pig Rabbit Animal" — the pet is an explicit object attached to the account and used in search/requests.
- Dog Walking page: "Book a dog walker to give your dog a **30-minute dog walk**. Your dog walker can stop by **as many times as you need—on whatever days you need them**" (recurring multi-visit walking). Price framing "from $15/walk" with bullets: 30 minutes walk / **Few Pets only** / **Route recorded**.
- **Dog Walking Report Card** (app): "Start and stop times, A map of their walk with total distance, **Pee, poo, food, and water breaks**, Cute photos and a personalized note." Walker app additionally: "Realtime dog walk report — show pet parents where you took their dog for walks and the activities you did"; "Send photos directly from your phone's camera."
- Matching flow (quote-style): "Make a request (answer questions about the service) → Match with Backers (up to 5 cost estimates) → Book to meet (place a **deposit** to schedule a **meet & greet**) → Confirm the Backer (proceed if suitable, otherwise meet others)."
- Payment/trust: "your payment stays secure until the service is complete" (escrow; "Refundable before job starts"); "100% Reservation Guarantee" (if sitter/walker cancels last minute, platform helps find a replacement or refunds); "Premium Pet Protection — your pet is covered for veterinary care in the event of an accident or unexpected emergency"; "no tips necessary"; verified transparent reviews; 24/7 support; "SPOT checks to ensure quality."
- Walker recruitment page: free to join, app-required (instant job notifications, photo sending, realtime walk report); walker obligations: respond quickly (**within 24 hours**), keep availability and account up to date, personally deliver the service, "confirm that you are legally able to provide Pet Service in your jurisdiction"; platform takes "a set percentage from the amount quoted … after you win and complete the request"; no upfront fees; encouraged: "Cage Free" service, rich photo profiles, bio.
- Reviews on homepage show walking-specific pricing units ("From 12€ / walk") and group-walk reality ("walks in local parks with a few other dogs").

### Product C — Holidog (Europe; Austrian site observed)

Key observations (Layer A unless noted):

- Positioning: "Vertrauensvolle Tierbetreuung in ganz Europa" (trusted pet care across Europe); claims 500k+ pets, 50k+ sitters; services: boarding at sitter's home (Hundebetreuung), house sitting (Hausbetreuung), **Gassi-Service / dog walking ("Tägliche Spaziergänge & Bewegung" — daily walks & exercise)**, house visits (Hausbesuche).
- Three-step flow: "Erzähl uns von deinem Haustier — Teile Persönlichkeit, Gewohnheiten…" (tell us about your pet — personality, habits) → find the match, connect with sitters, arrange a Kennenlernen (meet & greet) → book with trust: protection + regular photo updates.
- **Full booking-process documentation** (help article): 1) owner sends booking request for chosen dates + service (no payment yet); 2) sitter reviews request — **up to 72 hours to respond** — during which parties exchange messages about the pet's habits, special needs; 3) sitter accepts; owner receives notification with the clearly displayed final price (day rate + all fees); 4) owner pays securely **on the platform**; money is held ("sicher hinterlegt") and **released to the sitter only after completion of the service**; 5) Meet & Greet organized (recommended, after booking confirmed/paid); 6) service takes place; owner receives updates and photos; 7) after service: sitter is paid, owner leaves a review on the sitter's profile; request/booking status tracked in a dashboard ("My Requests").
- Trust & safety: "Nur verifizierte Sitter — Background-Checks & Referenzen" (verified sitters — background checks & references); real reviews from pet owners; "Holidog Protection" included in every booking (a **limited commercial guarantee**, T&C apply); secure payments handled by the platform; 24/7 support; emergency support.
- Chat safety controls: help categories include "Warum kann ich meine Telefonnummer oder E-Mail im Chat nicht senden?" (contact info blocked in chat), "Wann kann ich die genaue Adresse des Sitters sehen?" (sitter address visibility rules), "Wie kommuniziere ich sicher mit Sittern?" — anti-circumvention and staged-reveal patterns.
- Sitter profile transparency: concurrent-pets questions ("how many pets does the sitter care for at once, will my pet be left alone", "does the sitter have pets at home").
- Pricing help: total price formula documented for overnight services (day rate × days × pets + fees); refunds depend on cancellation timing and service type; sitter response window 72h. Live-activity feed on homepage shows nearby care/walking requests happening now.
- Monetization: membership tier ("Mitgliedschaften / Plus").

### Product D — Pawshake (partial)

Observations (Layer A, thin):

- Root serves a region selector: 20+ country sites (AU, AT, BE, CA, DK, DE, FR, HK, IE, IT, JP, LU, NL, NZ, NO, SE, UK, SG, FI, CH) with localized languages; free app "to find and book your loving pet sitter."
- No walking-specific content was reachable (regional sites 403). Included only as evidence that the multi-country pet-care marketplace population is broad; no walking-flow claims rest on Pawshake.

## Cross-product Comparison

| Dimension | Mad Paws | PetBacker | Holidog | Pawshake (partial) |
|---|---|---|---|---|
| Two-sided roles | Owner / Sitter-Walker (A) | Pet Parent / "Backer" (sitter-walker) (A) | Tierhalter / Tiersitter (A) | implied by sitter positioning (A) |
| Dog/pet profile as object | Yes: pet selection required in search; sitters "read the pet profile" (A) | Yes: "Add your Pet" attached to account & search (A) | Yes: "tell us about your pet" (personality, habits) (A) | not observed |
| Walker profiles as search object | Yes: browse reviews/profiles, skills, calendar (A) | Yes: profiles + quotes + reviews (A) | Yes: profile cards with ratings/reviews (A) | yes, positionally (A) |
| Discovery mode | Search/browse + booking | Quote-request matching (up to 5 quotes) → deposit → meet → confirm (A) | Search/browse + booking request (A) | not observed |
| Meet & Greet | Recommended, owner-organized (A) | Deposited step in flow ("Book to meet") (A) | "Part of the normal booking process", recommended (A) | — |
| Walk as service unit | Yes: distinct daytime service vs daycare; 1-on-1 or with other dogs (A) | Yes: 30-min walk unit, "few pets only", repeat visits on chosen days (A) | Yes: Gassi-Service "daily walks & exercise" (A) | — |
| Walk reporting | Photos sent by walker (A) | Report card: start/stop times, walk map + distance, pee/poo/food/water breaks, photos, note; realtime report (A) | Updates + photos during service (A) | — |
| Recurring walking | "Repeat weekly bookings — set & forget" (A) | "Stop by as many times as you need, on whatever days" (A) | "Tägliche Spaziergänge" framing (daily) (A) | — |
| Booking lifecycle | Find → confirm & pay ahead → service (A) | Request → quotes → deposit → meet → confirm → service (A) | Request → 72h review → accept w/ final price → pay (held) → meet & greet → service → payout → review (A) | — |
| Payment posture | Pay ahead on platform; funds to sitter upon completion (A) | Escrow: payment secure until service complete; refundable before job starts (A) | Platform payment held and released after service (A) | — |
| Reviews | On profiles; rating pages (A) | Transparent verified reviews (A) | Review on sitter profile after completion (A) | — |
| Verification / trust | All sitters identity-verified; optional police checks (A) | Reviewed profiles, spot checks, premium pet protection (A) | Verified sitters, background checks & references (A) | — |
| Protection | Mad Paws Guarantee: explicit NOT insurance; vet cap $8,000 AUD, property $25k, third-party $25k; $350 min contribution; meet & greet excluded (A) | Premium Pet Protection (vet care coverage) + Reservation Guarantee (rebook/refund on last-minute cancel) (A) | Holidog Protection: limited commercial guarantee, in every booking (A) | — |
| Anti-circumvention / chat safety | Not observed on fetched pages | "Communicate directly within platform" (A) | Phone/email blocked in chat; staged address reveal (A) | — |
| Walker-side economics | 20% commission per booking + owner fee; own pricing/hours; earnings on completion (A) | Percentage of quoted amount after winning/completing; no upfront fees (A) | Sitter sets rates; membership tier exists (Plus) (A) | — |
| Multi-service scope | 7 services incl. walking (A) | 8 services incl. walking (A) | 4 services incl. walking (A) | sitter-centric positioning (A) |
| Employment stance | Sitter = own small business; platform = marketplace (A) | Walker must be "legally able to provide Pet Service in your jurisdiction" (A) | Verified independent sitters (A) | — |
| Geography | Australia | 50 countries (Asia/EU/Americas) | Europe (AT site observed) | 20+ countries |

Stable commonalities (Layer B, cross-product):

- Two differentiated participant roles with separate entry paths (owner/pet parent vs walker/sitter).
- The **dog/pet profile is a first-class, account-attached object** used in search, requests, and sitter vetting (all three deep products — contrast with babysitting, where child profiles could not be verified).
- The **walker profile** is the central persistent, searchable object: photo, bio/experience, services offered, rates, availability, verification badges, reviews.
- Discovery is owner-driven: search/browse profiles, or request quotes; platform mediates contact.
- A **Meet & Greet** step is a normalized part of arranging walks (all three, in different positions of the flow).
- Walking engagements are **scheduled and repeatable**: weekly repeats, multi-visit days, daily-walk framing.
- **In-platform payment with deferred release**: money is collected up front (or as deposit) and released to the walker after the service.
- Post-service **reviews** accumulate on walker profiles.
- **Platform protection** wraps every booking — explicitly framed as a guarantee/protection, in one product's own terms "NOT INSURANCE".
- Walk reporting to the owner during/after the walk: photos/updates universally observed; structured route/distance reporting observed on one product.
- Multi-service drift: every reachable product realizes walking inside a broader pet-care marketplace (sitting, boarding, daycare…).
- Independent-provider posture: walkers are self-employed individuals; platform disclaims employer/agency role.

Key divergences: discovery mechanics (search+book vs quote matching), payment timing details, fee structure (commission vs quote-percentage vs membership), protection depth and caps, group-walk posture, geographic scope, chat-safety strictness.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Minimal structure without which the product stops being a Dog Walking Platform:

1. **Two-sided participation** — differentiated dog-owner (care-seeking) and walker (care-providing) roles, each with its own account/registration.
2. **Walker profiles** — persistent, structured, self-described identities of individual walkers carrying dog-care-relevant attributes (experience, services, rates, availability…).
3. **Owner-driven discovery and selection** — owners search/browse/request among candidate walkers and choose whom to engage.
4. **Platform-mediated engagement for a walk** — the owner initiates contact/booking with a specific walker through the platform for a dog-walking engagement: a short-duration outing in which the walker exercises the owner's dog (typically in the dog's local area, during the day, while the owner is absent or busy).
5. **Walking-engagement intent** — the platform's purpose is arranging actual dog-walking engagements (the "walk job"), not content, community, transport of the owner, or employment brokerage in the abstract.

Historical check: an older, directory-era, city-specific dog-walker listing site with structured walker profiles, owner search, and contact/messaging — with no online payments, no booking engine, no GPS, no mobile app — satisfies all five (the observed PetBacker quote-flow and Holidog's request-first flow show payment and booking mechanics vary widely while the skeleton stands). Conversely: a classifieds board of transient "dog walker wanted" ads without walker profiles/roles fails #1–2 (classifieds); an operator-side scheduling tool used by a dog-walking company fails the two-sided stranger-matching core (Pet Care Business Management); the same skeleton pointed at overnight custody of the animal is the Pet Sitting sibling. L0 stands.

### L1 — Common Mature Structure (cross-product, not definitional)

- **Dog/pet profile** as a first-class object on the owner's account (breed/size/age/personality/care notes), used in search, booking, and walker vetting.
- In-platform messaging between owner and walker, with contact-information blocking and staged information reveal before booking.
- Booking lifecycle: request → walker review/accept → platform payment (held) → optional/recommended meet & greet → service → payout on completion → review.
- Reputation layer: reviews/ratings from past owners displayed on walker profiles.
- Verification layer: identity verification at minimum; background/police checks and references in varying intensity.
- Platform protection wrapping bookings (guarantee/protection with exclusions; sometimes explicit "not insurance").
- Recurring/regular scheduling of walks (weekly repeats, multi-visit days).
- Walk reporting: photos and updates to the owner; on some products a structured walk report (times, route, distance, care breaks).
- Walker-side workspace: profile editor, availability calendar, job/request inbox, earnings/payout view.
- Cross-selling of adjacent pet-care services (sitting, boarding, daycare, grooming, training) within the same product.

### L2 — Variant / Optional Structure

- Discovery mode: search-and-book marketplace (Mad Paws, Holidog) vs quote-matching (PetBacker) vs (market-reported, unverified in this sample) on-demand instant dispatch.
- Group walking vs solo walking (explicit owner choice on one product; "few pets only" constraint on another).
- Fee architecture: sitter-side commission (20% observed), percentage of quoted amount charged post-completion, membership tiers.
- Protection depth: capped commercial guarantee with minimum contribution and exclusions vs insurance-like premium protection vs limited guarantee; caps and windows are product-specific numbers.
- Payment timing: pay-ahead-and-hold vs deposit-to-meet-then-confirm.
- Geographic scope: single-country, regional, or global (50-country) footprints; service availability varies by market.
- Surface mix: web+app marketplaces; app-centric walker operations.
- Scope envelope: walking-only positioning vs walking as one service in a multi-service pet-care marketplace (the latter is the observed norm).

### L3 — Vendor-specific (research notes only)

- Mad Paws: 20% sitter fee + owner fee; "up to $1,600/month" earnings claim; guarantee caps ($8,000 AUD vet / $25,000 property & third-party / $350 minimum contribution / 48h-14d-30d windows); Brainfish help centre; "set & forget" weekly repeats; police-check add-on; product review badges.
- PetBacker: 30-minute default walk unit; "from $15/walk" price framing; report-card field set (start/stop, map+distance, pee/poo/food/water, photos, note); 5-quote matching; deposit-to-meet; escrow refundable before start; Reservation Guarantee; Premium Pet Protection; credits/milestone vouchers; "Cage Free" ethos; 24h walker response obligation; spot checks; multi-messenger onboarding (WhatsApp/Line/WeChat…); 50-country footprint.
- Holidog: 72-hour sitter response window; price formula (rate × days × pets + fees); contact-info blocking in chat; staged sitter-address reveal; live activity feed of nearby requests; Holidog/Holivet Protection (limited commercial guarantee); Plus membership; 500k-pets/50k-sitters claims.
- Pawshake: 20+ country-site structure (region-selector root).

## Rejected Findings

- "A dog walking platform is defined by GPS-tracked walks / walk report cards" — **rejected as definitional**: route/distance reporting was directly observed on one of three deep products; photos/updates are the broader common layer. GPS-grade reporting is L1 (partial) / L2, not the core. A platform without GPS remains squarely this Type.
- "Dog Walking Platform = 'Uber for dogs' (real-time on-demand dispatch)" — **rejected/unverified**: the observed products schedule walks ahead (or match via quotes); none of the reachable sources documents instant-dispatch as the defining mechanic. The on-demand pole could not be observed (Rover/Wag blocked); recorded as a sampling limitation, not asserted.
- "The Type is walking-only products" — **rejected**: every reachable product realizes walking inside a multi-service pet-care marketplace. Walking-only scope is a legitimate variant shape but was not directly observed as the dominant structure; the leaf is defined by the walking engagement, not by single-service scope.
- "Walkers are licensed/employed professionals" — **rejected**: registration is open to individuals with verification; the only legality requirement observed is "legally able to provide the service in your jurisdiction"; the platform consistently disclaims employer/agency status.
- "Payment is definitional" — **downgraded**: all three observed products process payment, but the babysitting sibling sample contains a canonical member processing no payments; payment rails are treated as common mature structure, not part of the definition. (For dog walking specifically no payment-free product was observed; claim kept at "common", not "universal".)
- "Reviews are two-sided (walkers rate owners)" — **not established**: only owner→walker review direction clearly observed; sitter-side review of owners not verified for this sample.

## Boundary Findings

1. **vs Pet Sitting Platform (§29 sibling)**: same two-sided marketplace skeleton, different service unit — the walk (short-duration outdoor exercise outing, daytime, repeatable, dog leaves with the walker or is collected from home) vs custody (overnight/extended care at sitter's or owner's home). The reachable products serve **both** services inside one product, which is the strongest sign these are sibling service-lens Types over a shared product population rather than disjoint industries. Test: remove the walk as the service unit and keep custody → Pet Sitting Platform. Joint review recommended when Pet Sitting Platform is processed.
2. **vs Pet Care Business Management (§29 sibling)**: operator-side administration for pet-care companies (client/pet records, staff scheduling, routing, invoicing) vs consumer-side two-sided matching of strangers. Test: remove owner-facing discovery of independent walkers, keep business administration → Pet Care Business Management. (No operator-side product was fetched this pass; boundary stated structurally.)
3. **vs Babysitting Marketplace (§29 sibling, processed 2026-09-06)**: identical two-sided skeleton (profiles → discovery → contact → booking → payment → review → protection); different care domain and trust semantics — child-safety trust (background-check intensity, in-home family context) vs animal-handling trust (dog temperament, walk safety, key/home access). Notable object-level contrast: the **dog profile is a verified first-class object** in this Type (all three deep products) while child profiles were unverified in the babysitting sample.
4. **vs Local Service Marketplace / Home Services Marketplace (§05.02 / §29)**: those broker generic services (often business providers, generic job objects); this Type's invariant is the individual walker profile + animal-care trust + recurring neighborhood cadence. Test: remove the animal domain and walker-profile structure → generic service marketplace.
5. **vs Classifieds Platform (§05.03)**: transient wanted/offered ads vs persistent profiled walker identities and role-differentiated accounts. Test: remove walker profiles + two-sided roles → classifieds.
6. **vs Ride-hailing / On-demand Delivery Platforms (§18)**: request→match→service mechanics resemble dispatch, but the object is a care engagement with accumulated trust on profiles, an animal as patient, and scheduling (not real-time hailing) as the observed norm. Test: replace the care engagement with person/goods transport → dispatch platform, not this Type.
7. **vs Pet Adoption Platform / Lost Pet Platform / Pet Health Application (§29 siblings)**: shared "pet" domain vocabulary only; no service engagement matching.
8. **Employment/agency boundary**: products that employ walkers as staff or operate as an agency placing walkers are outside this Type (consistent with the babysitting pass's venue-not-employer finding; observed here as "own small business" / "legally able to provide service" postures).

"去掉什么就变成另一个 Type" summary: remove walker profiles + two-sided roles → classifieds; remove the animal/walk domain → generic local-service marketplace; remove two-sided stranger matching → pet care business management; replace the walk with custody → pet sitting platform; replace care engagement with transport of person/goods → dispatch platform.

## Uncertainties

- **Rover and Wag! unobserved** (HTTP 403 on all attempted domains, incl. help subdomains): the two largest US walking-first products could not confirm or challenge any pattern. The on-demand dispatch pole, walk-pass/subscription products, and US market structures are unverified; no product-level claims about them appear anywhere.
- **GPS tracking prevalence unknown**: directly observed on one product (route recorded, map + distance in report card); photos/updates common; the prevalence of route tracking across the market cannot be asserted.
- **Pawshake thin**: region selector only; regional sites blocked; used solely as breadth evidence.
- **Mad Paws walk-specific operational detail**: help centre is JS-rendered (339+143 articles unreachable); walk-specific articles (e.g., what a walker does with keys, leash handling rules) unobserved.
- **Key/home-access mechanics**: walkers collect the dog from the owner's home (implied by multi-visit walking while owner is out), but explicit key/lockbox/building-access features were not documented in reachable pages; not asserted.
- **Two-way reviews, cancellation windows, insurance details beyond one product's terms**: not cross-verified.
- **Walking-only products**: none directly observed in the reachable sample; their existence in the market is plausible (and market-reported) but unverified here.

## Final Synthesis

A Dog Walking Platform is a consumer-facing, two-sided platform on which dog owners and individual dog walkers meet through structured walker profiles. Owners add their dog as a first-class profile, discover and select a walker (by searching profiles or requesting quotes), and book walking engagements — short, daytime, outdoor outings of the owner's dog in its local area, frequently on a repeating schedule. The platform mediates first contact (with chat-safety controls), holds payment until the service completes, accumulates trust signals (verification badges, reviews, protection guarantees) on walker profiles, and expects a pre-engagement meet & greet. During and after walks, owners receive reports — universally photos/updates, sometimes structured route-and-care reports. Walkers are independent providers with their own profiles, availability, and pricing, and every reachable product additionally bundles adjacent pet-care services (sitting, boarding, daycare), making walking one service of a marketplace whose definition this leaf isolates. The Type is distinguished from classifieds by persistent profiled walker identities, from generic service marketplaces by animal-care trust and the walk as service unit, from pet care business management by being two-sided and consumer-facing, and from its sibling Pet Sitting Platform by the unit of care — the walk, not custody.
