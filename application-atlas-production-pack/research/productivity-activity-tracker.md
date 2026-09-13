# Research Notes — Productivity Activity Tracker

Research date: 2026-09-08 · Methodology: update-v1 · Leaf: §03.14 Time & Focus — Productivity Activity Tracker (slug: productivity-activity-tracker)

## Research Goal

Understand the Productivity Activity Tracker as an Application Type: what its defining core is, how products capture and organize computer activity, what varies, and where the boundaries run against Time Tracking Application, Focus Timer, Time Blocking Application (all §03.14 siblings), Personal Dashboard (§03.13, processed), platform-native screen-time/wellbeing utilities (no directory leaf), Digital Employee Experience Management (§14, processed), and the org-facing employee-monitoring market (no exact directory leaf).

## Initial Boundary

Working hypothesis at start: a Productivity Activity Tracker automatically observes which applications/websites/documents a person uses and for how long, accumulates a usage record, and interprets it through a productivity frame (classification, scores, trends, goals) so the person (or their organization) can understand and improve how time is spent. Nearest confusions: (a) Time Tracking Application (user-initiated, project/billable); (b) Focus Timer (deliberate sessions — this pass's pre-hung seam); (c) platform Screen Time (capture without productivity frame); (d) employee monitoring/DEXM (org-facing telemetry).

## Research Questions

1. What exactly gets captured (apps, window titles, URLs, documents), and how is attribution handled (active window, idle/AFK)?
2. How is raw usage organized — vendor-default productivity taxonomies, user-defined category rules, or learned/ML mapping?
3. What does the record look like (timeline, daily summaries, trends) and what does the daily review loop feel like?
4. What productivity outputs exist (scores, percentages, reports, goals, alerts), and are they definitional or common?
5. Where is the data held (local-first vs cloud), and what privacy controls exist (pause, private time)?
6. How do team/org-facing postures (dashboards, screenshots, sharing) relate to the personal record center?
7. Where do the seams run vs Time Tracking, Focus Timer, Time Blocking, Personal Dashboard, screen-time utilities, and employee monitoring/DEXM?
8. Historical check: do older, local, and platform-native realizations still fit the definition?

## Representative Products

| Product | Why sampled | Pole |
|---|---|---|
| RescueTime | Category-defining personal automatic tracker (15+ years on market per its own copy); productivity scoring lineage; sells Focus (this Type) and Timesheets (Time Tracking straddle) as two named tools | classic personal SaaS, vendor-default productivity taxonomy |
| ActivityWatch | Free open-source, local-first, privacy-first; excellent Tier-1 docs (architecture, data model, categorization) | FOSS / local-first, user-defined classification |
| DeskTime | Team/employer-facing automatic tracker since 2011; markets itself simultaneously as "automatic time tracking" and "employee monitoring software" | business/team tier, employer-visible record |
| Rize | Modern desktop tracker with ML project mapping and productivity/focus coaching; pivoted toward team billable visibility | modern AI-era, straddles this Type, Focus Timer, and Time Tracking |

Secondary (cross-product evidence via official ActivityWatch comparison article): ManicTime (local automatic tracking + tagging, offline tagging), Apple ScreenTime (platform-native capture + categories, "focused on app limits and downtime").

## Sources

All fetched 2026-09-08 (Tier 1 = operational docs; Tier 2 = official product pages):

- ActivityWatch — https://activitywatch.net/ (Tier 1/2 homepage + FAQ); https://docs.activitywatch.net/en/latest/ (docs index); https://docs.activitywatch.net/en/latest/features/categorization.html (Tier 1); https://activitywatch.net/blog/comparing-time-trackers/ (official comparison: RescueTime, ManicTime, Apple ScreenTime)
- RescueTime — https://www.rescuetime.com/ (Tier 2); https://www.rescuetime.com/features/focus/solo (Tier 2 with operational FAQ)
- DeskTime — https://desktime.com/ (Tier 2; feature taxonomy, solutions, FAQ)
- Rize — https://rize.io/ (Tier 2; FAQ with privacy/capture detail)

Sourcing limitations: deep help-center articles (help.rescuetime.com, help.desktime.com) were not fetched; product pages carry the evidence. No precise numeric claims (score scales, idle thresholds, plan limits, default category lists beyond what pages name) are asserted anywhere. All four sources reached on first attempt; no degradation needed.

## Product Observations

### RescueTime (evidence layer A)

- "RescueTime runs in the background, automatically tracking time spent on apps and websites"; Solo Focus page: "automatically tracking where your time is spent across apps, websites, and documents. No timers, no spreadsheets."
- Capture mechanism: collects **window titles** of active apps/websites; explicitly does NOT collect keystrokes, form input, screenshots, or webpage content (FAQ).
- Interpretation: "Activities are given a productivity level by default but can be customized on the Activities page." Named levels observed in copy: "Personal or Distracting" (blocking rule keys off productivity levels). Reports available "by category, app or website, and productivity level."
- Outputs: weekly summaries with "average productivity score"; insights/trends over "weeks, months, or years"; Goals & Real-Time Alerts ("unlimited focus goals"); Daily Target Goals; Daily Highlights (user notes about the day).
- Actuation (Premium): Focus Sessions block selected websites/apps that are rated Personal/Distracting, silence notifications; built-in Timer ("Pomodoro technique or timing client work") feeding a Highlights Report.
- Offline Activity Tracking: log in-person meetings/calls; categorize offline activities "and view them by productivity just like your online activities."
- Detail depth: Premium "Detailed Tracking" of documents/file names; Keyword Search over reports; free plan sees up to two weeks of history, Premium unlimited (plan detail — research notes only).
- Companion surfaces: iOS app (start Focus Sessions, timers, log offline activity, "Allow Screen Time access to see trends in your mobile activity"); The Assistant (daily hub: meeting schedule + Focus Sessions + insights).
- Org tier: Team Focus — "Track team key tools, productivity trends, and work categories", team productivity report, daily pattern report; members keep full individual features.
- Straddle: **Timesheets** sold as a separate tool ("No timers, spreadsheets, or guesswork") — automatic project/client/task logging, billable rates, client reports; role-based access control. Vendor-drawn seam between this Type's Focus and Time Tracking's Timesheets on one platform.
- Multi-computer: time aggregated across machines, not separated by device (FAQ).

### ActivityWatch (evidence layer A)

- "app that automatically tracks how you spend time on your devices"; FAQ: "automated time tracker that runs on your computer and monitors which applications and websites you use."
- Capture: "Tracks active application and window title out of the box, more with watchers"; browser extensions track the active tab (Chrome/Firefox); editor watchers track coding; media and other watchers extensible; AFK detection documented in FAQ ("How does ActivityWatch know when I am AFK?" — configurable).
- Data model (docs): local server (web UI at localhost:5600), buckets & events, heartbeats carrying app/title and duration; export, pause logging, filtering documented as features.
- Interpretation: **Categorization** docs — categories give "more easily understandable labels for the data such as 'Work', 'Gaming' or 'Social Media'"; each category has title, optional parent/children, and a rule (regex matched on app and title values); deepest sub-category wins; users add/edit categories in Settings. Productivity weighting is NOT part of the documented categorization machinery — the homepage frames "monitor your productivity" as a use, and the comparison article does not claim a productivity score.
- Purpose framing (homepage): "Use it as an activity tracker or productivity tracker to monitor time spent on different projects, manage screen time habits, track work hours, or just understand how you spend your day"; quantified self / lifelogging framing; research use.
- Privacy posture: local-first — "your data stays on your device — never uploaded to the cloud"; sync between devices is a work-in-progress feature; remote server possible but explicitly discouraged/documented as advanced.
- Interfaces: web UI with Activity view (category visualizations) and Timeline view; tray icon; screenshots on homepage show dashboard with app/category breakdowns.
- Blocking: deliberately absent — official comparison article: "there are other free and open-source tools for blocking distractions, which is why ActivityWatch doesn't offer this feature."
- Comparison article (official, B evidence for the two non-sampled products): ManicTime = "comprehensive computer usage tracking, supports offline activity tagging", local+cloud storage options, tagging/categorization customization; Apple ScreenTime = "tracks applications and website usage", "basic reporting on screen time and app categories, little customization", "focused on app limits and downtime", Apple-ecosystem-bound, on-device encrypted storage.

### DeskTime (evidence layer A)

- "Automatic time tracking software for productivity insights"; "starts tracking your employees' time the moment they turn on their device—no timers to click and no timesheets to fill out later. Throughout the workday, DeskTime tracks the apps, websites, and documents your team uses and **automatically sorts them into productive or unproductive categories**."
- Feature taxonomy (official nav): Automatic time tracking; Project time tracking; Manual & offline time tracking; Private time ("Let users take a break from tracking when needed"); Productivity calculation; Screenshots ("proof-of-work in cases of questionable productivity or integrity" — optional); URL & app tracking; Document title tracking; Customizable settings; Notifications; Reports; Admin dashboard; User dashboard; Exports; AI summary ("daily and weekly insights instantly with AI-powered summaries").
- Workforce-management layer (suite furniture, not this Type's center): shift scheduling, absence calendar, attendance management, employee directory, IP location.
- Both-facing posture: solutions split "For managers" (performance evaluation, employee monitoring, remote work monitoring, productivity & efficiency) and "For employees" (well-being, work-life balance, burnout prevention, self-accountability).
- Privacy/monitoring stance (FAQ): "DeskTime is certainly not a spy tool…"; Private time disables tracking for non-work tasks; transparency framing — "employees to review all data collected about their own work activity."
- Straddle: project/client/billable tracking ("Billable hours captured automatically for client invoicing"), integrations with Jira/Asana/Trello/Calendar for project and offline time.
- Security posture: ISO 27001/27701, GDPR, encryption in transit/at rest, 2FA (security page claims — plan/platform level).

### Rize (evidence layer A)

- "Automatic time tracking… captures every billable hour in the background… No timers, no timesheets, no screenshots by default."
- Capture: desktop app (macOS/Windows) reads "only window metadata — app name, title, and URL — to categorize your time"; no keystrokes, no stored screenshots; opt-in "Screen Text" feature reads screen content, private to the user (FAQ).
- Interpretation: "Rize uses machine learning to assign each work session to the correct client or project based on window titles, URLs, and learned patterns" (AI time tracking FAQ) — ML mapping layer alongside category organization.
- Outputs: daily timeline + productivity score on dashboard (image alt text: "daily timeline, project breakdown, and productivity score"); AI productivity coach; focus detection ("Automatic focus detection and intelligent distraction blocking"); break reminders / wellness prompts; per-member customization.
- Org posture: "Employees control what time data is shared with their team. Only entries you explicitly tag to a team project or client are visible to your admin"; "review and approve their time data before leadership sees it"; "edit or delete any tracked time"; explicitly answers "How is Rize different from employee surveillance software?" — screenshots/keylogging/webcam named as the surveillance signals it refuses.
- Straddle: profitability dashboards, billable vs non-billable, utilization, client reports, QuickBooks export — Time Tracking-facing; focus tools/breaks — Focus Timer-facing.

## Cross-product Comparison

| Dimension | RescueTime | ActivityWatch | DeskTime | Rize |
|---|---|---|---|---|
| Capture trigger | background agent, always on | background watcher set, always on | starts when device turns on | desktop app, background |
| Capture object | active app/website/document (window titles); no keystrokes/content/screenshots | active app + window title; browser tab via extension; editor/media watchers; AFK detection | active apps/websites/documents; URL & document titles; optional screenshots | window metadata: app name, title, URL; opt-in Screen Text; no screenshots/keylogging |
| User starts/stops anything? | no | no | no | no |
| Interpretation layer | default productivity levels + categories, user-customizable; productivity level reports | user-defined categories with regex rules on app/title (no score documented) | automatic productive/unproductive sorting; productivity calculation | ML mapping to client/project; productivity score |
| Productivity score | yes (weekly average productivity score) | none documented | yes (productivity calculation) | yes (productivity score) |
| Record surfaces | reports by category/app/productivity level; weekly summaries; trends over years | Activity view + Timeline view; local dashboards | admin + user dashboards; reports; exports | daily timeline; team dashboards |
| Goals/alerts | Goals & real-time alerts; daily targets | none documented | notifications configurable | break reminders; AI coach nudges |
| Blocking/focus sessions | Focus Sessions (premium) | deliberately none (official statement) | not documented as core | distraction blocking, focus detection |
| Offline/manual entry | offline activity logging with productivity view | manual entry documented | manual & offline tracking | not documented on fetched pages |
| Pause/privacy | plan-level; privacy FAQ (no keystrokes/content) | pause logging; local-first storage | Private time feature | employees approve what is shared; edit/delete |
| Data residence | vendor cloud | local device (sync experimental) | vendor cloud (encrypted) | vendor cloud; user-controlled sharing |
| Audience | solo + team tiers | individual | managers + employees | individuals + teams (billable) |
| Straddles | + Timesheets (Time Tracking) | — (deliberately minimal) | + project/billable + workforce suite + employee-monitoring label | + billable (Time Tracking) + focus (Focus Timer) |

### Cross-product commonality (layer B, supports standard capabilities)

- Ambient automatic capture of active app/website (usually with window/document title; URL via browser watcher) — 4/4.
- Persistent reviewable record: timeline + aggregated summaries by app/category/day — 4/4.
- Interpretation layer turning raw usage into classes — 4/4, with three realizations: vendor-default productivity taxonomy (RT, DeskTime), user-defined rules (AW), learned mapping (Rize).
- Productivity score/percentage — 3/4 (AW none) → common, NOT definitional.
- Idle/AFK gating of attribution — AW documented; DeskTime idle detection claimed in reviews/copy; RT behavior implied → common.
- Manual/offline activity entry — 3/4 documented (AW manual features page exists; RT, DeskTime) → common.
- Pause/privacy control (AW pause logging, DeskTime Private time, Rize approval flow) — 3/4 documented → common.
- Desktop agent + dashboard + (often) mobile companion — 4/4 desktop; mobile companion 2/4 documented.
- Project/billable layer — 3/4 (AW deliberately not) → optional straddle toward Time Tracking.
- Blocking/focus actuation — 2/4 (AW explicitly refuses) → optional, drifts toward Focus Timer/wellbeing.
- AI summaries/ML mapping — 2/4 current-generation → era machinery, optional.
- Org-facing dashboards/screenshots — tier-dependent → variant.

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **Ambient automatic capture of active usage** — a background agent continuously observes which application/website (commonly with window/document title, often URL) holds the person's attention and attributes durations to it, with nothing for the user to start or stop (idle detection commonly gates attribution). *Remove → user-initiated timers = Time Tracking Application; manual diaries = pre-software time logs.*
2. **The persistent usage record** — captured activity accumulates into a reviewable personal history: a timeline of what was used when, plus aggregated allocations per app/site/category over days and longer spans. *Remove → a live "current app" indicator or system monitor with no memory.*
3. **The productivity-interpretation layer** — raw usage is organized into meaningful classes (productivity levels or categories, via vendor-default taxonomies, user-defined rules, or learned mapping) through which the person — or, in org-facing tiers, their organization — reads the record as "how time was actually spent" and acts on it (goals, alerts, habit change). *Remove → a raw event log; the platform screen-time recorder, which keeps usage stats but serves limits/downtime rather than a work-productivity reading, also falls out of the Type.*

Jointly-held is load-bearing: 1+2 without 3 = a screen-time/wellbeing recorder (platform Screen Time class); 1+3 without 2 = a live productivity meter with no history; 2+3 without 1 = a self-entered time log (Time Tracking lineage).

### L1 — Common Mature Structure

- productivity score / productive-vs-unproductive percentages (3/4 sampled)
- reports and trends over weeks/months/years; weekly summaries
- goals and real-time alerts keyed to the interpretation layer
- idle/AFK detection gating attribution
- manual/offline activity entry folded into the same record
- deeper capture via browser extension and document-title tracking
- pause logging / private time
- category editing / re-classification surfaces
- mobile companion apps
- exports, API, calendar/PM-tool integrations

### L2 — Variant / Optional Structure

- data residence: local-first (AW) vs vendor cloud (RT, DeskTime, Rize); sync maturity varies
- audience posture: personal self-tracking vs team/employer-visible record (DeskTime's dual "for managers / for employees" framing; Rize's employee-approval flow)
- actuation bundle: distraction blocking / focus sessions (RT, Rize; AW refuses) — drifts toward Focus Timer / wellbeing blocker
- project/client/billable attribution (RT Timesheets, DeskTime, Rize) — drifts toward Time Tracking
- org surveillance depth: optional screenshots as proof-of-work (DeskTime) — drifts toward employee monitoring; Rize/RT explicitly refuse screenshots/keystrokes
- AI summaries / ML session mapping (DeskTime, Rize) — era machinery
- platform-native realization: Apple ScreenTime-class utilities keep capture + record + categories but serve limits/downtime, not the productivity reading — adjacent, not in-Type

### L3 — Vendor-specific (research notes only)

- RescueTime: The Assistant daily hub; Daily Highlights notes; Highlights Report for timer sessions; keyword search over reports; free-vs-premium history windows; "Personal or Distracting" level naming; iOS Screen Time integration; 15+ years / 2M+ users / 3B hours marketing claims.
- ActivityWatch: watcher architecture (aw-watcher-window/afk/web), buckets/events/heartbeats data model, localhost server, regex rules matched on app/title (URL matching planned), aw-server-rust migration, Pro subscription/donations, Thankful app, quantified-self/lifelogging positioning.
- DeskTime: the "52/17" work-break marketing claim; screenshots proof-of-work; shift scheduling/absence/attendance/IP location suite; ISO/GDPR security stack; reseller/affiliate programs; 730k+ users marketing claim.
- Rize: Screen Text opt-in; MCP server for AI assistants; profitability/utilization dashboards; AI tools ranking page; client-ready scheduled reports; profit/rate calculators.

## Boundary Findings

- **vs Time Tracking Application (§ sibling, unprocessed)** — seam: *who starts the clock and what the record is for*. Time Tracking centers user-initiated timers/entries organized by project/task/client for reporting and billing; this Type centers ambient capture organized by usage interpretation for productivity understanding. Market blurs deliberately: RescueTime sells "Focus" and "Timesheets" as two tools on one app (vendor-drawn seam, first-hand); DeskTime and Rize bundle project/billable layers onto the ambient record. Test: remove ambient capture (everything user-started/manual) → Time Tracking; remove billable/project center-of-gravity → this Type remains.
- **vs Focus Timer (§ sibling, processed 2026-09-07)** — their recorded seam ratified from this side: focus timer runs deliberately initiated bounded sessions; this Type measures ambient usage without sessions. Bundling observed in both directions: RT Focus Sessions and Rize focus detection/blocking live *inside* trackers as support capabilities; test (theirs): remove the ambient record → focus timer. Rize is the market's clearest straddling pole (both centers, neither absorbed).
- **vs Time Blocking Application (§ sibling, unprocessed)** — seam: plan-future vs record-past. Trackers occasionally touch planning (RT Assistant shows the meeting schedule; daily target goals) but the accumulated record is the center. Test: remove the record, keep the plan → Time Blocking.
- **vs Personal Dashboard (§ sibling, processed 2026-09-08)** — their row stands: a tracker measures one activity domain as its record (computer usage); a personal dashboard composes many sources into a cross-domain overview. A tracker's dashboard is a capability of this Type; the composed cross-domain surface is that Type.
- **vs platform screen-time / digital wellbeing utilities (no directory leaf)** — official ActivityWatch comparison separates Apple ScreenTime by purpose: "focused on app limits and downtime" with "basic reporting… little customization", vs trackers' productivity reading and customization. Structural: screen-time utilities hold legs 1+2 (capture + record) but lack the productivity-interpretation leg as the organizing purpose; enforcement (app limits) replaces it. Taxonomy note for maintainers: no leaf exists for this adjacent platform-native Type.
- **vs Digital Employee Experience Management (§14, processed 2026-09-08)** — both run endpoint agents, but DEXM's record is device/application *performance and experience* telemetry serving IT's experience-operations loop; this Type's record is the person's *usage allocation* serving productivity understanding. No conflict with DEXM's own L0 (their third leg — IT-owned operations loop — is absent here).
- **vs org-facing employee monitoring / UAM (no exact directory leaf)** — DeskTime markets itself simultaneously as "automatic time tracking" and "employee monitoring software"; screenshots-as-proof-of-work is the drift marker toward surveillance, and Rize/RescueTime explicitly differentiate by refusing keystrokes/screenshots. Seam (proposed): who the record serves — the tracked person's self-understanding (this Type, with org visibility as a variant) vs organizational oversight/compliance with capture depth beyond usage metadata (monitoring). Taxonomy note: the UAM/employee-monitoring market has no directory leaf; nearest neighbors are this Type and DEXM; the insider-risk-management pass (§15, processed) already flagged this neighborhood.
- **vs Task Mining Platform (§10, processed 2026-09-08)** — task mining captures user-interaction streams for *process analysis* of business workflows (organizational BPM context); this Type's record is personal daily usage for productivity reading. Different object, different audience; noted because the capture mechanism (foreground app/window observation) is shared.
- **§24 historical / market-sample check — passed.** Late-2000s-generation trackers (RescueTime's own 15+ years claim; ManicTime via official comparison) satisfy all three legs with no cloud requirement, no AI, no mobile apps. The definition names no cloud sync, no AI mapping, no productivity score, no mobile capture — all held as standard/optional. The platform-native probe (Apple ScreenTime) deliberately fails leg 3, confirming the productivity frame is the leaf's load-bearing qualifier rather than era bias. No analog-era ancestor exists or is claimed: ambient observation of foreground usage is inherently a software capability; manual time journals belong to the Time Tracking lineage instead.

## Uncertainties

- Help-center depth not reached for any product (help.rescuetime.com, help.desktime.com unfetched); attribution mechanics (exact idle thresholds, what counts as "active", multi-display behavior) are documented only at FAQ level for AW/RT — no numeric claims made anywhere.
- ActivityWatch productivity weighting: the docs' categorization machinery carries no productivity weights; whether any AW UI surface computes a productivity metric was not confirmed — AW is treated as the no-score pole, which only strengthens the claim that scoring is non-definitional.
- Rize's exact current center of gravity (personal productivity coach vs team billable visibility) is shifting per its own marketing; treated as a straddling pole, not as evidence for either sibling Type's core.
- DeskTime's screenshots feature is documented as existing and optional ("proof-of-work in cases of questionable productivity or integrity"); default-on/off state and config depth not verified.
- Whether offline/manual entries are ever auto-classified into productivity levels in DeskTime (RT documents it explicitly) — unverified.
- No claims drawn from ManicTime, Timely, Time Doctor, memtime, or ActivTrak beyond the one official AW comparison article (B-layer only).

## Final Synthesis

The Productivity Activity Tracker is the automatic observer of computer work: it watches which application, website, or document holds the user's attention, accumulates those observations into a durable usage record, and organizes the record through a productivity lens — categories and/or productivity levels, vendor-default, user-ruled, or learned — so that the person (or, in team tiers, their organization) can see how time was actually spent and act on that reading. Nothing about the defining core requires a score, a cloud, a blocklist, a billable hour, or an employer dashboard: those are the market's common and optional furniture. The Type's identity is held by the three jointly-bearing structures (ambient capture + persistent record + productivity interpretation), and its edges are exactly where those structures give way: where the user must start the clock, it becomes Time Tracking; where the user starts a deliberate session, it becomes a Focus Timer; where the record plans the future, Time Blocking; where usage stats serve limits rather than a productivity reading, platform screen-time territory; where the record serves organizational oversight with capture depth beyond usage metadata, employee monitoring — a market the directory does not yet carry as its own leaf.
