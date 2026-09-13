# AI Meeting Assistant

## Overview

An **AI Meeting Assistant** captures what was actually said in a meeting and produces a machine-generated meeting record on the participant's behalf: a transcript of the conversation combined with AI-derived understanding — a summary, action items, and answers to questions about what was discussed.

It solves a specific problem: meetings produce information faster than participants can record it. Someone who is presenting, driving discussion, or joining back-to-back meetings cannot simultaneously take usable notes. The assistant attends or listens to the meeting in the user's place, and afterwards hands back a structured record the user can trust, search, share, and act on.

The defining core is small:

```text
Identified meeting occasion (a real, dated meeting)
└── Captured meeting content (what was actually said, ingested by the system)
    └── Machine-generated meeting record
        ├── faithful representation (transcript)
        └── AI-derived understanding (summary / action items / answers)
```

Three properties hold across the Type:

- **Bound to a real, identified meeting occasion.** The record's source of truth is an event that happened — dated, titled, attended. The assistant does not generate content from imagination; everything it produces traces back to the captured event.
- **Meeting capture as system input.** The system ingests the actual spoken event. The human does not author the source material. How the capture happens — a bot participant, the meeting platform's own feed, local device audio, or an uploaded recording — varies by product and is not part of the definition.
- **Machine-generated meeting record.** The system, not a human, produces both the faithful representation (transcript) and the derived understanding (summary, action items, answers). This is what makes it an *assistant*: the record exists because the system produced it, so the participant can be absent, inattentive, or simply free of note-taking.

If the derived-understanding layer is removed — leaving only a recording and verbatim transcript for later human reading — the product is a Meeting Recording & Transcription Application. If meeting capture is removed — the human writes the notes and the AI only formats them — it is a Meeting Notes Application. The capture-plus-understanding combination is the Type.

## Users & Context

The primary user is a working professional who spends much of the day in meetings and needs their contents to survive afterwards:

- **Individual contributors and managers** who attend internal meetings (stand-ups, planning, reviews) and need a reliable record without taking notes themselves.
- **Sales representatives and customer-facing teams** who run external calls and must keep CRM records and follow-ups current without manual effort.
- **Recruiters, consultants, researchers, journalists** for whom the exact wording of a conversation matters.

A second circle of users are **stakeholders who did not attend**: teammates who read the shared summary, managers who scan action items, colleagues who catch up on a meeting they skipped by asking the assistant questions about it.

Typical context: the assistant runs alongside the organization's existing meeting stack — a calendar (Google Workspace or Microsoft 365) and one or more meeting platforms (Zoom, Google Meet, Microsoft Teams, and similar). It is rarely the place where meetings happen; it is the place where meetings are remembered. Work is split between a brief setup (connect calendar, choose how meetings get captured), the meeting itself (usually hands-off), and a post-meeting pass (review, refine, share, push outputs into other tools).

## Core Model

### The Defining Core

```text
Meeting occasion
  → captured content
    → transcript (faithful record)
    → AI-derived understanding (summary, action items, answers)
  → delivered to the participant and their stakeholders
```

- **Meeting occasion.** A real event with a time, a title, and participants, usually known to the assistant through the calendar. Every record the assistant holds belongs to one occasion. This binding is what keeps the assistant honest: its outputs are claims about something that actually happened.
- **Captured content.** The spoken content of the occasion, ingested by the system. The ingestion mechanism is a variant (see below), but the invariant is that the source material is the event itself, not human-authored text.
- **Transcript.** The faithful, time-ordered representation of what was said, with speaker attribution. It is the grounding layer: summaries and answers are derived from it, and users fall back to it when they need exact wording.
- **AI-derived understanding.** The layer that makes the product an assistant rather than a recorder: a readable summary, extracted action items (often with suggested owners), and the ability to answer questions about the meeting. These outputs are generated, editable, and traceable back into the transcript.
- **Delivery.** The record is produced for the participant and made usable by others — shared directly, pushed into other tools, or queried by people who were never in the meeting.

### Standard Capabilities of Mature Products

These are not part of the definition, but a mature product carries most of them:

- **Calendar connection.** The assistant reads the user's calendar to know which meetings exist, when, and on which platform. This drives automatic capture and pre-meeting context.
- **Speaker identification.** The transcript labels who said what. Labels often start generic (the system may only distinguish "you" from "others") and are refined through speaker tags that the user or admin sets up; users can usually correct names afterwards.
- **Customizable summary formats.** Beyond a default recap, mature products let users define the structure of summaries — sections, detail level, role-specific templates (sales calls, one-on-ones, stand-ups) — so the output fits the workflow it feeds.
- **Action items with owners.** Extracted next steps, frequently auto-assigned to the people they concern, and usually linked back to the transcript passage they came from. Users can add, edit, reassign, or delete them.
- **Highlights and key moments.** Marked passages — set live during the meeting or afterwards — that let a reader consume the important parts without the full transcript.
- **Ask-the-meeting Q&A.** A chat surface where the user asks questions ("what did we decide about X?", "what are my action items?") and gets answers grounded in the transcript — for one meeting or across the whole library.
- **Meeting library.** A persistent, searchable archive of past meeting records, organized with folders, channels, or spaces, often with team-wide visibility rules.
- **Sharing and distribution.** Records can be shared with links and permissions, automatically sent to attendees, or delivered into chat channels and email.
- **Integrations.** Outputs flow into the surrounding toolchain: CRM updates from customer calls, task creation from action items, notes pushed to docs or wiki tools, automation platforms triggering on new meetings.
- **Team workspace and administration.** Shared workspaces with members, roles, admin controls over capture behavior, sharing defaults, retention, and security/compliance options.
- **Live mode.** During the meeting itself: live transcript, live summary, in-meeting questions, and highlight capture.

### One Structure, Many Implementations

The core model is conceptual. Products realize each piece differently:

```text
Concept:   Meeting capture
Implementations:
  - bot participant that joins the meeting as a visible guest
  - platform-native capture (the meeting platform's own assistant)
  - local device capture (desktop app reading system audio and microphone)
  - upload of an existing recording

Concept:   Speaker attribution
Implementations:
  - platform-provided speaker identity
  - browser-extension or client-based speaker tags
  - generic "you / others" labels refined by AI inference and manual correction

Concept:   Meeting record
Implementations:
  - transcript-first record with generated summary panels
  - note-first record (user's own notes enhanced by AI from the transcript)
```

A reader who has only seen one style — say, a bot that joins Zoom calls — should still be able to recognize a platform-native assistant or a notes-first local tool as the same Type from the core model.

## How It Works

### Set up capture

```text
Connect the calendar
→ the assistant learns the user's scheduled meetings
→ choose how each meeting gets captured
  (automatic bot join / platform-native notes / open the app to capture locally)
→ set defaults: which meetings to capture, who sees the results
```

Setup is the only step that requires decisions. Most products default to capturing calendar meetings on supported platforms, with controls to exclude meetings, stop automatic joining, or require manual starts.

### Capture the meeting

```text
Meeting starts
→ the assistant's capture mechanism engages
  (a bot appears as a participant, or the platform feed opens,
   or the local app starts listening to system audio and microphone)
→ speech is transcribed as the meeting proceeds
→ live surfaces may show the running transcript and summary
→ capture ends when the meeting ends
```

During the meeting the user normally does nothing. Some products allow the user to send the assistant to a meeting they cannot attend themselves, and to ask questions mid-meeting. Capture can fail for practical reasons: the meeting platform may restrict guest participants, audio may be misconfigured, or back-to-back meetings may blur into one another — which is why manual start/stop controls exist alongside automation.

### Generate the record

```text
Meeting ends
→ transcript is finalized with speaker attribution
→ summary, action items, and key points are generated
→ the record appears in the user's meeting library
→ optionally: auto-shared with attendees or pushed to connected tools
```

Generation is where the assistant earns its name. The transcript is produced first; the derived outputs — summary, action items, decisions, topics — are generated from it. Because they are generated, they are also editable: users correct speaker names, reword action items, adjust summaries, and in some products regenerate outputs after edits.

### Use and distribute the record

```text
Open the meeting record
→ read the summary; drill into the transcript where exact wording matters
→ ask questions about the meeting (or across all meetings)
→ refine: fix speakers, edit action items, add highlights
→ share with teammates or attendees
→ push outputs outward: CRM entries, tasks, chat posts, docs
```

Over time the library becomes a searchable memory of the user's meetings. The Q&A surface turns it into an answer source: questions about a single meeting or across months of meetings, answered from transcripts rather than re-watched recordings.

### Capability tiers

**Defining core** — without these, not an AI meeting assistant:

- binding to a real, identified meeting occasion
- system capture of the actual meeting content
- machine-generated transcript
- AI-derived understanding (summary, action items, answers)

**Standard in mature products:**

- calendar connection and automatic capture
- speaker identification with correction
- customizable summary formats
- action items with owners and transcript links
- highlights / key moments
- Q&A over one meeting and across the library
- persistent searchable library
- sharing, auto-share, and distribution
- integrations (CRM, tasks, chat, automation)
- team workspace with admin controls
- live in-meeting surfaces

**Variant / optional:**

- capture mechanism (bot / native / local / upload)
- in-person and mobile capture
- file upload of existing recordings
- conversation-intelligence analytics (talk time, sentiment, topics)
- consent and transparency tooling
- audio retention vs transcript-only posture
- compliance packaging (HIPAA agreements, private storage, data residency)

## Interfaces

### Capture surface

What the meeting sees. Either a **bot participant** — a named guest in the participant list that records the call — or **no visible participant at all**: platform-native capture inside the meeting client, or a desktop/mobile app listening to system audio and microphone. Products differ sharply here, and the difference is user-visible: a bot announces itself by existing; local capture may require the user to disclose it manually.

### Meeting record page

The center of the product. Typically split into:

- **Summary view** — the generated recap: short summary, action items with assignees, key points or outline. Primary actions: review, edit, reassign, add missing items, copy, share.
- **Transcript view** — the full time-ordered text with speaker labels, synced audio playback where the product keeps audio, highlights, comments, and search within the meeting. Primary actions: play, search, correct speakers, highlight, comment, edit text.

### Chat / Q&A surface

A conversational panel over the meeting — or over the whole library. Purpose: get answers and generate follow-up outputs (emails, recaps, task lists) without reading the transcript. Primary actions: ask a question, request a generated artifact, act on the answer.

### Library

The archive of past meeting records. Purpose: find and organize. Typical information: meeting title, date, participants, platform, summary preview. Primary actions: search, filter, organize into folders/spaces, open a record, manage sharing.

### Settings and administration

User-level: capture defaults (auto-join or manual), sharing defaults, summary templates, language, connected integrations, privacy choices. Organization-level (in team products): member management, capture policy, sharing and retention rules, security and compliance configuration.

## Important Rules / Behaviors

### Outputs are derived, and can be wrong

Summaries and action items are generated interpretations of the transcript, not ground truth. Mature products treat them as editable drafts: users correct speaker attribution, reword items, and add what the AI missed. A common pattern: the generated summary is fixed at generation time, while the chat surface can produce fresh answers that incorporate later edits — exact behavior varies by product.

### Capture is generally visible or disclosable

Recording a meeting involves other people. Bot-based products are inherently visible — the bot appears as a participant, and reputable products state that it cannot join invisibly. Bot-free and platform-native capture is less visible, which is why some products ship explicit transparency tools (automated chat notices to the meeting, watermarks on the user's video) and guidance to obtain consent. Meeting platforms themselves also carry recording notices. The practical rule: the assistant records real people, and the product family has developed visible-participation and disclosure mechanisms accordingly.

### The assistant acts on the user's behalf — within configured limits

Auto-join settings decide which meetings the assistant attends, including meetings the user themselves skips. This delegation is the point of the Type, but it is always scoped: per-meeting opt-outs, workspace policies, admin controls over who may capture what, and platform-level permission gates (for example, meetings that do not allow guest participants will not admit a bot).

### Capture has failure modes

The assistant depends on the meeting environment: guest restrictions on the meeting platform, audio routing problems, meetings that run over or end early, back-to-back sessions that can merge into a single record. Products therefore expose manual start/stop, per-meeting status, and troubleshooting surfaces alongside the automation.

### Retention and data posture vary materially

What is kept after the meeting differs by product and plan: some retain playable audio and video, others keep only the transcript and generated text, some offer auto-deletion of transcripts, private storage, or compliance agreements for regulated use. This is a real selection criterion between products, and it is governed by workspace policy in team settings.

### The record is event-bound

Everything in the library traces to a specific dated meeting. The assistant does not merge knowledge across meetings into a profile of its own accord (some products build directories of people and companies from meeting metadata, but the meeting record itself stays bound to its occasion). Cross-meeting reasoning happens on demand, through search and Q&A.

## Variants

- **Bot-based independent notetaker.** A standalone product whose bot joins meetings across Zoom, Meet, Teams, and similar platforms. Broadest platform coverage; the bot's visibility is the consent surface. (e.g. Otter.ai, Fireflies.ai)
- **Platform-native assistant.** The meeting platform's own assistant: capture is native (no external bot), outputs live inside the platform, and access is licensed with the platform. Extends to third-party platforms in some products. (e.g. Zoom's assistant with its note-taking feature)
- **Bot-free local capture.** A desktop app that listens to system audio and microphone; nothing joins the meeting. Often paired with a notes-first model where the user's own jotted notes are merged with the transcript by AI. (e.g. Granola)
- **Sales-focused assistant.** Capture plus CRM synchronization, deal-oriented summary formats, and follow-up drafting; overlaps with conversation-intelligence features such as talk-time and sentiment metrics. (e.g. Fathom; Fireflies' analytics layer)
- **Enterprise-governed deployment.** Admin-controlled capture policy, retention rules, private storage, compliance agreements, identity-provider sign-in, and transparency tooling deployed organization-wide.

A variant stays a variant while the defining core holds. When the primary object stops being the single meeting record — for example, when the product's center of gravity becomes org-scale analytics and rep coaching over thousands of recorded calls — it has become a Conversation Intelligence Platform.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Meeting Recording & Transcription Application | substrate | provides the recording + verbatim transcript for later human use; lacks the AI-derived understanding layer (generated summaries, action items, Q&A) that defines the assistant |
| Meeting Notes Application | adjacent | the human authors the notes; AI may format or enhance them, but the system does not capture the meeting event itself |
| Virtual Meeting Platform | host | hosts the meeting itself; may embed an assistant as a capability (platform-native variant), but its core object is the live meeting, not the generated record |
| Conversation Intelligence Platform | downstream / overlap | ingests many recorded calls and produces org-scale analytics, scorecards, and coaching; the assistant's object is the single meeting record and its immediate use |
| Meeting Action-item Management | downstream consumer | manages action items as tracked work objects with lifecycle and ownership across meetings; the assistant produces action items as one output among several |
| Meeting Scheduling Application | upstream | arranges the meeting on the calendar; the assistant consumes that calendar to know what to capture |
| AI Research Assistant / Answer Engine | different domain | answers from web or document corpora; no meeting capture and no binding to a real occasion |
| Enterprise AI Assistant | broader | general-purpose work assistant across many data sources; the meeting assistant is specialized to captured meetings as its source of truth |

The two most important boundaries: against **Meeting Recording & Transcription** (remove the generated-understanding layer) and against **Meeting Notes** (remove the capture of the event itself). The platform-native case is the subtlest: an assistant embedded in a meeting platform is still structurally an AI Meeting Assistant, but it ships as a capability of a Virtual Meeting Platform rather than a standalone product.

## Representative Products

- **Otter.ai** — bot-based, transcription-first notetaker with live summaries, Q&A chat, and workspace/enterprise tiers
- **Fireflies.ai** — team/enterprise notetaker with custom summary templates, search, conversation-intelligence analytics, and a broad integration set
- **Fathom** — free-first notetaker with bot and bot-free capture modes, sales/CRM orientation, and account-wide Q&A
- **Zoom (assistant / My Notes)** — platform-native assistant embedded in the meeting platform, extending to third-party platforms and in-person capture
- **Granola** — bot-free desktop notepad: local system-audio capture, user notes enhanced by AI, strong sharing/integration surface

The defining core was checked against all five capture philosophies (bot, platform-native, local, notes-first) to avoid defining the Type by any single mechanism.

## Sources

Research date: **2026-09-06**

- Otter.ai Help Center — What is Otter?; Conversation Page Overview; Otter Notetaker Overview — https://help.otter.ai/
- Fireflies.ai Knowledge Base — What is Fireflies.ai; What are your post-meeting features; Summaries collection — https://help.fireflies.ai/
- Fathom Help Center — Quick Start Guide; Getting Started; Using Fathom After a Call — https://help.fathom.video/
- Zoom — AI assistant product page (ZoomMate / My Notes) — https://www.zoom.com/en/ai-assistant/
- Granola Docs & Help Center — Granola 101; How transcription works — https://docs.granola.ai/

> Sourcing notes: all five products were researched from official documentation on 2026-09-06. Zoom's assistant was observed via its product page (marketing tier) rather than step-by-step support articles; claims about it are kept at positioning level. Vendor-stated counts (supported languages, integration counts) and numeric operational limits (timeouts, per-plan quotas) were deliberately excluded from this document. Detailed observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
