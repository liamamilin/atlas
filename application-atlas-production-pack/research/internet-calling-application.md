# Research Notes — Internet Calling Application

## Research Goal

Identify the smallest stable invariant that defines the **Internet Calling Application** Type, and place every other observed feature at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

Evidence layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Internet Calling Application (directory section 01.03 Voice & Calling)

Nearest confusing Types:

- Softphone Application (same section)
- Push-to-Talk Application (same section)
- Conference Calling Application (same section)
- Virtual Phone Application (same section)
- Video Calling Application (section 01.04)
- Instant Messaging Application (section 01.01)
- Social Audio Platform (section 01.08)

Working hypothesis:

> An Internet Calling Application is a personal application whose central act is a real-time voice call between specific people, carried over the internet by the service itself rather than by the telephony voice channel.

The hypothesis is deliberately broader than "Skype-class standalone app" — the current market realizes the Type mostly inside messaging apps and platform-native surfaces.

## Research Questions

- What is the central object/act of this Type — the call, the line, the contact, or the number?
- How is the callee addressed across products and eras (service account, phone number, platform account, email)?
- What is the call lifecycle as products expose it (place → ring → answer/decline → active → end → logged)?
- What in-call controls and in-call capabilities are standard vs optional?
- Where does video fit — a separate Type, or an upgrade of the same call?
- Where does calling real phone numbers (PSTN breakout) sit — core or optional?
- How is the Type packaged (standalone app vs messaging-embedded vs platform-native)?
- Where are the boundaries with Softphone, Conference Calling, Push-to-Talk, Virtual Phone, and IM?

## Representative Products

| Product | Why selected |
|---|---|
| Skype | historical archetype of the standalone internet calling product; retired May 2025 — documented from Microsoft's own retirement and dial-pad support pages |
| FaceTime | platform-native calling; audio and video calls on one identity; deepest directly-reachable official documentation |

Products intended for the sample but **not reachable** on the research date (official help centers timed out; see Sources):

- Viber — standalone messaging+calling app with PSTN breakout ("Viber Out")
- WhatsApp — messaging-embedded calling; dedicated Calls tab
- Telegram — messaging-embedded calling

These are used only at the level of widely-attested structural facts, corroborated by the Instant Messaging research pass of 2026-09-05 (which directly recorded "voice/video call on the same identity" as a common mature structure across WhatsApp, Signal, Telegram, and WeChat). No precise operational details are claimed for them.

Historical / market-sample breadth (per `WORKFLOW_v1.1.md §24`), used for the §24 check, not for primary structural evidence:

- early Skype (2003-era) — Skype Name identity, contact list, free Skype-to-Skype calls, no phone number required
- Google Talk (2005-era) — Google account identity, voice chat initiated from a chat roster
- iChat AV (2003-era) — AIM/platform identity, audio (and video) chat between service users
- PC-to-phone internet-telephony clients (late-1990s pattern, e.g. Net2Phone-class) — account identity, calls placed to conventional phone numbers over the internet

## Sources

Research date: **2026-09-08**

Directly fetched (Layer A):

- Skype is retiring in May 2025: What you need to know — Microsoft Support: https://support.microsoft.com/en-us/skype
- How do I make a call in the Skype Dial Pad? — Microsoft Support: https://support.microsoft.com/en-us/skype/how-do-i-make-a-call-in-the-skype-dial-pad
- Use FaceTime with your iPhone or iPad — Apple Support: https://www.apple.com/facetime/ (redirects to the support article)
- FaceTime User Guide for Mac (macOS Tahoe) — Apple Support: https://support.apple.com/guide/facetime/welcome/mac
- Make and receive calls in FaceTime on Mac — Apple Support: https://support.apple.com/guide/facetime/make-and-receive-calls-in-facetime-fctm35828/mac
- Use FaceTime audio call features on Mac — Apple Support: https://support.apple.com/guide/facetime/use-facetime-audio-call-features-fctmb53ce460/mac

Not reachable (repeated timeouts on 2026-09-08; abandoned after 2 attempts each per the network rule):

- Viber — https://www.viber.com/en/ , https://help.viber.com/hc/en-us , https://www.viber.com/en/features/
- WhatsApp — https://faq.whatsapp.com/ , https://www.whatsapp.com/
- Telegram — https://telegram.org/faq , https://telegram.org/tour , https://telegram.org/blog/calls

Per `WORKFLOW_v1.1.md §23 Source-access Limitation`:

> 1. record the limitation in Research Notes ✓
> 2. reduce assertion strength ✓
> 3. avoid precise workflow/rule claims that depend on inaccessible evidence ✓
> 4. do not compensate by silently filling detail from model memory ✓

Consequence: the directly documented sample is two products (Skype, FaceTime) with deliberately different philosophies (standalone cross-platform archetype vs platform-native). Messaging-embedded calling is asserted only as qualified cross-product commonality, corroborated by the IM research pass of 2026-09-05. Precise numbers (e.g. FaceTime's documented group-call participant cap) are kept in these Research Notes and excluded from the final document.

## Product Observations

### Skype (Layer A — from Microsoft's retirement and dial-pad support pages)

- Layer A: Skype is retired as of May 5, 2025; Microsoft's own FAQ describes its core as "one-on-one and group calls, messaging, and file sharing", with contacts, chats, and **call history** transferring to Teams Free when signing in with Skype credentials.
- Layer A: identity is the Skype account ("Skype credentials"); no phone number is required for Skype-to-Skype calling.
- Layer A: paid calling services existed alongside free app-to-app calling: Skype Credit and calling subscriptions for international/domestic calls, the **Skype Dial Pad** for calling landlines and mobile numbers (enter or select a phone number → Call), **Skype Numbers** for receiving calls from conventional phones, plus SMS, call forwarding, voicemail, and caller ID setup — all listed as retired services.
- Layer A: the dial pad is a number-addressed surface, distinct from the person-addressed contact surface; it required an active subscription or credit.
- Layer B observation: the Skype pattern (free service-to-service calling as the core, metered PSTN breakout as an optional paid layer) matches the classic standalone internet-calling archetype.

### FaceTime (Layer A — Apple Support, iOS article + Mac User Guide)

- Layer A: making a call — New Call button; type a name and pick from Contacts (the person's phone number or email saved in Contacts); tap the **Audio** button or the **FaceTime** (video) button. Calls run over Wi-Fi or cellular data.
- Layer A: identity — sign-in with an Apple Account; FaceTime connects "using any FaceTime-enabled numbers or addresses stored for that person". The callee is a person in Contacts, not a dialed number.
- Layer A: answering — Accept; when already on a call: **End & Accept**, **Hold & Accept**, or Decline; a video call can be answered **as audio** (camera off). Calls can be answered even when the app is not open (notifications).
- Layer A: declining — decline, reply with a message, create a callback reminder, or send an audio call to voicemail (with live transcription on the caller's screen in the documented iPhone flow).
- Layer A: in-call — Add People (adds participants to the current call), Contact Card, Live Captions, Live Translation, Hold Assist, Screen Sharing, SharePlay; audio-call recording with transcript (stored in the Notes app); move the call to another device.
- Layer A: call history — a filterable log: Calls (recent video and audio calls), Missed, Video messages, Voicemail, Unknown Callers, Spam, plus Manage Filtering; actions include returning recent/missed calls, deleting history entries, and blocking callers.
- Layer A: group calls — enter each person's contact information in the To field; Apple documents a participant cap of 32 for Group FaceTime (product-specific number; kept out of the final document).
- Layer A: FaceTime Links allow starting or joining a call via a link (a meeting-like joining surface).
- Layer A: the Mac guide distinguishes FaceTime calls (internet) from Phone-app calls (cellular minutes) — the transport distinction is explicit in Apple's own documentation.

### Messaging-embedded calling (Layer B — reduced strength; official docs unreachable)

- Layer B (corroborated by the IM research pass of 2026-09-05, which directly recorded this across WhatsApp, Signal, Telegram, WeChat): mature messaging products commonly offer voice and video calls placed to a contact on the same identity as the text thread; the call is logged against the contact/thread.
- No precise claims (call quality modes, limits, encryption specifics) are made for these products on this research date.

### Historical / market-sample breadth (§24 check)

- Early Skype (2003-era): Skype Name identity, contact list, free Skype-to-Skype voice calls. Fits the hypothesized core without phone numbers, dial pads, voicemail, or video.
- Google Talk (2005-era): voice chat from a chat roster on a Google account identity. Fits.
- iChat AV (2003-era): audio/video chat between service users on AIM/Mac identities. Fits.
- PC-to-phone internet-telephony clients (late-1990s pattern): account identity and internet-carried calls, but the callee is a phone number rather than a service person. Fits only partially — the "reachable specific people" leg is realized as a number dialer. Treated as a breakout-first variant pole, not the canonical center.

The historical check passes: none of the older samples require phone-number identity, dial pads, voicemail, video, or group calls. The core survives all of them.

## Cross-product Comparison

| Finding | Skype | FaceTime | Messaging-embedded (B) | Historical samples | Abstraction level |
|---|---|---|---|---|---|
| personal in-service calling identity | yes (Skype account) | yes (Apple Account) | yes (messaging identity) | yes (Skype Name / Google account / AIM) | L0 |
| call target is a specific known person from a people surface | yes (contacts) | yes (Contacts / recents) | yes (contacts) | yes | L0 |
| real-time stateful call (place → ring → answer/decline → active → end) | yes | yes (documented in detail) | yes | yes | L0 |
| live two-way audio carried over the internet by the service | yes | yes (Wi-Fi/cellular data; distinct from cellular-minutes phone calls) | yes | yes | L0 |
| call log / recents with missed calls | yes (call history transfers) | yes (Calls/Missed filters) | yes (logged to contact/thread) | varies | L1 |
| contacts / people surface as reachability graph | yes | yes | yes | yes | L1 |
| in-call controls (mute/end-class; hold documented) | yes | yes (End & Accept / Hold & Accept) | yes | basic | L1 |
| video upgrade of the same call | yes | yes (video call; answer-as-audio) | yes (common) | iChat AV yes | L1 |
| group/multi-party call | yes (group calls) | yes (Add People; Group FaceTime) | yes (common) | varies | L1 |
| ringing/missed states + notifications | yes | yes (answer when app closed) | yes | varies | L1 |
| PSTN breakout (dial pad, credit, numbers) | yes (paid layer) | no (phone calls via iPhone continuity are a different mechanism) | some products (qualified) | PC-to-phone era yes | L2 |
| presence / availability status | yes (historically) | no presence surface documented | yes (via messaging layer, qualified) | yes (early IM) | L2 |
| voicemail | yes (retired paid service) | yes (documented) | not asserted | no (early) | L2 |
| call filtering / unknown callers / spam | not asserted | yes (documented) | not asserted | no | L2 |
| call recording + transcript | not asserted | yes (documented) | not asserted | no | L2 |
| captions / translation / screen share / co-watching in call | not asserted | yes (documented) | not asserted | no | L2 |
| move call across devices | not asserted | yes (documented) | not asserted | no | L2 |
| join-by-link call surface | not asserted | yes (FaceTime Links) | not asserted | no | L2 |
| encryption posture | varies | varies | varies | no (historical) | L2 |
| identity substrate: service account / platform account / phone number | service account | platform account + numbers/addresses | phone-number common (qualified) | service accounts | L2 |
| branded paid services (Credit, Numbers, Manager, caller ID, SMS) | yes | no | n/a | no | L3 |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as an Internet Calling Application:

```text
Personal Calling Identity
└── Reachable specific people (contacts / recents surface)
    └── Real-time voice call as a stateful event
        (place → ring → answer/decline → active → end)
        └── Live two-way audio carried over the internet by the service
```

Four properties:

1. **Personal calling identity** — each participant is individually addressable in the service's identity space.
2. **Reachable specific people** — the call target is a specific known person drawn from the application's own people surface (contacts, recents), not a public room, a scheduled bridge, or a random pairing.
3. **The call as a stateful real-time event** — it is placed, rings, is answered or declined, is active while both parties are simultaneously present, and ends. Synchronous co-presence is what separates a call from an async voice message.
4. **Live two-way audio over the internet** — the medium and the transport: the service itself carries the call, rather than the telephony voice channel.

Removal tests:

- remove *personal calling identity* → anonymous or room-based audio (Social Audio Platform territory)
- remove *reachable specific people* → scheduled dial-in bridges (Conference Calling) or random pairing (Random Video Chat)
- remove *the stateful real-time call* → asynchronous voice messaging (an IM capability, not a call)
- remove *live audio over the internet* → a telephony dialer, not internet calling

## L1 — Common Mature Structure

Common in mature products; not required to recognize the Type:

```text
Call log / recents (incoming, outgoing, missed; return-a-call action)
Contacts / people surface as the reachability graph
In-call controls (mute, end; hold-class handling of a second incoming call)
Video upgrade of the same call (video call; answering a video call as audio)
Group / multi-party call (adding people to a live call)
Ringing / missed states with notifications (answering when the app is closed)
```

A product can be a full member of the Type without any of these (early text-era voice chat had no video, no group calls, thin logs), but a typical modern product carries most of them.

## L2 — Variant / Optional Structure

```text
Packaging (the dominant variant axis)
- standalone cross-platform app (the Skype-class archetype; retired in 2025)
- platform-native calling (identity from the platform account; device-integrated)
- messaging-embedded calling (calls on the messaging identity; the current market's center of gravity)

Identity substrate
- service account (Skype Name pattern)
- platform account + registered numbers/addresses (Apple Account pattern)
- phone-number identity (common in messaging-embedded products — qualified)

PSTN breakout
- dial pad + prepaid credit/subscriptions + inbound virtual numbers (the Skype pattern)
- absent entirely (platform-native pattern)
- breakout-first clients (late-1990s PC-to-phone pattern; partial fit)

Presence / availability status (some products; platform-native sample has none)
Encryption posture (varies by product)
Voicemail (telephony-inherited; present in some products)
Call filtering / unknown-caller / spam handling
Call recording + transcript
In-call extras: captions, translation, screen sharing, co-watching
Device handoff (moving a live call between one's own devices)
Join-by-link call surfaces (drift toward meeting semantics)
```

## L3 — Vendor-specific Structure

- Skype: Skype Credit, Skype Numbers, Skype Manager, caller ID setup, SMS connect, call forwarding, the Skype Dial Pad web portal (calling.web.skype.com), the migration path into Teams Free, the 60-minute Skype-calls benefit in Microsoft 365 subscriptions.
- FaceTime: Group FaceTime participant cap (32, per Apple's documented Mac flow), FaceTime Links, SharePlay, Hold Assist, Live Voicemail transcription, call recordings stored in the Notes app, RTT calls, iPhone-continuity phone calls, Live Translation.
- Specific numeric limits, protocol names, and quality-adaptation mechanics for all products.

These remain in Research Notes; they do not enter the Application Document.

## Canonical Model (v1.1)

```text
L0
Personal Calling Identity
└── Reachable specific people (contacts / recents)
    └── Real-time voice call (stateful event, synchronous co-presence)
        └── Live two-way audio over the internet
```

Everything else is L1 or lower.

## Boundary Findings

### vs Softphone Application

- The softphone's core object is a **telephony line**: a SIP account registered to a PBX or telephony service; its surface is dialpad-first with desk-phone semantics (extensions, transfer, hold/park, DND, corporate directory); its calls ride the organization's telephony system.
- The internet calling application's core object is the **person**: no line registration, no extension semantics; calls ride the consumer service.
- Boundary test: remove the line/PBX registration and desk-phone semantics from a softphone → an internet calling application. Give an internet calling application a registered corporate line → it is being used as a softphone.

### vs Video Calling Application

- Both Types share the same call object (identity → person → stateful call). The differentiator is the **primary medium**: voice-first with video as an upgrade (this Type) vs video-first (Video Calling Application).
- The seam is genuinely straddled by real products: FaceTime is video-first historically yet documents audio calls as a first-class mode; messaging-embedded products expose both. A center-of-gravity rule (which medium is the default button) is the practical discriminator.
- **Flagged for joint review** — recorded in STATUS.md Boundary Issues.

### vs Conference Calling Application

- Conference calling centers on a **scheduled multi-party meeting**: dial-in bridges, host/moderator controls, agendas, participant management.
- Internet calling centers on the **impromptu personal call**: 1:1 center of gravity; group calls are ad-hoc, small, and formed by adding people to a live call, not by scheduling a meeting.
- Join-by-link surfaces (FaceTime Links) drift toward meeting semantics — noted as a variant, not a Type change by itself.

### vs Push-to-Talk Application

- PTT is half-duplex broadcast to a channel/group (walkie-talkie semantics): press to talk, release to listen; no ring/answer phase, no synchronous co-presence negotiation.
- Internet calling is full-duplex, point-to-point, with an explicit answer act.

### vs Virtual Phone Application

- The virtual phone product's managed object is a **phone number** (a secondary number with its own inbox/log); calling is one use of the number.
- The internet calling application's managed object is the **call between people**; a number appears only in the optional breakout variant (and then as a metered destination, not as the user's standing identity).

### vs Instant Messaging Application

- IM's primary surface is the message thread; calls are an L1 capability on the same identity (per the IM pass).
- This Type's primary surface is the call; messaging may coexist (messaging-embedded packaging) but the call is the center of gravity.
- The two Types share identity and reachability machinery; the boundary is which act is primary.

### vs Social Audio Platform

- Social audio is room/broadcast-shaped with many listeners and public discovery; internet calling is private, person-addressed, and small.

## Uncertainties

- Only two products were directly documented (Skype post-retirement pages; FaceTime). The messaging-embedded pole — the current market's center of gravity — is asserted at reduced strength from cross-pass corroboration, not from fresh direct observation.
- Whether the standalone internet-calling form remains a viable market category post-Skype is uncertain; the 2026 market realization appears to be messaging-embedded + platform-native. This does not change the Type definition (the §24 check passes for older standalone products) but it does change where current evidence is strongest.
- The exact status of call log as L0 vs L1: both directly documented products have rich call logs, but older samples (chat-roster-initiated voice chat) did not surface a standalone log; kept at L1.
- The boundary with Video Calling Application needs a joint pass (see Boundary Issues).
- Presence/availability was not directly documented for the reachable products beyond Skype's historical behavior; asserted only as a qualified variant.

## Final Synthesis

Canonical Internet Calling Application, v1.1:

```text
L0 (defining invariant)
- Personal calling identity
- Reachable specific people (contacts / recents surface)
- Real-time voice call as a stateful event (place → ring → answer/decline → active → end)
- Live two-way audio carried over the internet by the service

L1 (common mature structure)
- Call log / recents with missed calls
- Contacts / people surface
- In-call controls (mute / end / hold-class)
- Video upgrade of the same call
- Group / multi-party call (add people to a live call)
- Ringing / missed states + notifications

L2 (variant / optional)
- Packaging: standalone / platform-native / messaging-embedded
- Identity substrate: service account / platform account / phone number
- PSTN breakout (dial pad, credit, inbound numbers) — optional paid layer
- Presence, encryption posture, voicemail, call filtering/spam, recording+transcript,
  in-call extras (captions/translation/screen share/co-watching), device handoff,
  join-by-link surfaces
```

The Application Document will present the L0 core and L1 common structure in natural language, with a Variants section naming the L2 options. L3 stays in Research Notes.
