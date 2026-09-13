# Research Notes — Attendee Management

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what the "Attendee Management" Application Type actually is in the real events-software market: what core objects exist, what lifecycle the attendee record follows, what operators do with the roster before / during / after an event, and how this Type differs from the many adjacent event-domain leaves (Event Registration Platform, Event Ticketing Platform, Event Credential / Badge Management, Event Mobile App, Event Management Platform).

## Initial Boundary

Initial hypothesis (before research): operator-facing software for managing the population of people attached to an event — who is expected, their details and entitlements, whether they actually showed up, and follow-up. Nearest neighbors: Event Registration Platform (intake flow), Event Ticketing Platform (inventory), Event Credential / Badge Management, Event Mobile App, Event Management Platform (broader suite). Key risk: this node may be only a capability/module of event suites rather than an independent Type.

## Research Questions

1. What is the core object (attendee/registrant/guest record) and what does it link to (event, order/ticket, registration, sessions, badge)?
2. How do people enter the roster (self-registration, RSVP, import, manual add)?
3. What lifecycle states does an attendee record move through (expected → confirmed/paid → checked in / attended / no-show / cancelled)?
4. What operator actions exist on the roster (search, filter, categorize, edit, resend, cancel/refund, transfer, assign sessions, badge, check in, message)?
5. What happens on site (check-in console, scanning, kiosks, badge printing, walk-in handling, record editing at the door)?
6. What rules matter (capacity, waitlist, ticket/reg type governing access, per-session capacity, cancellation, offline behavior, data privacy)?
7. What surfaces exist (roster tables, attendee detail, check-in console, badge designer, kiosk, reports, attendee-facing self-service/app)?
8. Where is the boundary against registration/ticketing/event-app/badge Types — and is this node an independent Type or a suite module?

## Representative Products

Chosen for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Position | Philosophy |
|---|---|---|
| Eventbrite | mass-market self-serve registration & ticketing; organizer app | order/ticket-centric; attendee list is a byproduct of orders |
| Whova | conference/association all-in-one; attendee-app-centric | engagement-centric; attendee list feeds app, badges, check-in |
| Swoogo | mid-market/enterprise event platform | registration-centric; strong onsite check-in module (Go Onsite) |
| zkipster | premium/luxury events (galas, fashion, art, sport hospitality) | guest-list-centric; invitation/RSVP model, not ticket-inventory model |

Note: the non-ticketed guest-list pole (zkipster) is deliberately included as the historical / differently-positioned sample: it has no ticket inventory, no paid registration by default, and still is recognizably the same Type.

## Sources

Official product pages and documentation surfaces fetched 2026-09-06:

- Eventbrite — Organizer Check-In App feature page: https://www.eventbrite.com/organizer/features/organizer-check-in-app/ ; Help Center home: https://www.eventbrite.com/help/en-us/
- Whova — Event Management Software page: https://whova.com/event-management-software/ ; product home: https://www.whova.com/
- Swoogo — Go Onsite (onsite check-in app) page: https://swoogo.events/mobile/go-onsite/ ; product home: https://swoogo.events/
- zkipster — Guest List Manager page: https://www.zkipster.com/guest-list-manager ; product home: https://www.zkipster.com/ ; support collections referenced at https://support.zkipster.com/en/

Access limitations:
- Cvent help center (https://help.cvent.com/hc/en-us) and a Cvent product URL returned 404; Cvent abandoned after two failures and excluded from the sample.
- Whova support subdomain (support.whova.com) unreachable; Whova documented from its product pages instead.
- Deep help-center articles (per-article URLs) were not directly reachable from the research environment for most vendors; research relies on official product pages and help-center/navigation structure. Per evidence rules, no precise numeric limits, default settings, or exact state-name vocabularies are asserted in the final document; moderate claim strength used throughout.

## Product Observations

### Eventbrite (evidence layer: A — directly observed on official pages)

- Organizer model is order/ticket-centric: attendees enter the roster by buying tickets / registering through a listing; the organizer's "attendee list" reflects orders and ticket types.
- The Organizer app (mobile) is the on-site surface: scan QR codes on tickets, verify online registrations instantly, prevent ticket fraud at the door, track live attendance in real time, process on-site ticket and merchandise sales, view event data and sales reporting.
- Help Center (attendee side) shows self-service record mutation paths: attendees can transfer tickets to someone else and edit their registration information — i.e., the roster can be updated by the attendee directly, not only by staff.
- Event formats supported include reserved seating and timed entry ticketing — roster state can be tied to seating/entry windows.

### Whova (evidence layer: A)

- Event Management Tools page documents the attendee-list-to-output pipeline: name badge generation aggregates all attendee list data; badge designs can differ by attendee type / ticket type (speakers, exhibitors, attendees, organizers color-coded).
- Check-in: search attendee by name and check in manually through mobile app or web dashboard; scan the QR code on the badge or in the app; add volunteers as check-in staff at any time; self check-in kiosk; event check-in, day check-in, and session check-in on the same platform.
- FAQ describes onsite check-in as: search personal information (email or registration number), confirm arrival, name badges instantly printed with correct information.
- Waiver/consent forms can be targeted to specific groups, ticket types or segments, tracked for completion, and signed on the spot during check-in.
- Analytics: pre-event ticket sales and registration responses, check-in progress, session attendance, sponsor/exhibitor analytics, cross-event comparison, post-event report.
- Attendance records are used to determine certificate recipients (qualifications from attendance records).
- Products named as adjacent modules: Registration & Ticketing, Abstract/Speaker Management, Exhibitor & Sponsor Management, Event App — i.e., in suites, attendee data is one data spine across modules.

### Swoogo (evidence layer: A)

- Go Onsite (check-in app): check attendees into the event or into sessions by attendee name or QR code; add guests to a session last minute on the spot.
- Real-time attendance tracking by registration type; sponsor check-in; "Check-In Planner Alerts" that auto-notify team members when a VIP checks in.
- Built-in badge designer; badge design assigned per registration type; on-demand badge printing at check-in.
- Kiosk Mode (paid add-on): attendee-led self check-in on a tablet, including paying outstanding balances and flagging profile edits.
- Walk-in registrants can be created at the door; attendee records can be edited on the spot; custom check-in questions collect info at check-in.
- Offline check-in: check-in continues without connectivity; locally stored check-in data syncs when connection returns (badge printing devices require Wi-Fi — vendor detail).
- Unlimited onsite user logins (staff/volunteer stations); package check-in; onsite payment processing (Stripe) as add-on; RFID and device rentals via partners.
- Platform-level: "global attendee record" in Data + Insights — attendee identity persists across events for cross-event reporting.

### zkipster (evidence layer: A)

- Two-layer people structure: a persistent contact database ("Audience" — tags, segments, deduplication, lists) separate from per-event guest lists; events integration pulls contacts into event lists.
- Guest lists per event are more than a flat list: multiple named lists (general admission, press, sponsors, VIPs, donors, talent…); custom fields and colors; filters; bulk changes; a master guest list is auto-generated for check-in day.
- Guest profiles: contact details, meal choices, pictures ("facesheets" for check-in staff to recognize VIPs), guest relationships (linked guests can RSVP for each other; relationships inform seating and sessions).
- Sessions and capacity management: sessions within events (workshops, breakouts, experiences), in-person/virtual/recurring; session capacities are dynamic — sessions become unavailable when full but can be overbooked internally; booking rights differ per guest category/list; session check-in plus main event check-in; per-session reports with attendance and arrival times.
- Check-in app (iOS/Android): search + QR/barcode scanning, kiosk mode, offline mode, name badge printing, check-in messages (text/email alerts).
- Intake: online RSVP forms, invitations via email/SMS/WhatsApp, spreadsheet import, CRM/ticketing-platform integrations via API; export of all guest data.
- No ticket-inventory model by default; payments exist but the event population is curated by the organizer (invitation/RSVP), not assembled from open ticket sales.

## Cross-product Comparison

| Dimension | Eventbrite | Whova | Swoogo | zkipster | Commonality |
|---|---|---|---|---|---|
| Core people object | attendee (from order/ticket) | attendee (from registration) | registrant/attendee (from registration) | guest (from contact + list + RSVP) | same concept, different names |
| Event container | event | event (multi-day) | event (multi-day, packages) | event with sessions | B |
| Roster entry points | self-registration/purchase | registration form | registration form | RSVP forms, import, manual, API | B (intake differs: open vs curated) |
| Roster segmentation | ticket types | attendee/ticket types | registration types | named lists + custom fields/colors | B |
| Check-in recording | QR ticket scan, real-time | name search, QR scan, kiosk | name/QR scan, kiosk, offline | search, QR/barcode, kiosk, offline | B — universal |
| On-site record editing | (on-site sales/registration) | — | walk-in creation, on-spot edits | real-time list/profile updates | B |
| Badge production | not emphasized (tickets are the credential) | badge generation from attendee list | badge designer + on-demand print at door | name badge printing at door | B (not universal — Eventbrite consumes tickets instead) |
| Sub-structures | timed entry, reserved seating | day/session check-in | session/package check-in | sessions with capacity, overbooking, booking rights | B — sub-structures common, shape varies |
| Presence analytics | live attendance, fraud prevention | check-in progress, session attendance, certificates | check-in reports by reg type, VIP alerts | per-list/per-session attendance, arrival times | B |
| Persistent people registry | (contact lists) | CRM/AMS integrations | global attendee record | Audience contact DB | B — persistence layer common in mature products |
| Staff model | organizer app, single organizer role implied | volunteers added as check-in staff | unlimited onsite logins | permissioned team access, hidden sensitive fields | B |
| Ticket inventory / selling | core | adjacent module | adjacent | minimal (payments add-on) | A-level per product, NOT common — varies by philosophy |
| Attendee self-service | transfer tickets, edit registration info | app-based self check-in, profile | kiosk self check-in, pay balance, flag edits | RSVP for self, sign forms | B |

## L0 / L1 / L2 / L3

### L0 — Defining Invariant

An operator-managed roster of identified attendees bound to a specific event, tracking each attendee's attendance state from expected to recorded presence (checked in / attended, or not present), with management actions over that roster (add, edit, find, categorize, mark).

Components:

1. **Event-scoped attendee roster** — identified person records (name at minimum) attached to one event; the population the organizer is responsible for.
2. **Attendance lifecycle per attendee** — at minimum expected vs. recorded-present; real products extend to confirmed/paid, checked in per day/session, no-show, cancelled.
3. **Operator management surface** — organizer-side ability to build, search, view, categorize, edit the roster and record arrivals (check-in).

Why this is minimal: remove the event-scoped roster and the product becomes generic CRM/contact management; remove attendance tracking and it collapses into Event Registration (intake only); remove operator management and it is just an attendee-facing ticket wallet. The paper guest list at the door — a host's list of expected names, checked off as people arrive — already satisfies this definition, which is the historical floor (§24 check passes).

### L1 — Common Mature Structure

Present across most sampled mature products; expected by the market, not definitional:

- **Intake connections** — roster populated from self-registration/RSVP forms, ticket purchases, spreadsheet import, or manual entry (mechanism varies; presence of at least one intake path is common).
- **Roster segmentation** — categorizing attendees by ticket/registration type or named lists (VIP, press, sponsors…); segmentation typically drives badge, access, and reporting.
- **Check-in operations machinery** — QR/barcode or name search, staffed mobile/console check-in, self check-in kiosks, walk-in creation, on-spot record edits.
- **Badge/credential production** — badge design driven by attendee data and category; bulk pre-event print and/or on-demand print at the door (in ticket-first products the ticket itself plays this role).
- **Session/day sub-rosters** — check-in and attendance tracked at day or session level; session capacities with availability behavior.
- **Presence reporting** — attendance counts, arrival times, no-shows, per-category/per-session breakdowns, cross-event comparison.
- **Communication to attendees** — confirmations/reminders/announcements targeted to roster segments; check-in-triggered alerts.
- **Persistent people layer** — contact database / global attendee record underlying repeated events; integrations toward CRM/AMS; deduplication.
- **Team/staff model** — multiple check-in staff/volunteers with scoped access; some products allow hiding sensitive fields.
- **Data in/out** — import/export, APIs.

### L2 — Variant / Optional Structure

Depends on segment, business model, or event format:

- **Open ticketed intake vs. curated invitation intake** (marketplace-style open sales vs. organizer-curated guest lists).
- **On-site payment processing** (walk-in sales, balance settlement at kiosk).
- **Consent/waiver capture tied to the roster or check-in** (common where liability matters).
- **Certificates/qualifications derived from attendance records** (education/association segment).
- **Attendee-facing app surfaces** (agenda, networking, matchmaking) — the roster feeds access, but the app itself is the Event Mobile App Type.
- **Virtual/hybrid attendee handling** — remote attendees as roster members with virtual check-in/engagement; shape varies.
- **Seating/floorplan integration** (banquet-style events).
- **Lead retrieval / exhibitor scanning** — attendee badges as scan targets (boundary object with Event Lead Retrieval Type).
- **RFID / hardware ecosystems** via partners.
- **Privacy regimes** — GDPR-facing data handling, field-level hiding; strength varies by market.

### L3 — Vendor-specific Structure

- Swoogo Go Onsite vs Go Onsite Pro tiering; "Check-In Planner Alerts"; badge printing requiring Wi-Fi; Stripe-specific onsite payments.
- Whova "Speaker Center", announcement wall, gamification, 50+ page post-event report.
- zkipster "Facesheets", guest relationships with RSVP-for-each-other, "Audience" product naming, WhatsApp/SMS invitation channels.
- Eventbrite marketplace positioning, 90M/270M style platform stats (marketing figures).
- Eventbrite ticket-fraud-prevention framing of scanning.

## Vendor-specific Findings

- Per-tier packaging of check-in features (Swoogo Go Onsite Pro: kiosk mode, alerts, onsite payments, custom check-in questions are paid add-ons) — packaging, not structure.
- zkipster's guest-relationship graph (linked guests updating each other's RSVPs) is the richest observed people-relationship model; no other sampled product exposes this.
- Whova derives certificate eligibility directly from attendance records — one observed pattern for post-event value extraction.
- Swoogo's "global attendee record" and zkipster's "Audience" both make the persistent people layer a first-class product surface; Eventbrite/Whova treat it more as a byproduct or integration point.

## Rejected Findings

- "Attendee Management = ticket selling / registration forms" — rejected. zkipster (and the invitation/RSVP tradition) manages attendees with no ticket inventory and no open registration; intake is an input, not the core.
- "Check-in always works via QR/barcode scanning" — rejected. All four sampled products support name search/manual check-in; scanning is the common fast path, not the definition.
- "Attendee records always include payment status" — rejected. Only ticketed/registration-paid flows carry payment state (Eventbrite, Swoogo, Whova); curated guest lists may be fully non-monetary (zkipster).
- "Badge printing is part of the definition" — rejected. Badge production is common but Eventbrite's model (ticket as credential, no badge print emphasized) shows the Type works without it.
- "Multi-day/session structures are universal" — rejected as L0; single-evening guest lists (galas, openings, dinners) are a full member of the Type.

## Boundary Findings

- **vs Event Registration Platform**: registration centers on the intake flow (forms, registration paths, payments); its roster is an output. Remove the roster/attendance tracking from this Type and only the intake flow remains → that is Event Registration. Conversely, remove the form-building/intake machinery and keep roster + check-in → still Attendee Management (zkipster proves this).
- **vs Event Ticketing Platform**: ticketing centers on ticket inventory, pricing, and sales; the person record is a byproduct of the ticket. Selling tickets to the public is not required here (zkipster); conversely ticketing products can exist with minimal per-person management.
- **vs Event Credential / Badge Management**: badges/credentials center on the credential artifact (design, security features, production); the roster feeds it. Badge production is an optional output of this Type, not its center.
- **vs Event Mobile App**: the event app is attendee-facing content/networking/engagement; attendee management is operator-facing roster control. App access is typically derived from the attendee record, but the app is a different Type.
- **vs Event Management Platform**: suites add marketing, websites, agendas, speakers, sponsors, budgets. The attendee-roster slice is what every such suite contains; the suite is broader. Record as a taxonomy note: "Attendee Management" is frequently marketed as a module/capability of suites (e.g., suites advertise attendee management features), but standalone guest-list/check-in products exist (zkipster and peers), so keeping an independent Type is defensible; the Type document should describe the slice, not the suite.
- **vs CRM / Membership Management**: a persistent people registry looks like CRM, but this Type binds people to a specific event with an attendance lifecycle; CRM binds people to a commercial relationship. The persistent people layer (L1) is where the two touch.
- **Naming**: the same structure appears as "guest management", "guest list", "attendee management", "registrant management", "onsite check-in" across vendors — a synonym cluster around one structure.

## Uncertainties

- Exact state vocabularies per product (registered/confirmed/checked-in/no-show/cancelled) were not verified at article level; final document describes lifecycle conceptually without asserting specific state names.
- Whether Cvent / enterprise suites expose materially different structures (e.g., deep badge-security or airport-style re-print workflows) could not be verified — Cvent sources unreachable.
- Depth of attendee self-service mutation (self-editing registration answers, reassignments, name changes) varies by product; only Eventbrite's transfer/edit paths were directly observed from the help-center navigation.
- Offline-mode behavior details (conflict resolution after sync) not researched at operational depth; only existence of offline check-in + later sync was confirmed (Swoogo, zkipster).
- Whether virtual-only attendee management (roster without physical presence) is best modeled as a variant of this Type or as a different Type was left to the boundary notes, not decided.

## Final Synthesis

Attendee Management is the operator-facing Type whose world is: **one event → a roster of identified attendees → each attendee's attendance state tracked from expected to recorded presence → management actions over the roster before, during, and after the event.** The defining core is the roster + attendance lifecycle + operator control (L0). Mature products wrap it in intake connections, segmentation, check-in machinery (staffed, kiosk, offline), badge production, session/day sub-rosters, presence reporting, attendee communications, and a persistent people layer (L1). The rest — payments, waivers, certificates, apps, hybrid, RFID — is segment- or format-dependent (L2), and packaging/naming specifics stay vendor-specific (L3). The Type holds across ticketed and unticketed, curated and open, one-evening and multi-day events; what changes between products is where the roster comes from and how much of the event stack is bundled around it.
