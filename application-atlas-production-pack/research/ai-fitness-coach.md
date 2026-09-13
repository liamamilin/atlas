# Research Notes — AI Fitness Coach

## Research Goal

Understand what an "AI Fitness Coach" application actually is as an Application Type: what the software does instead of a human coach, what objects and loops make it up, how personalization and adaptation really work, and where its boundary lies against Workout Programming Application, Workout Tracking Application, Online Fitness Coaching, Wearable Fitness Platform, and sport-specific training applications.

## Initial Boundary

Initial hypothesis (before research):

- Core use: an automated system plays the coach role for an individual trainee — assess the user, generate a personalized training plan, guide workout execution, capture performance/feedback, and adapt the plan over time.
- Primary users: individual consumers training for strength, muscle, weight loss, endurance, or general fitness; also embedded in premium home-gym hardware.
- Nearest neighbors: Workout Programming Application (human trainer authors programs for clients), Online Fitness Coaching (human coach delivers coaching remotely), Workout Tracking Application (log-first, no plan generation), Wearable Fitness Platform (data/monitoring first), Running Application (sport-specific), Nutrition Coaching Platform (food, not training).
- Likely boundary test: **who performs plan generation and adaptation** — software (AI coach), a human coach (programming/online coaching), or nobody (static plan library / tracker).
- Unknowns: how "AI" is realized per product (rules/algorithm vs ML vs conversational LLM), plan granularity (per-session vs multi-week journey vs daily refresh), how much user control exists, whether nutrition is in scope, whether human-in-the-loop hybrids belong here.

## Research Questions

1. What does the coach produce — a single workout, a weekly plan, or a multi-week journey?
2. What inputs drive personalization (goals, experience, equipment, schedule, performance history, recovery, wearables)?
3. Where does adaptation happen — per session, per week, per day, in real time?
4. What are the core objects (profile, goal, plan/journey, workout/session, exercise, set, feedback, progress metric)?
5. What does the "AI" actually do (generation, progression, substitution, form feedback, conversational assistant)?
6. How much control does the user have over the AI's decisions (swap, skip, regenerate, adapt)?
7. What rules matter (equipment constraints, recovery-aware rotation, safety/medical disclaimers)?
8. What interfaces does the user face (onboarding, today view, workout player, plan view, progress, chat)?
9. Where is the boundary vs human-coached and tracking-first products?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy | Customer tier | Why selected |
|---|---|---|---|
| Fitbod | algorithmic per-session workout generator (strength-first) | consumer subscription | clearest "AI as plan generator" pure-play; strong official FAQ |
| Freeletics | adaptive multi-week "Training Journey" with a coach persona | consumer subscription | explicit vendor statement that the Coach is AI, not a person; journey-level adaptation |
| Tonal | hardware-embedded AI coaching (adaptive resistance + AI assistant) alongside human-coach video programs | premium hardware + membership | different surface, different price tier, human+AI hybrid structure |

Boundary probes (not primary samples): Whoop (wearable platform with an AI coach add-on — support site unreachable, dropped), Future / Runna (human-coach-led hybrids — not fetched; used only as categorical contrast).

## Sources

All fetched 2026-09-06.

### Freeletics (Tier 1 — official Help Center, reachable)

- Help Center root: https://help.freeletics.com/hc/en-us (category structure: Training / Nutrition / Community)
- "Get started with Freeletics Training": https://help.freeletics.com/hc/en-us/articles/115004675229
- "Adapt your Bodyweight training session": https://help.freeletics.com/hc/en-us/articles/360003933780
- "Can I talk to the Coach?": https://help.freeletics.com/hc/en-us/articles/360004957019

### Fitbod (Tier 2 — official product pages + official FAQ; help center unreachable)

- Homepage: https://www.fitbod.me/
- FAQs: https://fitbod.me/faqs/
- Limitation: support.fitbod.me and fitbod.zendesk.com both failed (transport errors, 3 attempts total). FAQ page is official and operationally detailed, so treated as Tier 1.5; precise numeric claims kept in these notes only.

### Tonal (Tier 1 — official knowledge base, reachable; main support subdomain blocked)

- Homepage: https://www.tonal.com/
- Support root: https://knowledge.tonal.com/s/ (support.tonal.com returned 401; knowledge.tonal.com used instead)
- Features & Functions category: https://knowledge.tonal.com/kb/en/features-functions-435874
- "Introducing Tia, Your Tonal Intelligent Assistant": https://knowledge.tonal.com/kb/guide/en/introducing-tia-your-tonal-intelligent-assistant-wvwQCWAhEk/Steps/5185269
- "Your Daily Lift": https://knowledge.tonal.com/kb/guide/en/your-daily-lift-A8ae2bsYli/Steps/4248520

### Dropped sources (network limitation)

- support.whoop.com — JS-rendered error page (1 attempt); wearable-coach boundary argued structurally, not vendor-specifically.
- support.tonal.com — 401 (2 attempts); replaced by knowledge.tonal.com.
- support.fitbod.me / fitbod.zendesk.com — transport errors (3 attempts); replaced by fitbod.me FAQ.

## Product Observations

### Product A — Freeletics (evidence layer A: direct official docs)

Key observations:

- Onboarding: register → answer onboarding questions → (with subscription) choose a **Training Journey** "according to your fitness goals and preferred training modality" → indicate **training days, available equipment, running preferences** → Coach generates the first workout.
- Adaptation cadence: "The Coach will be adjusting your training plan based on your performance and feedback after each session."
- The coach is explicitly not human: "The Freeletics Coach is not a real person that you can talk to. The Coach is a digital program that uses the state of the art artificial intelligence to adjust your training plan to your goals, progress, strengths and weaknesses throughout your fitness Journey."
- Journey families: Bodyweight, Weights, Running (and hybrid journeys mixing them). Journeys have adjustable preferences.
- Per-session adaptation ("Adapt session"): user can regenerate the session with constraints — limited time, no equipment, no space, can't run, need quiet training, want a different session, exclude up to two body areas, change difficulty (easier/harder). Safety note in the exclusion option: never use with possible strain/joint pain/injury; "When in doubt, always see a doctor!"
- Exercise alternatives can be chosen; exercises can be excluded from the journey; skill progression paths exist (can be blocked).
- Logging: coach workouts can be logged manually; exercises/workouts/runs outside the journey can be logged; sync from other apps; Strava, Apple Health, Health Connect, Apple Watch integrations.
- Progress/gamification: Daily Athlete Score (DAS), points/levels/Stars, "Perfect weeks" and streaks, weekly training update statistics.
- Free tier exists without the Coach: user assembles training manually from a library (God Workouts, single exercises, runs) — i.e., the same app without AI plan generation is a workout library/tracker.
- Separate Nutrition product with its own "Coach" (meal plans, coach week, food preferences) — sold as a separate subscription/bundle.
- Community features (forum, network, before/after pictures) are a separate pillar.

### Product B — Fitbod (evidence layer A: official homepage + FAQ)

Key observations:

- Positioning: "personalized strength training app that delivers fully customized workouts based on your goals, fitness level, and available equipment"; built "exclusively for resistance and strength training."
- Personalization inputs (official FAQ): "fitness level, performance history, recovery status, available equipment, and training goals. The result is a plan that adapts with you; session by session."
- Machine learning description (official FAQ): "the app's algorithm learns from your performance data, like reps, sets, fatigue, and rest, to dynamically adapt and recommend the appropriate future workouts."
- Progressive overload is the stated organizing principle of the algorithm; recovery-aware muscle rotation ("rotates muscle groups intelligently, prioritizing fresh muscle groups").
- User control: set preferred workout duration (e.g., 30/45/60 min presets); switch goals anytime (strength, hypertrophy, circuit training, general fitness, powerlifting, olympic weightlifting) and "Fitbod will automatically update your training plan"; customize equipment settings (bodyweight-only possible); skip or manually add exercises; substitute any exercise (injury/mobility) — "The app will begin learning your preferences over time."
- Guidance: every exercise has a video demo + written coaching cues; warm-ups and cooldowns integrated; not a cardio app (conditioning movements only).
- Progress: PRs, estimated strength, volume trends, training streaks.
- Integrations: Apple Health, Fitbit, Garmin, Strava; Apple Watch / Wear OS companions; offline mode (generated workout usable offline).
- Platforms: iOS, Android; web only for onboarding. Consumer subscription (monthly/annual; exact prices in notes only).
- No nutrition module; no human coach; no community pillar.

### Product C — Tonal (evidence layer A: official homepage + knowledge base)

Key observations:

- Surface: wall-mounted smart home gym (digital weight machine) + mobile companion app; membership required; household accounts ("unlimited accounts").
- Hardware AI: "Tonal learns your strength and sets the optimal resistance for every rep, increasing in as little as one-pound increments" — adaptive resistance; automatic progress tracking; strength insights.
- Human-coach layer: video **Programs** led by named human coaches; "Coaches" is a first-class navigation section. So Tonal combines human-authored programs with AI features.
- **Tia** (intelligent assistant, chat-style): "Ask for workout recommendations, create custom workouts, or get insights into your progress, all tailored to your goals, preferences, and training history." Positions itself against "knowing what to do next."
- **Your Daily Lift**: "a custom workout intelligently built for you based on your recent lifts and recovery, refreshed daily"; "tailored to your training preferences and muscle readiness"; built "leveraging the same principles Tonal's expert coaches and performance team use"; user can customize duration and target muscle groups (Push/Pull/Upper/Legs/Full Body), regenerate with a tap, use filters, and swap movements ("Movement Replacements") before or during the workout; can apply "Recovery Weight" to a movement mid-workout.
- Product-specific rule: if the member completed a Program workout within the last 14 days, Daily Lift is hidden from the Today tile (still accessible elsewhere) — AI recommendation defers to the active human-led program.
- Other AI/adaptive features in KB: Dynamic Weight Modes, Muscle Recovery tracking, Coaching Cues, rep counting, Personal Records, Strength Score (homepage: "unlocks insights about your strength"), heart-rate zones, leaderboards.
- KB category structure: Installation / Getting Started / Features & Functions / Account & Membership / Troubleshooting / Relocation / Commercial & Healthcare / Warranty & Legal / General Questions — hardware-product support shape.

## Cross-product Comparison

| Dimension | Fitbod | Freeletics | Tonal |
|---|---|---|---|
| Surface | consumer mobile app | consumer mobile app | wall-mounted hardware + mobile companion |
| Coaching unit | one generated workout per session ("smart workouts") | multi-week Training Journey with coach-assigned sessions | human-coach Programs + AI "Daily Lift" (daily-refreshed generated workout) |
| Personalization inputs | goals, experience level, performance history, muscle recovery, equipment | onboarding answers, journey choice, training days, equipment, running prefs; performance + feedback after each session | goals, preferences, training history, muscle readiness (recent lifts + recovery), learned strength |
| What the AI does | generates each workout; recommends weights/reps/sets; adapts session by session | adjusts the plan across the journey; regenerates sessions on constraint feedback | daily workout generation; conversational assistant; per-rep adaptive resistance; strength learning |
| User control over AI | swap/skip/add exercises, duration presets, goal switching, equipment settings | adapt-session options (time/equipment/space/noise/difficulty/body-area exclusions), exercise alternatives, exclusions | regenerate, filters, duration, muscle-group focus, movement replacement before/during workout |
| Performance capture | manual set/rep/weight logging | manual logging + app syncs | automatic rep counting and weight adaptation |
| Progress metrics | PRs, estimated strength, volume trends, streaks | Daily Athlete Score, levels, stars, perfect weeks, weekly update | strength insights/score, personal records, leaderboards |
| Exercise guidance | video demo + written cues per exercise | video/technique guidance, skill progressions | coaching cues, trainer-led video programs |
| Human coach | none | none (community/support separate) | human coaches on video inside Programs |
| Nutrition | none | separate Nutrition product with its own coach | none |
| Community/gamification | streaks | community forum, network, streaks, levels | leaderboards |
| Business model | consumer subscription | consumer subscription (training; nutrition separate) | premium hardware + monthly membership |

Stable across all three (cross-product commonality, layer B):

1. A single-trainee profile with goals, ability, and constraints (equipment, schedule).
2. The software itself composes the training (workout or plan) — the user does not assemble it from a static library as the primary mode.
3. Guided workout execution with per-exercise guidance and performance capture.
4. The plan/workout changes in response to performance, feedback, and constraints (adaptation loop).
5. User override: every product exposes ways to swap, skip, regenerate, or constrain what the AI produced.
6. Recovery/readiness as an input to what comes next.
7. Progress measurement surfaced back to the user (scores, records, trends, streaks).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

An AI Fitness Coach is recognizable only if all four hold:

1. **Individual trainee profile** — the system knows one person's goals, ability, and constraints (equipment, schedule, preferences). The unit of coaching is the person, not a class, team, or client roster.
2. **Software-composed training** — the application itself generates the training plan/workout content. The user's primary mode is not assembling workouts from a fixed library and not receiving human-authored programs.
3. **Guided execution with performance capture** — the app walks the user through the session (what to do, how much, in what order) and records what was done.
4. **Feedback-driven adaptation** — the plan changes based on performance, feedback, and constraints. The system, not a human, performs the coach's adjust-and-progress function.

Remove #2 → workout tracker or plan library. Remove #4 → static plan generator (no coaching). Remove #1 → random workout generator. Remove #3 → a planning document, not a coaching application.

Note on "AI": the defining property is that **software performs the coach function** (generation + adaptation). Whether that is implemented as rules, a proprietary algorithm, machine learning, or a conversational LLM is an implementation question (L2/L3). Older algorithmic products (Fitbod's stated "proprietary algorithm", Freeletics' "digital program") satisfy the Type without any LLM.

### L1 — Common Mature Structure

Present in all or nearly all mature products (layer B):

- onboarding assessment (goals, experience, equipment, schedule)
- exercise library with media and form cues
- workout logging (manual and/or automatic)
- exercise substitution / swap
- session-level adaptation options (time, equipment, difficulty)
- recovery/readiness tracking as plan input
- progress metrics (records, volume, trends, streaks, scores)
- wearable/health-platform integrations
- goal switching that re-targets the plan

### L2 — Variant / Optional Structure

- **Coaching granularity**: per-session generator (Fitbod) vs multi-week journey (Freeletics) vs daily-refreshed generated workout (Tonal Daily Lift)
- **Domain focus**: strength/resistance, bodyweight/HIIT, running/endurance
- **AI interface**: silent algorithm vs conversational assistant (Tia — single-product so far)
- **Surface**: app-only vs hardware-embedded with adaptive resistance (Tonal)
- **Human-in-the-loop hybrids**: human-coach programs alongside AI features (Tonal); human-coach-led services with app delivery (Future/Runna pattern — not directly researched)
- **Nutrition companion**: separate coached nutrition product (Freeletics)
- **Community/gamification layer**: forums, networks, leaderboards, levels
- **Free/manual tier**: same app without the coach as a workout library (Freeletics free version)
- **Identity/business model**: consumer subscription vs hardware+membership; household accounts (Tonal)

### L3 — Vendor-specific (research notes only)

- Freeletics: Training Journeys, God Workouts, Workout Creator, Daily Athlete Score, Perfect Weeks, Skill Progression paths, "each side counts as one" convention, Hardcore journey lacking some adapt options.
- Fitbod: "smart workouts" branding, Gym Profile settings, strength-tester marketing tool, HSA/FSA eligibility positioning, exact pricing.
- Tonal: Tia, Your Daily Lift (beta), Daily Lift hidden from Today tile when a Program workout was completed in the last 14 days, Dynamic Weight Modes, Drop Sets, Eccentric mode, Recovery Weight, Strength Score, one-pound resistance increments, 12-month membership commitment, unlimited household accounts.

## Vendor-specific Findings

- Tonal's rule that AI recommendations defer to an active human-led program (Daily Lift hidden from Today tile within 14 days of a Program workout) is single-product evidence — do not generalize.
- Freeletics' nutrition coach is a separate product/subscription — do not fold nutrition into the Type's core.
- Fitbod's strength-only scope is a positioning choice; Freeletics covers bodyweight/running; so domain breadth is variant, not invariant.

## Boundary Findings

- **vs Workout Programming Application** (sibling leaf): there, a human trainer authors and adjusts programs for clients; the software is the delivery/management channel and the object graph is coach→client. Here, the software itself performs plan generation and adaptation and there is no coach role or client roster. Structural test: **who adapts the plan** — software (this Type) vs human (Workout Programming). Flagged for joint review because vendors increasingly bundle both (human-coach platforms adding AI assist).
- **vs Workout Tracking Application**: tracking centers on logging what the user chose to do; no plan generation or adaptation (at most static templates). Structural test: remove plan generation → tracker; add software-composed, adapting plans → this Type. Note: Freeletics' own free tier demonstrates the same app degrading into a tracker/library when the coach is removed.
- **vs Online Fitness Coaching**: a human coach delivers coaching remotely, often through an app; the coaching intelligence is human. Structural test: is the adaptation performed by a person or by the system? Hybrids (human check-ins + AI plans) sit on the gradient; Tonal shows one product carrying both structures side by side.
- **vs Wearable Fitness Platform**: wearable platforms center on measurement (recovery, strain, sleep, activity) with coaching as an optional add-on; this Type centers on deciding and adapting training. Probe of a wearable vendor's support site failed, so this boundary is argued structurally, not vendor-specifically.
- **vs Running Application / sport-specific training apps**: sport-specific apps may embed AI plan generation (Freeletics Running Journeys does inside its coach); when the AI coach is the product's center and the sport is one journey among several, it stays here; when the sport's own data/analysis is the center, it belongs to the sport-specific Type.
- **vs Nutrition Coaching Platform / Meal Planning Application**: food domain; adjacent only when bundled (Freeletics sells it separately).
- **"去掉什么就变成另一个 Type" 判据**: remove software-composed training → Workout Tracking Application; remove software adaptation (human does it) → Workout Programming / Online Fitness Coaching; remove the individual profile → generic workout generator/library; remove guided execution → a planning tool, not a coach.

## Uncertainties

- Fitbod's help center was unreachable; its operational detail comes from the official FAQ (official but marketing-adjacent). Precise algorithm claims (e.g., exact recovery decay) were not verified and are not asserted anywhere.
- Tonal's adaptive-resistance mechanics are described by vendor marketing ("learns your strength… one-pound increments"); treated as vendor claims, not canonical structure.
- Human-coach-led hybrid products (Future, Runna) were not directly researched; the human-coach boundary is drawn categorically (who adapts the plan), not from those vendors' docs.
- Wearable-platform boundary (Whoop-style AI coach add-ons) could not be verified from official docs; recorded as structural reasoning only.
- The market term "AI" is currently inflated (LLM-era rebranding of older algorithmic products); the Type definition deliberately does not depend on the implementation technology.

## Final Synthesis

The AI Fitness Coach is best understood as **software performing the coach loop for one trainee**: know the person (profile/assessment) → compose the training (plan/workout generation) → guide the session (execution + capture) → adapt (performance/feedback/constraints feed back into composition). Everything else — journeys vs daily lifts vs per-session generation, conversational assistants, hardware, nutrition, community, gamification — is variant or vendor structure. The Type's edge is defined by who does the coaching: software (here), a human (Workout Programming / Online Fitness Coaching), or nobody (Workout Tracking / static libraries).
