# Research Notes — Church Management System / ChMS

Research date: 2026-09-07
Slug: church-management-system-chms
Directory leaf: Church Management System / ChMS (§25 Nonprofit, Membership & Religious Organizations)

## Research Goal

Understand what a Church Management System (ChMS) actually is as an Application Type: what objects exist inside it (people, households, groups, attendance, contributions, check-ins), who operates it and how, what the member lifecycle looks like, how the record core relates to the surrounding church-software modules (giving, communication, scheduling, worship planning), and where the boundary lies against Nonprofit CRM, Membership Management, AMS, and the sibling §25 leaves.

## Initial Boundary

Core guess: the church's central record system — congregation people records (individuals + households) with participation history (attendance, giving, group involvement), operated by church staff/leaders for ministry administration, with member-facing self-service as a secondary surface.

Likely nearest neighbors:

- Church Giving Platform (§25 sibling, processed) — contribution record overlap
- Church Communication Platform (§25 sibling, processed) — messaging module overlap
- Nonprofit CRM / Donor Management System (§25) — structurally similar
- Association Management System / AMS (§25, processed) — flagged ChMS as adjacent
- Membership Management System / Congregation Membership Management (§25) — possible slice/alias
- Ministry Scheduling, Worship Planning, Religious Small-group Management, Pastoral Care Management, Religious Volunteer Management (§25) — capability slices
- Childcare Management System (§25, processed) — check-in overlap
- CRM (§07) — generic relationship-record grammar

Prior sibling findings to respect:

- church-giving-platform: "ChMS owns people/membership/ministry life; the giving platform owns collection channels + contribution records + money movement… if the product's center of gravity is parish life (groups, classes, check-in, pastoral care) it is ChMS even with a contributions module."
- church-communication-platform: "ChMS is the record system (people, groups, events, giving); this Type is the communication loop over those records… Remove the sending loop → ChMS." Also documented the spectrum: standalone comms tools / ChMS-embedded messaging modules / ChMS with no comms product (Planning Center).
- association-management-system-ams: ChMS "structurally similar (people records, giving, groups) but a distinct market with its own leaf; adjacent, not the same Type."
- chapter-management-platform: campuses are internal locations of one congregation, not self-governing subordinate units.

## Research Questions

1. What is the central record object — person, household, or family? What lives on it?
2. How do people enter the system (first-time guest, connection card, form, check-in) and what lifecycle states exist (guest → regular → member → inactive)?
3. What are groups (small groups, classes, teams) and how do leaders relate to them?
4. How does attendance work — event attendance, group attendance, headcounts, check-in?
5. How does children's check-in work — security labels, pickup authorization, what makes it a safety system?
6. How do contribution records relate to people records (record-keeping vs collection)?
7. What workflows exist for follow-up and pastoral care (guest follow-up, care, volunteer pipelines)?
8. What roles and permissions exist (staff, lay leaders, volunteers, members) and how granular are they?
9. What does the member-facing surface do (portal/app: profile, directory, giving, signups, schedules)?
10. How do the surrounding modules (communication, scheduling, worship planning, websites/apps) relate to the record core?
11. What variant poles exist (denominational heritage, packaging, deployment, scale)?
12. Historical check: would a 1990s office membership database or a Catholic parish census system still fit the definition?

## Representative Products

| Product | Position in market | Why sampled | Evidence tier |
|---|---|---|---|
| Planning Center | Modular suite; free People database + paid per-product modules; very large installed base | Modular-suite philosophy; strongest public documentation | Tier 1–2 (4 pages: People, ChMS use-case, Check-Ins, Groups + 1 Tier-1 help article) |
| Tithe.ly Church Management (formerly Breeze ChMS) | SMB/simple pole; flat-price all-in-one | Simple-all-in-one philosophy; rebrand of a well-known SMB ChMS | Tier 2 (product page with vendor ChMS definition + FAQ) |
| Pushpay ChMS (formerly Church Community Builder) | Enterprise pole; engagement/giving-led suite | Enterprise philosophy; CCB heritage = process-queue lineage; names its own competitors | Tier 2 (2 pages: homepage + dedicated ChMS page with vendor ChMS definition + FAQ) |
| Rock RMS | Open-source, self-hosted pole | Open-source philosophy; widest feature surface (websites, TV apps, LMS) | Tier 2 (features page) |
| ParishSOFT | Catholic parish/diocese heritage pole | Regional/denominational heritage check; census/sacramental model | Tier 2 (homepage + module index) |

Sample rationale: two philosophy poles (modular vs all-in-one), one enterprise engagement-led pole, one open-source pole, one denominational-heritage pole. Customer tiers span church plants to multi-site large churches and dioceses.

## Sources

All fetched 2026-09-07:

- Planning Center People — https://planning.center/people (Tier 2 product page)
- Planning Center as a Church Management System — https://planning.center/use-cases/chms (Tier 2 use-case page)
- Planning Center Check-Ins — https://planning.center/check-ins (Tier 2 product page)
- Planning Center Groups — https://planning.center/groups (Tier 2 product page)
- Planning Center People help: Manage custom fields — https://pcopeople.zendesk.com/hc/en-us/articles/204263134 (Tier 1 help article)
- Tithe.ly Church Management — https://tithe.ly/chms (Tier 2 product page; 404 on https://www.tithely.com/products/church-management first try, recovered via /chms)
- Pushpay — https://www.churchcommunitybuilder.com/ (redirects to Pushpay homepage; Tier 2)
- Pushpay ChMS — https://pushpay.com/product/chms-software/ (Tier 2 product page; 404 on /products/church-management first try, recovered via /product/chms-software/)
- Rock RMS features — https://rockrms.com/rock-features (Tier 2; /Rock/Book returned 404 — book documentation not reachable this pass)
- ParishSOFT — https://www.parishsoft.com/ (Tier 2 homepage + module index)

Sibling research reused for boundary context (not for product claims): research/church-giving-platform.md, research/church-communication-platform.md, research/association-management-system-ams.md, research/chapter-management-platform.md.

## Product A — Planning Center

### Key observations (evidence layer A unless noted)

**Positioning:** "People is the free membership database of the Planning Center platform—where you can centralize information from across your ministries." FAQ explicitly compares itself to "other church management systems like F1, Tithe.ly, Breeze, CCB/PushPay, and Shelby" and differentiates on being free. Use-case page: "Planning Center as a Church Management System — Equip your team and connect your church with a single system."

**People (record core):**
- Person profile: default fields (name, birth date, gender, contact details — Tier-1 help article); custom fields/tabs (text, paragraph, date, yes/no, dropdown, checkboxes, number, file) usable in list rules, forms, and the congregant's Church Center profile
- Ministry activity on the profile: "attendance, giving, volunteering, and more"
- Notes: "prayer requests, counseling notes, and health conditions"
- Background checks: "order and monitor background check completion and expiration dates"
- Communication history tracked "for up to three months"
- Duplicate merge; CSV import/export
- Lists: rule-based people queries ("attended Sunday Services at any location, ever"), auto-refresh, organized by campus/category; contact people from a list via text/email/Church Center announcement
- Workflows: "multi-step workflows to track peoples' progress toward specific goals like becoming a member or serving in a ministry"; forms auto-add people to workflows; automations (welcome email after connection card, background-check task after volunteer signup, profile updates like age/membership status/primary campus)
- Permissions: "assign the appropriate permission level to each user"; custom-tab collaborators by role or name — non-collaborators see "[hidden content]" instead of field answers (field-level privacy, Tier-1)
- Schools field with grade promotion ("Promotes To")

**Check-Ins (child safety):**
- Unlimited check-in stations; name tags + parent security labels
- Volunteer-run station (create profiles for new children, search for regulars); self-check via Church Center (pre-check barcode/QR); classroom clipboard checklist
- Security labels: custom editor (birthdays, allergies, diaper bags, contact info); system "automatically restricts certain information—such as child location, or contact information—from the parents' security label"
- Emergency texting to parents; medical notes displayed on name tags; live class lists (who checked in/out, when); multicampus selections
- Check-out: match security labels or scan barcodes; roster check-off; "verify trusted people… who's a safe person to pick them up, even if labels don't match"
- Attendance reports filterable by event type/date/classroom/grade; lists like "first-time visitors" and "households without adult contact information"
- Grade promotion in one click; Headcounts free app; background checks via Checkr integration; volunteer check-in
- Pricing by unique check-ins on busiest day

**Groups:**
- "Create groups for every part of your church": small groups, Bible studies, staff, admin, elders, deacons, recovery, care
- Confidential groups: "hide member details" / anonymous member lists "to everyone but the group leader and admins" (recovery, grief)
- Group types (small groups, Sunday School, recovery); open signups via QR; private groups
- Leaders: take attendance, group-wide announcements + chat, group calendar/events/materials
- Attendance reports: "follow up with anyone who stops attending"; church-wide engagement (demographics, drop-off)
- Permissions: view all groups / subset / only their groups
- Terms of Service: children under 13 may not log in to Church Center — kids tracked via Check-Ins instead

**ChMS use-case page (whole-system view):**
- Permissions philosophy: "Give people access to just the products and features they need… Your finance department might only need access to Giving… but everyone needs access to the central database in People."
- Volunteer scheduling: "schedule people for services, events, and classes months in advance according to volunteers' availability"; blockout dates
- Church Center (member-facing): "give, join a group, sign up for an event, view their volunteer schedule, chat with their group"; church-wide directory; profile self-update
- Core feature set by product: engagement dashboard (attendance, donations), custom reports (lists), activity feed; push/email/text; signups + payments; room/resource booking; fast check-in with label printing; event/group/general attendance; all-team scheduling; events, group chat/directory, online church; worship planning/sheet music/rehearsal; donations (ACH/card/Apple Pay/text/cash/check), reports by campus/fund/type, statements; permissions, check-in/check-out security labels, background checks; web/desktop/mobile + label printers (Citizen, Brother, Dymo, Zebra)

## Product B — Tithe.ly Church Management (formerly Breeze ChMS)

### Key observations (evidence layer A)

**Positioning:** "The #1 All-in-One Church Management Software… organizes people, volunteers, giving and contributions, communications, events, services, and more—all in one place." Vendor's own Type definition (FAQ): "Church management software, commonly called ChMS, helps churches manage member and family records, giving, attendance, children's check-in, volunteers, events, groups, communication, forms, follow-up workflows, and service planning in one system."

**Structures observed:**
- People database: "manage member information, track engagement, and support your congregation"
- Tags & Groups: "customizable Tags… small groups, volunteers, or event attendees, tagging makes it simple to organize and reach the right people"
- Kid's Check-In: "Print parent and child name tags, track attendance, and ensure safety with unique security codes"
- Messaging: text + email "to individuals or groups"
- Events: "built-in volunteer scheduling and children's check-in"
- Service Planning: worship services, Song Library, SongSelect® integration, Tithely Worship App
- Forms: "public-facing forms for sign-ups, registrations… Automatically associate form submissions with member profiles"
- Automation: "birthday emails, assigning members to groups, and managing follow-ups"
- Groups: "small groups to Bible studies and ministry teams… join… right from your Church App"
- Church Safety: MinistrySafe background checks + abuse prevention training integrated
- Church Calendar: events, rooms & resources, avoid double bookings
- Giving Dashboard: real-time gifts, filter by date/fund/giver type
- Migration: free data migration from other ChMS; CSV import/export
- Pricing: flat $72/mo ChMS; $119/mo All Access bundle (giving + apps + sites + ChMS + service planning)

## Product C — Pushpay ChMS (formerly Church Community Builder)

### Key observations (evidence layer A)

**Positioning:** "A ChMS that Strengthens Connections… grow with your church, whether you're a small community, a mid sized church, or a large church." Vendor's own Type definition: "a centralized platform churches use to organize member data, automate ministry operations, and bring the people, processes, and information that keep a church running into a single system." Vendor's list of what "most ChMS platforms include": member and family profiles with engagement history; check-in and attendance tracking; group and volunteer management; workflow automation for follow-up and pastoral care; email/SMS/push tools; reporting on attendance, engagement, and church health.

**Structures observed:**
- Member profiles: "complete profiles with family relationships, attendance history, group involvement, and giving data" in one place
- Process Queues (CCB heritage): "Automate next steps for connection, and follow-up. Keep your ministry flowing without missing a single person"
- People Workflows: "First Time Guest Follow up, Volunteer pipelines, and Care"
- Check-In: "digital kiosks… secure drop off and pick up experience for parents… Send text messages to parents, print tags, set room capacities, and print room rosters"; touchless pre-check from car with barcode
- Attendance: headcounts + individual attendance; "spot trends, like a family that's attended four weeks in a row or a regular member who's been absent for three. That visibility is where attendance tracking becomes useful for pastoral care, not just recordkeeping"
- Groups: events, messages, "Needs" (meal trains), attendance, RSVP
- Volunteer scheduling: positions, rotations, requests, confirmations, availability, household scheduling, burnout visibility ("who's been serving frequently (and might be heading toward burnout)")
- Forms: registrations "for up to ten people in a single form, and payments"
- Rooms and resources: facility scheduling with approval routing
- Worship planning: service plans, song library (SongSelect®), chord charts
- Reporting: system/custom/dashboard reports; saved shareable people searches; AI-powered natural-language people search
- LEAD App: mobile ChMS for staff/ministry leaders (profiles, notes, follow-up on the go)
- Member apps: MyChurch App / Custom Church App (RSVP, profile updates, giving, group messaging)
- Nurture: "Timely, trackable pastoral care from your existing church data"
- SacramentTracker (Catholic pole): "Automate every milestone of the sacramental journey"
- Heritage: "Pushpay acquired Church Community Builder… core strengths (people management, process queues, donor development tools)"
- Named competitors: Planning Center, Breeze ChMS, Shelby System, Fellowship One, Subsplash, Rock RMS
- Who uses it (vendor FAQ): senior pastors (church health), executive pastors/administrators (operations), ministry leaders (groups, serving teams, guest follow-up), volunteer coordinators (schedules), congregation (app: RSVP, profile updates, giving)

## Product D — Rock RMS

### Key observations (evidence layer A)

**Positioning:** "All-in-One Church Management Tools… Unified tools to manage your people, processes, communication & so much more." Open-source project of Spark Development Network; community documentation/Q&A/recipes; demo site.

**Four feature domains:**
- Church Management: People Management (individual and family profiles, custom attributes, configurable notes, personality assessments); Check-in (flexible options, secure check-in & check-out, smart room assignments, customizable labels); Metrics & Reporting (metrics, reports, attendance analytics, giving analytics, "BI Ready"); Prayer (prayer-request management, AI moderation, self-harm alerts); Finance Tools (giving options, financial reporting, check scanning, pledges & benevolence); Event Registration; Workflows (automate complex processes, form building, triggers)
- Communication: email, SMS conversations (two-way shared team inbox), SMS pipeline (keyword triggers), push, communication flows (drip), analytics
- Digital Platform: personalization, websites, mobile apps, TV apps, content management, shortlinks, media + analytics, interactions
- Engagement: Groups ("organize individuals by purpose (e.g., small groups, serving teams, classes)… group requirements to enforce training, background checks… public group finder"); Group Scheduling (accept/decline, conflicts); Connections ("Automate follow-up for first-time guests… Assign connection requests to staff or volunteers… Track progress from initial contact to full engagement"); Steps ("Define clear discipleship paths (e.g., baptism, membership, volunteering)… Track individual spiritual milestones"); LMS; Sign-ups

## Product E — ParishSOFT

### Key observations (evidence layer A)

**Positioning:** "Church Management Software for Dioceses & Catholic Parishes… built by Catholics for Catholics." Part of Ministry Brands. "Diocesan-compliant system."

**Parish modules:** Accounting; Facility Calendar; Faith Formation ("Streamline classes, schedules, and sacramental programs with easy tools for attendance, planning"); Families ("Manage records online with streamlining census, records, and communication"); Giving; Intelligent Query ("custom query reports"); Ministry Scheduler; Mobile App (giving, events, prayer requests); My Parish ("A secure parishioner portal and mobile directory that improves accuracy while easing the administration of parishioner records"); Offering ("track giving and pledges with superb reporting"); ParishCast (mass/group communications); Safe Environment ("trusted background screening"); Streaming; Tuition (Catholic schools); Websites.

**Diocese modules:** Census ("Complete data for families, sacraments, staff, and volunteers in your diocese, along with tools to manage roles"); Development Manager; Diocesan Accounting; Diocesan CRM; Facility Calendar; Families; Giving; Intelligent Query; Safe Environment; Websites.

**Structural note:** the suite separates Offering (contribution record-keeping) from Giving (online collection) — consistent with the church-giving-platform research finding that the record half has a long history independent of online payment.

## Cross-product Comparison

| Structure | Planning Center | Tithe.ly ChMS | Pushpay ChMS | Rock RMS | ParishSOFT |
|---|---|---|---|---|---|
| People records (individual + household/family) | A: People profiles, custom tabs/fields | A: People database, member info | A: member profiles with family relationships | A: individual and family profiles | A: Families/census records |
| Participation history on the person | A: attendance, giving, volunteering; activity feed | A: engagement tracking | A: attendance history, group involvement, giving data on profile | A: attendance/giving analytics; interactions | A: sacraments, formation attendance, offering |
| Groups/classes/teams as organizing units | A: Groups (small groups, elders, recovery…) | A: Tags & Groups | A: Groups (events, messages, needs) | A: Groups by purpose + requirements | A: Faith Formation classes; Ministry Scheduler |
| Attendance + check-in | A: Check-Ins product (stations, labels) | A: Kid's Check-In (security codes) | A: kiosks, capacities, rosters | A: secure check-in/out, labels, room assignment | A: formation attendance; (check-in via suite) |
| Child security machinery | A: security labels, pickup verification, emergency texting | A: parent/child name tags, security codes | A: parent pickup labels, room capacities, texts | A: secure check-in/out | A: Safe Environment screening |
| Contribution records linked to people | A: giving on profile; statements | A: giving syncs with People | A: giving data on profile; pledges; statements | A: giving analytics, pledges, benevolence | A: Offering module (record) separate from Giving (collect) |
| Follow-up / care workflows | A: workflows (guest follow-up, membership progress) | A: automations (follow-ups) | A: Process Queues, People Workflows (guest/volunteer/care) | A: Connections, Steps (discipleship paths) | B: (not surfaced on homepage) |
| Communication from records | A: text/email/Church Center announcements from lists | A: Messaging (text + email) | A: email/SMS/push segmented by filters | A: email/SMS/push to groups or data views | A: ParishCast |
| Volunteer/serving scheduling | A: Services scheduling + availability | A: volunteer scheduling in Events | A: rotations, availability, household scheduling | A: Group Scheduling | A: Ministry Scheduler |
| Events + registration | A: Registrations + Calendar | A: Events + calendar | A: event management + forms + payments | A: Event Registration, Sign-ups | A: Facility Calendar |
| Member-facing self-service | A: Church Center (profile, directory, giving, signups, schedules, chat) | A: Church App (groups join) | A: MyChurch/Custom App (RSVP, profile, giving) | A: Rock mobile app (check-in, giving, next steps) | A: My Parish portal + Mobile App |
| Reporting/engagement analytics | A: dashboards, lists, activity feed | A: Giving Dashboard | A: system/custom/dashboard reports; Insights | A: metrics, reports, BI-ready | A: Intelligent Query |
| Safety/background checks | A: Checkr integration | A: MinistrySafe integration | B: integrations (background checks named in FAQ) | A: group requirements enforce background checks | A: Safe Environment module |
| Notes with privacy sensitivity | A: prayer requests, counseling notes; field-level collaborators | B: (not surfaced) | A: LEAD App record notes | A: configurable notes | B: (not surfaced) |
| Multi-campus / multi-org | A: campuses across products | B: multi-site (giving research) | A: multi-site positioning | B: (campus support in platform) | A: diocese ↔ parishes hierarchy |
| Custom fields | A: full custom tab/field engine (Tier-1) | B: tags | B: custom filters/searches | A: custom attributes | A: Intelligent Query |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a ChMS:

1. **Congregation people records** — identified individual persons, organized into households/families, held as the system's central records. (Remove → scheduling tool, giving tool, or generic contact list.)
2. **Participation records over time attached to those people** — attendance, involvement, giving history recorded against the person, forming the engagement history that staff act on. (Remove → static member directory / address book.)
3. **Church-side administration** — the congregation's staff and lay leaders (not the members) operate the system of record for ministry administration; members appear in records and may self-serve, but the organization owns and governs the data. (Remove → member-owned community app or personal tool.)

Historical check (§24): a 1990s office membership database (people + attendance + contributions, single desktop PC) and a Catholic parish census/sacramental register satisfy all three without check-in kiosks, apps, texting, or workflows. Modern machinery stays out of L0.

Groups: deliberately NOT in L0. Every sampled product has groups, and historical systems tracked classes/committees, but a minimal people + attendance + contributions system without a group module would still be recognized as a (small-church) ChMS. Groups are the strongest L1 item.

### L1 — Common Mature Structure

Present across the sample (layer B) and documented per-product (layer A):

- **Groups/classes/teams** as organizing units between the person and the whole church, with leaders, types (small groups, classes, serving teams, governance bodies), attendance, and often privacy postures (confidential/anonymous membership)
- **Contribution records linked to people** (the record half of giving; collection channels belong to the Church Giving Platform Type)
- **Attendance machinery**: event attendance, group/class attendance, headcounts
- **Children's check-in with security machinery**: stations/kiosks, child + parent labels with security codes, pickup authorization/verification, room rosters, parent texting, medical/allergy notes surfaced on labels
- **Member lifecycle & follow-up workflows**: first-time guest capture (forms/connection cards) → welcome/follow-up → membership/next-step progress tracking; re-engagement of drifting people ("falling through the cracks")
- **Communication from the records**: email/SMS/push to lists/segments derived from people data
- **Volunteer/serving scheduling**: positions, rotations, availability/blockouts, requests/confirmations
- **Events + registration + facility/room & resource booking**
- **Reporting/dashboards** over attendance, giving, engagement
- **Member-facing self-service** (portal/app): profile self-update, directory, giving, event signups, schedules, group interaction
- **Forms** feeding records (connect cards, registrations)
- **Safety/background checks** for volunteers, with renewal tracking
- **Sensitive notes** (prayer requests, counseling, health) with privacy controls
- **Custom fields** to extend the person record
- **Multi-campus** support
- **Data migration/import-export** (CSV; vendor migration services)

### L2 — Variant / Optional Structure

- **Denominational/heritage poles**: Catholic parish/diocese (census, sacramental milestones, faith formation, diocesan compliance/reporting, tuition for schools) vs evangelical engagement-led (guest pathways, discipleship steps) vs mainline membership-led
- **Packaging**: modular per-product pricing (Planning Center) vs flat all-in-one (Tithe.ly) vs enterprise suite bundle (Pushpay ChurchStaq) vs open-source self-hosted (Rock RMS)
- **Deployment**: SaaS dominant; self-hosted open-source pole
- **Depth of finance**: giving records only vs fund accounting/check scanning/benevolence (Rock, ParishSOFT Accounting)
- **Worship/service planning depth**: from basic volunteer scheduling to full service plans, song libraries, chord charts, rehearsal tools
- **Digital-platform breadth**: websites, custom church apps, streaming, TV apps, content/sermon libraries (Rock widest)
- **AI assistance**: natural-language people search, giving-data Q&A, prayer moderation, self-harm alerts, list building
- **Scale posture**: church plant → single campus → multi-site → diocese (hierarchical multi-org)
- **Regional/regulatory**: diocesan compliance, child-safety regimes, privacy postures
- **Learning/discipleship depth**: LMS-style courses, steps/pathways

### L3 — Vendor-specific Structure (research notes only)

- Planning Center: People free; per-product pricing tiers by usage (check-ins/day, group members); Church Center app; Headcounts app; Checkr integration; grade promotion with "Promotes To"; "[hidden content]" masking for non-collaborators; communication history retained ~3 months; named printer brands
- Pushpay: Process Queues; LEAD App; SacramentTracker; Everygift®; ChurchStaq/ParishStaq naming; Nurture; "6 second giving"; acquired CCB; named-competitor FAQ
- Tithe.ly: All Access $119/mo flat; MinistrySafe integration; SongSelect®; Breeze rebrand; free migration claims
- Rock RMS: Lava templating; Spark Development Network; TV apps (Apple TV/Roku); personality assessments; self-harm alerts; SMS keyword pipelines; "BI Ready"
- ParishSOFT: Census module; Offering vs Giving module split; Tuition; My Parish portal; Ministry Brands ownership; "patent pending" footer

## Vendor-specific Findings

See L3. Additionally: only Planning Center documents field-level permission masking and label-content restriction at Tier-1 depth; only Pushpay documents the attendance-as-pastoral-signal framing explicitly ("absent for three"); only Rock documents prayer-request moderation and self-harm alerts; only ParishSOFT documents the diocesan hierarchy and sacramental registers. None of these are promoted to the canonical model.

## Boundary Findings

1. **vs Church Giving Platform (§25 sibling, processed).** ChMS owns the people record and the contribution *record*; the giving platform owns collection channels, money movement, and donor-facing giving UX. Seam test from the sibling: center of gravity = parish life → ChMS even with a contributions module. ParishSOFT's Offering/Giving split and Planning Center's People/Giving product split both confirm the seam. Remove collection channels → ChMS contribution module; remove people records → giving platform.
2. **vs Church Communication Platform (§25 sibling, processed).** ChMS is the record system; comms is the sending loop over those records. Spectrum documented by the sibling: standalone comms tools with ChMS integrations / ChMS-embedded messaging modules (Tithe.ly) / ChMS with no comms product delegating to integrations (Planning Center). Remove the sending loop → ChMS; remove the people-record substrate → generic email/SMS marketing.
3. **vs Nonprofit CRM / Donor Management System.** Structurally similar (people records, giving, groups, workflows). ChMS-specific objects: households as first-class units, attendance/check-in, child security, worship-life milestones (baptism, membership classes, sacraments), volunteer serving teams, member portal. AMS research already judged ChMS "adjacent, not the same Type." The seam is the domain object model, not the record grammar.
4. **vs Membership Management System / Congregation Membership Management (§25 leaves).** Membership management is a *slice* of the ChMS record core (people + membership status + directory). ChMS adds participation machinery (attendance, check-in, giving records, groups, workflows) and the operational modules. Flag: "Congregation Membership Management" is a probable partial-overlap sibling; joint review recommended.
5. **vs Ministry Scheduling / Worship Planning / Religious Small-group Management / Pastoral Care Management / Religious Volunteer Management (§25 leaves).** These are capability slices that exist both as ChMS modules and as standalone specialists (the same spectrum the comms sibling documented). ChMS is the system of record that unifies them; the specialists own their loop's depth.
6. **vs Childcare Management System (§25 sibling, processed).** Both have check-in with custody/security machinery. Childcare is a *business* (enrollment, tuition billing, ratios, licensing); ChMS check-in is *ministry safety* inside a record system, with no tuition/billing core. Remove the business/billing core from childcare → its check-in resembles ChMS check-in.
7. **vs CRM (§07).** Same record grammar (people + activities + pipeline-like follow-up), different domain: ChMS objects are congregation-life objects; the "pipeline" is a discipleship/guest pathway, not a commercial deal. ChMS is best understood as a domain-specialized record system, not a CRM configuration.
8. **"Remove what to become another Type" tests:** remove people records → giving platform / scheduling tool / comms tool; remove participation history → member directory; remove church-side administration (members own the data) → community/member app; remove the congregation domain (generic members, no ministry objects) → Nonprofit CRM / Membership Management System.

## Uncertainties

- Rock RMS book/documentation (rockrms.com/Rock/Book) returned 404 this pass; Rock observations rest on the features page (Tier 2). Depth of Rock's people/permission model not verified at Tier 1.
- Tithe.ly, Pushpay, ParishSOFT evidence is product-page tier (Tier 2); no Tier-1 help-center articles fetched for them this pass. Precise operational details (exact permission ladders, exact status vocabularies, numeric limits) intentionally not asserted.
- Member lifecycle status vocabularies (guest/visitor/regular/member/inactive) are conceptually present (workflows "track progress toward… becoming a member"; profile updates to "membership status") but exact status sets vary by product and were not exhaustively documented — kept conceptual in the final document.
- ParishSOFT Faith Formation / Safe Environment depth not verified beyond module descriptions.
- Denominational breadth beyond Catholic/evangelical poles (mainline Protestant, Orthodox) not sampled; treated as variant space, not asserted.

## Final Synthesis

A Church Management System is the congregation's central record system: identified people (organized into households) held as records, with their participation over time — attendance, group involvement, giving history, serving — attached to those records, all administered by the church's staff and lay leaders under permissioned access, with members as the subjects (and partial self-servers) of the records rather than the operators. Around that record core, mature products add the operational machinery of congregational life: groups with leaders, attendance and children's check-in with security machinery, guest-to-member follow-up workflows, communication drawn from the records, volunteer scheduling, events and facilities, reporting, and a member-facing portal/app. The Type's center of gravity is the record core — which is why giving platforms, communication platforms, scheduling specialists, and worship planners all exist beside it, integrate with it, or ship as its modules, and why a ChMS can lack any one of those modules while remaining a ChMS. The definition survives the historical check: a parish census register or a 1990s office membership database satisfies the core without any modern machinery.
