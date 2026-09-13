# Research Notes — Video Conferencing Application

Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

## Research Goal

Understand what a Video Conferencing Application really is, from real products: what the core objects and roles are, how a meeting is convened and joined, what happens inside the live session, how the session ends and what it leaves behind, what rules (admission, roles, recording permission) shape behavior, and where the boundary sits against neighboring Types (Conference Calling, Video Calling, Virtual Meeting Platform, Webinar Platform, Team Messaging, Meeting Recording, Virtual Classroom).

## Initial Boundary

- Directory leaf: 01.04 Video Communication & Meetings — "Video Conferencing Application".
- Sibling leaves in the same family: Video Calling Application, Virtual Meeting Platform, Webinar Platform (all unprocessed at research time).
- Nearest processed neighbors: conference-calling-application (2026-09-07, recorded a seam with this leaf), meeting-recording-transcription-application (2026-09-08, holds this Type as host/substrate), team-messaging-application, meeting-scheduling-application.
- Initial hypothesis: software for real-time audiovisual meetings among multiple participants, organized around a convened, addressable "meeting" (scheduled or instant) with host controls, screen sharing, and chat. Neighbors: personal video calling (contact-graph calls), conference calling (audio bridge), webinar (one-to-many broadcast).
- Historical check planned: room-based videoconferencing (dedicated endpoints, MCU bridges, ISDN/H.323) must still fit the definition.

## Research Questions

1. What is the central object — the meeting? What makes it addressable and joinable?
2. How does a meeting get convened (scheduled vs instant) and how do participants join (link, ID, dial-in, video device)?
3. What happens in the live session: media, sharing, chat, roles, controls?
4. Who controls what: host/organizer vs participant vs (enterprise) administrator?
5. How does the session end, and what artifacts remain (recordings, transcripts, chat)?
6. What admission/security machinery exists (lobby, password, guest join, E2EE)?
7. Where is the boundary vs Conference Calling (audio bridge), Video Calling (personal calls), Webinar (broadcast), Team Messaging (calls inside chat), Meeting Recording (the record as product)?
8. Does the definition survive the room-system era (no cloud, no links, no personal devices)?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers/deployment models:

| Product | Philosophy / position | Evidence level reached |
|---|---|---|
| Zoom (Zoom Meetings / Workplace) | meeting-first standalone; consumer-grade simplicity; born-cloud | Tier 2 (product/pricing page; help center JS-rendered) |
| Microsoft Teams | suite-embedded (meetings inside a collaboration platform); enterprise admin layer | Tier 1 (admin documentation, fetched) |
| Cisco Webex | enterprise legacy; longest history; room-device heritage | Tier 1 (help center articles, fetched) |
| Jitsi Meet | open-source, self-hostable; no-account pole | Tier 1 (handbook, fetched) |
| Google Meet | web-first, lightweight, suite-embedded | UNREACHABLE (all Google domains timed out ×3) |

## Sources

Fetched 2026-09-09:

- Zoom — Meetings product page (explore.zoom.us/en/products/meetings/): feature inventory, plan tiers, free-tier limits. [Tier 2]
- Microsoft Teams — "Overview of meetings and events in Microsoft Teams" (learn.microsoft.com/en-us/microsoftteams/overview-meetings-events). [Tier 1]
- Microsoft Teams — "Plan for Teams meetings" (learn.microsoft.com/en-us/microsoftteams/plan-meetings): meeting types, policies, roles table, lobby, recording, limits. [Tier 1]
- Microsoft Teams — admin documentation hub (learn.microsoft.com/en-us/microsoftteams/). [Tier 1]
- Cisco Webex — Help Center home + Getting started (help.webex.com). [Tier 1]
- Cisco Webex — "Get started with Webex Meetings for hosts" (help.webex.com/en-us/article/nrebr3c). [Tier 1]
- Cisco Webex — "Join a Webex meeting" (help.webex.com/en-us/article/nrbgeodb). [Tier 1]
- Jitsi Meet — Handbook: intro, user-guide category, "Start a Jitsi Meeting", FAQ (jitsi.github.io/handbook). [Tier 1]

Unreachable / abandoned (per source-access limitation rules):

- Google: support.google.com/meet (timeout ×1), support.google.com/a/users (timeout ×1), workspace.google.com/products/meet (timeout ×1) — Google domain abandoned. No Meet-specific operational claims are made anywhere in this research.
- Zoom support.zoom.com — JS-rendered shell, no article content reachable. Zoom evidence stays at product-page level.
- en.wikipedia.org/wiki/Videotelephony — timeout ×2, abandoned. Legacy-era (room-system/MCU/ISDN) primary sources not fetched.

## Product Observations

### Zoom (Tier 2 — product/pricing page)

Key observations [A for product-page claims]:

- Self-positioning: "Zoom Meetings: Conference call service for virtual collaboration… trusted video meetings"; "video conferencing built for modern work".
- Feature inventory: HD audio and video meetings; noise suppression; backgrounds/effects; built-in collaboration tools (whiteboards, documents, notes); AI summaries/notes; caption translations; "streamlined scheduling and join… tightly integrated calendar"; "continuous meeting chat… before, during, and after meetings"; screen sharing; virtual backgrounds; breakout rooms; teleconference/audio plan add-ons.
- Join/host surfaces: "Join a meeting" (zoom.us/join) and "Host a meeting" (zoom.us/start/videomeeting) as top-level product actions.
- Plan tiers (vendor-specific, plan-dependent): Basic free — 40 minutes max per meeting, 100 participants max; Pro — 30 hours per meeting, 100 participants; Business — 300 participants max. [L3 — do not generalize]
- Suite context: Zoom Workplace bundles Meetings with Chat, Phone, Mail & Calendar, Scheduler, Whiteboard, Clips; Webinars & Events sold as separate business line; Zoom Rooms for physical meeting spaces; Zoom Node hybrid deployment.
- Devices: desktop/mobile apps; "effortless device switching between desktop, mobile, and room systems".

### Microsoft Teams (Tier 1 — admin docs)

Key observations [A]:

- "There are multiple ways to meet in Microsoft Teams: Meetings, Events." Meetings vs events is a first-class product split (events = structured communications to larger audiences with organizer/co-organizer/presenter roles, registration, broadcast-style capacity).
- "Meetings are generally best for situations where participants need to interact with each other via voice, video, or chat and where multiple people might be presenting."
- Capacity (vendor-specific): up to 11,000 participants; first 1,000 fully interactive (audio, video, screen sharing); extra up to 10,000 view-only. Plan-meetings page: "audio, video, and screen sharing capabilities for up to around 1,000 people"; view-only kicks in around 900.
- Join without account: "Participants don't need to be a member of an organization, or have a Teams account to join a Teams meeting. They can join directly from the calendar invitation via the Join meeting link or call in via audio if available."
- Meeting types: Private meetings (scheduled with specific people); Channel meetings (visible to everyone in a channel, team can see/join/use the meeting chat); Meet now meetings (unscheduled, started through a chat).
- Two-layer control: admin meeting policies (who can join, join experience, feature availability, captions, recording/transcription policies) vs organizer meeting options (who can present, lobby bypass, recording, roles). Explicit roles: organizer, co-organizer, presenter, attendee.
- Lobby machinery: "Who can bypass the lobby", "whether anonymous participants can start a meeting", "whether people dialing in can bypass the lobby"; organizer can change per meeting.
- Access modes for outsiders: guests, people from trusted organizations, anonymous participants — configured separately.
- Audio Conferencing: license assigned to organizers so attendees can dial in from phones; organizers can dial out. (Conference-calling machinery as license-gated add-on — matches the conference-calling pass's finding.)
- Recording: policy-gated (both starter and organizer must be allowed); saved to OneDrive (private meetings) or SharePoint (channel meetings); attendees have view permission by default; expiration/recycle-bin behavior; download blocking; compliance recording (automatic, admin policy).
- In-meeting features from the admin/organizer table: breakout rooms (organizer-managed), Q&A, reactions, live captions/transcription (incl. translated), language interpretation, CART captioning, green room, RTMP-In/Out streaming, meeting apps, PowerPoint Live/whiteboard/shared notes, watermarks, sensitivity labels, E2EE (Premium), telemetry/real-time monitoring, attendance reports.

### Cisco Webex (Tier 1 — help center)

Key observations [A]:

- Host article: "Meetings makes hosting an online meeting easy. You can schedule a meeting in advance or start one right away." Schedule via User Hub; start from Upcoming Meetings; Personal Room as a standing personal meeting address.
- Audio connection choice at join: Use computer audio (default) / Call me / Call in (global call-in numbers) / Don't connect to audio (e.g., in a conference room, or a video device already connected).
- Video: start/stop before join; mirror self-view; virtual background (blur or replace).
- Share content: from the meeting control panel; "Anyone can share content, but only one person can share at a time" (Webex Suite video resource).
- Recording: "The recording includes the audio, video, and presentation." In-meeting recording indicator visible to all; recordings page in User Hub; cloud recording link by email.
- Join article: "You can join a meeting from your computer, mobile device, phone, or video device."
- Join flow: email invite → Join meeting → app auto-download (or browser join; Linux/Chromebook browser-native) → name entry → Sign in for full features OR "Join as a guest" → meeting password if set → pre-join preview (audio/video) → Join.
- Guest/account: "You don't need a Webex account to join meetings that you're invited to. You do need an email invitation that provides the information you need to join the meeting."
- Dial-in mechanics: access code or meeting number + attendee ID; "If you don't have your attendee ID, press # to wait in the lobby until someone in the meeting lets you in"; attendee ID connects name to audio, otherwise audio appears as a "separate call-in user". Dial-in users "can hear everyone… but won't be able to see anyone or what they share".
- Video-device join (legacy interop): "When you join a meeting from Cisco or third-party video devices, you can dial a SIP URI or IP address to join the meeting" — meeting number + SIP/H.323. [Key evidence bridging to the room-system era.]
- Recording permission: host-only by default; cohost assumes host role when host absent, original host takes it back on arrival; site storage limits; admin enablement; watermark-driven recording prevention.
- Suite context: Webex App = "all-in-one app to call, meet, message"; Webinars/Events as separate lines; Slido polling; Devices (Room/Desk/Board series); Control Hub admin.

### Jitsi Meet (Tier 1 — handbook)

Key observations [A]:

- Self-description: "Jitsi is a video conferencing platform. It is easy to use, easy to self-host…"; "State-of-the-art video conferencing you can self-host."
- Meeting address: room name → URL ("People can invite each other to Jitsi meetings by simply sending a link"). Start flow: enter conference name → Go → browser camera/mic permission → display name → Join meeting.
- Moderator role: "If you are the moderator of a conference, you can mute everyone's microphone. You cannot unmute other people's microphones, and they can unmute their microphones at any time." First participant on the hosted service "will be asked to either authenticate or wait for a moderator" (Google/Facebook/GitHub auth).
- Room protection: strong room name; different room name per meeting; room password ("Only people who have the password can join from that point on, but it does not affect people who have already joined"); password removed when the meeting ends; "secure domain" config (username/password to open a room → become moderator).
- Multi-party architecture: P2P mode for two participants; traffic passes through jitsi-videobridge (SFU) when a third joins. [Direct evidence of the 2→3+ bridge structure.]
- Recording: local recording (webm saved to device storage, max-size stop); external methods (OBS, RTMP server via Jibri, Dropbox integration, live-stream to YouTube).
- Deployment: hosted meet.jit.si, self-hosted (Debian/Docker), JaaS (8x8). Mobile apps + browser. Google Calendar extension. Participant-limit plugin for self-hosters.
- No dial-in audio observed in the handbook; no breakout rooms/captions observed in fetched pages. [Absence observations — weak, do not over-claim.]

### Google Meet (UNREACHABLE)

- All Google domains timed out (3 attempts across 2 domains). No operational claims made. Held as a representative product on market-position grounds (major suite-embedded meeting service); its structure is assumed to be covered by the cross-product pattern but is NOT cited as evidence for any specific claim.

## Cross-product Comparison

| Structure | Zoom | Teams | Webex | Jitsi | Meet |
|---|---|---|---|---|---|
| Meeting as convened addressable session (ID/link/room) | Y (join link, meeting ID) | Y (join link in calendar invite) | Y (meeting number/link, Personal Room) | Y (room name → URL) | (unreachable) |
| Live real-time audio+video | Y | Y ("voice, video, or chat") | Y | Y | — |
| Multi-party (more than two, mixed/bridged) | Y | Y (1,000 interactive + view-only) | Y | Y (P2P for 2 → videobridge for 3+) | — |
| Host/organizer role with controls | Y (host) | Y (organizer/co-organizer/presenter/attendee) | Y (host/cohost) | Y (moderator; optional via secure domain) | — |
| Join without account | Y | Y (explicit) | Y (guest join; explicit) | Y (no account at all) | — |
| Screen/content sharing | Y | Y | Y (one presenter at a time) | Y | — |
| In-meeting chat | Y (continuous meeting chat) | Y | Y | Y | — |
| Lobby/waiting room | (market-common) | Y (policy + per-meeting) | Y (press # → lobby) | (password instead) | — |
| PSTN dial-in / call-me audio | Y (audio plan add-on) | Y (Audio Conferencing license) | Y (call in/call me) | N (not observed) | — |
| Recording | Y | Y (policy-gated, OneDrive/SharePoint) | Y (host-only default; cloud/local) | Y (local webm; Jibri) | — |
| Scheduling + calendar + invitations | Y | Y (Outlook add-in, channel meetings) | Y (User Hub, Outlook) | Y (calendar extension) | — |
| Breakout rooms | Y | Y | (webinar line) | N (not observed) | — |
| Captions/transcription | Y (translations) | Y (incl. interpretation) | Y (AI summaries/transcripts) | N (not observed) | — |
| Virtual backgrounds | Y | Y | Y | N (not observed) | — |
| Room-device / SIP-H.323 interop | Y (Zoom Rooms) | Y (Teams Rooms) | Y (SIP URI/IP + meeting number) | N | — |
| Self-hosted deployment | N (hybrid Node) | N | N | Y (core identity) | — |
| Webinar/large-event mode | separate product line | Events (webinar/town hall) | separate product line | N | — |
| Suite-embedded | Y (Workplace) | Y (M365) | Y (Webex Suite/App) | N (standalone) | — |

Reading: the first three rows are universal; host role is universal in the sample but has a no-moderator pole (Jitsi without secure domain); dial-in audio, room devices, webinars, and suite embedding are bundling/variant axes, not identity.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **Live real-time audiovisual session** — participants see and hear each other in real time; the visual meeting (live video streams + shared stage) is the medium of record. Remove → conference calling (audio bridge) territory.
2. **Multi-party shared session** — the session is a common space mixing multiple simultaneous participants (more than two by design; the system bridges/mixes them). Remove → paired video calling.
3. **The convened addressable meeting** — the session exists as an addressable entity (meeting ID / join link / room name / room-system address) created ahead of or independent of the live connection, distributed by invitation or link, which participants join. Remove → person-to-person video calling (reachability via personal contact graph).

Jointly-held load-bearing: (1) alone = 1:1 video call; (2) without (1) = audio conference bridge; (3) without (1)+(2) = a booked slot with no live media (scheduling territory); (1)+(2) without (3) = ad-hoc group video chat drifting toward video calling / social live video; (1)+(3) without (2) = scheduled 1:1 video call (video-calling pole).

### L1 — Common Mature Structure

- Host/organizer role with in-session controls (mute others, admit/remove, assign roles: cohost/co-organizer/presenter). Universal in sample; Jitsi's optional-moderator pole shows a conference can exist without enforced host controls → held common, not definitional.
- Screen/content/application sharing (one presenter at a time; request/transfer control).
- In-meeting text chat.
- Participant roster (names/avatars, speaking indicators, hand-raise).
- Pre-join preview: device selection (mic/camera/speaker), audio connection choice, video on/off, background.
- Scheduling + calendar integration + invitations carrying the join link; instant "meet now" as the second convening mode.
- Personal meeting room (standing personal address; vendor terms vary).
- Lobby/waiting-room admission (or password protection as the lighter alternative).
- Recording with in-session notice/indicator; cloud or local storage; post-meeting playback/share.
- Layouts (gallery/speaker), self-view, per-participant mute/camera toggles.
- Multi-device clients: desktop app, mobile app, browser/web.
- Modern additions near-universal in the business tier: breakout rooms, polls/reactions, live captions/transcription, virtual backgrounds.

### L2 — Variant / Optional Structure

- PSTN dial-in/call-me audio (conference-calling machinery bundled; license-gated in Teams, plan-gated in Webex/Zoom; absent in the Jitsi sample).
- Room-system/hardware interop (SIP/H.323 video-device dial-in; certified room devices; room-mode products).
- Webinar/large-event mode (registration, broadcast roles, view-only audiences) — packaged as separate product lines or modes; boundary to Webinar Platform.
- Encryption posture (transport default; E2EE as premium/optional mode).
- Deployment: cloud SaaS vs self-hosted/open-source (Jitsi pole) vs hybrid.
- Packaging: standalone meeting product vs suite-embedded (chat/calling/docs around it).
- AI overlays (recaps, summaries, in-meeting assistants), whiteboards, meeting apps, RTMP streaming.
- Compliance machinery (watermarks, sensitivity labels, compliance recording, retention/expiry).
- Free-vs-paid economics (duration/participant limits as plan gates).
- Industry/audience variants (education, telehealth, government, events).

### L3 — Vendor-specific (research notes only)

- Zoom: 40-min free meeting cap, 100/300-participant tiers, ZoomMate/AI Companion naming, Zoom Rooms, Zoom Node, Workplace bundling.
- Teams: meeting policies admin layer, Teams Premium feature gating, channel meetings, green room, RTMP-In/Out, Copilot interpreter agent, OneDrive/SharePoint recording storage, ~1,000 interactive / 10,000 view-only capacity.
- Webex: attendee ID mechanics + "separate call-in user" failure mode, Personal Room, User Hub, cohost handback, Slido polling, Control Hub, Room/Desk/Board devices.
- Jitsi: secure domain, prosody config, jitsi-videobridge SFU, Jibri recording, JaaS, room-name generator, password-cleared-at-end behavior.

## Rejected Findings

- "Video conferencing = any video call" — rejected: the convened addressable meeting (not a call placed to a person) is the organizing object; 1:1 contact-graph calling is the Video Calling sibling.
- "Screen sharing is definitional" — rejected: remove it and the product is still recognizably video conferencing; it is the strongest common capability, not the invariant.
- "Host controls are definitional" — rejected (weakly): Jitsi's no-moderator pole (no secure domain) is still recognizably video conferencing; host role held common-not-definitional. Uncertainty flagged.
- "Dial-in audio is part of the Type" — rejected: it is conference-calling machinery bundled into meeting products (license/plan-gated); the Jitsi pole lacks it entirely.
- "Cloud accounts and links are definitional" — rejected: room-system-era addressing (SIP/H.323 + meeting number) realizes the same addressable-meeting concept; Jitsi realizes it with a bare room name.
- "Capacity numbers are definitional" — rejected: plan- and product-dependent (Zoom 100–300; Teams ~1,000 interactive + 10,000 view-only; Jitsi self-hosted configurable).
- "Webinar features (registration, broadcast) are part of this Type" — rejected: they belong to the Webinar Platform sibling; in sampled suites they are separate product lines/modes.

## Boundary Findings

- **vs Conference Calling Application (01.03, processed 2026-09-07)** — RATIFIED from this side on the medium-of-record seam exactly as that pass framed it: remove the visual meeting → conference calling; remove the audio bridge → this Type. Modern meeting products bundle both; dial-in audio appears here as license/plan-gated adjacent machinery (Teams Audio Conferencing license; Webex call-in/call-me; Zoom audio plan), symmetric to that pass's finding that video is bundled adjacent machinery there.
- **vs Video Calling Application (01.04, unprocessed)** — organizing-object seam: here the session is a convened addressable meeting distributed by invitation/link (participants join the meeting); there the call is placed to a person via a personal contact graph (participants answer a call). Both support 1:1 and group; center of gravity differs. FLAG for joint review at that pass: proposed test — remove the convened addressable meeting → video calling; remove person-addressed calling from a personal contact graph → this Type.
- **vs Virtual Meeting Platform (01.04, unprocessed)** — potential alias/umbrella. The market phrase "virtual meetings" is used by sampled vendors for ordinary meetings (Zoom's own URL slug is "virtual-meetings"); the conference-calling pass recorded "the meeting platform is the container (scheduling, workspace, content)". FLAG for joint review at that pass: decide alias vs container-level umbrella vs spatial-venue variant; this pass holds Video Conferencing Application as the meeting-centric Type and makes no directory change.
- **vs Webinar Platform (01.04, unprocessed)** — many-to-many conversation vs one-to-many broadcast with registration/audience management. Large-meeting/view-only modes (Teams view-only tier; Webex/Zoom webinar product lines) sit on the seam and are packaged as separate modes/products in-sample. FLAG for joint review at that pass.
- **vs Team Messaging Application (processed)** — persistent conversation spaces vs live convened sessions; meetings embedded in chat (Teams channel meetings/meet-now from chat; Zoom continuous meeting chat) are bundling, not identity.
- **vs Meeting Recording & Transcription Application (processed)** — recording is an embedded capability here (host-gated, stored in the meeting product's estate); that Type's world is the record library independent of which platform hosted the session. Consistent with that pass's own boundary table.
- **vs Meeting Scheduling Application (processed)** — scheduling products book the meeting (host-published availability, invitee self-booking); conferencing products run it. The join link is the shared object across the seam; video-conferencing defaults in scheduling products are an integration, not this Type.
- **vs Virtual Classroom (23, unprocessed)** — same media, different purpose: instruction/assessment semantics, persistent class context. Not asserted further.
- **vs Social Live Streaming Platform (01.08, unprocessed)** — broadcast-to-audience vs mutual participation among known invitees; no registration/audience machinery here.
- **vs Remote Customer Support Platform (processed)** — support records, consent machinery, unattended access vs meeting-shaped scheduled sessions.
- **Web-conferencing heritage note** — products that began as screen-share+audio "web conferencing" and later added live video are now this Type; the live video medium is what makes them video conferencing (consistent with the conference-calling pass holding video as the other Type's medium). Screen-share-only meetings without live video sit at the conference-calling/web-conferencing side of the seam.

## Historical / Market-Sample Check

- Room-based videoconferencing era (dedicated room endpoints dialing each other over ISDN/IP, multiparty via MCU bridges, scheduled conferences): fits L0 — live audiovisual ✓, multi-party via bridge ✓, convened addressable session (scheduled conference / endpoint address) ✓. No cloud accounts, no join links, no personal devices, no chat, no screen share required. Evidence: structural (C-layer canonical inference) + one surviving bridge in the modern sample (Webex documents SIP URI / IP address + meeting number join from video devices [A]); legacy-era primary sources were NOT fetchable (Wikipedia unreachable ×2) — the historical fit is argued structurally, not from fetched legacy documentation. Confidence: moderate.
- Early consumer videochat (person-to-person) — belongs to the Video Calling sibling, not this Type.
- Screen-share-only web conferencing (audio + content, no live video) — sits at the conference-calling side of the medium seam; products of this heritage that added video are in-Type today.
- The definition does not presuppose: phone numbers, work accounts, cloud recording, AI features, or any specific capacity.

## Uncertainties

- Google Meet unreachable — no Meet-specific claims anywhere; Meet held as representative on market-position grounds only.
- Zoom help center JS-rendered — Zoom evidence is product-page level; no Zoom operational defaults asserted.
- Host-role definitional status — held common-not-definitional on the strength of one product's optional-moderator pole; if the video-calling/virtual-meeting passes disagree, revisit.
- Legacy room-system era — structural fit argued, not directly sourced; recorded as moderate-confidence canonical inference.
- Whether lobby/waiting-room is universal vs password-only protection (Jitsi pole) — held as common implementations of one admission concept, not separately definitional.
- Exact capacity/duration numbers — plan-dependent, vendor-specific; never asserted in the final document.

## Final Synthesis

A Video Conferencing Application is a live multi-party audiovisual meeting service. Its defining core is three jointly-held structures: the live real-time audiovisual session (the visual meeting is the medium of record), the multi-party shared session (a common space bridging more than two participants), and the convened addressable meeting (a session with its own address — ID, link, room name, or room-system address — that exists before the live connection and is distributed by invitation or link, which participants join, often without any account). Around that core, mature products add the host/organizer role with in-session controls, screen/content sharing, in-meeting chat, the pre-join preview, scheduling and calendar invitations, personal meeting rooms, lobby/password admission, recording with notice, layouts, and multi-device clients; the modern business tier adds breakout rooms, polls, captions/transcription, and virtual backgrounds. Dial-in audio, room-device interop, webinar modes, E2EE, self-hosting, suite embedding, AI overlays, and compliance machinery are variant axes. The Type survives from the room-system era (endpoints + bridge + scheduled conference) through free dial-in-less open-source rooms to suite-embedded enterprise meeting stacks — the live audiovisual + multi-party + convened-addressable-meeting structure is the invariant.
