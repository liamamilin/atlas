# Sports Video Analysis

## Overview

A **Sports Video Analysis** application is a coaching-side system whose center is a persistent library of sports footage that staff break down into structured, reviewable analysis and deliver back to athletes and teams as feedback material.

The defining structure is small:

```text
Footage library of record
└── Sport-purposed analysis structure
    (tagged/clipped events, annotated frames, comparisons)
    └── Coaching review loop
        (playlists / presentations / shared clips → athletes & staff)
```

Everything commonly associated with modern products — cloud delivery, AI auto-tagging, vendor capture cameras, livestreaming, highlight reels, tag-derived statistics — is widespread in current products but is not what makes the product a sports video analysis application. A desktop license with a local video database, a phone app for individual coaches, and a camera-plus-editor bundle all fit the same definition.

When the center of gravity moves to quantified performance measurement (Sports Performance Analytics), to an external-athlete registry and evaluation (Sports Scouting Platform), to the coach–client relationship and its business machinery (Sports Coaching Platform), or to timeline editing that renders a finished program (Video Editor), the product is drifting toward a different Application Type.

## Users & Context

The primary user is a **coach or sports analyst** working for a team, club, academy, or as an individual instructor. They bring footage of their own athletes into the system, break it down, and turn it into review material.

Typical reasons to open the application:

- break down a just-finished match or session into tagged events
- build a playlist or presentation for the next team film review
- annotate a technique attempt and send it to one athlete
- filter the season's events to study tendencies (own team or an upcoming opponent)
- exchange video with another team ahead of a fixture

Secondary users:

- **athletes** — receive and watch assigned clips, see drawings and comments on their own performances
- **assistant/analyst staff** — do the tagging and assembly work, often live during games
- **administrators** — manage the team/club account, members, and sharing scope

The work environment is split between the desk (post-game breakdown and assembly) and the field (live tagging during games, phone capture at training). Individual-sport coaches (golf, tennis, track, swimming) use the same structure around technique attempts rather than matches.

## Core Model

### The Defining Core

```text
Footage library of record
└── Recording (match / session / technique attempt, with sport context)
    └── Analysis unit (tagged event or annotated clip, referencing moments in time)
        └── Markup (drawings, telestration, notes, comparisons on frames)
    └── Review assembly (playlist / presentation / filtered event list)
        └── Delivery to athletes & staff (shared, commented, watched)
```

Three properties. If any one is removed, the product is no longer recognizable as sports video analysis:

- **Footage library of record** — a persistent, organized collection of recordings tied to sport context (team, opponent, date, athletes, session). The library accumulates across the season and is what the whole system works on. Without it, the product is a one-off video tool or a file store.
- **Sport-purposed analysis structure** — the video is subdivided and marked up into analysis units that reference moments in time: tagged or clipped events with sport meaning, annotated frames, side-by-side comparisons. The markup is held as structured references into the footage, not as re-edited media. Without it, the product is a video archive with playback.
- **Coaching review loop** — analysis units are assembled into review material and delivered back to athletes and staff through the product, with feedback attached to the moments themselves. Without it, the product is footage logistics or a fan-facing highlight service.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They are not what makes the product a sports video analysis application, but they make it practical:

- **Tagging / breakdown mechanism** — user-defined event categories and descriptors (button panels or tagging windows in team-sport products); automatic event detection in some capture-first products; simple clip-and-annotate in technique products
- **Review assemblies** — playlists, presentations, filtered event lists, highlight reels
- **Frame markup** — drawing and telestration tools, slow motion, frame-by-frame stepping, pan/zoom, side-by-side comparison
- **Comments on moments** — feedback attached to specific timestamps, visible to the assigned athletes
- **Team communication surface** — messaging or a team channel attached to the video work
- **Season archive with search and filter** — by opponent, athlete, event type, date
- **Video exchange with other teams** — secure sharing of film with opponents or league peers
- **Stats derived from tags** — event counts and tendencies computed from the breakdown
- **Live support** — tagging during the game and streaming video/data to the bench
- **Role separation** — analysts/coaches build and share; athletes review

### One Structure, Many Implementations

The core model is written in conceptual terms. Products realize each concept differently:

```text
Concept:          Footage library of record
Implementations:  cloud team library, local desktop video database, phone library with cloud backup

Concept:          Analysis unit
Implementations:  button-panel tagged events, AI-detected events, manually clipped moments, annotated technique clips

Concept:          Review assembly
Implementations:  playlists, presentations, filtered event lists, shared clip collections

Concept:          Delivery to athletes
Implementations:  team messaging, athlete app access, shared links, film-session projection
```

A reader who has only seen one implementation (for example, a cloud platform with AI tagging) should still be able to recognize a desktop-license breakdown tool or a mobile technique app as the same Type from the core model.

## How It Works

### Get footage in

```text
Record (vendor camera / phone / sideline camera)
→ upload or import into the library
→ attach sport context (team, opponent, date, session, athletes)
```

How footage arrives is a variant, not the definition: some products ship cameras that upload automatically, some record on phones, some import files from any source. The analysis layer is indifferent to the capture posture.

### Break it down

```text
Open a recording
→ tag events as they occur (live) or while scrubbing (post-game)
→ each tag becomes a clip referencing a moment in the footage
→ attach athletes and descriptors to events
```

This is the central working act. In team-sport products it is button-driven tagging against a user-defined event vocabulary; in capture-first products the vendor's AI proposes the events and staff correct them; in technique products the equivalent act is clipping and annotating individual attempts. The result is the same: a structured layer of analysis units over the raw footage, so that nobody has to rewatch an entire game to find its moments.

### Mark up and assemble

```text
Open an event or clip
→ draw on frames, add notes, slow down, compare side-by-side
→ collect events into a playlist or presentation
→ filter the library by event type, athlete, or opponent to study tendencies
```

### Review with the team

```text
Share the playlist / clips to the team, a group, or one athlete
→ athletes watch in the app, see drawings and comments on their moments
→ coach delivers feedback attached to the footage
→ the library keeps everything as the season's record
```

### Core vs Common vs Optional

**Defining core** — without these, not sports video analysis:

- footage library of record with sport context
- analysis units referencing moments in the footage (tagged/clipped events, annotated frames)
- assembly and delivery of analysis to athletes/staff for review and feedback

**Standard in mature products** — present in most modern products:

- tagging panels / event vocabularies
- playlists and presentations
- drawing/telestration, slow motion, comparison
- comments on moments
- team messaging surface
- season archive with search/filter
- highlight export
- video exchange with other teams
- live tagging and bench streaming
- stats derived from tags

**Variant / optional** — depends on segment, sport, era, and posture:

- capture hardware and auto-upload (capture-first pole)
- AI auto-event detection
- delivery model: desktop license, cloud subscription, mobile freemium
- technique/motion-analysis tooling (measurement overlays, multi-angle compare)
- education and healthcare/physiotherapy use of the same tooling
- livestreaming to supporters (fan-facing adjacency)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Library / recordings list

The entry surface: the season's recordings organized by context.

- lists matches, sessions, and technique attempts with opponent, date, and status
- primary actions: open a recording, upload/import footage, search and filter the archive

### Breakdown / tagging workspace

Where footage becomes analysis.

- video timeline plus a tagging panel of user-defined event buttons (or an AI-detected event list to confirm)
- primary actions: tag an event, adjust clip boundaries, attach athletes and descriptors, review the event list

### Video player with markup

The analysis surface.

- playback controls (slow motion, frame-by-frame, pan/zoom), drawing and telestration tools, timestamped notes, side-by-side comparison
- primary actions: annotate frames, comment on moments, clip and bookmark

### Playlist / presentation builder

Where analysis becomes review material.

- ordered collections of events and clips, optionally with titles and notes
- primary actions: assemble, reorder, add events from the library, prepare for a film session

### Sharing / team surface

Where review material reaches people.

- team or group selection, per-athlete assignment, comments and replies, watch state
- primary actions: share to team/group/individual, exchange video with another team, message the group

### Live surface (where supported)

- live tagging during the game; streaming video and data to the bench; in-session feedback

## Important Rules / Behaviors

### Analysis is references, not re-edits

The working unit is a tag or clip that points into the original footage. Breakdown does not consume or alter the recording; the same footage supports unlimited event vocabularies and review assemblies. This is what makes the library a season-long record rather than a pile of edited files.

### The library is the memory

The value compounds over time: last month's events are filterable against this month's, and an athlete's attempts accumulate into a comparison record. Products that lose the library (one-off markup tools) lose the Type's central payoff.

### Feedback lives on the footage

Comments and drawings attach to specific moments and are visible to the athletes they concern. The review loop is anchored in the video itself, not in a separate discussion thread.

### Capture posture does not change the model

Whether footage arrives from a vendor camera, a phone, or an import, the breakdown → markup → review loop is the same. Products that make capture the entry point still reduce to this loop once footage lands.

### Live and post-game are one model at two speeds

The same event vocabulary is applied in real time during games and again while scrubbing afterwards. Live work is provisional; post-game work refines it.

### Highlights are a byproduct

Exportable highlight reels and MP4 downloads exist in most products, but they are outputs of the analysis layer. A product whose center is producing highlights for an audience has drifted toward media/fan territory.

## Variants

The Type is realized in several recognizable shapes:

- **Team cloud platform** — upload from any camera, tag, share, and exchange at team/club scale; dominant in schools, universities, and clubs (e.g., Hudl)
- **Veteran specialist suite** — desktop-lineage tooling with game-analysis and motion-analysis poles, subscription ladders, federation/pro and education customers (e.g., Dartfish)
- **Desktop-license breakdown suite** — tiered licensed software with a local video database, tagging windows, and a cloud companion for sharing (e.g., Nacsport)
- **Capture-first bundle** — vendor camera or phone setup with automatic upload and AI event detection, aimed at grassroots/amateur clubs (e.g., Veo)
- **Mobile-first technique app** — phone capture, frame-by-frame annotation, direct coach-to-athlete sharing for individual sports and private coaching (e.g., OnForm)
- **Elite code-window analysis** — fully custom event vocabularies and multi-angle live analysis for professional analysis departments (sold as separate products by the same vendors)

A variant remains a **Variant** unless it changes users, core objects, workflow, or rules so much that the core model no longer applies — as happens when the center moves to opposition/tactical content (Tactical Analysis territory), to measurement corpora (Sports Performance Analytics), to external-athlete evaluation (Sports Scouting), or to the coach–client business relationship (Sports Coaching Platform).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Video Editor / NLE | adjacent | timeline editing that renders a finished program; no sport-contextualized library, no tagged-event model, no team review loop |
| Tactical Analysis Platform | sibling, shared tooling | centers opposition/tactical match content and next-opponent preparation; this Type centers own-team/own-athlete footage for coaching review — center-of-gravity seam inside one tooling family |
| Sports Performance Analytics | complementary | centers a quantified measurement corpus over an athlete population; here the corpus is footage with markup; tag-derived stats sit at the seam |
| Sports Scouting Platform | downstream / upstream handoff | centers an external-athlete registry + evaluation with video as evidence; scouting content is commonly pushed into video-analysis workspaces for coaching work |
| Sports Coaching Platform | capability-slice neighbor | centers the coach–client relationship (roster, sessions, exchange, business machinery); the analysis suite is one medium inside it; standalone products center the tooling itself |
| Athlete Management System | complementary | owns the programming loop (plan → assign → deliver → track); video review feeds preparation but assigns nothing |
| Media Asset Management | different purpose | media ingest/catalog/distribution logistics for media organizations; sport-agnostic even when the footage is sports |
| Video Streaming Platform | adjacency | livestream add-ons exist here, but audience-facing distribution without library/breakdown/review is a different Type |
| Referee Management / officiating replay | different user | VAR-style replay serves officials' decision loops; vendors sell it as a separate product line from coaching analysis |

The most important boundary is with **Tactical Analysis Platform**: the two Types share tooling (tagging, telestration, match footage) and mid-market products often serve both uses. The seam is the center of gravity — whose footage is the record, and for which loop (own-team coaching review vs opposition/tactical preparation). The elite market separates them into distinct products.

## Representative Products

- **Hudl** — cloud team video platform; upload, breakdown, playlists, feedback, video exchange; dominant from high school through professional tiers
- **Dartfish** — veteran specialist with game-analysis and motion-analysis product poles; federation, professional, education, and healthcare customers
- **Nacsport** — desktop-license breakdown suite (tiered editions) with tagging windows, live bench streaming, and a cloud sharing companion; grassroots to professional
- **Veo** — capture-first bundle (AI camera or two-phone setup) with an editor for AI/manual event breakdown; grassroots and amateur clubs
- **OnForm** — mobile-first technique-analysis app for individual coaches; straddles into coaching-platform territory with its student roster and business machinery

The defining core was checked across the cloud-platform, desktop-license, capture-first, and mobile-first postures, and against the analog game-film practice and the 1990s–2000s desktop era, so the definition does not depend on any one delivery model, capture fashion, or era.

## Sources

Research date: **2026-09-09**

- Hudl — product page: https://www.hudl.com/en_gb/products/hudl (plus product-family pages for Sportscode, Studio, Assist, Focus)
- Dartfish — home, game analysis, and pricing pages: https://www.dartfish.com/ , https://www.dartfish.com/game , https://www.dartfish.com/plans
- Nacsport — home page and manuals hub: https://nacsport.com/ , https://www.nacsport.com/manuals.php
- Veo — product pages and help center: https://www.veo.co/ , https://www.veo.co/product/veo-editor , https://support.veo.com/hc/en-us (including the "Watching and analyzing" category)
- OnForm — home page and FAQ: https://onform.com/

> Sourcing limitation: Hudl's help center was not reachable from the research environment (JavaScript-rendered portal error), so claims about the market leader rest on its official product pages. Only Veo's help-center structure was reached at documentation level; no vendor's full operational article set was read. Precise operational details (permission models, storage quotas, plan limits, frame-rate figures) are therefore not asserted in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary review against the neighboring sports-software Types are recorded in the paired Research Notes.
