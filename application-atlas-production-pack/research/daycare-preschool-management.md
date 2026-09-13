# Research Notes — Daycare / Preschool Management

Slug: daycare-preschool-management
Directory location: §29 Home, Family, Personal & Local Services (siblings: Childcare Management System, After-school Program Management, Camp Management System, Babysitting Marketplace)
Research date: 2026-09-07

This pass carries the **joint-review obligation** recorded by the childcare-management-system pass (its Boundary Findings #2: "probable alias / segment-slice … joint review recommended when daycare-preschool-management is processed"). This pass IS that joint review; the outcome is recorded in Boundary Findings #1 and flagged in STATUS.md. The after-school pass's related flag (childcare-management-system vs daycare-preschool-management) was already discharged from the childcare side; this pass closes the remaining seam.

---

## Research Goal

Process the directory leaf "Daycare / Preschool Management" and answer the flagged taxonomy question: is this a distinct Application Type (software specifically for daycare centers and/or preschools, structurally different from a childcare management system), or an alias / segment-slice of the childcare-management family? If distinct, model the distinct structure; if aliased, document the leaf from its own lens and record the directory issue.

## Initial Boundary (working hypothesis before research)

- Daycare = full-day, year-round, licensed custody care for young children; preschool = an early-childhood education program (learning/curriculum emphasis) for pre-kindergarten ages. Both are operator-side businesses.
- Prior sibling evidence suggests both segments are served by the same products sold as "childcare management software."
- Alternative hypotheses to falsify: (a) a distinct daycare-only category without learning tooling; (b) a distinct preschool-management category with school-like structures (academic-year sessions, school-of-record semantics, grades); (c) regional categories (UK "nursery management", "childminder" software; kindergarten; Kita) that might diverge structurally.

## Research Questions

1. Do vendors maintain "daycare management" and "preschool management" as distinct product categories, or as segment labels on one product?
2. When one vendor uses all three labels (childcare / daycare / preschool), is it the same product? What differs between the segment surfaces?
3. Does a preschool deployment differ structurally from a daycare deployment — objects, workflows, rules — or only in emphasis (care logistics vs learning layer)?
4. How do regional naming families map onto the same structure (UK nursery/childminder; kindergarten)?
5. Does the childcare-management defining core (enrolled child + guardian account under ongoing care enrollment; daily custody attendance; care-day documentation shared with guardians) hold against fresh, un-reused samples?
6. Is there any product population answering to "daycare management" or "preschool management" that does NOT carry that core?

## Representative Products

| Product | Segment posture | Philosophy | Customer tier | Evidence strength |
|---|---|---|---|---|
| brightwheel | US modern platform; uniquely informative for this review — runs parallel "childcare management" and "preschool management" segment pages selling one product | engagement/app-first | SMB centers + preschools + in-home + multisite | Strong (Tier-2 ×2 fresh this pass; Tier-1 help center ×7 in sibling pass) |
| Famly | UK/EU regional pole — sells the same family as "nursery management software" with a childminder segment | parent-partnership + daily-logs first | single nurseries → nursery groups; childminders | Medium (Tier-2 root fresh; help centre not fetched) |
| illumine | international pole (US/SG/AE/IN); one product carrying childcare/daycare/preschool labels simultaneously; AI-heavy posture | AI-assisted operations + learning records | single centers → enterprise multi-center | Medium (Tier-2 root fresh; help center not fetched) |
| Procare Solutions / Smartcare / Kangarootime / Lillio | corroborating sample from the same-day sibling pass (childcare-management-system) | — | — | A in sibling notes; reused here at B-level |

Sample rationale: three fresh vendors chosen for label-architecture evidence (parallel segment pages), regional naming (UK), and international multi-label positioning; the sibling pass's five products corroborate without being re-fetched.

## Sources

Fresh fetches (2026-09-07):

- brightwheel root — https://mybrightwheel.com/ (Tier-2)
- brightwheel preschool segment page — https://mybrightwheel.com/preschools/ (Tier-2)
- Famly root (UK) — https://www.famly.co/ (Tier-2)
- illumine root — https://illumine.app/ (Tier-2, incl. embedded FAQ/structured-data markup)

Reused (same day, from research/childcare-management-system.md — not re-fetched):

- brightwheel Help Center (Tier-1 ×7), Procare Solutions root + Classroom Management page + Procare Support (Tier-1 support index + "Child Pickup" article), Kangarootime root + CCMS solution page, Smartcare/RevTrak child-care page, Lillio root + feature pages

Not fetched / unreachable:

- Famly help centre (help.famly.co) — not attempted for this pass (the alias question did not require it); Famly claims kept at root-page module level
- illumine help center — not attempted; same calibration
- Lillio support center — JS-gated (recorded in sibling pass)

---

## Product A — brightwheel (fresh fetches)

### Key observations (evidence layer A)

- Root page headline: "The Best Childcare Management Software" / "#1 childcare management software"; body section: "Your complete preschool & childcare management system" — one platform. (A)
- "Who we serve" navigation lists segments of one product: Preschools ("You own or manage a preschool with an educational program"), Childcare centers ("You provide care for children including supervision, feeding, and naps"), Multisite centers, In-home child care, Camps & afterschool programs, Montessori, Government & network partners. (A)
- One product's feature groups: Billing & finances (billing & payments, childcare invoice, receipts, expense management); Staff & family management (communication, daily report, staff scheduling, classroom management, payroll, mobile app, professional development); Learning & curriculum (curriculum & assessment, lesson plans, daily schedules, progress report); Site management (enrollment & admissions, center management, attendance & check-in, childcare forms, menus CACFP, daily health checks). (A)
- Preschool segment page: H1 "#1 preschool management software"; "Simplify your preschool operations with brightwheel's all-in-one preschool management software"; enumerated features: centralized attendance (digital check-in/out, real-time per class, attendance integrated with billing and payroll), family communication (daily updates, photos, SMS, newsletters), automated billing (recurring payments, invoices, autopay, reports), staff management (lesson planning, schedules), secure data management (child records, medical info, licensing documents), learning (curriculum, progress reports, standards alignment). (A)
- The same page's FAQ defines the category in one breath: "Preschool management software is a digital platform designed to help early education programs streamline administrative tasks like attendance tracking, billing and invoicing, family and staff communication, lesson planning, and reporting." (A)
- Cross-label self-identification: the preschool page invites switching "from other childcare management software" and describes "preschool management software that streamlines every part of your childcare program" — both labels on one product. (A)
- Vendor claims (kept as claims, not asserted): 160,000+ reviews at 4.9; 20 hrs/month saved; 95% satisfaction; 99.9% uptime; pricing based on enrollment capacity; PCI Level 1. (A-as-claims)

## Product B — Famly (fresh fetch)

### Key observations (evidence layer A unless noted)

- Positioning: "The Early Childhood Platform for every size Nurseries"; "The nursery app that does everything for you." UK primary site with US/German/Danish variants behind language flags. (A)
- Platform modules (root page): Parent partnerships (instant messages, observations, updates); Child development (digital observations, assessments, unique curriculums); Daily logs (sleep times, nappy changes, medication, personal news feed); Occupancy & attendance (predict, manage, track enquiries and attendance); Efficient staffing (rotas, holidays, automatic ratios); Easy finances (in-app payments, funding & reconciliation). (A)
- Built-for roster: Owners, Managers, Nursery groups, Educators, Parents. (A)
- Regional naming architecture: a "nursery management software" solution page with Small nurseries / Larger nurseries / Nursery groups variants, plus a separate "Childminders" solution — the home-based provider segment under its UK name, on the same platform. (A)
- Regime markers: Ofsted-related guides ("SEND in the Early Years", Ofsted visits), "funding & reconciliation" wording (UK funding regimes); EYFS vocabulary appears only in site-generated helper text (B-level, not asserted). (A/B)
- Review sources span pre-schools, Montessori nurseries, day nurseries — the same buyer population under UK nouns. (A)

## Product C — illumine (fresh fetch)

### Key observations (evidence layer A)

- One product, all three labels: page title "All-In-One Childcare Management Software"; H1 "Top Childcare Management Software"; page keywords include "childcare management software, daycare software, preschool management, AI childcare software"; site self-description "childcare management software for modern daycare centers and preschools." (A)
- Single-category definition in its own FAQ markup: "Childcare management software is a digital platform that helps preschools, daycares, and childcare centers run daily operations, including attendance, billing, enrollment, parent communication, and learning records, from one system instead of juggling spreadsheets, paper forms, and separate apps." (A)
- Modules: Billing & Payments (automated invoices, credit/debit notes, discounts, subsidies, taxes, reminders, late fees, tax/financial reports); Enrollment Management (inquiry capture, tours, waitlists, marketing campaigns, childcare CRM); Daily Attendance (QR ID cards, kiosk codes, leaves/time-offs, student-staff ratios, late check-out/early check-in fees, geofencing, e-signatures); Parent Communication (AI daily reports, media/messages with real-time translation, drop-off/pick-up/medical requests, newsletters, surveys, consent forms); Learning & Assessments (observations, learning journals, progress reports, curriculum-framework integration, personalized lesson plans). (A — vendor pages)
- Enterprise tier: multi-center batch operations, group-level dashboards, dedicated "enterprise childcare management" page. (A)
- Customer geography/testimonials: US Montessori group, Kuwait Reggio center, Malaysia kindergarten ("Amazing Kindergarten"), Nordic group — kindergarten appears as the regional segment name. (A — testimonials)
- Vendor claims (kept as claims): 3,000+ centers; 500,000+ children; founded 2015; monthly plan tiers; AI enrollment agent answering parent calls around the clock; facial-recognition check-in (structured-data claim, not verified in product documentation); NPS/retention figures. (A-as-claims)

## Product D — corroborating sample from the sibling pass (B-level here; A in childcare-management-system notes)

- Procare Solutions: one product line positioned for "daycare, preschool, Head Start or ECE center"; solutions map (Child Care Centers, Head Start Grantees, Before and After School Programs, Youth Organizations) with sub-segments (Franchises, In-Home Daycare, Multi-Centers, School Districts, YMCA, Shared Services); support index documents the full module set (family/child data, contract/formula/drop-in billing, agency accounting, attendance tracker with custody controls, meal tracker, employee data/payroll, general ledger). (B here)
- Smartcare/RevTrak: "Childcare & Daycare Centers" and "Preschool & Early Childhood Programs" presented as two segment blocks of one product, alongside Before & After Care, Private Schools (Montessori/K-12), Faith-based, and Districts Pre-K. (B here)
- Kangarootime: "All-in-One CCMS" with preschool customers; separate Before/After School solution. (B here)
- Lillio: "Childcare Management Software" with a Home Daycare user segment; curriculum + billing + professional-development extensions (positioning-level). (B here)

---

## Cross-product Comparison

### Label architecture (the joint-review core question)

| Product | "childcare management" | "daycare" | "preschool" | Distinct product for daycare or preschool? |
|---|---|---|---|---|
| brightwheel | "#1 childcare management software" (root H1) | daycare in business-plan content and customer types | "#1 preschool management software" (segment-page H1); "preschool & childcare management system" | No — one product; parallel segment pages |
| Famly | "early childhood platform" | (US variant uses childcare vocabulary) | "nursery" is the UK primary noun for the same segment | No — nursery management software = same platform; childminder = home-based segment |
| illumine | primary label (root H1) | "daycare software" keyword + "daycare centers" copy | "preschool management" keyword; "Loved by Preschools Across the Globe" | No — all labels on one product page |
| Procare | "Child Care Management Software" | "daycare" throughout (in-home daycare tier, bookkeeping) | "preschool" inside the one-product positioning sentence | No |
| Smartcare | "childcare program" | "Childcare & Daycare Centers" segment | "Preschool & Early Childhood Programs" segment | No — two segments, one product |
| Kangarootime | "CCMS" | childcare customers | preschool customers | No |
| Lillio | "Childcare Management Software" | Home Daycare segment | preschool/early-childhood framing | No |

Zero sampled vendors maintain a distinct daycare-management or preschool-management product; all seven place the labels on one product, mostly as parallel landing/segment surfaces.

### Structure comparison (fresh samples vs the sibling pass's core)

| Dimension | brightwheel | Famly | illumine | Sibling-pass core |
|---|---|---|---|---|
| Central record | child/student under family contacts | child records under nursery; parents alongside | child enrollment under center | enrolled child bound to guardian/family account |
| Enrollment shape | ongoing; admissions pipeline (prospects/tours/waitlists) | occupancy & enquiries; waitlists implied by occupancy module | inquiry→tour→waitlist→admission CRM | ongoing care enrollment + pipeline |
| Daily attendance | digital check-in/out, real-time per class, feeds billing & payroll | attendance + occupancy | QR/kiosk, ratios, late/early fees | custody check-in/out events |
| Custody machinery | approved pickups/codes/signatures (documented in sibling Tier-1 notes) | pickup handling not on root page (unverified) | geofencing, e-signatures (claim-level) | authorized adults, custody handover |
| Daily documentation | daily reports; activity logs | daily logs (sleep, nappy, medication) + personal news feed | AI daily reports, media | care-day documentation shared with guardians |
| Rooms/ratios | classroom management; ratio tracking | automatic ratios with rotas | student-staff ratios | rooms + capacity + ratio (center segment) |
| Tuition billing | recurring billing, autopay, invoices | in-app payments, funding & reconciliation | invoices, subsidies, late fees, tax reports | recurring + attendance/drop-in + subsidy money |
| Learning layer | curriculum & assessment, lesson plans, progress reports | observations, assessments, curriculums | observations, journals, frameworks, lesson plans | learning documentation (depth varies; preschool emphasis) |
| Health/safety | daily health checks; forms | medication logging | medical requests | health & safety records |
| Multi-site | multisite segment | nursery groups | enterprise multi-center | multi-site management |

The fresh samples reproduce the sibling core item for item; no dimension differs by segment label.

### Historical / regional check

- UK: Famly sells the same structure as "nursery management software" with a childminder (home-based) segment — regional naming over the same objects (daily logs, ratios, rotas, funding).
- Kindergarten (Malaysia testimonial at illumine) — same product.
- Desktop-era and paper-era practice (Procare desktop, card-swipe stations, paper daily sheets — sibling pass) satisfies the core; nothing in the core depends on mobile apps or cloud delivery.
- Conclusion: the core survives the historical/regional check; naming (daycare / preschool / nursery / childminder / kindergarten) is regional and segment vocabulary over one Type.

---

## Abstraction Hierarchy

### L0 — Defining Invariant

The joint review confirms the leaf resolves to the same defining core as Childcare Management System; the daycare/preschool framing adds no fourth structure:

1. **Enrolled child bound to a guardian/family account** under an ongoing (non-session) care enrollment — the child is the cared-for record; the guardian account is the contracting, paying, communicating counterparty.
2. **Daily care attendance recorded as custody events** — check-in/check-out by authorized adults; answers "which children are in care right now, and with whom may they leave."
3. **Care-day documentation shared with guardians** — meals, naps, toileting, activities, photos, notes, incidents recorded by the operator and handed back with the child.

Falsification attempts:

- "Preschool adds a school-of-record structure (grades, transcripts, academic promotion, annual registration)" — rejected: no sampled product carries those semantics in its preschool segment; the learning layer is observations/progress documentation, and enrollment remains ongoing care enrollment.
- "Daycare removes the learning structure" — rejected: learning/curriculum tooling is sold across the whole base (brightwheel's learning feature group on the general product; illumine's observations module; Famly's child-development module), not gated to preschool segments.

Hence: same L0 as the sibling leaf; "daycare" and "preschool" are emphasis poles, not structural variants.

### L1 — Common Mature Structure (unchanged from the sibling core; re-corroborated by fresh samples)

Rooms/classrooms with capacity + staff-to-child ratio monitoring; custody machinery (authorized-pickup lists, contact types, codes/signatures, deny-entry); tuition billing with recurring/attendance/drop-in models + family ledger; third-party/subsidy money (agency billing, co-pays, state reporting; UK "funding"); enrollment pipeline (leads, tours, waitlists, admissions packets, status lifecycle with licensing retention); health & safety records (immunizations, medications, incidents, health checks); meals & food-program tracking; staff records/scheduling/time cards; family engagement app/portal; learning documentation (observations, assessments, curriculum, progress reports); reporting framed for licensing; multi-site management.

### L2 — Variant / Optional Structure

- **Segment emphasis** — daycare center (care-logistics center of gravity: meals/naps/diapering/ratios) vs preschool/early-education program (learning emphasis: curriculum, observations, progress reports) — a deployment continuum, not two Types.
- **Regional naming + regime overlays** — UK nursery/childminder (rotas, funding reconciliation, Ofsted/EYFS framing); kindergarten; (unsampled: German Kita, Nordic, Australian CCMS, Japanese regimes — expected to add regulatory overlays only).
- **Program-type overlays** — Montessori, faith-based, state-funded/Head Start (deeper compliance/reporting), in-home/home-based (rooms drop away).
- **Suite depth** — payments, payroll, GL/bookkeeping, CRM/marketing, educator LMS/PD, curriculum marketplace, hardware (kiosks, card readers), AI assistance.
- **Deployment** — cloud SaaS app-first vs legacy desktop with check-in stations.
- **Customer scale** — single independent center / in-home provider / multi-site group / district Pre-K.

### L3 — Vendor-specific (research notes only)

- brightwheel: parallel segment-page architecture (root "#1 childcare" vs preschool "#1 preschool") selling one product; pricing posture tied to enrollment capacity; Experience Curriculum add-on; PCI Level 1 claim; review-count claims; savings-calculator marketing.
- Famly: rota + automatic-ratio module; occupancy & enquiry tracking module; funding & reconciliation; Famly Insights; public API (docs.famly.co); community/podcast content marketing; country variants (UK/US/DE/DA); Ofsted/EYFS content marketing.
- illumine: AI enrollment agent (call answering); AI daily reports; real-time translation (20+ languages claim); geofencing and facial-recognition check-in claims; QR ID cards; late check-out/early check-in fees; structured-data pricing tiers (claims); multi-country presence (US/SG/AE/IN).
- Procare/Smartcare/Kangarootime/Lillio specifics: see sibling research notes.

## Vendor-specific Findings

None promoted to canonical structure. Two over-generalization risks checked:

- **Parallel landing-page architecture** (a childcare page and a preschool page for the same product) is vendor marketing architecture, not category structure — but it is the strongest direct evidence FOR the alias finding.
- **"Preschool = school-year sessions"** — a tempting hypothesis; not supported. Sampled preschool deployments retain ongoing enrollment, custody attendance, and daily documentation; some preschools run school-year calendars (a scheduling configuration), but no sampled product makes session structure the preschool defining shape.

## Rejected Findings

- "Daycare / Preschool Management is a distinct Type from Childcare Management System" — rejected on cross-vendor label architecture (brightwheel, illumine, Procare, Smartcare, Kangarootime, Lillio, Famly) + structural identity.
- "Preschool management is the early-education subset with different objects (classes/grades/semesters)" — rejected: no school-of-record semantics observed; learning documentation is the only preschool-leaning structure, and it exists across the whole base at varying depth.
- "Daycare management is care-only" — rejected: learning tooling ships to the full base.
- "Nursery management (UK) is a separate Type" — rejected: regional naming of the same structure (Famly).

## Boundary Findings

1. **vs Childcare Management System (§29 sibling, processed) — ALIAS / SEGMENT-SLICE CONFIRMED (this pass's joint-review outcome).** Evidence: (a) brightwheel runs "#1 childcare management software" and "#1 preschool management software" H1s on one product, and its preschool page cross-references "childcare management software" as the same category; (b) illumine places all three labels (childcare/daycare/preschool) on one product with a single FAQ definition covering "preschools, daycares, and childcare centers"; (c) Procare's one product line addresses "daycare, preschool, Head Start or ECE center"; Smartcare presents daycare and preschool as two segments of one product; Kangarootime/Lillio serve both interchangeably; (d) Famly shows the regional alias (nursery/childminder) mapping onto the same structure. No sampled vendor maintains a distinct category. Removal tests: from a preschool deployment remove the learning emphasis → childcare management; from a daycare deployment add learning emphasis → preschool; nothing structural remains to separate them. Conclusion: **one market family behind two directory names**; "Daycare / Preschool Management" names the two flagship segments, "Childcare Management System" names the business type. Both leaves' documents stand (each with its own lens, consistent with the digital-whiteboard/collaborative-canvas precedent); the merge/alias decision is escalated to directory review.
2. **vs After-school Program Management (§29 sibling, processed)** — sibling Types split by care context (full-day custody care + care-day documentation vs scheduled part-day session programs around the school day); vendors ship both as sibling solutions (brightwheel's nav lists "Camps & afterschool programs" as a separate segment page; Procare/Kangarootime/Smartcare ship sibling solutions). Consistent with both prior passes; both leaves stand.
3. **vs Camp Management System (§29 sibling, processed)** — seasonal consecutive-day sessions vs year-round ongoing care; brightwheel's nav placing "Camps & afterschool programs" in one segment page corroborates the gradient-on-care-overlay seam.
4. **vs Babysitting Marketplace (§29 sibling, processed)** — operator-side administration of a licensed care business vs two-sided consumer matching between families and individual caregivers; different primary users entirely.
5. **vs Student Information System / School Management System (§23)** — the preschool in this family is not the child's school of record: no grades, transcripts, or promotion; the objects of record are care enrollment, custody attendance, care-day documentation, learning observations, and tuition. (Smartcare lists Private Schools Montessori/K-12 as a separate segment — the seam where the school of record begins.)
6. **vs Parenting / Baby Tracking Application (§29 sibling)** — the consumer journal shares the "log the day" surface (sleep, feeding, nappies — Famly's daily-logs wording mirrors it) but has no enrollment, custody counterparty, staff, or billing.
7. **vs Lesson Planning Application (§23)** — the learning/curriculum layer inside these products serves the operator's program documentation; a dedicated lesson-planning Type is teacher authoring tooling, a different center of gravity.

"去掉什么就变成另一个 Type" summary: remove the care context (custody handover + care-day documentation + ongoing full-day enrollment) and keep scheduled part-day sessions → after-school program management; make sessions seasonal and consecutive-day → camp management; move matching to the consumer side with caregiver profiles → babysitting marketplace; remove the operator and keep a family logging their own child's day → parenting/baby tracking; remove care operations and keep only pedagogical authoring → lesson planning; and: rename to "childcare management" and nothing changes at all — that is the alias finding.

## Uncertainties

- **Famly/illumine depth**: only root/positioning pages fetched for this pass (help centers not attempted — the alias question did not require them); module structures are taken from official marketing pages (A for existence, weaker for behavior).
- **Regional regimes unsampled**: German Kita software, Nordic, Australian CCMS, Japanese childcare/kindergarten software not sampled; expected to be naming + regulatory overlays, unverified.
- **Preschool-only product population**: no product answering to "preschool management" WITHOUT the care/custody/billing core was found in this sample; if one exists (pure pedagogical administration), it would sit nearer Lesson Planning/SIS. Not asserted either way.
- **Lillio** remains positioning-level (inherited from sibling pass).
- Vendor volume/scale claims (40,000+ centers, 3,000+ centers, review counts, uptime) recorded as claims only.

## Final Synthesis

"Daycare / Preschool Management" is not a distinct Application Type: it is the same market family as Childcare Management System, named by its two flagship segments. Fresh cross-vendor evidence (brightwheel's parallel segment pages for one product; illumine carrying all three labels on one product with a single definition; Procare/Smartcare/Kangarootime/Lillio segment maps; Famly's regional nursery/childminder naming) confirms that no vendor maintains a separate daycare-management or preschool-management category, and that the defining core — enrolled child bound to a guardian account under ongoing care enrollment, daily custody attendance, care-day documentation shared with guardians — is identical across daycare and preschool deployments, with the learning layer as a depth dial rather than a boundary. The leaf's application document describes this family from the daycare/preschool program lens; the alias is recorded in STATUS.md for a directory-level decision.
