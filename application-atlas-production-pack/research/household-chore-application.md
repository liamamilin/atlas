# Research Notes — Household Chore Application

## Research Goal

Understand the Application Type "Household Chore Application" from real products: what the core objects are, how the chore cycle works, who uses it, how household members share the work, and where its boundary runs against neighboring Types (To-do List, Family Organizer, Home Maintenance, Home Management, cleaning-business software).

## Initial Boundary

Hypothesis at start:

- Core subject: recurring routine domestic work (cleaning, tidying, laundry, dishes, trash, pet care) rather than one-off tasks.
- Distinguishing question #1 vs To-do List Application: is the recurrence/cadence + household domain the organizing spine, or just tasks with due dates?
- Distinguishing question #2 vs Family Organizer: the family-organizer pass (STATUS.md 2026-09-07) left a forward note: chore-only products (chore charts, cleaning routines, gamified chores without a household calendar hub) belong to this leaf; the discriminator is the shared family calendar present as a co-equal defining layer in the organizer. This pass must verify that discriminator from this side.
- Distinguishing question #3 vs Home Maintenance Application: the home-maintenance pass (STATUS.md 2026-09-08) recorded the seam "task subject: home fabric vs household routine labor". Verify.
- Known risk: this market is dominated by small consumer apps with thin official documentation; marketing landing pages may be the only reachable official layer.

## Research Questions

1. What is a "chore" as an object? What attributes does it carry (name, area/room, frequency, effort/points, assignee)?
2. How does the chore lifecycle work: how does a chore become "due", how is completion recorded, what happens to the schedule after completion?
3. Is member assignment / rotation / fairness machinery defining or common? Does a single-user product still fit the Type?
4. What scheduling philosophies exist (fixed calendar vs interval/dueness vs effort-budget)?
5. What gamification/reward structures exist and are they definitional?
6. How does the app's "world" scope to one household, and what surfaces does the user face?
7. Where exactly are the boundaries vs To-do List, Family Organizer, Home Maintenance, Home Management, and cleaning-business software?

## Representative Products

Selected for different product philosophies and user contexts (market representation + reachable official documentation + different poles of the Type):

| Product | Pole | Why selected |
|---|---|---|
| Tody (LoopLoop ApS) | interval/dueness-based cleaning schedule; strong single-user core + household sharing | market-leading cleaning app; unusually deep official landing + FAQ |
| Sweepy | gamified shared home cleaning (points, leaderboard, parent approval) | consumer gamification pole; household-sharing pole |
| ChoreBuster | automatic fair chore-schedule generation for families (email/print delivery) | schedule-generation + fairness pole; parent-orchestrated family pole |
| Grocy | self-hosted "household ERP" with chores as one module | power-user/self-hosted pole; chores-as-module packaging; open source |

Rejected / unreachable:

- **OurHome** (ourhomeapp.com, both www and apex) — transport errors ×2 → abandoned per network rule. Would have been the kids-points/allowance pole.
- **Homey** (gethomey.com, www + apex) — empty responses ×2 → abandoned.
- **Flatastic** (flatastic.app, www + apex) — transport errors ×2 → abandoned. Roommate pole therefore under-evidenced; roommate usage observed only via Sweepy/ChoreBuster copy.
- Sweepy App Store / Google Play pages — redirect/timeout (official vendor content, but unreachable from this environment).

## Sources

All fetched 2026-09-08.

- Tody — https://todyapp.com/ (landing) and https://todyapp.com/faq (official FAQ). Tier 1-2.
- Sweepy — https://sweepy.app/ (official landing). Tier 2.
- ChoreBuster — https://chorebuster.net/ and https://chorebuster.net/how-it-works.php (official). Tier 1-2.
- Grocy — https://grocy.info/ (official site) and https://github.com/grocy/grocy (official README). Tier 1-2.

Sourcing limitation: the sampled products expose no traditional multi-page help centers reachable from this environment; official content = landing pages, FAQ, how-it-works, README. Gamified family chore apps with allowance economies (OurHome, Homey) could not be reached; claims about allowance/money rewards are kept at the level supported by ChoreBuster's "rewards based on chores completed" only. No precise numeric limits, pricing details, or default values from memory.

## Product A — Tody

### Key observations (Evidence layer A unless noted)

- Positioning: "a cleaning-schedule app … that keeps track of what needs cleaning, when it was last done, and whose turn it is — so none of it has to live in your head."
- **Room/area organization**: home screen shows every room as a tile (Kitchen, Living Room, Bathroom, Children, Basement, Laundry, Office, Bedroom) with a color-coded dueness indicator.
- **Dueness model**: every task has its own interval ("how often it realistically needs doing" — e.g. vacuuming weekly, oven every few months). "Dueness is how far a task is along that interval since you last completed it: green means it can wait, red means it's overdue." Example tasks with due states: "Change bed linen — 5 days overdue", "Dust — Due today", "Vacuum floor — Due in 8 days", "Wash curtains — Due in 60 days".
- **Scheduling philosophy**: "You clean when things need it, not because it's Tuesday" — condition/interval-based rather than fixed weekday. FAQ explicitly contrasts with "a paper schedule [that] tells you to clean on fixed days whether things are dirty or not" and with a to-do list ("only knows what you remember to put on it").
- **Today's list**: the app "builds today's short list" of just what's due.
- **Assignment**: "Assign a chore once, or let Tody rotate it automatically each cycle"; "Everyone sees what's due on their own phone, and completed work stays visible without anyone having to chase it."
- **Fairness**: FairShare "turns your agreed split into a monthly target for each member" (Premium+). Leaderboards with per-member completed counts and percentages; "130 tasks done together this month".
- **Household sync** (Premium+): "everyone in the household also sees the same live cleaning plan on their own phone, anyone can check off a task".
- **Single-user core**: "The free plan is the core cleaning plan for one person" — includes assigning chores and rotating them automatically. So membership/sync is an upgrade, not the base.
- **Multiple homes** (Premium) — a household-scoped app that supports more than one home.
- **Gamification**: Dirt indicators "fill up as things get dirty and reset when you act"; streaks; "Dusty" dust-bunny nemesis with a monthly race; "Miss a week and nothing breaks; the race starts fresh each month."
- **Method**: break the home into rooms and bite-sized tasks with sensible frequencies; clean what's due; stay motivated.
- Vacation mode mentioned only in a quoted user review → weak evidence (layer B-at-best), keep out of final document or mark as unverified.

## Product B — Sweepy

### Key observations (Evidence layer A unless noted)

- Positioning: "The app that helps turn your chores into a game"; "Home Cleaning Schedule".
- **Chore list construction**: "Create a list of all your cleaning chores… We have a large selection of task suggestions… You can also create as many custom tasks as you want."
- **Points/effort model**: "Each task in Sweepy carries up to 3 points. Easy tasks like 'dust surfaces' might carry 1 point. More tedious tasks like sweeping and mopping the floor carry 3 points." Users can "filter tasks by level of difficulty and dirtiness."
- **Cleanliness state**: "Our visual indicators will help you measure the cleanliness of your home and choose what you will clean next." (Room-level organization implied but not explicit on the landing page — weaker evidence for this product.)
- **Smart Schedule (premium)**: "Tell Sweepy how much you want to clean every day of the week, and depending on your effort configuration, we will generate a needed number of tasks" — an effort-budget daily checklist generator. (Scheduling philosophy #3.)
- **Household sharing**: "Invite your family members or roommates to join in, and complete your cleaning tasks together. Compete for a spot on the family leaderboard!"
- **Parent approval**: "For the little ones, Sweepy also has an approval system. Their tasks will be marked as completed only after a parent's validation." and "Review the work of your little ones and manually approve their tasks to reward them points."
- **History/streaks**: "Keep up your cleaning streak… browse the history of your accomplished cleaning tasks."
- Account model: email / Apple / Google sign-in; a web sign-in exists alongside mobile apps.

## Product C — ChoreBuster

### Key observations (Evidence layer A unless noted)

- Positioning: "A Fair Chore Schedule, Automatically… The ultimate family chore chart, ChoreBuster lets you manage and assign chores to each member of your family." (Copy also mentions household/workplace.)
- **Schedule generation**: "ChoreBuster automatically generates a schedule of chores that are shared in a fair way"; "The schedule is automatically generated for you rather than you needing to manually assign chores to people." The schedule "can be different every week."
- **Setup model**: (1) enter all people in the household; (2) enter all chores — "How often it needs to be done and the intensity of the work are the main things to think carefully about"; preset chore library can be imported and tweaked. (3) view/adjust the generated schedule.
- **People configuration**: "Each person can be emailed a copy of the schedule, have fewer or no chores on certain days."
- **Chore configuration**: frequency + intensity; per-chore exclusions ("some people can be excluded from certain chores, other people can have more chores than others").
- **Delivery**: "The schedule is emailed to you every week (and/or daily emails with chores for that day to everyone in the schedule)"; "printing options to generate a monthly schedule, a schedule per person, per room, and more."
- **Rewards**: "Easily calculate rewards based on chores completed" — reward economy grounded in chore completion.
- **Accessibility detail**: "Icons are optional but can be helpful for people who are still learning to read." (pre-reader children).
- **Surface split**: the web app is the system; the mobile apps are "ChoreBuster Viewer" — view-only companions. Email/print are first-class delivery surfaces, not the app UI.
- Room-anchoring: per-room schedule printing exists → rooms are a known organizing dimension here too (layer B across products with Tody).

## Product D — Grocy

### Key observations (Evidence layer A unless noted)

- Positioning: "ERP beyond your fridge… a web-based self-hosted groceries & household management solution for your home." Motivation: "A household needs to be managed… this is my aim for a 'complete household management'-thing. ERP your fridge!"
- **Chores as a module**: "Track your household chores — Think less about 'oh, when have I done last...' and stay organized easier." Chores overview is a first-class page (screenshot), one major feature set beside stock, shopping list, recipes, meal plan, tasks ("just another to do list"), batteries, equipment.
- **Feature flags**: "If you don't use certain feature sets of Grocy (for example if you don't need 'Chores'), there are feature flags per major feature set to hide/disable the related UI elements" — direct evidence that chores is a separable module of a broader household ERP, i.e. a packaging variant, not the Type's boundary.
- **Multi-user**: default admin user, per-user settings/localization → supports household with several users (self-hosted, so users are configured by the operator).
- **Self-hosting**: PHP/SQLite web app; Docker; desktop variant; PWA (no offline); third-party mobile clients; REST API for everything.
- Chore-specific mechanics (period types, per-user assignment options, rescheduling) are not documented on the reachable surfaces → not asserted.

## Cross-product Comparison

| Dimension | Tody | Sweepy | ChoreBuster | Grocy |
|---|---|---|---|---|
| Unit of record | task with per-task interval | cleaning task with points/difficulty | chore with frequency + intensity | chore with last-done tracking |
| Household scoping | rooms as tiles; multiple homes | home cleanliness; members | household people list; per-room printouts | one household instance per deployment |
| Due/done cycle | dueness along interval since last done; overdue states; resets on completion | completion marks task; streaks/history; points awarded (kids after approval) | schedule generated per period; completion feeds rewards calculation | "when have I done last" tracking; chore log |
| Scheduling philosophy | interval/dueness ("not because it's Tuesday") | effort-budget daily checklist (Smart Schedule) | auto-generated fair weekly/daily schedule | recurring chores inside ERP (mechanics not doc-reachable) |
| Member distribution | assign once or auto-rotate; FairShare targets | invite members; leaderboard | auto-assignment with fairness constraints/exclusions | assignment to users (per product model) |
| Parent orchestration | leaderboard/counts | approval gating for kids' tasks | rewards calculation; icons for pre-readers | n/a (self-hosted adults) |
| Gamification | Dirt indicators, Dusty nemesis, monthly race | points, streaks, leaderboard | mild (rewards, "chores busted") | none |
| Primary surface | mobile (iOS/Android), no web | mobile + web sign-in | web app + email/print + view-only mobile | self-hosted web/PWA + API |
| Packaging | standalone freemium app | standalone freemium app | standalone web subscription | chores module of household ERP |

Evidence layers: most cells above are layer A (directly observed on official pages) for the product in question; cross-product claims in the synthesis are layer B; the canonical abstraction is layer C.

## L0 — Defining Invariant

Minimal joint structure without which the product stops being a household chore application:

1. **The chore as the unit of record** — a recurring routine domestic task held persistently with its cadence (how often it needs doing) and usually its effort, not a one-off arbitrary to-do. Remove → generic to-do list.
2. **The due-and-done cycle** — the app computes current state from cadence + last completion (due / overdue / next due), accepts completion of instances, and advances the record; what was done and when remains remembered. Remove → static cleaning checklist / chore-chart template, nothing managed.
3. **The household as the app's world** — the chores are the routine living work of one home; the organizing domain is that household (its members and/or its spaces), not a team, project, or an undifferentiated personal list. Remove → generic recurring task manager.

Jointly-held is load-bearing:

- 1 alone = static chore list / printable chore chart template.
- 1+2 without 3 = generic recurring to-do / personal habit machinery.
- 1+3 without 2 = cleaning-tips content or a checklist with no tracking — below the Type.
- 2+3 without 1 = reminders about the home with no chore record — contrived, not observed as a product shape.

**Historical / market-sample check (§24 reasoning)**: a paper chore chart on the fridge — recurring chores listed with daily/weekly cadence, checked off, reset for the next week, sometimes with names attached — satisfies all three legs. A rotating weekly cleaning rota among flatmates satisfies. Neither has gamification, reminders, apps, room-tile UIs, or cloud sync. Conversely the check removes modern overfitting candidates from the core: member assignment is NOT invariant (Tody's free plan is "the core cleaning plan for one person"; a solo adult with a cleaning routine fits), gamification is NOT invariant (Grocy has none), mobile-first is NOT invariant (ChoreBuster's system is web+email+print; Grocy is self-hosted web), room tiles are NOT invariant (ChoreBuster/Grocy have no tile UI). Historical checklist/rota products and regional/low-tech deliveries all satisfy the core.

## L1 — Common Mature Structure

Widespread in the sampled modern products but not required to recognize the Type:

- Member profiles and assignment of chores to members (assign-once or auto-rotation) — Tody, Sweepy, ChoreBuster, Grocy multi-user (B across sample).
- Room/area organization of chores — Tody (rooms as tiles), ChoreBuster (per-room printouts), Sweepy (implied cleanliness-per-area; weaker) (B).
- A suggested/default chore library to accelerate setup — Sweepy ("large selection of task suggestions"), ChoreBuster ("preset list of chores") (B).
- Due-state visualization / cleanliness indicators — Tody (color-coded dueness, dirt fills up), Sweepy (visual cleanliness indicators) (B).
- Reminders / digests at the right moment — Tody ("reminds you at the right moment"), ChoreBuster (weekly/daily email per person) (B).
- Chore history / accomplishment log — Sweepy (history of accomplished tasks), Tody (completed work stays visible; effort counted), Grocy ("when have I done last") (B).
- Gamification layer (points, streaks, leaderboards, mascots) — Tody, Sweepy strongly; ChoreBuster mildly (rewards); Grocy none → common, not definitional (B).
- Shared live plan across members' devices — Tody Premium+, Sweepy members (B).

## L2 — Variant / Optional Structure

Depends on segment, philosophy, deployment:

- **Scheduling philosophy** (the clearest market split):
  - interval/dueness-based: clean when the task is due since last completion (Tody)
  - generated fixed-period schedule: fair weekly/daily schedule with per-person constraints (ChoreBuster)
  - effort-budget daily checklist: app fills today's list to a configured effort level (Sweepy Smart Schedule)
- **Fairness machinery**: rotation, contribution targets, per-person day-load limits, per-chore exclusions (Tody FairShare, ChoreBuster constraints) — present where households share work; absent single-user.
- **Parent orchestration / child accounts**: approval gating before completion counts (Sweepy), rewards calculation (ChoreBuster), icons for pre-readers (ChoreBuster). Allowance/money economies are known market-wide but unverified in the reachable sample (OurHome/Homey unreachable) — keep qualified.
- **Audience variant**: families with kids (ChoreBuster, Sweepy approvals) vs couples/roommates (Sweepy invites roommates; Tody "partner, family, or roommates") vs solo adults (Tody free core).
- **Delivery surface**: native mobile vs web+email+print (ChoreBuster treats print as first-class) vs self-hosted web/API (Grocy).
- **Packaging**: standalone chore app vs chores as one module of a household ERP (Grocy feature flags) vs chore chart as one capability inside a Family Organizer (per family-organizer pass).
- **Multiple homes** (Tody Premium) — optional.

## L3 — Vendor-specific Structure (research notes only)

- Tody: Dusty mascot/monthly race; FairShare (brand name); specific pricing tiers ($9.99/yr Premium; Premium+ Duo/Family/Team at $25/$40/$80 per year; 30-day trial); Focus Timer; vacation mode (review-quoted only).
- Sweepy: 1–3 point scale; "Smart Schedule" brand; premium gating specifics; "1,000,000+ households" marketing claim.
- ChoreBuster: "ChoreBuster Viewer" companion apps (view-only); household/people/chores counters (119,174 / 229,001 / 946,874); email-from-the-system digests; icons for children learning to read.
- Grocy: feature-flag configuration; REST API + Swagger UI; self-host install/config model; Home Assistant add-on; barcode tooling (adjacent modules, not chores).

## Boundary Findings

- **vs To-do List Application**: a to-do list holds arbitrary user-entered one-off tasks with optional due dates; there is no household domain and recurrence is not the organizing spine. Tody's own FAQ draws this line explicitly ("A to-do list only knows what you remember to put on it"). Discriminator: remove the chore-of-record-with-cadence and the household domain and what remains is a to-do list; conversely a to-do app configured with a "cleaning" list still has no due-and-done chore cycle as its center → different Type. This Type is deliberately narrower than "recurring tasks": the domain (routine domestic work of one home) is part of the definition.
- **vs Family Organizer**: the organizer's defining core is the conjunction of household circle + shared family calendar + shared items layer (calendar is load-bearing). Here no calendar hub is required and none of the sampled products centers a family calendar; chores are the center. The organizer-side forward note (2026-09-07: chore-only products belong here; the chore chart inside a full organizer is a standard capability there) is confirmed from this side — the discriminator holds both ways. Bundling exists in the market (organizers ship chore modules; gamified chore apps ship shopping lists), so center-of-gravity decides.
- **vs Home Maintenance Application**: home-maintenance pass records the seam "task subject: home fabric vs household routine labor" — confirmed: chores are the household's routine living work (cleaning, laundry, dishes, trash, tidying) done by members on short cadences; maintenance targets the home's physical fabric and systems (filters, gutters, appliances) on long/seasonal cadences. Products can drift (a chore app with "clean the gutters yearly" blurs), but the center of gravity separates them. The home-maintenance pass also noted "2+3 without 1 = generic recurring to-do/chore app", i.e. that Type fails without the home-anchored record — symmetric evidence for this seam.
- **vs Home Management Application**: home-management is the whole-home binder of record (premises records); its pass explicitly excluded "consumables-chores ERP" (Grocy named as boundary specimen). Chores apps keep no premises records — different center.
- **vs Cleaning Business Management / commercial cleaning software**: different customer and world entirely — a cleaning company's client jobs, staff scheduling and invoicing vs the household's own self-managed routine work. No sampled product serves businesses.
- **vs Habit-tracking products** (no dedicated directory leaf): gamified repetition overlaps, but habit trackers center a personal habit loop (self-improvement), while chore apps center the household's shared work with assignment/fairness. Gamified chore apps borrow habit mechanics; the direction of the borrow matters (Sweepy/Tody gamification motivates domestic work; the work, not the self, is the object).
- **Rejected Type claim**: "Household Chore Application" is not merely an audience variant of Task Management. The task-management family's center (team work items, projects, workflows) does not cover the household domain, the cadence-first chore record, or fairness/rotation machinery; conversely chore apps lack project/workflow structure. Keep separate.

## Uncertainties

- Allowance/money-reward economies (chores → pocket money) are a widely known market pattern (OurHome, Homey) but both were unreachable; only ChoreBuster's "rewards based on chores completed" is documented in-sample. Kept as qualified claim.
- Room/area organization for Sweepy is implied ("cleanliness of your home", difficulty/dirtiness filters) but not explicitly documented on the reachable page; asserted only as implied for that product, explicit for Tody/ChoreBuster.
- Grocy's precise chore mechanics (recurrence period types, per-user assignment options, reschedule rules) are not on the reachable surfaces; only "last done" tracking and the module's existence are asserted.
- Roommate/flat-share products (Flatastic) unreachable; the roommate audience is evidenced via Sweepy/Tody/ChoreBuster copy only.
- Whether a dedicated "chore schedule generator" product family (ChoreBuster pole) persists as a distinct species or is being absorbed by dueness-based apps is a market observation, not resolvable from this sample.

## Final Synthesis

A Household Chore Application is an application whose world is the routine domestic work of one household. Its unit of record is the chore — a recurring household task carrying its cadence (and usually effort), optionally scoped to a room/area and assigned to a member. The engine of the Type is the due-and-done cycle: the app derives current state from each chore's cadence and last completion (due today / overdue / next due), accepts completions, records them, and advances the schedule — replacing the mental load of noticing, planning and chasing ("whose turn is it", "when were the sheets last changed"). Around this core, mature products add member profiles with assignment and rotation, fairness machinery (targets, constraints, exclusions), room/area organization, setup libraries, reminders/digests, and a motivational layer (points, streaks, leaderboards, approval gating for children). The market realizes the Type in several philosophies — dueness-based cleaning trackers, generated fair-schedule charts, effort-budget checklist generators — and in several packagings — standalone consumer apps, family chore charts with print/email delivery, and a chores module inside a broader household ERP. What keeps the Type coherent is that all of these orbit the same object (the recurring chore of one household) and the same cycle (due → done → next due), regardless of how scheduling, gamification, or delivery are implemented.
