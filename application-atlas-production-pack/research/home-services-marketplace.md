# Research Notes — Home Services Marketplace

## Research Goal

Understand what a Home Services Marketplace (DIRECTORY §29) actually is as an Application Type: what the venue centers on, how home-service supply is structured, how homeowners find and book providers, what the engagement and its money flow look like, what trust machinery the "stranger enters your home" problem requires, and where the boundaries lie — especially against the generic Service Marketplace umbrella (§05.02), the unprocessed Local Service Marketplace sibling (§29), lead-generation surfaces, and operator-side trade software.

## Initial Boundary

Hypothesis before research: a two-sided marketplace where homeowners/renters find, book, and pay independent providers for services performed at their home (cleaning, handyman, plumbing, electrical, HVAC, lawn/outdoor, moving, assembly, junk removal, painting, renovations). Expected to be a domain-structured sibling of Service Marketplace (§05.02), per that pass's own taxonomy note ("the generic venue documented as the umbrella Type over the domain-structured marketplace siblings (beauty-service-marketplace, babysitting-marketplace, home-services-marketplace, local-service-marketplace §29 …)").

Nearest neighbors:

- Service Marketplace (§05.02, processed 2026-09-07) — the generic umbrella; this leaf is a domain-structured sibling per the umbrella's recorded structure
- Local Service Marketplace (§29, unprocessed) — sharpest live seam; both local and on-site
- Babysitting Marketplace (§29, processed) — same skeleton, different domain; left a joint-review flag for this pass
- Beauty Service Marketplace (§29, processed) — precedent for how domain-structured marketplace siblings are documented
- Classifieds Platform (§05.03, processed) — listings + off-platform contact
- Lead Generation Platform (§06, processed) — sells contact/quote requests; no on-platform engagement
- Operator-side trade software (cleaning-business-management, handyman-business-management, lawn-care-business-management, etc., processed) — one business's execution system vs the demand-side market
- Homeowner-side §29 siblings (Home Improvement Planner, Home Maintenance Application, Home Management Application — all processed) — the planning/record side; forward notes left for this pass
- Property Maintenance Management (§17) — landlord/owner-side maintenance operations
- Appointment Scheduling Application (§03.09, processed) — one operator's bookable offerings

Prior passes referencing this leaf:

- babysitting-marketplace: "joint review recommended when Service Marketplace and Home Services Marketplace are processed" — Service Marketplace processed 2026-09-07; this pass discharges the flag from the home-services side
- home-improvement-planner: "vs Home Services Marketplace (hiring leg vs planning record)"
- home-maintenance-application: "the hiring leg (finding and booking pros) vs the homeowner's upkeep plan and record; complementary"
- home-management-application: "the hiring transaction is the center; home management's pro list is a record-keeping directory that may link out to one"
- handyman-business-management / cleaning-business-management: "demand-side discovery and booking versus operator-side execution and billing; a marketplace lead becomes a job here"
- dog-walking-platform: framed "Local / Home Services Marketplace" as generic brokers — this pass refines that framing (see Boundary Findings #2)

## Research Questions

1. What is the unit of supply, and how is home-service supply organized (trades/categories, profiles, offerings)?
2. Where does the work happen — is the customer's home/property a structured part of the job (location, access, size)?
3. What matching flows exist (browse-and-book, request→offers, platform-matched claim) and who sets prices?
4. What trust machinery exists, and how much of it is specific to in-home access (background checks, ID, licensing, insurance, damage protection)?
5. How do engagements work: one-off jobs vs recurring plans; what lifecycle states matter?
6. How does money move (charge timing, holds, payouts, tips), and what leakage rules apply?
7. What does the provider side look like (job feeds, claims, earnings, software)?
8. What rules govern property access, cancellation, and guarantees?
9. Where is the boundary against generic local-service marketplaces and lead-sale surfaces?

## Representative Products

Selected for market representation + different transaction philosophies + different segments/geographies:

| Product | Domain shape | Matching/pricing philosophy | Segment | Doc access |
|---|---|---|---|---|
| Handy (powered by Angi) | multi-trade home services (cleaning, handyman, installation, outdoor, renovations) | instant browse-and-book at platform-set upfront prices; claim-based pro side | consumer (US/CA/UK) | Marketing/service pages Tier-1 reachable; help center 401 (see Sources) |
| LawnStarter | vertical (lawn & outdoor) | platform-matched claim model; satellite property pricing; recurring plans | consumer + light commercial (US) | Homepage + FAQ + provider pages Tier-1 reachable |
| TaskRabbit | local home tasks (assembly, mounting, cleaning, moving, repairs) | browse-and-book at provider-set hourly rates | consumer (global) | Help Center fully reachable (evidence from Service Marketplace pass, 2026-09-07) |
| Bark | generalist local services incl. House & Home group | request→matched leads; pros pay per lead, no commission | consumer/SMB (UK/global) | Homepage + help article Tier-1 reachable — boundary anchor, not a representative |
| Networx | home improvement quote marketplace | describe project → matched pros → quotes → hire; pros buy lead access | consumer (US) | Homepage Tier-2 reachable — boundary anchor, not a representative |

Angi (help center Okta-walled; www.angi.com 403), Thumbtack (empty responses, consistent with the umbrella pass), Urban Company (403), Porch (403) — all abandoned per network rules. The quote-request pole WITH platform settlement (Angi/Thumbtack class) is therefore under-evidenced; that pole is evidenced only in its lead-sale form (Bark, Networx) and generically via Airtasker (umbrella pass).

## Sources

Research date: 2026-09-08. All fetches 2026-09-08 unless noted.

- Handy: https://www.handy.com/ (homepage); https://www.handy.com/trust-and-safety; https://www.handy.com/handy-guarantee; https://www.handy.com/services/home-cleaning; https://www.handy.com/apply (Angi Services pro enrollment)
- LawnStarter: https://www.lawnstarter.com/ (homepage); https://www.lawnstarter.com/faq; https://www.lawnstarter.com/lawn-care-businesses (provider page); https://www.lawnstarter.com/lawn-care-software
- Bark: https://www.bark.com/ (homepage); https://help.bark.com/hc/en-gb/articles/13342669635484-What-is-Bark-and-how-does-it-work
- Networx: https://www.networx.com/ (homepage)
- TaskRabbit + Airtasker: evidence imported from research/service-marketplace.md (2026-09-07, Zendesk help centers fully reachable there)
- Unreachable (abandoned per network rules): help.angi.com (Okta login wall), www.angi.com (403), www.thumbtack.com (empty ×1 this pass; empty ×3 in umbrella pass), www.urbancompany.com (403), porch.com (403), help.handy.com (401 on both category and article URLs — limitation recorded)

**Source-access limitation:** Handy's operational help-center articles were not reachable (401); Handy operational details below come from its public service/trust pages (Tier-1 official but marketing-adjacent). No fee percentages, exact time windows beyond those printed on those pages, or internal state names are asserted in the final document. Angi/Thumbtack/Urban Company were not observed at all; no claims are made about them.

## Product Observations

### Handy (evidence layer A — directly observed, official pages)

- Positioning: "The easy, reliable way to take care of your home." Home cleaning + handyman tasks "booked and paid for through Handy" at "an upfront price". "Handy powered by Angi."
- Service taxonomy (five groups, ~40 services): Cleaning (home, move-out, office, deep); Installation (TV mounting, picture/shelf hanging, light fixtures, ceiling fans); Handyman (furniture assembly, general handyman, general plumbing, faucets, toilets, general electric, outlets/switches, moving help); Outdoor Projects (lawn care, gutters, tree removal/trimming, fence, deck, exterior painting, power washing); Home Renovations (bathroom/kitchen/basement remodel, roofing, windows, interior painting, window treatments).
- Booking flow (cleaning): enter zipcode → select bedrooms (0–10) × bathrooms (0–10) → system recommends hours (3–10h) → pick date/time → "Get a Price" (upfront). Home size is the pricing input; minimum booking length exists (3h, vendor detail).
- Recurring plans: weekly/biweekly/monthly cleaning plans, auto-scheduled, reschedulable; plan minimum terms with an early-cancel fee (vendor detail); after minimum term, auto-continues until cancelled.
- Extras: inside cabinets/fridge/oven, laundry, interior windows — each adds time/cost.
- Pro continuity: "Pro Team" — add a favorite pro, "they'll be requested first for all future bookings"; backup pros for scheduling conflicts.
- Screening (trust-and-safety page): individual pros — Jumio computer-vision ID credential verification + Checkr background check (national/state/county, ≥7 years, vendor detail); company providers — corporate information verification + owner background check. "Handy-Approved Pros."
- Guarantee/insurance: Happiness Guarantee — re-send another pro at no extra charge; "Bookings made and paid for directly on the Handy platform are insured" (damage coverage). Guarantee applies only to bookings made and paid through the platform.
- In-home access: "when you book a house cleaner through the Handy platform, you are allowing a stranger to enter your home"; custom instructions/preferences; entry instructions shared via app/text; app shows "when your cleaner arrives and check the progress of their cleaning."
- Money: entirely cashless — pay in app by card; tips through the app, "the entirety of the tip gets passed through to the pro — Handy doesn't take any percentage."
- Reschedule rule (service-page FAQ): without penalty ≥24h ahead; fees inside 24h (vendor detail).
- Pro side (apply page → "Angi Services [Handy for Pros]"): primary-service list of ~30 home trades (Appliance Repair … Window Cleaning); "Access hundreds of local jobs with no commitment! Claim the jobs you want"; "Get upfront pricing. See prices customers are paying for jobs before you claim them"; requirements: paid experience, background check, valid ID, "must attest to possessing all applicable licensing and registration for any jobs claimed"; "Angi Services isn't an employer. We connect businesses and independent service professionals with customers."
- Demand visibility for supply: a public "Recent Job Requests" feed (zipcode, base hours, bedrooms/bathrooms, description) — supply sees live demand.
- Distribution: retail partnerships — "partners who want to provide their customers, tenants, or employees easy access to quality home services" (B2B2C channel).

### LawnStarter (evidence layer A — directly observed, official pages)

- Positioning: lawn care, landscaping, outdoor services "at the click of a button"; 25 services, 1 app; US, 3,000+ cities.
- Property-address pricing: "Enter Your Address → See Your Exact Price"; "We use satellite imagery to instantly measure your lawn and calculate a fair price based on size, location, and services needed"; property features (pools, driveways, garden beds, patios) identified via "satellite and AI technology"; repricing rare (vendor detail).
- Recurring plans: weekly/biweekly/monthly frequencies; no contracts; skip/pause/reschedule/cancel with notice windows (vendor detail); 3-visit minimum (vendor detail); seasonal pause with auto-resume.
- Matching: platform-matched — "we'll match you with a Pro in your area"; customer picks date, not pro; "change my Pro" / "swap crews instantly" self-service; pro pairing preserved ("we keep that pairing so they learn exactly what you like").
- Access: "you don't need to be home"; gate codes/special notes in account; unlock gates, secure pets; day-level scheduling (not time-level); weather rescheduling.
- Trust: "all pros must pass background checks and maintain our standards"; "insurance verification"; "pros must maintain minimum ratings"; "less than 5% of pros who apply make it past our trial period" (vendor detail); "$2 Million Property Protection Pledge" for accidental damage — report via app with photos, repair/reimburse.
- Guarantee: "Done Right Guarantee" — report within 5 days, re-mow or refund (vendor detail).
- Money: card on file, "Inspect First, Pay Later" — charged 3 days after service (vendor detail); autopay; receipts; pro payouts weekly (Stripe); platform handles "payments, tax documents and route optimization".
- Provider side: "We're like Uber for lawn care. Recurring, paying customers delivered to you at no cost. Claim only the jobs that work for you, do the work, and get paid weekly." No lead fees, no bidding: "LawnStarter uses proprietary software to price each lawn based on square footage and other factors. You don't have to worry about bidding on jobs or visiting properties to price them yourself." Explicit self-distinction: "Are you a lead generation service? Not at all." Requirements: own equipment, truck/SUV, work authorization, background check.
- Provider software: free "LawnStarter Pro" business software — schedule management, route optimization, invoices, automatic billing/card processing — the marketplace bundles operator-side tools for its pros.
- Commercial extension: "LawnStarter does service commercial properties"; multiple properties per account.

### TaskRabbit (evidence layer A — imported from Service Marketplace pass, 2026-09-07)

- Local home-task marketplace: categories Cleaning, Moving, Furniture Assembly, Mounting, Home Repairs, etc.; client books a Tasker by category + task description + task location/address + date/time; sees Tasker list filtered by availability, work-area map, category, price.
- Provider-set hourly rates; providers set schedules and work areas; registration with approval step.
- Cashless platform: card required at booking, charged within 24h after the Tasker submits a post-task invoice (hours + agreed expenses); cash and off-platform payment apps prohibited; protection program covers only platform-booked-and-paid tasks.
- Contact gating: Taskers never receive the client's phone/email; task address hidden until the Tasker accepts.
- Client-side service fee + separate trust & support fee; tips 100% to Tasker; cancellation fee inside 24h (vendor details).

### Airtasker (evidence layer A — imported from Service Marketplace pass; boundary context for the request→offers pole)

- Post a task (scope, photos, time, budget) → Taskers make offers → customer assigns → escrowed payment released on completion; must-have requirements gate offering; local + remote.

### Bark (evidence layer A — boundary anchor, official pages)

- Generalist local-services venue: categories span Business, Events & Entertainers, Health & Wellness, House & Home (architects, CCTV, fencing, garden clearance, gardening, gutter cleaning, house cleaning…), Lessons, More. House & Home is one group among many — the venue is NOT home-centered.
- Model (own help article): customer answers questions about the need → "We instantly match their request to professionals" → pro "review[s] the lead and decide[s] whether to contact them" → "You pay only for the leads you choose — no commission, no hidden fees" → "You get in touch, win the job, done."
- Contact-detail gating: "Professionals will only be given your details once they've sent you a quote."
- This is the lead-sale pole: the platform sells lead access (credits), takes no commission, and the engagement/settlement happen off-platform.

### Networx (evidence layer A/B — boundary anchor, official homepage)

- "We connect homeowners with trusted local pros" — home-native (home improvement, contractors).
- Flow: describe project (service + size/timeline/budget) → "Get matched with local pros" → review profiles/services/ratings → "Receive quotes, ask questions, and compare options… there's no obligation to hire."
- Contractor side: "Get real time access to our exclusive network of local jobs" + /generate-leads — lead-sale posture; cost guide and review content surround the matching.

## Cross-product Comparison

| Dimension | Handy | LawnStarter | TaskRabbit | Bark (anchor) | Networx (anchor) |
|---|---|---|---|---|---|
| Domain center | multi-trade home services | lawn & outdoor (vertical) | local home tasks | generalist local (House & Home one group) | home improvement quotes |
| Job site | customer's home | customer's property (address) | task address | varies (often premises) | customer's project site |
| Property as job attribute | bedrooms/bathrooms → hours → price | satellite-measured property → price | address + description | minimal | size/timeline/budget details |
| Matching pole | instant browse-and-book | platform-matched claim (swap anytime) | browse-and-book | request→matched leads | request→quotes |
| Pricing regime | platform-set upfront fixed | platform-set (computed) | provider-set hourly | provider quotes (off-platform) | provider quotes (off-platform) |
| Provider admission | ID + background check (+ company verification) | background check + trial + insurance verification | approval + registration fee | free signup | signup |
| Licensing posture | attestation required per claimed job | "pros maintain required local licenses" (claim) | not observed | not observed | "fully insured" (review quote) |
| Settlement | on-platform, cashless, tips 100% through | on-platform, charge-after-service, weekly payouts | on-platform, charge-after-invoice | none (no commission) | none observed |
| Damage protection | insured bookings + guarantee | $2M property protection pledge + guarantee | protection program | n/a | n/a |
| Recurring plans | cleaning plans (weekly/biweekly/monthly) | mowing plans (weekly/biweekly/monthly) | no (one-off) | n/a | n/a |
| Pro continuity | Pro Team (requested first) | pairing preserved, swap anytime | rebook favorites | n/a | n/a |
| Provider economics | claim jobs, no lead fees, platform-set prices | claim jobs, no lead fees, platform-set prices, weekly pay | provider-set rates, platform commission | pay per lead, no commission | pay for lead access |
| Access machinery | entry instructions, arrival/progress tracking | gate codes, pets secured, no presence needed | address hidden until accept | contact gated until quote | contact after quote |

Evidence-layer summary:

- **B-layer (cross-product, 3/3 representatives):** operator-run venue over many independent home-service providers; providers author their presence (profile/credentials/availability/work scope) as the supply customers evaluate; the matching decision happens on-platform (browse-and-book, platform-matched claim, or request→offers); the engagement binds customer × provider × home service × property × terms and is tracked to completion; payment flows through the platform (cashless posture, tips passed through, provider payouts administered); leakage/cash prohibitions; post-job ratings; distinct customer and provider surfaces.
- **B-layer domain structuring (3/3 representatives + both home-native anchors):** the customer's home/property is the job site — its location scopes the market locally, access to it is part of the job (entry instructions, presence optional), and its physical characteristics are pricing/scope inputs; supply is organized as home trades; trust machinery addresses letting a screened stranger onto the property (background checks, ID, licensing posture, insurance/damage protection); guarantees with re-do/refund remedies are standard.
- **B-layer as common structure (not definitional):** recurring service plans, pro continuity/pairing, property-attribute pricing engines, provider job feeds with claim flows, weekly payout administration, bundled provider business software, B2B2C partner distribution.
- **A-layer (product-specific, kept out of the canonical core):** Happiness Guarantee, Done Right Guarantee, $2M Property Protection Pledge, OptiMOWzation, Taskprotect, Pro Team, Checkr/Jumio specifics, plan minimum terms and early-cancel fees, 24h/48h notice windows, 3-visit minimum, long-grass fee, "powered by Angi", Angi Services branding, satellite-pricing claims, trial-period percentages.

## Canonical Model

### Level 0 — Defining Invariant

The Service Marketplace skeleton (five structures), domain-bound by one added property. Six properties; remove any one and the product stops being a home-services marketplace:

1. **Operator-run two-sided venue over many independent home-service providers** — the operator hosts external, self-employed individuals/businesses and is not the performer. (Remove multi-provider independence → one business's booking site; remove external independence → an operator's own field-workforce dispatch.)
2. **Provider-authored presence as the supply** — providers author who they are, their credentials, their trade scope, their availability/work area; this authored presence is what the demand side evaluates (directly, or via the platform's vetting of it). The depth of provider control over *pricing* varies by product (provider-set ↔ platform-set) and is not definitional. (Remove authored presence → an operator-configured catalog, not a market.)
3. **On-platform matching decision across providers** — the customer's selection (browse-and-book, accept an assigned/matched pro, or pick among offers) and the providers' own accept/claim/decline decisions all happen inside the venue. (Remove → directory/lead-sale handoff.)
4. **Service engagement of record bound to the customer's property as the job site** — a persistent unit binding customer × provider × home service × property × terms, carried through a status lifecycle to completion or cancellation. The property is a first-class job attribute: its location scopes the market, access to it is part of the job, its characteristics shape scope and price. (Remove the property-as-job-site binding → a generic service marketplace; remove the engagement → a listing board.)
5. **Platform-mediated settlement** — payment for the engagement flows through the platform under its rules (charge, hold, release, payout), with off-platform workarounds prohibited. (Remove → lead-sale/classifieds surfaces — exactly the Bark/Networx pole.)
6. **Home-trade domain binding** — the venue's supply, matching, and engagements center on services that maintain, repair, or improve the customer's home or property (cleaning, handyman, plumbing, electrical, HVAC, lawn/outdoor, moving, assembly, junk removal, painting, renovations). (Remove → generic local-services marketplace.)

Historical/market-sample check: the six-property core is era- and region-independent in structure. A pre-digital home-service agency (brokerage that signs vetted cleaners/tradespeople, takes customer bookings, charges the customer, pays the worker) satisfies the core without apps, satellite pricing, or AI — the agency-dispatch model is the platform-matched pole in paper form. Yellow-pages directories and newspaper classifieds fail the core (no on-platform matching decision, no settlement) and are correctly ancestors, not instances. Regional products (UK Bark at the boundary; India's Urban Company unreachable but structurally represented by the claim-model pole) fit without US-specific machinery; nothing US-specific is in the core.

### Level 1 — Common Mature Structure

Present across the researched sample; makes the market work but does not define the Type:

- Home-trade service taxonomy (categories/subcategories structuring supply and demand)
- In-home trust machinery: background checks, ID verification, company verification for business providers, licensing attestation/verification posture, insurance verification
- Property-damage protection and satisfaction guarantees with re-do/refund remedies, tied to platform-booked-and-paid engagements
- Property-attribute-driven pricing (home size → hours/price; property measurement → price)
- Recurring service plans (weekly/biweekly/monthly) with skip/pause/reschedule and notice windows
- Pro continuity (favorite-pro teams, pairing preservation) with swap/change-pro self-service
- Two consoles: customer app/web (book, track, message, pay, review) + provider app (job feed/claims, schedule, earnings)
- In-platform messaging with contact-detail gating (address/phone hidden until acceptance, in the observed forms)
- Ratings/reviews loop gated to completed jobs
- Provider earnings administration (payouts, statements, tax documents)
- Access & arrival machinery (entry instructions, arrival notices, progress visibility)
- Cashless payment posture; tips passed through to the provider

### Level 2 — Variant / Optional Structure

- Matching pole: instant browse-and-book ↔ platform-matched claim ↔ request→offers (all on-platform); the lead-sale pole (pay-per-lead, no settlement) sits OUTSIDE the Type
- Pricing regime: provider-set hourly ↔ platform-set upfront fixed ↔ computed property pricing ↔ quoted per job
- Breadth: multi-trade generalist ↔ single-trade vertical marketplace
- Cadence: recurring-plan-centric (cleaning, lawn) ↔ one-off-job-centric (assembly, mounting, repairs, moves)
- Supply entity: individual professionals ↔ companies/franchisees under verification
- Distribution: direct consumer ↔ B2B2C partner channels (retail, property managers, employers)
- Property scope: residential center of gravity with commercial extension (some products)
- Managed-marketplace depth: pure brokerage ↔ platform-run pricing/routing/software for pros
- Era-current additions: satellite/AI property measurement, AI matching/assistance

### Level 3 — Vendor-specific Structure

Remains in Research Notes: branded guarantees and protection programs, named screening vendors, exact fees/percentages, notice windows and minimum terms, branded provider software, "powered by Angi" branding, public job-request feeds, trial-period percentages, satellite-pricing marketing claims.

## Vendor-specific Findings

- Handy: Happiness Guarantee (re-send another pro), insured bookings, Pro Team, Jumio/Checkr screening stack, company-provider onboarding track, plan minimum terms with early-cancel fee, public "Recent Job Requests" feed, retail partnerships, "Handy powered by Angi"; pro side rebranded "Angi Services" with claim-based jobs and upfront platform pricing.
- LawnStarter: satellite/AI property pricing, Done Right Guarantee (5-day window), $2M Property Protection Pledge, Inspect-First-Pay-Later (charge 3 days after service), weekly Stripe payouts, pro pairing + swap, free LawnStarter Pro software (scheduling/routing/invoicing/billing), explicit "not a lead generation service" self-distinction, day-level scheduling with weather rescheduling, commercial-property extension.
- TaskRabbit: provider-set hourly rates, address hidden until acceptance, charge-after-invoice, trust & support fee line item, Taskprotect.
- Bark: credit-based lead purchase, no commission, contact details released only after a quote is sent.
- Networx: matched-pro quotes with "no obligation to hire", contractor lead-access product, cost-guide content layer.

## Boundary Findings

1. **vs Service Marketplace (§05.02 umbrella, processed)** — domain-structured sibling, per the umbrella's own recorded structure. Same five-structure skeleton; this Type adds the property-as-job-site binding and home-trade domain. The umbrella's "local task marketplaces" variant (TaskRabbit-class) overlaps this Type's one-off pole; the umbrella's digital/professional poles (Fiverr/Upwork) do not. Joint review with the umbrella is effectively discharged: the umbrella pass ratified the sibling structure and this pass confirms it from the sibling side. No taxonomy change proposed.
2. **vs Local Service Marketplace (§29, UNPROCESSED — sharpest live seam)** — both are local, on-site, multi-provider marketplaces. Working discriminator from this side: Home Services Marketplace centers the customer's home/property as the job site and organizes supply as home trades (the whole venue is home-shaped); a generic local-service venue carries any local service (events, lessons, wellness, business services) with generic job objects. Bark is the live specimen of the generalist shape (House & Home is one category group; machinery is generic) — it sits on the local-services side, not this Type. The dog-walking pass's framing of "Local / Home Services Marketplace" as generic brokers is hereby refined: home-services is domain-structured, not generic. JOINT REVIEW RECOMMENDED when local-service-marketplace is processed.
3. **vs Babysitting Marketplace (§29, processed)** — joint-review flag from that pass DISCHARGED from this side (Service Marketplace having been processed 2026-09-07). Same two-sided skeleton; domains differ structurally: babysitting's invariant object is the individual caregiver profile with child-safety trust construction and in-home family context; home services' invariant is the property-as-job-site with in-home access trust and trade licensing posture. Both remain distinct domain-structured siblings; boundary held.
4. **vs Classifieds Platform (§05.03, processed)** — consistent with the umbrella's test: platform-mediated settlement + recorded engagement are load-bearing; strip them → classifieds. The lead-sale anchors (Bark, Networx) sit between this Type and classifieds/lead-gen and are excluded from the Type for exactly this reason.
5. **vs Lead Generation Platform (§06, processed)** — Bark ("pay only for the leads you choose — no commission") and Networx (contractor lead access, "no obligation to hire") sell contact/quote opportunities; the engagement and its settlement do not occur on the platform → not this Type. They are documented adjacent poles of the same demand.
6. **vs operator-side trade software (cleaning/handyman/lawn-care business management, processed)** — demand-side multi-provider market vs one business's execution/billing system; a marketplace job becomes the operator's job. Boundary specimen: LawnStarter bundles free business software for its pros — the marketplace supplying operator-side tools does not make it operator-side software.
7. **vs homeowner-side §29 siblings (Home Improvement Planner, Home Maintenance Application, Home Management Application — processed)** — the hiring transaction vs the homeowner's planning/record. Marketplaces feed the planner's hiring machinery; the planner's records are not the marketplace's object. All three passes' forward notes are answered from this side; complementary, not identical.
8. **vs Property Maintenance Management (§17)** — professional/landlord-side maintenance operations over a property portfolio vs consumer-side hiring market for one's own home.
9. **vs Appointment Scheduling Application (§03.09, processed)** — one operator's own bookable offerings vs a competitive multi-provider market.
10. **vs Field Service Management / Small Business Field Service Management** — dispatch of a business's OWN field workforce vs matching among independent external providers.

## Uncertainties

- The quote-request pole WITH platform settlement (Angi/Thumbtack class — describe job → competing quotes → book and pay on-platform) could not be directly observed (Angi Okta-walled + 403; Thumbtack empty across both passes). Its existence is structurally implied by the umbrella's Flow B and by Airtasker's post→offers→assign model, but home-native operational details remain unverified. No claims about Angi or Thumbtack are made in the final document.
- Handy's help center was unreachable (401); Handy operational rules (exact cancellation windows, fee mechanics) rest on its public service/trust pages only.
- Whether regulated-trade licensing is verified or merely attested could only be observed as attestation (Angi Services apply page); LawnStarter's license claim is marketing-level. Held at "licensing posture varies and is asserted per job" strength.
- Non-US managed-marketplace products (Urban Company, Helpling) unreachable; the non-US pole is represented structurally (Bark UK; TaskRabbit global) but not by a managed-marketplace specimen.
- Recurring-plan machinery is evidenced in two products (Handy cleaning plans, LawnStarter mowing plans); held as common-mature rather than definitional on that evidence.

## Final Synthesis

A Home Services Marketplace is the Service Marketplace skeleton instantiated for the home: an operator-run two-sided venue where independent home-service providers author their presence as supply, homeowners make the matching decision on-platform, the resulting engagement is recorded as a binding of customer × provider × home service × property × terms, and payment is settled through the platform. The domain binding that makes the Type recognizable is the customer's home/property as the job site — its location scopes the market, access to it is part of the job, and its characteristics shape scope and price — together with supply organized as home trades and trust machinery built for letting a screened stranger onto the property. Everything else commonly seen — background-check programs, damage protection, recurring plans, property-pricing engines, pro-pairing, provider software, partner distribution — is mature market machinery around that core, not the definition. The lead-sale pole (Bark/Networx) and the generalist local-services venue sit outside the Type; the operator-side trade systems and the homeowner-side planning apps sit on the other side of the demand/supply and transaction/record seams.
