# Research Notes — Event Mobile App

Research date: 2026-09-10
Leaf: Event Mobile App (§26 Travel, Hospitality, Food Service & Events)
Slug: event-mobile-app

## Research Goal

Understand the attendee-facing "event app" as an Application Type in its own right: what the product is bound to, who authors it, who uses it, what it contains, how it is published and updated, and where its boundaries sit against the already-processed event-family Types (Event Management Platform, Event Registration Platform, Event Agenda Management, Attendee Management, Event Credential/Badge Management, Event Lead Retrieval, Audience Response System, Convention/Exhibition Management, Festival Management).

This leaf carries two pending joint-review obligations from sibling passes:

1. **event-agenda-management (2026-09-07)** recommended joint review with event-mobile-app + speaker-management ("sibling leaves sharing the session/speaker data spine; Cvent-class vendors span all three").
2. **attendee-management (2026-09-06)** recommended boundary cross-check when Event Registration Platform, Event Credential/Badge Management and Event Mobile App are processed.

Also relevant: **event-management-platform (2026-09-07)** lists "event apps & engagement" as an *optional* capability of that Type — this pass must decide whether the event app is merely that capability (fold) or an independently recognizable Type (keep), given that standalone app-first products exist.

## Initial Boundary

Working hypothesis before research:

- The Event Mobile App is the **attendee-facing mobile application published for a specific event** — the "conference app" / "event app" category (Whova, EventMobi, Guidebook, Attendify, Swapcard, Cvent Attendee Hub).
- Nearest neighbors: Event Management Platform (organizer-side lifecycle; the app is one of its optional surfaces), Event Agenda Management (the program record the app presents), Attendee Management (the roster the app authenticates against), Community Platform (year-round drift), Virtual Event Platform (virtual venue center), Audience Response System (in-app polls/Q&A).
- Main taxonomy risk: the Type may be argued to be a **delivery surface / module** of Event Management Platforms rather than a Type. Counter-evidence to check: standalone products whose entire center is the event app.

## Research Questions

1. What is the app bound to — one event, an event series, an organizer's portfolio? How is the container created and published?
2. What content does the organizer author into the app (program, people, places, info, announcements)?
3. How do attendees get in — app-store download, event code, login via registration data, guest/no-login access, SSO?
4. What does the attendee do in the app — personal agenda, navigation, updates, networking, engagement, content?
5. What organizer-side machinery exists — builder console, analytics, access control, moderation?
6. How does the app behave across the event lifecycle (before / during / after), and what happens to it after the event?
7. What are the publication variants — single-event app, multi-event container app, branded/white-label app, web app vs native app?
8. Where are the boundaries: vs EMP, agenda management, attendee management, badge management, community platform, virtual event platform, ARS, social network?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| **Whova** | App-first all-in-one; networking/community-led; the market's most-cited "event app" | Associations, universities, conferences, community events |
| **EventMobi** | App-centered all-in-one platform; deep organizer console ("Experience Manager") | Associations, agencies, corporations |
| **Guidebook** | Self-serve guide/app builder; broader-than-events (campus, tours, EHS); "no login required" posture | Higher education (current focus), associations, nonprofits |
| **Swapcard** | AI-matching / exhibitor-ROI-first; mobile & web app as one surface of a revenue platform | Trade shows, conferences, hosted-buyer programs |
| **Cvent Attendee Hub** | Engagement layer (web + mobile) inside the dominant enterprise event suite | Enterprise |

Market anchors not sampled (noted for breadth): Attendify (acquired by Cvent 2021), vFairs / Hopin-class virtual-event platforms with app surfaces, EventsAir / Stova / Bizzabo suites.

## Sources

Fetched 2026-09-10:

- Whova — Event App product page + FAQ: https://whova.com/whova-event-app/ (Tier 2)
- EventMobi — Event Apps product page: https://www.eventmobi.com/event-apps/ (Tier 2); root: https://www.eventmobi.com/ (Tier 2); **Knowledge Base, Event Organizers section: https://help.eventmobi.com/en/knowledge/event-organizers (Tier 1)**; KB home (three audience sections: Event Organizers / Attendees & Speakers / Sponsors & Exhibitors): https://help.eventmobi.com/hc/en-us (Tier 1)
- Guidebook — product home + case studies: https://www.guidebook.com/ (Tier 2)
- Swapcard — product home: https://www.swapcard.com/ (Tier 2)
- Cvent — Attendee Hub product page + FAQ: https://www.cvent.com/en/event-marketing-management/attendee-hub (Tier 2)

Source-access limitations:

- Guidebook support portal (support.guidebook.com) timed out / transport-errored ×2 — abandoned per network rule; Guidebook evidence is Tier-2 product pages and case studies only.
- Whova, Swapcard, Cvent organizer-side help centers were not article-fetched this pass (not attempted beyond product pages after EventMobi's KB supplied the Tier-1 structural evidence; sibling passes 2026-09-07 also recorded these domains as blocked/JS-app).
- EventMobi's /en/event-apps/ URL 403'd once; the equivalent /event-apps/ page fetched successfully on retry.

Consequence: precise operational details (app-store review timelines, update-propagation speeds, offline sync mechanics, post-event access windows in days, pricing) are **not asserted** anywhere; article titles from EventMobi's KB index are used as structural evidence only where the title itself is unambiguous.

## Product Observations

### Whova (Tier 2 — product page + FAQ; evidence layer A for Whova-specific claims)

- Self-defines the category in its FAQ: "An event app, also known as a conference app, is a mobile application used before, during and after any event or conference to help both organizers stay organized and keep attendees engaged." [A]
- Attendees download the app free from App Store / Google Play, or use a free web-browser version. [A]
- Content/brochure layer: personal agenda, multi-track & session management, interactive maps, document sharing (slides/handouts), branding customization, offline accessibility ("Offline? no worries, it's always accessible"), instant updates. Marketing frames the app as replacing the printed program ("60% savings in printing costs" — vendor claim). [A]
- Engagement: announcements (push notification + email), live polling, mobile surveys & session feedback, community board (meet-ups, ice-breakers, discussions), social media integration, gamification (leaderboard, photo contests). [A]
- Sponsors/exhibitors: sponsor banner ads, lead capture by scanning in the app, digital booth profiles (brochure, videos, chat, giveaways/coupons), attendee passport contest, appointment scheduling, tier packages, ROI reporting. [A]
- Networking: SmartProfiles, business card scanning & exchange, 1:1 and group messaging, video calling, attendee matchmaking, meeting scheduler, speed networking. [A]
- Organizer side: separate organizer login portal; FAQ says organizers "manage check-ins, communicate to attendees efficiently, track sessions". [A]
- Adoption/marketing stats (100% adoption, comment/message counts) — vendor claims, not generalized. [A, vendor-claim]

### EventMobi (Tier 1 — knowledge base index + Tier 2 product pages; evidence layer A)

- Product page: "Easily create branded Mobile Event Management Apps"; app "easily accessible on any mobile browser or as a native app on iOS or Android"; syncs with registration, virtual space, onsite digital signage. [A]
- Attendee access by **event code**: the site's global header offers "At an event and looking for your event app? … enter your event code at eventmobi.com/<code>". [A]
- Organizer console named **Experience Manager** (experience.eventmobi.com); KB covers: Event App Settings, Building your Team, Managing Organizer Access and Permissions, Multi-Event organization ("How do I organize multiple events for various customers"), Session Conflict Management. [A]
- Content model visible in KB section titles: **People Library** (profiles for attendees/speakers/companies; custom fields; bulk Excel upload; self-edit invites to an attendee portal; profile-visibility control; external IDs), **Sessions** (create sessions for the agenda; personal schedules for attendees — attendee-starred or organizer-assigned custom schedules for groups; session access & capacity settings; video/live-stream states per session), **Sections** (create and manage app sections), **Maps** (linked to sessions/companies), **Documents**, **Video Library**. [A]
- Publication model (KB "Launch the Event App" section): app-store publication ("How And When Can I Access My Event In The App Stores?"), **Multi-Event App (MEA)** ("What Is A Multi-Event App (MEA) And What Does It Do?"; "Manage Your Events in Your Multi-Event App"), **branded/white-label native apps** submitted under the client's developer accounts ("Branded App Client Submission Requirements", "Resigning Branded App (Android/iOS)"), web app vs native app distinction ("How Does A Web App Differ From A Native App?"; "Will I Still Have The Web Version?"), live-while-building state ("Is my Event App live right now? Can people see it while I'm building it?"), update propagation ("What changes on the Event App cause an 'Update Now' notification?"; "How Soon Will My Changes And Updates Appear In The Event App?"), post-event access ("How Long Can I Continue To Access My Event App After My Event Ends?"), attendee login page configuration ("Creating Your Login Page"), SSO with identity providers, event-access instructions for attendees. [A]
- Registration integration: "Connecting your Extended Registration with your Event App", "Syncing QR Codes From Registration to the Event App", "Check-in Codes - Registration to Event App". [A]
- Engagement: live chat, anonymous Q&A, live polls & surveys, gamification, activity feed, group discussions; announcements with push + prescheduling. [A]
- Onsite: digital badges / QR touchless check-in; session attendance tracked by scanning badges at the door; BadgeON check-in app; Live Display (onsite screens driven from the same content). [A]
- Sponsors: Companies section, banner ads with placement control, lead capture enablement per company, appointment booking; "over fifteen different sponsor promo opportunities" (vendor claim). [A]
- Analytics: login rates, page views, messages/chats, video views; app usage over time. [A]
- Year-round: "turn your event app into an evergreen content platform / year-round community". [A]
- White label: "one of the few providers that offers a fully brandable white label app" with DIY drag-and-drop design (Homepage Designer). [A]
- KB is organized by **audience**: Event Organizers / Attendees & Speakers / Sponsors & Exhibitors — three distinct user populations with separate documentation. [A]

### Guidebook (Tier 2 — product home + case studies; evidence layer A for Guidebook-specific claims)

- Self-description (repeated across page footer of every article): "Guidebook is an event tech platform with native mobile event apps, registration, badges, and event websites. Built to keep attendees informed and engaged." [A]
- Current strategic focus is higher education (orientation, admissions/yield events, campus tours, homecoming, year-round department licenses "Unlimited events, year-round"); case studies also include associations/conferences (CIVSA replacing a 60-page printed book; UPCEA; DECA virtual) and non-event guides (ReadyKey EHS/compliance apps for companies). [A]
- Branded apps downloaded from the app stores; "No login required. Just the schedules, maps, and real-time updates they need." [A]
- Content: session-specific schedules and tracks, interactive campus maps, handbooks/directories, personalized schedules, built-in notes, real-time push notifications, photo/social feeds. [A]
- Value framing: "One app, one source of truth"; "Update anytime. Push instantly."; replaces printed materials (case studies quantify printing savings — vendor claims). [A]
- Builder at builder.guidebook.com (organizer login); Slate (CRM) integration: "Student records flow from Slate into the app. Engagement flows back." [A]
- Accessibility positioning (WCAG 2.1 AA, VPAT) — published support article exists but portal unreachable this pass. [A, title-only]

### Swapcard (Tier 2 — product home; evidence layer A for Swapcard-specific claims)

- Positions as "revenue-first event management platform"; the app is described as "AI-powered mobile & web app" delivering the program, networking, and exhibitor engagement. [A]
- Program builder: "unlimited session hierarchies", abstracts, child/sub-child sessions, speaker coordination — the app renders a complex multi-track program. [A]
- AI: "Sherlock AI transforms program complexity into personalized recommendations"; "one-tap peer chat and AI matchmaking to drive higher-quality exhibitor leads". [A]
- Same platform powers registration, onsite check-in/badge printing, access control "fully connected to live registration and attendance data". [A]
- Analytics across the attendee journey (registration/intent, engagement/behavior, exhibitor/sponsor performance, revenue). [A]
- Scale claims (4,000+ events, 7M+ attendees; adoption "70–80% vs 30–40% industry") — vendor claims, research notes only. [A, vendor-claim]

### Cvent Attendee Hub (Tier 2 — product page + FAQ; evidence layer A for Cvent-specific claims)

- Self-description: "an engagement platform (web + mobile) that connects attendees to your event's content, networking, and sponsors before, during, and after the event, across in-person, virtual, and hybrid formats." [A]
- "One home base for content, networking, and sponsors. It travels with them on any device, before the event starts and long after it ends." [A]
- Lifecycle framing is explicit: pre-event (personal agenda building, appointment scheduling, teaser videos, know-before-you-go, discussions, pre-event surveys), during (gamification, session engagement via polls/Q&A, push notifications and announcements for last-minute changes, activity feeds, sponsor activations, digital experience for remote attendees), post-event (feedback surveys, document downloads, 1:1 messaging, video on demand, discussion groups, analytics). [A]
- FAQ explicitly distinguishes: "A standard event app is typically a mobile agenda and info hub; Attendee Hub is a full engagement layer spanning web and mobile…" — i.e., the vendor itself names the narrower "standard event app" form inside the same category. [A]
- AI (CventIQ): session recommendations, daily summaries. [A]
- Cvent's suite separates sibling products: Event app (mobile-event-apps), Check-in & badging, Trade show lead capture (iCapture), Trade show meetings (Jifflenow), Virtual experience — the app is one product line among many. [A]

## Cross-product Comparison

| Dimension | Whova | EventMobi | Guidebook | Swapcard | Cvent Attendee Hub |
|---|---|---|---|---|---|
| Event-bound container | per-event app | single-event app **or** Multi-Event App container | per-guide app; branded container apps; year-round dept licenses | one app across an organizer's events | per-event hub in suite |
| Organizer-authored content | agenda, maps, docs, sponsors, announcements, community boards | sections: agenda/sessions, people, companies, maps, docs, video, info | schedule/tracks, maps, directories, handbooks, lists | program (hierarchies), speakers, exhibitors | agenda, content library, exhibitor profiles, discussions |
| Organizer console | organizer portal | Experience Manager | Builder | platform console | suite builder |
| Attendee access | app-store download (free) + web version | event code (web) / native app; configurable login page; SSO | app-store download; **no login required** | login; AI profiles | login via registration; web + native |
| Personal agenda | yes (star sessions) | yes (star; organizer-assigned group schedules) | yes | yes + AI recommendations | yes + appointment scheduling |
| People directory | attendees + SmartProfiles | People Library (attendees/speakers/companies) | directories | attendees/speakers/exhibitors | attendees, exhibitor profiles |
| Maps | interactive maps | interactive maps (multi-venue/floor), linked to sessions/companies | interactive maps (core feature) | (venue context) | (suite) |
| Push/announcements | push + email | push, alerts, prescheduled | push notifications | push | push + announcements |
| Networking | messaging, matchmaking, business cards, video calls, speed networking | public/private messaging, profiles, meeting requests | light (social feeds) | AI matchmaking, one-tap chat | AI-powered networking, 1:1 messaging, appointments |
| Session engagement | polls, surveys, session feedback | live chat, anonymous Q&A, polls, surveys | — | chat, engagement | chat, Q&A, polls, surveys |
| Gamification | leaderboard, photo contests, passport contest | challenges, leaderboard | — | — | challenges, leaderboards |
| Onsite extensions | check-in management, lead scan | digital badge/QR check-in, session-attendance scan, Live Display | badges (product line) | check-in, badge printing, access control | suite: separate check-in & badging product |
| Virtual/hybrid | streams, virtual sessions | session video states, Studio, Zoom/Webex embeds, video library | virtual hub (DECA case) | streams in sessions | live/simulive streaming, on-demand |
| Registration data intake | registration product / integrations | native registration sync; QR sync; check-in codes | Slate/CRM sync | native registration | native (suite) |
| Analytics | adoption/engagement stats | login rates, page views, messages, video views | engagement back to CRM | full journey analytics | engagement analytics |
| Post-event | content remains | defined post-event access; evergreen option | guides persist; year-round | content library | explicit post-event phase |
| Beyond events | community events | year-round community | **campus apps, tours, EHS guides** | — | — |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The event-bound app container.** An application instance published for a specific event occasion (or an organizer-defined set of events), created, configured, and published by the event's organizer; everything inside — content, people, interaction — is scoped to that event. Remove → a generic app builder or a generic community app (no event binding).
2. **Organizer-authored event content.** The organizer composes what the app presents: the event's program (sessions/agenda), its people (speakers, attendees, exhibitors/sponsors), its places (maps, venue info), and its information and announcements. Attendees consume and act on this published content; they do not author the app's structure. Remove → a social/UGC application.
3. **The attendee's pocket-companion use across the event cycle.** The primary user is the event's attendee, on their personal mobile device (the characteristic surface of the Type; web/desktop companions are standard co-deliveries), using the app as their companion to the event — find what is on and where, plan a personal schedule, receive the organizer's updates, participate — before, during, and after the event. Remove → organizer-side event management software (EMP) or a static event website/brochure.

Jointly-held is load-bearing:

- 1 alone = app-builder tooling (no event semantics)
- 2 alone = content management
- 3 without 1+2 = a generic social/chat app used at events
- 1+2 without 3 = an organizer-side publishing tool with no audience surface
- 2+3 without 1 = an event website (browser page, no app container)
- 1+3 without 2 = an empty shell with nothing to present

"Mobile" in the leaf name: the smartphone is the Type's characteristic and historically defining surface (the Type exists because of the smartphone; its pre-digital analog, the printed program, is a different artifact class). Every sampled product's primary named artifact is a mobile app (native or mobile web); every sampled product also ships a web companion. The defining structure is the event-bound attendee companion; the phone is where it lives.

### L1 — Common Mature Structure

Present in most modern products; not definitional:

- Personal agenda (bookmark/star sessions; organizer-assigned schedules for groups)
- Session detail pages (time, room, speakers, description, materials/live-stream link)
- People directory with profiles (attendees, speakers; visibility controls)
- Exhibitor/sponsor directory and profiles
- Interactive venue/campus maps
- Push notifications and announcements (incl. prescheduling)
- Document/content library (slides, handouts, video on demand)
- Attendee networking (messaging, profiles, meeting requests/appointments)
- Session engagement (live polls, Q&A, chat)
- Gamification (challenges, leaderboards, passports)
- Surveys and session feedback
- Organizer analytics (adoption/login rates, page views, engagement, sponsor metrics)
- Registration/attendee-data intake (login against registration records; QR/check-in codes; CRM sync)
- Onsite extensions (digital badge/QR check-in, session-attendance scanning)
- Virtual/hybrid delivery (session streams, on-demand video)

### L2 — Variant / Optional Structure

- **Publication model**: single-event app vs multi-event container app (one installed app holding many events) vs branded/white-label native app under the client's own developer accounts
- **Access model**: open/no-login guides vs registration-gated login vs SSO; profile visibility controls
- **Year-round posture**: evergreen content platform / year-round community continuing after the event
- **Builder breadth**: same builder used for non-event guides (campus apps, tours, EHS/compliance handbooks) — outside this Type's binding but same product
- **AI layer**: recommendations, matchmaking, summaries (product-specific implementations)
- **Companion surfaces**: onsite digital signage/live displays driven from app content
- **Exhibitor-side tools inside the app**: lead capture, appointment booking, ROI reporting
- **Multilingual apps; offline behavior; accessibility conformance** (product-specific depth)

### L3 — Vendor-specific (research notes only)

- Whova: SmartProfiles, Speed Networking, Community Board, MicroEvents; "100% adoption" marketing stat
- EventMobi: Experience Manager, BadgeON, Live Display, MobiAI, "People Credits" licensing, 15+ sponsor promo placements claim
- Guidebook: Slate Platinum partnership, higher-ed strategic pivot (2026), Indiana Tech yield claims
- Swapcard: Sherlock AI, "revenue-first" positioning, adoption-rate comparison claims
- Cvent: Attendee Hub / CventIQ naming; Attendee Hub vs "standard event app" self-distinction; iCapture/Jifflenow siblings

## Vendor-specific Findings

See L3 above. None promoted to the canonical model. Notably, Cvent's own FAQ names the "standard event app" as "a mobile agenda and info hub" — useful as a market-internal articulation of the Type's minimal form, cited as a vendor articulation rather than adopted as the definition.

## Boundary Findings

1. **vs Event Management Platform (EMP)** — RATIFIED keep-both from this side. EMP is the organizer-side lifecycle system of record (event record + registration surface + managed attendance lifecycle); the event app is the attendee-facing published companion surface. The EMP pass lists "event apps & engagement" as optional capability — correct as far as suite products go, but standalone app-first products (Whova, EventMobi, Guidebook) exist whose center is the attendee surface, and the app exists with no registration machinery at all (Guidebook's no-login guides). Removal tests: remove the attendee-facing published app → EMP survives (it is organizer-side); remove the organizer-side lifecycle → the event app survives (it consumes registration data via import/sync — EventMobi KB documents registration→app sync and check-in codes as an integration seam). Seam: who sits in front of the screen — organizer working records vs attendee consuming the published event.
2. **vs Event Agenda Management** — DISCHARGES the agenda pass's joint-review flag from this side. Agenda management is the program's system of record (sessions → agenda → published program); the event app *presents* the agenda as one content module among many (networking, maps, sponsors, engagement) and is one of the surfaces the agenda publishes to (the agenda pass itself lists "the schedule view inside an event app" as a publication surface). The app is not the program's system of record; program edits originate in the agenda/EMP side and propagate into the app. Keep both; speaker-management's side of that joint review remains open (not dischargeable here).
3. **vs Attendee Management** — keep both. Attendee management is the organizer-side roster + attendance lifecycle; the event app is attendee-facing and *consumes* the roster (login against registration/attendee records; QR/check-in codes synced from registration) and can feed engagement/session-attendance data back. The attendee pass's cross-check recommendation is discharged: the seam is operator-roster vs attendee-companion.
4. **vs Event Credential / Badge Management** — keep both. Badge management centers the credential artifact (design, issuance, access meaning); the event app may *carry* a digital badge/QR for touchless check-in (EventMobi digital badges) — a capability interlock, not the center.
5. **vs Event Lead Retrieval** — keep both. Lead retrieval is exhibitor-side show-floor capture; the event app can embed lead capture for exhibitors (Whova, EventMobi) as a capability, but the app's center is the attendee companion.
6. **vs Audience Response System** — keep both (consistent with the ARS pass). Live polls/Q&A inside the app are engagement capabilities; ARS centers the facilitator-run live session instrument with real-time aggregate display.
7. **vs Community Platform / Social Network** — the year-round drift (EventMobi "evergreen content platform / year-round community"; Cvent "build a community after the event"; Whova community boards) is a variant posture, not a Type change, **as long as the event container remains the organizing unit**. When the container becomes a standing community with no event binding, the product leaves this Type (community-platform territory). The "remove the event binding" test is exactly what Guidebook's non-event guides (campus, EHS) demonstrate on the builder side.
8. **vs Virtual Event Platform** — keep both. Virtual event platforms center the online venue/session delivery; the event app centers the attendee companion and treats streams as session attributes. Hybrid events blend them; several vendors ship both as separate product lines (EventMobi: Event Apps vs Virtual Event Platform; Cvent: Attendee Hub vs Virtual Experience). Straddle acknowledged.
9. **vs the event website** — both are attendee-facing published surfaces from the same content; the app is the installable/persistent pocket companion (push, personalization, offline, identity), the website the browser page. Not a directory question (no website leaf in §26); noted because vendors ship both from one content base.
10. **Capability-vs-Type packaging** — same pattern as sibling event leaves (credential/badge, lead retrieval, agenda): the Type is realized as standalone app-first products, as named modules of event suites (Cvent Attendee Hub, EventMobi Event Apps inside a suite), and as builder products whose scope transcends events (Guidebook). Type stands; packaging is variant.

## Historical / Market-Sample Check

- The Type is smartphone-era by origin (the "conference app" wave of the early 2010s replacing printed programs; Whova's own marketing anchors on replacing paper programs). There is no pre-smartphone form of this Type — the printed program is the predecessor *artifact*, not a form of the Type. The historical check therefore asks whether **early-generation event apps** fit the L0: single-event native apps with organizer-authored agenda/maps/info and push updates, no networking, no login — yes, all three L0 structures hold. The definition does not over-fit to modern networking/AI/community features (all L1/L2).
- Platform-native / regional check: events delivered via generic tools (PDF programs, event websites, social-media event pages) are not this Type — no app container, no organizer-configured app instance. The boundary holds.
- The "no login required" pole (Guidebook) confirms that identity-based personalization is not definitional; the attendee companion use is.

## Uncertainties

- Exact app-store publication timelines, update-propagation speeds, offline sync mechanics, and post-event access windows: article titles confirm these are managed dimensions (EventMobi KB), but article contents were not fetched; **no precise numbers asserted anywhere**.
- Whether attendee login is required: varies by product and per-event configuration (Guidebook no-login; EventMobi configurable login page + SSO; Whova login for networking features). Documented as variant, not resolved further.
- Adoption-rate figures (Swapcard, Whova, Guidebook case studies): vendor marketing claims; recorded here only, never generalized.
- The exact split of "engagement platform" vs "event app" inside Cvent's own naming (Attendee Hub vs mobile-event-apps product page): treated as one realization family for this Type; Cvent's self-distinction recorded as vendor articulation.
- Speaker-management leaf (unprocessed): the session/speaker data spine joint review remains open on that side.

## Final Synthesis

The Event Mobile App is the attendee-facing event companion application: an application instance published by the event's organizer for a specific event (or event set), filled with organizer-authored event content — program, people, places, information, announcements — and used by attendees on their personal mobile devices (web companions standard) as their pocket companion to the event before, during, and after it. Its defining core is the jointly-held triple: event-bound container + organizer-authored content + attendee companion use. Everything else the market associates with the category — personal agendas, networking, live polls/Q&A, gamification, maps, sponsor promotion, analytics, digital badges, streams — is standard or optional capability layered on that spine. The Type stands independently of Event Management Platform (organizer-side lifecycle), Event Agenda Management (program record), and Attendee Management (roster): those Types author and manage what the app publishes and consumes.
