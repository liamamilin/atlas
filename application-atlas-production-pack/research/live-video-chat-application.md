# Research Notes — Live Video Chat Application

## Research Goal

Understand what a Live Video Chat Application actually is as an Application Type: its defining structure, the interaction loops that constitute it, the surfaces users operate, the social machinery wrapped around live video conversations, and the boundaries against adjacent Types — especially the three processed §01.08 siblings (Random Video Chat Application, Social Live Streaming Platform, Social Audio Platform) and the unprocessed §01.04 Video Calling Application.

This pass owns two pre-hung joint-review flags:

1. **From random-video-chat-application (2026-09-08)**: market labels overlap heavily — "live video chat" is used as the self-description of random-pairing products (HOLLA headlines itself "Live Video Chat Platform"), while the Azar-style pole adds persistent identity/social furniture that "drifts toward video-social-discovery territory". Proposed discriminator from that side: Random Video Chat = platform-drawn stranger pairing + ephemeral session + re-roll loop; Live Video Chat = live video conversation organized around chosen/persisting contacts.
2. **From social-live-streaming-platform (2026-09-09)**: multi-guest live rooms with a watching audience straddle the broadcast/chat seam — the asymmetric-broadcast vs symmetric-peer-group discriminator should be ratified jointly on this side.

Also to be handled: the social-audio-platform pass instructed sibling passes to treat platform-embedded rooms symmetrically; the video-conferencing-application pass (2026-09-09) characterized video calling as "call placed to a person through a personal contact graph" (unratified — the video-calling-application pass failed and the leaf remains unprocessed).

## Initial Boundary

- Candidate confusion set: Video Calling Application (§01.04, unprocessed), Video Conferencing Application (§01.04, processed), Random Video Chat Application (§01.08, processed), Social Live Streaming Platform (§01.08, processed), Social Audio Platform (§01.08, processed), Friend Discovery Application (§01.05, processed), Dating Application (§01.07, processed), Community Chat Platform (§01.06, processed), Instant Messaging Application (§01.01, processed).
- The market phrase "live video chat" is a grab-bag: random-pairing products, contact-graph video-calling apps, video-social-discovery apps, hangout-room products, and paid performer-session ("cam") products all self-label with it.
- Initial hypothesis: the leaf's non-redundant content (vs the processed siblings and the §01.04 family) is the *social live video conversation surface* — live two-way video among equal peers, counterparts selected by the user, wrapped in a persistent personal social layer.

## Research Questions

1. What structures recur across products sold as "live video chat" that are NOT random re-roll (owned by Random Video Chat), NOT broadcast (owned by Social Live Streaming), NOT governed audio floors (owned by Social Audio), NOT convened work meetings (owned by Video Conferencing)?
2. Who selects the counterpart in each product — the user or the platform? Does anything persist after a conversation?
3. What organizing models exist (call / discovery / hangout / other)? Which are definitional, which variant?
4. What social furniture surrounds the live conversation (profiles, relationships, messaging, history)?
5. Where exactly is the seam vs Video Calling Application, given that leaf is unprocessed?
6. Where is the seam vs Friend Discovery and Dating, given the discovery pole's profile-browsing and gender-filter furniture?
7. Historical check: would older, regional, platform-native, or differently positioned products still fit the definition?

## Representative Products

Selected for market representation, documentation reachability, and spread across product philosophies and customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| **Azar** | video-social discovery (meet new people through live video, persistent social layer, gem economy) | the pole the random pass flagged as drifting into this territory; Tier-1 help center reachable |
| **JusTalk** | contact-graph call model with leisure furniture + family/kids posture | standalone consumer "video call & video chat" app; Tier-1 site + help center reachable |
| **FaceTime** | platform-native call-utility pole | the pure person-addressed call product; sampled as the **boundary anchor** for the Video Calling seam; Tier-1 user guide reachable |

Market-structure observations (pivot evidence, fetched directly): **Airtime** (now sells work-video tooling — camera/recorder/presentations, "essential tools for video at work") and **Bunch** (bunch.live now fronts "Mini Party", a party-game app). Both formerly hung around the social video-hangout space; their pivots are direct evidence that the standalone hangout generation dissolved.

Attempted and unreachable (no operational claims made for any of these): imo (imo.im — timeout ×2), Discord support (timeout ×2), Snapchat support (transport error), Houseparty (Wikipedia + rest API timeout ×2), Tango (transport error), Azar main marketing site (403 — help center reachable), HOLLA/OmeTV/Camsurf (owned by the random pass, not re-fetched).

## Sources

Tier-1 (official operational documentation, fetched 2026-09-10):

- Azar Help Center — https://help.azarlive.com/ (hub: categories Notices / Using Azar / Account / Payment / Technical Support / Safety, Security & Privacy / FAQ)
  - "How Do I Meet New People On Azar?" — https://help.azarlive.com/hc/en-us/articles/227042248 (breadcrumb: Using Azar › Video Chat)
  - "What is Pick & Match?" — https://help.azarlive.com/hc/en-us/articles/22888596405017 (breadcrumb: Using Azar › Video Chat)
  - "What is Azar Lounge and How to Use?" — https://help.azarlive.com/hc/en-us/articles/6666152554137 (breadcrumb: Using Azar › Azar Lounge)
  - "How Can I Use The Video Call Feature?" — https://help.azarlive.com/hc/en-us/articles/4408439077017 (breadcrumb: Using Azar › Message & Friend)
  - "How to Follow Others on Azar?" — https://help.azarlive.com/hc/en-us/articles/4408439024665 (breadcrumb: Using Azar › Message & Friend)
  - Hub FAQ: "Why Has My Account Been Suspended?" (community guidelines: match/messages conduct, profile rules), "What If Other Users Make Me Uncomfortable (How to report)?", "What are the Azar Plus and Azar Premium and Azar Supreme benefits?" (subscription tiers, gems, gender filter items)
  - Article list via Zendesk API (categories + "Using Azar" articles), confirming surface inventory: Video Chat, Pick & Match, Lounge, Message & Friend, history, translation, Azar Assistant (AI), badges, profile suggestions, invite friends
- JusTalk — product page https://www.justalk.com/ ("Free 1v1 Video Call & Video Chat App"; "Video Calls & Messenger"; 1v1 + group calls; in-call doodles/stickers/photos/games; Memories recording; Moments; encryption claim; Premium/Premium Family/Platinum Family tiers; JusTalk Kids / JusTalk Family products)
  - Help Center hub https://justalk.com/category/help-center.html (topics: Account and Settings / Premium and Benefits / Chat and Call / Personalization and Moment / Family and Control / Hardware and Products / Others)
  - "Chat and Call" category https://justalk.com/category/help-center/chat-and-call.html (sections: Add Friends / Call and Meetings / Chat / Friend Homepage / Friend Management / Group Management / Groups / Send Messages)
  - "Call and Meetings" category https://justalk.com/category/help-center/chat-and-call/call-and-meetings.html (articles: Make 1v1 Call / Make a Group Call / Schedule a Meeting / Share Screen / Use Filters in a Call / traffic modes / troubleshooting)
- FaceTime User Guide for Mac (macOS Tahoe 26) — https://support.apple.com/guide/facetime/welcome/mac (TOC: make/receive calls, return recent or missed calls, filter calls from unknown numbers, block callers, delete calls from call history, FaceTime links, add people to a call, video effects (Center Stage/Portrait/Studio Light/Reactions/backgrounds), SharePlay watch/listen together, collaborate on projects during a call, Live Captions, share screen with remote control, translate)

Tier-1 pivot observations (fetched 2026-09-10):

- Airtime — https://www.airtime.com/ ("The essential tools for video at work" — Camera / Recorder / Creator / Stacks; © mmhmm inc.)
- Bunch — https://www.bunch.live/ (now fronts "Mini Party — Multiplayer Party Game with Friends!")

Sibling-pass counterparty evidence (processed Atlas passes, used at counterparty strength):

- research/random-video-chat-application.md (§Boundary Findings; the seam proposal and the Azar-pole observation)
- research/social-live-streaming-platform.md (asymmetry discriminator; "remove the assembled audience → live video chat")
- research/social-audio-platform.md (medium seam; "room becomes a chosen-counterpart session without an audience → video calling / live video chat")
- applications/video-conferencing-application.md + its STATUS entry (convened addressable meeting; proposed video-calling characterization)
- STATUS.md entries for friend-discovery-application and dating-application (seam vocabulary)

## Product A — Azar

### Key observations (evidence layer A unless noted)

- Self-description (help article): "Azar is a video chat app that allows you to find ready connections with millions of like-minded people near you and around the world. **You no longer need to wait for a match to happen; Just go to the Video Chat tab to discover and connect with new friends who are online, based on your social preferences.**" — the product has a discovery model (browse who is online, connect), explicitly distinguished from waiting for a match.
- **Pick & Match** (Video Chat tab): "curate your social circle by selecting profiles that match your interests"; a popup displays profiles; the user **selects the profiles they would like to connect with**; "The connection will start once the other person is available"; a Waiting tab lists pending selections (cancel one or pause all); requires gems; cost deducted whether the user starts or skips. — Counterpart selection is **user-driven from displayed profiles**, not random assignment; availability gating replaces the ring/answer handshake.
- **Azar Lounge**: a profile-discovery surface — browse profile cards (photos/videos), open a user's details, follow instantly, send a message (requires gems or free message items), filter by country/gender/language, limited manual refreshes. **No live video in the Lounge itself** — it is profile browsing feeding the social layer.
- **Video Call Feature** (Message & Friend section): "Go to the 'Message' tab, enter a chat room, and then select the video call button" — a contact-graph video call placed from a message thread.
- **Follow mechanics**: follow during a video chat ("if you're enjoying the match"), or later from the history tab ("even if you missed the chance to 'Follow' them during the chat"), or search by Azar ID, or invite friends. — The **encounter→relationship bridge**: a live conversation can be converted into a persistent follow/friend relationship, and the history tab is the record that makes later follow-up possible.
- **History tab**: past matches listed; reporting is available "while you are matched with them or from the history tab" — the encounter record persists on the user's side.
- Monetization: gems (virtual currency), subscription tiers (Azar Plus / Premium / Supreme) with benefits including gender filter items; message sending in Lounge costs gems or free message items.
- Safety: community guidelines covering conduct during matches and messaging (sexual content, insults/threats/hate), profile rules (no nudity/illegal/commercial content, no personal contact info); reporting during match or from history; account suspension as enforcement.
- Other surfaces: translation feature, Azar Assistant (AI), badges, profile suggestions, invite friends, rear-camera switch, location change.

### Reading

Azar is the **discovery pole**: live video chat as the way you *meet people*, with a persistent social layer (profile, follows, friends, messages, history) wrapped around the conversations. Counterparts are strangers, but **selected by the user** (browse online / pick profiles), never randomly assigned. This is exactly the pole the random pass flagged as "drifting toward video-social-discovery territory" — i.e., toward this leaf.

## Product B — JusTalk

### Key observations (evidence layer A unless noted)

- Self-description (product page): "JusTalk - Free 1v1 Video Call & Video Chat App"; "Video Calls & Messenger — Talk, Share, Connect with Loved Ones. Stay close through simple, safe, and fun 1v1 calls, group calls, and messages."
- Call model: free 1v1 video calls and group calls (product page states "up to 50 members" — product-specific figure, kept out of the Type-level document); help center documents "Make 1v1 Call", "Make a Group Call", "Schedule a Meeting", "Share Screen", in-call filters (iOS), traffic-mode settings.
- Leisure furniture *inside the call*: "Draw and share your doodles, stickers and photos in real-time. Or challenge your friends in enjoyable games during the call." — the live conversation is treated as a leisure activity, not a utility event.
- **Memories Recording**: "Record and save your video & voice call with just a tap. These memorable moments stay available in your 'Memories'." — the conversation as a keepsake; a social-memory posture, not a work-record posture.
- Persistent social layer: Add Friends / Friend Homepage / Friend Management / Group Management / Groups / Send Messages (help-center section inventory); "Moments to Share Happiness — Capture life's moments and share them with friends and family" (a personal feed surface).
- Family/kids posture: dedicated JusTalk Kids and JusTalk Family products; Premium Family tier with kids-friends management, sensitive-content control, live location, parent-account linking; TalkiePods hardware with parental settings. — A **family customer tier** inside the same Type.
- Positioning vocabulary: "Family & Friends Choice"; user quotes compare it to FaceTime ("I think it is like FaceTime").

### Reading

JusTalk is the **contact-graph pole**: live video conversation with chosen loved ones (1:1 and group), wrapped in messaging, friends, groups, Moments, and Memories, with an explicit leisure/family posture. Its call mechanics overlap Video Calling territory; its social layer and leisure furniture are this Type's furniture.

## Product C — FaceTime (boundary anchor)

### Key observations (evidence layer A)

- Apple's own guide frames it as **calls**: "Make and receive calls in FaceTime", "Return recent or missed calls", "Filter calls" (unknown numbers/spam "silenced and listed separately in your call history"), "Block callers", "Delete calls from your call history", "Start or join a call from a FaceTime link", "Add people to a FaceTime call" (Group FaceTime).
- Leisure features on the call: video effects (Center Stage, Portrait, Studio Light, Reactions, backgrounds), SharePlay ("watch TV shows, movies, and live sports, or listen to music together" during a call), "Collaborate on projects during a FaceTime call", Live Captions, screen share with remote control, translation.
- **No in-product social layer**: identity is the platform account (Apple ID / phone); there is no profile surface, no friends list, no messaging, no discovery of new people — relationship data lives in the OS (Contacts), and the only in-product record is call history.

### Reading

FaceTime is the **pure call-utility pole**: person-addressed video calls with leisure features, but no persistent personal social context held by the product. It is the archetype consumers call "video chat" — and simultaneously the archetype of §01.04 Video Calling. It is used here as the boundary anchor: it demonstrates both that the call-model pole is shared territory and that the pure utility pole lacks this Type's social context.

## Cross-product Comparison

| Structure | Azar | JusTalk | FaceTime |
|---|---|---|---|
| Live two-way video conversation | yes (Video Chat tab, Pick & Match, video call in messages) | yes (1v1 + group calls) | yes (calls + Group FaceTime) |
| Equal peer roles (no broadcaster/audience) | yes | yes | yes |
| Small co-present group (no assembled audience) | 1:1 | 1:1 + group | 1:1 + group |
| Counterpart selection | user-selected: browse online / pick profiles / follow list / Azar ID search | user-selected: contacts/friends/groups | user-selected: platform contacts / links |
| Persistent personal social context in-product | strong: profile, follows, friends, messages, history | strong: friends, groups, messages, Moments, Memories | absent: call history only; relationships live in the OS |
| Discovery/presence layer | yes (who's online, profile suggestions, Lounge) | no | no |
| Leisure furniture | gems economy, filters, translation, badges | in-call games/doodles, filters, Memories | effects, Reactions, SharePlay |
| Purpose posture | meet new people (stranger-social) | connect with loved ones (family/friends) | personal calls (utility + leisure features) |
| Monetization | gems + subscription tiers | free core + premium tiers | free (platform bundle) |
| Safety machinery | conduct rules, reporting (in-match + from history), suspension | kids/family controls, sensitive-content control | filter unknown/spam, block |

### Findings by evidence layer

- **B (cross-product commonality)**: live two-way video among equal peers in 1:1 or small-group form; user-selected counterparts; in-call personal toggles; some record of past conversations (history in the broad sense).
- **B (common but not universal)**: persistent in-product social layer (profiles, relationships, messaging) — present in Azar and JusTalk, absent in FaceTime; leisure furniture — present in all three but differently shaped; safety/reporting machinery — strong where strangers meet, thinner where only contacts meet.
- **A (product-specific)**: gems/Pick & Match waiting lists/Lounge (Azar); Memories/Moments/TalkiePods/kids tiers (JusTalk); SharePlay/Center Stage (FaceTime); JusTalk's 50-member group figure.

## Canonical Model — four abstraction layers

### L0 — Defining Invariant (four jointly-held structures)

1. **The live two-way video conversation** — real-time audio+video with every participant on camera, live while it happens. Remove → text/voice chat (IM, Social Audio) or recorded video (short-video, streaming).
2. **Equal peer roles in a small co-present group** — symmetric conversants; no broadcaster/audience asymmetry, no governed floor, no assembled audience of watchers; 1:1 or a small group. Remove the symmetry or add an audience → Social Live Streaming broadcast (or its 1:1 cam-style pole); add a governed stage → Social Audio.
3. **User-selected counterparts** — the user chooses whom to converse with: from their relationships, from suggestions, or by browsing available people; the platform never randomly assigns the counterpart. Remove → Random Video Chat (platform-drawn stranger pairing + re-roll).
4. **The persistent personal social context around the conversations** — the product holds profile, relationships, and messaging/history around the live conversations, so a conversation is one surface of an ongoing personal social space rather than an isolated utility event. Remove → pure person-addressed video-calling utility = the Video Calling Application pole (seam flagged for joint review with the unprocessed §01.04 pass).

Jointly-held load-bearing analysis:

- 1+2+3 without 4 = a video-calling utility (FaceTime-class) — Video Calling territory
- 1+2+4 without 3 = a social product where the platform picks counterparts — drifts to Random Video Chat / matchmaking
- 1+3+4 without 2 = 1:1 performer-customer sessions — cam/broadcast drift
- 2+3+4 without 1 = a social/messaging product without live video — IM / Friend Discovery territory
- 4 alone = a social app; 3 alone = a contact list; 1 alone = video transport

### L1 — Common Mature Structure

- The persistent social layer's furniture: profile (self-presentation), relationships (friends/follows), messaging threads, and a record of past conversations (history in the broad sense — match history, call history, memories).
- The call surface: place/answer, ring or availability-gated connection, camera/microphone toggles, self-view, end control.
- In-conversation leisure furniture: effects/filters/reactions; shared activities (games, co-viewing, doodles) where the product treats the conversation as hangout time.
- Safety machinery: reporting and blocking attached to live conversations and to the people met in them; conduct rules; (kids/family controls at the family pole).
- Group form alongside 1:1 (group video calls with chosen participants).

### L2 — Variant / Optional Structure

- **Organizing model**: call-model (place a call to a chosen contact), discovery-model (browse who's online / pick from suggested or displayed profiles), hangout-room model (drop into a live video room among friends; the standalone generation of this lineage has closed or pivoted — observed directly for two products — and the structure survives mainly in embedded forms).
- **Discovery/presence layer**: who-is-online browse, profile suggestions, profile-browsing surfaces (present at the discovery pole; absent at the contact-graph and platform-native poles).
- **Identity substrate**: platform account (Apple ID/phone), app account with ID search, phone-number/account variants.
- **Monetization**: free core (two poles) vs virtual-currency + subscription economy (discovery pole); premium family tiers.
- **Audience posture**: general consumer vs kids/family (dedicated kids products, parental controls).
- **Standalone vs embedded realization**: the same structure appears as a capability inside IM/community/social products.

### L3 — Vendor-specific (research notes only)

- Azar: gems economy, Pick & Match waiting list with pay-per-start-or-skip, Azar Lounge profile-browsing surface with refresh limits, Azar ID search, badges, Azar Assistant, subscription tier names, gender filter items per tier.
- JusTalk: Memories recording, Moments feed, Talkie/TalkiePods push-to-talk hardware, night vision, 50-member group figure, Premium/Platinum Family tier structure.
- FaceTime: SharePlay, Center Stage/Studio Light, call filtering of unknown numbers, FaceTime links, Live Photos during calls.

## Rejected Findings

- **"Live Video Chat = video calling" REJECTED as the leaf's definition.** The pure call-utility pole (FaceTime-class) lacks the persistent personal social context; defining the leaf as calling would make it redundant with §01.04 Video Calling Application and would contradict the directory's placement of the leaf in the Live Social family. The call-model pole is instead recorded as *shared territory* with a joint-review flag.
- **"Live Video Chat = random stranger video chat" REJECTED.** That structure is owned by Random Video Chat Application (platform-drawn pairing + re-roll + ephemerality). The discovery pole's counterparts are user-selected, and its encounters convert into persistent relationships (follow from history) — the opposite of the re-roll loop's nothing-persists posture.
- **"The discovery/presence layer is definitional" REJECTED.** The contact-graph pole (JusTalk) and the platform-native pole lack it entirely; it is a variant realization of counterpart selection, not an invariant.
- **"Leisure furniture (games/effects/co-viewing) is definitional" REJECTED.** Present in all three samples but differently shaped; a bare live video conversation with none of it remains squarely in the Type.
- **"Group video chat requires a convened addressable meeting object" REJECTED for this Type.** Group calls here are placed to people/groups from the social layer, not convened as addressable meetings distributed by invitation (that is the Video Conferencing structure). JusTalk's "Schedule a Meeting" is a feature riding on the call machinery, not the organizing object.
- **"Paid performer-session cam products belong here" REJECTED (structural).** They self-label "live video chat" but are broadcaster-viewer asymmetric (one side performs for the other) and commercial — the broadcast side of the asymmetry seam. No cam products were sampled; recorded as a structural boundary note only.

## Boundary Findings

| Neighbor | Seam | Removal test |
|---|---|---|
| Random Video Chat Application (§01.08, processed) | who selects the counterpart + what persists | platform-random assignment + nothing persists → Random Video Chat; user-selected + persistent social layer → this Type |
| Social Live Streaming Platform (§01.08, processed) | symmetric peers vs broadcaster/audience | add an assembled audience beyond the participants (incl. multi-guest rooms with watchers) → broadcast side; everyone present is a co-present participant → this Type |
| Social Audio Platform (§01.08, processed) | medium | audio-primary governed floor → Social Audio; video-primary peer conversation → this Type |
| Video Calling Application (§01.04, UNPROCESSED) | the persistent personal social context | remove the social context → pure person-addressed calling utility (FaceTime-class) = Video Calling pole; **shared territory at the call-model pole — flagged for joint review; alias risk recorded** |
| Video Conferencing Application (§01.04, processed) | convened addressable meeting + work purpose | add a meeting object with its own address distributed by invitation + work posture → Video Conferencing |
| Friend Discovery Application (§01.05, processed) | the primary surface | profile-evaluation + consent-gated contact formation + friendship as declared intent → Friend Discovery; immediate live video conversation as the surface → this Type (Azar's Lounge profile-browsing surface is Friend-Discovery-shaped furniture *inside* a video product — and it carries no live video) |
| Dating Application (§01.07, processed) | intent + contact gate | romantic-partner intent + mediated mutual-consent gate + pairing-bound conversations → Dating; gender filters and "curate your social circle" furniture at the discovery pole drift toward it but without the declared intent or the gate |
| Community Chat Platform (§01.06, processed) | container | standing community rooms with member populations → Community Chat; personal social space around one's own relationships → this Type |
| Instant Messaging Application (§01.01, processed) | primary surface | persistent message threads as the primary surface with calls as a capability → IM; the live video conversation as the surface around which the social layer is organized → this Type (embedded realizations straddle by packaging) |
| Paid performer-session cam products (unsampled, structural) | symmetry + commercial posture | one side performs for the other → broadcast-side/commercial territory, not the peer-conversation core |

## Historical / Market-Sample Check

- The smartphone social-video generation satisfies the definition across all three poles: discovery (Azar), contact-graph (JusTalk), platform-native call (FaceTime — as the boundary anchor just outside the Type proper).
- The hangout-room lineage (Houseparty-class): the definition covers it structurally (rooms among friends = user-selected counterparts + persistent social context; the live session entered as a room rather than placed as a call is an organizing-model variant). Its standalone generation has dissolved — observed directly: Airtime now sells work-video tooling; Bunch now fronts a party-game app. Houseparty's own documentation was unreachable (timeouts); no operational claims are made for it.
- Pre-smartphone two-way video products (CU-SeeMe/NetMeeting-class, argued structurally, no fetch): they lack the persistent personal social context and belong to the calling/conferencing lineage. This is recorded as a **scope finding**: the leaf's population is the social-video generation; the utility lineage is the Video Calling seam, not a failure of the definition.
- Regional mass-market call+chat apps (imo-class, unreachable this pass): structurally they carry contacts + chat + history + calls and fit the contact-graph pole; no operational claims are made.

## Uncertainties

1. **The Video Calling seam is unratified** — the neighboring leaf is unprocessed (its batch run failed). The discriminator proposed here (persistent personal social context as the Type's fourth leg; pure calling utilities on the Video Calling side) must be jointly reviewed when that pass runs. Alias risk is real: the market uses "video chat" and "video call" interchangeably at the contact-graph pole (JusTalk's own user quotes compare it to FaceTime).
2. **The hangout-room lineage is documented at structural strength only** — its standalone products are closed/pivoted and their documentation is largely unreachable; the "survives mainly embedded" claim is a moderate-strength market observation (Discord/Snapchat documentation was unreachable this pass).
3. **The discovery pole's internal boundary vs Friend Discovery** is drawn from one product's surface inventory (Lounge carries no live video); other discovery-pole products might blur it further.
4. **Cam-style paid sessions** were not sampled; the boundary note is structural, not evidence-backed.
5. Whether the market will keep treating the contact-graph pole (JusTalk/imo-class) as "live video chat" or fold it into Video Calling is a market-label question the Atlas can only flag, not settle.

## Final Synthesis

The Live Video Chat Application is the **social live-video conversation surface**: live, real-time, two-way video among equal peers in 1:1 or small-group form, where the user selects the counterparts (from relationships, suggestions, or a browsable pool — never platform-random assignment) and the product holds a persistent personal social context (profile, relationships, messaging/history) around those conversations. The live conversation is one surface of an ongoing personal social space — the product's reason for existing — rather than an isolated utility event (Video Calling), a platform-random encounter (Random Video Chat), a broadcast (Social Live Streaming), a governed audio floor (Social Audio), or a convened work meeting (Video Conferencing).

Three organizing models realize the Type: the **call model** (place a video call to a chosen contact — shared territory with Video Calling, flagged), the **discovery model** (browse who's online / pick from profiles and start a live video chat — the distinctive Live Social realization), and the **hangout-room model** (drop into live video rooms among friends — standalone generation dissolved, survives embedded). The persistent social layer — not any single organizing model — is what makes the leaf non-redundant within the Atlas.

Seams discharged this pass: the random-video-chat seam (ratified with the generalization from "chosen/persisting contacts" to "user-selected counterparts", covering the discovery pole that pass flagged as drifting here) and the social-live-streaming broadcast/chat discriminator (ratified: an audience beyond the participants = broadcast side). Seam flagged: the Video Calling joint review (call-model pole shared territory; alias risk recorded).
