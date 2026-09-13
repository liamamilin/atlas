# Research Notes — Meeting Recording & Transcription Application

## Research Goal

Understand what a Meeting Recording & Transcription Application really is, from real products: what gets captured, how capture happens, what the transcript is, how meeting records are organized and reused, what rules (consent, permissions, retention) shape behavior, and where the boundary lies against neighboring Types (AI Meeting Assistant, Meeting Notes Application, Video Conferencing Application, Conversation Intelligence Platform, generic transcription tools).

## Initial Boundary

Working hypothesis before research:

- Core use: capture the audio/video of a meeting as it happens and produce a transcript of what was said, so people can review, search, share, and reuse the record.
- Users: anyone who runs or attends meetings — individuals (journalists, students, researchers), teams, sales/customer-facing roles, enterprises.
- Nearest neighbors: AI Meeting Assistant (sibling leaf), Meeting Notes Application (sibling leaf), Video Conferencing Application (recording as embedded capability), Conversation Intelligence Platform (sales-call analytics), dictation/transcription utilities.
- Known tension: modern products market themselves as "AI notetakers" and realize recording + transcription + AI notes simultaneously; the directory splits these into three leaves. Each document must hold its own center.

## Research Questions

1. What exactly is captured (audio only vs audio+video), and through which capture mechanisms (bot participant, botless local capture, platform-native recording, file import)?
2. What is the transcript: verbatim? speaker-labeled? timestamped? editable? live vs post-processing?
3. What is the meeting record, and how is it organized (library, list, folders, notebook, dashboard)?
4. What do users do with records: review, playback, search, highlight/clip, edit, share, export?
5. Where does the AI layer (summaries, action items, chat) sit — definitional or common?
6. Which rules matter: consent/recording notice, platform access (guest policies), processing states, retention/expiration, storage metering, permissions?
7. Where is the boundary against AI Meeting Assistant, Meeting Notes, conferencing platforms, Conversation Intelligence, and generic transcription?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy / position | Customer tier |
|---|---|---|
| Otter.ai | transcription-first personal archetype; "conversations" framing; consumer→business ladder | individual → SMB → enterprise |
| Fireflies.ai | bot/integration-first team product; wide platform coverage; workspace + AI layer | individuals → teams → enterprise |
| tl;dv | video-first recorder; clips/reels; product & research customers; EU security posture | free-forever → teams |
| Fathom | free-forever AI notetaker; sales-oriented; bot-free capture push | individuals → sales teams |
| Microsoft Teams | platform-native recording + transcription embedded in the conferencing product (positioning + historical check) | enterprise (org-administered) |

Zoom was originally considered as the platform-native sample but its support portal could not be fetched (JS-rendered; two attempts failed). Microsoft Teams (Microsoft Learn admin documentation) was substituted. See Sources.

## Sources

Tier 1 (official operational documentation, fetched 2026-09-08):

- Otter.ai Help Center: What is Otter?; Conversation Page Overview; Otter Notetaker Overview; Share a conversation — https://help.otter.ai/
- Fireflies Knowledge Base: What is Fireflies.ai; What are your post-meeting features; collection structure (Getting Started, Meeting Controls & Settings, Call Recording Rules, Migrations, Conversation Intelligence, AI Skills) — https://help.fireflies.ai/
- Fathom Help Center: Getting Started category; How to find your calls in Fathom; Using Fathom After a Call category — https://help.fathom.video/
- Microsoft Learn (Teams admin docs): Introduction to recording Microsoft Teams calls, meetings, and events (teams-recording-policy); Overview — Recording and transcription for Teams meetings, events, and calls (recording-transcription-overview) — https://learn.microsoft.com/en-us/microsoftteams/

Tier 2 (official product/marketing pages):

- tl;dv: homepage; Recordings & Transcriptions feature page — https://tldv.io/ , https://tldv.io/features/meeting-recordings-transcriptions

Source-access limitations:

- Zoom support portal (support.zoom.com / support.zoom.us): JS-rendered, content not retrievable; two attempts, abandoned. Zoom not used as a sampled source.
- tl;dv help center (intercom.help/tldv): request timed out twice, abandoned. tl;dv evidence is Tier 2 only; product-specific operational details (retention windows, exact behaviors) are NOT asserted.
- Microsoft end-user support article (support.microsoft.com "Record a meeting in Teams"): 404; Microsoft Learn admin documentation used instead (admin-facing; end-user surface inferred only where the admin doc states it).
- Otter/Fireflies/Fathom help centers were reachable; observations below are Layer A (directly observed) unless marked otherwise.

## Product A — Otter.ai

### Key observations (Layer A unless noted)

- Positioning: "converting your voice interactions into searchable, shareable smart notes" for meetings, interviews, brainstorming, and transcribing existing recordings. (What is Otter?)
- The central object is the **conversation** = one captured session. The Conversation Page is the record: two tabs — **Summary** (AI-generated summary, AI-generated action items, outline) and **Transcript** (full transcript, keywords, speakers with per-speaker talk-time percentage breakdown, highlights, audio playback controls synced to text).
- Transcript is editable; speakers can be tagged/named; comments, highlights, images, reactions attach to transcript positions. Audio playback follows the transcript.
- Action items: AI-generated (with "View in transcript" linkage back to the source utterance) plus manually added; assignable to people; deletable (permanent).
- Notable product rule: the AI summary "cannot be regenerated at this time" — it is generated from the live meeting content; later speaker tags/edits are not reflected (users are told to use Otter Chat for a fresh summary incorporating edits).
- Capture modes: (1) Otter Notetaker bot — connects Google/Microsoft calendar, syncs events, auto-joins Zoom/Google Meet/Teams meetings as a visible guest participant named "[Your Name]'s Notetaker (Otter.ai)"; cannot join anonymously; requires the platform to allow guest participants; leaves after continuous silence (12 min; 5 min past scheduled end). (2) Botless recording via the Otter Desktop app (system audio). (3) Mobile app for in-person recording. (4) Import of audio (mp3, aac, wav, m4a, wma) and video (mp4, avi, mov, wmv, mpg) files for transcription.
- Library: "My Conversations" + **Folders** (organize by team/project/location) + **Channels** (organize and share with groups). Bulk operations on multiple conversations.
- Sharing: per-conversation permission levels — **Collaborator** (edit, view, playback, export, chat, takeaways, optionally re-share) vs **Viewer** (view + playback only; export only if owner toggles it); link settings — restricted / anyone in workspace / anyone with the link; revocable anytime; **snippet links** share a single highlighted transcript portion (with audio playback of that portion; cannot be restricted/revoked once created).
- Export: text and audio in various formats; import/export both first-class.
- AI layer: Meeting Summary, Action Items, Outline (live summary during recording), Otter Chat (Q&A over conversations), automated slide capture (photos of slides/whiteboards integrated into transcripts).
- Team layer: Workspaces, seats, admin controls, admin logs, deduplication of Notetakers, auto-share rules (e.g., auto-share with same-domain users), HIPAA support.
- Consent posture: Notetaker FAQ — "Always obtain any required consent and follow applicable recording laws"; bot is always visible to participants.

## Product B — Fireflies.ai

### Key observations (Layer A unless noted)

- Positioning: "AI notetaker assistant that helps you capture, transcribe, summarize, and search meetings – all in one secure workspace", across in-person, Zoom, and uploaded recordings. (What is Fireflies.ai)
- Capture modes: (1) Fireflies bot invited to live meetings on Zoom, Google Meet, Teams, Webex and more; (2) Chrome extension transcribing Google Meet calls from the browser; (3) Desktop app recording in-person meetings or system audio; (4) mobile app for in-person; (5) upload of audio/video files; (6) integrations (Zoom, dialers, Dropbox) auto-syncing recordings; (7) Migrations collection — import meetings, recordings, and transcripts from supported platforms.
- Post-meeting pipeline (documented as a distinct phase): check if meetings/files are **processed** (asynchronous processing states; a dedicated **Meeting Status Page** tracks per-meeting status); then transcripts, AI summaries, action items.
- Transcript: "accurate transcripts with speaker labels in 100+ supported languages"; transcripts are editable (Notepad); searchable within and across meetings.
- Library: **Notebook** — "Organize meetings, tasks, contacts, and insights"; search and find meetings; storage limits and transcription credits are plan-metered (recording/transcription is a metered resource).
- Collaboration: clip **soundbites**, build playlists, leave comments, share transcripts/summaries; download transcripts, summaries, and recordings.
- AI layer: AI summaries with key topics, action items, custom sections; **AskFred** (Q&A over meetings); **AI Skills** (100+ prebuilt templates for tailored outputs); Conversation Intelligence (talk time, monologues, sentiment, topics, trends) — a distinct module.
- Controls: Call Recording Rules collection (transcription language default/auto-detect/multi-language; how to remove Fireflies from a meeting or stop it from joining); Advanced Settings; Private Storage for workspaces; Super Admin role; Enterprise plan.
- Integrations: 50+ apps sending meeting data to CRMs, PM tools, ATS, Slack.

## Product C — tl;dv

### Key observations (Layer B/C — Tier 2 sources only; help center unreachable)

- Positioning: "AI Notetaker built for Team Collaboration… captures knowledge, finds answers, and automates meeting workflows"; "Too Long, Didn't View".
- Core promise (feature page): "As soon as a call ends, tl;dv's AI Notetaker automatically generates a video recording, a translatable transcript, and a shareable summary." Records across Zoom, Google Meet, Microsoft Teams; slide capture; automatic recording of every meeting ("no need to click a thing"); "NO BOT REQUIRED" (botless capture option marketed).
- Transcript: automatic speaker recognition ("every voice is identified and attributed"); 30+ languages; transcription + translation; search transcripts, titles, and participants by keyword and "jump straight to the moments that matter most".
- Record-work layer: highlight any transcript part → auto-generated shareable clip; combine clips into shareable **Reels**; topic trackers; trimming recordings (marked "soon" at research date).
- AI layer: AI meeting notes/summaries (customizable formats, e.g., MEDDIC in Japanese), AI reports aggregating insights across meetings, sales coaching module, CRM logging and follow-up drafting.
- Security posture (marketing): E2E encryption, GDPR, SOC 2, EU hosting, "Your recordings and transcripts are yours (not ours)… never used to train AI."
- NOT asserted (source unreachable): retention windows, exact consent mechanics, processing states, permission model details.

## Product D — Fathom

### Key observations (Layer A unless noted)

- Positioning: free AI notetaker; desktop-app-centric; recent "bot-free experience" where Fathom "detects your meetings automatically and you choose your capture" (Getting Started).
- Capture modes: (1) bot-free desktop capture (detects calendar meetings with Meet/Teams links, records locally); (2) Fathom Notetaker bot joins Teams meetings as a participant; (3) Fathom Zoom App records directly within Zoom; (4) test call for onboarding. Calendar authentication (Google/Microsoft) drives meeting detection.
- Library: **Fathom Dashboard** — "access all of your captured calls"; scroll-loading of older recordings; **Team Calls Library** for paid Team Edition seats.
- Record sharing/visibility (Team Edition): per-recording visibility dropdown — No Team Visibility (private) / Visible to Support Only (sub-team) / Visible to All Teams / Visible to Multiple Teams; org admin rules govern auto-shared external meetings; setting "Make external meetings visible to your team by default".
- Record-work layer: transcript (copy/paste; direct download not offered — copy is the export path for text), recording download as MP4 (MP3 "coming soon"), trimming calls by hovering transcript sections, highlights (in-meeting or post-meeting), AI summaries (customizable), action items with "Copy for Asana", Ask Fathom (Q&A over one call; account-wide Ask Fathom across meetings), MCP connection to external AI assistants (Claude/ChatGPT).
- Auto-share: Fathom can automatically share recordings and/or AI summaries with meeting attendees when enabled.
- Deletion of recordings supported.

## Product E — Microsoft Teams (platform-native)

### Key observations (Layer A — admin documentation)

- Native capability inside the conferencing product: "your users can record and transcribe their meetings, events, and calls. Transcription automatically turns spoken dialogue into written text… Recording captures audio, video, and screen-sharing activities."
- Two recording kinds: **convenience recording** (user-initiated, user-managed) vs **compliance recording** (third-party, admin/system-initiated, company-owned, no participant-consent support, enforced notification).
- Governance machinery (admin policy layer): recording and transcription are separately policy-controlled per meetings/events/calls; **auto recording** organizer setting; **explicit recording consent** policy (participants must consent to be included in recording/transcription); participant notification enforced for both convenience and compliance recording; **recording and transcript expiration** policy; custom privacy-statement URL; download blocking for recordings/transcripts in SharePoint/OneDrive; eDiscovery search over recordings and transcripts; storage in OneDrive/SharePoint with permission inheritance; sensitivity labels/templates (Teams Premium) to control who can record/transcribe; Copilot "intelligent recap" depends on transcript availability and licensing.
- Recording limits documented (what is NOT captured: >4 video streams at once, whiteboards/annotations, shared notes, embedded media, multi-screen share) — evidence that even platform-native recording is a lossy capture of the meeting, not the meeting itself.
- Transcripts stored as files alongside recordings (OneDrive/SharePoint); organizer can restrict participants from copying/forwarding transcripts and AI insights.

## Cross-product Comparison

| Dimension | Otter | Fireflies | tl;dv | Fathom | Teams (native) |
|---|---|---|---|---|---|
| Capture mechanisms | bot + botless desktop + mobile + file import | bot + browser extension + desktop + mobile + upload + integration sync + migration import | bot + botless + auto-record (Tier 2) | bot-free desktop detection + bot + platform app | native in-meeting recording |
| Recording medium | audio native; audio/video import | audio/video | video + audio | video (MP4 download) | audio + video + screen share |
| Transcript | speaker-labeled, editable, playback-synced | speaker-labeled, editable, 100+ languages (vendor claim) | speaker recognition, 30+ languages, translatable (Tier 2) | transcript, copy/paste export | transcript files (.vtt-class), policy-gated |
| Library | My Conversations + Folders + Channels | Notebook + search + storage metering | meeting list + search (Tier 2) | Dashboard + Team Calls Library | OneDrive/SharePoint storage + lists |
| Processing lifecycle | processing after capture (implied) | explicit Meeting Status Page / processed checks | not verified | recordings appear on dashboard after capture | storage after meeting; expiration policy |
| AI layer | Summary/Action Items/Outline/Chat | summaries/action items/AskFred/AI Skills | AI notes/reports (Tier 2) | AI summaries/action items/Ask Fathom | Intelligent recap (Copilot, licensed) |
| Sharing | permission levels + links + snippets | share transcripts/summaries, soundbites, playlists | clips/reels/summaries (Tier 2) | visibility dropdown + auto-share + MP4 | SharePoint/OneDrive permissions + download policy |
| Consent/notice | consent reminder; bot always visible | removable from meetings; recording rules | not verified | — | notification enforced; explicit consent policy; compliance recording variant |
| Team/admin layer | Workspaces, admin controls, dedupe | Super Admin, private storage, enterprise | teams plans | Team Edition, org settings | full policy machinery |

Stable across all five (Layer B):

1. A captured meeting becomes a persistent record holding a recording (audio at minimum) and a transcript together.
2. The transcript is the record's text substrate: verbatim speech-to-text, with speaker attribution and time alignment as the dominant implementations.
3. Records accumulate in a retrievable library (list/dashboard/notebook/folders/storage), searchable across meetings.
4. Users work the record after the meeting: read/search/edit transcript, playback aligned to text, highlight/clip, share with permissions, export.
5. Capture is multi-mechanism: bot participant, botless local capture, platform-native recording, file import — often several in one product.
6. An AI derived layer (summary, action items, Q&A) sits on top of the record in all current products — but is a derived layer, not the substrate.
7. Capture is consent-sensitive and platform-access-dependent; processing is asynchronous; retention/permissions are governed.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The captured meeting record** — a real spoken session (meeting, call, interview, lecture) captured as a recording (audio, optionally video), whether captured in-product or imported; the recording is the record's media substrate. Remove → generic voice recorder or a conferencing platform's recording vault.
2. **The transcript** — the session's spoken content rendered as text, held as part of the same record. Remove → plain recording storage.
3. **The retrievable meeting library** — records persist as individually identified, organized, searchable entries the user returns to over time; recording and transcript stay bound to the same record. Remove → a one-shot transcription utility/service that converts inputs into documents with no memory of meetings.

Joint-held test:

- 1 alone = voice recorder / meeting-recording vault
- 2+3 without 1 = transcript archive (human transcription service territory)
- 1+3 without 2 = recording library without transcription
- 1+2 without 3 = recorder+transcriber utility (voice-memo-with-transcription shape)

Historical / market-sample check (§24-style, applied):

- Analog era: tape recorder + typist-produced transcript filed per meeting in a cabinet — satisfies all three legs (no AI, no bots, no cloud, no video, no speaker diarization machinery). ✓
- Platform-native: Teams recording + transcript stored in OneDrive/SharePoint, retrievable per meeting — satisfies (as embedded capability). ✓
- Pre-AI standalone: recorder + ASR/human transcript library — satisfies. ✓
- Therefore L0 must NOT include: bots, AI summaries, calendar sync, video, live view, speaker diarization, cloud, timestamps, team workspaces. All are L1/L2.

### L1 — Common Mature Structure

- Speaker identification/labeling (diarization + human naming/correction of speakers)
- Timestamp alignment: transcript positions link to playback positions
- Transcript editing (correct text, tag speakers)
- Highlights/comments on transcript positions; clips/soundbites/snippets
- Sharing with permission levels; link sharing; revocation
- Export (text formats; audio/video download) and import (audio/video files)
- Search across meetings and within transcripts
- AI derived layer: summary, action items, Q&A/chat over records (near-universal in the current market, but derived — pre-AI products are complete without it)
- Calendar connection driving scheduled capture
- Team/workspace layer with roles and admin controls (in team products)
- Organization containers: folders / channels / notebook / collections

### L2 — Variant / Optional Structure

- Capture posture: bot participant vs botless (desktop/system-audio, platform-app embedding) vs platform-native recording vs file import; auto-join vs manual
- Video vs audio-only recording
- Live transcription/live notes during the session vs post-session processing
- Language coverage, translation, multi-language meetings
- Cross-meeting intelligence: analytics (talk time, sentiment, topics), aggregated reports, coaching (seam toward Conversation Intelligence Platform)
- Downstream integrations: CRM, task tools, ATS, Slack, Zapier-class automation
- Retention/expiration policies, compliance recording, eDiscovery, private storage
- Consent machinery: enforced notification, explicit-consent gates, custom privacy URLs
- Metering: transcription credits, storage limits, minutes quotas
- Business-model shapes: free-forever, seat-based teams, enterprise

### L3 — Vendor-specific (Research Notes only)

- Otter: Otter Chat, Outline, Takeaways, Channels, snippet links, photo/slide capture into transcripts, 12-minute silence auto-leave, Notetaker display-name scheme, workspace Notetaker deduplication, summary non-regeneration rule, HIPAA support, AI Agents (Sales/Recruiting/Education/Media)
- Fireflies: AskFred, Soundbites, playlists, Notebook, AI Skills, Meeting Status Page, Super Admin, private storage, transcription credits, dialer integrations, Voice Agents
- Fathom: Team Calls Library visibility model, Ask Fathom (per-call and account-wide), MCP connection, bot-free experience, Copy for Asana, referral program
- tl;dv: Reels, topic trackers, "no bot required" positioning, MEDDIC-class summary templates, 96% accuracy claim (marketing), EU-hosting posture
- Teams: policy machinery (meeting/event/calling policies), sensitivity labels/templates, Copilot intelligent recap, OneDrive/SharePoint storage and permission inheritance, eDiscovery, compliance-recording third-party program, RTT, custom dictionaries

## Vendor-specific Findings

- Otter's summary non-regeneration (AI summary fixed at generation time; edits handled via Otter Chat) is product-specific behavior — do not generalize.
- Fireflies' Meeting Status Page and transcription-credit metering are product-specific implementations of the general processing/metering pattern.
- Fathom's Team Calls Library visibility enum (none/sub-team/all/multiple) is product-specific; the general pattern (per-record team visibility) is common.
- Teams' explicit-recording-consent policy and compliance-recording program are platform-specific realizations of consent machinery; Otter/Fireflies handle consent through visibility + user responsibility instead.
- tl;dv's Reels and topic trackers are product-specific record-work extensions.

## Rejected Findings

- "AI summary/action items are part of the definition" — REJECTED. Pre-AI and platform-native forms satisfy the Type without them; the AI layer is derived from the record, not the record itself. Held at L1 (common mature).
- "A bot participant is required" — REJECTED. Botless capture (Otter desktop, Fathom bot-free, tl;dv no-bot, Fireflies desktop/mobile) and platform-native recording (Teams) and file import (all) realize capture without a bot. Bot is one capture implementation.
- "Video recording is required" — REJECTED. Otter is audio-native (video only via import); Teams supports audio-only recording. Audio is the invariant minimum; video is common but not definitional.
- "Speaker labels are definitional" — REJECTED. Analog/human transcripts and raw ASR output can lack speaker attribution; it is the dominant modern implementation (L1), not the invariant.
- "This Type = Conversation Intelligence" — REJECTED. Analytics/coaching modules exist in Fireflies/tl;dv but are extensions; the record library is the center.
- "This Type = AI Meeting Assistant" — REJECTED as an identity, but the overlap is real and recorded under Boundary Findings.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what makes it a different Type) |
|---|---|---|
| AI Meeting Assistant | closest sibling; heavy market overlap | This Type's center is the verbatim record (recording + transcript) held in a library; AI outputs are derived. An AI Meeting Assistant centered on generated notes/insights/action items — where the verbatim capture library is not the substrate — is the other Type. Current products realize both; each document must hold its center. |
| Meeting Notes Application | sibling | Human-authored notes about meetings; no capture machinery, no verbatim substrate required. |
| Video Conferencing Application | host/substrate | The conferencing product runs the meeting; recording+transcription is one embedded capability. This Type's whole world is the record of the meeting, independent of who hosted it. Platform-native embedding is a packaging variant. |
| Conversation Intelligence Platform | downstream/adjacent | Adds analysis, coaching, CRM workflows over call recordings; center is the analytics/CRM motion, not the record library. |
| Meeting Action-item Management | downstream | Consumes action items; does not hold the verbatim record. |
| Dictation / generic transcription tools | adjacent | Single-speaker dictation or batch audio→document conversion without meeting semantics or a meeting library. |
| Podcast/interview recording & editing | adjacent | Production-oriented (editing/publishing) vs record-of-record orientation. |

"Remove one leg" judgments:

- Remove the transcript → meeting recording vault (conferencing storage / plain recorder)
- Remove the recording/capture → live captioning or a human transcription service
- Remove the persistent library → one-shot transcription utility
- Remove the meeting/spoken-session framing → generic audio transcription
- Move the center to analytics/coaching/CRM → Conversation Intelligence Platform
- Move the center to human notes → Meeting Notes Application
- Move the center to AI-generated notes without the verbatim substrate → AI Meeting Assistant

Taxonomy tension (record for STATUS Boundary Issues): the three sibling leaves under 03.10 (Meeting Notes Application / Meeting Recording & Transcription Application / AI Meeting Assistant) are realized by the same small set of market products, all self-described "AI notetakers". The split is defensible only if each document holds a distinct center (human notes vs verbatim record library vs AI-derived notes/insights). Recommend joint review of the three leaves.

## Uncertainties

- tl;dv operational details (retention, consent mechanics, permission model, processing states) unverified — help center unreachable; only Tier 2 evidence used.
- Zoom's native recording/transcription specifics unverified (support portal unreachable); Teams substituted as the platform-native sample. Zoom's existence as a platform-native recorder is common knowledge but was not source-verified in this pass.
- End-user (non-admin) surface details for Teams are inferred from admin documentation only.
- Whether any sampled product supports transcription without any recording (Teams policy machinery suggests transcript-without-recording is possible platform-side) — not confirmed end-user-side; does not affect the L0 held here (standalone Type centers on the recording substrate).
- Market-wide default retention windows, consent-notice formats, and language counts vary and were not exhaustively compared.

## Final Synthesis

A Meeting Recording & Transcription Application is defined by three jointly-held structures: the captured meeting (a real spoken session held as a recording — audio at minimum, captured in-product or imported), the transcript (the session's speech rendered as text within the same record), and the retrievable meeting library (persistent, organized, searchable records the user returns to). Around this substrate, mature products add speaker attribution, timestamp-aligned playback, editing, highlights/clips, permissioned sharing, export/import, cross-meeting search, and — universally in the current market — an AI derived layer (summaries, action items, Q&A). Capture is multi-mechanism (bot, botless, platform-native, import) and consent-sensitive; processing is asynchronous; retention and permissions are governed. The Type's center is the verbatim record of what was said — not the meeting itself (conferencing), not human notes (Meeting Notes), not AI-generated notes as the primary object (AI Meeting Assistant), and not analytics over calls (Conversation Intelligence).
