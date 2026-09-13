# TV Production Management

## Overview

A **TV Production Management** application is the production office's system of record for making episodic television. It organizes a series or show as a persistent production whose recurring unit of work is the episode: each episode carries its own script or rundown, is broken down into the scenes or segments it needs, is arranged into shooting days on a schedule, and is dispatched day by day to the cast and crew through call sheets — with the whole cycle repeating across episodes, blocks, and seasons, and with people, sets, locations, and other assets carried forward from episode to episode.

The defining core is small:

```text
Series / Show (the production of record)
└── Episodes (the recurring unit of production and delivery)
    └── Script or rundown, broken down into scenes/segments
        └── Shooting schedule (scenes arranged into shooting days)
            └── Daily dispatch (call sheets to the people executing the plan)
```

Everything else commonly bundled with the category — breakdown catalogs, budgeting, season-continuity tools, calendars, multi-camera rundowns, AI-assisted breakdown — is standard or optional structure that makes the core practical, not what makes the software what it is. The same core was practiced by pre-software episodic production offices working from per-episode scripts, paper stripboards, typed call sheets, and continuity books.

When the recurring episode structure collapses into a single finite production, the software becomes film production management. When the focus shifts to what was actually spent, it becomes production accounting. When the center becomes rundown-to-air and transmission operations, it is broadcast/newsroom territory.

## Users & Context

The primary users are the people who run the production office of an episodic production:

- **Line producer / unit production manager** — owns schedule and budget across episodes; watches day-out-of-days and cost-facing views where present.
- **1st assistant director** — builds and maintains each episode's shooting schedule; owns the shape of each shooting day; coordinates block shooting and multiple units.
- **Production coordinator / production office staff** — maintains cast, crew, and character records; generates and distributes call sheets and episode paperwork; tracks acknowledgments.
- **Producer / showrunner's production team** — oversees the whole series: story arcs, episode flow, approval of changes, reporting to financiers, broadcasters, or commissioners.

Secondary users consume what the system produces:

- **Department heads** (camera, art, wardrobe, hair & makeup, VFX) — read breakdowns, element lists, and sides for their departments; in some products granted partial access to just their department's material.
- **Cast and crew** — receive call sheets and schedules, confirm receipt, and read scripts or rundowns on mobile; recurring cast persist across episodes.
- **Executives, co-producers, and commissioners** — in some products, given oversight views across productions and episodes without editing rights.

The context differs from a single film in one structural way: the work is a **running cycle, not one finite push**. An episodic production office lives with the material for months or years — episodes in different states at the same time (one shooting, one in prep, one in rewrite), teams shooting in parallel blocks, and for daily or long-run programming a cadence of new episodes every day or week. The system is therefore used continuously: scheduling next episodes while tracking current ones, reusing last season's data while preparing the next.

## Core Model

### The Defining Core

**Series / show (the production of record).** One persistent identified TV production — a series, format, or show — that outlives any single episode. Scripts, plans, people, documents, and (where present) budgets attach to it. The container is what makes the work a *series* rather than a pile of unrelated shoots: teams, characters, sets, locations, and paperwork conventions persist inside it, and finished episodes remain part of its record.

**Episode.** The recurring unit of production and delivery. An episode is a bounded, individually identified production instance inside the series: it carries its own script or rundown, its own planning and daily paperwork, commonly its own metadata (title or code, synopsis, director, producer, technical specifications) and its own production period. The machinery of the system — breakdown, scheduling, dispatch — runs once per episode and repeats across the run. In mature products episodes are explicit containers: documents link to them, access rights scope to them (individually or by block of episodes), production calendars place them, and produced episodes can be set aside as the run advances. Whether episodes are modeled as such explicit containers, or simply as successive productions sharing a workspace, varies by product — episodic organization itself is the invariant, not any one software realization of it.

**Episode script or rundown.** The content basis of each episode. Scripted television works from screenplays imported or written per episode and broken down into scenes; studio and entertainment formats work from rundowns — ordered segment lists for multi-camera productions — which at least one platform in this category treats as a first-class script type alongside screenplays, attachable to episodes in the same production. Either way, the script or rundown is the input that seeds the episode's planning.

**Shooting schedule (per episode).** The plan of record for each episode: scenes or segments extracted from the script or rundown and arranged into an ordered sequence of shooting days (the stripboard tradition), with day breaks, banners for non-shooting events, and omitted material set aside rather than deleted. Ordering follows production logic — locations, cast availability, interior/exterior, day/night — by hand or by automatic sorting. In block-shot series, several episodes' scenes interleave across shared shooting days; in multi-unit productions, teams shoot in parallel, each with its own schedule and call sheet.

**Daily dispatch.** The mechanism that closes the loop for every shooting day of every episode: the system generates a call sheet from the schedule — who is called, when, where, with what schedule, weather, maps, contacts, and safety information — and distributes it to the production community, tracking whether each recipient received, viewed, and confirmed it.

### Standard Capabilities

Mature products commonly add these structures around the core:

- **Script breakdown per episode** — tagging the elements each scene or segment needs (cast, props, wardrobe, set dressing, equipment, effects) under categories; per-scene breakdown sheets and a cumulative element catalog. May be manual, AI-suggested with human confirmation, or automatic.
- **Cast, crew, and character records** — a people database with roles, departments, and contacts; character management spanning the series (recurring cast, per-character wardrobe/makeup information), because the same characters recur across episodes.
- **Locations and sets** — location records with maps and notes, and standing-set records with scene items and continuity, reused across episodes and seasons.
- **Series and season continuity** — carrying people, sets, locations, and wardrobe data forward: reusing prior-season data when a new season starts, keeping main actors, locations, sets, and costumes consistent; location and asset libraries that outlive single episodes.
- **Production reports** — day-out-of-days reports per shooting day, breakdown sheets, script sides for the day's scenes; some products also generate daily production reports and one-liner schedules.
- **Episode production periods and calendars** — dated periods per episode surfaced on a production calendar or planner, so the office can see at a glance which episodes are current; whole-series timelines from development through shooting.
- **Multi-team support** — parallel shooting units, each with its own schedule and call sheet.
- **Collaboration and scoped access** — shared access with per-feature, per-role, and (in some products) per-episode or per-block permissions; distribution security such as watermarking and per-recipient view/download tracking; oversight views for executives and commissioners.
- **Budget estimating** — a budget built from breakdowns and schedules, commonly linked so schedule changes surface cost consequences. Common but not universal: some all-in-one suites ship no budgeting module, and dedicated budgeting products exist in the wider family. Deep cost tracking and payroll belong to production accounting software.

### One Structure, Many Implementations

```text
Concept:  Episode as recurring unit
Realizations:  explicit episode containers with linked documents and production periods;
               episodes as successive projects inside a shared workspace;
               episodic content handled script-by-script

Concept:  Content basis of an episode
Realizations:  imported or in-product screenplays (scene-based);
               multi-camera rundowns / segment lists (studio and live formats);
               image-based AV scripts (short-form, branded content)

Concept:  Season continuity
Realizations:  new-season import from company data with selected carry-over;
               persistent character/location/set records within the series;
               per-project transfer of contacts and assets
```

## How It Works

The typical lifecycle runs at two levels: the series level (structure and continuity) and the episode level (the repeating production cycle).

**1. Create the series production and structure its episodes.**
Open the series/show container. Turn on episodic organization and create the episode set — one entry per episode with its title or code, synopsis, responsibility, and (commonly) production period. For a continuing series, some products let the office seed the new season by importing data from the previous one, choosing which people, locations, sets, and wardrobe to carry forward.

**2. Bring in each episode's content basis.**
For each episode, import or write the screenplay, or build the rundown for a studio format. Scenes or segments are extracted automatically and appear ready to break down and schedule. One script or rundown per episode is the normal discipline; mixing script types across a production is supported by some products (e.g., a screenplay for the episode plus a rundown for a studio segment).

**3. Break down each episode.**
Tag the elements each scene or segment needs — recurring cast, props, standing sets, wardrobe, effects — under categories. Because characters and sets recur, breakdowns draw on series-level records, and new elements accumulate into the series' catalogs.

**4. Build the shooting schedule per episode — and across blocks.**
Arrange scene strips into shooting days for each episode, or interleave several episodes' scenes into shared block-shooting days. Insert day breaks, banners, and company moves; set omitted scenes aside; duplicate schedules to compare scenarios. In multi-unit productions, assign scenes to teams, each team carrying its own schedule.

**5. Manage the people.**
Maintain cast, crew, and character records at series level; attach cast to scenes so availability views and day-out-of-days reports derive correctly across episodes. Scope access so that, for example, a department head sees their department's material and a commissioner sees oversight views only.

**6. Dispatch each shooting day.**
Generate the call sheet for the next shooting day from the schedule — scenes, call times, locations with maps, weather, contacts, safety information — customize it, send it by email and text, and track per-recipient delivery and confirmation; resend updates when the plan changes.

**7. Absorb change across the running cycle.**
Scripts are rewritten mid-season; scenes move between episodes; cast availability shifts. Changes propagate downstream — a revised script re-seeds the episode's scenes and breakdown, a moved scene updates the schedule, the affected call sheets, and the derived reports — and, in products with linked episode documents, a change to one document alerts the departments attached to the others. As episodes complete, they are closed out of the working view without losing their record.

**8. Roll the season.**
When a season ends, its data — people, locations, sets, costumes, budget structures — becomes the substrate for the next season's episodes. Where the product supports it, the office rolls the season by importing the prior season's data and selecting what to carry forward; otherwise the continuity is rebuilt from the series' persistent records.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Series overview / episode list

The primary entry surface for the production of record.

- the episode set with titles/codes, status or production periods, and the series' calendar
- primary actions: create/edit episodes, set production periods, open an episode's workspace, set produced episodes aside from the working view (where supported), roll a new season

### Episode workspace

The per-episode planning scope.

- the episode's script or rundown, its scenes/segments, its breakdown, its schedule, its documents
- primary actions: import/sync script, tag breakdown elements, build and reorder the schedule, generate documents

### Stripboard / shooting schedule board

The central per-episode (or per-block) planning surface.

- scene strips with attributes (page count, location, cast, elements), grouped into shooting days separated by day breaks, with banners for non-scene events
- primary actions: reorder strips, move scenes between days, insert day breaks and banners, omit/restore scenes, assign scenes to teams/units, duplicate the schedule, auto-sort, filter, export

### Script & breakdown view

- the episode script with tagged elements highlighted by category color; per-scene breakdown sheets and cumulative element lists
- primary actions: tag/untag elements, edit element details, standardize names, generate breakdown sheets

### Rundown editor (studio/entertainment variants)

- ordered segment list for a multi-camera production with per-segment content and timings; per-view layouts for different roles; live-editing with update logs during rehearsal and broadcast
- primary actions: add/reorder segments, set timings, choose view, push to connected systems (teleprompters, graphics, vision mixing) where integrated

### Call sheet builder & distribution dashboard

- the day's schedule, call-time grids, location and weather blocks, contacts, notes, safety information; per-recipient delivery states (sent / viewed / confirmed / undeliverable)
- primary actions: auto-populate from the schedule, customize, attach documents, send by email/SMS, track and resend

### People (cast, crew & characters)

- series-level records with roles, departments, contact details; character pages linking recurring cast to wardrobe/makeup/continuity information across episodes
- primary actions: add/edit people and characters, assign to scenes or departments, manage access

### Calendar / production planner

- the whole-series timeline: episode production periods, prep/shoot/post phases, arcs and milestones across episodes
- primary actions: place and adjust events, view episodes against the calendar, export

### Budget (where present)

- category-structured budget derived from breakdowns and schedules, with scenario comparison
- primary actions: generate from breakdown, adjust rates/fringes, compare scenarios

### Settings & access

- team members, per-feature/per-role/per-episode permissions, security options (watermarking, distribution tracking) where offered

## Important Rules / Behaviors

### The episode is the repeating unit

Breakdowns, schedules, call sheets, and reports are episode-scoped: the machinery of the system runs once per episode and repeats across the run. Products differ in whether episodes are explicit containers or successive projects, but day-to-day work is always anchored to a specific episode's plan.

### The schedule is the plan of record; documents derive from it

Call sheets, sides, day-out-of-days, and (where present) budget lines derive from the schedule and breakdown. Editing the plan updates its derivatives — automatically in some products, semi-automatically in others. The single-plan-of-record discipline is the organizing rule.

### Episodes are set aside, not destroyed

Produced episodes drop out of the working view but remain part of the series record (in at least one product via an explicit hide-and-restore mechanism). Deleted planning material is not the normal model on a running series.

### Series continuity is deliberate

People, sets, locations, and wardrobe persist across episodes and seasons because the content recurs. Products provide named mechanisms — season data import, persistent character/set/location records — to keep that continuity consistent instead of re-entering it per episode.

### Access is scoped to protect unreleased content

Episode material circulates to large temporary workforces before public release. Mature products treat watermarking, per-recipient tracking, and scoped access (per feature, per role, and in some products per episode or block of episodes) as structural. Oversight roles can monitor without editing.

### Long-run handling is a first-class concern

For daily and weekly programming, the system must separate current from finished work quickly (dated episode periods, hide-produced mechanisms) and accelerate repetition (copy dates forward, reuse templates and prior data).

### Block and multi-unit shooting are scheduling facts, not exceptions

Series television routinely shoots scenes from several episodes on one day, or runs several teams in parallel. The schedule and call-sheet model therefore has to support scene-to-episode attribution across shared days and per-team call sheets.

### Budget estimating is not cost tracking

Where budgeting exists, it projects what the plan will cost. Recording what was actually spent — actuals, payroll, cost reports — belongs to production accounting software, which may consume this system's plan as its starting point.

## Variants

Common shapes of the same Type:

- **Scripted episodic drama / comedy** — the screenplay-driven center: per-episode scripts, scene-based breakdowns and schedules, block shooting, season continuity. The market's core shape.
- **Studio & entertainment formats** — talk shows, variety, game shows: rundown/segment-driven production of multi-camera episodes, rehearsal-to-broadcast cycles, sometimes live; at least one platform provides a dedicated rundown suite with cue cards and broadcast integrations as an optional layer.
- **Unscripted / reality & factual** — episode structures over loosely scripted material; document and schedule machinery carries the load where scene breakdowns thin out.
- **Daily / long-run programming** — telenovela and talk-show cadences: many consecutive episodes, dated episode periods, hide-produced handling, heavy template reuse.
- **Children's programming** — episodic machinery with additional handling for young performers.
- **All-in-one cloud suite vs specialist pairs** — the dominant packaging is the all-in-one suite; desktop-era specialist scheduling/budgeting pairs persist from the film family's heritage.
- **AI-first platform** — automatic breakdown and schedule optimization with human approval, positioned on pre-production speed.
- **Regional posture** — European co-production machinery (multi-language, multi-country budgeting, broadcaster clientele) versus US-centric tiers; the professional US episodic tier is served by long-standing specialist tools whose documentation was not reachable in this research (see Sources).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Film Production Management | closest sibling | same machinery family over a single finite production rather than a recurring episode sequence inside a series container; sampled products largely serve both from one codebase |
| Production Scheduling / Call Sheet Application | capability slice | the scheduling spine plus daily mobilization (scene → day → schedule → call sheet) without the surrounding production-office objects: episode/series containers, breakdown catalogs, people hub, budget, security, season continuity |
| Theater Production Management | sibling, different delivery unit | theater's center is the live performance run (rehearsal process → repeated performances of a fixed show); TV's center is capture — episodes shot on days or studio shows produced to air |
| Broadcast Management System / Newsroom Management System | adjacent, station-side | govern rundown-to-air, ingest, and transmission operations; this Type governs the production office that makes the content before transmission. A production platform's rundown suite that syncs to playout systems is the overlap edge, not the same center |
| Production Accounting Platform | downstream sibling | records what was actually spent (actuals, payroll, cost reporting) instead of planning what will be shot per episode |
| Script Breakdown Application | upstream slice | stops at tagging and catalogs, without the schedule and dispatch loop |
| Casting Platform / Audition Management | adjacent, upstream | discovers and selects talent; this Type manages the already-chosen recurring cast inside the production |
| Media Asset Management / MAM | adjacent, downstream | governs recorded footage and media assets after wrap, not the plan and people that produce them |
| Project Management Application (generic) | structural contrast | plans abstract tasks, not script/rundown-derived units with production semantics (day breaks, call times, episode periods, day-out-of-days) |

The most important boundary is with Film Production Management: the underlying system is the same family, and the film/TV split is best understood as two organizing structures over one machinery — a single finite production versus a recurring episodic sequence with series-level continuity. The scheduling/call-sheet leaf is the capability slice both share.

## Representative Products

- Yamdu — European cloud production management platform with a dedicated TV Series line (episodes, seasons, blocks, per-episode access)
- Dramatify — TV-native cloud platform spanning episodic drama and multi-camera studio/entertainment formats, including a rundown suite
- Filmustage — AI-first pre-production platform covering films, series and TV shows
- StudioBinder — all-in-one cloud suite self-labeled for video, TV and film, with episodic structure support

Scenechronize, the long-standing professional episodic production tool (Entertainment Partners), is recognized as part of this market but could not be documented here: its site was not reachable from the research environment (see Sources).

## Sources

Research date: **2026-09-09**

- Yamdu — main site and TV Series audience page: https://www.yamdu.com/en/ , https://www.yamdu.com/en/for-productions/tv-series/
- Dramatify — main site and "Working with Episodes and Series" help article: https://dramatify.com/ , https://dramatify.com/faq/series-episodes
- Filmustage — main site: https://filmustage.com/
- StudioBinder — main site: https://www.studiobinder.com/

> Sourcing limitation: Scenechronize (Entertainment Partners) could not be reached — its site presents a browser/cookie gate and no operational documentation was accessible; no statements about it are made in this document. Entertainment Partners' Movie Magic family was likewise unreachable (consistent with the paired Film Production Management research of 2026-09-07). Episodic-container machinery is evidenced at full depth for Yamdu and Dramatify; for Filmustage and StudioBinder the episodic evidence is at content-scope/feature-naming level, and the document's claims are calibrated accordingly. Precise numeric limits, plan gates, and default settings are intentionally not stated.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary resolutions are recorded in the paired Research Notes.
