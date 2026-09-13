# Research Notes — Meeting Scheduling Application

Research date: 2026-09-08

## Research Goal

Understand how real meeting-scheduling products work: what objects they manage, how a host's availability becomes bookable meeting times, how an invitee books, where the meeting record lives and how it travels, which rules govern booking, and — because this leaf sits in the three-sibling §03.09 family — how it holds its boundary against Appointment Scheduling Application and Group Availability Scheduling Application, plus Calendar Applications and other neighbors. This pass is also the flagged "joint review" counterpart for the appointment-vs-meeting boundary recorded in STATUS on 2026-09-06.

## Initial Boundary

- Directory §03.09 Scheduling: Meeting Scheduling Application, Appointment Scheduling Application (processed 2026-09-06), Group Availability Scheduling Application (processed 2026-09-07). Family signature recorded by prior passes: "publish availability → another party books a time".
- From the appointment pass: the pair "shares the entire booking-link machinery"; the working distinction was center of gravity — service-business semantics (service catalog, client records, appointment policies) vs meeting semantics (event types as meeting templates, invite distribution, team routing). Joint review flagged for this pass.
- From the group-availability pass: "meeting scheduling has an organizer with authority — a time is proposed and invitees accept/decline; booking links publish the organizer's *own* availability; the meeting record lands on calendars."
- Initial hypothesis: the core is the booking-link loop applied to meetings — host publishes availability via duration-carrying meeting kinds; invitee self-books a slot; the outcome is a meeting record that lands on calendars. No service catalog, no client ledger.
- Open question carried in: is the "propose a time → invitees accept/decline" flow (calendar-invite semantics) part of this Type's core, or does it belong to the Calendar Application? This pass must sharpen the group-availability pass's phrasing.

## Research Questions

1. What is a meeting kind (event type / link / meeting type) and what does it carry?
2. How is host availability expressed and computed (schedules, working hours, external-calendar busy-checking, date overrides, out-of-office)?
3. What does the invitee booking flow look like, and what identity/details does it collect?
4. What is the meeting record, where does it live (bookings list, calendars), and what is its lifecycle (confirm/reschedule/cancel/no-show)?
5. Which booking rules exist (buffers, minimum notice, booking window, start increments, frequency limits, confirmation/approval)?
6. How does team scheduling work (round-robin, collective, group, routing forms, ownership)?
7. Which capabilities are common-but-not-defining (video links, reminders/workflows, payments, analytics, AI, embeds)?
8. Where are the boundaries: vs Appointment Scheduling, vs Group Availability, vs Calendar, vs Interview Scheduling, vs Event Registration?
9. Would older / platform-native / differently-positioned products still fit the definition?

## Representative Products

| Product | Segment / philosophy | Customer tier | Why selected |
|---|---|---|---|
| Calendly | Market-defining link-first scheduler; "book appointments and meetings" | Individuals → enterprise | Canonical product; the appointment pass used it as the boundary-straddling sample |
| Cal.com | Open-source "scheduling infrastructure"; developer/dev-tool posture | Solo → organizations; self-host pole | Different philosophy (open infrastructure, API/MCP, deep team mechanics) |
| SavvyCal | Recipient-experience-first scheduler ("the fresh way to find a time to meet") | Prosumer → teams | Different philosophy (calendar overlay, preferred slots, time blocks) |
| Chili Piper (ChiliCal) | Revenue-team meeting scheduling embedded in lead routing | B2B sales/enterprise | Revenue-team pole: form→booking, routing, CRM actions |
| Microsoft Bookings — Personal Bookings | Platform-native scheduler inside Microsoft 365 | Organizations on M365 | Platform-native anchor for the historical/market-sample check (observed in the appointment pass, 2026-09-06) |

Notes on sampling: Google Calendar appointment schedules was a candidate platform-native sample but support.google.com timed out twice this pass (see Sources); it is documented structurally only. YouCanBook.me, Reclaim.ai, HubSpot Meetings were candidates; the five selected already cover link-first, open-source, recipient-experience, revenue-team, and platform-native positions.

## Sources

Tier 1 (official operational documentation), fetched 2026-09-08:

- Calendly Help Center home (with inline quick-answer articles): https://help.calendly.com/hc/en-us — calendar connections, embed options, availability fine-tuning (limits & buffers, free/busy rules, start-time increments), meeting limits, buffers, Troubleshoot tool
- Calendly product pages: https://calendly.com/features , https://calendly.com/scheduling — how-it-works (5 steps), event types as meeting templates, team scheduling, routing forms, platform products (Callie, Notetaker, Contacts, Payments)
- Cal.com Help Desk index: https://cal.com/help/llms.txt ; articles fetched: What are Links (event-types/event-types.md), Create your first event type (create-first-event.md), Round Robin Scheduling (round-robin.md), How to require confirmation (how-to-requires.md), Edit Availability (availabilities/edit-availability.md); article inventory from the index (booking questions, min notice, buffers, limit future bookings, user-level booking limits, date overrides, out-of-office, collective events, dynamic group links, managed events, private links, no-show, reschedule, workflows, routing, paid bookings, Cal Events)
- SavvyCal product page: https://savvycal.com/ ; Knowledge Base: https://docs.savvycal.com/ — Scheduling Links category inventory (32 articles), Configuring link availability (article/26), Meeting Polls category + Scheduling group meetings with polls (article/79)
- Chili Piper Help Center ("Chili Hub"): https://help.chilipiper.com/ — platform category structure: ChiliCal (scheduler for customer-facing reps: meeting types, personal pages, scheduling links incl. one-on-one/round-robin/group/ownership/smart, working hours, custom schedules, suggested times, no-shows, CRM actions), Concierge (webform→booking), Web Experiences (chatbot→route/schedule), Distro (lead distribution), Handoff (scheduling + lead routing across teams), Orchestrator, Reporting

Tier 2 (official product pages): as listed above (Calendly /features and /scheduling; SavvyCal homepage).

Prior-pass direct observation reused (evidence layer A, fetched 2026-09-06, recorded in research/appointment-scheduling-application.md):

- Microsoft Learn — Microsoft Bookings overview: https://learn.microsoft.com/en-us/microsoft-365/bookings/bookings-overview — Personal Bookings ("creating meeting types... publish your personal booking page... share the link with anyone") and Shared Bookings (services, staff, business hours)

Access limitations:

- support.google.com (Google Calendar appointment schedules) timed out twice → source abandoned per network rule; Google documented structurally only, no Google-specific claims.
- Calendly help-center category pages (e.g. /help/event-types) render the same JS shell as the home page; category article lists were not obtainable. Calendly claims rest on the help-center home quick-answers + product pages; kept at structure level where not directly observed.
- Chili Piper observed at section/article-title level (structure); no operational details asserted.
- Calendly invitee-side reschedule/cancel not directly observed this pass; kept at moderate assertion strength.

## Product Observations

### Calendly (evidence layer: A for fetched help-center quick-answers and product pages)

- **Positioning**: "A better way to book appointments and meetings"; "The #1 scheduling tool trusted by over 20M professionals"; solutions by team: sales, marketing, customer success, recruiting; by size: individuals → enterprise.
- **How it works (product page, 5 steps)**: 01 connect your calendars ("avoid double bookings and only offer times you're free"; Google, Outlook, Microsoft Office) → 02 customize availability ("preferred meeting hours, daily meeting limits, and built-in buffers and breaks") → 03 select a meeting template ("for one-on-one or multi-person meetings, and customize the location, description, branding, and other details") → 04 share your booking link ("email, social media, your website... Invitees choose a time and the meeting is booked") → 05 set up automations ("meeting reminders and follow-ups, qualify and book leads from your website").
- **Event types**: "pre-built event types" for "one-on-one appointments, multi-host sales demos, or group classes"; landing page embed displays "all active personal or team event types", booking page embed displays "a single event type".
- **Availability machinery (help center)**: connect Google/Outlook/Office 365/Exchange calendars; "Calendly checks your calendar for busy times and adds new meetings to it"; choose calendars to check for conflicts and one main calendar for bookings; per-event-type "Limits and buffers" (meeting limits per day/week/month; buffer time before/after), "Free/busy rules" ("choose what this meeting takes priority over"), start-time increments; Troubleshoot tool explaining why a time is unavailable.
- **Sharing**: booking links via email/social/website; embeds (inline, pop-up text, pop-up widget); browser extension; mobile app.
- **Team/scale**: "team templates, admin controls, routing forms, meeting distribution tools"; admin categories: managing users, teams & groups, managed events & automations, SCIM, SAML SSO.
- **Routing**: "Website embeds and lead routing forms — Qualify, route, and schedule meetings instantly from your website."
- **Adjacent products**: Callie (AI assistant, beta), Notetaker (meeting recaps), Contacts (relationship management), Payments (Stripe/PayPal; "How to sell services using meeting packages and payment links"; invoices).
- **Meeting polls**: feature page exists (/scheduling/meeting-polls) — bridge toward group availability.

### Cal.com (evidence layer: A — direct observation of help-desk articles)

- **Event types = "Links"**: "Links are your pre-set meetings, events, consultations, etc., which you can share with potential attendees... each event type is customizable in terms of its name, URL, duration, availability, and location of the event." Example: "A HR person could have a 'Job Interview' event type lasting 30 minutes, a 'Performance Review' event type for 60 minutes both with different settings on each."
- **Personal vs team event types**: "Personal event types set up a meeting where people can book just you, whereas team event types allow you to either book one person from the team, or multiple people at the same time."
- **Slot computation**: "Once you preview the URL of your link, that link's availability will show in the form of slots that are available for booking. Your link can also check your integrated calendar for conflicts; any current events in your calendar will occupy the associated time slot."
- **Create event type minimum**: Title, URL, Description, Length.
- **Availability**: availability dashboard; schedules with date overrides, multiple schedules, multiple time slots per day, out-of-office ("block bookings, redirect them to a teammate"), holidays; team availability; timezone handling (lock timezone on booking page).
- **Booking rules**: event buffers; custom time-slot intervals; minimum notice; limit future bookings; booking frequency; user-level booking limits (per day/week/month/year caps across all event types); booker active booking limit; event-type-specific conflict checking; restriction schedule; optimized slots.
- **Booking questions**: custom questions; require/exclude email domains; prefill fields; UTM tracking; booking success redirect parameters.
- **Confirmation flow**: "By default, any open slot on your booking page can be booked instantly. Requiring confirmation adds a manual approval step: when someone books, the request comes to you first, and the booking is only pushed to your calendar and confirmed to the attendee once you accept it. Until then, the booking stays in a pending state and no confirmation email is sent." Options: always, or "when booked with less than X notice"; unconfirmed bookings can still block slots; free-email-provider gating; pending bookings in an "Unconfirmed" tab; accept pushes to calendar, reject notifies with optional reason.
- **Lifecycle**: host reschedule with busy/free slot indicators; disable cancelling/rescheduling; allow rescheduling past events; mark guests as no-show; reassign round-robin bookings (transfer meeting to another host without cancelling).
- **Team scheduling — Round Robin**: "distribute meetings amongst team members... based on availability"; host assignment by priority ranking (default 'medium'), weights (default 100%, proportional adjustment for new hosts), least-recently-booked fallback; **Round-Robin Groups** (one host from each group joins — e.g., "a sales representative and a solutions engineer"); **Fixed hosts** (always attend) combined with round-robin hosts.
- **Collective events** (multiple hosts required); **Dynamic Group Links**; **Managed Events** ("create and manage shared event types for your team from one place").
- **Routing**: routing forms; "Routing with Round Robin and Attribute Matching"; headless routing; connect routing-form data to booking questions; redirect when an event type is accessed without a routing form.
- **Workflows**: "Automate messages, actions, and follow-ups for your bookings"; SMS/WhatsApp credits.
- **Payments**: paid bookings; receive payments on event types.
- **Embeds**: embed events; slots in email; prefill in embed; snippet generator.
- **Private/secret links**; hide organizer email; hide notes in calendar.
- **Adjacent feature — Cal Events**: "Events are for a single, fixed-date happening that guests register for, such as a workshop, meetup, dinner, or launch party" — event-registration semantics shipped as a separate feature inside the same product (boundary evidence).
- **AI**: Cal.ai; MCP server ("manage your schedule with natural language").
- **Enterprise**: delegation credential (admin-managed calendar connections for all members), audit logs, custom SMTP, instant meetings, organizations; seat billing.
- **Open source**: GitHub repo; self-hosting; API v2 (OAuth/API keys; bookings, schedules, event-types, teams endpoints).

### SavvyCal (evidence layer: A for homepage + fetched articles; B for article-title inventory)

- **Positioning**: "The fresh way to find a time to meet. You'll love it for the flexible controls to keep your calendar sane. They'll love it for the ultra-convenient booking experience."
- **Booking experience**: "replaced the inefficient 'click-a-day then click-a-time' interface with a gorgeous, high-fidelity week view. Recipients can even overlay their calendar on top of your link to spot ideal times at a glance."
- **Scheduling links** (32-article category): custom domains; configuring link availability; time blocks to define availability; highlight preferred times; collective scheduling links; round robin scheduling links; embedding links; sharing availability with people outside your team; customizing event names; custom questions; require approval for new events; frequency limits; schedule a time zone change; customizing the confirmation page; showing your name on Google Calendar invites.
- **Availability rules (article/26)**: Buffer Before / Buffer After ("minimum amount of time to keep open before/after a new event"), Minimum Notice ("minimum amount of lead time required before the start of a new event"), Start Time Increments ("how frequently we should generate time slots"); Frequency Limits ("maximum number of events... on a given day, week, or month").
- **Availability philosophy**: "Defend your focus time... Just because you're technically 'available' doesn't mean we should fill your calendar with meetings" — time blocks (budget time using calendar events), preferred slots ("encourage people to schedule meetings at the optimal time of day and clustered near other meetings").
- **Team scheduling**: Collective Mode ("combine your availability with multiple colleagues"), Round Robin Mode ("distribute meetings across a pool of organizers. Perfect for sales and customer support"), Group Mode ("allow multiple schedulers to join the same time slot. Perfect for webinars and group coaching calls"); Organizations.
- **Payments**: Stripe; **Workflows**; **Sender Profiles**; **Chrome extension**; **Meeting Polls** (see bridge below).
- **Meeting polls (article/79)**: "propose multiple time slots to a group of people and gather votes"; pre-add teammates with their "Busy" times blocked; publish poll link; organizer "select[s] the attendees... and click[s] **Schedule** on your desired time slot" → event confirmed with invitations. Bridge toward the group-availability sibling.

### Chili Piper / ChiliCal (evidence layer: A for structure — section and article titles; no operational details asserted)

- **ChiliCal**: "the only smart scheduler built specially for customer-facing reps." Components observed: MyApp scheduler home; Meeting Types; Guest Forms; Personal Pages; Scheduling Links (One-On-One, Round-Robin, Group, **Ownership**, Smart); Setting your Working Hours; Custom Schedules; Multiple-Calendar Connections; Inserting Suggested Times; Priority Scheduling; Reminders and Messages; Managing No Shows; CRM Actions; Dynamic Tags for Meeting Types and Reminders; One-Click Booking Links; Passing Smart Parameters / UTM; video integrations (Teams, RingCentral, GoToMeeting, Webex).
- **Platform modules around the scheduler**: Concierge ("Convert leads to pipeline directly from webforms or in-app"); Web Experiences (chatbot: "route them to an available rep, or let them schedule a meeting"); Distro ("Intuitive Lead Distribution"); Handoff ("automate scheduling and lead routing from prospecting to sales to implementation"); Orchestrator ("GTM Control Layer... listens for signals... makes decisions... takes action"); Reporting; Command Center (admin).
- Reading: the revenue-team pole packages the same meeting-scheduling core inside lead-routing machinery; the booked object remains a meeting with a customer-facing rep.

### Microsoft Bookings — Personal Bookings (evidence layer: A, prior pass 2026-09-06)

- "Personal Bookings: manage your own appointment timeslots... set aside time for specific activities by **creating meeting types**. Once you publish your **personal booking page**, you can share the link with anyone."
- Shared Bookings (same product family): "define services, manage staff members, configure schedules and availability, business hours" — the service-business pole.
- Reading: Microsoft's own product split (Personal Bookings with meeting types vs Shared Bookings with services/staff) mirrors the meeting/appointment taxonomy line inside one vendor's suite. Platform-native packaging satisfies the meeting-scheduling core without any link-vendor specifics.

### Google Calendar appointment schedules (not verified this pass)

- support.google.com timed out twice; source abandoned. Recorded as the other platform-native anchor (booking page created from the calendar; booker picks a slot; event created on calendars) at **structure level only** — no Google-specific feature claims.

## Cross-product Comparison

| Structure / capability | Calendly | Cal.com | SavvyCal | ChiliCal | MS Personal Bookings | Evidence |
|---|---|---|---|---|---|---|
| Host-side bookable meeting kinds (event types / links / meeting types) with duration | ✔ event types ("meeting template") | ✔ links/event types | ✔ scheduling links | ✔ meeting types | ✔ meeting types | B |
| Kind carries duration → slot computation | ✔ | ✔ (Length) | ✔ | ✔ | ✔ | B |
| Kind carries location/video, description, branding | ✔ | ✔ | ✔ | ✔ | ◐ | B |
| Availability from schedules/working hours + external-calendar busy-check | ✔ (multi-calendar conflict check; main booking calendar) | ✔ (schedules, date overrides, out-of-office, holidays; calendar conflict check) | ✔ (buffers article; calendar connections) | ✔ (working hours, custom schedules, multiple-calendar connections) | ✔ (integrated with Outlook) | B |
| Shareable booking surface: personal landing page + per-kind page + embeds | ✔ (landing page / booking page; inline/popup embeds; extension) | ✔ (personal link; embeds; slots in email) | ✔ (links; embeds; custom domains; extension) | ✔ (personal pages; one-click links) | ✔ (personal booking page) | B |
| Invitee self-booking: pick kind → slot → details (name/email; questions) | ✔ | ✔ (+ booking questions, email-domain rules) | ✔ (+ custom questions) | ✔ (+ guest forms) | ✔ | B |
| Meeting record persists and is manageable (reschedule/cancel) | ◐ (not directly observed invitee-side this pass) | ✔ (host reschedule w/ busy indicators; disable options; reassign) | ◐ (confirmation-page customization; approval article) | ◐ (no-show management) | ◐ | B (partial) |
| Meeting written back to host calendar (commonly invitee's too) | ✔ ("adds new meetings to it") | ✔ ("pushed to your calendar") | ✔ (Google Calendar invites with your name) | ✔ (calendar connections) | ✔ (Outlook-integrated) | B |
| Booking rules: buffers / min notice / start increments / frequency limits / booking window | ✔ (buffers, meeting limits, increments, "prevent last-minute") | ✔ (buffers, min notice, intervals, frequency, limit future bookings, user-level caps) | ✔ (buffers, min notice, increments, frequency limits) | ◐ (custom schedules, priority scheduling) | ◐ (not observed) | B |
| Confirmation/approval mode (pending → accept/reject) | ◐ (not observed this pass) | ✔ (requires confirmation; pending state; notice threshold; free-provider gating) | ✔ (require approval article) | — (not observed) | — (not observed) | B — optional |
| Video conferencing as default location | ✔ (Zoom/Meet/Teams) | ✔ (Cal Video, Zoom) | ✔ (integrations) | ✔ (Teams/RingCentral/GoTo/Webex) | ◐ (Teams per appointment — Shared Bookings observation) | B |
| Notifications/reminders/workflows | ✔ (reminders & follow-ups; workflows) | ✔ (workflows; SMS/WhatsApp credits) | ✔ (workflows) | ✔ (reminders and messages) | ✔ (email/SMS reduce no-shows — Bookings overview) | B |
| Team scheduling: round-robin distribution | ✔ (meeting distribution tools) | ✔ (priority/weights/least-recently-booked; groups; fixed hosts; reassign) | ✔ (round robin mode) | ✔ (round-robin links) | — | B |
| Team scheduling: collective (multiple hosts required) | ◐ (multi-host event types) | ✔ (collective events) | ✔ (collective mode) | — (not observed) | — | B |
| Group event types (multiple invitees per slot) | ✔ (group classes) | ✔ (dynamic group links; seats) | ✔ (group mode) | ✔ (group links) | — | B |
| Routing forms (qualify → route → book) | ✔ (routing forms) | ✔ (routing forms; attribute matching; headless) | — (not observed) | ✔ (Concierge/Distro routing) | — | B — team/revenue pole |
| Payments for meetings | ✔ (Stripe/PayPal; meeting packages) | ✔ (paid bookings) | ✔ (Stripe) | — (not observed) | — | B — optional |
| Invitee/contact records | ◐ (Contacts as adjacent product) | ◐ (booking data; no contacts product) | — (not observed) | ✔ (CRM actions) | ◐ (customer data — Shared Bookings) | B — optional |
| Analytics on bookings | ✔ (analytics & reporting category) | ✔ (insights dashboard; booking page analytics) | — (not observed) | ✔ (Reporting) | — | B |
| AI scheduling assistant | ✔ (Callie, beta) | ✔ (Cal.ai; MCP server) | — (not observed) | — (not observed) | — | B — emerging |
| Meeting polls (bridge to group availability) | ✔ (feature page) | — (not observed) | ✔ (meeting polls) | — (not observed) | — | B |
| Platform-native packaging (inside a calendar suite) | — | — | — | — | ✔ (M365/Outlook) | A (prior pass) |
| Open-source / self-host | — | ✔ (GitHub; self-host; API v2) | — | — | — | product-specific (Cal.com) |
| One-off dated events with registration (adjacent feature) | — | ✔ (Cal Events: "single, fixed-date happening that guests register for") | — | — | — | product-specific (Cal.com) |

Legend: ✔ directly observed; ◐ observed indirectly/partially or at lower evidence strength; — not observed in fetched sources.

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

Four properties. Remove any one and the product stops being a Meeting Scheduling Application:

1. **Host-published availability** — the host (a person, or a team of hosts) expresses when they can meet as reusable availability rules (schedules/working hours, checked against connected calendars' busy time), from which the system computes open meeting times. The host's availability — not the participants' declarations, not a provider's service capacity — defines the candidate times. Remove → messaging/calendar coordination with no booking loop.
2. **Meeting kinds as bookable templates** — at least one named, duration-carrying meeting kind (event type / link / meeting type) that shapes the booking (location or video link, description, optionally questions). Duration is what makes slot computation possible. Remove → a blank "share my calendar" surface.
3. **Invitee-initiated booking through a shareable surface** — an external invitee selects a meeting kind and a specific open slot via a shareable link/page/embed and books it, providing their identity/contact details, without the host mediating each booking. This is the §03.09 family signature. Remove → calendar invite (host proposes, invitees accept/decline) or a group time poll.
4. **The meeting as the outcome and record** — the booking persists as a meeting binding host × invitee(s) × time, manageable afterwards (reschedule/cancel), and in mature products written to the participants' calendars. Remove → a one-shot poll result or a form submission.

Justification tests:

- Remove invitee self-booking (host proposes a time, invitees accept/decline) → Calendar Application semantics (§03.08), not this Type.
- Remove host-published availability (participants declare their own availability to find a time) → Group Availability Scheduling Application.
- Add service-business semantics (priced service catalog, client records/ledger, appointment policies, deposits) → Appointment Scheduling Application territory.
- Remove the persistent meeting record (output is a chosen time only) → Group Availability Scheduling Application.
- Historical/platform check: Microsoft Personal Bookings (meeting types + personal booking page, platform-native) satisfies all four with no link-vendor specifics; the core requires no video links, embeds, AI, payments, or team distribution — those are era-current additions. The Type does presuppose shared digital calendars as the surrounding infrastructure (the meeting record's natural home), which is what separates it from pre-calendar paper "appointment books".

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B), expected of mature products but not defining:

- Shareable booking surfaces: personal landing page listing all meeting kinds; per-kind booking pages; one-off/single-use and private links; embeds (inline / pop-up / widget); browser extension; email-slot insertion.
- Booking rules: buffers before/after; minimum notice (lead time); booking window (limit future bookings); start-time increments; frequency/meeting limits per day/week/month; per-booker active-booking caps; timezone display and locking.
- Calendar synchronization: busy-checking across one or more connected calendars; a designated booking calendar; write-back of booked meetings.
- Video conferencing attachment (Zoom/Meet/Teams-class) as the default meeting location.
- Notifications and automations: confirmations, reminders, follow-ups; workflow automation for booking-related messages.
- Reschedule/cancel by host and invitee; host-side reschedule with busy/free slot indicators; no-show marking; reassignment of team bookings.
- Team scheduling: round-robin distribution across a host pool (availability-based, with fairness/priority mechanisms); collective events (multiple hosts required); group event types (multiple invitees per slot); shared/managed team event types; team pages.
- Booking questions / custom fields; URL prefill; UTM tracking.
- Approval/confirmation mode: bookings as pending requests the host accepts or rejects (optional).
- Payments for meetings (processor integrations, meeting packages) — optional.
- Routing forms: qualify an inbound visitor and route to the right host's booking (team/revenue pole).
- Analytics/insights on bookings; admin layer (SSO/SCIM, managed events, org-wide controls) at enterprise tier.

### L2 — Variant / Optional Structure

- **Platform-native packaging** — scheduler embedded in a calendar/productivity suite with suite identity and storage (Microsoft Personal Bookings; Google Calendar appointment schedules).
- **Open-source / self-hosted infrastructure** — the scheduler as deployable infrastructure with API/MCP access (Cal.com).
- **Recipient-experience philosophy** — booking UX innovations aimed at the invitee (calendar overlay, preferred slots, time blocks as availability inputs) (SavvyCal).
- **Revenue-team packaging** — meeting scheduling embedded in lead routing and CRM machinery (form→booking, ownership links, CRM actions, lead distribution) (Chili Piper).
- **AI scheduling assistants** — delegate scheduling to an agent over email/chat or via API (Callie, Cal.ai/MCP).
- **Meeting polls embedded in scheduling products** — bridge feature toward the group-availability sibling (Calendly, SavvyCal).
- **Paid meetings / meeting packages**; private/secret and single-use links; custom domains/white-labeling.
- **Adjacent one-off "events with registration"** inside scheduling products (Cal.com Events) — drifts toward Event Registration Platform when dominant.

### L3 — Vendor-specific (research notes only)

- Calendly: Troubleshoot tool for unavailable times; free/busy rules ("what this meeting takes priority over"); Notetaker/Contacts/Callie product family; landing-page vs booking-page embed distinction; 20M-professionals claim (marketing).
- Cal.com: round-robin weights math (default 100%, proportional adjustment formula for new hosts), priority ranking (default 'medium'), least-recently-booked fallback; round-robin groups (one host per group); fixed hosts; free-email-provider confirmation gating; "unconfirmed bookings still block calendar slots" toggle; delegation credential (admin-managed calendar connections); event-type-specific conflict checking; restriction schedule; optimized slots; booker active booking limit; hide host details in reassignment notifications; seat billing; messaging credits; MCP server.
- SavvyCal: calendar overlay for recipients; preferred slots; time blocks as availability definition; sender profiles; week-view booking interface; buffer-direction explanation (buffers apply to the hypothetical new event); Time Zone API.
- Chili Piper: MyApp; ownership scheduling links; smart parameters; dynamic tags; Concierge/Web Experiences/Distro/Handoff/Orchestrator module stack; priority scheduling; suggested-times insertion.
- Microsoft: Personal vs Shared Bookings split; storage in Exchange Online shared mailboxes (Shared Bookings observation, prior pass); book.ms entry; M365 SKU gating.

## Rejected Findings (not canonical)

- "Meeting scheduling = calendar invites with accept/decline" — the propose-a-time/accept-decline flow is calendar-invite semantics (§03.08). This Type's core is invitee self-booking into host-published availability. The group-availability pass's contrast phrasing ("a time is proposed and invitees accept/decline") is hereby sharpened: the discriminator vs group availability is *whose availability defines the option set*, not the accept/decline mechanic.
- "Meeting scheduling requires video conferencing" — era-current common (all sampled modern products attach video), but platform-native and older forms satisfy the core without it.
- "Meeting scheduling = Calendly-style public links only" — platform-native (Personal Bookings) and embedded forms satisfy the core; the shareable surface is the invariant, the public-link mechanic is one implementation.
- "Round-robin/team distribution is definitional" — team-pole capability; individual scheduling satisfies the Type fully.
- "Payments are definitional" — absent from the platform-native pole; optional.
- "Meeting scheduling owns the meeting's content" — notes/recaps/action items belong to Meeting Notes / AI Meeting Assistant (§03.10); scheduling products attach them as adjacent products, not as the scheduling core.

## Boundary Findings

1. **vs Appointment Scheduling Application (§03.09 sibling — the flagged joint review)**: the two Types share the entire booking-link machinery (published availability, duration-carrying kinds, shareable booking page, calendar sync, reminders, even payments). Resolution from this side: **keep both Types; the boundary is center of gravity, and it is real but thin.** Meeting scheduling models *professional meetings between people*: meeting kinds are templates for conversations (intro calls, interviews, 1:1s, demos); the booked object is a meeting that lands as a calendar event on host and invitee calendars; there is no priced service catalog, no client ledger, no appointment policies (deposits, cancellation fees, intake forms as business records); distribution machinery (round-robin, routing) exists to put the *right person* in the meeting. Appointment scheduling models a *service business's bookable offerings*: services with prices and policies, persistent client records, operator-side appointment management, deposits/no-show handling. Corroborating evidence: Microsoft itself splits the poles inside one product (Personal Bookings = meeting types + personal page; Shared Bookings = services + staff); Calendly markets both words ("appointments and meetings"); Cal.com serves both with one event-type engine and ships payments as an optional layer. Products straddle deliberately; the pair remains the closest sibling pair in the directory and should be reviewed together whenever either is revised.
2. **vs Group Availability Scheduling Application (§03.09 sibling)**: discriminator = whose availability defines the candidate times. Meeting scheduling: the host's published availability defines the options; the invitee picks one. Group availability: participants declare their own availability; the group converges on a time. Meeting polls inside scheduling products (Calendly, SavvyCal) are bridge features, not mergers — in a poll, the organizer does not publish *their* bookable availability; they propose discrete options for voting.
3. **vs Calendar Application (§03.08)**: a calendar manages the user's own time and events, including the invite flow (propose time → invitees accept/decline). Meeting scheduling publishes availability for *external self-booking* and manages bookings as records. Calendar sync is the bridge (busy-checking, write-back); platform-native packaging (booking pages inside a calendar product) blurs the surface but not the structure: remove the booking machinery (kinds, rules, shareable booking surface) and only a calendar remains.
4. **vs Interview Scheduling Platform (§09)**: interview scheduling maintains persistent, hiring-anchored interview records with interviewer-pool reconciliation and ATS integration. Meeting scheduling is context-free: Cal.com's own documentation uses "Job Interview" as an example event type — the generic tool *hosts* the use case; the dedicated Type adds candidate records, interviewer constraints, and hiring workflow.
5. **vs Event Registration Platform (§26)**: Cal.com ships both semantics as separate features — event types ("book a time with me") vs Cal Events ("a single, fixed-date happening that guests register for"). Group event types (many invitees, one slot) sit in the overlap; when dated one-off happenings with attendee rosters dominate, the product drifts toward event registration.
6. **vs AI Meeting Assistant / Meeting Productivity (§03.10)**: scheduling ends where the meeting begins. Notetakers, recaps, and action items are adjacent products attached to scheduling platforms (Calendly Notetaker), not part of the scheduling core.
7. **vs Sales Engagement / Lead-routing platforms**: the revenue-team pole (Chili Piper) packages meeting scheduling inside lead distribution and CRM machinery. The scheduling core (meeting types, availability, booking links) is identical; routing is packaging. When lead routing rather than meeting booking is the center of gravity, the product belongs to the sales-side Types.

**"去掉什么就变成另一个 Type" 判据汇总**：
- 去掉受邀人自助预订（主办方指定时间、受邀人接受/拒绝）→ Calendar Application
- 去掉"主办方发布自己的可用性"（由参与者自报可用性凑时间）→ Group Availability Scheduling Application
- 加入服务目录/客户台账/预约政策（定价、押金、取消政策）→ Appointment Scheduling Application
- 去掉持久会议记录（输出只是选出的时间）→ Group Availability Scheduling Application
- 加入招聘语境与面试记录 → Interview Scheduling Platform
- 加入"一次性日期活动 + 报名者名册"→ Event Registration Platform

## Uncertainties

- **Google Calendar appointment schedules**: platform-native pole not directly verified this pass (support.google.com timed out twice). Documented structurally; Microsoft Personal Bookings (prior-pass direct observation) carries the platform-native evidence.
- **Calendly invitee-side reschedule/cancel**: strongly implied by the product model but not directly observed this pass (help-center category pages are JS shells); kept at moderate assertion strength.
- **Chili Piper operational details**: observed at structure level (section/article titles); no operational claims asserted.
- **Meeting state machines**: no sampled product documents a canonical state set; the lifecycle is written conceptually (booked → confirmed → held → completed / no-show; cancelled / rescheduled). Exact labels vary by product.
- **Prevalence of approval/confirmation mode**: directly observed in Cal.com and SavvyCal; not observed in Calendly/ChiliCal fetched pages this pass. Treated as optional (L2), not universal.
- **Historical naming** (ScheduleOnce/TimeTrade-class 2000s–2010s link schedulers) comes from memory/context, was not verified against sources, and is not asserted in either document. The historical check is instead carried by the platform-native sample and by the era-independence of the four L0 legs.

## Final Synthesis

The Type is best understood as **a self-booking machine for a host's meeting time**. Its world contains: host-published availability (schedules/working hours checked against connected calendars, computed into open slots), meeting kinds as duration-carrying bookable templates (event types/links with location/video, description, questions), a shareable booking surface (personal page, per-kind page, embeds, extension) on which an invitee picks a kind and a slot and books it, and the meeting as the persistent record — binding host × invitee(s) × time, manageable afterwards, and written to the participants' calendars. Around this core, mature products add booking rules (buffers, minimum notice, booking windows, start increments, frequency limits), calendar sync, video-conferencing defaults, notifications/workflows, reschedule/cancel/no-show handling, team distribution (round-robin, collective, group), booking questions, routing forms, payments, analytics, and admin controls. Platform-native packaging, open-source infrastructure, recipient-experience design, revenue-team packaging, AI assistants, and embedded meeting polls are variants. The three-sibling boundary is held by two tests: **whose availability defines the options** (host-published → this Type; participant-declared → Group Availability) and **what is booked** (a meeting between people with no service catalog or client ledger → this Type; a priced service appointment with client records and policies → Appointment Scheduling). The sharpest remaining seam is with Appointment Scheduling — shared machinery, different center of gravity — and it is recorded for joint review in STATUS.
