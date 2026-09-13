# Research Notes — AI Meeting Assistant

Research date: 2026-09-06

## Research Goal

Understand what an AI Meeting Assistant actually is as an Application Type: what it captures, what it produces, how the capture and generation loop works, what users do with the outputs, and where its boundary lies against neighboring Types (Meeting Recording & Transcription Application, Meeting Notes Application, Conversation Intelligence Platform, Virtual Meeting Platform, Meeting Action-item Management).

## Initial Boundary

Initial hypothesis (before research):

- Core use: a software agent attends or otherwise captures a real meeting on the user's behalf, then produces a machine-generated record (transcript + summary + action items) so the human does not have to take notes.
- Primary users: individual professionals (sales, recruiting, consulting, management) and teams.
- Nearest neighbors: Meeting Recording & Transcription Application (capture without AI understanding), Meeting Notes Application (human-authored notes), Conversation Intelligence Platform (org-scale analytics over recorded calls), Virtual Meeting Platform (hosts the meeting itself).
- Unknowns: whether the bot participant is definitional or just one capture mechanism; whether platform-native assistants (Zoom) belong to this Type; how far sales-focused products drift toward Conversation Intelligence.

## Research Questions

1. How does the meeting get captured? (bot participant / platform-native / local device capture / file upload)
2. What are the core objects? (meeting record, transcript, speaker, summary, action item, highlight, Q&A)
3. What happens during the meeting vs after it?
4. What AI outputs exist, and in what forms? (summaries, action items, decisions, answers)
5. What is the post-meeting workflow? (sharing, distribution, integrations, CRM/task sync, search)
6. What roles, permissions, and admin controls exist?
7. What rules and constraints matter? (consent/visibility, retention, privacy, data posture)
8. What variants exist? (individual vs team vs enterprise; general vs sales; bot vs botless)

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy | Tier | Documentation used |
|---|---|---|---|
| Otter.ai | Independent, transcription-first, bot-based notetaker; freemium | Individual / SMB / Enterprise | Help Center (Tier 1) |
| Fireflies.ai | Independent, team/enterprise workspace, integration-heavy, adds conversation intelligence | Team / Enterprise | Knowledge Base (Tier 1) |
| Fathom | Independent, free-first, sales-team oriented; bot and bot-free modes | Individual / Team | Help Center (Tier 1) |
| Zoom (ZoomMate / My Notes, formerly AI Companion) | Platform-native assistant embedded in the meeting platform | Enterprise / all Zoom tiers | Product page + support links (Tier 2) |
| Granola | Bot-free local capture; human notes enhanced by AI ("AI notepad") | Individual / Business | Docs & Help Center (Tier 1) |

## Sources

All fetched 2026-09-06.

### Otter.ai (Tier 1 — Help Center)
- https://help.otter.ai/ (home; categories)
- https://help.otter.ai/hc/en-us/articles/360035266494-What-is-Otter
- https://help.otter.ai/hc/en-us/articles/5093228433687-Conversation-Page-Overview
- https://help.otter.ai/hc/en-us/articles/4425393298327-Otter-Notetaker-Overview

### Fireflies.ai (Tier 1 — Knowledge Base)
- https://help.fireflies.ai/ (home; collections)
- https://help.fireflies.ai/collections/9407773578-intro_to_fireflies
- https://help.fireflies.ai/articles/1193528158-what-is-fireflies-ai
- https://help.fireflies.ai/articles/3891980883-what-are-your-post-meeting-features
- https://help.fireflies.ai/collections/9851200227-summaries
- Note: https://learn.fireflies.ai/ failed (transport error); help.fireflies.ai used instead.

### Fathom (Tier 1 — Help Center)
- https://help.fathom.video/ (home; categories)
- https://help.fathom.video/en/categories/74880-getting-started
- https://help.fathom.video/en/articles/276608 (Quick Start Guide)
- https://help.fathom.video/en/categories/65984-using-fathom-after-a-call

### Zoom (Tier 2 — product page; support portal linked)
- https://www.zoom.com/en/ai-assistant/ (ZoomMate product page, incl. My Notes, pricing tiers, FAQs)
- Support portal referenced: https://support.zoom.com/hc/en/ai-companion

### Granola (Tier 1 — Docs & Help Center)
- https://www.granola.ai/docs (redirects to docs.granola.ai)
- https://docs.granola.ai/llms.txt (documentation index)
- https://docs.granola.ai/help-center/getting-started/granola-101.md
- https://docs.granola.ai/help-center/taking-notes/transcription.md

## Product Observations

### Otter.ai (evidence layer A unless noted)

Positioning: "converts voice interactions into searchable, shareable smart notes"; Notetaker described as "AI meeting notetaker that automatically joins your Zoom, Google Meet, and Microsoft Teams meetings to record, transcribe, and capture your meetings in real time."

Capture:
- Calendar connection (Google or Microsoft) → meetings sync to Otter home → Notetaker auto-joins events containing a meeting link; manual add also possible.
- Notetaker joins as a visible guest participant; cannot join anonymously ("Notetaker cannot join a meeting anonymously or without appearing to other participants"). Consent/recording laws referenced.
- Botless alternative: Otter Desktop app records system audio without a bot participant.
- Mobile app for in-person recording; import of audio/video files for transcription; photos (whiteboards/slides) can be captured into the transcript.
- Auto-leave behavior: leaves after 12 continuous minutes of silence (5 minutes past scheduled end). [precise vendor number — research notes only]
- Workspace deduplication: one Notetaker per meeting for a workspace (enterprise).

Core objects (Conversation Page):
- Conversation = the meeting record. Two tabs: Summary and Transcript.
- Summary tab: AI-generated summary, AI-generated action items (auto-assigned to people; manual add/assign/rename/delete; "View in transcript" links back to source), Outline (live-generated top points).
- Transcript tab: keywords & speakers (with talk-time percentage breakdown), full editable transcript, highlights, comments, images, audio playback synced to text.
- Speaker management: tag speakers; summary cannot be regenerated with new speaker tags (workaround: Otter Chat).
- Otter AI Chat: ask questions of conversations; can generate alternative summaries/action items incorporating edits.

Organization & collaboration:
- Folders; share conversations with edit/comment/view permissions; auto-share settings; auto-share with same-domain users.
- Workspaces with seats; Enterprise admin controls; HIPAA offering; workspace admin logs.
- Integrations: Zoom, Google/Microsoft Calendar & Contacts, Slack, Salesforce, HubSpot, Dropbox, Zapier.
- Live features: live summary (Outline), Live Notes, AI Chat with Voice, automated slide capture.
- Positioning extensions: "AI Agents" for Sales / Recruiting / Education / Media (marketing-level; not researched in detail).

### Fireflies.ai (evidence layer A)

Positioning: "AI notetaker assistant that helps you capture, transcribe, summarize, and search meetings – all in one secure workspace."

Capture:
- Bot invited to live meetings on Zoom, Google Meet, Teams, Webex "and more".
- Chrome extension transcribes Google Meet calls from the browser.
- Desktop App records in-person meetings or system audio; mobile app for in-person; Web Recorder for offline/in-person meetings.
- Upload audio/video files for transcripts and summaries.
- Dialer integrations auto-sync recordings; other integrations (Dropbox etc.).
- Meeting Status Page: track processing state of meetings.

Post-meeting:
- Transcripts with speaker labels; vendor claims 100+ supported languages. [vendor-stated]
- AI summaries: key topics, action items, custom sections; view/customize/expand/regenerate; custom summary templates.
- Smart Search across meetings; AskFred (chat Q&A over meetings).
- Conversation Intelligence: talk time, monologues, sentiment, topics, trends.
- Notebook: organize meetings, tasks, contacts; Notepad for editing transcripts.
- Soundbites (clips) & playlists; comments; sharing; downloads.
- AI Skills: prebuilt templates (vendor claims 100+) for industry-specific summaries/insights/follow-ups/reports.
- Integrations: vendor claims 50+ apps — CRMs, PM tools, ATS, Slack.

Workspace & governance:
- Teams; Super Admin role; Enterprise plan; Private Storage option; security collection.

### Fathom (evidence layer A)

Positioning: free-first AI notetaker; "Fathom will be there, quietly working in the background, capturing the key moments."

Capture:
- Connect Google or Microsoft calendar → auto-join meetings and handle notetaking.
- Desktop app (Windows/Mac) recommended; Zoom app records within Zoom; Chrome extension; "Fathom Notetaker" bot joins Microsoft Teams meetings.
- New "bot-free experience": detects meetings automatically from calendar; user chooses capture method; no manual adding needed.
- Supports Zoom, Google Meet, Microsoft Teams.
- Settings: auto-record for all meetings; auto-share recaps/highlights to attendees; team visibility of external meetings.
- Onboarding connects the user to "the right CRM" (sales orientation).

Post-meeting (call recording page):
- Transcript (copy/paste; no direct download), AI summary (copy; customizable formats), recording download (MP4), delete, trim, share recordings.
- Highlights (in-meeting or post-meeting depending on experience version).
- Action Items with "Copy for Asana".
- Ask Fathom: Q&A over one call or account-wide (Premium/Team; usage limits announced).
- Auto-share recordings/summaries with attendees.
- MCP connection to Claude/ChatGPT.
- Dashboard lists all captured calls.

### Zoom — ZoomMate / My Notes (evidence layer A for product page; Tier 2)

Positioning: "ZoomMate analyzes, learns, and acts on your conversations"; assistant embedded in Zoom Workplace. (Formerly AI Companion; support portal still uses "AI Companion" paths. Rebrand observed 2026-09-06.)

Meeting-assistant capabilities observed:
- My Notes (AI note-taking): "captures insights from your conversations — on Zoom, in-person, on mobile, and across third-party platforms."
- Meeting summaries; in-meeting questions (ask during the meeting); custom meeting summary templates ("create your own formats, and ZoomMate will follow for recaps").
- Meetings use case framing: before (agendas, prep from past interactions) / during (My Notes captures content) / after (Salesforce updates, follow-up emails, drafting decks).
- Agentic search over transcripts, chats, docs, contacts; connected third-party sources (Salesforce, Jira, Google Drive, OneDrive).
- Workflows (templates, triggers), agents (pre-built + custom), AI Productivity Suite (Slides/Sheets/Paper/Canvas) — beyond the meeting-assistant core.
- Pricing: Basic (free) tier includes meeting summaries for 3 hosted meetings/month, in-meeting questions for 3 hosted meetings/month, AI note-taking for Zoom and third-party platforms (3 uses/month), AI queries (20/month); paid tiers add unlimited note-taking, custom summary templates, credits system. [precise vendor numbers — research notes only]

Structural significance: capture is native to the meeting platform (no external bot), and the assistant is a licensed capability of the platform rather than a standalone product. Extends to third-party platforms via My Notes.

### Granola (evidence layer A)

Positioning: "AI notepad" for meetings; desktop app (macOS/Windows) + mobile.

Capture:
- Calendar sync (Google/Outlook) → upcoming meetings listed; clicking a meeting creates a note; transcription starts only when the user opens the note (or via notification / New Note for ad-hoc calls).
- "There is no meeting bot — Granola runs only on your computer and uses your system audio and microphone."
- System audio + microphone capture; cannot isolate per-application audio; no audio/video recording is saved ("does not record or save audio or video at any point"); live transcription only — no file import/upload.
- Auto-stop on call-end detection, 15-minute audio inactivity, or sleep; back-to-back meetings can merge into one transcript (manual stop recommended). [precise vendor numbers — research notes only]
- Speaker tags via browser extension (Google Meet) or Zoom settings; otherwise "Me"/"Them" labels; AI infers speakers from context; user can correct names.
- Mobile app: face-to-face meetings and phone calls; Apple Watch start.

Record & generation:
- Note = the meeting record: user's own typed notes + AI enhancement ("Your notes guide the AI enhancement" — AI merges user's jotted points with transcript context into comprehensive notes).
- Templates (sales calls, 1:1s, stand-ups); pre-meeting briefs (open threads, context, agenda points); follow-up email drafting (transcript + calendar + past Gmail threads).
- Granola Chat: query across meetings, spot patterns, generate follow-ups; Workflows in Chat (draft email, send Slack, schedule events — with review step before anything is sent); Recipes (saved prompts).
- People and Companies: directory auto-built from meetings/calendar.

Organization & sharing:
- Spaces (My notes private vs team space) and folders; sharing controls; share to Slack/Notion; integrations (Zapier, HubSpot, Attio, Affinity); API, MCP (connect Claude/ChatGPT to notes), webhooks; CSV export.

Governance & privacy:
- Transparency features: automated chat message announcing transcription + "Granola Watermark" (virtual camera watermark); admin deployment guides.
- Transcript auto-deletion policy; model-training opt-out; SOC 2 Type 2; HIPAA BAA available; MDM deployment guides.

## Cross-product Comparison

| Dimension | Otter | Fireflies | Fathom | Zoom (ZoomMate/My Notes) | Granola |
|---|---|---|---|---|---|
| Bound to real meeting occasion | Yes | Yes | Yes | Yes | Yes |
| Machine-generated record | Yes | Yes | Yes | Yes | Yes (AI-enhanced note) |
| Transcript with speaker attribution | Yes (tagging, talk-time) | Yes (labels; 100+ languages claimed) | Yes | Yes | Yes (tags or Me/Them) |
| AI summary | Yes (+ live Outline) | Yes (custom sections/templates, regenerate) | Yes (customizable) | Yes (custom templates) | Yes (AI-enhanced notes, templates) |
| Action items | Yes (auto-assign + manual) | Yes | Yes (Copy for Asana) | Yes (post-meeting tasks) | Yes (via Chat/Recipes) |
| Q&A over meetings | Yes (Otter Chat) | Yes (AskFred, Smart Search) | Yes (Ask Fathom, account-wide) | Yes (in-meeting questions, agentic search) | Yes (Granola Chat) |
| Meeting library / organization | Yes (folders, workspaces) | Yes (Notebook, channels) | Yes (Dashboard) | Yes (in-platform) | Yes (notes, spaces/folders) |
| Search across meetings | Yes | Yes | Yes | Yes | Yes |
| Sharing / distribution | Yes (permissions, auto-share) | Yes | Yes (auto-share to attendees) | Yes | Yes (Slack/Notion/export) |
| Integrations (CRM/task/chat) | Yes | Yes (50+ claimed) | Yes (CRM, Asana, MCP) | Yes (Salesforce, Jira…) | Yes (CRM, Slack, Notion, Zapier, MCP, API) |
| Team workspace / roles | Yes (Workspaces, seats, admin) | Yes (Teams, Super Admin) | Yes (Team plans) | Yes (org admin) | Yes (workspaces, spaces, admin guides) |
| Calendar connection | Yes | Yes | Yes | Native | Yes |
| Bot participant capture | Yes (visible guest) | Yes | Yes (Teams bot; Zoom app) | No (native; My Notes covers third-party) | No (explicitly no bot) |
| Local/desktop capture | Yes (Desktop botless; mobile) | Yes (Desktop, mobile, Web Recorder) | Yes (Desktop bot-free) | Yes (in-person/mobile via My Notes) | Yes (desktop only for capture) |
| File upload / import | Yes (audio/video) | Yes (audio/video) | Not verified | Not verified | No (live only) |
| Conversation intelligence / analytics | Limited | Yes (talk time, sentiment, topics) | Sales-oriented features | Separate product line (Revenue Accelerator) | No |
| Consent / transparency surface | Visible bot + consent guidance | Not directly observed | Not directly observed | Platform recording notices (native) | Automated chat message + Watermark |
| Audio retention posture | Audio playback retained | Recordings retained | Recordings retained (MP4 download) | Platform recording posture | No audio stored (transcript only) |
| In-person meeting support | Yes (mobile) | Yes (mobile, Web Recorder) | Not emphasized | Yes (My Notes) | Yes (mobile, phone calls) |
| Live in-meeting surface | Yes (live summary/notes) | Yes | Yes (live highlights) | Yes (in-meeting questions) | Live transcript panel only |

### Cross-product commonalities (evidence layer B)

Observed across ≥3 of 5 products each:

1. Calendar connection as the scheduling-awareness layer (all 5).
2. Transcript as the faithful record, with speaker attribution needing setup or correction (all 5).
3. AI-generated summary as the headline deliverable (all 5), increasingly with customizable formats/templates (Fireflies, Fathom, Zoom, Granola).
4. Action item extraction with assignees (all 5).
5. Q&A / chat over the meeting or the meeting library (all 5).
6. Persistent meeting library with organization + search (all 5).
7. Sharing/distribution of the record (all 5).
8. Integrations pushing outputs into CRMs, task tools, chat tools (all 5).
9. Team/workspace tier with admin controls (all 5).
10. Multiple capture mechanisms per product (bot + desktop + mobile + upload in several).

### Capture mechanism is NOT definitional (key finding)

- Bot participant: Otter, Fireflies, Fathom (and explicitly rejected by Granola; absent in Zoom native).
- Platform-native capture: Zoom My Notes.
- Local device capture: Granola (only mechanism), Otter/Fireflies/Fathom (secondary), Zoom (in-person).
- File upload: Otter, Fireflies (secondary); Granola explicitly refuses.

All five still recognize as the same Type. Therefore capture mechanism is a variant dimension, not an invariant. The invariant is that the system ingests the actual meeting event (what was said) as source material.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

```text
Identified meeting occasion (a real, dated meeting)
└── Captured meeting content (what was actually said, ingested by the system)
    └── Machine-generated meeting record
        ├── faithful representation (transcript)
        └── AI-derived structured understanding (summary / action items / answers)
```

Three properties. Remove any one and the Type collapses into a neighbor:

- **Bound to a real, identified meeting occasion** — the record's source of truth is an event that happened (dated, titled, attended). Without this → generic AI assistant / note tool.
- **Meeting capture as system input** — the system ingests the actual spoken event (bot, native feed, local audio, or uploaded recording); the human does not author the source material. Without this → Meeting Notes Application.
- **Machine-generated meeting record with AI-derived understanding** — the system, not a human, produces both the faithful representation (transcript) and derived understanding (summary, action items, answers). Without the derived-understanding layer → Meeting Recording & Transcription Application.

The assistant posture is the consequence: the record is produced on the participant's behalf, so they can be absent, inattentive, or free of note-taking.

### L1 — Common Mature Structure

- Calendar connection / scheduled-meeting awareness (auto-join or meeting detection)
- Speaker identification / diarization with correctable labels
- Customizable summary formats / templates
- Action items with assignees, linked back to transcript evidence
- Highlights / key moments
- Ask-the-meeting Q&A (single meeting and across the library)
- Meeting library: persistent archive, organization (folders/channels/spaces), search
- Sharing & distribution (links, permissions, auto-share to attendees)
- Integrations: CRM sync, task tools, chat tools, automation platforms
- Team workspace with roles and admin controls
- Live mode (live transcript/summary during the meeting)
- Multiple capture mechanisms per product (bot + local + upload)

### L2 — Variant / Optional Structure

- Capture mechanism: bot participant vs platform-native vs local device capture vs file upload
- Scope posture: individual vs team vs enterprise
- Segment focus: general productivity vs sales (CRM sync, deal notes) vs recruiting/education/media
- Analytics depth: none → conversation intelligence metrics (talk time, sentiment, topics)
- Consent/transparency posture: visible bot vs manual disclosure tools (chat notice, watermark) vs platform-native recording notices
- Data posture: audio retention vs transcript-only; retention/auto-deletion policies; private storage; HIPAA/compliance offerings
- Platform coverage: which meeting platforms are supported
- Business model: free-first vs subscription vs bundled with platform license/credits
- In-person meeting support (mobile capture, phone calls)

### L3 — Vendor-specific (research notes only)

- Otter: "Notetaker" branding and display name; Otter Chat / AI Chat with Voice; Outline live summary; automated slide capture; silence auto-leave (12 min / 5 min past end); workspace deduplication; Sales/Recruiting/Education/Media "Agents"; HIPAA page.
- Fireflies: AskFred; Soundbites & playlists; Notebook/Notepad; AI Skills (100+ templates claimed); Voice Agents; Super Admin; Private Storage; Meeting Status Page; "100+ languages" claim.
- Fathom: free-first model with consumer-domain signup constraint (upcoming meeting required); bot-free experience upgrade path; Copy for Asana; Ask Fathom account-wide usage limits; MCP integration.
- Zoom: ZoomMate rebrand (formerly AI Companion); My Notes; AI credits economy; agentic search; workflows/agents; AI Productivity Suite (Slides/Sheets/Paper/Canvas); per-tier numeric limits (3 meetings/month etc.).
- Granola: notes-enhancement model (user notes guide AI); no audio storage; Me/Them default labels; Granola Watermark + automated chat notice; Recipes; pre-meeting briefs; follow-up emails from Gmail threads; People & Companies directory; transcript auto-deletion; Apple Watch.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model. Notably:

- Otter's silence auto-leave numbers, Zoom's per-tier numeric limits, Granola's 15-minute inactivity timeout: precise vendor numbers, kept out of the final document.
- Fireflies' "100+ languages" and "50+ integrations" are vendor-stated counts, not independently verified.
- Zoom's rebrand (AI Companion → ZoomMate) is recent; support documentation still references the older name in URLs.

## Boundary Findings

| Neighbor Type | Distinguishing test | Evidence basis |
|---|---|---|
| Meeting Recording & Transcription Application | Remove the AI-derived understanding layer (only recording + verbatim transcript for later human use) → that Type. The assistant's deliverable is machine-generated understanding, not just the verbatim record. | Structural; all 5 sampled products have the understanding layer as headline value |
| Meeting Notes Application | Remove meeting capture (human authors the notes; AI only formats/enhances human text) → that Type. Granola sits nearest this pole but captures the meeting's audio, so it remains an assistant with a notes-first interface. | Granola docs (capture is central); Otter "What is Otter" (notes framing but capture-driven) |
| Conversation Intelligence Platform | Shift the unit from the single meeting record to org-scale analytics/coaching over many recorded calls (aggregate metrics, rep scorecards) → that Type. Fireflies bundles CI features; Zoom sells CI as a separate line (Revenue Accelerator) — a gradient, not a wall. | Fireflies CI collection; Zoom product architecture |
| Virtual Meeting Platform | The platform hosts the meeting; the assistant consumes it. Platform-native assistants (Zoom My Notes) blur this: the assistant is a capability inside the hosting platform. The AI Meeting Assistant Type still describes the capability's structure; the hosting platform is a different Type that may embed it. | Zoom product page |
| Meeting Action-item Management | Action items are one output of the assistant; the dedicated Type manages them as tracked work objects with lifecycle/ownership across meetings. | Otter/Fathom action-item surfaces are record-local |
| AI Research Assistant / Answer Engine | Different source domain (web/documents vs meetings); no meeting capture. | Directory adjacency only |

"Remove what to become the neighbor" summary:

- Remove AI-derived understanding → Meeting Recording & Transcription Application
- Remove meeting capture → Meeting Notes Application
- Remove single-meeting focus, add org-scale analytics → Conversation Intelligence Platform
- Make the assistant a feature of the meeting host → capability inside a Virtual Meeting Platform (boundary observation, below)

## Boundary Issues (for STATUS.md)

1. **Platform-native assistants blur the Type boundary.** Zoom's assistant (ZoomMate/My Notes) is a licensed capability inside a Virtual Meeting Platform, structurally identical to standalone AI Meeting Assistants. The leaf remains valid (standalone products clearly exist), but the boundary with Virtual Meeting Platform is porous: meeting platforms increasingly bundle assistants. Recorded as observation; no taxonomy change made.
2. **Gradient to Conversation Intelligence Platform.** Team-oriented AI meeting assistants increasingly bundle conversation-intelligence analytics (Fireflies explicitly; Fathom for sales). The two leaves remain distinguishable by primary object (single-meeting record vs org-scale call analytics), but products span both.

## Historical / Market-Sample Check (§24)

- Would older products fit the L0? A conference-call recording + human transcription service (e.g., transcription bureaus) fails the "machine-generated understanding" test → correctly excluded (that is the Recording & Transcription lineage). A dictation tool fails "meeting capture" → excluded. Both exclusions are correct.
- Would older/regional AI meeting assistants fit? Early bot-based notetakers (pre-LLM, e.g., transcription bots) satisfy capture + machine transcript; if they lacked derived understanding they were Recording & Transcription products. The L0's "AI-derived understanding" is what makes the Type emergent rather than timeless — appropriate, since the Type itself is recent. The definition does not depend on any single capture mechanism (bot), platform, or business model, so it should survive mechanism shifts (e.g., platform-native capture replacing bots).
- Platform-native check: Zoom fits without a bot. Bot-free check: Granola fits without any server-side capture. Both confirm mechanism-independence.

## Uncertainties

1. Zoom rebrand recency: product page shows "ZoomMate" (formerly AI Companion); support articles still under AI Companion paths. Feature-level details of My Notes for third-party platforms not verified beyond the product page claim.
2. Fathom file-upload/import capability: not verified (not observed in fetched pages).
3. Consent/recording-notice behavior is largely governed by the meeting platform, not the assistant; only Granola's transparency tools and Otter's visible-bot + consent guidance were directly observed. Generalized claims about consent handling kept weak.
4. Fireflies language count and integration count are vendor-stated.
5. Enterprise admin depth for Fathom not researched (trust center exists but not fetched).
6. Whether "file upload" belongs in L1 or L2: observed in 2 of 5 products (Otter, Fireflies) as a secondary path; treated as common-but-not-universal (L1-adjacent, listed as optional in final doc).

## Final Synthesis

The AI Meeting Assistant is defined by a three-part invariant: it binds to a real, identified meeting occasion; it ingests the actual meeting content as system input (via bot, native feed, local capture, or upload — mechanism is variant); and it produces a machine-generated meeting record combining a faithful representation (transcript) with AI-derived structured understanding (summary, action items, answers), delivered on the participant's behalf.

Around this invariant, mature products converge on a common structure: calendar-driven meeting awareness, speaker attribution, customizable summaries, action items with assignees, Q&A over meetings, a persistent searchable library, sharing/distribution, integrations into CRMs/tasks/chat, team workspaces with admin controls, and live in-meeting surfaces.

Variation concentrates in: capture mechanism (bot vs native vs local vs upload), scope (individual/team/enterprise), segment focus (general vs sales vs role-specific), analytics depth, consent/transparency posture, data retention posture, and business model.

The Type's edges: without AI-derived understanding it is Meeting Recording & Transcription; without meeting capture it is Meeting Notes; at org-scale analytics it becomes Conversation Intelligence; embedded in the meeting host it is a capability of a Virtual Meeting Platform.
