# Research Notes — Local Service Marketplace

## Research Goal

Understand what a Local Service Marketplace (DIRECTORY §29, "Home, Family, Personal & Local Services") actually is as an Application Type: what the venue centers on, how supply and demand are structured, how locality is expressed, how the engagement and its money flow work across the market's different transaction philosophies, and where the boundaries lie — especially against the generic Service Marketplace umbrella (§05.02), the domain-structured marketplace siblings (Home Services, Babysitting, Beauty), classifieds, lead generation, and directory/review surfaces.

## Initial Boundary

Hypothesis before research: an operator-run venue where consumers find and engage local service providers across many service categories, with geography (the customer's locality) as the primary organizing axis. Expected to be a sibling of the Service Marketplace umbrella per that pass's recorded structure.

Prior passes already referencing this leaf — three flags to discharge from this side:

- **home-services-marketplace (§29, processed 2026-09-08)** — flag ②: "vs Local Service Marketplace (§29, unprocessed) — sharpest live seam: home-shaped venue … vs any-local-service venue with generic job objects; Bark documented as the generalist specimen … JOINT REVIEW RECOMMENDED when local-service-marketplace is processed." Flag ③: lead-sale pole (Bark, Networx) kept out of the home Type on the settlement+engagement test.
- **beauty-service-marketplace (§29, processed)** — "joint review recommended when Local Service Marketplace and Service Marketplace are processed" (Service Marketplace was processed 2026-09-07; the local half remains).
- **service-marketplace (§05.02, processed 2026-09-07)** — recorded local-service-marketplace among its "domain-structured marketplace siblings (beauty, babysitting, home-services, local-service §29 …)".

Nearest neighbors:

- Service Marketplace (§05.02 umbrella, processed) — locality-agnostic; its sample includes remote/digital services; L0 requires platform-mediated settlement
- Home Services Marketplace (§29, processed) — domain-structured sibling (property-as-job-site + home trades)
- Babysitting Marketplace / Beauty Service Marketplace (§29, processed) — domain-structured siblings
- Classifieds Platform (§05.03, processed) — self-published ads, off-platform contact, no matching venue
- Lead Generation Platform (§06, processed) — sells contact/quote opportunities; no consumer-facing matching market
- Directory Application / Listings Platform (§02.11) — browse-only records, no demand intake
- Review Platform (§02.10) — reputation first, transaction absent
- Appointment Scheduling Application (§03.09) / Appointment-based Service Business Management (§29, processed) — one operator's bookable offerings vs a market
- Operator-side service-business software (cleaning/handyman/HVAC/appliance/garage-door passes, processed) — demand-side market vs one business's execution system; repeatedly recorded seam "a marketplace lead becomes a job here"
- Homeowner/planner-side §29 siblings (Home Improvement Planner, Home Maintenance Application, processed) — the hiring leg vs the planning record

## Research Questions

1. What is the unit of supply — provider profile, bookable offering, or lead? How is provider presence authored?
2. How is locality expressed and enforced — service areas, city/category pages, address scoping?
3. What matching flows exist (request→instant match→quotes, post→offers, browse-and-book) and where does the matching decision happen?
4. What is the transaction/engagement object in each product, and does the platform settle payment for the service?
5. How is the venue monetized — client-side fees/commission, provider-side per-response charges, or both — and how does monetization relate to settlement depth?
6. How broad is the service taxonomy, and is the machinery domain-generic or domain-structured?
7. What trust machinery exists (reviews, verification, gating of contact details), and what is generic vs domain-specific?
8. What rules govern participation (admission, leakage, cancellation, disputes)?
9. Where are the boundaries: vs umbrella, vs domain siblings, vs classifieds/lead-gen/directory, vs operator-side software?

## Representative Products

Selected for market representation + different transaction philosophies + different geographies + doc accessibility:

| Product | Shape | Transaction philosophy | Geography | Doc access |
|---|---|---|---|---|
| Bark | generalist local services (many domains) | request→instant match→pro contacts; pro pays per lead (credits), no commission | UK-origin, 10+ locales (observed) | Help Centre reachable this pass (Tier-1) |
| TaskRabbit | local tasks across several task domains (home-weighted: cleaning, moving, assembly, mounting, repairs; also personal assistant, shopping & delivery) | browse-and-book at provider-set hourly rates; platform settlement | city-scoped, global | Help Center reachable this pass; detailed Tier-1 evidence imported from Service Marketplace pass (2026-09-07) |
| Airtasker | generalist local odd jobs (+ remote extension) | post-task→offers→assign; escrow at assignment | AU-origin, AU/UK/US/IE | Support Centre reachable this pass; detailed Tier-1 evidence imported from Service Marketplace pass (2026-09-07) |
| Thumbtack | generalist local services, quote-request model (market position) | — | US | NOT reachable this pass (empty response; also empty in umbrella and home-services passes) — limitation recorded, no claims made |
| Yelp (boundary anchor, not a representative) | directory/review-first with local-services surfaces | — | global | yelp-support.com transport error ×2 this pass — abandoned per network rules; no claims made |

## Sources

Research date: 2026-09-08. All fetches this pass dated 2026-09-08 unless noted.

- Bark Help Centre (Zendesk): root https://help.bark.com/hc/en-gb; article "What is Bark and how does it work?" (/hc/en-gb/articles/13342669635484); article "What is a credit and how much does it cost?" (/hc/en-gb/articles/13346288068892); category "New to Bark" (/hc/en-gb/categories/13168462136732) — all fetched 2026-09-08
- Bark homepage/category structure: imported from research/home-services-marketplace.md (2026-09-08, official bark.com pages fetched there: category groups incl. House & Home as one group among many; contact-details gating article)
- TaskRabbit Support Center root https://support.taskrabbit.com/hc/en-us (fetched 2026-09-08: Client/Tasker/Registration/Account/Policy Center categories; nav "Services by City", "All Services", "Become a Tasker"); detailed article evidence imported from research/service-marketplace.md (2026-09-07, Tier-1)
- Airtasker Support Centre root https://support.airtasker.com/hc/en-au (fetched 2026-09-08: "I am a Customer" / "I am a Tasker" / "Airtasker Guidelines"); detailed article evidence imported from research/service-marketplace.md (2026-09-07, Tier-1)
- Unreachable, abandoned per network rules: http://www.thumbtack.com (empty ×1 this pass; empty ×3 umbrella pass; empty home-services pass); www.yelp-support.com (transport error ×2); help.angi.com / www.angi.com (Okta-walled / 403 in home-services pass — not re-attempted)

**Source-access limitation:** the US quote-request generalist pole (Thumbtack-class, Angi-class) has no directly observed operational evidence in this or any prior pass. Its existence is recorded as a market position only. No precise mechanics, fees, or flows are attributed to Thumbtack or Angi anywhere in this research or the final document. Yelp's role is limited to a structural boundary mention (directory-first posture) without product claims.

## Product Observations

### Bark (evidence layer A — directly observed this pass, Tier-1 help centre; homepage/category evidence imported from home-services pass same date)

- Positioning (own words): "Every day, people come to Bark looking for professionals across **hundreds of service categories**. Bark connects them with the right people."
- Domain breadth: generalist — category groups span Business, Events & Entertainers, Health & Wellness, House & Home (architects, CCTV, fencing, gardening, gutter cleaning, house cleaning…), Lessons, More (imported from home-services pass's bark.com fetches). House & Home is one group among many; the venue is not home-centered.
- Demand flow (help article, verbatim structure): customer "answers specific questions about what they need" → "We instantly match their request to professionals" → pro "review[s] the lead and decide[s] whether to contact them" → pro "pay[s] only for the leads you choose — no commission, no hidden fees" → "You get in touch, win the job, done."
- Monetization: provider-side, per-lead credits. "Credits are the currency you use on Bark to connect with potential customers. Every lead has a credit cost shown clearly before you commit." Lead pricing depends on service type ("some industries have higher demand") and job size/scope. Credit prices vary by country; packs, auto top-up, expiry windows exist (vendor details). Customer side is free to post (implied by "You only spend credits" addressed to professionals; the help centre's billing sections are professional-side).
- Engagement/settlement: the documented flow ends at "get in touch, win the job, done" — hiring and payment happen outside the platform. No engagement-of-record lifecycle and no payment-for-service machinery is documented in the reachable help centre (which is overwhelmingly professional-side: Credits & Billing, invoices, subscriptions).
- Contact gating: "Professionals will only be given your details once they've sent you a quote" (imported from home-services pass's official-page fetch).
- Admission: "Your Bark account is free to set up" — open provider signup; no approval step documented.
- Geography: 10 locale variants (UK, DE, AU, CA, IE, IN, NZ, SG, US, ZA) observed in the help-centre language switcher; per-country credit pricing. Locality scoping of leads is inherent in the request→local-pros match but no precision asserted beyond that.

### TaskRabbit (evidence layer A — reachability verified this pass; detailed observations imported from Service Marketplace pass, 2026-09-07, Tier-1)

- Local task marketplace: categories span several task domains — Cleaning, Moving, Furniture Assembly, Mounting, Home Repairs, Personal Assistant, Shopping & Delivery, Help Moving (home-weighted but not home-exhaustive; machinery is generic).
- Demand flow: pick category → task description + task location/address + date/time (same-day possible) → **see a list of Taskers filtered by availability, work-area map, category, and price** → select → "Confirm and chat."
- Supply: Taskers set their own hourly rates, schedules, and work areas; registration includes an approval step and a registration fee.
- Settlement: cashless platform — card required at booking; charged within 24h after the Tasker's post-task invoice (hours + agreed expenses); cash and off-platform payment apps prohibited; protection covers only platform-booked-and-paid tasks.
- Fees: client-side service fee + separate trust & support fee; tips 100% to Tasker; cancellation fee inside 24h of scheduled time.
- Contact gating: Taskers never receive the client's phone/email; task address hidden until the Tasker accepts; communication via in-app chat/call.
- Locality surfaces: "Services by City" site nav (observed this pass); provider work-area maps.
- Reputation: clients evaluate profiles, reviews, and hourly rates before booking.

### Airtasker (evidence layer A — reachability verified this pass; detailed observations imported from Service Marketplace pass, 2026-09-07, Tier-1)

- Generalist odd-jobs venue, local tasks with a remote-task extension.
- Demand flow: post a task (scope, photos, time, **budget** — "Tasks that simply ask for a quote are not supported") → posted to the task feed → Taskers make offers (price "based on time, skill, and effort") → customer reviews and **accepts an offer (assign)** → private chat to arrange details. Must-have requirements gate offering.
- Settlement: card required before assignment; payment debited at assignment and **held in escrow** until completion; customer releases payment; labor cost must flow through the platform; genuine expenses (materials, dump fees) separable with receipts.
- Trust: badges/verifications, building-trust and safety sections, insurance, task conflicts/dispute/refunds sections; community guidelines govern conduct; unassigned tasks expire.
- Current-era extension: ChatGPT integration for posting/comparing/hiring with payments still handled through the platform (vendor detail).

### Thumbtack (no evidence — limitation recorded)

Not observed in this pass or any prior pass (empty responses across three passes). Retained as a market-representative example of the generalist local quote-request pole. No claim in this research or the final document depends on Thumbtack mechanics.

### Yelp (no evidence — boundary anchor only)

yelp-support.com unreachable this pass (transport error ×2, abandoned). Yelp is retained only as a structural boundary reference: a directory/review-first product family with local-services surfaces; the load-bearing distinction (demand intake + matching venue vs browse-only directory) is argued structurally, not from Yelp internals.

## Cross-product Comparison

| Dimension | Bark | TaskRabbit | Airtasker | Thumbtack (unverified) |
|---|---|---|---|---|
| Domain breadth | generalist (hundreds of categories; many groups) | multi-domain tasks, home-weighted | generalist odd jobs (+ remote) | generalist (market position) |
| Unit of supply | provider profile + lead responses (credits) | Tasker profile + hourly rate + work area | Tasker profile + offers | — |
| Demand intake | structured questions about the need | category + task description + address + time | task post (scope, photos, time, budget) | — |
| Matching | platform instant-match to fitting pros | provider list filtered by availability/area/category/price | posted task feed → offers | — |
| Matching decision on-platform | yes (request matched inside venue; pro opts in via lead) | yes (client selects Tasker) | yes (client assigns an offer) | — |
| Provider response machinery | review lead → contact (paying credits) | accept booking | make offer → get assigned | — |
| Engagement of record | no (ends at contact; "win the job, done") | yes (Task with lifecycle to completion) | yes (Task, assigned → escrow → completion) | — |
| Platform settlement of the service | no (off-platform hiring) | yes (charge after provider invoice) | yes (escrow at assignment) | — |
| Who pays the platform | provider per lead (credits; no commission) | client (service fee + trust fee) | both sides in machinery; commission/fees in platform pay | — |
| Contact gating | customer details released only after a quote | phone/email never shared; address hidden until accept | private chat after assignment | — |
| Admission | free open signup | approval + registration fee | registration + guidelines | — |
| Locality expression | request matched to local pros; per-country pricing; 10 locales | city pages, work-area maps, task address | task location; remote as extension | — |
| Reputation | not directly observed this pass | reviews on profiles evaluated pre-booking | badges/verifications; guidelines | — |
| Leakage posture | hiring off-platform is the documented flow | off-platform payment prohibited | labor cost must flow through platform | — |

Evidence-layer summary:

- **B-layer (cross-product, 3/3 observed products):** an operator-run venue over a population of independent local service providers; provider-authored presence (profile: categories, service area, rates/credentials) as the supply the demand side evaluates; consumer demand intake (structured questions, task description, or booking pick) with the matching decision made inside the venue (instant match, filtered provider list, or posted request answered by offers); provider response through venue machinery (contact a lead, accept a booking, make an offer); locality anchoring (service areas, city surfaces, locally scoped requests); a distinct provider-side console.
- **B-layer where the sample SPLITS (the defining tension of this Type):** transaction depth. TaskRabbit and Airtasker record the engagement and settle payment on-platform with leakage prohibitions. Bark's documented flow ends at a brokered connection — the platform monetizes per response (credits, "no commission") and hiring/settlement happen off-platform, explicitly.
- **A-layer (product-specific, kept out of the canonical core):** credit pricing/expiry/auto top-up, per-country credit rates, credit-pack subscriptions, "no commission" positioning, TaskRabbit service fee + trust & support fee split, charge-after-invoice timing, Taskprotect, Airtasker escrow-at-assignment, must-have requirement gates, task expiry, ChatGPT integration, "hundreds of service categories" claim, locale lists.

## Canonical Model

### Level 0 — Defining Invariant

Four structures; remove any one and the product stops being a local service marketplace:

1. **Locality-anchored two-sided market over independent local providers** — an operator-run venue whose supply is a population of independent local service providers (individuals and small businesses), with the market organized by geography: demand is scoped to the customer's area, providers declare where they work, and the services are performed in the physical world near the customer. (Remove the geographic anchoring → the locality-agnostic service-marketplace umbrella; remove provider independence → one business's booking site; remove the provider population → a single-operator tool.)
2. **Provider-authored market presence** — providers author who they are, which service categories they cover, their service area, and (varyingly) pricing and credentials, as records inside the venue that the demand side evaluates. (Remove → an operator-configured catalog or a lead-resale list, not a market.)
3. **Demand intake + on-platform matching** — the consumer submits a service need into the venue (structured questions, a task description, or a category pick), and the venue performs the matching against its own provider population — instantly matching a request, listing bookable providers, or broadcasting the request for offers. Providers respond through the venue's machinery. The matching decision is made inside the venue, not delegated to an external channel. (Remove → classifieds, lead resale, or a passive directory.)
4. **The request of record** — the submitted need persists as the unit around which matching, responses, and the consumer's comparison happen, and the venue retains it (with the responses it drew) as the market's transactional trace. (Remove → ephemeral matching with no venue memory; nothing for either side to act on.)

The Type's identity is completed by a negative binding: **the machinery is domain-generic** — the venue spans many service domains (home, personal, events, lessons, wellness, business services, pets) and carries no domain-specific object structure (no property-attribute pricing, no caregiver-profile child-safety construction, no duration/price service menus). Strip the domain-generic breadth and add a domain's machinery → the domain-structured sibling Types (Home Services, Babysitting, Beauty).

**Transaction depth is deliberately NOT in L0.** The market realizes the Type in two poles: venues that continue from the matched connection into a recorded engagement settled on-platform (with leakage prohibitions), and venues whose product is the brokered connection itself — monetized per response, with hiring and payment left to the parties. Both poles carry all four L0 structures. This is the honest reading of the generalist segment: the connection-brokered model is not a degenerate case but the documented center of a leading generalist venue (Bark), and the settlement-bearing model is the documented center of the task-booking venues (TaskRabbit, Airtasker). Requiring settlement would define the Type by its minority pole; requiring connection-only would exclude the task venues.

Concept → implementation separation:

```text
Concept:  locality-anchored market
Impl:     city service pages + work-area maps (TaskRabbit) ·
          locally scoped request matching, per-country pricing (Bark) ·
          task location + remote extension (Airtasker)

Concept:  provider-authored presence
Impl:     profile + categories + rates + service area (TaskRabbit/Airtasker) ·
          free professional profile + category coverage (Bark)

Concept:  demand intake + on-platform matching
Impl:     browse-and-book from a filtered provider list (TaskRabbit) ·
          post → offers → assign (Airtasker) ·
          structured questions → instant match → pro-initiated contact (Bark)

Concept:  request of record
Impl:     task (TaskRabbit) · task post (Airtasker) ·
          customer request + its matched leads (Bark)

Concept:  transaction depth (variant axis, NOT invariant)
Impl:     engagement lifecycle + platform settlement + leakage rules
          (TaskRabbit, Airtasker) ·
          connection-only: per-response monetization, off-platform hiring
          (Bark) · hybrids plausibly exist in the market (unverified)
```

### Level 1 — Common Mature Structure

Present across the observed sample or strongly common; makes the market work but does not define the Type:

- service taxonomy (categories/subcategories) structuring both sides' search and browsing
- provider reputation surfaces — reviews/ratings and verification signals (directly observed in the settlement pole; Bark's reputation machinery not directly observed this pass, held at "common" strength)
- in-venue messaging with contact-detail gating (details released at defined points — after quote, after acceptance, never)
- pricing machinery appropriate to the pole: provider-set rates, budgets with offers, quote-per-job
- provider-side console: incoming leads/bookings/offers, response management, spend or earnings views
- provider admission machinery (open signup ↔ approval steps; verification where domain risk warrants)
- locality surfaces: city/category pages, service-area declarations, radius/address scoping
- cancellation/dispute machinery in the settlement pole; review loop gated to completed engagements

### Level 2 — Variant / Optional Structure

- **Transaction depth (the main axis):** connection-brokered (per-response monetization, off-platform hiring) ↔ engagement-of-record + platform settlement (charge/escrow/payout, leakage prohibition) ↔ hybrid postures (market position, unverified)
- Monetization side: provider-side per-lead credits ↔ client-side fees/commission ↔ both
- Matching pole: request→instant-match→quotes ↔ post→offers↔assign ↔ browse-and-book
- Pricing regime: provider-set hourly ↔ budget + negotiated offers ↔ quote per job
- Domain weighting: pure generalist ↔ generalist with heavier home-task weight
- Supply entity: individuals ↔ small businesses
- Geographic posture: city-scoped ↔ multi-country; remote tasks as an extension in some venues
- Era-current: AI matching/assistance surfaces; agent integrations with payments kept on-platform

### Level 3 — Vendor-specific Structure

Remains in Research Notes: Bark's credit economics (per-credit price, expiry windows, auto top-up, pack subscriptions, per-country rates), "no commission" positioning, contact-release-after-quote rule; TaskRabbit's fee line items, 24h charge window, Taskprotect, registration fee, Elite program; Airtasker's escrow-at-assignment, must-have gates, task expiry, ChatGPT plugin; Thumbtack's and Angi's mechanisms (entirely unverified).

## Historical / Market-Sample Check

- **Pre-digital analog:** the local services brokerage/agency — a local office holding a roster of registered tradespeople and cleaners (provider-authored presence via registration: trade, coverage area, references), taking household requests (demand intake), matching the request to suitable names (on-"platform" matching decision), and recording the request and the introductions made (request of record). Monetization split the same way the modern poles do: the agency either collected and paid the worker (settlement analog) or charged the worker a placement/introduction fee (lead-fee analog). The core satisfies all four L0 structures. The yellow-pages directory and newspaper classifieds fail L0 property 3/4 (no demand intake, no matching venue) and are correctly ancestors, not instances.
- **Regional spread:** Bark operates 10 locales (observed); Airtasker is AU-origin across AU/UK/US/IE; TaskRabbit is global and city-scoped. No region-specific machinery is in the core.
- **Era-independence:** nothing in L0 requires mobile apps, GPS work areas, credits, escrow, background checks, or reviews. Early-web local "request a quote" venues satisfy the core. Historical check passes.

## Vendor-specific Findings

- Bark: per-lead credit model with visible per-lead cost before committing; lead cost varies by service type and job size/scope; per-country credit pricing; contact details released only after a quote; free professional signup; documented flow ends at off-platform "get in touch, win the job, done"; "no commission" self-positioning; generalist claim of "hundreds of service categories."
- TaskRabbit: browse-and-book only; provider-set hourly rates; charge within 24h of the provider's post-task invoice; client service fee + separate trust & support fee; address hidden until acceptance; registration approval + fee.
- Airtasker: budget required at posting (quote-only tasks unsupported); escrow debited at assignment, released at completion; must-have requirements gate offering; unassigned tasks expire; ChatGPT integration with payments kept on-platform.

## Rejected Findings

- **Rejected: "platform-mediated settlement is a defining property of this Type."** The generalist local segment splits on transaction depth, and the connection-brokered pole is the documented center of a leading generalist venue (Bark: "You pay only for the leads you choose — no commission… You get in touch, win the job, done"). Settlement characterizes the task-booking pole (TaskRabbit, Airtasker), not the Type. Held as the Type's variant axis, with the divergence from the Service Marketplace umbrella's settlement invariant recorded in Boundary Findings.
- **Rejected: "Local Service Marketplace is merely a regional variant of the Service Marketplace umbrella."** The umbrella's L0 is locality-agnostic and includes remote/digital supply (freelance/digital-services variant); the local leaf's market is geographic by construction, its taxonomy domain-generic. The settlement-bearing pole overlaps the umbrella; the connection-brokered pole does not satisfy the umbrella's L0 at all. Overlap is documented; identity is separate.
- **Rejected: "breadth alone defines the leaf."** Breadth (many categories) is the negative domain binding and only becomes defining together with the locality anchoring and the generic machinery; a narrow-catalog venue with domain machinery is a domain sibling, not a shallow version of this Type.
- **Rejected: "the consumer always pays the platform."** Bark's monetization is entirely provider-side (credits); TaskRabbit's is client-side. Both realize the same Type.

## Boundary Findings

1. **vs Service Marketplace (§05.02 umbrella, processed)** — sibling with a documented overlap and a documented divergence. Shared skeleton over the settlement-bearing pole (TaskRabbit/Airtasker are instances of both). Divergence: the umbrella's L0 requires platform-mediated settlement and is locality-agnostic (it hosts the freelance/digital-services variant); this leaf's L0 is locality-anchored, domain-generic, and holds transaction depth as a variant — so the connection-brokered generalist venue (Bark) is an instance of this Type and NOT of the umbrella. No taxonomy change proposed; the overlap and the settlement-axis divergence are recorded here for the umbrella's side.
2. **vs Home Services Marketplace (§29, processed) — JOINT REVIEW FLAG DISCHARGED.** That pass's flag ② asked this pass to resolve the seam; its domain-axis pointer is RATIFIED from this side: Bark (generalist, House & Home one group among many, generic machinery) sits on the local-services side of the seam, and the discriminator is domain structuring — home-services centers the customer's property as the job site and organizes supply as home trades; this Type carries any local service domain with generic objects (a request, a task, a quote) and no domain machinery. Its flag ③ (lead-sale pole excluded from home-services on the settlement+engagement test) is respected for the HOME leaf — and refined for THIS leaf: the connection-brokered posture is a variant inside the local generalist Type, because the locality-anchored matching market is the invariant both poles share. Boundary held: remove the home-domain binding from home-services → this Type; add home-domain machinery to this Type → home-services.
3. **vs Beauty Service Marketplace (§29, processed) — JOINT REVIEW FLAG DISCHARGED (local half).** Beauty's domain structuring (provider-defined service menus with duration/price, licensing/vetting norms, beauty categories, portfolio imagery) is exactly what this Type's generic machinery lacks. Bark's generic request/lead/credit machinery across hundreds of categories confirms the seam from this side. Sibling status ratified; no taxonomy change. Consistent with that pass's own note that vendor bundling of both surfaces in one brand does not merge the Types.
4. **vs Babysitting Marketplace (§29, processed)** — same pattern: the individual-caregiver profile with child-safety trust construction is domain machinery; this Type's objects are generic. Consistent with the babysitting pass's recorded test.
5. **vs Classifieds Platform (§05.03, processed)** — classifieds are self-published, time-bound ads with off-platform contact and no demand intake or matching venue. The load-bearing test is L0 property 3: strip demand intake + matching → classifieds. Locality-shared but structure-distinct; the neighborhood-social-network pass's framing of these as "commerce-heavy neighbors" is consistent.
6. **vs Lead Generation Platform (§06, processed)** — the sharpest residual seam, honestly recorded: the connection-brokered pole (Bark) monetizes responses like lead-sale does. Distinction held structurally: the lead-gen Type sells contact/quote opportunities to businesses without a consumer-facing matching market — no venue-hosted provider population the consumer evaluates, no provider-authored market presence, no on-platform matching decision, no request of record the venue retains for both sides. Bark has all four. The seam is real but does not merge the Types; noted for the lead-gen pass's side.
7. **vs Directory Application / Listings Platform (§02.11)** — directories expose browse-only provider records; no demand intake, no matching, no request of record (L0 property 3/4). A "directory with request-a-quote" posture drifts toward this Type as the request machinery matures.
8. **vs Review Platform (§02.10)** — reputation is the primary object there; here reputation is trust machinery around the matching market. Yelp-class products live on the directory/review side until matching/settlement becomes the center (unverified for Yelp itself — limitation recorded).
9. **vs operator-side service-business software (cleaning/handyman/HVAC/appliance/garage-door/electrical passes, processed)** — demand-side multi-provider market vs one business's execution/billing system; RATIFIED from this side: a marketplace lead or booking becomes a job in those systems. ~10 sibling passes record the same seam; this pass confirms it from the demand side.
10. **vs Appointment Scheduling Application (§03.09) / Appointment-based Service Business Management (§29, processed)** — one operator's bookable offerings vs a competitive market over many independent providers; that pass's own note ("consumer-side discovery vs operator-side management") ratified.
11. **vs homeowner/planner-side §29 siblings (Home Improvement Planner, Home Maintenance Application, processed)** — the hiring market vs the homeowner's planning/record; complementary. Consistent with those passes' forward notes.
12. **vs Home Services-led hybrids (Angi-class)** — the US market shows venues that mix lead-sale for projects with booking for standardized services. Recorded as a plausible hybrid posture (market position only; unverified — no claims). Hybrid postures do not merge the Types; center of gravity decides.

## Uncertainties

1. The US quote-request generalist pole (Thumbtack, Angi) has zero directly observed operational evidence across all passes. Whether it settles on-platform, charges leads, or runs hybrids is unknown here. The final document names Thumbtack only as a market example with the limitation stated; no mechanics claims.
2. Bark's customer-side and reputation machinery (reviews on profiles, guarantees) was not directly observed this pass; the reachable help centre is professional-side. No customer-side mechanics asserted beyond the documented request→match→contact flow.
3. Whether connection-brokered venues are converging toward on-platform booking/payments (a hybrid future) could not be verified; the variant axis is written as current observed poles plus a flagged hybrid possibility.
4. The precise relationship between per-lead credit pricing and locality (does locality affect lead price?) was not observed; Bark's documented lead-pricing factors are service type and job size/scope only.
5. Overlap governance with the umbrella: TaskRabbit/Airtasker are instances of both Types. If the taxonomy ever consolidates, the umbrella's "local task marketplace" variant and this leaf are the consolidation candidates — recorded as a taxonomy note, not decided here (per the online-marketplace alias precedent).

## Final Synthesis

A Local Service Marketplace is an operator-run, locality-anchored market where consumers submit service needs and the venue matches those needs against a population of independent local providers spanning many service domains with domain-generic machinery: providers author their presence (categories, service area, rates/credentials), the matching decision happens inside the venue (instant match, filtered provider list, or broadcast request answered by offers), and the submitted request persists as the unit around which responses and comparison happen. The Type's main variant axis is transaction depth: task-booking venues continue into a recorded engagement with platform settlement and leakage rules; connection-brokered venues monetize the matched response itself (per-lead) and leave hiring and payment to the parties. Domain-structured siblings (home, babysitting, beauty) add a domain's machinery to the same skeleton; classifieds, lead resale, and directories lack the demand-intake-plus-matching core; operator-side business software lives on the other side of the lead-becomes-a-job seam.
