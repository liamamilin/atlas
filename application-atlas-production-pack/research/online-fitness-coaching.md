# Research Notes — Online Fitness Coaching

Directory leaf: Online Fitness Coaching (§28 Sports, Fitness & Recreation)
Slug: online-fitness-coaching
Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what an "Online Fitness Coaching" application actually is as an Application Type: what the coach-side software holds, what the client-side software does, how the remote coaching loop really operates, and where its boundary lies against the neighboring §28 types (Personal Training Management, Workout Programming Application, Workout Tracking Application, AI Fitness Coach, Nutrition Coaching Platform, Fitness Progress Tracker, Wearable Fitness Platform), plus adjacent types from other sections (Coaching Commerce Platform §27, Telehealth/Practice Management §22, on-demand workout content).

## Initial Boundary (hypothesis before research)

- Hypothesis: an Online Fitness Coaching application mediates a *human* coach's delivery of fitness coaching to clients who are not physically present — the coach composes training, the client executes remotely and reports back, the coach reviews and adapts. The human is the adapting intelligence.
- Nearest neighbors:
  - **Personal Training Management** — likely centers the training *business* (appointments, packages, billing, staff) rather than the remote coaching loop. Unprocessed leaf; seam to flag.
  - **Workout Programming Application** — likely centers the program *artifact* (authoring), not the ongoing relationship. Unprocessed leaf; seam to flag.
  - **AI Fitness Coach** (processed 2026-09-06) — software adapts the plan; here a human adapts. This pass must discharge the ai-fitness-coach pass's joint-review flag from this side.
  - **Nutrition Coaching Platform** (processed 2026-09-08) — same loop shape, nutrition is the managed prescription subject. This pass must discharge that pass's forward flag ("which prescription is the managed center").
  - **Coaching Commerce Platform** (§27, processed 2026-09-07) — centers selling the engagement (offer → checkout → tracked service entitlement); here the center is the coaching delivery loop.
  - **Fitness Progress Tracker** (processed 2026-09-08) — person-facing record of one's own metrics; no coach authority.
- Unknowns: does the Type require a dedicated client-facing app? Is 1:1 the defining scope or are teams/groups inside? Is the client-execution record (logging) part of the defining core or a standard capability? Where does the "online" qualifier actually bind?

## Research Questions

1. What objects does the coach side hold? (client, program, workout, exercise, library, check-in, metrics, messages)
2. What is the core loop, step by step, from client acquisition to plan adaptation?
3. What does the client see and do? Is there a client-side surface, and is it definitional?
4. How is "delivery" realized (calendar, email digests, app push, share links)?
5. What state/lifecycle objects exist (client lifecycle, program scheduling, compliance windows)?
6. What rules govern the relationship (who invites, who owns data, compliance calculation, program stacking)?
7. Where are the boundaries vs the seven neighbor types listed above?
8. Historical check: do pre-app implementations (email + spreadsheets + YouTube links + text messages; paper plans) satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| **ABC Trainerize** | full-suite coach-side platform (independent trainers → gyms → enterprise) | the market-defining "online coaching platform"; very deep Tier-1 help center |
| **TrueCoach** | lean coach-side platform for personal trainers / strength coaches | focused philosophy (delivery + compliance, minimal extras); Tier-1 help center incl. a dedicated client-experience article |
| **TrainHeroic** | strength & conditioning pole with team delivery + program marketplace | team/athlete vocabulary, hybrid remote+in-person rosters; Tier-2 product pages (help center timed out) |
| **Everfit** | modern all-in-one with heavy automation | newest-generation competitor; Tier-1 help center category TOC |
| **Future** | consumer B2C pole (platform employs/matches human coaches) | shows the client-experience-first shape of the same structure; Tier-2 product page + thin help center |

## Sources

Tier 1 (official operational documentation):
- ABC Trainerize Help Center — https://help.trainerize.com/ — root TOC; category "Managing and Monitoring Clients" (Client management, Monitoring client compliance sections); category "Training – Programs, Workouts, Exercises" (Master Programs, Master Workouts, On-Demand Video Workouts, Exercises, Workouts FAQ, Programs FAQ sections)
- TrueCoach Help Center — https://help.truecoach.co/ — root TOC (collections: Account Settings & FAQs, TrueCoach Client Tutorials, Managing Clients, The Workout Calendar & Sidebar, Library, Programs, Transfers and Team Accounts, Payments, Messaging, Wearables, MyFitnessPal); article "The TrueCoach Client Experience"; collection "Managing Clients" article list (incl. Client Types, Compliance Rates, Client Due Dates, Client Grouping, Archived Clients)
- Everfit Help Center — https://help.everfit.io/ — root TOC (collections: Getting Started, Everfit's Workout Builder, Manage Clients, Booking & Scheduling, Nutrition Coaching, Tasks & Habits, Metrics, Group Coaching (Autoflow/Automation), On-demand Training Features, Payment & Packages, Team Features, Client App, Forums and Leaderboards, White Label Solution)

Tier 2 (official product pages):
- TrueCoach — https://truecoach.co/ (features, positioning, compliance-tracking feature description)
- TrainHeroic — https://www.trainheroic.com/ and https://www.trainheroic.com/coach (positioning, coach tools, teams/1:1, video review, marketplace, athlete app)
- Future — https://www.future.co/ (positioning, coach check-ins, member profile dimensions, plan flexibility); https://faq.future.co (help center exists; only one collection surfaced — see Limitations)

Source-access limitations:
- TrainHeroic support center (https://support.trainheroic.com/hc/en-us) timed out once; per network rules the source was dropped rather than retried repeatedly. TrainHeroic evidence is therefore held at product-page strength (no Tier-1 operational claims).
- Future's help center fetch returned only the root (one collection, "Future Pro", 23 articles, not itemized). Future claims held at product-page strength; no precise operational mechanics asserted.
- TrueCoach marketing pages include pricing ("$50 first month, then $199/month" appears on Future's page; TrueCoach quotes 16,000+ coaches / 50M+ workouts delivered) — marketing figures recorded here only, never asserted in the final document.

---

## Product observations

### ABC Trainerize (Tier 1: help center)

Evidence: A (direct observation of official help-center structure and article titles).

- Root TOC categories: Getting Started; Account and Billing; Business; Training – Programs, Workouts, Exercises; Nutrition; Goals and Habits; **Managing and Monitoring Clients**; Messaging, Engaging Clients and Building Digital Communities; Team and Business-Level Controls; Selling Digital Fitness; Payments; Appointments and Video Calls; Custom Branded Apps; Add-ons and Integrations.
- Client management section: "Different Ways Clients Can Be Added", "Offline Clients" (clients not actively using the app), "Bulk Assign Actions", "Web Account vs Mobile App feature access", "Assign a Client to Multiple Trainers" — documents coach-owned roster mechanics and multi-coach assignment.
- Monitoring client compliance section: "Threshold Alerts", "Client Insights Dashboard", "Progress Tiles", "Configuring Tiles on the Client Dashboard", "Tracking and Measuring Client Progress", "Company-Wide Compliance on the Overview Page" — documents the coach-side review layer over client adherence (individual + business-wide views).
- Training structure: **Master Programs** library (Phased Programs, On-Demand Programs, Program Tags, "Multiple Programming", "How To Setup A Client's Calendar"), **Master Workouts** (library, workout types, interval/metcon builders, **AI Workout Builder**), **On-Demand Video Workouts** (including captions, content strategy), **Exercises** (notes, **exercise substitution during a workout**, tags, library currency), Workouts FAQ (auto-fill exercise stats, scheduling workouts and cardio on web/mobile, clients filtering workouts, RPE), Programs FAQ ("Trimmed" in a client's program, **backdating or pausing a client's program**, subscribing vs copying a program, **how programs stack in a client's calendar**, mass delete calendar items incl. auto-messages).
- Positioning (Tier 2, footer/nav): audiences "Independent Trainers", "Gyms and Studios", "Enterprise Solutions"; "Selling Digital Fitness" (digital storefront); payments; branded apps; Trainerize.me trainer directory.

Reading: Trainerize realizes the full coach-business suite wrapped around a delivery-and-review core: roster → master program/workout libraries → schedule onto client calendar → client app execution → compliance dashboards and alerts → messaging/engagement → business modules (payments, storefront, appointments, nutrition, habits).

### TrueCoach (Tier 1: help center; Tier 2: product site)

Evidence: A (help-center TOC + full client-experience article); A for feature descriptions quoted from official pages.

- Help-center collections: Account Settings & FAQs; **TrueCoach Client Tutorials** ("how to navigate your TrueCoach client account"); **Managing Clients** ("everything from messaging to archiving clients"); **The Workout Calendar & Sidebar** ("all the basics you need to write workouts for your clients"); Library (exercise library, warmups, cooldowns, metric sets, documents); **Programs** ("write a program to assign to multiple clients or groups"); Transfers and Team Accounts; The TrueCoach App; Payments; Messaging; Wearables; MyFitnessPal integration; Coach Profile (leads).
- Article "The TrueCoach Client Experience" (full text observed): coach adds client → client receives **invitation email** → sets password → account activated; access via web or dedicated **client iOS app**; assigned workouts arrive as **daily workout emails** (toggleable by either side) plus a **"workout is missed" email**; email links "Open in TrueCoach"; the workout view shows warm-up / exercises / cool-down with **demo videos and written instructions**; per-exercise **Exercise History**; a **Past** tab for any date's workout; clients **enter results and upload photos/videos** per exercise; client profile holds **metrics, progress photos, shared library files**; **real-time messaging** for training communication; empty state when no workouts assigned. Client types mentioned: "remote and dual clients" (i.e., client typing distinguishes remote vs in-person-involved clients).
- Managing Clients article list: Adding a New Client, **Client Types**, Client Grouping, **Compliance Rates**, **Client Due Dates**, Archived Clients, Deleting a Client, Onboarding Sequence (automation), Client Invitation Email, In-App Timer, export.
- Product site (official feature descriptions): "Compliance Tracking — each of your clients will have a 7, 30, and 90-day compliance rate… calculated by the number of exercises completed vs. the number of exercises assigned" (precise windows are product-specific); "Dashboard — know what your clients are doing and where they are in a programming cycle"; Program Builder ("write your programs once, then customize for each client"); Video Exercise Library (3,000+ videos claimed in marketing — not asserted further); messaging ("all coach-to-client communication kept in one place"); nutrition tracking; habit tracking; wearables; public profiles (lead capture); automated payments via Stripe; custom theming.
- Positioning: "#1 platform built for personal trainers — train your clients online"; explicitly names the displaced baseline: *"the 'glue-it-together' days of spreadsheets, email, YouTube videos, and text messages are in the past"* — direct vendor acknowledgment of the pre-platform coaching stack (valuable for the historical check).

Reading: TrueCoach is the lean realization: roster + program authoring + calendar delivery + client logging + compliance math + messaging. Business machinery (payments, profiles) present but clearly secondary to the coaching loop.

### TrainHeroic (Tier 2: product pages only — help center unreachable)

Evidence: B-level at best (product-page claims; no operational documentation fetched).

- Coach page: "Deliver a premium athlete experience, **manage remote and in-person clients in one place**"; "Teams and 1:1 — coach 1:1 or group clients into **teams** for easy program delivery and group communication"; "**Video review** — review athlete videos and deliver fast, actionable feedback"; "Customizable library — create and organize workouts, circuits, and full programs — or use ours"; "Real-time chat"; "**Client tracking** — track compliance, progress, programming status and more from one powerful dashboard"; "Easy client onboarding — send an invite and we'll handle the rest"; branding ("add your logo, custom exercise demos").
- Home page: "**Where great programming becomes great coaching.** Sending workouts isn't the same as coaching. TrainHeroic unifies your tools, tracking, and communication into a single command center… guide your athletes without the spreadsheet headaches." — vendor-articulated statement that one-way delivery is not the product's center; the loop is.
- Marketplace: "sell your programs in the TrainHeroic Marketplace" / "Turn your programming into revenue — reach more athletes and sell training programs" — pre-built program commerce as an attached revenue channel (adjacent pole inside the product).
- Athlete side: "a world-class app for athletes to log, track, and stay engaged"; leaderboards; athlete testimonial: "My workout is delivered to my phone"; another: "I won't go back to the old pen and paper workout log."
- Vocabulary: coach/athlete (not trainer/client) — strength & conditioning market.

Reading: same spine as Trainerize/TrueCoach (roster → program library → delivery → logging → compliance/tracking → chat), plus two notable extensions: teams as a first-class delivery container, and a marketplace for selling pre-built programs (where the review loop drops out — the adjacent pole documented from inside a sampled product).

### Everfit (Tier 1: help-center TOC; article bodies not fetched)

Evidence: A at category level (official TOC with collection names and article counts).

- Collections: Getting Started (59); **Everfit's Workout Builder** (38); **Manage Clients** (22); **Booking & Scheduling** (15); **Nutrition Coaching** (43); **Tasks & Habits** (18); **Metrics** (5); **Group Coaching (Autoflow / Automation)** (21); **On-demand Training Features** (11); **Payment & Packages** (29); Team Features (6); **Client App** (58); Settings (15); Forums and Leaderboards (9); Zapier Integration (3); White Label Solution (5).
- Reading: TOC confirms the same object set (workout builder → clients → client app → metrics) plus heavy investment in automation ("Autoflow" — branded automation of program/client actions) and community surfaces (forums, leaderboards). A dedicated "Client App" collection (58 articles) documents the client-side surface as a first-class half of the product.

### Future (Tier 2: product page; help center root only)

Evidence: A for quoted product-page claims; B-level for mechanics.

- Positioning: "Personal training, reimagined — dedicated coaching and support"; consumer membership (pricing figures observed on page — recorded in notes only).
- Coach matching: "Find Your Coach" via an intake **survey/quiz** — the platform matches client to coach (consumer-pole onboarding).
- Loop claims (official page copy): "Our coaches **create your program** with proven methods"; "**Your coach checks in, monitors your progress, and holds you accountable**"; "**Move workouts, adjust days, and adapt your plan** at any time without penalty"; "**Your coach actively refines your plan over time** so your training evolves with you."
- Product-page visuals document: coach **video check-in** and chat feedback referencing the client's logged sets ("Nice lift, Alex! You recovered quickly between sets…"); a member profile structured as **Schedule / Equipment / Experience / Injury Record / Goals** — the client-profile dimensions the coaching relationship is built on; exercise library with **video demos, voice cues, form guidance**; Apple Watch integration.
- New line extension visible: "health coaching — nutrition, sleep, and more" (adjacent-domain expansion).

Reading: Future is the consumer-pole realization: the member never sees coach machinery — they see a matched human coach, their plan, guided execution, and the coach's check-ins/refinements. Structurally identical spine (roster → prescription → delivery → execution capture → review/adaptation), with the coach side hidden behind the platform.

---

## Cross-product Comparison

| Structure / capability | Trainerize | TrueCoach | TrainHeroic | Everfit | Future | Evidence |
|---|---|---|---|---|---|---|
| Coach-held client roster (add/invite, persists) | A: "ways clients can be added", offline clients, multi-trainer assignment | A: invitation email, Client Types, grouping, archiving | B: "send an invite and we'll handle the rest" | A: Manage Clients collection | B: platform-matched coach, member profile | Cross-product |
| Client-facing surface (app/web) for the coached person | A: web vs mobile feature access article | A: dedicated client app + client tutorials collection | B: athlete app | A: Client App collection (58 articles) | B: member app | Cross-product |
| Coach-composed training prescription (workouts/programs bound to client) | A: Master Programs/Workouts, client calendar | A: Workout Calendar & Sidebar, Programs | B: customizable library, full programs | A: Workout Builder collection | B: "coaches create your program" | Cross-product |
| Remote delivery onto client surface (calendar/email/app) | A: client calendar, program stacking, scheduling articles | A: daily workout emails, missed-workout email, "Open in TrueCoach" | B: "workout is delivered to my phone" | A: collections imply (client app) | B: plan on member's device | Cross-product |
| Client execution capture (results, photos/videos, history) | A: exercise substitution, auto-fill stats, RPE, tracking workouts | A: results entry, photo/video upload, Exercise History, Past tab | B: video review, athlete logging | A: implied by Metrics/Client App collections | B: guided logging, Apple Watch | Cross-product |
| Coach review & compliance/adherence layer | A: Insights Dashboard, Threshold Alerts, progress tiles, company-wide compliance | A: Compliance Rates article, dashboard | B: "track compliance, progress, programming status" | A: Metrics collection | B: "coach monitors your progress" | Cross-product |
| Adaptation by the human coach | A (implicitly: scheduling, program revision tools) | B (dashboard: "give them what they want before they tell you") | B: "fast, actionable feedback"; video review | B | B: "coach actively refines your plan" | Cross-product |
| Messaging bound to the relationship | A: Messaging & community category | A: Messaging collection ("all communication in one place") | B: real-time chat | A (implied by TOC) | B: chat + video check-ins | Cross-product |
| Reusable master/template libraries | A: Master Programs/Workouts, tags | A: Library, Programs collections | B: "create and organize… or use ours" | A: Workout Builder | (not surfaced) | Cross-product |
| Progress: metrics, photos, goals | A: Tracking and Measuring Client Progress | A: client profile (metrics, progress photos) | B: progress tracking | A: Metrics collection | B: member profile dimensions | Cross-product |
| Nutrition module | A: Nutrition category, Advanced Nutrition Coaching | A: nutrition tracking, MyFitnessPal | (not surfaced on fetched pages) | A: Nutrition Coaching collection (43) | B: health-coaching expansion | Cross-product (common) |
| Habits/tasks | A: Goals and Habits | A: Habit Tracking | (not surfaced) | A: Tasks & Habits | B (sleep etc. under health coaching) | Common |
| Payments/packages/billing | A: Payments + Selling Digital Fitness | A: Payments collection (36), Stripe | B: marketplace revenue | A: Payment & Packages (29) | B: consumer subscription | Common (not universal shape) |
| Appointments / video calls / booking | A: Appointments and Video Calls | (not surfaced) | (not surfaced) | A: Booking & Scheduling (15) | (not surfaced) | Optional |
| Group/team delivery + challenges | A: groups, challenges (community category) | A: programs "to multiple clients or groups" | B: teams first-class | A: Group Coaching (Autoflow) | (not surfaced) | Common |
| Pre-built program marketplace | B: Trainerize.me directory (trainer listing) | (not surfaced) | B: TrainHeroic Marketplace | (not surfaced) | (not surfaced) | Optional (single-product pole) |
| On-demand video content | A: On-Demand Video Workouts | (not surfaced) | (not surfaced) | A: On-demand Training Features | (not surfaced) | Optional |
| Wearables integration | B (integrations category) | A: Wearables collection | (owner is Garmin — device heritage) | (not surfaced) | B: Apple Watch | Common |
| Multi-coach teams / business controls | A: Team and Business-Level Controls | A: Transfers and Team Accounts | B: assistant coaches | A: Team Features | (n/a — platform employs coaches) | Common at business tier |
| White-label / branded apps | A: Custom Branded Apps | B: custom theming | B: "make it your own" | A: White Label Solution | (n/a) | Optional (business tier) |
| Automation of client actions | B: auto-messages (calendar items), onboarding | A: onboarding sequences | (not surfaced) | A: Autoflow (branded) | B: automated nudges implied | Common |
| AI drafting assists | A: AI Workout Builder | B: AI meal-plan generator (blog) | (not surfaced) | (not surfaced) | (not surfaced) | Emerging, optional |
| Client-side plan flexibility (move workouts) | B (clients filter workouts) | B | (not surfaced) | (not surfaced) | B: "move workouts, adjust days" | Common, form varies |

Observations:
1. The first nine rows appear in **every** sampled product with Tier-1 or strong Tier-2 support — this is the Type's stable spine.
2. Business machinery (payments, booking, storefront, white-label) concentrates in the coach-side suite products and varies freely — not definitional.
3. The vocabulary varies by market (client vs athlete; trainer vs coach; program vs training plan) but the structure is identical.
4. Two "poles" live inside the same products: the coaching relationship pole (all three legs) and the pre-built program pole (legs 1–2 only, via marketplaces/on-demand) — products themselves treat these as different offerings, confirming the loop's definitional weight.

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The client as a managed record under the coach's care.** A coach or coaching business holds identified client records — added or invited by the coach (or matched by the platform at the consumer pole), persisting across the engagement, carrying the client's profile/context (goals, schedule, equipment, history/injuries) and everything the engagement produces. Remove → a contact book / workout-programming tool with no held clients.
2. **The training prescription delivered for remote execution.** The coach composes training — programs and workouts built from exercises with prescriptions (sets/reps/loads, notes, demo videos) — and the platform delivers it into the client's own surface, where the client executes without the coach physically present. The platform operates the delivery channel between coach and client (calendar, digest email, app). Remove → in-person training management (appointments are the container) or a plan document/content library.
3. **The coach review-and-adaptation loop.** Execution evidence — logged results, completed/missed workouts, form photos/videos, comments, check-ins, metrics — flows back to the coach, who reviews (per client and across the roster, commonly as compliance/adherence views) and responds: feedback, message, or a revised prescription. The adapting authority is the human coach. Remove → one-way plan delivery ("sending workouts isn't the same as coaching" — vendor's own words) or software-driven adaptation (AI Fitness Coach).

Jointly-held load-bearing analysis:
- 1 alone = client CRM / contact book
- 2 without 1+3 = plan or content delivery (e-book, marketplace plan, on-demand library)
- 3 without 1+2 = communication tool
- 1+2 without 3 = one-way program delivery — the marketplace/on-demand pole
- 1+3 without 2 = appointment-centered in-person training (Personal Training Management territory) — the "online" qualifier fails
- 2+3 without 1 = anonymous generator/coach — AI Fitness Coach territory

### L1 — Common Mature Structure

Standard capabilities documented across the sample (A-level for Trainerize/TrueCoach/Everfit, B for others): client invitation & onboarding (incl. intake/consultation forms); master exercise/workout/program libraries with templates/tags; client calendar scheduling with program stacking, pausing/backdating; per-exercise demo videos and instructions; execution capture (results entry, exercise history, past views, RPE, photo/video upload, exercise substitution); compliance/adherence computation surfaced to the coach (individual + roster-wide dashboards, threshold alerts); progress records (body metrics, progress photos, goals); relationship-bound messaging; check-ins; habit/nutrition modules; due-date/missed-workout surfacing.

### L2 — Variant / Optional Structure

- Business layer: payments/packages/subscriptions, digital storefronts, lead-capture profiles, booking & appointments/video calls, multi-coach teams with permissions, white-label/branded client apps, business dashboards.
- Delivery-shape variants: 1:1 vs teams/groups vs challenges/cohort programs; hybrid remote+in-person rosters (client types such as "remote and dual"); client-side flexibility (move workouts, adjust days); automation of recurring actions.
- Content variants: on-demand video workout libraries; pre-built program marketplaces (loop-dropping adjacent pole inside a sampled product).
- Data integrations: wearables, nutrition trackers, Zapier.
- Emerging: AI drafting assists (workout/meal-plan generation) under coach review.
- Consumer-pole variant: platform-operated matching (survey → assigned coach), platform-employed coaches, consumer subscription pricing (Future).

### L3 — Vendor-specific Structure (research notes only)

- TrueCoach: compliance-rate windows of 7/30/90 days; "remote and dual" client types; in-app timer; NASM CEU library; public-profile lead capture.
- Trainerize: "Trimmed" program semantics; Master Programs subscribe-vs-copy distinction; offline-client concept; Trainerize.me directory; ABC ownership branding; Academy/business courses.
- TrainHeroic: coach/athlete vocabulary; leaderboards; Marketplace revenue share; assistant-coach add-on pricing; Garmin (Peaksware) ownership.
- Everfit: "Autoflow" branded automation; forums/leaderboards; white-label tier.
- Future: matching survey; coach video check-ins; Apple Watch voice cues; $199/month-class consumer pricing (marketing page, not asserted in final doc).

## Vendor-specific Findings

See L3 above. Additionally: TrainHeroic's and Trainerize's marketing pages carry scale claims (coaches/athletes/workouts delivered) — marketing figures, not asserted as facts about the Type.

## Boundary Findings

1. **vs Workout Programming Application (§28 sibling, unprocessed).** Programming centers the program *artifact* — authoring high-quality training plans (for print, export, teams, or self-use) — where the deliverable is the plan. Online Fitness Coaching centers the *relationship loop*: the plan exists as a client-bound, delivered, revised object inside a held relationship. A programming tool has no client roster and no review loop. Expect product blending (coaching platforms ship strong builders). Flag for joint review when that leaf is processed.
2. **vs Personal Training Management (§28 sibling, unprocessed).** PT management centers the training *business operations* around in-person sessions: appointment scheduling, session packages, billing, staff, facility. The software container is the calendar/ledger, not the coaching loop. In Online Fitness Coaching the platform itself carries the relationship (delivery + review between sessions). Blending: coach-suite products ship appointment/booking modules (Trainerize "Appointments and Video Calls"; Everfit "Booking & Scheduling") — capability-tier packaging. **Boundary issue recorded in STATUS.md for joint review**: the two leaves plausibly form one family with the seam at "appointment-centered business ops vs relationship-centered coaching loop"; the "who holds the engagement in-system" test is proposed.
3. **vs AI Fitness Coach (§28, processed 2026-09-06).** Discharges that pass's flag from this side: the who-adapts test holds. Here a human coach holds prescription authority and performs review/adaptation; software drafts (AI workout builders, auto-messages) remain under coach ownership. Fully software-adaptive products belong to the AI coach Type; human-coach platforms adding AI assists sit on the gradient, not across the wall.
4. **vs Nutrition Coaching Platform (§28, processed 2026-09-08).** Discharges that pass's forward flag from this side: the managed-prescription-subject test holds — here the managed center is the training/exercise prescription; nutrition appears as a module (meal plans, macro targets, tracker sync) in most sampled products, exactly mirroring how fitness appears as logged context there. Same gradient, same keep-both outcome.
5. **vs Coaching Commerce Platform (§27, processed).** Commerce centers converting a purchase into a tracked human-service engagement (productized offer → checkout → entitlement). Here the center is running the coaching itself. Payments/packages appear as L2 machinery; a coaching platform with no checkout is still this Type; a commerce platform with no delivery/review loop is still that one.
6. **vs Fitness Progress Tracker (§28, processed).** The tracker centers the person's own metric record (self-serve). Here the record exists *for* the relationship: the coach is an acting party, execution data is captured against the coach's prescription, and compliance is computed against assigned work. Metrics/progress views appear here as standard capabilities, not the center.
7. **vs Wearable Fitness Platform / Running / Endurance types.** Data-first or sport-first; here relationship-first and domain-general training.
8. **vs on-demand workout content / video libraries / pre-built plan marketplaces.** No roster, no review loop → not this Type, even when sold by the same vendor inside the same product (TrainHeroic Marketplace documents the pole from inside).
9. **The "online" qualifier binds to the relationship, not the coach's location.** Sampled products explicitly serve hybrid coaches ("manage remote and in-person clients in one place" — TrainHeroic; "remote and dual" client types — TrueCoach). What must be online is the delivery+review channel carrying the coaching between face-to-face contact; if the platform only manages appointments for in-person work, it is PT-management territory.

Historical / market-sample check (per workflow): the pre-platform baseline — coach maintains a client list, emails spreadsheets/PDF plans and YouTube links, client replies with results, coach adjusts next week's plan (named verbatim as the displaced baseline in TrueCoach's own positioning; the pen-and-paper log named in TrainHeroic testimonials) — satisfies all three L0 structures with no app, dashboard, payments, or automation. Definition therefore names no app form, no compliance math, no payments, no wearables, no AI.

## Uncertainties

1. TrainHeroic operational documentation unreachable (timeout) — its row in the comparison rests on product-page claims; no operational mechanics asserted from it.
2. Future help center thin (root only) — consumer-pole mechanics (check-in cadence, coach-load model, revision flow) unverified; held at product-page strength.
3. Whether a *dedicated check-in object* (vs free-form messaging + scheduled forms) is universal is unverified; documented as common, not definitional.
4. Everfit observed at collection-TOC level only (article bodies not fetched); its per-feature semantics not asserted.
5. The exact boundary behavior of "group coaching automation" (Everfit Autoflow) — whether automated group delivery still requires any coach review — is not documented in fetched sources; treated as a delivery-shape variant.

## Final Synthesis

An Online Fitness Coaching application is the coach-side system of record for delivering fitness coaching remotely, paired with the client-side surface that receives the coaching. Its defining core is three jointly-held structures: (1) the client as a managed record under a coach's care — an invited, persistent, context-carrying record that exists because the relationship exists; (2) the training prescription — coach-composed programs/workouts bound to that client and delivered through the platform into the client's own device for execution without the coach present; (3) the review-and-adaptation loop — execution evidence flowing back to the coach, who reviews it (individually and across the roster) and adapts the prescription, with the human coach as the adapting authority. Everything else — libraries, calendars, compliance dashboards, messaging, check-ins, payments, booking, nutrition/habit modules, teams, marketplaces, branded apps, AI drafts — is standard or variant machinery built on that spine. The Type's edges are defined by three tests: who holds the client (roster vs anonymous buyer), who is present at execution (remote delivery vs appointment), and who adapts (human coach vs software vs nobody).
