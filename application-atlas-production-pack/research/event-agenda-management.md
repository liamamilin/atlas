# Research Notes — Event Agenda Management

## Research Goal

Understand what "Event Agenda Management" software actually is as an Application Type: what core objects exist (sessions, tracks, the program), who composes and maintains the agenda, how the agenda is assembled and published, how attendees consume and personalize it, and how changes are handled before and during the event. Determine whether this leaf is an independent Type, a capability of Event Management Platforms, or an alias of a sibling leaf (Event Mobile App, Speaker Management, Attendee Management).

## Initial Boundary

Working hypothesis before research:

- Core use: build, publish, and maintain the schedule/program of sessions for an event (conference program, session schedule).
- Primary users: event organizers / program chairs / committees; secondary: attendees (consumption), speakers (detail supply, change alerts).
- Nearest neighbors: Event Management Platform (broader), Event Mobile App (delivery surface), Attendee Management, Speaker Management, Event Registration, Meeting Scheduling, Calendar Application, Academic Timetabling, Worship Planning (order-of-service adjacency).
- Key unknowns:
  1. Is the agenda a distinct managed object with its own machinery, or just a module view inside event platforms?
  2. What does the session record carry, and how is agenda data ingested (spreadsheets, abstract systems, speaker self-service, API)?
  3. Is attendee personalization (personal agenda) definitional or common-not-core?
  4. Is change propagation after publication part of the defining core of "management"?

## Research Questions

1. What is the unit of the agenda (session/talk/slot) and what attributes does it carry?
2. How is the agenda structured (days, tracks, rooms, parallel sessions)?
3. How do organizers author it: manual entry, bulk import, drag-and-drop from submitted content?
4. Where is the agenda published (web, app, print) and how are changes propagated?
5. How do attendees consume it: browse/filter/search, personal agenda, reminders?
6. What planner-side quality machinery exists (conflict detection, status of presenters)?
7. What optional machinery attaches to sessions (check-in, feedback, capacity/booking, livestream, materials)?
8. Where is the boundary vs Event Management Platform, Event Mobile App, Speaker Management, Meeting Scheduling, and Academic Timetabling?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Fourwaves | purpose-built academic conference platform with a dedicated "Conference Program" module | richest operational documentation of program building; academic pole |
| Whova | all-in-one event app + management platform; agenda management named as a platform capability | mid-market broad-events pole; agenda as spine of an event app |
| Cvent (Attendee Hub) | enterprise event marketing/management suite; agenda inside engagement platform | enterprise suite-module pole |
| Guidebook | generic event guide/app builder where the schedule is the central guide component | guide-builder pole; higher-ed/associations customer layer |
| Sched | standalone agenda/program-first product | market anchor only — site unreachable (403 ×2); no claims rest on it |

## Sources

All fetched 2026-09-07.

- Whova — homepage (https://whova.com/), Event App product page (https://whova.com/whova-event-app/), Event Management Tools page (https://whova.com/event-management-software/), Guides index (https://whova.com/pages/whova-guides/). Product/marketing pages with operational claims; organizer-side help center not publicly fetchable (limitation).
- Cvent — Attendee Hub product page (https://www.cvent.com/en/event-marketing-management/attendee-hub), including product FAQ. Knowledge Base (support.cvent.com) is a JS community portal — not fetched (limitation).
- Guidebook — homepage (https://guidebook.com/), Conference App page (https://guidebook.com/conference-app). Help center support.guidebook.com timed out twice (limitation).
- Fourwaves — homepage (https://fourwaves.com/), Conference Program page (https://fourwaves.com/conference-program/). Product page with unusually operational "how to build" and FAQ content.
- Sched — https://sched.com/ and https://www.sched.com/ both returned 403 (limitation; market anchor only).

## Product Observations

### Fourwaves (Evidence: A — directly observed on official product pages)

Program module page documents the program builder operationally:

- "What is a conference program builder" (vendor's own definition): the tool an organizing committee uses to turn accepted abstracts into a schedule — creating sessions with a date, time, and room, placing presentations inside those sessions, ordering them, and publishing the result as an online program, a mobile agenda, and a printable program booklet.
- Organizer workflow (six documented steps):
  1. Create sessions per day: start/end times, room, track, livestream link; color-code sessions by track.
  2. Drag accepted presentations into sessions and order them; each presentation carries title, authors, abstract, uploaded files (slides, poster, video) from the submission — "never copy-pasted" from the abstract/review modules.
  3. Check for conflicts: conflict checker flags presenters double-booked across parallel sessions, "works across tracks and rooms"; separate filter shows presenters who have not registered yet.
  4. Notify presenters: email presenters of a specific session with time/room/instructions; re-email when the session moves.
  5. Publish everywhere at once: event website, conference app, downloadable program booklet in Word or PDF with or without abstracts, with author index.
  6. Update in real time: withdrawn presenter marked/tagged "within seconds" across online program, app, and next booklet export; replacement dragged into the freed slot; "every view of the program refreshes with no re-export".
- Presentation surfaces: detailed or compact grid view; multi-day and parallel sessions; public program browsable by day and track.
- Attendee side: search by topic/track/speaker; bookmark sessions → personal agenda on the phone; speaker bios and presentation files per entry; download full program for offline; session recordings watchable through the program.
- Speaker side: speakers update bio/presentation details anytime; "receive alerts when your session changes or conflicts arise".
- Positioning claim: "The conference schedule connects every part of your event: submissions, speakers, and attendees."
- App module: "Works offline, with schedule and room changes synced automatically."

### Whova (Evidence: A on product pages; organizer-side operational docs not reachable)

- Homepage names "agenda management" and "speaker management" among platform capabilities; "personalized agendas, real-time updates" is the event app's lead claim.
- Event App page: "Replace paper programs with an easy-to-navigate, interactive digital agenda" — features listed: **Personal Agenda**, multi-track & session management, interactive maps, document sharing (slides and handouts), branding, offline access, "Instant Update at anytime".
- FAQ: attendees "check event schedules digitally without paper programs… pick the sessions and activities and create a personalized agenda."
- Management Tools page: Speaker Center — speakers upload bios, headshots, and session details directly; customer quote confirms updates auto-sync "on the speaker page and the agenda page". Check-in tiers documented: event check-in, day check-in, and **session check-in** on the same platform. Session feedback per session documented.
- Event types: conferences, trade shows, association, university, government, festival — agenda is the shared spine.

### Cvent Attendee Hub (Evidence: A on product page + FAQ)

- Product FAQ: "Attendees can build and manage their personal agendas and schedule 1:1 appointments with other attendees, sponsors, and exhibitors directly in Attendee Hub and the Event App, so meetings and sessions live in a single, unified schedule."
- Pre-event feature list: "Personal agenda building & appointment scheduling so attendees can make the most out of their time at your event"; highlight "new confirmed speakers, popular sessions and sponsors".
- During event: "Session engagement helps audiences participate through polls, surveys, and Q&A"; "Push notifications and announcements help attendees keep informed of important events and last minute changes."
- FAQ framing: "centralizing agendas, video, interactions, and exhibitor content in one place"; contrasts itself with "a standard event app [that] is typically a mobile agenda and info hub".
- AI layer (CventIQ): "From session recommendations to daily summaries."
- Platform context: Cvent also sells speaker/content management, registration, check-in & badging as separate products — agenda lives inside the engagement layer, not as a standalone SKU page.

### Guidebook (Evidence: A on product pages; help center unreachable)

- Root positioning: "Schedule, maps, tours, and every answer in your own branded app"; "One app, one source of truth"; "Update anytime. Push instantly."; "Live updates. One source of truth. A room moves, a time shifts, and everyone knows in seconds."
- Conference App page feature set: "Personalized Schedules — Attendees build their own agenda in seconds"; "Speaker & Session Details — Bios, topics, and times within easy reach"; "Push Notifications — Real-time updates"; "Make real-time changes without chasing anyone down."
- Case-study evidence of program structure: "Schedule tracks" (multiple events); "Full program agenda, with specific tracks for families, students, and guests" (FGCU orientation); "12 different content streams… presented in one easy-to-read schedule" (Festival of Marketing); "Limited seats in sessions were managed through in-app booking" (same); "Specific schedules for first-year students, transfer students, and families" (NC State); separate family/student tracks with parallel programming (Coastal Carolina).
- Customer quote: Guidebook Open API used to "integrate our custom scheduling system into Guidebook's Builder" — agenda data can be supplied from external scheduling systems.
- Customer layer: dominated by universities (orientation/admissions), associations, nonprofits — the event guide pattern, where the schedule is the anchor component of a wider guide.

### Sched (Evidence: none — unreachable)

- Well-known standalone conference-program/agenda product; Guidebook and Fourwaves both list it as a comparison/alternative, confirming its market position as an agenda-first pole. No operational claims made from it.

## Cross-product Comparison

| Dimension | Fourwaves | Whova | Cvent Attendee Hub | Guidebook |
|---|---|---|---|---|
| Session as program unit | explicit (date/time/room/track + nested presentations) | explicit (multi-track & session management) | explicit (sessions + meetings unified in one schedule) | explicit (sessions/talks with bios, topics, times) |
| Day/time program organization | multi-day grid, compact/detailed views | agenda by day (app) | unified schedule (web + app) | schedule organized by day; tracks |
| Tracks/streams | color-coded tracks | multi-track management | not directly evidenced | schedule tracks / content streams / persona tracks |
| Speakers attached to sessions | presentations carry authors + bios; speaker alerts | Speaker Center auto-syncs bios/session details to speaker page and agenda page | "new confirmed speakers" highlighted; speaker content in hub | speaker & session details in app |
| Ingestion of agenda data | from abstract/review modules (no copy-paste) | speaker self-service upload | not evidenced (KB unreachable) | external scheduling systems via API |
| Publication surfaces | website + app + printable booklet | event app (replaces paper program) | web hub + native event app | branded app + website |
| Personal agenda (attendee) | bookmark sessions → personal agenda, offline | Personal Agenda | personal agenda building + appointments | personalized schedules |
| Change propagation | real-time sync everywhere, "no re-export" | Instant Update at anytime | push notifications for last-minute changes | update anytime, push instantly; "room moves… everyone knows in seconds" |
| Conflict detection | conflict checker (double-booked speakers across tracks/rooms) | not evidenced | not evidenced | not evidenced |
| Session-level engagement | session recordings in program | session check-in, session feedback | session polls/Q&A/surveys | not evidenced (event QR check-in) |
| Session capacity/booking | not evidenced | not evidenced | not evidenced | limited seats via in-app booking (one case study) |
| Print/export | booklet (Word/PDF, author index) | anti-print positioning | not evidenced | anti-print positioning (case studies) |
| Audience segments in one program | tracks | tracks | appointments across attendee types | tracks per persona (students/families/guests) |

Reading of the table:

- **Universal across the sample (4/4 direct):** session as the program unit; day/time organization; publication to an audience-facing surface (web and/or app); attendee personal agenda; change propagation after publication.
- **Strong commonality (3/4 direct):** speakers attached to session records with sync; search/filter/browse; notifications about changes.
- **Common but not universal:** tracks/streams (3/4; Cvent not directly evidenced), materials/recordings attached to sessions, ingestion machinery (mechanism varies: abstract pipeline, speaker self-service, API).
- **Single-product evidence:** conflict checker (Fourwaves), session check-in + session feedback (Whova), session polls/Q&A (Cvent), session capacity booking (Guidebook), printable booklet (Fourwaves), persona-segmented tracks (Guidebook). All treated as optional/variant, never canonical.

## Abstraction Levels

### L0 — Defining Invariant

Three structures; remove any one and the product is no longer Event Agenda Management:

1. **The event's session record.** A persistent, identified unit of the program — a session/talk/activity — carrying at minimum a title and a date-time placement within the event; commonly extended with place, people, category, description, materials. Remove → a pile of event documents or a generic notes tool.
2. **The agenda as the event's ordered program under organizer authoring and continued maintenance.** Sessions are composed into a day/time-ordered whole owned by the organizing side, which keeps composing and revising it through the event's life. Remove → a static snapshot, not management; a personal calendar tool.
3. **An audience-facing published program.** The agenda is rendered for the event's audience beyond the planning team — the rendering surface is an implementation choice (printed program, website, app, screens), but a published program view must exist. Remove → internal planning document (which is a calendar/planning tool, a different Type).

Not in L0 despite market expectations: multi-track, personal agendas, apps, real-time push, speaker management, rooms. All fail the historical check below.

### L1 — Common Mature Structure

- Tracks/streams/categories with visual coding, enabling browsing of parallel programs.
- Speakers/presenters as records attached to sessions (bios, photos), commonly synced from a speaker-management surface.
- Session types (keynote, break, workshop, poster) and descriptions.
- Search/filter/browse by day, track, speaker, topic.
- Personal agenda: attendee bookmarks/favorites compose a personal schedule derived from the master program.
- Multi-surface publication from one source of truth (web program page, event app, embeds; print export at some products).
- Change propagation: planner edits after publication reach published surfaces; participants alerted (push/email).
- Agenda data ingestion from outside the agenda editor: spreadsheets, abstract/review systems, speaker self-service, APIs.
- Rooms/locations on sessions; venue/map linkage at some products.
- Session materials (slides, handouts, recordings) attached to session entries.

### L2 — Variant / Optional Structure

- Conflict/double-booking detection and presenter-status filters (documented at one product; likely wider in practice, evidence insufficient to generalize).
- Session capacity limits with in-app session booking/registration (documented in one case study).
- Session check-in, session-level attendance tracking, session feedback/polls.
- Livestream links per session for hybrid events; on-demand session recordings in the program.
- AI session recommendations / daily summaries.
- Printable program booklets / proceedings export.
- Audience-segmented program variants (tracks per persona; separate guest programs).
- White-label/branded delivery of the published agenda.

### L3 — Vendor-specific Structure (Research Notes only)

- Fourwaves: withdrawn-presenter tagging semantics, registration-status filter beside the conflict checker, booklet export with author index, "no re-export" real-time framing, six-step documented build flow.
- Whova: Speaker Center auto-sync quote, event/day/session check-in tiers, 50+ page post-event report, MicroEvents tier.
- Cvent: CventIQ session recommendations/daily summaries, Appointments module as sibling add-on, "standard event app" comparison framing.
- Guidebook: Branded app deployment tiers, Open API for external scheduling systems, Slate integration (higher-ed CRM), "12 content streams" case study.
- Sched: unreachable; no claims.

## Rejected Findings

- "Agenda management = a feature of event apps" — rejected: purpose-built program builders and standalone agenda products exist as a distinct market pole; the agenda has its own authoring machinery, ingestion pipelines, and publication surfaces even when packaged inside a suite.
- "Real-time push is definitional" — rejected: the invariant is that maintained changes reach the published program; instant digital propagation is the modern mechanism (paper era: reprints, corrected notice boards).
- "Personal agenda is definitional" — rejected: printed-program-era agenda management has no personalization; personal agenda is the dominant modern consumption pattern but not the defining structure.
- "Tracks are definitional" — rejected: single-track/single-room programs (research days, one-day seminars) are fully in-type; Fourwaves' own copy covers "a one-day research day with a single room".
- "Print export is definitional" — rejected: two sampled products position themselves as paper-program replacements; booklet export is an era-typical optional output.
- "Agenda data always comes from an abstract pipeline" — rejected: ingestion mechanisms vary (hand entry, spreadsheets, speaker self-service, APIs, abstract systems); only the academic pole ties it to peer-review output.

## Boundary Findings

- **vs Event Management Platform (Event Management Software):** center-of-gravity test. EMP's center is the attendee lifecycle (registration, ticketing, marketing, check-in, analytics); the agenda is one module. Event Agenda Management's center is the program record: compose sessions, organize the program, publish and maintain it. Removing registration/ticketing still leaves this Type intact (standalone agenda products sell without it); removing the agenda machinery leaves an EMP intact. The two interlock (agenda ↔ registration ↔ check-in) but neither subsumes the other's center.
- **vs Event Mobile App:** the app is a delivery surface that contains agenda + networking + maps + sponsor content. The agenda Type's output can be an app, a website, a booklet, or all three. Test: if the product's only surface is an app and the agenda is one component among many, it is an Event Mobile App with an agenda capability; if the product is organized around building/maintaining/publishing the program (any surfaces), it is this Type.
- **vs Speaker Management:** speaker-centric (collect bios/headshots/materials from speakers, speaker pages) vs program-centric (sessions in time). They interlock: speaker updates sync into the agenda. Sibling leaf stands.
- **vs Attendee Management / Event Registration:** attendee records, registration, badging vs program records. Session check-in and session-capacity booking are the contact points (optional capabilities), not the center.
- **vs Meeting Scheduling Application / Calendar Application:** those schedule people's time and hold personal calendars; the agenda schedules a public program for an event audience. The attendee "personal agenda" is a derived consumption view (bookmarks of program sessions), not a scheduler. Appointment-setting between attendees (Cvent pole) is adjacent machinery that some agenda surfaces unify.
- **vs Academic Timetabling:** institutional, recurring, resource-constrained course/room scheduling with optimization; the agenda is event-scoped, session-based, publication-oriented, with no recurring-term or resource-optimization machinery at its center. (One sampled vendor explicitly frames itself against "generic scheduling tools.")
- **vs Worship Planning / order-of-service tools:** a church order of service is a small analog of an event program; Worship Planning's center is service planning within a church-management context. The agenda Type is event-industry-agnostic; no need to merge, but the shared lineage ("program" as a published run-of-show) is noted.
- **Capability-vs-Type question (recorded, not silently resolved):** the dominant market realization is as a module inside event platforms (2 of 4 sampled) or guide builders (1 of 4), with a standalone-specialist pole (Sched-class) and a dedicated-program-module pole (Fourwaves) keeping the Type independently recognizable. The leaf is kept as a Type with the module realization documented as a variant, mirroring how the directory treats sibling surfaces (Event Mobile App, Speaker Management). Joint review with Event Mobile App / Speaker Management recommended at directory level.

### The "remove what" test

- Remove the session record and its program assembly → nothing remains but documents and messages: not the Type.
- Keep sessions but remove organizer authoring/maintenance → a static published page: not management.
- Keep authoring but remove audience-facing publication → an internal planning/calendar tool: not this Type.

## Historical / Market-Sample Check

- Pre-digital: printed conference programs, theatre/event programs, church bulletins, orders of service, congress program booklets — a structured, time-ordered program of sessions, authored by organizers, published to the audience, revised through reprints and corrected schedules. All satisfy the L0 triple. The modern sample adds personalization, multi-surface sync, and instant propagation — kept out of L0.
- Regional/segment breadth: academic congresses (Fourwaves), association conferences and corporate events (Whova, Cvent), university orientation/admissions guides (Guidebook), standalone conference agenda products (Sched). A single-track research day and a 12-stream festival both fit the core. No era or segment overfit detected.

## Uncertainties

- Organizer-side operational documentation for Whova and Cvent (help centers) was not reachable; authoring mechanics (bulk import UIs, exact session fields) are evidenced directly only at Fourwaves and partially at Guidebook (API quote). Assertions about typical session fields are calibrated accordingly.
- Guidebook's help center timed out; its capabilities are evidenced from product pages and case studies only.
- Conflict detection is evidenced at one product; it may be common in mature program builders, but the sample cannot confirm — kept optional.
- Sched (the purest standalone pole) could not be examined; the "standalone agenda product" pole rests on market anchors (competitor comparison pages) rather than direct documentation.
- Whether session-level attendance/check-in is rising toward standard could not be established from this sample; left as optional.

## Final Synthesis

Event Agenda Management is the event's program system of record: the organizing side composes sessions (title, time, and commonly place, people, category, materials) into the event's ordered multi-day program, keeps maintaining that program as reality changes, and publishes it to the event's audience on one or more surfaces, with changes propagating to what was already published. Attendees consume the program — browse, search, filter — and, in the dominant modern pattern, derive a personal agenda from it. Everything else (tracks, speaker sync, ingestion pipelines, conflict detection, session check-in, capacity booking, livestreams, booklets, AI recommendations) is common, optional, or product-specific structure layered on that spine. The Type is realized in the market both as standalone agenda/program products and as a module of event management suites and guide builders; its nearest boundaries are Event Management Platform (attendee lifecycle is the center there), Event Mobile App (a delivery surface, not the program record), and Speaker Management (person-centric counterpart).
