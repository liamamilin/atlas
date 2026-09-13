# Research Notes — Production Scheduling / Call Sheet Application

Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

## Research Goal

Understand what a Production Scheduling / Call Sheet Application is as an Application Type: what objects exist inside it, how a film/TV shoot gets planned day by day, how the daily call sheet is produced and distributed, what rules constrain the work, and where the Type's boundaries sit against neighboring Types (Script Breakdown, Film/TV Production Management, generic Project Management, Employee Scheduling, Event Management).

## Initial Boundary

The leaf sits in DIRECTORY §27 (Media, Entertainment, Creator & Culture), adjacent to Film Production Management, TV Production Management, Production Accounting Platform, and Script Breakdown Application.

Initial hypothesis (to be tested, not asserted):

- Core purpose: turn a script into a shooting schedule (scenes grouped into shooting days) and produce the daily call sheet that tells cast and crew when/where/what.
- Primary users: 1st Assistant Director (schedule), Production Manager / Line Producer (oversight), Production Coordinator (call sheets, distribution).
- Nearest neighbors: Script Breakdown (upstream input), Film/TV Production Management (broader suite), Project Management (generic), Employee Scheduling (shift-based workforce), Event Management (sessions/attendees).
- Open question: is the call sheet definitional, or only common? Movie Magic Scheduling is reputed to lack call-sheet tooling while remaining the scheduling standard — if true, the Type's center must be the schedule→call-sheet chain, not either artifact alone.

## Research Questions

1. What is the core object model? (production/project, scene, breakdown elements, shooting day, stripboard/schedule, call sheet, recipients, reports)
2. How does the script become a schedule? (import, breakdown tagging, stripboard, day breaks)
3. What does a shooting day contain? (ordered scenes, banners, company moves, call/wrap, unit, location)
4. What does a call sheet contain, and how is it produced and distributed? (sections, personal call times, weather/maps/safety, email/SMS/PDF, tracking, confirmations, revisions)
5. What derived documents exist? (DOOD, one-liner, breakdown sheets, sides, production reports)
6. What rules/constraints matter? (page counts, time estimates, cast availability, turnarounds, company moves, versions)
7. What interfaces exist? (stripboard, calendar, call sheet editor, distribution dashboard, mobile recipient view)
8. How do products differ? (desktop vs cloud, schedule-first vs call-sheet-first, suite vs point tool, AI-native)

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Shape | Tier / market | Why sampled |
|---|---|---|---|
| Movie Magic Scheduling (Entertainment Partners) | Desktop, offline scheduling + breakdown | Legacy industry standard, studios | The schedule-centric pole; the data standard others import/export |
| StudioBinder | Cloud all-in-one (write→breakdown→schedule→call sheets) | Indie → mid-market → enterprise brands | Strongest public documentation of the full chain |
| SetHero | Cloud, call-sheet-first point tool | Commercials / episodic / indie | The call-sheet-centric pole; distribution/tracking depth |
| Yamdu | Cloud production management suite | European broadcasters/streamers | Regional suite pole; schedule import from MMS; DOODs; security posture |
| Filmustage | Cloud, AI-native pre-production | Indie → studios | AI breakdown/scheduling pole; conflict detection; multi-unit |

## Sources

Fetched 2026-09-09 (Layer A unless noted):

- SetHero — https://sethero.com/ (root), https://sethero.com/call-sheets/ (feature page), https://help.sethero.com/en/ (help center structure)
- StudioBinder — https://www.studiobinder.com/ (root), https://www.studiobinder.com/film-scheduling-software/, https://www.studiobinder.com/call-sheet-builder/, https://www.studiobinder.com/movie-magic-scheduling-software-vs-studiobinder/ (competitor comparison — Tier 3 for MMS claims)
- Yamdu — https://www.yamdu.com/en/ (root)
- Filmustage — https://filmustage.com/ (root), https://filmustage.com/shooting-schedules/
- Entertainment Partners — https://www.entertainmentpartners.com/ and /movie-magic-scheduling/ and /products/movie-magic-scheduling/ all failed (empty response / 404 ×2). Per source-access limitation, EP official documentation was NOT reachable. MMS structural claims below are sourced from StudioBinder's comparison page (Tier 3, competitor marketing) and corroborated structurally by three vendors' integration pages (SetHero MMS exporter, Yamdu MMS schedule import, Filmustage MMS integration). Marketing-flavored MMS claims (price, update cadence) are recorded but NOT promoted into the final document.

## Product Observations

### Movie Magic Scheduling (Entertainment Partners) — evidence layer: B/C (competitor-sourced + integration corroboration)

- Desktop scheduling and breakdown software; generates production documents (per StudioBinder comparison page).
- Offline / no cloud access; versioned PDFs generated and manually distributed (competitor claim).
- Stripboard shooting schedule builder; banners & day breaks; estimated times; auto-reordering; boneyard; reports incl. DOOD (competitor feature table).
- No call sheet builder, no contact management, no shot list/storyboard, limited calendar (competitor claims — treat as Tier 3).
- Corroboration of its role as the scheduling data standard: SetHero ships a "Movie Magic Scheduling to Excel" exporter (own help-center collection); Yamdu lists "Movie Magic — import your schedule"; Filmustage lists Movie Magic among integrations. Three independent vendors build bridges INTO/OUT OF MMS data — strong Layer B evidence that MMS is the schedule-of-record format many productions start from.
- Still widely used by studios (competitor claim; consistent with three vendors building import/export bridges).

### StudioBinder — evidence layer: A

- Full pipeline: Write → Breakdown → Visualize → Plan → Shoot. Scheduling page: "Stripboards, stacked in your favor."
- Script import: Final Draft, PDF, Fountain, TXT → "Every scene is automatically added to your stripboard."
- Stripboard mechanics: scene strips; drag-and-drop or auto-schedule by scene criteria; auto group/reorder by setting, day/night, INT./EXT.; day breaks inserted based on page count or estimated shoot time; banners for meal breaks, company moves, estimated shoot time, production notes; toggle scene details (cast, shoot location, page count, script day, elements, prep, shoot time); boneyard (omitted scenes removed and returned); duplicate schedule to compare variations; search strips; scene notes; PDF/CSV export.
- Call sheets: "Generate call sheets directly from your stripboard, automatically populated with cast, shoot locations and map links, company details, contacts, live weather, banners, and schedule details — so nothing has to be entered twice."
- Call sheet builder page: call sheet types (shoot day, scout, rehearsal); auto-populated weather, locations, parking notes, map links, schedules, contact info; customizable sections (show/hide/rearrange bulletins, department notes, atmos); templates; private notes per recipient; delivery via SMS + email; tracking dashboard (sent / viewed / confirmed / undeliverable); reminder emails; features list: parking details, hospital information, weather auto-updates, daily agenda (call times for cast, crew, meal breaks, wrap), Google Maps, schedule modification (scenes, banners, company moves), PDF page breaks, footer notes (walkie channels), attachments (shot lists, storyboards, sides), atmosphere & location prep (extras tally, holding areas), department notes, advanced schedule (next day), department layout, 12/24h clock, °F/°C.
- Reports from stripboard: shooting schedules, one-liner schedules, DOOD reports, breakdown sheets, daily sides.
- Collaboration: share schedule via link, invite collaborators to edit, comments, assign scheduling tasks.
- MMS comparison page (Tier 3 for MMS): positions MMS as desktop/offline/manual-entry; StudioBinder as cloud/collaborative; claims MMS lacks call sheet builder.

### SetHero — evidence layer: A

- Positioning: "Digital Call Sheets & Film Production Management"; "Damn good call sheets in 20 minutes"; "#1 call sheet software trusted by professional film producers and ADs."
- Call sheet builder: drag-and-drop editor; customizable sections (choose sections, drag order, add own sections); live preview; PDF/Excel export; single or multi-page with custom page breaks; printer-friendly; watermarking for drafts.
- Smart Assist (AI): automatic weather forecasts, overtime calculations, time typo detection.
- Call sheet sections: scheduling (day's shooting schedule + advance schedule for next shooting day); cast (pickup, arrival, makeup, blocking times); extras and stand-ins (own section, headcounts, call/wrap times); personal call times per person; precalls to entire departments with one click; cascading time changes (change main call time → cascades to other times); automatic map links for company moves; automatic weather + sunrise/sunset from shoot location; attachments; walkie channels; quote of the day; "Week at a Glance".
- Publish: email and/or text message, personalized per recipient, preview before send, custom messages/style/sender, reply-to address; seamless revisions ("revise your call sheets and then rebroadcast them in just one click").
- Track: who received/opened/confirmed call time; delivery failure detection (bounces/spam); one-click resend to non-openers; auto-follow-up (marked "coming soon").
- Guest call sheet without signup (my.sethero.com/guest/callsheet).
- Contact management: central cast & crew hub; production reports interface with call sheets ("intelligently copy relevant information from a call sheet over to a production report").
- Industries: commercials/client/agency films, episodic TV, feature films, short films.
- Help center collections: "Building Call Sheets" (23 articles), "Publishing Call Sheets" (11), "Importing/Exporting Data", "Movie Magic Scheduling to Excel Converter".
- Note: SetHero's scheduling surface is the day-level schedule inside the call sheet ("Build your shooting schedule for the day") — no full stripboard product observed on fetched pages.

### Yamdu — evidence layer: A

- Positioning: "The Production Management Software for Films and Media"; "Create script breakdowns, shooting schedules, call sheets, time cards, and align all your projects in one single source of truth."
- Script import: Final Draft (partner), PDF, other formats; AI breakdown suggestions for departments to confirm.
- Shooting schedule: "Import existing schedules or assemble your stripboard by dragging and dropping scenes — and generate your Day-Out-Of-Days reports in real-time!"
- Call sheets: "Create or reuse templates and let us fill in all the details. Edit and customize the sheet to your liking, then send and track with Yamdu."
- Integrations: Final Draft, Fountain, PDF, Celtx (script import); Movie Magic, Fuzzlecheck (schedule import); Google Calendar / iCal / Outlook (calendar export); Slack; Zapier; Lockit Script sync; Showbiz Budgeting (schedule export).
- Wider suite: budgeting (Dynamic Globals®), smart time cards (labor-agreement templates, payroll export), CO₂e budgeting/sustainability (PEAR, MEDIA Carbon Calculator, KlimAktiv), project calendar, production calendar (Gantt), cast & crew hub, announcements, file sharing, comments.
- Security: watermarking, tracking of who viewed/edited/downloaded, advanced permissions, TPN membership, GDPR, Azure hosting, ISO badges; MovieLabs OMC-based API.
- Customer base: European broadcasters (ARD, ZDF, RTL, France TV...) + Netflix/Disney+/HBO logos; roles addressed: producers, line producers, production managers, production coordinators.
- Customer quote (Constantin Film): "things change all the time. And with Yamdu, everyone can see changes immediately."

### Filmustage — evidence layer: A

- Positioning: "The Complete AI Pre-Production Platform"; "Every step from locked script to first shooting day — breakdowns, schedules, budgets, and call sheets, built automatically with your input and kept in sync." "Change the script — your breakdown, schedule, budget, and call sheets update with it."
- Scheduling page:
  - Structured schedule automatically from script; organize scenes by location, character, INT/EXT, day/night; shooting days based on hours or pages; assign units and locations; "Adjust your schedule without rebuilding it — when one scene moves, everything stays connected."
  - AI Scheduling Agent with natural-language commands: "Group scenes by location", "Put all night scenes together", "Balance heavy shooting days", "Move scenes with John earlier", "Create a 10-hour shooting schedule starting March 1."
  - Conflict detection: reads stripboard, DOOD, and calendars; factors in hold days, conflict dates, overtime risk, force calls, company moves; flags days where availability doesn't line up; "restack strips while you're still in prep."
  - Calendar view: drag-and-drop scenes between shooting days; move entire days; spot overloaded days; test alternate versions.
  - Risk detection: overtime risks, tight turnarounds between night and day shoots, inefficient location jumps, missing time estimates, unbalanced shooting days.
  - DOOD: actor DOOD, unit-based DOOD, day-by-day summaries, scene counts per day, day/night breakdown.
  - Multi-unit: create/manage multiple shooting units, assign scenes per unit, auto-create units from script analysis.
  - Smart shooting day creation: max hours per day (8h/10h/12h), days by page count, exact number of shooting days, start dates, exclude weekends, add holidays, auto-calculate day count from time estimates.
  - Strip editing: edit text/color on strips, change scene numbers, Cast ID per scene, export in various formats.
- Call sheets: "Automatically transform your shooting schedule into professional, detailed call sheets... customizable and editable... Adjust times, crew details, locations, and more."
- Sides: assembled from the shooting schedule (shoot or script order), per-department filtered views, QR code on every page to confirm current version on set; "Bundle Call Sheet + Sides into one PDF and the whole day ships as a single file."
- Team access: per-feature permissions (None/View/Edit/Full); team chat; annotations in layers.
- Integrations: Movie Magic, Gorilla Scheduling, Final Draft. Security: SOC 2 Type II, TPN.

## Cross-product Comparison

| Dimension | Movie Magic Scheduling | StudioBinder | SetHero | Yamdu | Filmustage |
|---|---|---|---|---|---|
| Deployment | Desktop, offline (Tier 3) | Cloud | Cloud | Cloud | Cloud |
| Script import → scene records | Manual entry into breakdown sheets (Tier 3) | FDX/PDF/Fountain/TXT → auto stripboard | (not observed) | Final Draft/PDF/Fountain/Celtx + AI suggestions | Auto AI breakdown, any language/format |
| Stripboard / scene strips | Yes (Tier 3) | Yes — strips, drag-drop, auto-sort | No full stripboard observed (day schedule inside call sheet) | Yes — drag-drop strips; imports MMS/Fuzzlecheck schedules | Yes — strips, editable text/color, scene numbers |
| Day breaks by pages/hours | Yes (Tier 3) | Yes — page count or estimated shoot time | n/a | n/a | Yes — hours (8/10/12) or pages, exact day count |
| Banners (meals, company moves, notes) | Yes (Tier 3) | Yes | Company moves appear as call-sheet map-link items | n/a | Company moves as constraint input |
| Boneyard / omitted scenes | Yes (Tier 3) | Yes | n/a | n/a | n/a |
| Schedule versions/alternates | Versioned PDFs (Tier 3) | Duplicate schedule to compare | Revisions + rebroadcast | n/a | Alternate versions in calendar view |
| DOOD reports | Yes (Tier 3) | Yes | n/a | Yes — real-time | Yes — actor/unit/day-by-day variants |
| One-liner / breakdown sheets / sides | Production documents (Tier 3) | Yes — one-liners, breakdown sheets, daily sides | n/a | n/a | Sides from schedule + QR version check |
| Call sheet creation | No call sheet builder (Tier 3) | Generated from stripboard, auto-populated | Core artifact — drag-drop builder | Templates + auto-fill | Auto-transform from schedule |
| Call sheet distribution | Manual PDF distribution (Tier 3) | Email + SMS, personalized | Email + SMS, personalized, guest access | Send and track | (send implied; sides bundling) |
| Delivery tracking / confirmations | — | Sent/viewed/confirmed/undeliverable | Received/opened/confirmed + bounce detection + resend | "send and track" | n/a observed |
| Personal call times / precalls | — | Custom call time grids | Per-person call times, department precalls, cascading | n/a | Adjust times |
| Weather / maps / safety on call sheet | — | Live weather, Google Maps, hospital info | Weather + sunrise/sunset, map links, (hospital common industry practice) | Auto-fill details | n/a observed |
| Contacts (cast & crew) | No contact management (Tier 3) | Contacts module | Contact management core | Cast & crew hub | Team access |
| Multi-unit | n/a | n/a | n/a | n/a | Yes — units, per-unit scenes |
| AI assistance | — | — | Smart Assist (weather, overtime calc, typo detection) | AI breakdown suggestions | AI scheduling agent, conflict detection, risk flags |
| Adjacent modules | — | Shot lists, storyboards, calendars, tasks, file sharing | Production reports | Budgeting, time cards, CO₂e, Gantt, announcements | Budgeting, VFX breakdown, storyboards, annotations, synopsis |
| Security posture | Offline | — | — | TPN, watermarking, permissions, GDPR | SOC 2, TPN, watermarking |

## Canonical Model (L0–L3)

### L0 — Defining Invariant

The Type's defining core is a derivation chain from script to crew mobilization, held as three jointly-held structures:

1. **The scene as the unit of scheduling** — a persistent, individually addressable record derived from the script (scene number, slugline semantics: INT/EXT, location, day/night, page count, cast, elements) carrying production attributes. Remove → generic task/event scheduling; the script-derived grain is gone.
2. **The shooting day as the unit of production** — a dated, bounded day to which an ordered set of scenes is assigned, carrying day-level logistics (unit, location / company moves, call/wrap framing). Remove → a scene inventory (Script Breakdown territory); nothing gets produced on a day.
3. **The call sheet as the daily mobilization artifact** — a per-day, person-addressed document derived from the day's plan (the day's scenes in order, call times per person, locations, safety/logistics, notes) and distributed to the cast & crew. Remove → an internal plan of record with no crew-facing daily instrument; the daily mobilization of the company is gone.

Binding relationship: breakdown feeds scheduling; the schedule feeds the call sheet. The chain is the invariant.

**Pole tolerance (either end may be thin, the chain stays):** the market realizes the chain with different centers of gravity —

- *Schedule-centric pole*: Movie Magic Scheduling holds structures 1+2 deeply and produces the call sheet downstream (manually or via companion tools — SetHero's MMS exporter and Yamdu's MMS import both exist to bridge this). In-type.
- *Call-sheet-centric pole*: SetHero holds structure 3 deeply with day-level scheduling inside the call sheet (structure 2 thin, structure 1 absent as a full stripboard). In-type.
- *Full-chain products*: StudioBinder, Yamdu, Filmustage hold all three in one system.

Jointly-held load-bearing analysis:

- 1 alone = script breakdown tool (element tagging, no days)
- 2 without 1 = generic day calendar / event scheduling
- 3 without 1+2 = a messaging/document tool with call times and no plan behind it
- 1+2 without 3 = internal plan of record (MMS pole — in-type; call sheet produced downstream)
- 2+3 without 1 = call-sheet tool with day schedules (SetHero pole — in-type)
- The full chain 1+2+3 in one product = the mature cloud pattern (StudioBinder/Yamdu/Filmustage)

### L1 — Common Mature Structure

Very common across the sampled cloud products; not required to recognize the Type:

- Script import (Final Draft / PDF / Fountain / TXT) with scenes auto-populating the schedule
- Breakdown tagging of scene elements (cast, background/extras, props, wardrobe, vehicles, animals, SFX/VFX, notes) feeding schedules and reports
- Stripboard interface: scene strips, drag-drop reordering, banners (meals, company moves, notes), day breaks, boneyard for omitted scenes
- Auto-sorting/grouping by location, day/night, INT/EXT, cast
- Page counts and time estimates; day-break computation by pages or hours
- Schedule versions / duplicate-and-compare alternates
- Derived reports: DOOD (day-out-of-days), one-liner schedules, breakdown sheets, sides
- Contact management for cast & crew
- Call sheet templates and customizable sections
- Auto-filled call sheet data: weather + sunrise/sunset, map links, parking, hospital/emergency info, walkie channels, department notes
- Personal call times per recipient; precalls; cascading time changes
- Digital distribution: email + SMS, personalized per recipient; PDF export/print
- Delivery tracking: sent / viewed / confirmed; bounce detection; resend; revision rebroadcast
- Advance schedule (next day) on the call sheet
- Collaboration: sharing, comments, tasks, permissions
- Production calendar spanning prep→shoot→post (suite products)

### L2 — Variant / Optional Structure

Depends on segment, region, scale, workflow:

- AI-native assistance: AI breakdown suggestions (Yamdu, Filmustage), AI scheduling agent with natural-language commands and conflict/risk detection (Filmustage), Smart Assist overtime/typo checks (SetHero)
- Multi-unit scheduling (Filmustage)
- Budgeting linkage from breakdown/schedule (Yamdu Dynamic Globals, Filmustage auto-budget)
- Time cards / labor agreements / payroll export (Yamdu)
- Sustainability / CO₂e accounting (Yamdu)
- Daily production reports fed from call sheets (SetHero, StudioBroker adjacency)
- Call sheet types beyond shoot day: scout, rehearsal (StudioBinder)
- Sides generation with per-page QR version confirmation; call sheet + sides bundled as one PDF (Filmustage)
- Episodic TV structures; commercials/short-form; music videos; photoshoots (industry spread across SetHero/StudioBinder/Yamdu/Filmustage)
- Deployment: desktop/offline (MMS) vs cloud SaaS; security postures (TPN, SOC 2, watermarking, per-feature permissions)
- Integrations: Final Draft, Movie Magic import/export, Fuzzlecheck, calendar export (Google/iCal/Outlook), Slack, Zapier, MovieLabs OMC API (Yamdu)

### L3 — Vendor-specific (Research Notes only)

- SetHero: "Week at a Glance" section, quote of the day, tap-to-contact mobile call sheet, guest call sheet without signup, MMS→Excel converter tool
- StudioBinder: shot-list setups feeding schedule time estimates; DOOD + sides from stripboard; °F/°C and 12/24h toggles
- Yamdu: Dynamic Globals® budgeting, MovieLabs OMC-based API, PEAR / MEDIA Carbon Calculator / KlimAktiv integrations, Fuzzlecheck import
- Filmustage: "AI Dude" production agent, QR-coded sides, call sheet+sides single-PDF bundling, auto unit creation from script analysis
- Movie Magic Scheduling: desktop license model; the de-facto schedule data format others bridge to

## Anti-overfitting Notes

- **Cloud/SMS/tracking is NOT definitional**: the desktop offline standard (MMS) satisfies the scheduling core; the paper-era practice (physical stripboard + paper call sheets) satisfies the whole chain without software.
- **AI is NOT definitional**: only some products ship AI agents; the chain works without it.
- **Stripboard-as-UI is NOT definitional**: it is the dominant realization of the ordered schedule (and its name preserves the physical-board lineage), but the invariant is the ordered scene→day schedule, not the strip metaphor. (SetHero operates without a full stripboard.)
- **DOOD/one-liner/sides are NOT definitional**: they are derived reports; common but not identity-carrying.
- **Shared-implementation caution**: email+SMS distribution with view/confirm tracking is near-universal in the cloud sample (4/4 cloud products) but is an implementation of "distribute the day's plan to the people", not the invariant itself; paper distribution satisfies the concept.

## Historical / Market-Sample Check (§24)

- Paper-era practice: physical stripboard (colored scene strips on a board), handwritten breakdown sheets, typed/handwritten call sheets distributed on paper at day's end. All three L0 structures are satisfiable without any software — the software digitizes an existing workflow rather than inventing it. The stripboard UI metaphor surviving in every modern product is itself evidence of the paper lineage.
- Older/regional products: MMS (desktop, offline generation) fits L0 without cloud machinery; Yamdu (European broadcast co-production context) fits without US-specific union machinery in the core.
- Platform-native check: no OS-vendor-native instance of this Type exists (it is a profession-specific tool), so the check reduces to era/deployment variance — passed.
- Conclusion: L0 holds across eras and deployment models; modern machinery (cloud, SMS, tracking, AI) stays in L1/L2.

## Vendor-specific Findings

See L3 above. Notable for the final document's Variants section: the schedule-centric vs call-sheet-centric product shapes; the all-in-one suite vs point-tool split; AI-native entrant.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove / add to cross) |
|---|---|---|
| Script Breakdown Application | upstream input | Breakdown's center is the element inventory extracted from the script (categories, tagging, breakdown sheets). Here, breakdown exists as a *means* to schedule days and populate call sheets. Remove the shooting-day/schedule/call-sheet chain → breakdown tool. |
| Film Production Management / TV Production Management | broader suite | Suites add budgeting, documents, casting, payroll, reporting across the whole production lifecycle. This Type's center is the scheduling spine + daily mobilization. Suites bundle it (StudioBinder "Shoot", Yamdu, Filmustage all position scheduling/call sheets inside wider platforms). |
| Project Management Application (generic) | adjacent | Generic PM schedules tasks/milestones with assignees; no script-derived scene grain, no page counts, no DOOD, no call sheet, no company moves. Add scene semantics + day production + crew mobilization → this Type. |
| Employee Scheduling Platform | adjacent | Workforce scheduling's unit is a person-shift against coverage requirements; here the unit is a scene-day and people are *mobilized around the plan* (call times derived from scenes), not shifted to cover demand. |
| Event Management / Event Agenda Management | adjacent | Events schedule sessions/attendees/venues for an audience-facing occasion; here the schedule is script-derived and the daily artifact mobilizes a working company, not attendees. |
| Construction Scheduling | analogous domain | Same shape (activities → dated days → daily coordination artifact) but different object semantics (construction activities vs script scenes) — separate Type in the directory. |
| Production Accounting Platform | downstream sibling | Money (budgeting, actuals, payroll) vs days (schedule, call sheets). Yamdu/Filmustage bundle both; the objects differ. |
| Casting Platform / Audition Management | upstream | Talent selection vs scheduling of already-cast talent into days. |

Boundary issue to record: the directory separates Film Production Management, TV Production Management, and this leaf. Research supports the seam (scheduling spine vs whole-production suite), but the sampled suite products (StudioBinder, Yamdu, Filmustage) all bundle scheduling+call sheets inside wider platforms — the standalone-vs-bundled split is packaging, not identity. No taxonomy change proposed.

## Uncertainties

1. **Movie Magic Scheduling first-party documentation was unreachable** (entertainmentpartners.com 404/empty ×2). All MMS structural claims derive from a competitor comparison page (Tier 3) plus integration-page corroboration. The final document deliberately avoids MMS-specific precision (price, update cadence, exact feature list) and describes the schedule-centric pole generically, naming MMS only as the representative product.
2. Whether any product fully auto-generates call sheets with *no* schedule object at all was not observed; SetHero's call sheets embed a day-level schedule. Not load-bearing for L0.
3. Depth of union-rule enforcement (turnarounds, force calls, overtime) varies; Filmustage documents force calls/overtime risk as constraint inputs, SetHero documents overtime calculations. Exact rule engines were not researched; the final document keeps this qualified.
4. Exact call-sheet section sets vary by product; only sections observed on official pages are claimed.
5. Yamdu call-sheet mechanics observed only at root-page depth (templates, auto-fill, send, track) — no dedicated feature page fetched.

## Final Synthesis

A Production Scheduling / Call Sheet Application is the film/TV production's scheduling system of record and daily mobilization instrument. Its defining core is a derivation chain: the script is broken into scenes carrying production attributes; scenes are ordered and grouped into dated shooting days; the ordered schedule is the plan of record; and each day's plan is projected into a call sheet — a person-addressed document carrying the day's scenes, call times, locations, safety and logistics — distributed to cast and crew and tracked to confirmation. The market realizes this chain with different centers of gravity: a desktop schedule-of-record standard whose call sheets are produced downstream; call-sheet-first cloud tools whose schedules live at day grain; and cloud suites holding the full chain with derived reports (DOOD, one-liners, sides) and adjacent modules (budgeting, time cards, creative pre-production). The chain — scene → shooting day → schedule → call sheet → confirmed recipient — is the invariant; every specific mechanism (stripboard UI, SMS delivery, AI agents, tracking dashboards) is a common or variant implementation of it.
