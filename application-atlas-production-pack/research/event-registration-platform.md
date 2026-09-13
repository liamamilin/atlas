# Research Notes — Event Registration Platform

## Research Goal

Understand what an Event Registration Platform is as an Application Type: what objects exist inside it, what the organizer does with them, how the intake flow works from offer to roster, where money/capacity/tickets sit (definitional vs common), and where the Type's boundary sits — above all against the Event Management Platform (the thinnest seam, flagged for joint review by the EMP pass), and against Event Ticketing Platform, Online Form Builder, Attendee Management, Digital Waiver Management, and Camp Management System (all flagged from prior passes).

## Initial Boundary

Working hypothesis before research:

- Core use: organizer-side software whose center is the sign-up intake — people register for an event through the platform's pages/forms, pay if applicable, and the output is a managed roster of registrants.
- Primary users: event and program organizers (conferences, nonprofits, races, camps, classes, community groups); registrants are the consumer-facing side.
- Nearest neighbors: Event Management Platform (broader — full event lifecycle), Event Ticketing Platform (ticket-as-inventory center), Online Form Builder (intake without event/roster machinery), Attendee Management (roster slice, processed), Event Agenda Management (program center, processed), Appointment/Meeting Scheduling (calendar-slot center), Course Registration System (education enrollment, separate leaf), Camp Management System (camp-operation layer, processed), Digital Waiver Management (waiver loop, processed), Restaurant Reservation Platform (table-inventory booking).
- Known unknowns: is payment definitional? Is capacity definitional? Is the ticket artifact definitional? Can registration exist for multiple occurrences (sessions/programs)? What roster operations are standard? Where exactly does the platform end and the EMP begin?

## Research Questions

1. What is the central object — the event, the registration offer, the registrant record, or the form?
2. What does the intake flow look like end-to-end (offer → page → form → payment → confirmation → roster)?
3. Is money/ticketing definitional or common? What direct evidence exists for registration without tickets/payment?
4. How are admission options modeled (ticket types, registrant types, pricing tiers, sessions)?
5. How is capacity handled (caps, spot tracking, waitlists, holds)?
6. What roster operations exist post-registration (edit, cancel, transfer, defer, refund, communicate, export, check-in handoff)?
7. How deep does information collection go (custom questions, conditional logic, waivers, documents)?
8. What does the platform NOT do (promotion? agenda? onsite? apps?) — boundary vs EMP.
9. Which poles exist (pure-play design-led, program registration, vertical endurance, marketplace, meeting-specialist, nonprofit-free)?
10. Historical check: do paper-era and platform-native sign-up practices fit the proposed core?

## Representative Products

Selected for market representation, documentation availability, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Evidence quality |
|---|---|---|---|
| RegFox (Webconnex) | pure-play, design-led registration platform | SMB→mid (conferences, camps, education, faith-based) | product home + attendee-management feature page directly fetched (Layer A) |
| RunSignup | vertical endurance-event registration platform | race directors/timers (vertical) | product home + registration product page directly fetched (Layer A) |
| Eventbrite | consumer marketplace with first-class registration mode | SMB/creator | help-center article directly fetched this pass + prior-pass help articles (Layer A) |
| rsvpBOOK | meeting/conference registration specialist expanding into EMP | corporate/association meetings | product home + registration product page directly fetched (Layer A) |

Abandoned samples (network rule): Regpack (program-registration pole — regpacks.com returned 403 twice); Zeffy (nonprofit free-platform pole — timeouts twice).

## Sources

- RegFox — product home: https://regfox.com/ ; attendee-management feature page: https://regfox.com/features/attendee-management (fetched 2026-09-07)
- RunSignup — product home: https://runsignup.com/ ; registration product page: https://info.runsignup.com/products/registration/ (fetched 2026-09-07)
- Eventbrite — Help Center, "How to set up an event that doesn't require PDF tickets (registration only)": https://www.eventbrite.com/help/en-us/articles/250995/how-to-set-up-an-event-that-doesn-t-require-tickets-registration-only/ (fetched 2026-09-07); plus prior-pass (2026-09-07) Eventbrite help articles recorded in research/event-management-platform.md (create-an-event flow, capacity, order machinery)
- rsvpBOOK — product home: https://rsvpbook.com/ ; registration product page: https://rsvpbook.com/event-registration-software.php (fetched 2026-09-07)
- Sibling docs consulted for boundary alignment: research/event-management-platform.md, research/attendee-management.md (via EMP doc), research/digital-waiver-management.md, research/camp-management-system.md, STATUS.md boundary entries

Source-access limitations:

- Regpack (regpacks.com) and Zeffy (zeffy.com) unreachable (403/timeout, two attempts each, abandoned per network rule). The dedicated program-registration pole (camps/classes with payment-plan machinery) and the free-for-nonprofit business-model pole are therefore evidenced only indirectly (RegFox payment plans + camp/class industry pages; RunSignup free-event FAQ).
- Deep operational help-center knowledge bases were fetched only for Eventbrite (one registration-mode article this pass; more in the prior EMP pass). RegFox, RunSignup, and rsvpBOOK evidence rests on official product/feature pages (marketing layer) — precise operational defaults, limits, and state names are not asserted anywhere in the final document.
- All sampled products are US-market. Regional registration products (e.g., Europe/Asia) were not sampled; claims are kept implementation-neutral accordingly.

## Product Observations

### RegFox (Webconnex) — evidence layer A (product pages)

- Self-label: "The #1 Most Affordable Event Registration Platform … a powerful event registration platform for conferences, workshops, camps, classes, and more."
- Intake construction: "Real View Page Builder" (drag-and-drop registration page, no code), Branding Control (page matching organizer's brand/fonts/colors), Conditional Logic ("create attendee workflows, require custom questions, and set dynamic pricing").
- Session Management: promote breakout sessions with pictures, descriptions, and a reservation system (registrants reserve sub-events).
- Admission/pricing machinery: coupon management (unlimited codes), convenience-fee control, payment plans (installments, balance auto-captured), pre-registration with card on file (register now, charge later), offline payment methods (mail-in check logged in the system), in-house payment processing, fast event payouts, purchase protection (registrant-funded refund-if-cannot-attend upgrade).
- Capacity machinery: waitlists per registration option that "automatically capture sales when spots open up".
- Group machinery: group registrations "for groups of any size".
- Data collection: digital release waivers (integrated signatures within the event page), required custom questions, add-ons & upgrades (merch/experiences sold during registration).
- Access control: restricted access ("limit online registration to specific attendees who authenticate themselves first").
- Roster operations (attendee-management page): "Edit any registration — make any change to any attendee without re-registering or canceling them" (explicitly contrasted with other registration platforms that force cancel-and-re-register); partial charge or refund "when attendee changes modify the total price due" (charge/refund card on file, override totals, free upgrades); refunds/cancellations as full refund, partial refund, or coupon-code credit for a future event; search/sort/filter attendees by event, status, date, type; instant exports (Excel/CSV, memorized exports auto-emailed); "when you make changes to attendees, all financials and inventories are automatically updated too."
- Communication: text messaging to attendees from the account; confirmation letters and reminders (customer quote).
- Onsite handoff: check-in app (scan/look up), badge printing (on-demand, mass, export), Mobile Pay Pass (onsite cashless payments).
- Adjacent modules: Event CRM (contacts/leads/attendees/vendors), Engage attendee app, membership management (sell/validate memberships), continuing education (CEUs/CECs), event fundraising, virtual events, marketing ad designer, social media tools, real-time analytics, exports/reports, integrations, fraud prevention, user access controls (unlimited admins/editors/users).
- Pricing model (L3 detail): per-paid-registrant fee (99¢ + 1%, capped at $4.99) — recorded as positioning, not asserted in the final document.
- Industries marketed: conferences/corporate, event agencies, education/trainings, higher education, retreats/workshops, faith-based, many camp sub-verticals.

### RunSignup — evidence layer A (product pages)

- Self-label: "all-in-one platform for endurance events … from registration through RaceDay"; registration page headline: "Race Registration Software that Makes Registering Easy & Running Your Event Even Easier — Registration Built for Race Directors, Not Just Registrants"; pillars: Simple & Advanced Registration, Participant Management, Flexible Information Collection, Secure Payment Processing.
- Setup: Race Wizard — guided step-by-step setup "for anything from a simple one-course race to a multi-day, multi-course event"; race dashboard; "no technical background required."
- Participant management: self-serve participant-initiated transfers (to another race), deferrals, and waitlist management; "admin controls so you decide what participants can (and can't) do themselves"; participant info changes configurable with a cutoff date; access sharing — "control what each team member and timer can see and edit" (timers are a distinct partner role in the endurance ecosystem).
- Pricing machinery: early-bird with automatic price increases by date or registration count; group/team/age-based/membership discounts; unlimited coupon codes; automated referral rewards; event tiles & bundles (register for multiple events at once).
- Capacity machinery: participant caps "by event or across events, with real-time spot tracking."
- Information collection: multiple-choice and open-ended custom questions; "up to three waivers per event, collected and saved digitally"; sensitive-data options; race notifications with customizable from-name.
- Payments: PCI Level 1 compliant processing; processing fee on paid registrations (usually covered by participants); "free events are entirely free to run" — direct evidence free registration is a first-class mode.
- Event-day handoff: RaceDay CheckIn App (QR scan or search at packet pickup), RaceDay Scoring (results), RaceJoy GPS tracking, photo platform — the vertical's onsite layer.
- Included marketing layer: free website per event, free email marketing (unlimited contacts/sends), RaceInsights analytics.
- Event types served: runs/races, walks, ultras, triathlons, cycling, swim, turkey trots, kids events, virtual/hybrid, trail, corporate team events, paddle, ski/snowshoe, gravel, obstacle, stair climbs.
- Adjacent products in same company: Memberships (running clubs), Ticket Events product, peer-to-peer fundraising; separate sibling brand TicketSignup for ticketed events (case study: a zoo uses RunSignup for its race and TicketSignup for its ticketed events) — evidence the company itself splits registration vs ticketing across brands.
- Discovery: "Find a Race" directory — a light marketplace surface in the vertical.

### Eventbrite — evidence layer A (help articles; this pass + prior EMP pass)

- Registration-without-tickets is first-class (this pass's article): "If you're hosting an event that doesn't require tickets, turn off PDF tickets" (Event Dashboard → Order Options → Order Confirmation → uncheck "Include printable tickets in all orders"); attendees told they need not show any ticket.
- "By default, free events are registration only. This can't be changed." — the strongest single piece of evidence that payment/ticket artifacts are NOT definitional for registration.
- Paid events can switch event type to "Registration event" (Tickets → Settings → Event type) — "registration" exists as a named event type distinct from ticketed events inside one product.
- Order machinery (prior pass): order form, custom questions, registration time limit, order confirmation emails with custom messages, waivers with registration, add-ons, guest lists.
- Capacity machinery (prior pass): set/restrict total capacity, holds, ticket sections.
- Lifecycle (prior pass): event status changes, scheduled publish, cancel, unpublish/delete, postpone/reschedule, copy event.
- Distribution: event page lives on Eventbrite's consumer marketplace with discovery recommendations — the business-model pole.
- Onsite (prior pass): organizer check-in app with ticket scanning, door sales.

### rsvpBOOK — evidence layer A (product pages)

- Self-label: "Event Management & Registration Software"; tagline: "Registration is only the beginning. Manage sessions, payments, attendee apps, onsite workflows, exhibitor leads, engagement and reporting from one flexible platform."
- Registration page headline: "Event Registration Software Built for More Than a Signup Form — create branded registration paths, collect the right attendee data, manage groups and sessions, take payments and carry the same record into onsite check-in and reporting."
- Registration mechanics: "Different attendee types can follow different paths, answer custom questions, select sessions, join groups or tables, purchase tickets and receive the event information they need. Once registration is complete, the same attendee data can continue into badges, check-in, communications, attendance and reporting."
- Registrant types + custom questions + conditional logic → per-type registration paths; unlimited custom questions (dropdowns, radio sets, uploaded forms).
- Groups and money: group and table registration; ticket sales; discounts and promo codes; payments "while keeping financial and attendee records connected to the event."
- Sessions: "Offer sessions, classes and workshops with capacity controls and keep those choices tied to each attendee for schedules, reporting and onsite attendance."
- Event-day handoff: badges, QR code scanning (Kiosk+), event/session attendance recording, staff access "without rebuilding attendee lists in another system."
- Reporting: built-in and custom reports over registration, sales, attendance; exports.
- Explicit layering toward the sibling Type: "Need the broader event-management platform? Registration is the starting point. rsvpBOOK can also extend into attendee mobile experiences, onsite operations, lead retrieval, gamification and other event-day workflows." — a vendor's own articulation of registration-as-center vs EMP-as-extension.
- Vendor-specific: trade-show prize wheel lead capture; AI-assisted event setup; nonprofit/government discount pricing.

## Cross-product Comparison

| Structure / capability | RegFox | RunSignup | Eventbrite | rsvpBOOK | Layer |
|---|---|---|---|---|---|
| Event as sign-up target with its own registration page | ✓ (page builder) | ✓ (race wizard + race website) | ✓ (event page) | ✓ (branded registration paths) | B |
| Registration form with custom questions | ✓ | ✓ (MC + open-ended) | ✓ (order form + custom questions, prior pass) | ✓ (unlimited, incl. uploaded forms) | B |
| Admission options / registration types with pricing tiers | ✓ | ✓ (tiers, early-bird, age-based) | ✓ (free/paid/donation types; "Registration event" type) | ✓ (registrant types; tickets) | B |
| Payment processing | ✓ (in-house) | ✓ (PCI L1) | ✓ | ✓ | B |
| Free registration as first-class mode | ✓ (fee framed per *paid* registrant) | ✓✓ ("free events are entirely free to run") | ✓✓ ("free events are registration only" by default) | (not surfaced) | B (A for RSU/EB) |
| Capacity / caps with live spot tracking | ✓ | ✓✓ (caps by/across events, real-time spot tracking) | ✓ (capacity + holds, prior pass) | ✓ (session capacity controls) | B |
| Waitlists | ✓ (auto-capture when spots open) | ✓ (self-serve management, customizable text) | ✓ (topic listing, prior pass) | (not surfaced) | B |
| Registrant record operations (edit/cancel/transfer/defer/refund) | ✓✓ (edit-in-place + partial charge/refund + credit) | ✓✓ (transfers, deferrals, self-serve w/ admin gates) | ✓ (cancel/refund policy, prior pass) | (records carried forward; ops not itemized on fetched pages) | B |
| Confirmations & registrant communication | ✓ (confirmations, reminders, SMS) | ✓ (race notifications) | ✓ (confirmation emails + custom messages) | ✓ (communications) | B |
| Reports / exports / analytics | ✓ | ✓ | ✓ (prior pass) | ✓ (built-in + custom) | B |
| Check-in handoff (scan/badges/attendance) | ✓ (check-in app, badge printing) | ✓ (RaceDay CheckIn, packet pickup) | ✓ (organizer app, prior pass) | ✓ (badges, QR kiosk, attendance recording) | B |
| Group/table registration | ✓ (any size) | ✓ (group/team) | (not surfaced) | ✓✓ (groups and tables) | B |
| Waivers collected inside registration | ✓ (integrated digital signatures) | ✓✓ (up to three per event, saved digitally) | ✓ (waivers with registration, prior pass) | (uploaded forms) | B |
| Conditional logic / per-type paths / dynamic pricing | ✓✓ | ✓ (price-increase rules) | (not surfaced) | ✓✓ (registrant-type paths) | B |
| Sessions / sub-events selection | ✓ (session reservation system) | ✓✓ (multi-course/multi-day, bundles) | (not surfaced) | ✓✓ (sessions w/ capacity tied to attendee) | B |
| Marketplace / directory distribution | ✗ | ✓ (Find a Race directory, light) | ✓✓ (defining business model) | ✗ | A |
| Marketing/promotion machinery | ✓ (ads designer, social tools) | ✓✓ (free email/websites, referrals, RaceInsights) | ✓ (ads, email, prior pass) | ✗ | B |
| Fundraising / donations | ✓ (event fundraising) | ✓✓ (P2P fundraising) | (not surfaced) | ✗ | B |
| Membership sell/validate | ✓ | ✓ (clubs product) | ✗ | ✗ | B |
| Attendee app / engagement | ✓ (Engage app) | (RaceJoy tracking) | ✗ | ✓ (attendee app, gamification) | B |
| Onsite extensions (kiosks, cashless, lead retrieval) | ✓ (Mobile Pay Pass) | ✓ (RaceDay suite) | ✓ (door sales) | ✓✓ (Kiosk+, prize wheel) | B |
| Vertical-specific machinery | ✗ | ✓✓ (timing/timer ecosystem, scoring) | ✗ | ✗ (prize wheel for trade shows) | A |

Reading: rows 1–13 are present across the sample → standard mature structure. No sampled product lacks rows 1–5. Rows with ✓✓ concentrated in one product → pole-defining or vendor-specific.

## Abstraction Levels

### L0 — Defining Invariant (minimal)

An Event Registration Platform is the organizer-side software whose center of gravity is the sign-up intake for an event. Three structures, each load-bearing:

1. **The event as a registration offer** — the organizer defines, inside the platform, an event (a dated occurrence or occurrence set — single event, multi-day, recurring, or multi-course/session programs) that people can sign up for. The offer carries the registration's state (open/closed/full). Capacity limits and admission/pricing options are the norm but not required (RSVP-style unlimited free sign-ups satisfy this structure). Remove → a form builder or a survey: intake with no event to register for.
2. **The application-mediated sign-up producing a registrant record** — the platform itself provides the intake surface (a public or invitation-gated page/flow) through which a person signs up (at minimum recording identity + attendance intent; typically a form with collected details, often with payment), and each completed sign-up becomes a persistent registrant record bound to the event. Remove → an advertisement with a link-out, or a paper form outside any system.
3. **The managed roster as the output** — registrant records accumulate into a roster the organizer works inside the same system: inspecting counts/take-up, finding and viewing registrants, modifying or cancelling registrations, communicating with registrants, and carrying the roster forward (exports, reports, check-in handoff). The roster mirrors the live state of the offer (spots taken vs remaining where capacity applies). Remove → a pile of form responses in a spreadsheet; the difference between "responses" and "a managed roster" is exactly the Type's center.

Historical check (§24):

- Paper-era practice (mail-in registration form → organizer's master list → confirmation by post; registration desk with a printed list) satisfies all three: offer = the announced event, intake = the form, roster = the master list. The digital platform mechanizes the same structures.
- Platform-native practice (a social platform's event page with RSVP states and a guest list the host can view and message) satisfies all three without money, capacity, tickets, or forms.
- A bare online form (form-builder boundary case) does NOT satisfy structure 2/3 in the registration sense: responses are not bound to an event object and not worked as a roster with take-up state.
→ Passes; the core is era- and implementation-neutral.

### L1 — Common Mature Structure

Present across the sample; expected in any mature product; not definitional:

- branded registration page/flow builder (the public intake surface)
- admission options: ticket types / registration types / registrant types with pricing machinery (tiers, early-bird rules, discounts, coupon codes)
- integrated payment processing with refunds; payout schedules; payment plans/installments at one pole
- capacity limits with live spot accounting; waitlists (auto-promotion in several products)
- custom questions, conditional logic / per-type registration paths, dynamic pricing
- waivers and document collection inside the registration flow
- group / table registration
- confirmation emails and registrant communication (email, SMS in several products); reminders
- registrant record operations: edit, cancel, refund (full/partial), transfer, defer; self-service registrant portals with organizer-controlled permissions
- reporting and exports (registration counts, revenue, take-up over time)
- check-in handoff: scanning apps, badge printing, attendance recording
- multi-event organization: organizer account, copying/templating, cross-event dashboards

### L2 — Variant / Optional Structure

Depends on segment, business model, or event format:

- marketplace/directory distribution (consumer marketplace pole; light vertical directories)
- promotion machinery (email marketing, ads, referral rewards, social tools)
- fundraising/donations and peer-to-peer fundraising
- membership sales/validation tied to registration
- session/sub-event selection with per-session capacity
- attendee event apps and engagement (gamification, networking)
- onsite extensions: kiosks, cashless payments, lead retrieval
- continuing-education credits
- vertical specialization (races with timing/timer ecosystem; camps; classes; trade shows)
- restricted/invitation-only registration (authentication-gated intake)
- virtual events
- business-model variants: per-registrant fees, free software + processing fee, marketplace fee model, free-for-nonprofit platforms

### L3 — Vendor-specific (Research Notes only)

- RegFox: per-paid-registrant fee (99¢ + 1%, capped $4.99); in-house payment processor; Real View builder; edit-in-place attendee philosophy (explicitly contrasted with cancel-and-re-register competitors); Engage attendee app; Mobile Pay Pass; memorized auto-emailed exports; purchase-protection upsell.
- RunSignup: Race Wizard; RaceDay suite (CheckIn app, Scoring, RaceJoy GPS, photo platform); timer as a first-class shared-access role; TicketSignup sibling brand (registration vs ticketing split at company level); USA Cycling sanctioned-event support; participant-info change cutoff dates; up-to-three-waivers rule; Find a Race directory.
- Eventbrite: consumer marketplace with discovery recommendations; "Registration event" as a named event type; PDF-ticket toggle; registration time limit; scheduled payouts.
- rsvpBOOK: registrant-type path builder; table registration; Kiosk+ onsite check-in; trade-show prize wheel lead capture; AI-assisted event setup; "Registration is the starting point" layering toward its own EMP.

## Vendor-specific Findings

See L3 above. Additional observations:

- RunSignup's parent company operates RunSignup (registration) and TicketSignup (ticketed events) as separate brands — organizational evidence that registration-centered and ticketing-centered products are distinct despite heavy feature overlap.
- rsvpBOOK's own positioning ("Registration is only the beginning"; "Need the broader event-management platform? Registration is the starting point.") is vendor-level confirmation of the registration → EMP layering recorded from the EMP side.
- RegFox's attendee-management page explicitly positions against competitors' cancel-and-re-register flows — evidence that registrant-record mutation semantics (in-place edit vs cancel/re-create) are a real differentiation axis within the Type, not a settled convention.

## Boundary Findings

1. **vs Event Management Platform (processed; joint-review flag DISCHARGED from this side)** — the thinnest seam in the event family, now documented from both sides. The registration platform centers the intake flow: the offer, the page, the form, the money, the registrant record — and the roster is its output. The EMP centers the whole event lifecycle (setup → publish/promote → register → manage → run → closeout). Every EMP contains registration machinery (directly observed in all five EMP-sample products); registration products exist without onsite, promotion, agenda, or closeout machinery. Removal tests hold both ways: remove the event lifecycle (publish states, promotion, onsite, closeout) → a registration platform remains; remove registration depth (curated manual-list operation) → an EMP survives. The market itself articulates the seam (rsvpBOOK: registration is the starting point, EMP is the extension; Eventbrite models "Registration event" as one event type inside a broader organizer platform). Boundary holds; keep-both ratified.
2. **vs Event Ticketing Platform (§26 sibling, unprocessed)** — ticketing centers on ticket inventory, pricing, and the ticket as the sold access artifact (allocation, seat maps, scanning the ticket); registration centers on the registrant record (who is coming and their collected data), with tickets optional. Direct evidence: Eventbrite's registration-only mode disables PDF tickets entirely; RunSignup's parent splits registration vs ticketing across brands. In registration products a ticket (if present) is a receipt/confirmation artifact of the registration; in ticketing products the ticket is the product being sold.
3. **vs Online Form Builder (§03.11, unprocessed)** — a form builder collects responses; a registration platform binds sign-ups to an event offer inside the same system with registration semantics: take-up state, capacity, admission options, confirmations, roster operations, money. A form-builder RSVP is the boundary case: intake without the registration machinery. (Consistent with the EMP doc's boundary #8.)
4. **vs Attendee Management (processed)** — Attendee Management is the roster slice (who is on the list, did they show up); the registration platform owns the machinery that fills and maintains the roster. That doc positions EMP as broader; the same containment holds here, with the registration platform as the intake-side owner of the roster.
5. **vs Event Agenda Management (processed)** — program center vs intake center. Session/sub-event selection exists inside registration (RegFox session reservation, rsvpBOOK sessions with capacity) as choices attached to registrant records — not a program-of-record with published agenda surfaces. Mirror of that doc's boundary from the other side.
6. **vs Camp Management System (processed; flag from that pass DISCHARGED)** — generic registration tools can process camp transactions, but lack the camp-operation layer (guardian accounts, health machinery, bunks, seasonal staff, session rosters). RegFox markets camps as an industry but ships registration machinery over them; the camp-management doc's boundary is confirmed from this side.
7. **vs Digital Waiver Management (processed; flag from that pass DISCHARGED)** — waiver-as-registration-step is a capability of this Type, directly observed (RegFox integrated digital release waivers within the event page; RunSignup up to three waivers per event collected and saved during registration; Eventbrite waivers with registration). A standalone waiver system has no registration, payment, or roster machinery.
8. **vs Association Event Management (processed)** — that Type = event machinery operated on a membership registry, with standing-conditioned access/pricing persisted to member records. Membership *validation as a pricing condition* appears inside registration products (RegFox membership validation/discounts, RunSignup membership discounts) as a capability; the registry substrate is the discriminator. Boundary holds.
9. **vs Appointment Scheduling / Meeting Scheduling (§03.09 siblings)** — scheduling products book an individual into a service provider's calendar slots (calendar-centric); registration products register a population for a dated event occurrence (offer-centric). Class/workshop booking with per-session capacity is the fuzzy middle; the sampled registration products model it as session choices on a registration, not as provider calendars.
10. **vs Course Registration System (§23 education leaf, unprocessed)** — academic course registration carries enrollment semantics (prerequisites, credit, grading, student records); event registration carries attendance semantics for dated occurrences. Separate leaf retained; noted for that pass.
11. **vs Restaurant Reservation Platform (§26 sibling)** — reservation books a table/cover at a hospitality time slot (table-inventory center); registration enrolls people into an event offer (roster center). Different object of record, different operator.

"Remove what to become the other Type" summary: remove the event binding and roster machinery → form builder; add the full event lifecycle (promotion, program, onsite, closeout) as the center → Event Management Platform; make the ticket/inventory the sold artifact → Event Ticketing Platform; make the roster+presence the center without intake → Attendee Management; add the membership registry substrate → Association Event Management; add the camp-operation layer → Camp Management System; make the waiver loop the center → Digital Waiver Management.

## Uncertainties

- The dedicated program-registration pole (Regpack-class: camps/classes with deep payment-plan and participant-account machinery) could not be fetched (403 ×2). Its existence is known to the market, but no direct evidence was captured; the pole is evidenced here only through RegFox's payment plans and camp/class industry pages. Flag for future enrichment.
- The free-for-nonprofit business-model pole (Zeffy-class) could not be fetched (timeout ×2); business-model variants are documented from the three poles that were fetched.
- Deep help-center KBs were fetched only for Eventbrite (registration-mode article this pass; more in the prior EMP pass). RegFox/RunSignup/rsvpBOOK evidence rests on official product/feature pages; precise operational defaults, exact state names, numeric limits, and refund-window specifics are deliberately not asserted.
- Waitlist auto-promotion was directly evidenced for RegFox ("automatically capture sales when spots open up"); for other products waitlists are evidenced but promotion mechanics are not.
- Whether invitation-only/restricted registration is common or rare is unclear (direct evidence in one product: RegFox restricted access); kept as variant.
- Regional (non-US) registration products were not sampled; geographic variants unknown.

## Final Synthesis

The Event Registration Platform is the intake-centered member of the event family. Its defining core is a three-link chain: the organizer defines an event as a sign-up offer inside the platform; the platform itself mediates the sign-up through a page/flow, turning each completed sign-up into a persistent registrant record bound to the event; and the records accumulate into a managed roster the organizer works — inspecting take-up, modifying registrations, communicating, collecting money where applicable, and handing the roster to check-in. Money, tickets, capacity, waitlists, forms, waivers, groups, confirmations, reports, and check-in machinery are the standard layers the market has grown around that spine — none of them is required for the Type to be recognizable (free registration-only events, RSVP guest lists, and paper-era master lists all satisfy the core). The Type's center of gravity is turning the public's intent to attend into a managed roster; everything beyond intake — promotion, program, onsite operations, closeout — is drift toward the Event Management Platform, which the market itself packages as an extension of registration (or registration as the starting point of an EMP).
