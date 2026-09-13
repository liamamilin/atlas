# Research Notes — Workout Programming Application

## Research Goal

Understand what software sits under the directory leaf "Workout Programming Application" (§28 Sports, Fitness & Recreation, listed between "Online Fitness Coaching" and "Workout Tracking Application"): what the central artifact is, how it is composed, how it is delivered and reused, and where the boundary lies against the three §28 siblings that carry pre-hung joint-review flags into this pass (Online Fitness Coaching, AI Fitness Coach, Endurance Training Platform), plus Workout Tracking Application (unprocessed sibling), Personal Training Management, Fitness Assessment Application, and the gym/venue management leaves.

## Initial Boundary

- **Hypothesis:** the Type centers the *program artifact* — an authored, reusable composition of prescribed exercise sessions — as opposed to the coaching relationship (Online Fitness Coaching), the executed-session log (Workout Tracking), the software-as-coach loop (AI Fitness Coach), or the endurance training process loop (Endurance Training Platform).
- **Pre-hung flags to discharge this pass:**
  1. online-fitness-coaching (processed 2026-09-08): "centers the program *artifact* — authoring quality training plans as the deliverable, for print, teams, or self-use. Here the program exists as a client-bound, delivered, revised object inside a held relationship… A programming tool has no client roster and no review loop. Expect product blending (coaching platforms ship strong builders)."
  2. ai-fitness-coach (processed): "who adapts the plan — software (AI coach) vs human trainer/coach (programming, online coaching) vs nobody (tracker/static plan library)… a gradient, not a wall; flagged for joint review when those leaves are processed."
  3. endurance-training-platform (processed): "Programming prescribes workouts (sets/reps or intervals) but the endurance platform closes the loop: prescription + capture + accumulated state + season periodization with endurance semantics… Remove the record-and-accumulate loop → programming tool."
- **Nearest neighbors:** Workout Tracking Application (sibling, unprocessed), Online Fitness Coaching, AI Fitness Coach, Endurance Training Platform, Personal Training Management, Fitness Assessment Application, Gym Management System / Fitness Studio Management, Athlete Management System, Sports Coaching Platform. Also noted: clinical exercise prescription (home-exercise programs) has no directory leaf; the clinical pole is probed through ExorLive.

## Research Questions

1. What is the central object of these products, and what is it composed of (exercise, prescription, session, day, week, block/phase)?
2. What authoring mechanics exist (builders, templates, libraries, duplication, views)?
3. What prescription semantics does the strength-training domain use (sets/reps/load/rest/intensity; absolute vs percentage-of-max load)?
4. How are programs delivered (athlete app, shared weight-room tablet, print/export, marketplace) and to whom (individual, team, roster, self, patient)?
5. How does execution relate to the program? Is there a plan-vs-actual loop, and how strong is it? (boundary vs tracking and vs endurance platform)
6. Is a recipient roster a held client relationship? (boundary vs online coaching)
7. Who is the author — human coach, template publisher, algorithm? (variant axis)
8. What is the displaced baseline the products themselves name? (historical check)
9. Does the clinical exercise-prescription pole belong to this Type or to a different one?
10. Where exactly do the boundaries to coaching, tracking, AI coach, and endurance platforms sit, and can the three pre-hung flags be discharged from this side?

## Representative Products

| Product | Pole / customer level | Philosophy | Documentation access |
|---|---|---|---|
| TeamBuildr (Strength) | team/institutional S&C (high school, college, pro, tactical) | tool, not authority — "doesn't tell you how to program"; heavy team deployment | product site + Strength platform + features page fetched (A) |
| TrainHeroic | coach 1:1 + teams, marketplace | "sending workouts isn't the same as coaching" — programming as coaching infrastructure | product pages fetched (A−); help center timed out (also in the 2026-09-08 coaching pass) |
| BridgeAthletic | clubs/orgs, pro & collegiate, independent trainers | precision program design; blocks/library builder; test→program loop with VALD | product root fetched (A−); help center timed out |
| Boostcamp | consumer self-use | program library as free public content; follow-and-log in one app | product site + FAQ + comparison pages fetched (A−) |
| ExorLive | clinical prescription (physio/clinic/municipality/education, Nordic market) | exercise-library → program → share, healthcare context | root + "Get started" help article fetched (A−); article bodies timed out |

## Sources

- TeamBuildr — https://www.teambuildr.com/en/ , https://www.teambuildr.com/platform-strength , https://www.teambuildr.com/features (fetched 2026-09-09). Support subdomain: https://support.teambuildr.com/hc/en-us returned 404; support root not further pursued (support is offered by email per footer).
- TrainHeroic — https://www.trainheroic.com/ , https://www.trainheroic.com/coach/ (fetched 2026-09-09). Help center https://support.trainheroic.com/hc/en-us timed out (second failure across passes; abandoned).
- BridgeAthletic — https://www.bridgeathletic.com/ (fetched 2026-09-09). Help center https://intercom.help/bridgeathletic/ timed out (abandoned).
- Boostcamp — https://boostcamp.app/ (fetched 2026-09-09; includes FAQ and vendor-authored comparison pages /vs/strong, /vs/hevy, /vs/fitbod, /vs/jefit).
- ExorLive — https://www.exorlive.com/ and help article "Get started" https://support.exorlive.com/hc/en-gb/articles/360000576589 (fetched 2026-09-09). Deeper article bodies (create-program, share) timed out.
- Sibling documents consulted for boundary continuity: applications/online-fitness-coaching.md, applications/ai-fitness-coach.md, applications/endurance-training-platform.md, research/online-fitness-coaching.md, STATUS.md boundary entries.

## Product Observations

### TeamBuildr (Strength)

Evidence layer: A (official product pages, features page, FAQ).

- Positioning: "Strength and Conditioning Software for Strength Coaches, Teams & Gyms"; vendor-stated 5,500+ organizations since 2012; segments: professional teams, colleges, high schools/PE, gyms & facilities, tactical (military, fire).
- Product split: **Strength** = "workout programming and athlete management"; **AMS** = paid add-on athlete-monitoring layer ("pain mapping, wellness, readiness, soreness, load monitoring… prescribed versus completed volume"); **OS** = separate gym member management (scheduling, payments, members). The programming Type observed here is the Strength product.
- Programming model: "Build percentage-based, velocity-based, and custom periodized programs for individuals, teams, or entire facilities." Authoring views: "date-based, free-form, and day-stacking views, drag-and-drop, keyboard shortcuts." Percentage-based loading "adjusts automatically to each athlete's maxes" (custom 1RM tracking). Annual Planner at the top tier.
- Authorship philosophy: "TeamBuildr doesn't tell you how to program, we give you full control whether you're working with one athlete or one hundred." AI statement: "technology should strengthen the coaching profession – not compete with it… Human expertise first. Technology in support."
- Library & templates: "1,000+ exercises with video demos, plus custom exercise creation and reusable templates."
- Team deployment: "Manage distinct programs for football, basketball, soccer… using Groups and Calendar features. Build a master template once and deploy it across every team with adjustments."
- Delivery surfaces: free athlete mobile app ("view workouts, log sets, upload video, team feed"); **Weight Room View** — shared station tablet, vendor-stated 4–8 athletes per tablet, "no phones, no paper"; TV displays at higher tiers.
- Reporting: "16+ exportable reports" (progress, maxes/PRs, wellness questionnaires, workout completion rates, activity; PDF/CSV/Excel export).
- Evaluations module: custom testing protocols, combine-style testing days, results feed reporting.
- Commerce: "use the payments portal marketplace for automated program delivery" (selling programs).
- Displaced baseline named by vendor: "replaces paper cards, whiteboards, and Excel systems."
- Pricing (vendor-stated, research-notes only): Silver $90/mo up to 50 athletes → Platinum Pro $280/mo up to 1,000 athletes; unlimited coach profiles at all tiers.

### TrainHeroic

Evidence layer: A− (official product pages; help center unreachable).

- Positioning: "The Premier Platform for Strength Coaches… Deliver a premium athlete experience, manage remote and in-person clients in one place." "Where great programming becomes great coaching. **Sending workouts isn't the same as coaching.**"
- Tools: "Teams and 1:1 — coach 1:1 or group clients into teams for easy program delivery and group communication"; video review with feedback; **"Customizable library — create and organize workouts, circuits, and full programs—or use ours"**; client tracking ("compliance, progress, programming status"); invite-based onboarding; white-label branding.
- Commerce: "Turn your programming into revenue — reach more athletes and sell training programs through the TrainHeroic Marketplace"; athlete app on iOS/Android; leaderboards.
- Pricing (vendor-stated, research-notes only): per-athlete tiers $9.99 (1 athlete) → $399.99/mo (1,000 athletes); assistant coaches add-on.
- Displaced baseline (customer quote on vendor site): "I won't go back to the old pen and paper workout log for me or my athletes."
- Note: the same "sending workouts isn't the same as coaching" sentence is quoted in the online-fitness-coaching pass — TrainHeroic straddles the programming/coaching seam; its help center has now failed twice across passes, so its mechanics stay at product-page strength.

### BridgeAthletic

Evidence layer: A− (official product root; help center unreachable).

- Positioning: "Strength and Conditioning Software for the Digital Age — design custom programs, train in-person or remotely, and track performance." Product named **BridgeTracker**. Segments: athletic organizations (pro, collegiate, performance centers, national teams), independent trainers, gyms & clubs, tactical, youth.
- Authoring: "The No-Spreadsheet Solution for Building Better Programs… Programs… require precision design. Leverage the best builder and exercise library in the business. Build out plans from scratch or start with templates to deliver the perfect program in minutes."
- Delivery: "Deliver workouts directly to your athletes' phone or display them on tablets in the weight room. Make changes, send surveys and communicate with videos, images and messages, all in real-time."
- Plan-vs-actual (customer quote on vendor site): "With prescribed vs. actual reporting, I can analyze how accurately I am predicting future workloads… Am I over-prescribing or under-prescribing?"
- Multi-practitioner (customer quote): "supports a multidisciplinary approach for athletes who see multiple practitioners, as everyone can be engaged in the athlete's program."
- Bridge + VALD: "Test. Build. Train. Where measurement meets programming. VALD captures objective data, Bridge turns it into precise programming and closes the loop."
- Displaced baseline (customer quote): "Switched from Google Sheets."
- Vendor-stated scale figures (5M+ workouts, 6,000+ teams, 200k+ athletes) — research-notes only.

### Boostcamp

Evidence layer: A− (official product site incl. FAQ and vendor-authored comparisons).

- Positioning: "The Free Workout App Lifters Actually Use — a free workout tracker and program app: 11,000+ programs, including coach-designed programs" from named coaches and communities (vendor-stated figures). Programs carry goal tags, days/week, join counts, ratings.
- Core consumer flow (vendor's "How it works"): 1) "Pick a program that matches your goals" (browse by goal, experience, schedule); 2) "Follow your workout, set by set — every session is laid out for you: exercises, sets, reps, and rest times. Log your weights, hit your targets, and let **auto-progression** handle the math"; 3) "Track progress and hit PRs" (analytics, estimated 1RMs, history).
- Authoring: "**AI Program Builder** — build your own with AI assistance or create from scratch. Set your split, exercises, progression — and share it with others."
- Boundary statements the vendor itself draws (valuable independent seams):
  - vs Strong/Hevy: "Strong and Hevy are workout loggers you build your own routines around; Boostcamp… adds a library of 11,000+ programs."
  - vs Fitbod: "Fitbod generates each session algorithmically… Boostcamp gives you a personalized workout program."
- Consumer pole facts: no roster, no teams, no coach delivery; self-follow; Pro subscription adds exclusive coach programs and analytics; no Apple Watch/Wear OS app (vendor FAQ).
- The product self-describes as "workout tracker **and** program app" — the market's consumer end blends the two Types; the center of gravity here is the program ("Every workout is planned for you").

### ExorLive

Evidence layer: A− (official root + one Tier-1 help article).

- Positioning: "Create exercise programs quickly and easily from over 8,000 exercises with video" (vendor-stated figure). Solutions packaged for **Municipality, Clinic, Fitness and sport, Education** — a Nordic/European exercise-prescription product sold into healthcare and public sector as well as fitness.
- Documented flow (help-center "Get started", Tier 1): **1. Find Exercises → 2. Create an exercise program → 3. Share an exercise program.** Print/PDF path visible on the help page.
- The three-step flow (library → program → share) is structurally identical to the strength-market products, applied to clinical and municipal contexts (patient exercise programs).
- Deeper article bodies timed out; mechanics stay at TOC strength.

## Cross-product Comparison

| Dimension | TeamBuildr | TrainHeroic | BridgeAthletic | Boostcamp | ExorLive |
|---|---|---|---|---|---|
| Central artifact | Periodized program for individuals/teams | Programs/workouts/circuits in a library | Custom program ("precision design") | Program (11k+ library; self-built) | Exercise program (patient/client) |
| Composition unit | Exercise w/ sets-reps-load; % of athlete max | Exercise w/ prescription; circuits; video demos | Exercise w/ prescription from library | Exercise + sets/reps/rest | Exercise (8k+ w/ video) |
| Time structure | Calendar or dateless views; day-stacking; annual planner | Sessions scheduled to athlete calendar | Plans built session by session | Program = N days/week over weeks | Program session(s) per patient |
| Author | Coach (full control positioning) | Coach | Coach/trainer | Coach-published programs; self + AI assist | Clinician/trainer |
| Recipient model | Individuals, teams/groups, whole facilities | 1:1 clients + teams; marketplace buyers | Athletes; multi-practitioner around one program | Self (consumer) | Patient/client |
| Delivery | Mobile app; shared weight-room tablet; TV; marketplace | Athlete app; marketplace | Athlete phone; weight-room tablets | Same app (self-follow) | Share (app/print/PDF) |
| Execution capture | Athletes log sets; completion reports | Athlete logging; compliance/status tracking | Prescribed vs actual reporting | Set-by-set logging; auto-progression | Adherence implied; not verified |
| Plan-vs-actual | AMS add-on (prescribed vs completed volume) | Programming status + compliance | First-class (customer quote) | Log vs targets (consumer grain) | Not verified |
| Library | 1,000+ w/ video; custom exercises; templates | Library "or use ours" | "Best builder and exercise library" (vendor claim) | Exercise demos w/ form videos | 8,000+ w/ video |
| Commerce | Payments portal + marketplace | Marketplace revenue stream | B2B SaaS | Free + Pro subscription | B2B SaaS (clinic/municipality) |
| Displaced baseline (named by vendor/quote) | "paper cards, whiteboards, Excel" | "pen and paper workout log" | "Google Sheets" | "spreadsheet" (reviews) | (paper exercise programs — not vendor-named; not asserted) |

**Layer-B (cross-product commonality) findings:** exercise library as composition vocabulary (5/5); program as multi-session composition on a time structure (5/5); prescription parameters distinct from recorded values (4/5 verified); delivery-as-a-unit to one/many executors (5/5); reusable templates/libraries of programs (4/5 verified); execution logging with completion/prescribed-vs-actual reporting (4/5 verified, grain varies); percentage-of-max load resolution per executor (2/5 verified — strength-market pattern, not assumed universal); marketplace/commerce for programs (3/5); teams/groups for bulk delivery (3/5 — market-segment dependent); shared weight-room hardware surfaces (2/5 verified).

## L0 / L1 / L2 / L3

### L0 — Defining Invariant (deliberately small)

1. **Exercise-based prescription unit** — every element of the plan names an exercise and specifies how it is to be performed (volume, load, rest, effort parameters; exact fields vary) — instructions authored *before* execution. Remove → a calendar or content library, not programming.
2. **The program artifact** — a durable, named, editable composition of multiple prescribed sessions arranged across a time structure (days/weeks/phases), existing as one unit that precedes and survives any particular execution. Remove → a single workout template (not a program) or a log of what happened (tracking).
3. **Portability as a unit** — the program can be handed to its executor(s) as one thing — assigned to an individual, deployed across a team, published/sold, printed/exported, or followed by its own author — and can be reused or revised as a whole. Remove → session-by-session chat coaching or an ephemeral generated workout.

Jointly-held: 1 alone = an exercise library; 2 without 1 = an empty calendar/plan container; 2+1 without 3 = a private document (arguably still the artifact but not the *application* family observed — every sampled product makes portability operational through some delivery mechanism; held as load-bearing at the family level, with self-follow as the degenerate-but-valid case).

### L1 — Common Mature Structure

- exercise library with instruction media (video/images) and custom exercise creation
- program/session templates and reusable libraries; duplication/cloning as the standard authoring accelerator
- percentage-of-max loading resolved per executor against tracked maxes; max/PR tracking
- delivery surfaces: personal mobile app, shared weight-room tablet/TV view, print/PDF export
- execution logging by the executor; completion and prescribed-vs-actual reporting
- groups/teams for bulk assignment; individual overrides on a shared program
- communication between author and executors (messaging, video, notes)
- commerce: selling programs (marketplace/payments portal) at the coach-facing pole

### L2 — Variant / Optional Structure

- periodization methodology depth: blocks/mesocycles, annual planner (segment-dependent)
- date-based vs dateless authoring views
- auto-progression algorithms (consumer pole: load adjusts per logged performance)
- AI-assisted program drafting (emerging; exists alongside human authorship)
- clinical realization: patient exercise programs from clinical libraries, healthcare packaging
- wellness/readiness monitoring modules; testing/evaluation modules (adjacent-Type capabilities feeding programming)
- hardware integrations: VBT devices, force plates, GPS
- facility/class programming (a venue publishing the day's workout to members) — lightly held; observed in sibling research, not directly this pass

### L3 — Vendor-specific (research notes only)

- TeamBuildr: day-stacking view; Weight Room View (4–8 athletes/tablet, vendor-stated); 16+ named reports; Silver→Platinum Pro tiers ($90–$280/mo, 50–1,000 athletes, vendor-stated); Strength/AMS/OS product split; Locker Room templates; "AI alongside coaches" manifesto.
- TrainHeroic: Marketplace mechanics; Coach Playbook; per-athlete pricing ($9.99–$399.99/mo vendor-stated); assistant-coach add-on; "sending workouts isn't the same as coaching" tagline.
- BridgeAthletic: BridgeTracker name; Bridge + VALD "Test. Build. Train." loop; Game Plan learning-content module; SOC 2 / HIPAA-aligned posture; vendor scale counts.
- Boostcamp: 11,000+ programs / 130+ coach-designed (vendor-stated); named coach catalog (Wendler, GZCL, r/Fitness); Live Activities support; Pro tier contents; vendor-authored vs-comparison pages.
- ExorLive: Municipality/Clinic/Fitness/Education packaging; 8,000+ exercise count (vendor-stated); Nordic market focus; developer API/integrations.

## Vendor-specific Findings

- TeamBuildr's Strength/AMS/OS split is itself evidence for the boundary web: programming (this Type), athlete monitoring (Athlete Management System territory), and gym operations (Gym Management territory) are sold as separable products — the market itself treats them as distinct centers.
- Boostcamp's own comparison pages are an unusually explicit market-drawn seam: "loggers you build your own routines around" (tracking) vs "generates each session algorithmically" (AI-generation pole) vs a program library and builder (this Type).
- TrainHeroic's tagline ("sending workouts isn't the same as coaching") is the coaching-side critique of this Type's one-way delivery — the two Types coexist in one market and vendors sell the difference.

## Boundary Findings

1. **vs Workout Tracking Application (sibling, unprocessed).** The tracker's unit of record is the executed session (what the user did); the programming application's unit of record is the prescribed artifact (what is to be done, composed before execution). Both blend at the edges: trackers ship "routines" builders; programming products ship logging. Boostcamp's own copy names the seam ("workout loggers you build your own routines around" vs program library). Seam = center of gravity. Remove the composed-plan-first artifact → tracker; the "routines" capability inside a tracker does not move it into this Type. To be flagged for the future workout-tracking pass.
2. **vs Online Fitness Coaching — joint-review flag DISCHARGED.** Discriminator ratified from this side: the programming Type centers the *artifact*; delivery may be one-way (team deployment, marketplace sale, print, self-follow) and no held client relationship or review loop is required — a team roster or a marketplace buyer is a distribution target, not a managed client. The coaching Type centers the *relationship loop* (client record + delivered prescription + coach review/adaptation). Blending confirmed as expected: coaching platforms ship strong builders (Trainerize master programs, TrueCoach programs — per the 2026-09-08 pass), and this pass's TrainHeroic sits on the gradient with its messaging/compliance layer. Keep-both; the capability-layer overlap is capability-tier packaging, not a Type collapse.
3. **vs AI Fitness Coach — joint-review flag DISCHARGED.** The who-composes/who-adapts test holds from this side: here the program is a composed artifact whose author is a human, a template publisher, or (at the emerging edge) an AI drafting assistant — but the artifact then governs execution as written; in the AI-coach Type the software itself continuously decides and adapts the plan for one trainee. Gradient confirmed (auto-progression, AI builders, adaptive plan products sit between; Boostcamp's own Fitbod contrast is market evidence). Keep-both.
4. **vs Endurance Training Platform — sibling judgment ratified from this side.** The endurance platform closes the loop: plan-of-record + captured execution + accumulated training state + season periodization with endurance semantics (thresholds/zones/load). This Type composes prescriptions with gym/strength semantics (exercise × sets × reps × load schemes) and treats capture as a reporting capability, not an accumulated-state system. Remove the record-and-accumulate loop from the endurance platform → a programming tool; add accumulated state and endurance semantics → endurance platform. Overlap exists (both prescribe before execution; endurance products ship structured workout builders) — capability overlap, distinct centers.
5. **vs Personal Training Management.** Business operations (appointments, packages, billing, staff) vs the program artifact. Unprocessed sibling; no direct evidence gathered this pass; seam noted for that pass.
6. **vs Fitness Assessment Application.** Testing/evaluation modules exist inside programming products (TeamBuildr Evaluations; Bridge+VALD "Test. Build. Train.") — assessment produces the reference values (maxes, baselines) that prescription consumes. Assessment = protocol + evaluation; programming = prescription artifact. Distinct Types feeding each other.
7. **vs Gym Management System / Fitness Studio Management / Athlete Management System.** TeamBuildr's own OS/AMS split demonstrates the market's separation: member operations and athlete monitoring are separate products from programming.
8. **Clinical exercise prescription pole (no directory leaf).** ExorLive's structure (library → program → share, with print/PDF) is structurally this Type applied to clinical/municipal contexts. No clinical-exercise-prescription leaf exists in the directory; held here as a variant/edge realization rather than forcing a new leaf. If a future pass needs it, it would be a domain-bound sibling (same pattern as the water-sports genus observation).

## "Remove what to become another Type" judgments

- remove the composed multi-session artifact → Workout Tracking Application (log-first) or a calendar
- add the held client relationship + review/adaptation loop → Online Fitness Coaching
- let software continuously compose/adapt for one trainee → AI Fitness Coach
- add accumulated training state + endurance semantics (thresholds/zones/load, season arc) → Endurance Training Platform
- center appointments/packages/billing → Personal Training Management
- center members/facility/class operations → Gym Management / Fitness Studio Management
- add protocol + scoring + norms → Fitness Assessment Application

## §24 Historical / Market-Sample Check

Would older, regional, platform-native products still fit? Yes:

- Paper program cards and whiteboard programs in weight rooms — exercise prescriptions composed into multi-session artifacts, copied per athlete, posted for a team. TeamBuildr itself names these as its displaced baseline ("replaces paper cards, whiteboards, and Excel systems").
- Excel / Google Sheets program templates — the modern coach's incumbent; BridgeAthletic and Boostcamp customers name spreadsheets as what they switched from; spreadsheets satisfy the defining core exactly (exercise rows, prescribed values, weeks as columns, copy-paste reuse, printout distribution).
- Printed PDF plans and book-form training programs (marketplace-precursor) — the artifact with print as the delivery mechanism.
- No cloud, no athlete app, no analytics, no marketplace is required by the defining core — all of those are L1/L2.

**Check passes.** The definition is written at the artifact level, not at the SaaS-delivery level.

## Uncertainties

- TrainHeroic and BridgeAthletic help centers were unreachable (timeouts; TrainHeroic failed in two independent passes). Their authoring mechanics are documented at product-page strength only; no operational claims asserted from them.
- ExorLive deeper help-article bodies timed out; its create/share mechanics are at TOC strength (the three-step flow is Tier-1 documented).
- Program *versioning* semantics (edit-in-place vs re-delivery as new version) could not be verified uniformly across products; kept as a low-strength observation.
- Facility/class programming (venue publishes the day's workout) was not directly observed this pass; held lightly as an L2 variant from sibling-pass evidence (SugarWOD in fitness-studio-management research).
- Adherence/completion semantics at the clinical pole were not verifiable from reachable sources.
- Whether the clinical pole should eventually be a separate leaf is a human taxonomy judgment; recorded as a boundary issue rather than resolved unilaterally.

## Final Synthesis

A Workout Programming Application is best understood as **the authoring-and-delivery application for the training program as an artifact**: a named, durable composition of prescribed exercise sessions — each exercise carrying performance parameters (sets, reps, load scheme, rest, effort) — arranged across a time structure, authored before it is executed, and portable as a unit: assignable to one executor or many, deployable to a team, publishable or sellable, printable/exportable, or followed by the author personally. The exercise library is the vocabulary; templates and duplication are the accelerators; percentage-based load resolution against tracked maxes is the strength market's signature prescription mechanic; execution capture exists as reporting (completion, prescribed-vs-actual) but the accumulated-state loop of endurance platforms and the held-relationship loop of coaching are both absent from the core. The defining core is deliberately small (exercise-based prescription + the multi-session program artifact + portability as a unit) so that paper cards, spreadsheets, printed plans, team S&C platforms, coach marketplaces, consumer program-library apps, and clinical exercise-prescription tools all fit it, while tracking-first, coaching-first, AI-coach-first, and endurance-process-first products stay outside it.
