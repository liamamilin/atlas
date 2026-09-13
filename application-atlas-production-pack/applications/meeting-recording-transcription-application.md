# Meeting Recording & Transcription Application

## Overview

A **Meeting Recording & Transcription Application** captures meetings and similar spoken sessions as recordings, converts what was said into transcripts, and holds recording and transcript together as persistent, retrievable records of each session.

The defining core is small — three structures held together:

```text
Captured session (a recording: audio at minimum, optionally video)
└── Transcript (the session's spoken content rendered as text)
    └── bound together as one Meeting Record
        └── accumulated in a retrievable Meeting Library
```

Each structure is load-bearing. Take away the transcript and the product is a voice recorder or a conferencing platform's recording storage. Take away the capture and it is a transcription service working on other people's files. Take away the persistent library and it is a one-shot conversion utility that turns audio into documents and forgets them.

Everything else the market associates with the category — bot participants that join calls, AI summaries and action items, video capture, calendar-driven automation, team workspaces, cross-meeting analytics — is a standard capability layered on this core, not what makes the Type. Older and simpler forms (a recorded meeting with a typed transcript filed per session) satisfy the core without any of them.

## Users & Context

Primary users:

- **Individual professionals** — consultants, journalists, researchers, students — who capture interviews, lectures, client conversations, and their own meetings because they cannot take verbatim notes while participating.
- **Team members and managers** who need internal meetings to survive beyond the room: attendees who want to re-check what was decided, and colleagues who missed the session entirely.
- **Customer-facing teams** (sales, customer success, support, user research) who keep records of customer conversations for handoffs, evidence, and review.
- **Administrators** in team and enterprise deployments, who govern who may record, where records live, how long they are kept, and who can see them.

The context of use is defined by where sessions happen: on video-meeting platforms, in physical rooms, over the phone. The application therefore operates alongside the session (a bot participant or a local recorder), inside the meeting platform itself (native recording and transcription), or after the fact (importing a recording file). The moment of value is almost always after the session ends — reviewing, searching, correcting, and sharing what was said.

## Core Model

### The defining core

Four concepts, three of them structural:

- **Captured session** — one real spoken session (a meeting, call, interview, or lecture) held as a recording. Audio is the invariant minimum; video is common. The recording may be captured by the application itself or imported from elsewhere; either way it becomes the record's media substrate.
- **Transcript** — the session's spoken content rendered as text and held as part of the same record. The transcript is the searchable, skimmable, quotable face of the record; the recording is its verifiable source.
- **Meeting record** — the persistent unit that binds the session's recording, transcript, and metadata (title, date and time, participants, source platform) into one identified entry. A record is created per session and outlives it.
- **Meeting library** — the accumulation of records, organized and searchable, that the user returns to over time. The library is what turns a sequence of conversions into a memory of what was said: it is the application's claim to being the place of record for meetings.

### Standard capabilities of mature products

These are widespread in current products and expected by the market, but they sit on top of the core rather than defining it:

- **Speaker attribution** — the transcript distinguishes who said what. Typically machine-detected voice separation plus human naming and correction of speakers.
- **Timestamp alignment** — transcript positions correspond to playback positions; selecting a line plays the recording from that moment.
- **Transcript editing** — the text and speaker labels can be corrected after the fact; the record is a working document, not a read-only output.
- **Highlights, comments, and clips** — users mark moments, attach comments, and cut shareable excerpts (clips, soundbites, snippets) directly from the record.
- **Sharing with permissions** — records are shared with individuals, teams, or links, under permission levels (typically at least view versus edit), revocable by the owner.
- **Export and import** — transcripts export as text formats and recordings as media files; recordings from other sources can be imported for transcription.
- **Search** — across the library (find the meeting) and within transcripts (find the moment).
- **AI derived layer** — automatically generated summaries, action items, and question-answering over one or many records. Near-universal in the current market, but derived from the record: earlier forms of the Type are complete without it.
- **Calendar-driven capture** — connecting a calendar so scheduled meetings are captured automatically or offered for one-click capture.
- **Team layer** — shared workspaces, organization containers (folders, channels, notebooks, team libraries), roles, and admin controls.

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:            Capture
Implementations:    bot participant joining the call; botless desktop/system-audio
                    capture; recording native to the meeting platform; import of
                    an existing audio/video file

Concept:            Recording medium
Implementations:    audio-only; audio + video; screen-share capture

Concept:            Transcript production
Implementations:    live transcription during the session; post-session processing;
                    (historically) human transcription from the recording

Concept:            Library
Implementations:    personal list with folders; team notebook; dashboard with a
                    team calls library; files stored inside the meeting platform's
                    storage

Concept:            AI derived layer
Implementations:    per-record summaries and action items; Q&A over one record;
                    Q&A and reports across many records
```

A reader who has only seen one shape — for example, a bot that joins video calls — should still be able to recognize the others (a phone app recording an in-person meeting, a platform's built-in recording with a transcript file) as the same Type.

## How It Works

### Capture the session

```text
Connect a calendar (or prepare a manual capture)
→ session starts
→ capture happens: a bot joins as a visible participant,
   or local capture records system/room audio,
   or the meeting platform records natively,
   or a recording file is imported afterwards
→ session ends; capture closes
```

Capture is deliberately multi-path because sessions happen in different places. The same product commonly offers several paths — a bot for platform meetings, a desktop recorder for in-person or botless capture, and file import for recordings made elsewhere.

### Processing

```text
Capture ends
→ the session is processed (asynchronously)
→ the record becomes available: transcript, aligned playback,
   and (in current products) AI-generated summary and action items
```

Processing is not instantaneous, and team-oriented products expose its state explicitly — a meeting may sit in a processing or failed state before its record is ready. Imported files go through the same pipeline.

### Work the record

```text
Open the record
→ skim the AI summary (if present) or the transcript
→ search within the transcript; jump to moments via timestamps
→ play back the recording while following the text
→ correct the transcript and speaker names
→ highlight key passages, attach comments, cut clips
→ collect action items
```

This is the loop the Type exists for: the record is not an archive cabinet but a working document that participants and absentees alike read, verify against the recording, and mark up.

### Share and distribute

```text
Choose the record (or an excerpt)
→ share with people, teams, or a link, under a permission level
→ or export: transcript as text, recording as media
→ or push derivatives to other tools (task items, CRM entries, chat)
```

Sharing an excerpt (a clip or snippet with its own link) is a common refinement: the recipient sees the moment, not the whole session.

### Return and retrieve

```text
Search the library by title, participant, or content
→ open past records; verify what was said against the recording
→ ask questions across records where the product offers it
```

Over time the library becomes the organization's or individual's memory of its spoken sessions — the reason records are kept rather than discarded after export.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Capture surfaces

- The **bot participant** appears in the meeting's participant list under an identifiable name; it can be admitted, removed, or blocked by meeting hosts and platform policies.
- The **local recorder** is a desktop or mobile surface with record/stop controls, used for in-person sessions or botless capture.
- The **import dialog** accepts audio/video files and queues them for the same processing pipeline.

### Meeting list / dashboard

The library's entry surface.

- lists records with title, date, participants, source, and processing state
- supports organization (folders, channels, notebooks, team libraries) and selection for bulk actions
- primary actions: open a record, search, share, delete, organize

### Meeting record page

The center of the product — where the record is read and worked.

- the transcript as the main body, with speaker labels and timestamps
- playback controls aligned to the text
- the AI summary and action items (where offered), alongside the transcript
- highlights, comments, and clip creation on transcript positions
- primary actions: search within the record, edit text/speakers, highlight, clip, share, export, delete

### Search

A first-class surface because the library's value is retrieval: search across titles, participants, and transcript content, jumping from a hit straight into the record at the matching moment.

### Sharing and settings

Permission controls per record (who can view, edit, export), link settings, auto-share rules (for example, sharing captures with meeting attendees or with a team library by default), and personal capture settings (which meetings are captured, by which mechanism).

### Admin console

In team and enterprise deployments: member and role management, capture policies, storage and retention governance, and security/compliance settings.

## Important Rules / Behaviors

### Recording is consent-sensitive

Capturing people's speech is legally and socially constrained, and the products carry that constraint in their behavior. Bots join as visible participants — they cannot hide. Products remind users to obtain any required consent and follow applicable recording laws. Platform-native implementations can go further: participant notification may be enforced by the platform, and administrators may require explicit participant consent before a person can be included in a recording or transcript. A compliance-recording variant inverts the usual posture entirely: recording happens automatically, without participant consent, owned by the organization for regulatory reasons.

### Capture depends on platform access

A bot is a guest in someone else's meeting platform. If the platform or the organization disallows guest participants or unapproved apps, the bot cannot join — capture then falls to local recording or native platform recording. Admin approval gates are a normal part of deploying these products inside organizations.

### Processing is asynchronous

Between capture and a usable record there is always a processing step. Users check status; failures are visible states, not silent losses. Metering often applies here: transcription minutes, storage, or credits are plan-limited resources in many products.

### The record is editable; derived outputs may not be

Transcripts and speaker labels are correctable working text. AI-generated summaries, however, are derived outputs: in some products a summary is generated once from the session and does not regenerate when the transcript is later corrected — the correction path is then to re-derive via the product's AI question-answering rather than the fixed summary. The general rule: the verbatim substrate is user-correctable; derived layers are regenerated only when the product explicitly supports it.

### Retention, expiration, and governance

Records are governed data. Team and platform-native implementations commonly support retention or expiration policies for recordings and transcripts, storage-location rules with inherited permissions, download restrictions, and legal-discovery access. In regulated deployments the record library is treated as part of the organization's records, not as personal files.

### Permissions gate the record

Visibility, editing, export, and re-sharing are separately controllable. A typical model distinguishes at least view-only from edit access, supports link-based sharing with scope limits, and lets owners revoke access. Team libraries add a second axis: whether a record is private, visible to a sub-team, or visible to the whole organization.

## Variants

- **Standalone bot-first recorder** — the dominant current shape: a cross-platform product whose bot joins meetings on the major video platforms, with local capture and import as secondary paths (e.g. Fireflies.ai, Otter.ai's notetaker mode).
- **Transcription-first personal tool** — descended from dictation-and-transcription; the individual's own recordings and imports are the center, with meeting capture as an extension (e.g. Otter.ai's original personal shape).
- **Video-first recorder** — emphasizes the video recording and visual excerpting: clips and reels built from transcript highlights, aimed at product, research, and customer-facing teams (e.g. tl;dv).
- **Free-forever notetaker** — the whole product free for individuals, monetizing teams; strong in sales-oriented deployments (e.g. Fathom).
- **Platform-native capability** — recording and transcription embedded in the meeting platform itself, governed by the platform's admin policies and stored in its storage (e.g. Microsoft Teams recording and transcription). The same three-part core, realized as a feature of the venue rather than a separate product.
- **Compliance recording** — organization-owned, automatically initiated recording without participant consent, via specialized integrations; the record exists for regulatory evidence rather than personal productivity.
- **In-person and mobile capture** — phone or desktop recorders for physical rooms, lectures, and interviews; the same capture→transcript→library loop without any meeting platform involved.

A variant remains a variant while the three-part core holds. When the center of gravity moves — to analytics and coaching over calls, to human-written notes, or to AI-generated notes as the primary object — the product is drifting toward a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| AI Meeting Assistant | closest sibling; heavy market overlap | The AI assistant's center is generated meeting content — notes, insights, answers. Here the center is the verbatim record (recording + transcript) held in a library; AI outputs are derived from it. Current market products realize both, which is why the boundary is drawn on the substrate, not the marketing. |
| Meeting Notes Application | sibling | Human-authored notes about meetings. No capture machinery and no verbatim substrate are required; the note exists because someone wrote it. |
| Video Conferencing Application | host / substrate | The conferencing product runs the meeting; recording and transcription are embedded capabilities within it. This Type's entire world is the record of the session, independent of which platform hosted it. |
| Conversation Intelligence Platform | downstream / adjacent | Adds analysis — talk time, sentiment, topics, coaching, CRM workflows — over recorded calls. The record library is its input, not its center. |
| Meeting Action-item Management | downstream | Consumes action items extracted from meetings; does not hold the verbatim record. |
| Dictation / generic transcription tools | adjacent | Single-speaker dictation or batch audio-to-document conversion, without meeting semantics or a persistent meeting library. |
| Podcast / interview recording and editing software | adjacent | Production-oriented: the goal is an edited, publishable artifact. Here the goal is the retrievable record of what was said. |

The boundary with **AI Meeting Assistant** is the most consequential one, because the current market sells one product under both descriptions. The structural test: is the verbatim capture library the substrate from which everything else is derived (this Type), or are generated notes and insights the product's primary objects (AI Meeting Assistant)?

## Representative Products

- **Otter.ai** — transcription-first archetype; personal-to-enterprise ladder; bot, botless, mobile, and import capture; conversation records with summaries, action items, and AI chat.
- **Fireflies.ai** — bot- and integration-first team product; wide platform coverage; notebook library, soundbites, AI summaries, and cross-meeting search.
- **tl;dv** — video-first recorder with clips and reels; product/research and customer-facing teams; EU security posture.
- **Fathom** — free-forever notetaker with a sales orientation; bot-free desktop capture plus bot and platform-app modes; team calls library.
- **Microsoft Teams (recording & transcription)** — the platform-native realization: recording and transcription embedded in the meeting venue, governed by organizational policy.

## Sources

Research date: **2026-09-08**

Official operational documentation (fetched 2026-09-08):

- Otter.ai Help Center — "What is Otter?", "Conversation Page Overview", "Otter Notetaker Overview", "Share a conversation" — https://help.otter.ai/
- Fireflies Knowledge Base — "What is Fireflies.ai", "What are your post-meeting features", and collection structure (Getting Started; Meeting Controls & Settings; Call Recording Rules; Migrations; Conversation Intelligence) — https://help.fireflies.ai/
- Fathom Help Center — Getting Started; "How to find your calls in Fathom"; Using Fathom After a Call — https://help.fathom.video/
- Microsoft Learn (Teams administrator documentation) — "Introduction to recording Microsoft Teams calls, meetings, and events"; "Overview: Recording and transcription for Teams meetings, events, and calls" — https://learn.microsoft.com/en-us/microsoftteams/

Official product pages (Tier 2):

- tl;dv — homepage and "Recordings & Transcriptions" feature page — https://tldv.io/ , https://tldv.io/features/meeting-recordings-transcriptions

> Sourcing limitations: the Zoom support portal could not be fetched (script-rendered content; two attempts), so Zoom was not used as a sampled source and Microsoft Teams was substituted as the platform-native sample. The tl;dv help center was unreachable (timeouts), so tl;dv observations rest on official product/feature pages only; product-specific operational details for tl;dv (retention, consent mechanics, permission model) are intentionally not asserted. Microsoft's end-user support article was unavailable; Teams observations come from administrator documentation. Precise numeric limits, retention windows, and default settings are deliberately not stated in this document; they remain, where known, in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
