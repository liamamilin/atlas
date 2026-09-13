# Research Notes — TV Production Management

Research date: 2026-09-09

## Research Goal

Understand what "TV Production Management" software actually is as an Application Type, from real products: what the core object model is (and specifically how episodic structure — episodes, seasons, long runs — is realized), how the film-style production machinery (script → breakdown → schedule → call sheet) applies per episode, who uses it, what states and rules govern it, and where the boundaries sit against neighboring Types (Film Production Management, Production Scheduling / Call Sheet Application, Theater Production Management, Broadcast Management System, Newsroom Management System, Production Accounting Platform, Script Breakdown Application, Casting Platform, Media Asset Management, generic Project Management).

This pass also discharges two pre-hung joint-review flags from sibling passes:

1. **film-production-management (§27, 2026-09-07) vs tv-production-management** — "probable one-Type-two-variants... recommend joint review when tv-production-management is processed to decide keep-both-as-variants vs merge."
2. **production-scheduling-call-sheet-application (§27, 2026-09-09)** — "seam to ratify when those leaves are processed = scheduling spine + daily mobilization chain vs whole-production lifecycle objects."

And it holds the seam ratified by **theater-production-management (§27, 2026-09-09)** from its side (delivery unit = live run → theater; shoot → film/TV territory).

## Initial Boundary (hypothesis before research)

- Core hypothesis: the production office's system of record for TV — same machinery family as film production management (script breakdown, shooting schedule/stripboard, call sheets, cast & crew, locations, budgeting), organized around episodic content: episodes/seasons as the recurring unit of production, ongoing cycles, series-wide continuity of people/sets/elements.
- Possible second pole: studio/entertainment TV (talk shows, variety, game shows) — rundown/segment-driven rather than screenplay-scene-driven; possible drift toward Broadcast Management System / Newsroom Management System territory.
- Likely users: line producers, UPMs, 1st ADs, production coordinators, producers; series production offices; broadcaster/streamer production teams.
- Likely confusions: vs Film Production Management (closest sibling — one machinery?); vs the scheduling/call-sheet slice; vs broadcast/newsroom systems (rundowns); vs theater (recurring-unit structure looks similar).
- Unknowns: do products model episodes/seasons as first-class objects or just as successive projects? Is season-level continuity machinery real? Is rundown machinery part of this Type? Does the professional US episodic tier differ structurally?

## Research Questions

1. What is the core object model for TV production management? (series production, episode, season, script/rundown per episode, scene/segment, stripboard, shooting day, call sheet, cast & crew, locations/sets, budget)
2. How is the episodic container realized — explicit episode objects with linked documents, seasons, blocks, or just one project per episode? What continuity machinery exists across episodes and seasons (recurring cast, standing sets, location/wardrobe libraries)?
3. How does the film-style pipeline (script → breakdown → schedule → call sheet) run per episode, and what is shared vs different?
4. What TV-specific workflow shapes exist: block shooting, multiple teams shooting simultaneously, daily/long-run programming (talk shows, telenovelas), multi-camera studio shows with rundowns?
5. Who uses the system, and how do roles/access change relative to film (per-episode access, broadcaster oversight)?
6. Where are the boundaries: vs Film Production Management, vs the scheduling/call-sheet slice, vs broadcast/newsroom rundown systems, vs theater, vs accounting/breakdown/casting/MAM, vs generic project management?
7. Historical check: would the pre-software episodic TV production office (per-episode scripts, paper stripboards, typed call sheets, continuity books) satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

1. **Yamdu** — European cloud production management platform with a dedicated TV Series audience page; mid-to-large productions and co-productions; clientele includes major European broadcasters and streamers. Strongest explicit seasons/episodes machinery in the sample.
2. **Dramatify** — TV-native cloud platform (Sweden-origin) spanning episodic drama AND multi-camera studio/entertainment formats; the sample's only product with a rundown suite; rich public help center (directly fetched).
3. **Filmustage** — AI-first pre-production platform (US-facing) covering "Films, Series & TV Shows", short/vertical dramas; machinery is per-script; indie-to-studio tier.
4. **StudioBinder** — cloud all-in-one suite self-labeled "Video, TV & Film Production Management Software" with "Episodic Structure" as a named platform feature; indie/SMB-to-enterprise tier.

Also noted: **Scenechronize** (Entertainment Partners) — the long-standing US professional episodic production tool — was attempted as a professional-pole sample but its site is behind a cookie/application gate; not usable as direct evidence this pass (see Sources).

Prior-pass corroboration (not re-sampled): film pass (2026-09-07) observed Gorilla, Celtx, and Movie Magic with the same machinery family; the scheduling pass (2026-09-09) observed the scheduling spine products.

## Sources

Directly fetched official sources (2026-09-09):

- Dramatify — main site (https://dramatify.com/); "Working with Episodes and Series" help article (https://dramatify.com/faq/series-episodes, updated 2026-01-05). Help-center index confirms additional articles (rundowns: create/views/access rights/updates; series creation; call sheets; budgeting incl. Movie Magic Budget import).
- Yamdu — main site (https://www.yamdu.com/en/) and TV Series audience page (https://www.yamdu.com/en/for-productions/tv-series/).
- Filmustage — main site (https://filmustage.com/).
- StudioBinder — main site (https://www.studiobinder.com/).

Source-access limitations:

- **Scenechronize**: root URL returned a cookie/browser-configuration gate (© Entertainment Partners); no operational documentation reachable. Per the network-restriction rule the source was abandoned after the failure. No feature claims about Scenechronize are made anywhere in this research; it is recorded only as an attempted professional-pole sample.
- **Entertainment Partners (Movie Magic family)**: unreachable in the film pass (2026-09-07); same limitation carries over.
- StudioBinder help center was unreachable in the film pass (HTTP 502); this pass used the main site only. Filmustage help center exists (help.filmustage.com) but was not fetched; main-site claims only.
- Evidence calibration: episodic-container machinery is evidenced at full depth for Yamdu and Dramatify; for Filmustage and StudioBinder the episodic evidence is content-scope/feature-naming level (details unobserved). Rundown machinery rests on a single product (Dramatize) and is therefore held as optional/product-specific, not canonical.

## Product Observations

### Yamdu (evidence layer: A — direct official observation)

- Self-labels: "The Production Management Software for Films and Media"; audience pages: Film, **TV Series**, Commercial, Documentary; "film, TV, commercial, documentary, unscripted, and everything in between."
- TV Series page headline: "**Keep All your Episodes and Seasons Together**" — "plotting out the entire timeline of your story from development to the first shooting day and beyond."
- Series hub: "Set up a Single Space for All Series Data" — one hub for production details; import Final Draft/PDF drafts; "plot out each episode with the crew, version by version"; "Make quick changes to a single document and see it automatically applied to all other linked documents — and let the system automatically alert every other department about it!"
- **Season continuity**: "Reuse Existing Data and Secure Each New Season" — creating a new season imports existing data from the company database; user selects what to bring; "keep assets like the main actors, locations, sets, and costumes consistent for every season."
- **Per-episode / per-block access rights**: "Manage access rights for every user either per episode or by blocks (multiple episodes). Limit which teams and members are involved in creating a production outline."
- Calendar: "Point out the stages of overarching arcs or storylines, and link production steps to episodes so that everyone knows who's responsible for editing what" — episodes as linkable planning objects; arcs span episodes.
- Shared machinery (main page): script import (Final Draft/PDF/Fountain/Celtx) + AI-enhanced breakdown with human confirmation; stripboard assembly or schedule import (Movie Magic, Fuzzlecheck); DOODs in real time; call sheet templates/auto-fill/send/track; budgeting (Dynamic Globals®); time cards with labor-agreement templates and payroll export; CO₂e budgeting (PEAR, MEDIA Carbon Calculator, KlimAktiv); project + production (Gantt) calendars; cast & crew hub (jobs, hiring); announcements/file sharing/comments; watermarking + view/edit/download tracking; advanced per-position permissions; TPN membership; GDPR/Azure; MovieLabs OMC-based API; 10 languages.
- Testimonial on the TV page from a line producer at a TV production company (" administering and collaborating on all aspects involved in a film project").

### Dramatify (evidence layer: A — direct official observation)

- Self-labels: "The Powerful Toolbox for Film, TV, and Video Production"; homepage hero workflows: general production, **multi-camera production ("From concept to live broadcast")**, drama production, sports, children's programming, non-fiction. Workflow pages: Film & Drama, Entertainment, Sports, Talk Shows & Current Affairs, Factuals & Documentaries, Children's, Branded content, Broadcasting & live streaming. Plans up to Enterprise ("companies & broadcasters").
- **Episodes & series** (help article "Working with Episodes and Series", fetched directly):
  - Episode functionality is a production-level toggle, activated at project setup or later ("Scripts & Episodes" sidebar); converting a multi-episode project back to a feature requires deleting all episodes (and their data) but one — the structures are mutually exclusive containers.
  - "The many uses for episodes": any project with multiple episodes; **TV series produced in blocks**; adding management/technical info to script/rundown headers; feature productions with additional content (promos, behind-the-scenes documentaries); storyboarding complex sequences (AV scripts); storing multiple script versions.
  - **Episode record**: title (only required field), episode/project code, synopsis, director, producer, archive ID (for external archiving systems), team assignment, technical specifications in the **episode header**.
  - **Episode production periods**: dated periods per episode; two stated advantages: (1) for productions with many episodes produced consecutively (stated examples: **a daily talk show or telenovela**) they identify current episodes; (2) periods show in the Production Planner where custom periods tie to episode/production periods. "Copy dates" moves periods forward for subsequent episodes.
  - **Scripts and rundowns attach to episodes**: add or copy a drama screenplay, AV script, or multi-camera live/studio rundown; "You can mix script types in the same production — **one script per episode**."
  - **Hide produced episodes**: for "producers of daily programming and long series," produced episodes can be hidden from view to unclutter the UI; hidden episodes remain reachable and marked.
  - **Teams**: up to 5 teams shooting at the same time, each with its own call sheet; default team if none configured.
- **Rundown suite** (homepage + help index): "World-class Rundowns — customise your multi-camera rundowns with flexible setups and enjoy **automatic cue cards** for flawless rehearsals and live productions"; 4 rundown views; script view formatting; access rights in the rundown; notifications/update log/**live edits**; integrations: **CuePilot** (vision mixing — "the main choice for the European Song Contest"), **AutoScript/AutoCue/MOS teleprompters** sync, **SPX Graphics** (design → content → playout).
- Full production machinery (homepage + help index): budgeting (top sheets, account numbers/sub-accounts, estimate column, multi-currency, Movie Magic Budget import, budget lock, copy from previous production, commissioner/company budget templates, CSV/Excel/Google Sheets export); script breakdown (scene items & scene elements, breakdown report, animals); shooting scheduling (stripboards: **Story Order stripboard**, **Running Order stripboard & report**; scene/segment/production times; unit/team assignment to scenes); Day Planner & Day List (daily schedules, print, calendar import); **DPRs** mentioned (semi-automatic call sheets "from screenplay import to semi-automatic call sheets and DPRs!"); call sheets (semi-automatic — "call sheets almost write themselves", for print and mobile; watermarking; archived call sheets); cast & crew management (personal/contact info, food prefs, allergies, time sheets, contracts); character management (auto-lists, statistics, booking sheets); sets/scenography (auto set lists, 3D files, scene items, continuity); locations (location bank, maps, automatic weather); wardrobe/makeup/hair with realtime updates; Story Shelf (plan/store/bounce scenes); Production Planner (Gantt, production periods); production dashboard "across productions"; **Resource Booking** (company-wide booking of staff, team, crew and cast); docs & resources sharing; food list/catering management; children & minors handling; free read-only access for cast & crew.
- Pricing: Free (3 active users, basic drama & documentary pre-production) → Bronze/Silver/Gold/Platinum → Enterprise for companies & broadcasters; education plans.

### Filmustage (evidence layer: A — direct official observation)

- Self-labels: "The Complete AI Pre-Production Platform"; content scope badge: "🌍 Any Language & Format 🎬 **Films, Series & TV Shows** 📱 Short & Vertical Dramas 🎙️ Podcasts & Treatments 🤖 AI-Powered"; "Trusted by 45,000+ filmmakers, from indie to major studios."
- Machinery (all per-script in observed material): AI script breakdown (auto-tag cast/props/locations/VFX/wardrobe, element mentions linked across the script, human confirmation); professional stripboard + drag-and-drop calendar; AI Production Agent ("analyzes risks, optimizes shooting days, executes structured changes with preview and approval"); time estimates; real location tagging; workload balancing; conflict detection; DOOD reports and call sheets auto-update; budget auto-generated from breakdown/schedule with fringes/deductions; VFX breakdown; storyboards synced to script scenes; live script annotations with per-department layers; call sheets auto-transformed from schedule; script sides assembled from the schedule with QR version codes, call sheet + sides bundled as one PDF; team access per feature (None/View/Edit/Full), team chat; SOC 2 Type II, TPN, forensic watermarking, "we do not use your data for training."
- Integrations: Movie Magic, Gorilla Scheduling, Final Draft.
- Episodic depth on the observed page: series/TV shows are named content scope; testimonial from "a film and TV Line Producer"; Hall of Fame lists TV series produced with the product (e.g., The Gentlemen/Netflix, Masters of the Air/Apple TV+, Gangs of London/amc+, Salem S2/DStv). No explicit episode-container machinery observed at this page's depth — recorded as an uncertainty, not assumed.

### StudioBinder (evidence layer: A — direct official observation)

- Page title: "**Video, TV & Film Production Management Software** | StudioBinder"; pipeline: Write → Breakdown → Visualize → Plan → Shoot.
- "**Episodic Structure**" is a named platform feature in "The complete video production platform" list (alongside Title Page Designer, Script Outlines, Script Versions, Custom Breakdown Categories, Advanced Scheduling Features, Call Sheet Templates...); the feature image is literally named "Video and TV Episodic Structure". Detailed episodic machinery is not described on the fetched page — recorded as an uncertainty.
- Machinery: screenwriting (industry format, revision colors, versions) or AV scripts/two-column; breakdown ("tag scene elements... props, set dressing, costumes, equipment, VFX"); stripboards with auto sorting (location, time of day) and alternate schedules; script sides (filter by scene number/character/location); reports (breakdown summary, element lists, shooting schedules, DOOD); contacts integrated across features and transferable between projects; production calendars; task boards; media library/file sharing; call sheets (auto-filled with weather/location/cast/nearest hospital, private notes per recipient, email + text distribution, delivery tracking with view counts and timestamped confirmations, resend/updates).
- Customers: brands/enterprise (ESPN, CBS Interactive, NBCUniversal, Blizzard, Spotify...). No budgeting module in the feature lists (consistent with the film pass observation).

### Scenechronize (evidence layer: — unreachable)

- Root fetch returned a cookie/browser gate (© 2007–2009 Entertainment Partners). No content usable. Recorded as attempted-and-abandoned per the network-restriction rule; the US professional episodic tier is therefore covered indirectly (the sampled cloud products' own testimonials and project lists reference episodic TV production) and all professional-tier-specific claims are withheld.

## Cross-product Comparison

| Structure | Yamdu | Dramatify | Filmustage | StudioBinder |
|---|---|---|---|---|
| Production/series container of record | ✓ ("single source of truth" projects) | ✓ (production = series container with episodes) | ✓ (project) | ✓ (projects) |
| Episodes as first-class objects | ✓ (episode hub; plot per episode; arcs link steps to episodes) | ✓ (episode records: header, specs, periods, teams; one script per episode; hide produced) | content scope ("Series & TV Shows"); containers not observed | ✓ feature named "Episodic Structure"; details not observed |
| Season machinery | ✓ (new-season data import; keep actors/locations/sets/costumes consistent per season) | — (not observed; episodes + copy-dates periods instead) | — | — |
| Episode/block access rights | ✓ (per episode or per block) | ✓ (access levels; per-user role access; rundown access rights) | ✓ per-feature (None/View/Edit/Full) | — (not stated) |
| Script per episode (screenplay import/sync) | ✓ (FD/PDF per episode, version by version) | ✓ (drama screenplay per episode; Final Draft/.fdx sync) | ✓ per script | ✓ (write or import FD/PDF/Fountain/TXT) |
| Rundown/segment script type (multi-camera) | — | ✓ (multi-camera live/studio rundowns; 4 views; cue cards; live edits; CuePilot/teleprompter/SPX sync) | — | — (AV scripts only) |
| Scene/segment → shooting-day schedule (stripboard) | ✓ (drag-drop assembly; schedule import) | ✓ (Story Order + Running Order stripboards; scene/segment times; multi-team scenes) | ✓ (stripboard + calendar; AI optimization) | ✓ (auto-sort stripboards; alternate schedules) |
| Breakdown with element categories | ✓ (AI suggestions + confirm) | ✓ (scene items/elements; breakdown report; partial departmental access) | ✓ (AI auto-tag + confirm) | ✓ (element tagger; custom categories) |
| DOOD / production reports | ✓ (real-time DOODs) | ✓ (cast DooD; DPRs stated; breakdown reports) | ✓ (DOOD auto-update) | ✓ (DOOD reports) |
| Call sheets generation + distribution tracking | ✓ (templates, auto-fill, send & track) | ✓ (semi-automatic; print + mobile; watermarking; archived) | ✓ (from schedule; QR-coded sides bundle) | ✓ (auto-filled; email/SMS; per-recipient tracking) |
| Multi-team simultaneous shooting | — (not stated) | ✓ (up to 5 teams, own call sheets) | — | — |
| Long-run / daily programming handling | — (not observed) | ✓ (episode production periods for daily talk shows/telenovelas; hide produced episodes) | — | — |
| Series-wide continuity (recurring people/sets/locations/costumes) | ✓ (season import keeps assets consistent) | ✓ (persistent character/wardrobe/makeup/set/location records within production; location bank) | — (not observed) | ✓ (contacts transferable between projects; not series-specific) |
| Budget estimating | ✓ (Dynamic Globals®) | ✓ (full budgeting; Movie Magic Budget import) | ✓ (auto from breakdown/schedule) | ✗ (no module in feature lists) |
| Time cards / payroll export | ✓ (labor-agreement templates) | ✓ (time sheets in cast/crew records) | ✗ | ✗ |
| Collaboration / cross-production dashboard | ✓ (comments, announcements, file sharing) | ✓ (dashboard across productions; resource booking company-wide) | ✓ (team chat, per-feature access) | ✓ (task boards, calendars) |
| Distribution security | ✓ (watermarking; view/edit/download tracking; TPN) | ✓ (watermarking screenplays & call sheets; access rights) | ✓ (SOC 2, TPN, forensic watermarking) | ✓ (call-sheet delivery tracking) |
| AI assistance | ✓ (breakdown suggestions) | ✓ (AI services for development) | ✓ (AI agent executes changes with approval) | — (not in sampled pages) |
| Deployment | Cloud SaaS | Cloud SaaS | Cloud SaaS | Cloud SaaS |
| Content breadth marketed | Film, TV Series, Commercial, Documentary, unscripted | Drama, entertainment/live, sports, talk/current affairs, factuals, children's, branded | Films, series & TV shows, short/vertical dramas, podcasts | Video, TV & film; also corporate/new media/photoshoots |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the leaf stops being recognizable as TV Production Management (from the TV lens of the shared production-management machinery):

1. **The series/show production as the container of record** — one persistent identified TV production (a series, format, or show) that outlives any single episode, holding its people, plan, documents, and (where present) budget. Remove → disconnected per-episode point tools.
2. **The episode as the recurring unit of production and delivery** — the production's work is organized as a sequence of episode instances; each episode carries its own script or rundown, its own planning and daily paperwork, and the production machinery repeats per episode across the run (including multi-team block shooting and long-run/daily cycles as common realizations). Remove → a single finite production: this is exactly the Film Production Management pole.
3. **The script-derived scene/segment as the atomic planning unit, arranged into shooting days** — per episode, the unit of planning derives from the script or rundown (scenes with script day/location/INT-EXT/cast, or rundown segments), organized into shooting days on the stripboard tradition. Remove → generic project/task management or an episode list manager.
4. **The daily operational dispatch to the production community** — the per-shooting-day call sheet carries the plan to the people executing it, with distribution and acknowledgment. Remove → planning-only software; the management loop never closes.

Jointly-held load-bearing checks: 1 alone = generic project container; 2 alone = an episode list; 3 alone = scheduling tooling (the sibling slice); 4 alone = a messaging tool; 1+3+4 without 2 = Film Production Management's definition; 2+3+4 without 1 = scattered episodes with no series memory.

Historical check (§24 pattern): the pre-software episodic TV production office satisfies this core — per-episode scripts and rundown boards, paper stripboards per episode/block, typed and distributed call sheets, series continuity books (recurring cast, standing sets) kept in the production office; block shooting and multiple units predate software; long-run daily shows predate software. Desktop-era products (Gorilla/Movie Magic heritage, corroborated third-party in the film pass) satisfy the same core without cloud or AI. The core is therefore not an artifact of the current cloud-SaaS generation.

### L1 — Common Mature Structure

Very common across the sample but not required to recognize the Type:

- **Script breakdown with element categories** per episode/scene (all four products), with element catalogs/scene-item records.
- **Cast & crew records** with roles/departments; recurring cast and characters managed across the series (Dramatify's character management; Yamdu's cast hub).
- **Locations and sets records** — standing sets and reused locations across episodes; location banks with maps/weather.
- **Production reports** — day-out-of-days per day, breakdown sheets, sides; DPRs stated by one product; one-liners in the family (film pass).
- **Call sheet templates, customization, and distribution tracking** (all four; per-recipient confirmation states in two).
- **Production calendar / planner** spanning episodes, seasons, prep-shoot-post; episode production periods.
- **Series-wide continuity**: reuse of people/locations/sets/costumes data across episodes and seasons (Yamdu's season import; Dramatify's persistent records) — strongly indicated for TV but realized differently per product.
- **Collaboration and scoped access** — per-feature/per-role permissions; distribution security (watermarking, view/download tracking).
- **Budget estimating** — common but NOT universal (absent from StudioBinder's feature set, consistent with the film pass); dedicated budgeting products exist in the family.
- **Multi-team support** for block/multi-unit shooting (Dramatify explicit; others not stated).

### L2 — Variant / Optional Structure

Depends on segment, geography, workflow, era, deployment:

- **Content-type poles**: scripted episodic drama (screenplay-driven, scene-based) vs studio/entertainment formats (rundown/segment-driven, multi-camera, live) vs unscripted/reality vs talk/current-affairs vs children's vs sports/factual. The machinery family is shared; the script format is the tuning knob.
- **Rundown suite (multi-camera live/studio)** — rundown views, cue cards, live edits, vision-mixer/teleprompter/graphics integrations — evidenced in one product only (Dramatify) → optional, product-specific-leaning; the same product's own drama pole works without it.
- **Episode-container depth**: explicit episode objects with linked documents and production periods (Yamdu, Dramatify) vs episodic content scope with per-script processing (Filmustage observed) vs named feature with unobserved depth (StudioBinder).
- **Season machinery** (season roll, data re-import, continuity selection): observed in one product → variant.
- **Long-run/daily programming patterns** (consecutive episode periods, hide-produced-episodes): one product → variant.
- **Per-episode/per-block access granularity**: one product explicit → variant (per-feature/per-role access is common).
- Regional/regulatory posture: European co-production machinery, multi-language, broadcaster clientele (Yamdu, Dramatify) vs US-centric tiers.
- AI posture: manual tagging vs AI-suggested breakdown vs AI agent executing schedule changes (era-typical).
- Office extensions: time cards with labor-agreement templates and payroll export; sustainability/CO₂e budgeting (Yamdu) — optional layers (consistent with film pass).
- Packaging/deployment: all-in-one cloud suite (dominant today) vs desktop-era specialist pairs (film pass heritage); AI-first packaging.

### L3 — Vendor-specific (research notes only)

- Dramatify: 4-rundown-views naming; CuePilot / AutoScript-AutoCue-MOS / SPX Graphics integrations; Story Shelf; AV scripts; Running Order stripboard; food list/catering module; children & minors handling; "hide produced episodes"; archive-ID field on episodes; free read-only cast/crew access; named plan tiers.
- Yamdu: Dynamic Globals® (branded budget linkage); named CO₂e calculators (PEAR, MEDIA Carbon Calculator, KlimAktiv); MovieLabs OMC-based API; Fuzzlecheck schedule import; Showbiz Budgeting export; Lockit Script sync; 10-language UI.
- Filmustage: "AI Dude" production agent; QR-coded sides for on-set version confirmation; call-sheet+sides single-PDF bundling; synopsis generation; per-feature None/View/Edit/Full access naming.
- StudioBinder: "Episodic Structure" feature naming; boneyard/alternate-schedule terminology (film pass); per-recipient call-sheet confirmation dashboard; photoshoot/corporate adjacency.

## Vendor-specific Findings

See L3. None promoted into the canonical model. The most consequential L3-adjacent question — whether rundown machinery belongs in the Type at all — is resolved as optional/variant (single-product evidence; the drama pole of the same product does not need it).

## Rejected Findings

- **"TV Production Management = Broadcast/Newsroom rundown system"** — rejected. Newsroom/broadcast systems center on news rundowns, ingest-to-air, and transmission operations; this Type centers on the production office machinery (people, plan, breakdown, schedule, dispatch, money-planning). Rundowns appear here only as one product's optional suite for studio/entertainment formats.
- **"TV production management is just film production management with more projects"** — rejected as *nothing more*: episodic organization adds real structure — recurring delivery units, series/season continuity of people and assets, per-episode access and periods, long-run cycle handling. But it is also rejected as *something entirely different*: the underlying pipeline and object set are shared with film. Net: one machinery family, two organizing structures.
- **"Every TV product models seasons explicitly"** — not supported (one product) → variant.
- **"Multi-camera rundowns are definitional"** — rejected (single-product evidence).
- **"Budgeting is definitional"** — rejected (StudioBinder absence, consistent with the film pass).
- **"Episodic support requires cloud/AI"** — rejected by the historical check (paper-era and desktop-era episodic production satisfies the core).

## Boundary Findings

- **vs Film Production Management** — thinnest boundary, same machinery family. The seam is the **container structure**: film organizes one finite production (script → one plan → one run of shooting days); TV organizes a recurring sequence of episode instances inside a series/show container, with continuity machinery across episodes/seasons and long-run cycle handling. Joint-review flag from the film pass discharged: **keep-both** — two leaves, one family, each documented from its own lens, cross-referenced. Test: make the production's unit of work a recurring episode sequence inside a persistent series container → this Type; collapse it to a single finite production → Film Production Management.
- **vs Production Scheduling / Call Sheet Application** — the sibling is the capability slice of this Type (and of film's): the scheduling spine + daily mobilization chain (scene/segment → day → schedule → call sheet) without the surrounding production-office objects (episode/series containers, breakdown catalogs, people hub, budget, security, season continuity). Seam ratified from this side, as that pass's forward flag requested. Suites bundle the slice as a module — packaging, not identity.
- **vs Theater Production Management** — seam held as ratified from the theater pass's side: the shared family (container/company/schedule/paperwork) splits on the delivery unit. Theater's center is the live performance run (rehearsal process → repeated scheduled performances of a fixed show; rehearsal/performance reports). TV's center is capture: episodes shot on days (or studio shows produced to air). TV's recurring unit (the episode) is a *production* that is itself shot/produced; theater's recurring unit (the performance) is an *execution* of an already-built show. Removing episode-production semantics in favor of performance-run semantics → theater.
- **vs Broadcast Management System / Newsroom Management System** — those Types govern transmission/playout operations and newsroom rundown-to-air workflows (station-side). This Type governs the production office that makes the content before it reaches transmission. Overlap edge: a production platform with a rundown suite that syncs to playout/teleprompter systems (Dramatify) — the sync seam, not the same center.
- **vs Production Accounting Platform** — planning vs actuals: this Type estimates and plans what will be shot per episode; accounting platforms record what was spent (actuals, payroll, cost reports). Budget estimating stays here as a common module; deep money-tracking belongs to the sibling (consistent with the film pass).
- **vs Script Breakdown Application** — breakdown is one stage of this Type's per-episode pipeline; a standalone breakdown tool stops at tagging/catalogs.
- **vs Casting Platform / Audition Management** — talent discovery/selection vs managing the already-chosen recurring cast inside the production. Casting output is an input here.
- **vs Media Asset Management / MAM** — MAM governs recorded media/assets; this Type governs the plan and people that produce them (episode footage lands in MAM after wrap).
- **vs generic Project Management Application** — script/rundown-derived units with production semantics (day breaks, call times, company moves, DOODs, episode periods) and industry-standard documents are what generic PM lacks.

**"Remove what to become the other Type" tests:**
- Remove the recurring-episode structure (keep one finite production) → Film Production Management.
- Remove the series container, budget, people hub, security; keep schedule+call sheets → Production Scheduling / Call Sheet Application.
- Replace capture semantics with live-performance-run semantics → Theater Production Management.
- Replace production-office planning with rundown-to-air/transmission operations → Broadcast/Newsroom territory.
- Replace planning with actuals/payroll → Production Accounting Platform.
- Remove scene/segment-based planning and production documents → generic project management.

## Uncertainties

- Scenechronize (US professional episodic standard) unreachable this pass; the professional-pole episodic tier is covered only indirectly. No claims are made about it.
- Filmustage's and StudioBinder's episodic-container depth is unverified (content scope / feature name observed; internal episode-object machinery not observed). The L0 episode-structure leg rests on Yamdu and Dramatify at full depth; it is treated as the TV lens' defining structure regardless, because episodic organization is inherent to TV production (and satisfied paper-era), while its software realization depth varies.
- Rundown machinery's market coverage beyond Dramatify is unknown (single-product evidence → held optional).
- Whether the earliest digital episodic scheduling products shipped call-sheet generation is unverified; the call sheet's paper-era existence is industry practice, not directly sourced.
- DPR (end-of-day report) machinery: stated by one product; depth unverified → held common-leaning-optional, not definitional.
- Exact numeric limits (episode counts, team caps, plan gates) deliberately not stated.

## Final Synthesis

TV Production Management is the production office's system of record for making episodic television. It shares one machinery family with Film Production Management — script/rundown-derived units broken down, arranged into shooting days, and dispatched daily through call sheets — but its defining structure is episodic: a persistent series/show container whose recurring unit of production and delivery is the episode, each carrying its own script or rundown, plan, and daily paperwork, with continuity of people, sets, locations, and assets across episodes and seasons, and with the cycle repeating through block shooting, multiple units, and long-run daily programming. Around that core, mature products add breakdown catalogs, cast/crew and character records, locations/sets, production reports, calendars spanning episodes, scoped access and distribution security, and commonly budget estimating; studio/entertainment formats add rundown-driven variant workflows (one product in sample). The leaf is held as one of two sibling lenses over one machinery family (film = single finite production; TV = episodic recurring production), with the scheduling/call-sheet leaf as the shared capability slice and theater split off on the live-performance delivery unit. Boundary resolutions recorded in STATUS.md.
