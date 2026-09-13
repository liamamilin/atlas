# Research Notes — Worship Planning

Research date: 2026-09-09
Leaf: Worship Planning (DIRECTORY.md §25, Nonprofit, Membership & Religious Organizations)
Slug: worship-planning

## Research Goal

Understand what Worship Planning software actually is as an Application Type: what a "service plan" contains, how songs/media/notes/people attach to it, how the plan reaches the team that produces the service, where the boundary lies against Ministry Scheduling, Sermon Management, Worship Presentation Software, ChMS, and event/agenda tooling — and whether the Type is one product family or just a capability of neighboring Types.

Flags to discharge this pass:

1. **ministry-scheduling (§25, processed 2026-09-08)** — forward flag: "tightest seam in the family — bundling vendors (PCO 'Worship planning & scheduling', Tithe.ly 'Service Planning' with songs/setlists) join planning-the-content with scheduling-the-people … expected outcome keep-both with a content-vs-people seam, but joint review recommended when that pass runs."
2. **sermon-management (§25, processed 2026-09-09)** — forward flag: "seam = message-as-record vs service-occasion organization; they meet at the service plan's sermon slot — Elvanto docs show 'the sermon' as a service-plan section … expected keep-both, confirm at that pass."
3. **religious-volunteer-management (§25, processed 2026-09-09)** — noted: "worship planning joins scheduling with service content (order, songs); this Type spans all ministries, not only worship. FellowshipOne sells Worship Planning (with volunteer scheduling) and Volunteer Management as separate suite members."
4. **presentation-application (§03.04, processed 2026-09-08)** — advance note for worship-presentation-software (unprocessed): live lyric/scripture display expected to be defined by its own live-display/liturgy/service semantics; cross-reference recommended from this side.
5. **event-agenda-management (§26, processed 2026-09-07)** — "worship-planning noted as a distant order-of-service analog — no merge proposed" — acknowledge.
6. **church-management-system-chms (§25, processed 2026-09-07)** — classified worship planning as a capability slice existing both as ChMS module and standalone specialist; confirm from this side.

## Initial Boundary

Hypothesis before research: Worship Planning products organize *what happens in a worship service* — an order of worship (songs, readings, sermon slot, announcements, media) for a dated service occasion — and distribute that plan to the people who make the service happen (worship team, AV, preacher) with the attachments each needs. Closest neighbors:

- Ministry Scheduling — *who serves*, not *what happens* (positions × occasions).
- Sermon Management — the *message as a record* (library, publication), not the service occasion.
- Worship Presentation Software — *live display during* the service, not preparation before it.
- ChMS — the record core; worship planning is a slice that can bundle into it.
- Event Agenda Management (§26) — program/agenda for a conference; different users and cadence.

Unknowns going in: is volunteer scheduling definitional or common? Is a song library definitional? Does a non-evangelical (liturgical) pole exist in product form? Is a live-run mode part of the core?

## Research Questions

1. What is the unit of record — plan, occasion, service type? What does a plan contain (items, sections, item types)?
2. How do songs/setlists integrate (library, keys, arrangements, transposition, chord charts, lyrics)?
3. How do people assignments attach to the plan, and how deep does the scheduling loop go (notify, accept/decline, swap, availability)?
4. What is the plan's lifecycle (template → schedule → fill → confirm → rehearse → run → archive)?
5. How is the plan delivered to the team (apps, print, public view, per-role views)?
6. What rehearsal machinery exists (audio parts, looping, sheet-music apps, practice tracking)?
7. What happens at the seams: planning→presentation hand-off, sermon slot, scheduling loop?
8. What denominational/segment variants exist (evangelical setlist vs liturgical Ordo)?
9. Does the Type stand alone in the market, or only as a ChMS module?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Planning Center Services | standalone specialist (separately-priced product of a modular suite); US market leader, "trusted by over 78,000 churches" | richest operational copy; straddles planning+scheduling; live-run mode |
| Elvanto (a Tithe.ly company) | ChMS-bundled worship module; international vendor (AU heritage, multi-region sites) | bundling pole; run sheets + live run sheets |
| WorshipTools Planning | free standalone app in a worship-tools family (Planning/Presenter/Charts/Community/Rehearse) | prep→display pipeline inside one vendor family; small-church tier |
| WorshipPlanning.com ("Planning", Ministry Brands) | long-lived standalone specialist | planner/helper role split; explicit planning→presentation integration copy |
| Source & Summit | Catholic liturgical preparation pole | non-evangelical shape: Ordo/Order of Worship assembly, missal/music program, NO volunteer scheduling — boundary-critical negative case |

Rejected/considered: Faithlife Proclaim (prep-to-display product; unreachable ×2 this pass — recorded as sourcing limitation, evidenced indirectly via WorshipPlanning.com's integration copy and WorshipTools' own Planning↔Presenter sync); OnSong-class musician repertoire apps (below the Type — musician tool, no service-occasion plan); FellowshipOne (module pole already covered by sibling passes' evidence).

## Sources

All fetched 2026-09-09 (Tier 2 product pages unless noted):

- Planning Center — https://www.planningcenter.com/services (Services product page)
- Elvanto — https://www.elvanto.com/features/worship/ (Worship feature page) + https://www.elvanto.com/features/
- WorshipTools — https://www.worshipextreme.com/ and https://www.worshipextreme.com/en-us/planning (Planning product page)
- WorshipPlanning.com — https://www.worshipplanning.com/ (Planning product page)
- Source & Summit — https://www.sourceandsummit.com/ (Digital Platform page)

Sourcing limitations:

- Faithlife Proclaim: proclaimonline.com timed out; faithlife.com/proclaim timed out (2 attempts each pattern) — abandoned per network rule. The planning→presentation seam is therefore evidenced from the planning side (WorshipPlanning.com's Proclaim integration copy; WorshipTools' Planning↔Presenter sync), not from Proclaim's own docs.
- Planning Center help-center articles were not individually fetched this pass; last pass reached only category listings. All PCO claims below are from the vendor's own Services product page (Tier 2). No precise operational rules (notification triggers, numeric limits) are claimed from PCO.
- Source & Summit: homepage/digital-platform copy only; help center not fetched. Liturgical-pole claims are calibrated to that level.

## Product Observations

### Planning Center Services (planningcenter.com/services) — Layer A

- Positioning: "Worship planning & scheduling" — one product in a modular suite; "Service planning and volunteer scheduling, for any team"; "Worship planning, volunteer scheduling, team communication, and rehearsal tools all in one place."
- FAQ widens scope beyond worship: "Is Services just for worship teams? Not at all! Services is for anyone who needs to coordinate volunteers or plan services, regardless of the ministry area."
- **Service Types**: "Create a Service Type for any kind of service at your church, like Traditional, Contemporary, Liturgical, and Youth. Store plan information and volunteer teams under each type."
- **Order of service**: "Set a detailed order for your services. Give your services a step-by-step flow so your whole team can know what's happening and when." Items: "Build your service order line by line by adding different items, such as songs, the sermon, announcements, and communion." Drag to rearrange; color-code rows; attach files (songs, media, documents).
- **Plan notes**: "store information your volunteers need to be prepared, like sermon notes or special reminders."
- **Service times**: single or multiple services; add volunteers to them.
- **Share your plan**: "Allow your entire team to see the service plan, or provide a public view of the plan."
- **Scheduling**: teams with leaders and custom positions; schedule far out; **Matrix** to view multiple plans at once; **templates** for regular teams/items; auto-schedule by recency/preferences/blockouts; blockout dates; signup sheets; household preferences; reminder emails.
- **Song library**: arrangements per song, multiple keys, select best key for the band, tags (fast/communion), "top songs across all churches over a six-week period"; transpose "update your chord charts and import the audio files to match"; integrations RehearsalPack, SongSelect (CCLI), PraiseCharts, MultiTracks for lyrics/chord charts/audio.
- **Rehearsal**: mobile media player ("listen to entire songs, hear just their parts, or even loop a specific section"), Apple CarPlay/Android Auto; **Music Stand** app ("annotate and swipe through sheet music with a foot pedal").
- **Services LIVE**: "Show your team what service item is happening in real-time so everyone can stay on track."
- Also: media library (images/docs/videos for future services), permission levels, plan templates, **CCLI reporting** ("Report your song usage to CCLI automatically"), series naming (title + artwork on plans).
- Pricing by number of team members; free tier (5).

### Elvanto Worship (elvanto.com/features/worship) — Layer A

- Positioning: ChMS feature area: "Running worship services and managing volunteers"; "Create run sheets, schedule your volunteers, access your song database, lyrics and chords."
- **Service Planning**: "Create detailed service plan/run sheets for your team that can be viewed online or printed depending on your needs."
- **Volunteer Positions**: "Predefine your departments & positions and assign volunteers"; scheduling based on availability; auto-schedule; teams; volunteer login (view roster, submit unavailability); swap & replace; scheduling preferences; automated reminders ("follow-up those who have not yet responded to their pending schedule"); SMS & email with templates.
- **Song database**: "your very own songs database for the worship team, and add different arrangements"; lyrics & chords stored, transpose into different keys; chord chart transposing ("automatically transpose into any key"); SongSelect integration.
- **Files/media**: upload and share files and media with your team.
- **Multi-service**: "Edit Multiple Services — quickly manage multiple services side-by-side and easily drag and drop volunteers between them."
- **Service Templates**: "predefine details of all your recurring services."
- **Reports**: on service, volunteers, and songs.
- **Live Run Sheets**: "View a live feed of the current service plan/run sheet along with progress, countdowns, notes and live chat."
- Mobile companion app (accept, decline, swap, replace, view schedule).

### WorshipTools Planning (worshipextreme.com/en-us/planning) — Layer A

- Positioning: "Service planning and scheduling that's volunteer friendly and free!"; one of five companion apps (Presenter = presentation software; Charts = chord charts/sheet music; Community = church database; Rehearse = rehearsal tool).
- **Build Your Service**: "Build your service flow, add items, songs, notes and details. Your service flow instantly syncs with Presenter and Charts, build once and done! Your service is sharable and printable, so everyone is on the same page."
- **Schedule Volunteers**: "Schedule and notify volunteers all in one place. When a volunteer is added to a service, they are notified and can accept or decline a service request."
- **Rehearsal**: "Give your team everything they need to come prepared, including direct integration with Rehearse … connect to Apple Music and Spotify and easily import charts from CCLI SongSelect and Loop Community."
- **Messages**: "Easily message your teams by name, role or service … reply and chat in realtime."
- **Lyrics presentation**: "Songs and services sync to the cloud, allowing you to open in Presenter, WorshipTools' presentation software."
- **Charts**: "songs and services sync to the cloud, allowing your worship team to access chord charts in Charts instantly."
- **CCLI auto-reporting**: "WorshipTools will send the songs used in your services directly to CCLI."
- Mobile apps iOS/Android; runs in browser.

### WorshipPlanning.com "Planning" (Ministry Brands) — Layer A

- Positioning: "Planning's cloud-based software makes it easy to organize and communicate"; "Ready for Weekend Services?"
- **Stated workflow** (vendor's own "How does it work?"):
  1. "**Plan** your service details with an easy-to-use worship flow editor. Add or import song details, upload files, and add notes for yourself or your team."
  2. "**Schedule and Notify** team members one week at a time or for multiple months. Team members are notified via email, text, and even Facebook. They can 'accept' or 'decline', and also access the service details you've set."
  3. "**Update** the worship flow and find substitutes to serve as needed. Since the plans are centrally stored in the cloud, you and your team can securely access them from anywhere, instantly."
- **Worship Flow Editor**: "intuitive drag-and-drop worship flow editor allows you to plan the fine details, or just a general set list"; marketing copy argues "you really need more than a simple text editor to effectively plan your worship service."
- **Songs Organizer**: 20+ fields (key, tempo, capo, lyrics…); CCLI SongSelect import; attach files; add songs on-the-fly while building a worship flow; CSV import (incl. date last performed); link Spotify/YouTube/Amazon; transpose keys for MP3 and text chord charts; performance histories by date range and location.
- **File Storage**: unlimited; MP3 transposer; audio "stream only" option; file access report ("see which musicians are actually practicing before rehearsal"); CCLI Rehearsal License reporting.
- **Mobile web app**: manage flow, sign-up to serve, respond to assignments, block availability, listen to attached audio, find team contacts.
- **Presentation Options**: "It is easy to go from worship flow to slides… Our integration with Proclaim Church Presentation Software makes building your presentation a snap. Or, if you use another program, slides can be centrally stored with each song in your library, then easily downloaded by your tech team to merge together." (Direct planning→presentation seam evidence from the planning side.)
- Integrations: SongSelect, Church Community Builder (ChMS), Faithlife Proclaim, OnSong, LifeWay Worship, Spotify, YouTube, Amazon.
- **Roles**: pricing by "Planners" (1/5/10/1000) vs unlimited "Helper Accounts" — an operator/viewer-participant split.
- Testimonials: "keeps a record of basically every detail of our services"; "Before I tried Planning, I was making schedules in Excel and we just had a file cabinet with the music to all our songs."

### Source & Summit (Catholic liturgical pole) — Layer A

- Positioning: "integrated digital liturgy preparation system" for Catholic parishes; "assembled … in a single, dynamic, sharable, printable **Order of Worship**."
- **Liturgy Preparation**: "Select from Music Suggestions & Texts; Change Keys, Select Verses, Adjust Format."
- **Music libraries**: "Hymns, Antiphons, Mass Settings; English, Latin, Spanish; Upload Your Own Digital Scores."
- **Custom Resource Creation**: "Edit and configure all of the elements of your **Ordo** and easily produce custom booklets, music packets, and music image files."
- **Program Coordination**: "Share your Ordos with your musicians, enabling them to download music for their role and learn their parts through interactive audio playback; Share Ordos with Groups; View Music Scores by Role."
- Product surface shows ordo-item vocabulary ("OPENING HYMN, ENTRANCE CHANT", key/verse controls, modern and square notation).
- **Licensing**: bundled "hassle-free" licensing — "no music reporting required" for native libraries (contrast with CCLI-reporting pattern of the evangelical pole).
- **No volunteer scheduling anywhere on the page** — the liturgical pole carries the plan-of-record + distribution legs without the people-scheduling loop.

## Cross-product Comparison

| Structure | PCO Services | Elvanto | WorshipTools Planning | WorshipPlanning.com | Source & Summit | Layer |
|---|---|---|---|---|---|---|
| Service plan = ordered item flow for a dated service occasion | order of service, line-by-line items (songs/sermon/announcements/communion), drag reorder, colors | service plan/run sheets, online or printed | service flow: items, songs, notes; sharable & printable | worship flow editor, drag-and-drop, "fine details or just a general set list" | Order of Worship / Ordo assembled from music & texts | A ×5 |
| Occasion scaffolding: service types / recurring templates / series | Service Types (Traditional/Contemporary/Liturgical/Youth); plan templates; series naming | service templates for recurring services | — | schedule one week → multiple months | Ordo per Mass (liturgical calendar) | A ×4 |
| Song library w/ keys, arrangements, transposition | arrangements, keys, tags, transpose; SongSelect/PraiseCharts/MultiTracks/RehearsalPack | song database, arrangements, lyric/chord transposition, SongSelect | SongSelect import; sync with Charts app | 20+ fields (key/tempo/capo), CCLI import, MP3+chord transposition, performance history | hymns/antiphons/Mass settings; change keys, select verses | A ×5 |
| Preparation content attached to plan items (files/media/notes) | attach songs/media/documents; plan notes; media library | upload & share files and media | notes + files in flow; sync to Rehearse | notes, files, stream-only audio | practice music & recordings; printable packets | A ×5 |
| Team-facing distribution (each contributor sees their part) | share plan with team (or public view) | run sheets for team; volunteer login | "everyone is on the same page"; app sync | team members "access the service details you've set"; mobile | share Ordos with musicians; scores by role | A ×5 |
| Volunteer scheduling inside the product | full loop (teams, positions, blockouts, auto-schedule, signup sheets, reminders) | full loop (positions, availability, auto-schedule, swap/replace, reminders) | notify + accept/decline | notify (email/text/Facebook) + accept/decline + substitutes + availability | **absent** | A ×4 |
| Rehearsal support | media player (parts, looping), Music Stand sheet-music app | reminders; (rehearsal depth via mobile) | Rehearse integration; Apple Music/Spotify | audio streaming; access report ("who is practicing"); OnSong | interactive audio playback; download music for their role | A ×5 |
| Live/run mode | Services LIVE (current item broadcast to team) | Live Run Sheets (progress, countdowns, notes, chat) | — | — | — | A ×2 |
| Licensing/usage reporting | CCLI reporting automatic | — | CCLI auto-reporting | CCLI rehearsal-license reporting | bundled licensing, "no music reporting required" (native library) | A ×4 |
| Print output | public view of plan | printed run sheets | sharable and printable | — | printable Order of Worship, booklets, music packets | A ×4 |
| Planning→presentation hand-off | — (Publishing product separate; Music Stand is rehearsal-side) | — | syncs service to Presenter (lyrics presentation) | Proclaim integration ("worship flow to slides"); slides stored per song | music image files export | A ×3 |
| Team communication | app chat + reminders | SMS & email, templates | messages by name/role/service, realtime chat | email/text/Facebook; reminders | — | A ×4 |
| Roles/permissions | permission levels; team leaders | departments/positions/teams | — | Planners (paid seats) vs Helper Accounts (unlimited) | scores by role | A ×4 |
| Reports | — | service/volunteer/song reports | — | file-access report; song performance histories | — | A ×3 |
| ChMS linkage | module of modular suite (People etc.); FAQ: not just worship teams | feature of full ChMS | Community app is a separate companion | integrates Church Community Builder (external ChMS) | parish program (missal/music), no ChMS claim on page | A ×5 |

Reading of the matrix:

- Present in 5/5: plan-as-ordered-items; song/media content layer; team distribution; rehearsal-adjacent support. These are the Type's stable structures.
- Present in 4/5: volunteer scheduling, licensing reporting, print, communication, roles. Strong "common" signals — but Source & Summit proves the Type stands without the scheduling loop, and licensing reporting is licensing-regime-dependent (CCLI world vs bundled-licensing world).
- Present in 2–3/5: live-run mode, presentation hand-off, reports. Variant/optional.
- The evangelical "setlist" shape (band + songs + charts + CCLI) dominates 4/5 samples; the liturgical Ordo shape replaces setlist machinery with liturgical-text/music assembly and print output, and drops scheduling. The shared abstraction is the **order of worship as an assembled, distributed plan**, not any particular item type.

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Two jointly-held structures over the congregation's worship-service life:

1. **The service plan of record** — a persistent, ordered, item-based plan for a dated worship-service occasion: the order of worship formalized. Items carry worship-service content (songs, readings/sermon slots, announcements, media, liturgy) and can be added, arranged, and annotated. Remove → a song list or task list with no service-shaped order; a generic to-do/calendar.
2. **The team-facing preparation loop** — the plan is distributed to the people who make the service happen; each contributor sees their parts, the notes, and the preparation content (files, lyrics, charts, media, timings) needed to prepare and rehearse. Remove → a private order-of-worship document: a planner the team never sees — below the Type (document-editor territory).

Domain binding: the occasions are worship services of a congregation (embedded in leg 1); the users are the congregation's service-production team.

Joint load-bearing:

- 1 without 2 = a worship-flow template document (word processor with a good template) — not an application of this Type.
- 2 without 1 = team messaging/notification with nothing planned.
- A song/chord-chart library without both = musician tooling (Charts-class apps), not worship planning.

Historical check (§24): the pre-software practice satisfies both legs — the printed order of worship/bulletin (an ordered item plan for a dated service) plus the rehearsal file (charts, recordings, run sheet distributed to musicians/AV/preacher). The liturgical tradition's Ordo is centuries old. No modern machinery (cloud, apps, accept/decline, CCLI) is named in the definition. **Historical check PASSED conceptually.**

### L1 — Common Mature Structure

Present in most sampled products; makes the Type practical, not definitional:

- song library with keys, arrangements, transposition, lyrics/chord charts (5/5)
- attachments/media on plan items and songs (5/5)
- volunteer scheduling attached to the plan: positions, notify, accept/decline, availability, substitutions (4/5)
- service types, templates, recurring series, multi-service editing (4/5)
- reminders and team communication (4/5)
- roles/permissions (planner vs participant/viewer) (4/5)
- print output of the plan (4/5)
- licensing/usage reporting (CCLI-pattern) (4/5, regime-dependent)

### L2 — Variant / Optional Structure

- live-run mode (current item broadcast to the team) — 2/5
- presentation hand-off (flow→slides sync or export) — 3/5, depth varies from file exchange to live cloud sync
- reports/analytics — 3/5
- liturgical-calendar/Ordo machinery and printed worship-booklet production — liturgical pole (Source & Summit); the evangelical pole substitutes setlist machinery
- public (non-member) view of plans — 1/5 observed
- scheduling depth: from simple notify+accept to full availability/auto-schedule/swap machinery — a depth/bundling axis that crosses into Ministry Scheduling territory

### L3 — Vendor-specific (Research Notes only)

- PCO: Matrix multi-plan view; Music Stand app with foot-pedal page turns; RehearsalPack/PraiseCharts/MultiTracks/RehearsalMix integrations; "top songs across all churches over a six-week period" (cross-church aggregate); CarPlay/Android Auto; pricing by team members with storage tiers; series artwork.
- Elvanto: drag-and-drop volunteers between services side-by-side; SMS templates; volunteer swap/replace; multi-region marketing sites.
- WorshipTools: free model; companion-app family (Presenter/Charts/Rehearse/Community) with cloud sync between Planning and the companions; Loop Community integration.
- WorshipPlanning.com: Facebook notifications; stream-only audio with file-access surveillance report; unlimited storage; Planners-vs-Helper pricing; OnSong integration; CSV import with last-performed date; carrier pigeon support channel.
- Source & Summit: missal/pew-resource products; square notation; Ordo element editing; bundled licensing with no reporting; English/Latin/Spanish libraries.

## Rejected Findings

- "Volunteer scheduling is definitional" — REJECTED. 4/5 sampled, but Source & Summit is squarely a worship-planning product with no volunteer scheduling; the scheduling loop is Ministry Scheduling's defining core. Within this Type it is a common bundled capability whose depth varies.
- "Setlist/song focus is definitional" — REJECTED as stated. Plans include songs, sermon, announcements, communion (PCO), liturgy texts and chants (Source & Summit). The band/setlist shape is the dominant market realization, not the definition.
- "Live-run mode is definitional" — REJECTED (2/5).
- "Planning→presentation output is definitional" — REJECTED (3/5, and the deepest observed forms are hand-offs; the display act belongs to Worship Presentation Software).
- "CCLI reporting is definitional" — REJECTED. It follows the CCLI licensing regime (US/anglophone church-music licensing); Source & Summit's bundled-licensing pole needs no reporting. Licensing-reporting is regime packaging.
- "Worship Planning = a capability slice of ChMS only (alias)" — REJECTED. Standalone, separately-sold specialists exist (PCO Services priced independently, WorshipPlanning.com, WorshipTools Planning free-standing). Module realization is a packaging variant, consistent with the ChMS pass.
- "Worship Planning = Ministry Scheduling with songs" — REJECTED. The content-vs-people seam holds: Source & Summit (plan without scheduling) vs Ministry Scheduler Pro (scheduling without planning) bracket the family from both sides.

## Boundary Findings

1. **vs Ministry Scheduling (§25) — DISCHARGES the ministry-scheduling forward flag from this side; keep-both RATIFIED on the content-vs-people seam.** Bundling vendors (PCO "Worship planning & scheduling", Tithe.ly/Elvanto) carry both loops in one product, but the loops are structurally distinct: Ministry Scheduling's unit is the person × position × occasion assignment forming the serving schedule; Worship Planning's unit is the plan's content for the service occasion. Bracket proof: Ministry Scheduler Pro has zero plan-content machinery (that pass's evidence); Source & Summit has zero volunteer scheduling (this pass). Churchteams' roadmap (scheduling shipped, service planning a separate future feature) treats them as distinct capabilities. Remove position-filling and keep order/songs → Worship Planning; keep position-filling without plan content → Ministry Scheduling. Joint review satisfied: this pass provides the second side.
2. **vs Sermon Management (§25) — DISCHARGES the sermon-management forward flag from this side; keep-both RATIFIED on the message-record-vs-service-occasion seam.** The plan carries a sermon *slot* (an item with notes/timing — PCO plan notes mention "sermon notes"; Elvanto's plan includes "the sermon" per that pass's evidence), while Sermon Management holds the *message as a record* that outlives the service (library, publication). The plan organizes the occasion; the sermon record organizes the message. They meet at the slot; neither implies the other (Source & Summit plans have no sermon-record machinery in evidence; a church with a sermon library needs no plan tool). Confirms the expected keep-both.
3. **vs Worship Presentation Software (§25, unprocessed)** — seam = preparation/organization vs live in-service display. Planning software organizes what will happen and equips the team before the service; presentation software displays lyrics/scripture/slides to the congregation during it. They meet at the hand-off: WorshipPlanning.com integrates Proclaim ("go from worship flow to slides"); WorshipTools Planning syncs its flow to its sibling Presenter; slides stored per song for tech-team download. This pass acknowledges the presentation-application pass's advance note: the live-display Type is expected to be defined by its own live-display/liturgy/service semantics, not absorbed by generic presentation grammar. Worship-presentation-software pass should ratify from its side; expected keep-both.
4. **vs Church Management System / ChMS (§25)** — confirms the ChMS pass's capability-slice classification from this side: the loop exists as a ChMS module (Elvanto Worship), as a separately-priced suite product (PCO Services), and as standalone specialists (WorshipPlanning.com, WorshipTools). ChMS boundary unchanged (record core is the center there).
5. **vs Religious Volunteer Management (§25)** — consistent with that pass: worship planning centers the service's content; volunteer-lifecycle machinery (recruiting, screening, training) is upstream and bundle-dependent. The two may be bundled (PCO, FellowshipOne per that pass) but neither implies the other.
6. **vs Event Agenda Management (§26)** — distant order-of-service analog as that pass noted. Distinctions: recurring weekly cadence vs one-off occasions; congregational service-production team vs conference speakers/exhibitors; worship content vocabulary; no attendee registration/tickets. No merge.
7. **vs Calendar Application / Church Calendar surfaces** — service occasions are dated, but the managed unit is the plan and its content/people, not events, rooms, or registrations.
8. **vs musician tools (Sheet Music Reader, chord-chart apps, rehearsal apps)** — music content is one layer of the plan; standalone musician apps have no service-occasion plan of record. Products integrate with them (PCO Music Stand, WorshipPlanning→OnSong, WorshipTools Charts) rather than absorb them.

## Uncertainties

- PCO detailed operational rules (notification triggers, exact plan-permission granularity, LIVE-mode mechanics) not article-verified; all PCO claims are product-page level.
- Faithlife Proclaim unreachable ×2 — the presentation hand-off is evidenced from the planning side only; the worship-presentation-software pass should verify the seam from the display side.
- Source & Summit verified at homepage/digital-platform level only; ordo-editing depth and the volunteer-free posture are marketing-level claims (though the *absence* of scheduling on a full product page is a reasonably strong negative datum).
- Whether Catholic parishes also use evangelical-shaped products (Elvanto in Catholic contexts) was not verified; denominational mapping is directional, not exhaustive.
- The historical check is conceptual (paper order of worship/bulletin + rehearsal file), not source-verified against archival documents.
- A pure "bulletin/order-of-worship document builder" with no team loop was not sampled; if it exists it sits below the Type (document territory).

## Final Synthesis

Worship Planning is the congregation's service-production planning system. Its defining core is two-fold: the **service plan of record** — an ordered, item-based plan for a dated worship-service occasion (the order of worship formalized: songs, sermon slot, readings, announcements, media, liturgy) — and the **team-facing preparation loop** — the plan distributed to the people who produce the service, each seeing their parts, notes, files, and timings, with rehearsal support. Around that core, mature products commonly add the song library (keys, arrangements, transposition, charts), volunteer scheduling on the plan, templates and multi-service management, communication, print output, licensing reporting, and roles. The market realizes the Type as standalone specialists, separately-priced suite products, ChMS modules, free companion-app families, and a distinct Catholic liturgical pole (Ordo assembly + printed worship resources, no volunteer scheduling) — packaging and item vocabulary vary; the plan-of-record-plus-preparation-loop does not.
