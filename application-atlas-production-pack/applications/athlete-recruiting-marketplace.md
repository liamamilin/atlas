# Athlete Recruiting Marketplace

## Overview

An **Athlete Recruiting Marketplace** is a two-sided recruiting platform that connects prospective student-athletes with college recruiting coaches. Athletes (with help from parents or club/high-school staff) build recruiting profiles that enter a searchable network; college coaches search that network for recruits; and both sides can signal interest and communicate directly — all in service of one outcome: an athlete being recruited onto a college roster.

The defining core is small:

```text
Athlete recruiting profile (athlete/family/club-authored)
└── Coach/program accounts (demand side)
    └── Coach-side searchable discovery across the athlete pool
        └── Two-way interest and contact between the sides
            └── Placement orientation (recruiting outcomes, organized by class year)
```

Everything else commonly associated with these products — highlight video, view tracking, matching algorithms, club organization accounts, roster-need postings, human recruiting coaches, events — is widespread in current products but is not what makes the product a recruiting marketplace. The platform records progression toward placement (and often logs commitments), but the placement itself — the offer, the visit, the signing — happens off-platform. The researched products do not move money between the two sides; their revenue comes from subscriptions and services sold to athletes, families, and organizations.

When the athlete stops being an active participant (profiles authored by scouts over already-visible performers, no two-way exchange), the product is drifting toward a different Application Type (Sports Scouting Platform). When the exchange loses the recruiting purpose and becomes general networking, it is drifting toward a social network.

## Users & Context

The marketplace has two primary sides and two important intermediaries:

**Athlete side (supply):**
- student-athlete: builds and maintains the recruiting profile, researches colleges, contacts coaches, responds to coach interest
- parent/guardian: heavily involved in the US college context; products address parents directly, and some features (guardians as an audience for roster needs) acknowledge them
- club coach / high-school staff: in many sports the de facto manager of athletes' recruiting — maintaining organization and team profiles, promoting athletes to colleges, tagging suitable schools, monitoring engagement on their behalf

**Coach side (demand):**
- college head and assistant coaches and recruiting-coordinator staff, acting for their program across divisions (the US market spans NCAA D1–D3, NAIA, and junior-college levels); the coach side is typically free to use

**Context:** the work is multi-year and calendar-driven. Recruiting is organized around graduating class years; athletes typically start years before enrollment, and the process culminates in visits, offers, and a commitment that the platform may record but does not execute. The US college recruiting context is governed by athletic-association rules (eligibility, contact windows, what services coaches may subscribe to), and products operate — and advertise their compliance — within that regime.

## Core Model

### The Defining Core

Five properties. If any one is removed, the product is no longer recognizable as an athlete recruiting marketplace:

- **Athlete recruiting profile** — an identified prospective student-athlete represented by a profile carrying recruiting-relevant attributes: sport and position, recruiting class / graduation year, athletic measurables and statistics, academic information, and contact details. The profile is authored by or for the athlete — by the athlete, the family, or club/high-school staff. This authorship is what distinguishes the marketplace from a scouting platform, where evaluators compile athlete information without athlete participation.
- **Coach/program accounts** — college coaches and recruiting staff as authenticated participants acting for their programs. They are the demand side; without them there is no one to be recruited by.
- **Coach-side discovery** — coaches search and filter across the athlete profile population by recruiting criteria (class year, position, geography, athletic and academic attributes). The athlete pool is the searched corpus; this is the marketplace's central direction of discovery.
- **Two-way interest and contact** — athletes (or their proxies) can express interest in programs and initiate contact with coaches; coaches can express interest and initiate contact with athletes. The channel runs inside the platform, and interest signals (views, favorites, interest markers) are visible to the other side. Without it, the product is a static database.
- **Placement orientation** — the entire exchange exists to produce recruiting outcomes: a roster spot at the next level. Class years structure the demand (programs recruit specific upcoming classes), and the outcome — a commitment — is recorded by the platform rather than transacted by it.

### Standard Capabilities

Mature products commonly add the following. They make the marketplace practical; they do not define it.

- **Video and highlights** — the athlete's film is the centerpiece of evaluation: uploading video, embedding from external hosts, building highlight reels in the platform, and team/game film libraries. Video is the current center of gravity of athlete presentation, but profiles can exist without it (and did in earlier eras of the market).
- **Academic documents** — transcripts, GPA, and test scores alongside athletic attributes, because college recruiting evaluates the student and the athlete together.
- **Athlete-side college discovery** — a searchable college database (by division, academics, location) and a personal target list where athletes favorite schools, classify them by fit, and track progress with each.
- **Interest and view tracking** — both sides see engagement: athletes see that colleges viewed their profile or video (often with the identity of the viewer as a paid unlock); coaches see which athletes viewed their program or marked interest in it.
- **Roster-need publishing** — colleges can publish their open roster spots by class year; athlete profiles matching a published need are surfaced to that coach (and often to the athlete, who can see which schools need their position and class).
- **Matching and fit assistance** — from deterministic profile-to-need matching to algorithmic or expert-in-the-loop "best fit" analysis combining athletic, academic, and personal preferences.
- **Organization accounts** — club and high-school programs get their own organization/team profile hierarchy, manage their athletes' presence, promote athletes to colleges, tag suitable schools, and monitor engagement across the organization.
- **Coach-side evaluation workflow** — favorites and skips, private notes, sharing evaluations across the coaching staff, and exporting recruit data to CSV or to dedicated recruit-CRM tools.
- **Tracked messaging** — direct messages between the sides, with tracked profile links and delivery/view indicators; coach-side copies are often forwarded to institutional email.
- **Commitment records** — commitments logged and celebrated as the marketplace's outcome metric.
- **Educational content** — guides, eligibility explainers, recruiting calendars, webinars; recruiting is confusing enough that content is a standard layer.
- **Mobile apps** — at least for the athlete side; coach and event surfaces vary.

## How It Works

### The athlete/family loop

```text
Create profile (bio, sport/position, class year, stats, academics, contact)
→ add video / build highlight reels
→ profile becomes searchable to coaches
→ research colleges; build a target list
→ reach out to coaches (messages carrying the tracked profile)
→ see who viewed / who expressed interest; respond
→ (off-platform) calls, visits, offers
→ commitment; recorded on the platform
```

Completeness is the operating currency: a finished profile is what makes an athlete discoverable, and products explicitly frame every action — adding video, favoriting schools, messaging — as increasing exposure.

### The coach loop

```text
Register with the program (institutional email)
→ optionally publish roster needs / openings by class year
→ search or browse the athlete pool (filters: class year, position, location, academics, video availability, interest in my program)
→ open athlete profiles; watch video; read academics
→ favorite / skip; add notes; share with staff
→ contact the athlete (or see that they contacted you)
→ track communications; often export to the program's recruit CRM
```

The coach side is free in the researched market, and the discovery filters include reverse signals — athletes who have already expressed interest in the program — so the coach's search can start from warm prospects.

### The organization (club/high school) loop

```text
Set up organization, team, and athlete profiles
→ staff maintain and complete athletes' profiles and film
→ promote athletes to colleges (send profiles/messages on their behalf)
→ tag schools that fit each athlete
→ monitor engagement (which colleges are viewing which athletes)
→ guide athletes' target lists and process
```

In club-heavy sports, the organization account is the primary operating surface; the athlete's profile is managed as part of the club's roster of prospects.

### The matching loop

Both sides are matched in the middle: published roster needs are compared against athlete profiles (class year, position, attributes), and fit engines combine preferences, academics, and — in service-heavy products — expert evaluations of video and measurables. Matches surface as scoped feeds for coaches and as school suggestions for athletes.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product. The two sides normally work in separate authenticated portals (sometimes separate domains or apps).

### Athlete profile builder

The athlete's primary workspace.

- profile fields (identity, sport/position, class year, measurables, stats, academics, contact), video library, highlight-reel editor, transcript upload
- primary actions: complete and update the profile, add/embed video, publish

### Athlete home / discovery

Where the athlete drives the process.

- college search with filters (division, academics, location), roster-need indicators, suggested fits
- target list with per-school status
- activity feed: which colleges viewed the profile or video; notifications
- primary actions: search schools, favorite/tag, message a coach, view tracking detail

### Coach search / discover feed

The coach's primary entry surface.

- filterable athlete pool (class year, position, geography, athletic/academic criteria, video availability, interest in my program), saved searches, roster-need-matched feeds
- primary actions: search, filter, open profiles, favorite/skip

### Athlete profile (coach view)

The evaluation surface.

- athletic stats and measurables, academic information, video player with highlights and full film, contact details, club/team context
- primary actions: watch video, favorite/skip, add note, share with staff, contact athlete, export

### Messaging

Direct communication between the sides.

- threaded messages with tracked profile links; view/open indicators; coach-side forwarding to institutional email
- primary actions: send, reply, track

### Organization console (club/high school)

The staff surface for managing many athletes.

- organization/team/athlete profile hierarchy, engagement dashboards (who is being viewed, who is messaging), tagging tools, roster exports (printable/embeddable)
- primary actions: manage athlete profiles, promote athletes, tag fits, monitor activity

### Program profile (public/semi-public)

The college's face in the marketplace.

- program information, published roster needs by class year, staff
- primary actions (coach): publish/edit needs; (athlete): view, favorite, express interest

## Important Rules / Behaviors

### Visibility is earned by completeness

An incomplete profile is effectively invisible. Searchability and discoverability are gated on profile completion and content (video, academics), which is why products push completion as the first job.

### Class year is the organizing axis

Roster needs, search filters, target lists, and timelines are all structured by recruiting class / graduation year. A program's need is not "a point guard" but "a point guard in the class of 2028."

### Interest visibility is tiered

Both sides generate engagement signals, but who may see what varies: athletes commonly see that they were viewed for free and pay to see who; coaches see interest in their program as part of free access; organizations see engagement across their whole athlete population. Identity-of-viewer is a monetization and permission surface, not a fixed property.

### The coach side is free — and that is partly regulatory

In the US college context, products advertise free access for every coach and commit to providing the same standardized athlete information to all programs, because athletic-association rules constrain how recruiting services may sell athlete information to coaches. Compliance certification is a marketed feature. Athlete-side and organization-side features, by contrast, are commonly tiered behind subscriptions.

### Contact is shaped by governing-body rules

Recruiting communication is regulated in the US college context: athletic associations publish eligibility requirements and recruiting calendars, and products carry extensive guidance content about them. The platform provides the channel and the education; it does not adjudicate eligibility or enforce contact windows itself.

### The outcome is recorded, not transacted

Offers, official visits, and commitments happen off-platform. The marketplace logs commitments as its success metric; it does not process scholarship money or signing documents between the sides.

## Variants

- **Service-heavy marketplace** — human recruiting coaches, assessments, personalized game plans, and direct promotion sold as membership layers on top of the network (the largest player's model)
- **Self-serve freemium** — free profiles with paid unlocks (messaging, view identity, advanced filters); guidance delivered as content rather than people
- **Club-workflow-first** — organization accounts as the primary customer; athletes' profiles managed and promoted by club staff; common in club-centric sports
- **Association-branded networks** — the same platform powering official recruiting networks for sport coaches' associations under co-branded names
- **Events-extended** — live-event companion apps (event schedules, rosters, on-site evaluation) and event-operator products; sometimes packaged as separate product lines
- **Sport-scope variants** — many-sport generalists vs concentration in club sports; division coverage from D1 through junior college

A variant remains a variant as long as the defining core holds. If athlete participation disappears (evaluator-authored profiles, one-way exposure), the product belongs to the scouting side of the boundary.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Sports Scouting Platform | evaluator-side talent identification and evaluation over athlete/video registries; athletes are subjects, not participating marketplace members; no two-way recruiting exchange |
| Coach-side recruiting CRM (recruit pipeline tools) | manages a college staff's recruiting pipeline (contacts, communications, boards); no athlete registry; marketplace products export to these tools rather than replace them |
| Student Recruitment CRM / Admissions Management | institution-side admissions funnel over applicants; no athlete-authored athletic registry and no two-sided athletic discovery |
| Talent Sourcing / Candidate Search / Job Board (HR) | structural analog (registry + search + contact + hiring) in professional hiring; lacks athletic-recruiting semantics (class years, eligibility, video evaluation, club intermediaries) |
| Team Management Application / Youth Sports Management | administration of active teams (schedules, rosters, communication, registration); no next-level exposure or coach-side discovery |
| Sports Video Analysis | video breakdown as the product; in the recruiting marketplace video is profile content feeding evaluation, not the managed object |
| Casting Platform (media) | structurally similar talent-profile marketplace, but for casting roles in productions; different domain, participants, and outcomes |
| College search / directory products | college discovery without an athlete registry; recruiting marketplaces embed college search as one capability |

The most important boundary is with the Sports Scouting Platform: the two are easily confused because vendors and regulators use "recruiting" and "scouting" interchangeably. The structural test is participation — who authors the athlete's presence and whether the exchange is two-way.

## Representative Products

- NCSA College Recruiting — service-heavy market leader; memberships with human recruiting coaches atop a free network; publishes its NCAA compliance posture
- SportsRecruits — club-workflow-first platform; organization accounts, roster-need publishing and matching, coach side free
- CaptainU (Stack Athlete Recruiting) — freemium, app-first; four product lines spanning athletes, colleges, teams, and events

The defining core was checked against the market's earlier, pre-video era (text profiles and coach databases; pre-web equivalents such as recruiting guides and mailed highlight tapes) to avoid defining the Type by today's video-and-algorithms implementation.

## Sources

Research date: **2026-09-06**

Primary vendor surfaces (product and program pages):

- NCSA College Recruiting — https://www.ncsasports.org/ (homepage; /college-coach; membership page; NCAA compliance page)
- SportsRecruits — https://www.sportsrecruits.com/ (homepage; /athletes; /colleges; /clubs)
- CaptainU — https://www.captainu.com/ (homepage)

> Sourcing limitation: vendor help centers / knowledge bases were not reachable from the research environment on 2026-09-06 (repeated timeouts), and one intended sample (FieldLevel) was blocked (HTTP 403). Operational details that would normally come from help documentation — exact profile field lists, message mechanics, eligibility gates, numeric limits — are therefore described conceptually rather than precisely, and no precise vendor figures are stated in this document. Detailed observations, vendor-reported statistics, and the cross-product comparison are recorded in the paired Research Notes.
