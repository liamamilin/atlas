# Research Notes — Race Management Platform

Research date: 2026-09-09
Directory leaf: Race Management Platform (§28 Sports, Fitness & Recreation)
Slug: race-management-platform

## Research Goal

Understand what a Race Management Platform actually is as an Application Type: what objects its world is built around (event, categories, participants, bibs, waves, results), who operates it (race director vs timer vs volunteers), how the event lifecycle flows (setup → registration → race day → results), which structures are definitional vs merely common in today's market, and where its boundaries sit against Race Timing System, Sports Registration Platform, generic Event Registration (§26), Endurance Training Platform, and League/Tournament Management.

## Initial Boundary

Working hypothesis at start:

- A Race Management Platform is **organizer-side** software for mass-participation racing events (running, triathlon, cycling, obstacle, swimming, nordic/biathlon, etc.): creating the race event with distances/categories, taking participant registrations, managing the roster (bib assignment, waves/corrals, packet pickup, check-in), integrating with timing, publishing results, and communicating with participants.
- Nearest directory neighbors:
  - **Race Timing System** (§28, line below this leaf) — chip timing hardware/software operated by timing companies
  - **Sports Registration Platform** (§28) — registration-first products for sport organizations
  - **Event Registration Platform / Event Management / Event Ticketing** (§26) — attendee-oriented events
  - **Endurance Training Platform** (§28, already processed) — athlete-side; its Related-Types table places this leaf as "organizer-side event operations"
  - **League Management / Tournament Management / Sports Meet Management** (§28 siblings) — season-long competition structures
- Prior pass note (endurance-training-platform, 2026-09-07): "Race Management Platform | organizer-side event operations; here events appear only as athlete-side targets the plan is built around" — this pass should ratify that seam from this side.

## Research Questions

1. What is the core object model — event, sub-event/distance/category, registration, participant, bib, wave/corral, result, timing data — and how do they relate?
2. What does the registration lifecycle look like with race-specific rules (pricing tiers, refunds/deferrals/transfers, teams/relays, waitlists, access codes, age gates)?
3. What race-day operations does the platform carry (packet pickup, check-in, onsite registration, bibs)?
4. How does timing data flow in, and how are results published (divisions, awards, live results, tracking)?
5. What event statuses / lifecycles exist on the organizer side?
6. What roles matter (race director, timer, volunteer, fundraising coordinator, participant)?
7. Where is the boundary against Race Timing System, Sports Registration Platform, Event Registration, and Ticketing?

## Representative Products

| Product | Geography / Segment | Why sampled |
|---|---|---|
| RunSignup | US, endurance-market leader | Market representation; rich product structure (registration + RaceDay suite); separate timer role |
| Race Roster | Canada/US, multi-sport | Deepest fetchable help documentation; explicit event/sub-event model; separate timer side |
| Zone4 | Canada, timing-anchored | Boundary pole: timing-first product that also does registration + results (tests the Race Timing System seam) |
| njuko | France/Europe, white-label | Regional + architectural pole: white-label, module-store registration platform (tests overfitting to the US all-in-one pattern) |

Rejected/avoided: ACTIVE Works (documentation URLs 404 in this environment); haku (root page returned empty — likely JS-rendered); products with marketing-heavy but documentation-light sites.

## Sources

### Fetched directly (Layer A unless noted)

- Race Roster Knowledge Base — https://help.raceroster.com/en-us/knowledge-base (category trees: Event Organizers and Race Directors; Timers) — fetched 2026-09-09
- Race Roster, "Understanding the different event statuses" — https://help.raceroster.com/en-us/knowledge-base/understanding-the-different-event-statuses — fetched 2026-09-09
- Race Roster, "How to create a sub-event" — https://help.raceroster.com/en-us/knowledge-base/how-to-create-a-sub-event — fetched 2026-09-09
- Race Roster product/positioning pages — https://www.raceroster.com/ (Products: Registration, Fundraising, Timing tools, CRM, Onsite, Virtual events; Solutions: Event organizers / Fundraising coordinators / Timers) — fetched 2026-09-09
- RunSignup homepage/positioning — https://runsignup.com/ (products, use cases, "A Technology Company for Endurance Events") — fetched 2026-09-09
- RunSignup RaceDay Real-Time product page — https://info.runsignup.com/products/raceday/ — fetched 2026-09-09
- RunSignup support portal root (Freshdesk) — https://help.runsignup.com/ and https://runsignup.com/How-To — fetched 2026-09-09 (home pages only; see limitation below)
- Zone4 product page — https://zone4.ca/about/products — fetched 2026-09-09
- Zone4 homepage/event calendar — https://zone4.ca/ — fetched 2026-09-09
- njuko homepage — https://www.njuko.com/ — fetched 2026-09-09

### Source-access limitations

- **RunSignup article-level docs**: the Freshdesk portal (help.runsignup.com / runsignup.com/support) served its home page, but all folder/article URLs attempted (/support/solutions, /support/solutions/17000080448, /support/solutions/articles/…) returned 404 or transport errors. Article-level operational detail for RunSignup is therefore **not verified**; assertions about RunSignup rest on its public product/positioning pages (Tier 2) and are calibrated accordingly. Per evidence rules, no article-level RunSignup claims (e.g., exact deferral mechanics) are stated in the final document.
- **njuko**: only marketing/positioning pages fetched; article-level documentation not reached. njuko-specific capabilities are kept weak ("positions itself as…") in the final document.
- **haku / ACTIVE Works**: not sampled (fetch failures). Recorded as sample gaps, not used for any claim.
- Vendor "by the numbers" claims (e.g., RunSignup's "30,000+ Events", "10 Million Annual Registrants") are marketing figures and are not used as evidence for any structural claim.

---

## Product A — Race Roster (deep documentation, Canada/US multi-sport)

### Key observations (all Layer A unless noted)

**Event model:**
- The **event** ("event page") is the container, identified by a unique 5–6-digit **EID**, with its own settings, data and reports on an event dashboard.
- The **sub-event** is "a category of registration for the event" — "the building block of participant data". Examples given by the vendor: a 10-mile bike ride (one free sub-event); a charity 5K (three sub-events: General Public / Veteran discounted / Fundraiser charge-later); a multi-sport race festival (seven sub-events: Sprint Tri, Olympic Tri, Team Relay Sprint, Team Relay Olympic, Duathlon, Aquabike, Aquathlon).
- Per-sub-event configuration: products, registration questions, team categories, **start groups**, fundraising permissions, waivers, discounts; per-sub-event: name (recommended format "sport + distance"), type (for indexing in the public event search), distance, custom date (multi-date events), tax, age min/max.
- Sub-events can be grouped, bundled ("challenge/bundle sub-event" — register for multiple at once), and one sub-event is **required** before registrations can complete ("Creating sub-events is one of the seven required steps to take an event page live").

**Event lifecycle (statuses):**
- Draft → Demo → Private → Live, plus Paused. Draft = staff-only, test registrations; Demo = second testing phase, entry code, "Test Registration" button; Private = accessible by direct URL only, not searchable/indexed, payments processed; Live = public, subject to registration opening date/time, requires all seven required settings complete; Paused = blocks registration (e.g., weather), only from Live/Private.
- Once Live, an event cannot return to Draft/Demo (can only go Private/Paused).

**Sub-event eligibility & restriction machinery (competition semantics):**
- Age settings: min/max age with date-of-birth validation; non-qualifying registrants get a blocking message (vendor example: "1 Mile Kids Fun Run" ages 5–15; Full Marathon 17+).
- Access codes to lock sub-events from the public; participant-country restriction; **validation lists** (only people on an uploaded list may register — vendor examples: pre-approved elite runners, employees, club members) with start/end dates (e.g., club-member early window before public opens).

**Registration & pricing:**
- Pricing modes: **block pricing** (price increases over time), **scheduled pricing**, **fixed pricing**, additional charges; promo/discount codes (incl. age discounts, 2-for-1/family, team categories, organizational promo codes, pay-later/invoicing registration codes for groups).
- Participant limits on events; alternate close dates for teams; gifting; refund protection program add-on.

**Participant management (organizer-side):**
- Manual add, edit, participant search, export; make participant anonymous; set which fields participants may self-edit.
- Lifecycle operations: **defer** (+ participants "claim deferral"), **transfer** (incl. automated online transfers, transfer to another event), **full or partial refund**, make inactive (cancel without refund), turn a registration into a donation.
- Participant list fields include distance-travelled and public-facing participant display customization.

**Onsite (race-week/race-day):**
- Onsite App for packet pick-up check-in: QR-code scanning, barcode scanners, quick check-in, check-in modal customization, waiver signature at check-in, onsite registration with onsite pricing, Stripe payment pads, staff/volunteer logins, kiosk bib assignment.

**Timer side (separate role):**
- Separate **Timer Dashboard** with its own permissions; "timing crew vs timing company" distinction.
- **Bib assignment**: automatic at registration, batch tool, CSV upload, dynamic at bib pickup, alphanumeric bibs, bib restrictions, per-participant bib edit, bibs for challenge/bundle sub-events, results-QR-on-bib best practices.
- **Results**: manual upload, import from **RunScore**, integrations with **RACE RESULT**, Agee Timing, RM Timing; posting results for events not using Race Roster registration (results-only service); unofficial-results expiry; custom columns; event progress dashboard; finisher videos; finisher certificates.
- **Awards**: create and assign awards; awards based on registration questions or custom values; duplicate races and awards across events; custom genders in results/awards data.
- **Predictive tracking** using estimated finish times (spectator "follow runner" pages); SMS text credits; photo galleries with participant uploads and collaborators.

**Broader suite (common-mature context):**
- Teams: categories, relay teams with min/max participants, team discounts, team leaders, mandatory teams, team close dates.
- Fundraising: participant fundraising, charity partners (via Grassrootz), leaderboards, achievements/badges.
- Volunteers: signup on the registration page, manual add, station assignment.
- Email campaigns (two types, merge tags, abandoned-registration campaigns), Mailchimp sync, marketing pixels/tracking links, digital engagement kits.
- Products/merch (participant store, bundles, tax), financials (payment profiles, payouts/remittance reports, disputes/chargebacks, tax reports, marketplace vs non-marketplace tax regions), CRM (organizations, validation lists, event groups).
- Virtual: Virtual Event Toolkit, virtual challenges, audio cues, splits/segments.
- Series pages, club/membership pages associable with events; USAT integration; bilingual pages; event schedule; sponsors; bib verification tab.

## Product B — RunSignup (US endurance leader)

### Key observations (Tier 2 positioning/product pages; article-level docs not reachable — see limitation)

**Positioning:** "Power your race from registration through RaceDay with RunSignup's expertly crafted, all-in-one platform for endurance events." Footer: "A Technology Company for Endurance Events." Setup via a "race wizard"; every race gets a free race website, email platform, fundraising, marketing tools, and RaceDay CheckIn App.

**Event types listed:** runs/races, walks, ultramarathons, triathlons, cycling, swim events, turkey trots, kids events, virtual & hybrid, trail races, corporate team events, paddle, ski & snowshoe, gravel grinders, obstacle course races, stair climbs.

**Products:** Event Registration; Memberships (running clubs); RaceDay Real-Time (suite); Email; Websites; Race Marketing; Fundraising; Ticket Events (separate **TicketSignup** product/portal). Use cases split across **Race Directors**, **Timers**, Fundraising Events, clubs, stores — race director and timer are distinct operator personas with separate use-case pages, certifications ("RaceDay Real-Time Certifications") and a Partner Program.

**RaceDay Real-Time suite (race-day operations layer):**
- **RaceDay CheckIn** (app): "Check-in participants in seconds through a QR code scan or intuitive search"; volunteer access limits; participants and volunteers in one app; real-time sync of participant lists and bib assignments.
- **RaceDay Scoring**: "Compatible with all major chip systems, including MYLAPS, Chronotrack, RFID, Race Result, and more"; two-way sync with RunSignup participant data; offline scoring with local changes; real-time scoring dashboard.
- **RaceDay Bibs**: "Set bibs to assign automatically at registration, in bulk after registration, or dynamically at bib pickup"; bib-number emails or QR codes; real-time sync across timing, scoring, check-in.
- **RaceDay Corrals**: corral/wave management; assign automatically by estimated finish time at registration, assign later, or CSV upload; estimation tools.
- **RaceDay Results**: publish results "via a variety of sources, including a direct upload from RaceDay Scoring, a CSV upload, a Dropbox upload, or a preformatted upload"; searchable results filterable by division; display customization (hide age/city); leaderboards and kiosks; results notifications via email and text; virtual results platform; weather conditions on results pages.
- **RaceDay Registration**: onsite registration on dedicated devices; online registration open "until the gun goes off"; QR-code signage for self-service mobile registration.
- **RaceDay Mobile**: backup timing (finish-line/split capture with offline sync), automated photo capture, announcer mode (live participant data stream).
- **RaceJoy**: real-time tracking — chip-timed progress alerts and continuous GPS phone tracking; spectator cheers; SOS/off-course alerts; safety monitoring.
- **RaceDay Photos**: albums, auto-tagging (Tagily), tagged photos on results/team pages, participant uploads.

**Boundary datum (vendor-level):** RunSignup operates **RunSignup** (races) and **TicketSignup** (ticketed events) as separate platforms/products — the vendor itself separates participant-race registration from ticket-event admission. Also separates Membership product (clubs) from registration.

## Product C — Zone4 (Canada, timing-anchored pole)

### Key observations

- Positioning: "Simplify your timing and online registration… Race Timing & Registration Systems." Slogan: "Every Second Counts" — accuracy first (1/1000th second).
- Products: **GoChip** timing chips (neoprene band); **Timing Software** ("Support for many sports and race formats; Live results, photos, racer tracking; Customizable results and Racer Pages; Commentator system and TV results"); **Broadcast Software** (auto-follow race action, camera mixing for YouTube Live, OBS/vMix compatible); **RapidCam** line-scan photo-finish camera; **Summit Timers** (FIS-homologated wireless timer); **Online Registration** ("Customizable Registration Forms — flexible form editor; unlimited custom or preset fields; Custom Reports, Quick Summaries, and built-in communication tools"); **Race Timing Services** (hire on-site/remote timing crews).
- Sports served: cross-country skiing, alpine, triathlon, running, enduro MTB, snowboard, biathlon, motorsport.
- Live calendar shows club-scale regional events (enduro, cyclocross, nordic, biathlon, half marathons, club memberships and NCCP coaching workshops) — the same platform registers memberships/clinics and races; event pages mix races and club programs.

**Reading:** Zone4 is one platform spanning registration + timing + results, anchored in the timing stack. It demonstrates (a) the seam with Race Timing System (the timing stack is its center of gravity), and (b) that registration-side structures (forms, reports, communication) also appear in timing-first products serving the same race-event world.

## Product D — njuko (France/Europe, white-label pole)

### Key observations (marketing-level evidence only — weak claims)

- Since 2012; team "from Ex-Race Directors, Chip timers and product developers".
- Three stated values: **white-label experience** (registration link/domain stays under the organizer's brand); **no data ownership or use by the platform** ("The data collected is YOUR data"); **your own payment gateway** (organizer controls cash flow, refunds, supplier payments).
- Four stated differentiators: **adaptive registration workflows** (per-participant workflows); **participant's dashboard** (single screen: social feeds, optional training plan, course map, shop); **module store** ("the first registration 'app store' with hundreds of modules… you only pay for what you choose"); expert services/marketplace.
- Per-event, per-distance ("or more") personalization of the registration experience; pricing "from €0.20 per registration"; multi-currency.
- Sport imagery/scope: running, marathon, triathlon, half-marathon, biathlon, kids race, colour run, ultra trail, obstacle race, team sports, swimming, cycling, bike & run, hiking, dog race, ski, canoe kayak, paddle, motor sports, roller.
- Hero imagery references bibs (dossard); a "Sport Ticketing" link exists in the footer (not explored).

**Reading:** njuko evidences a white-label, API/module-oriented registration-architecture pole of the same Type, with competition-oriented personalization (per-distance workflows), and a different data/ownership philosophy from the US platforms. Article-level capabilities (results, timing integrations) were not reachable — njuko's exact coverage of the results leg is **unverified**; this is recorded in Uncertainties.

---

## Cross-product Comparison

| Dimension | Race Roster | RunSignup | Zone4 | njuko |
|---|---|---|---|---|
| Race event as unit of record | Event page (EID) | Race/event + free website | Event pages in calendar | Event ("CREATE AN EVENT") |
| Categories/distances | Sub-events (explicit, per-sub-event config) | Distances/race options (wizard); bundles/corral config per distance | Race formats per sport | Per-event, per-distance personalization (weak claim) |
| Registration forms | Custom questions, validation, hidden fields, waivers | "Mobile friendly registration pathway" | Flexible form editor, custom/preset fields | Adaptive workflows (weak claim) |
| Eligibility gates | Age min/max with DOB blocking; access codes; validation lists; country restriction | Present (article-level unverified) | Not detailed on fetched pages | Not verified |
| Bibs | Auto/batch/CSV/dynamic-at-pickup; alphanumeric; restrictions | Auto/bulk/dynamic at pickup; bib emails/QR | Chip-based bib identification (GoChip) | Bib imagery (weak) |
| Start organization | Start Groups (per sub-event) | Corrals (auto by est. finish time / later / CSV) | Not detailed on fetched pages | Not verified |
| Timing relationship | Timer role + dashboard; RunScore/RACE RESULT/Agee/RM integrations; results-only posting | RaceDay Scoring "compatible with all major chip systems (MYLAPS, ChronoTrack, RFID, Race Result)"; two-way sync; offline | Own timing stack (chips, photo-finish, FIS timer) + timing services | Timing via partners (unverified) |
| Results | Upload/manual/RunScore import; unofficial results expiry; awards by division/question/custom; predictive tracking; finisher videos/certificates | RaceDay Results (multi-source upload, division filter, leaderboards/kiosks, notifications, virtual results) | Live results, racer pages, TV/commentator output | Unverified |
| Race-day onsite | Onsite App (check-in, QR, onsite registration/pricing, waiver capture) | RaceDay CheckIn app + onsite registration + RaceDay Mobile | On-site timing crews | Not verified |
| Teams/relays | Team categories, relay min/max, team discounts | Team events (use case) | Club/team context in calendar | Not verified |
| Fundraising | Deep (charity partners, leaderboards, badges) | Deep (P2P fundraising product) | Not observed | Not verified |
| Participants self-service | Transfer/defer/claim/edit | "Flexible participant management with admin and self-serve options" (weak) | Not detailed | Participant dashboard (weak) |
| Event lifecycle statuses | Draft/Demo/Private/Live/Paused (explicit) | Not article-verified | Not detailed | Not verified |
| Multi-event / organizations | Organizations, event groups, series pages, CRM | Memberships/clubs; Partner Program for multi-event timers | Club pages/memberships | Resellers/partners |
| Virtual events | Virtual toolkit, challenges, audio cues | Virtual & hybrid use case; virtual results platform | Not observed | Not verified |
| White-label / data posture | Platform-branded | Platform-branded ("customized for your brand" websites) | Platform-branded | White-label core value |
| Payment rails | Platform payment profiles (Stripe), marketplace vs non-marketplace tax | Platform processing (PCI L1 claim) | Platform | Organizer's own gateway |

**Cross-product commonalities (Layer B):** every sampled product organizes its world around a **race event with categories/distances and participant registrations**; every product that documents race-day mechanics has **participant identity on course** (bib/chip) and **start organization** (waves/groups/corrals or age-group categories); every product that documents outcomes publishes **results against the roster** (own stack, imports, or integrations); a **timer/timing-partner role** is structurally distinct from the organizer in the three products that document roles deeply (Race Roster, RunSignup; Zone4 IS the timer).

**Vendor-specific (Layer D examples):** Race Roster EID/Smart Links/Grassrootz/ASICS Runkeeper; RunSignup RaceDay suite names, RaceJoy, Tagily/RaceInsights, separate TicketSignup; Zone4 GoChip/RapidCam/Summit/Commentator/Broadcast; njuko module store, white-label values.

---

## Abstraction Hierarchy

### L0 — Defining Invariant (candidate)

A Race Management Platform is recognizable as such only if all four hold:

1. **The race event as the unit of record** — a persistent, organizer-created event with a date and one or more race categories/distances, presented on a public (or access-controlled) event page. Remove → event directory / calendar listing.
2. **A participant roster built through registration** — each registration creates a participant record tied to one category, carrying race-relevant attributes (identity, DOB/age, gender/division data, emergency contact, waiver, optional team). The participant is a **competitor**, not an attendee or ticket-holder. Remove → generic registration/form platform.
3. **Competition-structuring machinery on the roster** — the roster is organized for a competition: eligibility/division classification (age/gender/category gates) and start organization (waves/start groups/corrals) with participant identity for the course (bib/chip as the classic implementation). Remove → attendee registration; the platform stops being race software.
4. **The results of record** — the platform holds or publishes the competitive outcome (finisher results) against the same roster, fed by its own timing/scoring layer, imports (CSV/RunScore-class), or timing-partner integrations; searchable and division-filterable. Remove → registration-only product (Sports Registration Platform territory) or timing-only product (Race Timing System territory).

Jointly-held load-bearing checks:
- 1 alone = event listing/directory
- 2 without 1 = form/registration engine
- 1+2 without 3+4 = Sports Registration Platform (registration-only for sport orgs)
- 3 without 1+2 = timing/scoring tools operating on imported rosters (Race Timing System)
- 4 without 1+2+3 = results-posting service
- 1+2+3 without 4 = registration + race-day logistics without the competitive outcome — arguably still short of "race management" (see Uncertainties: njuko's results coverage unverified; the market contains registration-strong products whose results leg runs through partners)

### L1 — Common Mature Structure (common in the sample, not definitional)

- Public searchable event pages / event directory
- Custom registration questions, waivers, validation
- Pricing machinery: tiered/block pricing, promo codes, fee handling, participant limits
- Participant self-service: transfer, defer/claim, edit, refunds
- Onsite check-in app (packet pickup, QR scanning) and onsite registration
- Teams/relays; volunteers; merchandise/add-ons
- Fundraising/donations (charity-partnered races)
- Email campaigns/participant communication; participant dashboards
- Live/predictive tracking, photos, digital medals/certificates
- Multi-event/series/organization management; CRM; financial reporting (payouts, tax, disputes)
- Virtual events
- Multi-language/regional tax handling

### L2 — Variant / Optional Structure

- **Product shape**: all-in-one suite (RunSignup, Race Roster) vs timing-anchored (Zone4) vs white-label modular (njuko) vs registration-marketplace
- **Regional/legal posture**: marketplace vs non-marketplace tax; fee-transparency/fee-passing legality (AU/NZ restrictions documented by Race Roster); data ownership (njuko's organizer-owned data stance)
- **Timing integration depth**: own scoring stack vs third-party integrations vs partner-mediated (unverified for some vendors)
- **Scale/customer**: club-scale regional races (Zone4 calendar) vs city marathons vs charity 5Ks vs series
- **Sport lens**: run-first vs multi-sport vs cycling/nordic/biathlon
- **Virtual/hybrid** as a first-class mode vs not offered

### L3 — Vendor-specific

RunSignup's RaceDay/RaceJoy/Tagily branding, certifications, Partner Program thresholds; Race Roster's EID, Smart Links, Grassrootz, timed "Paused freezes payouts" mechanics; Zone4's GoChip/RapidCam/Summit hardware lines and FIS homologation; njuko's module-store pricing. These stay in Research Notes.

---

## Historical / Market-Sample Check

- **Paper-era lineage**: a race organized with paper entry forms, a typed entry list (roster), race numbers with safety pins, start waves by expected time, age-group classes, and hand-computed/posted results satisfies all four L0 legs with no software. The digital platform automates this structure; it does not define it.
- **Regional check**: Zone4's club-scale nordic/biathlon/enduro calendar (Canada), njuko's European multi-sport scope, and US road-race platforms all fit the four legs without US-specific machinery (US tax forms, fee-transparency laws are L2 variants).
- **Platform-era check**: older regional platforms (e.g., registration-plus-results portals for ultramarathons) and timing-company products with registration bolted on also fit; products that never touch the roster-competition-results structure (pure membership systems, pure fundraising platforms) do not.
- **Anti-overfit**: no single vendor's suite structure is definitional — e.g., RunSignup's RaceDay suite names, Race Roster's sub-event terminology ("sub-event" is Race Roster's label; RunSignup says "distances", Zone4 says "race formats") — the canonical concept is **race category/distance under one event**, realized with different vocabularies.

## Vendor-specific Findings

- Race Roster: EID identifiers; "seven required steps/settings" gate before Live; Paused freezes payouts; two email campaign types; validation lists with start/end windows; Grassrootz charity backend; results-only posting for events not using Race Roster registration.
- RunSignup: separate TicketSignup platform for ticketed events; RaceDay Scoring's explicit chip-system compatibility list (MYLAPS, ChronoTrack, RFID, Race Result); RaceJoy certified-timer model; free-tier structure ("Get Started for Free"); RaceDay Mobile backup timing with offline sync.
- Zone4: FIS-homologated timer; commentator/TV output; broadcast software with OBS/vMix; timing services (staffed timing as a service).
- njuko: white-label domain/brand retention; organizer-owned payment gateway; module store with per-module pricing; "no data ownership or use" stance.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (with removal test) |
|---|---|---|
| **Race Timing System** (§28, adjacent leaf) | deepest operational seam | Timing systems center the **timing stack** (chips, decoders, photo-finish, scoring software) operated by/for timing companies, importing rosters; race platforms center the **organizer's event operations** and consume timing output. Remove the roster/registration/event operations → Race Timing System; remove the timing stack → race platform. Zone4 straddles (registration + timing + results) — center-of-gravity call. RunSignup's RaceDay Scoring is a scoring layer *over* third-party chip systems, not a chip/hardware system. |
| **Sports Registration Platform** (§28) | registration-only sibling | Serves sport organizations' registration needs (leagues, camps, clubs) without competition-structuring or results machinery. Add divisions/waves/bibs/results → race platform; strip them → sports registration. |
| **Event Registration Platform / Event Management Platform** (§26) | attendee-side neighbor | Attendees, ticketing/admission semantics, agenda/session management; participants are not competitors and results do not exist. RunSignup itself splits TicketSignup from RunSignup — vendor-level confirmation of the participant-vs-attendee seam. |
| **Event Ticketing Platform** (§26) | admission vs participation | Ticket inventory/admission vs roster with competition semantics and course identity. |
| **Endurance Training Platform** (§28, processed) | opposite side of the same event | Athlete-side plan/execution system of record; events appear as targets. This leaf is organizer-side event operations. Ratifies the endurance pass's placement. |
| **League Management / Tournament Management / Sports Meet Management** (§28 siblings) | different competition container | Season-long leagues, bracketed tournaments, multi-team meets with schedules/standings vs single mass-participation timed events with individual finishers. |
| **Fundraising platforms / Nonprofit event management** (§25) | bundled capability | Charity runs bundle fundraising; fundraising-first products without race machinery are a different Type. |

## Uncertainties

1. **njuko's results/timing leg** is unverified (article docs unreachable). If njuko truly ships no results pathway, it would sit at the L0 boundary (registration + competition semantics without results-of-record) — the "1+2+3 without 4" load-bearing case. The synthesis treats the results leg as definitional but flags this single-sample uncertainty.
2. **RunSignup article-level mechanics** (deferral windows, transfer rules, exact statuses) unverified due to Freshdesk 404s; kept out of the final document.
3. **Waitlisting** observed indirectly (participant limits; "reserve the final few spots" validation example) but not as a named first-class object in fetched sources — recorded as likely-common, unverified-as-structural.
4. **haku / ACTIVE Works / ChronoTrack / MyLaps / UltraSignup** not sampled (fetch failures / out of budget); enterprise and pure-timing poles are under-sampled relative to their market weight.
5. **Race-specific qualification semantics** (e.g., qualifying-time validation for marathons) — validation lists plausibly support this but no direct source was fetched; recorded as unverified.

## Final Synthesis

A Race Management Platform is the **organizer-side system of record for a race event**. Its world has four load-bearing structures: the **race event** (a dated event with one or more race categories/distances, presented on a public or access-controlled event page); the **participant roster** built through registration (competitor records carrying identity, age/division data, waivers, teams); **competition-structuring machinery** (eligibility gates, division classification, start organization, and participant course identity such as bibs/chips); and the **results of record** (finisher results held or published against the same roster, fed by an own or integrated timing layer). Around this core, mature products add the registration commerce layer (tiered pricing, promo codes, refunds/deferrals/transfers), race-day operations (packet pickup check-in, onsite registration, volunteer tools), communication (email campaigns, participant dashboards, tracking), and the growth/fundraising layer (charity partnerships, merch, marketing). The market realizes one Type in several shapes: all-in-one suites, timing-anchored platforms, white-label modular platforms, and registration-marketplace portals — with the timer as a structurally distinct operator role. Boundaries: strip the competition/results machinery and it is a Sports/Event Registration Platform; strip the organizer-side operations and it is a Race Timing System; make participants attendees and it is Event Registration/Ticketing (§26).
