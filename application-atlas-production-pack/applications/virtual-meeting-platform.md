# Virtual Meeting Platform

## Overview

A **Virtual Meeting Platform** is software for holding meetings online: it convenes a session with its own address, distributes that address to participants by invitation or link, and lets them join from wherever they are to see and hear each other in real time, talk, and work over shared content as a group.

One naming fact should be stated plainly: this is the same application the market usually calls a **Video Conferencing Application**. "Video conferencing" is the discipline and category term — it names the technology and the industry. "Virtual meeting platform" is the market's everyday phrase for the same product: the leading meeting vendor's own product URL is literally "virtual-meetings", and online-meeting vendors maintain dedicated "virtual meeting" pages describing exactly the audio-plus-video-plus-screen-sharing meeting. No separate product population answers to one label and not the other. Both directory entries describe one application from two angles — this document from the market-phrase angle — and readers should treat the two as one Type with two names.

The word "platform" carries three senses in the market, and none of them is a separate kind of software:

- the **meeting product itself** — the convened session and everything needed to run it (the sense used here);
- the **vendor suite** built around it — chat, phone, calendar, whiteboards, rooms, admin consoles packaged under one brand;
- the **embeddable API** — the same meeting machinery sold to other product builders as an SDK.

Everything commonly associated with modern meeting products — host controls, screen sharing, chat, lobby admission, recording, breakout rooms, captions, AI notes, dial-in phone audio, calendar integration — is standard or optional capability that mature products add, not what makes the product a virtual meeting platform. A bare named room joined by nothing more than a URL satisfies the definition; so does a scheduled conference dialed into by dedicated room devices.

The boundaries of the Type are held by three tests. Remove the convened, addressable meeting and what remains is person-to-person video calling. Remove the live video and what remains is conference calling. Replace mutual participation with a broadcast to a registered audience and what remains is a webinar platform.

## Users & Context

The primary users are people who need to meet across distance: colleagues in an organization, teachers and students, external business parties, distributed teams of any kind that must talk and look at shared material at an appointed time.

Typical reasons to open the platform:

- convene a scheduled meeting with a distributed set of participants
- join a meeting someone else convened, from an invitation or link
- start an unscheduled meeting on short notice
- present or review material with a group while talking
- meet clients, candidates, or patients in a scheduled session

Roles are asymmetric. One participant convenes the meeting and holds host or moderator powers: admitting or removing people, muting others, controlling who presents or records, assigning co-hosts. Everyone else joins as a participant with control over their own microphone, camera, and — where permitted — their ability to present. In organizationally deployed products a third layer sits above the host: administrators who manage users, set what meetings in their organization may do, and brand the service (custom domains, co-branded invitations, department-scoped meetings).

The work environment spans desktop and laptop computers, mobile devices, browsers, and physical conference rooms equipped with video devices — the same meeting is routinely joined simultaneously from all of these. A defining convenience of the Type is that participants usually need no account at all: the invitation is the credential.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being recognizable as this Type:

- **The convened addressable meeting** — the session exists as an entity with its own address: a meeting identifier, a join link, a permanent room URL, or a meeting key. The meeting is created ahead of the live connection (scheduled) or on the spot (instant), and it is distributed to participants by invitation or link. Participants join the *meeting*, not a person. Many products also give each user a standing personal meeting address or a set of persistent rooms.
- **The live real-time session** — while the meeting runs, participants exchange live audio and video. The visual meeting is the medium of record: participants see each other and a shared visual stage. Without this, the product is an audio conference call.
- **The multi-party shared session** — the meeting is a common space that mixes more than two simultaneous participants. Everyone perceives the same shared situation: who is present, who is speaking, what is being shown. Without this, the product is a paired call.

### What the Platform Holds Around the Meeting

Mature products carry most of the following. They are not what makes the product a virtual meeting platform, but they make meetings workable:

- **Convening machinery** — scheduling against calendars with invitations that carry the join address; instant "meet now" meetings; recurring meetings; standing personal rooms or named team rooms that can be joined at any time.
- **Host / moderator role** — the convening participant's distinct powers: admission from a lobby or queue, muting others, removing disruptors, locking the meeting, assigning presenter or co-host roles, starting recording.
- **Content sharing** — a participant presents their screen, an application window, or a document onto the shared stage; conventionally one presenter at a time, with the presenting role transferable.
- **In-meeting chat and reactions** — text, files, and emoji alongside the live audio and video.
- **Participant roster** — who is in the meeting, with speaking indicators and per-participant state (muted, camera off, hand raised).
- **Pre-join preview** — device selection (microphone, speaker, camera), audio-path choice, and background choice before entering.
- **Admission control** — a lobby the host admits from, a meeting password, a meeting lock, or an open room; alternative implementations of one gate.
- **Recording** — host-gated, visibly announced while active, stored in the product's estate (cloud) or locally, replayable and shareable afterwards.
- **Layouts and self-view** — gallery or speaker-focused arrangements of participant video.
- **Multi-device clients** — desktop application, mobile application, and browser join for the same meeting.
- **Collaboration surfaces** — whiteboards, notes, and file sharing inside the meeting.
- **AI layer (era-current)** — live captions and translation, transcription, AI-generated summaries and keynotes, AI note-taking.

### One Structure, Many Implementations

The core model is conceptual. Specific products realize each concept differently:

```text
Concept:            The meeting's address
Implementations:    numeric meeting ID + password, one-click join link,
                    permanent room URL, meeting key + password,
                    standing personal room, room-system address

Concept:            Admission control
Implementations:    lobby/waiting room with host admission, meeting password,
                    host-applied meeting lock, open room (no gate)

Concept:            The shared stage
Implementations:    screen/window/document share, remote-control handover,
                    built-in whiteboards and notes

Concept:            Audio path
Implementations:    computer audio (default), dial-out "call me",
                    telephone dial-in with access code, no audio
                    (join for content only)

Concept:            Recording venue
Implementations:    cloud storage in the product's estate, local recording
                    on the host's device
```

A reader who has only encountered one implementation — for example, link-joined cloud meetings — should still be able to recognize the permanent-room form (a named URL that always works), the key-and-password form, and the room-device form as the same application.

## How It Works

### Convene the meeting

```text
Choose the mode
→ schedule against a calendar (title, time, timezone, participants, agenda, settings)
   or start instantly
   or use a standing personal room / named team room
→ the platform creates the meeting with its address
→ invitations go out carrying that address
   (email invites, calendar entries, or a shareable link)
```

Scheduling is the dominant mode for business meetings; instant meetings cover the unscheduled remainder. In organizationally deployed products, the host may be assigned to someone else, co-hosts may be named in advance, and meetings may be scoped to a department. Recurring meetings repeat the same setup on a schedule.

### Join

```text
Receive the invitation (calendar entry, email, chat message, link)
→ open the join address
→ identity: sign in, or join as a guest with a display name
   (participants normally need no account — the link or key is the credential)
→ pass the gate: meeting password, lobby admission, meeting lock, or nothing
→ pre-join preview: choose the audio path and devices,
   set camera and background
→ enter the live session
```

Participants join from computers, phones, browsers, or dedicated video devices. A participant may also join by ordinary telephone (audio only) where the product bundles dial-in audio; such participants hear the meeting but typically cannot see it or the shared content.

### Run the live session

```text
See and hear the other participants (gallery or speaker layout)
→ converse; mute/unmute and camera on/off remain personal toggles
→ a participant presents content onto the shared stage
   (one presenter at a time; presenting role can move)
→ participants chat, react, ask questions, collaborate on a whiteboard
→ the host manages the room: admit people, mute a noisy line,
   lock the meeting, remove a disruptor, assign roles
→ optionally split into breakout sub-sessions and reassemble
```

The interaction loop is continuous and mutual: unlike a broadcast, every participant can take the floor, present (where permitted), and see the same shared state.

### End the meeting and what remains

```text
Host ends the meeting for all (or participants leave individually)
→ the live session ceases to exist
→ artifacts remain in the product's estate:
   the recording (if made), the meeting chat,
   attendance records, and in modern products
   AI-generated recaps, transcripts, or keynotes
→ recordings are stored, permissioned, and shared like other documents
```

The meeting itself is ephemeral; its artifacts persist. This is the opposite of the messaging Types, where the conversation is the durable object and the live call is the transient event.

### Capability tiers

**Defining core** — without these, not this Type:

- convened addressable meeting
- live real-time audiovisual session
- multi-party shared session

**Standard capabilities** — present in most mature products:

- convening machinery (scheduling, instant meetings, personal/team rooms)
- host/moderator role and controls
- content sharing (one presenter at a time)
- in-meeting chat, roster, pre-join preview
- admission control (lobby / password / lock)
- recording with notice
- layouts, multi-device clients, whiteboards
- AI captions, transcription, summaries (era-current)

**Optional / variant** — depends on product, plan, or deployment:

- dial-in telephone audio and call-back
- breakout rooms, polls, virtual backgrounds
- organization administration (users, policies, departments, custom domain, co-branding)
- browser-only delivery (no downloads)
- local vs cloud recording
- embeddable API/SDK delivery of the same meeting machinery
- webinar packaging of the same media machinery
- end-to-end encryption posture

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### Scheduling surface

Where meetings are convened.

- meeting title, date, time and timezone, duration, participant list, agenda, recurrence, meeting options
- primary actions: schedule a meeting, start an instant meeting, open the personal room or team rooms
- in organizationally deployed products, administrator settings shape what is schedulable and which options exist

### Pre-join / preview screen

The gate between invitation and session.

- audio path choice (computer audio, call-me, dial-in, no audio), device selection, camera preview, background choice
- identity entry (sign-in or guest name), password or key entry where required
- primary actions: configure and enter, or wait to be admitted

### The meeting stage

The live session's main surface.

- participant video in gallery or speaker-focused layout; self-view; speaking indicators
- persistent controls: mute/unmute, camera on/off, share, chat, participants, reactions, leave
- primary actions: take the floor, present content, send a chat message, raise a hand or react

### Content share surface

The shared stage while someone presents.

- the presented screen, window, or document; annotation or remote control where offered
- presenter controls (what is shared, stop sharing); viewer actions (request control, view fullscreen)

### Participants roster and host controls

Who is in the room and what the host can do about it.

- participant list with per-participant state; lobby queue awaiting admission
- host actions: admit, mute others, remove, lock the meeting, assign roles, start recording, manage breakout rooms

### Chat panel

Text alongside the live session.

- messages to everyone or to individuals; files and links; in some products the chat persists after the meeting and is attached to it

### Post-meeting artifacts surface

Where the session's residue lives.

- recordings list with playback and sharing permissions; meeting chat history; attendance reports; AI recaps, transcripts, or keynotes where offered

### Settings and administration

Personal configuration (default devices, background, notifications) and, in organizationally deployed products, the administrative layer: user management, meeting policies, department structure, custom domain, co-branded invitations.

## Important Rules / Behaviors

### The invitation is the credential

Attendance normally requires the meeting's address plus whatever gate the host set — and mature products commonly allow joining an invited meeting **without an account**, as a guest identified only by a display name, or by entering a meeting key and password. The meeting address, not a membership relationship, is what confers access. Hosts, by contrast, need accounts. This is a defining behavioral contrast with workspace- or contact-graph-based communication Types.

### Admission is gated, and the gate has variants

The same concept — controlling who enters — is implemented as a lobby the host admits from, a meeting password, a host-applied meeting lock, a requirement that a designated organizer authenticate, or no gate at all. The gate interacts with identity: organizations commonly configure different admission rules for internal users, guests, and anonymous participants.

### Roles gate powers

What a participant may do is a function of role. Hosts (and their delegates) admit, mute others, remove, record, and assign roles; presenters put content on the shared stage; attendees control their own audio and video. In organizationally deployed products, administrator policies sit above the host and can fix what any meeting in the organization may do — who can record, whether video is allowed at all, which meetings exist — with the host choosing within that envelope.

### One presenter at a time

The shared stage carries one presentation at a time; presenting is a transferable role rather than a free-for-all. This single-stream convention is what keeps a multi-party session legible.

### Audio path is a per-participant choice

Each participant independently chooses how they connect audio — computer, telephone call-back, telephone dial-in, or none (joining only to watch and share content). Dial-in participants are commonly audio-only: they hear the meeting but cannot see participants or shared content.

### Recording is permission-gated and announced

Recording is restricted to the host and permitted delegates, may be further constrained by plan or administrator policy, and is visibly announced to participants while active. The recording lands in the product's storage estate — or, in some products, on the host's device — with its own sharing behavior.

### The meeting is ephemeral; artifacts persist

The live session has no life between its start and end. What survives is what the platform stores: recordings, chat, attendance, AI recaps. Meetings are not places one returns to (that is the workspace or channel model); they are events that leave records. The standing personal room is the exception that proves the rule: the *room* persists, but it is an address, not a session.

## Variants

Common shapes of the Type:

- **Standalone meeting product** — meetings as the center, with light companions (scheduling, recording); the free-form entry point for individuals and small teams.
- **Suite-embedded meetings** — meetings as one pillar of a communication suite alongside chat, phone, mail/calendar, whiteboards, and room devices; meetings inherit the suite's identity, calendar, and storage.
- **Browser-native products** — the whole meeting runs in the browser with no downloads; guests join with one click from a permanent room link; popular where friction matters most (client sessions, telehealth, education).
- **Open-source / self-hosted** — the meeting service operated by its users on their own infrastructure; the bare-room-address pole.
- **Room-system / hybrid-room deployments** — certified room devices and room-mode products that join the same meetings from physical conference rooms.
- **Organizationally administered deployments** — user management, meeting policies, departments, custom domains, and co-branded invitations for regulated or large organizations.
- **Webinar and large-event packaging** — the same media machinery packaged for one-to-many events with registration, presenter/attendee roles, and view-only audiences; in mature suites this is sold or configured as a separate mode or product line (see Webinar Platform).
- **Dial-in-audio bundles** — telephone dial-in and call-back attached to meetings as a licensed or plan-gated add-on.
- **Embeddable delivery** — the same meeting machinery exposed as an API/SDK so other products can host meetings inside themselves; sold as a separate developer-facing product line by the same vendors.
- **Venue-adjacent packaging** — persistent spatial spaces (virtual offices) where people move between simultaneous meetings; the venue is a different Application Type (Virtual Office Workspace), and products that sell both keep the two as separate product modes.

A variant remains a variant while the defining core — convened addressable meeting, live audiovisual session, multi-party shared stage — is intact.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Video Conferencing Application | the same Application Type under the discipline/category name; this leaf records the market-phrase name. One product family, two directory names |
| Conference Calling Application | the audio bridge is the product there (dial-in numbers, access codes, keypad control); here the visual meeting is the medium of record. Modern products bundle both; remove the video and this Type collapses into that one, remove the audio bridge and that one collapses into this |
| Video Calling Application | calls are placed to a person through a personal contact graph and answered; here a convened meeting with its own address is joined by invitation. Both support 1:1 and group; the organizing object differs |
| Webinar Platform | one-to-many broadcast with registration, audience management, and moderated Q&A; here the session is many-to-many mutual conversation. Vendors keep the two distinct in their own product splits and FAQs |
| Virtual Office Workspace | a persistent spatial venue (floors, rooms, spatial audio) where people "walk the floor" between simultaneous meetings; the venue is the durable object there, the convened session here. Products increasingly sell both as separate modes |
| Virtual Classroom | same media, different purpose: instruction, class context, and assessment semantics rather than a convened meeting |
| Team Messaging Application | persistent conversation spaces with meetings as an in-space capability; here the live convened session is the product and chat is an in-meeting panel |
| Meeting Scheduling Application | that Type books the meeting (host-published availability, invitee self-booking); this Type runs it. The join link is the shared object across the seam |
| Meeting Recording & Transcription Application | that Type's world is the record of the session (recording + transcript library), independent of which platform hosted it; here recording is one embedded, host-gated capability |
| AI Meeting Assistant | that Type captures and understands meetings from the outside (or as a licensed capability inside the host); here the platform hosts the meeting itself and may bundle a native assistant. The boundary is porous by bundling, not by structure |
| Social Live Streaming Platform | broadcast to an audience of followers; here the participants are known invitees with mutual floor rights |

The sharpest seam is with **Conference Calling Application**, because modern meeting products bundle both media. The test is the medium of record: strip the live video and shared visual stage, and what remains is conference calling; strip the audio bridge, and what remains is this Type.

## Representative Products

- Zoom (Zoom Meetings)
- Zoho Meeting
- Whereby (Whereby Meetings)
- Kumospace (online meetings product)
- Livestorm (meetings mode)

The sample deliberately spans product philosophies and customer tiers: the market-leading suite platform, a suite vendor's standalone security-first meeting product, a browser-native embed-first challenger, a venue-adjacent suite's meetings product, and a webinar-first product's meetings mode — so that the definition does not over-fit any one packaging, deployment model, or customer tier. The venue family (virtual office / virtual event platforms) was checked against this leaf and found to self-label differently ("virtual office", "virtual and hybrid event platform"), confirming that it belongs to other Application Types.

## Sources

Research date: **2026-09-09**

- Zoom — Virtual Meetings product page (Zoom Meetings): https://www.zoom.com/en/products/virtual-meetings/
- Zoho Meeting — product homepage: https://www.zoho.com/meeting/
- Zoho Meeting — "Virtual Meeting: What it is, Types & Best Practices": https://www.zoho.com/meeting/virtual-meeting.html
- Whereby — homepage: https://whereby.com/
- Whereby — Meetings product page: https://whereby.com/information/meetings
- Whereby — Support Center: https://whereby.frontkb.com/en
- Kumospace — homepage: https://www.kumospace.com/
- Livestorm — homepage: https://www.livestorm.co/
- Airmeet — homepage (venue-family self-label check): https://www.airmeet.com/

> Sourcing limitations: GoTo Meeting's site returned an access error and was not used. Zoom's help center rendered no article content, so Zoom evidence is limited to its product page (positioning, feature inventory, plan structure) and no Zoom-specific operational defaults are asserted. Zoho's help-center articles were not retrievable; Zoho operational detail comes from its product pages. Precise capacity, duration, and pricing figures are plan- and product-dependent and are intentionally not stated in this document. The historical fit of the definition (pre-cloud "online meeting" / "web meeting" vocabulary) is argued from the vendors' own era-bridging terminology and structurally, not from fetched legacy documentation.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the alias resolution and the rejected alternative readings) are recorded in the paired Research Notes.
