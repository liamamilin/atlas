# Research Notes — Personal Dashboard

Research date: 2026-09-08
Methodology: WORKFLOW v1.1 / WRITING GUIDE v1.1

## Research Goal

Understand what a **Personal Dashboard** actually is as an Application Type, from real products: what the central surface is, what units it is composed of, what data those units surface, how the surface stays current, what users do on it (and what they deliberately do elsewhere), and where the boundary lies against the sibling leaves in 03.13 (Personal Organizer, Life Planning Application), the organizational Dashboard Platform (§13), Information Portal (§02.11), Bookmark Manager (§02.13), and the single-purpose personal apps (to-do, calendar, habit, finance) whose data dashboards mirror.

## Initial Boundary (hypothesis before research)

- Hypothesis: a personal, self-facing **composed surface** — one standing screen assembled from multiple widgets/panels, each surfacing a slice of the person's own life data (tasks, calendar, habits, weather, metrics, links), used at the start of a day/session to orient at a glance.
- Adjacent Types suspected upfront:
  - Personal Organizer (sibling leaf in 03.13, unprocessed) — the working PIM where records are created vs the dashboard as a view over them
  - Life Planning Application (sibling, processed) — holds a plan of record; a dashboard only displays progress
  - Dashboard Platform (§13, processed) — organizational data display; prior pass recorded "name collision only"
  - Information Portal (§02.11, processed) — prior pass set the removal test: widgets showing only the user's own data/tasks → Personal Dashboard
  - Bookmark Manager (§02.13) — link-centric start pages
  - To-do / Calendar / Habit / Personal Finance applications — the systems of record the dashboard mirrors
  - Platform-native widget boards (iOS/Android/Windows) — possible variant or separate phenomenon
- Known risks: the market label "dashboard" is loose (BI dashboards, car dashboards, admin dashboards all use the word); the start-page family straddles bookmark managers and portals; quantified-self aggregators may be their own thing.

## Research Questions

1. What is the central structure — the widget? the composed surface? both?
2. What data do the units surface — only the person's own data, or also external content (weather, news, feeds)?
3. Is the data native (entered in the product) or aggregated/mirrored from other services and apps? Which posture is definitional?
4. How is the surface composed and customized (add/remove/arrange/configure units; layouts; themes)?
5. What interactions happen on the surface — glance only, light actions, or deep work?
6. What delivery surfaces exist (browser new tab, web start page, desktop widget layer, OS-native boards, mobile app)?
7. How does the surface stay current (live, periodic sync, manual)?
8. Who uses it, and when in their day/session?
9. What does the product NOT do — where are the lines vs organizer, planner, task manager, portal, BI dashboard?
10. Historical check: would the 2000s widget/start-page era (iGoogle, Netvibes, macOS Dashboard, Yahoo Widgets, Palm Today screen) satisfy the same model? Is there any paper-era analog?

## Representative Products

Selected for different product philosophies, delivery surfaces, and data postures:

| Product | Pole | Delivery | Data posture | Customer level | Evidence |
|---|---|---|---|---|---|
| Momentum | focus/productivity new-tab dashboard | browser extension (new tab) | native-light (own todo/focus) + weather | professionals, freemium + Teams | homepage (Layer A) |
| Exist | quantified-self aggregation dashboard | web + iOS + Android | aggregation-heavy (services + manual entry) | self-trackers, subscription | homepage + KB (Layer A) |
| Protopage | classic web start page | web | personally-selected streams (RSS/bookmarks/sticky notes) | consumers, free | homepage (Layer A, thin — JS-limited page) |
| Rainmeter | compose-your-own desktop widget engine | Windows desktop | display skins over system/personal data | enthusiasts, free OSS | homepage (Layer A) |
| Apple widgets (iOS) | platform-native widget boards | Home Screen / Lock Screen / Today View | mirrored app data | all iOS users | official support article (Layer A) |

Dropped / not sampled (with reasons):

- **start.me** — personal start page; two fetch timeouts. Abandoned per network rule; the start-page pole rests on Protopage (thin) only.
- **Gyroscope** (quantified-self health dashboard) — gyroscope.com is a physical gyroscope toy shop (domain collision); correct product domain not identified without guessing. Dropped.
- **Netvibes** — netvibes.com/en returned 404; personal product status unverified. Used only as a reasoning anchor in the historical check, never as evidence.
- **Momentum help center** (momentumdash.help) — transport error; Momentum detail limited to its homepage.
- **iGoogle** (discontinued 2013) — historical anchor via reasoning, not sampled.

## Sources

Fetched 2026-09-08 (all Layer A direct observation unless noted):

- Momentum — https://www.momentumdash.com/ (home: positioning, widget set, Plus/Teams)
- Exist — https://exist.io/ (home: model, services list, pricing), https://kb.exist.io/ (KB structure), https://kb.exist.io/article/19-whats-the-difference-between-a-service-and-an-attribute (service/attribute data model)
- Protopage — https://www.protopage.com/ (home; page is JS-heavy, only partial text retrieved — thin evidence)
- Rainmeter — https://www.rainmeter.net/ (home: positioning, skins, license, community)
- Apple — https://support.apple.com/en-us/HT207122 "How to add and edit widgets on your iPhone" (widget mechanics, stacks, Lock Screen/Today View)

Source-access limitation: start.me unreachable (2 timeouts), Momentum help center unreachable (transport error), Netvibes 404, Gyroscope domain collision. Claims for the web-start-page pole are therefore thinner than for the other poles; no precise operational details (limits, sync intervals, pricing tiers beyond what pages state) are asserted anywhere.

## Product Observations

### Momentum

Evidence: Layer A (official homepage).

- Self-positioning: "Turn your New Tab page into a focused, productive, and inspiring dashboard." A **start page** that replaces the browser new tab.
- Widget set visible on the page: **Daily focus** ("What is your main focus for today?" — a single intention for the day), **To-do list** (with completion count, "+ New Todo"), **Links and bookmarks** ("+ New Link" with name/address), **Weather and more** (current conditions + multi-day forecast for a named location), **Search** box, **greeting** ("Good afternoon, Sam."), **daily inspiration** (photo + quote/mantra).
- **Focus mode**: "Create a deep work routine with sounds, timers and focus-enhancing apps."
- **Plus tier**: "Customize", "Integrations", "Power-ups" — customization and integrations are paid capabilities.
- **Teams**: "Momentum for your team — Get on the same page" (team variant exists).
- Scale claim: 3+ million active users (marketing figure, recorded as claim only).
- Help center exists at momentumdash.help (unreachable this pass).

### Exist

Evidence: Layer A (official homepage + KB article).

- Self-positioning: "Exist · Understand your behaviour." "Track everything in one place. See numbers about things like your health, activity, productivity, social media, and local weather all together."
- Data model (KB, verbatim): a **"service"** is an app you sync data into Exist (Fitbit, Todoist, Oura); an **"attribute"** is a single type of data tracked about yourself (tracks played, steps today, time active, wind speed, min/max temperature from WeatherKit).
- **Aggregation posture**: "Data syncs automatically from connected services, so your step count and time asleep are right next to manual data points, like your energy level and how many coffees you drank."
- Connected services listed: Apple Health, Health Connect, Fitbit, Garmin, Oura, Withings, Strava, RescueTime, Todoist, Toggl, GitHub, Instapaper, Mastodon, Calendar, Swarm, Last.fm, Trakt, Apple Weather, Spotify/Deezer (via Last.fm).
- **Manual tracking**: custom data points as "a quantity, time period, scale from 1–9, percentage, or time of day. Or just add a tag to a day" — usable as habit tracker, medication/symptom record, subjective measures.
- **Analysis layer**: daily insights, long-term trends and averages, **correlations** ("Which habits go together?" — "What makes me happiest?"), mood tracking, weekly summary email.
- Pricing: $6.99/month, single plan; Android, iOS, web.
- Data stance: "Exist is for you to track and understand yourself, not so others can find out how to better sell you things."

### Protopage

Evidence: Layer A but thin (JS-heavy page; only partial text retrieved).

- Self-positioning: "Free Personalized Start Pages"; "an award winning RSS reader. Use it to read RSS feeds, keep bookmarks, sticky notes and to share information."
- "RSS widgets to you as part of an **Ajax dashboard start page**."
- Also marketed as: "an intranet dashboard, an intranet portal, employee portal or web portal" — the vendor itself straddles the portal seam.
- Unit types confirmed: RSS feed widgets, bookmarks, sticky notes, sharing.

### Rainmeter

Evidence: Layer A (official homepage).

- Self-positioning: "desktop customization tool… display customizable skins on your desktop, from hardware usage meters to fully functional audio visualizers."
- **Skins** are the unit: community-created, installable, modifiable; "Create and modify your own skins in a simple language"; "Rainmeter is not just an application, it is also a robust toolkit."
- Skin gallery shown: weather, clocks, system meters, audio visualizers.
- Free, open source (GNU GPL v2), Windows 7–11; docs at docs.rainmeter.net; community forum/Discord/IRC.
- The desktop itself becomes the composed surface; there is no single "dashboard page" — the whole desktop is the canvas.

### Apple widgets (iOS)

Evidence: Layer A (official support article, published 2025-09-17).

- "With widgets, you get **timely information from your favorite apps at a glance** on your Home Screen, Lock Screen, or Today View."
- Widget examples: weather, calendar events, temperature, air quality, battery level.
- Mechanics: add/remove/move widgets; choose widget **size**; **edit widget** configuration (e.g., Weather widget location); widget **stacks** ("stack up to 10 widgets"); **Smart Stacks** ("displays the right widget based on factors like your location, an activity, or time… automatically rotates widgets to show the most relevant information throughout the day"); **Widget Suggestions** (apps can automatically appear based on past activity).
- Surfaces: Home Screen, Lock Screen (iOS 16+), Today View (swipe right).
- Note: the OS home screen is the composed surface; widgets mirror data from the user's apps. The user composes; the OS hosts.

## Cross-product Comparison

| Structure | Momentum | Exist | Protopage | Rainmeter | Apple widgets | Strength |
|---|---|---|---|---|---|---|
| One standing personal surface the user returns to | A ✓ (new tab) | A ✓ (daily overview, web+app) | A ✓ (start page) | A ✓ (the desktop) | A ✓ (Home/Lock/Today View) | Universal in sample |
| Multiple independent units composed on it | A ✓ (focus/todo/links/weather/search) | A ✓ (attributes across domains) | A ✓ (RSS/bookmark/sticky widgets) | A ✓ (skins) | A ✓ (widgets, stacks) | Universal in sample |
| User composes the surface (add/remove/arrange/configure) | A ✓ (Plus "Customize") | A ✓ (choose services/attributes) | A ✓ (add widgets) | A ✓ (install/edit skins) | A ✓ (add/edit/move/stack) | Universal in sample |
| Units surface the person's own situation | A ✓ (your todos, your focus, your weather) | A ✓ (your steps, sleep, mood, services) | A ✓ (your feeds, your bookmarks, your notes) | A ✓ (your system, your weather) | A ✓ (your apps' data) | Universal in sample |
| Kept current (automatic refresh/sync) | A ✓ (weather; todo persists) | A ✓ ("syncs automatically") | A ✓ (RSS widgets refresh) | A ✓ (live meters) | A ✓ ("timely information") | Universal in sample |
| At-a-glance posture; light interaction only | A ✓ (check todo, set focus) | A ✓ (quick manual entry) | A ✓ (read headlines, jot sticky) | A ✓ (display; some skins interactive) | A ✓ (glance; taps into apps) | Universal in sample |
| Records of record / deep work live elsewhere | A ✓ (todo is lightweight; focus routine is a pointer) | A ✓ (source services hold the data) | A ✓ (feeds consumed at source) | A ✓ (skins display) | A ✓ (widgets open their apps) | Universal in sample |
| Widget catalog spanning life domains | A ✓ (todo/focus/links/weather) | A ✓ (health/productivity/social/weather) | A ✓ (news/bookmarks/notes) | A ✓ (clock/weather/system/media) | A ✓ (weather/calendar/battery/air quality) | Universal in sample |
| Appearance layer (backgrounds, themes, aesthetics) | A ✓ (daily photo + quote) | ✗ not part of the product | A ~ (customizable page) | A ✓ (the entire point) | A ~ (wallpaper context) | Common, not universal |
| Aggregation from third-party services via connectors | A ~ (Plus "Integrations") | A ✓ (the core mechanic) | A ~ (RSS is the connector) | A ~ (skins poll sources) | A ✓ (widgets mirror apps) | Common; heavy only in the quantified-self pole |
| Insights/analytics over the data | ✗ | A ✓ (correlations, trends, weekly email) | ✗ | ✗ | ✗ | Single-product in sample — Optional |
| Native data entry beyond light edits | A ~ (todo/focus are native) | A ✓ (manual attributes/tags) | A ✓ (sticky notes) | ✗ | ✗ | Varies by pole |
| Team/sharing variant | A ✓ (Teams) | ✗ | A ✓ ("share information") | ✗ | ✗ | Optional |
| AI assistance | ✗ not documented | ✗ not documented | ✗ | ✗ | A ~ (Smart Stack "Smart Rotate"/suggestions — curation intelligence, not AI chat) | Era-current optional |

Reading of the table:

- Seven structures hold across all five sampled products (Layer B, universal-in-sample): one standing personal surface; multiple independent units; user composition; the person's own situation as substrate; currency; at-a-glance posture with light interaction; records of record elsewhere.
- Everything else varies by pole: appearance layer, aggregation mechanics, insights, native entry, sharing.

## Canonical Model (synthesis)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable as a Personal Dashboard — three jointly-held structures:

1. **The composed personal surface** — one standing screen the person owns and returns to, assembled by the user from multiple independent widget units (chosen, arranged, configured by the person). Remove → a single-purpose app (one widget alone) or a vendor-organized page (no composing hand → portal/feed territory).
2. **The person's own life as the data substrate** — every unit surfaces a slice of the person's own situation: their tasks, events, metrics, habits, environment (their weather, their location), or personally-selected streams. The person is both the subject and the only audience. Remove → public portal, kiosk display, or an organizational dashboard.
3. **At-a-glance currency** — the surface is kept current (automatic refresh or sync) and built for glance-and-go orientation with light interactions; the records of record and deep work live in other applications, which the dashboard mirrors, summarizes, or links to. Remove the currency → a static snapshot; remove the glance posture (the surface becomes where records are created and managed) → a personal organizer/PIM.

Jointly-held is load-bearing:

- 1 alone = a generic widget platform / portal start page (no personal substrate)
- 2 alone = scattered single-purpose apps / raw personal data
- 3 alone = a public display or kiosk
- 1+2 without 3 = a personal organizer / PIM workspace (the sibling seam)
- 1+3 without 2 = a generic widget board (clock and weather for anyone)
- 2+3 without 1 = the underlying apps themselves

Anti-overfitting notes:

- **Aggregation from third-party services is NOT definitional.** Momentum's core widgets are native-light; Apple's widgets mirror whatever apps the user has; Exist aggregates everything. The canonical concept is "the person's own situation, however sourced" — connectors are a common implementation.
- **Any specific widget set is NOT definitional.** Weather/todo/calendar are the most common trio but Rainmeter ships system meters and Exist ships mood attributes; the catalog is open-ended.
- **The browser new tab is NOT definitional** — it is one delivery surface among five distinct ones in the sample.
- **Insights/correlations are NOT definitional** — single-product in sample (Exist), held as Optional.

### L1 — Common Mature Structure

Widespread in mature modern products, not required for the definition:

- widget catalog spanning life domains: tasks/todo, calendar/events, weather, clock/date, notes, links/bookmarks, news/RSS feeds, habits, fitness/activity, sleep, media, system stats (battery/CPU), finance figures
- light actions on the surface: check off a todo, add a link, log a value, jot a note
- layout and appearance customization: arrange, resize, themes, backgrounds, dark mode
- an inspiration/aesthetic layer: photos, quotes, greetings (signature of the new-tab pole, common beyond it)
- search entry on the surface
- cross-device sync of surface configuration and data
- connectors/integrations to source services and apps
- notifications/reminders surfaced on or from the surface
- insights/analytics over aggregated personal data (trends, correlations, summaries) — Optional, quantified-self pole
- sharing/team variants — Optional

### L2 — Variant / Optional Structure

- **Delivery surface**: browser new tab (Momentum) / web start page (Protopage, start.me) / desktop widget engine (Rainmeter) / OS-native widget boards (iOS Home Screen, Lock Screen, Today View; Android/Windows equivalents) / dedicated mobile+web app (Exist)
- **Data posture**: native-light (Momentum's own todo/focus) vs aggregation-heavy (Exist: services + manual attributes) vs mirrored-only (Apple widgets display app data)
- **Purpose flavor**: focus/productivity (Momentum), quantified-self (Exist), information start page (Protopage), aesthetic desktop (Rainmeter), general at-a-glance (iOS)
- **Composition freedom**: curated fixed set with optional customization (Momentum free tier) vs fully compose-your-own (Rainmeter skins, Protopage widgets)
- **Curation intelligence**: static user arrangement vs auto-rotating context-aware stacks (Apple Smart Stacks/Smart Rotate/Widget Suggestions)
- **Monetization**: free extension + paid tier (Momentum Plus), single-plan subscription (Exist), free with ads (Protopage), free OSS (Rainmeter), OS-bundled (Apple)

### L3 — Vendor-specific Structure

- Momentum: the daily-focus question as a first-class widget; mantra/quote of the day; focus mode with sounds/timers; Teams edition; Chrome-store distribution
- Exist: attribute entry types (quantity / time period / scale 1–9 / percentage / time of day / tags); correlation engine; mood tracking; weekly summary email; single $6.99/mo plan; "data values" privacy stance
- Protopage: sticky-note widgets; RSS-reader framing; "intranet dashboard / employee portal / web portal" positioning (vendor-side straddle of the portal seam)
- Rainmeter: skin authoring language; community skin ecosystem (DeviantArt/forum); GPL v2; Windows-only
- Apple: Smart Stacks, Smart Rotate, Widget Suggestions, stack limit of 10, Lock Screen widget zone, per-widget size classes

## Historical / Market-Sample Check (§24 reasoning, marked reasoning-based)

Question: would older, regional, platform-native, or differently positioned products still fit the L0?

- **iGoogle (2005–2013)**: personalized start page with user-added gadgets (gmail preview, weather, todo, news feeds, clocks) — composed surface ✓, personal substrate ✓, at-a-glance currency ✓. Pass.
- **Netvibes / Pageflakes era start pages (2005+)**: same trio. Pass (reasoning anchor; Netvibes unreachable this pass).
- **macOS Dashboard (2004+), Konfabulator/Yahoo! Widget Engine (2002+), Windows Sidebar gadgets (2006+)**: desktop widget layers over personal/system data (clocks, weather, calendars, system meters). Pass — confirms the desktop-engine pole predates the mobile era.
- **Palm/PocketPC "Today" screens (2000s)**: at-a-glance home screen showing appointments, tasks, email counts — platform-native ancestor of the OS widget board. Pass.
- **Paper-era analog**: none satisfies the composed-surface leg — a desk blotter or wall calendar board is a single-purpose surface, and the Filofax-style organizer is the *organizer's* ancestry, not the dashboard's. The Type is genuinely screen-era; its ancestry is the 2000s widget/start-page wave. The definition requires no modern capability (cloud sync, AI, mobile apps, connectors) — the iGoogle-era form satisfies the core fully.

Conclusion: the L0 survives the historical check; nothing modern is required. The Type's ancestry is the 2000s widget/start-page era, not paper.

## Vendor-specific Findings

Recorded above under L3. None promoted into the canonical document beyond neutral, non-branded description.

## Rejected Findings

Candidate structures considered and rejected for the defining core:

1. **Third-party service aggregation/connectors** — core mechanic for Exist, absent-or-light for Momentum/Protopage/Rainmeter. Rejected as invariant; the canonical concept is "the person's own situation, however sourced."
2. **The browser new tab as the surface** — Momentum's delivery, but four other delivery surfaces in sample. Held as a variant.
3. **Insights/correlations/analytics** — single-product in sample (Exist). Optional; also the seam toward a hypothetical "personal analytics" Type for which no directory leaf exists.
4. **A fixed widget set (weather + todo + calendar)** — the most common trio, but Rainmeter (system meters) and Exist (mood attributes) prove the catalog is open-ended. The widget catalog is a common structure, not a fixed list.
5. **Aesthetic/inspiration layer (photos, quotes)** — signature of the new-tab pole, absent in Exist. Common, not definitional.
6. **Deep-work tooling (focus timers, routines)** — Momentum-specific apparatus sitting *on* the dashboard; the dashboard's own job remains orientation. Held as vendor/optional capability.
7. **Team/sharing** — 2/5 sample, optional.
8. **Manual data entry as defining** — Exist's manual attributes and Protopage's sticky notes have it; Apple widgets and Rainmeter are display-only. Light interaction is the invariant; substantial native data entry is a pole, not the Type.

## Boundary Findings

| Nearby Type | Distinguishing test |
|---|---|
| **Personal Organizer** (sibling 03.13, unprocessed) | The organizer is the working application where the person's records of record are created and managed (events, tasks, contacts, notes as editable records); the dashboard is the composed at-a-glance view over such data, mostly mirrored or lightly edited. Removal test: if the surface is where the user's records live and work happens → organizer; if it is a standing overview over data largely generated elsewhere → dashboard. Momentum's lightweight native todo shows the dashboard pole can hold thin native data without becoming an organizer — the todo exists for the glance. **Joint review recommended with the personal-organizer pass.** |
| **Life Planning Application** (sibling 03.13, processed) | Confirmed from this side: a dashboard can *display* goal/habit progress but holds no plan of record — no goals, decomposition, or review loop. Remove the plan-of-record requirement and the dashboard remains a dashboard. |
| **Dashboard Platform** (§13, processed) | Confirmed "name collision only" from this side: organizational display systems over connected data sources with distribution to viewers vs a person's self-facing life widget board. Substrate (organizational metrics vs personal life), audience (team/viewers vs the single person), and composition hand (builder vs the person themselves) all differ. |
| **Information Portal** (§02.11, processed) | Confirmed from this side with that pass's removal test: widgets surfacing only the user's own data/tasks → Personal Dashboard; operator-organized public information with onward routing → portal. Protopage is the live drift specimen: RSS widgets carry external published content (portal-ish), but the selection is personal and the page is user-composed; the vendor itself also markets "intranet portal" positioning. |
| **Bookmark Manager** (§02.13) | Link-centric start pages (grids of saved links) are bookmark-manager territory; a dashboard's units are live data slices. Products that are primarily link collections with a widget veneer straddle the seam; the substrate test (links vs live personal data) decides. |
| **To-do / Calendar / Habit / Personal Finance applications** | Those Types hold the data of record for their domain; the dashboard mirrors, summarizes, or lightly edits it. A dashboard todo is a glance list, not a task management system; a dashboard calendar widget is a view, not a calendar of record. |
| **Productivity Activity Tracker** (§03.14) | The tracker automatically measures one activity domain as its record (e.g., computer usage); Exist *consumes* such trackers as services and spans all life domains. A tracker's own overview screen is a capability of that Type; the cross-domain composed overview is this Type. |
| **Personal Finance Management** (§08) | Money-domain system of record; a PFM's home screen is a capability of that Type, not this one. |
| **Smart-home dashboards** | Device/home substrate, not the person's life data; different Type (no directory leaf; out of scope here). |

"去掉什么就变成另一个 Type" 判据总结：

- remove the user's composing hand (vendor-fixed layout) → information portal / personalized feed
- remove the personal substrate (public/operator content) → portal / kiosk / org dashboard
- remove the multi-unit composition (one widget) → single-purpose app
- remove currency → a static snapshot/document
- remove the glance posture (records created and managed here) → personal organizer / PIM
- remove the standing surface (ephemeral) → a notification shade / transient view

## Uncertainties

1. The web-start-page pole is under-evidenced: start.me unreachable (2 timeouts), Protopage thin (JS-limited page), Netvibes 404. Start-page-specific operational claims were kept to what Protopage's page states.
2. Momentum's help center was unreachable; Momentum detail is homepage-level. Widget behavior details (sync, offline, per-widget config) unverified.
3. Whether the quantified-self aggregation pole (Exist) should eventually be a separate "personal analytics" Type — no directory leaf exists for one; held inside this Type as a pole, flagged for future taxonomy review if such a leaf is ever added.
4. The seam vs Personal Organizer is defined from this side only; the organizer leaf is unprocessed. Joint review recommended.
5. Android/Windows widget-board documentation was not fetched; the platform-native pole rests on Apple's article plus reasoning that other OS vendors ship equivalent surfaces. Claims kept generic.
6. Insights/analytics held Optional on single-product evidence (Exist); a second aggregation product (Gyroscope) could not be reached to corroborate.

## Final Synthesis

A Personal Dashboard is a **personal at-a-glance overview surface**: one standing screen the person composes from multiple independent widgets, each surfacing a slice of their own life — tasks, events, metrics, habits, environment, or personally-selected streams — kept current automatically, designed for glance-and-go orientation with light interactions, while the records of record and deep work remain in the applications the dashboard mirrors, summarizes, or links to. The defining core is the jointly-held trio: composed personal surface + the person's own life as data substrate + at-a-glance currency. Aggregation connectors, any specific widget set, the new-tab delivery, aesthetics, insights, and team variants are common or optional structures, not the definition. The Type's ancestry is the 2000s widget/start-page era (iGoogle, desktop widget engines, PDA Today screens), which satisfies the core without any modern capability. Boundaries are held against the Personal Organizer (records of record vs view), Life Planning Application (no plan of record), Dashboard Platform (organizational vs personal), Information Portal (own data vs public information), Bookmark Manager (links vs live slices), and the single-purpose domain apps whose data the dashboard mirrors.
