# Tactical Analysis Platform

## Overview

A **Tactical Analysis Platform** is a staff-facing analysis application used to break down match content — footage and/or match event data — into tactically meaningful structure, and to turn that structure into deliverables that prepare a team for its next matches.

Its center of gravity is the **match and the opponent**: analyzing how matches were played, what patterns and tendencies the opposition shows, and what the game plan should be. This distinguishes it from own-team video review (which centers athlete development) and from performance measurement (which centers physical and output metrics).

The defining structure is small:

```text
Match content corpus (footage and/or event data, with match context)
└── Tactical breakdown structure (events, patterns, annotated frames)
    └── Preparation loop (reports / presentations / dashboards → coaching staff)
```

Everything else commonly associated with the category — tagging button panels, telestration, live bench streaming, AI auto-detection, cloud sharing — is widespread in current products but is not part of the defining core. Pre-digital practice (opposition dossiers, coded match sheets, hand-drawn diagrams) satisfies the same structure without any of it.

## Users & Context

Primary users:

- **opposition / tactical analyst**: collects opponent matches, breaks them down, builds scouting and game-plan deliverables
- **head / assistant coach**: consumes the analysis, shapes the game plan, decides what the team trains against
- **performance / video analyst** (generalist): in smaller organizations, one person runs both own-team review and opposition preparation in the same tool

Secondary users:

- **players**: view prepared presentations and clips, usually read-only
- **data analysts** (elite end): build custom metrics and models over match event data

The work context is the weekly match cycle: collect the next opponent's recent matches → break them down → assemble the report → brief the team → play → review. The same tooling is also used for reviewing one's own matches through a tactical lens (set plays, phases, formations), which is why mid-market products often serve both uses in one tool.

## Core Model

### The Defining Core

```text
Match content corpus
└── Tactical breakdown structure
    └── Preparation loop
```

Three structures, held jointly:

- **Match content corpus** — an organized, persistent record of matches (the team's own and/or opponents') carrying match context: teams, competition, date. It accumulates across the season and is the object the whole application works on. The substrate varies — match footage, match event data, or both — but the organized, context-carrying, accumulating corpus is constant. Without it there is only a video editor or a bare data feed.
- **Tactical breakdown structure** — analysis units with tactical meaning imposed on the content and referencing moments in it: tagged or coded events, tactical patterns and sequences, annotated or drawn-over frames, tactical visualisations on a pitch or court. The breakdown is organized around tactical questions — opponent tendencies, set plays, formations, phases of play — not around generic highlights. Without it the corpus is just an archive.
- **Preparation loop** — breakdown assembled into deliverables (reports, presentations, filtered event lists, dashboards) that coaching staff consume to make preparation decisions for upcoming matches. Without it the analysis is a database nobody works from.

### Capabilities Shared by Mature Products

- **Tagging / coding windows** — button panels that stamp events onto the timeline while watching (live or post-game), producing a structured event record bound to video moments.
- **Telestration** — drawing, arrows, and shapes over frozen frames to explain positioning and movement.
- **Filtered event lists and playlists** — selecting events across one or many matches by category, team, player, or situation.
- **Presentations and reports** — clips, frames, and statistics assembled into deliverables for staff and players.
- **Statistics from tagged events** — counts and rates computed from the breakdown itself.
- **Multi-match comparison** — patterns observed across several opponent matches rather than one.
- **Live in-game use** — coding during the match and streaming selected video/data to the bench.
- **Role-based sharing** — analysts build, coaches direct, players view.

### One Structure, Many Implementations

```text
Concept:            Match content corpus
Implementations:    user-imported match footage; vendor-collected event data;
                    vendor-operated video libraries; both combined

Concept:            Tactical breakdown
Implementations:    manual tagging windows; scripting-driven coding;
                    vendor event data with analytical models; AI auto-detection

Concept:            Preparation deliverable
Implementations:    video presentations; written/paged reports;
                    interactive dashboards and pitch visualisations
```

A reader who has only seen one implementation (e.g. a tagging-window desktop tool) should still recognize a data-first platform as the same Type.

## How It Works

### The weekly preparation cycle

```text
Acquire match content (own + next opponent's recent matches)
→ break down: tag/code events, mark patterns, annotate frames
→ filter and compare across matches
→ assemble the deliverable (report / presentation / dashboard)
→ brief coaches and players
→ play; review own match through the same structure
→ repeat
```

### Break down a match

The analyst opens a match in the corpus and imposes structure on it: tagging events with a coding window (or consuming vendor-collected event data), clipping sequences that show a pattern, drawing over frames to show spacing or movement. Each analysis unit references a moment in the match and carries tactical meaning (what happened, in which phase, by whom, against what).

### Compare and question

The value of the corpus is accumulation: the analyst filters events across several matches — all opponent corner kicks, all sequences where a certain formation was pressed, all turnovers in a zone — to answer tactical questions that no single match can answer.

### Assemble and deliver

Selected events, frames, and statistics are assembled into a deliverable shaped for its consumer: a coach-facing game-plan report, a player-facing presentation, an interactive dashboard. The deliverable is the product of the loop; after the match, the same structure is used to review the team's own performance.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- organized match content corpus with match context
- tactical breakdown structure referencing moments in the content
- preparation loop delivering analysis to coaching staff

**Common mature structure** — present in most modern products:

- tagging/coding windows, telestration, playlists, presentations
- event-derived statistics, multi-match comparison, role-based sharing

**Variant / optional** — depends on segment, sport, and era:

- content substrate (footage-only / data-only / both)
- who produces the breakdown (user coding / vendor data / AI)
- live in-game coding and bench streaming
- cloud delivery and mobile companions
- dual-use packaging with player scouting
- deep scripting/customization (elite end)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Match library

The entry surface: the organized corpus of matches with context (teams, competition, date) and the season's accumulation.

- primary actions: import or acquire matches, open a match, search/filter the corpus

### Breakdown workspace

The analyst's main working surface: video (or a data view of the match) plus the coding/tagging mechanism and the event timeline.

- typical information: match video, event timeline, coding window, clip list
- primary actions: tag/code events, clip sequences, annotate frames, edit event records

### Event list / comparison view

Filtered views over the breakdown across one or many matches.

- typical information: filtered events with context, derived counts
- primary actions: filter by category/team/player/situation, build playlists, compare across matches

### Presentation / report builder

Where breakdown becomes deliverable.

- typical information: selected clips, annotated frames, statistics, narrative structure
- primary actions: assemble, order, annotate, publish to staff/players

### Dashboard / visualisation surface (data-first products)

Pitch/court visualisations and computed metrics over event data.

- typical information: match/event data, models, pitch plots
- primary actions: configure visualisations, query, export

### Live surface (where offered)

In-game coding and bench streaming.

- primary actions: code live, stream selected video/data to the bench

## Important Rules / Behaviors

### The corpus is the memory

The breakdown only becomes powerful because it accumulates: this season's and previous matches stay organized and queryable. A tool that loses structure between matches stops being this Type.

### Analysis units reference moments, not re-edited media

Tagged events, annotations, and patterns are structured references into the match content — not new edited video. The original match stays intact; the analysis layer can be rebuilt, re-filtered, and recombined.

### The analyst builds, the coach decides

In mature deployments the division of labor is structural: analysts produce the breakdown and deliverables; coaches consume them and make the preparation decisions; players mostly view. Sharing is role-based.

### Own-team and opposition uses share one tool in the mid-market

Many products serve both own-team review and opposition preparation with the same tagging and presentation machinery. The elite market separates them into distinct products. The use — not the tool — determines which Type a given deployment instantiates.

### Live use is an extension, not the center

Live coding and bench streaming extend the same breakdown structure into the match itself, but the defining loop is the preparation cycle around upcoming matches.

## Variants

- **footage-first desktop analysis** — user imports and codes match video; desktop license; common from grassroots to pro (e.g. the tagging-window tradition)
- **elite customizable tooling** — scripting-driven coding, separate analytics and telestration products, deep customization for pro/national-team analysis departments
- **data-first event analytics** — vendor-collected event data and models with an analytics platform and integrated video; tactical analysis named as a primary use
- **cloud platform with team sharing** — online tagging, team channels, season tracking, mobile companions
- **dual-use analysis + scouting packaging** — one video/data library serving both coaching analysis and recruitment

A variant remains a **Variant** unless it changes users, core objects, workflow, or rules so much that the core model no longer applies — as happens when the center moves to own-team athlete development (Sports Video Analysis), to athlete/team performance measurement (Sports Performance Analytics), or to external-player evaluation (Sports Scouting Platform).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Sports Video Analysis | sibling, shared tooling | centers own-team/own-athlete footage for coaching review and development; this Type centers opposition/tactical match content and next-match preparation — center-of-gravity seam inside one tooling family; the elite market sells them as separate products, the mid-market merges both uses |
| Sports Performance Analytics | adjacent, drift seam | centers athlete/team performance measurement (load, testing, physical output); this Type centers opposition/tactical match content. Match-event analytics products drift here when opposition content becomes the center |
| Sports Scouting Platform | adjacent — shares match video | scouting video is evidence about players and the deliverable is a player evaluation; here the match is the analyzed object and the deliverable is a game plan |
| Match data provider | adjacent | a bare data feed without breakdown structure and preparation loop is a data product; data providers cross into this Type when they ship an analytics platform and name tactical analysis as the use |
| Tactic-board / diagramming tools | different tool family | diagram and playbook authoring without a match content corpus; no analysis loop over real matches |
| Referee / VAR systems | different users | officials' in-match decision loop, not coaching preparation |
| Video Editor / NLE | different output | timeline editing toward a program output; here analysis units reference moments in intact match content |

The most important boundary is with **Sports Video Analysis**: the two Types share tagging, telestration, and match footage, and mid-market products often serve both uses. The seam is the center of gravity — whose content is the record, and for which loop (own-team coaching review vs opposition/tactical preparation). The elite market separates them into distinct products.

## Representative Products

- Hudl Sportscode / Insight / Studio (elite customizable analysis, analytics, and telestration family)
- Nacsport (desktop tagging-window analysis suite, Basic→Elite tiers, with Hub cloud sharing)
- Dartfish myDartfish game-analysis line (live and delayed game analysis)
- Hudl Statsbomb (data-first event analytics with integrated video)
- Hudl Instat (dual-use video + data analysis and scouting)

The Core Model was checked against pre-digital practice (opposition dossiers, coded match sheets, hand-drawn tactical diagrams) to avoid over-fitting to the modern tagging/AI/cloud pattern.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces (product pages):

- Hudl Sportscode — https://www.hudl.com/en_gb/products/sportscode
- Hudl Statsbomb — https://www.hudl.com/en_gb/products/statsbomb
- Hudl product catalog (Insight, Studio, Instat, Fastmodel descriptions) — https://www.hudl.com/en_gb/products/sportscode
- Nacsport — https://nacsport.com/en/
- Dartfish — https://www.dartfish.com/

> Sourcing limitation: vendor help-center and user-manual pages were not reachable in this research pass; evidence is held at product-page strength. Precise operational details (tag limits, exact workflow steps, numeric claims) are intentionally not stated in this document.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary ratifications are recorded in the paired Research Notes.
