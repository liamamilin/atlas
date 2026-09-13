# Research Notes — Sports Coaching Platform

## Research Goal

Understand what a "Sports Coaching Platform" really is as an Application Type: whose system it is (the individual coach's? an organization's? the consumer's?), what its core objects and workflows are, and where its boundaries sit against the heavily adjacent §28 family (Sports Academy Management, Sports Club Management, Athlete Management System, Online Fitness Coaching, AI Fitness Coach, Personal Training Management, Sports Video Analysis, Team Management Application) and against consumer lesson marketplaces.

This pass also **discharges the flag hung by the sports-academy-management pass (2026-09-09)**: "Upper Hand's individual-coach pole (booking, billing, zero admin) sits at this seam: a single coach's client business vs a multi-program organization."

## Initial Boundary

Working hypothesis before research (to be tested, not asserted):

- The leaf is probably the **individual sports coach's client-practice system**: the coach as a private instructor (tennis pro, golf pro, swim instructor, pitching coach, skills trainer) running a lesson business — client roster, booked lessons, packages/payments, and the coaching exchange (feedback, video, drills) around those lessons.
- Nearest neighbors: Sports Academy Management (organization pole of the same market), Personal Training Management (fitness vertical sibling, unprocessed), Online Fitness Coaching (remote prescription delivery, processed), AI Fitness Coach (software-as-coach, processed), Athlete Management System (org-level preparation, processed), Sports Video Analysis (capability slice, unprocessed), Team Management Application (team ops, unprocessed), consumer lesson marketplaces (CoachUp-class, marketplace territory).
- Main risk: the leaf could collapse into (a) the academy/club organization pole, (b) a generic appointment-booking tool, or (c) a video-analysis tool. The synthesis must hold all three seams.

## Research Questions

1. Who is the primary user — the individual coach, a coaching organization, or the consumer?
2. What is the system's unit of record — the athlete/client relationship, the lesson, the program, the booking?
3. What does the coach actually do in the product day to day?
4. Is the money loop (packages, payments, billing) definitional or common?
5. Is video analysis definitional or the dominant realization of something more abstract?
6. Is scheduling/booking machinery definitional or common?
7. How do products span solo coach → multi-coach organization, and where does that become Academy territory?
8. Where does the consumer-side marketplace (CoachUp-class) sit relative to this Type?
9. Historical check: does the definition hold for a paper-era or regional private coach with no software?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole / Philosophy | Tier |
|---|---|---|
| **Upper Hand** | business-machinery-first (booking, billing, client engagement); spans individual coach → facility → franchise | solo → enterprise |
| **CoachNow** | relationship/delivery-first (per-athlete Spaces, video analysis, communication); business tools at top tier | solo → multi-coach academy |
| **V1 Sports (V1 COACH)** | video-analysis-first teaching business, golf vertical, two-sided athlete app + demand generation | solo pro → studio |
| **OnForm** | mobile video-analysis-first, multi-sport, roster + feedback delivery; booking/payments not evidenced | solo → coaching organization |
| **CoachUp** (boundary pole only) | consumer-side lesson marketplace — NOT the coach's practice system | consumer |

## Sources

All fetched 2026-09-09 (Layer A = official product pages directly observed):

- Upper Hand — https://upperhand.com/ (root; product/feature/solutions navigation)
- CoachNow — https://coachnow.com/ (root) and https://coachnow.com/coach-features (feature + membership-tier page)
- V1 Sports — https://v1sports.com/ (root) and https://v1sports.com/coaches/v1-coach-app/ (coach product page)
- OnForm — https://onform.com/ (root) and https://onform.com/video-analysis-for-coaches/ (coach product page)
- CoachUp — https://coachup.com/ (root; boundary pole only)

Not fetched (recorded as sourcing limitations): help.upperhand.com, help.coachnow.io, help.v1sports.com, support.onform.com (help centers exist but were not fetched this pass); OnForm pricing page; V1 studio (V1 PRO) page; CoachUp coach-side pages.

## Product Observations

### Upper Hand (Layer A — official product pages)

- Self-labels: "The sports technology platform coaches trust"; homepage headline dynamically names "sports facility academy lessons teams camps club programs … in one system".
- Business-type ladder on the homepage: **"Individual coach — Booking, billing, zero admin"**, "Sports facility — One platform for your entire operation", "Growing academy", "Franchise network". The individual-coach pole is explicitly served.
- "Upper Hand was created by sports coaches to make sports training easier. Whether you conduct private and group lessons, host camps or clinics, or coach a team, Upper Hand allows you to configure the software to cater to your business offerings."
- Feature blocks: scheduling & registration (private lessons, classes, teams, clinics; capacity controls, waitlists); engagement (reminders, targeted messages, athlete mobile app); payments (accept payments, memberships and pricing plans, discounts, recurring billing); staff & payroll; facility & resource scheduling; retail & inventory; teams (rosters, schedules, payments); marketing campaigns; website builder (WebKit); AI analytics (Upper Hand AI); Camp Pulse (camps).
- **No video-analysis or skill-content delivery machinery observed** on the fetched pages. The coach→athlete channel is reminders/messages plus the athlete mobile app. This is the business-machinery pole of the Type.
- By-offering navigation: Private & Group Lessons, Camps & Clinics, Registration, Classes & Programs, Teams, Rentals — lesson-led at the individual pole.

### CoachNow (Layer A — root + coach-features page)

- Self-labels: "The Highest Rated Coaching App in the World"; "all-in-one coaching app/platform"; "Servicing Thousands of Academies, Camps, and Organizations Worldwide"; vendor-claimed scale "1 million+ coaches and athletes across 60+ sports in 140+ countries".
- FAQ definition: "combines video and image analysis, private communication, cloud storage, and automation so coaches and athletes can stay connected **before, during, and between sessions**"; "dedicated space for each athlete or team"; works for in-person AND remote coaching; memberships "for athletes, solo coaches, and multi-coach organizations".
- **Spaces** — the core container: "your training space to communicate one-on-one with your athletes … a secure, private channel dedicated solely to your athlete's improvement." Posts, video analysis, and feedback live in the Space.
- **Groups** — team/group channels with topics ("Scheduling", "Game day Plans", "Team Goals").
- Video analysis suite: annotation tools (angles, shapes, timers, text), voice-over, CoachCam (live rear-camera recording into feedback), Versus mode (side-by-side comparison), AI-enabled skeleton tracking, Live MultiCam (multi-angle simultaneous capture, Apple Watch remote capture), slow motion up to 240 FPS, timer tool, tags, document attachments.
- Cloud library: store and reuse "drills, models, practice plans, or any other media"; shoot in app, reuse from library, or upload.
- Automation & engagement: post/template scheduling, automated content sequences ("drip your content at a pre-determined cadence"), Lists/Smart Lists (message thousands; athletes auto-organized by in-app activity), main feed aggregating all Spaces/Groups with search, view tracking and read receipts, "messaging automations for when an athlete falls behind."
- Business & Facility Management (top tier): Scheduling & Facility Calendar ("Create and manage Facility and Client scheduling, directly in CoachNow. Students automatically receive confirmation and cancellation notifications via email and text"); Billing & Programming ("one-time packages or recurring subscriptions, purchasable directly on your Coach Profile … send invoices directly in CoachNow", via Stripe Connect); third-party integrations (club systems, calendars, launch monitors, on-course stats, video analytics, USGA handicapping).
- **Membership tiers (the natural experiment)**: ANALYZE ($9.99/M) = analysis + storage + communication; PRO ($49.99/M) adds MultiCam, unlimited Spaces/Groups, Smart Lists, automation, view tracking; ACADEMY ($899/Y) adds **Integrated Session Scheduling, Facility Calendar, Invoicing/Billing, third-party integrations**. Scheduling and billing are tier-gated add-ons; the lower tiers remain fully recognizable coaching platforms. Strong evidence that business machinery is common-but-not-definitional.
- Vendor's own framing: "video analysis – no matter how advanced – can't replace good coaching" — analysis serves the coaching relationship, not the reverse.

### V1 Sports — V1 COACH (Layer A — root + coach product page)

- Self-labels: "MORE THAN SWING ANALYSIS — Empowering golfers to improve their game. Supporting coaches in growing their business"; "The industry leader in video analysis is now your solution for building your business."
- Two-sided structure: **V1 GOLF** (athlete app: analyze swing, track progress, train on own with video tools; "connect with one of the world's best coaches right inside the app"; "come in and start working with a new coach from day one") + **V1 COACH** (coach side).
- V1 COACH features: "Video Analysis & Lesson Delivery — tools to capture, compare, and share swing analysis"; model-swings library ("hundreds of included model swings"); athlete data management ("Manage all your athlete data from one place"); send drills; chat with students inside the V1 GOLF app; branded experience; "AI Lesson Follow Ups — automatic recaps and reminders to keep students practicing"; V1CTOR AI assistant (replies "in your voice, 24/7").
- Demand layer: "Promoted to 100k+ Golfers — get in front of golfers looking for coaching"; "Pre-Qualified Golfer Leads — V1CTOR builds interest and hands off golfers when they're ready to commit to lessons."
- Additional services: **Billing & Scheduling** ("manage your offerings and schedules … a smooth and efficient booking process for both coach and athlete from within the V1 GOLF app") — packaged as an add-on service, not the core app; Custom Store (lesson packages, merchandise, affiliate links); website creation/hosting; marketing services; social-media services.
- Platform metric: "Lessons Delivered" counted alongside active athletes/coaches.
- Studio pole: V1 PRO Studio Software (in-studio teaching), V1 Paired (launch-monitor pairing), Team Solutions (baseball). Golf-first vertical with baseball second.

### OnForm (Layer A — root + coach product page)

- Self-labels: "The Ultimate Mobile Video Coaching Platform"; "a powerful sports coaching app that helps coaches elevate athlete performance through video analysis"; "the sports coaching app built to help you stay organized and help scale your business."
- Record → Analyze → Share workflow: capture in-app (5 recording modes, 1080p up to 240fps, manual shutter speed, auto-detect hands-free recording) or import; analyze (slow motion, frame-by-frame, drawing tools, voiceovers, side-by-side, 4-way player, AI skeleton tracking, 3D for golf); share ("Share videos with individual athletes, small groups or full teams in just a few taps"; "Broadcast messages to your entire database with lesson openings or weather updates").
- Relationship persistence: "athletes have a full library of videos, analyses, and chats to look back on to keep them improving all year long"; "Record voiceovers so athletes remember what they're working on between sessions."
- Organization: videos/athletes/teams organized with "titles, tagging, and collections"; automatic cloud backup; "Centralized Admin Tools — bulk invite students, manage staff, and organize multi-location academies."
- Remote coaching: "Coach students anywhere in the world. Send annotated video feedback asynchronously — they watch it on their own time."
- Athlete side: "Free if your coach is on Onform"; athletes record/review their own technique, receive annotated feedback, compare themselves over time.
- Demand layer: Golf Coach Directory (findacoach.onform.com).
- Scale span: "Whether you're a private instructor working with a handful of students or part of a large coaching organization training thousands."
- Adjacency: HIPAA-compliant platform; Physical Therapy/Medical sport page.
- Studio hardware: Multi-Cam MAX (fixed cameras, iPad as control room); sensor integrations (Full Swing KIT, Pocket Radar).
- **Booking/payments machinery NOT observed** on fetched pages. "Lesson openings" broadcasts imply a lesson concept; scheduling/payment machinery unverified. Sourcing limitation recorded.
- Competitive set self-named in a comparison blog: "Onform vs V1, CoachNow and Sportsbox" — confirms the market cluster.

### CoachUp (Layer A — boundary pole only)

- Consumer-side marketplace: "Train with the largest network of expert coaches"; "Find a Coach"; "Easy Booking & Payment — every coaching session can be booked in minutes through CoachUp and all financial transactions are securely processed online"; background checks; "Good-Fit Guarantee … 100% money-back guarantee"; "Coach With Us" (coach supply-side application); CoachUp U (collegiate athletes "legitimize their coaching business" through the platform).
- Primary user is the athlete/parent; the platform mediates discovery, booking, and payment. The coach is a supply-side participant, not the system's owner. This is marketplace territory, not the coach's practice system.

## Cross-product Comparison

| Structure | Upper Hand | CoachNow | V1 COACH | OnForm |
|---|---|---|---|---|
| Coach's client roster | client management + engagement + athlete app | Spaces per athlete + Groups + Lists/Smart Lists | "manage all your athlete data from one place" | athletes organized via titles/tagging/collections; bulk invite |
| Session/lesson as unit | private & group lessons scheduling (core) | Integrated Session Scheduling (Academy tier only) | lessons delivered (platform metric); Billing & Scheduling add-on | lessons referenced ("lesson openings"); machinery unverified |
| Coach→athlete exchange | reminders, targeted messages, athlete app | video analysis + posts + feedback in private Spaces | video analysis + online lessons + chat + AI follow-ups | video analysis + voiceovers + messages + chats |
| Video analysis suite | absent (pole) | deep suite | deep suite (heritage core) | deep suite |
| Payments / packages | memberships, pricing plans, recurring billing (core) | packages/subscriptions, invoicing (Academy tier) | Custom Store lesson packages (add-on service) | not observed |
| Self-service booking | core | Academy tier | add-on service | not observed |
| Reusable content library | not observed | cloud library (drills, models, practice plans) | model swings | video library + collections |
| Athlete-side app/access | mobile app for athletes | athlete role/app | V1 GOLF app | athlete app (free with coach) |
| Automated engagement | reminders, campaigns | post scheduling, drip sequences, view tracking | V1CTOR recaps/reminders | broadcasts |
| Demand generation | website builder, marketing campaigns | not observed | promoted leads, pre-qualified leads | Golf Coach Directory |
| Multi-coach / organization | facility/franchise tiers | Academy tier (multi-coach) | studio/team solutions | admin tools, multi-location academies |
| Team/group support | teams module | Groups | Team Solutions (baseball) | share to teams/groups |

Evidence-layer reading:

- **Layer B (cross-product commonality, 4/4):** the coach's managed athlete/client population; the coach→athlete exchange through the platform; the lesson/session as the organizing concept of delivered instruction; athlete-side access; engagement/communication tooling.
- **Layer B (3/4 or tier-gated):** self-service booking; payments/packages; multi-coach/organization support; team/group support; demand generation (3/4 in some form).
- **Layer A single-product facts:** CoachNow's tier gating (scheduling/billing only at top tier); V1's Billing & Scheduling as an add-on service; OnForm's missing booking/payments machinery; Upper Hand's missing video analysis. Together these four facts **block any attempt to make booking, payments, or video analysis definitional**.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (three jointly-held structures)

1. **The coach's client roster of record** — persistent identified athletes/students/clients held by the coach (or coaching organization) as the population under their care, each relationship carried in a per-athlete space/profile that accumulates the coaching exchange over time (videos, feedback, notes, sessions, payments). Remove → a video tool, a messaging app, or a booking page with no memory of who it serves (= contact/CRM list).
2. **The session/lesson as the unit of coached instruction** — discrete coaching events (private or group; in-person, or remote/on-demand) through which the coach delivers instruction and against which the practice is organized. Remove → one-way content publishing (course/channel territory) with no delivered-instruction unit.
3. **The coach→athlete exchange through the platform** — the platform is the direct channel through which the coach delivers coaching to the athlete: feedback, technique analysis (video being the dominant modern medium), drills/content, and communication — around and between sessions, in person or remotely. Remove → a generic appointment scheduler or contact manager.

Jointly-held load-bearing analysis:

- 1 alone = contact list / CRM
- 2 alone = a lesson calendar / booking page (generic appointment scheduling)
- 3 alone = a messaging or video-feedback tool
- 1+2 without 3 = a generic service-booking business tool (any appointment vertical)
- 1+3 without 2 = a remote content/communication relationship without delivered-instruction units (drifts toward online-course / online-coaching territory)
- 2+3 without 1 = anonymous lesson transactions (marketplace / one-off territory)

### L1 — Common Mature Structure (present in most sampled products; not definitional)

- self-service booking/scheduling with confirmations and reminders (Upper Hand core; CoachNow top tier; V1 add-on service; OnForm unobserved)
- payments: packages, subscriptions, invoicing (same distribution)
- video analysis suite: capture, slow motion, annotation, voice-over, side-by-side comparison (the delivery pole's signature capability)
- reusable content library: drills, model swings, practice plans
- athlete-side app/access: the athlete's own library, responses, self-recording
- automated engagement: reminders, follow-ups, broadcasts, view tracking
- group/team support
- multi-coach / organization support

### L2 — Variant / Optional Structure

- philosophy pole: delivery-first (CoachNow, V1, OnForm) vs business-first (Upper Hand)
- in-person vs remote/hybrid coaching emphasis
- solo coach vs multi-coach organization/facility (the org pole overlaps the academy seam)
- vertical depth: golf-first (V1) vs multi-sport (CoachNow, OnForm, Upper Hand)
- attached demand layer: coach directory (OnForm), promoted leads (V1); the full marketplace is a different Type (CoachUp)
- sensor/launch-monitor integrations (V1 Paired, OnForm Full Swing KIT/Pocket Radar, CoachNow launch monitors)
- PT/rehab adjacency (OnForm HIPAA, CoachNow PT/rehab)

### L3 — Vendor-specific (research notes only)

- V1CTOR AI assistant and lead-promotion machinery (V1)
- Upper Hand AI dashboard, WebKit website builder, Camp Pulse
- OnForm Multi-Cam MAX, 3D swing metrics, auto-detect recording
- CoachNow skeleton tracking, CoachCam, Smart Lists, tier pricing ($9.99/$49.99/$899)
- All numeric limits and prices stay here, not in the final document.

## Historical / Market-Sample Check (§24)

- **Paper-era private coach**: a 1980s tennis pro with an appointment book (sessions), a lesson-package card file (roster + money), a camcorder and VHS review sessions (delivery), and phone calls (exchange) satisfies all three L0 legs with no software. **Passes.**
- **Regional coaches**: cricket coaches, swim instructors, martial-arts instructors running private-lesson practices on the same shape. **Passes.**
- **Platform-native pole**: a golf pro teaching inside a launch-monitor-branded studio suite (V1 PRO-class) — same legs, different substrate. **Passes.**
- Conclusion: the L0 is era- and region-neutral. Video analysis and online delivery are era-current realizations of the exchange leg, not invariants; booking and payment machinery are commercial-layer realizations, not invariants.

## Vendor-specific / Rejected Findings

- **Video analysis is NOT definitional** — Upper Hand (a self-avowed coach platform) has none on its fetched pages; the paper-era coach satisfies the Type without it. It is the dominant modern medium of the exchange leg.
- **Booking/scheduling machinery is NOT definitional** — tier-gated at CoachNow, add-on at V1, unobserved at OnForm.
- **Payments/packages are NOT definitional** — same distribution; free tiers and cash-payment historical poles satisfy the Type.
- **Demand generation (directories, promoted leads) is NOT definitional** — present in 3/4 as optional layers; the full marketplace is a different Type.
- **Teams are NOT definitional** — group/team support is common but the 1:1 coach-athlete relationship is the center; team ops are Team Management Application territory.
- **Multi-coach organization support is NOT definitional** — the solo pole is the center of gravity; the org pole is the academy seam.
- **AI assistants (V1CTOR, Upper Hand AI) are era-current vendor machinery** — L3.
- **HIPAA compliance** — PT/rehab adjacency variant, not definitional.
- CoachUp-class marketplaces are NOT this Type (consumer-side; platform-mediated transactions; no coach-owned practice record).

## Boundary Findings

1. **vs Sports Academy Management (processed; FLAG DISCHARGED from this side)** — the academy pass hung its flag on Upper Hand's individual-coach pole. Resolution: **keep-both, scale/organizational-form seam**. The individual coach's client practice (roster of personal clients, lessons, packages, 1:1 exchange) vs the organization's program portfolio (multi-program offer, enrollment machinery, season/term rhythm, family accounts). Upper Hand legitimately spans both poles with one product (individual coach → franchise ladder), as does CoachNow (solo → multi-coach academies); the seam is center of gravity, and each leaf documents its own pole. The academy's enrollment/program machinery is not this leaf's core; this leaf's 1:1 exchange/Spaces machinery is not the academy's core.
2. **vs Personal Training Management (§28 sibling, UNPROCESSED) — FLAG HUNG for that pass**: the two are likely vertical siblings of the same practice spine (client roster + sessions + money + delivery). Market overlap is direct: CoachNow lists "fitness, PT/rehab" among its sports; OnForm ships a Physical Therapy/Medical page and HIPAA compliance; Upper Hand's individual pole says "coach, trainer, instructor". Proposed discriminator: domain center of gravity (sports skill instruction vs fitness training), with the expectation that many products serve both and family treatment may be warranted (same pattern as the class-management family flag).
3. **vs Online Fitness Coaching (processed 2026-09-08)** — keep-both, center-of-gravity seam. Online fitness coaching centers the training prescription composed by the coach and executed remotely by the client (programs→workouts→exercises, adherence review loop); this Type centers the coach-athlete relationship and coach-led skill instruction organized around lessons (technique feedback dominant). Remote video lessons (V1's online coaching) sit at the seam; the domain (fitness programming vs sports skill instruction) and the center (prescription-execution-review vs relationship-lesson-feedback) decide. Consistent with that pass's own boundary note ("PT-management territory" adjacent).
4. **vs AI Fitness Coach (processed 2026-09-06)** — clean seam: here a human coach is the delivering authority and the system is the coach's instrument; there the software itself composes and adapts the training. Hybrid human+AI tooling (V1CTOR drafting replies in the coach's voice) stays on this side — the human remains the coaching authority.
5. **vs Athlete Management System (processed)** — clean seam, consistent with that pass's row: AMS = the organization's management of athlete preparation across domains (S&C, medical, analytics); this Type = the coach's client practice and skill development. A coach using an AMS works for an organization; a coach using this Type runs their own practice.
6. **vs Sports Video Analysis (§28 sibling, UNPROCESSED) — FLAG HUNG for that pass**: capability-slice pattern (same as fitness-class-booking vs fitness-studio-management). The analysis suite is a standard capability inside coaching platforms (3/4 sampled); a standalone video-analysis product centers the tooling itself (often team/school-oriented). OnForm straddles: its analysis suite is deep (video-analysis territory) while its roster/directory/feedback-delivery layer is practice machinery (this territory). Proposed seam: the tool as the product's center vs the coach-athlete relationship system that contains the tool as one medium.
7. **vs Team Management Application (§28 sibling, UNPROCESSED)** — single-team operations (one roster, one schedule, one communication graph for a team) vs the coach's client practice (many 1:1 relationships, a business). Teams appear inside coaching platforms as a variant (CoachNow Groups, OnForm teams, Upper Hand teams module) — capability slice, keep-both expected.
8. **vs consumer lesson marketplaces (CoachUp-class; no dedicated directory leaf — marketplace territory)** — consumer-side discovery/booking/payment marketplace vs coach-side practice system. CoachUp's primary user is the athlete/parent; the platform owns the transaction and trust machinery (background checks, guarantee). Coaching platforms may attach a demand layer (OnForm directory, V1 promoted leads) while the center stays the coach's practice record. Boundary held.
9. **vs Nutrition Coaching Platform (processed)** — consistent with that pass's row: the nutrition process is the center there; here it is one content type at most inside the exchange.
10. **vs Tutoring Platform (§23, cross-family)** — structurally analogous 1:1 instruction practice (client roster, sessions, packages); domain differs (academic subjects vs sports skills) and tutoring platforms skew marketplace-shaped. Cross-family adjacent; no seam conflict.

## Uncertainties

- OnForm's booking/payments machinery is unverified (not observed on fetched pages; "lesson openings" broadcasts imply a lesson concept). The money/booking tier is held at common-not-definitional partly on this pole.
- Upper Hand's individual-coach pole is documented from product/feature pages; its help center was not fetched — operational flow detail (booking mechanics, package draw-down) asserted at product-page strength only.
- V1's Billing & Scheduling mechanics ("booking process … from within the V1 GOLF app") asserted at product-page strength; it is packaged as an add-on service and may be partially human-delivered.
- CoachUp's coach-side tooling was not researched; the marketplace boundary is drawn from the consumer-side evidence only.
- Vendor scale claims (CoachNow "1 million+ coaches and athletes", V1 "100k+ golfers") are marketing figures recorded here, not asserted in the final document.
- Whether the market converges on treating Personal Training Management and this leaf as one family (per Boundary Finding 2) is a decision for that pass.

## Final Synthesis

A Sports Coaching Platform is the **sports coach's client-practice system**: the coach-side system of record for a private instruction business. Its defining core is three jointly-held structures: the coach's client roster of record (persistent identified athletes/students, each relationship carried in a per-athlete space accumulating the coaching exchange), the session/lesson as the unit of coached instruction (private or group, in-person or remote), and the coach→athlete exchange through the platform (feedback, technique analysis — video dominant — drills, and communication, around and between sessions).

The market realizes the Type in two poles that share this spine: a **delivery-first pole** (CoachNow, V1, OnForm — per-athlete spaces, video analysis, communication, with business machinery tiered or add-on) and a **business-first pole** (Upper Hand — booking, payments, client engagement, with no analysis suite). Booking, payments, content libraries, athlete apps, automation, teams, and multi-coach organization support are the common mature layer; demand generation, sensor integrations, vertical depth, and PT/rehab adjacency are variants. The Type is bounded against the organization pole (Sports Academy Management), the remote-prescription pole (Online Fitness Coaching), the software-as-coach pole (AI Fitness Coach), the org-preparation pole (Athlete Management System), the tooling slice (Sports Video Analysis), and the consumer marketplace (CoachUp-class).
