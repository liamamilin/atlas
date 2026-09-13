# Research Notes — Virtual Meeting Platform

Research date: **2026-09-09**
Leaf: Virtual Meeting Platform (DIRECTORY §01.04 Video Communication & Meetings)
Slug: `virtual-meeting-platform`

Cross-references (joint-review obligations inherited from prior passes):

- research/video-conferencing-application.md §Boundary Findings — flag #2: decide alias vs container-umbrella vs spatial-venue variant for this leaf.
- research/conference-calling-application.md §Boundary Findings — "the meeting platform is the container (scheduling, workspace, content); conference calling is the audio-session capability."
- research/ai-meeting-assistant.md §Boundary Issues — platform-native assistants blur the boundary; joint review at this pass.

## Research Goal

Determine what the market actually sells under the phrase "virtual meeting platform", and decide whether the directory leaf is:

1. an **alias** of Video Conferencing Application (one market family, two names),
2. a **container-level umbrella** (the platform that holds meetings + scheduling + workspace + content + admin, above the meeting-centric Type),
3. a **spatial-venue variant** (persistent virtual spaces/venues where meetings happen — Gather/Kumospace-office/Remo/Hopin family),
4. or a genuinely distinct Type with its own core.

## Initial Boundary

Hypothesis before research: "virtual meeting" is the market's modern phrase for the ordinary online meeting (the convened addressable meeting family already documented as Video Conferencing Application); "platform" is packaging language (standalone product or vendor suite), not a structure. The main risk to this hypothesis: a distinct venue/spatial product family that self-labels "virtual meeting platform".

Nearest neighbors: Video Conferencing Application (§01.04, processed 2026-09-09), Video Calling Application (§01.04, unprocessed), Webinar Platform (§01.04, unprocessed), Conference Calling Application (§01.03, processed 2026-09-07), Virtual Office Workspace (§03.12, unprocessed), Virtual Classroom (§23, unprocessed), Team Messaging Application (processed), Meeting Scheduling Application (processed), Meeting Recording & Transcription Application (processed), AI Meeting Assistant (processed).

## Research Questions

1. Which products self-label "virtual meeting platform", and what do they actually sell?
2. Is there a product population answering to "virtual meeting platform" that lacks the convened-meeting structure (convened addressable meeting + live audiovisual + multi-party)?
3. Does the "platform" word carry a distinct structure (container: scheduling + workspace + content + admin) beyond the meeting-centric Type?
4. Do the spatial-venue products (virtual office / virtual events) claim the phrase "virtual meeting platform"?
5. Where does the embeddable-API family (video SDK/embed) sit?
6. Does the reading survive the historical/era check (pre-cloud "online meeting" / "web meeting" vocabulary)?

## Representative Products

Selection logic: products that use the phrase or its immediate variants for their meeting products, spanning market position (leader / suite vendor / challenger), product philosophy (app-first / browser-native / embed-first / venue-adjacent / webinar-hybrid), and customer tier (consumer→enterprise).

| Product | Why sampled | Tier / philosophy | Evidence level |
|---|---|---|---|
| Zoom (Zoom Meetings) | market leader; its own URL slug for the Meetings product is "virtual-meetings" | consumer→enterprise; suite platform (Zoom Workplace) | Tier-2 product page (help center JS-rendered per sibling pass) |
| Zoho Meeting | suite vendor's standalone meeting product; maintains a dedicated "virtual meeting" page defining the term | SMB; browser-based, security-first | Tier-2 product pages (2 fetched; help-center article returned empty) |
| Whereby (Whereby Meetings) | browser-native, embed-first challenger; permanent room links | individuals/teams + platform builders (Embedded) | Tier-2 product pages (2 fetched) + support-center structure |
| Kumospace | venue-adjacent suite that also sells ordinary "online meetings" — the boundary test for the spatial-venue reading | SMB remote/hybrid teams; spatial venue | Tier-2 product page |
| Livestorm | webinar-first product with a meetings mode — the webinar-seam test | marketing teams; browser-based | Tier-2 product page |

Venue-family check (to test reading #3): Airmeet (self-label check). Attempted, failed: GoTo Meeting (HTTP 403 ×1 — abandoned per network rule; not used).

## Sources

All fetched 2026-09-09:

- Zoom — Virtual Meetings product page (Zoom Meetings): https://www.zoom.com/en/products/virtual-meetings/ (also served at explore.zoom.us/en/products/meetings/ per sibling pass)
- Zoho Meeting — product homepage: https://www.zoho.com/meeting/
- Zoho Meeting — "Virtual Meeting: What it is, Types & Best Practices": https://www.zoho.com/meeting/virtual-meeting.html
- Whereby — homepage: https://whereby.com/
- Whereby — Meetings product page: https://whereby.com/information/meetings
- Whereby — Support Center (category structure): https://whereby.frontkb.com/en
- Kumospace — homepage: https://www.kumospace.com/
- Livestorm — homepage: https://www.livestorm.co/
- Airmeet — homepage (venue-family self-label check): https://www.airmeet.com/

Sourcing limitations:

- GoTo Meeting homepage returned HTTP 403 (1 attempt) — abandoned; no GoTo claims made.
- Zoom help center is JS-rendered (known from the sibling pass) — Zoom evidence is product-page level only; no Zoom operational defaults asserted.
- Zoho help-center moderator-controls article returned empty content — Zoho operational detail comes from its product pages (which are detailed).
- Whereby support-center article bodies not fetched (category listing only).
- Legacy-era ("web meeting" / early "online meeting") pages not fetchable — the historical check is argued structurally plus via Zoho's own era-bridging vocabulary.

## Product Observations

### Zoom (Zoom Meetings) — evidence layer A (product page)

- **The phrase is Zoom's own URL slug**: the Meetings product lives at `/en/products/virtual-meetings/`; the nav item "Meetings" points there. Page H1: "Zoom Meetings: Conference call service for virtual collaboration — Connect, collaborate, and get more done together with trusted video meetings." Section heading: "Video conferencing built for modern work."
- Feature inventory on the page: HD audio and video meetings; built-in collaboration tools (whiteboards, documents, notes); Zoom AI and My Notes (AI summaries, next steps, queries); caption translations; streamlined scheduling and join (calendar integration); continuous meeting chat (channels before/during/after meetings).
- Suite context: "Zoom Workplace" — Communication (Meetings, Chat, Phone, Mail & Calendar, Scheduler), Productivity (Canvas, Whiteboard, Clips, Hub), Spaces (Rooms, Workspace Reservation, Digital Signage, Visitor Management), Employee Engagement (Workvivo); Business Services (Revenue Accelerator, Webinars & Events, Bonsai, BrightHire); Zoom CX; Zoom AI (ZoomMate, My Notes, Virtual Agent, AI Services); Developers (Video SDK, Meeting SDK, APIs, Marketplace).
- Rooms: "transforming any space into a meeting environment through Zoom Rooms… device switching between desktop, mobile, and room systems."
- Plan-gated numbers (vendor-specific, L3): Basic free 40 min/100 participants; Pro 30 hours/100; Business 300 participants.
- Zoom uses "virtual meeting" language itself: "Virtual meeting tools and integrations — easily schedule and join virtual meetings from your existing email or calendar application."

### Zoho Meeting — evidence layer A (two product pages)

- Self-labels: "Online Meeting Software & Platform", "a secure online meeting platform", "virtual meeting software" (linked to its own `/meeting/virtual-meeting.html` page), "virtual meeting platform".
- Definition (dedicated page): "A virtual meeting is a type of online communication where people from anywhere in the world can connect, collaborate, and share their ideas using audio conferencing, video conferencing, and screen sharing. Use Zoho Meeting's secure virtual meeting platform to meet virtually…"
- FAQ: "Virtual meetings are online conferences where teams can connect and collaborate with each other via online meetings in a virtual environment. Also known as virtual conferencing…"
- **Types of virtual meetings** (Zoho's own taxonomy): audio conferencing / video conferencing / web conferencing / screen sharing. "Web conferencing is a broad term that comprises various types of virtual meetings over the web."
- **Meeting vs webinar** (Zoho's own seam): "Meetings are typically collaborative events where the host and participants engage equally… Webinars are online group events where an organizer broadcasts presentations… to a selected group of attendees."
- Documented workflow (schedule): log in → Schedule → title/date/time/duration → timezone (auto-populated) → host role assignable to other org members → participants by email + agenda → More Options (recurring, co-hosts, associate meeting rooms, upload session files) → Schedule.
- Documented capabilities: multi-video feed grid; host/moderator controls (switch roles, manage participant entry/exit, mute/unmute participants); lock meeting; entry/exit notifications; record/replay/share/download recordings from cloud storage; recurring meetings; multi-device (desktop/web/iOS/Android); collaborative whiteboard; "virtual meeting rooms" (standing rooms with a rooms controller for hands-free team sessions); virtual backgrounds; org administration (add/edit/remove users, define camera settings for all users, custom domain, co-branding of invitations); integrations (Gmail, Outlook, Projects, CRM, Slack, Teams); departments ("manage multiple teams as different departments… assign specific roles, schedule department-only meetings"); AI auto-generated transcriptions and session keynotes.
- Join model: "If you're a participant joining a meeting, you don't need to have a Zoho Meeting account. You can join either by using the meeting link or by entering the meeting key and password." Hosts need an account.
- Security posture: TLS 1.2, DTLS-SRTP, 256-bit AES; lock meetings; moderator controls.
- Separate pillar: "Calls" (business phone numbers + SMS; US/EU data centers only) — a distinct product line inside the same page, not the meeting.
- Plan-gated numbers (L3): Free 60 min/100 participants; paid adds co-hosts, international dial-in, recording & storage; video-conferencing page claims up to 250 participants / 50 video feeds.

### Whereby (Whereby Meetings) — evidence layer A (two product pages + support structure)

- Positioning: "Secure video calls. Zero hassle"; "video conferencing API and SDK" for the Embedded product; Meetings product: "Instant video calls in your browser… No downloads and no login for guests required. Just instant, memorable meeting rooms."
- **Room model**: permanent room links are the unit — plan tiers are expressed in room URLs (Free: 1 room URL; Pro: 3; Business: unlimited + "Shared and Flex rooms" + custom subdomain); rooms are customizable (URL, colors, logos).
- Features: chat (messages, reactions, files), screen sharing, background effects/blur, **locked rooms** ("Control who can join your rooms"), **local recording** ("Record your calls and save them locally"), calendar integrations (Google), breakout groups, virtual whiteboard; transcriptions listed under Embedded.
- Guest model: no download, no login for guests; FAQ exists for "Do I need to be present to start a meeting in my Whereby room?" (answer not fetched — not asserted).
- Support-center taxonomy: Getting Started / **Meeting Controls** / **Room Management** ("Your room is a space where you can meet with your participants — here are specific user guides for room modifications") / Account & Admin / Billing / Troubleshooting.
- **Two-product split**: "What is the difference between Meetings and Embedded?" — Meetings (end-user product) vs Embedded (API/SDK, programmatic room creation, for product builders). Whereby itself treats these as different products.
- Plan-gated numbers (L3): Free 1 host/1 room/4 attendees/30 min; Pro $10.99, 100 attendees, no time limit; Business $13.99/host, 200 attendees.

### Kumospace — evidence layer A (product page) — the spatial-venue boundary test

- Self-labels: "#1 virtual office software", "virtual office platform", "virtual workspace", "immersive virtual events platform" (FAQ). NOT "virtual meeting platform".
- Suite nav: **Online Meetings** ("Run productive virtual meetings"), **Video Conferencing** ("Video chat built for hybrid and remote work"), **Virtual Office** ("Voted #1 virtual workspace software"), **Virtual Events**, **Webinar Platform**, Team Chat, Screensharing, Online Whiteboard, Spatial Audio, Document Sharing.
- The venue mechanics belong to the Virtual Office product: "Move around your virtual office and connect seamlessly with spatial audio"; "Walk the floor—just like if you were in the office"; watercooler moments; people analytics ("visibility into how your team is spending their time").
- Marketing uses "virtual meeting tool" loosely for the whole suite ("The most highly reviewed virtual meeting tool on G2!") — but the *meetings* product itself is ordinary online meetings.
- Integrations include Zoom, Microsoft Teams, RingCentral, Slack, Outlook, Google Calendar, Miro, Google Drive.

### Livestorm — evidence layer A (product page) — the webinar-seam test

- Self-label: "All-in-one Webinar Software for Marketing Teams"; "The webinar leader, designed in Europe"; products: Webinars (live / on-demand / automated), Virtual Events, Restreaming, AI.
- Meetings capability exists as a mode (product-demos use case: "Meet engaging and personalized sales experiences"); one marketing card says "the easiest and most engaging webinar and meeting platform".
- Feature inventory is webinar-shaped: registration pages, email cadences, custom branding, analytics, CRM integrations, polls, Q&A with upvotes, moderators, dial-in by phone, breakout rooms, whiteboards, transcription, replays.
- Vendor's own guides distinguish the categories: "What is a webinar?", "What is video conferencing?", "What is a virtual event?".

### Airmeet — evidence layer A (product page) — venue-family self-label check

- Self-labels: "Virtual and Hybrid Event Platform", "Event Experience Cloud", "AI powered Webinar platform". NOT "virtual meeting platform".
- Use cases: townhalls, conferences/summits, job fairs, webinars, expos, community meetups; capabilities: registration/landing pages, speed networking, lounges, exhibition booths, ticketing, gamification/leaderboard, attendee analytics.
- Confirms: the venue/event family claims "virtual event platform", not "virtual meeting platform".

## Cross-product Comparison

| Structure | Zoom | Zoho Meeting | Whereby | Kumospace (meetings) | Livestorm (meetings) |
|---|---|---|---|---|---|
| Convened addressable meeting (own address: ID / link / room URL / key) | ✔ (meeting links; slug evidence) | ✔ (link or meeting key + password; meeting rooms) | ✔ (permanent room URLs) | ✔ | ✔ |
| Live real-time audiovisual session | ✔ | ✔ | ✔ | ✔ | ✔ |
| Multi-party shared session | ✔ | ✔ | ✔ | ✔ | ✔ |
| Host / moderator role with controls | ✔ | ✔ (moderator controls, role switch) | ✔ (room owner, locked rooms) | ✔ | ✔ (moderators) |
| Screen/content sharing | ✔ | ✔ | ✔ | ✔ | ✔ |
| In-meeting chat | ✔ | ✔ | ✔ | ✔ | ✔ |
| Recording | ✔ (cloud) | ✔ (cloud, download) | ✔ (local) | ✔ | ✔ |
| Scheduling + calendar integration | ✔ | ✔ (recurring; calendar tab) | ✔ (Google) | ✔ (integrations) | ✔ |
| Join without an account | (join page exists; not asserted) | ✔ (explicit) | ✔ (explicit) | not observed | ✔ (one-click access) |
| Admission gate variants | ✔ | ✔ (lock) | ✔ (locked rooms) | not observed | ✔ |
| Dial-in audio | ✔ (audio plan add-on) | ✔ (paid, international) | ✘ | not observed | ✔ (dial-in by phone) |
| AI notes / captions / transcription | ✔ (My Notes, captions) | ✔ (AI keynotes, transcription) | (Embedded tier) | ✘ | ✔ |
| Whiteboard | ✔ | ✔ | ✔ | ✔ (separate product) | ✔ |
| Breakout rooms | ✔ | ✔ | ✔ (breakout groups) | not observed | ✔ |

Reading of the table: every sampled product that sells "virtual meetings" realizes exactly the convened-meeting structure documented for Video Conferencing Application. No sampled product answers to "virtual meeting platform" with a different core.

## Abstraction Levels

### L0 — Defining Invariant

Identical to the sibling Type's core (re-derived independently from this pass's sample):

1. **The convened addressable meeting** — a session with its own address (meeting ID, join link, room URL, meeting key) that exists before the live connection and is distributed by invitation; participants join the meeting.
2. **The live real-time audiovisual session** — participants see and hear each other in real time; the visual meeting is the medium of record.
3. **The multi-party shared session** — a common space mixing more than two simultaneous participants with a shared view of presence and content.

Remove any one → a different Type (1 → video calling; 2 → conference calling; 3 → paired call). The alias claim is precisely that the market phrase "virtual meeting platform" denotes this same three-part core.

### L1 — Common Mature Structure

Host/moderator role with in-session controls; screen/content sharing (one presenter at a time); in-meeting chat; participant roster; pre-join preview; scheduling + calendar invitations + standing personal rooms; admission control (lobby / password / lock); recording with notice; layouts/self-view; multi-device clients; whiteboards; breakout rooms; AI notes/captions/transcription (era-current).

### L2 — Variant / Optional Structure

- Packaging: standalone product vs suite-embedded pillar (Zoom Workplace; Zoho Meeting+Calls; Kumospace suite) vs open-source/self-hosted (sibling pass's Jitsi pole).
- Delivery surface: installed app vs browser-only (Whereby, Zoho web) vs room devices (Zoom Rooms).
- Audio path: computer audio default; dial-in/call-me as plan-gated add-ons; absent at some poles.
- Recording venue: cloud estate vs local (Whereby local recording).
- Governance depth: org administration (users, policies, departments, custom domain, co-branding) — organizationally deployed products.
- Embed/API delivery of the same meeting machinery to other products (Whereby Embedded, Zoom Meeting/Video SDK) — a different product line, not a different meeting structure.
- Webinar packaging of the same media machinery (registration, broadcast roles) — the Webinar Platform sibling.
- Venue-adjacent packaging: persistent spatial spaces where meetings happen (virtual office) — a different Type (Virtual Office Workspace §03.12).
- Encryption posture, virtual backgrounds, captions/translation depth.

### L3 — Vendor-specific (research notes only)

- Zoom: "Zoom Workplace" suite naming; ZoomMate / My Notes (AI); Zoom Rooms / Zoom Node; plan numbers (40 min/100 free; 30 h/100 Pro; 300 Business); "continuous meeting chat".
- Zoho: Calls pillar (business phone numbers, US/EU); departments; 50 video feeds / 250 participants claims; 60-min free tier; custom domain + co-branding; "virtual meeting rooms" as standing team rooms.
- Whereby: room-URL plan tiers (1/3/unlimited; 4/100/200 attendees); Shared/Flex rooms; local recording; Meetings-vs-Embedded product split.
- Kumospace: spatial audio, floor-walking, people analytics, furniture/games; "virtual meeting tool" as suite marketing.
- Livestorm: registration/email-cadence/CRM machinery; "webinar and meeting platform" phrasing.

## Vendor-specific Findings

See L3. None of these enters the canonical core.

## Rejected Findings

- **"Virtual Meeting Platform is a container-level umbrella above meetings (scheduling + workspace + content + admin)"** — REJECTED as a distinct Type. The umbrella is the vendor *suite* (Zoom Workplace; Zoho's Meeting+Calls; Kumospace's multi-product nav), and suite packaging is already a documented variant of the meeting-centric Type. The container reading adds no objects that the meeting-centric Type lacks: scheduling, personal rooms, content, and admin are standard capabilities there (sibling doc). A Type defined as "the suite that contains other Types" would overlap Video Conferencing, Conference Calling, Webinar, and Team Workspace simultaneously.
- **"Virtual Meeting Platform = persistent spatial venue (Gather / Kumospace-office / Remo / Hopin / Airmeet)"** — REJECTED on self-label evidence: that family claims "virtual office" (Kumospace), "virtual & hybrid event platform" (Airmeet), not "virtual meeting platform". The directory already has Virtual Office Workspace (§03.12) for the office variant and event leaves in §26; claiming the venue family here would collide with both. Kumospace's own nav separates "Online Meetings — run productive virtual meetings" (ordinary meetings) from "Virtual Office" (the venue).
- **"Virtual Meeting Platform = embeddable video API platform (Whereby Embedded, Zoom Video SDK)"** — REJECTED: developer-facing infrastructure sold as a separate product line (Whereby's own FAQ splits "Meetings" vs "Embedded"; Zoom separates Meeting SDK/Video SDK from Meetings). The meeting structure is the same; the delivery model is a variant.
- **"Virtual meeting = webinar"** — REJECTED on the vendor's own seam: Zoho's FAQ distinguishes meetings (host and participants engage equally) from webinars (organizer broadcasts to attendees). Livestorm, a webinar-first vendor, keeps "meetings" as a distinct mode.
- **"The phrase denotes a distinct product population"** — REJECTED: across five sampled products plus the venue-family check, every use of "virtual meeting(s)" denotes the ordinary convened-meeting product.

## Boundary Findings

1. **vs Video Conferencing Application (§01.04, processed 2026-09-09) — ALIAS RESOLVED.** One market family behind two directory names. "Video conferencing" is the discipline/category term (room-system heritage; the industry category name); "virtual meeting platform" is the market's modern phrase for the same product. Direct evidence: Zoom's own URL slug "virtual-meetings" for its Meetings product; Zoho's dedicated "virtual meeting" page defining virtual meetings as audio+video+screen-share online communication and selling "Zoho Meeting's secure virtual meeting platform"; Kumospace's "Online Meetings — run productive virtual meetings". This discharges the video-conferencing pass's flag #2 (alias vs container-umbrella vs spatial-venue → **alias**). Both documents describe the same Type and stand alone; no directory change made from this side; consolidation-as-one-leaf remains a taxonomy-owner option.
2. **vs Conference Calling Application (§01.03, processed 2026-09-07) — observation absorbed.** That pass recorded "the meeting platform is the container (scheduling, workspace, content)". This pass resolves what the container *is*: the meeting platform is the video-conferencing product family itself; scheduling/workspace/content are standard capabilities of that Type, not a separate Type. The audio bridge remains that Type's center; dial-in audio appears here as plan-gated bundled machinery (Zoom audio plan; Zoho paid international dial-in; Livestorm dial-in), symmetric to the sibling passes' findings.
3. **vs AI Meeting Assistant (§03.10, processed 2026-09-06) — flag discharged from this side.** Platform-native assistants (ZoomMate/My Notes inside Zoom Meetings; Zoho's AI keynotes) are capabilities inside the hosting platform — and the hosting platform is this Type (= Video Conferencing Application). The standalone AI Meeting Assistant leaf remains valid for bot-based/capture-independent products. The boundary is porous by bundling, not by structure; consistent with that pass's own framing.
4. **vs Webinar Platform (§01.04, unprocessed) — seam confirmed, not owned.** Zoho's own meeting-vs-webinar FAQ (equal participation vs broadcast) and Livestorm's product split (webinar product with a meetings mode) confirm the many-to-many vs one-to-many seam already recorded by the video-conferencing pass. Large-meeting/view-only modes and webinar product lines sit on the seam; left to the webinar pass.
5. **vs Video Calling Application (§01.04, unprocessed) — not re-litigated.** The organizing-object seam (convened addressable meeting vs person-addressed call) was proposed by the video-conferencing pass; this pass's sample adds nothing that changes it. Zoom's "video calling" feature page under the Meetings product suggests the call is a mode of the meeting product — consistent with the seam's "both support 1:1 and group" note.
6. **vs Virtual Office Workspace (§03.12, unprocessed) — venue family forwarded.** The persistent spatial-venue population (virtual office: Kumospace's office product; Gather-class products) self-labels "virtual office", not "virtual meeting platform". Flag for that pass: the office venue is a different Type from the convened meeting; the two bundle (Kumospace sells both).
7. **vs Event leaves (§26, various) — venue/event family forwarded.** Airmeet/Hopin-class "virtual & hybrid event platforms" are event-shaped (registration, expo, stages, networking) and do not claim "virtual meeting platform". No leaf conflict with §01.04.
8. **去掉什么就变成另一个 Type (alias form):** remove the convened addressable meeting → video calling; remove the live video → conference calling; remove multi-party → paired call; add registration/broadcast roles → webinar; add persistent spatial occupancy → virtual office workspace; add event machinery (expo, ticketing, agendas) → virtual event platform (§26 territory).

## Historical / Market-Sample Check

- The alias reading is era-robust: "online meeting", "web meeting", "web conferencing", and "virtual meeting" are successive market phrases for the same convened-meeting family. Zoho's own pages bridge them ("web conferencing is a broad term that comprises various types of virtual meetings"; "Also known as virtual conferencing"). The room-system era (dedicated endpoints + bridge + scheduled conference) satisfies the same three-part core — argued structurally, consistent with the sibling pass's treatment (legacy primary sources not fetchable).
- The phrase "virtual meeting" itself is era-modern (it presupposes remote participation), but the *product* it names is not: dial-in-era and web-conferencing-era products are the same family under older names. The leaf's identity therefore does not depend on any single era's vocabulary.
- No regional or platform-native product was found that answers to "virtual meeting platform" with a different structure.

## Uncertainties

1. GoTo Meeting (the classic "online meetings" lineage) unreachable (403) — its self-label usage is unverified; no claims made. Confidence in the alias is carried by Zoom + Zoho + Kumospace + Livestorm evidence.
2. Zoom help center JS-rendered — no Zoom operational defaults asserted anywhere; Zoom evidence is positioning/feature-inventory level.
3. Zoho help-center article body empty — Zoho operational detail comes from product pages only; the moderator-controls detail set is therefore partial.
4. Whereby FAQ answers (e.g., "do I need to be present to start a meeting in my room?") not fetched — room-presence semantics not asserted.
5. Whether any niche vendor uses "virtual meeting platform" for pure video-interop infrastructure (Pexip-class "virtual meeting rooms" for room systems) — not researched; if so it would be an infrastructure variant inside the same family, not a distinct Type. Recorded as an open question only.
6. Kumospace/Livestorm meeting-mode operational details not fetched (nav-level evidence only for Kumospace; Livestorm's meetings mode inferred from use-case copy).

## Final Synthesis

**Virtual Meeting Platform ≡ Video Conferencing Application — one market family behind two directory names.** The market phrase "virtual meeting platform" denotes the convened online meeting product: a session with its own address that participants join, in which they see and hear each other in real time as a multi-party group. The defining core is the sibling Type's three jointly-held structures, re-derived here from an independent sample (Zoom, Zoho Meeting, Whereby, Kumospace-meetings, Livestorm-meetings). The three rival readings are rejected on product-own evidence: the container-umbrella is vendor suite packaging (a variant, not a Type); the spatial-venue family self-labels "virtual office"/"virtual event platform" and belongs to other leaves; the embed/API family is a delivery variant sold as a separate product line. The alias is stated in the final document; both documents stand alone; no directory change is made from this side.
