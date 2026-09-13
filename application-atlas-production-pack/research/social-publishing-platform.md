# Research Notes — Social Publishing Platform

## Research Goal

Understand, from real products, what a Social Publishing Platform is and how it works: the objects inside it, the publishing loop it supports, the scheduling machinery that organizes it, and its boundaries against the neighboring §06 Types — above all the open joint-review flag left by the social-media-management-platform pass (social-media-management-platform vs social-publishing-platform, "outbound publishing slice vs two-sided presence operation", joint review recommended when this leaf is processed).

## Initial Boundary (pre-research hypothesis)

- Core use: an organization (or a creator acting as one) publishes content to its own social network accounts from one console — compose, adapt per network, schedule, deliver through the networks' official interfaces.
- Hypothesis from the sibling pass: this Type is the outbound publishing center — a product whose defining closure is the post delivered to the network at a planned time, with the inbound response loop absent, thin, or secondary.
- Nearest neighbors: Social Media Management Platform (two-sided operation), Content Planning Platform (shared plan without connected-account delivery), Social Media Analytics Platform (measurement center), Content Marketing Platform (marketing content program), plus the 02.07 web-publishing Types (CMS / Blogging Platform) that share the word "publishing" but not the substrate.
- Unknowns: does a real product population exist whose engagement surface is absent/thin — or does every product in the class converge to SMM (which would make this leaf an alias)? Is scheduling definitional or merely universal? What does "publishing depth" (queues, recycling, automation) look like in the products that center it?

## Research Questions

1. Is the connected social account the anchor, and how does connection work (OAuth, tokens, reconnection, plan metering)?
2. What is the post's lifecycle (draft → scheduled → published / failed), and how is per-network adaptation modeled (global vs per-channel content, per-platform settings)?
3. Is the scheduled future time / calendar / queue the organizing structure? What scheduling machinery exists (time slots, recurring posts, best times, RSS automation)?
4. What engagement (inbound) surface do publish-center products carry — full unified inbox, publish-anchored inbox, or none? Is it definitional or an attached add-on?
5. What team/agency machinery exists (approvals, client containers, permissions), and is it post-centered or presence-centered?
6. What role do analytics, automation (RSS, plugs, webhooks, API), and AI play — core or attached?
7. Removal tests vs Social Media Management Platform and the other neighbors; verdict on the open joint-review flag.

## Representative Products

| Product | Segment / philosophy | Why sampled |
|---|---|---|
| MeetEdgar | SMB/creator, automation-first evergreen publisher (library → categories → queue → schedule) | cleanest automation-center specimen; documents a minimal, publish-anchored inbox |
| Typefully | creator/prosumer, writing-first publisher for text networks | strongest absence-of-engagement specimen ("Boost Engagement" is all outbound automation); team collaboration without presence operation |
| Postiz | open-source / self-host + cloud, calendar-first multi-platform publisher (34 platforms), API/CLI/MCP | most explicit lifecycle + vocabulary documentation; client containers; automation depth; zero documented inbox |
| Later | mainstream SMB/creator scheduler grown toward a suite (visual/Instagram heritage) | the drift specimen: publishing-center product that added a plan-gated Social Inbox; separate influencer-marketing product |
| Planable | agency/team, approval-first publisher | approval machinery as the flagship; engagement/inbox as a recent add-on; straddles the Content Planning seam deliberately |

This sample spans customer tiers (creator, SMB, agency, developer/self-host) and product philosophies (automation-first, writing-first, calendar-first, approval-first, growth-drift). Hootsuite (category incumbent) was already unreachable in the sibling pass and was not retried; dlvr.it (pure RSS-to-social automation) was attempted twice and abandoned (transport errors) — the RSS pole is evidenced through MeetEdgar's RSS import and Postiz's RSS auto-posting instead.

## Sources

Research date: 2026-09-08. All Layer-A evidence from official help centers and product documentation (Tier 1), fetched live.

- MeetEdgar Help Center: https://help.meetedgar.com/ — home; /en/collections/47695-edgar-s-features-and-best-practices (53-article collection inventory); /en/articles/6213008-using-inbox-feature-in-meetedgar; /en/articles/281190-scheduling-with-edgar.
- Typefully Help Center: https://help.typefully.com/ — home (collection inventory); /en/collections/7473562-publish-schedule; /en/collections/7473726-boost-engagement; /en/articles/8728077-what-and-where-can-i-publish-with-typefully.
- Postiz Documentation: https://docs.postiz.com/ — index (llms.txt); /general/concepts.md ("How Postiz works"); /general/composer/scheduling.md.
- Later Help Center: https://help.later.com/hc/en-us — home; /hc/en-us/categories/360002957213-Schedule-Publish; /hc/en-us/categories/360003329913-Analyze-Engage; /hc/en-us/articles/31010972850199-Manage-DMs-Comments-in-Later-with-Social-Inbox.
- Planable Help Center: https://help.planable.io/hc/en-us — home; /hc/en-us/categories/21715206753052-Collaboration-workflow.
- Sibling-pass evidence reused for comparison (Layer A, 2026-09-07): research/social-media-management-platform.md (Buffer/Agorapulse/Sprout/Metricool/Sendible pillar structure and inbox depth).

Source-access limitations: dlvr.it unreachable (2 transport errors, abandoned); Hootsuite not retried (repeated timeouts in sibling pass). Absence claims (e.g., "Typefully documents no inbox") are statements about the vendors' own documentation, not audited feature absence. Planable's inbox category was not fetched at article level. Later's Social Inbox article is dated July 2026 (very recent, replaces an earlier "Conversations" tool) — product drift in progress.

## Product Observations

### MeetEdgar (Layer A unless noted)

- Positioning: automated scheduling. Core structure: **Library** (content storage, bulk edit) → **Categories** (organize content; default categories offered) → **Schedule** (weekly automations = repeating time slots) → **Queue** → **Post History**. (A)
- Time slots: weekly repeating/non-repeating; each slot targets chosen social profiles and pulls from a category or an individual post; "Random time slot" pulls a random post from the library whether or not already published; weekly automation count is plan-limited; suggested time slots offered at setup. (A)
- Queue: skip/shuffle/un-shuffle to reorder; **pause the queue** to stop publishing; "Edgar says my post couldn't be published" troubleshooting; empty-queue fixes. (A)
- Composer: Add New Content; **Variations** (multiple versions of a post); Canva design import; previews; weekly themed / recurring posts; use-once; expiration dates for limited-run content; UTM parameters; Inky AI sidekick. (A)
- Import: RSS feeds, bulk import (CSV, with images), Zapier; bookmarklet + Chrome extension; link shortening with click tracking. (A)
- Connections: connect social accounts (FB, Pinterest, Twitter/X, IG, LinkedIn, GBP, Threads); **refresh & reconnect** article; plan limits on account count ("increasing the limit"); account permissions. (A)
- History/analytics: post history page, weekly performance reports, dashboard. (A)
- **Inbox (1 article, plan-gated to the top plan, FB+IG only)**: "Your Inbox collects all comments and direct messages from posts **that Edgar publishes for you**… Posts published manually or through other tools won't appear in the inbox." Three views (DMs / Unread / Comments); reply inside the app; **no deletion ("must be done directly on Facebook or Instagram")**; no advanced filtering or search; any team member with account access can view and reply. → **publish-anchored engagement**: the inbox exists to handle responses to the tool's own published posts, not to operate the account's whole inbound stream. (A)

### Typefully (Layer A)

- Positioning: writing/scheduling for X, LinkedIn, Threads, Bluesky, Mastodon, Substack Notes; personal profiles and LinkedIn Pages; cross-posting; X posts/threads/**X Articles** (X Articles not cross-postable). (A)
- Help-center weight: **Publish & Schedule (12 articles)** and **Writing & Editing (9)** are the core; Analytics = 1 article; Collaboration = 3; Apps (2); API & Integrations (6). (A)
- Scheduling: Scheduling and Calendar; **Planned Posts**; scheduling timezones; "Why did my post fail?"; "Repurpose Your Published Posts" (rework published content). (A)
- **Boost Engagement collection (6 articles) is entirely outbound automation**: Engagement Tools for X/Twitter, **Auto-DM campaigns**, **Auto-Retweets for X posts**, **Auto-plugs**, Thread Finisher, LinkedIn PDF carousels. **No inbox/inbox-like collection exists in the help center.** (A; absence = statement about the documentation)
- Collaboration and analytics exist but are minimal-footprint; Zapier automation + public API (v1→v2 migration documented). (A)

### Postiz (Layer A)

- Positioning: "Schedule and publish to **34 social platforms** from one calendar… tailor each post per platform, generate content and media with AI, and publish on a calendar you can hand to a client." Cloud + self-hosting poles; Public API, CLI, and MCP "connect an AI agent to it". (A)
- Own vocabulary ("How Postiz works" page): **Organisation** (container for channels/posts/media/team); **Channel** = one connected social account (API name: **integration**; can be **disabled** rather than deleted, keeping history; channel caps per cloud plan); **Customer** = group of channels, normally one client — enables calendar filtering per client and an **invite link so a client connects their own accounts without having an account**; **Post and post group** — "When you schedule one piece of content to five channels, Postiz stores five **posts** that share a **group**"; inside one post, multiple parts (X thread; LinkedIn post + comments); **Global vs per-channel content** (unlocking a channel's tab detaches it; mentions only available on detached channels because "a handle is only meaningful on one platform"); per-platform **Settings** (YouTube title/privacy, Reddit subreddit/flair, Pinterest board — "Some are required and the post will not save without them"); **Tag** (colored label = campaign/client/content type on the calendar); **Set** (saved channel selection + settings); **Signature** (auto-appendable block); **Time slot** (per channel, drives Day-view rows, RSS next-slot, find-slot API — "a scheduling convenience, not a restriction"); **Post state**: Draft / Scheduled / Published / **Error** ("platform rejected it — red ring, reason in a tooltip"); **Preview link** (public page where a client reads the post as it will appear and comments, without an account); **Plug** (automation firing after publish: auto-repost, follow-up comment). (A)
- Scheduling page: three ways to finish a post — **Save as Draft / Add to calendar / Post Now**; browser timezone; **Repeat Post Every** (day→month cycle; "editing a recurring post affects **all future occurrences**"); drafts occupy their calendar slot "so you can see the shape of the week, but the scheduler ignores it"; after scheduling: publishes at its time, calendar switches to published with a link to the live post; if it fails, red ring + error; **"Postiz does not silently retry a rejected post: fix the cause and reschedule."** (A)
- Automation surface: **RSS auto-posting** (feed → scheduled posts, optional AI rewriting), **Plugs**, **Webhooks** ("notify another system when Postiz publishes"), third-party media integrations, AI agent. (A)
- API: posts CRUD with draft/schedule status changes; **"Get Missing Content"** — when a platform did not return a usable post ID the post's `releaseId` is set to `"missing"` and can be re-linked (a documented delivery-confirmation failure state); find-available-slot endpoint; channel connect via OAuth URL; delete channel deletes its scheduled posts. (A)
- Approvals: light — preview link + client comments (client needs no account). (A)
- **No inbox/conversations/community-management section exists anywhere in the documentation index** (the internal "Notifications" API is product notifications, not social interactions). (A; absence = statement about the documentation)

### Later (Layer A)

- Positioning: "Later Social" with **three separate help centers** (Social media managers / Enterprise brands / Creators); a separate **Later Influence** help center for enterprise influencer marketing. (A)
- Category structure: Social Profiles & Connections; Media & Planning; **Schedule & Publish**; **Analyze & Engage** ("Track performance, drive traffic with Linkin.bio, and respond to comments"); Account & Billing; Campaigns. (A)
- Schedule & Publish: per-network sections (YouTube, Instagram, Facebook, TikTok, LinkedIn, Pinterest, Snapchat, Threads); **Troubleshooting Failed Posts**; **Publish Instagram Posts Using Notification Publishing** (manual fallback where API publishing isn't possible); Missed Post Notifications; "Where is the Publish Now button?"; Instagram Auto Publish Post Limit; Best Times to Post (IG/FB/TikTok); Working with Time Zones; calendar features (switch between social profiles). (A)
- Analyze & Engage: Link in Bio (19 articles, affiliate links, UTM), Analytics (22 articles incl. **Meta ad account connection**, social listening "Brand DNA" and benchmarking), and **Conversations → 1 article: "Social Inbox"** — replaces the earlier "Conversations" tool; brings **IG+FB DMs and IG/FB/TikTok comments** into one place; **plan-gated (Growth and Scale; Free/Starter can preview but not reply)**; desktop only; beta; reply to DMs/comments, hide/delete comments; documented limits (7-day DM reply window due to Instagram API, 30-day request-tab activity window, no emoji reactions, no new threads to strangers, read state not synced back to Instagram); **"Can I restrict a member's access to Social Inbox? Not at this time"** (inbox access not separately permissioned — roles exist for publishing: Reviewers, Publish Without Approval). (A)

### Planable (Layer A)

- Positioning: "The command center for modern marketing teams"; use cases: multi-channel content calendar, agency workflow management, centralized campaign management, social media collaboration workflow; industries: agencies, multi-location brands, multi-brand companies. (A)
- Feature pillars: Create / Plan / Collaborate / **Approve** / Schedule / Analyze / Engage. (A)
- Collaboration workflow (the flagship, 4 sections): **Managing users** (permissions, invite, **collaborators with a link**, change owner); **Feedback and reviewing** (comments, **annotations**, **suggestions**, resolve, emoji reactions); **Approval process** (approve a post, approvals and approval workflows, **multi-level approvals**, **automated reminders for approvals**, client approval, **schedule posts automatically on approval**); **Internal–External collaboration** (review links, external collaborators, team vs client/external membership, internal notes). (A)
- Creating & scheduling; Views & organizing posts (views, filters, campaigns); Channels ("Connect social pages and fix connection issues"); Company & workspaces; Mobile App; Analytics. (A)
- **Engagement features** category + **"Social inbox and community management — Reply to comments and manage DMs from Planable"** — a separate, newer category alongside the core workflow categories. (A; article-level depth not fetched)

## Cross-product Comparison

| Structure | MeetEdgar | Typefully | Postiz | Later | Planable | Reading |
|---|---|---|---|---|---|---|
| Connected accounts via network authorization | Refresh/reconnect article, plan-limited account count | Per-network publish support docs (X limits, media formats) | Channel = integration; OAuth connect API; disable vs delete; plan channel caps | Social Profiles & Connections category; refresh profiles | Channels category ("connect social pages and fix connection issues") | **Core (B)** |
| One composed item → per-channel adaptation | Variations; per-network composer behavior | Cross-posting with per-network limitation docs | Global vs per-channel tabs; per-platform settings (required ones block save); parts (thread/first comment) | Per-network sections; caption handling | Per-platform composer + previews | **Core (B)** |
| Managed delivery lifecycle ending in published/failed | "Post couldn't be published"; queue pause; post history | "Why did my post fail?"; Planned Posts | Draft/Scheduled/Published/**Error** states; no silent retry; `releaseId: "missing"` re-linking | Troubleshooting Failed Posts; Missed Post Notifications; notification publishing | Publish after approval; scheduling on approval | **Core (B)**; exact state names vary |
| Scheduled future time as organizing structure | Weekly automation time slots; queue; random slots | Publish & Schedule collection; calendar; planned posts | Calendar as product spine; time slots; repeat cycles; find-slot API | Calendar features; best times; timezone handling | Schedule pillar; calendar views | **Core (B)**; slots/queues = one implementation family |
| Multi-account single console | Multi-account queue/schedule views | Multi-network cross-post | 34 platforms; organisation switcher | Multi-profile calendar | Multi-channel calendar | **Core (B)** as normal form (single-account degenerate cases exist) |
| Team machinery | Any team member shares account access | Collaboration (3 articles) | Team members; client containers + no-account client invite links | Team collaboration & content approvals roles | **Approval-first**: multi-level approvals, external/client collaborators, annotations/suggestions | **Common (B)**; post-centered, not presence-centered; depth varies |
| Approval workflow | Not observed | Not observed (collaboration only) | Light (preview link + client comments) | Content approvals roles | **Flagship** | **Common (B)** — absent/light in individual-form products |
| Content library / recycling / automation depth | Library + categories + random slots + evergreen | Repurpose published posts | Media library; RSS auto-posting; plugs; webhooks; API/CLI/MCP | (media & planning category) | Views/campaigns | **Common, publish-center signature (B)** |
| Inbound engagement surface | **1-article inbox, publish-anchored** (only posts Edgar published), FB+IG, plan-gated, no delete | **None documented**; "Boost Engagement" = outbound automation | **None documented** | **1-article Social Inbox**, plan-gated, beta, desktop-only | Separate "Social inbox and community management" category (recent) | **Optional add-on (B)** — absent, thin, plan-gated, or recent; never the center |
| Analytics module | Weekly reports + dashboard | 1 article | Per-platform/post metrics + API analytics | 22-article analytics + ad accounts + listening drift | Analytics category | **Common module (B)** — never the center |
| Link infrastructure | Link shortening + click tracking + UTM | — | Links & validation; short links | Linkin.bio + UTM + affiliate | — | **Common (B)**; link-in-bio pages optional |
| AI assistance | Inky | (not observed in fetched docs) | AI generation + AI agent + MCP | Caption Writer | (free AI tools on marketing site) | **Common, current-era (B)** |
| Client/agency containers | (plan tiers) | (workspaces implied by collaboration) | **Customer** + no-account client invite links | Enterprise brands center | **Workspaces + client/external membership** | **Common (B)** at the agency pole |

## Abstraction Levels

### L0 — Defining Invariant (minimal)

A Social Publishing Platform is an operator-side console that **publishes content to social networks on the operator's behalf**. Three jointly-held properties; removing any one changes the Type:

1. **Connected accounts of the operator's organization** — the org's own social-network profiles attached through each network's official authorization machinery (OAuth-class connect, network-side role prerequisites, token expiry with documented reconnection/refresh flows, plan-metered account counts). The platform acts through the networks, is partially constrained by them, and documents per-network capability scope. Remove → a content/planning tool with no network reach.
2. **The outbound post as managed unit with a delivery lifecycle** — one composed item addressed to one or more connected accounts, adapted per network (per-channel content variants, per-platform settings, previews), carried through an explicit lifecycle (draft → scheduled → published, with a recorded failure state and error reasons, and no silent failure). Remove → a bare composer or a campaign calendar; there is no publishing operation.
3. **Deferred delivery as the organizing structure** — the calendar/queue of planned posts is the product's spine; the platform delivers at the planned time **without the operator being present at the moment of publication** (fixed date-time, recurring slots, queue automation, or feed-driven auto-posting all satisfy the same structure). Remove → a compose-and-send messenger or native-app posting, not a publishing platform.

Conscious exclusions from L0 (with evidence): the **inbound response loop** is not definitional (Typefully and Postiz document none; MeetEdgar's is publish-anchored; Later's is plan-gated/thin; Planable's is a recent add-on — while every sample documents the delivery lifecycle as the core); **analytics** is not definitional (present everywhere as a module, thin in 3 of 5); **approval workflows** are not definitional (absent in individual-form products); **multi-account operation** is the normal form but not required (single-account publishing tools satisfy the definition).

Historical check (§24-style, reasoned — see Uncertainties): the founding generation of this class (early-2010s multi-account schedulers, and the still-living MeetEdgar, founded on library→category→queue automation) already exhibits all three properties, while its engagement surface is demonstrably a later add-on (MeetEdgar's inbox article is recent and plan-gated; Later's Social Inbox replaced "Conversations" in 2026). RSS-to-social automation (the dlvr.it pole, unreachable this pass) satisfies the same three properties with zero engagement. The definition therefore does not depend on the current suite-shaped market.

### L1 — Common Mature Structure

- Multi-account single console with an organization/team container; client/customer grouping at the agency pole (Postiz "Customer" + no-account client invite links; Planable workspaces with client/external membership).
- Per-network adaptation surfaces: global vs per-channel content detachment, per-platform settings panels (required fields block saving), previews, character/format limits, thread and first-comment handling.
- Publishing calendar (day/week/month/list) with drag-rescheduling and state-colored post cards; per-channel time slots and queues ("next available slot"); recurring/repeat posts; best-time suggestions; timezone handling.
- Failure machinery as first-class: failed-post troubleshooting, error reasons on the card, missed-post notifications, notification-publishing fallbacks where network APIs restrict auto-publish, delivery-confirmation edge cases (Postiz `releaseId: "missing"` re-linking).
- Content library / media library; design-tool imports (Canva-class); bulk/CSV import; bookmarklet/browser extensions.
- Publishing-side automation: RSS auto-posting, evergreen recycling and random slots, post-publish automations (auto-repost, auto-retweet, auto-plug, auto-DM), webhooks, public APIs, Zapier, CLI/MCP.
- Link infrastructure: shortening, click tracking, UTM parameters; link-in-bio pages (optional).
- Approval machinery in team forms: submit for review, comments/annotations/suggestions, multi-level approvals, client/external review links without accounts, schedule-on-approval, approval reminders.
- A thin analytics module (post metrics, weekly reports, exports); AI caption/media generation in current-era products; mobile apps.

### L2 — Variant / Optional Structure

- **Inbound engagement surface** — the pivotal variant: absent (Typefully, Postiz), publish-anchored (MeetEdgar: only interactions on the tool's own published posts), plan-gated and thin (Later Social Inbox: two networks' DMs + comments, beta, desktop-only), or recent add-on (Planable). When this surface becomes a first-class pillar covering the account's whole inbound stream with team operation (assignment, moderation, SLAs), the product has become a Social Media Management Platform.
- Product-philosophy poles: automation-first evergreen (MeetEdgar), writing-first creator (Typefully), calendar-first multi-platform breadth (Postiz: 34 targets incl. blogs, newsletters, communities — channel-specific seams), visual/Instagram-heritage scheduler grown toward a suite (Later), approval-first agency (Planable).
- Network-coverage poles: text-first (X/LinkedIn/Bluesky/Mastodon/Threads) vs visual-first (Instagram/TikTok/Pinterest/Snapchat).
- Deployment: SaaS vs open-source self-hosting (Postiz: own developer apps per network, OIDC, storage, reverse proxies) with API/CLI/MCP automation posture.
- Analytics depth: post metrics (common) vs account growth/competitor benchmarking/listening-flavored features (Later's Brand DNA) — the latter drifts toward the analytics/listening Types.
- Paid amplification (ad-account connection, boosting) — present at one sample's analytics layer, optional.

### L3 — Vendor-specific (research notes only)

- Postiz: "Channel"/"integration" naming duality; "Customer" container; Sets and Signatures; Plugs; releaseId "missing" re-link endpoints; Temporal-based self-host architecture; per-provider self-hosted developer apps; 34-platform breadth including Discord/Slack/Telegram/Skool/Whop/WordPress/Medium/Dev.to/Hashnode/Listmonk targets.
- MeetEdgar: category-driven queue; Random time slots; weekly automation plan limits; "Inky" AI; bookmarklet; the publish-anchored inbox's explicit "posts published manually or through other tools won't appear" rule.
- Typefully: Auto-plugs, Auto-DM campaigns, Auto-Retweets, Thread Finisher; X Articles support; API v1→v2 migration; repurpose-published-posts.
- Later: three help-center split (managers/enterprise-brands/creators); Later Influence as separate product; Linkin.bio affiliate/UTM machinery; Social Inbox plan gates and documented API limits (7-day DM window, 30-day request window); "no member restriction for inbox access".
- Planable: annotations/suggestions review model; schedule-automatically-on-approval; collaborators-with-a-link; internal-vs-external membership.

## Vendor-specific Findings

See L3. Notable single-product facts kept out of the canonical document: MeetEdgar's inbox covers only tool-published posts; Later's inbox cannot be permission-restricted separately from publishing roles; Postiz documents a delivery-confirmation repair flow (`releaseId: "missing"`); Postiz stores N posts per N channels sharing one group (deletion semantics follow); Typefully's engagement features are all outbound automation.

## Rejected Findings

- "A social publishing platform is just an SMM platform minus the inbox" — rejected as a definition: publish-center products add publishing-depth machinery (evergreen libraries, category-driven queues, random slots, RSS auto-posting, post-publish plugs, webhooks) that SMM suites carry only as one pillar; the difference is center of gravity, not subtraction.
- "Absence of an inbox is definitional" — rejected: three of five sampled products ship some inbox; the discriminator is anchoring and depth (publish-anchored / plan-gated / recent), not feature presence.
- "Queue-based scheduling is the definition" — rejected: fixed date-time, calendar, and feed-driven auto-posting satisfy the same structure; Postiz explicitly calls time slots "a scheduling convenience, not a restriction."
- "Multi-network breadth (34 platforms) is a different Type" — rejected: same console structure; blog/newsletter/community targets create channel-specific seams (those targets have their own Types) but the publishing-console structure is unchanged.
- "Approval workflow is definitional" — rejected: absent from the individual-form products (Typefully, MeetEdgar, Postiz-light); common only in team forms.
- "Analytics is definitional" — rejected: thin module in 3 of 5 samples (1-article collections at two products).

## Boundary Findings

**vs Social Media Management Platform (§06 sibling) — the open joint-review flag, DISCHARGED from this side.** Keep both Types. The ratified discriminator is center of gravity, now evidenced from the publish side: (a) in publish-center products the delivery lifecycle (compose → adapt → schedule → deliver → confirmed/failed) is the documented spine — Postiz's vocabulary page and scheduling page are almost entirely about it; Typefully's two largest collections are Publish & Schedule and Writing & Editing; (b) the inbound loop is absent, publish-anchored, plan-gated, or a recent add-on in all five samples (Typefully: none documented, engagement = outbound automation; Postiz: none documented; MeetEdgar: 1-article inbox explicitly limited to posts the tool itself published; Later: 1-article plan-gated beta inbox; Planable: recent separate category) — against SMM samples where the inbox is a first-class pillar (Agorapulse 20-article collection, Sprout engagement category with approval workflows for replies, Buffer selling it as a co-equal pillar); (c) removal tests both directions: remove the inbound loop and presence-operation machinery from an SMM product → what remains is this Type's center; remove the delivery engine and scheduling spine from this Type → an empty shell (SMM's pillar structure does not re-emerge, because the two-sided machinery was never there). Sharpest single datum: MeetEdgar's inbox exists **only** for posts MeetEdgar published — engagement as the shadow of publishing, not the operation of a presence. Market naming corroborates: publish-center products sell themselves as scheduling/publishing (Later "Schedule & Publish", Postiz "schedule and publish… one calendar", Typefully "Publish & Schedule", Planable "Creating & scheduling"), while SMM sells "management". Products drift in the direction Later and Planable show (scheduler adds inbox), which is real but leaves the center of gravity readable from documentation weight.

**vs Content Planning Platform (§06, processed 2026-09-07).** The planning Type's center is the shared plan + coordination lifecycle, with publishing as an attached, channel-dependent capability (native social scheduling in 3 of 4 of its samples; manual-mark for non-social). Here, the connected accounts and the delivery closure ARE the center. Straddle products exist and are acknowledged: Planable self-labels "multi-channel content calendar" (planning language) while shipping connected channels, delivery, and approval — classified here as a publishing-center product with approval-first philosophy because its documentation weight (collaboration/approval workflow + channels + scheduling) centers the post going out, not a shared program layer. The seam is center-of-gravity-based, consistent with the content-planning pass's own ruling.

**vs Content Marketing Platform (§06, processed 2026-09-07).** CMP's defining closure is the content piece carried into its marketing channels from plan to performance, with the piece as unit of record. Here the unit of record is the post addressed to connected accounts, and there is no editorial program layer (campaigns/tags exist as labels, not as a program). A CMP publishing to social through integrations is channel-crossing of its piece; an SPP has no piece-of-record notion beyond the post.

**vs Social Media Analytics Platform (§06, processed) and Social Listening Platform (§06, processed).** Measurement and observation centers vs the delivery/action center. Analytics modules inside publishing products are thin (1–22 articles; never the spine); Later's listening-flavored "Brand DNA"/benchmarking features are the drift edge. Consistent with the analytics pass's own removal tests.

**vs Content Publishing Types (§02.07: CMS, Headless CMS, Blogging Platform).** The word "publishing" collides; the substrate differs. CMS/blogging Types own the presentation of web content; a social publishing platform acts on third-party social networks through their official interfaces and never renders the destination page. (Postiz's 34 targets include WordPress/Medium/Dev.to/Hashnode/Listmonk — when the target is a blog/newsletter the delivery semantics belong to those channels' Types; the console remains an SPP. Recorded as a boundary note, not a Type change.)

**vs Email Marketing Platform (§06).** Owned subscriber list vs network-mediated accounts; different authorization substrate (list import vs OAuth to networks). Postiz's Listmonk target sits on the same seam.

**vs Marketing Campaign Management Platform (§06).** The campaign is not the organizing object here — the account and the post are; campaigns/tags/labels group posts. One sample markets "centralized campaign management" (Planable) — center-of-gravity test applies.

**vs Business / Customer-to-Business Messaging Applications (§01.01).** Where publish-center products ship thin inboxes, the conversation management is an attached shadow of publishing (see MeetEdgar), not a standalone messaging surface with business identity; the seam matches the SMM pass's ruling and is even wider here.

## Uncertainties

1. dlvr.it (pure RSS-to-social automation, likely the purest zero-engagement pole) unreachable after 2 transport errors — the automation pole is evidenced indirectly (MeetEdgar RSS import; Postiz RSS auto-posting + webhooks). No claims are made about dlvr.it itself.
2. Hootsuite — the best-known incumbent — unreachable in both the sibling pass and this one; no market-centering claims are made.
3. "Documents no inbox" claims (Typefully, Postiz) are statements about the vendors' own documentation, not audited feature absence; kept qualified in the final document.
4. Planable's "Social inbox and community management" category was observed at title level only; its depth is unknown. Its classification as publish-center rests on documentation weight overall, which is a judgment call recorded here.
5. The historical check is reasoned from the structure of the evidence (MeetEdgar's still-current automation-first form; Later's 2026 inbox replacement showing the engagement surface is the newer layer) rather than from primary sources of defunct early products; no claims about specific early products appear in the final document.
6. Later's Social Inbox article (July 2026) is very recent; plan gates and limits will move. Exact limits (7-day/30-day windows) are recorded here only, not in the final document.

## Final Synthesis

The Social Publishing Platform is the outbound half of social-presence software elevated to a Type of its own: a console that attaches the operator's own social accounts through the networks' official authorization machinery, composes one post and adapts it per network, organizes planned delivery on a calendar/queue/time-slot spine, and delivers each post through the network's interface at the planned time without the operator present — recording a published/failed outcome for every delivery. Its signature depth is publishing machinery (evergreen libraries, category-driven queues, recurring slots, RSS auto-posting, post-publish automations, link tracking, APIs); its team machinery (approvals, client containers) centers the post going out; its engagement surface, where it exists at all, is thin, plan-gated, and publish-anchored — the shadow of publishing rather than the operation of a presence. The joint review with the Social Media Management Platform is resolved: keep both Types, discriminated by center of gravity (delivery closure vs two-sided presence operation), with removal tests recorded in both passes and the drift direction (scheduler grows an inbox → SMM) documented from both sides.
