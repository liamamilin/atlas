# Research Notes — Dating Community Platform

## Research Goal

Identify the smallest stable structure that defines the **Dating Community Platform** Type (DIRECTORY §01.07, sibling of Dating Application), and resolve the joint-review flag recorded by the dating-application pass:

> "dating-community-platform centers community surfaces (events/groups/content) around dating rather than the 1:1 candidate loop; recommend joint review when each sibling is processed — candidate outcomes are keep-the-family-split with the who-selects test, or umbrella consolidation."

Abstraction levels per `WORKFLOW_v1.1.md §22`; evidence layers per `§23`; historical check per `§24`.

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

## Initial Boundary

Target:

> Dating Community Platform (DIRECTORY §01.07 Dating & Relationship Discovery)

Nearest confusing Types:

- Dating Application (sibling, §01.07) — sharpest seam; joint-review flag
- Matchmaking Platform (sibling, §01.07, unprocessed)
- Relationship Discovery Application (sibling, §01.07, unprocessed)
- Community Platform / Online Forum / Interest Community Platform (§01.06)
- Interest-based Social Network / Friend Discovery / General Social Network (§01.05)
- Event Management Platform / Event Registration (§26)
- Instant Messaging (§01.01), Random Video Chat / Social Live Streaming (§01.08)

Working hypothesis:

> A Dating Community Platform is a member community organized around partner discovery: shared participatory spaces (groups, discussions, events, feeds) are first-class structures alongside partner-oriented member profiles, and community participation is a designed path to meeting partners.

## Research Questions

1. What objects make up the world: community container, groups, discussions, events/activities, feed, member profiles, 1:1 messaging?
2. Is the community layer first-class (own navigation, own roles, own lifecycle) or an add-on to a dating loop?
3. How does partner discovery work here — through community surfaces, through a candidate loop, or both? Which is organizing?
4. Is there a contact gate (mutual-consent match) or is messaging open (gated by verification/subscription instead)?
5. What roles exist (member, organizer, co-organizer, moderator, community leader/champion)?
6. What rules matter: community guidelines, verification, commercial-activity bans, event liability, meetup disclaimers?
7. Where are the boundaries: vs Dating Application (candidate loop), vs Community Platform (§01.06, no partner discovery), vs Event Management (organizer-side), vs Social Network (§01.05)?

## Representative Products

| Product | Pole | Why selected | Evidence obtained |
|---|---|---|---|
| Her | hybrid (dating loop + communities) | queer dating app with first-class Communities, events, Add Friend | Tier-1: root + support center ×4 |
| Stitch | community-first (companionship community) | explicitly "not a dating site, a community" with a companionship/matching layer | Tier-1: root + FAQ + blog + help center ×4 |
| Frolo | two-mode (Community mode + Dating mode) | single-parent app with explicit two-mode architecture | Tier-1: root + community + dating pages |
| Christian Connection | dating site + member meetups + vendor events | faith dating site with member-run meetup layer since 2001 | Tier-1: root + events page + helpdesk ×3 |
| Hornet | social-network-shaped partner discovery | queer social network (feed/discover/chat) used for partner finding | Tier-2: root page only (support unreachable) |

Boundary cases observed (not core samples): Kippo (niche gamer dating app), Stir (Match-family dating app help structure), plus unreachable market-context products (FetLife, Taimi, ConnectingSingles, Mingle2, Thursday).

The sample spans: identity niches (queer ×2, single parents, Christian, 50+), organizing philosophies (community-first / hybrid / two-mode / dating+events / social-network-shaped), and business models (subscription, freemium, social enterprise).

## Sources

Research date: **2026-09-07**

Official sources (Tier 1 unless noted):

- HER — https://weareher.com/ (root)
  - HER Support Center — https://support.weareher.com/hc/en-us
  - Communities FAQ — https://support.weareher.com/hc/en-us/articles/37020509469467-Communities-FAQ
  - Meeting Others / Swiping — https://support.weareher.com/hc/en-us/articles/37020698193947-Meeting-Others-Swiping
  - Getting Started category — https://support.weareher.com/hc/en-us/categories/36990617156379-Getting-Started
- Stitch — https://www.stitch.net/ (root)
  - FAQ — https://www.stitch.net/faq/
  - "What is Stitch, exactly?" — https://www.stitch.net/blog/2016/08/what-is-stitch-exactly/
  - Help Center — https://support.stitch.net (collection structure)
  - How Stitch works — https://support.stitch.net/en/articles/700315-how-stitch-works
  - The Members section on Stitch — https://support.stitch.net/en/articles/2664791-the-members-section-on-stitch
  - Stitch vs Meetup — https://support.stitch.net/en/articles/3417025-stitch-vs-meetup-how-is-stitch-different-from-meetup
  - The Stitch Community collection (25 article titles) — https://support.stitch.net/en/collections/49023-the-stitch-community
- Frolo — https://frolo.com/ (root)
  - Frolo Community — https://frolo.com/community
  - Frolo Dating — https://frolo.com/dating
- Christian Connection — https://www.christianconnection.com/ (root)
  - Events — https://www.christianconnection.com/about-events
  - Helpdesk — https://help.christianconnection.com (category structure)
  - What are Meetups? — https://help.christianconnection.com/help/what-are-meetups
  - What events do you run? — https://help.christianconnection.com/help/what-events-do-you-run
- Hornet — https://hornet.com/ (root; Tier-2 surface only)

Unreachable sources (per the network-restriction rule, abandoned after 1–2 failures):

- FetLife — https://fetlife.com/about — timeout ×2
- Taimi — https://taimi.com/ and https://support.taimi.com/ — timeout ×2 each
- ConnectingSingles — https://www.connectingsingles.com/ — 403
- Mingle2 — https://www.mingle2.com/ — timeout
- Hornet support — https://hornet.com/support — timeout ×2 (root page used instead)
- Stir root — https://www.stir.com/ — 403 (help center subdomain reachable)
- Thursday — https://www.getthursday.com/ — title only (JS-gated body)

Per the Source-access Limitation rule: limitations recorded ✓; assertion strength reduced for Hornet (root-page evidence only) and for the lifestyle/forums poles (market context only) ✓; no precise claims drawn from unreachable sources ✓; no model-memory fill-in ✓.

## Product Observations

### Her (hybrid: dating loop + communities)

- Layer A: positioning — "Join a safe space where queer women, nonbinary and trans sapphics come to meet, chat and flirt, all with the goal of finding their person"; "15+ million active members"; "Join one of our vibrant 35+ communities"; "We have community spaces to connect with other people like you." (root)
- Layer A: free core features enumerated as "adding friends, viewing profiles, starting chats, viewing events, and joining communities" — dating and community surfaces listed side by side. (root FAQ)
- Layer A: explicit dual self-description — "HER isn't just a dating app — it's also a queer and lesbian community app… a fantastic tool for discovering new friends"; "Add Friend" option on profiles; "dedicated community section… engage in conversations on varied topics". (root FAQ)
- Layer A: Communities mechanics — topic/interest areas inside the app; join/leave; posts (photos, memes, links, blogs, videos, gifs); like/comment/share; @-tagging limited to matches and prior interactors; report/block from post menu; no limit on communities joined; feed icon → Communities tab → "My Communities". (Communities FAQ)
- Layer A: dating loop intact — Meet section driven by filters (free: age, distance; Premium: gender identity, sexual identity, relationship status, last online); swipe left/right; liking from inside the community (expand profile → heart); mutual like → match → chat box; "You have to Like people to start a conversation"; swiped-left profiles can reappear. (Meeting Others / Swiping)
- Layer A: community as fallback discovery — "We may be new in your area and there may not be too many active users nearby. If so, hop into the Feed/Community and you can meet all the other people there." (Meeting Others / Swiping)
- Layer A: help-center sections — About HER / Profile & Account Management / Messaging & Matches (Unmatching, Expiring Matches & Chat Archive, Sending Messages) / HER Premium Features. (Getting Started category)
- Layer A: verification "by connecting their profiles with existing social media accounts"; moderators on the Trust & Safety team; report/flag machinery. (root)
- Layer B: the community layer is first-class (dedicated tab, join/leave lifecycle, posting mechanics) AND the candidate loop is fully present — a true hybrid.

### Stitch (community-first companionship)

- Layer A: positioning — "The Social Community for Anyone Over 50"; "the world's leading companionship community"; 400,000+ members; "activities, interest groups, social connections, companionship and more". (root)
- Layer A: explicit non-dating positioning — "we don't actually call Stitch a 'dating site'… we're much more than that… a grassroots member-based community created by members for members." (FAQ)
- Layer A: companionship spectrum — "For some people this might be a romantic partner, for others it could just be a friend… Companionship covers friends, marriage, and everything in between"; married adults welcome for non-romantic activity partners. (FAQ)
- Layer A: "Stitch is not a Dating Site… Stitch isn't a Social Network… Stitch is a COMMUNITY… You don't USE Stitch. You JOIN."; profile browsing "caters to all types of companionship, from friendship right through to romance" via companionship settings; "one of the major features of Stitch is the ability to browse profiles of other members and get matched based on your companionship settings"; members organize events/activities/travel; "chat rooms & discussion forums"; Community Champions; "We try to emphasize real-world events and activities rather than just viewing profiles." (What is Stitch, exactly?)
- Layer A: platform structure — four top-level sections: **Community** (Activities, Groups, Discussions, Travel), **Members** (browse profiles, connect one-on-one), **Messages** (direct messages), **More** (settings/benefits). "The Community section is built on the idea that the best connections happen through shared experiences, not just browsing profiles." "Our first Stitch marriage happened through a Discussions forum!" (How Stitch works)
- Layer A: the two-layer articulation — "Activities, Groups, and Discussions are for connecting in a community setting. The Members section is for personal, direct connection." Members page = directory with sections: Newest members, Closest members, Most responsive, Most recently active, Matched members. (Members section)
- Layer A: community machinery (25-article collection) — find/attend/create activities; activity suggestions → scheduled activities; groups (location or interest; Regular/Public/Private types; group-scoped activities); discussion forums (General vs Debate & Discussion types; location scopes; owner-controlled participation); "Your Network"; attendance marking; co-organizers/owners; waitlists; first activities reviewed before publishing; virtual activities (Stitch Video Chat or Zoom); blocking from messages/events/groups; feedback about activities and member interactions; Welcoming Program; automated personal invites; Travel & Trips (Beta). (Community collection)
- Layer A: boundary self-articulation vs generic community platforms — "on Stitch these features are designed to serve the goal of finding companionship, rather than being an end to themselves"; Meetup's interest groups are the center there, while "on Stitch, interest groups are only optional… Stitch members connect with other members right across the community"; smaller ad-hoc activities suggested by any member; verification system; rich messaging; commercial activity prohibited; no advertising. (Stitch vs Meetup)
- Layer A: safety — mandatory verification before communicating (also enforces the 50+ eligibility); "not a public website"; "the behavior of all members… forms part of their profile"; community rules & guidelines collection with moderation/escalation; sexual-harassment/stalking policy detail; organizer/attendee liability guidance. (root, FAQ, collections)
- Layer A: membership tiers — Limited (free: public events/groups/discussions, create activities, receive messages with limited reply window) / Community Basic / Community Standard / Community Manager (paid unlocks private events/groups and fuller 1:1 browsing/messaging). (root, FAQ)

### Frolo (two-mode: Community + Dating)

- Layer A: positioning — "One app, two ways to connect: community & dating for single parents"; "private, members-only space where you can build friendships, find support, or meet someone special - all in one trusted app"; "3M+ messages sent, 50K+ meetups attended"; "The Frolo app has two modes - Community and Dating." (root)
- Layer A: Community mode surfaces — **Feed** ("share and seek guidance with the wider community"); **Chats** (private messages with connections + "join or create location or topic based 'Group Chats' which could be anything from 'Co-parenting tips' to 'Dublin frolos chat' to 'Recipe Exchange' to 'Frolo parents of SEN kids'"); **Discovery** ("search by Mum, Dad or both, parenting type, kids age, and location proximity"); **Meetups** ("find or create in real live and virtual meetups ranging from playdates, to Frolo nights out, to expert virtual meetups, to holidays and camping trips"). (Community page)
- Layer A: Dating mode — "A refreshing dating experience for single parents - and those who want to date them"; "Filter to find only other single parents or broaden your search for even more connections"; "everyone is who they say they are"; dating values (authentic / respectful / empowering). (Dating page; root)
- Layer A: community values framing — "We cherish our community / We empower each other / We are kind / We share safely"; "No shame or stigma here." (Community page)
- Layer B: the two modes are explicitly separated in product architecture while sharing one membership — the clearest two-mode realization in the sample.

### Christian Connection (dating site + member meetups + vendor events)

- Layer A: positioning — "Award Winning Christian Dating Site"; "Thousands of couples have started relationships and many more Christians have found friendship"; ice-breakers: "send a like, wave or profile reaction to get the conversation started… as you gain confidence, you can follow it up with a message." (root)
- Layer A: opportunities enumerated — "Browse photos and profiles of single Christians in your area; Send waves and messages; Attend meetups; Be in the loop for Christian dating events." (root)
- Layer A: events layer — "Dating events & free community meetups… we also run regular dating events where you can meet other single Christians in a fun, relaxed environment. You can also discover events near you with free meetups, or create your own! There are frequent gatherings in restaurants, bars, churches, museums or country walks." (root)
- Layer A: two event kinds distinguished — **Official Events** (vendor-run since 2001: speed dating, dance classes, comedy nights, guided walks; tickets via the Events for Christians site for "events hosted by Christian Connection and other approved organisers") vs **Local Meetups** ("member-run meetups. These gatherings are organised *by* Christian Connection members, *for* other members"; walks, bowling, evening meals, festival get-togethers; "Attend Meetup" option; email updates on time/venue changes; see who else is planning to attend). (Events page)
- Layer A: meetup governance — "Free local events. By CC members, for CC members… promoted on the site… Meetups are free to attend, except for the cost of any activity. Please be aware that these are unofficial events, which are not run or regulated by Christian Connection… Can't find any meetups near you? Why not organise one yourself, we'll promote it on the Weekly Review email." (What are Meetups?)
- Layer A: vendor events status — past events included speed dating, dance classes, quiz nights, comedy nights, talks/workshops, Christmas/Valentine's parties; "We are currently not running any events"; members "plan and run regular meetups." (What events do you run?)
- Layer A: helpdesk categories — Service / Logging On / Profile & Photos / Membership & Subscriptions / Messages (Wave, Favourites and Fans, Seen-at, recently-sent-only viewing) / App / **Events** / Privacy Safety & Security (scammer protection, meeting-up safety advice, blocking). (Helpdesk)
- Layer B: the dating loop is the primary product (search, waves, messages, subscription); the community layer is event/meetup-shaped rather than feed/group-shaped — the events-pole realization.

### Hornet (social-network-shaped partner discovery; root page only)

- Layer A: positioning — "Hornet, the Queer Social Network"; "over 100 million users worldwide… your go-to app for fun, engaging chat with gay men." (root)
- Layer A: navigation — Feed / Discover (grids/nearby) / Chat / Stories. (root)
- Layer A: community surfaces — "Be a part of discussions with Community Leaders on current topics and learn about the hottest trends all curated by Hornet's team of editors and a worldwide network of influencers"; "Browse the feed to see what's happening in the queer world"; short videos; "Hashtags allow you to discover other users who share your interests"; Feed "features posts by users you follow, users nearby, influencers, and users we think you'll want to connect with." (root)
- Layer A: partner discovery — "Filters enable you to find exactly who you're looking for and where you can find them"; Discover grids/nearby; "Meet anyone anytime - there's always someone online." (root)
- Layer A: safety — "Moderators and staff of Hornet ensure the community is a safe space"; privacy-first positioning; 24/7 support. (root)
- Layer B (limited): no match-gate language on the root surface; chat appears open. Support center unreachable — deeper structure (groups/communities, verification) not verified. Assertion strength reduced accordingly.

### Boundary cases (observed this pass)

- **Kippo** — "The Dating App for Gamers": match based on favorite games; card-deck profiles; "Direct Message and Chat with matches, send gifs, or invite to play together"; support FAQ is thin (SMS issues, countries, free tier, Infinity subscription). No community structures documented on any fetched surface → classifies as a niche **Dating Application**, not a community platform. Useful negative case: an interest niche alone does not make a community platform.
- **Stir** — help center (help.stir.com) shows the Match-family dating structure: Likes / Messages / Searching / Matching / Profile & Photos / Paid Features & Power-Ups / Advice and Safety / Manage My Subscription. No events or community category → niche **Dating Application** (Match Group's single-parent-focused product per market context; the fetched pages themselves only prove the dating-app structure).
- **FetLife, Taimi, ConnectingSingles, Mingle2, Thursday** — unreachable; carried as market context only: lifestyle/kink community with partner discovery (FetLife), LGBTQ+ social+dating (Taimi), community-structured free dating sites with forums/blogs (ConnectingSingles, Mingle2), events-first singles app (Thursday, title: "Events, Everyone Single. Every Week"). No operational claims drawn from them.

## Cross-product Comparison

| Finding | Her | Stitch | Frolo | Christian Connection | Hornet | Level |
|---|---|---|---|---|---|---|
| Bounded member community (join; eligibility/verification gate) | yes (app + social-media verification) | yes (mandatory verification; 50+ gate) | yes (members-only) | yes (email confirm; scam protection) | yes (join; 100M users) | L0 |
| Shared participatory community spaces (first-class) | Communities (topic feed) + events | Activities, Groups, Discussions, Travel | Feed, Group Chats, Meetups | Member meetups + vendor events | Feed, Stories, hashtags, Community Leaders | L0 |
| Partner-oriented member profiles | yes (Meet) | yes (Members page, companionship settings) | yes (Dating mode) | yes (profiles, photos) | yes (profiles, grids) | L0 |
| Discovery of members as potential partners over the pool | Meet swipe + community fallback | Members directory + suggestions + community | Dating mode + community Discovery search | browse/search + Discover filters | Discover grids + hashtags + filters | L0 |
| Community participation as designed path to meeting partners | explicit ("hop into the Feed/Community…") | explicit ("best connections happen through shared experiences"; marriage via forum) | explicit (two modes, one membership) | explicit (meetups to "mix and mingle… expand your network") | implicit (feed/hashtags → chat) | L0 |
| 1:1 messaging layer | chat after match (gated) | direct messages (verification-gated) | private messages with connections | messages (subscription-gated) | open chat | L1 (gate = L2 variant) |
| Member-created events/activities with organizer roles | events viewed (creation not verified) | any member suggests/creates; co-organizers; waitlists; attendance | find or create meetups | member-run meetups + vendor events | not observed | L1 |
| Topic/interest groups with join/leave | Communities join/leave | Groups (Regular/Public/Private) | Group Chats (location/topic) | not observed | not verified | L1 |
| Community feed with posts/reactions/comments | yes | Discussions (topic threads) | yes | not observed | yes | L1 |
| Moderation & guidelines; report/block | yes (moderators, report) | yes (rules collection, escalation, feedback) | values + child-safety policy | yes (safety team, ODDA) | yes (moderators) | L1 |
| Multi-intent framing (friendship + romance) | Add Friend + dating | companionship spectrum | two modes | friendship + dating | social + dating | L1 |
| Membership tiers gating depth | free core + Premium | Limited + 3 paid tiers | free to join (blog) | free + full subscription | free (root) | L2 |
| Contact gate (mutual-consent match) | yes | no (open, verified messaging) | not verified | no (waves/messages, subscription-gated) | no (open chat) | L2 — variant |
| Two-mode architecture (explicit mode switch) | blended | blended (sections, not modes) | explicit (Community/Dating modes) | blended | blended | L2 |
| Identity-niche segmentation | queer women/nonbinary/trans | 50+ | single parents | Christians | gay men/queer | L2 |
| Vendor-run official events | not verified | members only (third-party orgs restricted) | — | yes (currently paused) | not observed | L2 |
| Travel/trips machinery | not observed | Stitch Travel (Beta) | meetups incl. trips | not observed | virtual travel feature | L2 |
| Presence/activity signals | last online (Premium filter) | Most responsive/Recently active directory sections | not observed | Seen-at on messages | "always someone online" | L2 |
| Branded mechanics/claims | Pride Pins, 35+ communities, 15M+ members | Champions, Welcomer/Pioneer Programs, Rewards, first-marriage anecdote | 3M+ messages/50K+ meetups claims, values framing | Wave, Favourites/Fans, Weekly Review email, ODDA | Community Leaders, editors/influencers, virtual travel | L3 |

## L0 — Defining Invariant

```text
Bounded Member Community
(membership join; population defined by the platform,
 commonly with an eligibility/verification gate)
└── Shared Participatory Community Spaces as first-class structures
    (groups, discussions/forums, events/activities, community feed —
     at least one family of these, with member participation mechanics)
└── Partner-oriented Member Profiles
    (self-presentation usable for romantic/lifestyle partner evaluation)
└── Discovery of Members as Potential Partners over the community's own pool
    (browse / search / suggest / match)
└── Integration: community spaces and partner discovery are one product;
    community participation is an explicit, designed path to meeting partners
```

Remove-tests:

- remove the shared community spaces → a Dating Application (candidate loop only)
- remove partner discovery / romantic orientation → a Community Platform or Interest-based Social Network (§01.06/§01.05) — Stitch's own Meetup comparison is the vendor-articulated version of this test
- remove member profiles / discoverability → a content forum
- remove the bounded community container → open classifieds/directory, not a community

Note what is deliberately NOT in L0:

- **The contact gate.** In a Dating Application the mediated contact gate is definitional. Here it is a variant: Her gates chat behind mutual match; Stitch, Hornet, and Christian Connection allow direct messaging gated by verification, subscription, or nothing. The community context itself (shared spaces, visible behavior, moderation) carries the trust load instead.
- **Any specific community-surface type.** Groups, forums, events, and feeds are interchangeable realizations; Hornet gets by with feed+hashtags, Christian Connection with meetups alone.
- **Multi-mode architecture.** Frolo's explicit mode switch is one realization; blended single-surface products (Stitch, Her) are equally valid.

## L1 — Common Mature Structure

```text
1:1 messaging layer (direct messages; gate varies — see L2)
Member-created events/activities with organizer roles
  (create/suggest, RSVP/attend, co-organizers, waitlists, attendance marking)
Topic/interest groups with join/leave and group-scoped content
Community feed with posts, reactions, comments, tagging
Moderation & community guidelines (report, block, escalation)
Verification before communication (mandatory in community-heavy products)
Multi-intent framing (friendship + romance; companionship spectrum)
Member directories with sorting (newest / closest / most active / matched)
Membership tiers gating community vs 1:1 depth
Safety machinery (meetup safety advice, liability guidance, harassment policies)
Presence/activity signals
```

## L2 — Variant / Optional Structure

```text
Contact gate posture
- mutual-consent match gate (dating-app style; documented at Her)
- open messaging gated by verification (Stitch), subscription (Christian
  Connection), or neither (Hornet root surface)

Architecture
- explicit two-mode (Community mode + Dating mode; Frolo)
- blended single surface with sections (Stitch, Her)
- social-network-shaped (feed/follow-first; Hornet pole)

Community-surface mix
- groups-centric / discussions-centric / events-centric / feed-centric
- member-created vs vendor-run official events vs both (Christian Connection
  runs both kinds and distinguishes them explicitly)

Segmentation
- identity niches: queer (Her, Hornet), age (Stitch 50+), life stage (Frolo
  single parents), faith (Christian Connection), lifestyle/kink (FetLife,
  market context)
- eligibility gates (age verification at Stitch)

Commercial & program machinery
- membership tiers; freemium vs subscription; rewards/points programs
- commercial-activity prohibitions; advertising posture (Stitch bans both)
- travel/trips programs; virtual events/video chat
```

## L3 — Vendor-specific Structure

Kept out of the Application Document:

- Stitch: Community Champions, Welcomer Program, Pioneer Program, Stitch Rewards (points/status levels), Stitch Travel (Beta), Stitch Video Chat, activity publication review, membership tier names and prices ($60/$120/$180 per year), "Stitch vs Meetup" comparison article, "first marriage via Discussions forum" anecdote, "You don't USE Stitch. You JOIN." slogan
- Her: Pride Pins, 35+ communities / 15M+ members claims, Premium feature set (incognito, rewind, who-viewed, unlimited swipes), social-media-account verification, Communities tab navigation details
- Frolo: named group-chat examples, 3M+ messages / 50K+ meetups claims, values framing, two-mode screenshots, "now free to join" pricing blog
- Christian Connection: Wave, Favourites and Fans, Seen-at, recently-sent-only message viewing, Weekly Review email promotion, Events for Christians ticketing site, ODDA founding membership, "not run or regulated" meetup disclaimer, "currently not running any events" status
- Hornet: Community Leaders program, editors/influencers curation, virtual travel feature, hashtag discovery

## Historical / Market-Sample Check (§24)

Question: would older, regional, platform-native, or differently positioned products still fit the L0?

- **Community-structured dating sites (2000s era)**: free dating sites organized around forums/blogs/groups/chat rooms with profiles and search (ConnectingSingles, DateHookup, Mingle2; Plenty of Fish's forums era; OkCupid's journals era) satisfy the L0 — community spaces + partner profiles + pool discovery. The modern feed/groups shape is not definitional; forums and chat rooms are equivalent realizations. (Market context; those sites were unreachable this pass — structural inference only, marked as such.)
- **Lifestyle/kink communities**: FetLife-class products (community-first: groups, events, discussions; profiles; open messaging; no match gate) satisfy the L0 with the open-messaging gate posture. (Market context; unreachable.)
- **Events-first singles platforms**: Thursday-class products (singles events as the spine) satisfy the L0 with an events-centric surface mix. (Market context; title-only evidence.)
- **Platform-native**: no OS-native analog exists for this Type; the web-era community sites are the "older pole".
- **Non-community dating products** (Tinder-class): fail the L0 (no shared community spaces) — correctly excluded, they remain Dating Applications.
- **Community platforms without partner discovery** (Meetup-class): fail the L0 — Stitch's own comparison article draws exactly this line ("designed to serve the goal of finding companionship, rather than being an end to themselves").

Conclusion: the L0 holds across eras and positions; no single surface type, gate posture, or architecture is definitional.

## Vendor-specific Findings

See L3 above. Additional notes:

- Stitch is the only sampled product with mandatory verification-before-communication and an explicit commercial-activity ban; both are strengths of its community-first posture, not Type requirements.
- Christian Connection is the only sampled product that runs (or ran) vendor-run official events alongside member-run meetups, and the only one with an explicit "unofficial, not run or regulated" disclaimer for member events — a liability pattern worth noting as common practice for member-created events, evidenced here at one product.
- Her is the only sampled product where the mutual-match gate and first-class communities coexist at full strength — the hybrid overlap zone.

## Boundary Findings

### vs Dating Application (sibling §01.07) — joint-review flag resolution

Sharpest seam. The distinguishing test is **which structure organizes the product**:

- Dating Application: the 1:1 candidate loop (profile → discover → like/pass → gate → chat) is the organizing structure; community surfaces are absent or peripheral add-ons. The mediated contact gate is definitional there.
- Dating Community Platform: shared community spaces are first-class structures alongside partner discovery, and community participation is a designed path to meeting partners. The contact gate is optional (open messaging is equally common) because the community context carries trust.

Corollary: the same feature (chat) has different definitional status in the two Types — gated candidate-loop chat defines Dating Application; community-contextualized open-or-gated messaging is just the 1:1 layer here.

**Hybrid overlap zone**: Her carries both structures at full strength (full swipe/match loop + dedicated Communities tab + events + Add Friend). Products like this straddle the seam; either classification is defensible, and the directory keeps both Types with the organizing-structure test as the discriminator. Recommendation recorded: **keep the family split** (two Types), with the overlap zone documented on both sides. Kippo and Stir confirm the negative direction: interest/life-stage niches without community structures are Dating Applications, not this Type.

### vs Community Platform / Interest Community Platform (§01.06)

§01.06 communities exist for discussion/content belonging; partner discovery is absent or incidental. Here partner discovery is a first-class purpose with dedicated structures (partner-oriented profiles, pool discovery). Stitch's vendor-articulated boundary vs Meetup is the cleanest statement: same surface machinery (groups, events), different purpose. Test: remove partner discovery → §01.06. Note the drift case: Meetup's "Sydney Singles 35+" groups show a generic community platform hosting dating-oriented groups without becoming this Type — the platform's purpose, not a group's topic, decides.

### vs Interest-based Social Network / General Social Network (§01.05)

Hornet pole: social-network-shaped products (feed, follow, stories) with partner discovery. Seam: in a social network the profile/feed/follow graph is the center and partner-finding is one use among many; here partner discovery is a first-class purpose with dedicated discovery structures. Hornet straddles (root-page evidence only) — recorded as a boundary case, not resolved.

### vs Friend Discovery Application (§01.05)

Same community mechanics, friendship-only intent. Multi-intent products (Stitch's companionship spectrum, Frolo, Her's Add Friend) span both; the romantic/lifestyle partner layer is what makes this Type. Stitch's "we don't call it a dating site" positioning is marketing framing, not taxonomy — romance remains a first-class intended outcome there.

### vs Matchmaking Platform (sibling §01.07, unprocessed)

Service-led introductions (a service selects and introduces candidates) vs self-service community participation. Not observed in this sample; the seam from the dating-application pass stands unchanged.

### vs Event Management Platform / Event Registration (§26)

Those are organizer-side tools for producing events as commercial/logistic objects. Here events are a community surface inside a member community: member-created, free-or-cost-sharing, with the relationship outcome as the point. Stitch's activity payments (organizer rules, attendee payments) are member-to-member cost sharing, not ticketing commerce. Test: who operates the event and why.

### vs Instant Messaging (§01.01) / Random Video Chat / Live Social (§01.08)

No persistent community container or partner-discovery layer in those Types; messaging here is one layer among several, anchored to the community membership.

## Uncertainties

- FetLife, Taimi, ConnectingSingles, Mingle2, Thursday were unreachable; the lifestyle-community, LGBTQ+-hybrid-second-sample, forums-pole, and events-first poles rest on market context, not direct evidence. No operational claims are drawn from them.
- Hornet evidence is root-page only (support timed out ×2); group/community structures, verification, and monetization at Hornet are unverified.
- Frolo Dating's exact mechanics (whether a like/match gate exists) are not documented on the fetched pages; not asserted.
- Her's event creation (who can create events) is not verified from fetched pages.
- Whether the "community-first pole" products (FetLife-class) would accept the "dating" framing is a positioning question; Stitch explicitly rejects the "dating site" label while keeping romance first-class — recorded as positioning, not taxonomy.
- The relative weight of the community layer vs the dating layer varies continuously across products; the L0 draws a binary line (community spaces first-class or not), but real products form a spectrum. The hybrid overlap zone (Her) is documented rather than forced to one side.
- Directory siblings matchmaking-platform and relationship-discovery-application remain unprocessed; the intra-family seams involving them are unchanged from the dating-application pass.

## Final Synthesis

```text
L0 (defining invariant)
- Bounded member community (join; commonly eligibility/verification-gated)
- Shared participatory community spaces as first-class structures
  (groups / discussions / events / feed — at least one family)
- Partner-oriented member profiles
- Discovery of members as potential partners over the community's own pool
- Integration: community participation is an explicit, designed path
  to meeting partners

L1 (common mature structure)
- 1:1 messaging layer; member-created events with organizer roles;
  topic groups; community feed; moderation/guidelines; verification;
  multi-intent framing; member directories; membership tiers; safety
  machinery; presence signals

L2 (variant / optional)
- contact-gate posture (match gate vs open/verified/subscription-gated
  messaging); two-mode vs blended vs social-network-shaped architecture;
  community-surface mix; identity-niche segmentation; vendor-run vs
  member-run events; travel/rewards/commercial-ban postures

L3 (vendor-specific)
- Champions/Welcomer/Pioneer/Rewards/Travel (Stitch); Pride Pins/Premium
  (Her); named group chats/values framing (Frolo); Wave/Favourites/Weekly
  Review/ODDA (Christian Connection); Community Leaders/virtual travel
  (Hornet)
```

Joint-review outcome for the dating-application flag: **keep the family split** — Dating Application (candidate loop organizes; contact gate definitional) vs Dating Community Platform (community container + partner discovery integrated; contact gate optional). Her-class hybrids documented as the overlap zone. relationship-discovery-application remains a probable umbrella alias (unchanged, for its own pass).
