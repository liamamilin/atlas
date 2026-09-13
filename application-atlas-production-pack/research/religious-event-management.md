# Research Notes — Religious Event Management

## Research Goal

Understand what "Religious Event Management" software actually is in the market: what products exist under this label, what their defining structure is, and how they relate to the neighboring Types already documented in §25 (Church Management System, Nonprofit Event Management, Association Event Management) and §26 (generic event management).

This pass must also discharge a SIBLING-FAMILY FLAG recorded by the nonprofit-event-management pass (2026-09-08): test whether religious events center on the **fundraising economy** (→ vertical variant of Nonprofit Event Management) or on **membership/community/program logistics** (→ §26-family variant or a sibling Type on the community-registry pattern). The association-event-management pass independently framed this leaf as "sibling pattern: same abstract shape (community registry + events) but a different registry (congregation), different users, and different event shapes (worship, ministry)."

## Initial Boundary

Working hypothesis at start:

- The leaf sits in the §25 church-software family (ChMS, Congregation Membership Management, Church Giving Platform, Ministry Scheduling, Worship Planning, …). The ChMS pass already classified "events, registration, and facilities" as a **standard capability** of ChMS, and classified the specialist slices (scheduling, worship planning, small groups, pastoral care) as "capability slices that own one loop in depth and exist both as a ChMS module and as a standalone specialist."
- Nearest neighbors to test: ChMS (record core), Nonprofit Event Management (fundraising economy), Association Event Management (membership-standing-conditioned events), Event Management Platform / Event Registration Platform (§26, generic), Church Giving Platform (money channels), Ministry Scheduling (serving rotations), Religious Small-group Management (ongoing groups), facility scheduling (rooms/resources).
- Open questions: Is there a standalone product population? Is money (fees? gifts?) part of the defining economy? Do products condition access/price on membership standing (association pattern)? How do camps/retreats/VBS fit? Where does facility booking sit?

## Research Questions

1. What event shapes do these products handle (VBS, camps, retreats, conferences, classes, holiday services, serving, connection cards)?
2. Is registration bound to identified people in the congregation's records — natively or via integration? What happens to unknown registrants?
3. What registration machinery exists (options/ticket types, custom questions, per-attendee data, family/multi-person registration, capacity, waitlists)?
4. What money machinery exists (fees, deposits, installments, refunds, discounts)? Is giving/fundraising part of the event product or separate?
5. How does participation write back to person records (attendance, signup history, engagement)?
6. What day-of machinery exists (check-in, rosters, name tags, child security)?
7. How are recurring events, multiple times/locations, and facilities/rooms handled?
8. What is religious-specific vs generic event software? Does membership standing gate access or price (association pattern)?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers — plus one non-church breadth check:

1. **Planning Center Registrations** — standalone event-registration product of the leading modular ChMS suite; mid-to-large churches; unusually good public documentation (product page + public API reference).
2. **Tithe.ly Events** — standalone event product from an all-in-one vendor (Giving + ChMS + Apps + Sites); small-to-mid churches; help center reachable.
3. **Pushpay ChMS (formerly Church Community Builder)** — enterprise engagement-suite module; large churches; product page + FAQ (help center unreachable).
4. **Churchteams** — mid-market all-in-one ChMS with a distinctive registration-as-group model and Text-to-Church channel; product feature page + FAQ.
5. **MOHID** — masjid (mosque) management platform; non-church religious breadth check; product page.

Rejected/absent candidates: Breeze ChMS (rebranded as Tithe.ly Church Management — same vendor family, not an independent sample); ShulCloud (synagogue; site returned 403); Subsplash (timed out); SignUpGenius-class generic signup tools (used by churches but not registry-bound — treated as the adjacent pole, not a sample).

## Sources

Tier-1 (official operational documentation):

- Planning Center — Registrations API reference (Signup, Attendee, SelectionType objects), version 2025-05-01 — https://api.planningcenteronline.com/docs/apps/registrations (+ /vertices/signup, /vertices/attendee, /vertices/selection_type)
- Tithe.ly Help Center — Events section: Overview of Events; Creating an Event — https://tithely.zendesk.com/hc/en-us/sections/7480287369623-Events

Tier-2 (official product pages):

- Planning Center Registrations — https://planning.center/registrations
- Tithe.ly Events — https://get.tithe.ly/product/events
- Pushpay ChMS — https://www.pushpay.com/product/chms-software/
- Churchteams Registration — https://go.churchteams.com/registration-churchteams/
- MOHID — https://www.mohid.net/

Unreachable / limitations:

- Planning Center help-center articles (help.planningcenter.com renders as a JS shell; old Zendesk help center closed) — mitigated by the public API reference, which is official documentation of the object model.
- Pushpay / Church Community Builder support site (503) — Pushpay claims rest on the official product page + FAQ.
- ShulCloud (403), Subsplash (timeout) — synagogue and church-app-platform breadth checks not completed.
- Breeze — rebranded into Tithe.ly Church Management (vendor's own banner), so not sampled as an independent product.

Research date: 2026-09-09.

## Product Observations

### Planning Center Registrations (evidence: A — API reference + product page)

- Positioning: "Create custom signups for all your church events… Coordinate the details for VBS, camps, retreats, and much more." A separate product in the Planning Center suite (People, Groups, Calendar, Registrations, Check-Ins, Services, Giving, Church Center app).
- Object model (API, official): **Signup** (name, description, logo, open/closed state, open_at/close_at windows, signup-level maximum_capacity, archived) → **SelectionType**s (the options people register for: name, price, per-type maximum_capacity, publicly_available flag, waitlist flag) → **Attendee**s ("a person registered for a signup"; active/canceled/waitlisted states; `complete` = personal information + questions + forms + add-ons done) → **Registration** (the purchaser's transaction) — with **SignupTime**s (multiple date/time options), **SignupLocation**, **Campus**, **Category**, and **EmergencyContact** as first-class objects.
- Registry binding (A): the Attendee's `name` is "derived from the associated person record"; every attendee includes a `person` relationship. Registration resolves into the People database.
- Event shapes named on the product page: VBS, camps, retreats, potlucks, service projects, conferences, dinners.
- Registration machinery (A + product page): attendee categories by role (leader/volunteer/participant) or demographic (child/adult/school grade); attendance caps at signup and selection-type level; **household signups** ("allow families to register for events together"); bonus purchase options (shirts, books, camp activities like horseback riding); headcount-only simple signups; multiple event times; waitlists.
- Money (product page): card/debit, ACH, Apple/Google Pay, in-person; cash/check recorded manually; discounts and scholarships; per-transaction processing fees; priced by biggest-event attendance tiers. **No giving machinery in Registrations** — Giving is a separate product.
- Day-of (product page): "Take event attendance and check people in… print name tags" (via the Check-Ins product); attendee groups auto-sorted (bus/cabin at camp, VBS crew, table at dinner).
- Operations (product page): reports/guest lists/CSV export; attachable forms (medical release, printable PDFs); event emails and reminders including balance-due reminders; permission levels for data privacy; posting signups to the church calendar and the Church Center app/website.
- Access model (A): "Organization admins can see all signups. Signup managers can only see the signups they manage." — per-signup scoped administration.

### Tithe.ly Events (evidence: A — help articles + product page)

- Positioning: "Church Online Event Registration… Tithely Events can be used for events such as VBS, summer camp, ministry training, workshops, conferences, marriage seminars, VIP dinners, missions send offs." Requires a free Tithely Giving account; no monthly fee — transaction fees only for paid events/donations.
- Event record (A, Creating an Event): name, church/campus, start date/time, address; optional end date, logo, location, notification emails, description, contact details. Fields can be hidden ("Not Visible") but not deleted; **a created event cannot be deleted** (Overview article).
- Tickets (A): multiple ticket/registration types with amounts and quantities; early-bird pricing with date windows; free events supported (price left blank); up to ten tickets per registration transaction.
- Attendee data (A): name + email required for every registrant; custom questions at event and attendee level (food allergies, t-shirt size, gender, campus, food preference); general questions.
- Money (A): partial or full payment; discount codes (fixed/percent, usage limits, expiration); **payment plans** (two installments; event must be at least two months away); refunds; ticket purchases sync to ChMS funds via fund mapping (Elvanto integration).
- Giving bridge (product page): "If someone gives through your events registration online, they instantly receive an email… All giving history for each member is also tracked" — a donation option at registration, riding on the Giving product.
- Registry binding (A): "If they don't have a Tithely account, one will be created for them" — unknown registrants become records; multiple people registered at once ("a parent can register each of their kids for VBS or one person can register themselves and their spouse for a marriage retreat").
- Day-of (product page): print attendee list; QR codes on tickets/receipts for check-in; kids check-in with security codes.
- Operations (A): attendee management (list, answers, payment status, CSV export, tickets); promotion via registration link and custom church app; permissions (Account Owner, Admin, or Limited Access with Events granted).

### Pushpay ChMS / Church Community Builder (evidence: B — product page + FAQ; help center unreachable)

- Events live inside the ChMS: "Creating and managing church events happens inside your ChMS. You can build events, set registration forms, collect payments, and promote them through your church app, email, or text."
- Write-back / engagement (product page): "After the event, engagement tracking shows you who attended, who RSVP'd but didn't show, and how participation compares to previous events." "Event Engagement Tracking… measure event engagement, and keep track of all your event notes and information in one place."
- Forms (product page): "collect sign ups, registrations for up to ten people in a single form, and payments."
- Church Event Management (product page): "church wide and group events that allow every member to know what's coming up and then rsvp directly from your church calendar or event invitation."
- Rooms and Resources (product page): "Manage facilities and assets needed for church events with our room and resource management tool… specific approvals, reports, and calendars for each room and resource."
- Check-in (product page): kiosks, name tags, parent pickup labels, room capacities, room rosters, parent texting; attendance tracking with headcounts and individual attendance, post-event summaries.

### Churchteams (evidence: B — feature page + FAQ)

- Positioning: "Create signups in minutes, let people register by text, web, or app, collect payments, and automatically follow up—all inside Churchteams."
- **Registration-as-group model** (product page): "Registration is tracked inside a group with a customized group view or dashboard… The group itself serves as your dashboard to manage everything, including text & email communications and payments." Registrants become a group in the people database.
- Registry binding, vendor-articulated (FAQ): "When people register, the system finds them based on form information or adds them to your database if there is no match." And the anti-silo argument: "The problem with using forms outside your church management system is that the data is siloed and inaccessible in your database unless you either manually enter it or run regular data syncs." — the market's own articulation of why registration must bind to the congregation's records.
- Channel breadth: text-keyword registration ("the system recognizes their phone number and prefills much of the form"), app, website link/embed; no login required.
- Money (FAQ): "promo codes, recurring/scheduled payments, deposits, payment reminders, limited spots, and auto-registration for additional groups."
- Follow-up (product page): "Use form responses to start follow-up actions like emails, texts, and task assignments. Drop-down responses can auto-register people into next step groups. Great for Connection Cards, VBS registration, event preparation…" — digital connection cards collect prayer requests/guest info into the database and trigger automated follow-up ("ensure no one falls through the cracks").
- Managed responses: t-shirt sizes, child-care needs, mission-team checklists handled in the group dashboard.

### MOHID (evidence: B — product page; non-church breadth check)

- Masjid (mosque) management platform: donation management, membership management, fundraising management, **program management** ("Simplify program creation, streamline registrations"), announcement email & SMS, "Event Management & Announcements", zakat management, virtual fundraiser, donation kiosks/hardware.
- The events/registration machinery exists as part of a masjid CRM (membership records as substrate), with fundraising as a separate module — same shape as the church products, different faith context. Documentation depth is product-page tier only.

## Cross-product Comparison

| Structure | Planning Center Registrations | Tithe.ly Events | Pushpay ChMS | Churchteams | MOHID |
|---|---|---|---|---|---|
| Event as configured record with lifecycle | Signup (open/close windows, capacity, archive) | Event (details, tickets, questions, discounts; no delete) | Events (build, promote, RSVP) | Signups/forms | Programs/events |
| Registration options w/ price + capacity | SelectionType (price, capacity, public flag, waitlist) | Ticket types (amounts, quantities, early bird, free) | Registration forms + payments | Limited spots, deposits | Program registration |
| Attendees bound to people records | Attendee ↔ Person (name derived from person record) | Unknown registrants get accounts created | Single member profile; RSVP from member app | System matches or adds to database | Masjid membership substrate |
| Multi-person / family registration | Household signups | Parent registers kids; ≤10 per transaction | ≤10 people per form | Family check-in; child-care needs | — |
| Custom per-attendee questions | Questions + forms + add-ons (in `complete`) | Allergies, t-shirt size, campus | Form templates | T-shirt sizes, checklists | — |
| Money for fee events | Card/ACH/wallets, cash/check manual, discounts, scholarships | Partial/full, installments, refunds, discount codes | Collect payments | Fees, deposits, recurring payments, reminders | Program fees (implied) |
| Giving at registration | No (Giving is a separate product) | Yes — donation option, receipts, giving history | No (Giving separate) | No (Giving separate) | Fundraising separate module |
| Capacity + waitlist | Signup- and type-level caps; waitlist | Quantities | Room capacities | Limited spots | — |
| Multiple times/locations | SignupTime / SignupLocation | Start/end, address | Calendar/invitation | — | — |
| Day-of check-in / attendance | Check-Ins integration, name tags | QR on tickets; kids security codes | Kiosks, tags, rosters, headcounts | Check-in product | — |
| Communications | Event emails, balance-due reminders | Notification emails, confirmations | App/email/text promotion, post-event summaries | Confirmations, reminders, follow-up workflows | Announcements email/SMS |
| Write-back / engagement | Attendance → person records (via People/Check-Ins) | Giving history on member | Who attended / no-show / vs previous events | Follow-up actions; auto-register into next-step groups | Engagement (implied) |
| Scoped admin access | Org admins vs signup managers | Owner/Admin/Limited Access | Roles | Staff/leaders | Admin app |
| Facilities/rooms | Separate Calendar product | Church calendar: rooms & resources | Rooms and Resources + approvals | — | — |
| Child-safety machinery | EmergencyContact object; grade categories | Kids check-in security codes | Pickup labels, capacities | Child-care needs | — |
| Event shapes named | VBS, camps, retreats, potlucks, service projects, conferences, dinners | VBS, summer camp, training, workshops, conferences, marriage seminars, dinners, mission send-offs | Church-wide and group events | Connection cards, VBS, mission teams | Mosque programs/events |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being this Type:

1. **The event as the managed unit of work.** A persistent, configured, published record — carrying its schedule (commonly multiple time options), location, registration options with prices and capacities, and open/close windows — which the organization creates, opens for registration, runs, and closes/archives. (Remove → a form builder or a calendar entry; nothing is being "managed.")

2. **The congregation-registry binding.** Every registration resolves to an identified person in the religious organization's people records — held natively or in an integrated registry. A registrant the organization doesn't yet know becomes a record; one registrant commonly registers other members of their household. (Remove → generic event registration software with anonymous attendees.)

3. **The participation write-back.** What happened — signed up, paid, attended, no-showed, completed forms — persists on the person's record and feeds the organization's follow-up and engagement picture. (Remove → an anonymous signup form tool; the record's life and the event are disconnected.)

Jointly-held load-bearing tests:

- 1 alone = generic event management platform (§26 territory).
- 2 without 1 = a people database with no events (ChMS record core).
- 3 without 1+2 = engagement notes with no event machinery.
- 1+2 without 3 = registration siloed from the person's record — exactly the failure mode vendors articulate against.
- 2+3 without 1 = the ChMS record core without the events loop (the ChMS sibling seam).

### L1 — Common Mature Structure

Present across the sample; expected in the market; not definitional:

- registration options / ticket types with price, capacity, and visibility (public vs restricted)
- registration forms with custom per-attendee questions (allergies, t-shirt size, grade, emergency data)
- multi-person registration (one registrant registers household members; per-transaction attendee limits)
- payments for fee-charging events: cards/ACH/wallets, partial payment, deposits/installments, refunds, discount codes, scholarships; free events equally first-class
- capacity states and waitlists
- multiple event times / time-slot selection
- day-of check-in and attendance (QR codes, kiosks, name tags), children's security machinery (pickup codes/labels)
- lifecycle communications: confirmations, reminders, balance-due notices, post-event follow-up
- scoped staff/leader access (per-event or per-ministry managers)
- reports and exports (attendee lists, payment status)
- public event page / posting to the organization's website and mobile app
- attachable forms (medical releases) and attendee grouping (cabins, buses, crews, tables) for camp/retreat-scale events

### L2 — Variant / Optional Structure

- giving/donation option at registration (documented at 1 of 5 sampled products; rides on the giving platform; absent where giving is a separate product)
- room/resource booking with approval routing (companion capability; a separate product in one sampled suite)
- text-keyword registration and other channel variants (app, embed, link)
- digital connection cards / guest capture forms (blurs into ChMS guest follow-up)
- recurring event series and automation around them
- fundraising-event shapes (galas, auctions) — when a religious organization runs one, the market routes it to fundraising/event-fundraising tools, not to this Type's machinery
- faith-tradition packaging: masjid program management, parish-style structures (not deeply sampled)

### L3 — Vendor-specific (Research Notes only)

- Planning Center: per-attendee-tier product pricing; Check-Ins/Calendar as sibling products; Church Center app surface; `publicly_available` selection-type flag; signup-manager permission model.
- Tithe.ly: events cannot be deleted; 10-attendee transaction limit; payment plans gated to events ≥2 months out; Elvanto fund mapping; requires a (free) Giving account.
- Churchteams: registration realized as a group in the database; Text-to-Church keyword prefill; auto-registration into next-step groups.
- Pushpay: ChurchStaq packaging; MyChurch App RSVP; rooms/resources approval routing; engagement comparison vs previous events.
- MOHID: hardware ecosystem (kiosks, tap devices, signage) around the masjid platform.

## Rejected Findings (anti-overfit)

- **Fundraising economy is NOT definitional.** Only 1/5 sampled products documents a giving option at registration, and it rides on a separate giving product; the other four keep giving entirely separate. No settlement-and-acknowledgment close (receipts to donors, donor attribution) exists in the events machinery. Event money is fees (tickets, deposits), not gifts. → This leaf is NOT a vertical variant of Nonprofit Event Management.
- **Member-standing-conditioned access/pricing is NOT observed.** No sampled product documents member-vs-non-member pricing or member-only event gating as a norm (contrast: Association Event Management, where it is the norm). Religious events are characteristically open to guests. Recorded as "not observed in sample," not asserted as universal.
- **Facilities/rooms booking is NOT definitional** — companion capability, separate product in one sampled suite.
- **Child-safety machinery is NOT definitional** — common and important (VBS/camps), but a headcount-only potluck signup satisfies the Type without it.
- **Specific channel (app/QR/text) is NOT definitional** — web link, text keyword, app, and kiosk are channel variants.
- **"Church" is NOT definitional** — the sample includes a masjid platform; the invariant is the religious organization's community registry, not a church-specific object.

## Historical / Market-Sample Check

- Paper-era pattern: a church office running VBS registration on paper forms, writing registrants into the church's membership rolls (or creating guest cards), and marking attendance afterward — satisfies all three L0 structures with no software machinery. A synagogue keeping a High Holiday seat reservation book bound to member files fits the same shape.
- The modern machinery (QR check-in, kiosks, apps, text keywords, payment plans) is era implementation, not definition.
- Non-church check: MOHID (mosque) fits with a membership substrate and program registration. Synagogue products could not be fetched (ShulCloud 403) — recorded as an uncertainty, not filled from memory.

## Boundary Findings

1. **vs Church Management System (ChMS):** the ChMS holds the record core (people + households + participation) and lists events as one standard capability. This leaf owns the **events loop in depth** — event configuration, registration machinery, capacity/waitlists, payments, day-of operation — and exists both as a ChMS module and as a standalone product (two of five sampled products are standalone). Remove the events loop → ChMS; remove the record core → generic event platform.
2. **vs Nonprofit Event Management:** different money economy. Nonprofit events center on event-linked giving machinery plus a settlement-and-acknowledgment close (receipts, donor attribution). Religious events center on participation; money is fees; giving is at most an optional bridge (1/5). SIBLING FLAG from the nonprofit pass **DISCHARGED**: this leaf is a real sibling Type on the community-registry pattern, not a fundraising-economy variant.
3. **vs Association Event Management:** same abstract shape (community registry + events) but different registry semantics. Association events condition **access and price on membership standing** (member vs non-member pricing is the norm; member-only visibility). Religious events are characteristically open to guests; standing rarely gates access or price (not observed in sample). The distinctive machinery here is household/family registration and child safety; the event shapes are ministry-shaped (VBS, camps, retreats, worship-adjacent) rather than conference/CE-shaped.
4. **vs Event Management Platform (§26):** generic platforms center on attendee experience and logistics (agendas, sessions, speakers, venues, event apps) with anonymous attendees and ticket revenue; no people-record substrate, no write-back. Seam for the §26 forward flag: registry binding + participation write-back vs anonymous attendee + logistics center.
5. **vs Event Registration Platform (§26):** the registration leg alone, anonymous, no registry, no write-back.
6. **vs Church Giving Platform:** giving channels and money movement vs event participation; they meet at the optional giving-at-registration bridge.
7. **vs Ministry Scheduling:** serving rotations (recurring team schedules) vs dated event participation; both draw on the same people records; volunteers at events are a common overlap.
8. **vs Religious Small-group Management:** ongoing communities vs dated events; one sampled product realizes registration as a group (product-specific blur, noted).
9. **vs facility scheduling:** rooms/resources are a companion capability, sometimes bundled, sometimes a separate product.
10. **vs camp-management software (no directory leaf):** dedicated camp/conference-center systems (sessions, health forms, cabin inventory, camp billing) serve camp ministries as a deeper specialist market; church event products handle camps/retreats at registration depth (attendee groups, add-on purchases, deposits). Recorded as an adjacent market, not sampled.

## Uncertainties

- Depth of camp/retreat machinery in this Type (deposits and attendee grouping documented; full camp-management machinery — session enrollment, cabin inventory, health-form workflows — not sampled).
- Whether any religious event product conditions price on membership standing (not observed; cannot assert absence market-wide).
- Synagogue-specific event machinery (seat reservations for high holidays) — source unreachable; not asserted.
- Pushpay's event machinery claims rest on product-page FAQ (help center 503).
- Recurrence semantics for weekly/repeating events (multi-time options documented; recurring-series behavior not deeply verified).
- MOHID's program/event machinery depth is product-page tier only.

## Final Synthesis

Religious Event Management is the religious organization's event-participation system: it owns the events loop — create, publish, register, run, close — operated on the congregation's people records. Its defining structure is the trio: the event as managed unit of work + the congregation-registry binding + the participation write-back. The money economy is fees for fee-charging events (camps, retreats, conferences), with free events equally first-class; fundraising is not the center (discharging the nonprofit pass's sibling flag). It is a real sibling Type — not a §26 variant — because the registry binding and write-back are structural (vendors articulate the anti-silo argument themselves), and not a variant of Nonprofit Event Management because the fundraising economy is absent from its center. It differs from Association Event Management in registry semantics (open-to-guests vs standing-conditioned access/pricing) and in event shapes (ministry-shaped vs conference/CE-shaped). The market realizes it as standalone event products, ChMS event modules, and (outside the church) masjid program management.
