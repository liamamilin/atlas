# Research Notes — Webinar Platform

## Research Goal

Understand the Webinar Platform as an Application Type: what the market product called "webinar software / webinar platform" actually is, what objects it holds, how a webinar runs end-to-end, and where its boundary sits against the sibling Types in §01.04 (Video Conferencing, Video Calling, Virtual Meeting Platform) and against live streaming, virtual events, and event registration.

This pass also owns three pre-hung joint-review flags from sibling passes (video-conferencing-application, virtual-meeting-platform, conference-calling-application), all pointing at the same seam: many-to-many conversation vs one-to-many broadcast with registration/audience management.

## Initial Boundary

Working hypothesis before research:

- A webinar platform runs **scheduled, one-to-many broadcast events** to an audience that signs up in advance.
- Nearest neighbors: Video Conferencing Application (equal participation), Social Live Streaming Platform (public drop-in broadcast), Virtual Event Platform (multi-session venue), Event Registration Platform (registration machinery), Online Course / LMS (structured curriculum).
- The likely seam vs video conferencing: participation model (equal vs asymmetric) + audience management (drop-in vs registered/tracked).

## Research Questions

1. What is the central object — the webinar event? What does its record carry?
2. Is registration definitional or common? What does the platform hold about each registrant/attendee?
3. What roles exist (organizer/host, co-organizer, moderator, panelist/presenter, attendee) and how asymmetric are they?
4. What happens in the live session — what can attendees do, what is host-controlled?
5. What is the full lifecycle (plan → promote → register → remind → live → follow-up)?
6. Which capabilities are universal vs variant: recording/replay, email automation, polls/Q&A/chat, analytics, CRM integration, branding, dial-in, breakouts, restreaming?
7. What delivery modes exist (live, simulive/pre-recorded-as-live, automated, on-demand, evergreen, paid)?
8. Where exactly is the seam vs video conferencing, live streaming, webcasts, and virtual events — per the vendors' own definitions?
9. Historical check: would older-generation webinar products (GoToWebinar/WebEx Event Center era) satisfy the same core?

## Representative Products

Selection logic: market coverage (suite leader, suite pillar, webinar-first independent, enterprise engagement pole, SMB/creator pole), different product philosophies, different customer tiers, documentation accessibility.

| Product | Position / philosophy | Customer tier | Evidence layer |
|---|---|---|---|
| Zoom Webinars | suite-embedded webinar line inside Zoom Workplace; meeting-adjacent (seam test from the meeting side) | enterprise + mid-market | A (product page + FAQ) |
| Zoho Webinar | suite pillar beside Zoho Meeting; own meeting-vs-webinar FAQ | SMB → mid-market | A (product page + FAQ) |
| Livestorm | browser-based webinar-first independent for marketing teams; EU | mid-market → enterprise | A (homepage + feature list + vendor guide) |
| ON24 | enterprise "intelligent engagement" pole — webinar as pipeline/analytics machine; now a Cvent company | enterprise (B2B marketing) | A (homepage + platform page) |
| WebinarJam | SMB/creator monetization pole — live + automated/evergreen webinar funnels | SMB / creators / coaches | A (homepage) |

Considered and rejected for sampling: GoTo Webinar (classic standalone; goto.com returned 403 and support site is a JS shell — abandoned after 2 attempts), Demio/BigMarker (overlaps the Livestorm/WebinarJam poles), Adobe Connect (training/classroom heritage; weaker doc access).

## Sources

All fetched 2026-09-09.

- Zoom — Webinars & Events product page + FAQ: https://explore.zoom.us/en/products/webinars/ (Tier 2; help center known JS-rendered per sibling pass)
- Zoho Webinar — product page + FAQ: https://www.zoho.com/webinar/ (Tier 2; help-center KB articles at help.zoho.com returned empty shells — JS-rendered)
- Livestorm — homepage + full feature list: https://livestorm.co ; vendor guide "What Is a Webinar & How Does It Work?": https://livestorm.co/resources/guides/what-is-a-webinar (Tier 2 + vendor educational guide)
- ON24 — homepage: https://www.on24.com/ ; platform page: https://www.on24.com/platform/ (Tier 2; /platform/capabilities/webinars/ returned 403)
- WebinarJam — homepage: https://www.webinarjam.com (Tier 2)
- Sibling-pass evidence reused: research/virtual-meeting-platform.md (Zoho meeting-vs-webinar FAQ quote; Livestorm product split), STATUS.md entries for video-conferencing-application and conference-calling-application (seam flags)

Sourcing limitations:

- GoTo Webinar (the classic standalone webinar product and the natural historical anchor) unreachable: goto.com 403, support.goto.com/webinar JS shell. Historical check is therefore argued structurally, consistent with how sibling passes treated legacy eras.
- Zoho help-center user-guide articles (create-a-webinar etc.) returned empty (JS-rendered); Zoho lifecycle evidence comes from the product page + FAQ only.
- ON24's webinar capability page 403'd; ON24 operational detail comes from homepage + platform page (both marketing-tier but structurally informative, including the "traditional webinars vs intelligent engagement" contrast).
- No Tier-1 help-center article was successfully fetched for any sampled product. All evidence is Tier-2 (official product pages, official vendor guides, official FAQs). Assertion strength calibrated accordingly: no precise numeric limits, no exact default settings, no exact state names in the final document beyond what vendor pages themselves state.

## Product A — Zoom Webinars (evidence layer A)

- Self-label: "Webinar Software: Host Professional Webinars & Events"; product line "Webinars & Events" under Zoom Business Services (inside Zoom Workplace suite).
- **Vendor's own definition (FAQ)**: "Webinar software is a digital platform that enables organizations to host one-to-many broadcast presentations, connecting presenters with large audiences through video, audio, and content sharing. Unlike regular video conferencing, webinar software is specifically designed for structured presentations where hosts control the experience and attendees primarily listen and engage through interactive tools like polls, Q&A, and chat."
- **Vendor's own meeting-vs-webinar seam (FAQ)**: "Zoom Meetings are designed for collaborative, two-way conversations where all participants can share video, audio, and screen content freely. Zoom Webinars are structured for one-to-many broadcasting, where hosts and panelists present to an audience that primarily listens and engages through controlled interactive features like polls and Q&A rather than open video/audio participation."
- Scale claims: "up to 100,000 attendees"; 9M+ webinars hosted annually, 692M+ attendees annually (marketing stats).
- Use cases: marketing webinars, product demos, training sessions, town halls, virtual events, educational seminars; internal comms (company-wide announcements) and external (lead gen, customer onboarding, thought leadership).
- Feature pillars: Event flexibility (one-time webinars, recurring series, multi-session conferences; "10 people or 100,000"); Event production (Production Studio: custom layouts, pre-loaded videos, scene switching; **Simulive** = pre-recorded content broadcast as live with real-time chat/polls/Q&A; private backstage for speakers/moderators; isolated audio/video recording for post-production; RTMP simulcast to YouTube/LinkedIn/Facebook); Audience engagement (branded registration pages, immersive event lobbies, emails, polls/Q&A/chat/reactions, breakout rooms, hybrid, AI captions 20+ languages); Content repurposing (branded video hubs, AI chapters/highlights, social clips, on-demand engagement tracking); Insights & integrations (content performance, most-engaged participants, interactive dashboards, CRM connection, pipeline influence).
- Plan ladder (L3): Webinars → Webinars Plus (adds modern platform, AI, on-demand video, pro production) → Events (multi-session virtual events with networking, ticket types, lobby, sponsors, hybrid).
- Customer quote (NBA): "control over moderating these virtual press conferences and interviews, and Zoom Webinars was perfect for that."

## Product B — Zoho Webinar (evidence layer A)

- Self-label: "webinar software", "webinar platform"; "secure online webinar software that helps you conduct your large-scale virtual conferences".
- **Vendor's own definition (FAQ)**: "Webinars are virtual group events that involve an organizer communicating and broadcasting to a set of attendees. The organizer can broadcast presentations and conduct interactive training sessions with the help of features like polls, Q&A sessions, etc. Attendees can sign up for the webinar, submit questions to the organizer, and interact with the polls."
- **Vendor's own meeting-vs-webinar seam** (from sibling pass, Zoho FAQ): "Meetings are typically collaborative events where the host and participants engage equally… Webinars are online group events where an organizer broadcasts presentations… to a selected group of attendees."
- Feature blocks: Interactive engagement (Q&A sessions, raise hand, audience polls, emoji reactions); Personalized branding (customizable registration links, social promotion, end-of-webinar display, livestream to social media); Advanced analytics (attendee list tracking, attendee reports, engagement analytics, CSV export); Lead generation (CRM push of attendees as leads, Marketing Automation nurture, monetization of virtual conferences).
- Moderator controls: "Choose what your audience can see during your webinar. From a shared screen or presentation slide, you decide what goes on the stage with you." Screen/app/monitor sharing. Recording to cloud, replay/share/download.
- Use cases: training, onboarding, live events, townhall. Scale claim: "Host 5000 attendees in a single webinar event". Download-free (browser) experience; iOS/Android apps.
- Security: DTLS-SRTP, TLS 1.2, registration moderation, advanced registration form preferences, TFA.
- Pricing tiers (L3): Standard (co-branding, recording, webinar series) / Professional (source tracking, live streaming, share material) / Enterprise (custom branding, email customizations, on-demand webinar). Integrations: Zapier, HubSpot, Zoho CRM, Zia, RevAI, Zoho Campaigns.

## Product C — Livestorm (evidence layer A)

- Self-label: "All-in-one Webinar Software for Marketing Teams"; "The webinar leader, designed in Europe". Products: Webinars (live), On-Demand Webinars, Automated Webinars, Virtual Events, Restreaming, AI.
- **Vendor's own definition (guide)**: "A webinar is a virtual presentation where hosts share information with attendees online. The word is short for 'web seminar.'"
- **Vendor's own three-way taxonomy (guide)**: online meeting (2–100, two-way, camera/mic/screen share, registration rarely) vs **webinar** (10–500+, one-to-many with structured interaction, chat/Q&A/polls, **registration required: Yes**, recording standard) vs webcast (1,000–10,000+, one-way, limited/no interaction, registration sometimes).
- **Vendor's own lifecycle (guide)**: planning/goal → promotion (email/social/ads → registration page) → registration (form: name, email, job title, company; "The webinar platform stores this information and uses it for communication before and after the event") → confirmation + reminder emails → live session (attendees join via browser/app; host presents via slides/screen share/demo; **"attendees don't turn on their cameras or microphones"**; interaction via live chat, Q&A with upvotes, polls; moderator manages audience interaction) → post-event follow-up (recording + slides to attendees, replay to no-shows; analytics: who attended, watch time, questions asked, poll responses → sales follow-up / nurture / next webinar).
- Delivery types (guide): live, evergreen, on-demand (register → immediate recording access), automated (pre-recorded on a set schedule simulating live, optionally with live chat + moderator), paid (ticket/subscription).
- Formats (guide): solo presentation, panel, roundtable, seminar, interview, workshop.
- Feature inventory (homepage): registration pages, custom registration, email cadences, custom branding, one-click invite, embeddable registration widget, company page, moderators, analytics, UTM tracking, contact profiles, attendance rate, questions/chat export, CRM integrations, replay analytics, on-demand events, event automation, multi-session events, team accounts, SAML SSO, browser-based, polls, chat, Q&A with upvotes + live answer banner, people tab, speaking permissions, dial-in by phone, instant replays, emoji reactions, contacts record, breakout rooms, public/private events, recording control, transcription, live-to-on-demand conversion, restreaming, Full HD, AI transcripts, raise hand, whiteboards, PowerPoint embedding, Plugin SDK, API.
- Use cases: product demos, customer training, marketing events/lead gen, staff enablement, internal communication, hiring events. Teams: marketing, sales, CS, HR.
- Benchmark stats (L3, vendor's own report): 49.6% of registrations come in the final week; average watch 26 minutes; public replays get more views than gated; 86.3% of marketers use email for promotion.

## Product D — ON24 (evidence layer A)

- Self-label: "AI Webinar & Engagement Platform"; "ON24 Intelligent Engagement Platform"; now a Cvent company ("ON24® is a trademark of ON24, Inc., a Cvent® company").
- Positioning: "Transform webinars, virtual events, and content into AI-powered experiences that propel first-party customer engagement and revenue."
- Capabilities: Webinars ("Create engaging, data-rich online events with the ON24 webinar platform, driving audience interaction and actionable insights"), Virtual Events, Landing Pages, Content Hubs ("resource centers that engage audiences with on-demand webinars and multimedia assets"), Performance Analytics, Translate, AI ACE (Analytics and Content Engine).
- **Vendor's own "traditional webinars vs intelligent engagement" contrast** (platform page) — the "traditional" column is a useful mirror of the Type's baseline: manual steps; generic one-size-fits-all experience; "passive attendance with one-way, static presentations"; one-off events never repurposed; superficial data; **"Downloaded list of registrant names on a spreadsheet"**. The "intelligent" column: templatized workflows; personalized messaging/CTAs; "Engaging experiences with 20+ ways to participate"; AI-generated content from events; "Analytics at the attendee, event and channel level"; real-time integrations.
- How it works (platform page): Personalize (custom-branded interactive webinar/hub/landing-page/virtual-event experiences, segment-personalized content) → Enrich insights (engagement profile at **prospect and account level**, heatmap "Key Moments", buying signals) → Improve efficiency (AI transcripts/ebooks/blogs, video clip highlights by engagement, publish to hubs) → Increase channel performance (first-party engagement data → Marketo/Salesforce/HubSpot; lead scoring and qualification, sales alerts, account prioritization).
- Industries: financial services, life sciences, insurance, technology, associations, manufacturing, professional services. Use cases: demand generation, HCP engagement, product marketing, customer marketing, partner enablement, professional certification, member enrollment.
- LinkedIn integration: build LinkedIn audience lists from ON24 first-party engagement data.

## Product E — WebinarJam (evidence layer A)

- Self-label: "The most powerful live and automated webinar software for selling online"; "The #1 webinar platform that turns your audience into customers". Audience: "coaches, experts, and creators"; 75,000 businesses across 40 industries (marketing stats).
- Three pillars: Engagement & Presentation (live webinar tools); Automation & Flexibility (automated scheduling/replays); Marketing & Monetization (built-in marketing tools).
- **"From live to evergreen sales"**: "Host powerful live webinars that convert in real time, then let them keep selling on autopilot… automated replays, timed offers, and follow-ups that keep revenue flowing long after you've gone off air."
- Use cases: host virtual events (multi-speaker), live product demos, sell courses online. Join model: "Attendees join instantly from their browser or device"; host without downloads.
- Integrations: ActiveCampaign (contacts & email automation), Zapier (5,000+ apps).
- Stats (L3): 1.1M webinars, 200M+ live attendees, 53M replays watched.

## Cross-product Comparison

| Structure | Zoom Webinars | Zoho Webinar | Livestorm | ON24 | WebinarJam |
|---|---|---|---|---|---|
| Webinar event as unit of record (scheduled session created ahead of time, with its own registration/join surface) | ✔ (one-time, recurring series, multi-session) | ✔ (registration links, webinar series) | ✔ (event created → registration page auto-generated) | ✔ (webinar experiences; series/programs) | ✔ (webinars listed/created ahead) |
| Registration / managed audience (registrant + attendee records, confirmations/reminders) | ✔ (branded registration pages, event lobbies, emails) | ✔ (registration links, registration moderation, attendee list tracking) | ✔ (registration pages, email cadences, contact profiles, attendance rate) | ✔ (registrant records; "downloaded list of registrant names" named as the legacy baseline) | ✔ (registration implied by "everyone who registers"; ActiveCampaign contact sync) |
| One-to-many broadcast, asymmetric roles (presenters vs audience that "primarily listens") | ✔ (vendor FAQ: hosts/panelists present, audience primarily listens) | ✔ (vendor FAQ: organizer broadcasts to attendees; moderator controls what goes "on the stage") | ✔ (vendor guide: attendees don't turn on cameras/mics) | ✔ ("passive attendance with one-way, static presentations" named as the baseline to improve) | ✔ (host presents to thousands) |
| Moderated interaction channels (Q&A, chat, polls) | ✔ (polls, Q&A, chat, reactions) | ✔ (Q&A, polls, raise hand, emoji reactions) | ✔ (chat, Q&A + upvotes, polls, surveys, reactions) | ✔ ("20+ ways to participate") | ✔ (engagement tools pillar) |
| Recording + replay / on-demand | ✔ (recordings, AI chapters, video hubs) | ✔ (cloud recording, replay/share) | ✔ (auto recording, replays, live-to-on-demand conversion) | ✔ (content hubs of on-demand webinars) | ✔ (automated replays; 53M replays watched) |
| Email automation around the event | ✔ (event emails) | ✔ (email customizations; promotion) | ✔ (email cadences: confirmation, reminders, follow-up) | ✔ (always-on nurtures) | ✔ (follow-ups; ActiveCampaign) |
| Attendee/engagement analytics | ✔ (dashboards, most-engaged participants) | ✔ (attendee reports, engagement analytics, CSV export) | ✔ (analytics dashboard, watch duration, poll responses, exports) | ✔ (attendee/event/channel-level analytics, heatmaps, account-level profiles) | ✔ (on-screen analytics claim; lighter) |
| CRM / marketing automation integration | ✔ (CRM connection, pipeline influence) | ✔ (Zoho CRM lead push, Marketing Automation) | ✔ (HubSpot/Salesforce/Marketo/Pardot, Zapier) | ✔ (Marketo/Salesforce/HubSpot native; LinkedIn audiences) | ✔ (ActiveCampaign, Zapier) |
| Branding/customization | ✔ (custom branding, backgrounds) | ✔ (co-branding → custom branding by tier) | ✔ (custom room design, asset branding) | ✔ (custom-branded experiences) | ✔ (marketing tools) |
| Delivery-mode variants beyond live | ✔ (Simulive; on-demand video) | ✔ (on-demand webinar tier) | ✔ (on-demand, automated, evergreen) | ✔ (on-demand hubs, always-on) | ✔ (automated/evergreen as a headline pillar) |
| Restreaming to social platforms | ✔ (RTMP to YouTube/LinkedIn/Facebook) | ✔ (livestream on social media) | ✔ (Restreaming product) | not observed | not observed |
| Phone dial-in | not observed on page | not observed on page | ✔ (dial-in by phone) | not observed | not observed |
| Breakout rooms | ✔ | not observed | ✔ | not observed | not observed |
| Multi-session / virtual events adjacency | ✔ (Events plan: stages, lobby, tickets, networking) | ✔ (virtual conference use case) | ✔ (Virtual Events product; multi-session events) | ✔ (Virtual Events capability) | ✔ (host virtual events use case) |
| Monetization | ✔ (ticket types in Events plan) | ✔ (monetize virtual conferences) | ✔ (paid webinars documented in guide) | not observed | ✔ (timed offers, evergreen sales) |
| Suite-embedded vs standalone | suite pillar (Zoom Workplace) | suite pillar (Zoho suite) | standalone | standalone (Cvent family) | standalone |

Reading of the table: every sampled product realizes the same three-part core — (1) the webinar event as a created-ahead-of-time unit of record with its own registration/join surface, (2) a managed audience held as registrant/attendee records with attendance tracked, (3) a one-to-many broadcast with asymmetric roles and host-controlled interaction channels. Everything else varies by pole and tier.

## Abstraction Levels

### L0 — Defining Invariant

Three jointly-held structures:

1. **The webinar event as the unit of record** — a planned broadcast session created ahead of time in the platform, carrying its own public face (registration/landing page or join link), scheduled time, and presenters; the object the platform lists, promotes, runs, and reports on. Remove → an ad-hoc meeting or a bare stream with no event record.
2. **The managed audience** — the audience is held as a tracked population: people sign up in advance (registration the dominant mechanism), receive confirmations/reminders, and are recorded as registrants and attendees with attendance (and commonly engagement) data per person. Remove → a public drop-in stream or an open room; the audience becomes anonymous and unmanaged.
3. **The one-to-many broadcast with asymmetric roles** — presenters/panelists produce the audio, video, and content; attendees watch and listen by default, interacting only through host-controlled channels (Q&A, chat, polls, raise hand). Remove → equal-participation video conferencing.

Jointly-held load-bearing tests:

- 1 alone = a scheduled calendar event / a landing page.
- 2 without 1 = a mailing list / a registration form.
- 3 without 1+2 = an ad-hoc broadcast.
- 1+2 without 3 = registration machinery with no broadcast (event-registration territory).
- 1+3 without 2 = a public webcast/livestream with no audience management.
- 2+3 without 1 = a drop-in broadcast room with no event record.

### L1 — Common Mature Structure

- Registration pages / landing pages with custom form fields and branding.
- Email automation: confirmation, reminders, follow-up (the dominant promotion channel per Livestorm's own data).
- Moderated interaction: Q&A (commonly with upvotes), chat, polls, post-event surveys, reactions, raise hand.
- Screen/content sharing, slides, media playback; moderator controls over what is "on stage".
- Recording + replay; live-to-on-demand conversion.
- Attendee and engagement reports with export.
- Role set: organizer/host, co-organizer/moderator, panelist/presenter, attendee; practice/rehearsal and backstage coordination in mature products.
- Calendar integration; browser and/or app join for attendees.
- CRM / marketing automation integrations feeding registrant + engagement data downstream.
- Branding/customization of pages, emails, and rooms.

### L2 — Variant / Optional Structure

- Delivery mode: live / simulive (pre-recorded broadcast as live with live interaction) / automated (scheduled simulated-live) / on-demand (register-to-watch recording) / evergreen; paid webinars.
- Purpose poles: marketing/lead-gen (ON24, Livestorm, WebinarJam), internal comms/town halls (Zoom, Zoho, Livestorm), training/certification (Zoom, ON24), customer onboarding.
- Scale: capacity numbers plan-dependent and vendor-specific (claims range from thousands to six figures).
- Multi-session series/recurring webinars; webinar programs.
- Restreaming/simulcast to social platforms; phone dial-in; breakout rooms; live interpretation/translation.
- Monetization: tickets, paid webinars, timed offers.
- Virtual events / multi-session venues as an adjacent product line or plan tier.
- AI: transcription, captions, summaries, content repurposing (era-current).
- Enterprise governance: SSO, workspaces, hosting region, compliance certifications.

### L3 — Vendor-specific (research notes only)

- Zoom: Webinars / Webinars Plus / Events plan ladder; Simulive; Production Studio; backstage; isolated-track recording; eCDN/Zoom Mesh; "up to 100,000 attendees"; 9M+ webinars/692M+ attendees marketing stats; NBA press-conference quote.
- Zoho: "5000 attendees" claim; source tracking; raise hand; emoji reactions; Zoho CRM/Marketing Automation lead push; Standard/Professional/Enterprise tier split; DTLS-SRTP/TLS 1.2; storage counted by recordings not size; Zia/RevAI integrations.
- Livestorm: up to 3,000 attendees; EU-hosted; Plugin SDK/API; Interprefy live interpretation; video engagement score; benchmark-report figures (49.6% final-week registrations; 26-min average watch; 86.3% email promotion; public-vs-gated replay views); "webinar leader, designed in Europe".
- ON24: ACE (AI Analytics and Content Engine); engagement heatmap "Key Moments"; "20+ ways to participate"; prospect/account-level engagement profiles; Marketo/Salesforce/HubSpot native integrations; LinkedIn audience integration; Cvent ownership; "traditional webinars vs intelligent engagement" contrast framing.
- WebinarJam: evergreen sales-engine framing; timed offers; ActiveCampaign integration; Genesis Digital LLC; 1.1M webinars / 200M+ live attendees / 53M replays stats.

## Vendor-specific Findings

See L3. None of these enters the canonical core. Notably: capacity numbers, plan ladders, engagement-score formulas, and benchmark statistics are all vendor-specific marketing/plan facts.

## Rejected Findings

- **"Webinar Platform = Video Conferencing with a bigger room"** — REJECTED on the vendors' own definitions. Zoom: "Unlike regular video conferencing, webinar software is specifically designed for structured presentations where hosts control the experience and attendees primarily listen." Zoho: meetings = equal engagement, webinars = broadcast to attendees. Livestorm's table separates meeting (two-way) from webinar (one-to-many with structured interaction). The seam is participation model + audience management, not room size.
- **"Registration is the defining invariant itself"** — REJECTED as too implementation-specific. The invariant is the *managed, tracked audience*; registration is its dominant mechanism (present in all five sampled products; Livestorm's own table marks registration "Yes" for webinars vs "Rarely" for meetings). Phrasing the core as "managed audience (typically via registration)" keeps the definition from over-fitting to one mechanism. (Whether some products also allow join-link-only webinars without registration was not verified in fetched sources and is not asserted.)
- **"Webinar Platform = Virtual Event Platform"** — REJECTED: the market keeps them apart. Zoom sells Webinars and Events as separate plans ("Everything in Webinars Plus, including multi-session virtual events"); Livestorm sells Webinars and Virtual Events as separate products; ON24 lists Virtual Events as a separate capability. The webinar is a single broadcast session; the virtual event is a multi-session venue (lobbies, expo, networking, tickets).
- **"Webinar Platform = live streaming platform"** — REJECTED: the webinar audience is a managed, registration-assembled, tracked population; the livestream audience is a public drop-in crowd. Restreaming a webinar to social platforms is an outbound capability, not a change of Type.
- **"Engagement analytics/lead scoring is definitional"** — REJECTED: depth of analytics is a variant axis (basic attendance reports at the SMB pole vs account-level engagement profiles at the ON24 pole). The invariant inside the core is only that the audience is held and tracked as records.

## Boundary Findings

1. **vs Video Conferencing Application (§01.04, processed 2026-09-09) — JOINT REVIEW DISCHARGED, keep-both RATIFIED.** The seam proposed by the video-conferencing pass ("many-to-many conversation vs one-to-many broadcast with registration/audience management") is confirmed by all three vendors' own definitions gathered independently in this pass (Zoom FAQ, Zoho FAQ, Livestorm guide/table). Removal tests: remove the broadcast role asymmetry and the managed audience → video conferencing; add equal participation → meeting. The market itself keeps the two apart as separate products/modes (Zoom Meetings vs Zoom Webinars; Zoho Meeting vs Zoho Webinar; Livestorm webinar product with a meetings mode). Large-meeting/view-only modes and webinar product lines sit on the seam and are packaged by vendors as separate modes/products — consistent with the video-conferencing pass's observation. Both Types stand; no directory change.
2. **vs Conference Calling Application (§01.03, processed 2026-09-07)** — that pass recorded "webinar is one-to-many broadcast with audience management; conference calling is many-to-many conversation". Confirmed; no conflict. Dial-in audio appears here only as a plan-gated capability (observed at Livestorm), symmetric to the sibling passes' treatment.
3. **vs Virtual Meeting Platform (§01.04, processed 2026-09-09, alias of Video Conferencing Application)** — the alias pass confirmed the same seam and left ownership to this pass; discharged by finding #1. Zoho's own meeting-vs-webinar FAQ (quoted in that pass and re-confirmed on Zoho Webinar's page) is the decisive vendor-drawn line.
4. **vs Social Live Streaming Platform (§01.08, processed)** — distribution model seam: webinar audience is private/controlled, assembled by registration, tracked per person; livestream audience is public, discovered through a platform/creator graph, untracked. Interaction differs accordingly (structured moderated Q&A/polls vs live comments). Restreaming to social platforms is a capability, not a boundary crossing.
5. **vs Video Streaming Platform (§27)** — the streaming platform's center is an on-demand/live content catalog for consumption; the webinar platform's center is the live scheduled event plus its audience operation. On-demand replays and content hubs (ON24) are webinar-platform capabilities that drift toward the streaming/content-hub territory without changing the Type.
6. **vs Virtual Event Platform (§26 territory, unprocessed leaves)** — single broadcast session vs multi-session venue (lobby, expo booths, networking, ticket types, agendas). Vendors sell them as separate products/plans (Zoom Events; Livestorm Virtual Events; ON24 Virtual Events). Flag for the §26 virtual-event pass: the webinar is the session-level Type; the virtual event is the venue-level Type; products bundle both.
7. **vs Event Registration Platform (§26)** — shared registration machinery; different centers. In the webinar platform, registration exists to assemble and manage the audience of the broadcast; in event registration, the registration/attendance operation is itself the system of record for physical/multi-format events. If the broadcast session is removed and only registration + attendance remain, the product is event-registration territory.
8. **vs Audience Response System (§26, processed 2026-09-06)** — consistent with that pass's own finding: native polls/Q&A inside webinar platforms are capabilities of this Type, not standalone ARS instances. The ARS center is the facilitator-run mass-response loop; the webinar center is the broadcast.
9. **vs Online Course / LMS (§23)** — webinars serve training use cases, but the platform holds events and audiences, not curricula, learner progress structures, or grades. Training/certification packaging (Zoom's certificate issuance on training sessions; ON24 professional certification) is a variant overlay.
10. **vs Webcast (no directory leaf; Livestorm's own three-way taxonomy)** — webcast = one-way broadcast, minimal/no interaction, registration sometimes; webinar = structured interaction + managed audience. The webcast population sits between this Type and Video Streaming; no directory conflict.
11. **去掉什么就变成另一个 Type:** remove the asymmetric roles (attendees get audio/video) → video conferencing; remove the managed audience (public drop-in) → social live streaming / webcast; remove the event record (ad-hoc session) → large meeting / stream; remove the live broadcast (keep registration + content) → event registration / content hub; add multi-session venue machinery → virtual event platform; add curriculum + learner records → LMS.

## Historical / Market-Sample Check

- The three-part core is era-robust on structural grounds: the classic standalone webinar generation (GoToWebinar-class, WebEx Event-class, 2000s–2010s) is defined in market memory by exactly registration pages, reminder emails, panelist/attendee role separation, live broadcast with Q&A/polls, attendee reports, and recordings — all three legs present. **Direct primary sources for this generation were not fetchable in this pass** (GoTo 403; WebEx not sampled) — the check is argued structurally, consistent with how sibling passes treated legacy eras; recorded as a sourcing limitation.
- The "web seminar" etymology (documented in Livestorm's own guide) anchors the Type in the seminar/broadcast lineage rather than the meeting lineage — the asymmetry is original to the Type, not a modern add-on.
- Regional products were not sampled; no evidence was found suggesting a regional webinar family with a different core. The definition does not depend on any single era's vocabulary (webinar / web seminar / online event).
- Automated/evergreen/paid webinars and AI repurposing are era-current variants layered on the same event record; they do not change the core.

## Uncertainties

- Whether some products allow fully registration-less webinars (join-link-only distribution) — not verified in fetched sources; the final document phrases the audience leg as "managed audience, typically assembled through registration" and does not assert the registration-optional case.
- Exact capacity ceilings, duration limits, and plan gating — vendor-specific and plan-dependent; deliberately excluded from the final document.
- Zoho's lifecycle detail (create/schedule steps) — help-center articles JS-rendered; lifecycle evidence for Zoho rests on the product page + FAQ.
- ON24's in-session mechanics (its webinar room's interaction set beyond "20+ ways to participate") — capability page 403; not asserted.
- GoTo/WebEx heritage — argued structurally only.

## Final Synthesis

The Webinar Platform is the broadcast-event counterpart of the video-conferencing Type. Its world is organized around **the webinar event** — a planned, promoted, scheduled broadcast session that the platform holds as a record from creation to follow-up. Around the event sit two structures that make it a webinar rather than a meeting or a stream: **a managed audience** (people who sign up, get reminded, attend, and are recorded as registrants/attendees with per-person attendance and engagement data) and **a one-to-many broadcast with asymmetric roles** (presenters produce; the audience watches by default and interacts only through host-controlled channels). The platform's job is to run the full loop around that event: create it, publish its registration surface, promote it, remind its audience, stage the live broadcast with moderated interaction, record it, and report on who attended and how they engaged — with recording/replay, email automation, analytics, branding, and CRM integration as the standard capability set, and delivery-mode variants (simulive, automated, on-demand, paid) reusing the same event record. The vendors' own definitions (Zoom, Zoho, Livestorm) independently draw the same seam against meetings: equal participation vs broadcast to a managed audience.
