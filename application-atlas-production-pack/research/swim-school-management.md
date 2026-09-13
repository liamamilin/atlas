# Research Notes — Swim School Management

Research date: **2026-09-09**

## Research Goal

Understand what software sits under the directory leaf "Swim School Management" (§28 Sports, Fitness & Recreation): what objects the system manages, what the swim school's operating loop is, how the class-management family spine is realized for swim, and where the boundary lies against the already-processed sibling leaves (Dance Studio Management, Martial Arts School Management, Sports Academy Management, Recreation Center Management, Fitness Studio Management, Climbing Gym Management, Sports Club Management) and the unprocessed sibling (Gymnastics Club Management).

Context entering this pass — explicit forward flags to discharge:

- The martial-arts-school-management pass (2026-09-08) predicted swim-school-management and gymnastics-club-management as "the closest siblings of all (children's class management; swim = level cycles/makeup emphasis, gymnastics = skill tracking/meets)" and required: spine-first discipline + time-structure seam check per vertical.
- The dance-studio-management pass (2026-09-07) recorded the **vertical-family taxonomy flag**: one product family (class management for children's-activity businesses) realized per vertical, with the same spine (family account + students, scheduled recurring classes, enrollment, tuition money loop, attendance, portals) and vertical signature extensions (dance: costumes/recitals/competition; martial arts: ranks/testing/promotions).
- The recreation-center-management pass (2026-09-09) documented the facility-operations core where swim lessons are one program among many; Dash and Amilia-class products appear on both sides of that seam.

## Initial Boundary (hypothesis before research)

- Expected core users: swim school owner/manager, deck supervisor/coordinator, swim instructors, front desk; parents (guardians) as portal users; children as the taught population.
- Expected core: the class-management family spine — swimmer records on family accounts, scheduled recurring lesson offerings, enrollment, lesson fees.
- Expected swim signature: level-based progression (learn-to-swim curricula organized in levels), evaluations/assessments, progress reports/certificates, and makeup-lesson machinery (children miss lessons; makeup scheduling is a known pain point).
- Expected neighbors: Martial Arts / Dance / Gymnastics siblings (same family), Recreation Center Management (facility-first operations), Sports Club Management (member org with teams), swim-team management products (team/meet orientation — adjacent market), Sports Registration Platform (one-shot transactions), Childcare Management, School Management / SIS.
- Open questions: is enrollment session-based (dance pattern) or continuous monthly (martial-arts pattern)? Is the level/progression layer definitional or a standard extension? How strong is the makeup machinery? How much facility/membership machinery rides on the same system?

## Research Questions

1. What is the population of record — swimmers? family accounts? members? How are minors handled?
2. How are lesson offerings modeled — levels, classes, sessions, private lessons, squads? What is the time structure (sessions vs continuous monthly)?
3. How does enrollment work — self-service, approval modes, capacity, waitlists?
4. What is the money model — lesson fees/tuition, memberships, private lessons, punch passes, squads? How does billing couple to enrollment?
5. How are skill levels, evaluations, certificates, and progress reports modeled? Is "level" a first-class structure?
6. How does the makeup-lesson machinery work — eligibility, tokens, parent self-scheduling?
7. What attendance/check-in machinery exists, and what is it used for?
8. What surfaces exist (admin, staff poolside, parent portal/app, kiosk)?
9. How much facility machinery (pools/lanes/resources) and membership machinery rides on the same system — core or pole-dependent?
10. Where does this Type end and the sibling verticals / Recreation Center Management / swim-team software begin?
11. Would an older/paper-era swim school still fit the model?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers. Three reachable poles plus family evidence from prior passes:

| Product | Pole | Why sampled |
|---|---|---|
| **iClassPro** | class-management family (gymnastics, cheer, dance, swim) — children's-activity class pole | Dedicated swim vertical page + deepest skill-tracking documentation of the reachable sample; direct test of the family flag; serves swim schools globally (US/CAN/AU/UK offices) |
| **Dash (DaySmart)** | aquatic facility / swim club management — facility-first pole | Dedicated Aquatics solution page; shows the same market served from the facility/membership side |
| **Amilia** | municipal/community recreation platform (YMCA, JCC, parks & rec) with a dedicated Swim School industry page | The community-aquatics pole: swim lessons as one program line of a multi-program operation |

Family/context evidence carried from prior passes (layer B here): iClassPro's class-management operational page (documented A-strength in the sports-academy pass: monthly/session/rolling-session class models, auto-approve/request-only enrollment, priority registration, waitlists, trials, drop-ins, punch passes, blackout closures with prorated billing, makeup tokens); Jackrabbit's family packaging (Jackrabbit Class/Dance/Swim/Cheer/Music editions — observed A-strength on jackrabbittech.com this pass); recreation-center-management pass (Dash already sampled there as a private-facility product).

Rejected / unreachable (recorded as sourcing limitations):

- **Jackrabbit Swim** — jackrabbitswim.com and www.jackrabbitclass.com (root and /swim/) returned HTTP 403 on three attempts; the corporate site confirms the edition exists ("Jackrabbit Swim — Swim School Management Software") but its swim-specific capability depth could not be directly verified.
- **CoursePro** (UK/ANZ leisure-trust swim-course pole) — coursepro.io timed out twice; abandoned per network rules.

## Sources

All fetched 2026-09-09. Official product pages (Tier 2); no help-center article bodies retrieved this pass.

- iClassPro — swim vertical page: https://www.iclasspro.com/swim-software-features
- iClassPro — skill tracking feature page: https://www.iclasspro.com/skill-tracking
- iClassPro — home (nav, positioning, feature tiles): https://www.iclasspro.com/
- Dash — home: https://dashplatform.com/
- Dash — aquatics solution page: https://dashplatform.com/solutions/swim-club-management-software/
- Amilia — home: https://www.amilia.com/
- Amilia — swim school industry page: https://www.amilia.com/industry/swim-school-software
- Jackrabbit Technologies — corporate home (product map confirming Jackrabbit Swim edition): https://jackrabbittech.com/

Prior-pass sources reused as layer B: research/sports-academy-management.md (iClassPro class-management page observations), research/dance-studio-management.md, research/martial-arts-school-management.md, research/recreation-center-management.md (STATUS entry), research/sports-club-management.md (STATUS entry).

Evidence layers: **A** = directly observed on an official page of this product this pass; **B** = cross-product commonality (including prior-pass observations); **C** = canonical inference.

## Product Observations

### iClassPro (all observations layer A unless noted)

- Positioning: "The #1 Class Management Software for Gymnastics, Cheer, Dance and Swim Schools"; swim page headline "The #1 Swim Class Management Software for Swim Schools across the globe." Scope named for swim: "group lessons, development squads, private lessons, birthday parties, events, student and staff schedules, waivers, email, SMS."
- Swim industry anchored: partner logos of the United States Swim School Association, Australian Swim Schools Association, Swim Coaches and Teachers Australia, AUSTSWIM-context body (swim.org.au), Swim Coaches and Teachers New Zealand, Canadian Swim School Alliance, International Swim Schools Association, Aquatic Professionals association (AoAP), and IACDP. Testimonials from swim-school operators (Ukiyo Swim School, Splash Swim School) and a "Learn to Swim Manager". Offices US/CAN/AU/UK.
- Office Portal: "Manage lessons, enrollment, billing, and customer accounts from one centralized location"; customizable dashboards, live calendar, reporting; Welcome Page metrics (new accounts, dropped enrollments, class transfers, new enrollments).
- Staff Portal: swim instructors "view planned student absences, record attendance, and track skill evaluations" on mobile; time clock with geolocation.
- Customer Portal + Branded App: families book classes and private lessons, manage accounts, pay, "track student skills"; ProShop; news. Branded App is plan-gated (one-time setup fee + monthly).
- **Makeup Lessons** (first-class module on the swim page): "Manage missed classes by offering makeup tokens. Choose to automate or manually track and allocate makeup classes… Parents can schedule makeup classes at their convenience, reducing administrative costs and helping to improve athlete retention." (Makeup tokens also documented on the class-management page — layer B from the sports-academy pass: "online makeup tokens that can be redeemed for another class or session approved for makeup enrollments.")
- **Skill Tracking**: custom Skill Trees ("creating custom trees that match your needs"), real-time evaluation from the staff portal phone/tablet ("no more printing paper evaluation sheets"), evaluate an entire class on one screen, custom certificates with layout/branding and automatic delivery, customizable progress reports visible to parents in the portal, branded evaluation-notification emails. (Skill Bank/Skill Trees with videos/images and skill evaluations updating to the customer's app/portal, tracked from the attendance screen — layer B from the sports-academy pass.)
- Private lessons: Appointments feature manages "private lessons, semi-private sessions, student evaluations"; plan-gated (Elite and higher).
- Punch Passes: families purchase a set number of passes for classes/lessons; individual or family passes; flexible attendance.
- Other modules: check-in kiosk (students bypass the front desk), camps/events, party booking (iPartyPro), Point of Sale/ProShop, payment processing, Autopilot Billing, Autopilot communication workflows, QuickBooks integration, Pro Insights dashboards, integrated websites.
- Enrollment control (class-management page — layer B via sports-academy pass): class models "monthly, session, or rolling session classes. Bill hourly, flat rate, or by time slot"; request-only vs auto-approve enrollment; priority registration; prorated billing; trials; waitlists; drop-ins; blackout schedules with prorated billing.
- Pricing: four plans (Signature/Elite/Premium/Enterprise) — plan architecture observed; per-feature gating noted (Appointments, Branded App).

### Dash (all observations layer A)

- Positioning: DaySmart recreation-facility platform ("Recreation Facility Management Software"); dedicated Aquatics page: "Make a Splash With Swim Club Management Software — Manage Your Programs, Lanes, Members, and More."
- Aquatic-center scope: memberships; scheduling and resource management (lanes/resources booked and reserved in one calendar; mass scheduling/editing for programs, lessons, events); registration for "lessons, leagues, and other programs" ("community members"); guest admission tickets for one-off events; attendance via digital check-in stations ("keep up with liability procedures and track program success"); registration forms collecting emergency contacts and waivers; payments built in (reservations, registration, concessions, tickets, memberships); recurring payment plans for community memberships and invoicing; in-app email marketing with activity-based targeting; reporting ("over 60 standard reports" for finances and facility usage).
- No swim-lesson-pedagogy machinery visible on the aquatics page: no level/skill trees, no evaluations, no makeup tokens. The aquatics realization is registration + resources + memberships + attendance + money — the facility pole.
- Customers: multi-sport complexes, ice facilities, parks & rec (consistent with the recreation-center pass's Dash sampling).

### Amilia (all observations layer A)

- Positioning: recreation & membership platform for YMCA/JCC/parks & rec/community centers; dedicated Swim School industry page: "centralizes all swimmer information, streamlines lesson scheduling, and simplifies class management tasks."
- Swim-school capability claims: parent self-service registration ("parents sign their children up for classes and lessons with a few simple clicks"); "Fill your swim classes with sessions, drop-ins or both"; flexible lesson scheduling (book facilities, coaches, activities; modify dates/times/facilities/staff); centralized swimmer data used "for attendance lists, skill tracking and client reporting"; staff management with certification tagging ("tag them according to their experience and certifications so you can assign the right coach to the right class"); staff app (schedules, availabilities, attendance); private lessons via the activity module ("group classes, private lessons, drop-in and camps"); memberships (individual and household); payments (recurring installments, payment recovery); forms/waivers at checkout; access control/self check-in.
- Aquatic customers: municipal aquatic complexes (Desjardins Aquatic Complex of Mascouche; Mouvement Aquatique Laval — waitlist pain quote; Triangle Aquatic Center — private lessons as a new revenue stream). Bilingual EN/FR (Montreal-based).
- Platform-level stats (vendor-claimed, kept in notes only): 8,200 locations, 80% self-serve transactions, $1B+ annual transactions.

### Jackrabbit Technologies (product map only — layer A, packaging)

- Corporate product map lists five vertical editions: Jackrabbit Class (gymnastics), Jackrabbit Dance, **Jackrabbit Swim ("Swim School Management Software")**, Jackrabbit Cheer, Jackrabbit Music; plus other youth-activity verticals. Direct packaging evidence of the class-management family selling swim as a vertical edition. Capability depth not verifiable (403).

## Cross-product Comparison

| Structure / capability | iClassPro (swim page) | Dash (aquatics) | Amilia (swim school) | Layer |
|---|---|---|---|---|
| Swimmer/student records centralized (children; family context) | ✓ customers/student profiles; parent portal | ✓ community members | ✓ "centralizes all swimmer information" | B |
| Family/guardian as paying unit (parents book and pay) | ✓ parent/customer portal books & pays | ✓ community members register | ✓ "parents sign their children up" | B |
| Scheduled recurring lesson offerings (levels/classes) | ✓ group lessons; development squads; private lessons | ✓ programs, lessons on facility calendar | ✓ group classes + private lessons + drop-ins + camps | B |
| Lesson organized around progressive skill levels | ✓ Skill Trees + evaluations + certificates + progress reports (pedagogy layer explicit) | not visible on aquatics page | ✓ "skill tracking" named as data use; level framing not explicit on page | A×2, weaker at facility pole |
| Enrollment with capacity/waitlists | ✓ waitlists, request/auto-approve modes (class page, layer B) | ✓ registration for programs | ✓ waitlist pain quoted by aquatic customer; sessions + drop-ins | B |
| Money loop: lesson fees/tuition billed against enrollment | ✓ billing from Office Portal; Autopilot Billing | ✓ payments built in; recurring payment plans | ✓ recurring installments, payment recovery | B (strong) |
| Memberships alongside lessons | punch passes (prepaid attendance), not membership-led | ✓ memberships + recurring payment plans (facility-led) | ✓ individual/household memberships (community-led) | B (pole-dependent) |
| Attendance / check-in machinery | ✓ staff portal attendance; kiosk | ✓ digital check-in stations | ✓ attendance lists; staff app attendance; access control | B (strong) |
| Makeup-lesson machinery | ✓ first-class module: makeup tokens, auto or manual allocation, parent self-scheduling | not visible | not visible on swim page | A (single product, but headline placement) |
| Skill evaluation outputs: certificates / progress reports / parent notifications | ✓ certificates, progress reports, branded emails | not visible | reporting mentioned | A (single) |
| Private lessons | ✓ Appointments module (plan-gated) | — (rentals/facilities instead) | ✓ activity module | B |
| Squad/competitive bridge ("development squads") | ✓ named swim scope | — (swim club/leagues framing) | — (swim team imagery, no squad machinery shown) | A (single) |
| Waivers/emergency info at registration | ✓ waivers | ✓ emergency contacts + waivers | ✓ forms/waivers at checkout | B |
| Communication (email/SMS/push, reminders) | ✓ Autopilot workflows | ✓ in-app email marketing | ✓ notifications (platform capability) | B |
| Facility/resource scheduling (pools/lanes/spaces) | ✓ live calendar (rooms/resources generic) | ✓ lanes/resources first-class ("Programs, Lanes, Members") | ✓ facilities + coaches booked per lesson | B (facility pole strongest) |
| Staff certification tagging for assignment | — | — | ✓ certifications tag → right coach to right class | A (single) |
| Instructor time clock / payroll | ✓ geolocated clock-in | — | staff schedules/availabilities | B (partial) |
| Instructor/instructor-portal evaluation entry poolside | ✓ real-time on phone/tablet | — | staff app attendance | A (single) |
| Events/parties/camps | ✓ parties, events, camps | ✓ guest tickets, events | ✓ camps | B |
| Session container (fixed terms) | ✓ available ("monthly, session, or rolling session") | ✓ seasons framing | ✓ sessions available | B — dual-mode |
| Continuous monthly/rolling enrollment | ✓ "monthly" / "rolling session" first-class | ✓ memberships/recurring plans | ✓ recurring installments; drop-ins | B — dual-mode |
| Reporting (enrollment, retention, revenue) | ✓ Pro Insights; Welcome Page metrics | ✓ 60+ standard reports | ✓ reporting & analytics | B |
| POS/retail | ✓ ProShop | ✓ POS/concessions | — (not on swim page) | B |

Three structural notes from the comparison:

1. **The swim signature layer is pedagogy + makeup machinery.** iClassPro is the only reachable product that documents the full swim-lesson pedagogy layer (skill trees → evaluations → certificates → parent-visible progress reports) and the only one with an explicit makeup module — and its swim page headlines both. Amilia names skill tracking as a data use. Dash's aquatics page shows none of it — the facility pole serves the pool (resources, memberships, admissions) without the lesson-pedagogy layer. This matches the martial-arts pattern: the signature layer is standard for the vertical, not present in every product that touches the market.
2. **Time structure is dual-mode in swim.** iClassPro documents "monthly, session, or rolling session" class models as equal choices; Amilia sells sessions + drop-ins with recurring installments; Dash frames seasons/memberships. Swim does not force either the dance pole (season/session container) or the martial-arts pole (continuous membership only): both are first-class in the same products. This discharges the martial-arts pass's time-structure seam check for swim: the seam exists inside swim, not between swim and the family.
3. **Membership machinery is pole-dependent.** Facility-first operators (Dash aquatics, Amilia/YMCA-JCC) run household memberships and admissions on the same system as lessons; class-first operators (iClassPro) lead with enrollment + tuition and reach membership-like entitlements via punch passes instead. Neither posture belongs to the definition of the swim-school Type; both are how the family spine meets the aquatic market's operator shapes.

## Canonical Model

### Level 0 — Defining Invariant (minimal)

```text
Swimmer record (identified learner, commonly a minor,
        held on a family/guardian account)
└── Scheduled lesson offerings (the school's offer:
    recurring group lessons — organized by level —
    plus private lessons; placed on the calendar)
    └── Enrollment (persisted swimmer↔lesson registration
        under capacity/waitlist, forming the roster)
        └── Lesson money loop (enrollment-driven fees posted
            to the family account, settled by payment,
            arrears actionable)
```

Four jointly-held structures. Removal test:

- Remove the swimmer record → a contact/CRM database; nobody is being taught.
- Remove scheduled lesson offerings → a billing engine or a people database, not a school.
- Remove enrollment → a class directory or a sign-up form; no roster, no "who swims when".
- Remove the money loop → a roster app; the school stops being run as a business in the system.

Deliberately NOT in L0 (each fails the "would it still be the same Type" or the historical test):

- **Level/skill progression machinery** (skill trees, evaluations, certificates, progress reports) — the swim pedagogy signature, documented at depth for one product and named by a second; but the facility pole operates lessons without it, a paper-era swim school ran levels with paper progress cards, and the family precedent (martial-arts ranks) holds signature layers as standard extensions. Standard, not definitional.
- **Makeup-lesson machinery** — first-class in swim (headline module for the class-pole product; a known family capability per the dance pass), but a paper-era school handled makeups by conversation, and its absence does not break the enrollment→money→lesson loop. Standard emphasis, not definitional.
- **Attendance/check-in, portals, communication, waivers, POS, private-lesson booking, squads, events/camps/parties** — common mature structure across the family sample.
- **Memberships / household memberships / admissions** — pole-dependent (facility-first operators), not definitional.
- **Facility/resource scheduling of pools and lanes** — load-bearing for aquatic-facility operators, optional for schools renting pool time; the swim-school record here is the lesson business, not the building.
- **Session container OR continuous billing as the time structure** — both are offered by the same products; neither is the invariant. The invariant is only that lesson offerings recur on a calendar and money follows enrollment.

Historical / market-sample check: a paper-era municipal swim-lesson program (registration card per child under the guardian's family file, a posted schedule of level classes, enrollment list per class, lesson-fee collection, attendance roll, paper progress card/certificate) satisfies every L0 element with zero software machinery. A regional swim school and a pool-rental lesson business fit equally. An aquatic facility running swim lessons as one program among many fits at the facility pole (lessons + memberships + resources on one system). L0 holds across eras and operator shapes.

### Level 1 — Common Mature Structure

- Enrollment machinery: online self-service registration by parents, capacity limits, waitlists, enrollment approval modes (request-approve vs auto-approve), trials, priority registration, prorated billing (family-class evidence, layer B).
- Level/skill progression layer (the swim pedagogy signature): lessons organized in progressive levels; per-swimmer skill records against the school's skill/curriculum trees; instructor evaluations recorded poolside from the staff portal; completion outputs — certificates, progress reports — pushed to the parent portal with branded notifications; evaluation data used for placement in the next level.
- Makeup-lesson machinery: absence-recorded lessons generate eligibility (tokens/credits in the class-pole product) that parents redeem by booking into makeup-approved classes; automatic or manual allocation.
- Attendance/check-in: instructor attendance from the staff portal; kiosk self check-in; attendance data feeding skills, billing, and reporting.
- Money machinery: recurring billing/autopay on the family account, payment recovery, one-time charges, refunds; payment processing bundled or partnered.
- Parent/customer portal + mobile app: book lessons and makeups, pay, view progress/skills, receive notifications.
- Staff machinery: instructor schedules and certification-tagged assignment, staff portal (rosters, attendance, evaluations), time clock.
- Communication: email/SMS/push announcements and reminders, automated workflows (enrollment confirmations, absence/makeup, cancellations).
- Private lessons: appointment-style booking against instructor availability, plan-gated in one product.
- Events beyond lessons: camps, parties, events with registration and payment.
- Waivers/emergency-contact collection at registration.
- Reporting: enrollment, retention, revenue, class-occupancy dashboards.
- Facility scheduling where the operator runs the pool: pool/lane/space resource calendars with conflict control (facility pole).

### Level 2 — Variant / Optional Structure

- Operator shape: independent swim school vs municipal/community aquatic center vs YMCA/JCC vs leisure-trust; the same family spine serves all, with facility/membership machinery swelling at the facility poles.
- Facility posture: dedicated learn-to-swim facility vs multi-use aquatic center (lessons + memberships + lane rentals + clubs) vs school renting pool time.
- Time structure: session-based enrollment (fixed terms, per-session rates) vs continuous monthly enrollment with autopay vs rolling sessions — dual-mode across and within products.
- Revenue mix: group-lesson tuition core vs private-lesson-led (documented as a growth revenue stream at an aquatic center) vs mixed; punch passes/prepaid attendance entitlements; drop-ins; camps/parties.
- Competitive bridge: development squads pre-team programs riding the same class machinery (named by the class-pole product); full swim-team/club operations (meets, entries, times) sit outside this Type.
- Curriculum source: school-defined level schemes vs national/federation curricula (industry-context observation; product-level support not directly verified — weak evidence, not asserted).
- Region: US/Canada dominant in the sample, with Australian/UK presence (product offices, industry-association partnerships); bilingual operation (EN/FR) at the municipal pole.
- Scale: single location → multi-location; branded app / integrated website add-ons; plan/edition gating.

### Level 3 — Vendor-specific (research notes only)

- iClassPro: makeup-token mechanics; Skill Trees; Autopilot Billing/Workflows; Pro Insights; QuickBooks-on-Autopilot; iPartyPro party booking; ProShop; geolocated time clock; Branded App pricing (one-time setup fee + monthly, Premium/Enterprise); four named plans (Signature/Elite/Premium/Enterprise); "Education Corner"; swim-industry association partner roster; Inc. 5000 / "100 Million Class & Camp Registrations" claims.
- Dash: DaySmart ownership ("Dash by DaySmart"); admin app on app stores; 60+ standard reports; integrations (SportNinja, Learn to Skate USA, facility-access partner); competitor comparison pages.
- Amilia: SmartRec platform naming; Amilia AI; social-equity capability; open API/integrations; 99.99% uptime claim; usage stats (8,200 locations, $1B+ annual transactions, 80% self-serve, 44% off-hours revenue, 68% mobile transactions); EN/FR bilingual product; "Amilia University" learning platform; migration/punch-card conversion FAQ.
- Jackrabbit: five vertical editions (Class/Dance/Swim/Cheer/Music); 99.9% uptime guarantee; B-Corp; (capability depth unreachable — 403).

## Rejected Findings

- **"Swim school management = recreation software with swim branding"** — rejected as a definition. The market does include facility-side products, but the lesson-business core (swimmers, levels, rosters, fees) is what the swim vertical pages lead with; the facility pole is an operator shape, not the Type.
- **"Level/skill progression is definitional"** — rejected: absent from the facility pole's public capability surface, absent from the historical baseline; same treatment as martial-arts ranks (signature standard extension).
- **"Makeup machinery is definitional"** — rejected: first-class and heavily emphasized in swim (more than any sampled sibling), but the core loop survives without it; held as the swim signature's second half plus a family capability.
- **"Session/term container is definitional"** (dance pattern) — rejected for swim: the same products offer monthly/session/rolling-session models as choices.
- **"Continuous membership is the time structure"** (martial-arts pattern) — equally rejected: sessions are first-class in swim.
- **"Family account is definitional"** — rejected per family precedent: the invariant is the swimmer record; family/guardian grouping is the dominant implementation for a minor-dominated market.
- **"Memberships are part of the swim-school Type"** — rejected: membership machinery is how facility-first operators monetize the pool, not what makes the system a swim-school system.
- **"Precise parameters (token expiry, billing cycles, level counts, class ratios)"** — rejected to notes: no help-center evidence retrieved; nothing asserted.

## Boundary Findings

- **vs Martial Arts / Dance Studio / Gymnastics Club / Sports Academy Management (processed siblings, same family)**: identical spine (student records on family accounts, scheduled recurring offerings, enrollment, tuition loop, attendance, portals). Signatures: dance = season/session + performance machinery (costumes/recitals/competition); martial arts = rank/testing/promotion layer + continuous memberships + strong lead funnels; sports academy = program portfolio (lessons/camps/teams) over an athlete population; swim = **level/skill progression with evaluations/certificates + first-class makeup machinery, time structure dual-mode (monthly AND session)**. Removal test: strip swim's level/makeup emphasis and add recital machinery → dance; add ranks/testing and continuous-only → martial arts. Keep-both posture ratified; the swim pass discharges the martial-arts pass's forward flag from this side and records that the family's time structure is not uniform (dance = season-forced, martial arts = continuous-forced, swim = dual-mode in one product).
- **vs Recreation Center Management (processed sibling)**: recreation centers hold the facility-operations core (building/spaces, membership entitlements validated at entry, programmed schedule of many activity types) with swim lessons as one program line; the swim-school Type centers the lesson business itself (swimmer records, levels, rosters, fees). The same products (Dash, Amilia) serve both sides — the seam is the center of gravity, exactly as the recreation pass's "aquatics/ice/… mix not definitional" note predicted.
- **vs Sports Club Management (processed sibling)**: club = member organization with teams, seasons, volunteers; swim school = lesson business with levels and rosters. Development squads bridge toward the club world but run on class machinery in the sampled lesson products.
- **vs swim-team management products (TeamUnify/SwimTopia-class market, no dedicated directory leaf)**: team/meet/entry-time orientation (rosters of competitive swimmers, meet entries, times) vs school/class/level orientation (learners, lessons, fees). Adjacent market, different core objects.
- **vs Sports Registration Platform**: one-shot registration transactions vs the ongoing lesson relationship (roster, recurring fees, progression, portal).
- **vs School Management System / SIS**: commercial lesson business vs educational institution records (family precedent).
- **vs Childcare Management System**: care context (rooms, ratios, custody check-in/out) vs scheduled lessons.
- **vs Membership Management System / Membership Billing**: generic dues/lifecycle engine; the swim Type instantiates dues against a level-organized lesson schedule.
- **vs Fitness Studio Management**: adult member + drop-in/class-pack economy vs minor swimmers on family accounts + level progression.
- **Family taxonomy note (reconfirmed)**: the swim pass adds a third independent confirmation of the vertical-family structure (iClassPro sells the same platform to gymnastics/cheer/dance/swim; Jackrabbit sells a dedicated Swim edition beside Dance/Cheer/Music; Amilia lists Swim School beside Martial Arts/Dance/Gymnastics industries). Whether the directory wants per-vertical leaves is a taxonomy question for joint review; this pass keeps the leaf as the swim realization, spine-first.

## Uncertainties

- **Jackrabbit Swim depth unverified**: the edition's existence is A-evidence (corporate product map); its swim-specific capability set could not be fetched (403 ×3). The pass does not attribute any capability to Jackrabbit Swim.
- **UK/ANZ specialist pole (CoursePro-class) uncovered**: two timeouts; the leisure-trust swim-course model (term courses against national curricula, direct debit) is documented only indirectly (iClassPro AU/UK offices; association partners). No claims made about that pole.
- **Level as a first-class data object**: skill trees/evaluations/certificates are A-evidence; "levels" as a named hierarchy of class organization is strongly implied by the swim context and the products' placement/progression framing but was not verified as a distinct object in any product. The final document phrases this as "lessons organized into progressive levels" without asserting an implementation shape.
- **Makeup machinery evidence is single-product** (iClassPro, A-strength, headline placement); Amilia/Dash swim pages do not show it. It is held as "first-class in swim" from one product plus family precedent (dance pass documented family-scheduled makeups), not as universal.
- **Payment-state gating at check-in** (documented for martial arts) was not observed for swim products this pass; not claimed.
- No vendor help-center article bodies retrieved; no precise operational parameters asserted anywhere.
- Water-safety/incident machinery (lifeguarding, in-pool safety records) was not observed in any sampled surface; not claimed as part of the Type.

## Final Synthesis

A Swim School Management application is the operator-side business system for running a swim school (a learn-to-swim lesson business). Its defining core is four jointly-held structures: **swimmer records** (identified learners, commonly minors, held on family/guardian accounts), **scheduled lesson offerings** (recurring group lessons — organized into progressive levels — plus private lessons, placed on the calendar), **enrollment** (persisted swimmer↔lesson registrations under capacity/waitlist, forming rosters), and the **lesson money loop** (enrollment-driven fees posted to the family account and settled by payment). Around that core, mature products add the swim signature layer — **level/skill progression** (skill trees, instructor evaluations recorded poolside, certificates and parent-visible progress reports, level-up placement) and **makeup-lesson machinery** (absence-generated eligibility that parents redeem by self-scheduling into makeup classes) — plus the family-wide operating machinery: attendance/check-in, parent and staff portals, recurring billing with recovery, private lessons, communication automation, waivers, events/camps/parties, and reporting. The Type's market straddles operator shapes: class-first swim schools run exactly this core; municipal/community aquatic centers and YMCA/JCCs run it alongside household memberships, admissions, and pool/lane resource management on the same platform; and the time structure is dual-mode (continuous monthly enrollment and fixed sessions are both first-class in the same products), distinguishing swim from both the session-forced dance pole and the continuous-forced martial-arts pole of the class-management family.

Taxonomy disposition: keep the leaf as the swim realization of the class-management family; keep-both-with-seam ratified against all processed siblings; martial-arts pass forward flag discharged from this side; family-level joint review remains open for Gymnastics Club Management (predicted closest remaining sibling) and Gym Management System.
