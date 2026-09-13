# Research Notes — Newsroom Management System

## Research Goal

Understand what a Newsroom Management System actually is as an Application Type: what the system of record for a news organization's *internal editorial operation* consists of, how work is planned, assigned, tracked, and assembled into the newsroom's scheduled output, and how this Type is separated from the adjacent News Publishing Type (already processed as `news-publishing-platform`) and from Broadcast Management, Content Planning, and generic project/task Types.

## Initial Boundary (hypothesis before research)

- Core use hypothesis: manage the newsroom's internal operation — forward planning (what will we cover), assignment (who covers it), production-status tracking, and (broadcast) assembly of rundowns for on-air shows.
- Likely nearest neighbors: News Publishing Platform (public output), Broadcast Management System (station business ops), Content Planning Platform (marketing content calendars), Production Scheduling / Call Sheet (film/TV production), Project Management Application (generic work), Media Asset Management (asset custody).
- Known market term mapping: in broadcast the category is historically the "Newsroom Computer System" (NCS) / NRCS; in print/digital it appears as "editorial planning" / "newsroom planning" software; at least one vendor literally names its product a "Newsroom Management System".
- Unknowns: whether assignment machinery is definitional or only common; whether the rundown is definitional or a broadcast-only realization; how far NRCS suites overlap the publishing Type.

## Research Questions

1. What are the core objects (story/planning item, task/assignment, rundown, slot, wire item, show, edition, platform)?
2. What is the canonical flow: plan → assign → produce → assemble → hand off?
3. What lifecycle/status structure does a work item carry?
4. What rules matter (deadline derivation, rescheduling, order/timing, permissions)?
5. Which capabilities are defining vs common vs broadcast-specific vs vendor-specific?
6. Where exactly is the seam with News Publishing Platform, and does the broadcast pole (NRCS driving playout) violate it?

## Representative Products (sampled)

| Product | Vendor | Pole | Customer level | Why sampled |
|---|---|---|---|---|
| Kordiam (formerly Desk-Net) | Kordiam (Desk-Net GmbH) | editorial planning-first (print/digital + broadcast digital teams) | regional/national newspapers (The Times, Handelsblatt), magazines, public broadcasters, comms teams | the clearest planning-first philosophy; rich official feature documentation; named lineage from the classic Desk-Net editorial planning tool |
| Dalet Pyramid | Dalet | story-centric converged news suite (planning + rundown + production + playout) | large multi-site broadcasters and news agencies; turnkey tier for small/mid operations | broadcast NRCS pole with modern story-centric architecture; official feature-level documentation |
| Dalet Galaxy five | Dalet | integrated NRCS + MAM + playout ("unified news operations") | large TV/radio/digital newsrooms | documents the classic integrated-NRCS framing (same vendor as Pyramid; treated as one vendor's product family, noted as sample limitation) |
| MOS Protocol (MOS Project) | industry body (150+ companies) | the vendor-neutral standard defining the Newsroom Computer System's role in broadcast | n/a (standard) | Tier-1 official definition of what an NCS is responsible for in broadcast (editorial information incl. playlists/running orders) |

Attempted but unreachable this pass (see Sources — access limitations): Avid iNEWS, AP ENPS, Octopus Newsroom, Ross Inception News (all canonical broadcast NRCS products), Wikipedia, web.archive.org. Evidence for the broadcast pole therefore rests on the MOS standard plus Dalet's official documentation, and assertion strength is calibrated accordingly.

## Sources

Fetched 2026-09-08 (all official):

- Kordiam homepage — https://kordiam.io/ (rebrand of Desk-Net confirmed; Capterra badge still shows "Desk-Net")
- Kordiam Content planning features — https://kordiam.io/content-planning-features
- Kordiam Task management — https://kordiam.io/task-management
- Kordiam Newsroom planning — https://kordiam.io/newsroom-content-planning
- Kordiam Broadcast newsroom software — https://kordiam.io/broadcast-newsroom-software
- Kordiam Integrations — https://kordiam.io/integrations
- Kordiam Topics — https://kordiam.io/topics
- Dalet News Organizations (Unified News Operations) — https://www.dalet.com/solutions/news/
- Dalet Pyramid product page — https://www.dalet.com/products/pyramid/
- Dalet Galaxy five product page — https://www.dalet.com/products/galaxy-five/
- Dalet blog "Rundown Redefined: Dalet's Story-Centric News Production Approach" — https://www.dalet.com/blog/rundown-story-centric-news-production-approach/ (official vendor essay, 2024-10-15)
- MOS Project Welcome + FAQ — https://mosprotocol.com/ , https://mosprotocol.com/mos-faq/

Cross-referenced (not refetched): `applications/news-publishing-platform.md` + its research (processed 2026-09-08, Arc XP / Brightspot / Superdesk / Thunder / Quintype docs fetched that pass) — establishes the ratified seam "planning vs publication" and the fact that publishing suites bundle planning surfaces as packaging, not identity.

Failed/abandoned sources (per network-restriction rules; 1–2 failures each, then abandoned):

- Avid iNEWS: avid.com/iNEWS (404), avid.com/resource-center/products/iNEWS (404), docs.avid.com (login/JS wall), web.archive.org attempts (timeouts ×2)
- AP ENPS: ap.org/en-us/products/enps.html (404), enps.com (transport error)
- Octopus Newsroom: octopusnewsroom.com with and without www (transport errors ×2)
- Ross Inception News: rossvideo.com product URLs (404 ×2)
- Wikipedia "Newsroom computer system" (timeouts ×2)
- Superdesk readthedocs planning page (404; docs index fetched — server-side technical docs only; Planning module documentation not directly verified this pass; index points to a User Manual PDF not fetched)

## Product A — Kordiam (formerly Desk-Net)

Evidence layer: A (direct observation, official site) unless noted.

### Key observations

- Positioning: "Plan stories, assign tasks and track publishing across every platform, all on the same tool. Built for newsrooms and comms teams." Teams pages: Newsrooms, Broadcasters (digital news teams), Magazines, Communications.
- **Story List** (central surface): "coordinate dozens or hundreds of stories each day"; per story visible: which platforms it runs on, workflow status, publication time, who is working on it, delays. "Keep editorial tasks on track so you publish at the right time, every time."
- **Story Card** (item detail): deadlines, publishing channels, attachments, update history, locations and deliverables in one view; collapsible side panel with attachments, versioning, location; "from pitch to publication".
- **Task management / assignments**: "Every assignment is tied to its story, so you always have the context you need"; Tasks Overview for coordinating editors: all teams' tasks, what's behind; custom task fields, custom task statuses, filtering/sorting/grouping per team (photo, video, graphics); "Deadlines derived from the publication date"; separate appointments for the assignee ("the event may start at 3:00, but the photo team gets there at 2:30" — vendor's own illustrative example); photo tasks carry a location and can be filtered by the event date, not just deadline; content uploader connected to tasks.
- **Short-term planning**: multiple days or issues side by side, "even across channels with different publication frequencies"; drag-and-drop; "Move your stories in Kordiam to the next day or time slot with a single click" for breaking news; in-list editing.
- **Monthly calendar view**: high-level overview; "spot the gaps in your plan"; filters by platform, status, etc.
- **Undated stories**: scheduled and undated stories shown together; editors review undated items and "choose which to include within your publication schedule".
- **Story templates**: editors define fields, defaults and production tasks per desk; "reporters pick a template and fill in only what's needed".
- **Custom fields**: audiences / user needs; saved and shared views.
- **Topics / campaigns**: structural overview of core topics and strategy; multi-level breakdown; briefings, hashtags, colors; "Orchestrate campaigns or major news coverages — from elections to marketing campaigns"; drag-and-drop an entire coverage/campaign (with all its content) to new dates; filter campaign content by persona/audience; promote sub-topic to key topic.
- **Staff coordination** (broadcast page): availability timeline ("Who's available? And who's too busy to assign a task?"); assign users to shifts; calendar sync.
- **Integrations** (the handoff leg): "Take a story from idea to CMS" — WordPress, Drupal, Livingdocs, Aptoma DrPublish ("exchanges story data between Aptoma's text editor … and Kordiam"), WoodWing, Purple, CUE, Glide, InterRed, Arc XP, EidosMedia (blog posts); **wire feeds** (listed among data-feed integrations); email import; event feed import; press invites; calendar export; story list export / story list emails / FTP export; Slack ("Kordiam will send assignments as notifications to Slack users"); UpScore performance analytics; DAMs (huGO, WoodWing Assets); Kordiam REST API + XML export; Okta / Active Directory FS / Microsoft Entra ID SSO; role-based access controls.
- Customer evidence (official quotes): The Times — "a single source of truth for all the stories we're planning to publish, whether it's today, this week, next week or beyond"; Handelsblatt — "Everyone can see the status of a story. We keep track of how the program looks for the day, for the weekend, and for the coming week"; regional newspaper group — replaced Excel + Outlook calendars; Erdee Media — "We work by the model: if it's not in Kordiam, it doesn't exist. We require our editors and teams to start every story in Kordiam"; public broadcaster (Nordics) — "cornerstone of our story tracking and content management".

### Interpretation

Kordiam is the pure "manage the newsroom's work" pole: no rundown, no prompter, no playout; the output spine is the publication schedule (dates × platforms/editions), and the product's exit point is the handoff to CMS/DAM/analytics. It demonstrates that the Type exists without any broadcast machinery.

## Product B — Dalet Pyramid (+ Galaxy five product family)

Evidence layer: A (direct observation, official vendor pages/essay) unless noted.

### Key observations

- Positioning: "Modular, story-centric and multiplatform news production & distribution"; feature areas: 1. Planning, 2. Rundown, 3. Ingest, 4. Editing, 5. Publish & Playout, 6. Manage.
- **Planning**: "Visualize, manage, assign and track stories across teams and locations"; Organize (create/display/sort stories across teams and stations; configurable dashboards/columns); Enrich ("Gather & centralize all content related to a story. Access news and documents, update your story with media assets, tags, description, dates and assignments"); **Assign & track** ("Create work orders and assign tasks to other newsroom members. Track the story progress, status and results").
- **Rundown** (official copy): "Enhance the production of your live shows, collaborate around stories, scripts & media with real-time co-authoring"; "Configurable views, blocks, timing and more"; "Assignments & real-time collaborative scripting with access to media, tags, and comments. Unified experience across teams and stations; rundowns seamlessly integrated with planning, cataloguing and editing"; "Seamless integration with your third-party newsroom systems and studio equipment: prompter, graphic system, studio automation, and more."
- **Rundown essay** (official, 2024): "For decades, the traditional rundown has been the backbone of newsroom operations… It coordinates work within the newsroom among producers, writers, directors, and editors, ensuring everything runs smoothly during live broadcasts or recorded shows"; "They are typically broadcast-centric, a blueprint for what will happen in a single show"; story-centric trend: "untethers content from specific output channels"; "Stories are available in the rundown and the rundown is available in your story planning tool"; real-time co-authoring of scripts "presented in an intuitive and familiar online shared document style"; "Easily add packages from stories and preview content directly in your rundown"; browser-based, cloud/on-prem/hybrid.
- **Ingest**: live feed recordings centralized (on-prem/cloud, growing files); file ingest "against a story" in the field; camera-card workflows with metadata schemas.
- **Editing**: web-based editor for TV and digital output; NLE extensions (Premiere Pro, Media Composer); proxy editing.
- **Publish & Playout**: "Broadcast your news story directly from the studio to one or different channels simultaneously. Integrate with your playout system"; "Share your stories directly to digital outlets (social media, OTT, CMS), manually or automatically."
- **Users** (official personas): journalist (mobile: draft stories, **read wires**, search and preview material, "follow the editorial status of her stories", upload from the field); news director (multi-city teams, reviewing packages); chief editor ("follow the progress of the newscast… check the status of stories").
- **Dalet Galaxy five** (same family): "Fully integrated NRCS… Manage end-to-end television, radio, digital and social news production within a single system with **unified planning**"; MAM pillar; ingest/playout/delivery pillar; workflow orchestration; mobile app (Dalet On-the-Go) "for news producers on the move".

### Interpretation

The Dalet family documents the broadcast NRCS pole plus the converged trend: planning and rundown as two views over the same story records; the rundown remains "the backbone" for live shows while being opened up to digital-first, story-centric workflows. Media/ingest/editing/playout pillars are suite packaging around the same work-management core.

## Product C — MOS Protocol (industry standard)

Evidence layer: A (direct observation, official standard body documents).

### Key observations

- "Media Object Server Communications Protocol (MOS): An evolving protocol for communications between **Newsroom Computer Systems (NCS)** and Media Object Servers (MOS) such as Video Servers, Audio Servers, Still Stores, and Character Generators."
- Message classes: (1) descriptive data for media objects pushed to the NCS (searchable awareness of media-server contents); (2) **playlist exchange — "The NCS can build and transfer playlist information to the MOS. This allows the NCS to control the sequence that media objects are played or presented by the MOS"**; (3) **status exchange both ways** — clip status, "the status of specific playlist items or running orders".
- Responsibility split (official FAQ): "the Newsroom Computer System is responsible for the creation, modification, and deletion of editorial information, **including playlists**"; the media object server is responsible for media objects and their metadata.
- History: first meeting 1998 at AP's ENPS developers conference; 150+ participating companies; vendor-neutral integration over TCP/IP.

### Interpretation

The broadcast standard confirms the NCS's defining role: hold and modify the editorial information (including the running order), and drive downstream studio systems from it, with bidirectional status feedback. It also independently documents the existence and naming of the "Newsroom Computer System" category since 1998 (developed at an ENPS conference), supporting the Type's lineage.

## Cross-product Comparison

| Dimension | Kordiam (planning pole) | Dalet Pyramid/Galaxy five (broadcast suite pole) | MOS standard (broadcast definition) | Assessment |
|---|---|---|---|---|
| Work item of record | story/planning item with status, platforms, publish time, tasks, attachments | story record with planning fields, assignments, media; rundown items tied to stories | "editorial information" held by the NCS | **Defining core** (all poles) |
| Assignment/task machinery | core: tasks tied to stories, per-desk task types, deadlines derived from publication date | core: "create work orders and assign tasks… track the story progress, status and results"; assignments inside rundowns | (not addressed) | **Defining core** |
| Planned output schedule | publication schedule: dates × platforms/editions, slots, one-click reschedule; monthly calendar; undated backlog | rundown for live shows (ordered, timed blueprint of a single show) integrated with planning | NCS builds playlists / running orders that control play sequence | **Defining core** (realization differs by medium) |
| Shared status visibility | "everyone can see the status of a story" (customer quotes, official site) | "follow the editorial status of her stories"; chief editor follows the newscast | status exchange between systems | **Defining core** (as behavior) |
| Rundown as timed show assembly | absent | yes (blocks, timing, co-editing) | running orders, playlist sequence | **Broadcast realization** of the output spine, not definitional |
| Scripts + prompter/graphics/automation integration | absent | yes (official) | CG/audio/still/video objects | Broadcast-pole common, not definitional |
| Wire/agency feed intake | yes, as integration ("Wire Feeds" in data feeds; Slack/email/event feeds) | yes ("read wires" in official persona; ingest pillar) | media objects pushed to NCS | **Common** (news-native deployments), not definitional |
| Handoff to publishing/production systems | core pattern (idea → CMS; story-data exchange) | core pattern (publish & playout integrations) | NCS → media servers | **Common/structural consequence** of the Type's scope, mechanics vary |
| Forward planning / topics / campaigns | core (Topics page, campaigns, months ahead) | planning across teams/stations, dates on stories | (not addressed) | **Common** (Kordiam-only depth → optional depth) |
| Staff coordination (availability, shifts) | yes (broadcast page) | not prominently documented | (not addressed) | **Optional** (single-product direct evidence) |
| Media ingest/editing inside the system | no (DAM integrations instead) | yes (suite pillar) | media objects server-side | **Suite packaging / variant**, not definitional |
| CMS/API export of planned stories | yes (API, XML, story-list export) | yes (digital publishing) | (different: playlist exchange) | **Common** |
| RBAC / SSO | yes (official FAQ) | enterprise posture documented generically | (not addressed) | **Common**, details vary |

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures (removing any one collapses the Type):

1. **The editorial work item of record.** Persistent, individually identified records for the units of newsroom work — the story/planning item — carrying what it is about, where and when it is intended to run, its production status, and its attached context (tasks, media, notes). Without it: scattered notes and messages, no shared state of the operation.
2. **The assignment-and-task machinery binding people to items.** Work orders/tasks/assignments linked to their items across the newsroom's production desks (text, photo, video, graphics), with deadlines derived from the planned run and per-assignee visibility. Without it: a passive content calendar; the "management" is gone.
3. **The planned output schedule as the spine items are placed into.** The newsroom's scheduled output — dated slots across platforms/editions (print/digital realization) or the ordered, timed blueprint of a specific show (broadcast rundown realization) — plus a forward-planning layer and an unscheduled backlog, all continuously adjusted as news changes. Without it: a task manager with no scheduled-output object to organize work around.

Jointly-held load-bearing analysis:

- 1 alone → a story/content status tracker (list of things being made)
- 1+2 without 3 → editorial task management (a generic task board with story linkage)
- 1+3 without 2 → a publication/content calendar nobody staffs
- 2+3 without 1 → shift/task scheduling detached from the editorial record
- none → the uncoordinated newsroom (email + spreadsheets), which is exactly what the products replace (documented by customer quotes)

### L1 — Common Mature Structure

- shared status visibility to the whole desk/newsroom (the operating picture)
- wire/agency feed intake (native or via integration) and other resource inflows (event calendars, press invites, email/pitch import)
- story templates and custom fields shaping items per desk
- short-term grid + monthly calendar views with gap-spotting and filtering
- rescheduling as an ordinary, low-friction operation (drag-and-drop, one-click moves)
- handoff/integration out to production-and-delivery systems (CMS, DAM, playout, analytics)
- roles and permissions (role-based access; desk-scoped views)
- notifications into work surfaces (e.g., assignment notifications)

### L2 — Variant / Optional Structure

- broadcast realization: rundown with per-item timing, blocks, real-time collaborative scripting, prompter/graphics/automation integration, playout handoff, MOS-class status exchange
- print/edition realization: issue-based planning, print+digital combined schedules
- radio realization: script-centric rundowns (lower visual-media load)
- staff coordination: availability timelines, shift assignment, absence views (single-product direct evidence this pass)
- topics/campaign/strategy layer over the plan (single-product depth this pass)
- converged story-centric suites: one story record shared by planning, rundown, production and digital publishing (vendor-documented trend)
- communications/PR teams reusing the same tooling (adjacent deployment)
- embedded media ingest/editing (suite packaging), AI overlays, analytics integrations

### L3 — Vendor-specific (research notes only)

- Kordiam: Story Card side panel, "undated stories" as a named concept, UpScore/huGO/WoodWing integrations, Skimmr/Eximio AI companion products, Desk-Net→Kordiam rebrand lineage
- Dalet: Pyramid "work orders", Galaxy five On-the-Go mobile app, "Rundown Redefined" product philosophy, Competitive Upgrade Program from legacy NRCS
- Historical NRCS market (not directly documented this pass): iNEWS, ENPS, Inception, Octopus product specifics — deliberately not asserted anywhere

## Rejected Findings (anti-overfitting)

- **"A Newsroom Management System = broadcast rundown software."** Rejected: the planning-first pole has no rundown yet is unambiguously the same Type (same objects, same loop). The rundown is one realization of the output spine.
- **"Wire ingestion is defining."** Rejected: Kordiam has it as an integration, the publishing sibling treats it as standard-not-definitional; it is a resource inflow, not the organizing structure.
- **"The NMS publishes the news."** Rejected: neither pole owns the public record — Kordiam exits to CMSs; Dalet exits to playout/publishing; the publishing sibling owns the gated publication lifecycle and curated surfaces. The broadcast NCS's playlist control is operational transmission coordination, not the revisable-public-record publication lifecycle.
- **"It's just project management for news."** Rejected: generic PM has no scheduled-output spine (shows/editions/slots), no domain inflows (wires/events), and no studio/CMS integration contract. The output schedule is what makes the Type newsroom-native.
- **"Suite pillars (MAM, ingest, editing, playout) are part of the Type."** Rejected: present in the Dalet family as packaging; absent in the planning pole; they belong to adjacent Types (Media Asset Management, etc.).

## Boundary Findings

- **vs News Publishing Platform** (ratified seam from the sibling pass): the publishing Type produces and publishes the public record (story lifecycle → gated publish act → public channels; curated surfaces; corrections/removals). This Type plans, assigns, and coordinates the work and assembles it into the scheduled output; the public record is owned downstream. Evidence for the seam from both sides: Kordiam's "idea to CMS" integrations and story-data exchange; the sibling's documented "editorial planning surfaces bundled into publishing suites (packaging, not identity)". Removing the publication/presentation machinery from the publishing side leaves a work-management system; removing plan/assign/schedule from this side leaves a publishing system.
- **Broadcast blur, flagged**: broadcast NRCS suites integrate playout and studio automation (Dalet; MOS standard). This is operational transmission control driven from the show blueprint — not the publication lifecycle of the public record. The distinction held: the NMS's deliverable is the *ready-to-run scheduled output + coordinated work*, not the *published, revisable public record*.
- **vs Broadcast Management System**: BMS = station business operations (programming/traffic/commercial scheduling); the NMS = editorial work. Different objects (spots/programs vs stories/assignments) even though both touch the broadcast day.
- **vs Content Planning Platform (marketing)**: structurally similar planning tools; different domain (campaigns/leads/SEO vs news output and broadcast rundowns). Kordiam itself documents communications-team deployments — the tool category straddles; the Type is defined by the newsroom operation it manages.
- **vs Production Scheduling / Call Sheet Application**: both plan production work against a schedule; film/TV production centers scenes/shoot days/calls; the newsroom Type centers stories against continuous news output with wires/rundowns/CMS contracts.
- **vs Project Management Application**: generic projects lack the output-spine, domain inflows, and delivery contracts; a newsroom can *run* on a PM tool only by sacrificing the rundown/slot structure that the products build natively.
- **vs Media Asset Management**: MAM owns asset custody; the NMS attaches/quotes media against work items (Dalet's MAM pillar is suite packaging; Kordiam integrates external DAMs).
- **"Remove what to become another Type" judgments**: remove assignment + schedule → publishing/CMS territory adjacent (content tracker); remove the editorial item's news semantics and wires/rundown/slots → generic PM; add the gated public-record lifecycle + curated surfaces → News Publishing Platform.

## Historical / Market-Sample Check

Paper-era newsroom (conceptual, layer C): the budget/forward-planning book and assignment book at the city desk; story slugs with reporter + run date + status on the board; the rundown board in the broadcast control room (ordered, timed items, scripts); the wire teletype as the inflow. All three defining legs are satisfied with zero software, no MOS, no CMS. The definition therefore does not depend on the current SaaS or converged-suite implementation, and no specific protocol, integration, or deployment form is named in the core. Regional/non-English markets (print-heavy groups, public broadcasters) are documented in the sample and fit.

## Uncertainties

1. Classic NRCS products (iNEWS, ENPS, Octopus, Inception) could not be documented from official sources this pass; the broadcast pole's rundown semantics rest on Dalet's official documentation plus the MOS standard. Vendor-specific NRCS details were deliberately not asserted.
2. Whether formal assignment records exist in *every* NRCS (vs. script authorship serving that role in rundown-centric products) — unresolved; assignment is kept in the core at the level of "binding people to items," which script authorship in a rundown satisfies.
3. Superdesk's Planning module (likely third vendor evidence) was not verifiable this pass; noted for a future pass.
4. Exact status vocabularies per product vary (Kordiam "workflow status"; Dalet "story progress, status and results"); only the existence of user-visible status is asserted.
5. Depth of the topics/campaign layer and staff-coordination layer across the market — direct evidence from one product each; held optional.

## Final Synthesis

A Newsroom Management System is the news organization's internal system of record for its editorial operation. Its world is made of: (1) persistent identified work items (stories/planning items) carrying intended run placement and production status; (2) assignments and tasks binding the newsroom's people to those items with schedule-derived deadlines; and (3) the planned output schedule — dated slots per platform/edition or the ordered, timed blueprint of a show — into which items are placed, from which deadlines derive, and which is continuously adjusted as news changes. Around this core, mature products add shared status visibility, wire/event inflows, templates and custom fields, calendar views, handoff integrations to CMS/playout systems, and role-based access. The broadcast NRCS is the Type's most machine-coupled realization (scripts, prompter, studio automation, MOS-class status exchange); the planning-first editorial tool is its lightest. The Type ends where the public record begins: publishing the news is the News Publishing Platform's job.
