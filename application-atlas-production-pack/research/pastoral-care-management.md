# Research Notes — Pastoral Care Management

Research date: 2026-09-08
Slug: pastoral-care-management
Directory leaf: Pastoral Care Management (§25 Nonprofit, Membership & Religious Organizations)

## Research Goal

Establish whether "Pastoral Care Management" is a defensible Application Type (rather than a bare capability slice of a ChMS), and if so, determine its defining core, standard capabilities, variants, and boundaries. Special obligations from prior passes:

- church-management-system-chms (§25, processed) listed pastoral-care-management among "watch-items: … capability slices that exist both as ChMS modules and as standalone specialists — the same module↔standalone spectrum the church-communication-platform leaf documented."
- church-communication-platform (§25, processed) mentioned "pastoral care" as a congregational message job.
- congregation-membership-management (§25, processed) is the record substrate this Type likely attaches to.

## Initial Boundary

Core guess: the church's care-organizing machinery — tracking who needs care (illness, hospitalization, bereavement, homebound, crisis, counseling), assigning care to caregivers (pastors, staff, lay leaders), recording the care given (visits, calls, cards, prayers), and following up until needs resolve — realized mostly as a module or configured workflows inside Church Management Systems, with standalone specialists reportedly existing.

Likely nearest neighbors:

- Church Management System / ChMS (§25, processed) — dominant host environment; flagged this leaf as watch-item
- Congregation Membership Management (§25, processed) — the people roll that care records attach to
- Ministry Scheduling (§25 sibling, unprocessed) — assignment/scheduling overlap (care-team rotations)
- Religious Small-group Management (§25 sibling, unprocessed) — groups are often the care-delivery context
- Care Plan Management (§22) — shares the word "care" but is clinical
- Social Services Case Management (§24) / Nonprofit Case Management (§25) — same workflow shape (intake → assign → visit → follow-up), different institutional logic
- Hospital chaplaincy / spiritual-care documentation (healthcare institutional context) — adjacent, not in the directory as its own leaf

## Research Questions

1. Do products exist that realize pastoral care as a named, documented structure? As a module? As configured workflows? As standalone products?
2. What is the tracked unit — a "care need", a "touchpoint", a task? How does it anchor to a person?
3. How is care assigned (creator/owner/assignee roles, transfer, delegation to lay caregivers)?
4. How are care interactions recorded, and what happens to them (per-person history, keywords/categories, export)?
5. How is confidentiality handled — is visibility restriction structural or optional?
6. What is the follow-up loop (task completion requiring a record? follow-up scheduling? open-item visibility)?
7. What parallel surfaces exist (prayer requests, benevolence/assistance, engagement signals as triggers)?
8. Historical check (§24): do pre-software pastoral care practices satisfy the proposed core (visitation logs, care card files, prayer chains, elder districts, confidential counseling files)?
9. Boundary vs ChMS, case management, healthcare care-plan management, ministry scheduling, small groups.

## Representative Products

| Product | Position in market | Why sampled | Evidence tier |
|---|---|---|---|
| TouchPoint | Enterprise ChMS for large churches; sells a named "Pastoral Care Software" feature (Tasks & Notes) with a dedicated product page and public documentation | The cleanest named-module realization with Tier-1 operational docs; defines the machinery in depth | Tier 2 product page + Tier 1 docs (Tasks, Notes, Tracking, Confidential Extra Values) |
| Rock RMS | Open-source ChMS (self-hosted or cloud); pastoral care realized via workflows/connections/prayer rather than a dedicated module | The workflow-assembly realization; large-church pole | Tier 2 (homepage + features page) |
| Planning Center | Modular SaaS suite; People is the record core; no dedicated pastoral-care product in the suite | Negative/contrast evidence: a major ChMS ships no named care product — the care loop is assembled from People workflows + notes; Church Center carries member-side prayer requests | Tier 2 (homepage/product list; changelog); plus Tier-1/2 People notes evidence recorded in the congregation-membership pass |
| ChurchTools | German-market SaaS ChMS (free churches/parishes) | Regional (§24) check: does a non-US market document a dedicated care module? | Tier 1 (help KB structure, modules index) |
| Churchteams | Mid-market full-suite ChMS | Mid-market suite without a named care page — automation/workflows as the machinery | Tier 2 (homepage) |

Sample rationale: one named-module realization (TouchPoint, deeply documented), two workflow-assembly realizations (Rock, Planning Center), one regional non-US check (ChurchTools), one mid-market boundary anchor (Churchteams). Customer tiers span large multi-site churches (TouchPoint, Rock) to small/mid churches (Churchteams, ChurchTools). No single vendor's philosophy dominates the sample.

## Sources

All fetched 2026-09-08 unless noted:

- TouchPoint — Pastoral Care Software feature page — https://www.touchpointsoftware.com/features/pastoral-care-software/ (Tier 2)
- TouchPoint — Documentation index — https://docs.touchpointsoftware.com/ (Tier 1 index)
- TouchPoint — Tasks & Notes section index — https://docs.touchpointsoftware.com/ContactsAndTasks/index.html (Tier 1)
- TouchPoint — Tasks — https://docs.touchpointsoftware.com/ContactsAndTasks/Tasks.html (Tier 1)
- TouchPoint — Add a Note — https://docs.touchpointsoftware.com/ContactsAndTasks/AddContact.html (Tier 1)
- TouchPoint — Tracking Tasks and Notes — https://docs.touchpointsoftware.com/ContactsAndTasks/TrackingTasks.html (Tier 1)
- TouchPoint — Confidential Comments as Extra Values — https://docs.touchpointsoftware.com/ExtraValues/ConfidentialComments.html (Tier 1)
- Rock RMS — homepage — https://www.rockrms.com/ (Tier 2)
- Rock RMS — features — https://www.rockrms.com/rock-features (Tier 2)
- Planning Center — homepage/product list — https://planning.center/ (Tier 2)
- Planning Center People notes/hidden-content evidence: recorded in research/congregation-membership-management.md (People Tier-2 page + Tier-1 custom-fields article from the ChMS pass, 2026-09-07)
- ChurchTools — Help KB, Modules index — https://churchtools.academy/en/help/churchtools-modules/ (Tier 1 structure)
- Churchteams — homepage — https://www.churchteams.com/ (Tier 2)

Unreachable this pass (recorded per source-access limitation rules; no memory-fill of their content):

- carenote.com — transport error ×2 (1st: GET https://carenote.com/ ; 2nd: GET https://carenote.com). CareNote is believed to be a standalone care-ministry product, but no content could be verified; its existence is therefore NOT used as product evidence.
- Search engines: html.duckduckgo.com + lite.duckduckgo.com timeouts ×2; Bing returned region-redirected irrelevant results; Mojeek captcha. Market-scan breadth is incomplete.
- wiki.rockrms.com manual (Tier-1 Rock detail) not fetched — Rock evidence stays features-page tier.
- TouchPoint Mobile App prayer-request help article not fetched — prayer evidence for TouchPoint stays feature-page tier.
- ChurchTools "Understanding follow-ups" article not fetched (index lists it); no claims made about its content.

## Product A — TouchPoint (Pastoral Care = "Tasks & Notes")

### Key observations (evidence layer A unless noted)

**Positioning (Tier 2):** dedicated feature page titled "Pastoral Care Software". "Care for every church member… track ministry follow-ups, record important conversations, and organize pastoral touchpoints, so no one slips through the cracks." Enterprise framing: "TouchPoint gives your team the visibility, workflows, and case tracking that serious pastoral care requires." Marketing pairs care with engagement insights ("a member quietly disengaging… someone walking through crisis… tracking care over time, coordinating follow-up"). FAQ: Tasks & Notes are "part of the wider TouchPoint Church Management System, meaning the care interactions tie back into the person's record — a single source of truth for attendance, giving, serving, and care touch-points." Target: "churches that have multiple ministries, are managing growth…"

**Ministry Tasks (Tier 1):**
- "TouchPoint has 2 types of Tasks" — Ministry Tasks and System-Generated Tasks. Ministry Tasks: "used in conjunction with Notes to help you follow up with your guests, minister to absent members, those in the hospital, or anyone with whom you need someone to communicate."
- Structure: a Ministry Task is "always **about one individual** and can be **assigned to another individual**". Named roles: Task Creator, Task Owner (monitors; receives acceptance/completion notifications), Task Assignee ("the person assigned to perform the Task… the minister"; must have a user account, full access or OrgLeadersOnly), Task About ("the person to be contacted or ministered to").
- Bulk creation: one task per person, created singly or "for a group of people at one time (from a Search or any list)" — use case: "On Sunday, 10 people visit your church worship service and you want to assign the appropriate staff member or lay leader a Task to follow up with each one, and you want a record of the contact in TouchPoint."
- Fields: Task Details (character-limited), Due Date, Keywords (admin-configured; documented examples "Pastoral Care", "Women's Ministry", "Prayer Request"; also "Hospitality, Marriage Ministry, Family Ministry, or Bereavement" on the Tier-2 page), Limit to Role ("If the Task you are creating is sensitive in nature").
- Lifecycle and notifications: creation emails the assignee; Type flows **Pending Acceptance → Accepted → Completed**; Accept/Decline actions (decline prompts for a reason; owner can then Complete or Edit); email notifications on assigned/accepted/declined/completed; owner keeps the task on the Task Search page until completed; assignee keeps it on the Home Page "My Task List" until completed; "My Action Required" filter; mass Assign/Complete/Archive/Delete; ownership transfer (documented tiered use case: a ministry assistant transfers tasks to owners — often life-group leaders — who then assign to lay leaders or complete themselves).
- Open items stay visible on the About person's record ("The Incomplete Task will display on the Touchpoints > About tab of the person about whom the Task was created").
- System-Generated Tasks are administrative (new-record data entry; failed recurring gift) — not pastoral machinery, but show tasks as a general work mechanism.

**Notes (Tier 1):**
- Purpose: "After you have made any sort of a contact with a member or guest and the information about that visit/call would be helpful for others to know when they are ministering to this person… Some common scenarios are: Personal visit; Phone call; Card or letter."
- Structure: Note Owner (who recorded it; the person logged in), Note About (the person; "can search and add additional people"), note details (character-limited), Keywords, Event Date (defaults to current date), **Limit to Role** ("This will limit the Note's visibility to only those with the corresponding role").
- Explicit confidentiality guidance: "(Do not add confidential information unless using the Limit to Role function)" and "once you select a role, only users with that role can see that the person had been contacted."
- Notes carry more control than profile-tab comments ("You will have more control over the roles that can view these Notes than if entered as a comment").
- From a note you can create a **Follow-Up Task**; mass actions: delete, add keywords, export to Excel.

**The completion rule (Tier 1):** "In order for a Task to be completed, the Assignee will have to **complete a Note**." The completed note lands on both the assignee's Owned/Assigned tab and the About person's Touchpoints tab. The care record is the deliverable of the care assignment.

**Where records live (Tier 1):** three surfaces — Tasks & Notes Search page (filter by keywords, owner, assignee, about, campus, dates; sort; manage); the person's **Touchpoints tab** (shows items owned by/assigned to or about that person); the Home Page **My Task List** widget (incomplete tasks assigned to the user). Search Builder conditions ("Has Incomplete Task", "Has Task With Name") find people with open care items.

**Visibility model (Tier 1, extensive):**
- Base access role required to view any tasks/notes; users cannot see tasks/notes about themselves.
- Unrestricted items visible to all base-access users; **role-restricted (private)** items visible only to holders of that role (example: a task limited to the Finance role visible only to Access+Finance holders).
- Special roles: Admin and a dedicated full-access care role see all; another role can "view all private tasks and notes"; a limited-leader role (OrgLeadersOnly) sees only people in involvements they lead — the documented mechanism by which **lay caregivers** get scoped access.
- Explicit staff-visibility warning: "any staff members with the Access role will be able to see Tasks & Notes about *anyone*… unless they are limited to a role… Be sure to limit sensitive Tasks & Notes to roles that only the appropriate people have."

**Person-level confidential fields (Tier 1):** Extra Values (custom person fields) can be assigned a Visibility Role — documented example: a multi-line-text "Confidential Notes" field visible/editable only to a specially created role. "Any type of Extra Value can be assigned a Visibility Role."

**Prayer requests (Tier 2):** in the church-branded mobile app — individuals submit prayer requests, choose anonymous prayer, "your team can review requests before they are shared more broadly"; the app shows how many people have prayed; hold-to-mark-prayed interaction.

**Automation (Tier 2 FAQ):** Process Builder generates tasks from conditions — "when a certain condition is met (e.g., a guest hasn't attended in 3 weeks), a Task can be generated automatically and assigned to the appropriate leader." Tasks/notes available in the mobile app.

## Product B — Rock RMS

### Key observations (evidence layer A for the fetched pages, Tier 2)

**Positioning:** open-source ChMS ("manage people, processes and communication"); cloud-hosted or self-hosted; large-church pole (claims about powering 10 of the 12 largest churches; 36M+ people records).

**Care-relevant features (features page):** the Church Management intro names "coordinating pastoral workflows and supporting prayer needs" as a platform job. Relevant machinery:
- **Prayer** as a first-class feature: "Manage Large Volumes of Prayer Requests", "Deliver High-Impact Prayer Experiences", "AI-Powered Prayer Moderation", "Automated Self-Harm Alerts" — prayer intake treated as a care surface with safety escalation.
- **Workflows**: "Automate Complex Processes", easy form building, versatile triggers, scalable/customizable — pastoral care is coordinated by configuring workflows, not by a fixed care module.
- **Connections**: "Automate follow-up for first-time guests or ministry interest; Assign connection requests to staff or volunteers; Track progress from initial contact to full engagement" — the assignment-and-tracking loop generalized beyond care.
- **People Management**: individual/family profiles, custom attributes, **Configurable Notes**.
- **Finance Tools**: "Pledges & **Benevolence Management**" — assistance/charity-giving record-keeping inside the same platform.

**Interpretation:** Rock demonstrates the workflow-assembly pole — the pastoral care loop exists as configured workflows over people records plus a dedicated prayer subsystem, rather than a named "pastoral care" module.

## Product C — Planning Center

### Key observations (evidence layer A for the homepage; notes evidence from the sibling pass)

**Product list (Tier 2, fetched):** People ("Free membership database"), Groups, Calendar, Registrations, Check-ins, Services, Music Stand, Church Center ("Custom mobile app for your church"), Publishing, Giving, Home ("Dashboard & task management"). **No pastoral-care product exists in the suite** — the negative observation that a major modular ChMS ships no named care product.

**Care-adjacent machinery (same page):** Church Center members can "submit prayer requests" among built-in participation ways; People has workflow machinery with steps and cards (changelog entries: "Automatic actions for workflow steps", "Snooze workflow cards overnight"); homepage testimonial from a Connections Director: "I want to make sure no one falls through the cracks…".

**From the congregation-membership pass (2026-09-07):** People notes are documented for "prayer requests, counseling notes, and health conditions", with hidden-content masking for non-collaborators; workflows track "peoples' progress toward specific goals".

**Interpretation:** the care job exists (guest follow-up, prayer, sensitive notes) and is realized through People workflows + masked notes + member-side prayer capture, without a named care module. Confirms the machinery is separable from the packaging.

## Product D — ChurchTools (German market)

### Key observations (evidence layer A for KB structure, Tier 1 index)

**Modules documented in the English help KB:** People (17 pages, incl. "Understanding follow-ups"), Groups (57), Posts, Calendar, Events, Resources, Check-in, Report, Wiki, Finances, Sync. **No pastoral-care/Seelsorge module appears in the documented module structure.**

**Care-adjacent machinery that does appear:** follow-ups in the People module (article listed; not read this pass — no claims about its content); group types/visibilities/roles (a care team would be a group); person fields and a dedicated Permissions Management KB (35 pages); automatic group membership and "routines" (workflow-like automation) in Groups.

**Interpretation:** regional check — a German-market ChMS documents no dedicated care machinery at module level; care-adjacent work runs through people follow-ups, groups, and permissions. The Type, if defined, must not require a "care module" as its defining structure.

## Product E — Churchteams

### Key observations (evidence layer A, Tier 2)

**Product list:** People & App, Check-in, Volunteers, Text-to-Church, Communication, Groups, Giving, Registration (Events & Forms), Automation, Websites. **No pastoral-care feature page** among the marketed features.

**Care-adjacent framing:** support culture claim ("all our staff have a vision for ministry and pastoral care"); "track progress, and add benchmarks to member records through automation" (FAQ); Churches' engagement/discipleship tracking via automation.

**Interpretation:** mid-market boundary anchor — full suite, care realized (to the extent marketed) through people records + automation, not a named care module.

## Cross-product Comparison

| Structure | TouchPoint | Rock RMS | Planning Center | ChurchTools | Churchteams |
|---|---|---|---|---|---|
| Care items anchored to an identified person | A (task About = one individual; bulk creation creates one task per person) | B (connections follow up on individuals; workflows over people) | B (People workflows; notes on person records) | B (follow-ups/groups attach to people) | B (automation benchmarks on member records) |
| Care assignment to a named caregiver | A (creator/owner/assignee; transfer; accept/decline; lay caregivers via limited roles) | A (connections: assign requests to staff or volunteers) | B (workflow cards assigned to people) | B (group roles; not verified) | B (automation assigns work; not verified in detail) |
| Care interaction recorded as a durable person-bound note | A (notes: visit/call/card; about person; event date; completion requires a note) | B (configurable notes; workflows record progress) | B (notes incl. prayer/counseling/health; masked) | B (person fields; group notes exist) | B (member records + automation; not named) |
| Restricted visibility for sensitive records | A (role-limited tasks/notes; confidential person fields with visibility roles; "do not add confidential information unless…") | — (not observed on fetched pages) | B (hidden-content masking for non-collaborators; sibling pass) | B (dedicated permissions KB) | — |
| Follow-up loop (open items persist; follow-up from records) | A (follow-up task from note; incomplete tasks persist on About person; My Action Required; decline→reassign) | B (connections track progress from contact to engagement) | B (workflow steps; snooze cards) | B (follow-ups article exists, unread) | B (automation; benchmarks) |
| Prayer requests as capture surface | A/B (feature-page: submit, anonymous, staff review before sharing, prayer counts) | A (prayer feature: manage volumes; moderation; self-harm alerts) | A/B (Church Center prayer submission) | — | — |
| Care categories/keywords | A (admin-configured keywords; documented examples: Pastoral Care, Prayer Request, Bereavement) | — | — | — | — |
| Automation triggers into care | A/B (Process Builder: attendance-lapse → task) | B (workflow triggers) | B (workflow automatic actions) | B (routines/automatic membership) | B (automation) |
| Reporting on care activity | A (search/filter by keyword/owner/about/date; Search Builder incomplete-task conditions; Excel export) | — | — | — | — |
| Benevolence/assistance tracking | — | A (Benevolence Management in Finance tools) | — | — | — |
| Named care module/page | A (dedicated "Pastoral Care Software" page) | — ("pastoral workflows" named as platform job, not module) | — (explicitly no care product) | — (no care module in KB) | — (no care page) |
| People-record substrate | A (single source of truth: care ties to person record) | A (people records core) | A (People is the record core) | A (People module) | A (People & App) |

Reading of the table: the person-anchored care item, assignment to a caregiver, the person-bound care record, and the follow-up loop are present in every sampled product at some evidence strength; the *packaging* differs (named module / configured workflows / record-level notes+permissions). Visibility restriction is documented in structural depth at TouchPoint, present as masking/permissions elsewhere, absent (unobserved) in two fetched pages — keep it a standard expectation, not a definitional invariant. Prayer requests appear in 3 of 5 as a parallel capture surface. No standalone pastoral-care product could be verified this pass.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as pastoral care management:

1. **The care need anchored to an identified person** — a recorded need or situation (illness, hospitalization, bereavement, absence, crisis, counseling, prayer request) bound to a specific person in the congregation's people records, entering by referral, staff entry, or self-submission. (Remove → generic notes/tasks with no care subject; also the congregation anchor is what makes it pastoral rather than generic.)
2. **The assigned caregiving loop** — responsibility for the need is given to a named caregiver (pastor, staff, or lay leader); the work appears on the caregiver's list; contact is made; the loop continues with follow-up until the need resolves. Ownership is transferable/delegable. (Remove → an unmanaged prayer list or bulletin notice; without the person anchor it is generic task management; without the loop it is a one-off visit log.)
3. **The person-bound, visibility-restricted care record** — each care contact (visit, call, card, conversation) is recorded as a durable note attached to the person's record, held under visibility restricted to those entrusted with the care, accumulating as the person's care history. (Remove → the assignment loop becomes bare to-do tracking; without restriction the pastoral-privilege dimension collapses into ordinary CRM activity logging.)

Jointly load-bearing: 1 alone = prayer-request/needs list; 2 without 1 = generic task/volunteer assignment (ministry-scheduling territory); 3 without 1+2 = a notes field or CRM activity log; 1+2 without 3 = ephemeral follow-up tooling with no care record; 1+3 without 2 = care-note archive nobody is responsible for; 2+3 without 1 = generic task tracking with notes, not bound to care needs of congregation people.

Historical check (§24): the paper pastoral-care practice satisfies all three — the visitation card file (per-parishioner cards: reason — illness, bereavement, homebound; each visit dated and noted) anchors needs to persons; the pastor/deacon/elder assignment (including the visitation-district tradition in European parishes) is the assigned caregiving loop with follow-up ("next visit due"); the records live in the pastor's desk / session file — physically visibility-restricted, accumulating as care history; the prayer-chain list is a parallel capture surface. None of the modern machinery (apps, workflows, keywords, dashboards) is required. Older, regional, and low-tech realizations therefore fit the definition.

Deliberately NOT in L0: prayer-request machinery (parallel surface, common but optional); keywords/categories; reporting; automation; mobile access; benevolence; member-facing apps; the specific roles vocabulary (creator/owner/assignee is one documented implementation); "module" as a packaging form (workflow and record-level realizations satisfy the core).

### L1 — Common Mature Structure

Present across the sample (layer B) and documented per-product (layer A where marked):

- **Prayer request capture and handling** — submission (often member-facing via app), review before sharing, prayer lists/streams; prayer counts in one product (A/B, TouchPoint Tier-2; Rock A; PCO A/B)
- **Care categories/keywords** as a searchable taxonomy over care touches (A, TouchPoint; categories implied by workflow naming elsewhere)
- **Reporting on care activity** — completed/incomplete items, by caregiver, by category, by person; export (A, TouchPoint)
- **Open-item persistence and follow-up** — incomplete care items remain visible on the person's record; follow-up scheduled from completed contacts (A TouchPoint; B others)
- **Automation triggers** — attendance lapse, new guest, form submission generating care items (B across TouchPoint/Rock/PCO/ChurchTools/Churchteams)
- **Mobile access** for caregivers in the field (A/B)
- **Care team organization via groups/roles** — lay caregivers as limited-access users; scoped visibility roles (A TouchPoint; B ChurchTools/PCO)
- **Benevolence/assistance funds** adjacent to care (A Rock)
- **Engagement/attendance signals** as care triggers (A/B)

### L2 — Variant / Optional Structure

- **Packaging**: named module of a ChMS (TouchPoint) vs configured workflows over ChMS records (Rock, Planning Center, Churchteams) vs record-level notes + permissions (ChurchTools) vs standalone specialist products (market-reported; unverifiable this pass)
- **Church size poles**: small church = pastor's notes and prayer list; large multi-staff church = care pastors, ministry assistants routing assignments, engagement dashboards, "case-like" care management
- **Tradition shapes**: evangelical follow-up culture (guest care, engagement-triggered care) vs parish/denominational homebound and sacramental visitation vs institutional chaplaincy (hospital/military — different institutional owner; adjacent, not evidenced this pass)
- **Member-facing surfaces**: prayer submission with anonymity, prayer counters (products vary; not universal)
- **AI moderation of prayer content and safety alerts** (single-product evidence — product-specific, not promoted)
- **Multi-campus care coordination**

### L3 — Vendor-specific Structure (research notes only)

- TouchPoint: 5,000-character limits on task details and notes; keyword lists admin-configured (LimitToRolesForTasksNotes setting; Admin > Advanced > Settings path); email template set (System Task Assigned/Accepted/Declined/Completed); role names (Access, OrgLeadersOnly, ManageTouchpoints, ViewPrivateTouchpoints); users cannot see tasks/notes about themselves; System-Generated Tasks (New People Data Entry; Failed Gift); My Task List homepage widget; mass actions incl. Excel export; Search Builder conditions ("Has Incomplete Task", "Has Task With Name"); sample Standard Extra Values shipped in newer databases; Process Builder attendance-lapse example (guest absent 3 weeks); hold-to-pray interaction and prayer counters in the app; pricing model (price-per-active-record, no tiers); CCB-alternative positioning.
- Rock: Spark Development Network project; RX26 conference; 36M+ people records / $5B+ giving metrics; 10-of-12 largest churches claim; AI agents; LMS; self-harm alert automation in Prayer; benevolence inside Finance tools.
- Planning Center: per-product pricing; People free; "no outside investors" positioning; changelog cadence (workflow snooze, automatic step actions); processed-fee comparisons; compare-pages naming competitors (Tithe.ly, Breeze, ChurchTrac, Pushpay, Subsplash).
- ChurchTools: SKR 42 chart of accounts, Optigem/DBSync imports, euBP exam — German-market finance machinery (irrelevant here but shows regional packaging); Finder; academy/forum support structure.
- Churchteams: Text-to-Church keyword mechanics; 25+ years; 70M emails claim; competitor comparisons (CCB, Church Trac, Planning Center).

## Vendor-specific Findings

- Only TouchPoint documents the care machinery at Tier-1 depth (task roles, completion-requires-note rule, visibility model, confidential person fields). Its specific role names, limits, and settings must not be promoted to the canonical model.
- Only Rock documents AI prayer moderation and automated self-harm alerts (single-source → optional/product-specific).
- Only Rock documents benevolence management on the fetched pages (single-source → optional).
- Only TouchPoint markets a dedicated "Pastoral Care" feature page among the sample; its absence elsewhere is packaging, not capability, absence (workflow/notes realizations carry the same loop).
- No standalone specialist could be verified — the market existence of standalone care-ministry products remains unproven in this record.

## Boundary Findings

1. **vs Church Management System / ChMS (§25, processed) — the watch-item from that pass.** Outcome: **keep-both with a center-of-gravity seam.** ChMS = the roll + whole-ministry machinery (membership, giving, groups, events, check-in, comms) operated as one system. Pastoral Care Management = the care loop (need → assignment → contact → record → follow-up) as the center of gravity, with the people records as substrate. Realizations documented at both poles of the spectrum the ChMS pass anticipated: a named module (TouchPoint sells it as a productized feature with its own page and docs) and workflow/record-level realizations (Rock, Planning Center, Churchteams, ChurchTools). Removal tests: strip care loop from a ChMS → still a ChMS (Planning Center ships none); strip the whole-ministry machinery and keep only the care loop → still this Type. Packaging is a variant axis, not the definition. Market-structure note: no independently-sold standalone product was verifiable this pass; if the market later proves to be module-only, this leaf degrades toward a ChMS capability — flagged in STATUS for a future joint review rather than resolved here.
2. **vs Congregation Membership Management (§25, processed).** The roll is the substrate: care needs and records attach to people held on the roll (TouchPoint explicitly ties care touch-points to the person record "single source of truth"). The roll leaf owns people/households/status; this leaf owns what the church does for people in need. Membership status is not required for a care need (guests and non-members receive care too — documented: tasks "about your guests").
3. **vs Ministry Scheduling (§25 sibling, unprocessed).** Overlap where care teams are rostered (visitation rotations). Distinction: scheduling centers service/role rosters for events and ministries; this Type centers the care need and its loop. Assignment machinery (assignee/owner) is shared grammar. Watch-item for joint review.
4. **vs Religious Small-group Management (§25 sibling, unprocessed).** Small groups are often the care-delivery context (TouchPoint's own transfer use case routes care to life-group leaders). Distinction: groups center community membership and group life; this Type centers individual care needs. Watch-item.
5. **vs Care Plan Management (§22 healthcare).** Shares the word "care". Distinction: clinical care plans hold assessments, goals, interventions, clinical terminology, orders, and clinical outcomes under healthcare governance; congregational care holds visits, calls, prayer, and counseling under church governance with no clinical content. Remove clinical machinery from Care Plan Management and it stops being that Type; add it here and it stops being this Type.
6. **vs Social Services Case Management (§24) / Nonprofit Case Management (§25).** Same workflow shape (intake → assign → visit → follow-up). Distinction: case management centers a case record with assessment, service plan, eligibility, benefits/program context, and outcomes reporting to funders/agencies; pastoral care centers person-level ongoing care relationships — visitation, prayer, confidential notes — typically delivered by volunteers and staff without eligibility machinery, and resolved relationally rather than through benefit determination. In large churches the loop takes case-like shapes (an enterprise vendor markets "case tracking"), so the seam is a gradient; the absence of program/eligibility/benefits machinery is the practical test.
7. **vs CRM activity notes / generic task management.** The same objects (notes, tasks) exist there; what makes this a distinct Type is the congregation context, the care-need semantics, and the structural confidentiality expectation. Remove the person-need anchor → task manager; remove confidentiality → CRM notes.
8. **vs hospital chaplaincy / spiritual-care documentation.** Adjacent institutional variant in clinical settings, owned by healthcare institutions; no directory leaf; products not researched. Recorded as unverified adjacency.

## Uncertainties

- **Standalone realization unverified.** CareNote (believed standalone care-ministry product) unreachable ×2; search engines degraded (DDG timeouts, Bing regional redirect, Mojeek captcha). The market breadth scan is incomplete; "module-dominant" is the honest, evidenced framing.
- Rock, Planning Center, and Churchteams care detail is Tier-2 (marketing/changelog tier); no Tier-1 help articles fetched for those products this pass. Their loop presence is cross-product (layer B) with named features (layer A), but operational rules (exact states, permissions, limits) were not verified per product.
- TouchPoint prayer-request observations are feature-page tier (the Mobile App help article was not fetched).
- ChurchTools "no care module" is an observation about the English help KB structure only — not a claim about undocumented capabilities; its follow-ups article was listed but not read.
- Historical-check specifics (visitation districts, prayer chains, session/deacon files) are reasoned from domain knowledge for the §24 check, not evidenced from product docs — used only as era-logic, not asserted as product fact.
- Chaplaincy/spiritual-care documentation products unverified; benevolence workflows not researched in depth.

## Final Synthesis

Pastoral Care Management is a defensible Application Type whose defining core is three jointly-held structures: the care need anchored to an identified person in the congregation's records; the assigned caregiving loop (a named caregiver takes responsibility, makes contact, and follows up until the need resolves); and the person-bound, visibility-restricted care record that accumulates as the person's care history. The market realizes the Type almost entirely inside Church Management Systems — as a named, productized module at one pole (TouchPoint) and as configured workflows plus record-level notes/permissions at the other poles (Rock, Planning Center, Churchteams, ChurchTools) — with the packaging a variant axis, not the definition. Prayer requests form a parallel capture surface; reporting, keywords, automation, and mobile access are standard but not definitional. The definition survives the historical check (visitation card files, assigned elder/deacon visitation, prayer chains, confidential counseling files satisfy all three structures with no software). Boundaries hold against ChMS (whole-ministry system vs care-loop center), membership management (substrate vs loop), healthcare care-plan management (clinical machinery), and case management (program/eligibility machinery). The unverified standalone-specialist market remains the one open question, recorded for a future taxonomy review.
