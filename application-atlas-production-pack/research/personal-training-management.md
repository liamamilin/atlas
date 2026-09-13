# Research Notes — Personal Training Management

Directory leaf: Personal Training Management (§28 Sports, Fitness & Recreation)
Slug: personal-training-management
Research date: 2026-09-10
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what a "Personal Training Management" application actually is as an Application Type: what the trainer-side (or training-business-side) software holds, what the core operating loop is, and where its boundary lies against the neighboring §28 types that have already been processed — Online Fitness Coaching, Workout Programming Application, Sports Coaching Platform, Nutrition Coaching Platform, Fitness Studio Management, Fitness Assessment Application, Fitness Progress Tracker, AI Fitness Coach, Gym Management System — plus Coaching Commerce Platform (§27). This pass must discharge nine pre-hung sibling flags (recorded in STATUS.md).

## Initial Boundary (hypothesis before research)

- Hypothesis: Personal Training Management centers the personal trainer's *business operations* around in-person (and hybrid) training sessions: client records, appointment/session scheduling, session packages, billing, trainer/staff management — with program delivery, assessments, and nutrition as attached modules. The software container is the calendar/ledger, not the remote coaching loop.
- Nearest neighbors and pre-hung flags to discharge:
  - **Online Fitness Coaching** (processed 2026-09-08) — sharpest seam; proposed discriminator: appointment-centered business ops vs relationship-centered remote coaching loop; "who holds the engagement in-system" test proposed.
  - **Sports Coaching Platform** (processed 2026-09-09) — probable vertical sibling, same practice spine (client roster + sessions + money + delivery); proposed discriminator = domain center of gravity (sports skill instruction vs fitness training); family treatment possible.
  - **Nutrition Coaching Platform** (processed 2026-09-08) — managed-prescription-subject test (which prescription is the managed center).
  - **Fitness Assessment Application** (processed 2026-09-07) — module-carries-core vs platform-centers-business-relationship test (Exercise.com/PT Distinction pattern named by that pass).
  - **Fitness Studio Management** (processed 2026-09-08) — appointment-led vs class-led center-of-gravity seam (studio suites carry appointments as a secondary booking type).
  - **Workout Programming Application** (processed 2026-09-09) — "center appointments/packages/billing → Personal Training Management" removal test recorded by that pass.
  - **Coaching Commerce Platform** (§27, processed) — selling the engagement vs running it.
  - **Fitness Progress Tracker** (processed) — self-record vs relationship record.
  - **AI Fitness Coach** (processed) — who-adapts test.
- Unknowns: Is the session-credit economy (packages/memberships) definitional or common? Is the trainer/staff layer definitional or does the solo trainer satisfy the core? How do the two market poles (appointment-led business systems vs remote-coaching suites sold under the same "personal training software" label) resolve?

## Research Questions

1. What objects does the trainer side hold? (clients, services/session types, appointments/sessions, packages, memberships, payments, trainers/staff, locations, programs, assessments)
2. What is the core operating loop, from client acquisition to session completion and payment?
3. How do sessions and money interact — per-session payment vs package/membership credits? What rules govern credits (expiry, carryover, modification)?
4. What is the session lifecycle after booking (attended / missed / cancelled / rescheduled — the "reconciling" concept)?
5. What staff/multi-trainer structures exist, and is the solo trainer a full citizen?
6. What client-facing surfaces exist (booking portal, client app)?
7. Where do program delivery / workout logging / assessments / nutrition sit — module or center?
8. Where are the boundaries vs the nine neighbor types listed above?
9. Historical check: does the paper-era implementation (appointment book + prepaid session card + cash) satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different customer tiers. The sample deliberately spans the two poles the market blends under one label:

| Product | Pole | Why sampled |
|---|---|---|
| **PTminder** | classic appointment-led PT business system (lean, trainer-centric) | the canonical "personal training software" shape: bookings + payments + packages + clients; Tier-1 help center |
| **Vagaro** | multi-vertical appointment-business platform (salons/spas/fitness incl. personal trainers) | shows the appointment-business family machinery the PT pole shares; Tier-1 help center |
| **Exercise.com** | full-suite white-label fitness-business platform (Personal Trainer as one industry solution) | the suite-absorbs-PT pole; Tier-2 product pages (support portal login-gated) |
| **PT Distinction** | automation-heavy remote-coaching suite sold as "personal trainer software" | documents the label-span: coaching-loop machinery under the PT label; Tier-2 product pages (help center unreachable) |
| **TrainerFu** | mobile-first coaching-loop app sold as "personal trainer software" | second label-span pole, app-first philosophy; Tier-2 product pages |

## Sources

Tier 1 (official operational documentation):
- PTminder Help Center — https://help.ptminder.com/en/ — root TOC (collections: General; Calendar & Bookings; Clients; Services; Finances; Reporting; Settings; Mobile Apps; Billing & Plans; Add-ons; Payment Integrations; Staff Management); articles fetched in full: "Packages explained", "Session Templates explained", "What is 'Reconciling' a past session/class all about?"; collection TOCs fetched: Calendar & Bookings (incl. Bookings & Scheduling + Reconciling sub-collections), Services (Packages/Memberships/Products/Service Categories/Session Templates/Class Templates/Direct Buy Links/Discount Codes), Clients (Client Management / Client Assessments / Workout Planner / Nutrition Planner / Messaging sub-collections)
- Vagaro Support — https://support.vagaro.com/hc/en-us — root TOC (categories: Getting Started; Checkout; Credit Card Processing; Business Settings; Email and Text Messaging; Employee Management; Payroll; Calendar and Scheduling; Things You Sell; Customer Management; Forms and SOAP Notes; Reports and Dashboard; Check-in App; …); "Things You Sell" category TOC (Services and Service Bundles; Classes and Workshops; Gift Cards; Add-Ons; Memberships; Packages; Categories; Resources; Inventory); article fetched in full: "Difference Between a Package and a Membership"

Tier 2 (official product pages):
- Exercise.com — https://www.exercise.com/ platform feature nav (Business: Check-Ins, Booking, Member Management, Staff Management, Reports, Custom-Branded Apps, Multi-Location, E-Sign Waivers, Automations; Workout: Workout Plan Creator, Workout Logger, Exercise Library, Rep Max Progressions, Progress Photos, Habit Tracking; Marketing: CRM, Assessments, Leads, Email/SMS, Sales Funnels, Websites; Online: Online Training, Sell Workout Plans, Livestreaming, On-Demand, Memberships; Payments: Payment Processing, Trainer Commissions, Invoicing, Account Balances, POS); solution page https://www.exercise.com/solutions/personal-trainer/ ("Easily schedule appointments and classes, accept payments, create and log workouts, send reminders, capture assessments, track visits, and view business reports from your custom-branded personal trainer apps… train clients online and in-person")
- PT Distinction — https://www.ptdistinction.com/ (feature grid: Branded apps, Training programs, AI Program Generator, Nutritional coaching, AI Meal Planner, AI Assistant, Assessments, Groups, Communication, Automated workflows, Habits, Client results, Integrations, Pre-made templates, Sell packages and take payments, Scheduled messaging; positioning "personal trainer software… trusted by personal trainers, hybrid coaches")
- TrainerFu — https://www.trainerfu.com/ (feature sections: Workouts, Tracking, Engagement, Automation, Business, Sell, Custom App, Habit, Teams; "Simple Personal Trainer Software for In-Person and Online Training"; workout builder, workout delivery to client app, tracking, sell programs/packages, automatic messaging, community feed, branded app)

Source-access limitations:
- Exercise.com support portal (https://help.exercise.com/) is login-gated ("only available to registered users") — Exercise.com evidence held at product-page strength; no operational mechanics asserted from it.
- PT Distinction help center (https://help.ptdistinction.com/) returned a transport error once; per network rules the source was dropped. PTD evidence held at product-page strength.
- Vagaro was previously sampled at Tier-1 depth in the spa-management-system pass (2026-09-10); this pass adds the Packages/Memberships distinction article and reuses that pass's Tier-1 observations as cross-pass evidence (marked Layer B where so).
- Marketing figures (PTD "60,000 training businesses"; PTminder booking/payment counters; Exercise.com review badges) recorded here only, never asserted in the final document.

---

## Product observations

### PTminder (Tier 1: help center)

Evidence: A (direct observation of official help-center structure and full article texts).

- Root TOC collections: General; **Calendar & Bookings**; **Clients**; **Services**; **Finances**; Reporting; Settings; Mobile Apps; Billing & Plans; Add-ons; **Payment Integrations** (39 articles); **Staff Management**.
- **Services** collection: "Packages explained", "Memberships explained", "Products explained", "Service Categories", "Session Templates explained", "Class Templates explained", "Direct Buy Links to Store items", "Managing 'Discount Codes' for Packages, Memberships & Products".
  - Packages (full article): "a package is a set number of sessions and/or classes that are purchased in bulk… mainly used to allow clients to purchase multiple sessions/classes at once… also a way to provide a discounted rate"; any mixture of sessions and classes in one package.
  - Session Templates (full article): pre-defined session templates populate the booking form; if online session bookings are enabled, clients choose a session template when booking online; **"Assigned Trainers"** dropdown restricts which trainers a session template is bookable with.
- **Calendar & Bookings** collection: "Booking in Sessions and Classes", "Online Class Bookings", "'Available' and 'Unavailable' Time Windows", "Waiting Lists", Zoom/video-conferencing links in bookings; **Reconciling** sub-collection: "What is 'Reconciling' a past session/class all about?" (full text): "Reconciling a past session/class is used to confirm that the particular session has successfully taken place, who attended that session and who paid what… Once a session is in the past, you have to reconcile that session and confirm whether your client(s) have **attended, missed, cancelled or rescheduled** that session. You also have the option to record the client payment for that session or **deduct it from a package/membership** if the client has one assigned." Plus how-to and unreconcile articles.
- **Clients** collection (21 articles): Client Management (add/remove client, **Family Accounts**, custom client fields, client notes, **Assigning a Package to a client**, **Assigning a Membership**, change/skip membership payments and credits, **modify the number of credits for assigned Packages/Memberships**, "view how many sessions/classes have been **booked, completed or are left** for a particular client", view upcoming/past sessions, **"Carryover Unused Sessions/Classes" and "Expiring Credits"**); Client Assessments (recording client assessments); **Workout Planner** (build workout plans from 1200+ exercise videos, record/track workouts); **Nutrition Planner**; Messaging (chat, automatic SMS reminders, manual SMS).
- Product site (Tier 2): four headline capabilities — Online Training ("build and assign workout plans, nutrition plans and record workouts remotely"), Client Management ("bookings, payments and progress"), Online Bookings ("view your schedule, book and pay for their next appointment"), Accept Payments ("bookings, packages, memberships and products"); "Organize your schedule… Assessments for clients… Sell your PT services: packages, memberships and products… Workout planner… Reminders… Nutrition planning"; branded mobile apps; Stripe/Debitsuccess/GoCardless/Ezidebit/PayPal integrations.
- Reading: PTminder is the classic appointment-led realization. The center is the calendar/bookings + services + money loop; the workout/nutrition/assessment layers are clearly secondary modules inside the Clients collection.

### Vagaro (Tier 1: help center; plus prior Tier-1 evidence from the spa-management-system pass)

Evidence: A.

- Root TOC categories: Getting Started; **Checkout**; **Credit Card Processing**; MySite; Business Settings; Email and Text Messaging; **Employee Management**; **Payroll**; **Calendar and Scheduling**; **Things You Sell**; **Customer Management**; Hardware; **Forms and SOAP Notes**; Reports and Dashboard; Check-in App; Live Stream; etc.
- **Things You Sell**: Set Up Services and **Service Bundles**; Create **Classes and Workshops**; Gift Cards; **Add-Ons**; Create **Memberships**; Create **Packages**; Categories; **Resources** ("Add Resources to Services and Classes" — per the spa pass: "a Resource is a room, space, furniture, or tool"); Inventory.
  - "Difference Between a Package and a Membership" (full article): "A **package** is a pre-bundled set of specific services, classes, or products that customers use over time" — "Sell a set number of future visits for services and classes", auto-renew "based on time (days, months, years) or **number of completed visits**", "Carry unused visits forward to the next billing cycle", pausable. "A **membership** applies discounts across eligible services, classes, and products instead of selling one fixed bundle" — discount-based, time-based auto-renew only. Worked examples include a fitness center selling "three cardio sessions at a discounted price… renewed automatically based on a specific charge frequency."
- From the spa pass (Tier-1, 2026-09-10): appointment booking against service/provider/resource with double-booking prevention; checkout resolving the visit into recorded payment; client records with purchase history.
- Reading: Vagaro realizes the generic appointment-business machinery that the PT pole inherits — services/classes catalog, packages as prepaid visit bundles, memberships as discount instruments, appointments, checkout, employees. Vagaro serves personal trainers as one audience among salon/spa/fitness verticals; it documents the family shape from outside the fitness-specific label.

### Exercise.com (Tier 2: product pages; support portal login-gated)

Evidence: A for quoted product-page claims and the platform's own feature taxonomy; B-level for mechanics.

- Platform nav (official): **Business** (Check-Ins, Booking, Member Management, Staff Management, Reports, Custom-Branded Apps, Multi-Location, Remote Door Access, E-Sign Waivers/Contracts, Automations); **Workout** (Workout Plan Creator, Workout Logger, TV Workouts, Exercise Library, Rep Max Progressions, Supersets, Performance Reporting, Leaderboards, Progress Photos, Habit Tracking); **Marketing** (CRM, Assessments, Leads, Member Engagement, Email, SMS, Push Notifications, Sales Funnels, Websites); **Online** (Online Training, Sell Workout Plans, Livestreaming, Online Groups, On-Demand, Challenges, Digital Products, Landing Pages, Memberships); **Payments** (Payment Processing, ECommerce, **Trainer Commissions**, Invoicing, Account Balances, Coupon Codes, Payment Splitting, BNPL, POS); Other (Analytics, Managed Apps, Custom Dev).
- Personal Trainer solution page (official copy): "Easily schedule appointments and classes, accept payments, create and log workouts, send reminders, capture assessments, track visits, and view business reports from your custom-branded personal trainer apps… you can train clients online and in-person on the all-in-one fitness business management platform."
- Positioning: "the only true all-in-one software platform" for fitness businesses; Personal Trainer is one of 16 industry solutions (Gym, Box & Affiliate, Personal Trainer, Fitness Influencer, Boutique Fitness, Sports Performance, Group Fitness, Sports Team, Strength Coach, Enterprise, Physical Therapy, Chiropractic, Yoga, Pilates, Martial Arts, Corporate Wellness); migration tooling imports "your clients payment, package, and other data".
- Reading: Exercise.com is the suite pole — the same product serves gyms, studios, and personal trainers; the PT solution page names the appointment-led loop (schedule appointments and classes, accept payments, track visits) with workout/marketing/online modules attached. Trainer Commissions documents the multi-trainer money split as a first-class payments capability.

### PT Distinction (Tier 2: product pages; help center unreachable)

Evidence: A for quoted product-page claims; B-level for mechanics.

- Self-label: "Personal Trainer Software with Every Feature Included"; "Train more clients in less time"; "trusted by personal trainers, hybrid coaches, and fitness professionals… to power their online coaching services".
- Feature grid (official): Branded apps; **Training programs** ("Build any type of program to train clients in your own unique way"); AI Program Generator; Nutritional coaching; AI Meal Planner; AI Assistant; **Assessments** ("Built-in, or custom assessments"); **Groups** ("challenges, trials, flagship programs, and group training"); Communication (email/SMS/app messages); **Automated workflows**; Habits; **Client results** ("workout results, habits, meal updates"); Integrations (payments, client metrics); Pre-made templates; **"Sell packages and take payments"** ("Take payments and sell packages on your own website, clients are automatically added and your packages delivered"); Scheduled messaging.
- Positioning themes: "Works while you sleep — Automate your entire training delivery with our advanced scheduling tools"; "Keep an eye on every movement — Live activity feeds, real-time data visualisations… track client progress"; "Completely branded as yours… your clients won't know we exist".
- Reading: PTD is the remote-coaching-loop suite sold under the "personal trainer software" label. Its center is the delivered-and-tracked coaching engagement (programs, results, habits, automation), with packages/payments attached. It documents the label-span pole from inside the market: the same words ("personal training software") name a structurally different center than PTminder's.

### TrainerFu (Tier 2: product pages)

Evidence: A for quoted product-page claims; B-level for mechanics.

- Self-label: "Simple Personal Trainer Software for In-Person and Online Training"; "build workouts, track progress, sell programs, engage clients and grow your fitness business".
- Feature sections (official): Customize & Manage Workout Plans (builder, videos, schedule weeks/months ahead); Train Your Clients Online ("Send workouts directly to your clients' Trainerfu app. Get notified when your clients complete a workout"); Track Everything (log every client workout, meals, habits, weight, body fat; automatic motivational insights — PRs, goals, streaks); Create & Sell Exercise Programs (embed on website/Instagram/Email/WhatsApp; training packages and challenges); Automatic Messaging (welcome messages and paperwork on signup, drip content, milestone congratulations, accountability reminders when workouts are missed); In-app community newsfeed; Branded app; Teams.
- Testimonial evidence (official page): "When I started using Trainerfu, I had zero online clients and around 15 one-on-one clients, but now I manage 18+ online clients, and around 50+ personal training clients" — documents the hybrid in-person + online roster as the normal case; "Before I found this app, I was working out of notebooks. Now I have all my clients training plans, notes, assessments available to me anytime" — names the displaced paper baseline.
- Reading: TrainerFu is the app-first coaching-loop realization under the PT label — workout delivery + tracking + engagement at the center, selling packages/programs attached. Like PTD, it documents the label-span pole.

---

## Cross-product Comparison

| Structure / capability | PTminder | Vagaro | Exercise.com | PT Distinction | TrainerFu | Evidence |
|---|---|---|---|---|---|---|
| Client records held by the trainer/business (add/remove, notes, custom fields) | A: add/remove, notes, custom fields, family accounts | A: Customer Management category | A: Member Management / CRM modules | A: client management implied by feature grid ("Manage clients from anywhere") | A: client roster implied ("manage 18+ online clients, 50+ PT clients") | Cross-product |
| Bookable service catalog (session types with duration/price; templates) | A: Session Templates, Service Categories, Class Templates | A: Services, Service Bundles, Classes | A: Booking module ("schedule appointments and classes") | B (packages imply services) | B (packages/challenges) | Cross-product |
| Appointment binding client×service×trainer×time | A: Booking in Sessions and Classes; assigned trainers on templates; available/unavailable windows | A: Calendar and Scheduling; Resources | A: Booking module | B (scheduling tools) | B (implied) | Cross-product |
| Session lifecycle through delivery (attended/missed/cancelled/rescheduled) | A: **Reconciling** — confirm attended/missed/cancelled/rescheduled + payment/credit deduction | B (checkout/visit completion per spa pass) | A: "track visits", Check-Ins | B (activity feeds) | B ("get notified when your clients complete a workout") | Cross-product |
| Money loop: per-session payment OR package/membership credit deduction | A: reconciling records payment or deducts from package/membership; credits booked/completed/left; carryover; expiring credits | A: packages = "set number of future visits", auto-renew by time or completed visits, carry forward; memberships = discounts | A: Payments modules incl. Account Balances, Invoicing; migration imports "payment, package, and other data" | A: "Sell packages and take payments… clients are automatically added and your packages delivered" | A: training packages and challenges; sell programs | Cross-product |
| Trainer/staff layer (multi-trainer, assignment, commissions) | A: Staff Management collection; Assigned Trainers on session templates | A: Employee Management, Payroll | A: Staff Management, Trainer Commissions | B (teams implied) | A: Teams feature section | Cross-product (common; solo trainer remains the center of gravity) |
| Client-facing booking/purchase surface (portal/app) | A: online session bookings, client online portal, Direct Buy Links | A: MySite, consumer app | A: custom-branded apps | A: branded apps | A: client app, branded app | Cross-product (common) |
| Workout program builder + delivery | A: Workout Planner (module inside Clients) | (not surfaced) | A: Workout Plan Creator, Workout Logger | A: Training programs, AI Program Generator | A: workout builder, send to client app | Cross-product (common module) |
| Nutrition planning | A: Nutrition Planner | (not surfaced) | (not surfaced in nav) | A: Nutritional coaching, AI Meal Planner | A: nutrition-coaching use case page | Common module |
| Assessments | A: Client Assessments | A: Forms and SOAP Notes | A: Assessments module | A: Assessments | A: assessments (testimonial) | Common module |
| Progress tracking (metrics, photos) | A: progress in client management | (not surfaced) | A: Progress Photos, Performance Reporting | A: Client results | A: Tracking Everything | Common module |
| Messaging / reminders / automation | A: chat, SMS reminders | A: Email and Text Messaging | A: Email, SMS, Push, Automations | A: Communication, Automated workflows, Scheduled messaging | A: automatic messaging, community feed | Common |
| Classes / group offerings alongside 1:1 sessions | A: Class Templates, Online Class Bookings | A: Classes and Workshops | A: "appointments and classes" | A: Groups | B (challenges) | Common |
| Waitlists | A: Waiting Lists | (not surfaced this pass) | (not surfaced) | (not surfaced) | (not surfaced) | Optional |
| Video-conferencing links in bookings | A: Zoom links in bookings | (not surfaced this pass) | (not surfaced) | (not surfaced) | (not surfaced) | Optional |
| POS / products / gift cards | A: Products, Payment Integrations | A: Checkout, Inventory, Gift Cards | A: POS, ECommerce | (not surfaced) | (not surfaced) | Optional |
| Multi-location | (not surfaced) | (not surfaced this pass) | A: Multi-Location module | (not surfaced) | (not surfaced) | Optional |
| Trainer commissions / payment splitting | (not surfaced) | (not surfaced this pass) | A: Trainer Commissions, Payment Splitting | (not surfaced) | (not surfaced) | Optional |
| Marketing/lead machinery (CRM, funnels, websites) | (not surfaced) | A: Marketing Your Business | A: CRM, Leads, Sales Funnels, Websites | B (integrations) | B (sell programs via embed) | Optional |
| AI drafting (program/meal generation) | (not surfaced) | (not surfaced) | (not surfaced in nav) | A: AI Program Generator, AI Meal Planner, AI Assistant | (not surfaced) | Emerging, optional |
| Remote-coaching loop as the product's center (delivery + review between sessions) | (secondary — Online Training feature) | (absent) | (secondary — Online Training module) | A: the product's center | A: the product's center | Pole split, not common structure |

Observations:
1. Rows 1–6 (client records, service catalog, appointment binding, session lifecycle, money loop, staff layer) appear across the sample — but rows 1–5 are the load-bearing set; the staff layer is trivially absent in a solo-trainer configuration and therefore common-not-definitional.
2. The sample splits into two poles: **appointment-led business systems** (PTminder, Vagaro, Exercise.com's business core) and **remote-coaching-loop suites wearing the same label** (PT Distinction, TrainerFu). The market sells both under "personal training software". The leaf's center of gravity, per the sibling flags and the appointment-led pole's evidence, is the appointment-led training business.
3. The session-credit economy is the distinctive money shape of this Type vs generic appointment businesses: packages/memberships carry session credits that bookings consume and reconciling settles — documented at Tier-1 in both PTminder and Vagaro.
4. Program delivery, nutrition, assessments, progress tracking appear as modules in every product — the "signature layer" of fitness training content riding the business spine, never the center of the appointment-led pole.

## Canonical Model

### L0 — Defining Invariant (five jointly-held structures, the appointment-business family core with fitness-training binding)

1. **The bookable training-service catalog.** The trainer's offer held as bookable service types — 1:1 sessions, partner/small-group sessions, classes — each carrying duration and price, commonly organized as reusable session templates with trainer assignment. Fitness-training-typed (training sessions, not haircuts, not medical procedures). Remove → a price list, not a business system.
2. **Client records.** Identified clients held by the trainer/training business, persisting across the relationship, carrying contact details, notes/assessment history, and their purchase/credit state. Family/guardian accounts common. Remove → an anonymous booking page or contact list.
3. **The appointment binding** client×service×trainer×time — the session booked on the trainer's calendar against availability, by the trainer or self-served by the client through a booking surface. Remove → a client database with no scheduled delivery.
4. **The session lifecycle through delivery.** The booked session moves to a named outcome — attended, missed, cancelled, rescheduled — confirmed by the trainer after the fact (PTminder's "reconciling": confirm who attended and who paid what). Remove → a booking calendar with no operational memory.
5. **The money loop resolving the session into recorded payment** — either a per-session payment or a deduction from a prepaid package/membership credit balance (packages = pre-bundled sets of future visits with expiry/carryover/auto-renew rules; memberships = discount/entitlement instruments). Remove → a schedule with no economics; the business stops being run as a business in the system.

Jointly-held load-bearing analysis:
- 1 alone = a price list
- 2 alone = a contact book / mini-CRM
- 3 without 1+2 = an empty calendar tool
- 4 without 1–3 = an attendance log
- 5 without 1–4 = a payment processor
- 1+2+3 without 4+5 = a booking page (the pure booking-loop pole)
- 1+2+4+5 without 3 = a billing system with no scheduled delivery
- all five without the fitness-training binding = the generic appointment-business family (salon/spa/clinic territory)

### L1 — Common Mature Structure

Standard capabilities documented across the sample: client self-service booking portal and/or client app; branded white-label apps; automated reminders (SMS/email) and no-show reduction; waiting lists; class/group offerings alongside 1:1 sessions; workout program builder with exercise library and delivery to the client's app; nutrition planning; client assessments and progress records (metrics, photos); messaging (chat + broadcast); trainer/staff management with assignment and (at suite tier) commissions; payment integrations; reporting (bookings, revenue, attendance); family accounts; discount codes; video-conferencing links in bookings.

### L2 — Variant / Optional Structure

- Business-scale variants: solo trainer (center of gravity) → multi-trainer business → multi-location operation; trainer commissions and payment splitting at suite tier.
- Sales-channel variants: direct buy links, discount codes, embedded checkout on the trainer's own website, gift cards, product/retail POS.
- Delivery-shape variants: in-person only; hybrid in-person + online rosters (the normal case per TrainerFu's testimonial evidence); remote-delivery-heavy configurations.
- Marketing/lead machinery: CRM, lead capture, sales funnels, websites, email/SMS campaigns.
- Content/community variants: on-demand libraries, challenges, groups, community feeds.
- Emerging: AI program/meal drafting under trainer authority; COVID-era verification features (product-era artifact).

### L3 — Vendor-specific Structure (research notes only)

- PTminder: "Reconciling"/"Unreconcile" terminology; carryover vs expiring credits distinction; family accounts; Covid-19 vaccination verification from the client portal; Xplor ownership; NZ/AU payment integrations (Debitsuccess, Ezidebit, GoCardless).
- Vagaro: package-vs-membership doctrine (prepaid visits vs discount entitlements); auto-renew by completed visits (packages) vs time-only (memberships); Resources as bookable rooms/tools; PayPro front-desk hardware; HIPAA-compliant posture.
- Exercise.com: Daxko ownership; 16-industry solution grid; Trainer Commissions; BNPL; managed apps/custom dev; "done-for-you migration" positioning.
- PT Distinction: AI Program Generator / AI Meal Planner / AI Assistant branding; "works while you sleep" automation positioning; all-features-included pricing philosophy; UK registration.
- TrainerFu: platform-separated apps (desktop/Android/Apple); Facebook-style client community feed; streak/PR motivational insights; sell-programs embed channels (Instagram/WhatsApp).

## Vendor-specific Findings

See L3. Marketing scale claims (PTD's "60,000 training businesses"; PTminder's 9.9M bookings / $218m payments counters) are vendor figures recorded here only.

## Boundary Findings

1. **vs Online Fitness Coaching (processed 2026-09-08) — joint-review flag DISCHARGED.** The proposed discriminator is ratified from this side: **who holds the engagement in-system**. Here the *appointment* is the container of the engagement — the calendar/ledger holds the business; delivery happens at the booked session, and the system's memory is attendance + payment (reconciling). In Online Fitness Coaching the *platform* carries the relationship between sessions — prescription delivered into the client's own surface for remote execution, review-and-adaptation loop carried by the platform. The "online" qualifier fails here: PTminder's online-booking machinery schedules in-person (or video-call) sessions; it does not carry the coaching loop. Blending confirmed as predicted: the market ships both in one product (PTminder's Online Training feature; Exercise.com's Online Training module; PTD/TrainerFu entire), and the "personal training software" label spans both poles — capability-tier packaging, keep-both. The two leaves form one market label with two structural centers; each leaf documents its own pole.
2. **vs Sports Coaching Platform (processed 2026-09-09) — flag DISCHARGED.** Vertical siblings of the same practice spine (client roster + sessions + money + delivery), as that pass predicted. Discriminator ratified: domain center of gravity — sports skill instruction (technique feedback, lessons, video analysis) vs fitness training (workout prescription, conditioning). Market overlap confirmed: Exercise.com serves both Personal Trainer and Strength Coach/Sports Performance solutions; PTD names "personal trainers, hybrid coaches"; TrainerFu serves both. Family treatment recorded (same pattern as the class-management family flag): same spine, domain decides, keep-both.
3. **vs Nutrition Coaching Platform (processed 2026-09-08) — forward flag DISCHARGED.** The managed-prescription-subject test holds: here the managed center is the training business (sessions, packages, money); nutrition appears as a planner module (PTminder Nutrition Planner; PTD Nutritional coaching; TrainerFu nutrition use case) — the same gradient that pass recorded in reverse. Keep-both.
4. **vs Fitness Assessment Application (processed 2026-09-07) — module-carries-core test DISCHARGED.** That pass named Exercise.com and PT Distinction as the embedded-module pole; this pass confirms at both vendors: assessments are a module (PTminder Client Assessments collection; Exercise.com Assessments module; PTD Assessments feature; Vagaro Forms and SOAP Notes). The platform centers the business relationship; the module carries the assessment core. Keep-both.
5. **vs Fitness Studio Management (processed 2026-09-08) — appointment-led vs class-led seam DISCHARGED.** That pass's flag is confirmed from this side: PTminder carries Class Templates and Online Class Bookings as a secondary offering type beside Session Templates — exactly the mirror of studio suites carrying appointments as a secondary booking type. Center of gravity decides; keep-both.
6. **vs Workout Programming Application (processed 2026-09-09) — removal test DISCHARGED.** That pass recorded "center appointments/packages/billing → Personal Training Management". Confirmed: the workout planner is a module here (PTminder Workout Planner collection; Exercise.com Workout Plan Creator), the program artifact is not the center; the session-and-money loop is. Keep-both.
7. **vs Coaching Commerce Platform (§27, processed).** Commerce centers converting a purchase into a tracked service entitlement (offer → checkout → entitlement). Here the center is running the training business around delivered sessions. The seam products: "sell packages on your own website" (PTD) and "sell programs anywhere" (TrainerFu) attach commerce channels; a PT system with no storefront is still this Type; a commerce platform with no session operations is still that one. Keep-both.
8. **vs Fitness Progress Tracker (processed).** The tracker centers the person's self-serve metric record; here progress records exist for the trainer's management of the client relationship (module, not center). Keep-both.
9. **vs AI Fitness Coach (processed).** The who-adapts test holds: AI program generators (PTD AI Program Generator) draft under the trainer's authority; the trainer remains the business's and the prescription's adapting authority. Fully software-adaptive products stay in the AI-coach Type. Keep-both.
10. **vs Gym Management System (processed).** The gym/studio family flag concerned membership/class-led facility operations; this leaf is the third pole of the same market — the appointment-led trainer-client practice. Gym systems center members/facility/access; PT management centers the trainer's session book. Keep-both; no new flag.
11. **The label-span finding (taxonomy observation, no directory change).** The market label "personal training software" spans two structural poles: appointment-led business systems (PTminder, Vagaro-for-PT, Exercise.com's business core) and remote-coaching-loop suites (PT Distinction, TrainerFu). Both poles are real products; the directory already holds a leaf for each pole (this leaf; online-fitness-coaching). Recorded in STATUS.md Boundary Issues as a family observation for the eventual §28 family review; no unilateral directory change.
12. **"去掉什么就变成另一个 Type" 判据**: remove the session-credit economy → generic appointment scheduler; remove the appointment binding → client CRM; remove the client records → anonymous booking; make the remote delivery+review loop the center → Online Fitness Coaching; make sports skill instruction the domain center → Sports Coaching Platform; make the class schedule the center → Fitness Studio Management; make the program artifact the center → Workout Programming Application; make nutrition prescription the center → Nutrition Coaching Platform; make the testing protocol the center → Fitness Assessment Application; make selling the engagement the center → Coaching Commerce Platform; make the facility/membership the center → Gym Management System.

## §24 Historical / Market-Sample Check

Would older, regional, platform-native products still fit? Yes:

- The paper-era personal training business: an appointment book (appointment binding), a client card file (client records), a rate card for session types (service catalog), the session card punched per visit (the session-credit package), cash collected at the session or against the prepaid card (money loop), and the trainer's mental/paper note of who showed and who owed (session lifecycle). All five L0 structures satisfied with no app, no portal, no reminders, no automation.
- Early desktop-era PT schedulers (calendar + client database + invoicing) satisfy the core without client apps or credit engines (per-session invoicing suffices — the money loop requires recorded payment, not a specific credit mechanism).
- Regional variants (e.g., session-card systems in Asia-Pacific gyms, direct-debit memberships in UK/AU markets — PTminder's Ezidebit/Debitsuccess/GoCardless integrations document the regional payment-rail variation) satisfy the core.

**Check passes.** The definition is written at the business-structure level, not at the SaaS/credit-engine level: the money loop requires recorded settlement of the session, not any particular package mechanics.

## Uncertainties

1. Exercise.com operational documentation login-gated — its suite-pole mechanics (booking rules, package semantics, commission flows) unverified; held at product-page strength.
2. PT Distinction help center unreachable — its appointment/scheduling machinery (if any beyond scheduling of program delivery) unverified; PTD's classification as the coaching-loop pole rests on its own product-page positioning, which is explicit.
3. TrainerFu's booking/appointment machinery not surfaced on fetched pages — its appointment-led capabilities (if any) unverified; held at product-page strength.
4. Whether a dedicated *waitlist* or *resource/room* layer is common across the Type is only partially evidenced (PTminder waiting lists; Vagaro resources from the spa pass); held optional.
5. The exact prevalence of trainer-commission machinery across the market is unverified (documented only at Exercise.com); held optional/suite-tier.

## Final Synthesis

A Personal Training Management application is the personal trainer's (or training business's) appointment-led system of record. Its defining core is five jointly-held structures inherited from the appointment-business family and bound to fitness training: the bookable training-service catalog (session types with duration/price), client records, the appointment binding client×service×trainer×time, the session lifecycle through delivery (attended/missed/cancelled/rescheduled, trainer-confirmed), and the money loop resolving each session into recorded payment — per-session or against a prepaid package/membership credit balance. Everything else — workout planners, nutrition planners, assessments, progress tracking, messaging, reminders, waitlists, branded apps, POS, marketing machinery, commissions, AI drafting — is standard or variant machinery built on that spine. The market sells this Type and the remote-coaching-loop Type under one label ("personal training software"); the structural seam is who holds the engagement in-system: the appointment (here) vs the delivered-and-reviewed prescription (Online Fitness Coaching). The Type's edges are defined by four tests: what is the container of the engagement (appointment vs relationship loop vs program artifact), what is the money object (session credits vs membership entitlements vs program sales), what is the domain center (fitness training vs sports skill vs nutrition), and who adapts the prescription (human trainer vs software).
