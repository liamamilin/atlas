# Research Notes — Service Marketplace

## Research Goal

Understand what a generic Service Marketplace (DIRECTORY §05.02) actually is as an Application Type: what exists inside it, how the two sides (customers and service providers) meet and transact, what machinery the platform operates, and where its boundaries lie against goods marketplaces, classifieds, vertical service marketplaces, scheduling tools, and job boards.

## Initial Boundary

Hypothesis before research: a platform-operated two-sided venue where many independent service providers are the discoverable supply, customers discover/select them, and the resulting service engagement is transacted through the platform. Nearest neighbors:

- Online Marketplace / Multi-vendor Marketplace (§05.02) — goods, not services
- Marketplace Platform (§05.02) — suspected to be venue-builder SaaS, not the venue
- Classifieds Platform (§05.03, processed) — ads + off-platform contact
- Vertical service marketplaces (§29 Home/Babysitting/Beauty/Local Service; §26 Food Delivery; §08 Insurance; §27 Brand-Creator) — domain-structured siblings
- Appointment Scheduling Application (§03.09) / Appointment-based Service Business Management (§29) — single-operator, no marketplace selection
- Job Board (§09, processed) — employment, not service engagements

Prior passes already referenced this leaf: beauty-service-marketplace ("documented as the beauty-domain sibling marketplace per the babysitting-marketplace precedent"), babysitting-marketplace ("boundary held on the domain-structured core"), artist-booking-platform ("structurally similar supply-profile + demand-request + transaction, but the performance-specific lifecycle is domain machinery"), appointment-based-service-business-management ("consumer-side discovery vs operator-side"). This pass is the generic side of those seams.

## Research Questions

1. What is the unit of supply — a profile, a service listing, a bookable offering? How is it structured?
2. How does demand find supply — catalog search, post-and-offer, or both?
3. What is the transaction object (booking / task / order / contract) and what lifecycle does it carry?
4. How does money move — who charges when, who holds funds, when is the provider paid, what does the platform keep?
5. What trust machinery exists (reviews, verification, insurance, guarantees) and how does it gate behavior?
6. What rules govern participation — leakage prohibitions, cancellation policies, moderation, provider admission?
7. What is the provider-side experience (the "supply app") versus the customer-side experience?
8. Which roles/entities exist on the supply side (individuals, businesses, agencies) and demand side (consumers, businesses)?

## Representative Products

Selected for market representation + different transaction philosophies + different segments:

| Product | Domain | Transaction philosophy | Segment | Doc access |
|---|---|---|---|---|
| TaskRabbit | local home tasks | browse-and-book hourly (provider-listed rates) | consumer | Help Center fully reachable (Zendesk) |
| Airtasker | local + remote odd jobs (AU-origin, AU/UK/US) | post-task → offers → assign | consumer | Help Center fully reachable (Zendesk) |
| Fiverr | digital services | productized gig catalog + AI brief → tailored offers | consumer/SMB | Help Center fully reachable (Zendesk) |
| Upwork | professional freelance work | post-job → proposals → contract (hourly/fixed, escrow) | SMB/enterprise | Help Center fully reachable (Zendesk) |
| Thumbtack | local services | quote-request model (market reputation) | consumer | NOT reachable (see Sources) |

Fiverr/Upwork test the boundary: they are commonly called "freelance marketplaces"; no separate freelance leaf exists in the DIRECTORY, so they are treated as the digital-services variant of this Type.

## Sources

Research date: 2026-09-07. All fetched 2026-09-07.

- TaskRabbit Support (Zendesk): help root https://support.taskrabbit.com/hc/en-us; categories/sections via Zendesk API; articles: "Why Can't I Find a Tasker?", "What Do Taskers Offer?", "Why Do You Need My Credit Card?", "Do Taskers See My Phone Number, Email, or Address?", "Can I Book a Same Day Task?", "How Far in Advance Can I Book My Task?", "What Info Should I Put in the Task Description?", "Can I Contact a Tasker Before Booking a Task?", "How Do I Pay My Tasker?", "What's the Taskrabbit Service Fee?", "What's the Taskrabbit Trust & Support Fee?", "How Do I Reimburse My Tasker For Expenses?", "I Think I Was Charged a Cancellation Fee", "Am I Charged a Sales Tax?", "Finding Volunteers on Taskrabbit".
- Airtasker Support (Zendesk): categories "I am a Customer" / "I am a Tasker" / "Airtasker Guidelines"; articles: "How do I post a task?", "I posted my task, what's next?", "How do I know how much to pay for a task?", "What is the maximum task price?", "How far ahead can I schedule a task?", "What happens if I get no offers on my task?", "What should I do with expired tasks?", "What are some must-have information for Customers?", "How to get things done with Airtasker on ChatGPT".
- Fiverr Help Center (Zendesk): help root; articles: "Creating a Gig", "Post a project brief: get tailored offers for your project", "The complete guide to your Fiverr order: Statuses and process", "Leaving and managing reviews on Fiverr", "Using the Resolution Center", "Your earnings page".
- Upwork Help Center (Zendesk): categories (client: Get Started / Find Talent / Make a Hire / Manage Your Project / Pay for Work / Project Catalog; freelancer: Get Started / Build Your Profile / Find a Project / Start Working / Get Paid); articles: "How to start hiring on Upwork", "How hourly and fixed-price contracts are different on Upwork", "What's the difference between a freelancer and an agency on Upwork?", "Job Success Score", "What is the Upwork Conversion Fee?", "Business Plus features and how they work".
- Thumbtack: https://help.thumbtack.com/ and https://www.thumbtack.com/ returned empty/JS-shell content (3 attempts across both hosts, abandoned per network rules). **Source-access limitation:** no direct evidence for Thumbtack; it is retained as a market example only, with no operational claims made about it anywhere in this research.

## Product Observations

### TaskRabbit (evidence layer A — directly observed)

- Roles: **Client** and **Tasker** (independent contractor). Help center categories: Client / Tasker / Registration / Account / Policy Center.
- Demand flow: pick a task category (Cleaning, Moving, Furniture Assembly, Mounting, Home Repairs, Personal Assistant, Shopping & Delivery, Help Moving, ...) → enter task description, task location/address (start+end for moves), date/time (same-day possible; up to 14 days ahead) → **see a list of Taskers based on availability, work area map, category, and price** → select → confirm booking ("Confirm and chat"). Before booking, contacting a Tasker is not possible; the client evaluates profiles, reviews, and hourly rates.
- Supply: Taskers "have the flexibility to set their own hourly rates, schedules, and work areas" — provider-defined pricing and availability. Registration includes an approval step and a registration fee (vendor detail).
- Payment: "Taskrabbit is a cashless platform" — a valid card is required at booking "to verify your identity and validate your card"; **charged within 24 hours after the Tasker submits their invoice post-task** (invoice = hours worked + agreed expenses). Cash and off-platform payment apps "are not allowed"; listing prohibited practices includes "any other action that circumvents the Taskrabbit payments system". Task protection ("Taskprotect") covers only tasks booked and fully paid through the platform.
- Fees: client-side service fee (percentage of hourly rate) plus a separate "Trust & Support fee" line item (funds the protection program and support); tips go 100% to the Tasker; expenses reimbursed via invoice with receipt photo proof (policy caps and partner-task exceptions are vendor details); cancellation fee if client cancels inside 24h of scheduled time or is unresponsive; sales tax collected in listed jurisdictions.
- Pricing variance: hourly is the default; **fixed-price / pre-paid pricing tasks exist** (partner tasks) — expenses not permitted on non-hourly tasks.
- Privacy/communication: Taskers never receive the client's phone/email; all communication via in-app chat and call; **task address hidden from the Tasker until they accept the task invite** — the platform mediates and gates contact information.
- Anomaly paths: address changes handled via chat or cancel+rebook; "General Marketplace tasks" vs partner tasks are named differently by the vendor itself; a free volunteer program runs the same task lifecycle without task charges (expenses still flow through the platform) — evidence that the booking/engagement machinery is separable from the payment amount but not from platform-mediated settlement.

### Airtasker (evidence layer A)

- Roles: **Customer (Poster)** and **Tasker**. Regional: Australia-origin, operating AU/UK/US; remote tasks allow a national audience.
- Demand flow: **post a task** — describe scope (photos attachable), set time, set a **budget** ("a starting point"; "Tasks that simply ask for a quote are not supported") → posted publicly on the task feed → interested Taskers **make offers** → customer reviews and **accepts an offer (assign)** → private message to arrange details. "Must-have" requirements (a small bounded set) gate offering: Taskers must agree to them before offering.
- Matching economics: "Taskers will offer a price based on time, skill, and effort"; price discussion happens in task comments before assignment; platform publishes cost guides and a service calculator; platform moderates unreasonably low budgets.
- Payment: card details required before assignment; **payment debited at assignment and "held securely in escrow" (platform pay service) until the task is complete**; the customer releases payment on completion. Labor cost must flow through the platform; genuine out-of-pocket expenses (materials, dump fees) may be paid separately with receipts/documentation. Unassigned tasks expire (7 days after deadline — vendor detail) and can be reposted as copies.
- Trust: dedicated help sections for Badges and Verifications, Building Trust, Keeping You Safe, Insurance, Task conflicts, Dispute, Refunds. Community guidelines govern posting and payment conduct; breaching them can limit or deactivate accounts.
- Current-era extension: a ChatGPT integration lets posters and Taskers run posting/comparison/hiring through an agent, with **payments still handled through the platform** ("Payments are handled through Airtasker, so you won't need to enter your card details into ChatGPT").

### Fiverr (evidence layer A)

- Roles: **Freelancer (seller)** and **Client (buyer)**; separate help universes "For freelancers" / "For clients" / "For Pro clients".
- Supply structure — the **Gig**: "Your Gig is how you offer services on Fiverr. It's your storefront." Composition: title ("I will..."), category/subcategory (locked after publish; some categories vetted-only), search tags, **pricing packages** (up to three tiers: Basic/Standard/Premium, each with delivery time, revision count, price), description, FAQs, **requirements** (structured intake questions the client must answer before work starts), media gallery (images/video/PDF portfolio), optional add-ons ("Gig Extras", e.g., faster delivery), milestones for larger projects. Publication goes through automatic policy review before the Gig becomes visible.
- Provider admission: full freelancer profile + phone/email verification + identity verification (KYC) + tax forms (W-9 US / DAC7 EU) + business information verification; gig counts and features are tiered by earned freelancer level (vendor detail).
- Demand path 1 — catalog: browse/search gigs → purchase a package → order opens. Demand path 2 — **project brief**: client posts a brief (AI-assisted refinement; timeline+budget mandatory), platform curates and routes it to matching freelancers, who send **tailored offers** ("custom offers"); the client compares offers and accepts, possibly several. Brief states: Live / Inactive / Hired / Rejected. Same product supports both matching poles.
- Order lifecycle (documented status ladder): order placed → **Requirements Needed** (client submits structured requirements; freelancer may skip) → **In Progress** → (optional draft previews, watermarked) → **Delivered** → client accepts / requests revisions (**In Revision**) / extends review window → auto-complete if no action within the review window (exact windows are vendor details) → **Completed** → review + tip. Late states (**Late**, **Very Late**) permit client cancellation without freelancer approval after defined delays. Tabs: Active / Missing details / Delivered / Completed / Cancelled.
- Money: client pays at order (extras/custom offers purchasable); **freelancer earns a fixed share of the purchase amount (80% documented)**; funds sit in "Future payments" → **Clearing** after completion → available balance → **withdrawal** to payout methods. Early payout for a fee and cash advance exist (vendor features). Seller earnings dashboard: balance, overdraft, activity ledger (clearing/earning/reversal/withdrawal), financial documents (statements, 1099-K, regional tax forms) — the platform is the payment intermediary of record for provider income.
- Reviews: "Reviews and ratings are the foundation of a trusted marketplace." **Two-way**: client reviews first; freelancer cannot see it until submitting their own; public star+text review on gig/profile pages plus an anonymous private satisfaction rating used internally; response option; review window after completion; reviews on eligible canceled orders under specific conditions. Ratings reflect a rolling window, not lifetime averages (vendor detail).
- Disputes: **Resolution Center** — structured requests (mutual cancellation, delivery-date extension, get an order update, partial-refund offer) sent to the counterparty with a response deadline and auto-accept; unavailable after completion/cancellation; cancellations affect the freelancer's performance metrics and search visibility — reputation governance enforced by the operator.
- Pro tier: vetted talent and managed onboarding for larger clients (vendor-specific tiering).

### Upwork (evidence layer A)

- Roles: **Client**, **Freelancer**, **Agency** (a team under one profile; payments go to the agency, which pays its members) — supply can be an individual or an organization.
- Demand path 1 — post a job: job post (description, skills, scope, budget) → freelancers send **proposals** → client reviews/invites → interviews (platform messaging, built-in video meetings) → **send an offer** → contract begins. Demand path 2 — **Project Catalog**: "predefined projects with a set scope, price, and timeline" purchased directly. Both poles again.
- Contract types (the transaction object): **hourly** (freelancer logs hours in a work diary; weekly billing cycle with a client review/dispute window before funds release; weekly hour limits) and **fixed-price** (project split into **milestones**; client **funds each milestone in escrow before work begins**; on submission the client approves → funds released; a review window auto-releases if no action). A one-time contract-initiation fee applies per new contract (vendor detail).
- Trust: **Job Success Score** — a platform-computed reputation score "based on client feedback, contract outcomes, and client relationships" (agencies get an aggregate); talent badges (including vetted tiers for higher plans); identity verification; Trust & Safety documentation. Client plans (Basic/Pro/Business Plus) tier vetted-talent access, AI recruiting assistance, invites/messaging quotas, monthly invoicing/30-day terms (enterprise billing), spend reporting.
- Leakage control: terms require work and payments to stay on-platform for an initial period; a **conversion fee** (documented formula based on the freelancer's estimated annual earnings) legitimizes taking the relationship off-platform; converting forfeits platform protections (support, payment protection, dispute resolution). Violation risks account suspension.
- Provider side: build profile (portfolio, rates, skills), search projects, send proposals (connects/points are a vendor metering detail), work (messages, work diary, contracts, feedback), get paid (earnings, withdrawal, reports, taxes), payment-issue and dispute paths.

### Thumbtack (no evidence — limitation recorded)

Not directly observed. Included in the sample as a market-representative example of the local-services quote-request pole. No claim in this research or in the final document depends on Thumbtack mechanics.

## Cross-product Comparison

| Dimension | TaskRabbit | Airtasker | Fiverr | Upwork |
|---|---|---|---|---|
| Domain | local home tasks | local/remote odd jobs | digital services | professional freelance work |
| Demand side | consumers | consumers | consumers/SMB | SMB/enterprise |
| Unit of supply | Tasker profile + hourly rate + categories | Tasker profile + offers | Gig (productized listing, packages) | Freelancer/Agency profile + proposals |
| Matching poles | browse-and-book only | post-and-offer (browse emerging) | both (gig catalog + brief→offers) | both (job posts + Project Catalog) |
| Transaction object | Task (booking) | Task (posted + offer) | Order (against a Gig) | Contract (hourly or fixed) |
| Pricing model | provider-set hourly; fixed/prepaid variants | budget + negotiated offer | seller-set packages; extras; hourly exists | provider rate / milestones / catalog price |
| Charge timing | after completion (provider invoice → auto-charge) | at assignment (escrow) | at order | weekly (hourly) / milestone pre-funding (fixed) |
| Platform money role | collects, pays Tasker, client-side fees | escrow hold + release | collects, holds through clearance, pays 80% share | escrow milestones / weekly billing; pays provider |
| Trust machinery | reviews; protection program; ID/card verification | reviews; badges/verifications; insurance | two-way reviews; KYC/ID; levels | JSS reputation score; badges; verification |
| Disputes | policy center + support | dispute/conflicts sections, refunds | Resolution Center (structured requests) | review/dispute windows; arbitration terms |
| Leakage rule | all payment on platform; prohibited off-platform | labor costs via platform pay; receipts for expenses | reviews only from on-platform purchases; payment terms | 2-year exclusivity + conversion fee |
| Supply entities | individuals | individuals | individuals (agencies via studios marginally) | individuals AND agencies |
| Demand-initiated docs | task description at booking | task post | project brief | job post |

Evidence-layer summary:

- **B-layer (cross-product, 4/4):** platform-operated venue over many independent providers; provider-authored supply (profile/offer/listing); on-platform matching decision across providers; recorded engagement binding customer×provider×service×terms with a status lifecycle; platform-mediated payment with hold/settle semantics; leakage prohibition; post-completion review loop feeding provider reputation; distinct customer and provider consoles; platform commission/fee.
- **B-layer as common structure (not definitional):** verification/badges, dispute machinery with named states, messaging, service taxonomies, search filters, provider-side earnings dashboards with withdrawal, performance metrics.
- **A-layer (product-specific, keep out of canonical core):** every named fee, percentage, window, cap, score formula, brand (Taskprotect, Airtasker Pay, Project Catalog, Resolution Center, Job Success Score, Gig, Tasker), level/ladder systems, AI assistant features, agency construct, enterprise billing, gift/volunteer programs.

## Canonical Model

### Level 0 — Defining Invariant

Five properties; remove any one and the product stops being a service marketplace:

1. **Operator-run two-sided venue over many independent providers** — the operator hosts a population of external, self-employed individuals/businesses and is not itself the service performer. (Remove multi-provider independence → a single business's booking site; remove external independence → internal workforce tooling.)
2. **Provider-authored service supply** — providers present themselves and their offerings (profile, rates, packages, portfolio) as discoverable records on the venue. (Remove → the venue is an operator-configured catalog, not a market.)
3. **On-platform matching decision across providers** — the customer discovers, compares, and selects a provider, or broadcasts demand that providers answer with offers; either way the matching decision is made on the venue from its own provider population. (Remove → a directory/lead-gen handoff, or a single-vendor storefront.)
4. **Recorded service engagement of record** — matching creates a persistent unit (booking/task/order/contract) binding customer × provider × service × terms (scope/time/price), carried through a status lifecycle to completion or cancellation. (Remove → ephemeral chat or a listing without a transaction.)
5. **Platform-mediated settlement** — payment for the engagement flows through the platform under its rules (charge, hold/escrow, release, payout), with off-platform workarounds explicitly prohibited. (Remove → classifieds: the venue brokers contact but not the transaction.)

Concept → implementation separation:

```text
Concept:  two-sided venue over independent providers
Impl:     open self-registration with approval (TaskRabbit/Airtasker) ·
          registration + KYC + tax forms + policy review (Fiverr) ·
          freelancers and agencies (Upwork)

Concept:  provider-authored supply
Impl:     profile + hourly rate + work area (TaskRabbit) ·
          profile + offers (Airtasker) ·
          gig listing with pricing packages (Fiverr) ·
          profile + proposals + contract rates (Upwork)

Concept:  matching decision on-platform
Impl:     browse-and-book (TaskRabbit) · post→offers→assign (Airtasker) ·
          gig purchase + brief→tailored offers (Fiverr) ·
          job post→proposals→offer + Project Catalog (Upwork)

Concept:  engagement of record
Impl:     Task (TaskRabbit) · Task (Airtasker) · Order (Fiverr) · Contract (Upwork)

Concept:  platform-mediated settlement
Impl:     charge-after-completion invoice (TaskRabbit) ·
          escrow at assignment, release at completion (Airtasker) ·
          pay-at-order → clearance → withdrawal (Fiverr) ·
          weekly billing / milestone escrow (Upwork)
```

### Level 1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- two-way or provider-side review/rating system gated to completed engagements, feeding a persistent provider reputation
- provider verification (identity, sometimes background/credential checks) surfaced as badges
- provider-side workspace: incoming demand (bookings/offers/job feed), engagement management (accept, schedule, communicate, deliver, mark complete, invoice), earnings (balance, hold/clearance, withdrawal, statements, tax documents), performance metrics
- customer-side engagement tracking: status ladder, messages, deliverables/arrival, review flow
- platform messaging between the matched parties; contact-detail gating/leakage rules
- structured demand intake (task description, brief, requirements, must-haves)
- service taxonomy with search/filter and location scoping (local vs remote)
- dispute/cancellation machinery with defined states and consequences (fees, refunds, metric impacts)
- platform fee structure on either side; tips; taxes collected where applicable
- payment-protection semantics (money held until completion/acceptance)

### Level 2 — Variant / Optional Structure

- matching model emphasis: browse-and-book vs post-and-offer (many products run both)
- pricing regime: provider-set hourly, negotiated offers/quotes, productized packages, fixed milestones, pre-paid fixed, subscriptions/recurring engagements
- charge timing and hold model (at booking / at assignment / weekly / on completion; escrow vs clearance ledger)
- domain: physical-local vs digital-remote; regulated and risky domains add vetting/insurance
- supply entity type: individuals vs businesses/agencies
- demand entity type: consumers vs SMB vs enterprise (enterprise tier adds invoicing, teams, spend controls, vetted talent, managed support)
- trust intensifiers: background checks, credential vetting, insurance/guarantee programs, curated/vetted tiers
- provider gamification: levels, gig limits, badges, membership programs
- AI assistance: brief generation, matching/shortlisting, offer drafting (current-market common, optional)
- marketplace distribution surfaces: web, mobile apps, agent/plugin integrations

### Level 3 — Vendor-specific Structure (research notes only)

- Named programs: Taskprotect (protection program), Trust & Support fee, IKEA partner tasks, GoGoGrandparent phone booking, volunteer program; Airtasker Pay, cost guides, service calculator, incentives, ChatGPT plugin; Fiverr Gig/Extra/Custom Offer/Seller Plus/Pro/Success Manager, freelancer levels and gig-count limits, Early Payout, Cash Advance, Promoted Gigs; Upwork Job Success Score, Project Catalog, Direct Contracts, Any Hire, Contract Initiation Fee, Conversion Fee, Expert-Vetted, Uma Recruiter, Business Plus monthly invoicing.
- Precise parameters (not canonical): exact fee percentages (e.g., Fiverr 80% seller share), review windows (14/30/60 days), auto-complete windows (3 days; 14 for shipping), resolution response window (48h), booking horizons (14 days; 6 months), expense caps ($100), price floors/ceilings ($5; $9,999; $3/hr; $5 project), registration fees, invite/messaging quotas, JSS threshold language (90%), expiration periods (7 days), sales-tax state lists, W-9/DAC7/1099-K specifics, conversion-fee formula.
- These are recorded here to keep the canonical document free of false precision; all were directly observed but are vendor settings, not Type structure.

## Vendor-specific Findings

- TaskRabbit: client-side service fee + separate trust fee; charge happens on the provider's post-task invoice; partner-channel tasks use fixed/prepaid pricing; free volunteer variant of the same task lifecycle; the vendor calls its own core "General Marketplace tasks" (self-identification as a marketplace).
- Airtasker: quote-only tasks prohibited (budget required); escrow debited at assignment; expenses separable with receipts; account limitation/deactivation powers; AI-agent surface for both sides.
- Fiverr: the gig as productized listing (packages, locked category, intake requirements, gallery) with publication review; two-way reviews with blind sequencing; anonymous private satisfaction ratings; structured Resolution Center requests with auto-accept; cancellation effects on seller metrics/search visibility; earnings clearance ledger with overdraft; regional tax-form machinery.
- Upwork: contract with hourly work-diary vs milestone escrow; agency construct; conversion fee as monetized leakage exit; enterprise plan ladder; platform-computed reputation score.

## Boundary Findings

1. **vs Online Marketplace / Multi-vendor Marketplace (§05.02 siblings):** goods marketplaces trade shippable product SKUs with inventory; the unit of supply here is a performed service bound to a time and a provider, and fulfillment is the provider's labor rather than logistics. Remove the service/performance semantics and the booking lifecycle → a goods marketplace.
2. **vs Marketplace Platform (§05.02 sibling, unprocessed):** this leaf is the consumer-facing venue; the sibling name is standard industry usage for software used to build/run venues (builder SaaS). The seam is operator-of-the-venue vs seller-of-the-venue-software. Joint review recommended when that leaf is processed.
3. **vs Classifieds Platform (§05.03, processed):** classifieds = self-published time-bound ads, contact and payment off-platform, no recorded engagement or settlement. The load-bearing test is property 5: strip platform-mediated settlement and the recorded engagement → classifieds. Consistent with the classifieds pass's own boundary evidence.
4. **vs vertical service marketplaces (§29 Home/Babysitting/Beauty/Local Service; §26 Food Delivery/Tour; §08 Insurance; §27 Brand-Creator; §18 Load Board; §09 Internal Talent; §25 Volunteer):** domain-structured siblings — same skeleton, domain-specific supply structuring, eligibility rules, and lifecycle machinery (the babysitting/beauty/artist-booking precedents). No change proposed.
5. **vs Appointment Scheduling Application (§03.09) / Appointment-based Service Business Management (§29, processed):** those center one operator's bookable offerings; there is no provider population and no cross-provider competitive selection. Removing the marketplace selection (property 3) collapses into those Types.
6. **vs Job Board (§09, processed):** job boards broker employment applications without platform-mediated engagement settlement; freelance/contract marketplaces record per-engagement contracts with escrowed payment. Fiverr/Upwork sit on this side.
7. **vs Internal Talent Marketplace (§09, processed):** that Type matches employees to internal opportunities inside one organization — no external independent providers, no external settlement.
8. **Lead-gen pole risk:** some local-services products monetize by selling quoted leads rather than hosting settlement; if demand-side intake exists but the engagement/settlement does not occur on the platform, the product drifts toward lead generation/classifieds. (Thumbtack is commonly described this way in market commentary, but no claims are made here — evidence limitation recorded.)

## Historical / Market-Sample Check

- Would older or differently positioned products fit? Web-era predecessors (pre-mobile local-services booking sites, early freelance job boards that moved payment on-platform) satisfy all five defining properties; nothing in the core requires mobile apps, instant matching, GPS work areas, background-check badges, or AI features (all L2). The core also survives removal of reviews themselves — a venue could operate on curation alone, though every sampled mature product has them (hence reviews are L1, not L0).
- The definition does not assume any particular payment instrument (card/wallet/bank) or currency; only that settlement is platform-mediated.
- Providers-as-independent-contractors is the market norm in the sample; the core requires independence and external participation, not any particular employment-contract doctrine (platform-labor regulation varies by jurisdiction and was not researched as legal fact).
- Verification: none of the five properties is tied to a single era, region, or vendor pattern. Historical check passes.

## Uncertainties

1. Thumbtack's actual mechanics (quote model, lead-based monetization) were not directly observed; the request/offer pole rests on Airtasker/Upwork/Fiverr-brief evidence. No canonical claim depends on Thumbtack.
2. Marketplace Platform (§05.02) is unprocessed; the venue-vs-builder seam is asserted from industry naming conventions, not from that leaf's research.
3. Whether the freelance/digital-services cluster deserves its own leaf if §05.02 is ever split — recorded as a taxonomy question, not decided here.
4. Provider payment share/timing varies by product and plan; canonical document states the hold/settle structure without percentages.
5. Legal characterization of provider relationships (contractor classification regimes) varies by jurisdiction; treated as out of scope.

## Final Synthesis

A Service Marketplace is an operator-run two-sided venue where many independent service providers publish their offerings as discoverable supply, customers make the matching decision on the platform (browsing a catalog, or broadcasting demand that providers answer with offers), the resulting engagement is recorded as a lifecycle-bearing unit binding the parties and its terms, and money for the engagement is settled through the platform under anti-leakage rules — with reputation, verification, dispute, and provider-earnings machinery surrounding that core.
