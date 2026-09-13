# Research Notes — Cinema Scheduling Application

## Research Goal

Understand what a Cinema Scheduling Application is as an Application Type: the tool a film exhibitor uses to plan which films play in which auditoriums at which times (the programme / schedule of showtimes). Determine:

1. The defining core (what makes it "cinema scheduling" and not generic scheduling or broadcast scheduling).
2. Whether a **standalone product family** exists, or whether scheduling is always realized as a module of the Cinema Management System — this is the disposition question pre-hung by the cinema-management-system pass (2026-09-10): "film programming/scheduling is the spine module of the management system… that pass should decide standalone-application-vs-slice disposition."
3. The standard capability ring around the core (session configuration, publication, distribution, AI assistance).
4. Boundaries vs: Cinema Management System (whole), Broadcast Management System, projection TMS/CMS, Employee Scheduling, film Production Scheduling, Event Ticketing, distributor-side release planning.

## Initial Boundary

Working hypothesis at start:

- A Cinema Scheduling Application is the film programmer's/booker's planning surface: it composes sessions (film × auditorium × date/time), attaches selling configuration, publishes the schedule, and distributes it to selling channels, signage, and the projection layer.
- Nearest neighbors: Cinema Management System (the whole business system — scheduling is its spine module), Broadcast Management System (schedules content for transmission), Theatre Management System (projection control — consumes the schedule), Employee Scheduling (staff shifts — a naming trap: "cinema scheduling" could be misread as staff scheduling), Production Scheduling / Call Sheet Application (film production — a different domain entirely), Event Ticketing Platform (sells dated admission but does not own the programme).
- Pre-hung seams: (a) cinema-management-system pass — "1 alone = a showtime calendar / scheduling tool (sibling leaf territory)"; (b) reserved-seating-platform pass — cinema seam discharged there (seat layer lives inside the cinema system's own model).
- Key open question: does any vendor sell scheduling as a standalone product?

## Research Questions

1. What is the central object model? (film records, auditorium/screen estate, sessions/showtimes, the schedule)
2. How does the scheduling work actually flow? (pre-planning → session composition → configuration → publication → distribution)
3. Who does the scheduling? (film programmer/booker at head office vs site manager; what is the division of labor and its permission machinery?)
4. Is there a standalone product family, or is scheduling always a module of the cinema management system?
5. What optimization/AI exists (assisted scheduling, forecasting, planning policies)?
6. What rules constrain the schedule (runtime + trailer/cleanup math, distributor agreements, ratings, planning policies)?
7. Where does the schedule end and the projection TMS begin?
8. Historical check: would a paper-era programmer's wall chart still fit the definition?

## Representative Products

Selected for market position spread, documentation quality, and different product philosophies. Because the scheduling function ships inside cinema management systems, the sample is the scheduling surfaces/modules of the four systems already documented in the sibling pass, re-examined from the scheduling side:

| Product (scheduling surface) | Position | Philosophy | Evidence layer |
|---|---|---|---|
| Vista — Film Manager + Showtime Manager (+ Assisted Scheduling, Cinema Intelligence) | Global enterprise leader for chains | Central hub for circuit-wide programming; programmer-owned schedule; AI-assisted | A (help-centre articles + product pages + vendor case study) |
| Veezi — Film Programming | SaaS for independent cinemas (Vista-engineered) | Self-serve drag-and-drop programming for small sites | A (feature page, full text) |
| RTS — Film & Schedule Management | US all-in-one; independents to chains, drive-ins | Scheduling embedded in operations suite; export to TMS/LMS | A (operations page, fetched live this pass) |
| Omniterm — Ticketing Control | North America, since 1978; POS-centric | Central film-data store feeding scheduling, pricing, seating | A (product pages, from sibling pass) |

Boundary references (not samples of this Type): OneCinema TMS (projection family — consumes the schedule); Cinematik (distributor-side data platform); Vue's bespoke AI scheduling (exhibitor-built tool, evidence of the function's distinctness, not a market product).

Rejected as samples (product-pollution traps): FilmSchedule, Gorilla Scheduling, StudioBinder, Shamel Studio (film **production** scheduling — stripboards, call sheets; different domain); Findmyshift, Vista MovieTeam (cinema **staff** scheduling — different object); Power Plant Cinema schedule page (consumer-facing showtime display, not the scheduling tool).

## Sources

Research date: 2026-09-10. All sources fetched live this pass unless noted.

- Vista Help Centre — "Showtime Manager": https://help.vista.co/hc/en-nz/articles/4416511988633-Showtime-Manager
- Vista Help Centre — "Creating and publishing draft sessions in film manager": https://help.vista.co/hc/en-nz/articles/59102702457369
- Vista Help Centre — "Restricting session properties in Showtime Manager": https://help.vista.co/hc/en-nz/articles/13960191819929
- Vista Classic product page (Film Manager + Cinema Intelligence + Cinema Manager descriptions): http://cinemaintelligence.com/ (serves Vista Classic content) and https://vista.co/vista-classic
- Vista Cinema Manager product sheet (PDF, 2020): https://cdn.prod.website-files.com/60a5ad9159a5687b2c694d70/6449a6151b308932ff0fe594_Cinema%20Manager%20Product%20Sheet%202020.pdf
- Vista insights — "Joint Innovation by Pathé and Vista Halves Film Programming Time" (Assisted Scheduling case study): https://vista.co/insights/joint-innovation-by-pathe-and-vista-halves-film-programming-time
- Vista homepage (industry value chain: "Cinema - Head Office … Film scheduling"): https://vista.co/
- Vista roadmap — "Film Manager: Film forecasting enhancement": https://roadmap.vista.co/c/604-film-manager-film-forecasting-enhancement
- Veezi — Film Programming feature page: https://www.veezi.com/features/film-programming
- RTS — Operations page (Film & Schedule Management): https://www.rts-solutions.com/operations-1
- Omniterm — Theatre Management page (Ticketing Control): https://omniterm.com/theatre-management/ (from sibling pass, 2026-09-10)
- OneCinema TMS (boundary reference): https://onecinema.de/en/produkte/onecinema-tms
- City A.M. — "Vue: Cinema chain hands over film scheduling to AI" (2024-07-22): https://www.cityam.com/vue-cinemas-ai-software-drives-admissions
- Screen Daily — "How major and indie cinema chains are using AI tools" (2026-04-16): https://www.screendaily.com/features/how-major-and-indie-cinema-chains-are-using-ai-tools-they-are-saving-me-at-least-one-day-a-week/5215694.article
- Cinematik (boundary reference, distributor-side): https://www.cinematik.app/services
- Sibling pass relied on for cross-checks: research/cinema-management-system.md + applications/cinema-management-system.md (2026-09-10)

## Product A — Vista (Film Manager / Showtime Manager / Assisted Scheduling / Cinema Intelligence)

### Key observations (evidence layer A unless noted)

**Positioning of the function.** Vista's homepage industry-value-chain places "Film scheduling" under "Cinema - Head Office" (alongside reporting, marketing, digital movie media, circuit management) — scheduling is a head-office function in the vendor's own map of the industry.

**Film Manager (product page).** "Schedule films throughout your circuit from a central hub and let clever automations create the perfect plan." Supports "all aspects of your film programmers' workflow – from pre-planning months in advance to session scheduling the week before a film plays at each cinema." Leverages Vista Group capabilities (Cinema Intelligence, Numero, MX Film) "to optimise attendance, monitor film performances, and manage movie data and media." "Enforce the screening requirements for a film through the central deployment of planning policies, a powerful tool that specifies the number and times of sessions per film per day."

**Showtime Manager (help centre).** "Film Manager's Showtime Manager is a tool for scheduling the sessions at your cinema." Parts: toolbar (display preferences; common actions such as "opening sessions for sale and adding films to the schedule"); film search bar ("lists all the available films for scheduling. You can drag and drop or click and 'paint' films from the search results onto your canvas to schedule them. If you use holdover bookings from your head office to create sessions, you'll see an Add holdover films button instead"); canvas ("divided into rows representing each of your cinema screens, and segments of time from left to right. Any film placed on the canvas is therefore assigned to a screen and a session time"); session properties panel ("Double-clicking any session expands its properties panel. Here you can specify details of the session's timing, sales, attributes, and more").

**Draft → publish lifecycle (help centre).** Draft mode builds and reviews sessions without making them visible; draft indicators (black dot, dotted border; white in status-colour view); "Draft sessions are not visible until they are changed to Planned and saved"; converting to Planned and saving "makes sessions visible to cinema managers once saved." Explicit warning: "Always confirm session status before saving to avoid publishing incomplete schedules."

**Programmer ↔ site-manager division of labor.**
- Cinema Manager product sheet: "Showtime Manager bridges the gap between cinema managers and film programmers by integrating with Vista Film Manager. Managers can easily schedule according to film programmers' instructions, and sessions created in Cinema Manager can be reviewed in Film Manager right away."
- Cinema Manager product page: "Film Manager native integration: managers can quickly adapt schedules to suit film programming requirements, which programmers can view and approve."
- Restricting session properties (help centre): "You can restrict some film booking properties to prevent cinema managers from making changes to sessions in Showtime Manager without approval from the film programmer." Restrictable properties: Film, Session start time, Film format, Screen. "The restricted properties will be disabled for anyone accessing Showtime Manager from Back Office. If you access Showtime Manager from Film Manager you'll be able to edit sessions with no restrictions."

**Assisted Scheduling (vendor case study with Pathé NL).** "Film scheduling is really a craft… You don't learn it in one day. It requires a deep understanding of what our audience wants, the operation dynamics of each cinema, and of course the agreements we have with distributors and studios" (Pathé programming manager). "A seven-screen cinema can show up to 35 or 40 different films in one week, which makes the puzzle very complex." Assisted Scheduling "creates an initial film schedule in moments… based on forecasting and past performance data… provides film programmers with a starting point to refine from"; "Film programmers can override suggestions… and add in requirements of sessions they know are the right call"; "taking the task of scheduling from one of manually dragging sessions into the schedule into one of refinement and optimisation"; "they are still in control." Vendor claims ~50% programming-time reduction (vendor claim, single customer).

**Cinema Intelligence (product page).** "An artificial intelligence powered solution for film forecasting, distribution negotiation, automated scheduling, and business analysis… Create a schedule in minutes and screen the best films for your target audience. Enhance booking decisions with 'what if' analysis and professional film insights."

**Head Office (product page).** Integrations "from film hire costs and film programming to stock movements" — programming sits in the head-office ring.

## Product B — Veezi (Film Programming)

### Key observations (evidence layer A)

**Positioning.** "Great film programming is key to the success of your cinema. To streamline the scheduling process Veezi has a preloaded database of current films, and the programming interface is simple and easy to use. Best of all, you can create and edit your schedule from anywhere!"

**Scheduling surface.** "Easily copy and create sessions via a drag-and-drop function. You can bulk copy schedules by day or week and can even edit show details by session, direct from the programming screen." Per-session editable details: price cards, sales-channel availability, allocated vs unallocated seating toggle, extra time for trailers and cleanup, 'private' showings (limited access). Cloud: "As long as you have internet access, you can manage your schedule from wherever you are—great for adding an extra session if a show is selling out!"

**Film data.** Pre-loaded film list from movieXchange MX Film ("studio-official film database"); each film record carries run time, rating, synopsis, poster graphics; editable after import; custom film records for special events.

**Marathons.** "Connect double or multiple features under one ticket… scheduled and ticketed as a single session while recording rental for each film" — settlement awareness inside the scheduling surface.

## Product C — RTS (Film & Schedule Management)

### Key observations (evidence layer A, fetched live this pass)

**Positioning.** "RTS's film and schedule management systems streamline your theatre's scheduling operations with an intuitive interface that allows managers to easily select films and click to schedule showtimes in their desired slots. Once scheduled, showtimes can be adjusted and moved around the calendar with simple drag-and-drop functionality. The built-in film database includes thousands of titles, complete with graphics and metadata, reducing manual data entry and ensuring accuracy. These tools help theatres optimize showtimes, minimize scheduling errors, and maintain synchronization across all locations for a seamless scheduling process from planning to showtime."

**Named capabilities.** "Use the extensive Film Database to create your movies. Drag and Drop film scheduler with features to make scheduling convenient. Export schedule to TMS/LMS. Automatically updates digital signage and websites through XML or API integration."

**Remote/enterprise.** "Make changes to show schedules… from any location" (remote connections); enterprise: "Centralized Multi-Location Management", "Remote Schedule Updates".

**Feedback loop.** Advance Ticket Sales report "breaks down ticket sales by showtime, auditorium, and date… Utilize this report for demand forecasting and strategic scheduling decisions" — sales data feeding the next scheduling decision.

## Product D — Omniterm (Ticketing Control)

### Key observations (evidence layer A, from sibling pass pages)

**Ticketing Control.** Central store of posters, trailers, ratings, synopses used by online ticketing, signage, POS, kiosks, website; "manage film scheduling, pricing, and seating."

**Automation Manager.** "Automated features that can update digital projection systems, LCD poster displays, box office marquees, and feed numerous online ticketing and social media sites" — the schedule distributed outward to projection and public surfaces.

## Cross-product Comparison

| Dimension | Vista | Veezi | RTS | Omniterm | Reading |
|---|---|---|---|---|---|
| Session = film × screen × time placement | Showtime Manager canvas (screen rows × time) | drag-and-drop session creation | drag-and-drop scheduler; showtimes in slots | scheduling in Ticketing Control | **All four**: the session placement is the unit of scheduling |
| Film records as schedulable content | film palette; MX Film integration | MX Film preloaded (runtime, rating, synopsis, posters) | built-in film database, thousands of titles, metadata | central store: posters, trailers, ratings, synopses | **All four**: films are managed records reused across sessions |
| Auditorium/screen estate as placement capacity | canvas rows = screens | sessions placed per screen | "manage auditoriums"; slots | screens in Ticketing Control | **All four** |
| Bulk/repeat composition | holdover bookings from head office; planning policies | bulk copy by day or week | copy schedules across multiple days | (not observed) | **3 of 4 documented**; chain-scale repetition is standard |
| Session-level selling configuration | session properties: timing, sales, attributes | price cards, channel availability, seating toggle, trailer/cleanup, private | ticket rules per performance | scheduling + pricing + seating together | **All four**: the schedule carries its selling configuration |
| Draft/compose-before-publish | explicit draft→planned→publish with visibility semantics | (edit live; cloud) | (not documented) | (not documented) | **1 of 4 explicit**; publish semantics asserted at moderate strength |
| Programmer ↔ site-manager split with permissions | Film Manager (programmer, unrestricted) vs Back Office (restricted properties); approval loop | single-operator self-serve | managers schedule directly | single-site orientation | **Split documented in the chain pole; single-site products collapse the roles** |
| Schedule distributed outward | signage, movieXchange showtime distribution | signage feature | export to TMS/LMS; XML/API to signage + websites | Automation Manager: projection systems, marquees, online ticketing | **All four**: the schedule drives downstream surfaces incl. projection |
| Performance feedback into scheduling | Cinema Intelligence forecasting; Assisted Scheduling | dashboard informs "switching out scheduled films" | Advance Ticket Sales report for "strategic scheduling decisions" | (not observed) | **3 of 4 documented** |
| AI/assisted scheduling | Assisted Scheduling; Cinema Intelligence | — | — | — | **1 of 4** (plus Vue's bespoke tool per press) — advanced, not definitional |
| Standalone product? | module of Vista suite | module of Veezi | module of RTS suite | module of Omniterm | **No standalone scheduling product in the sample or in searches** |

## Abstraction

### L0 — Defining Invariant

Three jointly-held structures over one binding (the exhibitor's own film programme in its own auditoriums):

1. **The session as the scheduled unit.** A film placed in one of the operator's auditoriums at a date and time, composed on a schedule surface (commonly a canvas of screen rows against a time axis), carrying its selling configuration. The schedule is a population of these placements, recomposed continuously (weekly/new-Release cycles). Remove → a film list and a screen list with nothing scheduled, or a generic time-grid tool.

2. **The two reference estates the session draws from.** (a) Films held as schedulable content records — title, runtime, rating, promotional media — created once and reused across many sessions and sites; runtime shapes the time math, rating gates age-checked selling. (b) The auditorium/screen estate — the operator's own screens with capacity — into which sessions are placed. Remove the film estate → generic resource/event scheduling; remove the auditorium estate → broadcast/content scheduling.

3. **The schedule as the operational programme of record.** The composed schedule is published to become the programme the cinema runs on: it becomes visible/buyable to selling channels, drives signage and public listings, and drives the projection layer. Remove → a private planning sketch with no operational effect.

Jointly-held load-bearing analysis:
- 1 alone = a generic calendar/time-grid tool
- 2 without 1 = estates with no programme
- 3 without 1+2 = publishing nothing in particular
- 1+2 without 3 = a planning sketch that never becomes operational
- 1+3 without 2 = generic show/event scheduling (event-ticketing shape)
- 2+3 without 1 = content and capacity with no schedule

Binding: the exhibitor's own rolling film programme (remove → broadcast scheduling for transmission, or generic resource scheduling).

### L1 — Common Mature Structure

Present across the sampled products; makes the function practical but does not define it:

- **Drag-and-drop schedule canvas** — screen rows × time columns; drag/paint films onto the grid.
- **Bulk composition** — copy schedules by day/week; holdover bookings from head office; template repetition.
- **Session-level selling configuration** — price cards/pricing rules, sales-channel availability, seating mode (allocated/unallocated), trailer and cleanup time, private/limited-access showings, per-performance ticket rules.
- **Film database integration** — central or studio-official film data (runtime, rating, synopsis, posters) feeding the schedule and the channels.
- **Programmer ↔ site-manager division of labor** — head-office programmers own the programme; site managers adapt within limits; approval/restriction machinery (Vista-documented; single-site products collapse the roles).
- **Planning policies** — centrally deployed rules specifying the number and times of sessions per film per day (Vista-documented; treat as common-in-mature, single-vendor-documented).
- **Outward distribution** — digital signage, websites, listing/ticketing services, and the projection TMS (export/XML/API).
- **Performance feedback loop** — advance-sales and attendance data informing the next scheduling cycle.
- **Marathons/double features** — multiple films under one ticketed session (with per-film rental recording in one product).

### L2 — Variant / Optional Structure

- Scale shape: circuit-wide central programming (programmer role) vs single-site self-scheduling (manager does everything).
- AI depth: none → assisted initial schedule (human refines) → automated scheduling with what-if analysis (Cinema Intelligence class); bespoke exhibitor-built tools (Vue AIS).
- Content breadth: festivals/repertory, alternative content/events, private screenings/group bookings scheduled in the same surface.
- Market shapes: reserved-first vs GA-first markets change what a session carries (seating mode), not the scheduling act.
- Drive-ins, dine-in cinemas (session-aligned service windows).
- Draft/publish formality: explicit draft states vs live editing.

### L3 — Vendor-specific (research notes only)

- Vista: Film Manager / Showtime Manager naming; draft/planned status labels and indicators (black dot, dotted border); RestrictFilmBookingProperties system setting; "Add holdover films"; planning policies; Assisted Scheduling (Pathé co-development; seconds-to-2-minutes generation claim; ~50% time-reduction claim); Cinema Intelligence ("what if" analysis); MX Film; movieXchange showtime distribution.
- Veezi: MX Film preloaded database; allocated/unallocated toggle; 'private' showings; marathon rental recording; gadget dashboard informing "switching out scheduled films".
- RTS: "Export schedule to TMS/LMS" phrasing; XML/API signage/website updates; remote schedule updates; Advance Ticket Sales report framing.
- Omniterm: Ticketing Control naming; Automation Manager; punch-clock-per-station (staff side, out of scope).
- Vue: bespoke "AI scheduling (AIS)" tool (press-reported; exhibitor-built, not a market product).

## Vendor-specific Findings

- Vista's draft→planned→publish lifecycle with explicit visibility semantics is product-documented; the canonical claim is "the composed schedule becomes visible/buyable when published" at moderate strength.
- Vista's property-restriction machinery (Film, Session start time, Film format, Screen; disabled from Back Office, unrestricted from Film Manager) is product-documented; the canonical claim is "the programmer's authority over the programme can be enforced through permissions" at moderate strength.
- Vista's Assisted Scheduling and Cinema Intelligence are single-vendor AI capabilities; the canonical claim is only "forecast-informed schedule generation exists as an advanced capability in the enterprise pole" (plus press evidence of a second exhibitor building its own).
- Veezi's marathon-rental recording shows settlement awareness reaching into the scheduling surface (second product after Vista's film-hire context; still L1/L2, not definitional).

## Boundary Findings

1. **vs Cinema Management System (processed sibling) — THE DISPOSITION.** Film programming/scheduling is the spine module of the cinema management system: every sampled scheduling surface (Vista Film Manager/Showtime Manager, Veezi Film Programming, RTS Film & Schedule Management, Omniterm Ticketing Control) is a module of a full business system that also sells tickets, runs concessions, and settles with distributors. **No standalone end-to-end cinema scheduling product family was found** — in the sample, in targeted searches ("standalone cinema scheduling software", "film programming software"), or in press (the only bespoke tool found is Vue's in-house AIS). The scheduling function nonetheless has its own user (film programmer/booker), its own craft and workflow (pre-planning → composition → publication → distribution), its own rules (runtime math, distributor agreements, planning policies), and its own AI layer. **Disposition: keep-both as slice-leaf** — this leaf documents the scheduling function (the programmer's planning surface and workflow); the cinema-management-system leaf documents the whole business system. The relationship is the same shape as reserved-seating-platform (seat layer) vs event ticketing: a real, coherent layer realized inside the sibling system rather than as standalone products. No directory change made unilaterally; recorded for the taxonomy owner.

2. **vs Broadcast Management System (§27 sibling).** Broadcast schedules content for transmission to an undifferentiated audience; cinema scheduling places ticketed sessions in seated auditoriums for individually sold admission. Removal test: remove the auditorium estate and the admission semantics → broadcast scheduling. Distinct Types.

3. **vs Theatre Management System / Circuit Management System (projection family; no directory leaf — gap already recorded by the cinema-management-system pass).** The TMS consumes the schedule to drive projection: OneCinema TMS "POS system import. Automatic import of show schedules, age ratings and sold tickets from your POS system"; RTS "Export schedule to TMS/LMS"; Omniterm Automation Manager "update digital projection systems"; Unique X "the film schedule drives the operation of the cinema". The scheduling application produces the schedule; the TMS executes it on screens' playback devices. Opposite ends of the schedule pipeline; distinct types.

4. **vs Employee Scheduling (§09) / cinema staff scheduling.** Naming trap: "cinema scheduling" in this leaf means FILM scheduling (the programme), not staff shift scheduling. Vista's own MovieTeam product and generic tools (Findmyshift) schedule people, not sessions. Different object, different users, different rules.

5. **vs Production Scheduling / Call Sheet Application (§27 sibling).** FilmSchedule, Gorilla, StudioBinder, Shamel schedule the *making* of films (script breakdown, stripboard, shooting days, call sheets). This leaf schedules the *exhibition* of finished films. Different domain entirely; the shared word "film scheduling" is a search-engine trap, not a taxonomy overlap.

6. **vs Event Ticketing Platform (processed).** Event ticketing centers organizer-defined one-off events with an on-sale moment; cinema scheduling centers the operator's continuously recomposed programme of sessions. The scheduling application does not sell; it feeds the selling system with buyable sessions. Distinct Types.

7. **vs Distributor-side release planning (e.g., Cinematik; Vista Maccs).** The distributor decides release dates and which cinemas book the film; the exhibitor's programmer decides sessions within the exhibitor's own estate. Opposite sides of the booking relationship. Adjacent, not the same Type.

8. **vs Meeting/Resource Scheduling (§03.09) and Academic Timetabling (§23).** Generic scheduling books resources for internal use against availability; cinema scheduling composes a public commercial programme from content records under distributor agreements and revenue intent. The film and auditorium estates + the commercial programme binding are what make it cinema scheduling.

## Historical / Market-Sample Check (§24)

- Paper-era single-screen cinema: the owner/programmer picks the week's programme (which film, which times) on a written or charted schedule; the marquee publishes it; the box office sells against it; the projectionist follows it. All three L0 structures present without any software — the definition does not over-fit the modern stack.
- Chain booking-sheet practice (holdovers, studio clearances, weekly programmes) is the pre-digital form of the same loop; Vista's "holdover bookings from head office" digitizes it.
- Regional/platform differences: single-site independents schedule directly in their management system; chains run head-office programming with site adaptation — both fit the L0.
- Older cinema systems (Omniterm, since 1978; DOS-era terminals) carried scheduling screens — the function predates the modern cloud stack.

## Uncertainties

- **Standalone-product question:** no standalone cinema scheduling product was found in the sample, searches, or press. Absence of evidence is not proof of absence — a niche standalone tool could exist outside the researched markets (e.g., a regional vendor). The disposition is therefore "slice-leaf, keep-both" with this uncertainty recorded, not a merge recommendation.
- Exact session-state vocabularies beyond Vista's draft/planned are unknown; publish semantics asserted at moderate strength.
- The precise split of scheduling responsibility between head office and site varies by circuit; documented for Vista, asserted moderately for the Type.
- RTS's scheduling depth (per-performance ticket rules) is documented at product-page level; deeper workflow detail was not reachable.
- The size of the AI-scheduling population (beyond Vista's products and Vue's bespoke tool) is unknown; Screen Daily (2026-04) indicates multiple chains use AI tools, but per-product documentation was not fetched.

## Final Synthesis

A Cinema Scheduling Application is the film exhibitor's **programme-planning function**: the surface on which a film programmer composes the schedule of sessions — films placed into the operator's own auditoriums at times, each carrying its selling configuration — and publishes it as the operational programme that drives selling channels, signage, and the projection layer. Its defining core is three jointly-held structures: the session placement as the scheduled unit; the film and auditorium estates as the two reference structures sessions draw from; and the schedule's publication as the programme of record. The market realizes this function **as the programming/scheduling module of cinema management systems** (enterprise chains add programmer-owned central scheduling with permission machinery and AI assistance; independents self-serve drag-and-drop scheduling), not as standalone products — the leaf is therefore documented as the scheduling slice of the exhibitor's system estate, keep-both with the cinema-management-system leaf. Boundaries: broadcast scheduling (transmission vs ticketed sessions), the projection TMS (consumes the schedule), staff scheduling and film-production scheduling (different objects despite shared words), event ticketing (sells; does not own the programme), and distributor-side release planning (the other side of the booking relationship).
