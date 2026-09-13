# Research Notes — Martial Arts School Management

Research date: **2026-09-08**

## Research Goal

Understand what software sits under the directory leaf "Martial Arts School Management" (§28 Sports, Fitness & Recreation): what objects the system manages, what the school's operating loop is, how money and entitlements couple to classes, attendance, and rank progression, and where the boundary lies against the already-processed sibling leaves (Dance Studio Management, Fitness Studio Management, Fitness Membership Management, Climbing Gym Management) and unprocessed siblings (Swim School Management, Gymnastics Club Management, Gym Management System).

Context entering this pass: the dance-studio-management pass (2026-09-07) recorded a **vertical-family taxonomy flag** — market evidence shows one product family (class/membership management for children's-activity and studio businesses) realized per vertical, with the same spine sold unchanged under different vertical editions, and verticals differing mainly in signature extensions. The fitness-studio pass (2026-09-08) and climbing-gym pass (2026-09-06) recorded compatible flags. This pass's job: document the martial-arts realization with direct evidence, hold the defining core at the shared spine, and discharge the joint-review recommendation from this side.

## Initial Boundary (hypothesis before research)

- Expected core users: school/dojo/academy owner (often also head instructor), front-desk staff, instructors; students and parents as portal users.
- Expected neighbors: Dance Studio Management (sibling vertical), Fitness Studio Management / Gym Management System (membership-driven), Sports Registration Platform (one-shot transactions), Youth Sports Management (team/league), generic CRM (prospect machinery), LMS (curriculum content).
- Open questions: is the customer record a family account (dance pattern) or an individual member (fitness pattern)? Is there a season/session container (dance pattern) or continuous membership (fitness pattern)? Is rank tracking definitional for the Type or a standard extension? How prominent is the lead/trial machinery?

## Research Questions

1. What is the central record — student, member, family account? How do they relate?
2. How are programs, classes, and schedules modeled? Is there a season/session container?
3. What is the money model — memberships, dues, contracts, testing fees, retail? How does billing relate to enrollment/membership?
4. How is attendance captured, and what is it used for (progression? entitlement? retention)?
5. How are ranks/belts/promotions modeled? What triggers promotion eligibility? Are test fees part of the money loop?
6. How prominent is the lead → trial → member funnel?
7. What rules gate participation (dues state, waiver state, membership state)?
8. What surfaces exist (admin, kiosk check-in, member portal/app, staff app, capture pages)?
9. Where does this Type end and Dance Studio / Fitness Studio / Gym Management begin?
10. Do older/smaller/no-rank programs still fit the model?

## Representative Products

Four products, selected for market representation, documentation completeness, different product philosophies, and different scale targets:

| Product | Philosophy / position | Why sampled |
|---|---|---|
| Kicksite | Martial-arts-only specialist; self-describes as "martial arts CRM and so much more"; explicitly positions against one-size-fits-all gym software | The vertical-purist pole; SMB; ~2.1K+ schools claimed |
| MyStudio | Martial-arts-first platform (also serves "enrichment programs"); growth/AI-lead-conversion-led; mobile-first; built by multi-location school owners | The growth-led, mobile-first pole; single location → franchise |
| Zen Planner | Multi-vertical platform (Daxko) with a dedicated Martial Arts vertical page; same product sold to functional fitness, boutique fitness, dance, gymnastics, climbing | Direct evidence that the shared spine is sold across verticals; boutique → multi-location |
| Gymdesk | "Started in martial arts" (BJJ, karate, taekwondo, judo, MMA) but now sells to all gym types; simplicity/transparent-pricing-led | Second direct cross-vertical evidence; origin-in-vertical generalist; SMB |

Rejected as primary samples: Spark Membership, PerfectMind, Member Solutions, iClassPro/Jackrabbit (cross-vertical children's-activity platforms — Jackrabbit returned HTTP 403, iClassPro martial-arts path returned 404; the dance pass already documents those vendors' cross-vertical packaging, cited here as layer-B evidence).

## Sources

All fetched 2026-09-08. Official product/feature pages (Tier 2) and one feature-depth documentation set (Kicksite feature pages). No vendor help-center article bodies were retrieved this pass.

- Kicksite — https://kicksite.com/ (home) — martial arts CRM positioning, feature tabs, member portal, pricing
- Kicksite — https://kicksite.com/martial-arts-management-software/ — feature overview (member mgmt, billing, attendance, belt tracking, leads, communication)
- Kicksite — https://kicksite.com/martial-arts-attendance-tracking-software/ — check-in modes, mass check-in, reporting, check-in restrictions
- Kicksite — https://kicksite.com/martial-arts-member-management/ — student/family profiles, memberships, agreements, member portal
- MyStudio — https://www.mystudio.io/ (home) — product map, positioning, pricing
- MyStudio — https://www.mystudio.io/product/rank-belt-management — rank/stripe/test/promotion machinery (deepest rank documentation of the sample)
- MyStudio — https://www.mystudio.io/solutions/martial-arts — vertical positioning, workflow claims
- Zen Planner — https://zenplanner.com/martial-arts/ — martial arts vertical page
- Zen Planner — https://zenplanner.com/product/ — full feature list (membership, scheduling, attendance, payments, retail, reporting, staff app, branded app)
- Gymdesk — https://gymdesk.com/ (home) — feature list, FAQ incl. rank tracking, cross-vertical gym types, pricing

Unreachable / abandoned: Jackrabbit martial-arts page (HTTP 403), iClassPro martial-arts path (HTTP 404). Sourcing limitation: no help-center/knowledge-base article bodies retrieved for any product; precise operational parameters (exact billing-cycle defaults, numeric limits, exact status names) are therefore not asserted.

## Product Observations

Evidence layers: **A** = directly observed on an official page of this product; cross-product generalizations are layer **B** and appear in the Comparison section.

### Kicksite (all observations layer A)

- Positioning: "Martial arts CRM software and so much more"; explicitly against one-size-fits-all software that "also caters to yoga, pilates, dance" (home page).
- Business types served: BJJ, Karate, Krav Maga, MMA, Taekwondo, Wrestling (nav). Note: **wrestling has no belt ranks** — the vendor serves rank-less programs too.
- Member management: centralized student and family profiles; student profile contains bio (email, phone, DOB, address), attendance log + attendance awards, agreements (received/signed/unsigned), comments (staff-visible, pinnable), finances (invoices, recurring billings, payments, payment methods), communication settings, documents, and an activity history ("what changes were made… and who made them").
- Family: "Martial arts is often a family affair" — Family Profile gives a comprehensive view of the entire family's memberships, agreements, and finances, with switching to individual Student Profiles.
- Memberships: Membership Templates — Individual or Trial templates; custom duration: Unlimited (no expiration), Limited Term (set days/weeks/months/years), or a specific number of class attendances; templates connect to one or multiple Programs; billing structures: One Time (paid in full), Recurring (customizable pricing, frequency, occurrences), or No Charge (trials/promotions).
- Billing: recurring automated billings, one-time charges, invoices for every transaction ("paper trail"), past-due invoice monitoring and resolution, automated past-due reminders, inventory for merch/apparel, integrated card processing via partner Basys (flat rate; option to pass service fees to students).
- Attendance: kiosk check-in (PIN, name search, or barcode via 2D scanner; barcodes printable or shown in member portal), Mass Check-In (filter/select/check in a group in one action; retroactive dates), live attendance feed, individual and grouped attendance reports (filter by date range, program/rank, student vs trial), per-student "classes and days at current rank".
- Check-in restrictions: configurable blocking of check-in for students/prospects with past-due balance, missing memberships, or missing signed agreements; customizable kiosk message explains the block; live attendance view shows red alert icons for past-due invoices, expired memberships, missing waivers.
- Belt tracking: custom belt rank curriculum; belt ranks connected to Programs and students; belt testing events; "Eligible to Promote" view with one-click promotion; full promotion history.
- Leads: lead capture forms and landing pages (free trial prospects, summer camp signups, full membership purchases online), shortlink/QR generators, drag-and-drop prospects board, two-way texting, automated lead-nurture message flows.
- Communication: free unlimited 1-way texts and emails; bulk announcements segmented by program/membership; automated alerts for expiring memberships and past-due invoices.
- Member portal / mobile web app: dashboard (announcements, achievements, upcoming classes and events), event registration, self check-in barcode, class registration, finances (invoice/payment history, manage payment methods), media library (videos/photos/documents for virtual learning).
- Pricing: monthly tiers by active student count ($49–$199); all features at every tier.
- FAQ: differentiators vs general gym software named as "belt rank tracking, promotion management, attendance awards, testing events, and student progression features".

### MyStudio (all observations layer A)

- Positioning: "all-in-one martial arts software… billing, belts, and camps from one place"; "Built around memberships, ranks, and retention"; also serves enrichment programs (coding schools, art/music, tutoring, after-school, parkour/ninja) — kids/family context.
- Product map: membership management, billing & payments, scheduling, attendance tracking, member app, member communication, **rank & belt management**, digital waivers, point of sale; sales enablement, marketing automation, AI lead conversion; website builder, custom app; task management, reporting & analytics.
- Rank & belt management (deepest of the sample):
  - Fully custom rank systems: rank names, colors, stripe counts; traditional kyu/dan terminology; stripe-heavy BJJ progressions; separate tracks per style ("run karate, taekwondo, and BJJ under one roof — each style gets its own belts and timeline").
  - Promotion requirements per rank: attendance minimums, months time-in-rank, techniques, instructor sign-off; system "tells you who's ready" (test-ready alerts surfaced automatically).
  - Belt test management: create belt test events, auto-fill with rank-ready students, collect test fees "through the same billing engine as memberships", record results as promoted or deferred; rank records update immediately.
  - Promotion announcements: automatic celebration message to student and parent when a rank is earned.
  - Curriculum & video library attached to ranks: technique videos, kata requirements; students see requirements in the member app.
- Membership/billing: manage every member from one clear profile; automated recurring billing and payment recovery; payment processing via partner processors.
- Scheduling: build classes, online booking; attendance tracking: check-ins and "spot members at risk".
- Waivers: digital waivers — "collect signed consent before class".
- Lead funnel: sales enablement, marketing automation, Amplify AI (answers inquiries and books trial classes 24/7); trial-to-member conversion named as an essential; parents self-complete online sign-up.
- Events: "Belt tests, tournaments, camps, birthday parties: MyStudio handles capacity, payment, waivers, and reminders."
- Member app: bookings, passes, progress (current rank, next test, what comes after) visible to students; promotions notified in-app.
- Scale: single location, multi-location, franchise ("one dashboard and control across all your studios"); testimonial from a 14-school operator.
- Pricing: starts $79/month per location, unlimited students; plan tiers named Essentials/Growth/Scale/Accelerate AI.

### Zen Planner (all observations layer A)

- Same platform sold across verticals (nav): Martial Arts (school/BJJ/MMA), Functional Fitness, Boutique Fitness (yoga/pilates/barre/cycling/rowing/climbing/group), Gymnastics & Dance — direct cross-vertical family evidence.
- Martial arts page: "Track belt progress, manage family memberships, automate payments, and schedule classes."
- Belt & skill tracking: "View each student's belt rank on their profile to identify who's next for belt testing"; member app tracks belt and skill progress and gives access to shared curriculums and videos "to advance outside of the class and reach their next belt more quickly".
- Family: "Seamlessly manage family memberships — one simple sign-up process for the entire family… easy family management."
- Payments: automated billing, revenue recovery, automatic card updates; integrated processing included.
- Scheduling/booking: online booking, embedded calendars/forms (free trial sign-up), real-time attendance tracking; appointments as a separate booking type with payroll options; conflict/double-booking elimination for staff scheduling.
- Attendance: kiosk mode and staff-app check-in; attendance history viewable by members — "for rank-based programs, can view progress towards their next belt or test"; automated absentee emails for members absent a period; milestone recognition emails (anniversaries, 100-classes attended — examples shown as feature copy).
- Member self-service: check-in, reserve class spots, resolve alerts, pay bills, purchase retail.
- Contracts/waivers: "Build customized contracts and waivers for specific membership categories" with digital signatures.
- Retail: sell/process/track retail purchases, inventory management.
- Reporting: customizable dashboards (financial, student, attendance data); automated alert notifications.
- Marketing: Zen Planner Engage (CRM, 2-way text/email, lead tracking, webchat, reputation); prospect email nurture ("attended an intro class").
- Staff app: rosters/capacity planning, check-ins and alert resolution, staff time clock.
- Pricing: starts $99/month (stated in FAQ).
- Customer base spans martial arts (SKH Quest Center NYC), CrossFit, personal training — same product.

### Gymdesk (all observations layer A)

- Origin and breadth: "We started in martial arts — BJJ, MMA, karate, taekwondo, Muay Thai, judo — so belt tracking, skills, and family memberships are built in. But it runs just as well for fitness gyms, yoga and Pilates studios, gymnastics, dance, CrossFit, and membership clubs." (FAQ) — second direct cross-vertical evidence.
- Feature list (all plans, no tiers): Memberships ("unlimited plans, ranks, programs, and family accounts"), Billing ("automatic collection, failed-payment recovery, and overdue alerts"), Attendance ("check in by kiosk, name search, barcode, or phone"), Booking ("a class schedule members book and manage from their phone"), Website, Point-of-sale, Marketing (email, SMS, referrals, automated follow-ups), Reporting, Mobile app ("members check in, book, and track their progress"), Facility access ("app and smart-lock door access — give members 24/7 entry"), Payment processors (Gymdesk Payments, Stripe, Square, GoCardless, Ezypay; cards, ACH, in-person; manual payment recording where no processor is available), Integrations.
- Rank FAQ: "Set each program's rank progression and how members qualify (classes, hours, attendance, skills, or age), and Gymdesk tracks everyone's progress and flags who's ready to promote."
- Lead machinery: lead management, landing pages, automations (example flow shown: schedule first class, send messages, change contact tags), referrals, reviews.
- Customer logos: major BJJ organizations (Alliance, Renzo Gracie, 10th Planet, Gracie University, Gracie Barra) plus taekwondo/judo operators in testimonials.
- Pricing: starts $75/month scaling with active member count.

## Cross-product Comparison

| Structure / capability | Kicksite | MyStudio | Zen Planner | Gymdesk | Layer |
|---|---|---|---|---|---|
| Student/member record as central object (profile spanning identity, finances, attendance, agreements) | ✓ student profile (8 sections) | ✓ "one clear profile" | ✓ member profile w/ belt rank | ✓ members | B |
| Family accounts holding multiple students | ✓ Family Profile | ✓ family enrollment/parent notifications | ✓ family memberships | ✓ family memberships | B (strong) |
| Programs + scheduled classes | ✓ Programs; schedules in FAQ | ✓ scheduling + online booking | ✓ classes + appointments | ✓ booking from phone | B |
| Membership as entitlement (template: duration/recurring) | ✓ templates incl. class-count and unlimited | ✓ memberships + passes | ✓ memberships/contracts | ✓ plans | B |
| Recurring dues + arrears machinery (failed payment, past-due alerts) | ✓ | ✓ payment recovery | ✓ revenue recovery | ✓ overdue alerts | B (strong) |
| Attendance check-in (kiosk/PIN/barcode/app) | ✓ 3 modes + mass check-in | ✓ | ✓ kiosk + staff app | ✓ 4 modes | B (strong) |
| Check-in/participation gating on dues, membership, or waiver state | ✓ explicit restrictions + kiosk messaging | ✓ "waivers before class"; at-risk flags | ✓ alert resolution at check-in | ✓ facility access control | B |
| Rank/belt tracking per program with promotion eligibility logic | ✓ eligible-to-promote, rank curriculum | ✓ requirements + auto test-ready | ✓ rank on profile, next-belt progress | ✓ per-program qualification rules | B (strong) |
| Belt testing events as a distinct event type with fees | ✓ testing events | ✓ test events + fee collection | belt testing named, event depth not shown | flags ready-to-promote (test events not shown) | A×2, partial |
| Promotion recorded as history (not an edit) + family notification | ✓ promotion history | ✓ instant update + announcement | implied (rank on profile) | tracks progress | B (partial) |
| Lead → trial → member funnel with automation | ✓ landing pages, prospects board, 2-way text | ✓ Amplify AI, trial booking | ✓ Engage, intro-class nurture | ✓ lead mgmt, automations | B (strong) |
| Waivers/agreements with e-signature and tracking | ✓ templates, unsigned list | ✓ digital waivers | ✓ contracts + waivers per category | forms (depth not shown) | B |
| Communication (email/SMS, announcements, automated alerts) | ✓ incl. expiring-membership/past-due alerts | ✓ targeted SMS/email/app | ✓ absentee emails, milestones | ✓ email/SMS/automations | B (strong) |
| Member self-service portal/app (book, pay, progress) | ✓ portal + mobile web app | ✓ member app shows rank path | ✓ member app + self-service | ✓ mobile app | B (strong) |
| Retail/POS + inventory | ✓ merch/apparel inventory | ✓ POS "sell gear" | ✓ retail + inventory | ✓ POS + inventory | B |
| Events beyond classes (camps, tournaments, parties) | ✓ events on portal; camps named | ✓ tests, tournaments, camps, parties | events on calendar | booking (depth not shown) | B (partial) |
| Curriculum/media attached to programs or ranks | ✓ media library | ✓ curriculum & videos per rank | ✓ shared curriculums/videos | skills (depth not shown) | B |
| Reporting (revenue, retention, attendance) | ✓ attendance + finances | ✓ reporting & analytics | ✓ dashboards + alerts | ✓ reporting | B |
| Season/session container with registration windows and copy-forward | not observed | not observed | not observed | not observed | — (absent from sample) |
| Continuous month-to-month membership posture | ✓ unlimited/term templates | ✓ recurring billing | ✓ monthly billing | ✓ monthly plans | B |
| Multi-location / franchise | ✓ scales | ✓ multi-location + franchise | ✓ multi-location customers | not prominent | B (partial) |
| Payment processing bundled/partnered | ✓ Basys partner | ✓ partner processors | ✓ integrated included | ✓ multiple processors / manual fallback | B |
| Website builder / branded app add-ons | ✓ website services | ✓ website + custom app | ✓ custom website + branded app | ✓ free website | B |
| Rank-less programs served (e.g., wrestling, boxing) | ✓ wrestling | — (styles listed all ranked; enrichment programs) | — | — (list includes ranked styles) | A (single) |

Two structural notes from the comparison:

1. **No season/session container appears anywhere in the martial-arts sample.** The dance sample's defining container (season/session with registration windows and copy-forward) is absent; instead the sample shows continuous memberships (unlimited/limited-term/class-count durations) and event anchors (belt tests, tournaments, camps). This is a real structural difference between sibling verticals, not just vocabulary.
2. **Both boundary poles are present in one product family.** Zen Planner and Gymdesk each directly sell one product across martial arts and fitness/gym verticals; the dance pass documented cross-vertical packaging on the class-management side (Jackrabbit/The Studio Director/Studio Pro/iClassPro, layer B for this pass). The martial-arts realization sits structurally between the two documented poles.

## Canonical Model

### Level 0 — Defining Invariant (minimal)

```text
Student record (identified person enrolled in the school;
        held on a family account when children train)
└── Program + scheduled class offerings (the school's offer)
    └── Membership / enrollment (entitlement linking the
        student to what they may attend)
        └── Dues-and-fees loop (charges generated by the
            membership, settled by payment, arrears tracked)
```

Four jointly-held structures. Removal test:

- Remove the student record → nothing left to manage; not a school system.
- Remove programs/schedule → a dues engine or contact list, not a school.
- Remove the membership/enrollment linkage → an attendance tracker or a class directory; there is no "who is enrolled in what" — the commercial relationship is gone.
- Remove the dues-and-fees loop → a class roster app; the school stops being run as a business in the system.

Deliberately NOT in L0 (each fails the "would still be the same Type" or the historical test):

- **Rank/belt tracking** — the signature extension of this vertical, present in all four sampled products, but (a) the dance pass holds the same spine for siblings, (b) some programs these very vendors serve (wrestling per Kicksite) have no ranks, and (c) a paper-era school ran fine with a promotion ledger. It is the standard martial-arts layer, not the definition.
- **Attendance machinery** — universal in the sample and deeply coupled to progression and gating, but the core loop (enroll → owe → pay → attend) still stands without it; consistent with the dance pass's treatment of attendance as standard capability.
- **Family accounts** — extremely common (all four products), but adult-individual academies are a large legitimate segment; the invariant is the student record, with family grouping as the dominant implementation for children.
- **Season/session container** — absent from the entire martial-arts sample; time is structured by continuous memberships and events.
- **Lead/trial CRM, portals, POS, communication, waivers, kiosk hardware** — common mature structure (L1) or variants (L2), not definition.

Historical/market-sample check (older, regional, platform-native, differently positioned): a paper-era martial arts school (student index cards, wall schedule, dues ledger, attendance cards, promotion record with certificates, cash test fees, signed paper waivers) satisfies every L0 element. Rank systems differ by discipline and era (kyu/dan, stripes, sashes, none) — the abstraction is "recorded progression per student where the discipline uses one," which the paper school also satisfies. A rank-less program (wrestling/boxing, directly served by Kicksite) still fits: the school manages students, programs, memberships, dues. L0 holds.

### Level 1 — Common Mature Structure

- Attendance and check-in machinery (kiosk PIN/name/barcode/app check-in, mass check-in, live feeds, history) — present in all four sampled products.
- Participation gating: check-in/access blocked or flagged on past-due balance, missing membership, or missing waiver; alert resolution at the door.
- Rank & advancement layer: per-program rank structures (custom names/colors/stripes; kyu/dan; stripe progressions), promotion requirements (attendance minimums, time-in-rank, techniques/skills, instructor sign-off), system-surfaced test-ready lists, belt testing events with fees, promotion history, promotion notifications to student and family.
- Curriculum content attached to programs/ranks (technique videos, kata requirements) and member-visible.
- Lead → trial → member funnel: capture forms/landing pages, free trial or intro-class offers, prospect tracking (board/pipeline), automated nurture, two-way texting. Conspicuously stronger in this vertical than in the documented dance sample.
- Waivers/agreements: templates, e-signature, unsigned tracking, attachment to registration.
- Member self-service portal/app: book classes, view schedule, pay/manage payment methods, view progress/rank, self check-in barcode, receive announcements.
- Communication: email/SMS, announcements segmented by program/membership, automated alerts (expiring memberships, past-due invoices, absences, promotions, milestones).
- Retail/POS with inventory (gear, uniforms, apparel).
- Events beyond classes (belt tests, tournaments, camps, birthday parties) with registration, payment, waivers, reminders.
- Reporting: revenue, retention, attendance, growth dashboards.
- Bundled or partnered payment processing with failed-payment recovery.

### Level 2 — Variant / Optional Structure

- Customer shape: kids/family-centric schools (parents as account holders) vs adult academies (individual members) vs mixed.
- Rank-system shape: kyu/dan (karate etc.), BJJ stripe progressions, taekwondo dan, custom colors; or no ranks at all (wrestling, boxing) — progression tracked as skills/attendance.
- Membership shape: recurring month-to-month, limited term, paid-in-full, class-count/punch entitlements, no-charge trials.
- Time structure: continuous enrollment anchored by events (belt tests, camps, tournaments) — contrast with season/session siblings.
- Billing posture: integrated/included processing, partner processors, bring-your-own processor, manual payment recording where no processor exists.
- Facility posture: staffed front desk with kiosk vs unstaffed 24/7 smart-lock access.
- Scale: single location → multi-location → franchise/association rollouts.
- Adjacent services: website builder, branded member app, marketing services, business insurance (vendor-specific variants below).
- Region: US-centric market with international presence (sample includes a Swiss customer story; MyStudio lists US/CA/UK/AU).

### Level 3 — Vendor-specific (research notes only)

- Kicksite: Basys flat-rate processing partnership; free unlimited 1-way texting; attendance "awards"; positioning as independently owned, martial-arts-only; pricing purely by active-student count with all features at every tier.
- MyStudio: Amplify AI lead conversion; official partnerships (Century Martial Arts, ATA, USA Muay Thai, USA Judo, MAIA, Code Ninjas); "built by owners who scaled five $1M+ locations" positioning; per-location pricing with unlimited students; named plan tiers.
- Zen Planner: Daxko ownership; Zen Planner Engage CRM suite; SugarWOD workout-tracking integration (functional-fitness carryover); business-insurance offering; appointment booking with payroll options; staff time clock.
- Gymdesk: all-features-in-every-plan/no-tier pricing; Guardian Project (charitable sponsorship of kids who can't pay); Gymdesk Payments; facility-access smart-lock module; "Martial Arts onRails" product heritage (review badges).

## Rejected Findings

- **"Martial arts management = fitness software + belts"** — rejected as a definition. The sampled products also carry the family/student/class/attendance spine documented for dance-type verticals; the Type is better modeled as one family realization with two neighboring gravity wells (see Boundary Findings). Kept as characterization, not definition.
- **"Family account is definitional"** — rejected: adult-individual academies are a first-class segment (Kicksite membership templates are "Individual or Trial"; Gymdesk/Zen Planner sell the same product to adult-only gyms); family grouping is the dominant implementation for children's programs.
- **"Belt/rank tracking is definitional"** — rejected: rank-less programs are served by the same products (Kicksite wrestling); progression abstraction must cover skills/attendance-based advancement.
- **"Season/session container is part of the core"** — rejected for this vertical: no sampled martial-arts product leads with a season/session container (contrast: the dance sample). Enrollments are continuous, anchored by events.
- **"Precise pricing/pricing-tier structures are Type structure"** — rejected to research notes; all sampled products price monthly by scale but plan architectures differ (per-student tiers vs per-location tiers vs all-inclusive scaling).
- **"Every martial art uses belt ranks"** — factually false (wrestling, boxing); noted so the final document never hard-codes belts into the definition.

## Boundary Findings

- **vs Dance Studio Management (processed sibling, §28)**: same family spine (student records on family accounts, scheduled recurring classes, enrollment/membership, tuition/dues loop, attendance, portals). Dancers' realization adds the season/session container and the performance layer (costumes, recitals, competition teams). Martial-arts realization adds the progression/testing layer (ranks, requirements, test events, promotions) and a stronger lead/trial machinery, and runs on continuous memberships instead of season enrollment. Removal test: strip ranks/testing from a martial-arts product and add season+costume/recital machinery → you have the dance realization; strip season+performance from dance and add ranks → this Type. Joint-review recommendation from the dance pass is **discharged from this side**: keep-both with the signature-layer seam is ratified; the shared spine stays the definition for both.
- **vs Fitness Studio Management (processed sibling, §28) and Fitness Membership Management (processed, §28)**: the membership/dues/check-in/booking spine is shared, and two sampled vendors sell one product across both markets (Zen Planner, Gymdesk) — the seam is structural, not vendor-claimed: fitness centers on the adult member and the drop-in/class-pack economy; martial arts centers on the enrolled student (often a minor on a family account), a program-and-rank progression, and testing/advancement events. Remove progression + minors/family + testing from this Type → fitness studio management.
- **vs Gym Management System (unprocessed sibling, §28)**: per the climbing-gym pass's segment-sibling pattern, the business core (members, entitlements, check-in, billing, booking, POS) is shared; expect the gym leaf to document the access/equipment/big-box layer while this leaf holds the school/class/progression layer. Same joint-review posture as the climbing pass.
- **vs Swim School / Gymnastics Club Management (unprocessed siblings, §28)**: predicted to be the closest siblings of all (children's class management; swim adds level cycles/makeup emphasis, gymnastics adds skill tracking/meets). Same family flag applies; recommend joint review when processed.
- **vs Membership Management System (§25) / Membership Billing**: generic dues/lifecycle engine without programs, class schedules, attendance, or progression semantics; the martial-arts Type instantiates membership dues against a program/class schedule.
- **vs Sports Registration Platform (§28)**: one-shot registration transactions for programs/seasons vs the ongoing membership relationship with rosters, dues, attendance, and progression.
- **vs Youth Sports Management / Team Management (§28)**: team/league/roster-and-game orientation vs school/class-and-membership orientation.
- **vs LMS / Learning platforms (§23)**: curriculum content exists here but is attached to business operations (ranks, retention); the teaching/learning loop is not the center — the school's commerce and operations are.
- **vs generic CRM**: this Type embeds a CRM-shaped prospect funnel (all four sampled products), but the center of gravity is the enrolled-student operating loop, not the deal pipeline. Kicksite's self-description as "martial arts CRM and so much more" shows the funnel's prominence without making it the Type.

## Uncertainties

- Belt-test event machinery is documented at depth for two products (Kicksite testing events; MyStudio test workflow with fees/results/notifications); Zen Planner names belt testing but event depth was not observed; Gymdesk shows eligibility flagging but not a test-event object. Test events are asserted as common, not universal.
- Waiver depth for Gymdesk was not directly observed (forms referenced; digital-waiver surface not fetched). Waivers are asserted as common from three products plus Gymdesk's paperwork/billing positioning.
- Help-center article bodies were not retrieved for any product; operational parameters (billing-cycle defaults, exact state names, numeric limits such as rank requirement thresholds) are intentionally not asserted anywhere.
- The cross-vertical packaging of iClassPro/Jackrabbit/The Studio Director/Studio Pro into martial arts is carried from the dance pass's research (layer B here); their martial-arts pages were not reachable this pass (403/404).
- Regional depth beyond the US (the sample shows a Swiss customer and US/CA/UK/AU vendor claims) was not researched; localization claims are not made.

## Final Synthesis

A Martial Arts School Management application is the operator-side business system for running a martial arts school (dojo/academy). Its defining core is four jointly-held structures: **student records** (held on family accounts when children train), **programs with scheduled class offerings**, **memberships/enrollments** linking students to programs as entitlements, and the **dues-and-fees loop** those memberships generate (recurring charges, payments, arrears). Around that core, mature products add the martial-arts signature layer — **progression tracking (rank/belt/skill structures per program, promotion requirements computed from attendance and time-in-rank, test-ready flags, belt testing events with fees, recorded promotions)** — plus the operating machinery common across the product family: attendance check-in with entitlement gating, lead/trial funnels, waivers, member portals/apps, communication automation, retail/POS, events, and reporting. Two structural traits distinguish this realization from its siblings: continuous membership posture (no season/session container) and event-anchored time (belt tests, tournaments, camps), and it structurally straddles the two documented poles of the family — class-management (dance side) and membership-management (fitness side) — which is why multi-vertical vendors sell one product across both.

Taxonomy disposition: keep the leaf as the martial-arts realization of the class/membership-management family; keep-both-with-seam is ratified against the dance and fitness passes; the family-level joint review remains open for Swim School Management and Gymnastics Club Management.
