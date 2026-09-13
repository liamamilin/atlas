# Research Notes — Audience Response System

Research date: **2026-09-06**
Methodology: v1.1 (update-v1/)

---

## Research Goal

Understand what an Audience Response System (ARS) actually is as an Application Type: its defining structure, its core objects, its live workflow, its variants (education clickers → modern web polling), and its boundaries against Survey Platforms, Polling Applications, webinar/meeting platforms, and event apps.

## Initial Boundary (hypothesis before research)

- ARS = a facilitator-run instrument for collecting structured input from a mass audience during a live session and aggregating it in real time for that same audience.
- Nearest neighbors: Polling Application (03.11 sibling), Survey Platform, Online Form Builder, Webinar Platform / Virtual Meeting Platform, Event Mobile App, Q&A Community, Assessment Platform.
- Suspected confusion: ARS vs Polling Application (both "polls"); ARS vs Survey Platform (both "questions + results"); embedded polling inside webinar platforms (capability vs Type).
- Historical dimension: the Type predates smartphones (classroom "clicker" systems); the definition must not depend on phone/web join mechanics.

## Research Questions

1. What objects exist inside an ARS? (session/event, items, responses, participants, results)
2. How do audience members join, and what identity/anonymity model applies?
3. What interaction item types exist, and how do they aggregate live?
4. What is the session lifecycle (prepare → run → close → report)?
5. What presenter surfaces exist (web dashboard, PowerPoint add-in, meeting-app integration)?
6. What variants exist (education, corporate, events, gamified, governance)?
7. Where exactly is the boundary vs Survey Platform / Polling Application / webinar-embedded polling?

## Representative Products

| Product | Philosophy | Customer tier | Why sampled |
|---|---|---|---|
| Slido (Cisco/Webex) | Q&A-first corporate meetings, integration-heavy | Enterprise / business | Market-leading meeting interaction; deep PowerPoint/Teams/Zoom/Webex integration |
| Mentimeter | Presentation-native interactive slides | Business + education | "Interactive presentation" philosophy; templates + AI authoring |
| Poll Everywhere | Presenter-classic live polling | Higher ed + corporate + events | Longest-standing web polling lineage; explicit "student response system" heritage; broad poll-type catalog |
| Kahoot! | Gamified live quiz | Education-first, expanding to work | Game-show mechanics (PIN join, leaderboard, timer); consumer-scale brand |
| Vevox | Anonymity- and inclusion-focused polling/Q&A | Education + business (UK/EU) | Emphasizes anonymity, moderation, LMS integrations, attendance |
| Echo360 (EchoPoll / PointSolutions, ex-Turning Technologies) | Education polling with clicker heritage | Higher ed / institutions | Historical sample: Turning Technologies was the classic hardware-clicker vendor; now software polling with LMS sync |

## Sources

Fetched 2026-09-06 (all successful):

- Slido — https://www.slido.com/ (homepage), https://www.slido.com/product (product tour)
- Mentimeter — https://www.mentimeter.com/ (homepage)
- Poll Everywhere — https://www.polleverywhere.com/ (homepage)
- Kahoot! — https://kahoot.com/ (homepage)
- Vevox — https://www.vevox.com/ (homepage)
- Echo360 — https://echo360.com/ (homepage; turning.com redirects here), https://echo360.com/echopoll/ (product + FAQ page)

Identified but **not fetched** (help centers / community sites):

- community.slido.com, support.polleverywhere.com, support.kahoot.com, help.vevox.com, info.echo360.com/pointsolutions

**Source-access limitation:** evidence is dominated by official product/marketing pages (Tier 2) plus one product FAQ page (EchoPoll, Tier 1-ish). Help-center articles were not fetched. Therefore: no precise numeric claims (participant caps, pricing, time limits, exact plan features) are made anywhere; workflow claims are calibrated to what product pages explicitly describe.

---

## Product Observations

### Slido (evidence layer: A — directly observed on slido.com and slido.com/product)

- Positioning: "audience interaction" for meetings and events — live polls, live Q&A, word clouds, ideas (brainstorming), quizzes, surveys.
- Live Q&A: participants ask questions from any device and **upvote** others' questions; asking can be **anonymous or named**.
- Five poll types named on the product tour: multiple choice, word cloud, rating, open text, ranking.
- Quizzes: live quiz with **timer and leaderboard**.
- Surveys: collect input **before, during, or after** the meeting (explicitly extends beyond the live moment).
- Analytics: engagement measurement, Q&A sentiment, exports of questions/poll results/quiz leaderboard/ideas to Google Sheets, Excel, PDF.
- **Q&A moderation**: "Review all incoming questions before your participants can see them."
- **Privacy**: SSO, passcode, other privacy settings to control who can access an event.
- **Spaces**: share meetings with selected team members and collaborate on them (co-hosting).
- Integrations: PowerPoint, Webex, Google Slides, Microsoft Teams, Zoom, live video, embed into websites/apps; "combine integrations".
- Join: "attendees can join without any logins or downloads"; homepage has a participant join entry ("Joining as a participant? Join now" with a code/hash input).
- Solutions pages: remote meetings, hybrid meetings, virtual events, all-hands, webinars, conferences, education.
- Enterprise: SSO, user management, security/compliance standards, dedicated success managers.
- Ownership: "Slido is now part of Webex" (Cisco).

### Mentimeter (evidence layer: A)

- Positioning: "Interactive presentation & audience engagement tool" — live polls, quizzes, Q&A.
- Business use: "Invite live, **anonymous** feedback"; open anonymous Q&A forum; brainstorming; "capture the team's input in one go"; interactive content.
- Education use: anonymous feedback as "in-the-moment snapshot"; anonymous knowledge checks ("stress-free"); student interactions.
- Authoring: templates, create from scratch, or **AI prompt** ("AI Menti Creator"); "ready to present and interact in no time".
- Setups: "Use with any tool. In-room, remote, or both."
- Scale claim: "500+ million users worldwide" (marketing figure — recorded, not reused in final doc).

### Poll Everywhere (evidence layer: A)

- Positioning: audience engagement for presenters; segments: Higher Ed, K-12 ("student response system"), Corporate, Events.
- Core loop described on homepage: **Create your poll** (choose poll type, enter prompt and answers, hit present) → **Engage your audience** ("See responses update in real-time as audiences answer via their device") → **Analyze the results** (participation, summaries, questions asked).
- Poll types: bar charts (multiple choice with bars growing in real time), word clouds, donut charts, **competitions** (series of multiple-choice questions + leaderboard), Likert scale, **Q&A** (submitted, upvoted/downvoted), radar charts.
- Audiences: teachers (real-time feedback, attendance automation), corporate presenters (all-hands, training), events (live interaction, interactive Q&A).
- Guides exist: Student Guide, Instructor Guide, Admin Guide (role separation).
- Integrations: "Embed and present directly in the tools you're already using" (apps for 1.0 and 2.0).
- Participant join: homepage has "Trying to join a poll? Join Here" (pollev.com).
- Heritage claims: "10m+ presenters", "200m+ participants", "40m+ presentations" (marketing figures — recorded, not reused).
- Comparison pages exist vs Kahoot, Mentimeter, Slido, Vevox, Wooclap, iClicker-adjacent tools — confirms the competitive set is exactly the ARS category.

### Kahoot! (evidence layer: A)

- Positioning: gamified learning/engagement ("learning games"); brands: Kahoot!+ (edu/personal), Kahoot! 360 (work), Kahoot! EDU.
- Work use cases: meetings & presentations, conferences & events, **polls & surveys** (dedicated poll-maker page), employee training, workshops & brainstorms, onboarding, townhalls, frontline communications.
- School use: interactive lessons, review & assessment, lectures, study prep.
- Join: dedicated participant surface at kahoot.it ("Join" in main nav); mobile apps emphasized ("Get the mobile app for the best Kahoot! experience!").
- Mechanics visible from product imagery/labels: quiz question screens, answer/results screens, lobby screens, podium imagery, rating-scale questions, brainstorm question type.
- Value props: interactive learning (gamified, solo or with others), real-time engagement ("participate and get instant feedback"), collaboration & connection.
- Ecosystem: content library (Discover), Kahoot! Certified, community; acquisitions (Actimo, Motimate, Whiteboard.fi, Drops, DragonBox/Poio) — vendor-specific, L3.

### Vevox (evidence layer: A)

- Positioning: "AI-Assisted Polling, Quizzing and Q&A Platform" for classes, training, meetings.
- Features: live polling (multiple choice, image-based, numeric, dynamic word clouds), quiz (leaderboards, timed polls), **anonymous Q&A** ("By enabling anonymity… even the shyest students"), word clouds, surveys ("self-paced feedback"), **anonymity** as a named feature, analytics, attendance tracking, spin-the-wheel, non-polling content (presentation maker), AI question helper (generates correct + plausible incorrect options, difficulty setting).
- Moderation: "anonymity or moderation controls".
- Integrations: Teams, PowerPoint, Google Slides, Zoom, Webex; LMS: Brightspace, Blackboard, Canvas, Moodle.
- Use cases: hybrid classes, workplace training, hybrid meetings, class assessments (formative), virtual meetings/classes, townhalls, everyday meetings, hybrid events, webinars.
- Pricing shapes: education plans, business plans, enterprise, institution, **one-time event plans** (evidence that one-off event usage is a real purchasing pattern).
- Participant join: homepage "Join a session" input.

### Echo360 — EchoPoll / PointSolutions (evidence layer: A; historical anchor)

- turning.com now redirects to echo360.com: Turning Technologies (the classic classroom clicker vendor) has been absorbed; its line is now **PointSolutions** ("pioneered learner response technology for both online and offline use… gamification functionality"), alongside **EchoPoll** ("next generation polling and engagement solution").
- EchoPoll FAQ (directly observed):
  - "Invite **registered and guest users** to participate in **live and asynchronous** EchoPoll sessions on any device."
  - "**QR codes** to expedite access to the EchoPoll session in the classroom from mobile devices."
  - "instructors can alternatively opt for using **clicker devices** for polling inputs… beneficial in areas where electronic device use is discouraged." → hardware response units persist as an input option in education.
  - Browser-based participation on any web-enabled device; no plug-ins required; optional desktop companion app with a floating toolbar for "instant polling within any PPT… OR with any application or website".
  - **LMS integration** (LTI; Sakai, Moodle, D2L, Blackboard, Canvas, Schoology, Google Classroom): syncs courses, **rosters**, and **scores** to the LMS.
  - **Asynchronous mode**: "Assignments" / "PollDecks" — interactive polls embedded in PowerPoint decks, assigned to students, with **gated progress** (must respond before advancing).
  - **Attendance tracking** / check-in.
  - 7 supported question types; performance reporting; Echo.ai Assist (question generation from course materials).
- Education positioning: engagement, attendance, comprehension, formative reinforcement; also business training use.

---

## Cross-product Comparison

| Dimension | Slido | Mentimeter | Poll Everywhere | Kahoot! | Vevox | EchoPoll/PointSolutions |
|---|---|---|---|---|---|---|
| Facilitator-run live session | ✔ (event) | ✔ (presentation) | ✔ (poll/presentation) | ✔ (game) | ✔ (session) | ✔ (session) |
| Mass participant join, no per-participant account required | ✔ "no logins or downloads" | ✔ (implied by live audience model) | ✔ (join page) | ✔ (kahoot.it join) | ✔ ("Join a session") | ✔ (guest users; QR) |
| Structured items: polls (MC/open/rating/ranking) | ✔ | ✔ | ✔ | ✔ (polls & surveys) | ✔ | ✔ (7 question types) |
| Word cloud | ✔ | ✔ | ✔ | (brainstorm type) | ✔ | — (not confirmed) |
| Q&A with upvoting | ✔ | ✔ | ✔ (up/downvote) | — (not confirmed) | ✔ | — (not confirmed) |
| Quiz with timer/leaderboard | ✔ | ✔ | ✔ (competitions) | ✔ (core) | ✔ | ✔ (gamification) |
| Anonymity control | ✔ (Q&A anonymous) | ✔ (anonymous feedback) | (not confirmed on page) | (not confirmed) | ✔ (named feature) | (registered vs guest implies identity options) |
| Q&A moderation | ✔ | (not confirmed) | (not confirmed) | — | ✔ | — |
| Surveys / self-paced (async) mode | ✔ (before/during/after) | (implied) | (not confirmed on page) | ✔ (polls & surveys; study modes) | ✔ (self-paced) | ✔ (assignments, gated PollDecks) |
| Results archive / export / analytics | ✔ (exports, analytics) | (implied by "turn live insights into action") | ✔ (analyze results) | ✔ (reports) | ✔ (analytics, data API) | ✔ (performance reporting, score sync) |
| PowerPoint integration | ✔ | (with any tool claim) | ✔ (apps) | (not confirmed) | ✔ | ✔ (PollDeck, floating toolbar) |
| Meeting-platform integration (Teams/Zoom/Webex) | ✔ | (any tool) | ✔ (apps) | (not confirmed) | ✔ | ✔ (Zoom, GoToMeeting, Teams) |
| LMS integration / roster / grade sync | (education plans exist; not detailed) | (not confirmed) | ✔ (higher-ed, instructor/admin guides) | ✔ (edu ecosystem) | ✔ (4 LMS named) | ✔ (LTI, roster + score sync) |
| Attendance tracking | — | — | ✔ ("automate attendance") | — | ✔ | ✔ |
| Hardware clicker input | — | — | (historical lineage; not on page) | — | — | ✔ (explicit FAQ) |
| AI assistance | ✔ (poll suggestions) | ✔ (AI Menti Creator) | (not confirmed) | ✔ (study tools) | ✔ (AI question helper) | ✔ (Echo.ai Assist) |

Legend: ✔ = directly observed on the fetched official page; "not confirmed" = not seen on fetched pages (may exist elsewhere); "—" = not applicable/observed.

### What is universal (candidate defining structure)

1. **Facilitator-run live session** — every product is organized around a host/presenter who prepares and runs a bounded session (event / presentation / poll / game / session). No product sells "audience response" without a facilitation side.
2. **Mass distributed response inputs bound to the session via low-friction access** — every product has a participant join surface (code/hash input, join URL, QR, dedicated join site/app); every product stresses that participants respond "via their device" without heavy setup. EchoPoll extends this to clicker devices and registered vs guest users — the invariant is the response unit, not the phone.
3. **Structured interaction items** — polls (multiple choice / open text / rating / ranking / numeric / image), word clouds, quizzes, Q&A boards. The exact catalog varies; the existence of a prepared item catalog is universal.
4. **Real-time aggregate feedback loop** — Poll Everywhere states it verbatim ("responses update in real-time"); Slido ("polling your audience in real time", "get their feedback in real time"), Vevox ("real-time polling", live word clouds), Kahoot ("real-time engagement… instant feedback"), Mentimeter ("Get answers in real time"). The aggregate is displayed back to the shared session — this is what separates ARS from survey collection.

### What is common but not defining (candidate L1)

- Participant join surface with code/URL/QR (universal in current products, but clicker-era systems used channel tuning/device registration instead → implementation, not invariant).
- Item-type library breadth (word clouds, ranking, image polls, Likert…).
- Anonymity controls (observed in Slido, Mentimeter, Vevox; likely broader — treat as common).
- Q&A moderation (Slido, Vevox observed).
- Results persistence + export + analytics (observed in most; universal in mature products).
- Presenter surface plurality: web dashboard + PowerPoint add-in + meeting-app integration + embed.
- Surveys/self-paced mode extending beyond the live moment (Slido, Vevox, EchoPoll, Kahoot).
- Reusable content: templates, question banks, content libraries (Mentimeter templates, Kahoot Discover, Slido AI suggestions).
- Multi-session management for larger events (Slido events/spaces; Vevox one-time event plans imply session-per-event structure).

### What is variant/optional (candidate L2)

- Identity substrate: anonymous guest (default in many) ↔ registered/SSO ↔ LMS roster identity (EchoPoll, Vevox, Poll Everywhere higher-ed).
- Education institutional layer: LMS/LTI sync, gradebook/score sync, attendance tracking, rosters (EchoPoll, Vevox, Poll Everywhere).
- Gamification depth: leaderboards, timers, points, podiums, music/characters (Kahoot; quiz features in others).
- Hardware response units (clickers) as input alternative (EchoPoll explicit; historical norm).
- Hybrid/remote delivery posture: integration into video conferencing and live-video embeds (Slido, Vevox, EchoPoll).
- Enterprise governance: SSO, user management, admin roles, compliance (Slido enterprise, Poll Everywhere admin guide).
- AI assistance (all six show some form — becoming common, still optional).
- One-time event licensing (Vevox, Slido one-time plans) vs annual/institutional.
- Governance-style voting (weighted/AGM voting): **not verified** in fetched pages — do not assert.

### Vendor-specific (candidate L3 — stays here)

- Slido: Spaces (shared meeting workspaces), Webex/Cisco ownership, "Ideas" as a named feature.
- Mentimeter: AI Menti Creator; "Menti" branding of presentations.
- Poll Everywhere: "Competitions" as a named mode; 1.0 vs 2.0 app split; radar chart type.
- Kahoot!: game PIN join at kahoot.it, characters/music/podium presentation layer, Discover content marketplace, brand family (Actimo, Motimate, Whiteboard.fi, Drops, DragonBox).
- Vevox: spin-the-wheel, non-polling content (presentation maker), data API, #1-alternative marketing pages.
- Echo360: PollDeck, floating-toolbar companion app, Echo.ai Assist, Echosystem bundling with EchoVideo/EchoExam/EchoInk.

---

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

An Audience Response System exists where all four hold:

1. **Facilitator-run live session** — a bounded live event container with a host/presenter role who prepares and controls the interaction.
2. **Mass distributed response inputs** — many audience members each submit their own response through an individual response unit (phone/browser/clicker), bound to the one session through a low-friction shared access path.
3. **Structured interaction items** — the facilitator presents prepared items (polls, quizzes, ratings, open prompts, Q&A boards) that define what the audience responds to.
4. **Real-time aggregate feedback loop** — responses are aggregated live and the aggregate is displayed back to the same shared session while it is happening.

Remove #4 → Survey Platform / Form Builder (async collection, no live room).
Remove #1 → unmoderated community Q&A / chat.
Remove #2 (mass) → single-user form or presenter-only tool.
Remove #3 (structure) → generic chat / backchannel.

### L1 — Common Mature Structure

- participant join surface (code / URL / QR / app)
- item-type library (multiple choice, open text, word cloud, rating/scale, ranking, numeric, image, quiz, Q&A with upvoting)
- anonymity controls (anonymous vs identified, per item or per session)
- Q&A moderation (review/approve/hide before display)
- results archive with export and engagement analytics
- multi-surface presenter control: web dashboard, PowerPoint add-in, meeting-platform integrations, embed
- self-paced/survey mode (before/during/after the live moment)
- reusable content (templates, question banks, AI question generation)
- multi-session/event management and co-host collaboration

### L2 — Variant / Optional Structure

- identity substrate: anonymous guest / registered account / SSO / LMS roster
- education institutional layer: LMS sync, gradebook, attendance, rosters
- gamification depth (leaderboards, timers, points, themed presentation)
- hardware response units (clickers) as input alternative
- hybrid/remote delivery posture (video-conference integration, live-video embed)
- enterprise governance (SSO, user management, compliance, admin roles)
- one-time event licensing vs institutional/annual
- AI assistance depth

### L3 — Vendor-specific

See Vendor-specific list above (Slido Spaces, Kahoot game PIN/podium, EchoPoll PollDeck, Vevox spin-the-wheel, Poll Everywhere Competitions, Mentimeter AI Menti Creator).

### Anti-overfitting check (historical / market-sample)

- Would a 1990s–2000s classroom clicker system fit the L0? Yes: receiver + facilitator software = live session; distributed handsets = response units; question slides = items; on-screen result bars = real-time aggregate. The L0 deliberately does not mention phones, join codes, or the cloud.
- Would a webinar platform's built-in poll fit? It has items + live aggregate, but the session container belongs to a different Type (meeting/webinar); native polling there is a capability, not a standalone ARS. Recorded as boundary finding.
- Would an async survey fit? No — fails #4 (and #1/#2 in the live sense). Confirms the boundary.

---

## Boundary Findings

1. **vs Survey Platform**: the decisive difference is the live shared session + real-time aggregate display to the same audience. ARS products *include* survey/self-paced modes (Slido "before/during/after", Vevox self-paced, EchoPoll assignments) — that is an extension into the neighbor's territory, not evidence that the Types are identical. Conversely, survey platforms do not run live rooms. "Remove the live feedback loop and it becomes a survey" is the clean test.
2. **vs Polling Application (directory sibling in 03.11)**: heavy overlap. A standalone "polling application" that only creates and distributes polls (async or embedded) lacks the facilitator-run session container and the live room loop. The ARS is the *session-instrument* specialization. Risk: the two leaves could be merged by a future pass; the distinguishing test is the live co-present feedback loop, not the poll object itself. **Flagged in STATUS Boundary Issues.**
3. **vs Webinar Platform / Virtual Meeting Platform**: those Types own the meeting container (video, audio, stage). ARS owns the interaction layer and explicitly integrates *into* those containers (Slido for Teams/Zoom/Webex; Vevox for Teams/Zoom; EchoPoll for Zoom/GoToMeeting/Teams). Native polling inside a meeting platform = capability of that platform, not an instance of this Type. Primary-surface test: what does the product exist to do?
4. **vs Event Mobile App**: event apps aggregate agenda/networking/maps/attendee services; ARS is the single-purpose interaction instrument that event apps may embed. Directory places ARS under Events (26), but the research shows the Type is cross-domain (education and corporate meetings are primary habitats for most sampled products). **Flagged in STATUS Boundary Issues.**
5. **vs Q&A Community**: community Q&A is persistent, discovery-oriented, asynchronous; ARS Q&A is session-bound, moderated by the facilitator, and dies into an archive.
6. **vs Assessment/Examination Platform**: ARS quizzes are formative/engagement instruments; when gradebook sync and high-stakes scoring dominate (EchoPoll score sync blurs this), the product is drifting toward Assessment. The live-room loop and anonymity-first posture keep it ARS.

## Uncertainties

- Exact anonymity defaults per product (default-anonymous vs opt-in) — not verified; help centers not fetched.
- Duplicate-response handling (one response per participant per item?) — universally implied but not directly evidenced; phrased softly in final doc.
- Whether Q&A-only deployments (no polls) are common enough to matter — Slido/Vevox/Poll Everywhere all support Q&A as a first-class item; treated as part of the item catalog, not a separate Type.
- Governance/AGM voting capabilities (weighted votes, verified quorum) — suspected for some vendors but **not verified**; excluded from final doc.
- Participant-scale limits and pricing — deliberately not stated (no evidence fetched).
- Historical clicker specifics (RF channels, device registration flows) — not directly evidenced in fetched pages; only the *existence* of clicker input is evidenced (EchoPoll FAQ).

## Final Synthesis

The Audience Response System is best understood as a **live-session instrument**: a facilitator prepares structured interaction items, a mass audience joins a shared live session through low-friction access and responds through individual response units, and the system aggregates those responses in real time and displays the aggregate back to the same room. Everything else — join codes, word clouds, leaderboards, PowerPoint add-ins, LMS sync, anonymity, AI — is mature market structure or variant posture layered on that loop. The Type's center of gravity has shifted historically from hardware clickers (education lecture halls) to web/mobile session instruments (meetings, classes, events, webinars), but the defining loop is unchanged. Its directory placement under Events captures only one habitat; education and corporate meetings are equally primary.
