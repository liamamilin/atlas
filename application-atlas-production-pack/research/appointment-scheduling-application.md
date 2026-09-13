# Research Notes — Appointment Scheduling Application

Research date: 2026-09-06

## Research Goal

Understand how real appointment-scheduling products work: what objects they manage, how bookable availability is produced, how a client books, how the appointment travels through its lifecycle, which rules govern booking, and where the boundary lies against Meeting Scheduling, Group Availability Scheduling, Calendar Applications, appointment-based service business management, and Patient Scheduling.

## Initial Boundary

Initial hypothesis (before research):

- The leaf sits in Directory §03.09 Scheduling with two siblings: Meeting Scheduling Application and Group Availability Scheduling Application. The family signature appears to be "publish availability → another party books a time".
- Closest neighbors to test against:
  - **Meeting Scheduling Application (03.09 sibling)** — same booking-link machinery, but meeting semantics (event types as meeting templates, invite distribution) vs service semantics (service catalog, client records, policies).
  - **Group Availability Scheduling Application (03.09 sibling)** — poll-based time-finding for a group, no persistent booking system.
  - **Calendar Application (03.08)** — manages the user's own time; no external booking machinery.
  - **Appointment-based Service Business Management (§29, already processed)** — the sibling research drew a removal test: "remove checkout + client ledger → appointment scheduling application remains". This leaf is that scheduling machinery.
  - **Patient Scheduling (§22)** — regulated clinical variant.
  - **Employee Scheduling Platform (§09, already processed)** — schedules staff shifts, not client appointments.
- Working assumption: the defining core is client-initiated booking into provider-published, availability-derived slots, producing a persistent appointment record.

## Research Questions

1. What objects make up the system's world? (service/appointment type, provider, client, appointment, resource, booking page...)
2. How is bookable availability produced? (working hours, special days, per-service/per-provider schedules, intersection logic, buffers, external calendar busy-checking)
3. How does client self-booking work, and what does the operator-side booking flow look like?
4. What is the appointment lifecycle (book → confirm → reschedule/cancel → complete/no-show), and who can change it?
5. Which booking rules exist (lead time, scheduling window, slot interval, capacity, cancellation windows)?
6. Which capabilities are common but not defining (reminders, payments, intake forms, client records, calendar sync, classes, packages)?
7. Where is the boundary against Meeting Scheduling, Calendar, service-business management, and Patient Scheduling?
8. Would older / regional / platform-native products still fit the definition?

## Representative Products

| Product | Segment / philosophy | Customer tier | Why selected |
|---|---|---|---|
| Acuity Scheduling (Squarespace) | Standalone appointment scheduler for service businesses; client-experience-first | Solo → multi-location | Best-documented scheduling core; explicit Calendly comparison page for boundary evidence |
| SimplyBook.me | Standalone, feature-rich, international; modular "Custom Features" | Solo → enterprise; strong non-US presence | Different philosophy (modular feature system, marketplace posture, cluster/multi-branch) |
| Setmore | SMB appointment scheduling with free tier | Solo → small teams | Cleanest documented appointment model ("3 elements") and booking-policy set |
| Microsoft Bookings | Platform-native scheduler inside Microsoft 365 / Teams / Outlook | Organizations on M365 | Platform-native sample for the historical/market-sample check |
| Calendly | Link-first scheduling; meeting-centric but widely used for appointments | Individuals → enterprise | Boundary-straddling sample; shows where the Type dissolves into Meeting Scheduling |

Notes on sampling: 10to8, Bookeo, Fresha, Booksy, Square Appointments were candidates. Square Appointments was already sampled in the sibling research (appointment-based-service-business-management) as the payments-platform bridge product; Fresha/Booksy are marketplace-first salon platforms closer to the §29 sibling. The five selected cover standalone/service-business/international/platform-native/link-first positions.

## Sources

Tier 1 (official operational documentation), fetched 2026-09-06:

- Acuity Scheduling Help Center (Zendesk, help.acuityscheduling.com):
  - Help center home (category/section structure): https://help.acuityscheduling.com/hc/en-us
  - Categories API: https://help.acuityscheduling.com/api/v2/help_center/en-us/categories.json
  - Setting up appointments and classes: https://help.acuityscheduling.com/hc/en-us/articles/29338604120717-Setting-up-appointments-and-classes
  - Limit when clients can book, edit, or cancel their appointments: https://help.acuityscheduling.com/hc/en-us/articles/27141282369037-Limit-when-clients-can-book-edit-or-cancel-their-appointments
  - Section/article listings for "Services, classes, and add-ons" and "Set your hours and availability" (titles observed via sections/articles API)
- SimplyBook.me Help Center (MediaWiki, help.simplybook.me):
  - Help Center TOC: https://help.simplybook.me/
  - Brief overview of the system: https://help.simplybook.me/index.php/Brief_overview_of_the_system
  - How to set my availability: https://help.simplybook.me/index.php/How_to_set_my_availability
  - How to manage bookings: https://help.simplybook.me/index.php/How_to_manage_bookings
- Setmore Support (Intercom, support.setmore.com):
  - Support home (category structure): https://support.setmore.com/
  - Sitemap (article inventory): https://support.setmore.com/sitemap.xml
  - Book, Reschedule, or Cancel an Appointment: https://support.setmore.com/en/articles/490875-book-reschedule-or-cancel-an-appointment
  - Double booking: https://support.setmore.com/en/articles/490878-double-booking
  - Booking lead, slot size, advance or cancellation time: https://support.setmore.com/en/articles/491024-booking-lead-slot-size-advance-or-cancellation-time
- Microsoft Learn — Microsoft Bookings overview: https://learn.microsoft.com/en-us/microsoft-365/bookings/bookings-overview
- Calendly Help Center (Zendesk, help.calendly.com): home page with inline quick-answer articles (calendar connections, embed options, availability fine-tuning, meeting limits, buffers): https://help.calendly.com/hc/en-us

Tier 2 (official product pages), fetched 2026-09-06:

- Acuity Scheduling homepage: https://www.acuityscheduling.com/
- Acuity vs Calendly comparison page: https://www.acuityscheduling.com/compare/acuity-vs-calendly
- Setmore homepage: https://www.setmore.com/
- Calendly features page: https://calendly.com/features

Access limitations:

- microsoft.com product pages blocked the fetcher ("request has been blocked"); the first learn.microsoft.com URL tried (microsoft-bookings/bookings-overview) returned 404; the microsoft-365/bookings/bookings-overview path succeeded. Deeper Bookings support articles (support.microsoft.com) were not fetched; Bookings assertions are kept at structure level.
- support.squarespace.com help center is a JS shell; Acuity's separate Zendesk help center (help.acuityscheduling.com) was used instead.
- SimplyBook.me "Adding services and providers" page URL 404'd once; equivalent structure was captured from "Brief overview of the system" and "How to set my availability"; no retry loop.

## Product Observations

### Acuity Scheduling (evidence layer: A — direct observation of Tier-1 help center)

- **Appointment types** ("represent the different services clients can book with you... vary in duration or price, and group them into categories"); intake form attachable to an appointment type; public vs private appointment types (private = bookable only via direct link); add-ons; group classes ("a type of appointment that allows multiple clients to join at the same time", with per-session capacity and series); class series.
- **Booking flow (client side)**: "Clients can book an appointment from your scheduling page. They can choose an appointment type, select a calendar if you have more than one, then pick the time slot that works for them. You can also have your clients enter their payment information before completing the booking process. They'll receive a confirmation email."
- **Booking flow (operator side)**: "You can also book appointments for clients in Acuity" — staff-side booking is a first-class alternative.
- **Availability**: basic availability settings; multiple calendars ("Adding and managing calendars", "Pooling calendar availability"); availability and scheduling limits **by appointment type**; blocking off unavailable time; padding between appointments; repeating hours; resources ("Use resources to limit bookings"); appointment locations; overlapping appointments / double booking; "look busy" / "minimize gaps" display settings.
- **Scheduling limits** (global + per calendar/availability group): minimum hours before start time that appointments can be booked; maximum days in advance; whether clients can reschedule/cancel and how close to the appointment time; edit intake forms window; start-time intervals; appointments per time slot; max appointments/hours per day or week; scheduler time zone display.
- **Calendar panel**: Day/Week/Month views, calendar filters, edit/reschedule/cancel from the appointment detail, labels.
- **Payments**: connect Stripe, Square, or PayPal; collect payments online, in person, or after booking; invoices and receipts; refunds/adjustments handled in the processor; packages, gift certificates, subscriptions, discounts/coupons.
- **Clients**: client list, client accounts, block clients; intake form responses; appointment notes; appointment history.
- **Communications**: automated client emails, text reminders, internal notifications and daily appointment summaries.
- **Integrations**: external calendar sync (Outlook, Google, iCloud), video conferencing, email marketing, CRM, accounting; analytics/conversion tracking.
- **Other**: staff management ("Add and manage staff"); advanced workflows (waitlists, appointment requests, multi-day and overnight appointment types, time-window based appointments, drop-off/pick-up); industry-specific solutions; HIPAA compliance options; enterprise tier; reports and client reviews.
- Positioning (Tier 2): "Book appointments, take payments, and automate the busywork"; industries: beauty, business services, wellness, fitness, arts, education; "250,000+ businesses". Comparison page positions Acuity against Calendly on "brand control, client log-in, and flexible payment options" — i.e., the appointment/client-experience pole.

### SimplyBook.me (evidence layer: A — direct observation of Tier-1 help center)

- **Two surfaces created at registration**: admin interface (operator-only) and booking page (client-facing: "There, they can book your services and leave contact info").
- **Admin structure**: Dashboard (statistics); Calendar (add/edit/delete bookings, break times); Manage (Services, Service Providers, Clients, Users; plus feature-gated sections: Classes, Packages, Membership, Service add-ons, Products for sale, Coupons and gift cards, Related resources, Intake forms, Client fields, News, Status, Flexible notifications, Book soon notification, Calendar note types, Calendar sync, Online video meetings, Taxes); Reports (booking details with filters by service/provider/client/date); Custom Features (modular enable/disable system); Settings (company opening hours, provider schedules, service schedules, general options, widgets); Plans & Prices.
- **Availability model** (documented in detail): company opening hours (weekly) + Special days (by date, company or provider level, with "Is working day?" toggle and group date selection); per-service schedules; per-provider schedules; **intersection rule**: "If you have both schedules for services and for providers, then only intersection of available time for service and for provider will be available for booking"; providers'/services' hours must be within company opening hours; slot interval; break times; buffer time; "Book days" (whole-day bookings); Events (services on particular dates); recurring services (packs).
- **Booking management**: book from admin calendar (click/drag a slot → pop-up form: select or add client, choose provider and service/class, set start/end; optional "Receive payment" to generate invoice at admin booking); edit bookings (drag-and-drop to reschedule; comments; view other bookings of the same client); cancel (admin side, or client side via the cancel link in the confirmation email or the "My bookings" tab on the booking website); cancelled bookings cannot be edited; "Client Rescheduling" custom feature lets clients change date/time themselves; "Cancellation Policy" custom feature can prohibit client cancellation.
- **Booking website**: design/layout adjustment, add/remove elements, categories and locations, additional questions on the Details step, client mobile application, accepting payments, client invoices.
- **Marketplace**: BooKing.Page ("How to list your services on our marketplace").
- **Integrations**: widgets for your own website, Facebook/Instagram booking, WordPress, custom domain, Google/Outlook calendar sync, Google Meet online appointments, SBPay.me payments, API/REST.
- Positioning: "Popular Appointment Booking System Scheduler"; cluster solution for multi-branch.

### Setmore (evidence layer: A — direct observation of Tier-1 help center)

- **Appointment model (direct quote)**: "There are 3 elements to every appointment: the provider, service, and customer."
- **Booking (operator side)**: click an open calendar slot → select service or class → choose provider → choose time slot → select customer (search existing or add new) → Create → "email confirmations (if activated) will be fired out".
- **Reschedule**: edit appointment (change date/time, also service or provider) or drag-and-drop to a new slot with confirmation.
- **Cancel**: delete from the calendar.
- **Double booking**: "By default, Setmore doesn't allow multiple appointments... in the same time slot"; can be enabled by admins; "Double-booking does not extend to your Booking Page. Customers cannot schedule an appointment in an occupied time slot"; does not extend to recurring appointments/classes.
- **Booking policies** (Settings > Booking Page > Booking policies): **lead time** (notice required before an appointment), **booking slot size** (interval between offered slots, e.g. 30-minute grid across business hours), **scheduling window** (how far in advance customers can schedule), **cancellation policy** (notice required to reschedule or cancel).
- **Structure**: Calendar (18 articles: setup, customization, sync); Appointments (book/reschedule/cancel, recurring, labels, export history); Booking Page (29 articles: setup, customization, sharing); Services & Classes (categories, buffer time, color coding); Team (working hours, breaks, time off, staff order, per-team booking page URLs, login/access); Customers (notes, stats, appointment history, merge, import/export); Payments (Square/Stripe/PayPal, deposits, payment links, cash register, payment history/receipts/refunds); Integrations (40+); Reminders & Notifications (email/SMS, team reminders); Connect (internal messaging); Reviews (Setmore + Google); Account & Plan.
- **Booking page**: custom URL ("can function as a standalone website"), branding, embed on website, QR code, Facebook/Instagram channels, show/hide categories/prices/durations, customer login, direct booking links that pre-select service and team member, hidden services shared via direct link, block customers, language, deactivation.
- **Other**: class booking with payments; recurring appointments; different availability per service; custom time slots; working hours/breaks/time off; income stats on the calendar; mobile and desktop apps.
- Positioning (Tier 2): "24/7 automated online booking, reminders, payments"; FAQ defines the Booking Page vs calendar split ("Your calendar is only visible to you... When you update your availability, it reflects on your Booking Page... Once a booking is confirmed, the details land in your calendar"); industries list includes beauty, medical, legal, tutoring, interview scheduling, tour booking, DMV.

### Microsoft Bookings (evidence layer: A — direct observation of Tier-1 Learn overview; structure level only)

- "Microsoft Bookings makes scheduling and managing appointments a breeze. It helps you schedule and manage appointments with your customers, clients, or colleagues... Bookings includes a web-based booking page, which is integrated with Outlook to optimize your calendar and give your customers the flexibility to book a time that works best for them. Email and SMS text notifications reduce no-shows."
- **Personal Bookings**: "manage your own appointment timeslots... configure and share your availability... set aside time for specific activities by creating meeting types. Once you publish your personal booking page, you can share the link with anyone."
- **Shared Bookings**: "invite your team members and create booking pages... define services, manage staff members, configure schedules and availability, business hours and customize how appointments are scheduled."
- Virtual meetings: each appointment booked as an online meeting creates a unique Teams meeting link.
- Data: customer, staff, service, and appointment details stored in Exchange Online shared mailboxes; compliance policies apply.
- Access: web (book.ms), Outlook and Teams apps; available in Microsoft 365 subscriptions (A/E/F/G/Business SKUs).
- Note: overview explicitly spans "customers, clients, or colleagues" — the platform-native product straddles the appointment/meeting line by design.

### Calendly (evidence layer: A for help-center articles; B for positioning)

- **Event types**: pre-built templates for "one-on-one appointments, multi-host sales demos, or group classes" (features page); event types carry duration, location, description, branding; personal landing page displays all active event types; single event-type booking pages; team event types.
- **Availability**: connect multiple calendars; "Calendly checks your calendar for busy times and adds new meetings to it"; one main calendar for bookings; custom availability schedules; meeting limits (per day/week/month per event type); buffers before/after; start-time increments; free/busy rules (what a meeting takes priority over); time-zone display; Troubleshoot tool explaining why a time is unavailable.
- **Sharing & booking**: booking links shared via email/social/website; embeds (inline, pop-up text, pop-up widget); browser extension; mobile app.
- **Automations & notifications**: reminders and follow-ups; workflows.
- **Team/scale**: team templates, admin controls, routing forms (qualify and route website visitors to the right person), meeting distribution tools (round-robin style), workspaces; SSO/SCIM.
- **Adjacent products**: Contacts (invitee relationship management), Payments (Stripe/PayPal; "How to sell services using meeting packages and payment links"; invoices), Notetaker (meeting recaps), Callie (AI scheduling assistant).
- Positioning (Tier 2): "A better way to book appointments and meetings"; "The #1 scheduling tool trusted by over 20M professionals"; solutions by team: sales, marketing, customer success, recruiting.

## Cross-product Comparison

| Structure | Acuity | SimplyBook.me | Setmore | MS Bookings | Calendly | Evidence layer |
|---|---|---|---|---|---|---|
| Bookable offering catalog (named types/services with duration; categories) | ✔ appointment types + categories | ✔ services (+ classes) | ✔ services & classes (+ categories) | ✔ services (Shared Bookings) | ✔ event types | B |
| Offering carries duration (slot computation) | ✔ | ✔ (+ interval, buffer, breaks) | ✔ (+ slot size, buffer) | ✔ | ✔ (+ buffers, increments) | B |
| Price on offering (optional) | ✔ (vary in duration or price) | ✔ (accept payments) | ✔ (prices shown/hideable) | ◐ (not observed on overview) | ◐ (payments via Stripe/PayPal) | B — optional |
| Availability from working hours + exceptions (special days / date-specific) | ✔ (basic availability, blocking time, repeating hours) | ✔ (opening hours + special days) | ✔ (working hours, breaks, time off) | ✔ (schedules, business hours) | ✔ (custom schedules) | B |
| Per-provider schedules; per-service/per-type availability overrides | ✔ (limits by appointment type; calendars) | ✔ (service + provider schedules + intersection rule) | ✔ (per-team hours; availability per service) | ✔ (staff schedules) | ✔ (per event-type availability) | B |
| External calendar busy-checking / sync to prevent conflicts | ✔ (Google/Outlook/iCloud sync; pooled availability) | ✔ (Google/Outlook sync) | ✔ (1-way/2-way Google/Office365/Apple) | ✔ (integrated with Outlook) | ✔ (busy check + add events) | B |
| Client-facing self-booking surface (page/link/embed) | ✔ scheduling page, embeds, direct links | ✔ booking website, widgets, client app | ✔ Booking Page, embed, QR, direct links | ✔ web booking page (book.ms), Outlook/Teams | ✔ scheduling links, embeds, extension | B |
| Client identity captured at booking (name/contact) | ✔ (+ intake forms) | ✔ (+ client fields, intake forms) | ✔ (+ customer records) | ✔ (customer data stored) | ✔ (invitee name/email; contacts) | B |
| Appointment record binds client × offering × provider × time | ✔ (type + calendar + slot) | ✔ (client + provider + service + times) | ✔ ("3 elements": provider, service, customer) | ✔ (service + staff + time) | ✔ (event type + host + time; invitee) | B |
| Operator-side calendar as working surface (day/week/month; edit/reschedule/cancel) | ✔ (Calendar panel, views, labels) | ✔ (Calendar; drag-drop) | ✔ (Calendar; drag-drop) | ✔ (booking calendar) | ◐ (dashboard/event list; calendar-centric editing less documented) | B |
| Client-side reschedule/cancel (with policy limits) | ✔ (limits on how close to appointment) | ✔ (email link / My bookings; policy feature) | ✔ (cancellation policy window) | ◐ (not observed at overview level) | ◐ (invitee can cancel/reschedule via confirmation; not directly observed) | B |
| Booking rules: min notice (lead time) / max advance (scheduling window) | ✔ (min hours before, max days ahead) | ◐ (interval/buffer documented; lead/window not directly observed) | ✔ (lead time + scheduling window) | ◐ (not observed) | ✔ (meeting limits; "prevent last-minute appointments") | B |
| Per-slot capacity / max bookings per day/week | ✔ (appointments per slot; max per day/week) | ◐ (not directly observed) | ◐ (class capacity; double-booking off by default) | ◐ (not observed) | ✔ (meeting limits per day/week/month) | B |
| Automated confirmations/reminders (email/SMS) | ✔ (emails, texts, internal notifications) | ✔ (notifications, flexible notifications) | ✔ (email/SMS, team reminders) | ✔ (email and SMS reduce no-shows) | ✔ (reminders/follow-ups) | B |
| Payments at booking (processor integration; deposits) | ✔ (Stripe/Square/PayPal; pay before booking) | ✔ (Accept payments; SBPay.me; taxes) | ✔ (Square/Stripe/PayPal; deposits) | ◐ (not observed) | ✔ (Stripe/PayPal; packages; invoices) | B — common, not universal |
| Client records/history (persistent client database) | ✔ (client list, history, notes, block) | ✔ (Clients section; import) | ✔ (notes, stats, history, merge) | ✔ (customer data in mailbox) | ✔ (Contacts) | B |
| Intake forms / custom booking questions | ✔ | ✔ (intake forms, client fields, details-step questions) | ◐ (not directly observed in fetched articles) | ◐ (not observed) | ◐ (not directly observed; routing forms adjacent) | B |
| Staff/team management (per-provider calendars, time off) | ✔ (add/manage staff) | ✔ (providers, users) | ✔ (team hours, breaks, time off, per-team URLs) | ✔ (staff members) | ✔ (team event types, round-robin distribution) | B |
| Resources (rooms/equipment) as booking constraints | ✔ (use resources to limit bookings) | ✔ (Related resources custom feature) | — (not observed) | — (not observed) | — (not observed) | B — partial |
| Group classes / group sessions alongside 1:1 | ✔ (group classes, capacity, series) | ✔ (Classes custom feature) | ✔ (class booking + class payments) | ◐ (not observed) | ✔ (group event types; "group classes") | B |
| Packages / prepaid series / gift certificates | ✔ (packages, gift certificates, subscriptions) | ✔ (packages, memberships, coupons/gift cards) | ◐ (not observed in fetched articles) | — | ◐ (meeting packages) | B — partial |
| Video meeting links attached to appointments | ✔ (video conferencing integrations) | ✔ (Google Meet online appointments) | ✔ (Zoom/Meet 1-click) | ✔ (Teams link per appointment) | ✔ (Zoom/Meet/Teams) | B |
| Operator books on behalf of client (staff-side booking) | ✔ ("book appointments for clients") | ✔ (book from admin calendar) | ✔ (book in calendar) | ✔ (schedule new appointments in app) | ◐ (not a documented primary flow) | B |
| Approval / request-then-confirm workflow | ✔ (appointment requests) | ◐ (Status custom feature; require-acceptance not directly observed) | — (not observed) | — (not observed) | — (not observed) | B — optional |
| Waitlist | ✔ (waitlists in advanced workflows) | — (not observed) | — (not observed) | — | — (not observed) | product-specific (Acuity) in sample |
| Marketplace / consumer discovery surface | — | ✔ (BooKing.Page) | — | — | — | product-specific (SimplyBook.me) in sample |
| Client accounts / login on booking surface | ✔ (client log-in, per comparison page) | ✔ (client mobile app; client fields) | ✔ (customer login article) | ◐ (M365 identities on operator side) | — (invitee flow is link-based) | B — optional |
| AI assistant | — (not observed) | — (not observed) | ◐ (Live Receptionist/AnswerConnect adjacent) | — (not observed) | ✔ (Callie) | B — emerging |
| Platform-native packaging (inside a productivity suite) | — | — | — | ✔ (M365/Teams/Outlook; Exchange storage) | — | product-specific (Microsoft) in sample |

Legend: ✔ directly observed; ◐ observed indirectly/partially or at lower evidence strength; — not observed in fetched sources.

## Canonical Model

### Level 0 — Defining Invariant

The smallest structure without which the product stops being an appointment scheduling application:

1. **Bookable offerings with duration** — the operator defines what can be booked: named appointment types / services, each with a duration (and optionally a price), organized as a catalog. Duration is what makes slot computation possible; without defined offerings the system is a blank calendar.
2. **Availability-derived open slots** — the system computes when an offering can actually happen, from working hours / provider schedules / resource and calendar constraints, and exposes those slots as real-time bookable times. Without computed availability, booking is a request form, not scheduling.
3. **Client-initiated self-booking** — an external client (not the operator) selects an offering and a specific open slot and books it, providing their identity/contact details. This is the family signature of §03.09 scheduling applications and the reason the Type exists at all.
4. **The appointment record with a managed lifecycle** — the booking persists as an appointment binding client × offering × provider × time on the operator's schedule, and the record can be changed afterwards (rescheduled or cancelled by operator and, in mature products, by the client). Without the persistent, manageable appointment, the product is a time-poll or a form.

Justification tests:

- Remove client-initiated booking (operator books everything, no client-facing surface) → the product collapses toward a Calendar Application / front-desk appointment book, not a scheduling application in the §03.09 sense.
- Remove the service/offering catalog (only "a meeting") → the product is a Meeting Scheduling Application.
- Remove availability computation (client proposes times, group picks) → Group Availability Scheduling Application.
- Remove the appointment record (output is a one-shot poll result) → Group Availability Scheduling Application.
- Add checkout + client ledger + staff economics → Appointment-based Service Business Management (§29 sibling; removal test already documented there in reverse).
- Historical check: platform-native Microsoft Bookings satisfies all four; international SimplyBook.me satisfies all four; a 2000s-era staff-side-only "appointment book" program does **not** satisfy #3 — it belongs to the calendar/practice-management lineage, and the modern Type is defined by the self-booking loop. The definition therefore does not overfit to one vendor generation, but it is deliberately scoped to the scheduling-application family (client books into published availability).

### Level 1 — Common Mature Structure

Present across the researched sample (evidence layer B), expected of mature products but not defining:

- A branded, shareable client-facing booking surface: standalone booking page with custom URL, embeds/widgets for websites, direct links (including links that pre-select a service or provider), QR codes, social-channel booking.
- Booking rules: minimum booking notice (lead time), scheduling window (maximum advance), slot interval / start-time increments, buffers between appointments, cancellation/reschedule notice windows, per-slot capacity, daily/weekly booking caps.
- Automated notifications: booking confirmations, reminders (email and SMS), staff/internal notifications; client-side reschedule/cancel via email links or the booking page.
- External calendar synchronization (Google / Outlook / iCloud; one-way or two-way) — busy-time checking to prevent conflicts, new appointments written back to the personal/work calendar.
- Provider/staff management: per-provider working hours, breaks, time off, per-provider service assignment; per-provider booking links.
- Persistent client records: contact details, appointment history, notes/stats, merge/duplicate handling, blocking; import/export.
- Intake forms / custom questions / client fields collected during booking.
- Payment collection at or around booking: processor integrations (Stripe/Square/PayPal-class), deposits, invoices/receipts, refunds; packages, gift certificates, subscriptions, coupons.
- Group classes / group sessions (capacity, series) alongside 1:1 appointments.
- Video meeting links (Zoom/Meet/Teams-class) attached to appointments.
- Operator-side booking on behalf of clients (phone/walk-in intake).
- Reporting: bookings, income, client statistics.
- Time-zone handling for remote booking; mobile apps for operators (and sometimes clients).

### Level 2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- **Marketplace posture** — the vendor operates a consumer discovery surface listing businesses (SimplyBook.me BooKing.Page); most products have none.
- **Client accounts** — client login / client mobile app with saved details and self-service history (Acuity client log-in, Setmore customer login, SimplyBook.me client app) vs anonymous link-based booking (Calendly-style).
- **Platform-native packaging** — scheduler embedded in a productivity suite with suite identity and storage (Microsoft Bookings inside M365/Teams/Outlook, appointments stored in Exchange mailboxes); calendar-embedded booking variants.
- **Approval workflows** — bookings as requests requiring operator acceptance before confirmation (Acuity appointment requests; SimplyBook.me status machinery).
- **Waitlists** — fill cancelled slots from a queue (Acuity).
- **Industry overlays** — beauty/wellness/fitness/education/tourism positioning; HIPAA-compliance options (Acuity); clinical-grade variants belong to Patient Scheduling (§22).
- **Multi-location / multi-branch** — locations on the booking page (SimplyBook.me categories and locations; cluster solution; Acuity/Setmore multi-location).
- **Product sales / add-ons / retail** — sell products or add-ons alongside appointments (SimplyBook.me products for sale, service add-ons; Acuity add-ons, POS).
- **Memberships** — recurring client memberships (SimplyBook.me membership feature).
- **Marketing/reputation add-ons** — email marketing, reviews, SEO of the booking page (Setmore reviews, SimplyBook.me Marketing Suite).
- **AI assistance** — AI scheduling assistants / automated reception (Calendly Callie; Setmore-adjacent AnswerConnect).
- **Hidden/private offerings** — unlisted services bookable only via direct link (Acuity private appointment types, Setmore hidden services).
- **Meeting-poll features** inside scheduling products (Calendly meeting polls) — a bridge toward the Group Availability sibling.

### Level 3 — Vendor-specific (research notes only)

- Acuity: "look busy" / "minimize gaps" availability display settings; pooled calendar availability; time-window based appointments ("book a time range for a service, like for a technician to arrive"); drop-off/pick-up appointment options; multi-day/overnight appointment types; labels; Acuity Scheduling Admin mobile app; availability groups; 20%-off promo mechanics.
- SimplyBook.me: modular "Custom Features" system (features enabled/disabled à la carte, with dependency and conflict documentation); "Book soon" rebooking notifications; calendar note types; news posts on the booking website; SBPay.me; BooKing.Page marketplace; cluster solution; "Is working day?" special-day toggle with group date selection; admin-side "Receive payment" checkbox generating the invoice only at booking creation.
- Setmore: Connect (internal team messaging); Live Receptionist / AnswerConnect (answering service integrations); income stats on the calendar; Instagram stream on the Booking Page; cash register article; color-coded services; tabbed vs drop-down calendar views.
- Microsoft Bookings: Personal vs Shared Bookings split; storage in Exchange Online shared mailboxes; book.ms entry URL; Teams/Outlook app embedding; unique Teams link per appointment; M365 SKU gating.
- Calendly: routing forms; meeting distribution (round-robin) tools; workspaces/team pages; Notetaker; Callie AI assistant; Troubleshoot tool for unavailable times; "free/busy rules" (what a meeting takes priority over); SSO/SCIM admin layer.

## Boundary Findings

1. **vs Meeting Scheduling Application (§03.09 sibling)** — the two Types share the entire booking-link machinery: published availability, duration-carrying event/service types, a shareable booking page, calendar sync, reminders, even payments (Calendly supports Stripe/PayPal; Acuity is a "Calendly alternative"). The working distinction is center of gravity: appointment scheduling models a **service business's bookable offerings** — a catalog of services with client records, appointment policies (deposits, cancellation windows, no-show handling), intake forms, and operator-side appointment management — while meeting scheduling models **professional meetings** (event types as meeting templates, invite distribution, round-robin team scheduling, routing forms) without service-business semantics. Products straddle deliberately: Calendly markets "appointments and meetings"; Microsoft Bookings addresses "customers, clients, or colleagues"; Acuity's comparison page draws the line exactly on client-experience/payment grounds. This pair needs joint review when Meeting Scheduling Application is processed (recorded in STATUS).
2. **vs Appointment-based Service Business Management (§29, processed)** — shares the entire booking machinery. The sibling's removal test applies in reverse: remove checkout and the client ledger → this Type remains. Sampled products confirm the gradient: Acuity/Setmore/SimplyBook.me carry payments and client records but not full checkout/POS/staff-payroll economics; Square Appointments (sampled in the sibling research) is the bridge product.
3. **vs Calendar Application (§03.08)** — a calendar manages the user's own time and events; an appointment scheduling application publishes availability for **external clients** to book and manages appointments as business records with policies. Calendar sync is the bridge (busy-checking), and platform-native variants (calendar-embedded booking) blur the surface but not the structure: the booking machinery (offerings, rules, client records) is what makes it scheduling, not calendaring.
4. **vs Group Availability Scheduling Application (§03.09 sibling)** — group availability finds a time that works for multiple participants (poll/proposal semantics, no persistent booking system, no service catalog); appointment scheduling books one client into provider-defined slots and keeps the appointment. Poll features inside scheduling products (Calendly meeting polls) are variants, not mergers.
5. **vs Patient Scheduling (§22)** — the clinical variant: the appointment is an encounter inside a clinical record system with provider licensure, referral, and insurance semantics. Generic appointment scheduling lacks clinical semantics; HIPAA options (Acuity) are an overlay, not a transformation.
6. **vs Employee Scheduling Platform (§09, processed)** — direction of binding: employee scheduling binds **staff to shifts** (the schedule is the artifact published to employees); appointment scheduling binds **clients to provider time** (the appointment is the artifact, the provider schedule is an input). Different central object, different lifecycle, different users.
7. **vs Event Registration Platform (§26)** — an event registration platform sells attendance at discrete events with many attendees; appointment scheduling sells provider time in ongoing 1:1 (or small-group) appointments. Group classes sit in the overlap; when dated one-off events with attendee rosters dominate, the product drifts toward event registration.
8. **vs Resource Calendar (§03.08)** — resource booking makes the shared resource (room/equipment) the booked object; appointment scheduling books provider time for a service, with resources as optional constraints (observed in Acuity and SimplyBook.me only — partial evidence).

## Uncertainties

- **Appointment state machines**: no sampled product documents a full canonical state set at the level the sibling research observed for Vagaro. Setmore documents operations (book/reschedule/cancel), SimplyBook.me gates statuses behind a custom feature, Acuity documents reschedule/cancel limits. The canonical lifecycle is therefore written conceptually (booked → confirmed → completed / cancelled / no-show); exact labels vary by product.
- **Approval workflows**: observed as optional (Acuity appointment requests; SimplyBook.me status machinery); not observed in Setmore/Bookings/Calendly fetched pages. Treated as L2, not universal.
- **Payment support breadth**: all five sampled products support payment collection in some form, but plan-gating and processor dependence vary; the final document states payment as common, not defining, and makes no plan-level claims.
- **Microsoft Bookings depth**: only the Learn overview was reachable (microsoft.com blocked; support.microsoft.com not fetched). Bookings observations are kept at structure level; no operational details asserted.
- **Calendly client-side reschedule/cancel**: strongly implied by the product model but not directly observed in fetched articles; kept at moderate assertion strength.
- **Marketplace breadth**: only SimplyBook.me in the sample operates a consumer marketplace; sibling research observed marketplace posture as an L2 variant in the §29 Type. Consistent treatment applied here.

## Final Synthesis

The Type is best understood as **a self-booking machine for provider time**. Its world contains: a catalog of bookable offerings (appointment types/services with durations, optionally prices, categories, add-ons), availability machinery that turns working hours + provider schedules + external calendars + resources into real-time open slots, a client-facing booking surface (page/link/embed) where clients select an offering and a slot and leave their identity, and the appointment as the central record binding client × offering × provider × time with a managed lifecycle (confirm, reschedule, cancel, complete/no-show). Around this core, mature products add booking rules (lead time, scheduling window, slot interval, capacity, cancellation windows), automated confirmations/reminders, calendar sync, staff schedules, persistent client records, intake forms, payment collection, packages, group classes, video links, and reporting. Marketplace exposure, client accounts, platform-native packaging, approval workflows, waitlists, industry/HIPAA overlays, multi-location, and AI are variants. The sharpest boundaries: toward Meeting Scheduling (remove the service-business semantics), toward the §29 business-management Type (add checkout + client ledger), toward Calendar (remove the external booking loop), and toward Group Availability (remove the persistent appointment).
