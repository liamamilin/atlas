# Research Notes — Association Event Management

Research date: 2026-09-06
Slug: association-event-management
Directory leaf: Association Event Management (Section 25 — Nonprofit, Membership & Religious Organizations)

---

## Research Goal

Understand what "Association Event Management" software actually is as an Application Type: what objects it manages, how association events are planned, published, registered for, run, settled, and recorded, and — critically — what distinguishes it from a generic Event Management Platform and from an Association Management System (AMS).

## Initial Boundary (hypothesis before research)

- Hypothesis: the distinguishing layer is the association's member registry (member types / status / levels / chapters) acting as the identity, eligibility, and pricing substrate for events, with event outcomes (attendance, credits) written back to member records.
- Neighboring types: Event Management Platform (26), Event Registration Platform (26), Attendee Management (26), Nonprofit Event Management (25), Association Management System / AMS (25), Continuing Education Management (25), Religious Event Management (25), Sponsorship Management.
- Risk: this leaf may be an industry Variant of Event Management Platform. Decision deferred to evidence.

## Research Questions

1. What event types do association products model (annual conference, chapter meeting, seminar, webinar, gala)?
2. How is registration bound to the membership record (login, member pricing, eligibility by member status/type/level)?
3. How do chapters/components relate to events?
4. What does the event lifecycle look like (setup → open → limits/waitlist → run → settle → repeat)?
5. How do CE/CPD credits get recorded back to member records?
6. What roles exist (event staff, chapter admin, finance, volunteers)?
7. Where do exhibitors/sponsors/speakers fit?
8. How do event financials work (fees, invoices, refunds, credits)?
9. Boundary vs generic Event Management Platform vs AMS vs Nonprofit Event Management.

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy | Tier | Customer segment |
|---|---|---|---|
| Wild Apricot (Personify) | membership-first all-in-one; events as a module of the member database | small-staff associations | primary sample |
| EventsAir | event-first enterprise platform; association membership delivered as a special "contact store" event type | enterprise / large conferences | primary sample |
| Cvent | event-first enterprise platform with an "Associations" vertical; AMS integration instead of native registry | enterprise | primary sample |
| Glue Up | association engagement suite (CRM + membership + events + community + chapters + credits) | mid-market, global chambers/associations | primary sample |
| YourMembership (Momentive Software) | AMS with event management as one capability | small/mid associations | secondary (thin docs) |

Avoided: researching multiple products from the same vendor family (Wild Apricot and YourMembership are both under Personify/Momentive umbrella brands but are distinct product lines; treated as separate observations with that caveat).

## Sources

### Wild Apricot (Tier 1 — official help center, articles fetched 2026-09-06)

Help center: https://gethelp.wildapricot.com/ (Elevio KB; article bodies extracted from embedded JSON-LD)

- Event registration process — https://gethelp.wildapricot.com/en/articles/100-event-registration-process
- Event details screen — https://gethelp.wildapricot.com/en/articles/90-event-details-screen
- Limiting event registrations — https://gethelp.wildapricot.com/en/articles/93-limiting-event-registrations
- Event waitlists — https://gethelp.wildapricot.com/en/articles/3-event-waitlists
- Multi-session events — https://gethelp.wildapricot.com/en/articles/92-multi-session-events
- Event attendance — https://gethelp.wildapricot.com/en/articles/34-event-attendance
- Canceling and deleting events and registrations — https://gethelp.wildapricot.com/en/articles/104-canceling-and-deleting-events-and-registrations
- Events tab (on contact record) — https://gethelp.wildapricot.com/en/articles/144-events-tab
- Event emails overview — https://gethelp.wildapricot.com/en/articles/31-event-emails-overview
- Part 4 — The Events module (admin training guide) — https://gethelp.wildapricot.com/en/articles/2898-part-4-the-events-module
- EventRegistrationTypes admin API call — https://gethelp.wildapricot.com/en/articles/500-eventregistrationtypes-admin-api-call

### EventsAir (Tier 1 — official help center, fetched 2026-09-06)

Help center: https://help.eventsair.com/ (Intercom)

- Membership Management (Membership Contact Store event type) — https://help.eventsair.com/en/articles/9564241-membership-management-membership-contact-store-event-type
- Attendee management - Overview — https://help.eventsair.com/en/articles/9564042-attendee-management-overview
- Detailed How-To Guides collection (article index) — https://help.eventsair.com/en/collections/10818886-detailed-how-to-guides

### Cvent (Tier 2 — official product/marketing pages, fetched 2026-09-06)

- Event Marketing & Management (platform root) — https://www.cvent.com/en/event-marketing-management
- Cvent for Associations — https://www.cvent.com/en/event-marketing-management/association-solutions
- Knowledge Base exists at https://support.cvent.com/s/knowledgebase (Salesforce Lightning portal; not article-fetched in this pass)

### Glue Up (Tier 2 — official product pages + help center structure, fetched 2026-09-06)

- All-in-one Association Management Software (root) — https://www.glueup.com/
- Event Management Software for Associations & Chambers — https://www.glueup.com/event-management-software
- Help center structure (Zendesk categories: Contacts / Events / Membership / Campaigns / Finance / Community / Chapter Management / Website / Mobile Apps / Payment Gateways / API) — https://help.glueup.com/
  - Event Module Guide article body did not render (gated/JS); not used for operational detail.

### YourMembership (Tier 2 — root page only, fetched 2026-09-06)

- Association Management Software root — https://www.yourmembership.com/
  - Deeper product pages returned 403 (bot protection); not retried per network rules. Role in sample: confirms AMS-with-events positioning only.

### Access limitations

- Community Brands (NetForum) product page returned 403; dropped from sample.
- Cvent operational help center (Salesforce-portal KB) not article-fetched; Cvent claims stay at product-page strength.
- Glue Up Event Module Guide body not accessible; Glue Up operational claims stay at product-page strength.
- No pricing, numeric limits, or plan-gated details were used from memory; all precise mechanics below come from fetched pages.

---

## Product A — Wild Apricot (membership-first, small associations)

Evidence layer: A (direct observation, official help articles)

### Key observations

**Event setup & types**
- Two complexity classes: simple events (RSVP only) and advanced events (custom fees, ticket types, multiple sessions, extra event costs).
- Event details screen: title + start date required to save; location, description (rich text), tags, event URL; "Allow registration" toggle; visibility control.
- Multi-session events: sessions on different days, manual or repeating schedules (weekly/monthly patterns), per-session reminders, per-session check-in; documented cap of 120 sessions per event (product-specific number).
- Copying an event (including its emails) — supports the annual recurrence pattern.

**Membership registry as substrate**
- Visibility: event can be Admin only, Public, or Restricted to selected membership levels and/or member groups. Restricted events appear only on calendars of members with granted levels.
- Individual ticket types can be restricted by membership level.
- Registration form auto-fill: common fields auto-filled for existing contacts even when not logged in; membership fields and member-only fields auto-filled when logged in.
- Contact record has an "Events tab": all of a contact's event registrations (date, event, ticket type, amount, invoice status) + "Record event registration" button for manual registration.
- People not in the database who register are added as contacts and emailed login credentials; they can then apply for membership. Guest registration optionally adds guests to the contact database.

**Ticket types & pricing**
- Advanced events require ≥1 ticket type before registration can open. Ticket types carry price, registration limits, waitlist option, member-level restriction, self-cancel option.
- "Disable multiple registrations for the same contact" per-event option.

**Capacity & waitlist**
- Registration limits per event and per ticket type; when reached, registration auto-closes and organizer is emailed; spaces-left shown on public calendar (hideable via CSS).
- Waitlists per event or per ticket type; automatic promotion (in order, guests considered, invoice auto-generated) or manual promotion; information collected from waitlisters configurable (name/email → full registration form).

**Registration flow (public site)**
- Enter email (pre-filled if logged in) → choose ticket type → registration form + event options (e.g., meal preference, sessions) → registration record created → payment path depends on event setup: offline (Confirm → invoice emailed), online (Pay online → payment provider), or both (Pay online / Invoice me).
- One person can register and pay for multiple attendees (before paying).
- Registrants see their registrations under "My registrations" on their member profile; can self-cancel if enabled for their ticket type.

**Money**
- Registration generates an invoice; partial payments supported; extra charge line items can be added later.
- Auto-cancel option: registrations unpaid after 15 minutes are automatically canceled (product-specific default window).
- Cancel vs delete: canceled registration stays in list and can be restored; deleted registration is removed; invoice auto-voided; paid fees become account credits (not automatic refunds); refunds issued via payment processors (Authorize.net, Stripe, PayPal Checkout, Personify Payments, 8am AffiniPay) or recorded manually.
- Deleting an event deletes its invoices (kept in financial history); paid fees remain as credits; deleted events cannot be restored; "archiving" = admin-only visibility + registration disabled.

**Check-in / attendance**
- Check-in from browser (registrants list) or admin mobile app; QR code in confirmation email (via {QR_Code} macro) scanned at door; unpaid registrations flagged (check in with/without payment choice); wrong-event or invalid QR handled with messages; guests checked in individually.
- Attendance count and percentage shown per event; printable attendance report; follow-up emails can target checked-in vs not-checked-in registrants.

**Event emails**
- Per-event: Announcements (up to 3; targeted to all contacts / members by level or group / past attendees / saved searches / non-members; excludes already-registered), Reminders (up to 3; registrants incl. unpaid + guests), Follow-ups (up to 3; all registrants / checked-in only / not checked in), Registration confirmed / pending / canceled, New waitlist registration, Invoice, Receipt.
- Timing rules documented (e.g., pending email after 15 minutes for online-payment registrations); scheduled relative to event local time.
- New events copy emails from the copied event or from organization defaults; macros for personalization.

**Roles**
- Full administrators and "event managers" can check in attendees (role distinction documented).

## Product B — EventsAir (event-first platform; membership as a contact store)

Evidence layer: A (direct observation, official help articles)

### Key observations

**Membership as a special event type**
- "Membership Contact Store" is a distinct event type (one per association/client) that carries a Membership module; used to deliver ongoing membership services: dues collection (fixed annual date or member anniversary), member contact data, invoices/receipts, payment & cancellation schedules, member discount codes, communications, forms, event invitations + attendance tracking, self-service member portal, CE/professional development management, merchandise.
- Member statuses computed by the system: Financial Members (paid current year), Non-Financial Members (renewed but unpaid), Non-Current Members (lapsed/canceled), Non-Members (in database, never members). These statuses drive renewal/cancellation Express Actions.
- Membership categories (Full, Student, Non-Member, honorary life, etc.) each require ≥1 fee type; fee types are one-time or recurring (anniversary-based or fixed annual date, with pro-rata option).

**Events linked to the member store**
- A regular event can be linked to a Member Contact Store; the link is permanent once made.
- Linked events can send invitations to member contacts with Auto Login Tokens (pre-authenticated links).
- **Registration Types in linked events can be restricted by Member Status** — "You can choose which Member Status(es) can select this specific Registration Type."
- **Event attendance is recorded on the member's contact record** in the Member Contact Store.

**Member Portal**
- Self-service: apply/renew, update details, view schedule, search CE classes, calendar of functions/courses/events, purchases (courses, memberships, merchandise), past purchases, event history, credits page with certificate printing.
- Portal page access filterable by any field in the store (public pages, member-only pages, category-specific pages).

**CE Courses**
- CE Courses module (also as CE Course Contact Store): ongoing scheduled classes and one-time classes/seminars; displayed in Member Portal; purchase, history, credits and certificates of completion.

**Attendee management (generic event side)**
- Attendee record aggregates modules: Registration, Accommodation, Travel, Agenda, Functions, plus (when applicable) Presentations (speaker/reviewer), Exhibitions, Sponsorship, CE Courses/CE Credits.
- Financials per attendee: payments, refunds, invoices, receipts, audit trail, miscellaneous charges.
- Attendee tools: cancel (all or selected items), replace attendee, name badge, online activity log, site auto-login, change log, delete or anonymize.
- Exhibitor lead management, sponsorship management, meetings/matching tools exist as separate guides.

## Product C — Cvent (event-first enterprise; association vertical)

Evidence layer: A for page existence/claims (Tier 2 product page); no operational articles fetched.

### Key observations

- Dedicated "Cvent for Associations" page: positioning is "Grow your membership with the right event technology" — events drive registrations, membership renewals, and sponsorship revenue.
- Association-specific claims on the page:
  - "Integrate your tech stack for fast membership authentication" (membership check at registration).
  - "Track and award continuing education credits across all events."
  - AMS integration ("Integrate with your association management software"; Salesforce app shown).
  - Chapters in practice: customer story "30+ events hosted for 375 chapters" (American Marketing Association).
  - Sponsors/exhibitors: mobile app notifications, downloadable content, one-on-one appointment scheduling between attendees, sponsors, exhibitors.
  - Speaker management hub; check-in and on-demand badge printing; replicated event websites/communications/branding.
- Platform breadth (from root page): registration & marketing, event app, check-in & badging, attendee hub, virtual/hybrid, webinars, reporting/insights, surveys, lead retrieval.
- 4.2K+ association and non-profit customers claimed.

## Product D — Glue Up (association engagement suite)

Evidence layer: A for page existence/claims (Tier 2 product pages + help center structure); operational article body not accessible.

### Key observations

- All-in-one association management software: modules = CRM, Events, Email Campaigns, Community, Memberships, Finance & Invoicing, CPD & CPE Credits, Tasks, Surveys, Website, Chapter Management, Mobile Apps, Payment Gateways, API.
- Events module positioning: "registration, payments, email campaigns, check-in, attendee data, CRM, mobile apps, and reporting together… in-person, virtual, and hybrid."
- "Track registrations, attendance, and access in one flow, with participation data automatically linked to member records."
- "Membership CRM Sync"; "complex pricing, access rules"; registration templates/blueprints; multi-language.
- Chapter Management: "Unified Dashboard, Consolidated Membership Data, Granular Control of Permissions, Shared Event Calendar" — chapters run events under shared data and permissions.
- CPD & CPE Credits module: "Manage and scale up your trainings and certification courses"; custom credit types, automatic approvals, certificates (product-update posts).
- Two apps: Manager app (staff: check-in, badges, real-time attendance) and My Glue app (attendees: agenda, speaker bios, materials, networking, digital business card).
- Monetization: registration fees, paid webinars, extra items, donations; sponsor/exhibitor premium branding.
- Engagement scoring: "Turn event activity into measurable engagement insights that inform follow-up, retention, and future programming"; event data "stored in individual CRM".
- Accounting integrations (QuickBooks, Xero, Sage Intacct); payment gateways (Stripe, Paygage); Zoom and Cvent integrations.

## Product E — YourMembership (AMS with events)

Evidence layer: A for page existence (Tier 2, root page only).

### Key observations

- AMS positioning for small/mid associations ("all-in-one AMS"); capability list includes "Event management — Easily create, host, and manage your association's events" and a Mobile Event App, plus LMS, job board, online community, website design.
- Confirms the AMS-with-events-module pattern; no operational event detail accessible (403 on deeper pages).

---

## Cross-product Comparison

| Dimension | Wild Apricot | EventsAir | Cvent | Glue Up | YourMembership |
|---|---|---|---|---|---|
| Association person registry | Native contact DB with membership levels & groups | Membership Contact Store (special event type) with member statuses & categories | External AMS integration; "membership authentication" | Native CRM/Membership module | Native AMS |
| Member-conditioned registration | Ticket types restricted by membership level; event visibility by level/group | Registration Types restricted by Member Status | Claimed: fast membership authentication | Claimed: access rules + member record linkage | AMS-native (asserted, thin) |
| Non-member handling | Registrant added as contact; can apply for membership | Non-Member status in store | Prospects/guests (implied) | Contacts in CRM | Contacts |
| Event lifecycle | Setup → allow registration → limits/waitlist → run → check-in → follow-up; cancel/delete/archive | Setup → registration → onsite → post-event; cancel/postpone guides | Plan → promote → run → measure | Create → promote → register → check-in → follow-up | Create → host → manage |
| Sessions/agenda | Multi-session events, repeating schedules | Agenda module, functions | Agenda management, speaker hub | Agenda in attendee app | Mobile event app |
| Check-in | Browser + admin app + QR; unpaid flag | Onsite portal, check-in/out, badges | Check-in & badging product line | Manager app check-in, badges | Mobile event app |
| Money | Invoices, partial payments, credits, refunds via processors, auto-cancel unpaid | Attendee invoices/payments/refunds/credit notes; EventsAir Pay | Registration fees; sponsorship revenue | Finance & invoicing module; payment gateways | AMS billing |
| CE credits | Not observed in events docs | CE Courses module + credits + certificates | Claimed across all events | CPD/CPE credits module | LMS adjacency |
| Chapters | Member groups (approximation) | Per-association stores (no chapter object observed) | Customer story: 375 chapters | Chapter Management module + shared event calendar | Not observed |
| Sponsors/exhibitors | Not observed | Exhibitions, Sponsorship modules, lead retrieval | Sponsor/exhibitor mgmt, appointments | Sponsor/exhibitor branding | Not observed |
| Member self-service | My registrations tab; event calendar gadgets | Member Portal (join/renew/history/credits) | Event apps | My Glue app; event calendar | Member portal (asserted) |
| Repeatability | Copy event incl. emails | Event copies/templates | Replicated event websites | Registration templates/blueprints | Not observed |
| Event email targeting | By membership level/group/past attendance/check-in state | Merge docs, auto-login tokens | Marketing automation | Branded invitations, automated notifications | Not observed |

### What is universal across the sample (Layer B)

1. Events are run by/for the association as part of a member-facing program (calendar of offerings, not one-off campaigns).
2. Registration binds to an identified person record in the association's database; membership standing is known at registration time.
3. Membership standing conditions registration — visibility, eligibility, and/or price differ for members vs non-members (implemented as member-level-restricted ticket types, member-status-gated registration types, or membership authentication).
4. Registration carries a tracked lifecycle (registered → confirmed/paid → attended/canceled) with money attached (invoice/payment/refund/credit).
5. Attendance/outcomes are recorded and remain attached to the person's record (Events tab, member contact record, member CRM record, portal history).
6. Non-member registrants flow into the association database as contacts/prospects.
7. Communication is lifecycle-driven (announcement → reminder → confirmation → follow-up) and targetable by membership attributes and attendance state.
8. Events recur annually/seasonally; products support copying/templating.

### What varies (Layer B→C gradient)

- Where the registry lives: native module (Wild Apricot, Glue Up, YM) vs special store inside an event platform (EventsAir) vs external AMS integration (Cvent).
- Chapter support: first-class module (Glue Up) vs approximated by groups (Wild Apricot) vs customer-story evidence only (Cvent).
- CE credits: dedicated module (EventsAir CE Courses, Glue Up CPD/CPE) vs platform claim (Cvent) vs absent from events docs (Wild Apricot).
- Conference-scale machinery (exhibitors, sponsors, speaker hubs, appointments, lead retrieval): present in event-first platforms; minimal in small-association tools.
- Scale of check-in machinery: QR/app check-in (Wild Apricot) vs onsite portal + badging product line (EventsAir, Cvent).

---

## Canonical Model (synthesis)

### L0 — Defining Invariant (minimal)

Association Event Management is event management performed **on top of an association's person registry**, such that:

1. **Association-governed event program** — events exist as offerings of the association (or its chapters) on a managed calendar, not as one-off campaigns.
2. **Registration bound to an identified person record with known membership standing** — every registration attaches to a persistent person record in the association's database, where the person's membership standing (member status/type/level, or non-member) is known at registration time.
3. **Membership standing conditions the registration** — who can see/register and/or at what price is determined by membership standing (at minimum: member vs non-member distinction).

Remove #1 → generic event/campaign tooling. Remove #2 → anonymous event registration (generic Event Registration Platform). Remove #3 → event management with a CRM attached, but not association event management. These three are the smallest set that keeps the Type recognizable.

Historical/market-sample check (§24-style): older and smaller-association practice (paper/PDF registration forms cross-checked against a membership list, member vs non-member price lists, attendance marked in the member record) satisfies all three invariants without any modern machinery (QR check-in, waitlists, mobile apps, CE modules). Modern implementations are L1, not L0.

### L1 — Common Mature Structure

- Registration/ticket types with per-type pricing, limits, and member-conditioned availability
- Capacity limits and waitlists (auto or manual promotion)
- Custom registration forms; guest registration; group/multiple-attendee registration
- Lifecycle event emails: announcements, reminders, confirmations, cancellation, follow-ups — targetable by membership attributes and attendance state
- Check-in/attendance tracking (list, app, QR/badge), attendance reporting
- Money: invoices, online/offline payment, partial payments, refunds/credits tied to registration
- Public/member event calendar and event detail pages; member self-service ("my registrations", portal event history)
- Sessions/agenda for multi-part events; copying/templating events for recurring cycles
- Reporting: registration, attendance, revenue
- CE/CPD credit awarding from event/session attendance (professional associations)
- Sponsors/exhibitors/speakers for conference-scale events
- Mobile event apps (attendee + staff)

### L2 — Variant / Optional Structure

- Chapter/component event governance (chapters run own events under shared calendar/permissions/brand)
- Registry substrate: native module vs external AMS integration vs store-inside-event-platform
- Fundraising-shaped events (galas, auctions, donations) overlapping nonprofit practice
- Virtual/hybrid delivery and webinar-style events
- Engagement scoring / member engagement metrics derived from event participation
- Travel/accommodation/room blocks; abstracts/presentations management (academic/professional conferences)
- Discount/promo codes; merchandise sales
- Member discount codes tied to membership categories

### L3 — Vendor-specific (research notes only)

- EventsAir: Membership Contact Store as an event type; Financial/Non-Financial/Non-Current/Non-Member statuses; Express Actions (Membership Renewals, Non-Financial Member Cancellations); Auto Login Tokens; permanent event↔store link; CE Course Contact Store; Member Portal page-level access filters.
- Wild Apricot: simple vs advanced event classes; 15-minute auto-cancel default; {QR_Code} macro; 120-session cap; Personify Payments / 8am AffiniPay refund paths; CSS-level hiding of spaces-left; "event managers" admin role.
- Cvent: OnArrival check-in/badging, CventIQ, Supplier Network, speaker management hub, Cvent Essentials (repeatable events).
- Glue Up: Manager app / My Glue app split; chapter rebate payments; Oasis LMS integration; Paygage/Stripe gateways.

---

## Vendor-specific Findings

See L3 above. None of these were promoted into the canonical model. The EventsAir member-status vocabulary (Financial/Non-Financial/Non-Current/Non-Member) is vendor-specific, but the underlying concept — a computed membership standing that gates registration — is cross-product (Wild Apricot membership levels/groups; Cvent membership authentication) and appears in L0/L1 as "membership standing".

## Boundary Findings

1. **vs Event Management Platform (26)**: shares the event substrate (event, registration, attendee, agenda, check-in, payments). The distinguishing layer is the association registry: person records with membership standing, member-conditioned eligibility/pricing, and outcomes persisted to member records. **Test: remove the membership registry and member-conditioned access/pricing → the product is a generic Event Management Platform.** Conversely, a generic event platform with deep AMS integration can serve association events — the Type is defined by the capability pattern, not by the module boundary.
   - Taxonomy note: this Type could arguably be modeled as a membership-governed Variant of Event Management Platform. The directory keeps them separate; documented as-is, with the relationship made explicit in the final document.
2. **vs Association Management System / AMS (25)**: the AMS is the registry (dues, renewal, member lifecycle, member data). Association Event Management consumes that registry to run events. Products ship both; if the event capability is removed, what remains is an AMS, not this Type.
3. **vs Nonprofit Event Management (25)**: nonprofit events center on donors and fundraising (galas, auctions, donations); association events center on members and member value (conferences, education, CE, community). Overlap exists (associations fundraise; nonprofits hold member events); the registry identity (donor vs member) and primary goal (mission revenue vs member program) separate them.
4. **vs Event Registration Platform (26)**: registration-only surface without the association program/registry layer.
5. **vs Attendee Management (26)**: the per-attendee/on-site slice of event operations; association event management spans the whole program and adds the registry layer.
6. **vs Continuing Education Management (25)**: CE management is the credit/certification system of record; association events are one common source of credits. Credit awarding appears here as a common capability, not the defining one.
7. **vs Religious Event Management (25)**: sibling pattern with a different registry (congregation) and different event shapes (worship, ministry scheduling); same abstract structure (community registry + events) but different users, objects, and rules.

## Uncertainties

- Exact CE credit mechanics (credit types, approval flows, certificate generation) verified only at Tier 2 for Cvent/Glue Up and by module existence for EventsAir; not deep-read.
- Chapter event governance details (approval flows, shared calendars, rebate economics) rest on Glue Up Tier 2 pages and a Cvent customer story; treat as common-but-not-precisely-verified.
- Whether member-vs-non-member pricing is universal: strongly suggested across the sample (member-level ticket types, member-status registration types, membership authentication), but the final document phrases it as "commonly" rather than "always".
- YourMembership event mechanics unverified (403); used only to confirm the AMS-with-events pattern.
- Wild Apricot CE credit support not observed in its events docs; absence of evidence, not evidence of absence.

## Final Synthesis

Association Event Management is best understood as **event management whose identity, eligibility, pricing, and record-keeping layers are the association's membership registry**. The event substrate (event → registration → attendee → check-in → money → communication) is shared with generic event management; what makes this Type distinct is that (a) events are offerings of a governed member organization and its chapters, (b) every registration binds to a persistent person record whose membership standing is known, (c) membership standing conditions access and price, and (d) participation persists on the person's record, feeding member history, continuing-education credits, and engagement views. Products implement this either as membership-first suites (registry at the center, events as a module), event-first platforms with an association registry store or AMS integration, or AMSs with event modules — the capability pattern is stable across all three shapes.
