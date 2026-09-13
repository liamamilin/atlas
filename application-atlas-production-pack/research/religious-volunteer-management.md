# Research Notes — Religious Volunteer Management

## Research Goal

Understand what a Religious Volunteer Management application is as an Application Type: what core structures define it, who uses it, how the volunteer work actually flows through the product, and where its boundaries sit against neighboring Types — Ministry Scheduling (§25, processed), the generic Volunteer Management System (§25, unprocessed), Church Management System (§25, processed), Religious Small-group Management (§25, processed), and Worship Planning (§25, unprocessed).

## Initial Boundary

Initial hypothesis: Religious Volunteer Management = software that manages a religious organization's volunteer program across the volunteer lifecycle — recruiting volunteers from the congregation, screening and training them, matching them to serving opportunities, tracking their service, and retaining them — with the scheduling act (who serves when) belonging to Ministry Scheduling.

Candidate confusions to resolve during research:
- Ministry Scheduling (processed 2026-09-08) — its pass forwarded a flag: "this Type centers the scheduling act on an existing pool... volunteer-lifecycle machinery (recruiting, training, background checks) appears only in ChMS-module realizations and is bundled-dependent — expect a lifecycle-vs-scheduling seam, joint review recommended."
- Generic Volunteer Management System (§25, unprocessed) — opportunities/applications/hours machinery vs religious grammar.
- ChMS — the ChMS pass (processed 2026-09-07) listed religious-volunteer-management among "capability slices that exist both as ChMS modules and as standalone specialists."
- Religious Small-group Management (processed 2026-09-09) — its pass forwarded: "religious-volunteer-management should expect serving-teams-as-groups packaging overlap (Churchteams runs volunteer teams through groups plus a separate Service Volunteer scheduling feature; Rock and Tithe.ly carry serve-team group types)."

## Research Questions

1. What is the center of this Type: the volunteer (person) and their serving lifecycle, or the serving opportunity/schedule?
2. What lifecycle stages do products document: recruit → apply/screen → train → match → place → serve → track → recognize/retain?
3. Is there a standalone product whose whole product is religious volunteer management (not scheduling)? (ServeHQ, Mobilize by Subsplash, TrainedUp were candidates.)
4. How do ChMS modules realize it, and is the module the dominant packaging?
5. What is the seam with Ministry Scheduling in products that bundle both?
6. What religious-specific machinery exists: spiritual-gifts matching, serving as discipleship, background checks / safe-environment compliance, congregation people-record binding?
7. What is the seam with the generic Volunteer Management System (VolunteerHub-class)?
8. How does the market label the category — does "volunteer management" collapse into "scheduling" anywhere?

## Representative Products

| Product | Pole | Why chosen |
|---|---|---|
| Churchteams | mid-market all-in-one ChMS with a named "Volunteers" feature spanning the full lifecycle | the ChMS-module pole with explicit recruit/train/schedule/track wording |
| FellowshipOne (Ministry Brands) | enterprise ChMS with a module literally named "Volunteer Management" | the named-module pole; the "volunteer pipeline" articulation |
| ParishSOFT (Ministry Brands) | Catholic diocesan suite; Ministry Scheduler module + Safe Environment module | the Catholic/liturgical pole; shows the label collapse (scheduler self-labeled "Catholic Church Volunteer Management Software") and the compliance split |
| Pushpay ChMS (ex-Church Community Builder) | enterprise engagement suite; "Volunteer Management" solution | the "beyond scheduling" articulation; richest volunteer-management FAQ |
| Rock RMS | open-source ChMS; serving teams realized as groups with requirements | the open-source pole; shows the group-machinery realization |
| VolunteerHub | generic volunteer management platform (boundary anchor, not a religious Type member) | the generic pole for the Volunteer Management System seam; has a "Religious Organizations" vertical |

Rejected as primary samples: ServeHQ (standalone church volunteer engagement platform — site blocked by JS challenge ×2, abandoned per source-access rule), Mobilize by Subsplash (standalone church volunteer management app — subsplash.com timed out ×2, abandoned), TrainedUp (church volunteer training — transport error ×2, abandoned), Tithe.ly (no volunteer product page — 404; its Elvanto-heritage scheduling was documented by the ministry-scheduling pass), Ministry Scheduler Pro (scheduling-only specialist, already documented by the ministry-scheduling pass).

## Sources

- Churchteams Volunteers feature page — https://go.churchteams.com/volunteers-churchteams/ (research date 2026-09-09; includes operational FAQ)
- FellowshipOne Volunteer Management — https://www.fellowshipone.com/church-management/volunteer-management/
- FellowshipOne root — https://www.fellowshipone.com/ (product map incl. Background Checks, Worship Planning)
- ParishSOFT root — https://www.parishsoft.com/
- ParishSOFT Ministry Scheduler — https://www.parishsoft.com/ministry-scheduler (page title: "Catholic Church Volunteer Management Software")
- ParishSOFT Safe Environment — https://www.parishsoft.com/safe-environment
- Pushpay ChMS — https://www.pushpay.com/product/chms-software/
- Pushpay Church Volunteer Management Software — https://pushpay.com/solutions/church-scheduling-software/
- Rock RMS root — https://www.rockrms.com/ ; Rock features — https://www.rockrms.com/rock-features
- VolunteerHub root — https://www.volunteerhub.com/ (platform feature taxonomy; Religious Organizations vertical)
- Tithe.ly volunteer-management product URL — https://get.tithe.ly/product/volunteer-management (404 — negative evidence)
- servehq.com — blocked (JS challenge ×2) — market anchor only
- subsplash.com — timed out ×2 — market anchor only
- trainedup.org — transport error ×2 — market anchor only
- Prior-pass evidence adopted: research/ministry-scheduling.md (Churchteams FAQ quotes, MSP/PCO/Tithe.ly observations)

## Product A — Churchteams (ChMS module, full lifecycle)

### Key observations (evidence layer A)

- Positioning: "Recruit, train, schedule, remind, and track how people serve with our complete volunteer scheduling system." The named feature module is "Volunteers"; the pitch names all lifecycle verbs in one sentence.
- **Find your people (recruit)**: "Use registration forms, reports, and referrals to recruit volunteers. Our system pools form information into a group, which makes tracking training and background checks easy. Use automation to sort people onto serving teams according to their interests."
- **Qualify**: FAQ — "Use a Churchteams registration to recruit and communicate with potential volunteers. Use Notes to track conversations and set follow up tasks. Easily request and track background checks and training workshops. When they are ready, transfer them to and schedule them on an active team." Background checks: "From the People Profile, email volunteers a link to complete the background check, or just add it to the volunteer sign-up form. Protect My Ministry is fully integrated. Information from other providers is easily managed in the database."
- **Schedule**: "Create volunteer schedules for a single team or several groups across multiple dates"; templates; conflicts found; substitutes and block-out dates; replies tracked; "Volunteers get an invite to serve along with a link to their schedule, and reminders before their scheduled date."
- **Shepherd (track/retain)**: "Help people find their ministry sweet spot using information such as spiritual gifts and member notes. Automated attendance not only measures involvement but also prevents burnout. Email and text volunteers from the group dashboard."
- The volunteer pool is the church's own people database; serving teams are groups; the pipeline runs from registration form → pooled group → screening/training → transfer to active team → schedule → attendance.

## Product B — FellowshipOne (enterprise ChMS, named "Volunteer Management" module)

### Key observations (evidence layer A)

- Module positioning: "Vital for recruiting, security approval, training and assignments of multiple volunteers, across multiple services and campuses."
- **The volunteer pipeline** (the module's own framing): "A well-defined volunteer pipeline is the key to seamlessly connecting the right people to the right tasks. Recruitment and retention of the generous individuals who volunteer are accomplished through giftedness-matching, frictionless application and approval, an efficient assignment and reminder process, training, support and gratitude."
- Feature list (verbatim): online access to volunteer opportunities; online applications; automatic background checks for church volunteers; prerequisites defined for volunteer positions & church event registration; volunteer pipeline auto-qualifies applicants; custom giftedness program with tracking; simplified matching of candidates with volunteer opportunities; event assignment management with options for volunteer preferences; automatic staff and volunteer attendance through check-in; volunteer service hours included in reportable data.
- Background checks: "FellowshipOne has automated this process to integrate background checks directly with the church's FellowshipOne database through several third-party vendors, with only a few simple touch points."
- Paid vs volunteer distinction: "Staffers, those helpers you pay, deserve the best church volunteer management software to eliminate much of the administrative burden of recruiting, application, qualification, and background checks." — the product explicitly separates paid staff from volunteers.
- Retention framing: "If the process is smooth and pleasant, most people will return to help again and again."
- The suite also sells Church Background Checks as a separate product ("integrated background checks help make it easy for you to recruit volunteers and staff with peace of mind") and Worship Planning ("planning services and volunteer scheduling") — the volunteer-management module, the screening product, and the worship scheduler are distinct suite members.

## Product C — ParishSOFT (Catholic pole: Ministry Scheduler + Safe Environment)

### Key observations (evidence layer A)

- **Label collapse evidence**: the Ministry Scheduler product page's HTML title is "Catholic Church Volunteer Management Software | ParishSOFT" — the vendor equates its scheduler module with "Catholic Church Volunteer Management Software."
- Ministry Scheduler: "empowers parishes to effortlessly organize and manage volunteers for every liturgical service, ministry, and event"; "recruit volunteers and schedule them according to their qualifications and availability"; self-service ("manage their own volunteer experience. From ministry signups to their personal service preferences and schedules, it's all online!"); "Track member-selected priorities, such as a parishioner who would rather serve as an usher first, then a Eucharistic minister second"; "Set up custom groups, ministries, roles, and events"; integration: "Ministry Scheduler uses your member and family records from Family Suite, so you'll never need to enter parishioner records twice."
- **Safe Environment Program (SEP)** — the screening/compliance half of the Catholic volunteer lifecycle, sold as a separate module: "background checks and compliance monitoring—all in one efficient system integrated with your ParishSOFT ChMS." Features: automated alerts ("new individuals, requirement completions, expirations, and outstanding issues"); background checks through Protect My Ministry; compliance ("real-time tracking of training completions, background screenings, errors, and re-certifications"); role-based customization ("Customized requirements - screenings, applications, trainings, approvals, USCCB. Based on assigned roles"); tracking ("status, completions, errors, issues, expirations, and recertifications"); "Historical records of role start/end dates, requirement completions, and issues"; USCCB audit-ready reporting.
- Census module: "Complete data for families, sacraments, staff, and volunteers in your diocese, along with tools to manage roles."
- Root page names "easier and quicker volunteer management" among the platform's building blocks.
- In the Catholic realization the volunteer lifecycle is split across modules: Census (volunteer data) + Safe Environment (screening/compliance) + Ministry Scheduler (placement/scheduling) — and the "volunteer management" label lands on the scheduler.

## Product D — Pushpay ChMS (enterprise engagement suite; "beyond scheduling" articulation)

### Key observations (evidence layer A)

- Navigation labels a solution "Volunteer Management" whose URL is /solutions/church-scheduling-software/; the page title is "Church Volunteer Management Software & Scheduling App"; the footer lists both "Schedules" and "Volunteer Scheduling" pointing to the same URL — direct evidence of the market's label blur between volunteer management and volunteer scheduling.
- **The articulation**: "Go beyond just a scheduling software. Cultivate a culture of serving with church volunteer scheduling and management software that not only helps you organize and schedule your teams, but empowers them all in one place."
- Scheduling core: Schedule Grid ("Schedule multiple services and weeks at a time to see at a birds eye that you're fully staffed"); Manage Teams (roles/positions); Serving Rotations; Availability and Preferences ("block out dates, preferred services and weeks to serve, along with finding their own replacements"); Congregant App ("manage their serving and browse open positions"); Open positions; Notifications; Family Calendar (household serving); Volunteer Check-In ("check-in stations for volunteers to notify their team leaders they are there and ready to serve"); Communications.
- **Pipeline machinery**: "Automated Workflows — Automatically plug individuals into serving positions or volunteer pipelines with digital forms and people automations"; FAQ: "With Process Queues, your church can be assured that your volunteers have completed a background check, attended a training, or completed any tasks before they're assigned an opportunity"; "Background Check alerts — Schedulers can be alerted when a church volunteer needs to complete or renew their background check before they can be scheduled."
- **Culture/engagement metrics**: "Roll up metrics — See the overall health of your church's volunteer culture or drill down to specific teams to review serving trends"; ChMS FAQ: "Leaders can see who's available, who's been serving frequently (and might be heading toward burnout), and who's new and ready for their first assignment... because volunteer data connects to the broader member profile, you can see how each person's serving fits into their overall engagement with your church."
- ChMS FAQ: "Most ChMS platforms include: ... Group and volunteer management"; People Workflows: "Custom workflows for items like First Time Guest Follow up, Volunteer pipelines, and Care"; "Ministry leaders use it to run groups, organize serving teams... Volunteer coordinators build schedules and send reminders."
- Burnout: "Leaders can minimize burnout by creating rotations and finding new volunteers to share the work."

## Product E — Rock RMS (open-source ChMS; serving teams as groups)

### Key observations (evidence layer A, feature-page level)

- Groups: "Organize individuals by purpose (e.g., small groups, serving teams, classes)"; "Track attendance and engagement over time"; "Use group requirements to enforce training, background checks, etc."; "Allow individuals to find and join groups via public group finder."
- Group Scheduling: "Coordinate serving teams with automated scheduling"; "Allow individuals to accept/decline serving requests"; "Manage conflicts and preferences with ease."
- Steps: "Define clear discipleship paths (e.g., baptism, membership, volunteering)"; "Track individual spiritual milestones" — serving framed as a discipleship step.
- LMS: "Deliver on-demand discipleship and training courses... Track course progress and completion for each individual" — training machinery adjacent to the volunteer loop.
- Sign-ups: "Create flexible registrations for events, classes, or serving."
- Connections: "Assign connection requests to staff or volunteers."
- In Rock the serving team IS a group with requirements attached; the volunteer lifecycle is assembled from group membership + requirements + group scheduling + steps + LMS rather than a dedicated volunteer module.

## Product F — VolunteerHub (generic boundary anchor)

### Key observations (evidence layer A)

- Positioning: "Helping Organizations Better Recruit, Engage, and Manage Volunteers"; "Over the last 20+ years, VolunteerHub has helped thousands of organizations manage billions of volunteer hours."
- Feature taxonomy — the generic volunteer program: Volunteer Management (Volunteer Recruitment, Volunteer Scheduling, Volunteer Hour Tracking, Volunteer Database, Volunteer Fundraising, Volunteer Liability Waivers, Rewards and Recognition, Reporting); Opportunity Management (Landing Pages, Check-In, Multi-Event Editor, Configurable Forms, Group Organization, Advanced Permissions, Mobile App); Volunteer Communication (Email, Text, Social).
- The volunteer is a self-registering person in the platform's own database: "volunteer self-registration from any device, and automated record management"; "Maintain a comprehensive database of your volunteers. Access contact information, skills, availability."
- Hours/impact center: "coordinators can easily track activity and hours for each volunteer for each individual event"; testimonials emphasize hours for grant funding and demonstrating community impact.
- **Religious Organizations is one of its Solutions verticals** — generic volunteer management is sold to churches; the seam with the religious Type is therefore not the customer but the structure.
- Background checks arrive as an integration (Sterling Volunteers, PeopleFacts), not as native eligibility gating.

## Cross-product Comparison

| Structure | Churchteams | FellowshipOne | ParishSOFT | Pushpay | Rock RMS | VolunteerHub (generic) | Layer |
|---|---|---|---|---|---|---|---|
| Volunteers held as identified people from the organization's own records | people database; pooled into groups | church database | Family Suite member/family records | member profiles | people records | platform's own volunteer database (self-registered) | A (5/5 religious) |
| Serving structures: ministries/teams/roles/opportunities | serving teams (groups) | volunteer opportunities + positions | ministries, roles, groups | serving positions, teams, ministries | serving teams (groups) | opportunities/events | A (6/6) |
| Recruitment into the pool (forms/referrals/signups) | registration forms, reports, referrals | online applications; online access to opportunities | ministry signups online | digital forms + automations | group finder + sign-ups | landing pages, self-registration | A (6/6) |
| Eligibility gating before placement (screening/training/prerequisites) | background checks + training workshops tracked; "when they are ready, transfer them" | prerequisites; pipeline auto-qualifies; automatic background checks | Safe Environment role-based requirements; "according to their qualifications" | Process Queues; background-check alerts before scheduling | group requirements enforce training/background checks | waivers + screening via integration (not native gating) | A (5/5 religious) |
| Matching people to opportunities (gifts/interests/qualifications) | automation sorts by interests; spiritual gifts + member notes | giftedness-matching; simplified matching | member-selected priorities (usher first, EM second) | volunteer pipelines; preferences | group requirements + finder | skills/availability in database | A (5/6) |
| Placement into service (assignment to occasions/roles, or self-signup) | schedules across dates; invites | event assignment management | schedules for services/ministries/events | schedule grid; rotations; open positions | group scheduling; accept/decline | scheduling + sign-up | A (6/6) |
| Service tracked back onto the person (attendance/hours/involvement) | automated attendance; burnout prevention | attendance through check-in; service hours in reportable data | not observed on fetched pages | roll-up metrics; serving trends; burnout signal | attendance and engagement over time | hour tracking per event | A (4/5 religious + generic) |
| Volunteer self-service (availability, preferences, subs, schedule) | block-out dates, substitute preferences, replies | volunteer preferences on assignments | self-service preferences/availability/signups | blockouts, preferences, find replacements, browse open positions | accept/decline; conflicts/preferences | self-registration, schedule access | A (6/6) |
| Volunteer check-in | not on fetched page (check-in product exists) | automatic attendance through check-in | not observed | volunteer check-in stations | attendance tracking | check-in | B (3/6) |
| Retention/recognition framing | "ministry sweet spot"; burnout prevention | "support and gratitude"; smooth process → return | "nurture your volunteer base" | "culture of serving"; volunteer-culture health | serving as a discipleship step | rewards and recognition | A/B (6/6, depth varies) |
| Scheduling machinery depth (rotations/templates/auto) | templates, conflicts, reminders | assignment + reminders | configurable rules, schedules in minutes | rotations, schedule grid, notifications | automated scheduling | scheduling + multi-event editor | A (6/6) |
| Screening/compliance as separate module | background checks via integration (Protect My Ministry) | background checks product + integration | Safe Environment module (USCCB audit reporting) | background-check alerts; integrations | group requirements | Sterling Volunteers integration | A (5/6) |
| Serving bound to congregational occasions (services/events) | any event incl. worship services | services and campuses | liturgical services, ministries, events | services/weeks | serving occasions via scheduling | events (generic) | A (5/5 religious) |

## Canonical Model — Four Abstraction Levels

### L0 — Defining Invariant

Four jointly-held structures over a religious organization's own people records; the volunteer-management character lives in their combination:

1. **The congregation-anchored volunteer record** — volunteers are identified people drawn from the organization's own people records (members, not anonymous self-registrants), each carrying serving-relevant state: eligibility/clearance status, training, availability, preferences, gifts/interests, and accumulated service history. Remove → a generic self-registration volunteer platform or an anonymous signup sheet.
2. **Serving opportunities as the demand structure** — the organization's ministries, teams, roles, and positions that need people, held as records people can be placed into. Remove → a people database with no serving dimension.
3. **The managed pipeline into service** — people are recruited into the pool, brought to eligibility (screening, training, prerequisites), matched to opportunities by gifts/interests/qualifications, and placed into service; eligibility gates placement. Remove → a bare roster or schedule with no lifecycle (recruiting/qualifying collapses out); remove the gate → an open signup board.
4. **Service tracked back onto the person** — service participation is recorded against the person (attendance, hours, involvement), feeding involvement, burnout, and retention views. Remove → one-way placement with no memory; the "management" reduces to matching.

Jointly-held is load-bearing: (1) alone = a people database with volunteer attributes; (2) alone = a ministry/org chart; (3) without (1)+(2) = a generic recruiting pipeline; (4) without (1)–(3) = an attendance log; (2)+(3) without (1) = the generic volunteer program (self-registered population); (1)+(2)+(3) without (4) = placement without memory. Domain binding: the organization is a religious congregation and the volunteers are its own members serving in ministry — unpaid, drawn from the pews; remove that binding and the generic Volunteer Management System remains.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Scheduling machinery over the placed people: rotations, templates, auto-scheduling, reminders, published schedules (shared with Ministry Scheduling)
- Volunteer self-service: personal schedules, availability/block-outs, serving preferences, finding substitutes, browsing open positions
- Background-check integration with screening vendors (Protect My Ministry, Sterling-class)
- Training tracking (workshops, courses, LMS completion)
- Spiritual-gifts / giftedness / interest matching
- Household/family serving preferences and family calendars
- Team-leader scoped permissions and leader apps
- Volunteer check-in at service occasions
- Communication tooling (email/text to teams and positions)
- Burnout signals and fair-distribution views
- Serving-culture metrics rolled up to leadership

### L2 — Variant / Optional Structure

- Denominational shapes: Catholic safe-environment compliance regimes (role-based requirements, recertification, audit-ready reporting) vs evangelical serving-culture/discipleship framing
- Serving as a discipleship step (paths: baptism → membership → volunteering)
- Screening/compliance packaged as a separate module vs native gating vs integration-only
- Event-volunteer signup (one-off occasions) vs ongoing ministry roles
- Paid-staff handling beside volunteers ("staffers")
- Recognition/rewards machinery (deep in generic products, thin in religious samples)
- Multi-campus operation
- Packaging: named ChMS module vs suite solution vs standalone product (standalone pole unverified this pass)
- Open-source assembly from group machinery (groups + requirements + scheduling + steps)

### L3 — Vendor-specific (kept out of the final document)

- Pushpay: Process Queues, LEAD App, My Church App, Schedule Grid, roll-up metrics, "Volunteer Management" solution URL = church-scheduling-software
- FellowshipOne: "Volunteer Pipeline" terminology, "Staffers", custom giftedness program, Background Checks as separate suite product
- ParishSOFT: Ministry Scheduler, Safe Environment Program (SEP), USCCB audit-ready reporting, Protect My Ministry integration, Family Suite record reuse, member-selected role priorities
- Churchteams: Text-to-Church, Notes, Protect My Ministry integration, service-planning feature "mid-2026" roadmap
- Rock: group requirements, Steps, Connections, LMS, group finder
- VolunteerHub: landing pages, liability waivers, rewards and recognition, volunteer fundraising, Sterling Volunteers/PeopleFacts integrations

## Vendor-specific Findings

See L3. Two structural market observations worth recording:

1. **The label blur is real and bidirectional.** Pushpay labels its scheduling-centered solution "Volunteer Management" (URL: church-scheduling-software) while articulating "go beyond just a scheduling software"; ParishSOFT labels its scheduler module "Catholic Church Volunteer Management Software"; FellowshipOne names a pipeline-centered module "Volunteer Management". The market uses "volunteer management" for the whole span from scheduling to pipeline; the pipeline center and the scheduling center are distinct centers under one label.
2. **The Catholic pole splits the lifecycle across modules** (Census + Safe Environment + Ministry Scheduler) while the evangelical pole bundles it into one volunteer feature (Churchteams, Pushpay, FellowshipOne) or assembles it from group machinery (Rock).

## Rejected Findings

- "Religious Volunteer Management = Ministry Scheduling under another name" — REJECTED. The scheduling act is shared machinery, but the pipeline center (recruit → qualify → match → track → retain) is vendor-articulated as the differentiator ("go beyond just a scheduling software"; the FellowshipOne pipeline; Churchteams' recruit/train/track verbs). The ParishSOFT label collapse is one vendor's labeling, not the Type's structure.
- "Background checks are definitional" — REJECTED as stated. The invariant is eligibility-gated placement; background checks are its dominant realization (5/5 religious samples), with training, prerequisites, and role-based requirements as alternative realizations. A small congregation can run the pipeline without formal screening machinery.
- "Spiritual-gifts matching is definitional" — REJECTED. Present in 3/5 religious samples (Churchteams, FellowshipOne, ParishSOFT priorities); matching by interests/qualifications is the general form.
- "Service-hours tracking is generic-volunteer machinery, not religious" — REJECTED. Religious samples track service back to the person (attendance, hours, involvement) with burnout/retention framing; what differs from the generic Type is that the record lands on the congregation's own people records.
- "This Type is only a ChMS capability (alias)" — REJECTED for now. Named modules with distinct centers exist (FellowshipOne Volunteer Management; Pushpay solution; Churchteams Volunteers), and the lifecycle loop is coherent and vendor-articulated. BUT the standalone pole is unverified (see Uncertainties) — the same posture as religious-education-management; flagged for revisit.
- "Volunteer check-in is definitional" — REJECTED. 3/6 sampled; an attendance realization, not the invariant.

## Boundary Findings

1. **vs Ministry Scheduling (§25, processed)** — the lifecycle-vs-scheduling seam, RATIFIED keep-both from this side; DISCHARGES that pass's forward flag. Ministry Scheduling is the serving-schedule system of record: positions × dated occasions × assignments + the people-side reconciliation loop; the schedule is the record of record and the volunteer pool is an input. Religious Volunteer Management is the volunteer-program system of record: the volunteer's serving state (eligibility, training, gifts, service history) is the record of record, moved through a managed pipeline into service; the schedule is one output. Seam test: remove the pipeline (recruit/qualify/match/track) and keep positions+occasions+assignments+response → Ministry Scheduling; remove the occasion grid and keep the person's serving lifecycle → this Type. Products bundle both (Pushpay, Churchteams, ParishSOFT, Rock); the standalone scheduling specialist (MSP) proves the scheduling act stands alone; the label blur (Pushpay URL, ParishSOFT title) is recorded as market vocabulary, not structure.
2. **vs Volunteer Management System (§25 generic, unprocessed)** — the congregation-binding seam. The generic Type centers the volunteer program over a self-registering population: opportunities posted to a public pool, applications, hours, waivers, recognition, fundraising; the volunteer database is the platform's own. This Type centers serving ministry over the congregation's own people records: volunteers are members, screening gates placement, service lands on the person's church record beside giving/attendance/groups, and the framing is discipleship/engagement. VolunteerHub's "Religious Organizations" vertical proves the seam is structural, not customer-based. FORWARD FLAG for the volunteer-management-system pass: adopt the people-record-substrate discriminator; note that generic products serve churches as a vertical.
3. **vs Church Management System / ChMS (§25, processed)** — module↔standalone spectrum. Volunteer management is a standard ChMS capability (Pushpay: "Most ChMS platforms include... Group and volunteer management"); named modules exist (FellowshipOne Volunteer Management, Churchteams Volunteers, Pushpay solution, ParishSOFT Ministry Scheduler). This leaf stands on the coherence of the lifecycle loop and the named-module centers; the standalone pole is UNVERIFIED (ServeHQ/Mobilize/TrainedUp unreachable) — same posture as religious-education-management; if future passes also cannot verify an independently-sold standalone product, revisit as a ChMS-family module Type.
4. **vs Religious Small-group Management (§25, processed)** — serving teams realized as groups. Rock: "Organize individuals by purpose (e.g., small groups, serving teams, classes)" with group requirements enforcing training/background checks and group scheduling coordinating serving teams; Churchteams pools volunteer form data into a group. The community loop (group life, attendance, health) vs the serving loop (eligibility, placement, service tracking) remain distinct centers; all-in-one systems realize both on the same group machinery. DISCHARGES that pass's forward note from this side.
5. **vs Worship Planning (§25, unprocessed)** — worship planning joins scheduling with service content (order, songs); this Type spans all ministries, not only worship. FellowshipOne sells Worship Planning (with volunteer scheduling) and Volunteer Management as separate suite members.
6. **vs Employee Scheduling / HR (§09)** — volunteers are unpaid members, not employees; FellowshipOne explicitly separates "Staffers, those helpers you pay" from volunteers; no wages, shifts-for-pay, or labor-compliance machinery here.
7. **vs Religious Event Management (§25, processed)** — one-off event volunteer signup vs the ongoing serving program; the ministry-scheduling pass recorded that event-volunteer signup is sold as a different product (MSP's Unison). Event volunteering appears here as one occasion type, not the center.
8. **vs Pastoral Care Management (§25, processed)** — volunteers may deliver care, but this Type manages the serving relationship (eligibility, placement, service), not care needs and visitation records.

## Uncertainties

- **Standalone pole unverified**: ServeHQ (JS challenge ×2), Mobilize by Subsplash (timeout ×2), and TrainedUp (transport error ×2) were all unreachable. Market reputation says standalone church volunteer-engagement products exist (training + scheduling + communication); this pass could not verify any. The Type's independence rests on loop coherence + named-module centers, not on a verified standalone product.
- ParishSOFT service-tracking (attendance/hours) was not observed on fetched pages — the service-tracked-back leg rests on 4/5 religious samples (FellowshipOne, Churchteams, Pushpay, Rock).
- Tithe.ly volunteer machinery not directly sampled (volunteer product URL 404; Elvanto scheduling documented by the ministry-scheduling pass).
- Recognition/rewards machinery is thin in the religious sample (FellowshipOne "gratitude" only) — held optional, not standard.
- The historical check is conceptual (parish-office volunteer card file: names, ministries, clearance status, assignments, service notes), not source-verified.
- VolunteerHub's religious-organization customers were observed as logos/testimonials only; no church-specific workflow documentation was fetched from the generic side.

## Final Synthesis

Religious Volunteer Management is the religious organization's volunteer-program system of record. Its defining core is the four-part structure over the congregation's own people records: volunteers held as identified members carrying serving-relevant state (eligibility, training, availability, gifts, service history) + serving opportunities (ministries, teams, roles) as the demand structure + the managed pipeline that recruits people, brings them to eligibility, matches them to opportunities, and places them into service with eligibility gating + service tracked back onto the person, feeding involvement, burnout, and retention views. The scheduling act (who serves when) is shared machinery with Ministry Scheduling — bundled in most products, owned in depth by that sibling Type. The market realizes the Type as named ChMS modules (FellowshipOne Volunteer Management, Churchteams Volunteers, Pushpay's solution, ParishSOFT's scheduler), as open-source assembly from group machinery (Rock), and — per market reputation, unverified this pass — as standalone engagement products. The label "volunteer management" is applied by the market to everything from pure scheduling to the full pipeline; the structure beneath the label is the volunteer's serving lifecycle over the congregation's people records.
