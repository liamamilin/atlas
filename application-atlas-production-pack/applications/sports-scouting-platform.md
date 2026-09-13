# Sports Scouting Platform

## Overview

A **Sports Scouting Platform** is evaluator-side talent-identification software. It maintains a persistent registry of athletes, lets scouting and recruitment staff search and compare that registry to surface candidates, and captures their judgments — reports, ratings, notes — as a shared, searchable record of the recruitment team's work. The whole loop exists to serve player-acquisition decisions: which athletes to sign, draft, or recruit into a roster.

The defining core is small:

```text
Athlete registry (the scouted population as persistent records)
└── Evaluation records (scout-authored reports/ratings/notes against the club's framework)
    └── Identification-and-tracking loop (search → shortlist → track → decide)
```

One structural property separates this Type from its closest neighbor: **the athlete is the object of record, never a participating account**. Athletes do not author their profiles, signal interest, or exchange messages here. When athletes author profiles and contact flows in both directions, the product is an Athlete Recruiting Marketplace. When the center of gravity is measured performance of the organization's own athletes rather than external acquisition targets, it is Sports Performance Analytics.

## Users & Context

Primary users are the professionals who run talent acquisition for sporting organizations:

- **scouts** (field scouts attending matches, and video scouts evaluating remotely) — search for candidates, watch footage, write evaluations
- **recruitment/analyst staff** — maintain the player database, run comparisons, prepare reports for decision-makers
- **technical directors, sporting directors, general managers, and personnel leaders** — consume evaluations, manage shortlists and boards, make acquisition decisions

Secondary users include **agents** (evaluating players for their own portfolios) and **coaching staff** (consuming evaluations and film). Some platforms also serve media and data-licensing customers, but those are adjacent businesses, not the scouting loop.

The working context is a club, team, federation, or agency recruitment department. Work is rhythmic rather than continuous: it intensifies around **transfer windows** and **draft cycles**, when targets must be identified, evaluated, compared, and tracked to a decision under time pressure. Much of the daily work is remote — evaluating players through video and data before committing travel — with live scouting as the confirming step.

## Core Model

### The defining core

**1. The athlete registry.** The system's foundation is a persistent set of identified athlete records — the scouted population. Each record carries sport context: identity, position or role, current club/team and competition, career and biographical information, and commonly performance history. The registry is the anchor: every evaluation, clip, and list item attaches to an athlete record that persists as the player moves between clubs and seasons.

The registry's substrate varies by product philosophy, and the variation is real:

- a **vendor-operated content library** — the vendor licenses video and data from competitions worldwide and maintains the registry as part of the product
- a **user-built database** — the scouting department creates and maintains its own player profiles, importing data where available
- a **hybrid** — league data feeds, transfer-portal populations, or imports combined with the department's own entries

**2. The evaluation record.** Around the registry, the system captures what scouts conclude: reports, ratings or grades, and notes, attached to athlete records. Evaluations are typically recorded against an **evaluation framework** — the organization's report templates, criteria, and rating scales — so that different scouts' judgments about different players remain comparable across the department. Accumulated evaluations become the department's memory: a searchable body of prior work that outlives individual scouts.

**3. The identification-and-tracking loop.** The registry and evaluations are worked through a loop: search and filter the registry to surface candidates, collect them into **lists, shortlists, or boards**, compare them against each other and against the organization's needs, and track their status over time toward a decision. The loop is what turns a database into a working scouting operation.

### What the evidence layers add

Two content layers are so widespread in mature products that they shape how the core is used, though neither defines the Type:

- **Video evidence** — match footage, tagged events, and curated clips linked to athlete records and attached to evaluations. The economic argument is consistent across the market: evaluate through video before spending travel budget, then confirm in person.
- **Statistics** — match data, season aggregates, and advanced metrics on athlete profiles, giving evaluations a quantitative counterpart. In the most analytics-driven products, derived metrics (position-specific traits computed from tracking data) become an evaluation vocabulary in their own right.

### How the pieces relate

```text
Athlete registry
   │  search / filter / compare
   ▼
Candidates surfaced
   │  evaluate (video + data + live observation)
   ▼
Evaluation records (reports, ratings, notes — against the club's framework)
   │  collect & track
   ▼
Lists / shortlists / boards
   │
   ▼
Acquisition decision (sign / draft / recruit — made off-platform)
```

## How It Works

### Build or adopt the registry

A recruitment department starts from a registry: it subscribes to a vendor-operated library covering competitions worldwide, or it builds its own player database profile by profile, or it combines licensed data with its own entries. Athlete records accumulate biographical details, career history, performance data, and video links over time.

### Search and surface candidates

Staff query the registry — by position, age band, competition, club, physical attributes, performance metrics, or whatever criteria the organization's recruitment philosophy prioritizes. Results are narrowed with filters, and candidates are compared side by side; many products can also surface players similar to a given profile. The output of this stage is a set of candidates worth evaluating.

### Evaluate

For each candidate, staff assemble the evidence — full matches, tagged clips, statistics, prior reports — and record a judgment: a report written against the organization's template, a rating on its scale, notes on strengths and weaknesses. Evaluations are attributed to their author and standardized to the shared framework, so the department's criteria stay consistent even as scouts change. Video and data narrow the field before anyone travels; live observation confirms what the remote work suggested.

### Track and decide

Evaluated candidates are collected into shortlists, custom lists, or boards — often with grades attached — and tracked as their status evolves: new footage appears, ratings are revised, windows open and close. The platform supports the department's internal conversation — sharing reports, clips, and lists — up to the point of decision. The acquisition itself (contract, negotiation, signing) happens outside the platform; the scouting record ends where the deal begins.

### Capability tiers

**Defining core** — without these, not a scouting platform:

- persistent athlete registry with sport context
- evaluator-authored evaluation records against a shared framework
- search/compare/track loop toward acquisition decisions

**Standard capabilities** in mature products:

- video library with tagged events and curated clips
- statistics and advanced metrics on profiles
- comparison tools and similar-player finding
- shortlists, custom lists, boards with grades
- report templates and configurable rating scales
- internal sharing with roles/permissions
- import/export and handoff to video-analysis workspaces
- mobile/tablet companion for staff

**Common variants** (see Variants): registry substrate, analytics depth, sport scope, dual-use packaging.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Player search / database view

The working entry surface for identification.

- the registry queried through filters (position, competition, age, attributes, metrics)
- primary actions: run a search, refine filters, save a query, add results to a list

### Player profile

The athlete's record — the unit everything else attaches to.

- identity, photo, position, current club and competition, career history, performance data, video links, prior evaluations
- primary actions: open video, open/edit the profile, write a report, add to a list, compare

### Video / event viewer

The evidence surface.

- full matches, tagged event lists, curated clips; clips linked to the athlete and attachable to evaluations
- primary actions: watch, clip, tag, attach to a report

### Report editor

Where judgment is recorded.

- the organization's report template (criteria sections, rating scale, free-text notes), attributed to the author
- primary actions: rate, write, save against the framework, share internally

### Lists / boards

The tracking surface.

- shortlists, custom lists, comparison boards; grades and status per player
- primary actions: add/remove players, grade, reorder, share, export

### Comparison view

Side-by-side evaluation of two or more players (or a player against similar players) across metrics, traits, and video.

### Mobile / tablet companion

Staff access to profiles, clips, and reports from the stands or the road; some products support offline clip download.

## Important Rules / Behaviors

### The athlete is the object of record

There is no athlete-side account, authoring, or contact channel. Profiles are created by the vendor's content operation, by scouting staff, or by import — never by the athletes themselves. This is the structural line between a scouting platform and a recruiting marketplace, and it holds across the researched market.

### Evaluations are standardized and attributed

Reports and ratings are recorded against the organization's framework — templates, criteria, rating scales — and attributed to their author. The point is comparability: a department's evaluations must aggregate into one consistent body of judgment. Products treat the framework as configurable precisely because clubs differ in scouting philosophy and revise it over time.

### The registry substrate changes the product's behavior

A vendor-operated library offers breadth (competitions worldwide) but its content is licensed — in the sampled market's content-library products, availability follows rights agreements, is delivered on a delayed basis for professional use, and can lapse when an agreement expires. A user-built database offers control but depends on the department's own upkeep. Hybrid products mix both.

### The loop follows the acquisition calendar

Tracking intensifies around transfer windows and draft cycles, when target lists must be current and decisions made. Products reflect this rhythm — transfer-target status tracking, portal populations that update rapidly during windows.

### The record ends at the deal

The platform carries identification, evaluation, and tracking to the point of acquisition decision. Contracts, negotiation, and signing are out of scope (some vendors sell separate club/agent tools for that); downstream video work is handed off to video-analysis products rather than performed inside the scouting record.

## Variants

- **Content-library pole** — the vendor operates a licensed global video+data registry as the product; scouting workflow layers on top. Breadth of coverage is the value proposition (dominant in global football).
- **Analytics-first pole** — evaluation vocabulary derived from tracking data and predictive models, with film attached to every metric; oriented to roster construction and draft decisions (US college/pro football shape).
- **Workflow-first / self-serve pole** — the department builds its own database and frameworks, importing external data; sold to individual scouts, small clubs, and agencies.
- **Dual-use analysis + scouting** — one video+data library serving both coaching analysis and player evaluation; the scouting use is a center of gravity, not the only one (common in basketball/hockey).
- **Sport and region shapes** — global single-sport depth (football), multi-sport families (basketball/hockey), the US college/pro draft axis (football, baseball, hockey).
- **Youth/talent-development orientation** — dedicated youth-competition coverage for early identification.
- **Secondary audiences** — player agencies (portfolio evaluation), media and data licensing (adjacent businesses on the same content).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Athlete Recruiting Marketplace | closest sibling — vocabulary overlaps heavily in this market | the marketplace's defining core requires athlete-authored profiles and a two-way interest/contact channel oriented to placement; here the athlete is the object of record with no participation channel. Vendors themselves split the two (one sampled vendor sells separate "Recruiting" and "Player Personnel" products) |
| Sports Performance Analytics | adjacent — shares data substrates | analytics centers measured performance of an analyzed population for performance decisions; scouting centers external athletes as acquisition targets with evaluator-authored records. Player-evaluation modules inside analytics products belong here when external-player recruitment becomes the center |
| Tactical Analysis Platform | adjacent — shares match video | when match content is broken down for opposition/tactical purposes the center is the match, not the athlete; scouting video is evidence about players |
| Sports Video Analysis | downstream — handoff relationship | video-analysis products center editing/annotating footage (usually own-team) for coaching; scouting centers the registry + evaluation with video as evidence. Scouting content is commonly pushed into video-analysis workspaces for downstream work |
| Athlete Management System | adjacent — different population | AMS manages the organization's own roster (readiness, programs, daily operations); scouting manages external talent identification |
| Vertical Search / sports data providers | supplier relationship | a data feed or statistics database without evaluation records and a tracking loop is a data product; the largest scouting platforms expose their data as separate API products |
| Job Board / HR recruiting family | structural analog | registry + search + evaluation + hiring decision in a different domain; the sports Type is defined by athletic-evaluation semantics (video evidence, position frameworks, transfer windows, draft cycles) |

## Representative Products

- **Hudl Wyscout** — global football; vendor-operated licensed video+data registry with a dedicated scouting workspace (content-library pole)
- **Teamworks Player Personnel** — US college football (with baseball/hockey siblings); tracking-data-derived player traits, film, and evaluation boards (analytics-first pole)
- **ScoutDecision** — football; self-serve player database, scout reports, and transfer tracking for scouts, small clubs, and agencies (workflow-first pole)
- **Hudl Instat** — basketball and ice hockey; video library + statistics serving both coaching analysis and scouting (dual-use pole)

## Sources

Research date: **2026-09-09**

Primary vendor surfaces (product pages, one vendor FAQ, official product documentation pages):

- Hudl Wyscout — product page: https://www.hudl.com/en_gb/products/wyscout (wyscout.com redirects here)
- Hudl Wyscout — Scouting Area: https://www.hudl.com/en_gb/products/wyscout/scouting-area
- Hudl Wyscout — FAQ: https://www.hudl.com/en_gb/products/wyscout/faq
- Teamworks — Player Personnel for College Football: https://teamworks.com/scouting
- ScoutDecision — homepage and FAQ: https://scoutdecision.com
- Hudl Instat — product page: https://www.hudl.com/en_gb/products/instat

> Sourcing limitation: vendor help-center / support-community content was not reachable from the research environment on 2026-09-09 (the sampled vendor's support portal is a script-rendered community that returned no content; one intended US pro-league sample was unreachable after repeated transport errors). Workflow detail therefore comes from official product pages and one vendor FAQ rather than step-by-step operational documentation. Precise field vocabularies, rating-scale values, list limits, and pipeline stage names are intentionally not stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary checks against the recruiting-marketplace and performance-analytics passes are recorded in the paired Research Notes.
