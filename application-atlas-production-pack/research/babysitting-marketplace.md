# Research Notes — Babysitting Marketplace

Research date: 2026-09-06

## Research Goal

Understand what a Babysitting Marketplace actually is as a class of software: what objects exist inside it (caregiver profiles, family accounts, job posts, bookings, trust signals), how families and caregivers find each other, how an engagement flows from discovery to completion, how trust and payment are handled, and where the Type's boundaries lie against neighboring marketplace, classifieds, and care-related Types.

## Initial Boundary

Directory location: §29 Home, Family, Personal & Local Services (siblings: Childcare Management System, Daycare / Preschool Management, Home Services Marketplace, Local Service Marketplace, Household Staff Management, Family Care Coordination, Pet Sitting Platform, Dog Walking Platform).

Working hypothesis: a consumer-facing, two-sided platform connecting families/parents seeking occasional in-home childcare with individual caregivers. Expected core: caregiver profiles + search/discovery + messaging + trust layer; expected modern additions: bookings and in-platform payments.

Potential confusions identified up front:

- Service Marketplace / Home Services Marketplace / Local Service Marketplace (generic service brokering)
- Classifieds Platform (caregiver "wanted" ads without structured profiles)
- Childcare Management System / Daycare-Preschool Management (operator-side, not two-sided)
- Pet Sitting Platform / Dog Walking Platform (same skeleton, different care domain)
- Tutoring Platform (human brokering, but pedagogy delivery)
- Dating Application (profile + browse + contact mechanics, different purpose)
- Job Board (one matching direction only)

## Research Questions

1. What are the core objects: caregiver profile, family account, child details, job post, booking, message, review, verification?
2. How does discovery work: search/filters, date/time-based matching, social graph, on-demand?
3. What is the engagement lifecycle: inquiry → contact → booking → sit → payment → review?
4. How is trust constructed: identity verification, background checks, reviews, curation at admission?
5. Who pays the platform and how (subscription, freemium, booking fee, B2B benefit)?
6. What tools exist on the caregiver side (availability calendar, rates, job board, payouts)?
7. What scope extensions occur (nanny, senior care, pet care, household, special needs, agencies)?
8. Where are the boundaries against neighboring Types, and is this leaf a Variant of Service Marketplace?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different geography/segment:

1. **Sittercity** (US) — one of the oldest pure babysitting marketplaces; subscription monetization; explicitly *not* handling payments.
2. **UrbanSitter** (US) — social-graph + search hybrid; in-app payments optional (cash or online); two-way reviews.
3. **Babysits** (NL-based, global, 100+ countries) — community model; mandatory ID verification; platform payments optional by country.
4. **Bubble** (UK) — mobile-first, curated admission (acceptance gate), social-circle trust, in-app payment with insurance.

**Care.com** was originally selected as a fifth representative (largest broad care marketplace) but was dropped: care.com and help.care.com both returned HTTP 403 (bot protection). Per the source-access limitation rule, no claims in this research rely on Care.com observations, and the final document's assertion strength is calibrated to the four observed products.

## Sources

Observed directly (2026-09-06):

- Sittercity — homepage (www.sittercity.com); Help Center (support.sittercity.com): "For Families" category index; "How Sittercity works for families"; "How do I pay my sitter?"
- UrbanSitter — Support Center (support.urbansitter.com): Families category index; "How to find & book in-home care"; "How UrbanSitter works for caregivers" (root www.urbansitter.com returned 403; support subdomain reachable)
- Babysits — homepage (www.babysits.com); "How it works" (/about-us/how-it-works/); Help - Bookings (/help/bookings/)
- Bubble — homepage (www.joinbubble.com); Trust and Safety page (/trust-pillars). Intercom-hosted FAQ (intercom.help/bubble-childcare-app) timed out; Bubble FAQ content was NOT successfully fetched.

Failed / limited sources:

- care.com, help.care.com — HTTP 403 (abandoned after 2 attempts)
- urbansitter.com root — HTTP 403 (support.urbansitter.com used instead)
- Bubble intercom help center — timeout (1 attempt, then abandoned; Bubble observations limited to its own site pages)

## Product Observations

Evidence layer per observation: **A** = directly observed on an official source of that product; **B** = cross-product commonality across the observed sample.

### Product A — Sittercity

Key observations (Layer A unless noted):

- Two-sided onboarding split at entry: "I'm a Parent" vs "I'm a Sitter" (distinct registration paths).
- Core family flow (homepage): *Create a job post to share what you need → Sitters apply to your job with their qualifications → Message your favorites to find your match.*
- Caregiver profile card shows: photo, review count, identity-verification badge, background-check badge (regular and "enhanced" variants), years of experience, distance, skill/certification chips (First Aid/CPR, child development, bilingual), response time, last-login/online status.
- Scope extensions: Babysitter (occasional, last-minute, date night, vacations), Nanny (regular), Pet, Companion/senior care; also Special Needs Care and Child Care listing pages; symmetric "Find Jobs" pages for caregivers.
- Trust & Safety positioning: background checks purchasable by parents ("Buy background checks"), identity verification, fraud prevention, safety screenings; dedicated Trust & Safety Center.
- Help center structure (families): getting started, job posting tips, choosing the right caregiver, messaging caregivers, reviewing a caregiver, background checks ("Run a background check on a caregiver", "How does Sittercity verify sitter identities"), guidelines & expectations (community guidelines, ratings & reviews guidelines, attendance expectations).
- Monetization: Premium/value plans (membership); Bright Horizons corporate benefit (B2B channel). Help article explicitly: "upgrade to Premium to send messages, buy background checks, and set up interviews."
- **Payments are explicitly out of scope**: "Once you hire someone from Sittercity, you are their employer… agree on the terms of payment (rate and form) up front. Forms of payment could include Venmo, Zelle, Paypal, cash, etc. … Sittercity does not get involved in the hiring process or monetary transactions between families and caregivers."
- Positioning: "not an agency that places individuals into specific jobs or employs sitters — an online meeting venue for families to connect with sitters in their area."
- Other: AI job-description writer (OpenAI-branded help article), "Sittercity Adventures" (a named program, purpose not fully observed), nanny shares and learning pods article, tax/Nanny Tax guidance, search filters include availability ("Search sitters by availability").

### Product B — UrbanSitter

Key observations (Layer A):

- Scope: in-home child care, senior care, pet care, and household services (cleaning, errands); search also surfaces agency care, daycare/preschool, tutors/homework helpers.
- Family flow ("How to find & book in-home care"): *Post your need → caregivers express interest → book straight from the post*; or *Search all caregivers, filter by care type, distance, rate, special skills → favorite, view profile (experience, availability, reviews) → message, book, or interview → save search + get notified of new matches*.
- **Social graph discovery**: connect Facebook account, add affiliations and local groups to see caregivers already in your network.
- Booking: one-time or recurring jobs; care type selected at booking; accept/decline of interview or booking requests ("Once accepted, you are committing to the booking").
- Payments: "pay your caregiver cash or use our online payment system to pay via credit card, use any applicable credits, and keep track of your history"; caregiver payouts via Branch (digital bank account + debit card); FSA invoices available.
- Reviews are **two-way**: families review caregivers; caregivers review families ("Can caregivers review parents, employers, or care seekers?"); family profiles show vaccine badges and "feedback from caregivers they've hired."
- Caregiver side: profile with years of experience, rates and services, special skills, languages/education, working location, profile video, recommendations, **availability calendar** ("Families search for caregivers by specific date and time so be sure to keep your availability updated"); Job Board to browse family posts and express interest with personal introduction + screening questions; stats page.
- Caregiver admission gate: "you need an active membership and a completed background check before being approved"; all caregivers background checked ("All caregivers are background checked with reviews, rates, experience and more detailed on their profiles"); parents can purchase upgraded background checks or driving record checks.
- Family accounts are authenticated before they can contact caregivers (two-sided verification).
- Monetization: family membership plans (with corporate care benefit category); credits/codes system.

### Product C — Babysits

Key observations (Layer A):

- Global community positioning ("used by 8+ million families… Babysits B.V.", 100+ country list); roles: parents and babysitters/nannies/childminders; also parents-help-parents and childcare agency listings.
- Flow: *Search (filter by needs, review detailed profiles) → Connect (send messages, screen members, introductory meeting) → Book (book a babysitting appointment, pay or get paid, download receipts).*
- **Mandatory ID verification for all members before messaging**; automated profile checks; monitored messaging; reviews and references from other members; ratings after every booking; **optional** basic background check (sitters can also self-upload documents such as background check or first-aid certification).
- Safety guidance: "Meet in a public place before your first booking."
- Membership: free basic tier (sitters message free; families reply free), Premium for unlimited messaging.
- **Bookings feature (where available)**: request to book (day/time/duration) → babysitter accepts → parent pays to confirm → appointment → payout within a few working days; payments via Stripe; sitters receive 100% of earnings; parents pay a service fee (3%, or 15% for non-Premium members — exact numbers product-specific); payment held ≥24h after booking end; cancellation allowed before start or up to 60 minutes after start; no-show leads to automatic negative review if the parent doesn't review; booking feature not visible in all countries; users under 18 can connect but cannot use the booking/payment system.
- Employment stance: "We're not an agency, we're a community… You're responsible for local labor regulations, taxes, and insurance."
- First-class navigation: Search / Bookings / Messages / Favorites.

### Product D — Bubble (UK)

Key observations (Layer A; FAQ help center NOT fetched — details below limited to homepage and trust page):

- Mobile-app-first babysitting/nanny marketplace; finding types: babysitter, night nanny, after-school nanny, full-time nanny, emergency childcare.
- **Curated admission**: "We only accept 1 in 4 sitters"; "multi-step verification process for every sitter who signs up"; DBS status (UK disclosure check) shown on profiles.
- **Social-circle trust as founding principle**: "connect with friends, school and nursery to see which babysitters and nannies the people you know already trust"; "see friends in common."
- Parent control framing: "Choose when, where and who will care for your children. Meet each other first if you like."
- **Payment always in-app**: "Pay securely in the app. Every sit is fully-insured"; buyer protection; human support 9am–9pm 7 days a week.
- Reviews: "honest, verified parent reviews" on sitter profiles.
- B2B: Bubble for Work (back-up childcare, eldercare as employee benefit); Bubble+ subscription tier exists (details unobserved).

## Cross-product Comparison

| Dimension | Sittercity | UrbanSitter | Babysits | Bubble |
|---|---|---|---|---|
| Two-sided roles | Parent / Sitter (A) | Families+care seekers / Caregivers (A) | Parents / Babysitters (A) | Parents / Sitters & nannies (A) |
| Caregiver profiles as search object | Yes: photo, badges, experience, distance, response time (A) | Yes: experience, rates, skills, languages, video, availability calendar (A) | Yes: profiles, references, uploaded documents (A) | Yes: reviews, DBS status (A) |
| Family-driven discovery & selection | Browse/search + job posts (A) | Search filters + date/time + job posts + saved searches (A) | Search + filters + jobs board (A) | Network-centric browse + booking (A) |
| Job posts by families | Core flow (A) | Core flow + caregiver Job Board (A) | Core direction (sitters search jobs) (A) | Not central (A) |
| Platform-mediated contact | Messaging (Premium to send) (A) | Messaging + interview requests (A) | Messaging (ID verification required first) (A) | In-app messaging (A) |
| Reviews / reputation | Parent reviews, guidelines (A) | Two-way reviews + family feedback (A) | Reviews + references + ratings per booking (A) | Verified parent reviews (A) |
| Verification | IDV badges; parents buy background checks (A) | Background check required for caregiver approval; parents buy upgraded checks (A) | Mandatory ID check; optional background check (A) | Curated admission gate; DBS status (A) |
| Booking engine | Not observed (interviews mentioned; no booking feature observed in help center) | Yes: one-time + recurring, accept = commitment (A) | Yes: request → accept → pay → payout lifecycle (A) | Yes: in-app booking ("when, where, who") (A) |
| Payments | **Off-platform only** (Venmo/Zelle/PayPal/cash; platform not involved) (A) | Cash or in-app (card/credits, Branch payouts) (A) | In-app in selected countries; optional; Stripe (A) | In-app only + insurance (A) |
| Monetization | Family membership; corporate benefit (A) | Family membership plans; credits (A) | Freemium + Premium; booking service fee (A) | Per-sit in-app; Bubble+; B2B (A) |
| B2B channel | Bright Horizons benefit (A) | Corporate care benefit category (A) | Babysits for Work (A) | Bubble for Work (A) |
| Scope extensions | Nanny, special needs, senior companion, pet (A) | Senior, pet, household, agency, daycare, tutors (A) | Nanny, childminder, special needs, agencies (A) | Night/after-school/full-time nanny, emergency childcare (A) |
| Agency disclaimer | Explicit: "online meeting venue… not an agency" (A) | Tax responsibility articles imply non-employer (A) | Explicit: "We're not an agency, we're a community" (A) | Not observed in fetched pages |
| Geography | US | US | Global (100+ countries) (A) | UK |

Stable commonalities (Layer B, cross-product):

- Two differentiated participant roles with separate registration (families vs caregivers).
- The caregiver profile is the central, persistent, searchable object.
- Families hold discovery and selection agency (every product frames parent choice as central).
- Platform-mediated first contact between a specific family and a specific caregiver.
- Purpose is arranging real childcare engagements (occasional/ad-hoc to regular).
- Reputation and verification signals attach to profiles (form varies).
- A "not an agency / parents remain the employer" posture (explicit in 3 of 4).
- A B2B/employee-benefit channel exists in all 4.
- Scope drift into adjacent care domains (senior, pet, household) is common.

Key divergences: payment posture (none → optional → hybrid → in-app-only), admission posture (open → gated), discovery mechanism (pure search → social graph), job-post centrality, booking engine presence.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Minimal structure without which the product stops being a Babysitting Marketplace:

1. **Two-sided participation** — differentiated family (care-seeking) and caregiver (care-providing) roles, each with its own account/registration.
2. **Caregiver profiles** — persistent, structured, self-described identities of individual caregivers carrying childcare-relevant attributes (experience, availability, qualifications…).
3. **Family-driven discovery and selection** — families search/browse/filter among candidate caregivers and choose whom to contact.
4. **Platform-mediated first contact** — the family initiates direct contact with a specific caregiver through the platform (message/inquiry/application).
5. **Childcare engagement intent** — the platform's purpose is arranging actual childcare engagements (the "sitting job"), not content, discussion, or employment in the abstract.

Historical check (§24 style): an older, directory-era, or regional babysitting site with profiles + search + messaging but no payments, no booking engine, no background checks, no mobile app still satisfies all five — this matches the *currently observed* Sittercity, which still processes no payments at all. Conversely, a classifieds board of transient "seeking sitter" ads without caregiver profiles/roles fails #1–2 and is a different Type. L0 stands.

### L1 — Common Mature Structure (cross-product, not definitional)

- Reputation layer: reviews/ratings from past families (two-way reviews in some products), references.
- Verification layer: identity verification, background checks (required for caregivers in some products, purchasable by parents in others, optional in others), displayed badges/certifications.
- Job posts by families + applications/expressions of interest (the reverse matching direction).
- In-platform messaging as the connective tissue; screening questions; interview scheduling (phone/in-person/meet-in-public guidance).
- Booking/scheduling: one-time and recurring engagements, request/accept lifecycle, caregiver availability calendar.
- In-platform payments where present: card on file, payout to caregiver, receipts, protection/purchase-fee mechanics.
- Search affordances: location-based search, filters (rate, distance, skills, availability), favorites, saved searches with match alerts.
- Caregiver-side workspace: profile editor, job board, booking management, earnings/receipts.
- B2B employee-benefit channel.

### L2 — Variant / Optional Structure

- Payment posture: off-platform only (Sittercity) / optional by country (Babysits) / cash-or-online hybrid (UrbanSitter) / in-app-only with insurance (Bubble).
- Who pays: family membership, freemium + booking fee, per-sit in-app pricing, employer-funded benefit.
- Admission posture: open registration vs gated/curation (Bubble's acceptance gate; UrbanSitter's membership+background-check approval).
- Discovery mechanism: pure search vs social-graph/network-centric (UrbanSitter, Bubble).
- Job-post centrality: central in Sittercity/UrbanSitter/Babysits; not central in Bubble.
- Scope envelope: nanny-only to multi-domain care portals (senior, pet, household, special needs, agency/daycare/tutor listings).
- Geography: single-country vs global; booking/payment feature availability varies by country within one product.
- Surface: web-first vs mobile-app-first.

### L3 — Vendor-specific (research notes only)

- Sittercity: OpenAI job-description writer; "Sittercity Adventures" program; Bright Horizons benefit integration; "96% of US neighborhoods" claim.
- UrbanSitter: Branch payout rail; vaccine badges on family profiles; agency care / daycare / tutor search verticals; caregiver stats page.
- Babysits: auto-negative review on unreviewed no-show; 3%/15% member-protection fee; 60-minute post-start cancellation window; ≥24h payment hold; under-18 booking exclusion; Supersitter program; Stripe as processor.
- Bubble: 1-in-4 acceptance rate; DBS status display; fully-insured sits; Bubble+ tier; 9am–9pm human support window.

## Rejected Findings

- "A babysitting marketplace is defined by in-app payments and bookings" — **rejected**: Sittercity (observed) is a canonical member with neither; Babysits ships payments only in selected countries. Payments/bookings are L1/L2.
- "Background checks are definitional" — **rejected**: Babysits makes them optional; historical/community products rely on references. Verification is L1 with region- and product-dependent intensity.
- "Babysitting Marketplace is a Variant of Service Marketplace" — **rejected** after comparison: the distinctive structure (individual caregivers as profiled persons, child-safety trust layer, in-home family context, occasional-care cadence, C2C roles) recurs across all sampled products and is the reason a separate category exists in the market. Flagged for directory review as a boundary note, not a rewrite.
- "Child profiles/household children are core objects" — **downgraded**: none of the four observed product surfaces documents child profiles as a first-class object in the fetched pages; family needs are described in profiles/job posts. Treat child-specific profile structures as unverified (likely present in some products' booking details; not asserted).
- "On-demand/last-minute instant matching defines the Type" — **rejected**: only Bubble's marketing emphasizes instant last-minute requests; others center deliberate search/vetting.

## Boundary Findings

1. **vs Classifieds Platform (§05.03)**: classifieds center transient wanted/offered ads; this Type centers persistent caregiver profiles and two-sided accounts. Test: remove caregiver profiles and role-differentiated accounts, keep ads → classifieds.
2. **vs Service Marketplace / Home Services Marketplace / Local Service Marketplace (§05.02, §29)**: those broker generic services, typically business providers, with generic job objects; this Type's invariant object is the individual caregiver profile with childcare-specific trust semantics and in-home family context. Test: remove childcare semantics and caregiver-profile structure, keep generic service matching → service marketplace. Structural skeleton (two-sided, profiles, discovery, contact, transaction) is shared; domain invariants justify the distinct leaf. Worth a joint review when Service Marketplace is processed.
3. **vs Childcare Management System / Daycare-Preschool Management (§29 siblings)**: operator-side administration of a care business (rooms, ratios, enrollment, billing) vs consumer-side two-sided matching. Completely different primary users. A marketplace does not manage anyone's care business; a childcare management system does not broker strangers.
4. **vs Pet Sitting Platform / Dog Walking Platform (§29 siblings)**: same marketplace skeleton, different care domain (animals, no child-safety trust layer). Sibling Types, not aliases.
5. **vs Tutoring Platform (§23)**: both broker individuals for in-home/scheduled human services; tutoring centers learning delivery, this Type centers custodial care. Domain object differs.
6. **vs Job Board (§09)**: job posts appear here but are one matching direction; the caregiver profile (supply side) is the center, and engagements are often informal service arrangements rather than employment listings.
7. **vs Dating Application (§01.07)**: shared profile/browse/contact mechanics; different selection purpose (childcare engagement vs romantic matching) and different trust semantics.
8. **vs Nanny agency systems**: all sampled products explicitly disclaim agency/employer status; a product that employs or places caregivers is operationally an agency system — outside this Type.
9. **vs Family Care Coordination (§29)**: internal family logistics around existing carers, not two-sided stranger matching.

"去掉什么就变成另一个 Type" summary: remove caregiver profiles + two-sided roles → classifieds; remove childcare domain → generic service marketplace; remove two-sided matching → childcare management (operator side); change care domain to pets → pet sitting platform.

## Uncertainties

- **Care.com unobserved** (HTTP 403 both domains): the largest broad-care portal could not confirm or challenge any pattern; all cross-product claims rest on 4 products.
- **Bubble details thin**: FAQ/help center unreachable (timeout); booking flow specifics (fees, cancellation, cancellation windows) unobserved; Bubble claims taken from its own homepage/trust page only.
- **Sittercity booking feature**: no booking engine observed in the help-center structure; asserted as "not observed", not as "does not exist".
- **Two-way reviews** (caregivers reviewing families): confirmed on UrbanSitter and implied on Babysits; Sittercity/Bubble unclear → treated as common-but-not-universal.
- **Child profiles**: likely exist inside booking/job details but were not documented in fetched pages; not asserted anywhere.
- **Historical samples** (pre-payment-era directory products, non-US products like Yoopies/Kombo, community sitter co-ops) not directly fetched; L0 was stress-tested against the *current* Sittercity (a de-facto historical-shape product) instead of memory-based claims.

## Final Synthesis

A Babysitting Marketplace is a two-sided, consumer-facing platform on which families seeking childcare and individual caregivers offering it meet through structured caregiver profiles. Families discover, evaluate, and select candidates; the platform mediates first contact and accumulates trust signals (reviews, verifications) on profiles; modern products add job posts, booking lifecycles, and in-platform payments — but the payment rails and booking engines are implementation layers, not the definition. The platform consistently positions itself as a venue, not an employer or agency: hiring, employment, taxes, and (in some products) payment remain with the family. The Type is distinguished from classifieds by persistent profiled caregiver identities, from generic service marketplaces by childcare-specific trust and in-home care context, and from childcare management systems by being two-sided and consumer-facing rather than operator-side.
