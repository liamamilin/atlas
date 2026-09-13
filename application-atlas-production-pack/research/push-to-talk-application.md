# Research Notes — Push-to-Talk Application

## Research Goal

Understand what a Push-to-Talk (PTT) Application is as an Application Type: the defining interaction model (press-and-hold transmission), the communication container (talk groups / channels vs dialed calls), the delivery model (instant, setup-free, floor-controlled voice), the roles (member, dispatcher, administrator), the operational feature cluster that surrounds the Type, and the boundaries against dialing-based calling, conferencing, messaging, and social audio.

## Initial Boundary

Initial hypothesis (before research):

- PTT applications are the software descendants of two-way radio (walkie-talkie): the user holds a control to transmit and releases to listen; voice is delivered instantly to a defined group; there is no dialing, no ringing, no answering.
- The container is a standing talk group / channel whose membership defines the audience — not a dialed session.
- Nearest neighbors: Internet Calling Application, Conference Calling Application, Team/Group Messaging (voice modes), Social Audio Platform, and hardware Land Mobile Radio (LMR) + dispatch consoles.
- Key open questions: whether person-to-person addressing is definitional or common; whether transmission history/replay is common; where "PTT as a transmission mode inside other apps" ends and "PTT as a dedicated application Type" begins.

## Research Questions

1. What exactly is the defining transmission interaction, and what floor discipline governs the medium?
2. What is the communication container: talk group, channel, contact? What group types exist?
3. Is delivery purely live, or store-and-forward / replayable? Is there transmission history or recording?
4. How do users acquire identity and group membership? Who manages groups?
5. What does the sender see while transmitting (floor/talker indication)? What do receivers see?
6. What roles exist (member, dispatcher, administrator)? What does a dispatch console do?
7. What operational features cluster around the Type (location, emergency, priority, LMR interop, accessories)?
8. Boundary: when is PTT a mode inside another Application Type vs a Type of its own? What separates it from calling/conferencing/social audio?

## Representative Products

Selected for market representation across customer tiers and product philosophies:

| Product | Posture | Why selected | Research access |
|---|---|---|---|
| ESChat | mission-critical / public-safety broadband PTT with LMR interop | richest official documentation reachable; deepest operational semantics | ✅ official pages fetched |
| Zello | consumer + small-work broadband PTT (free app + paid work tier) | dominant consumer/worker PTT product | ❌ unreachable (timeouts ×3 across zello.com, zellowork.com, support.zello.com) |
| Motorola WAVE PTX | enterprise/mission-critical broadband PTT suite + PTT devices | major enterprise/critical-communication vendor | ❌ unreachable (404 ×2 on motorolasolutions.com) |
| Voxer | asynchronous walkie-talkie messaging hybrid (voice messages + live) | represents the store-and-forward philosophy | ❌ unreachable (timeouts ×2) |
| Carrier PTT offerings (T-Mobile ESChat edition, Verizon/AT&T PTT lines; historical Nextel Direct Connect lineage) | carrier-distributed PTT | represents the distribution channel variant | ❌ unreachable (403 t-mobile.com, telus.com) |

Note: the market existence and general posture of Zello / WAVE PTX / Voxer / carrier PTT are used as orientation anchors only. No operational claims about them are made from model memory.

## Sources

Fetched successfully (2026-09-08):

- ESChat — home page: https://eschat.com/ (service positioning, certifications, device forms, LMR interop summary)
- ESChat — Push-to-Talk service page: https://eschat.com/service/ (call types, eight talk group types, notable features, group-size limits, pricing)
- ESChat — Dispatch: https://eschat.com/dispatch/ (console integration modes, console feature matrix, cross-patching, talker ID)
- ESChat — Call Logging & Recording: https://eschat.com/call-logging-recording/ (SIPREC, SaaS logging, metadata recording)

Attempted and unreachable (limitation recorded; no claims drawn from these):

- zello.com, zellowork.com, support.zello.com — request timeouts (×1 each, host abandoned)
- voxer.com, support.voxer.com — timeouts
- motorolasolutions.com (wave-communications, /p/wave-ptx) — 404
- kb.eschat.com — timeout
- apps.apple.com (Zello listing) — redirected to regional storefront front page, no app content
- t-mobile.com — 403; telus.com — 403
- en.wikipedia.org (Push-to-talk, Zello) — timeouts
- etsi.org (MCPTT) — 404
- web.archive.org — timeout

Source-access limitation: only one vendor (ESChat) of the intended 4–5 product sample was reachable with official documentation. All Layer-A evidence below is ESChat-specific. Cross-product and historical findings are marked Layer B/C only where they rest on structural reasoning from the radio/PTT model and the market structure, not on inaccessible documentation. Assertion strength in both files is calibrated downward accordingly; precise non-ESChat operational details are absent by design.

## Product Observations

### ESChat (official pages, 2026-09-08) — Evidence Layer A

Positioning:

- "Broadband Push-to-Talk ... Communication for the Serious Workforce"; "Mission Critical PTT"; subscription-based PTT service for smartphone, feature-phone, and IoT devices.
- "ESChat's PTT technology provides a 'radio like' experience, providing encrypted communication between individuals, or groups with up to 3,000 members" — the radio analogy is the vendor's own primary framing.
- FedRAMP® Certified / GovRAMP™ / TX-RAMP / FirstNet Certified / DISA-approved; used by U.S. military and federal/state/local agencies. Public-safety/defense posture, but sold commercially as well.
- Distribution: direct subscription plus carrier editions (T-Mobile, Telus); "Available on All Wireless Carriers; Cross Carrier Communications without Gateways".
- Hosting: multi-tenant cloud (AWS commercial + GovCloud, georedundant), private cloud, or on-premise.

Core communication structure:

- Call types: 1:1, ad hoc, and Group. "ESChat allows users to communicate on a 1:1, adhoc and Group basis." Ad hoc = select multiple contacts from the contact list, press the PTT button to establish a call.
- Talk groups are the central container: eight distinct Talk Group types, "each customized to fill a particular mission", "from the basic Nextel type Group" to specialized ones; "Each multi-way Talk Group will support 3,000 members with the press of a single button."
- Talk Group types observed (all Layer A, product-specific semantics):
  - Personal Groups — created by a user, visible only to the creator, only the creator initiates calls.
  - Member Groups — visible to all members; any member may initiate.
  - Enterprise Open Groups — any user may join; optional owner/managers (who need not participate).
  - Enterprise Closed Groups — membership added only by owner/manager.
  - Surveillance Channel — long calls that are not auto-ended after inactivity (law-enforcement profile).
  - Public Safety Unicast Channel — monitor-only broadcast of audio feeds (NOAA weather, air traffic control, an LMR network feed).
  - Enterprise Dispatch Groups — time-of-day/day-of-week shift definitions; membership changes per shift; calling the group routes to on-shift members.
  - Ad hoc Groups — transient multi-contact selection from the contact list, established by pressing PTT.
- Group size limits documented: 250 (Personal/Member/Ad hoc) vs 3,000 (Enterprise/Surveillance/Unicast/Dispatch) — product-specific figures, not generalized.
- Floor control is a first-class, user-visible concept: "Floor Control Indication" is listed as a feature; talk groups are inherently multi-way one-speaker media.
- Presence: "Presence for Groups and Individual Contacts."
- Priority machinery: "User and Group Priority to control user access", "Priority Broadcast Calling", "Priority Calling and in-call pre-emption" — explicit priority/pre-emption semantics (mission-critical posture).
- Late Join on Group Calls — joining a group call already in progress.
- Multimedia messaging alongside PTT voice; real-time and historical location tracking and mapping ("Historical [Bread Crumb] Mapping", breadcrumb data download).

Roles & administration:

- Account/user/group management from both the handset UI and a web-based interface; enterprise administration via web interface; admin portal.
- Dispatch: PC-based dispatch client for Windows (SDK-integrated console partner), plus standards-based console integration (Wireline AIS with ISSI-connected P25) and RoIP gateway integration. Console feature matrix includes: private calls, group calls, emergency calls, multi-call support, talker ID displayed on console, user location displayed, cross-patching between channels, user ID passed across cross-patched channels. Explicit goal: dispatchers "will not be required to change their operational process or protocol" when moving between LMR and LTE PTT.
- Interoperability with LMR: P25 (ISSI), DMR (AIS), "any LMR (RoIP)"; wireline (ISSI, AIS, NXIP) and gateway (RoIP, SDK) integration; ATAK integration; the product "can operate as a standalone broadband solution ... or be integrated with" LMR.

History, recording, security:

- Call Logging & Recording: "Mission Critical Call Logging" — third-party recorders via SIPREC (NICE, Eventide, Exacom, Stancil, Komutel), or a SaaS logging service; "securely store their PTT voice and associated metadata"; browser-based access to archived recordings.
- Voice privacy: AES-256 symmetric encryption, ECDSA asymmetric, ECDH key exchange, SHA-384 — product-specific crypto stack.
- Encrypted account management; network isolation options; dedicated enterprise servers.

Devices & interaction surfaces:

- Clients: Android smartphones (including PTT-button "Android for PTT" models), iPhone, Android D-Pad feature phones (Sonim XP5S-class), IoT PTT devices (Siyata SD7 "IoT Radio"), PC client, accessories (PTT accessories page).
- Initiation patterns documented: "Initiate and Receive Calls with flip closed" (hardware-phone posture); "Front Screen Contact and Group navigation"; "Easy to use Contact and Group Selection"; "Instant Ad Hoc Group Calling".
- "press of a single button" for multi-way group calls — the single-button gesture is explicitly the vendor's framing of the interaction.

### Zello (unreachable) — orientation anchor only

Not directly observed. Market role: the mass-market broadband PTT app (consumer free tier + paid business tier), widely cited as the category's consumer anchor. Recorded as a representative product for market structure; no operational claims drawn.

### Motorola WAVE PTX (unreachable) — orientation anchor only

Not directly observed. Market role: enterprise/mission-critical broadband PTT suite from the incumbent LMR vendor, including PTT-over-cellular device lines. Recorded for market structure; no operational claims drawn.

### Voxer (unreachable) — orientation anchor only

Not directly observed. Market role: walkie-talkie-style messaging in which transmissions are held as replayable voice messages (asynchronous philosophy) rather than purely live. Recorded as the hypothesized store-and-forward pole of the delivery-model variant; flagged as unverified.

### Carrier PTT (T-Mobile edition of ESChat; Verizon/AT&T PTT lines; historical Nextel Direct Connect lineage) — orientation anchor only

Carrier pages 403/404. Market role: PTT distributed and branded by mobile carriers; historically, cellular-phone PTT (Nextel Direct Connect lineage) established contact/talkgroup-list PTT on phones in the 2000s. Recorded as the distribution-channel variant; historical claims kept qualitative.

## Cross-product Comparison

| Dimension | ESChat (observed) | Radio/LMR heritage (canonical reasoning, Layer C) | Broadband category (market structure, Layer B/C, weakened) |
|---|---|---|---|
| Transmission control | PTT button; "press of a single button"; floor control indication | physical PTT switch | the defining gesture across the category by the Type's own name |
| Container | talk groups (8 types) + 1:1 + ad hoc | channels/talkgroups; private calls common in trunked LMR | groups/channels primary; 1:1 common |
| Call setup | none — press and talk | none | none (category-defining) |
| Floor discipline | one speaker; priority/pre-emption | one speaker (channel discipline) | one speaker (half-duplex by design) |
| Delivery model | live; recording via logging systems | live | live in PTT-dedicated products; store-and-forward voice appears in messaging hybrids (Voxer-class) — unverified, variant strength |
| Presence | yes, per contact and group | n/a (radio has no presence) | commonly present in app-based PTT |
| Location | real-time + breadcrumb mapping | n/a | common in workforce/critical PTT |
| Emergency | emergency calls; priority broadcast | emergency channel/alarm conventions | common in workforce/critical PTT |
| Dispatch | PC dispatch client; talker ID; cross-patching | console dispatch is the radio standard | dispatch consoles common in workforce/critical PTT |
| History/recording | call logging + recording (SIPREC/SaaS) | logging recorders exist in LMR | compliance logging common in critical tiers |
| Group management | web admin + handset; open/closed/personal/dispatch types | radio system programming | admin portals common in managed PTT |
| LMR interop | ISSI/AIS/RoIP/SDK, ATAK | native (is LMR) | varies: none → gateway → standards → suite-level |
| Identity substrate | account provisioning via admin portal (web/handset) | radio IDs | account- or carrier-provisioned identities vary by product |
| Device forms | phone app, feature phone, IoT radio, PC | dedicated radio hardware | phone app + PTT accessories; some rugged/IoT device lines |

Because only ESChat was directly observable, no row above is promoted from single-product evidence into the defining core on breadth grounds alone; the defining core rests on the structural model of the Type (Layer C) whose observable instance is ESChat, and on the category's self-evident name-level contract (push-to-talk as gesture).

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures; remove any one and the product stops being a push-to-talk application:

1. **Standing addressed participant sets** — the audience of a transmission is a defined set of identified members (a talk group / channel; person-to-person addressing is a two-member set of the same kind) that exists before and after any transmission. Membership, not dialing, defines who hears. Remove → dialing-based calling (the audience is assembled per call, not standing).
2. **Press-and-hold transmission gesture** — transmitting is gated by a held control: press and hold to speak, release to listen. Speaking is a continuous explicit act; listening is the resting state. Remove → voice-chat/call applications where the microphone is simply open or a session is joined.
3. **Setup-free, floor-controlled delivery** — a press delivers voice to the set immediately, with no dialing, ringing, or answering step; reception is passive (no action required of listeners); one participant holds the floor at a time. Remove → conference calling (session setup + full-duplex) or uncontrolled multi-party audio.

Jointly-held is load-bearing: (1) without (2) is group voice chat; (2) without (1) is a point-to-point intercom — PTT gesture without the radio communication model; (1)+(2) without (3) is a dial-based group call with a PTT button, not radio-style communication; (3) alone is conferencing.

### L1 — Common Mature Structure

Verified present in the reachable sample (ESChat) and structurally consistent with the radio heritage; stated at "commonly" strength in the final document:

- contact list / member directory
- person-to-person (private) calls alongside group calls
- ad hoc group formation from selected contacts
- presence / availability indicators (per contact, per group)
- user-visible floor state — who is transmitting / talker indication
- text and multimedia messaging alongside voice
- location sharing and mapping (incl. historical traces)
- call logging / recording for compliance (critical tiers)
- emergency alerting and priority broadcast
- user/group priority with pre-emption
- late join to in-progress group calls
- administration portal (users, groups, policies) separate from the talk surface
- dispatch console for coordinators (channel banks, talker ID, cross-patching)
- PTT accessories / hardware buttons; speaker-mode use; multiple client forms (phone, PC, dedicated device)

### L2 — Variant / Optional Structure

- Posture/market tier: consumer & informal groups vs general workforce vs mission-critical/public-safety (certification regimes, e.g. government-cloud authorization in the critical tier)
- Delivery model: purely live transmission vs store-and-forward/replayable voice-message hybrids
- Distribution: independent subscription vs carrier-branded editions; cross-carrier interop as a differentiator
- LMR interoperability depth: none / RoIP gateway / standards wireline (ISSI/AIS-class) / SDK console integration / ATAK-class tactical integrations
- Hosting: vendor cloud / private cloud / on-premises
- Device realization: phone app only / phone + PTT accessories / dedicated rugged or IoT PTT devices / PC dispatch and client
- Encryption posture: transport-only vs default end-to-end (critical tier), product-dependent
- Group governance: creator-only, member-open, manager-closed, dispatch-shift-rostered groups (taxonomy of group types is product-specific in detail)

### L3 — Vendor-specific (research notes only)

- ESChat's eight named Talk Group types and their exact semantics; group-size limits (250 / 3,000); monthly price points; SIPREC logging partner list (Exacom, NICE, Eventide, Stancil, Komutel); specific console partners (CSS Mindshare, Zetron ACOM, Avtec Scout); ATAK integration; Viking Connect; certification badges (FedRAMP/GovRAMP/TX-RAMP/FirstNet/DISA); named device models (Sonim, Samsung XCover, Siyata SD7); "Nextel type Group" self-reference.

## Vendor-specific Findings

- The radio analogy is ESChat's own primary self-description ("'radio like' experience") — strong support that the Type's self-image is radio-style communication, not a calling product.
- Dispatch-shift talk groups (membership rotating by shift schedule) are documented in one product; held as vendor-specific until seen elsewhere.
- Monitor-only unicast channels (listen-only broadcast of external audio feeds) documented in one product; likely maps to a general "listen-only channel" capability but kept vendor-specific.
- Surveillance channels (inactivity auto-end disabled) — vendor-specific tuning for law-enforcement call patterns; implies other products auto-end transmissions after inactivity (plausible but unverified here).

## Boundary Findings

- **vs Internet Calling Application**: internet calling dials a person/session; ringing and answering occur; sessions are typically 1:1 or small ad hoc multiparty and full-duplex. PTT addresses standing sets, has no setup, and is floor-controlled. Remove L0 legs (2)+(3) → the product becomes an internet calling app. Boundary clean.
- **vs Conference Calling Application**: conferencing assembles participants into a scheduled/dialed session with full-duplex multi-party audio. PTT is instant, standing-set, half-duplex by floor control. Remove L0 leg (1) (dial-based assembly) + leg (3)'s floor discipline → conferencing. Boundary clean.
- **vs Team Messaging / Group Messaging (voice features)**: messaging Types are text-first with persistent channels; voice appears as recorded voice messages or joined calls. PTT-as-a-transmission-mode is a *capability* many voice/chat apps offer (a setting that gates the mic). The Type boundary proposed here: a Push-to-Talk Application is a dedicated application whose primary surface and organizing model is PTT transmission over standing sets — when PTT is only an input-mode option inside a messaging or voice-chat product, that product belongs to its own Type. Recorded as a taxonomy note (mode vs Type) in STATUS.md.
- **vs Social Audio Platform**: social audio rooms are audience/broadcast entertainment surfaces with public discovery and speaker/audience roles; PTT sets are private/organizational operational groups with equal-member floor discipline and no discovery surface. Boundary clean.
- **vs hardware LMR / radio dispatch systems (not a directory leaf)**: two-way radio is the pre-history of the Type. Broadband PTT applications interoperate with LMR (gateways, ISSI/AIS-class standards, console integration) and can replace or overlay radio fleets. The directory leaf documents the software application; LMR systems themselves are out of scope.
- **vs voice-message features of messaging apps (async hybrid)**: store-and-forward voice messaging alone is a messaging capability, not PTT; hybrid products (recorded voice messages + live PTT) straddle the messaging and PTT families; delivery model is therefore held as a variant axis, not a boundary wall.
- **"去掉什么就变成另一个 Type" tests**: remove press-and-hold → calling/voice-chat Type; remove standing sets (dial instead) → calling/conferencing; remove floor control → conferencing; remove radio-communication purpose and make it public/entertainment broadcast → social audio. The Type survives era changes (analog radio → cellular PTT → broadband app) with all three legs intact.

### Historical / Market-Sample Check

- Analog two-way radio / walkie-talkie: standing channels, PTT switch, no call setup, one-speaker discipline — satisfies all three L0 legs without any software, cloud, phone number, or location.
- Trunked LMR systems with dispatch consoles: talkgroups, radio IDs, priority/emergency, console dispatch — satisfies the legs at organizational scale.
- 2000s carrier phone PTT (Nextel Direct Connect lineage): contact/talkgroup lists on phones, button-initiated instant calls — satisfies the legs; identity was carrier-provisioned, not app-account.
- Modern broadband PTT apps (consumer, enterprise, public-safety tiers): satisfy the legs with app accounts and cloud infrastructure.
- Conclusion: the L0 is era-, network-, and device-agnostic; no modern implementation detail (cellular, cloud, apps, location, text messaging, encryption) leaks into the definition. Check passed.

## Uncertainties

1. Reachability: Zello, Voxer, Motorola WAVE PTX, and carrier PTT documentation were all unreachable (timeouts/403/404), and Wikipedia/ETSI/archives also failed. All cross-product breadth claims are therefore calibrated at Layer B/C strength; the final document states the limitation in Sources.
2. Delivery-model split: whether purely-live vs store-and-forward/replayable is a major market split (as hypothesized via the Voxer anchor) could not be verified; kept as a variant axis at weak strength.
3. Replay/history on consumer PTT: whether consumer PTT products commonly keep replayable transmission history is unverified; recording is verified in the critical tier (compliance logging) only.
4. Group-type taxonomy: the eight-type structure is ESChat-specific; the *kind* distinctions (personal/member-managed/open/closed/dispatch-rostered) are plausibly general but unconfirmed elsewhere.
5. Presence/late-join/priority in consumer products: unverified outside the critical tier.
6. Exact floor-control mechanics (timeout behavior, interruption rules, queueing) were not documented in reachable sources beyond the existence of floor-control indication; no mechanics are asserted.

## Final Synthesis

A Push-to-Talk Application is broadband software that reproduces the two-way-radio communication model: identified members belong to standing addressed sets (talk groups/channels; person-to-person as the two-member case); a held control (button) gates transmission; releasing it returns to listening; a press delivers voice to the whole set instantly with no dialing, ringing, or answering; one participant holds the floor at a time; reception is passive. Around this core, mature products add directory/contact lists, presence, messaging, location, emergency and priority machinery, administration portals, dispatch consoles, recording/logging, LMR interoperability, and multiple device forms including dedicated PTT hardware. Postures range from consumer/friends, through general workforce, to mission-critical/public-safety with certification regimes. The Type is distinct from internet calling and conferencing (no dialed session), from messaging (transmission is the medium, not an attachment), and from social audio (private operational sets, not public broadcast rooms); PTT as a mere input mode inside other applications does not constitute this Type.
