# Research Notes — Coaching Commerce Platform

Research date: 2026-09-07
Slug: coaching-commerce-platform
Directory leaf: Coaching Commerce Platform (§27 Media, Entertainment, Creator & Culture — creator-economy cluster)

## Research Goal

Understand what a Coaching Commerce Platform actually is as an Application Type: what a coach sells through it, how a sale happens, what a purchase converts into, and how the platform tracks fulfillment — then separate the defining structure from common mature structure, variants, and vendor-specific detail.

## Initial Boundary

Hypothesis before research:

- Core use: coaches (life, business, executive, health, career, fitness) package coaching into sellable offers and sell them online — checkout, scheduling, client management.
- Primary users: solo coaches; secondary: multi-coach firms, clients.
- Nearest Types: Creator Course Commerce Platform (content products), Creator Storefront (generic goods), scheduling/booking tools (Calendly-class), coaching management software (delivery-first), freelance service marketplaces, therapy practice management.
- Main unknowns: exact offer structures; how scheduling attaches to purchase; whether client management is definitional or common; marketplace vs standalone posture; how the creator-economy positioning relates to the broader "coaching software" market category.

## Research Questions

1. What is the sellable object (offer/package/program/subscription) and what can it contain?
2. How does checkout work, and in what order do scheduling / contract / intake / payment occur?
3. What does a purchase convert into (session credits, program access, subscription period)?
4. What client-side surfaces exist (sales page, checkout, client portal)?
5. What client management does the platform keep (notes, files, history, forms)?
6. What payment models exist (one-time, installments, subscription, coupons, B2B invoicing)?
7. Where does content delivery fit relative to live coaching?
8. How do multi-coach / B2B variants change the model?
9. Where are the boundaries vs course commerce, storefronts, booking tools, practice management?

## Representative Products

| Product | Why selected | Positioning observed |
|---|---|---|
| Paperbell | Dedicated coaching-commerce product; commerce-first philosophy; solo coaches | "the simple way to sell coaching online" — website + packages + scheduling + payments |
| CoachAccountable | Delivery/engagement-first philosophy; solo → organizations; since 2012 | "coaching results happen BETWEEN sessions"; engagements, courses, groups, Team Edition |
| Delenta | Multi-coach / scale posture; marketplace-style; enterprise | "coaching management platform helps you scale"; 5–500+ coaches; HR dashboard |
| Simply.Coach | All-in-one; solopreneur → enterprise/universities; India-based (regional breadth) | "digital coaching platform" for coaches, therapists, counsellors, consultants, trainers |

Rejected/considered: Practice (practice.do — 404 twice, abandoned), Kajabi coaching product page (404 twice, abandoned as boundary evidence), TrueCoach/Trainerize (fitness vertical — noted as variant from secondary knowledge only, not fetched; not used for claims).

## Sources

Tier 1 (official operational documentation):

- Paperbell Support / Help Center — https://paperbell.com/support/
  - "Packages" — https://paperbell.com/support/knowledge-base/packages/
  - "The Client's Guide to Paperbell" — https://paperbell.com/support/knowledge-base/the-clients-guide-to-paperbell/
- Paperbell product pages (Tier 2): https://www.paperbell.com/ , https://paperbell.com/coaching-software/
- CoachAccountable homepage + Product Tour (Tier 2, incl. full feature checklist): https://www.coachaccountable.com/ , https://www.coachaccountable.com/tour
- Delenta homepage (Tier 2): https://www.delenta.com/
- Simply.Coach homepage + Business Management page (Tier 2): https://simply.coach/ , https://simply.coach/business-management/

Source-access limitations:

- practice.do returned 404 on both www and apex (2 attempts) — abandoned; Practice not used for any claim.
- kajabi.com/products/coaching and kajabi.com/coaching returned 404 (2 attempts) — abandoned; the "course platform adds a coaching product" boundary is reasoned from the sampled products' own content-delivery features instead of Kajabi evidence.
- Delenta and Simply.Coach evidence is Tier-2 (product/marketing pages), not help-center articles; claims from these two are held at "product pages state…" strength and not used for precise operational rules.
- No numeric limits, prices, or time windows from Delenta/Simply.Coach/CoachAccountable are asserted in the final document; Paperbell-specific numbers stay in these notes.

## Product A — Paperbell

Evidence layer: A (direct observation, Tier-1 help articles + Tier-2 product pages).

### Key observations

- **Package = the sellable offering.** "Paperbell packages are the offerings that you sell to your clients." A package can include: 1:1 appointments (a count of sessions with set lengths), group sessions / live online classes (coach-scheduled, all package holders auto-invited), digital downloads/content, or any combination.
- Package templates at signup: Free Discovery Call, one-time Breakthrough Session, Payment Plan, Subscription, Group Coaching, Digital Download, Online Course.
- Package status: Active / Invite-only (live but unlisted, shared by direct URL) / Draft / Expiry Date. Archive keeps existing clients booking remaining appointments and receiving emails/SMS/surveys.
- **Appointments are session credits**: "The number of appointments you set here is the number of appointments clients with this package can book with you." Mixed lengths allowed; clients book them in the order listed.
- **Pricing structures**: One Time Payment; Monthly Subscription (Stripe only — "sessions per month", auto-billed until client cancels in-product); Payment Plan / installments (fixed number of charges; weekly/biweekly/monthly/bimonthly/quarterly frequencies). Multiple prices per package (e.g., pay-in-full discount); coupons (including 100%-off as free grant); optional set-up fee.
- **Checkout flow is configurable**: "book appointment first" (recommended, so the client checks availability before paying) vs "Purchase → Book appointment". "If you're attempting to purchase a paid package your appointment will not be secured until you've completed checkout including payment."
- Purchase limit: cap the number of buyers (e.g., group program seats).
- Per-package auto-generated landing page: cover image, short description, description, features list, testimonials, FAQs; plus package-level schedule link and embeddable booking calendar.
- **Contract gating**: "When you add a contract, your clients will be required to sign before they can complete their purchase" (DropBox Sign e-signature).
- **Surveys/intake forms**: package-specific, triggered at defined points (e.g., intake, post-session, exit); answers appear on the client profile.
- **Automated emails** with triggers: appointment, group session, purchase, reminder-to-book, final appointment. Package-specific.
- **Content delivery**: files/links to the client portal; package-wide or private (single client); drip-feed over time; can be sold standalone as digital downloads.
- **Client portal** (PaperbellClient.com): Overview (upcoming appointments, content, surveys), Appointments (book/reschedule/cancel), Content (incl. client uploads back to coach), Surveys, Purchases (billing details, cancel subscription, buy again), Profile (email/phone/timezone/photo), SMS reminders (verify phone; reply STOP to opt out). Passwordless login via email one-time code.
- Client-side rules: <24h before appointment → no self-serve cancel/reschedule; subscription cancellation keeps appointments before the renewal date and auto-cancels those after; payment plans cannot be self-cancelled; refunds handled by the coach.
- Payments via the coach's own Stripe/PayPal; "Paperbell adds zero additional transaction fee, and we never hold or even touch your earnings."
- Integrations: Zoom/Meet (meeting links auto-attached), Google/Outlook/Apple calendars, Zapier; scheduling features of "dedicated scheduling tools" (buffers, automatic time-zone translation).
- Coach site at paperbell.me/yourname; positioning: replace "Calendly plus DocuSign plus checkout"; link-in-bio from social; discovery sessions; gift a package.

## Product B — CoachAccountable

Evidence layer: A for homepage/tour content (Tier-2 official, detailed feature checklist); no help-center fetch.

### Key observations

- Philosophy: delivery/engagement-first — "Coaching Results Happen BETWEEN Sessions"; the platform's differentiators are Actions, Metrics, Session Notes, Worksheets, Courses — with commerce built in ("go from brand-new customer to selling coaching on your website in under 3 minutes").
- **Offerings**: "Package your coaching in an easy-to-buy format… Sell coaching directly from your own website (or your social media, or your email newsletter…) from start to finish, including appointment scheduling, intake forms, and payment." Embeddable booking widget; prospective clients can book exploratory calls.
- **Engagements**: "Manage client engagements and coaching packages… see at a glance how many sessions or days a client has remaining; automatically invoice and bill on schedule; updates on engagement progress are automatically sent to you and your clients." → the purchase converts into an engagement with a session/day budget.
- **Invoicing & Payments**: one-time and recurring invoices; automatic recurring billing; memberships & subscriptions; installment billing; company billing; unpaid invoice lockout; Packages. Processed through the coach's own Stripe/Square/PayPal ("no additional processing fees").
- **Agreements**: rich documents with signature/initial areas, timestamp + IP capture, tamper prevention, organized record of agreements on file.
- Scheduling: self-schedule or coach-scheduled; individual + group sessions; recurring appointments; pre/post-session worksheet assignments; SMS/email reminders (SMS in US/CA/UK/AU); calendar sync (Google/Outlook/iCal), .ics invitations; Zoom integration.
- Client management: private & shared notes, action plans, metrics/KPI tracking, activity history, CSAT, digital contracts, company management.
- **Companies**: organize clients by company; invoice organizations rather than individuals; company-wide engagements; personnel (client-side stakeholders) with their own access.
- **Team Edition**: coaches/administrators/personnel roles, customizable access roles, master-coach permissions, coach–client pairing, oversight, shared resources/templates; coaching hours log; coach engagement reports.
- Courses: self-paced or calendar-based, group courses, content drip sequences, onboarding task automation; Groups with shared actions/metrics/projects.
- Client portal: branded; clients log in from the coach's website (white-labeled login widget); installable home-screen app; mobile web workspace.
- Posture: no AI/ML, no outside investment, GDPR compliant (not HIPAA), data export, API + Zapier; platform billed monthly by active-client count.

## Product C — Delenta

Evidence layer: A for homepage content (Tier-2 official); no help-center fetch; claims held at "product pages state…" strength.

### Key observations

- Positioning: "coaching management platform helps you scale — grow revenue, cut admin, empower your coaches"; audiences: solopreneurs (coaches/consultants/trainers/therapists), teams, enterprise (5–500+ coaches).
- Feature set (nav): Client Management (CRM), Client Portal, Sessions & Bookings, Group Coaching, Sales & Payments, Course Management, Landing Page, Multi-Coach Teams, AI Note-Taker.
- **Sales & Payments**: "Client Onboarding & Checkout"; Subscription & Payments — "automatic billing & renewals with reminders; session tracking — both coach & client see usage at a glance; roll-over unused sessions for active members"; Digital Contracts; intake forms; branded landing pages; branded booking calendar; leads via customizable forms.
- **Multi-coach / marketplace**: "Create your own marketplace — connect your associates and services with every client in one centralized platform"; curate coaching team under one brand; showcase each coach's expertise; clients book discovery sessions directly; track billable/non-billable hours; pay-per-coach rates and real-time earnings dashboards; coaching logs & CPD.
- Enterprise: HR dashboard for B2B sponsors; real-time dashboards on coach activity, client usage, program progress; white-label/branded portals; reports exportable across clients, sessions, financials.
- Specialties listed: career, executive, health & wellness, ADHD, life, coaching consultancy, not-for-profit, fitness, training/certifications.
- Integrations: Zoom, Stripe, Google "and many more"; iOS/Android apps; GDPR/ISO/HIPAA badges claimed on site.

## Product D — Simply.Coach

Evidence layer: A for homepage + business-management page (Tier-2 official); no help-center fetch; claims held at "product pages state…" strength.

### Key observations

- Positioning: "digital coaching platform" for coaches, therapists, counsellors, consultants, trainers; audiences: solopreneurs, multi-coach businesses, L&D teams, universities.
- **Subscriptions & Session Packages**: "create ready-to-view session packages and allow users to buy them or subscribe to them — complete with payment gateway integration."
- **Showcase Page**: branded landing page — profile, credentials, testimonials, contact form, appointment scheduling for prospective clients; lead-generation touchpoints.
- **Prospect Management**: leads from the Showcase Page logged as prospective clients; automation tracks likelihood of converting to paying customers.
- **Journeys**: reusable program templates — "map any coaching/therapy/training methodology onto a reusable program template… provide service at scale."
- **Contracts**: templates (incl. ICF-specification contracts for coaches), digital signatures both ways, per-client contract storage.
- **Invoicing & Payments**: send/store invoices, accept & track payments from one module.
- Client management: goals & development planning, action plans, notes, forms, nudges, scheduling ("multiple calendars, time zones, minute availability settings, time buffers"), client workspaces, resource library, team engagements, coach matching, stakeholder integration.
- Embedded video conferencing (Zoom, Google Meet, Microsoft Teams); CPD log toward credential renewal; email/contact management; SOC2/HIPAA/GDPR compliance claims.

## Cross-product Comparison

| Structure | Paperbell | CoachAccountable | Delenta | Simply.Coach | Layer |
|---|---|---|---|---|---|
| Sellable offer object | Package (1:1 appts + group sessions + downloads) | Offerings / Packages → Engagements | Packages & subscriptions (Sales & Payments) | Session Packages + Subscriptions (+ Journeys as program template) | **L0** |
| Self-serve purchase (checkout) | Book-first or pay-first flow; payment secures appointment | Sell "from start to finish" incl. scheduling, intake, payment | Client onboarding & checkout | Buy/subscribe with payment gateway | **L0** |
| Purchase → tracked engagement | Appointment credits in package; expiring packages | Engagement with sessions/days remaining; auto-billing on schedule | Session tracking, both sides see usage; rollover | Session packages; subscription periods | **L0** |
| Public sales surface | Auto-generated per-package landing page + coach site | Embeddable widget; sell from own site/social | Landing pages; branded booking calendar; team marketplace page | Showcase Page with scheduling + contact form | L1 |
| Scheduling of sessions | Client self-schedule; buffers; timezones | Self- or coach-schedule; recurring; group sessions | Branded booking calendar; discovery sessions | Multi-calendar smart scheduling; buffers | L1 |
| Client portal | Yes (passwordless) | Yes (branded, login from coach site) | Yes (branded/white-label) | Client workspace | L1 |
| Contracts / e-sign | Required pre-purchase if configured | Agreements (timestamp + IP) | Digital contracts | Digital signatures; ICF templates | L1 |
| Intake forms / surveys | Package-specific, triggered | Pre/post-session worksheets; intake | Intake forms | Forms; intake | L1 |
| Client management | Notes (private/shared), purchase & appointment history | Notes, action plans, metrics, activity, CSAT | Notes, goals, tasks | Goals, action plans, notes, reports | L1 |
| Content delivery | Files/links, drip, private vs package | Worksheets, courses (drip), resource library | Course management, resources | Resource library; Journeys | L1 |
| Group coaching | Group sessions in package, auto-invite | Groups (shared actions/metrics/projects) | Group coaching | Team engagements | L1 |
| Discovery/intro offer | Free discovery package template | Prospects book exploratory call | Clients book discovery sessions | Prospect management + scheduling | L1 |
| Payment models | One-time, subscription, installments; coupons; setup fee | One-time, recurring, memberships, installments, company billing | Subscriptions, auto-renewal | Buy or subscribe; invoicing | L1 |
| Payment rails | Coach's own Stripe/PayPal; no platform fee | Coach's own Stripe/Square/PayPal; no extra fee | Stripe (stated) | Payment gateway (stated) | L1 |
| Video integration | Zoom/Meet | Zoom/Teams/Meet | Zoom | Zoom/Meet/Teams embedded | L1 |
| Reminders | Email + SMS | Email + SMS (regional) | Reminders | Nudges/reminders | L1 |
| Multi-coach roles | No (solo-focused) | Team Edition (coaches/admins/personnel) | Multi-coach teams; marketplace; payroll | Multi-coach businesses; coach matching | L2 |
| B2B / sponsor side | No | Companies (invoice org; company engagements) | HR dashboard; B2B sponsors | Stakeholder integration; L&D/HR reporting | L2 |
| Vertical breadth | Coaching/consulting | Life/business/health/relationship/career/team | Career/exec/health/ADHD/life/fitness/NFP | Coaches/therapists/counsellors/consultants/trainers | L2 |
| White-label depth | Site branding | Branded portal + login widget | White-label onboarding | Branded showcase | L2 |
| Distinctive extras | Gift a package; invite-only offers; drip content | Unpaid-invoice lockout; no-AI stance; CSAT | AI note-taker; coach earnings/payroll; rollover | Journeys builder; CPD log; coach matching | L3 |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

A Coaching Commerce Platform is recognizable only if all three hold:

1. **Coach-defined productized coaching offer** — the coach packages coaching (sessions, a program, an ongoing service) into one or more sellable offers with price and purchase options. The catalog is the coach's, not a marketplace's (marketplace posture is a variant).
2. **Client-side self-serve purchase** — a prospect can buy an offer directly through the platform (checkout with payment via integrated processors), and the purchase is what converts a buyer into a client.
3. **Purchase converts into a tracked coaching engagement** — the sale creates a fulfillment structure the platform tracks and consumes: bookable session credits, program access, or a subscription service period. The platform knows what was sold, what remains to be delivered, and what was delivered.

Remove #1 → generic invoicing/payment-link tool. Remove #2 → coaching management software without commerce. Remove #3 → a storefront/landing-page builder that happens to list coaching. Remove the coaching subject matter and only the generic structure remains (service booking / digital product commerce).

### L1 — Common Mature Structure

Present in all four sampled products; expected in mature products but not definitional:

- public sales surface (coach site / per-offer landing page / showcase page) with booking entry points
- session scheduling bound to availability (buffers, time zones, calendar sync, video-conferencing links)
- client portal (client-facing home: book, content, purchases, profile)
- contracts / e-signature inside the purchase or onboarding flow
- intake forms / surveys triggered at lifecycle points
- client management: notes, purchase & appointment history, files
- content/resource delivery (worksheets, files, drip; sometimes full courses)
- group coaching / cohort sessions
- discovery/consultation offer as a standard acquisition mechanism
- payment models: one-time, installments/payment plans, subscriptions/memberships; coupons/discounts
- automated reminders and lifecycle emails (appointment, reminder-to-book, purchase)
- session credit / usage tracking visible to coach and client

### L2 — Variant / Optional Structure

- operator scale: solo coach → multi-coach firm (roles, coach–client pairing, oversight) → enterprise/marketplace (coach profiles under one brand, coach matching, payroll/earnings, sponsor dashboards)
- buyer side: B2C self-serve vs B2B (company billed, personnel/stakeholder access, HR/L&D reporting)
- vertical: life/executive/career/health/ADHD/relationship coaching; fitness coaching (program-delivery emphasis); adjacent professionals (therapists, counsellors, consultants, trainers) on the same structure
- delivery style: live scheduled sessions vs program/course-based vs (in some products) async support; content-only offers (digital downloads) sold alongside coaching
- commerce posture: standalone dedicated product vs module inside a broader creator/education platform
- fee posture: flat SaaS fee with coach-owned payment rails (no platform cut) vs marketplace-style intermediation
- white-label/branding depth; regional compliance postures (GDPR/HIPAA claims vary by product)

### L3 — Vendor-specific (research notes only)

- Paperbell: appointments bookable in listed order within a package; <24h self-cancel lockout; subscription cancellation keeps pre-renewal appointments and auto-cancels later ones; payment plans not self-cancellable; passwordless client login; gift-a-package; invite-only package status; $57/mo price point and 30-day refund (marketing page, 2026-09-07); "no transaction fee" posture.
- CoachAccountable: unpaid-invoice lockout; agreement timestamp + IP capture; CSAT reporting; coaching hours log; explicit no-AI/no-ML stance; platform priced by active-client count; "Terms of Awesome".
- Delenta: AI note-taker; HR dashboard for sponsors; pay-per-coach rates and earnings dashboards; rollover of unused sessions; marketplace builder.
- Simply.Coach: Journeys (reusable program templates); CPD log for credentialing; ICF-specification contract templates; coach matching; stakeholder integration; "coming soon" email/LinkedIn integrations.

## Vendor-specific Findings

See L3 above. Cross-product vendor-neutral observations worth keeping:

- All four products let the coach connect their own payment processor account; three explicitly advertise "no additional platform transaction fee" (Paperbell, CoachAccountable; Delenta/Simply.Coach do not state a cut either way on fetched pages — do not generalize beyond "integrated processors").
- All four treat the **session credit** as the bridge between commerce and delivery: the offer defines a quantity of sessions (or a period), the purchase grants it, scheduling consumes it, and both sides can see the balance.
- All four bundle contract e-signature and intake forms into the purchase/onboarding flow rather than leaving them to external tools.

## Boundary Findings

- **vs Creator Course Commerce Platform**: a course is a content product consumed self-serve; coaching is a human service delivered through scheduled personal time / an ongoing relationship. The seam is what the purchase converts into: content access vs a tracked coaching engagement. Coaching platforms commonly include content delivery (drip, worksheets, even courses), and course platforms commonly add a coaching product type — so the boundary is drawn on the fulfillment structure, not on feature presence. Remove the human-service engagement and this Type becomes course commerce.
- **vs Creator Storefront / Digital Product Commerce**: storefronts sell goods/downloads with no service-fulfillment structure. A coaching platform can sell digital downloads too (Paperbell does), but its defining loop is offer → purchase → engagement.
- **vs Scheduling / booking tools (Calendly-class, appointment scheduling)**: booking is a capability inside this Type. A pure scheduling tool has no coach-owned offer catalog, no checkout, no client engagement record. Remove checkout + engagement and this Type collapses into a booking tool.
- **vs Coaching Management Software (delivery-first)**: same market, different emphasis. The sampled set spans the spectrum (Paperbell commerce-first → CoachAccountable delivery-first), and every product does both loops. The directory has a single leaf here, so the Type is defined by the commerce loop (offer → checkout → engagement) with delivery management as the standard companion structure. No separate directory leaf exists for delivery-only coaching software; not flagged as a taxonomy error, but the emphasis spectrum is recorded.
- **vs Therapy / clinical practice management**: structurally adjacent (same objects: clients, sessions, notes, billing); the seam is the professional discipline and regulatory posture, not the structure. Two sampled products explicitly serve therapists/counsellors on the same structure — recorded as a variant, not a separate Type.
- **vs Freelance service marketplaces / generic appointment-with-payment**: generic services lack the coaching-specific engagement structure (packages of sessions, session credits, ongoing relationship artifacts: contracts, intake, notes, goals). A marketplace posture (Delenta) is a variant of this Type, not a different one.
- **vs Paid Community / Fan Membership / Creator Subscription**: those sell access to a community/content stream; this Type sells human coaching time and tracks its delivery.
- **Directory-context note**: the leaf sits in the creator-economy cluster, but the market category the products occupy is usually called "coaching software / coaching management platform" and is dominated by professional coaches (executive, life, health) rather than social-media creators. The creator-coach (selling to a social audience via link-in-bio) is one customer posture (Paperbell markets exactly this), not the whole Type. The defining structure is identical; recorded here so the final document does not overfit to the creator framing.

## Historical / Market-Sample Check

- Would older products fit? CoachAccountable (founded 2012) already exhibits the full L0 loop (offerings → purchase → engagements). Pre-platform coach workflows (Calendly + PayPal + email + Word contracts) are exactly the fragmentation this Type integrates — they are not instances of the Type, which supports an integration-based definition.
- Would regional / vertical products fit? Simply.Coach (India-based) and Delenta (UK/international) fit unchanged. Fitness-coaching platforms (program-delivery emphasis) fit the L0 via the "engagement" abstraction (program access instead of session credits) — noted as variant, not verified by direct fetch.
- The definition does not depend on: phone/link-in-bio acquisition, subscription billing, content drip, group coaching, multi-coach roles, or any specific payment processor. All are L1/L2.

## Uncertainties

- Delenta and Simply.Coach evidence is Tier-2 (product pages); operational rules (e.g., exact checkout ordering, cancellation mechanics) were not verified for them and are not claimed.
- CoachAccountable's checkout ordering (schedule-first vs pay-first) was not observed in fetched pages; only that offerings sell "from start to finish, including appointment scheduling, intake forms, and payment."
- The fitness-coaching vertical (TrueCoach/Trainerize class) was not fetched; its inclusion as a variant rests on the L0 abstraction, not direct evidence.
- Marketplace-style coaching platforms (e.g., coach directories with built-in commerce) were not sampled; the marketplace posture is evidenced only through Delenta's "create your own marketplace" positioning.
- Refund mechanics, tax handling, and payout timing were not researched in depth; only Paperbell's "refunds handled by the coach" client-side rule was directly observed.

## Final Synthesis

A Coaching Commerce Platform is the coach-side system of record for selling coaching: the coach defines productized offers (sessions, packages, programs, subscriptions); prospects buy them self-serve through a public sales surface and checkout (often gated by contract and intake); each purchase converts into a tracked coaching engagement — session credits to book, program access, or a subscription period — whose consumption (scheduled and delivered sessions) the platform records for both coach and client. Around this loop, mature products add scheduling, client portals, client management, content delivery, group coaching, reminders, and payment-option breadth; scale and buyer-side (B2B) variants add multi-coach roles, coach matching, sponsor reporting, and marketplace posture. The Type is bounded from course commerce by what a purchase converts into (human service engagement vs content access), and from booking tools by the presence of the offer catalog, checkout, and engagement record.
