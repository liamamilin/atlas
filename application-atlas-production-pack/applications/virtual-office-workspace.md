# Virtual Office Workspace

## Overview

A **Virtual Office Workspace** is a persistent virtual place that recreates a team's office as a navigable digital space — rooms, zones, and personal spots — where teammates appear continuously while they work, and live audio/video conversations form by co-location (entering the same room or moving near someone) rather than by dialing.

The defining structure is small:

```text
The persistent workplace-shaped place
└── Continuous embodied presence
    └── Co-location-initiated live conversation
```

Everything else commonly associated with the category — game-like maps, spatial audio, always-on video, desks, whiteboards, analytics — is widespread in current products but is not what makes the product a virtual office. An older-generation floor-plan product with nothing but rooms, avatars, and walk-over conversation is still fully recognizable as this Type; a product without the standing place, the continuous presence, or the co-location conversation mechanic is a different Type (a meeting tool, a chat tool, or a workspace container).

The category exists to solve a specific problem of distributed work: scheduled calls and async chat lose the ambient awareness of a shared office — who is around, whether they are free, and the ability to ask a quick question without scheduling. The virtual office restores that awareness by making the team's workplace itself the software.

## Users & Context

The primary user is a member of a remote-first, distributed, or hybrid team who "arrives" at the virtual office at the start of the workday and stays while working — the office runs as a background surface of daily work, not as an app opened per meeting.

Typical reasons to be in the product:

- sit at a personal desk and work with the office visible nearby
- see who is in, where they are, and whether they are free
- ask a quick question by walking over, without scheduling
- join a conversation happening nearby
- hold a planned meeting in a meeting room
- bump into colleagues informally (the "watercooler" role)

Secondary users:

- **administrators** — set up and maintain the office: layout, rooms, desks, membership
- **guests** — clients, candidates, or contractors who join for a meeting through a link or a check-in, without becoming members

The work environment is dominated by the desktop (browser or dedicated app); mobile apps exist in some products as companion surfaces. The product complements — rather than replaces — team chat and scheduled conferencing, though several products market themselves as reducing both.

## Core Model

### The Defining Core

```text
The persistent workplace-shaped place
└── Continuous embodied presence
    └── Co-location-initiated live conversation
```

Three properties. If any one is removed, the product is no longer recognizable as a virtual office:

- **The persistent workplace-shaped place** — the product's unit of record is a standing space structured as a workplace: partitioned into rooms and zones with office semantics (meeting rooms, common areas, team areas) and personal spots. The place persists across sessions and days — it is not created per meeting; users arrive at it. Its owners can shape it as a whole: add rooms, resize areas, arrange desks, change the layout. Without the standing place, the product is a meeting tool.
- **Continuous embodied presence** — each member appears in the place, at a position, while they work. Presence is visible (an avatar or representation), positioned (at a desk, in a room), and state-carrying (available, focused, away, in a meeting). The place answers, at a glance, who is in and where. Presence is ambient and continuous during the workday — not something that appears only when a call starts. Without continuous presence, the product is a presence list inside a chat tool.
- **Co-location-initiated live conversation** — live audio/video connections form because of shared location: enter the room where someone is talking and you are in the conversation; move near a colleague and you can speak; or use an in-place gesture (a wave, a knock, a "join me") that brings the other person's presence to you. The conversation belongs to the place, not to a dialed call object, and it ends when participants walk away. Without this mechanic, the product is explicit video calling.

### What the Place Contains

Beyond the defining core, a typical product's place is populated with:

- **Personal desks/spots** — a claimable or assigned personal location that serves as the member's home base: the spot colleagues look to find them, and a visible signal of being at work. In some products, seating new members near their teams is part of onboarding.
- **Meeting rooms** — named rooms for planned or private conversations, often bookable from a calendar so a scheduled meeting produces a link into a specific room.
- **Common areas** — informal spaces (lounges, coffee areas) where ambient social contact happens.
- **Work surfaces** — whiteboards, embedded documents and apps, and screen-sharing surfaces that attach to conversations where they happen.
- **Interactive objects** — decorative or playful items (games, music, themed furniture) that carry the office's culture.

### The People Layer

- **Members** — the team's standing population; they enter freely, hold desks, and appear in the place.
- **Guests** — outsiders admitted for a visit or a meeting through links or check-in, with restricted capabilities (typically: no desk, no decorating, sometimes requiring a member to let them in).
- **Status** — an availability layer over presence: free, focused/busy, away, in a meeting; in mature products, status can be driven by the calendar or by which work app the person is currently using.

### One Structure, Many Implementations

The core model is written in conceptual terms. Products realize each concept differently:

```text
Concept:   the place
Realized as:  game-like top-down map, schematic floor plan, video-tile space,
              multi-floor buildings, minimal room layouts

Concept:   co-location conversation
Realized as:  distance-based audio falloff, room-membership audio,
              spatial audio with multiple simultaneous conversations

Concept:   the in-place pull
Realized as:  "wave over", "knock on the door", "get/invite to join me"
              (the invited person's avatar walks to the inviter)
```

A reader who has only seen one implementation (for example, only game-map products) should still be able to recognize a schematic floor-plan product as the same Type from the core model.

## How It Works

### Set up the office

```text
Create the space (usually from a template)
→ shape the layout: rooms, team areas, desks, common areas
→ invite members (link or email; some products auto-admit by email domain)
→ seat people: members claim desks, or an admin assigns them
```

Setup is an administrative act done once and maintained as the team grows — the office is furniture, not a per-session artifact.

### Arrive for work

```text
Open the office (desktop app or browser)
→ appear at your desk (or wherever you position yourself)
→ set availability (or let calendar/app integration set it)
→ work with the office running nearby
```

Microphone and camera are off by default in typical products; being present does not mean being on camera.

### See and be seen

The office's map or list shows who is in, where they are, and their availability. This ambient awareness is the product's daily value: it replaces "are you free?" messages and removes the need to schedule quick conversations.

### Start or join a conversation

```text
See someone free (or hear a conversation nearby)
→ walk over / enter the room / wave them over / knock
→ audio (and optionally video) connects by co-location
→ others nearby can hear and join open conversations
→ participants leave → the conversation dissolves
```

For privacy, a conversation or room can be locked so others cannot hear or enter without permission; some desks and rooms are private by default.

### Hold a planned meeting

```text
Schedule from the calendar (or copy a room link)
→ attendees click into the named meeting room
→ meeting view (call-style) or stay in the office view
→ share screens (commonly several people at once), collaborate on whiteboards or embedded docs
→ lock the room if the meeting is private
```

Scheduled meetings live inside the same place as spontaneous conversation — that continuity (a meeting room sits next to the desks) is characteristic of the Type.

### Guard attention

Because presence is continuous, products expose attention controls: mute by default, focus/do-not-disturb states, notification settings for nearby conversations, and the ability to work "in" the office while listening only to what matters.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### The office space (primary surface)

The map or view of the place itself.

- shows the layout: rooms, desks, common areas, and the people in them
- primary actions: move (walk/click to a location), approach someone, enter a room, interact with objects
- carries presence: avatars, availability states, activity indicators

### Conversation surface

The live audio/video layer of a co-located conversation.

- participant video tiles or in-place video, audio controls, screen shares
- two typical postures: a focused call-style view, and a split view that keeps the office visible while talking
- primary actions: mute/unmute, camera on/off, share screen, lock the conversation, invite someone in

### People directory / office list

A list view of the place's population.

- who is in, where they are, their status and (in some products) current app
- primary actions: find a person, join them, invite them to join you

### Layout / customization editor

The administrative surface over the place.

- add/move/resize rooms and areas, place desks and objects, change templates
- typically admin-restricted; edits publish to everyone

### Membership & settings

- invite/remove members, manage guests, configure privacy and audio defaults, integrations (calendar, chat tools), notifications

## Important Rules / Behaviors

### Co-location is the conversation boundary

Who hears whom is determined by location: people in the same room (or near each other) are in one conversation; people elsewhere are not. This is the Type's defining behavior — it makes "walking over" the equivalent of starting a call, and it makes overhearing (and joining) open conversations natural. Locking a conversation or room overrides the default and makes it private.

### Presence is a communication channel

Being at your desk, being away, or being in focus mode communicates availability to colleagues without any message being sent. Status is therefore a first-class surface, commonly enriched from the calendar or from the work apps a person is using. Some products even reflect external calls: taking a call elsewhere can set the person's status to busy and visibly move them into a room.

### The place persists; conversations do not

The office, its layout, desks, and membership persist across days. Conversations are live and dissolve when they end — there is no conversation history as the unit of record (text chat exists as an auxiliary surface). This contrasts deliberately with messaging products, where the thread is the durable object.

### Guests are gated; members are free

Members move freely and hold desks; guests are admitted for visits and meetings through explicit mechanisms (links, check-in) with restricted capabilities. Membership administration (invite, seat, deactivate) is an administrative loop of the same standing place.

### Attention protection is structural

Because the office is always on, products treat muting, focus states, and notification control as structural settings rather than afterthoughts. Camera-on is never required by the model; presence without video is a supported, marketed posture.

## Variants

Common forms of the Type:

- **game-like spatial office** — a top-down, pixel-style map with a movable avatar (the most visible modern style)
- **schematic floor-plan office** — a drawn floor plan with rooms; participants click between rooms (the older-generation style)
- **video-spatial office** — presence and audio organized spatially around live video tiles
- **presence-first minimal office** — the office reduced to rooms and presence with little or no spatial rendering
- **education deployments** — the office shaped as a campus or classroom for schools and programs
- **community/event deployments** — the same place mechanics serving recurring communities or one-off events
- **function-specific floors** — sales floors and similar team-shaped spaces
- **scale variants** — from a small team's single room to large multi-floor buildings

A variant remains a variant unless it changes the core: if the space becomes one-off and public (an event for strangers) or the pedagogy becomes the product (classroom management), the product is drifting toward a different Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Team Workspace Platform | a persistent container assembling work surfaces (conversations, files, tools, meetings); its product is the assembly, its home surface is a stream/app rail — not a place with presence; remove the assembly from a virtual office and it is still a virtual office |
| Video Conferencing / Virtual Meeting Platform | the convened meeting is the unit: a session with its own address, joined by invitation; no standing place or ambient presence; a virtual office can host meetings as one behavior inside its rooms |
| Team Messaging Application | persistent async text threads are the unit; no live co-located conversation in a standing place; chat inside a virtual office is auxiliary |
| Collaborative Workspace | organizes natively authored content items in a governed container; no spatial presence or co-location conversation |
| Virtual Classroom | pedagogy machinery (class rosters, attendance, class control) is the center; education-shaped virtual offices remain this Type |
| Coworking / Flexible Workspace Management | manages physical flexible-workspace businesses; note that a "virtual office" there means an address/mail/phone service package — a business service, not this software Type |
| Digital Whiteboard | the canvas is the product; in a virtual office, whiteboards are surfaces serving conversations |
| Social VR / virtual event platforms | share spatial presence mechanics but center entertainment or one-off public events rather than a standing team workplace |

The sharpest seams are with Team Workspace Platform (container-of-surfaces vs place-of-presence) and Video Conferencing (convened session vs standing place) — the market sells both pairs as separate products, sometimes from the same vendor.

## Representative Products

- Gather
- Teamflow
- Kumospace
- Sococo
- oVice

The core model was checked against an older-generation product (Sococo's floor-plan generation) and a regional product (oVice) to avoid over-fitting the definition to the current game-map style. Tandem (self-labeled "a virtual office for remote teams") was sampled for positioning but its documentation was not reachable; no structural claims rest on it.

## Sources

Research date: **2026-09-09**

Primary vendor surfaces:

- Gather — knowledge base: https://support.help.gather.town/ (Studio Overview; Managing Desks & Where People Sit; Set Status & Availability; Desk Overview; Meeting Overview; Adding & Removing Members; Features collection) and product root: https://gather.town/
- Teamflow — product root: https://www.teamflowhq.com/
- Kumospace — product root: https://www.kumospace.com/ and Virtual Office page: https://www.kumospace.com/virtual-office
- Sococo — product root: https://www.sococo.com/ and https://www.sococo.com/why-sococo/
- oVice — product root: https://www.ovice.com/
- Tandem — product root (positioning only): https://www.tandem.chat/

> Sourcing limitation: official help-center/knowledge-base content was reachable only for Gather. Teamflow's knowledge base, Sococo's support center, oVice's help center, and Kumospace's help center were unreachable (404/403/timeout) and were abandoned after repeated failures; Tandem's site is script-rendered and yielded only its positioning title. Claims about those products are therefore calibrated to their official product pages, and precise operational details (audio falloff behavior, defaults, limits, plan gates) are intentionally not stated in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the joint reviews with the Team Workspace Platform and Virtual Meeting Platform passes) are recorded in the paired Research Notes.
