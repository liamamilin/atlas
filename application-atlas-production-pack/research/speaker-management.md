# Research Notes — Speaker Management

Research date: 2026-09-10
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what "Speaker Management" software actually is as an Application Type in the events market: what core objects exist (speaker records, session assignments, materials, tasks), who uses it (organizers vs speakers), what the speaker-side and organizer-side workflows are, how it interlocks with the event agenda and attendee systems, and whether this leaf is an independent Type, a suite capability, or an alias of a sibling leaf (Event Agenda Management, Attendee Management, Abstract Management).

## Initial Boundary

Working hypothesis before research:

- Core use: collect, maintain, and coordinate the people who present at an event — their profiles (bio, headshot, title), their session assignments, their materials (slides, videos), their requirements, and the communications around their participation.
- Primary users: event organizers / program teams / speaker coordinators; secondary: speakers themselves (self-service portals).
- Nearest neighbors: Event Agenda Management (program-centric sibling), Attendee Management (roster-centric sibling), Event Management Platform (broader suite), Abstract Management (academic intake pipeline), speaker-bureau / talent-booking software (different domain), CRM.
- Key unknowns:
  1. Is the speaker record the core object, and what does it minimally carry?
  2. Is there a definitional coordination loop (collection, tasks, reminders), or is this just a published speaker page?
  3. Is the call-for-speakers/submission pipeline definitional or one intake variant?
  4. Is this an independent Type or only a module of event platforms?
  5. Where exactly is the boundary vs Event Agenda Management (the pending joint-review flag)?

## Research Questions

1. What is the speaker record and what does it carry (bio, headshot, title, affiliation, contact, social links)?
2. How are speakers linked to the event's sessions/presentations, and what is the cardinality?
3. How do speakers enter the system (organizer manual add, agenda auto-add, call-for-speakers, import)?
4. What organizer-side coordination machinery exists (tasks, deadlines, reminders, communications, tracking)?
5. What speaker self-service exists (portal, profile editing, material upload, schedule view, alerts)?
6. What is collected beyond profiles (slides, videos, handouts, A/V needs, dietary, accessibility, agreements, travel)?
7. How do speaker updates propagate to event surfaces (agenda, app, website, signage)?
8. Where is the boundary vs Event Agenda Management, Attendee Management, Abstract Management, Event Management Platform, and speaker-bureau software?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Cvent | enterprise suite with a dedicated Speaker Resource Center / speaker management product line | enterprise suite-module pole; richest task/portal documentation |
| Whova | mid-market all-in-one platform with a dedicated "speaker management software" product page | mid-market pole; vendor's own category definition; self-service + sync evidence |
| Swoogo | registration-centric platform; Call for Speakers paid add-on + public API object model | registration-centric pole; API documents the canonical object model |
| Fourwaves | academic conference platform, program-first | academic pole; speaker-side self-service and change alerts |
| Lineup Ninja | standalone speaker management & conference content product | standalone specialist pole (capability-vs-Type anchor) |
| Submitto | minimal standalone speaker collection tool | minimal pole — proves how thin the Type can be and still hold |
| OpenWater | abstract-management platform with Speaker Manager add-on module | post-acceptance boundary anchor vs Abstract Management |

## Sources

All fetched 2026-09-10 unless noted.

- Cvent — Speaker Resource Center product page: https://www.cvent.com/en/event-management-software/speaker-resource-center ; Speaker Management Software page: https://www.cvent.com/en/event-management-software/speaker-management-software ; Content Management page: https://www.cvent.com/en/event-marketing-management/content-management ; Abstract Management page: https://www.cvent.com/en/event-marketing-management/abstract-management-software (search-surfaced highlights + full fetch of Speaker Resource Center).
- Whova — Event Management Software page: https://whova.com/event-management-software/ ; Event Speaker Center page: https://whova.com/event-management-software/event-speaker-center/ ; All-in-One Speaker Management Software page: https://whova.com/speaker-management-software/ ; Abstract Management page: https://whova.com/abstract-management/ .
- Swoogo — Call for Speakers page: https://swoogo.events/call-for-speakers/ ; Event Logistics page: https://swoogo.events/event-logistics/ (search-surfaced highlights) ; Developer API speakers overview: https://developer.swoogo.com/api-reference/overviews/speakers .
- Fourwaves — Conference Program page: https://fourwaves.com/conference-program/ (includes organizer/speaker/participant role sections and FAQ).
- Lineup Ninja — homepage: https://lineup.ninja/ .
- Submitto — Speaker Management page: https://submitto.io/speaker-management (search-surfaced highlights; official site).
- OpenWater — Speaker Management Software page: https://openwater.com/speaker-management-software (search-surfaced highlights; official site).
- MemberRun — Conference Planners solutions page: https://memberrun.com/solutions/conference-planners (search-surfaced highlights; official site; secondary anchor only).

Access limitations:
- Cvent Knowledge Base (support.cvent.com) is a JS portal — not fetched (consistent with prior passes). Cvent claims rest on official product pages.
- Swoogo help center and deep help articles not fetched; Swoogo claims rest on product pages + developer API docs.
- Submitto / OpenWater / MemberRun evidence comes from official-site content surfaced via search, not full-page fetches; claims from them are calibrated accordingly and used mainly as packaging-pole anchors.
- No precise numeric limits, default settings, or exact state-name vocabularies are asserted anywhere; moderate claim strength used throughout.

## Product Observations

### Cvent (evidence layer: A — directly observed on official product pages)

- Dedicated product line: "Speaker Resource Center" works with Cvent Event Management to "streamline communications with your speakers and collaborate with them on logistics and content."
- Organizer side:
  - **Task management**: "create all the necessary tasks for your event, with the flexibility to assign them to all speakers or individual ones"; "speaker task and session reports" give "a clear view of task progress."
  - **Notifications**: "Schedule branded task reminders to speakers using templates"; "Send custom emails to any speaker"; framing: "There's no more need to track down speaker agreements, headshots, bios, session information, or presentation slides."
  - Value framing: automate tedious tasks / collect all speaker content "in one central location" / reports on task completion + branded reminders.
- Speaker self-service portal (direct link provided to speakers):
  - View tasks and deadlines **by session**
  - Mark tasks as complete
  - View and modify their speaker profile and session details
  - Answer questions from the event organizer
- Content Management page (broader content/speaker curation): "Easily source speakers, build intuitive agendas"; "Assign speaker tasks and get alerted to edits"; "Collect on-site or virtual requirements with questionnaires"; "Allow speakers to update their profiles and session information"; "Provide speaker-specific information through custom web pages and targeted emails."
- Abstract Management page: CFP workflow Collect→Review→Decide→Publish; "capture full speaker details in one place"; accepted submissions become sessions in the agenda; automated invitation/confirmation/reminder/decision emails. Speaker management is positioned as the machinery *after* selection ("publish final content selections… build your agenda").
- Speaker Management Software page: "manage their details and information easily"; "showcase speakers and profiles throughout the event website and registration pages."

### Whova (evidence layer: A — directly observed on official product pages)

- Dedicated product page titled "All-in-One Speaker Management Software": "a centralized hub to handle everything" — speaker applications, dedicated communication, bios, session updates.
- Vendor's own category definition (FAQ): "Speaker management software handles the process of recruiting, accepting and managing speakers for events and conferences." Key features listed: online call for speakers; information collection (bios, dietary restrictions, accessibility needs, AV needs); communication (venue info, itineraries via dedicated email/chat); centralized management (organizer can "manually add, edit or delete any speakers"); promotion (scheduled/automated emails, in-sync speaker webpages); reporting (speaker engagement and session attendance).
- Data collection: customizable speaker forms; speakers directly input "bios, photos, talk details"; custom fields "such as A/V needs, dietary restrictions and accessibility needs"; scheduled emails with links to their speaker forms.
- Central hub mechanics: "adding session speakers in the agenda automatically adds them to Whova's Speaker Center"; "update speaker information in one place and automatically sync in event app, website and more"; dedicated speaker email templates (welcome, logistics, registration).
- Speaker self-service: personal form to "submit their bio, upload a photo, provide handouts, write session descriptions, and list discussion topics"; individual links let speakers "create polls… manage their Q&As before or during the session, and even upload resources or their presentation."
- Messaging portal: draft/schedule/send emails to speakers; message individual or multiple speakers via app or web; dashboard shows "a timestamp… everything that was sent, how many, who was not responding."
- Call for Speakers intake: branded submission portal; live status from incomplete to submitted; "Automatically add speakers from accepted submissions to speaker management hub"; CFS-collected info (name, email, affiliation, job title, bio, profile pic) "auto-populate into the speaker center once their talks are added to the agenda."
- Publication: speaker webpage templates (16), hosted or embedded; "Publish once, update anytime. All speaker information changes are automatically synced"; customer quote (100+ speakers): self-updates "automatically being updated and published on the speaker page and the agenda page."
- AV requirements: collected via speaker form; "organizers can find the responses to AV requirement questions within the speaker manager"; appears as its own column in the exported sheet.
- Promotion: automated email campaigns featuring speakers; ready-to-share social images for organizers and speakers.

### Swoogo (evidence layer: A on product pages + developer API docs)

- Developer API — canonical object model (directly documented):
  - "Speakers are presenters associated with event sessions. Each speaker has profile information — name, bio, company, photo — and can be linked to one or more sessions."
  - Capabilities: "Create and manage speaker profiles with biographical details and photos"; "Assign speakers to sessions — link a speaker to one or more agenda items"; "Remove speaker assignments when schedules change."
  - **Speaker-session linking is many-to-many**: "A speaker can present at multiple sessions, and a session can have multiple speakers."
  - Profile data: "name, title, company, biography, and social links. This information is typically displayed on event websites and in the event agenda."
  - Relationships: Events (the event), Sessions (assigned sessions), Images (profile photos).
- Call for Speakers (paid add-on): submission website; submission forms ("The data you need from speakers is different from attendees"); automated emails for reviews/acceptance; "Turn submissions into sessions — one click and it's in your Swoogo event as a session"; safe file storage ("No hunting for decks or documents on event day"); review/grading portal; call-for-papers/abstract management; "Standardize your speakers' journey from beginning to end — automate the communications that guide your speakers through all their pre-event steps, from acceptance to due date"; speaker types customized to complement attendee types; cloneable.
- Event Logistics page: "Direct your presenters to the correct (online or in-person) room… with your favorite streaming integrations"; "Need a full-on speaker portal? Check out our Call for Speakers add-on!"
- In-person events page: "A complete solution for managing speakers and multi-track schedules. Build multi-track schedules, onboard guest speakers and headliners in seconds, and manage content from call-for-speakers to show day."

### Fourwaves (evidence layer: A — directly observed on official product pages)

- Academic, program-first platform; speaker side documented as a first-class role ("I'm a speaker"):
  - "Update your bio and presentation details anytime"
  - "Upload slides, posters, videos, and supporting material"
  - "Receive alerts when your session changes or conflicts arise"
  - "Submit once and keep everything updated for a stress-free experience."
- Organizer side touching speakers:
  - Conflict checker "flags presenters who are double-booked across parallel sessions… works across tracks and rooms"; separate filter shows "presenters who have not registered yet."
  - "Notify presenters. Email the presenters of a specific session with their time, room, and instructions, and email them again if the session moves."
  - Withdrawn presenter: marked/tagged "within seconds" across online program, app, and next booklet export; replacement dragged into the freed slot.
  - Presentations carry "title, authors, abstract, and uploaded files (slides, poster, video) from the submission" — never copy-pasted from the abstract module.
- Publication: speaker bios and presentation files attached to program entries; attendees "open speaker bios and presentation files from each entry."
- Positioning: "The conference schedule connects every part of your event: submissions, speakers, and attendees."

### Lineup Ninja (evidence layer: A — directly observed on official homepage; standalone pole)

- Self-positioning: "Advanced speaker management software for ambitious conference producers, marketers and operations teams" — a standalone product, not a suite module.
- Three documented pillars:
  1. **Streamlined Content Collection** — custom workflows for the content collection process; automated speaker communication and task tracking; "Content portal gives speakers a simple submission and onboarding journey by providing a single place for tasks and communication"; team-shared speaker communications; file collection (slides, videos); submission & review; awards submissions.
  2. **Easy Agenda Planning** — smart drag-and-drop scheduler; speaker availability and clash detection "as standard"; rule-based session scheduling; auto-scheduling; diversity reporting.
  3. **Painless Content Distribution** — "the single source of truth for your agenda, that can publish to your website, marketing platform, matchmaking app, virtual event platform and digital signage"; "Make agenda changes in one place; update everywhere"; "AV technicians can pull the latest versions of slide decks down for presentation on the show floor."
- Customer evidence of scale/shape: "5 events (each with 4-5 stages & 100+ speakers)"; "3 days, 14 stages, 180 sessions, 400 speakers, 12 professional moderators" — moderators as managed participants; "speakers… able to use the portal to upload and amend their sessions throughout the content collection process"; "speaker and agenda information in one place with the ability to push out changes to the website, apps and digital signage in real-time."

### Submitto (evidence layer: A− — official site content via search; minimal pole)

- Positioning: "Speaker management software for conferences and events. You collect every slide, bio, and headshot through one link, renamed and sorted by session and tracked against your roster."
- Mechanics: one speaker link (no account) collects deck + bio + headshot with per-item fields/formats; files "arrive renamed to your convention and sorted by session"; submission-tracking dashboard "built from your roster" showing who is in/missing; one-click reminders to everyone outstanding; AV team gets "a read-only speaker ready room, files already grouped by session"; roster built by uploading a spreadsheet "built from your days and sessions."
- Explicit scope boundary: "You use Submitto to collect files, not to handle contracts, so there is no speaker agreement template here. It is good at what comes after the agreement." — confirms agreements/contracts sit adjacent to the Type's center.

### OpenWater (evidence layer: A− — official site content via search; post-acceptance anchor)

- Definition: "Speaker management software helps conference and program teams collect participant information, assign requirements, track outstanding materials, and organize speakers across sessions… bios, headshots, disclosure forms, presentation files, and other post-acceptance requirements."
- Framing: "Accepting an abstract is only the beginning" — speaker management is the post-acceptance machinery.
- Structures: centralized participant profiles ("one complete record for each speaker, even when that person serves in multiple roles or appears in multiple sessions"); participant types (Speaker, Moderator, Author, Panelist) with role-specific required fields and workflows; configurable tasks (upload headshot, submit bio, sign disclosure, sign agreement, upload materials) assignable by program/type/session/individual; participant dashboard (update profile, view sessions/applications, see outstanding items); searchable public speaker gallery linked to sessions/abstracts.
- Packaging: "built into the existing OpenWater platform as an add-on module that expands the speaker and participant management capabilities of the abstract management process."

### MemberRun (evidence layer: A− — official site content via search; secondary anchor)

- "Speaker profiles with bios, headshots, session assignments, and contact details, all in one place… Speakers can update their own profiles."
- "Speaker portal with magic-link auth": speakers update bio, upload headshot and slides, "complete the speaker agreement, and submit travel preferences. You see readiness % per speaker."
- Problem framing matches the Type's reason to exist: "Bios, headshots, session descriptions, AV requirements, travel details, scattered across 47 email threads."

## Cross-product Comparison

| Dimension | Cvent | Whova | Swoogo | Fourwaves | Lineup Ninja | Submitto |
|---|---|---|---|---|---|---|
| Speaker record with profile content | profile + session details, modifiable by speaker | bio, photo, talk details, custom fields | name, title, company, bio, photo, social links (API) | bio + presentation details, speaker-updatable | participant profiles, role-typed | bio + headshot via link |
| Session/presentation assignment | tasks & deadlines **by session**; session details | agenda auto-adds speakers to hub; session info in forms | many-to-many speaker↔session (API) | presentations nested in sessions; authors carried | sessions linked to speakers; clash detection | files sorted **by session** from roster |
| Organizer collection/coordination loop | task assignment (all/individual), reports, branded reminders | forms + scheduled emails + messaging portal + templates | CFS journey automation "from acceptance to due date" | presenter emails per session; re-email on change | custom workflows, automated comms, task tracking | tracking dashboard + one-click reminders |
| Speaker self-service | portal: tasks, deadlines, profile/session edits, answer questions | personal form: bio, photo, handouts, descriptions, polls/Q&A | portal via CFS add-on | update bio/details, upload materials, change alerts | portal: upload and amend sessions | one link, no account, editable |
| Materials collection | agreements, headshots, bios, session info, slides | documents, handouts, resources, presentations | decks/documents stored in portal | slides, posters, videos, supporting files | slides, videos | decks (+bio/headshot), renamed per convention |
| Intake paths | manual + questionnaires; CFP via Abstract Mgmt | manual add + agenda auto-add + CFS portal | manual (API) + CFS add-on | from abstract/review modules | submission & review + manual | spreadsheet roster import |
| Custom questionnaires | on-site/virtual requirements | A/V needs, dietary, accessibility | (CFS forms customizable) | — | custom workflows | dietary/parking/mic (The Project Crew analog) |
| Publication to event surfaces | event website + registration pages | speaker webpage + app + agenda page | event websites + agenda (API) | program entries (bios + files) | website, apps, signage, matchmaking/virtual platforms | none (AV read-only room only) |
| Change propagation to speakers | reminders, custom emails | messaging portal, scheduled emails | automated journey emails | alerts when session changes/conflicts | automated comms | one-click reminders |
| Review/selection machinery | separate Abstract Management product | separate Abstract Management product | CFS includes review/grading portal | separate peer-review module | submission & review included | none (post-agreement scope) |
| Agreements/contracts | "track down speaker agreements" (collected via tasks) | not evidenced | not evidenced | not evidenced | not evidenced | explicitly excluded |
| Role typing | speakers (individual/all assignment) | speaker types (badge color-coding) | speaker types ↔ attendee types | presenters/authors | moderators as managed participants | — |
| Packaging | suite product line | suite product page + module | paid add-on | integrated platform module | standalone product | standalone micro-tool |

Reading of the table:

- **Universal across the sample (6/6):** the speaker record with presentation-facing profile content; binding to sessions/presentations; an organizer-side collection & coordination loop; speaker self-service submission of profile/materials; materials collection (slides at minimum).
- **Strong commonality (4–5/6):** dedicated speaker communications; custom questionnaires (A/V, dietary, accessibility); publication of speaker profiles to event surfaces; change propagation to speakers.
- **Common but not universal:** review/selection machinery (bundled at Swoogo/Lineup Ninja, separate products at Cvent/Whova/Fourwaves, absent at Submitto); agreements/contracts; role typing beyond speaker; publication breadth (signage, matchmaking platforms).
- **Single-product evidence:** readiness-% per speaker (MemberRun), AV export column (Whova), withdrawn-presenter tagging (Fourwaves), auto-scheduling (Lineup Ninja), diversity reporting (Lineup Ninja). All optional/variant.

## Abstraction Levels

### L0 — Defining Invariant

Three jointly-held structures; remove any one and the product is no longer Speaker Management:

1. **The speaker record.** An identified person held by the organizing side in a presentation role at a specific event — speaker, panelist, moderator, chair — carrying presentation-facing profile content destined to represent that person in the event's program (name at minimum; bio, headshot, title/affiliation as the mature content). Remove → a generic contact list or CRM.
2. **The program assignment.** The speaker's link to the event's sessions/presentations — what they present and where it lands in the program; many-to-many (a speaker across multiple sessions, a session with multiple speakers). Remove → a talent roster or address book with no event-program binding.
3. **The organizer-managed collection & coordination loop.** The organizer runs a managed, persistent process over the speaker population: collecting and completing profiles and materials, coordinating tasks and deadlines, and communicating with speakers about their participation (invitations, forms, reminders, change alerts). Remove → a static speaker directory or the agenda's speaker attachments — publication without management.

Joint load-bearing test:

- 1 alone = a list of notable people.
- 2 without 1 = the agenda's session records with names attached (Event Agenda Management's territory).
- 3 without 1+2 = a generic form/task/communication tool.
- 1+2 without 3 = a published speaker directory (a capability, not management).
- 1+3 without 2 = bureau-style talent coordination with no program binding (a different domain).
- 2+3 without 1 = session logistics with anonymous presenters.

Not in L0 despite market expectations: call-for-speakers pipelines, review/scoring, speaker webpages, real-time sync, agreements, travel logistics, A/V questionnaires, role typing, reporting. All fail the historical check below or rest on partial evidence.

### L1 — Common Mature Structure

- **Presentation-facing profile content** — bio, headshot, title, affiliation, social links (documented verbatim in Swoogo's API; universal in sample).
- **Speaker self-service portal** — speakers update their own profiles, upload materials, view tasks/deadlines by session, view session details; access commonly via personal link, sometimes without an account.
- **Materials collection** — slides, posters, videos, handouts, supporting files; often organized/renamed per session for downstream use (AV handoff).
- **Task assignment & tracking** — organizer-defined tasks (headshot, bio, disclosure, agreement, materials) assigned by program/type/session/individual, with progress visibility and completion tracking.
- **Dedicated speaker communications** — templates, scheduled/bulk emails, messaging portals with delivery/response visibility; change alerts when sessions move.
- **Custom questionnaires** — A/V needs, dietary restrictions, accessibility needs, on-site/virtual requirements.
- **Publication of speaker profiles to event surfaces** — speaker webpages, event app, agenda pages, program entries; one-place updates syncing everywhere.
- **Multiple intake paths** — organizer manual add, auto-add from agenda or accepted submissions, call-for-speakers portals, spreadsheet/API import.
- **Role/category typing** — speaker types (keynote, panelist, moderator, author) driving forms, badges, and audience matching.

### L2 — Variant / Optional Structure

- **Call-for-speakers / submission & review machinery** — branded submission portals, reviewer assignment, scoring rubrics, blind review, conflict-of-interest detection; the conference/academic pole. Not required: invited-speaker models (keynotes, headliners) enter by manual add.
- **Agreements, disclosures, consents** — speaker agreements, disclosure forms collected as tasks (Cvent, MemberRun, OpenWater); explicitly out of scope at the minimal pole (Submitto).
- **Travel & on-site logistics** — travel preferences, hotel, registration-status tracking, comped registration (MemberRun, Fourwaves' unregistered-presenter filter, Cvent questionnaires).
- **Promotion machinery** — speaker webpages as marketing surface, social share images, email campaigns featuring speakers (Whova).
- **Speaker-side engagement tools** — speakers managing session polls/Q&A, messaging attendees (Whova).
- **Post-event reporting** — speaker engagement, session attendance (Whova FAQ).
- **Virtual/hybrid presenter logistics** — streaming-room assignment, virtual requirements (Swoogo, Cvent).
- **Downstream distribution breadth** — digital signage, matchmaking apps, virtual event platforms, marketing platforms as publication targets (Lineup Ninja).
- **Auto-scheduling / diversity reporting** (Lineup Ninja) — agenda-side extras at the straddle zone.

### L3 — Vendor-specific Structure (Research Notes only)

- Cvent: "Speaker Resource Center" product naming; task/session reports; "get alerted to edits"; questionnaires for on-site/virtual requirements; positioning of Speaker Management as distinct from Abstract Management.
- Whova: "Speaker Center" naming; 16 webpage templates; messaging dashboard with response tracking ("who was not responding"); AV needs as export column; auto-add from agenda; CFS auto-population field list (name, email, affiliation, job title, bio, profile pic); social share images for speakers.
- Swoogo: CFS as flat-priced add-on; speaker types complementing attendee types; cloneable CFS; API object model (Events/Sessions/Images relationships); "onboard guest speakers and headliners in seconds."
- Fourwaves: withdrawn-presenter tagging semantics; registration-status filter beside the conflict checker; presenter emails tied to session moves; booklet author index.
- Lineup Ninja: auto-scheduling tool; rule-based session scheduling; lineup diversity reporting; AV slide-deck pull on show floor; moderators as first-class managed participants.
- Submitto: file-renaming conventions; AV read-only room; roster-from-spreadsheet flow; explicit no-contracts scope.
- OpenWater: participant types with per-role workflows; readiness tracking; gallery layouts.
- MemberRun: magic-link portal; readiness % per speaker.

## Rejected Findings

- **"Speaker management = call for speakers"** — rejected. The invited-speaker model (manual add, agenda auto-add) is fully in-type at every sampled product; CFS/submission pipelines are one intake variant concentrated in the conference/academic pole.
- **"Speaker management = a speaker webpage"** — rejected. Publication is an output; the minimal pole (Submitto) publishes nothing publicly and remains unmistakably speaker management. The coordination loop is the management.
- **"Speakers always self-register into a portal"** — rejected. Organizer-side manual add/edit/delete is universal; self-service is the dominant modern pattern, not the definition.
- **"Abstract review is part of the Type"** — rejected. Review/selection is Abstract Management's center; speaker management begins at/after acceptance (OpenWater's own framing). Several products ship both; the machinery is separable.
- **"Speaker agreements/contracts are definitional"** — rejected. Collected as tasks at some products, explicitly excluded at the minimal pole.
- **"Speaker management is only a suite module"** — rejected. Standalone products (Lineup Ninja, Submitto) exist and keep the Type independently recognizable; module realization is the dominant packaging, not the identity.

## Boundary Findings

- **vs Event Agenda Management (joint review — DISCHARGED from this side):** the agenda pass characterized this Type as "speaker-centric (collect bios/headshots/materials from speakers, speaker pages) vs program-centric (sessions in time)" — CONFIRMED from the speaker side. The two Types interlock on shared data: agenda auto-adds speakers (Whova), speaker updates sync into agenda pages (Whova, Fourwaves), speaker-and-agenda-in-one-place with real-time push (Lineup Ninja). Remove-test: remove the person-collection/coordination loop from a bundled product → Event Agenda Management remains (program record, publication, change propagation); remove the session/time machinery → Speaker Management remains (profiles, materials, tasks, communications). Neither subsumes the other's center. **Keep both — RATIFIED.** Bundling (Lineup Ninja, Fourwaves, suite vendors) is packaging, not identity.
- **vs Attendee Management:** attendee records carry a participation lifecycle (expected → present) and operations-facing data (badges, check-in); speaker records carry a presentation role and presentation-facing content (bio, headshot, materials) with task coordination. Contact points: speakers commonly also register as attendees (registration-status filters, comped registration, speaker badge types); session check-in touches both. Removing the presentation-role content and coordination from speaker management leaves a roster → Attendee Management; removing the roster/attendance machinery leaves speaker coordination intact. Keep both.
- **vs Abstract Management:** CFP submission → review → decision is Abstract Management's center; the accepted person's profile, materials, tasks, and communications are Speaker Management's center. OpenWater states the seam directly: "Accepting an abstract is only the beginning." Bundled in suites (Cvent, Whova, Swoogo); separable in principle and in packaging (Submitto has no intake pipeline; Fourwaves keeps them as linked modules). Keep both.
- **vs Event Management Platform:** the dominant realization is as a module/product line inside suites (Cvent, Whova, Swoogo, OpenWater add-on). A standalone pole exists (Lineup Ninja positions itself as speaker-management software; Submitto is a dedicated micro-tool), keeping the Type independently recognizable. Capability-vs-Type resolved per the sibling-event-leaf precedent (event-agenda-management, event-mobile-app): keep as a Type with module realization documented as a variant.
- **vs speaker-bureau / talent-booking software (Artist Booking Platform, Talent Agency Management, §27):** agency-side products manage a persistent roster of represented speakers booked across many events (bookings, fees, contracts); this Type manages the event-side population for one event's program (profiles, session assignments, materials, coordination). Different object worlds. Submitto's explicit disclaimer ("collect files, not handle contracts") marks the seam from inside the Type.
- **vs CRM:** persistent speaker databases across events (some platforms) touch CRM territory, but the binding here is event-scoped presentation roles with a program assignment; CRM binds people to commercial relationships.
- **vs Event Mobile App:** the app consumes speaker records (bios, sessions) as content; the app is a publication surface, not the speaker system of record (consistent with the event-mobile-app pass, which listed speaker-management systems among the app's data sources).

### The "remove what" test

- Remove the speaker record and its coordination loop → only sessions with names remain: Event Agenda Management, not this Type.
- Keep profiles but remove the session/presentation assignment → a talent roster or contact list: not this Type.
- Keep records + assignments but remove the managed collection/coordination → a static speaker directory: a capability, not management.

## Historical / Market-Sample Check

- Pre-digital: program chairs collected bios and headshots by mail, kept lists of who speaks in which session, exchanged letters/phone calls with presenters, and printed speaker bios and photos in program books; printed speaker instruction packets served as the coordination artifact. All satisfy the L0 triple (record + assignment + coordination loop) without portals, submission software, or real-time sync. The modern sample adds self-service portals, automated comms, multi-surface sync — kept out of L0.
- Segment breadth: academic conferences (Fourwaves), associations and corporate events (Whova, Cvent), field-marketing/B2B conferences (Swoogo, Lineup Ninja), minimal collection-only deployments (Submitto). A single-keynote internal event and a 400-speaker multi-stage congress both fit the core. No era or segment overfit detected.
- The minimal pole (Submitto) deliberately lacks publication, review, agreements, and portals — and is still self-described speaker management software. This confirms the L0 is not over-fitted to the modern suite pattern.

## Uncertainties

- Organizer-side operational documentation (help-center articles) was not reachable for Cvent, Swoogo, and Whova; task/state vocabularies and exact portal mechanics are evidenced from product pages and API docs only. Assertions are calibrated to moderate strength.
- Submitto / OpenWater / MemberRun evidence rests on official-site content surfaced via search rather than full-page fetches; used as packaging/boundary anchors, not for precise workflow claims.
- Whether speaker-agreement/contract handling is rising toward standard could not be established — evidence is split (collected as tasks at Cvent/MemberRun/OpenWater; explicitly excluded at Submitto); left as variant.
- Travel/logistics depth (hotels, flights, travel preferences) is thinly evidenced (MemberRun snippet, Cvent questionnaires); depth varies and was left as variant.
- Speaker-side engagement tools (polls/Q&A management by speakers) documented at one product only (Whova); kept optional.
- The exact prevalence of persistent cross-event speaker databases (vs per-event records) could not be established from this sample; noted as a CRM-adjacent uncertainty.

## Final Synthesis

Speaker Management is the event's presentation-side people system: the organizing side holds a record for each person presenting at the event (speaker, panelist, moderator, chair), binds each record to the program units the person appears in, and runs a managed collection-and-coordination loop over that population — collecting and completing presentation-facing profiles and materials, assigning and tracking tasks and deadlines, and communicating with speakers about their participation, with speakers commonly participating through self-service links/portals. Mature products add dedicated speaker communications, custom questionnaires (A/V, dietary, accessibility), publication of speaker profiles to the event's surfaces (webpages, app, agenda) with one-place-updates syncing everywhere, multiple intake paths (manual, agenda auto-add, call-for-speakers, import), and role typing. The rest — submission/review pipelines, agreements, travel logistics, promotion machinery, speaker-side engagement tools, downstream distribution breadth — is segment- or product-dependent. The Type is realized both as suite modules/add-ons (the dominant packaging) and as standalone products (from full conference-content platforms to minimal collection tools); its nearest boundaries are Event Agenda Management (the program-centric sibling it interlocks with), Attendee Management (the participation-side roster), and Abstract Management (the intake pipeline that feeds it).
