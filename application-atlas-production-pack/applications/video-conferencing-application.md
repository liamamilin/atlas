# Video Conferencing Application

## Overview

A **Video Conferencing Application** is a live multi-party audiovisual meeting service: it convenes a session that participants join through a shared address, in which they see and hear each other in real time, talk, present content, and collaborate as a group.

The defining structure is small:

```text
Convened addressable meeting
└── (meeting ID / join link / room address, distributed by invitation)
    └── Live real-time session
        └── Multiple participants, seen and heard together
            └── Shared stage: conversation + presented content
```

Everything else commonly associated with modern meeting products — host controls, screen sharing, chat, lobby admission, recording, breakout rooms, captions, virtual backgrounds, dial-in phone audio, calendar integration — is widespread in current products but is not what makes the product a video conferencing application. The room-system era of videoconferencing (dedicated room endpoints dialing each other through a bridge, with none of those extras) satisfies the same definition, and so does a bare open-source room joined by nothing more than a URL.

When the primary surface becomes an audio bridge with phone-keypad control, the product belongs to a different Application Type (Conference Calling Application). When the session becomes a one-to-many broadcast with registration and audience management, it belongs to another (Webinar Platform).

## Users & Context

The primary users are people who need to meet across distance — colleagues in an organization, teachers and students, external business parties, groups of any kind that must talk and look at shared material at an appointed time.

Typical reasons to open the application:

- convene a scheduled meeting with a distributed set of participants
- join a meeting someone else convened, from an invitation
- start an unscheduled meeting on short notice
- present or review material with a group while talking
- bring a physical meeting room into a remote participant's conversation

Roles inside a meeting are asymmetric. One participant convenes the meeting and typically holds host or organizer powers (admission, muting others, recording, assigning roles); everyone else joins as a participant with control over their own microphone, camera, and — where permitted — their ability to present. In organizationally deployed products there is a third layer above the host: administrators who set what meetings in their organization are allowed to do at all.

The work environment spans desktop and laptop computers, mobile devices, browsers, and physical conference rooms equipped with dedicated video devices. The same meeting is routinely joined simultaneously from all of these.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being recognizable as this Type:

- **The convened addressable meeting** — the session exists as an entity with its own address: a meeting identifier, a join link, a room name, or a room-system address. The meeting is created ahead of the live connection (scheduled) or on the spot (instant), and it is distributed to participants by invitation or link. Participants join the *meeting*, not a person. Without this, the product is person-to-person video calling.
- **The live real-time session** — while the meeting runs, participants exchange live audio and video. The visual meeting is the medium of record: what distinguishes this Type from audio conference calling is that participants see each other and a shared visual stage. Without this, the product is a conference call.
- **The multi-party shared session** — the meeting is a common space that mixes more than two simultaneous participants. Everyone in the session perceives the same shared situation: who is present, who is speaking, what is being shown. Without this, the product is a paired call.

### Standard Capabilities

Mature products carry most of the following. They are not what makes the product a video conferencing application, but they make meetings workable:

- **Host / organizer role** — the convening participant holds distinct powers: admitting or removing participants, muting others, controlling who may present or record, and assigning helper roles (co-hosts, co-organizers, presenters). In organizationally deployed products, administrators additionally shape what meetings may do through policies that sit above individual hosts.
- **Content sharing** — a participant presents their screen, an application window, or a document onto the shared stage. Conventionally one participant presents at a time, with the presenting role transferable during the meeting.
- **In-meeting chat** — text messages exchanged alongside the live audio and video, visible to participants in the session.
- **Participant roster** — the visible list of who is in the meeting, with names or avatars, speaking indicators, and per-participant state (muted, camera off, hand raised).
- **Pre-join preview** — before entering, the participant selects their microphone, speaker, and camera, chooses whether to join with audio and video on, and often sees themselves in a self-view.
- **Scheduling and invitations** — meetings are scheduled against calendars, and the invitation carries the join address; instant "meet now" meetings are the second convening mode. Many products also give each user a standing personal meeting address.
- **Admission control** — a lobby or waiting room the host admits people from, and/or a meeting password; the two are alternative implementations of the same gate.
- **Recording** — the host (or permitted participants) records the session; participants are shown that recording is in progress; the recording is stored in the product's estate and shared afterwards.
- **Layouts and self-view** — gallery or speaker-focused arrangements of participant video, plus the participant's own preview.
- **Multi-device clients** — desktop application, mobile application, and browser join for the same meeting.

The modern business tier commonly adds: breakout rooms (splitting the meeting into sub-sessions the host creates and manages), polls and reactions, live captions and transcription, and virtual backgrounds or background blur.

### One Structure, Many Implementations

The core model is conceptual. Specific products realize each concept differently:

```text
Concept:            The meeting's address
Implementations:    numeric meeting ID + password, one-click join link,
                    personal meeting room, bare room name in a URL,
                    room-system address (SIP URI / IP address + meeting number)

Concept:            Admission control
Implementations:    lobby/waiting room with host admission,
                    meeting password, authenticated-organizer requirement,
                    open room (no gate at all)

Concept:            The shared stage
Implementations:    screen/window/document share, remote-control handover,
                    built-in whiteboards and notes, embedded meeting apps

Concept:            Audio path
Implementations:    computer audio (default), dial-out "call me",
                    telephone dial-in with access code, no audio
                    (join for content only)
```

A reader who has only encountered one implementation — for example, link-joined cloud meetings — should still be able to recognize the room-system-era form (two endpoints dialing a bridge) and the open-source form (a named room on a self-hosted server) as the same Application Type.

## How It Works

### Convene the meeting

```text
Choose the mode
→ schedule against a calendar (title, time, participants, settings)
   or start instantly ("meet now")
   or use a standing personal meeting address
→ the product creates the meeting with its address
→ invitations go out carrying that address
```

Scheduling is the dominant mode for business meetings; instant meetings cover the unscheduled remainder. In organizationally deployed products, what a user may schedule and which meeting features exist are shaped by administrator policies before the host ever sets options.

### Join

```text
Receive the invitation (calendar entry, email, chat message, link)
→ open the join address
→ identity: sign in, or join as a guest with a display name
   (most products do not require an account to attend an invited meeting)
→ pass the gate: meeting password, lobby admission, or nothing
→ pre-join preview: choose audio path and devices,
   set camera and background
→ enter the live session
```

Participants join from computers, phones, browsers, or dedicated video devices. A participant may also join by ordinary telephone (audio only) where the product bundles dial-in audio; such participants hear the meeting but typically cannot see it or the shared content. Room video devices join by dialing the meeting's device-compatible address.

### Run the live session

```text
See and hear the other participants (gallery or speaker layout)
→ converse; mute/unmute and camera on/off remain personal toggles
→ a participant presents content onto the shared stage
   (one presenter at a time; presenting role can move)
→ participants chat, react, ask questions
→ the host manages the room: admit people from the lobby,
   mute a noisy line, remove a disruptor, assign presenter or co-host roles
→ optionally split into breakout sub-sessions and reassemble
```

The interaction loop is continuous and mutual: unlike a broadcast, every participant can take the floor, present (where permitted), and see the same shared state.

### End the meeting and what remains

```text
Host ends the meeting for all (or participants leave individually)
→ the live session ceases to exist
→ artifacts remain in the product's estate:
   the recording (if made), the meeting chat,
   attendance/participation records in organizationally deployed products,
   and in modern products AI-generated recaps or transcripts
→ recordings are stored, permissioned, and shared like other documents
```

The meeting itself is ephemeral; its artifacts persist. This is the opposite of the messaging Types, where the conversation is the durable object and the live call is the transient event.

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### Scheduling surface

Where meetings are convened.

- meeting title, time, recurrence, participant list, meeting options
- primary actions: schedule a meeting, start an instant meeting, open the personal meeting room
- in organizationally deployed products, administrator policy determines what is schedulable and which options exist

### Pre-join / preview screen

The gate between invitation and session.

- audio path choice (computer audio, call-me, dial-in, no audio), device selection, camera preview, background choice
- identity entry (sign-in or guest name), password entry where required
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
- host actions: admit, mute others, remove, assign roles, start recording, manage breakout rooms

### Chat panel

Text alongside the live session.

- messages to everyone or to individuals; files/links; in some products the chat persists after the meeting and is attached to it

### Post-meeting artifacts surface

Where the session's residue lives.

- recordings list with playback and sharing permissions; meeting chat history; attendance reports and recaps where offered

### Settings

Personal configuration: default devices, background, notifications, and in organizationally deployed products, visibility into what policies allow.

## Important Rules / Behaviors

### The invitation is the credential

Attendance normally requires the meeting's address plus whatever gate the host set — and most products explicitly allow joining an invited meeting **without an account**, as a guest identified only by a display name. The meeting address, not a membership relationship, is what confers access. This is a defining behavioral contrast with workspace- or contact-graph-based communication Types.

### Admission is gated, and the gate has variants

The same concept — controlling who enters — is implemented as a lobby the host admits from, a meeting password, a requirement that a designated organizer authenticate to open the room, or no gate at all. Lobby behavior interacts with identity: organizations commonly configure different admission rules for internal users, guests, trusted external organizations, anonymous participants, and telephone dial-ins.

### Roles gate powers

What a participant may do is a function of role. Hosts (and their delegates) admit, mute others, remove, record, and assign roles; presenters put content on the shared stage; attendees control their own audio and video. In organizationally deployed products, administrator policies sit above the host and can fix what any meeting in the organization may do — who can record, who can bypass the lobby, whether captions or transcription exist — with the host choosing within that envelope.

### One presenter at a time

The shared stage carries one presentation at a time; presenting is a transferable role rather than a free-for-all. This single-stream convention is what keeps a multi-party session legible.

### Audio path is a per-participant choice

Each participant independently chooses how they connect audio — computer, telephone call-back, telephone dial-in, or none (joining only to watch and share content, for example from inside a physical conference room). Dial-in participants are commonly audio-only: they hear the meeting but cannot see participants or shared content, and their phone connection may appear in the roster separately from their name unless they identify themselves.

### Recording is permission-gated and announced

Recording is restricted to the host and permitted delegates, may be further constrained by administrator policy or plan, and is visibly announced to participants while active. The recording lands in the product's storage estate with its own permission and retention behavior.

### Host muting is one-directional in some products

Where a host or moderator can mute other participants, some products deliberately do not let them force-unmute: the muted participant unmutes themselves. Control over one's own microphone is treated as personal, with the host holding collective-silence powers only.

### The meeting is ephemeral; artifacts persist

The live session has no life between its start and end. What survives is what the product stores: recordings, chat, attendance, recaps. Meetings are not places one returns to (that is the workspace or channel model); they are events that leave records.

## Variants

Common shapes of the Type:

- **Standalone meeting product** — meetings as the center, with light companions (chat, scheduling); the free-form consumer entry point.
- **Suite-embedded meetings** — meetings as one pillar of a communication suite alongside chat, calling, and documents; meetings inherit the suite's identity, calendar, and storage.
- **Open-source / self-hosted** — the meeting service operated by its users on their own infrastructure; the no-account, bare-room-address pole.
- **Room-system / hybrid-room deployments** — certified room devices and room-mode products that join the same meetings from physical conference rooms; device addressing (SIP/H.323-class) survives from the room-system era.
- **Webinar and large-event packaging** — the same media machinery packaged for one-to-many events with registration, presenter/attendee roles, and view-only audiences; in mature suites this is sold or configured as a separate mode or product line (see Webinar Platform).
- **Dial-in-audio bundles** — telephone dial-in and call-back attached to meetings as a licensed or plan-gated add-on (the conference-calling machinery riding on the meeting).
- **Compliance-grade deployments** — watermarks, sensitivity labels, enforced recording, retention and expiry rules for regulated organizations.
- **Industry tunings** — education (class rosters, waiting rooms for students), healthcare (consultation framing), government (sovereign deployment).

A variant remains a variant while the defining core — convened addressable meeting, live audiovisual session, multi-party shared stage — is intact.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Conference Calling Application | the audio bridge is the product there (dial-in numbers, access codes, keypad control); here the visual meeting is the medium of record. Modern products bundle both; remove the video and this Type collapses into that one, remove the audio bridge and that one collapses into this |
| Video Calling Application | calls are placed to a person through a personal contact graph and answered; here a convened meeting with its own address is joined by invitation. Both support 1:1 and group; the organizing object differs |
| Virtual Meeting Platform | nearest sibling leaf; the market phrase "virtual meetings" is used for ordinary meetings, so the boundary (container/umbrella vs the meeting-centric Type) deserves its own research pass |
| Webinar Platform | one-to-many broadcast with registration, audience management, and moderated Q&A; here the session is many-to-many mutual conversation. Large-meeting and view-only modes sit on this seam |
| Team Messaging Application | persistent conversation spaces with meetings as an in-space capability; here the live convened session is the product and chat is an in-meeting panel |
| Meeting Recording & Transcription Application | that Type's world is the record of the session (recording + transcript library), independent of which platform hosted it; here recording is one embedded, host-gated capability |
| Meeting Scheduling Application | that Type books the meeting (host-published availability, invitee self-booking); this Type runs it. The join link is the shared object across the seam |
| Virtual Classroom | same media, different purpose: instruction, class context, and assessment semantics rather than a convened meeting |
| Social Live Streaming Platform | broadcast to an audience of followers; here the participants are known invitees with mutual floor rights |
| Remote Customer Support Platform | support sessions carry consent machinery, support records, and endpoint control; meetings carry none of those |

The sharpest seam is with **Conference Calling Application**, because modern meeting products bundle both media. The test is the medium of record: strip the live video and shared visual stage, and what remains is conference calling; strip the audio bridge, and what remains is this Type.

## Representative Products

- Zoom (Zoom Meetings)
- Microsoft Teams
- Cisco Webex
- Google Meet
- Jitsi Meet

The sample deliberately spans product philosophies: a meeting-first standalone product, two suite-embedded enterprise platforms, a web-first suite service, and an open-source self-hostable service — so that the definition does not over-fit any one packaging, deployment model, or customer tier.

## Sources

Research date: **2026-09-09**

- Zoom — Meetings product page: https://explore.zoom.us/en/products/meetings/
- Microsoft Teams — Overview of meetings and events: https://learn.microsoft.com/en-us/microsoftteams/overview-meetings-events
- Microsoft Teams — Plan for Teams meetings: https://learn.microsoft.com/en-us/microsoftteams/plan-meetings
- Microsoft Teams — admin documentation hub: https://learn.microsoft.com/en-us/microsoftteams/
- Cisco Webex — Help Center / Getting started: https://help.webex.com/
- Cisco Webex — Get started with Webex Meetings for hosts: https://help.webex.com/en-us/article/nrebr3c
- Cisco Webex — Join a Webex meeting: https://help.webex.com/en-us/article/nrbgeodb
- Jitsi Meet — Handbook (introduction, user guide, start-a-meeting, FAQ): https://jitsi.github.io/handbook/

> Sourcing limitations: Google's documentation surfaces (support and product pages) were unreachable from the research environment on 2026-09-09 after repeated attempts, so no product-specific operational claims are made for Google Meet; it is retained as a representative product on market-position grounds only. Zoom's help center rendered no article content, so Zoom evidence is limited to its product page (positioning, feature inventory, plan structure) and no Zoom-specific operational defaults are asserted. Legacy room-system-era documentation was not directly reachable; the historical fit of the definition is argued structurally, supported by the surviving device-addressing (SIP/H.323-class) join path documented in one sampled product. Precise capacity and duration figures are plan- and product-dependent and are intentionally not stated in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
