# Research Notes — Video Calling Application

## Research Goal

Understand the Video Calling Application as an Application Type from real products: what the organizing object is (the call), how a call is placed and answered, what the call lifecycle looks like, what capabilities mature products carry, and where the boundary sits against the sibling Types in §01.04 (Video Conferencing, Virtual Meeting Platform) and the adjacent Types that share the live-video surface (Live Video Chat, Random Video Chat, Internet Calling, Conference Calling, Instant Messaging).

## Joint-Review Obligations (flags awaiting this pass)

1. **video-conferencing-application (§01.04, processed 2026-09-09)** — organizing-object seam proposed: there the session is a convened addressable meeting distributed by invitation/link (participants join the meeting); here the call is placed to a person via a personal reachability surface (participants answer a call). Both support 1:1 and group. Proposed test: remove the convened addressable meeting → video calling; remove person-addressed contact-graph calling → video conferencing. **Discharged below.**
2. **live-video-chat-application (§01.08, processed 2026-09-10)** — call-model pole recorded as shared territory; that pass assigns pure calling utilities (no social layer, no discovery, no leisure posture — FaceTime-class, used as boundary anchor) to Video Calling; contact-graph call products with social/leisure furniture (JusTalk-class) straddle; alias risk recorded. **Discharged below.**
3. **internet-calling-application (§01.03, processed)** — same call object (identity → person → stateful call); differentiator proposed as primary medium (voice-first with video as upgrade vs video-first); that pass noted the boundary "needs a joint pass". **Ratified from this side below.**
4. **random-video-chat-application (§01.08, processed)** — remove the stranger-pairing → video calling (already ratified from that side; confirmed here).
5. **virtual-meeting-platform (§01.04, processed)** — seam not re-litigated there; noted Zoom's "video calling" feature page under the Meetings product (call as a mode of the meeting product). Consistent with the seam; noted below.

## Initial Boundary

- Initial hypothesis: software for live person-to-person (or small-group) video conversation, organized around a *call* placed to a person, with ringing/answer semantics inherited from telephony.
- Neighbors: Video Conferencing (meeting object), Conference Calling (audio medium), Internet Calling (voice-first), Live Video Chat (social context), Random Video Chat (platform-paired strangers), IM (calls as embedded capability), Telehealth (domain video consultation), Virtual Office Workspace (persistent space).
- The leaf's batch run failed on 2026-09-09; this pass re-runs it. No prior research or application file existed.

## Research Questions

1. What is the organizing object — call, meeting, room, or stream — and what defines it?
2. How is the callee addressed (contact graph, phone number, email, username, platform account, link)?
3. What is the call lifecycle (placement, ringing, answer/decline/miss, active state, end), and what record does it leave?
4. Is group calling in-type, and how does it relate to the meeting model?
5. What video-specific structure exists (camera as medium, effects, switching)?
6. Where exactly are the seams vs Video Conferencing (organizing object), Live Video Chat (social context), Internet Calling (medium), Random Video Chat (counterpart selection)?
7. What happens when calling products and meeting products merge (Duo→Meet, Skype→Teams)?
8. Historical check: do videophone-era and desktop-era products satisfy the definition?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| **FaceTime** (Apple) | platform-native pure call utility | the boundary anchor named by the live-video-chat pass; richest Tier-1 documentation (User Guide) |
| **Google Duo → Google Meet** | phone/email-addressed consumer calling app, later merged into a meeting product | the convergence case: a standalone video-calling app absorbed by a meeting-centric product |
| **Skype** | historical archetype (username identity, consumer + paid telephony) | the two-decade archetype; retired May 2025, folded into Teams Free — second convergence case |
| **JusTalk** | contact-graph calling + social/leisure furniture | the straddle case named by the live-video-chat pass |
| **imo** | regional/emerging-market calling-first app with messaging layer | regional pole; international-calling posture |

Five poles: platform-native / cross-platform-consumer / historical-archetype / social-furniture straddle / regional. Different product philosophies and customer tiers.

## Sources

- Apple — FaceTime User Guide for Mac (welcome, make and receive calls, FaceTime links): https://support.apple.com/guide/facetime/welcome/mac , https://support.apple.com/guide/facetime/make-and-receive-calls-in-facetime-fctm35828/mac , https://support.apple.com/guide/facetime/start-or-join-a-call-from-a-facetime-link-fctm2cd42547/mac — fetched 2026-09-10 [A]
- Google — Workspace blog "Bringing the power of Google Meet to Google Duo users" (2022-06-01) and The Keyword "Duo, meet Meet": https://workspace.google.com/blog/product-announcements/bringing-the-power-of-google-meet-to-google-duo-users , https://blog.google/products-and-platforms/products/duo/duo-meet — via search excerpts 2026-09-10 [A for Duo feature framing]
- Google Meet Community thread (2025-11-11) "Did the app change completely?" — product-expert reply confirming merger and removal of chat + direct ringing call: https://support.google.com/meet/thread/386895191/did-the-app-change-completely [B — community, not official policy page]
- Microsoft — "Skype is retiring in May 2025: What you need to know": https://support.microsoft.com/en-us/skype — fetched 2026-09-10 [A for retirement facts and feature framing]
- JusTalk — product page + Help Center index (Chat and Call category: Add Friends, Call and Meetings, Chat, Friend Homepage, Friend Management, Group Management, Groups, Send Messages): https://www.justalk.com/ , https://justalk.com/category/help-center.html , https://justalk.com/category/help-center/chat-and-call.html — fetched 2026-09-10 [A]
- imo — official site and App Store listing via search excerpts: https://imo.im/ , https://apps.apple.com/ca/app/imo-international-calls-chat/id336435697 — 2026-09-10 [A− via excerpts; direct fetch timed out]
- Press coverage of the Duo/Meet merger (TechCrunch 2022-06-01, CNET 2022-06-01, Wired/Ars 2022-08-06) [B]

### Source-access Limitations

- **Google help center unreachable** — support.google.com/meet and support.google.com/duo both timed out (2 attempts each across this and the prior video-conferencing pass). Duo's detailed call mechanics (ringing UX, pre-call previews) are NOT directly verified; Duo evidence relies on Google's own blog announcements and press. No precise Duo mechanics are asserted anywhere.
- **Skype operational documentation retired** — the support URL now serves the retirement FAQ only. Skype's call mechanics are NOT restated from memory; Skype is used as the historical archetype with evidence limited to the retirement page's own feature framing ("one-on-one and group calls, messaging, and file sharing").
- **imo.im direct fetch timed out** — official positioning taken from search excerpts of imo.im and the App Store listing; assertion strength reduced accordingly.
- **Historical samples argued structurally, no fetch** (same precedent as the live-video-chat pass): videophone / circuit-switched mobile video telephony and desktop-era person-to-person videochat.

## Product Observations

### FaceTime (Apple) — platform-native pure call utility [A]

- Identity: sign in with Apple Account; calls addressed by **name, number, or email**; suggested contacts offered. Calls reach "anyone who's using an Apple device" (ecosystem-bounded), with web join for Android/Windows via FaceTime links.
- Call placement: New Call → enter name/number/email or pick a suggested contact → **FaceTime Video call** or **FaceTime Audio** (menu choice). Group call: enter each person's contact information in the To field (documented limit: 32 participants — vendor number, L3).
- Answer/decline: incoming calls ring **even when FaceTime isn't open**; answer as video, answer as audio (camera automatically off), answer RTT; while on another call: End & Accept or Hold & Accept (**video calls can't be placed on hold** — vendor-specific semantics, L3). Decline paths: decline, reply with a message, create a callback reminder, send audio call to voicemail.
- Voicemail: unanswered FaceTime audio calls can go to voicemail with live transcription (product-specific, L3).
- Call history: recent and missed calls; return recent or missed calls; delete from history; **filter calls** from unknown numbers/spam (silenced, listed separately); block callers.
- Group call lifecycle: leaving a Group FaceTime call leaves it active until all participants leave; **rejoin an active call from call history**.
- FaceTime **links**: create a link for a new or current call, share it; join from the app or Messages; Android/Windows users join on the web; link creator (and anyone in the call ≥30s) can approve/decline join requests and remove recent joiners; delete link; FaceTime video calls can be attached to calendar events. → a shareable, joinable, manageable invitation object riding on a call.
- In-call: add people; move call to another device (continuity); SharePlay (watch/listen together); collaborate on projects; change view; audio call features; Live Captions; translation.
- Video features: video effects (Center Stage, Portrait, Studio Light, Reactions, backgrounds); take a Live Photo during call.
- Screen share + request/give remote control (conferencing-flavored capability inside a calling product).
- Framing: "FaceTime video calls let you see others' expressions and reactions just as if you were face to face. When you don't want to use your camera, you can make a FaceTime audio call." → **video is the primary medium; audio is the no-camera mode.**

### Google Duo → Google Meet — consumer calling app merged into a meeting product [A for Duo framing; B for post-merger]

- Duo's own framing (Google blog, 2022): "cross-platform video calling app"; video calls to friends and family **by phone number or email address**; group calls (documented limit 32); family mode with doodles, masks, fun effects; filters/effects; messages; Google Assistant voice placement; conversation history, contacts, messages saved in the app.
- Merger (2022): Duo upgraded with all Meet features — schedule meetings, virtual backgrounds, in-meeting chat, live sharing, captions, larger participant limits — then **renamed Google Meet**; "a single solution for both video calling and meetings". Existing Duo features "here to stay".
- Post-merger reality (Google Meet Community, 2025-11, product-expert reply): the Duo app "has been merged into Google Meet, and some old features have been removed. **The chat messaging feature and the direct ringing call function are no longer available**… Google Meet mainly focuses on meetings and video calls." → the meeting object absorbed the call object; the ringing call model receded.
- Market perception (community comment): merging Duo and Meet is "equivalent to merging FaceTime with Microsoft Teams — they're two different apps for two different uses." → users perceive calling and meeting products as distinct Types.

### Skype — historical archetype, retired [A for retirement; mechanics not restated]

- Microsoft retirement FAQ (fetched): "As of May 5th, 2025, Skype is retired." Users moved to Microsoft Teams Free with Skype credentials; "chats and contacts automatically transfer".
- Skype's core features framed by Microsoft itself: "one-on-one and group calls, messaging, and file sharing" — the consumer calling archetype's own summary of what it was.
- Paid telephony machinery (Skype Numbers, Skype Credit, Dial Pad, SMS, call forwarding, caller ID) documented as retired services → the PSTN-interconnect variant of the calling lineage, folded into Teams/Teams Phone territory.
- No operational call mechanics available (docs retired). Skype is used here only as: (a) the historical archetype of person-addressed consumer video calling, (b) the second convergence case (consumer calling folded into a meeting-centric product), (c) evidence of the paid-telephony variant boundary.

### JusTalk — contact-graph calling with social/leisure furniture (the named straddle) [A]

- Self-label: "Video Calls & Messenger — Talk, Share, Connect with Loved Ones… simple, safe, and fun 1v1 calls, group calls, and messages." User review quoted by the vendor: "I think it is like FaceTime."
- Calls: free 1v1 video calls and group calls (documented premium limit: 50 members — vendor number, L3); HD video; smooth switching across Wi-Fi/3G/4G; night vision.
- In-call leisure furniture: draw and share doodles, stickers, photos in real time; games during the call.
- Memories: record and save video & voice calls, kept in a "Memories" archive.
- Messaging layer: texts, photos, videos, stickers 1v1 or in groups; push-to-talk "Talkie" feature.
- Social layer: "Moments" feed (share life's moments); friends machinery in help center (Add Friends, Friend Homepage, Friend Management); groups machinery (Groups, Group Management).
- Help center top-level categories: Account and Settings / Premium and Benefits / **Chat and Call** / Personalization and Moment / Family and Control / Hardware and Products — the call sits at the center, wrapped by social and family machinery.
- Family/kids editions: JusTalk Kids, JusTalk Family (parent account linking, kids friends management, sensitive content control, live location, usage limits, dedicated hardware).
- Monetization: free core + Premium/Premium Family/Platinum Family memberships.
- Encryption claim: end-to-end encryption of calls and messages (vendor claim).

### imo — regional calling-first app with messaging layer [A− via excerpts]

- Self-label: "imo: Free Video Calls and Messages… Connect with your loved ones through calls and messages"; App Store: "imo is a FREE, simple, and secure international video call & instant messaging app"; 200M+ users, 170+ countries, 62 languages; App Store category: Social Networking.
- Calls: free HD video calls, audio & video, international calls stable over 2G/3G/4G/5G/Wi-Fi (low-bandwidth posture).
- **Personal Calling Card / Global Web Call**: "Share a single link for free cross-platform calls" — WebRTC-based calls and messaging with people regardless of whether they are imo users → link/web invitation surface.
- Privacy/security: end-to-end encryption, disappearing messages, "Time Machine", 2-step verification, spam blocking.
- Messaging layer: photos, videos, voice messages, documents; imo Cloud sync; instant message translation.
- Social furniture: **VoiceClub** — create or join voice chat rooms, host events (talent shows, talk shows, competitions) → social-audio-shaped furniture inside a calling product.
- Regional extras: Hajj & Umrah assistant (pilgrimage guidance, location sharing, navigation).

## Cross-product Comparison

| Dimension | FaceTime | Duo→Meet | Skype | JusTalk | imo |
|---|---|---|---|---|---|
| Organizing object | the call | the call (pre-merger) → meeting (post-merger) | the call | the call | the call |
| Person addressing | name / number / email (Apple Account identity) | phone number / email | username (archetype; docs retired) | contacts / friends | contacts (international calling posture) |
| Reachability surface | suggested contacts + entered addresses | contacts + phone/email entry | contact list | friends list + add-friends machinery | contacts + messaging |
| Video as medium | primary; audio = no-camera mode | primary (pre-merger) | primary (archetype) | primary | primary |
| Ringing/answer model | yes (rings app-closed; answer/decline/voicemail) | yes pre-merger; **direct ringing removed post-merger** (community) | yes (archetype) | yes | yes |
| Call lifecycle record | call history (recent/missed, return, delete, filter) | history/contacts/messages saved (pre-merger) | archetype | call + chat history | history + cloud sync |
| Group calling | yes (add people; documented 32 limit) | yes (documented 32 pre-merger) | yes (archetype) | yes (documented 50 premium limit) | group chat + calls |
| Audio-only mode | yes (FaceTime Audio) | yes | yes (archetype) | yes (voice calls) | yes (audio calls) |
| Link/web invitation | FaceTime links + web join | meeting links (post-merger) | meet-now/chat invite links (retired FAQ) | — | Personal Calling Card / Global Web Call |
| In-call extras | effects, SharePlay, screen share + remote control, captions, translation | family mode doodles/masks, filters (pre-merger) | archetype | doodles/stickers/games, recording ("Memories") | translation, disappearing messages |
| Social furniture | none (pure utility) | messages (pre-merger) | messaging | Moments feed, friends, groups | VoiceClub rooms, messaging |
| Domain extras | — | Google Assistant | paid PSTN (numbers/credit — retired) | kids/family editions, hardware | Hajj/Umrah assistant, low-bandwidth focus |
| Status | current, ecosystem-bounded | absorbed into Meet (2022) | retired 2025 → Teams Free | current | current |

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The person-addressed call.** A live session placed by the caller addressing a specific identified person (or set of persons) through a personal reachability surface — a contact entry, phone number, email, username — and **answered** by the recipient. The counterpart is addressed by the caller, not convened at a meeting address distributed by invitation, and not assigned by the platform. *Remove → the convened addressable meeting (Video Conferencing) or the platform-paired stranger (Random Video Chat).*
2. **Live real-time audiovisual connection with video as the medium of record.** While connected, participants see and hear each other in real time; the product exists to put faces on the call (audio-only is a mode within the product, not the product's identity). *Remove the video → voice calling (Internet Calling / telephony); remove the live connection → video messaging.*
3. **The bounded call lifecycle.** The call exists as a discrete session with connection states — placed → ringing → connected → ended, with declined and missed outcomes — and ends when the participants hang up; the product holds no persistent shared space beyond the call. *Remove → a persistent room (Virtual Office / hangout territory) or a scheduled convened session (meeting territory).*

Jointly-held load-bearing:
- 1 alone (person-addressed, no live AV) = a voice/phone call
- 2 without 1 = random video chat / live video chat / broadcast territory
- 3 without 1+2 = a call log or redial machine
- 1+2 without 3 = an always-on personal video link (drifts toward persistent personal rooms)
- 2+3 without 1 = a video conference (bounded live AV addressed by a meeting object)
- 1+3 without 2 = internet calling / telephony

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Personal reachability surface (contact list / address book / suggested contacts) — the implementation of person-addressing
- Group calling — add people during the call; participant limits vary by product and plan
- Audio-only mode and mid-call video↔audio switching
- Call history — recent/missed calls, return-call, delete
- Answer/decline affordances — reply with a message, callback reminder
- Camera/microphone controls, camera switching
- Incoming-call notification that reaches the device with the app closed
- Block / filter unknown or spam callers
- Video effects (backgrounds, portrait/lighting, filters)
- In-call text messages
- Cross-device continuity (move an active call between devices)
- Shareable link invitation (call links, web join, calling cards) — straddles toward the meeting model; see Boundary Findings
- Encryption posture (transport or end-to-end; varies)

### L2 — Variant / Optional Structure

- Identity substrate: platform account (ecosystem-bounded), phone number/email, username, phone-contacts graph
- Ecosystem posture: platform-native closed ecosystem vs cross-platform (with web join bridges)
- Recording of calls (in-call capture kept as an archive)
- Screen sharing / remote control inside a call (conferencing-flavored optional)
- Co-watching / shared activities / in-call games (leisure layer)
- Social furniture around the call (feeds, friend machinery, voice rooms) — drifts toward Live Video Chat / Social Audio territory
- Family/kids editions with parental controls and managed friend lists
- Paid PSTN interconnect (virtual numbers, credit, dial-out to phones) — the softphone/internet-calling boundary
- Regional/low-bandwidth tuning; translation; religious/lifestyle assistants
- Monetization: free core with premium tiers

### L3 — Vendor-specific (research notes only)

- FaceTime: 32-participant group limit; Live Voicemail with transcription; Hold & Accept semantics (video calls can't hold); 30-second caller-management window on links; Center Stage/Studio Light/Reactions; SharePlay; RTT calls; ecosystem restriction with Android/Windows web join.
- Google Duo: family mode (doodles, masks); phone/email addressing; Google Assistant placement; 32-participant group limit (pre-merger); post-merger removal of chat + direct ringing (community-sourced).
- Skype: Skype Numbers, Skype Credit, Dial Pad, SMS, call forwarding, caller ID (all retired 2025–2026); Skype Manager administration.
- JusTalk: 50-member premium group limit; night vision; Talkie push-to-talk; TalkiePods kids hardware; Memories archive; Moments feed.
- imo: VoiceClub rooms; Hajj & Umrah assistant; Time Machine; Personal Calling Card; imo Cloud.

## Historical / Market-Sample Check (§24)

- **Videophone / circuit-switched mobile video telephony** (3G video-call era; the videophone lineage before it): calls placed to a phone number, ringing, bounded, 1:1, video as the medium. Satisfies L0 with **no app, no contact list, no internet protocol, no group calling**. → phone-number identity, contact graphs, and apps are NOT definitional. *(Argued structurally, no fetch.)*
- **Desktop-era person-to-person videochat** (iChat AV-class; the consumer videochat lineage the live-video-chat pass already scoped out of its own Type): calls placed to a username/account, answered, bounded. Satisfies L0. *(Argued structurally, no fetch — same precedent as the live-video-chat pass's CU-SeeMe/NetMeeting scope finding.)*
- **Modern sample** (FaceTime, Duo, Skype, JusTalk, imo): all satisfy L0; all carry L1 furniture in varying degrees.
- Conclusion: the L0 holds across eras and platforms. The canonical concept for addressing is **person-addressing through a personal reachability surface**, not the phone number and not the contact app.

## Boundary Findings

### vs Video Conferencing Application — organizing-object seam RATIFIED from this side

The seam proposed by the video-conferencing pass is confirmed exactly as framed: **the call is placed to a person and answered; the meeting is convened at an address and joined.** Both Types support 1:1 and group; the center of gravity differs. Test ratified: remove the convened addressable meeting → video calling; remove person-addressed calling from a personal reachability surface → video conferencing.

Documented overlap zone (both directions):
- Calling products grow link invitations: FaceTime links (create ahead, share, join from app/web, manage joiners, attach to calendar) and imo's Personal Calling Card are addressable, shareable, joinable objects riding on calls — but the product's center remains the call (ringing, answer/decline, call history); the link is an invitation surface, not a convened meeting with host roles and scheduling as the organizing object.
- Meeting products grow calling modes: the virtual-meeting pass observed Zoom's "video calling" feature page under the Meetings product (call as a mode of the meeting product).
- **Convergence evidence (two independent cases):** Google merged Duo (calling app) into Meet (meeting product) in 2022 — meeting features were added to the calling app, and the merged product later **removed the direct ringing call function** (community-documented), receding to "meetings and video calls". Microsoft retired Skype (consumer calling archetype) into Teams Free (meeting-centric) in 2025. In both mergers the **meeting object absorbed the call object** — the seam is a real market force, and the standalone calling Type is under consolidation pressure. This is recorded as a market-trend uncertainty, not a taxonomy change.

### vs Live Video Chat Application — call-model pole flag DISCHARGED, ratified as proposed

The live-video-chat pass's discriminator is ratified from this side: **the persistent personal social context** (profile, relationships, messaging/history held in-product as the product's center) is that Type's fourth leg; **pure calling utilities** (no social layer, no discovery, no leisure posture — FaceTime-class) belong to Video Calling. This pass's sample confirms the assignment: FaceTime is a pure call utility (no profile social space; call history is a log, not a social surface).

The JusTalk-class straddle is resolved as follows: JusTalk holds the **call at its center** (self-label "Video Calls & Messenger"; premium tiers sell call capabilities; help center centers on Chat and Call) with messaging, Moments, and games as furniture — held **in-type here as a Video Calling Application with social/leisure furniture**, with the alternative reading (Live Video Chat) recorded as the flagged straddle. The alias risk that pass recorded ("video chat" used loosely at the contact-graph pole) is acknowledged: the discriminator is what the product holds at its center — the call session (this Type) vs the personal social space (Live Video Chat). imo's VoiceClub rooms are social-audio-shaped furniture inside a calling product, same treatment.

### vs Internet Calling Application — medium-of-record seam RATIFIED from this side

The internet-calling pass's proposal is ratified: both Types share the same call object (identity → person → stateful call); the differentiator is the **primary medium** — voice-first with video as an upgrade (Internet Calling) vs video-first (this Type). FaceTime itself documents the posture: video calls "let you see others' expressions… just as if you were face to face"; audio is what you use "when you don't want to use your camera". Products carrying both media on one call surface are in-type here when video is the defining medium.

### vs Conference Calling Application — symmetric medium seam

Symmetric to the conference-calling pass's medium-of-record finding: remove the video medium → conference calling; the audio bridge is that Type's machinery. Paid PSTN interconnect (Skype Numbers/Credit-class) belongs to the calling/softphone lineage, not the meeting lineage.

### vs Random Video Chat Application — counterpart selection confirmed

Confirmed from this side (already ratified from that pass): there the platform assigns the counterpart from a stranger pool; here the caller addresses a specific person. Remove the stranger-pairing → video calling.

### vs Instant Messaging Application — capability vs Type

Video calling embedded in an IM product (the IM pass lists "voice/video call on the same identity" as common mature IM structure) is a **capability of IM**, not this Type. The standalone Type is the product whose **primary surface is the call**. Calling-first products with a messaging layer (JusTalk, imo) are held in this Type because the call, not the chat thread, is the center.

### vs other neighbors

- **Telehealth Platform**: domain video consultation bound to clinical context and scheduling — different Type; the video call is a medium inside it.
- **Virtual Office Workspace**: persistent spatial presence vs the bounded call.
- **Social Audio Platform**: a room becomes a chosen-counterpart session without an audience → this Type's territory (per that pass's own seam table).

### 去掉什么就变成另一个 Type

- Remove the person-addressed call (add a convened addressable meeting) → Video Conferencing
- Remove the video medium → Internet Calling / Conference Calling
- Remove person-addressing (platform assigns the counterpart) → Random Video Chat
- Add a persistent personal social context as the center → Live Video Chat
- Add an assembled audience → Social Live Streaming
- Add a persistent spatial workplace → Virtual Office Workspace
- Embed as a capability inside a chat product → Instant Messaging (capability, not Type)

## Uncertainties

1. **Google help center unreachable** (this pass and the prior conferencing pass) — Duo's detailed call mechanics unverified; Duo evidence rests on Google's own blog framing + press. No precise Duo mechanics asserted.
2. **Post-merger Meet behavior** (removal of direct ringing + chat) sourced from a Google support community product-expert reply, not an official policy page — moderate confidence, flagged [B].
3. **Skype mechanics** unavailable (docs retired); Skype used only as archetype + convergence case + paid-telephony variant evidence.
4. **imo evidence via search excerpts** (direct fetch timed out) — assertion strength reduced; no precise imo mechanics asserted.
5. **Market trajectory**: two independent mergers (Duo→Meet, Skype→Teams) show calling products being absorbed into meeting products. Whether a standalone consumer video-calling Type remains a durable market category or survives mainly as (a) platform-native call surfaces (FaceTime-class) and (b) calling-first regional/consumer apps (JusTalk/imo-class) is a market question the Atlas records but cannot settle.
6. **Group-size numbers** (32 FaceTime/Duo; 50 JusTalk premium) are vendor- and plan-specific — excluded from the final document.
7. Whether JusTalk-class products ultimately read as Video Calling (this pass's holding) or Live Video Chat (the alternative reading) may shift with market labeling; the center-of-gravity discriminator is recorded for future passes.

## Final Synthesis

The Video Calling Application is the **person-addressed live video conversation utility**: the user places a call to a specific person through a personal reachability surface, the recipient answers, and the participants see and hear each other in real time until they hang up. Its defining core is exactly three jointly-held structures — the person-addressed call (answered, not joined; addressed, not assigned), the live real-time audiovisual connection with video as the medium of record, and the bounded call lifecycle (ringing → connected → ended, with missed/declined outcomes, no persistent room). Mature products commonly add the reachability surface, group calling, audio-only mode, call history, answer/decline affordances, effects, in-call messages, device continuity, and shareable link invitations; variants span platform-native ecosystems, cross-platform contact calling, calling-first apps with messaging/social furniture, family/kids editions, low-bandwidth regional tuning, and paid PSTN interconnect. The Type's neighbors are separated by four discriminators: the organizing object (call vs convened meeting — Video Conferencing), the medium (video vs voice — Internet Calling / Conference Calling), the counterpart selection (addressed vs platform-assigned — Random Video Chat), and the center (call session vs personal social space — Live Video Chat). The market is consolidating calling into meeting products (Duo→Meet, Skype→Teams), leaving the Type carried by platform-native call surfaces and calling-first consumer apps — a trend recorded, not a taxonomy change.

**Joint-review discharges**: video-conferencing-application's organizing-object seam RATIFIED exactly as proposed (with the link-invitation and calling-mode overlap zones documented); live-video-chat-application's call-model-pole flag DISCHARGED (pure calling utilities = this Type, confirmed; JusTalk-class held in-type with the alternative reading recorded); internet-calling-application's medium-of-record seam RATIFIED from this side; random-video-chat-application's boundary confirmed.
