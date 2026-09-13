# Research Notes — Interest Community Platform

## Research Goal

Understand the Application Type behind the directory leaf **Interest Community Platform** (§01.06 Community & Discussion): what the application is, who uses it, what its core objects and workflows are, and where it sits against the already-processed siblings — Community Platform (§01.06), Interest-based Social Network (§01.05), Community Chat Platform (§01.01), Discussion Board (§01.06) — and the unprocessed siblings Online Forum and Q&A Community.

Two incoming flags must be resolved by this pass:

1. From the **community-platform** pass (STATUS.md): interest-community-platform flagged **VARIANT-RISK** — "audience-axis variant (interest communities are frequently run ON community platforms)". This pass must confirm or refute variant status.
2. From the **interest-based-social-network** pass (STATUS.md): Douban/Ravelry-class community-heavy interest networks were kept in the network Type by center of gravity; "the interest-community-platform pass should confirm the **container-vs-network seam**".

## Initial Boundary

Working hypothesis before research:

- The leaf most plausibly denotes a **venue of many member communities organized around interests** (Reddit-class): communities are first-class joinable units, scoped by topic, hosted many-at-a-time under one platform identity.
- Adjacent confusables: Community Platform (operator-run single container software), Online Forum (single standing venue), Community Chat Platform (chat rooms in a container), Interest-based Social Network (profile-and-stream spine), social-network group features.
- Unknowns: whether "interest anchoring" is definitional or merely typical; whether multi-community hosting is definitional or an implementation posture; whether voting/discussion threads are required; evidence access for consumer-social products (prior passes hit widespread 403s).

## Research Questions

1. What is the central object of the application — the community, the person, the board, or the room?
2. How does a community come into being, and who creates it?
3. What does membership mean: is there a join/subscribe act, and what does it change?
4. Does one user account span multiple communities? What does the personal home surface aggregate?
5. What is the participation surface: threads, events, media, chat?
6. How is governance structured: community-level vs platform-level?
7. How are communities discovered: directories, search, recommendations, targeted announcement?
8. Where is the seam against the Community Platform (operated container), the Interest-based Social Network (profile spine), the Community Chat Platform (live rooms), and the Online Forum (single venue)?
9. Would older/regional realizations (Usenet newsgroups, Yahoo!-class email groups, Baidu Tieba) still satisfy the definition?

## Representative Products

Selection rationale: market representativeness + documentation completeness + different product philosophies + different customer layers (ad-funded consumer venue / paid-organizer two-sided market / non-commercial federated / regional mega-platform).

| Product | Posture | Evidence level reached |
|---|---|---|
| Reddit | ad-funded consumer venue of interest communities | corporate/product positioning only (help center 403) |
| Meetup | event-anchored interest groups; organizer-paid two-sided market | help center, Tier-1 articles (rich) |
| Lemmy | federated, self-hostable, non-commercial community discussion | official docs, Tier-1 (rich) |
| Amino Apps | mobile-first fandom interest communities | NOT REACHED — abandoned (see Sources/limitations) |
| Baidu Tieba | regional (China) interest-community platform, founded 2003 | NOT REACHED (403) — historical/regional anchor by reasoning only |

## Sources

- Reddit — corporate site/product positioning: https://www.redditinc.com/ (fetched 2026-09-08, includes "How does Reddit work?" product explanation: post/comment/vote in "communities organized around their interests")
- Reddit — help center: https://support.reddithelp.com/hc/en-us → **403, unreachable** (1 attempt, abandoned)
- Reddit — wiki FAQ: https://www.reddit.com/wiki/faq/ → **timeout** (1 attempt, abandoned)
- Meetup — Help Center home: https://help.meetup.com/hc/en-us (fetched 2026-09-08)
- Meetup — category "Groups and Communications": /hc/en-us/categories/39488576274573 (first attempt 403, retry succeeded)
- Meetup — section "All about Meetup Groups" (organizer): /hc/en-us/sections/39488600077197
- Meetup — section "Create and Manage your Group": /hc/en-us/sections/39488592030221
- Meetup — article "Starting a Meetup group and publishing your first event": /hc/en-us/articles/39233113742477
- Meetup — article "What is a Meetup group?": /hc/en-us/articles/39428296398093
- Meetup — article "Joining a Meetup group": /hc/en-us/articles/39234752483853
- Meetup — section "Participating in Events": /hc/en-us/sections/39488935111949
- Meetup — category "Events": /hc/en-us/categories/39488950343693
- Lemmy — official site: https://join-lemmy.org/ (fetched 2026-09-08)
- Lemmy — docs Introduction: https://join-lemmy.org/docs/index.html
- Lemmy — docs Getting Started: https://join-lemmy.org/docs/users/01-getting-started.html
- Lemmy — guessed moderation-doc path → 404 (1 attempt, stopped)
- Amino — https://support.aminoapps.com/hc/en-us (timeout ×2) and https://aminoapps.com/ (timeout ×1) — **abandoned**
- Baidu Tieba — https://tieba.baidu.com/ → **403** (1 attempt, abandoned)

Research date: 2026-09-08.

**Source-access limitation (binding for the final document):** Reddit, Amino, and Baidu Tieba official operational documentation could not be retrieved. Reddit's contribution is official product-positioning text (corporate site) only; Amino and Tieba serve as market/structural anchors with **no product-level claims** anywhere. The abstraction therefore rests on Meetup (Tier-1, event-anchored pole) and Lemmy (Tier-1, federated discussion pole), plus Reddit positioning. No precise numeric limits, defaults, or time windows are asserted for any product beyond what the fetched pages state.

## Product Observations

### Reddit (official product-positioning evidence only — corporate site)

Evidence layer: A (direct, but positioning-level — no operational docs).

- Self-description: "The heart of the internet… Reddit is home to **thousands of communities**, endless conversation, and authentic human connection. Whether you're into breaking news, sports, TV fan theories… there's a community on Reddit for you."
- "How does Reddit work? Every day, millions of people around the world post, vote, and comment in **communities organized around their interests**."
- The product explanation names exactly three participation primitives: **Post** ("The community can share content by posting stories, links, images, and videos"), **Comment** ("The community comments on posts"), **Vote** ("Comments & posts can be upvoted or downvoted. The most interesting content rises to the top").
- Headline metrics include "**Active communities**" — the community is the counted unit of the product.
- Site structure names: "Reddit for Community", "Reddit Rules", "Moderator Code of Conduct" — a platform-rules layer and a moderator layer coexist.
- No operational detail retrieved (join mechanics, creation flow, moderation tooling internals — all unverified this pass).

### Meetup (Tier-1 help center — event-anchored pole)

Evidence layer: A (direct, operational).

- Definition of the unit: "Meetup is about connecting people with something in common… **a Meetup group is a community**. A community of people who come together because they care about the same thing. Mountain climbers, first-time parents, aspiring circus performers, coders… you name it, there's a good chance there's a Meetup group for it (and if there isn't, maybe you should create one)." → the unit is an interest-scoped community; the catalog is open-ended ("if there isn't… create one").
- Multi-membership: the Find page surfaces "groups and events based on your location and interests. **Join one, join ten. Join as many as you want.**" → one account, many group memberships, explicitly.
- The join act: "Log in… Go to the homepage of the group you want to join… Click Join this group. Depending on the group's settings, you will either: become a member right away, or wait for the organizer to approve your request." Joined groups surface as "Your groups". Leaving is supported.
- Community lifecycle (organizer side): choose a group name, write a description ("describe the purpose of your group, who the ideal members are, and what members should expect to learn and do together… Clearly list any requirements, **group rules**"), sign up for an **organizer subscription** ("compulsory for all organizers") before organizer tools unlock.
- **Platform review gate**: "a member of our team reviews it based on our community guidelines and makes sure it gets promoted to the right people… a decision by email within 24 hours… whether your group was accepted, still needs editing, or was rejected. Until then, your group and its related events **aren't searchable by or announced to the Meetup community**." → communities are not discoverable until they pass a platform-level review against platform-wide guidelines.
- Discovery machinery: "Shortly after a group is approved, we'll help share it with interested members in your area. This announcement is **targeted to members who have similar interests** to your group and invites them to join." → interest-targeted, locality-scoped distribution.
- Participation surface: "While the connections begin online, the real memories are made at **events**. Meetup events are real-life gatherings where members and organizers get together to connect, discuss, and practice activities related to their shared interests." Event machinery: create/manage events, attendee management, waitlists, "Your event ticket and QR code", refunds for event fees, uploading photos of an event, sharing feedback/reviews about an event, attendance history per group, event chats and third-party messaging.
- Communication: "Messages and Communications" surfaces for groups and members.
- Monetization: organizer subscriptions (Starter/Standard/Pro tiers named in pricing article titles), "Meetup+" member tier, plus organizer-side "ticketed events or member dues" ("Meetup proudly supports flexible monetization strategies, so you can offset your organizing costs with ticketed events or member dues").
- Governance roles observed: organizer (runs the group, approves members), Meetup team (platform review/enforcement), attendee/member. Organizer succession exists: "Stepping up as new Organizer of a Meetup group" — a group can change hands rather than die.

### Lemmy (Tier-1 docs — federated discussion pole)

Evidence layer: A (direct, operational).

- Definition: "Lemmy is a selfhosted, federated social link aggregation and discussion forum. It **consists of many different communities which are focused on different topics**. Users can post text, links or images and discuss it with others. Voting helps to bring the most interesting items to the top. There are **strong moderation tools** to keep out spam and trolls."
- Deployment substrate: many interconnected **instances** (servers) run by different operators, each with its own topics and rules; federation (ActivityPub) lets a user on one instance "follow a Facebook group from your Reddit account"-style interact with communities elsewhere. A community has a federated address (e.g. `!main@feddit.org`).
- The join act: "**Following Communities**… you can directly **subscribe** to communities… click on the community name to **browse the community first, see what its posted and what the rules are before subscribing**." Community rules are a first-class surface (sidebar, below the Subscribe button).
- Discovery: a communities list "filtered by subscribed, local or all" (local = hosted on your instance; all = federated); browsing the front page and subscribing from post sidebars; external discovery ("Lemmy Explorer") for communities not yet known to your instance.
- The personal timeline: front-page "Type" setting chooses "only posts from communities that you **subscribe** to, posts in local communities, or all posts including federated" → the home feed is assembled from community subscriptions.
- Participation: comment (top-level or nested reply), create post (mandatory title; optional link/image/body; **a Community dropdown allows choosing a different community to post in**; NSFW marking; language selection). → posting targets a community; subscription and posting are distinct acts.
- Identity/profile: username (immutable, unique per instance) + display name + bio + avatar + banner; blocking of **users and communities** ("so that their posts will be hidden") — community-level blocking exists as a user control.
- Governance: community-level rules visible on each community; "**Moderation actions are transparent and can be viewed in the mod log**"; instance-level registration gating (admin-set application question with manual approval, mandatory email, captchas, NSFW content opt-in) — two governance layers (community moderation + instance administration) both evidenced.
- Extra surfaces: private messages between users, notifications (in-app + email), RSS/Atom feeds for community/user/subscribed views, "Full vote scores like old Reddit", NSFW post/community support, bot accounts.
- Non-commercial posture: "no advertising, tracking, nor secret algorithms… funded solely by donations."

### Amino Apps (NOT REACHED — structural anchor only)

No official documentation retrieved (support site timed out ×2, main site timed out ×1). Used in research reasoning only as a widely-cited mobile-first fandom-community product. **No product-specific claims appear in the final document.**

### Baidu Tieba (NOT REACHED — regional/historical anchor only)

Official site returned 403. Used only as a reasoning-level check that the Type has long-standing regional realizations organized as topic-scoped communities ("bars") under one account. **No product-specific claims appear in the final document.**

## Cross-product Comparison

| Structure | Reddit | Meetup | Lemmy | Amino / Tieba (anchor only) |
|---|---|---|---|---|
| Community as named, first-class unit | Yes — "communities" are the counted unit | Yes — "a Meetup group is a community" | Yes — "consists of many different communities" | yes (public knowledge) |
| Interest/topic scoping of the unit | "communities organized around their interests" | group purpose/ideal members/rules in description; review against community guidelines | "communities which are focused on different topics"; per-community rules | yes (public knowledge) |
| Many communities per platform, one user account spanning them | "thousands of communities" (one product) | "Join one, join ten. Join as many as you want." | subscribe across instances via federation | yes (public knowledge) |
| Join/subscribe act per community | structural (not op.-verified) | Join this group; immediate or organizer approval | subscribe; community rules shown before subscribing | — |
| Persistent content organized inside the community | posts + comments (stories/links/images/videos) | groups hold events, photos, attendance history, messages | posts + threaded comments persist per community | — |
| Voting/ranking | post/comment up/down votes | not observed (feedback/reviews instead) | up/down votes, sort options | — |
| Discovery of communities | platform-level (positioning-level only) | Find page (location + interests) + targeted announcements to similar-interest members | communities list (subscribed/local/all) + federation search | — |
| Home surface aggregates joined communities | structural | "Your groups"; homepage lists groups | front page = subscribed timeline | — |
| Two-layer governance (community + platform) | Moderator Code of Conduct + Reddit Rules (structural) | organizer approval + Meetup team review/enforcement | community rules/mod log + instance admin registration gating | — |
| Events as participation surface | not evidenced | core (RSVP/waitlist/ticket/photos/feedback) | none evidenced | — |
| Real-time chat as primary object | no | no (event chats are side surface) | no (private messages side surface) | — |
| Monetization | ad-funded posture (structural) | organizer subscriptions + member dues + Meetup+ | donations, non-commercial | — |
| Deployment | single hosted venue | single hosted venue | federated, self-hostable, multi-app clients | — |

**Cross-product reading:** the three directly-documented products agree on the same skeleton — a platform hosting many interest-scoped communities, each joinable, each holding persistent member-contributed content, with community-level governance nested under platform-level governance, and a personal home surface assembled from one's community memberships. They disagree — product philosophically, not structurally — on the participation anchor (discussion threads vs real-life events), on voting, on monetization, and on deployment. That disagreement pattern (shared skeleton, divergent emphasis) is the signature of one Application Type with variants, not of two Types.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The interest community as a first-class unit.** A named, membership-holding container explicitly scoped by a shared interest or topic; the scope is stated (description/purpose/rules) and governs what belongs in the community. Remove the interest scoping → generic group features of a social platform; remove the container entirely → a profile-centric network.
2. **A multi-community venue under one account.** The application hosts many such communities in parallel and makes them discoverable (listing/search/announcement); one user identity holds memberships in several communities simultaneously, and the personal home surface is assembled from those memberships. Remove multi-community hosting → a single-community site (an online forum or an operated community platform); remove member-side discoverability → private groups only, no venue.
3. **Persistent member participation inside the community.** Members contribute content that organizes within the community's space — discussion posts with replies, event records, shared media — and persists as the community's readable archive. Remove participation → a directory/listing of communities; make the live stream the primary object → Community Chat Platform territory.

Jointly-held is load-bearing: (1)+(3) without (2) = a single interest forum or one operated community; (1)+(2) without (3) = a discovery directory; (2)+(3) without (1) = a social platform with arbitrary personal groups.

### L1 — Common Mature Structure (cross-product, not definitional)

- Community discovery surfaces (directory/filter/search; interest- and locality-scoped suggestions; targeted announcement of new communities)
- Voting/ranking on posts and comments (Reddit, Lemmy — absent in the event-anchored pole, so common-but-not-universal)
- Threaded discussion with replies; media attachments (links/images/video)
- Community rules as a visible, first-class surface
- Two-layer governance machinery (community moderator/organizer powers; platform rules and admin/review enforcement; mod log transparency in one product)
- Member profiles carrying participation (joined groups, attendance history, bio/avatar)
- Personal home feed aggregating joined communities; per-community notification controls
- Member-to-member messaging and event/chat side surfaces
- Blocking/muting of users and, in one product, of whole communities
- NSFW/adult-content classification at post and community level (where present)

### L2 — Variant / Optional Structure

- Participation anchor: discussion-thread communities vs real-life event communities vs (structurally adjacent) chat rooms
- Deployment: single hosted venue vs federated multi-instance network; commercial vs non-commercial
- Creation posture: who may create a community and what vetting applies (documented: member-initiated creation with a platform review gate in the event-anchored pole; creation postures vary and are not universalized)
- Membership gating: immediate join vs organizer/admin approval; platform-level account gating (application questions, email confirmation) vs open signup
- Identity posture: pseudonymous usernames vs real-name-leaning profiles
- Monetization: advertising, organizer subscriptions, member dues, paid member tiers, ticketed events, donations
- Regional/regionalized mega-platforms and email/newsgroup-era realizations as historical variants

### L3 — Vendor-specific (kept out of the final document)

Reddit karma/awards/mod-tooling specifics and the "subreddit" naming; Meetup's named subscription tiers (Starter/Standard/Pro), "Meetup+", ChatGPT-assisted group descriptions, 24-hour review window; Lemmy's ActivityPub addressing (`!community@instance`), Lemmy Explorer, bot-account flags, RSS exports. Tieba bar-level systems — unverified, unasserted.

## Vendor-specific Findings

- Meetup: organizer subscription is compulsory before organizer tools unlock; platform review gates discoverability; interest-targeted announcement of approved groups; event machinery (waitlist, QR tickets, photo albums, event feedback, attendance history); organizer succession.
- Lemmy: federation substrate (instances, ActivityPub, cross-instance subscribe and reply); instance-level registration gating including admin-answered questions; community blocking; mod log transparency.
- Reddit: post/comment/vote triad as the officially explained model; "Moderator Code of Conduct" as a named platform instrument.

## Boundary Findings

1. **vs Community Platform (§01.06, processed) — resolves its VARIANT-RISK flag: keep-both.** The processed sibling is organization-operated software: the container is created/owned by an organization distinct from its members, sold to that operator, and instrumented for operator management and engagement measurement. This Type is the members' venue: many communities hosted in parallel, discovered and joined by members; the community unit — not an organization's container — is the spine. Removal tests hold both ways: remove the operator/owner organization and operator analytics from a community-platform deployment and a members' venue can remain (this Type); remove the multi-community venue and member-side discovery from this Type and what remains is one managed container (the sibling). Interest communities *run on* community-platform software (a hobby club on a Circle-class product) are instances of the sibling Type, not of this one; conversely a Reddit-class venue is not sold to a container-owning organization. Overlap zone: small single-interest communities exist in both; the seam is one-operated-container vs many-member-joined-units.
2. **vs Interest-based Social Network (§01.05, processed) — container-vs-network seam CONFIRMED from this side.** There, the member's profile-as-interest-record is the spine and content binds to a domain's objects (film/book/route/pattern); groups/forums are optional containers. Here, the community unit is the spine: content binds to communities, profiles are thin participation records, and the home surface aggregates joined communities rather than followed people. Douban/Ravelry-class products (profile + domain-keyed loop primary, groups as containers) stay in the network Type; Reddit/Meetup-class products (community unit primary) come here.
3. **vs Community Chat Platform (§01.01, processed).** Both can be multi-community venues with interest scoping (chat "servers"). The seam is the primary object: live rooms with real-time message streams vs persistent asynchronous content (threads/events) as the community's asset. No sampled product here is chat-first; chat appears as side surface (event chats, private messages). Seam held from this side, consistent with the chat pass's own record.
4. **vs Online Forum (§01.06, unprocessed).** A forum is a single standing venue organized around boards/topics; a board is a section of the venue, not itself a joinable community with its own membership and scope. This Type's unit carries membership. The online-forum pass should check the seam from its side; alias-risk flags from the discussion-board and community-platform passes remain open for that pass.
5. **vs Q&A Community (§01.06, unprocessed).** Format seam: participation organized around question/answer pairs with accepted answers vs the community unit. Q&A machinery can exist inside communities (as it does inside community platforms) without being the Type.
6. **vs Discussion Board (§01.06, processed).** The topic-and-reply surface is a tool; this Type supplies the venue of joinable communities in which such surfaces typically live. A discussion board without community membership does not satisfy this Type's core.
7. **Other keys that can scope a community container** — locality (Neighborhood Social Network), partner discovery (Dating Community Platform), organizational membership (Member Community Platform / AMS family). The interest key is what keeps this leaf distinct from those.
8. **Anonymous interest boards** (no membership, no accounts) fail structure L0-1/L0-2's membership basis; treated as outside this Type (reasoning-level; no fetched source).

## Historical / Market-Sample Check

Would older, regional, or platform-native products still fit?

- **Usenet newsgroups** (reasoning-level, no fetched source): hierarchically organized topic groups (rec.*, comp.*), each a named topic-scoped unit; users subscribed from one news account; articles persisted in threads per group; group-level moderation conventions and gateway hierarchies existed under a transport-level governance layer. Satisfies all three L0 structures with none of the modern machinery (no voting, no media, no apps, no feeds) → the core is not overfit to modern implementations.
- **Yahoo!-class email interest groups / mailing-list communities** (reasoning-level): named interest groups joined by subscription, persistent threaded archives, member contributions, list-owner + provider governance. Satisfies the core.
- **Baidu Tieba (2003, China)**: topic-scoped communities ("bars") under one account at regional scale — fits the core as a regional anchor, but **not directly researched this pass** (403); carried as an anchor only, no product claims.
- Conclusion: the defining core survives the historical/regional check; modern features (voting, media, apps, feeds, subscriptions) stay out of the core.

## Uncertainties

1. Reddit operational documentation (join mechanics, community creation flow, moderation internals, karma) was unreachable — all Reddit statements in the final document are positioning-level; no operational claim rests on Reddit alone.
2. Amino and Baidu Tieba were not researched at all; the mobile-fandom and regional poles are carried by market knowledge at anchor level only. If a later pass reaches their docs, the variant list should be re-checked.
3. Community-creation postures: only the event-anchored pole documents member-initiated creation with a platform review gate. Whether open member-creation without review is a common posture could not be verified across the sample — the final document phrases creation posture as varying by product.
4. Whether voting is "standard" or "common": evidenced in two of three directly-documented products; written as common-but-not-universal.
5. Community end-of-life behavior (archival, locking, banning of communities) was not directly evidenced; deliberately absent from the final document.
6. The 24-hour review window, subscription tier names, and similar figures are Meetup-specific facts, recorded here and in the final document's product notes only where the fetched page states them; no other numeric claims are made.

## Final Synthesis

An **Interest Community Platform** is a venue that hosts many member communities as first-class, discoverable units, each scoped by a shared interest and each holding persistent member-contributed content, with one user account spanning memberships across communities and governance exercised in two layers — community-level (creator/organizer/moderators, rules) under platform-level (site rules, review, admin enforcement). The Type stands as a distinct leaf: it is neither an operator's community container (Community Platform), nor a profile-and-stream interest network (Interest-based Social Network), nor a live-room chat venue (Community Chat Platform), nor a single standing forum venue (Online Forum). The community unit is the spine; everything else — voting, events, media, chat, monetization, federation — is common structure or variant posture.
