# Research Notes — Dating Application

## Research Goal

Identify the smallest stable invariant that defines the **Dating Application** Type, and place every other observed feature at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

Evidence layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation (official source for a specific product)
B Cross-product Commonality
C Canonical Inference
```

## Initial Boundary

Target:

> Dating Application (DIRECTORY §01.07 Dating & Relationship Discovery)

Nearest confusing Types:

- Matchmaking Platform (same family, §01.07)
- Relationship Discovery Application (same family, §01.07)
- Dating Community Platform (same family, §01.07)
- Friend Discovery Application (§01.05)
- General Social Network (§01.05)
- Instant Messaging Application (§01.01)
- Random Video Chat Application / Social Live Streaming Platform (§01.08)

Working hypothesis:

> A Dating Application lets people present themselves through profiles built for romantic evaluation, discover other members as potential romantic partners, express interest, and — through a contact gate — open a private two-person conversation.

The hypothesis intentionally avoids baking in the swipe deck, the mutual-swipe "match" mechanic, phone-number auth, or mobile-first design — those are dominant modern implementations, not obviously the defining structure.

## Research Questions

1. What objects make up the world: profile, candidate feed, like/pass, match, conversation, preferences, reports?
2. How does discovery actually work — deck, search, recommendations, curated picks? Which of these is definitional?
3. What gates contact between two members? Is the mutual-consent match required, or is direct messaging possible?
4. What is the interaction loop from profile creation to (a) conversation and (b) exit (unmatch/delete/success)?
5. What lifecycle states exist (match expiry, pausing, hidden profiles, unmatching)?
6. What rules matter: preferences/filters, first-message rules, verification, safety enforcement?
7. Where are the boundaries with matchmaking (service-led introductions), friend discovery, social networking, and IM?

## Representative Products

| Product | Why selected | Evidence obtained |
|---|---|---|
| Hinge | modern relationship-oriented app; prompt-based profiles; recommendation-feed discovery; "designed to be deleted" philosophy | Tier-1 help center, 6 pages fetched |
| Bumble | safety-forward consumer app; conversation-start gating; multi-mode product (Date/BFF) | Tier-1 support center, 4 pages fetched |
| Match | oldest surviving major service; search-era web heritage; subscription model; older demographic | Tier-1 help center, 4 pages fetched |
| OkCupid | long-running questionnaire/compatibility heritage; same help-center platform as Match | Root page only (deeper pages did not render) |
| Tinder | category-defining swipe-deck mainstream app | Help center unreachable (2 transport errors) — market context only |

The sample deliberately spans eras (Match 1990s web heritage vs mobile-first modern apps), discovery philosophies (search vs feed), and conversation-gating philosophies (open-to-subscriber vs strict mutual consent vs two-sided opening message).

## Sources

Research date: **2026-09-07**

Official help centers (Tier 1):

- Hinge Help Center — https://help.hinge.co/hc/en-us
  - What is Hinge? — https://help.hinge.co/hc/en-us/articles/26845979318803-What-is-Hinge
  - Connecting With Matches (category) — https://help.hinge.co/hc/en-us/categories/36230398395539-Connecting-With-Matches
  - How Do I Match with Someone and Start Chatting? — https://help.hinge.co/hc/en-us/articles/360011090134-How-Do-I-Match-with-Someone-and-Start-Chatting
  - Discover Feed — https://help.hinge.co/hc/en-us/articles/36311592824595-Discover-Feed
  - Managing My Profile (category) — https://help.hinge.co/hc/en-us/categories/36230426264467-Managing-My-Profile
- Bumble Support — https://bumble.com/en/help (renders support.bumble.com help center)
  - Finding love (category) — https://support.bumble.com/hc/en-us/categories/27406393448477-Finding-love
  - How conversations start on Bumble — https://support.bumble.com/hc/en-us/articles/36679912947229-How-conversations-start-on-Bumble
  - Category listing text observed for: Expired matches, Using the People tab, Using the Discover tab, Sending Notes, Your conversations, Viewing who's liked you, Recommending people to others
- Match Help Center — https://help.match.com/
  - Member Communication (category) — https://help.match.com/hc/en-us/categories/6241311005595-Member-Communication
  - Messages – How to Chat with Your Matches — https://help.match.com/hc/en-us/articles/7341373823771-Messages-How-to-Chat-with-Your-Matches
  - Searching on Match — https://help.match.com/hc/en-us/articles/6241693282331-Searching-on-Match
- OkCupid Help Center (root only) — https://help.okcupid.com/hc/en-us

Unreachable sources:

- Tinder help center (https://help.tinder.com/ and /hc/en-us) — transport errors on 2 attempts; abandoned per the network-restriction rule. Tinder is used as market context only; no operational claims are drawn from it.
- OkCupid category/section pages — the fetched pages rendered only the help-center root layout on 2 attempts; abandoned. Only the root category list is used.

Per the Source-access Limitation rule:

> 1. limitations recorded here ✓
> 2. assertion strength reduced for OkCupid and Tinder ✓
> 3. no precise workflow/rule claims drawn from unreachable sources ✓
> 4. no model-memory fill-in for precise details (e.g. OkCupid questionnaire mechanics, Tinder limits) ✓

## Product Observations

### Hinge

- Layer A: positioning — "the dating app designed to be deleted"; goal is getting members off the app onto dates ("Through in-depth and personalized profiles, daters have unique conversations that get them off the app and out on great dates"). (What is Hinge?)
- Layer A: "Every match begins by someone liking or commenting on a specific part of your profile." (What is Hinge?)
- Layer A: Discover feed — "recommendations based on mutual interest, meaning the users you see fit your preferences, and you fit theirs." Explicitly: "Hinge does not offer a search option to search for specific people." (Discover Feed)
- Layer A: like attaches to a specific profile element (photo or prompt) with optional comment; skip with X; undo of the most recent skip — free members 1 per week, subscribers unlimited; Remove and Report from profile menu. (Discover Feed)
- Layer A: subscriber filters (height, dating intentions, Active Today, New Here); all members can filter by age. (Discover Feed)
- Layer A: matching paths — (1) accept an incoming like in "Likes You" tab; (2) send a like in Discover, or a Rose in Standouts; "If they accept your Like or Rose, you'll match, and their profile will move to your Matches tab." (How Do I Match…)
- Layer A: matches can disappear (dedicated article); unmatching exists; chat supports messages, emoji, message likes, quoted replies; "Your Turn" and turn limits structure the reply loop; Convo Starters; hide chat. (Connecting With Matches category)
- Layer A: "We Met" — after exchanging phone numbers with a match, the app follows up to hear how the date went "so we can make better recommendations in the future." (What is Hinge?; Meeting section)
- Layer A: profile composition — photos (Top Photo feature), Prompts with prompt feedback, personal information such as religion, height, politics; gender/sexuality options. (What is Hinge?; Managing My Profile)
- Layer A: account machinery — phone number login with SMS verification, pause account, location settings, delete account / data export. (Managing My Profile)
- Layer A: monetization — free core; Hinge+ / HingeX subscriptions (see everyone who liked you, advanced preferences, priority likes); Roses; Boost. (What is Hinge?; My Purchases)
- Layer A: safety set — report/appeals, block people you know, Comment Filter, "Are You Sure?", Match Note, "Did This Bother You", age checks. (Connecting With Matches / Reporting & Appeals / Safe Dating categories)
- Layer B: no imported-contact reachability graph — discovery operates on the app's own member pool.

### Bumble

- Layer A: multi-mode product — Date, BFF (friends), plus business mode heritage; the "Finding love" category governs the Date mode; separate sections for friend-finding. (Support root; category pages)
- Layer A: People tab — "designed to help you meet people on Bumble Date. If you like each other, you'll match!" (Using the People tab, category listing)
- Layer A: Liked You tab — "shows you who's already liked you—so you can skip the search and match instantly." (Viewing who's liked you, category listing)
- Layer A: Discover tab — "a selection of members who have similar interests, the same dating goals, and communities in common." (Using the Discover tab, category listing)
- Layer A: Notes (formerly Compliments) — "friendly messages you can send to another member before you match." (Sending Notes, category listing)
- Layer A: conversation start (as of 2026-08-10 article update) — "Instead of just one person making the first move, you both get one opening message before the chat fully unlocks." Both parties have 72 hours from matching to send an opening message; 72 hours to reply once one is sent; if neither sends within 72 hours of matching, the match expires; opening message editable once within 5 minutes; a Note counts as an opening message. Opening Moves (the previous women-set-openings feature) "are no longer part of the experience." (How conversations start on Bumble)
- Layer A: Chats tab — "where all your conversations and active matches are stored." (Your conversations, category listing)
- Layer A: expired matches — "On Bumble, a match expires if no one sends a message within 72 hours of matching. Once a match expires, they'll have…" (Expired matches, category listing; 72 hours also stated in the conversations-start article)
- Layer A: unmatching and disappeared-matches handling documented. (category listing)
- Layer A: safety set — ID verification, reporting, safety features hub, "Taking a break" (pause-style), helpline linkage; separate Safety Center site. (Support root)
- Layer A: monetization — subscriptions with cancel flows documented in popular topics.
- Layer B: recommend-to-a-friend feature exists (sharing a profile to a friend) — sharing is a side surface, not the discovery spine.

### Match

- Layer A: search-first discovery — custom search with criteria (age and location defaulting from the profile's stated preferences; additional attributes: appearance, interests, background/values, lifestyle, keywords); "Online Now" checkbox; Reverse Search, Mutual Search, Saved Search; search sorting; some advanced filters reserved for Platinum subscribers. (Searching on Match)
- Layer A: recommendation surfaces coexist — "Recommended - Top Picks", "Member Recommendations to your Inbox", "Improving Matching Results". (Member Communication > Matching)
- Layer A: "Do my matches receive me as well?" article title — mutuality is treated as a question members ask; Mutual Search exists as a search type. (Member Communication category)
- Layer A: conversation gating — "All of our free members are now able to chat with every match! Once you match with someone, you can message each other directly." (Messages – How to Chat with Your Matches)
- Layer A: match/conversation states visible in the Matches tab: "She/He Liked You", "You Liked Him/Her", "You're a Match"; "Your Turn" reply affordance; new/unread bold. (same article)
- Layer A: pre-match one-way messages exist — "Messages from unmatched members appear in your Likes tab" with message previews; Intros feature ("How to Make Your Profile Stand Out"). (same article; Likes section)
- Layer A: likes taxonomy — Likes (blue heart), Super Likes (purple star), Likes History, Unlike; "Fake Likes and Messages" warning article. (Member Communication > Likes)
- Layer A: message immutability — "Messages can't be unsent, recalled, or retracted once sent." (same article)
- Layer A: regional overlay — "Special Notes for NY, NJ, CT, TX, and OK Residents": free messaging with all Mutual Matches; either member can start the conversation for free when both like each other. (same article; the article does not explain the regulatory reason — recorded without interpretation)
- Layer A: hidden profile mode — communication rules while hidden (dedicated article); Blocking and Unblocking; Deleting Messages and Unmatching; Message History. (Member Communication > Messages)
- Layer A: activity status — Green Dot / Green Circle presence indicator. (Searching section listing)
- Layer A: monetization — subscription tiers incl. Platinum; "Paid Features & Power-Ups" category. (Help root)
- Layer B: web surface with desktop navigation (Matches / Likes tabs "in the top navigation bar on Desktop") plus app — web heritage product.

### OkCupid (root only)

- Layer A (root only): help-center categories mirror Match's (same platform family): Profile & Photos, Paid Features & Power-Ups, Account Settings, Member Communication, Advice and Safety, Manage My Subscription. No structural detail drawn beyond this.

### Tinder (market context only)

- Not fetched (unreachable). Widely known as the popularizer of the swipe-card deck and the mutual-match mechanic in the modern era. No operational claims are made from this pass; the Type analysis below never depends on Tinder-specific evidence.

## Cross-product Comparison

| Finding | Hinge | Bumble | Match | Abstraction level |
|---|---|---|---|---|
| profile as self-presentation for romantic evaluation | yes (photos + prompts + personal info) | yes (profile + dating goals) | yes (preferences + attributes + photos) | L0 |
| candidate pool = app's own members (strangers), not imported contacts | yes (no search even) | yes | yes (search within member base) | L0 |
| discovery shaped by stated preferences | yes ("you fit their preferences, and they fit yours") | yes (People/Discover tabs) | yes (search criteria default from profile preferences) | L0 |
| unilateral interest expression (like-class) | yes (like photo/prompt, Rose) | yes (like; Notes pre-match) | yes (likes, Super Likes, Intros) | L0 |
| pass/skip as the negative expression | yes (X, undo limits) | yes (implied by like/match pairing) | yes (Unlike; removing profiles from search results) | L0 |
| mediated contact gate before two-way chat | yes (accept like / mutual) | yes (match; both send opening message) | yes ("once you match… message each other directly") | L0 |
| mutual-consent match as the gate | yes | yes | yes (current product) | L1 (see era check below) |
| one-way pre-match note attached to interest | yes (comment on like) | yes (Notes) | yes (Intros) | L1 |
| match/conversation list with states | yes (Matches tab, Your Turn) | yes (Chats tab, expired) | yes (state labels, Your Turn) | L1 |
| unmatch / block / report | yes (Unmatching, Remove, Report, block people you know) | yes (Unmatching, Reporting) | yes (Blocking and Unblocking, Deleting and Unmatching) | L1 |
| match/pairing lifecycle incl. expiry | yes (matches disappear) | yes (72h expiry documented) | yes (states; no-response article) | L1 |
| preference filters (age/location base; more gated) | yes (age free; others subscriber) | yes (tabs/goals) | yes (some filters Platinum) | L1 |
| "liked you" visibility surface | yes (Likes You; paid bulk visibility) | yes (Liked You tab) | yes (Likes tab/history) | L1 |
| activity/presence indicator | yes (Active Today) | — (not observed) | yes (green dot) | L1 |
| verification / safety machinery | yes (SMS verification, age checks, comment filter, report) | yes (ID verification, safety hub) | yes (advice & safety, fake likes warnings, phishing) | L1 |
| paid subscriptions / power-ups | yes (Hinge+/HingeX, Roses, Boost) | yes (subscriptions) | yes (tiers, Platinum, Power-Ups) | L2 (commercial machinery) |
| discovery = recommendation feed, no search | yes (explicit "no search") | hybrid (People + Discover tabs) | no (search-first, feed secondary) | L2 (philosophy pole) |
| first-message rule | either party | both must send one opening message (since 2026 update; earlier women-first) | either party (with US-state variations for free messaging) | L2 (product rule, changes over time) |
| match expiry window | not documented here | 72h documented | not documented here | L2 |
| multi-mode (date + friends) | no | yes (BFF) | no | L2 |
| post-date feedback loop into recommendations | yes ("We Met") | — (not observed) | — (not observed) | L2/L3 |
| web + app surfaces | app-first (mobile) | app-first | web heritage + app | L2 |
| branded mechanics (Roses, Standouts, Most Compatible, Top Picks, Reverse Search, Super Likes, Boost…) | yes | yes | yes | L3 |

## L0 — Defining Invariant

The smallest structure without which the product would no longer be recognizable as a Dating Application:

```text
Dating Profile (self-presentation built for romantic-partner evaluation)
└── Candidate Discovery over the app's own member pool
    (strangers, shaped by stated preferences — NOT an imported contact graph)
    └── Unilateral Interest Expression toward a specific candidate
        (like-class / pass-class)
        └── Mediated Contact Gate
            (the product controls when a two-way channel opens)
            └── Private Two-person Conversation
                (pairing record with a controllable lifecycle:
                 chat → unmatch / expire / block / report)
```

Five properties. Remove-tests:

- remove the *dating profile* (evaluation-oriented self-presentation) → anonymous chat / random video chat surface
- remove *candidate discovery over strangers* → messaging with existing contacts (Instant Messaging)
- remove *unilateral interest expression* → people browsing / directory, no decision loop
- remove the *contact gate* (anyone may freely address anyone) → open-messaging social/discovery surface (Social Network class)
- remove the *romantic-partner orientation* → friend discovery / social networking

## L1 — Common Mature Structure

Common in mature modern products but not required to recognize the Type:

```text
Mutual-consent match as the gate realization (both must express interest)
Match record with lifecycle (matched → chatting → unmatched / expired / removed)
One-way pre-match note attached to the interest expression (comment/Note/Intro)
"Liked you" visibility surface (often partially paywalled)
Preference filters shaping the candidate pool (age/location base; deeper filters often paid)
Match/conversation list with reply-turn affordances
Unmatch / block / report and anti-abuse filtering
Verification machinery (SMS/phone, photo/ID verification, age checks)
Presence/activity indicators on profiles
Paid subscriptions and à la carte power-ups (see-who-likes, boosts, priority placement)
Web and/or mobile surfaces
```

## L2 — Variant / Optional Structure

```text
Discovery philosophy poles
- recommendation/deck-first with no search (documented at one sampled product)
- search-first with saved/reverse/mutual search (documented at one sampled product)
- hybrid tabbed surfaces (documented at one sampled product)
- questionnaire/compatibility-flavored discovery (market heritage; not verified this pass)

Contact-gate refinement
- either party opens the conversation
- designated first mover (one sampled product's historical rule; replaced in 2026 by a
  two-sided opening-message requirement — evidence that this rule is product-specific
  and time-varying)
- two-sided opening message before chat "fully unlocks" (current at one product)
- match expiry windows when no one messages (documented 72h at one product; varies)

Intent specialization
- casual vs serious-relationship positioning
- marriage/matrimonial orientation (leans toward the Matchmaking Platform sibling)
- identity/community niches (LGBTQ+-focused, religion, profession, age groups)

Commercial machinery
- freemium subscription tiers; à la carte boosts/priority likes; paid bulk visibility

Surface and account
- mobile-first vs web-heritage; phone/SMS vs email vs social-login identity
- multi-mode products embedding friend-finding or professional modes beside dating

Regional/regulatory overlays
- US-state-specific free-messaging rules documented at one product (recorded as fact;
  reason not stated by the vendor)
```

## L3 — Vendor-specific Structure

Kept out of the Application Document:

- Hinge: Roses, Standouts, Most Compatible, Priority Likes, Prompt Feedback, Your Turn limits, Match Note, Comment Filter, "Are You Sure?", "Did This Bother You", "We Met", Top Photo, Hinge+/HingeX, New Here badge, undo-skip quotas (1/week free), pause account
- Bumble: Notes (ex-Compliments), Opening Moves (retired), BFF mode, Plans (companion app for IRL meetings), recommend-to-a-friend, 5-minute opening-message edit window, 72-hour timers, ID verification flow
- Match: Top Picks, Reverse/Mutual/Saved Search, Intros, Super Likes (purple star), Likes History, Hidden Profile mode, Green Dot activity status, Platinum tier, Power-Ups, NY/NJ/CT/TX/OK free-messaging notes, "Do my matches receive me as well?" article
- OkCupid: (not verified this pass — root only)
- Tinder: (not verified this pass — unreachable)

## Historical / Market-Sample Check (§24)

Question: would older, regional, or differently positioned dating products still fit the L0?

- **Search-era subscription products**: Match's heritage model (searchable profile database; subscription-gated contact rather than strict mutual consent; pay-per-message eras) satisfies L0 — profile + member-pool discovery + interest expression + mediated contact + private chat. The *form* of the gate differs (paywall/entitlement vs mutual consent), but contact mediation is present in both eras. Therefore the mutual-swipe match is L1 (dominant modern realization), not L0.
- **Regional products**: East-Asian and Southeast-Asian mainstream dating apps follow the same profile → discover → gate → chat shape; Japanese marriage-hunting (konkatsu) apps and South-Asian matrimonial sites share profile + search + contact machinery but shift intent toward brokered marriage — they lean toward the Matchmaking Platform sibling. Recorded as a boundary note, not forced into this Type's canonical core.
- **Platform-native products**: dating has no meaningful OS-native analog; the web-era services are the "older pole".
- **Non-swipe present-day products**: Hinge (prompts + likes) and Match (search) prove the deck is not definitional.

Conclusion: L0 holds across eras; the swipe deck, mutual-swipe match, phone-number auth, and mobile-first design all stay out of the definition.

## Boundary Findings

### vs Matchmaking Platform (sibling, §01.07, unprocessed)

Sharpest intra-family seam. In a Dating Application the user self-serves: the user evaluates the candidate stream, expresses interest, and passes the gate. In a Matchmaking Platform a service (human matchmaker or guided/curated machinery) selects and *introduces* candidates to each other; discovery-by-the-user is replaced or dominated by introductions-by-the-service, often with assisted communication and offline/event components. Test: replace self-service discovery with service-selected introductions and the product leaves this Type. Joint review recommended when matchmaking-platform is processed.

### vs Relationship Discovery Application / Dating Community Platform (siblings, unprocessed)

Probable umbrella/adjacent leaves. Working distinctions recorded for joint review: a *dating community platform* centers community surfaces (events, groups, content) around dating rather than the 1:1 candidate loop; *relationship discovery* reads as a broader umbrella label for the same loop. Recommend joint review when each sibling is processed; candidate outcomes are alias consolidation or family-split poles.

### vs Friend Discovery Application (§01.05)

Same structural skeleton (profile → discover strangers → interest → contact) but different intent and usually weaker/absent consent gating. The romantic-partner orientation is what makes this Type. Note the straddle: Bumble ships friend-finding (BFF) inside the same product — multi-mode products are one product, two Types by mode.

### vs General Social Network (§01.05)

Social networks center identity, feed, and a follow/friend graph; contact is graph-anchored and open. Dating centers the candidate loop over strangers with romantic framing and a consent gate. A dating profile is written to be *evaluated*, not followed.

### vs Instant Messaging Application (§01.01)

Chat exists in both, but in dating it is (a) gated by the pairing/match record, (b) anchored to candidate discovery, (c) deletable by unmatching, and (d) never drawn from an imported personal contact graph. Remove discovery + gate from a dating app and the remainder is not IM (there is no personal address book); remove profile+gate from IM and it remains IM.

### vs Random Video Chat / Social Live Streaming (§01.08)

No persistent evaluation-oriented profile loop and no consent-gated pairing record; live/ephemeral broadcast or random-pairing surfaces instead.

## Uncertainties

- Tinder's help center was unreachable; its market-defining mechanics (swipe deck, mutual match) are used only as widely-attested market context, never as evidence for precise claims.
- OkCupid deeper pages did not render; its questionnaire/compatibility discovery flavor was **not** verified this pass and is deliberately not asserted.
- The reason for Match's US-state free-messaging exceptions is not explained in the fetched article; recorded without interpretation (plausibly regulatory, but unverified — do not assert).
- Whether Bumble's two-sided opening-message rule applies uniformly across modes/regions/plan tiers is not verified beyond the fetched article (dated 2026-08-10).
- Match-expiry behavior at Hinge/Match is referenced ("matches disappeared", "No Responses") but exact windows were not documented for them; only Bumble's 72h window was directly documented.
- Directory siblings (matchmaking-platform, relationship-discovery-application, dating-community-platform) were not processed in this pass; all intra-family seams are one-sided recommendations for joint review.
- Whether "profile built for evaluation by strangers" should be split into two L0 objects (profile + stranger-pool) is an open refinement question; they are kept as one chain here because neither is independently meaningful in this Type.

## Final Synthesis

Canonical Dating Application:

```text
L0 (defining invariant)
- Dating profile as self-presentation for romantic-partner evaluation
- Candidate discovery over the app's own member pool (strangers), shaped by stated preferences
- Unilateral interest expression (like-class / pass-class) toward a specific candidate
- Platform-mediated contact gate controlling when a two-way channel opens
- Private two-person conversation as the working unit, with a controllable pairing
  lifecycle (unmatch / expire / block / report)

L1 (common mature structure)
- mutual-consent match as the gate realization; match record with lifecycle
- pre-match one-way notes attached to interest expressions
- "liked you" visibility; preference filters; reply-turn chat list
- unmatch/block/report + verification and anti-abuse machinery
- presence indicators; paid subscriptions/power-ups; web and/or mobile surfaces

L2 (variant / optional)
- discovery philosophy poles (feed-only / search-first / hybrid / questionnaire)
- first-message rules (either party / designated first mover / two-sided opening
  message) and match expiry windows
- intent specialization; commercial shapes; surface/auth postures; multi-mode
  embedding (friends); regional regulatory overlays

L3 (vendor-specific)
- Roses/Standouts/Most Compatible/We Met; Notes/BFF/Plans; Top Picks/Reverse Search/
  Intros/Hidden Profile/Platinum; state-specific messaging notes; etc. (research notes only)
```

The Application Document will present the L0 chain as the defining core and L1 as standard capabilities, with L2 covered as variants. L3 stays here.
