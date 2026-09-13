# Research Notes — Childcare Management System

Slug: childcare-management-system
Directory location: §29 Home, Family, Personal & Local Services (siblings: Daycare / Preschool Management, After-school Program Management, Camp Management System, Babysitting Marketplace)
Research date: 2026-09-07

This leaf carries a **joint-review obligation** recorded in STATUS.md by the after-school-program-management pass: "after-school-program-management vs childcare-management-system / daycare-preschool-management … flagged for joint review when those leaves are processed." Discharged below (Boundary Findings #1 and #2).

---

## Research Goal

Understand what "Childcare Management System" software actually is as an Application Type: who operates it, what core objects exist inside it, how the enrollment → daily-care → documentation → billing loop works, and where its boundary sits against the neighboring after-school, camp, daycare/preschool, and marketplace Types.

## Initial Boundary (working hypothesis before research)

- Operator-side software for businesses that provide full-day, year-round care for children (daycare centers, preschools, home-based family childcare).
- Expected core: child/family records, ongoing enrollment, daily attendance with sign-in/out custody, rooms and ratios, tuition billing, daily reports to parents.
- Nearest neighbors: After-school Program Management (same spine, part-day programs), Daycare / Preschool Management (probable overlap), Camp Management System (seasonal sessions), Babysitting Marketplace (two-sided consumer matching), Parenting/Baby Tracking Application (consumer-side logging).
- Key open question: which care-context structures (rooms, ratios, custody, daily reports) are definitional vs common, given home-based providers may lack rooms.

## Research Questions

1. Who are the operator-side and participant-side users, and what roles exist?
2. What is the central record — child, family, or enrollment — and how do they relate?
3. How is enrollment shaped (ongoing vs session-bounded) and what lifecycle states exist?
4. How does daily care get recorded: attendance, custody handover, authorized pickups?
5. What is the daily documentation loop to guardians, and what does it carry?
6. How do rooms/classrooms, capacity, and staff-to-child ratios work — and are they definitional?
7. How does tuition billing work (recurring plans, formulas, subsidies/third-party payers)?
8. What health/safety/compliance machinery exists (immunizations, incidents, licensing records)?
9. Where is the boundary with after-school/camp/daycare-preschool/marketplace Types?
10. Do older (desktop-era), regional, and home-based products still fit the same definition?

## Representative Products

| Product | Segment posture | Philosophy | Customer tier | Evidence strength |
|---|---|---|---|---|
| Procare Solutions | legacy all-in-one incumbent (centers, Head Start, in-home, before/after-school, youth orgs) | business-suite (billing + attendance + payroll + GL) | single centers → multi-site/franchise; in-home low-cost tier | Medium-strong (Tier-2 product pages + Tier-1 support index + Tier-1 articles) |
| brightwheel | modern mobile-first SaaS, "100% early education" | engagement/app-first | SMB centers/preschools; family engagement emphasis | Strong (Tier-1 help center, multiple deep articles) |
| Lillio (formerly HiMama) | documentation/curriculum-first | family-engagement + learning documentation | SMB centers; home-daycare segment; enterprise tier | Weak-medium (Tier-2 marketing pages only; support center JS-gated) |
| Kangarootime | multi-location "CCMS", back-office emphasis | business-ops + classroom split (Business/School/Connect/Educator) | multi-site growing groups | Medium (Tier-2 product pages) |
| Smartcare (RevTrak/Vanco) | payments-platform-owned childcare suite | payments-centric, white-glove | centers, preschools, faith-based, districts; third-party payers | Weak-medium (Tier-2 product page only) |

Sample rationale: legacy suite vs modern app-first vs documentation-first vs multi-location back-office vs payments-owned; spans in-home providers to franchises and state-funded programs. Sandbox Software (Canadian, subsidy-heavy) abandoned after two timeouts; Lillio support center and HiMama help center JS-gated (Salesforce) — Lillio calibrated to positioning-level evidence.

## Sources

Fetched 2026-09-07:

- brightwheel Help Center (Intercom, Tier-1): home; "Get to know brightwheel"; "Everything you need to know about student check-in"; "Log activities"; "3 reasons to use brightwheel billing features"; "Create & share Admissions packets"; "Set a student's enrollment status"; "Get started with rooms"; Program Management collection TOC
- Procare Solutions (Tier-2): root page; Classroom Management capability page; footer capability/solutions map
- Procare Support (Document360, Tier-1): support home; llms.txt documentation index (full module map); "Child Pickup" article
- Kangarootime (Tier-2): root page; "Childcare Management System" solution page
- Smartcare / RevTrak (Tier-2): revtrak.com/child-care product page
- Lillio (Tier-2): root page; "Manage your center" and "Communicate with parents" feature pages

Unreachable / degraded:

- Lillio support center (support.lillio.com) and legacy HiMama help center (help.himama.com) — Salesforce JS shell ("CSS Error"), 1 attempt each → Lillio claims kept positioning-level
- Sandbox Software (sandboxsoftware.com) — timeout ×2 → abandoned
- smartcare.com — redirects to RevTrak (product absorbed into RevTrak/Vanco portfolio); original help center not reachable

---

## Product A — Procare Solutions

### Key observations (evidence layer A unless noted)

- Positioning: "A Leader in Child Care Management Software"; "trusted by educators at over 40,000 child care centers"; serving "daycare, preschool, Head Start or ECE center" with one product line; since 1992. (A)
- Solutions map: Child Care Centers, Head Start Grantees, Before and After School Programs, Youth Organizations; sub-segments include Franchises, In-Home Daycare, Multi-Centers, School Districts, YMCA, Shared Services. (A)
- Capabilities map: Child Care Management Software, Family Engagement, Payment Processing, RoomRunner (AI-assisted enrollment planning: "see future openings, plan room transitions, match the right family to the right seat"), Classroom Management, Head Start Management (ChildPlus), Early Childhood Learning, Professional Development, Child Care App, Third-Party Integrations; footer adds Financial Management (daycare bookkeeping), Meal Planning, Multi-Center Management, Staff Management. (A)
- Classroom management page: track attendance and room movement; staff-to-child ratios "governed by state requirements" with ratio reporting; name-to-face reporting; tracking "attendance, ratios, remaining room capacity, enrollments, meals, health checks and authorized pick-ups"; unscheduled attendance for drop-in students; contactless check-in/out; Infant Activity Dashboard (bottles, naps, diaper changes with nap position, bottle size, diaper-change types; reminders); student schedules with overrides/absences compared to staff schedules room by room; Insights (enrollment capacity per room/program, open availability, staffing needed to retain ratio). (A)
- In-home version: full feature set at low price, but "classroom management functionality is not available for in-home users" — rooms are segment-dependent, not universal. (A)
- Support index (Tier-1, module map): Family & Child Data (Account/Family Information, Add Child to Account, Assign Child Schedules, Child Enrollment Status, Batch Change Enrollment Status, Child Schedule Overrides & Absences, Classroom Forecasting, Classroom Graduation, Secondary Classroom, Divorced Parents, Duplicate Family Accounts – Merge, When to Remove a Child, Immunizations, Log Sheet/Log Sheet Types); Family Accounting (Automated Contract Billing, Automated Formula Billing, Drop-In Formula Billing, Billing Formula Builder, Contract Billing Cycles, Account Ledger Card, Deposits, Family Discount, Late Payment Calculator, NSF/declines, Scholarships, End-of-Year Statements, Fund Accounting, Employee Child Care); **Agency Accounting** (Assign Agencies to Families, Billing Box with Agencies, Third-Party Agency Setup/Adjustment Codes, Agency Payment Posting, Agency Prepays and Take-Backs, Handling Co-Pays, Agency Overpayment); Attendance Tracker (Check-In Options, Check-In Computer, cardswipe, fingerprint bypass via Person ID, Check-In Monitor, Child Batch Check In/Out, Child Time Card, **Child Pickup**, **Deny Entry / Block Check In**, Register a Pickup Person, Receptionist Check In, Temporary Registration Number); Meal Tracker (menus, age groups for meal counts, food-program status, reimbursement amounts); Activity Manager (rotating schedules, batch activities, FTE, Schedule Adherence); Employee Data & full Payroll (time cards, approval, pay codes, W4s, tax tables, direct deposit); Expenses & Ledger (chart of accounts, journal entries, bank reconciliation, vendors, budgets); Configuration (Classrooms, Regions and Schools, multi-location copy, Buying/Selling a Center, New Location Checklist). (A)
- "Child Pickup" article: each authorized person is marked as Pickup per child via Child Information & Relationships; each pickup person has a Child Pick Up screen listing the children they may check in. (A)
- RoomRunner (support home): AI-powered insights and projections to "manage classroom capacity, waitlists, and transitions." (A)
- Three platforms: Procare Desktop (legacy), Procare Online (cloud), Procare SchoolCare Works; integrated payment processing (Tuition Express). (A)

## Product B — brightwheel

### Key observations (evidence layer A)

- Positioning: "focused 100% on Early Childhood Education"; features headline: check-in & attendance ("state licensing approved"), parent invoicing & online bill pay, daily reports & activities, photo & video sharing, learning/curriculum/assessment tools, messaging, admissions packets; iOS/Android apps for staff and parents + web portal. (A)
- Check-in: kiosk (mobile device as station) and QR Quick Scan; contacts (parents, guardians, **approved pickups**) check children in/out; 4-digit check-in codes; optional digital signatures, health-screen questionnaires, drop-off forms (wake-up time, last meal, bathroom use, optional pickup time); staff Attendance Mode (check in/out, move students between rooms, mark absent); "All check-in data is automatically recorded, giving administrators real-time visibility into attendance and room ratios needed for licensing and tuition billing." (A)
- Contact types: Parents, Family, Approved Pickups, Emergency Contacts — Approved Pickups and Emergency Contacts cannot see activities; a student's feed is visible to teachers and Parent/Family contacts. (A)
- Rooms: "Rooms are a fundamental part of how brightwheel works" — teachers, staff, and students assigned to rooms; check-in, activity logging, and parent messaging happen from rooms; Room Ratios and Capacity (custom max capacity + desired student-to-staff ratio per room); Room Check report (real-time ratios); out-of-ratio alerts; Room Feed with admin approval of staff-only posts; Room Device Mode (shared device without shared logins). (A)
- Activity logging (the daily documentation loop): activity types Photo, Video, Observation (against state standards/learning frameworks), Food (custom menus, meal types; CACFP tracking in Premium), Nap (start/end, in-progress icon), Potty (diaper changes/potty breaks), Note, Kudos, Custom, Meds, Name to Face (internal whereabouts, staff-only), Incident, Health Checks (temperature); log from a Room (multiple students) or a student's feed; staff-only visibility flag; feed approval workflow. (A)
- Enrollment statuses: Active, Graduated, Inactive, Removed, Duplicate, Prospect, Toured, Applied, Waitlist, Enrolled; admissions pipeline "from their first tour to graduation day"; statuses "retain historical records for licensing"; auto-set Active on enrollment date; role limits (Lead Staff cannot set Inactive/Duplicate/Removed/Graduated; parents cannot change status). (A)
- Admissions packets: consolidate required forms, fillable documents, contracts, handbooks, document requests, welcome info, and fees into one digital packet; due dates (admin-visible), submission fees; shared directly to existing families or via link (new families create an account + child profile). (A)
- Billing: one-time or recurring billing plans; automated invoicing and reminders; custom frequencies (weekly, monthly, quarterly); attendance-based invoices; autopay; charges split between multiple payers; Tap to Pay; year-end tax statements; revenue reports; rate-sheet upload; billing templates. (A)
- Program Management collection: room administration, student management (add, assign to rooms, enrollment status, transfer between program locations for multi-sites), student contacts management (permissions, parent directory), staff management (assign to rooms, permissions/roles), monitor program activities (room feeds, approval), **send data to government systems** (My Food Program; Indiana I-LEAD Provider Portal; Minnesota DCYF; KinderConnect; Iowa; Kentucky). (A)

## Product C — Lillio (formerly HiMama)

### Key observations (evidence layer A for positioning; B/C for structure)

- Positioning: "#1 Rated Childcare Management Software"; "Build, manage and grow your early childhood program"; solutions: Center management, Curriculum (Funshine Express), Family engagement, Billing & payments, Professional development (Lillio Academy). (A)
- Users: Owners and directors, Educators, Families, Enterprise, **Home Daycare**. (A)
- Claims: 35,000+ customers; "2.1B moments shared with families"; customer stories reference QRIS quality-rating achievement and documentation time savings. (A — vendor claims, kept as claims)
- Family engagement: "regular updates, photos and videos, and better insight into their child's day and development." (A)
- Structure beyond positioning could not be verified (support center JS-gated); the daily-documentation-first philosophy is corroborated by the "moments shared" metric and customer stories. (B/C)

## Product D — Kangarootime

### Key observations (evidence layer A)

- Positioning: "The All-in-One CCMS [Child Care Management System] for Growing Multi-Location Childcare Businesses"; "Whether you operate two centers or twenty." (A)
- Suite split: **Business** ("automates registration and enrollment, lead management, billing, staff scheduling"), **School** ("attendance and custody, builds student profiles and tracks their progress, communicates with families, and provides staffing insights"), **Connect** (parent app: "share photos and videos, track daily logs, send messages, and highlight activities… even pay their bill"), **Educator** (on-demand guidance, lesson plans, in-the-moment coaching). (A)
- Users: Owners ("manage your entire business in one system"), Directors, Teachers, Parents. (A)
- Separate **Before and After School Management** solution ("extended care and seasonal programs") — evidence that childcare and after-school are sibling segments of one vendor. (A)
- Education Hub (LMS for educator training, via CypherWorx partnership). (A)
- Customer quotes reference daily notes, online payments, staff timesheets in one place; preschool customers. (A)

## Product E — Smartcare (RevTrak / Vanco)

### Key observations (evidence layer A)

- Positioning: "All-in-one platform to power your childcare program"; "connects hundreds of thousands of parents to preschools, early childhood learning programs, before and after care programs, daycares, enrichment programs, and more." (A)
- Segments as separate blocks of one product: Childcare & Daycare Centers ("enrollment, digital check-in and check-out, attendance, billing & payments, reporting, and lead tracking"), Preschool & Early Childhood Programs ("center management tools, teacher tools, daily reports, family communication"), Before & After Care ("online enrollment, attendance, touchless check-in and check-out, waitlist, enrollment, billing, payments"), Private Schools (Montessori/K-12), Faith-based Childcare, K-12 Districts (Pre-K). (A)
- Capabilities: automate online enrollment, track leads, build waitlist, manage compliance, real-time financial reporting; "customize billing by schedule, tuition plans, discounts, and **third-party payers**"; parent and teacher apps; electronic check-in/out. (A)
- Owned by a school-payments platform (RevTrak/Vanco) — payments-centric posture. (A)

---

## Cross-product Comparison

| Dimension | Procare | brightwheel | Lillio | Kangarootime | Smartcare |
|---|---|---|---|---|---|
| Central record | Family account → children (payer + children) | Student profile + student contacts | Child/family (positioning-level) | Student profiles under center | Child enrollment under program |
| Enrollment shape | Ongoing; enrollment status + withdraw date; classroom graduation/transition | Ongoing; status pipeline Prospect→Toured→Applied→Waitlist→Enrolled→Active; Graduated/Inactive/Removed | Ongoing (positioning-level) | Ongoing; registration/enrollment automated | Ongoing; enrollment + waitlist + leads |
| Daily attendance | Check-in station (cardswipe/fingerprint/Person ID); child time cards; batch check-in/out | Kiosk/QR/staff mode; check-in codes; real-time ratios from check-in data | (positioning-level) | "Attendance and custody" | Digital/touchless check-in/out |
| Custody controls | Authorized pickup persons per child; deny entry; receptionist check-in | Approved-pickup contact type; digital signatures; check-in codes | (unverified) | "custody" named in School module | (implied by check-in/out) |
| Rooms & ratios | Classrooms; ratio monitoring "governed by state requirements"; forecasting; **absent for in-home tier** | Rooms "fundamental"; capacity + desired ratio per room; out-of-ratio alerts; Room Check | (unverified) | Classroom dashboard; staffing insights | (implied) |
| Daily documentation | Log sheets; Infant Activity Dashboard (bottles/naps/diapers); family app sharing | Activity types (photo/video/food/nap/potty/note/meds/incident/health/observation); room feed + approval | Core brand ("moments shared") | Daily logs, photos/videos via Connect app | Daily reports |
| Tuition billing | Contract billing, formula billing, drop-in billing, ledger, deposits, discounts, late fees, statements | Recurring plans, attendance-based invoices, autopay, split payers, tax statements | Billing & payments module | Automated billing | Billing by schedule/tuition plans/discounts |
| Subsidy / third-party money | Agency Accounting (third-party agencies, co-pays, adjustment codes) | State portal integrations (I-LEAD, DCYF, KinderConnect, KY, IA); CACFP food reporting | (unverified) | (unverified) | Third-party payers named |
| Health & safety | Immunizations + requirements; health checks at check-in | Health screens, Meds, Incident, Health Checks activity types | (unverified) | (unverified) | "manage compliance" |
| Meals / food program | Meal Tracker (menus, age groups, reimbursement amounts) | Food activity + CACFP reporting (Premium) | (unverified) | (unverified) | (unverified) |
| Staff side | Employee data, time cards, scheduling, full payroll, GL | Staff check-in, room assignment, roles/permissions, staff schedules | Educator tools | Staff scheduling, Staff App, timesheets | Teacher app |
| Family-facing surface | Child care mobile app; email/SMS; newsletters | Parent app + web; messaging; gallery | Parent app | KT Connect app | Parent app |
| Learning/curriculum | Early Childhood Learning; curriculum partners | Observations vs state standards; Experience Curriculum; assessments | Curriculum (Funshine); documentation-first | Educator guidance + lesson plans | Teacher tools |
| Multi-site | Multi-center management; copy between locations; corporate reconciliation | Transfer students between program locations | Enterprise tier | Core positioning (2–20 centers) | Districts |
| Deployment | Desktop legacy + cloud (Online) + SchoolCare Works | Cloud SaaS, app-first | Cloud SaaS, app-first | Cloud SaaS | Cloud SaaS (payments-owned) |

Layer-B commonalities (present in ≥3 sampled products with direct evidence): child+guardian records; ongoing enrollment with status lifecycle; daily check-in/out attendance; authorized-pickup custody machinery; rooms with capacity/ratio (center segment); daily documentation to guardians; recurring tuition billing with autopay; family app/portal; staff assignment to rooms; multi-site support; roles separating admin/staff/parent.

---

## Abstraction Hierarchy

### L0 — Defining Invariant

Three structures. Remove any one and the software stops being recognizable as a childcare management system:

1. **Enrolled child bound to a guardian/family account.** The child is the cared-for person and the operator's central record; the guardian/family account is the contracting, paying, and communicating counterparty. Enrollment is ongoing (continuous care relationship), not a session or course booking. Without the child-guardian enrollment shape there is no care business to manage.
2. **Daily care attendance recorded as custody events.** Each care day is recorded through check-in and check-out performed by authorized adults — the custody handover that defines care delivery (who dropped off, who is authorized to pick up, when the child left). Without it the system cannot answer "which children are in care right now," and the licensing/billing/ratio machinery built on attendance collapses.
3. **Care-day documentation shared with guardians.** The operator records what happened during the care day (meals, naps, diapering, activities, photos, notes, incidents) and shares it with the child's guardians. This loop — the operator holds the child during the day and hands back both the child and an account of the day — is the defining communication structure of care; it exists in paper form (daily sheets) predating software, appears in every sampled product, and is the primary family-facing surface.

Historical/market-sample check (§24 reasoning): the definition is written without rooms, ratios, phone apps, or cloud deployment. Procare's desktop-era product (cardswipe/fingerprint check-in stations, log sheets) and its in-home tier (no classroom management) both fit; a home-based family childcare provider with no rooms fits; the paper-era daily-sheet practice fits. Nothing in L0 depends on one era, region, or vendor pattern.

### L1 — Common Mature Structure

Standard capabilities that mature products commonly add to make the core loop workable (cross-product, Layer B):

- **Rooms/classrooms with capacity and ratio settings** — children and staff assigned to rooms; room transfers; capacity limits; desired staff-to-child ratio per room; real-time ratio checks and out-of-ratio alerts; ratio reporting for licensing. (Absent in home-based deployments — segment-dependent, hence not L0.)
- **Custody machinery around attendance** — authorized-pickup lists per child, contact types (parent/family/approved pickup/emergency), check-in codes or signatures, deny-entry controls, health screening at drop-off.
- **Tuition billing and family ledger** — recurring billing plans/contract billing (weekly/monthly frequencies), attendance- or schedule-based billing formulas, drop-in billing, deposits, discounts/sibling discounts, late-payment handling, autopay against authorized methods, split payers, statements and year-end tax statements.
- **Third-party / subsidy money** — agency or third-party payer billing (subsidy co-pays, agency payment posting, adjustment codes) and/or state-system reporting integrations; food-program (CACFP-style) meal counting and reimbursement reporting. Regional depth varies.
- **Enrollment pipeline machinery** — leads, tours, applications, waitlists, admissions packets (forms, contracts, handbooks, fees), enrollment statuses with history retained for licensing.
- **Health & safety records** — immunizations and requirements, medications, incident logging, health checks.
- **Meal tracking** — menus, meal counts by age group, food-program reporting.
- **Staff management** — staff records, room assignment, staff schedules, time cards, staff-to-child ratio visibility; roles/permissions separating administrators, (lead) teachers, and family contacts.
- **Family engagement surfaces** — parent app/portal, messaging, photos/videos, newsletters, calendars.
- **Learning & development documentation** — observations against state standards/learning frameworks, milestones, assessments, lesson plans/curriculum (depth varies widely; some products bundle curriculum content).
- **Reporting** — attendance, ratios, enrollment, revenue; records retention framed for licensing.
- **Multi-site management** — multiple locations under one organization with consolidated oversight.

### L2 — Variant / Optional Structure

- **Segment posture**: daycare centers; preschools (learning emphasis); Montessori/private; faith-based; Head Start and state-funded programs (deeper compliance/reporting); home-based family childcare (no rooms; lighter everything); before/after-school programs run by care operators (borrowed from the sibling Type).
- **Philosophy poles**: engagement/documentation-first (app-first, family experience as the product) vs business/back-office-first (billing, staffing, profitability as the product).
- **Suite depth**: integrated payment processing; payroll; general ledger/bookkeeping; CRM/marketing and lead tracking; educator LMS/professional development; curriculum marketplace; hardware (kiosks, cardswipe, fingerprint readers, tablets).
- **Deployment**: cloud SaaS app-first vs legacy desktop with local check-in stations; hybrid (desktop + cloud platforms from one vendor).
- **Regional/regulatory shape**: US state subsidy portals and food-program reporting; state licensing ratio regimes; quality-rating systems (QRIS). Sample is North American.
- **Customer scale**: single independent center; in-home provider (low-cost tier); multi-site/franchise group; school district Pre-K programs.

### L3 — Vendor-specific (research notes only)

- brightwheel: 4-digit check-in codes; Quick Scan QR; Attendance Mode; Room Device Mode; Room Feed approval; contact-type model (Parent/Family/Approved Pickup/Emergency); enrollment-status vocabulary (Prospect/Toured/Applied/Waitlist/Enrolled/Active/Graduated/Inactive/Removed/Duplicate); Experience Curriculum; Premium feature gating; Tap to Pay; state integrations (Indiana I-LEAD, Minnesota DCYF, KinderConnect, Iowa, Kentucky, My Food Program); "15 minutes to onboard" and satisfaction-percentage marketing claims.
- Procare: Tucker AI assistant; Tuition Express payment processing; RoomRunner (AI enrollment planning); ChildPlus (Head Start); SchoolCare Works platform; Mini Procare (60-family limit); billing formula builder/withholding builder; agency adjustment codes; KidKare/Checkr/Gusto/QuickBooks/IntelliKid/Listen360 partnerships; in-home tier at a flat low monthly price; "40,000+ centers" / "10M+ app downloads" / "70% of largest for-profit orgs" claims; three-platform split (Desktop/Online/SchoolCare Works).
- Kangarootime: Business/School/Connect/Educator suite naming; KT Connect parent app; Training by Kangarootime (CypherWorx LMS); "two centers or twenty" multi-location positioning.
- Smartcare/RevTrak: Vanco payment rails; white-glove client-adoption specialist model; "hundreds of thousands of parents" claim.
- Lillio: Funshine Express curriculum; Lillio Academy CEUs; "2.1B moments shared" / "35,000+ customers" claims; HiMama heritage branding.

---

## Vendor-specific Findings

None promoted to the canonical model. Two over-generalization risks were checked and kept out of L0:

- **Rooms/classrooms** are the most visually distinctive childcare structure, but Procare's in-home tier explicitly excludes classroom management and home-based providers are a named segment for Procare and Lillio — rooms are segment-dependent (L1), not definitional.
- **Ratio tracking** is highly characteristic and licensing-driven, but it presupposes rooms/staff structures and regulatory regimes that vary by jurisdiction; it is standard machinery (L1), not the invariant. The custody handover (L0 #2) is the care-specific part of the same attendance event.

## Rejected Findings

- "Childcare management = daycare + preschool + after-school + camp in one product" — rejected as a definition; vendors do span segments (Procare, Kangarootime, Smartcare all sell sibling solutions), but the directory treats these as sibling Types distinguished by care context and schedule shape.
- "Camera/video monitoring is part of childcare management" — not directly evidenced in any fetched source; not asserted.
- "Payroll is part of the Type" — only some products (Procare Desktop full payroll; Kangarootime staff scheduling/timesheets); classified L2 suite depth.

---

## Boundary Findings

1. **vs After-school Program Management (§29 sibling; JOINT REVIEW DISCHARGED)**: the two Types share the entire family-enrollment-attendance-billing spine. The difference is the **care context**: childcare is full-day, year-round, licensed care whose daily loop is custody handover + care-day documentation, organized (in centers) by rooms and ratios; after-school programs are scheduled part-day offerings around the school day, run from session rosters. Direct evidence that the market treats them as sibling segments of single vendors: Procare sells a dedicated "Before and After School Programs" solution alongside its child care solution; Kangarootime ships a separate "Before and After School Management" solution; Smartcare lists "Before & After Care" as a segment of the same product. Removal tests: remove rooms/ratios/custody/daily-care documentation and keep scheduled session programs → after-school program management; remove scheduled sessions and keep full-day custody care → childcare management. Conclusion: **related Types sharing a core, not duplicates — both leaves stand**; each documents the seam from its own side. The after-school pass's flag is discharged.
2. **vs Daycare / Preschool Management (§29 sibling, unprocessed)**: **probable alias / segment-slice.** No sampled vendor maintains a distinct "daycare management" or "preschool management" product category separate from childcare management: Procare's one product line addresses "daycare, preschool, Head Start or ECE center"; Smartcare presents "Childcare & Daycare Centers" and "Preschool & Early Childhood Programs" as segments of one product; Kangarootime's childcare customers include preschools; Lillio addresses preschools and daycares interchangeably. Preschool deployments emphasize the learning/curriculum layer; daycare deployments emphasize care logistics — a segment emphasis inside one Type, not a separate Type. Recommend joint review when daycare-preschool-management is processed; likely outcomes: alias consolidation or explicit segment-variant note.
3. **vs Camp Management System (§29 sibling, processed)**: year-round ongoing care vs seasonal consecutive-day sessions; camp products carry session rosters, bunks, health centers, seasonal staff; childcare carries custody attendance, rooms/ratios, ongoing enrollment. Consistent with the seam recorded by the camp pass ("gradient on the care/licensing overlay, not a wall" — vendors span both).
4. **vs Babysitting Marketplace (§29 sibling, processed)**: operator-side administration of a care business vs two-sided consumer matching between families and individual caregivers. Completely different primary users; consistent with the seam recorded by the marketplace pass.
5. **vs Student Information System / School Management System (§23)**: the childcare operator is not the child's school of record — no grades, transcripts, or academic promotion; the objects of record are care enrollment, custody attendance, care-day documentation, and tuition. (School-age care programs bridge toward the school world but the care business remains the center.)
6. **vs Parenting / Baby Tracking Application (§29 sibling)**: the consumer-side baby tracker shares the "log the day" surface (feeds, naps, diapers) but has no enrollment, no custody counterparty, no staff, no billing — a personal journal vs an operator's business system. The daily-documentation loop appears in both, which is why L0 #3 is framed as the *operator's* record shared with guardians.
7. **vs Appointment-based Service Business Management (§29 sibling)**: drop-in care exists (Procare drop-in billing/enrollment), but the defining enrollment shape is an ongoing care relationship, not a bookable appointment; appointment machinery is not the center.
8. **vs Household Staff Management (§29 sibling)**: a family employing a nanny manages an employee; a childcare operator manages a licensed care business serving many families. Different record centers (employment vs enrollment). (Inference from segment structure; no direct product evidence fetched — kept as directional.)

"去掉什么就变成另一个 Type" summary: remove the care context (custody handover + care-day documentation + ongoing full-day enrollment) and keep scheduled part-day sessions → after-school program management; make sessions seasonal and consecutive-day → camp management; move matching to the consumer side with caregiver profiles → babysitting marketplace; remove the operator entirely and keep a family logging their own child's day → parenting/baby tracking; remove children/care and keep staff scheduling + billing for a generic service business → appointment-based service business management.

---

## Uncertainties

- **Lillio structure**: support center and legacy help center both JS-gated; Lillio's inclusion in cross-product claims rests on positioning pages plus the fact that it is repeatedly named as a comparable by Procare ("vs Lillio" competitive guide). Claims about Lillio internals are avoided.
- **Smartcare depth**: only the RevTrak product page was reachable; operational detail (statuses, ratio machinery, custody controls) is inferred from feature names and kept generic.
- **Regional scope**: sample is North American. Other markets (UK nursery management, Australian CCMS/childcare subsidy systems, German Kita software) were not sampled; the L0 is written implementation-neutral, but regional regulatory overlays (e.g., national subsidy schemes) are unverified and likely add L2 variants.
- **Waitlist/capacity behavior specifics** (invitation vs open racing when a seat opens) were not directly evidenced in fetched pages for this Type; kept generic.
- **Camera/streaming integrations**: often associated with childcare in the market but not evidenced here; not asserted anywhere.
- **Home-based provider tooling depth**: Procare's in-home tier and Lillio's Home Daycare segment confirm the segment exists, but its full feature shape was not documented in reachable sources.

---

## Final Synthesis

A Childcare Management System is operator-side software for running a child care business — daycare centers, preschools, home-based family childcare, and related early-childhood programs. Its defining structure is small: an enrolled child bound to a guardian/family account under an ongoing (non-session) care enrollment; daily care attendance recorded as custody events (check-in/check-out by authorized adults, with authorized-pickup controls); and care-day documentation shared with guardians (meals, naps, diapering, activities, photos, notes, incidents). Around that core, mature products add the machinery a licensed care business runs on: rooms/classrooms with capacity and staff-to-child ratio monitoring (absent in home-based deployments), tuition billing with recurring plans and family ledgers, third-party/subsidy money handling, enrollment pipelines with waitlists and admissions paperwork, health/immunization/incident records, meal and food-program tracking, staff records and scheduling, family engagement apps, learning documentation, reporting framed for licensing, and multi-site management. The Type shares its enrollment spine with after-school program management (joint review discharged: sibling Types split by care context, with vendors shipping both as sibling solutions), is probably aliased with the unprocessed daycare/preschool-management leaf (flagged for joint review), and is entirely distinct from the two-sided babysitting marketplace and the consumer-side baby tracker.
