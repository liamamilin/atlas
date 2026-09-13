# Research Notes — Theater Production Management

## Research Goal

Understand what software for "Theater Production Management" actually is, from real products: what the core objects are, who uses it, how production work flows through it, and where it separates from adjacent Types (Film/TV Production Management, Production Scheduling / Call Sheet, Performing Arts Organization Management, Venue Management, generic Project Management).

## Initial Boundary

Working hypothesis at start:

- Core use: coordinating the making and running of a theater production — rehearsals, performances, technical work, cast/crew coordination, stage-management paperwork.
- Nearest neighbors: Film Production Management, TV Production Management, Production Scheduling / Call Sheet Application, Script Breakdown, Casting Platform, Performing Arts Organization Management (ticketing/CRM side), Venue Management System, Project Management Application.
- Key risk: this leaf could collapse into "Film Production Management with different vocabulary." The seam needed explicit testing.
- Secondary risk: the word "callboard" collides with an unrelated consumer product (see Rejected Findings).

## Research Questions

1. What is the managed "unit" — the production, the season, the organization, or the event?
2. What objects exist inside a production: schedule events/calls, company members, roles, documents, reports, spaces?
3. How does the rehearsal → performance run lifecycle map into the software? What is a "call"?
4. How does information flow between managers and the company (the callboard function)? Is company-facing distribution definitional?
5. What machinery exists for conflicts, availability, attendance, reports?
6. How do budgets/labor/inventory appear (core, common, or modular)?
7. What separates this from film/TV production tools, and what separates it from the ticketing/CRM side of a performing arts organization?
8. Would a paper-era theater production office (physical callboard, prompt book, typed reports) satisfy the definition? (Historical check.)

## Representative Products

Selected for market representability + documentation completeness + different philosophies + different segments:

| Product | Pole | Segment | Status |
|---|---|---|---|
| VirtualCallboard (EmptySpace Technology) | company coordination / callboard / stage-management paperwork | theater & opera companies, education | Sampled, Layer A |
| Propared | production planning (schedule/team/resources/budget) for producing organizations | theater, opera, dance, festivals, universities, live events | Sampled, Layer A |
| Dramatify | full production suite — film/TV/broadcast (adjacent comparator for the boundary) | film, TV, broadcast, sports | Sampled, Layer A (adjacent Type) |
| CallBoard (callboard.app) | individual stagehand career tracking | individual workers | Sampled, REJECTED as representative (different Type) — kept as boundary evidence |
| Stage Write | stage-management documentation (Broadway-class) | professional theater | Target sample UNREACHABLE (see Sources) |

## Sources

- VirtualCallboard — homepage (virtualcallboard.com), Features page (virtualcallboard.com/features/), For Education page (virtualcallboard.com/for-education/). Fetched 2026-09-09. All Layer A.
- Propared — homepage (propared.com), Explore Scheduling page (propared.com/explore-scheduling/), extensive official training-video transcripts embedded on fetched pages (Contacts, Inventory, Mobile Companion, QR coding, Production Books, Reports, Team/Roles, Labor/Crew, Settings/Access, Timeline/Cloning). Fetched 2026-09-09. All Layer A.
- Dramatify — homepage (dramatify.com) incl. feature/workflow/role inventory. Fetched 2026-09-09. Layer A (adjacent comparator).
- CallBoard — homepage + Features page (callboard.app, /features). Fetched 2026-09-09. Layer A (rejected as representative).
- Stage Write — stagewriteapp.com returns only a JS-rendered shell ("Stage Write", no crawlable content; tried /features, /tour); stagewrite.zendesk.com help center closed; stagewriteapp.freshdesk.com 404; help.stagewriteapp.com returned a bare "Admin" shell; Wayback Machine attempts timed out ×2. **Source-access limitation:** the stage-management-documentation pole (blocking/cue-sheet tools) could not be verified through official documentation. Per evidence rules, no claims about specific such products are made anywhere in this research or the final document; the pole is acknowledged only as a hedged, unverifiable edge.

## Product A — VirtualCallboard

### Key observations (Layer A)

Self-description: "Total Theatre Management for Stage and Production Managers"; "Scheduling software for the performing arts"; "the ultimate online platform for managing theatrical productions"; web + mobile app.

Module inventory (Features page):

- **Announcements** — site-wide or targeted to specific productions; expiration dates so notices disappear when no longer relevant.
- **Notes and Email** — notes to individuals or groups; system "confirms receipt so you know your message reached everyone."
- **Discussions** — threaded, with file/image attachments, participation control per conversation.
- **File Sharing** — folders, access control over sensitive materials.
- **Scheduling Calls** — "Organize and publicize production and individual schedules while automatically detecting conflicts. The system prevents double-booking of people and spaces, allows crew members to self-sign up for open calls, and generates printer-friendly calendar views."
- **Track Attendance** — daily or per call; managers compute weekly hours; users see their own attendance ("when they've missed important calls or fittings").
- **Reports** — "unlimited custom report templates tailored to your different production types"; drafts; edits produce updated revisions that "automatically go out to all specified collaborators"; delivered to designated email addresses. (This is the rehearsal/performance report machinery of stage management.)
- **Contact Sheets** — generated/printed with per-user privacy over which contact details are shared; managers with permission can access private info.
- **External Contacts** — vendor/supplier directory organized by department.
- **User Management** — unique logins; user levels controlling module access; emergency contact and medical information stored for managers/administrators.
- **Multi-Production Management** — one account, many productions; "VirtualCallboard automatically silos information so users only see the calls, files, reports, and team members relevant to their specific production."
- **Archive** — admins can access data from deactivated productions ("historical records … secure and retrievable").

Education page adds: "the callboard, scheduling, and communication system built for educational theatre"; notifications by push/SMS/email "the moment you post them"; availability and conflict tracking; sign-in sheets; "living reports that show who did what"; parents/guardians added so they see schedules and get notifications; positioned to teach student stage managers.

Named user roles: stage managers, production managers; cast and crew as consumers.

## Product B — Propared

### Key observations (Layer A)

Self-description: "Production planning software for arts & events"; "Schedules, people, spaces, resources, and budgets in one shared place"; served verticals: Theatre & Performance, Opera & Dance, Education, Venues, Festivals, Corporate Events, Live Event Production, Digital Events. Scheduling-page framing: "Rehearsals shift, locations change, and people move between projects… Stop sending static PDFs and start managing dynamic schedules that update themselves."

Core objects (homepage + training transcripts):

- **Projects** — the production/show/event as a persistent container ("The Lion Queen"). Projects have teams, timelines, requirements, finance rollups. Project-level cloning from a source project using a **reference task** ("I'll use the Performance as the reference") — cloning re-anchors a copied schedule relative to a chosen event. **Template projects** hold reusable deadlines, schedules, locations, roles.
- **Timeline** — dated, time-bound events (Load-In, Performance, Rehearsal) with durations, locations, departments, categories; bulk edit, shift dates; "watch updates ripple across your team's views"; events link tasks, people, locations; day/week/month/year/list views; filters by department/show/venue/crew member. Rehearsal-tagged events feed a rehearsal schedule automatically.
- **Team** — contacts are People, Organizations, Locations; locations have nested **Spaces** (main stage, costume shop, storage). Project team carries **roles** and **groups** ("Cast," designers, production staff). Roles can be scheduled **before the person is known** ("you can establish a role before you know who will fill it… Lightboard Op… set up each character as a role and build a preliminary rehearsal schedule in advance"); cast grouping by scene ("Act 1, Scene 1" groups).
- **Labor / crew** — Positions with rates; labor cost rule sets (a default rule set with an overtime multiplier exists; exact multipliers are vendor defaults, not industry facts); **labor lines** attach crew needs to events (quantities, e.g., "four Electricians"); **crew bookings** fill slots by person; per-person call-time overrides; cross-project conflict and weekly-hours visibility ("42 hours this week… weekly overtime"); CSV export "for payroll systems or prefilled timesheets."
- **Inventory / Items** — items owned/rented/borrowed; departments (Props, Costumes, Lighting…) determine available types/keywords; sources with quantities; collections (saved bundles); QR-code labeling; photos; private vs public details. Items are **not project-specific** — "a cache of available objects you can use in your projects." A separate plan tier ("Inventory Foundations") exists — inventory is modular.
- **Requirements** — items pulled into projects ("a ladder and a projector" for a press event), with budget information; finance aggregates requirements + labor into a project budget rollup.
- **Reports** — rehearsal reports, performance reports, end-of-night reports, meeting minutes; created from an event in the timeline or the Notes & Reports screen; templates with general and departmental note sections; **tracked notes** with due dates that surface in shared pages; shared by URL "just like production books."
- **Production Books** — the distribution mechanism: "shareable webpages that display up-to-date information, tailored to exactly what someone needs to see. … no login required"; pages include Schedule, Notes/To-dos, Attachments, Locations, Team, Requirements, Inventory, Labor, Finance; per-viewer filters (self, department, location, recently changed); webcal subscribe ("embed the schedule as a read-only calendar in Google, Outlook, or Apple Calendars"); email distribution to groups (e.g., rehearsal book to the Cast group). Company calendar aggregates all projects; season built via cloning/templates ("I can build an entire season in about two days" — production manager, Alley Theatre; other testimonials from ACT, Oregon Shakespeare Festival, Battery Dance, Joffrey Ballet, etc.).
- **Access model** — Administrators (all projects), Project Managers (subset of projects — "perfect for stage managers or others brought on for a limited number of projects"), Inventory Managers, Field Users (mobile only). Distribution pages require no accounts: "Only editing users work in Propared, while everyone else stays connected through auto-updating webpages including staff, cast, crew, clients, designers, and vendors."

Named users: production managers, production coordinators, directors of production at theaters/opera/ballet/festivals/universities.

## Product C — Dramatify (adjacent comparator)

### Key observations (Layer A)

Self-description: film/TV/video/broadcast production platform ("The Powerful Toolbox for Film, TV, and Video Production"). Modules: management & budgeting, planning & scheduling (shooting scheduling, stripboards, semi-automatic call sheets, daily production schedules, DPRs), cast & crew management (team lists, food preferences, allergies, timesheets, contracts), screenplays (Final Draft/.fdx sync, script sides, watermarking), script breakdown, rundowns for multi-camera live/studio (cue cards, CuePilot, teleprompters), locations (maps, weather), sets/scene items/continuity, wardrobe/makeup/hair. Workflows: drama, entertainment, sports, talk shows, documentaries, children's programs, branded content, galas/live events.

**Negative findings (as important as positives):** nowhere in the fetched material is there rehearsal scheduling, a performance run, rehearsal/performance reports, season calendars, or company-facing "callboard" distribution in the theater sense; scheduling is scene/shoot-day-centric (script breakdown → stripboard → call sheet per shoot day). This product population plans **recorded-media capture**, not **live performance runs**.

## Product D — CallBoard, callboard.app (rejected sample)

### Key observations (Layer A)

"For stagehands, by stagehands." Features: call management tracking the individual's own gigs with start/end times, hourly/day rates, automatic earnings; skills/certifications by department with proficiency levels; expense tracking; public profiles; gamification; invite system. This is an **individual worker's career/work-log tool**, not a production-side management system — despite the "callboard" name. Rejected as representative; retained as a word-collision boundary finding.

## Cross-product Comparison

| Structure | VirtualCallboard | Propared | Dramatify | Assessment |
|---|---|---|---|---|
| Production/show as managed container | Yes (multi-production, siloed) | Yes (projects, seasons, cloning) | Yes (productions) | Cross-product common; theater-native pair make it the organizing unit |
| Company roster with production roles/departments | Yes (users, user levels, departments, contact sheets) | Yes (team, roles fillable pre-casting, groups) | Yes (cast & crew management) | Common across all; theater pair bind roster to production |
| Schedule of dated calls/events binding people+spaces | Yes (scheduling calls, conflict detection, space double-booking prevention) | Yes (timeline events, locations/spaces, ripples) | Yes but shoot-day/scene-centric | Common shape; content semantics differ by Type |
| Rehearsal + performance-run semantics | Yes (rehearsal schedules, per-call attendance, fittings) | Yes (rehearsal events, performances as schedule anchors, preliminary rehearsal schedules before casting) | Absent | Theater-native pair only → candidate for the Type's distinguishing content |
| Company-facing distribution without accounts | Yes (all team members access; read confirmations; printer-friendly calendars; push/SMS/email) | Yes (production books: no-login auto-updating pages, webcal, email to groups) | Crew app access exists (read-only free access) but call-sheet-centric | Common in theater pair; distribution target = whole company |
| Report cycle (rehearsal/performance reports with tracked follow-ups) | Yes (templates per production type, revision propagation, delivery) | Yes (rehearsal/performance/end-of-night reports, templates, tracked notes) | Daily production reports (DPRs) — shoot-oriented | Strong in theater pair; film analog exists but different semantics |
| Availability/conflicts | Yes (conflict detection; self-signup for open calls) | Yes (crew conflicts, weekly hours, cross-project) | Cast conflict handling in scheduling | Common |
| Attendance / sign-in / hours | Yes (per call/day, weekly hours) | Yes (attendance-adjacent; hours on labor lines; crew bookings) | Timesheets | Common in theater pair |
| Budgets / labor rates / overtime | Not documented | Yes (positions, rates, labor lines, finance rollup) | Yes (film budgeting, Movie Magic import) | Product-dependent → variant in this Type |
| Inventory / requirements / QR | Files only | Yes (modular plan) | Scene items/props/wardrobe modules | Variant |
| Season-level planning (templates, cloning, company calendar) | Partial (multi-production management) | Yes (season calendars, template projects, reference-task cloning) | Slate-level oversight for exec producers | Common-to-variant |
| Ticketing / box office / donors | Absent | Absent | Absent | Belongs to Performing Arts Organization Management, not here |

## Abstraction

### L0 — Defining Invariant

Four jointly-held structures; remove any one and the product is no longer a theater production management application:

1. **The production as the unit of record** — a persistent, identified show/production to which schedule, company, documents, and reports attach; held alongside other productions in one system (a season/slate); surviving to archive after closing. (1 alone = generic project container.)
2. **The company** — cast, crew, designers, stage management, production staff held as people records with production roles and departmental groupings, bound to the production; the system is two-sided: managers plan, the whole company is the audience. (2 alone = contact/CRM database.)
3. **The schedule of production calls** — dated, time-bound events (rehearsals, performances, load-ins/technical work, fittings, meetings) binding people and spaces, maintained through change, with the performance run as repeated scheduled performances of the show. (3 alone = calendar/scheduling tool.)
4. **Company-facing production communication (the callboard function)** — distribution of production information (announcements, notes, files, schedules, reports) to the whole company with low friction (read confirmations, no-login shared pages, notifications), plus company→manager feedback (availability/conflicts, sign-ups, report notes). (4 alone = message board.)

Joint-load-bearing checks: 1+2 without 3+4 = contact sheet for a show; 1+3 without 2+4 = venue/event calendar; 1+4 without 2+3 = announcement board; 2+3 without 1 = generic workforce scheduling; 1+2+3 without 4 = planner the company never sees; 1+2+4 without 3 = group chat for a show.

### L1 — Common Mature Structure

- Rehearsal/performance report machinery (templates, revision propagation, tracked follow-ups) — 2/2 theater-native sampled.
- Conflict handling and availability (double-booking guards over people and spaces; self-sign-up for open calls).
- Attendance / sign-in / hours tracking.
- Contact sheets with per-user privacy; emergency/medical information for managers.
- Archives of closed productions; multi-production information siloing.
- Notification fan-out (email/SMS/push) on posting.
- Season/portfolio calendar and reusable templates/cloning.
- Webcal/iCal feeds and print views for schedules.

### L2 — Variant / Optional Structure

- Budgets, labor rates, overtime rule sets, payroll exports (strong at one pole, absent at the other; modular plan at Propared).
- Inventory / requirements / QR-labeled items (modular; depends on whether the organization runs shops/stock).
- Education variant: parents/guardians as viewers, student stage managers, sign-in sheets framed for school programs.
- Union/crew-booking depth, per-person call-time overrides.
- Cross-media flexibility (festivals, corporate events, live events) — adjacent audiences served by the same structures.
- Deployment/form: cloud web+mobile is current-market dominant but not definitional (historical check).

### L3 — Vendor-specific (Research Notes only)

- Propared: Production Books as the named distribution construct; reference-task project cloning; magic-link login; labor cost rule sets with a documented default overtime multiplier (1.5× after 8h, optional double-time after 10h — vendor default, NOT an industry fact); QR-code address spreadsheets; "Inventory Foundations" plan tier; explicit no-AI positioning.
- VirtualCallboard: announcement expiration dates; notes with per-person read confirmation; demo site (demo.vcallboard.com); 30-day trial; educator discounts; free archive plan.
- Dramatify: CuePilot/SPX/AutoScript integrations; Movie Magic Budget import; watermarking; specific plan tiers.
- CallBoard.app: gamification tiers, invite credits (rejected sample).

## Vendor-specific Findings

See L3. Additionally: vendor self-labels vary — "Total Theatre Management," "production planning software for arts & events," "production management," "theatrical productions" — the market has no single name; the leaf name "Theater Production Management" describes the function and matches how VirtualCallboard and Propared describe their users' job (stage/production management) rather than any brand term.

## Boundary Findings

1. **vs Film Production Management / TV Production Management (§27 siblings) — keep both.** Shared family: production container, cast & crew records, schedules, breakdowns/paperwork, reports. The seam is the delivery unit: theater plans a **live performance run** (rehearsal process → repeated scheduled performances of a fixed show; rehearsal/performance reports; season calendars), while film/TV plans **capture** (script breakdown → scenes on shoot days → call sheets per shooting day; DPRs). Sampled evidence runs both directions: Dramatify (film/TV-native) contains no rehearsal/performance-run machinery; VirtualCallboard and Propared contain no stripboard/shoot-day machinery. Remove the performance-run/rehearsal semantics and substitute shoot semantics → Film/TV Production Management. Boundary issue recorded in STATUS.md.
2. **vs Production Scheduling / Call Sheet Application (§27 sibling)** — that leaf is the scheduling/call-sheet instrument (film tradition); this Type is the whole production-office system (schedule + company + communication + reports). The daily call schedule is one instrument inside this Type.
3. **vs Performing Arts Organization Management (§27 sibling)** — organization/audience/business side (ticketing, subscriptions, fundraising, marketing) vs making-and-running productions. All three sampled production-side products contain no ticketing/donor machinery; the production is the unit of record, not the audience relationship.
4. **vs Venue Management System (§26)** — venue/booking/rental as unit vs production as unit. Spaces appear here as schedulable resources bound to calls (double-booking prevention), not as bookable sellable inventory.
5. **vs Project Management Application (§03.07)** — same genus (projects, tasks, teams, calendars); the difference is production-native objects: calls, performances, the company with cast/crew/departments, reports tied to events, conflict guards over people and spaces. Generic PM tools are a real-world substitution pattern at the small-producer pole; the domain-specific structure is what the market builds dedicated tools for.
6. **vs Event Management Platform (§26)** — attendee-facing event logistics (registration, ticketing) vs company-facing production logistics. A performance is an event, but the managed population here is the company, not attendees.
7. **Word collision (recorded, no action):** "callboard" is used by an individual stagehand career tracker (callboard.app) for gig logging — production-side vs worker-side. Also adjacent-but-different categories: show control / cue playback tools (technical execution during performance) and prompt-book/blocking documentation apps (the unverifiable pole — see Sources limitation).
8. **Potential variant risk within the leaf:** education-focused deployments (VirtualCallboard for Education) change the audience (students, parents) but not the core structure — variant, not separate Type.

## Historical / Market-Sample Check

Paper-era theater production office: the physical callboard at the stage door carrying posted rehearsal schedules, performance calls, notices and contact sheets; the company roster; the stage manager's rehearsal and performance reports; sign-in sheets. This satisfies all four L0 structures with zero software — so cloud/mobile/no-login distribution/push notifications are implementations, not invariants. Regional and differently-positioned products (opera, dance, festival, university theater, corporate events served by the same product population) fit unchanged. Historical check **passed**.

## Uncertainties

- The stage-management-documentation pole (prompt book / blocking / cue sheets) could not be verified through official sources (Stage Write unreachable). Whether such tools belong inside this Type or at an adjacent edge is unresolved; the final document only hedges at this edge.
- Budget/labor machinery frequency across the wider market is unknown (one of two sampled products; modular plan tier) — held as variant, not common.
- Dramatify was sampled as the film/TV comparator; a dedicated theater-adjacent full-suite vendor with both shoot and run semantics in one product was not found in the reachable sample.
- Attendance/industry rule details (e.g., union rest rules) were not researched; no numeric claims made.

## Final Synthesis

A Theater Production Management application is the production office's system of record for making and running live performances. Its defining core: the production as a persistent managed unit; the company (cast, crew, designers, stage management) bound to it with production roles; the schedule of production calls (rehearsals, performances, technical work) binding people and spaces through change; and the callboard function that distributes production information to the whole company and carries availability/report feedback back. Around this core, mature products add the stage-management report cycle, conflict/attendance machinery, contact sheets, archives, season planning, and — depending on segment — budgets/labor and inventory/requirements. It is distinct from film/TV production management (capture vs live run), from performing arts organization management (production vs audience/business), from venue management (production vs bookable space inventory), and from generic project management (production-native objects and two-sided company audience).
