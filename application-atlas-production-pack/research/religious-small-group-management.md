# Research Notes — Religious Small-group Management

## Research Goal

Understand what "Religious Small-group Management" software actually is in the market: what products exist under this label, what their defining structure is, and how the Type relates to its already-processed §25 siblings — Church Management System / ChMS, Congregation Membership Management, Religious Event Management, Religious Education Management, Pastoral Care Management — and to generic group/community software.

This pass must discharge three flags recorded by earlier passes:

1. **ChMS pass (2026-09-09):** groups were deliberately kept OUT of the ChMS L0 ("the strongest L1 item"); the ChMS pass classified Religious Small-group Management as a "capability slice that owns one loop in depth and exists both as a ChMS module and as a standalone specialist." This pass must verify that the slice has a real standalone product population and identify its own loop.
2. **Religious Event Management pass (2026-09-09):** recorded "vs Religious Small-group Management: ongoing communities vs dated events; one sampled product realizes registration as a group (product-specific blur, noted)." This pass must confirm the ongoing-vs-dated seam and characterize the blur.
3. **Pastoral Care Management pass (2026-09-09):** recorded a watch-item — "small groups are often the care-delivery context (TouchPoint's own transfer use case routes care to life-group leaders). Distinction: groups center community membership and group life; this Type centers individual care needs." This pass must confirm or amend that distinction.

## Initial Boundary

Working hypothesis at start:

- The leaf sits in the §25 church-software family. In church practice, "small groups" (life groups, home groups, cell groups, connect groups, Bible studies, care groups) are the congregation's ongoing midweek communities — distinct from dated events, from Sunday-school classes run as a program, from serving rotations, and from the whole-congregation membership roster.
- The ChMS pass observed that every sampled ChMS carries a Groups capability (small groups, Bible studies, staff, elders, recovery, care) with leaders, attendance, and privacy postures — and that standalone specialists exist beside the suites.
- Nearest neighbors to test: ChMS (record core + groups as organizing unit), Congregation Membership Management (whole-congregation roster), Religious Event Management (dated events), Religious Education Management (classes/terms/milestones), Pastoral Care Management (individual care needs), Ministry Scheduling / Religious Volunteer Management (serving teams often realized as groups), Church Communication Platform (sending loop), Group Messaging Application / Community Chat Platform (§01, conversation-centered), Member Community Platform (§25 association side), generic group tools (Meetup-class, no congregation substrate).
- Open questions: Is there a genuine standalone product population, or only ChMS modules? What is the group record's anatomy? How do joining mechanics work (open/request/closed)? Is leader self-service definitional or common? Is attendance definitional? Where does the "group health" idea sit? How do serving teams / mission trips / classes fit when the same machinery carries them?

## Research Questions

1. What is the anatomy of a group record (name, schedule, location, type, tags, leader, roster, privacy, lifecycle)?
2. How is membership modeled (person↔group binding, roles, joined dates, one-membership rules)?
3. How do people join (public finder, open signup vs request-to-join vs closed, limits, approval workflow, prospect follow-up)?
4. What does the group's ongoing life look like (meetings, attendance capture, messaging, events, resources)?
5. Who operates the system — staff vs lay leaders — and how is access scoped (leader self-service, confidential groups, people-database access)?
6. What reporting/health machinery exists (attendance trends, drop-off follow-up, active rate, health surveys, coaching)?
7. How does group participation write back to person records?
8. What is religious-specific vs generic group software? Does the machinery carry non-small-group uses (serving teams, mission trips, governance)?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

1. **Planning Center Groups** — standalone product of the leading modular ChMS suite; mid-to-large churches; member-facing finder + chat emphasis; unusually good public documentation (product page + public API reference).
2. **GroupVitals** — independent standalone small-group specialist; small-to-mid churches; group-health/coaching philosophy; product pages + Help Scout knowledge base.
3. **Tithe.ly Groups** — module of an all-in-one vendor (Giving + ChMS + Apps + Sites); small-to-mid churches; app-first joining; product page with operational FAQ.
4. **Churchteams** — mid-market all-in-one ChMS with a group-centric data model (groups carry small groups, teams, trips, assimilation); feature page + FAQ.
5. **Pushpay ChMS (formerly Church Community Builder)** — enterprise engagement-suite module; large churches; groups with events, messages, needs, attendance, RSVP (product page; support site unreachable — same limitation as the event pass).

Rejected/absent candidates: Rock RMS (open-source ChMS with groups by purpose + group finder + group scheduling — observed at Tier 2 in the ChMS pass; its public book/documentation returned 404 again this pass, so not sampled as a primary); Breeze (rebranded into Tithe.ly Church Management — same vendor family); ShulCloud (synagogue; 403 in prior passes); TouchPoint (care-transfer use case cited by the pastoral-care pass; docs not fetched this pass). Non-church religious breadth: small-group software is a Protestant-evangelical-led market; GroupVitals' own FAQ states it also serves "churches, parishes, non-profits, peer groups, coaching organizations" — recorded as a breadth data point rather than forcing a weak sample.

## Sources

Tier-1 (official operational documentation):

- Planning Center — Groups API reference (Group, Membership, GroupApplication, Enrollment, Attendance objects), version 2023-07-10 — https://api.planningcenteronline.com/docs/apps/groups (+ /versions/2023-07-10/vertices/group | membership | group_application | enrollment | attendance)
- GroupVitals — Getting Started: Overview (Help Scout knowledge base) — http://support.groupvitals.com/article/113-getting-started-overview-read-this-first

Tier-2 (official product pages):

- Planning Center Groups — https://planning.center/groups
- GroupVitals — https://www.groupvitals.com/ (+ /group-signups, /health, /attendance, /dashboard)
- Tithe.ly Groups — https://get.tithe.ly/product/groups
- Churchteams Groups — https://go.churchteams.com/groups-churchteams/
- Pushpay ChMS — https://www.pushpay.com/product/chms-software/

Prior-pass evidence reused (official sources fetched on 2026-09-09 by the ChMS and event passes):

- Pushpay ChMS Groups observations (events, messages, Needs/meal trains, attendance, RSVP) — Pushpay product page, ChMS pass.
- Rock RMS Groups observations (groups by purpose incl. small groups/serving teams/classes, group requirements enforcing training/background checks, public group finder, group scheduling) — Rock features page, ChMS pass.
- Planning Center ChMS use-case page (Church Center: "give, join a group… chat with their group"; permissions view all/subset/own; confidential groups; attendance reports "follow up with anyone who stops attending") — ChMS pass.

Unreachable / limitations:

- Tithe.ly help center returned HTTP 403 this pass (it was reachable on 2026-09-09 for the event pass) — Tithe.ly Groups evidence stays at product-page tier.
- Rock RMS book/documentation 404 (same as ChMS pass) — Rock not sampled as a primary.
- Pushpay support site unreachable (503 in the event pass; not retried) — Pushpay evidence stays at product-page tier.
- Planning Center end-user help articles remain a JS shell (event-pass finding); mitigated by the public API reference.

Research date: 2026-09-09.

## Product Observations

### Planning Center Groups (evidence: A — API reference + product page)

- Positioning: "Community organization & communication… Where pastors, admins, and community leaders can organize groups online, take attendance, and bring people together with messaging." A separate product in the Planning Center suite (People, Groups, Calendar, Registrations, Check-Ins, Services, Giving, Publishing, Church Center). "Create groups for every part of your church": small groups, Bible studies, staff, admin, elders, deacons, recovery, care.
- **Group object (API, official):** "A group of people that meet together regularly." Attributes: name, description, header image, **schedule** ("a text summary of the group's typical meeting schedule… 'Sundays at 9:30am' or 'Every other Tuesday at 7pm'"), location (physical or virtual preference; virtual_location_url "a zoom link, for example"), contact_email ("display a contact button on the public page where potential members can ask questions before joining"), **listed** (visible on Church Center — the public finder), events_visibility (public or members), **members_are_confidential** ("whether or not group members can see other members' info"), chat_enabled, direct_messages_enabled, leaders_can_search_people_database, memberships_count, archived_at, tag_ids; relationships: group_type ("unique groups do not belong to a group type"), location, campuses.
- **Membership object (API):** "The state of a Person belonging to a Group. **A Person can only have one active Membership to a Group at a time.**" Attributes: joined_at, role (member or leader). CRUD: add person to group, change role, delete membership.
- **GroupApplication object (API):** "A request to join a group which can be approved or rejected." Attributes: applied_at, message ("an optional personal message from the applicant"), status (pending / approved / rejected). Approve action "immediately add[s] the person to the group… optionally… role… as member (default) or leader. **Only administrators or managers can create leaders.**" Reject action: person not added.
- **Enrollment object (API):** "Details on how and when members can join a Group." Strategy: **open_signup, request_to_join, or closed**; member_limit ("total number of members allowed before enrollment should automatically close"), date_limit, auto_closed + auto_closed_reason; status: open / closed / full / private (unlisted).
- **Attendance object (API):** "Individual event attendance for a person" — attended (boolean), role at time of event (member, leader, visitor, or applicant), bound to person + group event.
- Group events (API association): events per group with RSVP (per product page); EventNote, Resource ("file and link resources shared with this group", some leader-only), Tag/TagGroup objects.
- Chat rules (API actions): enable_chat "will make the names, profile photos, and genders of members visible to other group members. **Chat cannot be enabled for a group if the member list is confidential.**" disable_chat requires confirm.
- Duplicate action (API): copy a group with selected fields (members, leaders, event defaults, event calendar, resources, basic info, Church Center settings, chat settings, automations) — seasonal group relaunch machinery.
- Product page: leaders take attendance ("track who's coming, who's missing"); group-wide announcements + chat; group calendar/events/materials; attendance reports "monitor involvement, follow up with anyone who stops attending, and track the amount of visitors"; church-wide engagement reporting (demographics, how often they attend, when they drop off, how frequently groups meet); Church Center mobile app/website (find and join groups, group chat, RSVP, group resources); confidential groups ("hide member details… anonymous to everyone but the group leader and admins… recovery, grief, healing"); group types (small groups, Sunday School, recovery); open signups via QR; permissions (view all groups / subset / only their groups); ToS: children under 13 may not log in to Church Center or access group messaging — kids tracked via Check-Ins instead.
- Pricing (L3): priced by total group members across the church per month; unlimited groups and events on all plans.

### GroupVitals (evidence: A for help-center overview; product pages Tier 2)

- Positioning: "Small Group Management Software: Signups, Attendance + Metrics… makes group signups and tracking easier and clearer for administrators and group leaders." Serves "churches & other organizations"; FAQ: "churches, parishes, non-profits, peer groups, coaching organizations."
- Getting Started overview (help center, official): 12 setup steps — personal settings; **group leadership structure**; group settings; invite staff; connection paths (**Prospects Pipeline, GroupFinder, general signup form**); add groups; add people; make people leaders and assign to groups; add members (or ask leaders to); **assign coaches to leaders and senior coaches to coaches** ("we always suggest to at least assign a staff member to be a coach to oversee a leader within their span of care"); understand attendance; onboard leaders. Framing: leaders get "more control over their group (that means less work for you)."
- **GroupFinder** (product page): "anyone can browse & join a group on any device"; search filters, map view, list view; pre-set filter links (e.g., a website button showing only Co-Ed groups); signup form → "instantly become a group prospect, guest or member."
- **Prospect pipeline** (product page): "full visibility of each step a person takes to successfully get plugged into a group"; email reminders to follow up (assigned staff); leader gets email + text with the sign-up's personal information; coach can be notified per signup ("another layer of accountability"); "never let someone fall through the cracks."
- **Attendance** (product page): automatic attendance reminders to leaders after each meeting (email/text; leader controls channel and timing); link opens the attendance form on any device; **names pre-checked, no login required**; guests added on the form; customizable open-ended question at the end ("How'd group go this week?"), answers emailed to staff + coach and saved in the group profile; **accountability reminders** — escalating reminders when a leader doesn't take attendance, then staff + coach notified; **active rate** metric — "% of the time the group has met in their last 4 scheduled meetings."
- **Health** (product page): leader feedback per meeting; **member health surveys** (spiritual growth, relational connection, recommendation, life impact — "address issues as they happen, rather than finding out after the group has ended"); attendance-based engagement ("how often people are showing up… how active your groups are").
- **Dashboard** (product page): metrics (first-time group joiners, last-semester signups, stick rate, showed up last month, groups that met at least once in the last 30 days); attention flags (someone wanting to join / unable to join / removed from a group / attendance suddenly dropped / guest showed up); comments loop (leader attendance comments, member health surveys, coach notes about leaders, staff notes about prospects).
- **Coaching leadership** (product page): "track your coaches & senior coaches to know which groups & people are within their span of care."
- Other: leader accounts (login to update group + send messages); **roster updates by email without login**; group types, life stage, group models, tags; multi-campus with restricted access; resources hub (private files/links to leaders); activity timelines per person and group; **integrations with church databases** (FellowshipOne, Church Community Builder) — data kept in sync; spreadsheet import.

### Tithe.ly Groups (evidence: B — product page + operational FAQ; help center 403 this pass)

- Positioning: "Tithely Groups is small group software for churches — a complete church group management system for small groups, Bible studies, youth groups, and ministry teams." Runs inside Tithe.ly Church Management: "every sign-up and attendance record lands in the same profile as that person's giving, check-ins, and events so you can finally see who's actually connected."
- Joining (product page + FAQ): searchable group directory organized by group type, in the church app; "Your Groups" section; "Request to join a group with one simple click." Privacy postures (FAQ): "public and open to anyone, publicly listed but requiring a join request that a group leader approves, or private and hidden entirely. Leaders control who's admitted." Student groups "typically set to require leader approval."
- Leader tools: rosters, attendance, messaging; customize group photo/description; accept new members; make groups private. FAQ: leaders take attendance "on their own devices for their own groups, without needing admin access to your church database… each week's attendance writes straight to the member records — so rosters stay current, and the office isn't retyping sign-in sheets."
- Messaging: each group has "its own channel for group messages and direct messages, plus two-way push notifications through your church app… no shared phone numbers, no separate group text thread to maintain."
- Group types (FAQ): "create as many Group Types as you need — youth, young adults, women's, men's, ministry teams, serve teams — each with its own settings for privacy, meeting details, and who can join."
- Write-back (FAQ): "group membership and attendance are attributes of the person record — visible next to giving history, check-ins, and event sign-ups. That's what lets you answer 'who attends on Sunday but isn't in a group?' without exporting anything."
- Packaging (FAQ): Groups included with Tithe.ly Church Management; the custom church app adds member-facing browsing/joining.

### Churchteams (evidence: B — feature page + FAQ)

- Positioning: "Tools you need to connect people with the right group and equip leaders to shepherd with excellence."
- **Groupfinder**: "add our Groupfinder feature to your website, outgoing emails, or Text-to-Church keywords"; "set up links to specific lists and add optional filters"; "empower people to email group leaders, find groups on a map, get more information, or register themselves into a group."
- Attendance: "tracking attendance through meeting reports or check-in is simple"; FAQ: "an email reminder with an attendance link or the app makes it easy for leaders to quickly take attendance on their phone"; staff kept "in the know with tracked attendance taken from any smart device."
- **Group health reports**: "monthly group health reports are sent to leadership"; "prayer requests and study notes, added in the attendance reports, can be shared with leadership."
- **Groups as universal organizer**: "Groups are used to organize and track people, tasks, and payments… Use for anything from small group discipleship to events and mission trips." FAQ: mission trips (registration forms create mission teams; group carries communications, notes, requirements checklists, contributions); volunteer teams (interest form → next-step team; background checks; the Service Volunteer feature adds schedule/reminders/attendance); "track assimilation and discipleship process."
- Reports: 45+ report types with group/people/financial filters.

### Pushpay ChMS / Church Community Builder (evidence: B — product page; support site unreachable)

- ChMS positioning (this pass): "a centralized platform churches use to organize member data, automate ministry operations…"; "Most ChMS platforms include… group and volunteer management…"; "Track involvement across attendance, groups, giving, etc."
- Groups observations (ChMS pass, product page): Groups carry events, messages, **"Needs" (meal trains)**, attendance, RSVP; member profiles carry "attendance history, group involvement, and giving data"; LEAD App for staff/leaders on the go.
- The group is one surface of the engagement suite; no standalone groups product depth is published.

## Cross-product Comparison

| Structure | Planning Center Groups | GroupVitals | Tithe.ly Groups | Churchteams | Pushpay ChMS |
|---|---|---|---|---|---|
| Group as persistent record | A: Group object (name, description, schedule, location, type, tags, archived_at) | A: groups with types/life-stage/models/tags | B: groups with type, meeting details, photo/description | B: groups (universal organizer) | B: groups with events/messages/needs |
| Designated leader | A: Membership role = leader | A: leaders assigned to groups; coaches above | B: leader tools; leaders approve joins | B: leaders email-able via finder | B: group leaders |
| Membership roster bound to people | A: Membership = person↔group state; one active membership per person per group | A: people added/imported; roster updates by email | B: membership on the person record | B: people in groups | B: group involvement on profile |
| Join mechanics | A: Enrollment strategies (open_signup / request_to_join / closed) + limits + auto-close; GroupApplication (pending/approved/rejected) | A: GroupFinder + general signup form; prospect pipeline | B: open / request-with-approval / private | B: finder links; self-registration into groups | B: RSVP (event-level) |
| Public finder/directory | A: listed flag; Church Center public group pages; contact button | A: GroupFinder (filters, map, list) | B: searchable directory by type | B: Groupfinder embeds + map | B: (group finder in Rock/CCB heritage; not on page) |
| Per-meeting attendance | A: Attendance object (attended, role incl. visitor) | A: reminder-link forms, pre-checked, no login, guests | B: leader attendance on own devices | B: meeting reports or check-in; email-link attendance | B: attendance on groups |
| Group messaging | A: announcements + chat; enable/disable rules; DMs | B: emails & texts to groups | B: group channel + DMs + push | B: communications via group | B: group messages |
| Group events | A: events per group, RSVP, visibility public/members | B: (meeting schedule implied) | B: meeting day/time/location on group page | B: group calendar | B: events + RSVP |
| Shared resources | A: Resource objects (files/links, leader-only) | B: resources hub (private files/links to leaders) | B: (not surfaced) | B: study notes in attendance reports | B: (not surfaced) |
| Attendance-based follow-up | A: "follow up with anyone who stops attending"; drop-off reporting | B: attention flags (dropped attendance, removed members) | B: (implied via person record) | B: staff see tracked attendance | B: engagement tracking |
| Health machinery | B: church-wide engagement reporting | A: active rate, health surveys, dashboard metrics, monthly attention flags | B: (not surfaced) | B: monthly group health reports to leadership | B: engagement tracking |
| Coaching layer | B: (not surfaced) | A: coaches + senior coaches, span of care | B: (not surfaced) | B: (not surfaced) | B: (not surfaced) |
| Confidentiality posture | A: members_are_confidential; anonymous lists; chat interplay | B: (not surfaced) | B: private/hidden groups | B: (not surfaced) | B: (not surfaced) |
| Scoped permissions | A: view all / subset / own groups; only admins create leaders | A: staff vs leader accounts; campus-restricted access | B: leaders without admin access | B: staff vs leaders | B: roles |
| Write-back to person records | A: attendance/membership on person (People integration) | B: sync with FellowshipOne/CCB | B: membership + attendance as person attributes | B: people database core | B: profile carries group involvement |
| Children boundary | A: under-13 no Church Center login/group messaging; Check-Ins instead | B: (not surfaced) | B: student groups require leader approval | B: check-in for kids | B: (not surfaced) |
| Non-small-group uses of machinery | A: staff, admin, elders, deacons, recovery, care | B: parishes, non-profits, peer groups, coaching orgs | B: ministry teams, serve teams | B: mission trips, volunteer teams, assimilation | B: serving teams |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being this Type:

1. **The group as a persistent community of record.** A named, ongoing sub-community of the congregation — carrying a designated leader, a bounded membership roster, and how/when it typically meets — held as a durable record that is created, maintained across meetings and seasons, and eventually archived or ended rather than expiring with any single date. (Remove → a dated event or a contact list.)

2. **The congregation-people binding.** Members and leaders resolve to identified people in the congregation's own records — held natively or in an integrated church database — and the group's membership and participation attach to each person's record. The group is a sub-community of a known population, not an open public graph. (Remove → generic social/community group tools.)

3. **The administered group-life loop.** The group's ongoing life is operated and recorded over time: people join and leave under the group's join rules, its meetings and participation are recorded against the roster, the group communicates as a body, and the organization can see and act on all of it. (Remove → a static groups directory; the "management" gone.)

Jointly-held load-bearing tests:

- 1 alone = a groups directory/listing.
- 2 without 1 = the ChMS people-record core.
- 3 without 1+2 = generic group chat / community platform.
- 1+2 without 3 = static org-chart/directory entries.
- 1+3 without 2 = generic club/team group management (Meetup-shaped).
- 2+3 without 1 = attendance machinery with no group containers.

Historical check (§24): a paper card file of home Bible study groups in a church office — one card per group (name, leader, members, meeting night), monthly attendance sheets, the pastor's follow-up list of who stopped coming — satisfies all three legs with no software, no public finder, no leader self-service, and no health metrics. The Methodist class meeting (class leader + class book of member rolls + weekly meeting + pastoral oversight) and the cell-group movement's home groups satisfy the same core. The definition therefore names no finder, no chat, no leader portal, no metrics — all era machinery stays out.

### L1 — Common Mature Structure

Present across the sample (layer B) and documented per-product (layer A):

- **Public group finder / directory** — searchable, filterable listing of joinable groups (by type, life stage, day, location; map views; pre-set filter links); group pages with description, schedule, location, leaders, and a join/contact action. Groups can also be unlisted/private — the finder is the dominant front door, not a requirement of every deployment.
- **Join mechanics** — open signup, request-to-join with leader approval, or closed; join requests as tracked objects (pending/approved/rejected, with applicant messages); enrollment limits (member caps, date limits) that auto-close enrollment.
- **Leader self-service** — lay leaders operate their own groups (roster updates, attendance, messaging) without admin access to the church database; the office keeps oversight.
- **Low-friction attendance capture** — per-meeting attendance recorded by leaders via reminder emails/texts with pre-checked names, no-login forms, guests added on the form.
- **Group messaging** — group-wide announcements, group chat/channels, direct messages, push notifications.
- **Group events** — a group calendar with events and RSVP, visibility-controlled (public vs members-only).
- **Shared resources** — files/links shared with the group (sometimes leader-only).
- **Attendance-based follow-up** — who stopped attending; drop-off and engagement views; visitor tracking.
- **Group health reporting to the organization** — dashboards, monthly health reports, attention flags.
- **Scoped permissions** — admins see all; leaders see their own groups; people-database access for leaders is gated (one vendor marks it "not recommended").
- **Confidentiality postures** — member lists hidden or anonymous (recovery, grief groups), with consequences for community features (chat disabled when members are confidential).
- **Group types and tags** — small groups, Bible studies, youth, women/men, recovery, serving teams, classes, governance bodies.
- **Multi-campus support** with campus-scoped access.
- **Write-back to person records** — group membership and attendance visible on the person's profile beside giving, check-in, and events.
- **Prospect/connection tracking** — seekers tracked from signup to connected member with follow-up reminders.

### L2 — Variant / Optional Structure

- **Coaching layer** — coaches over leaders (and senior coaches over coaches) with a defined span of care; deep in the standalone specialist, absent from other sampled products' public docs. Rooted in cell-group ministry practice, not in software necessity.
- **Health surveys** — member-experience feedback (spiritual growth, connection, recommendation) collected mid-group-life.
- **Leader recruiting machinery** — prospective-leader pipelines.
- **Attendance accountability escalation** — reminders that escalate to staff/coach when leaders don't respond.
- **Chat depth** — full member-visible chat vs announcements-only; interplay with confidentiality.
- **Integration posture** — native people database (suite modules) vs sync with an external church database (standalone specialists).
- **Semester/cycle-based groups** vs continuous groups (seasonal launches, group duplication into a new cycle).
- **Virtual/hybrid groups** (virtual location URLs alongside physical locations).
- **Non-small-group uses of the same machinery** — serving teams, mission trips, governance bodies, staff teams, assimilation tracking (all-in-one systems use groups universally).
- **Non-church organizations** — parishes, non-profits, peer groups, coaching organizations (vendor-stated breadth).
- **Deployment/packaging** — standalone product, suite module, open-source module.

### L3 — Vendor-specific Structure (research notes only)

- Planning Center: GroupApplication/Enrollment object split; enrollment strategies + auto-close reasons; "only administrators or managers can create leaders"; chat-enable blocked when members confidential; leaders_can_search_people_database flagged "Not recommended"; duplicate-group field selection; Church Center public group pages + contact button; pricing by total group members; under-13 ToS boundary; attendance roles include "visitor" and "applicant".
- GroupVitals: active rate (% of last 4 scheduled meetings met); accountability-reminder escalation; health survey; coaches/senior coaches; prospect pipeline stages; no-login roster updates by email; FellowshipOne/CCB sync; spreadsheet import service.
- Tithe.ly: Groups included with ChMS; app-first joining ("Your Groups" section); two-way push via church app; student groups default to leader approval (vendor-stated typical practice).
- Churchteams: Groupfinder links with pre-set filters; Text-to-Church keyword entry; monthly group health reports; prayer requests/study notes flowing from attendance reports to leadership; groups carrying mission trips (contributions through groups) and volunteer teams (Service Volunteer scheduling feature); 45+ report types.
- Pushpay: Needs (meal trains) on groups; LEAD App; engagement tracking framing.
- Rock RMS (prior pass): group requirements enforcing training/background checks; group scheduling with accept/decline and conflicts.

## Vendor-specific Findings

See L3. Additionally: only GroupVitals documents the coaching layer, health surveys, and attendance-accountability escalation; only Planning Center documents the join-request object model and the confidentiality/chat interplay at Tier-1 depth; only Churchteams documents groups carrying mission-trip contributions and volunteer scheduling on the same object. None of these are promoted to the canonical model.

## Boundary Findings

1. **vs Church Management System / ChMS (§25, processed).** The ChMS pass kept Groups out of its L0 ("the strongest L1 item") and classified this leaf as a capability slice owning one loop in depth. Confirmed: the group loop (finder → join → group life → health) is owned here; the ChMS owns the whole-congregation record core (people, giving, check-in, events) of which groups are one organizing unit. The Type exists both as a ChMS module (Tithe.ly, Churchteams, Pushpay, Rock) and as a standalone product (GroupVitals; Planning Center Groups as a standalone product of a modular suite). Remove the group loop → ChMS; remove the whole-congregation core → this Type.
2. **vs Congregation Membership Management (§25).** Whole-congregation roster vs sub-community membership: membership management maintains the congregation's people records and membership status; this Type organizes known people INTO ongoing communities and runs those communities. A person's congregational membership is the substrate; group membership is the structure built on it.
3. **vs Religious Event Management (§25, processed) — FLAG DISCHARGED.** The seam holds: an event is a dated occurrence with registration options and a close; a group is a standing community that persists across meetings and seasons. Groups carry events (group calendars with RSVP) but the group outlives any event. The recorded blur is real and product-specific: Churchteams realizes event registration as a group ("registration is tracked inside a group"), and its own docs use groups "from small group discipleship to events and mission trips" — one machinery, two loops. Planning Center, by contrast, ships Registrations and Groups as separate products. The blur is packaging, not identity.
4. **vs Religious Education Management (§25, processed).** Classes are groups, but education centers the enrollment→class→session-attendance→milestone loop over a program term, with grades, catechists, and sacrament/milestone records; small groups center ongoing community life without terms, grades, or milestones. The education pass already documented the overlap (Protestant Sunday school frequently realized as groups + check-in); the loops remain distinct.
5. **vs Pastoral Care Management (§25, processed) — WATCH-ITEM DISCHARGED.** The prior distinction holds: groups center community membership and group life; care management centers individual care needs (needs, visits, prayer, follow-up). The overlap is real — group-health feedback surfaces care signals (GroupVitals' leader question "How can we be praying for your group?"; Pushpay's meal-train Needs on groups; Churchteams' prayer requests flowing from attendance reports to leadership) — but these are bridges, not identity. Remove the care loop → this Type; remove the group container → care management.
6. **vs Ministry Scheduling / Religious Volunteer Management (§25).** Serving teams are frequently realized as groups (Churchteams FAQ; Rock's group types; Tithe.ly's "serve teams" group type), but the scheduling loop (positions, rotations, times, confirmations) belongs to ministry scheduling. All-in-one systems realize both on group machinery — packaging overlap, not identity. Remove the rotation/scheduling machinery → this Type.
7. **vs Church Communication Platform (§25, processed).** Comms is the sending loop over the records; here messaging is one capability of the group record (group channels, announcements). Remove group management → comms tool; remove the sending loop → this Type.
8. **vs Group Messaging Application / Community Chat Platform (§01).** Conversation-centered products have no group-of-record lifecycle, no leader role, no congregation substrate, no attendance. Group chat here is a feature of the group, not the product's center.
9. **vs Member Community Platform (§25, association side) and generic community/group tools (Meetup-class).** Similar abstract shape (community registry + groups + discussion), but no congregation people-record substrate, no ministry grammar, and (for Meetup-class) an open public graph. Remove the congregation binding → those Types.
10. **"Remove what to become another Type" tests:** remove the group record → people database (ChMS); remove the people binding → generic group community app; remove the life loop → a groups directory; remove the congregation domain → generic club/team management.

## Uncertainties

- Tithe.ly help center returned 403 this pass; Tithe.ly Groups mechanics rest on the product page + its FAQ (operational in tone but Tier 2). No Tier-1 help articles fetched.
- Pushpay's groups depth is thin in public docs (support site unreachable); its Groups observations come from the product page (this pass + ChMS pass). Deep Pushpay group mechanics unverified.
- Rock RMS not sampled as a primary (docs 404 again); its groups observations are prior-pass Tier 2.
- Coaching structures outside GroupVitals could not be verified from public docs; the coaching layer is marked variant (single-product-dominant in the sample), though the underlying ministry practice (supervisors over lay leaders) is widespread — recorded as an inference, not asserted as market fact.
- Synagogue (chavurah) and mosque small-group software not found as a distinct product population; non-church religious breadth rests on GroupVitals' own stated organizational breadth. Small-group software appears to be a Protestant-evangelical-led market — recorded as market-structure observation, not asserted beyond the sample.
- Attendance as strictly definitional vs common-mature: all five sampled products record participation, but a hypothetical roster+join+messaging tool without attendance would arguably still be group management; the canonical phrasing keeps "participation recorded" inside the loop while per-meeting attendance marks are named as the dominant realization.

## Final Synthesis

Religious Small-group Management is the congregation's small-group ministry system: it holds each ongoing group — life group, home group, Bible study, care or affinity group — as a persistent record with a designated leader and a bounded roster bound to the congregation's own people records; it connects people to groups through a find-and-join front door (public finder, open/request/closed join rules, prospect follow-up); it runs each group's ongoing life — meetings, attendance, messaging, shared resources, group events — largely through self-serving lay leaders while staff keep oversight; and it reports the group picture back to the organization (attendance trends, drop-off follow-up, health reporting) with everything writing back to the person's record. The Type exists both as a ChMS module and as a standalone specialist; its center is the group loop, not the record core (ChMS), the dated event (Religious Event Management), the program term (Religious Education Management), the individual care need (Pastoral Care Management), or the serving rotation (Ministry Scheduling). The definition survives the historical check: a paper card file of home groups with attendance sheets and a pastor's follow-up list satisfies the core without any modern machinery.
