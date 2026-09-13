# Newsroom Management System

## Overview

A **Newsroom Management System** is the news organization's internal system of record for its editorial operation. It holds the work — the stories and content items the newsroom intends to produce — as persistent, identified records; binds the newsroom's people to that work through assignments and tasks; and places every item into the newsroom's planned output schedule: the dated publication slots across platforms and editions, or the ordered, timed blueprint of a specific broadcast show. It is the system the newsroom runs its day from.

The defining structure is deliberately small:

```text
Editorial work item
  (planned story: what, intended run placement, production status)
├── Assignment & task machinery
│     (people bound to items, deadlines derived from the schedule)
└── Planned output schedule
      (publication dates/slots per platform & edition,
       or the rundown for a specific show)
      → the shared, continuously adjusted operating picture of the day
```

Everything else commonly associated with newsroom software — agency wire feeds, story templates, topic and campaign planning, staff availability and shifts, CMS or studio integrations, analytics hooks — is standard or optional machinery layered on that core, not what makes the product a newsroom management system. The definition names no deployment form, no protocol, and no medium: a broadcast rundown, a print edition plan, and a multi-platform digital grid are all realizations of the same output schedule.

The boundary that matters most: this system manages the *work*; it does not own the *public record*. Producing and publishing the news — the gated publication lifecycle, corrections and removals, curated front pages — belongs to the News Publishing Platform, which typically receives finished work from, or is paired with, the newsroom management system.

## Users & Context

The primary users are the members of the newsroom's editorial operation:

- **planning editors / assignment editors** — build the forward plan, decide what gets covered, and distribute the work
- **reporters and journalists** — pick up and work their assignments, draft items, follow their stories' status, and draw on incoming material such as wire content
- **producers (broadcast)** — build and adjust the rundown for their shows, co-edit scripts, and assemble the on-air sequence
- **desk editors and production desks** (photo, video, graphics) — receive, track, and deliver the tasks attached to stories
- **news directors / editors-in-chief** — read the day, the weekend, and the coming week at a glance; watch the plan fill and the status move

The work environment is a continuous news cycle on multiple clocks: broadcast shows air at fixed times, digital platforms publish around the clock, print editions close once a day, and breaking news reorders everything without notice. Multiple teams in multiple locations work the same pool of stories simultaneously, which is precisely why the shared operating picture — who is doing what, for which slot, in what state — is the product's reason to exist.

## Core Model

### The Editorial Work Item

The unit of record is the **work item** — the story (also called a planning item, budget line, or rundown item depending on the realization): a persistent, individually identified record that carries what the item is about, where and when it is intended to run (platform and publication time, or the show it belongs to), its production status, and its attached context: the tasks assigned against it, media and documents, notes, related events, and its history. Items exist before they are scheduled: an unscheduled backlog of ideas, pitches, and wire-derived leads sits alongside the scheduled plan until editors decide what makes it into the output.

### Assignment and Task Machinery

Work is coordinated through **assignments and tasks bound to their items**. A story generates work across the newsroom's production desks — a reporter to write it, a photographer to cover the event, a video editor to cut the package, a designer to build the graphic — and each piece of that work exists as a trackable task linked to its story, so the context travels with the assignment. Task deadlines are derived from the planned run: a story slated for tomorrow morning's show or edition pulls its tasks' urgency backward from that moment. Per-desk task types, statuses, and views let photo, video, and graphics teams work differently while feeding one shared picture.

### The Planned Output Schedule

The third structure is the newsroom's **output schedule** — the spine that items are placed into and deadlines are derived from. It has two common realizations:

- **Publication schedule (print/digital).** A grid of dates × platforms (and editions/issues, where they exist), holding one or many slots per day. Editors fill slots, compare several days side by side across channels with different publication rhythms, spot gaps in the plan, and move items between dates and slots as the news changes. An unscheduled backlog is reviewed against this grid and promoted into it.
- **Rundown (broadcast).** The ordered, timed blueprint of a single show: the sequence of items — scripts, packages, media elements, graphics — that will make up the broadcast, with per-item timing. Producers build and re-order it collaboratively, edit scripts in place, and adjust it continuously up to and through the broadcast. In mature broadcast deployments the rundown connects onward to studio systems — teleprompters, graphics, playout automation — and receives status back from them, so the on-air sequence follows what the newsroom assembled.

Stretching over both realizations is the **forward-planning layer**: longer-range calendars, recurring and one-off events to cover, and grouped coverage efforts (an election, a themed series) that bundle many items under one structural topic and can be rescheduled as a whole.

### Standard Capabilities (not definitional)

Mature products commonly add the following machinery. Its absence in a lean implementation does not disqualify the product; its presence does not define the Type.

- **Shared status visibility** — every story's state (planned, assigned, in production, ready, scheduled) visible to the whole desk; the operating picture is the point.
- **Wire and resource inflows** — agency wire feeds, event calendars, press invitations, and email/pitch intake entering the plan as potential items.
- **Story templates and custom fields** — per-desk item shapes with preset fields, defaults, and pre-linked production tasks; organization-specific planning fields (audiences, user needs) with saved shared views.
- **Calendar and gap views** — short-term grids, monthly overviews, filtering by platform, status, desk, or topic.
- **Handoff integrations** — finished items moving outward to content management systems (with story data exchanged), digital asset libraries, playout and publishing systems, and performance-analytics tools; assignment notifications pushed into work-chat tools.
- **Roles and permissions** — role-based access control and desk-scoped views.
- **Staff coordination** — availability timelines, shift assignment, and absence views used when deciding who can take what.
- **Broadcast production coupling** — script co-editing, teleprompter/graphics/automation integration, and playout handoff in the rundown realization.

### One Structure, Many Implementations

```text
Concept:  Work item of record
Realizations:  planning story with platform/slot metadata · rundown item
               with script and timing · budget line in a forward plan

Concept:  Output schedule (the spine)
Realizations:  publication grid (dates × platforms/editions) ·
               broadcast rundown (ordered, timed show blueprint)

Concept:  Assignment
Realizations:  tasks/work orders tied to stories · desk-specific task types ·
               script authorship inside a rundown

Concept:  Resource inflow
Realizations:  wire feed integrations · event calendar import ·
               email/pitch intake · ingest of field media against a story
```

A reader who has only seen one realization — say, a web-based planning grid for a newspaper, or a control-room rundown for a TV channel — should still be able to recognize the other as the same Application Type.

## How It Works

### Plan

```text
Ideas, pitches, wire leads, and scheduled events enter the system
→ items are created (often from desk-specific templates)
→ editors review the unscheduled backlog
→ items are placed into the forward plan or the near-term output schedule
→ grouped coverage (topics, events, campaigns) bundles related items
```

Planning runs on two clocks at once: months-out structural planning and today's list. Both stay visible together, and the schedule is a living object — items move between days, slots, and platforms in a single motion when news forces a re-plan.

### Assign

```text
Editor creates or opens an item
→ attaches tasks (write, shoot, edit, graphic…) to it
→ assigns them to specific people (or desks)
→ deadlines are derived from the item's planned run
→ assignees see their work with the story's context attached
```

The linkage is structural: every task belongs to its story, so "what and why" travels with "who and when."

### Produce

```text
Reporters, photo/video/graphics desks work their tasks
→ drafts, media, and finished deliverables attach to the item
→ the item's status moves through the production cycle
→ the desk watches the list: what's on track, what's behind, who's free
```

The list is the newsroom's shared surface — the state of the operation is public to the team by design, replacing the email-and-spreadsheet coordination these products exist to retire.

### Assemble into the output

```text
Print/digital:  fill and re-fill the publication grid
                (move items between dates, platforms, and slots;
                 promote backlog items into open slots)

Broadcast:      build and run the rundown for the show
                (order items, set timing, co-edit scripts,
                 attach media and graphics)
                → adjust continuously as the news develops
                → the rundown drives, and receives status from,
                  the studio systems it is integrated with
```

### Hand off

Finished items leave the system through its integrations: story data flows to the content management system for publication, finished broadcast assemblies flow to playout, deliverables reach asset libraries, and outcome data may flow back from analytics. The newsroom management system's deliverable is the coordinated, ready-to-run work and its scheduled placement — what happens on the public side belongs to the systems downstream.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Story list / planning grid

The primary entry surface. Typical information: items for the selected day(s) or issue(s) with platform, publication time, status, assignees, and delay indicators. Primary actions: create items, move them between dates/slots/platforms, filter and group views, promote backlog items.

### Story card (item detail)

The work item's full record. Typical information: description and briefing, intended placement, status, attached tasks and assignees, media and documents, related events, update history, location. Primary actions: edit, attach material, create/assign tasks, change status, reschedule.

### Task / assignment board

The production desks' surface. Typical information: all tasks across teams, grouped and filtered by desk, status, or date, with deadlines derived from the plan. Primary actions: assign, reassign, update status, spot what is running behind.

### Calendar views

Short-term (days/issues side by side) and monthly overviews. Typical information: the planned output across platforms with gaps visible. Primary actions: drag items to new dates/slots, reschedule grouped coverage as a whole, filter to a specific platform or topic.

### Rundown view (broadcast realization)

The show's ordered, timed assembly. Typical information: items in run order with per-item timing, scripts, attached media and graphics, assignment and editing state. Primary actions: reorder, adjust timing, co-edit scripts, insert packages from stories, hand off to studio systems.

### Wire / feeds monitor

Where external streams arrive (common in news-native deployments): incoming wire items and feeds, ready to be scanned and turned into work items. Primary actions: read, convert to an item, route to a desk.

### Staff availability / shifts

The coordination layer over assignment decisions. Typical information: who is available, when, and on which shift. Primary actions: assign shifts, check availability before assigning work.

### Topics / campaigns overview

The structural layer over the plan (common; depth varies). Typical information: core topics and grouped coverage with their items and calendars. Primary actions: break down strategy into coverage, drag a whole effort to new dates, filter by audience or persona.

## Important Rules / Behaviors

- **Assignment carries context.** Every task is bound to its story; the assignee always works with the item's who/what/when attached. Detached task lists defeat the model.
- **Deadlines derive from the schedule.** Task due times are pulled back from the item's planned run — the output schedule, not the task list, is the source of urgency.
- **The schedule is alive.** Rescheduling is an ordinary, first-class operation — single items, slots, and grouped coverage move as news changes; breaking coverage re-plans the day in one motion rather than by deleting and recreating.
- **Status is shared by default.** The state of every item is visible to the newsroom; many organizations adopt the discipline that if a story is not in the system, it does not exist — coverage starts in the tool, not beside it.
- **Scheduled and unscheduled are distinct states.** Backlog items wait visibly for placement; scheduling them is a deliberate editorial act.
- **The broadcast rundown is a timed, ordered blueprint for one show.** Its changes propagate to the studio systems it is integrated with, and equipment status flows back — the sequence that airs follows what the newsroom assembled, and the newsroom sees what the equipment did with it.
- **Roles bound the loop.** Access and visibility are permission-scoped (role-based access, desk views); planning, assignment, and status changes follow the organization's editorial hierarchy.
- **The system ends at the public record.** Publication, correction, and removal of the published news are downstream operations; this system's records are the work and its schedule, not the published artifact.

## Variants

- **Broadcast NRCS (TV/radio)** — rundown-centric: scripts, timing, media, prompter/graphics/automation integration, playout handoff; the classic "newsroom computer system" lineage. Deepens the production coupling while keeping the same core.
- **Print/digital editorial planning** — publication-grid-centric: dates, issues, platforms, CMS handoff; the lightest realization of the Type.
- **Converged story-centric suites** — one story record shared by planning, rundown, production, and digital publishing across linear and digital teams; the current direction of the broadcast pole, explicitly aimed at running TV and digital from the same items.
- **Agency and multi-location newsrooms** — shared plans across desks, titles, or regions; content exchange between cooperating newsrooms.
- **Communications-teams deployments** — the same planning/assignment tooling reused by corporate communications teams for their content operations (an adjacent deployment of the same structures, without broadcast machinery).
- **Lean newsrooms** — planning grid plus tasks with no wire, no rundown, and light permissions; the core loop intact.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| News Publishing Platform | sibling (planning vs publication) | that Type produces and publishes the public record — gated publication lifecycle, corrections/removals, curated front pages; this Type plans, assigns, and assembles the work and hands it off. Planning modules bundled inside publishing suites are packaging, not identity |
| Broadcast Management System | sibling (business vs editorial) | station business operations (programming, traffic, commercial scheduling); this Type manages the editorial work, not the commercial schedule |
| Content Planning Platform | adjacent (different domain) | marketing content calendars plan campaigns and channels; this Type plans news output against editions, platforms, and broadcast shows, with wire/rundown/CMS contracts |
| Production Scheduling / Call Sheet Application | adjacent (different production world) | film/TV production plans scenes, shoot days, and calls; this Type plans continuous news work against a running output schedule |
| Project Management Application | structurally similar, different Type | generic projects lack the scheduled-output spine (shows/editions/slots), the domain inflows (wires, events), and the delivery contracts to CMS/playout |
| Media Asset Management | adjacent | MAM owns asset corpus custody; here media is attached to and quoted against work items, and asset libraries appear as integrations |
| Content Distribution Platform | downstream | distributing finished content to external surfaces; this Type's handoff feeds such systems but does not perform it |
| News Application / News Aggregator | consumer-side counterpart | reading surfaces for audiences, served by downstream publication systems; different users and objects entirely |

The most important boundary is with the News Publishing Platform: the test is whether the system's center of gravity is the *work and its schedule* (this Type) or the *published record and its presentation* (that Type). In the broadcast realization the boundary is tested by the rundown's studio coupling — that coupling drives transmission equipment operationally; it still does not make the system the owner of a revisable public record.

## Representative Products

- Kordiam (formerly Desk-Net) — editorial planning-first system used by newspapers, magazines, and broadcasters' digital teams
- Dalet Pyramid — story-centric converged news suite (planning, rundown, production, playout)
- Dalet Galaxy five — integrated NRCS for television, radio, and digital news operations (same vendor's product family as Dalet Pyramid; sampled as one vendor's news line)

## Sources

Research date: **2026-09-08**

- Kordiam (official site and feature pages) — https://kordiam.io/ , including /content-planning-features, /task-management, /newsroom-content-planning, /broadcast-newsroom-software, /integrations, /topics (fetched 2026-09-08)
- Dalet News Organizations solution page — https://www.dalet.com/solutions/news/ (fetched 2026-09-08)
- Dalet Pyramid product page — https://www.dalet.com/products/pyramid/ (fetched 2026-09-08)
- Dalet Galaxy five product page — https://www.dalet.com/products/galaxy-five/ (fetched 2026-09-08)
- Dalet, "Rundown Redefined: Dalet's Story-Centric News Production Approach" — https://www.dalet.com/blog/rundown-story-centric-news-production-approach/ (fetched 2026-09-08)
- MOS Project — MOS Protocol welcome and FAQ (official standard documentation) — https://mosprotocol.com/ , https://mosprotocol.com/mos-faq/ (fetched 2026-09-08)

> Sourcing limitations: official documentation for the classic broadcast newsroom-system products (Avid iNEWS, AP ENPS, Octopus Newsroom, Ross Inception News) could not be reached from the research environment this pass (unreachable sites or login-walled documentation portals), so the broadcast pole's characterization rests on the MOS Protocol standard's definition of the Newsroom Computer System's role plus the reachable vendor's official documentation; vendor-specific broadcast-product details are intentionally not asserted in this document. The print/digital planning pole rests on one vendor's official feature documentation, so product-specific depths (topics/campaign layer, staff shifts) are described as common variants rather than universal structure. No precise numeric limits, defaults, or timing values are asserted; details of that kind were not verifiable at the required strength this pass.
