# Research Notes — Event Management Platform

## Research Goal

Understand what an Event Management Platform (EMP) actually is as an Application Type: what objects exist inside it, what the organizer does with them, how work flows from event creation through registration to the event itself and closeout, and where the Type's boundary sits against the many sibling event Types already processed in §26 (Event Agenda Management, Attendee Management, Association Event Management, Convention/Exhibition Management, Event Credential/Badge Management) and the unprocessed siblings (Event Registration Platform, Event Ticketing Platform, Reserved Seating Platform, Venue Management System, Event Mobile App).

## Initial Boundary

Working hypothesis before research:

- Core use: organizer-side software to plan, publish, register attendees for, run, and close out an event.
- Primary users: event organizers/planners; secondary: marketing, finance, onsite staff; consumers: attendees.
- Nearest neighbors: Event Registration Platform (narrower), Event Ticketing Platform (narrower), Attendee Management (roster slice, processed), Event Agenda Management (program center, processed), Association Event Management (registry substrate, processed), Convention/Exhibition Management (floor-sale machinery, processed), Venue Management System (venue-side), Online Form Builder (forms without event lifecycle), Webinar/Virtual Event Platform (delivery-centric), Meeting Scheduling (different object).
- Known unknowns: is money/ticketing definitional or common? Is the public event page part of the defining core? Is check-in definitional? Where exactly does EMP end and Event Registration Platform begin?

## Research Questions

1. What is the central object — the event, the registration, or the attendee?
2. What does the organizer's working loop look like end-to-end?
3. Is payment/ticketing part of the defining core, or a common capability? (free events, registration-only modes)
4. Is the public event page/registration surface definitional?
5. Which capabilities are common-mature vs optional vs vendor-specific?
6. How do the poles differ (self-service marketplace vs enterprise suite vs marketing-led)?
7. How does this Type interlock with the already-documented sibling Types?
8. Historical check: do paper-era and platform-native event practices fit the proposed core?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Evidence quality |
|---|---|---|---|
| Cvent | enterprise all-in-one suite | enterprise | product pages + platform structure (help KB not article-fetched) |
| EventsAir | enterprise event-management pure-play | enterprise/association/government | help center articles directly fetched (Layer A) |
| Eventbrite | self-service ticketing + discovery marketplace | SMB/creator | help center articles directly fetched (Layer A) |
| Whova | mid-market all-in-one (app-led) | associations/universities/corporate | product pages + FAQ (Layer A/B) |
| Splash | marketing-led corporate (event-led growth) | corporate marketing teams | product pages (Cvent-owned) (Layer A/B) |

## Sources

- Cvent — Event Marketing & Management solutions page: https://www.cvent.com/en/event-marketing-management (fetched 2026-09-07)
- EventsAir Help Resources — home, Detailed How-To Guides collection, Attendee management - Overview: https://help.eventsair.com/ , https://help.eventsair.com/en/collections/10818886-detailed-how-to-guides , https://help.eventsair.com/en/articles/9564042-attendee-management-overview (fetched 2026-09-07)
- Eventbrite — Organizer overview: https://www.eventbrite.com/organizer/overview/ ; Help Center "Creating an event" topic: https://www.eventbrite.com/help/en-us/topics/creating-an-event/ ; "Create an event": https://www.eventbrite.com/help/en-us/articles/551351/how-to-create-an-event/ ; "Registration only" setup: https://www.eventbrite.com/help/en-us/articles/250995/how-to-set-up-an-event-that-doesn-t-require-tickets-registration-only/ (fetched 2026-09-07)
- Whova — Event Management Software page + FAQ: https://whova.com/event-management-software/ (fetched 2026-09-07)
- Splash — product home + platform structure: https://splashthat.com/ (fetched 2026-09-07)
- Sibling docs consulted for boundary alignment: applications/event-agenda-management.md, applications/attendee-management.md, applications/association-event-management.md (all processed 2026-09-06/07)

Source-access limitations:

- Cvent's operational knowledge base (support.cvent.com) was not article-fetched in this pass; Cvent evidence rests on official product pages and the platform's own navigation structure. Claims about Cvent are kept at product-page level.
- Splash's help center was not fetched; evidence from product pages and platform navigation.
- Whova's organizer-side help portal (xems) was not fetched; evidence from public product pages and FAQ.

## Product Observations

### Cvent (enterprise suite) — evidence layer A (product pages), B (structure)

- Self-positions as "all-in-one solution for every event type across the entire event lifecycle" for in-person, hybrid, virtual events and webinars.
- Platform organized in three phases visible in its own navigation: **Plan your event** (registration & marketing, venue sourcing, vendor sourcing, event diagramming, repeatable events, hotel room blocks, approvals & budgeting, speaker management); **Run your event** (event app, check-in & badging, attendee engagement, trade-show lead capture, meetings, virtual experience, webinars); **Measure and scale** (event & attendee insights, integrations, surveys, lead retrieval, AI content repurposing).
- Four capability pillars on the solutions page: **Plan and Promote** (personalized marketing, fully branded websites, automated promotions/communications, speakers/sponsors/exhibitors in one place); **Attendee Engagement** (branded event experiences, check-in and badging, mobile event apps); **Spend and Workflow** (meeting requests, budgets, approvals, spend tracking); **Actionable Insights** (attendee-journey insights, data flow to SaaS integrations, feedback).
- Marketing framing: events as a marketing channel; "drive attendance, then capture and act on audience interests."
- Scale claims (8.3M events managed, 89% of Fortune 100) — marketing numbers, recorded here only as positioning.
- Vendor-specific extensions: venue sourcing (Supplier Network), event diagramming, room-block management (Passkey), webinar platform, CventIQ AI.

### EventsAir (enterprise pure-play) — evidence layer A (help center articles)

- Help center structure shows the product's spine: overall settings, quick-start guides, detailed how-to guides, panel-by-panel guides, apps & portals, virtual/hybrid platform (OnAIR), integrated payments (EventsAir Pay), FAQs.
- **Attendee record is the working hub**: the Attendees Panel lists attendees; each attendee record carries contact details plus "all the information about what they've selected or been added to within various modules: Registration, Accommodation, Travel and more" — and, if involved, Presentations (speaker/reviewer), Exhibitions, Sponsorship, CE Courses. Module items include Contact, Notes, Marketing, Communications, Registrations, Agenda, Functions, Accommodation, Travel.
- **Attendee actions** (from the record): Financials (payments, refunds, invoices, receipts, audit trail, miscellaneous charges), Send communication (email/SMS/app messages, merge docs), Group linking, Print personalized documents (labels, certificates of attendance, itineraries, pro-forma invoices), Change log (date/time/user/details), Attendee tools (cancel all or selected items, name badge, online activity log, PDF merge doc, replace attendee), delete or anonymize.
- **Attendee financials** are a first-class collection: payments, invoices, refunds including credit notes, audit trail and receipts.
- **Onsite**: preparing to go onsite, check-in and check-out options, location beacons.
- **Engagement**: EventStream social network, gamification, live Q&A and polling.
- **Registration site**: "interactive (registration) sites" with Google Tag Manager support; site auto-login links pre-populate forms/portals with the attendee's details; attendee verification for known contacts.
- **Contact Store**: a persistent contact database creatable and usable across events (separate from per-event attendee records).
- **Membership Management** exists as a Membership Contact Store event type (the substrate the Association Event Management sibling documented).
- Other modules: presentations & abstracts, exhibitions & trade fairs, meeting matching, VIP/elite group management.
- Cancelled/postponed events have a best-practices guide (event-level cancellation is a supported, consequential operation).

### Eventbrite (self-service marketplace) — evidence layer A (help center articles)

- Organizer overview: "all-in-one ticketing and discovery platform"; features grouped as **Event Creation** (event page builder, event registration, event payments, reserved seating, timed entry, sell tickets online), **Event Promotion** (ads, email marketing, TikTok promotion, promo codes), **Event Hosting** (ticket scanning/check-in app, contactless payments).
- **Create an event** flow (help article): build event page (title, summary, date/time, location, overview, additional info, agenda/lineup) → create online event page (if online) → add tickets and add-ons (free, paid, or donation ticket types; copy from other events; venue map for reserved seating) → set up order form and order confirmation (collect information, custom questions, custom confirmations) → publish and manage (preview, organizer, search settings, refund policy, payout details, promote).
- **Registration-only mode** (help article): events that don't require tickets — disable printable tickets; "By default, free events are registration only"; paid events can switch event type to "Registration event". → Direct evidence that ticketing/payment is NOT definitional; registration without tickets is a first-class mode.
- **Event lifecycle states** (topic list): change event status, schedule a publish time, cancel event, unpublish or delete, postpone and reschedule, multi-date/multi-location events, recurring/timed-entry events, copy event.
- **Capacity** (topic list): set and restrict total capacity; holds; ticket sections; automatic price changes; early-bird types.
- **Order machinery**: order form, custom questions, registration time limit, order confirmation, waivers with registration, add-ons (merchandise), guest lists.
- **Marketplace distribution**: attendee discovery with personalized recommendations; Eventbrite Ads; the event page lives on Eventbrite's consumer marketplace — a business-model variant (distribution built in).
- Organizer app for check-in and door sales; payouts scheduled (weekly/per-event/etc. — marketing page).

### Whova (mid-market all-in-one) — evidence layer A/B (product pages + FAQ)

- Product line: Event App, Event Management Tools, Hybrid & Virtual, Registration & Ticketing, Abstract Management, MicroEvents, Event Website Builder, Exhibitor & Sponsor Management.
- Management tools page: registration & ticketing (custom forms, multiple ticket types, add-ons, secure payments, instant payouts), name badge generation (templates, per-attendee-type designs, QR codes, bulk or on-demand printing), attendee check-in (phone/laptop search, QR scan, volunteer delegation, self check-in kiosk, event/day/session check-in), speaker center (self-service bio/headshot/session upload, auto-sync to pages), digital waivers (templates, targeting by group/ticket type, reminders, check-in integration), polls/surveys/session feedback, certificates (from attendance records), announcement wall (venue screens), post-event analytics (pre-event registration analytics, live stats, sponsor/exhibitor ROI, cross-event comparison, 50+ page post-event report).
- FAQ defines the category: "Event management software is an online platform designed to simplify the planning and delivery of events. It brings key functions such as attendee registration, event promotion, check-in, speaker management, attendee engagement, badge generation, and performance analytics into one centralized platform."
- FAQ confirms: in-person/virtual/hybrid; micro-events and large conferences; CRM/AMS integrations.
- Vendor-specific: MicroEvents (small recurring events reusing settings), 50+ page post-event report, announcement wall.

### Splash (marketing-led corporate; Cvent-owned) — evidence layer A/B (product pages)

- Platform modules: Event Design (branded pages), Guest Management (real-time sync, automation, visibility), Ticketing, Invites and Reminders (email), Virtual Venue, Attendance Insights (AI-powered predictions), On-Site Tools (check-in, badge printing, live data sync), Integrations (Marketo, Salesforce, Slack), Reporting, Team Management (user roles, compliance rules, asset library), Security & Compliance, Event Calendars (roadshows, microsites).
- Positioning: "event-led growth" — events as pipeline; customer quotes emphasize registration pages, RSVP sync to Salesforce, lead handoff to sales, ROI attribution.
- Guest Management is the roster layer; the marketing layer (design, invites, reminders) is the differentiating emphasis vs operations-led suites.
- Event Calendars: managing a program of many events (roadshows) as a first-class surface.
- Release log hosted on cvent.com; community on Cvent's site — Splash is a Cvent company (corporate fact, recorded as context).

## Cross-product Comparison

| Structure / capability | Cvent | EventsAir | Eventbrite | Whova | Splash | Layer |
|---|---|---|---|---|---|---|
| Event as managed record with lifecycle (draft→published→held→closed/cancelled; postpone/reschedule) | ✓ (plan phase) | ✓ (incl. cancelled/postponed guide) | ✓ (status, publish scheduling, cancel, unpublish, postpone) | ✓ | ✓ | B |
| Public event page as registration surface | ✓ (branded websites) | ✓ (interactive registration sites) | ✓ (event page builder on marketplace) | ✓ (website builder) | ✓ (branded pages) | B |
| Registration/attendee records as managed population | ✓ | ✓ (attendee record hub with modules) | ✓ (orders/attendees, guest lists) | ✓ (attendee list) | ✓ (guest management) | B |
| Registration form / custom questions | ✓ | ✓ (registration site forms) | ✓ (order form, custom questions) | ✓ (custom forms) | ✓ | B |
| Ticket types incl. free/paid/donation | ✓ | ✓ | ✓ (free/paid/donation; registration-only mode) | ✓ (multiple ticket types, add-ons) | ✓ (ticketing module) | B |
| Payment processing, refunds, payouts | ✓ | ✓ (payments/invoices/refunds/credit notes/receipts) | ✓ (payments, payouts, refund policy) | ✓ (secure payments, instant payouts) | ✓ | B |
| Capacity / waitlists / holds | ✓ | ✓ | ✓ (capacity, holds) | ✓ | (not surfaced on fetched pages) | B (A for EB/EA) |
| Registrant communication (confirmations, reminders, targeted email) | ✓ (automated promotions/communications) | ✓ (communications panel, merge docs, SMS/app messages) | ✓ (emails to attendees, custom confirmations) | ✓ (announcements, reminders) | ✓ (invites & reminders) | B |
| Check-in / onsite (scan, badges, kiosks) | ✓ (check-in & badging) | ✓ (check-in/check-out, beacons) | ✓ (organizer check-in app, ticket scanning) | ✓ (QR check-in, kiosk, badges) | ✓ (on-site tools) | B |
| Reporting / analytics | ✓ (event & attendee insights) | ✓ (reports; audit trails) | ✓ (real-time analytics) | ✓ (post-event report) | ✓ (reporting, attendance insights) | B |
| Multi-event organization (copy, recurring, calendars) | ✓ (repeatable events) | ✓ (contact store across events) | ✓ (copy event, recurring/timed-entry) | ✓ (MicroEvents reuse) | ✓ (event calendars/roadshows) | B |
| Agenda/lineup & speakers | ✓ (speaker management) | ✓ (presentations/abstracts) | ✓ (agenda/lineup on page) | ✓ (speaker center, abstract mgmt) | (webinar/virtual venue) | B |
| Event mobile app / engagement (polls, networking, gamification) | ✓ (event app, attendee hub) | ✓ (attendee app, EventStream, polls) | ✗ (not in fetched scope) | ✓ (event app, polls, gamification) | ✓ (virtual venue) | B |
| Exhibitors / sponsors / lead retrieval | ✓ | ✓ (exhibitions, sponsorship, lead mgmt) | ✗ | ✓ (exhibitor/sponsor mgmt, lead retrieval) | ✗ | B |
| Virtual/hybrid delivery | ✓ (virtual platform, webinars) | ✓ (OnAIR, AIRCast) | ✓ (online events, Zoom connect) | ✓ (hybrid/virtual) | ✓ (virtual venue) | B |
| Marketing automation depth / CRM sync | ✓ (integrations) | ✓ (marketing module items) | ✓ (email tools, ads) | ✓ (integrations) | ✓✓ (Marketo/Salesforce, ELG positioning) | B |
| Marketplace/discovery distribution | ✗ | ✗ | ✓✓ (defining business model) | ✗ | ✗ | A — product-specific |
| Budgeting/spend workflow & approvals | ✓✓ (spend workflow) | (accounting overview) | ✗ | ✗ | ✗ | A — product-specific |
| Venue sourcing / diagramming / room blocks | ✓✓ (Supplier Network, diagramming, Passkey) | ✗ | ✗ | ✗ | ✗ | A — product-specific |
| Travel/accommodation modules | ✗ | ✓✓ (Accommodation, Travel modules) | ✗ | ✗ | ✗ | A — product-specific |
| CE credits / certificates | (surveys) | ✓✓ (CE courses/credits) | ✗ | ✓ (certificates) | ✗ | B |
| AI features | ✓✓ (CventIQ) | ✗ (not surfaced) | ✓ (AI event creation) | ✗ | ✓ (attendance predictions) | B |

Reading: rows 1–12 are present across the whole sample → common mature structure (L1). Rows marked ✓✓ appear strongly in one product → vendor-specific or pole-defining (L3/L2). No sampled product lacks rows 1–5.

## Abstraction Levels

### L0 — Defining Invariant (minimal)

An Event Management Platform is the organizer-side system of record for putting on an event. Three structures, each load-bearing:

1. **The event as a managed record** — a named, dated occurrence (single, multi-day, or recurring series) that the organizer creates, configures, publishes, and carries through a lifecycle (draft → published/open → held → completed/cancelled, with postpone/reschedule). Everything else hangs from it. Remove → a form builder or a static web page.
2. **The registration surface turning sign-ups into records** — a public-facing event page with a sign-up flow (registration form, ticket/registration types) through which attendees become persistent registration/attendee records bound to the event (public, invitation-gated, or organizer-filled intake). Remove → an advertisement or listing.
3. **Organizer-side management of the event's attendance lifecycle** — the organizer works the event and its registrations as managed records: opening/closing registration, tracking against capacity, confirming/modifying/cancelling registrations, communicating with registrants, and recording what happened (attendance where applicable), with records persisting through and after the event. Remove → a listing site or a bare RSVP button.

Historical check (§24): paper-era practice (invitation + RSVP cards + door list + printed tickets, organizer keeping the master list) satisfies all three without any digital machinery; platform-native Facebook Events (event page + RSVP states + guest list + host announcements) satisfies all three without payment, badges, or analytics. The core is era- and implementation-neutral. Passes.

### L1 — Common Mature Structure

Present across the sample; expected in any mature product; not definitional:

- event page/website builder (branding, images, agenda/lineup display)
- ticket/registration types with pricing machinery (free/paid/donation, tiers, promo codes, add-ons)
- integrated payment processing, refunds, payouts/invoices/receipts
- capacity limits, waitlists, holds
- registration forms with custom questions; order confirmations
- registrant communication (confirmations, reminders, targeted/segmented email)
- check-in & onsite machinery (scan apps, badge printing, kiosks, door sales)
- reporting & analytics (registrations, revenue, attendance, engagement)
- multi-event organization (organizer account, copying/templating, recurring events, cross-event reporting)
- agenda/lineup and speaker handling (module — sibling Type Event Agenda Management)
- integrations (CRM/marketing automation, payment, streaming)

### L2 — Variant / Optional Structure

Depends on segment, business model, or event format:

- marketplace/discovery distribution (consumer marketplace pole)
- event mobile apps & attendee engagement (polls, Q&A, networking, gamification, social walls)
- virtual/hybrid delivery (streaming, virtual venue)
- exhibitors/sponsors (booths, lead retrieval, sponsorship packages)
- abstract/presentation management (academic/conference)
- travel & accommodation modules (enterprise multi-day)
- marketing-automation depth & CRM/pipeline attribution (event-led-growth pole)
- budgeting/spend workflow & approvals (enterprise governance)
- continuing-education credits & certificates (association/education)
- waivers/consent forms (liability-bearing events)
- team roles/permissions/compliance (enterprise)
- curated invitation-only posture (guest-list-led corporate/social)

### L3 — Vendor-specific (Research Notes only)

- EventsAir: module-per-attendee-record architecture (Registration/Accommodation/Travel/Presentations/Exhibitions/Sponsorship/CE Courses inside one record), Contact Store, EventStream social network, OnAIR virtual platform, AIRCast streaming, EventsAir Pay, site auto-login tokens, replace-attendee tool, location beacons.
- Eventbrite: consumer marketplace + discovery recommendations, Eventbrite Ads, TikTok promotion, recurring/timed-entry machinery, "registration event" type toggle, scheduled payouts.
- Cvent: Supplier Network (venue sourcing), event diagramming, room-block management (Passkey), spend workflow, CventIQ AI, iCapture/Jifflenow lead capture, Attendee Hub.
- Whova: MicroEvents, 50+ page post-event report, announcement wall, community awards positioning.
- Splash: event-led-growth positioning, AI attendance predictions, roadshow event calendars/microsites; Cvent ownership.

## Vendor-specific Findings

See L3 above. Additionally:

- Eventbrite's self-description ("ticketing and discovery platform") shows the marketplace pole naming itself by its distribution model rather than by the generic Type — evidence that the same underlying structure (event + registration + management) is marketed under different flags.
- Splash's "guest management" naming for the roster layer and "event-led growth" for the revenue framing show the marketing pole's vocabulary.
- EventsAir's attendee-record-with-modules is the deepest realization of "one record per person per event with everything attached"; lighter products flatten this into simpler attendee lists.

## Boundary Findings

1. **vs Event Registration Platform (sibling, unprocessed)** — thinnest seam in the family. Registration platform centers on the intake flow (forms, registration paths, payments); EMP centers on the whole event lifecycle (setup → publish/promote → register → manage → run → close out). Every EMP contains registration machinery; a registration product can exist without onsite, promotion, or closeout. Test: remove the event lifecycle (publish states, onsite, follow-up) — what remains is a registration platform; remove registration depth (curated manual lists) — an EMP survives. Flag for joint review when that leaf is processed.
2. **vs Event Ticketing Platform** — ticketing platform centers on ticket inventory, pricing, and sales (the ticket as sold inventory); EMP centers on the event and its attendee lifecycle, with ticketing as one capability. Eventbrite straddles (marketplace ticketing + full organizer tooling) but its organizer dashboard covers the full lifecycle. Registration-only mode (directly documented) proves ticketing is not the EMP's center.
3. **vs Attendee Management (processed)** — Attendee Management is the roster slice: who is on the list and did they show up. EMP is the whole production; the roster slice is contained in every EMP (that doc itself positions EMP as "broader suite"). The seam: EMP owns the registration machinery that fills the roster; Attendee Management consumes rosters from intake connections.
4. **vs Event Agenda Management (processed)** — program center vs attendee-lifecycle center. Mirror of that doc's boundary: "an event platform remains one without agenda depth, and an agenda product exists with no registration at all." Agenda/lineup appears in EMPs as a page element and a module, not the center.
5. **vs Convention/Exhibition Management (processed)** — that Type's differentiator is the sellable-floor inventory (booth states on a floor plan) and space-sale machinery. Broad suites (Cvent, EventsAir, Whova) straddle both Types. Both Types stand; containment documented from that side, mirrored here.
6. **vs Association Event Management (processed)** — that Type = EMP machinery operated on a membership registry, with standing-conditioned access/pricing and participation persisted to member records. Remove the registry layer → generic EMP. The joint-review flag recorded by that pass is discharged from this side: the boundary holds as documented (registry substrate vs generic attendee intake).
7. **vs Venue Management System** — venue-side space inventory and booking (the venue's calendar of what occupies its rooms) vs organizer-side event production. Different operator, different object of record.
8. **vs Online Form Builder** — a form collects responses; an EMP anchors responses to an event record with lifecycle, capacity, communication, money, and attendance machinery. A form-builder RSVP is the boundary case: intake without management. (Splash review quote noting teams "using Eventbrite to Google forms" before consolidating shows the market's own perception of the gap.)
9. **vs Marketing Campaign Management / Marketing Automation** — events as one campaign type vs the event as the center. Splash straddles from the marketing side but its center remains the event page + guest management + onsite.
10. **vs Webinar Platform / Virtual Event Platform** — delivery-centric (streaming, engagement) vs lifecycle-centric. Virtual delivery is a module inside EMPs (all five sampled products either ship it or integrate it).
11. **vs Meeting Scheduling Application** — schedules individuals' meetings/availability; EMP produces public events with attendee populations. Different object.
12. **vs Community Platform** — Meetup-class products center on a standing community with recurring events; EMP centers on producing events. Drift, not identity.

"Remove what to become the other Type" summary: remove the event lifecycle & management → registration/form tool; remove registration depth → listing/promotion; remove the event container → CRM; remove the generic attendee intake and add a membership registry → Association Event Management; add the sellable floor → Convention/Exhibition Management; make the program the center → Event Agenda Management; make the roster+presence the center → Attendee Management.

## Uncertainties

- Cvent's operational help-center articles were not fetched; Cvent-specific workflow details (registration build steps, state names) are unverified at article level. Claims kept at product-page level.
- Exact event-lifecycle state names vary by product (draft/live/cancelled vs draft/published/completed vs active/archived); documented conceptually.
- Waitlist machinery was directly evidenced for Eventbrite (topic listing) and EventsAir (association doc context) but not surfaced on Whova/Splash fetched pages — treated as common, not universal.
- The Event Registration Platform leaf is unprocessed; the seam is documented from this side only and should be revisited in that pass.
- Whova's organizer-side help portal was not fetched; Whova evidence is product-page level.
- Splash's help center was not fetched; Splash evidence is product-page level.

## Final Synthesis

The Event Management Platform is the general-purpose, organizer-side Type of the event family: its center of gravity is the **event's attendance lifecycle** — the event record, the registration surface that fills it with attendee records, and the organizer's management of both through publish, registration, the event itself, and closeout. Money, marketing, onsite machinery, apps, agendas, and analytics are the standard and optional layers that the market has grown around that spine; none of them is required for the Type to be recognizable. The Type is deliberately the *generic* member of its family: the sibling Types (Association, Nonprofit, Religious, Convention/Exhibition, Agenda, Attendee, Registration, Ticketing) are each produced by moving the center of gravity to a specific substrate, artifact, or slice, while this Type keeps the whole lifecycle in view for the general event.
