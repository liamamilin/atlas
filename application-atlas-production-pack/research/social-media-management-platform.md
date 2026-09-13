# Research Notes — Social Media Management Platform

## Research Goal

Understand, from real products, what a Social Media Management (SMM) Platform is and how it works: the objects inside it, the operating loop it supports, the roles and rules that shape it, and its boundaries against the neighboring marketing/social Types in the directory (§06 siblings: Social Publishing Platform, Social Media Analytics Platform, Social Listening Platform; plus Marketing Campaign Management, Influencer Marketing, Business Messaging).

## Initial Boundary (pre-research hypothesis)

- Core use: an organization (brand, agency serving brands) operates its own social network accounts from one place — connect accounts, compose/schedule/publish posts, respond to audience interactions, measure results.
- Users: social media managers, marketing teams, agencies.
- Nearest neighbors: Social Publishing Platform (outbound-only slice?), Social Media Analytics Platform (measurement center), Social Listening Platform (public-conversation observation center), Marketing Campaign Management (cross-channel orchestration), Influencer Marketing (third-party creators).
- Unknowns: whether engagement (inbound) is definitional or merely common; whether analytics is definitional; the post's lifecycle; how deeply network-API constraints shape the Type.

## Research Questions

1. Is the connected social account the structural anchor? How do connections work (authorization, tokens, expiry)?
2. What is the post's lifecycle (draft → approval → scheduled → published/failed)?
3. How does per-network adaptation work (one post → many network variants)?
4. What is the engagement model (unified inbox, assignment, moderation, reply constraints)?
5. What team/agency structures exist (users, roles, approval workflows, client/brand separation)?
6. What role do analytics/reporting, listening, advocacy, ads play — core or bundled module?
7. Removal tests vs sibling Types.

## Representative Products

| Product | Segment / philosophy | Why sampled |
|---|---|---|
| Buffer | SMB / simplicity-first, publish+analyze+engage triad | cleanest statement of the three-pillar structure; strong per-channel capability matrix |
| Agorapulse | agency/mid-market, inbox-first philosophy | deepest engagement/inbox documentation; per-network composer panels |
| Sprout Social | mid-market/enterprise, suite pole | approval workflows, Cases/Reviews customer-care drift, premium modules |
| Metricool | SMB/creator+agency, straddles analytics | account structure (User/Brand/Profile), inbox API-constraint documentation, white label |
| Sendible | agency-focused, mid tier | Publish/Activity/Collaborate/Reports pillar framing, white-label |

Hootsuite (category incumbent) was selected but its help center and site timed out repeatedly from the research environment; abandoned per network-restriction rules and replaced by Sendible. No Hootsuite-specific claims appear anywhere below.

## Sources

Research date: 2026-09-07. All Layer-A evidence from official help centers (Tier 1), fetched live.

- Buffer Help Center: https://support.buffer.com/ — home; /articles/connecting-your-channels-to-buffer-HvWLgAJvL9; /articles/getting-started-with-buffers-publishing-features-adhqleECyT; /articles/getting-started-with-buffers-community-feature-vBndIuv1x0; home-page category and article-slug inventory (Channel Management 26, Scheduling Posts 24, Creating Posts 12, Team Collaboration 11, Engaging with Comments 4, Analyzing Your Data 5, Mobile App 28, Integrations 10).
- Agorapulse Help Centre: https://support.agorapulse.com/ — home; /en/collections/7505345-publishing; /en/collections/7426820-inbox; /en/articles/8769280-how-to-create-and-schedule-a-post-in-agorapulse.
- Sprout Social Help Center: https://support.sproutsocial.com/hc/en-us — home; /hc/en-us/categories/115001115146-Engagement; /hc/en-us/categories/115001115166-Publishing; /hc/en-us/articles/205974715-Message-Approval-Workflows.
- Metricool Help Center: https://help.metricool.com/en/ — home; /account-structure-user-brand-and-social-profiles-xun54; /inbox-manager-how-to-manage-messages-and-comments-from-metricool-s9zze.
- Sendible Support: https://support.sendible.com/hc/en-us — home (category inventory only).
- (Unreachable) Hootsuite: https://help.hootsuite.com/, https://www.hootsuite.com/ — repeated timeouts; no evidence drawn.

Source-access limitation: all five sampled help centers were reachable, but article-level depth varies by product (Sendible observed at category/feature level only; Agorapulse/Buffer/Sprout/Metricool at article level). Hootsuite evidence entirely absent → market-share weighting is not asserted anywhere; claims rest on the five reachable samples. Operational specifics observed in only one product are marked product-specific.

## Product Observations

### Buffer (Layer A unless noted)

- Own tripartite framing: "Once a channel is connected, you can **publish** posts, **analyze** results, and **engage** with comments." (A)
- **Channel** is the core connected object; per-network capability matrix in the connection guide: each channel supports Publishing / Analytics / Engagement differently (e.g., Facebook Pages ✓✓✓; Pinterest/TikTok/GBP/YouTube Shorts publishing-only; LinkedIn profiles publishing+engagement, no analytics; Instagram personal accounts notification-publishing only). (A)
- Connection = OAuth: log into the social account in a tab, authorize in the network's own dialog; the network issues Buffer an **access token**; "Buffer uses that token to post on your behalf, so you don't have to stay logged in." (A)
- Connection prerequisites are network-side roles: Facebook Page Full control, LinkedIn Page Super Admin, YouTube channel Owner. (A)
- Tokens expire; product documents periodic reconnection ("Refreshing a channel in Buffer"); "Unavailable"/locked channel states when a channel is connected to another Buffer organization. (A)
- Organization/team: channels under "Manage Channels" may be invisible in Publishing per user permission; org owner updates access. (A)
- Composer flow: + New → select channels → text + media → **"Customize for each network"** → schedule options: **Next Available** (next queue slot), **Prioritize** (top of queue), **Set Date and Time**, **Now** → Schedule Post. (A)
- Per-channel settings: timezone, **Posting Times** (the per-channel queue schedule that the queue fills). (A)
- Channel groups, tags, saved replies configured at account level. (A)
- Engagement = **Community** tab: choose channel → open a post with unanswered comments → reply inline or use a suggested reply → send; mobile equivalent. (A)
- **Notification publishing** fallback where API publishing is not possible (Facebook groups, Instagram personal accounts): the tool sends a reminder; the user publishes natively. (A)
- Free plan meters channels (channel as billable unit; lifetime per-network connection caps on free). (A)
- Category inventory adds: Ideas (idea capture), Start Page (link-in-bio), API, integrations (Dropbox/Google Drive/OneDrive/OneDrive-class media sources). (A)

### Agorapulse (Layer A)

- Help-center pillar order and depth: Publishing (44 articles) and Inbox (20) are the two largest core collections; Analytics (25), Advanced Listening (6), Advocacy (5), AI & Automations (5), Archie (AI writing, beta) around them. (A)
- Composer: select one/multiple profiles → text with live per-network character limits → media (computer / Agorapulse Library / Google Drive / Canva) → optional draft toggle → per-network **Social Network Options panels**: Facebook (post type incl. Story, album, boost, first comment, audience targeting), Instagram (Post/Reel/Story, **publish via mobile notification**, link-in-bio, first comment, tag users, collaborators, product tagging), LinkedIn (poll, targeting), X (thread), TikTok (privacy, duets/stitches, mobile-notification publishing), YouTube (title/description/privacy/category/playlist/tags/license/embed/notify/made-for-kids), Google Business (post type CTA buttons), Bluesky (no options). (A)
- Social Media Preview panel; **per-profile customization** with "Customized" label — customized profiles detach from the central panel. (A)
- Scheduling: date/time per profile; multiple dates for recurring publication (explicitly blocked for X by Twitter ToS); **recommended publishing times** computed from the account's engagement data (plan-gated). (A)
- Submit points: **Publish Now / Schedule / Save draft / Send for approval** (single approver or "Everyone must approve") / send to Advocacy tool. (A)
- Publishing Calendar: scheduled/published/failed posts; delete published post; CSV export of posts. (A)
- Queues: dedicated queue objects with **timeslots**; add/manage content in a publishing queue. (A)
- Draft management; **bulk import via CSV**; asset library with public URLs; publishing labels; hashtag groups; link shortening/tracking; alt text; subtitles. (A)
- Approval: send for approval → approver reviews → approval workflows managed (multi-user). (A)
- Inbox: unified conversations across networks; **reply, assign to teammates, review (QA), labels, saved replies, sentiment marking, delete/hide items, search/filter/sort, bulk actions, export, filter presets, custom inboxes**; ad-comment sync from connected ad accounts; **automated moderation** rules; documented common reply errors. (A)
- "Advanced Listening" = keyword/brand tracking collection (small, clearly secondary). (A)

### Sprout Social (Layer A)

- Nav pillars: Publishing / Analytics & Reporting / Engagement / AI and Automation / Social Listening / Customer Care / Tagging / Integrations; separate products: Employee Advocacy, Influencer Marketing, NewsWhip (media intelligence). (A)
- Engagement category description: "Manage your **social inbox, cases, reviews and community efforts** with centralized workspaces and automated workflows." Sections: Social Inbox Management (Smart Inbox, sentiment rules, Instagram liking) + Community Management (People View, Contact Profile Views, influencer indicators, custom contact lists). (A)
- Publishing category: compose (custom variables), **Sprout Queue**, avoid post failures, per-network guides; **Message Approval Workflows**; bulk scheduling; Reddit support; Send to Advocacy. (A)
- Approval workflow mechanics (article-level): named multi-step workflows, step = named approvers with **Any/All** sign-off; permissions ladder per profile (Read Only → Can Reply → Needs Approval → Publish/Full Publishing) + **Approve Others** toggle; external approvers (people **without a Sprout account**, agency-to-client sign-off, up to 3 on Advanced — product-specific limit, research notes only); submit from Compose → **Needs Approval** tab → approve/reject/edit with **Approval Activity** (change log + internal comments + step position); rejected → **Rejected** section, editable + resubmittable; expired approval → not published, author notified, stays in Needs Approval; reply approvals for the Smart Inbox as a parallel flow; mobile approvals. (A)
- Post states observed: draft / queued / scheduled / Needs Approval / Rejected / **Failed Posts** (retryable after reconnecting a profile). (A)
- Profile/connection configuration in "Users & Social Profiles" and Onboarding categories: invite users, manage permissions, connect social profiles; SSO section. (A)
- Customer Care category: Cases (+AI, collaboration, reporting), Bots, Reviews — a deeper service desk layer on the same connected-account substrate. (A)
- Per-network sections each split Getting started / Posting / Interacting / Analyzing — the same per-network capability grammar as Buffer's matrix. (A)

### Metricool (Layer A)

- Account structure: **User → Brand → Social profile**. "With each Metricool brand, you can manage a complete brand or client with all its social networks associated… Within each brand you can connect one social profile of each platform." Agencies manage clients' brands. (A)
- Sections: Connecting your social networks (by-network connection guides + troubleshooting); Planning (create & schedule, optimize scheduling, publishing by social network, **collaboration & approval**, content creation tools, guidelines & limits); Analytics (metrics by social network, competitor analysis); Reporting (reports, campaign dashboards, Looker Studio); **Inbox**; Ads (create Meta/Google campaigns, boost posts); SmartLinks (link-in-bio); Mobile app; **White Label** (agencies + integrators); API/MCP. (A)
- Inbox constraints (richest API-boundary documentation of the sample): Inbox is **read-and-reply**; **no delete/hide from the tool** — must be done on the network; per-network reply eligibility matrix (FB comments+DMs; IG comments+DMs; TikTok comments business-only; X DMs; LinkedIn comments/mentions only, no DMs; GBP reviews; YouTube comments); **network-imposed reply windows** (Meta: comments ~24h, DMs ~7d after sending — exact windows product-documented, see Precision note); read/unread state not shared with the networks; Inbox does not store history — reloads from the network; per-brand only (no cross-brand unified view); **no conversation assignment** in this product; **no auto-replies** — saved replies only; notes on conversations; filters by network/type/search; inbox permission levels (full / view-only / none, custom roles). (A)
- Publishing: per-network publishing requirements; troubleshooting sections for scheduling/publishing errors. (A)

### Sendible (Layer A, category level)

- Pillars: **Publish** ("Plan and schedule content for your social profiles all from one place"), **Activity** ("Follow your feeds and engage with your audience"), **Collaborate** ("Work with tasks and approvals from team members and clients"), **Reports** ("Measure and gain insight from your social data"); Settings / Account / Troubleshooting / **White-label accounts**. (A)
- Audience tiers: Solopreneurs / Small teams / Agencies and large teams. (A)
- Feature names: Smart Posts (compose with per-profile customization of message and images), priority inbox, optimal time scheduling, link previews, compose-box image editing. (A)

## Cross-product Comparison

| Structure | Buffer | Agorapulse | Sprout | Metricool | Sendible | Reading |
|---|---|---|---|---|---|---|
| Connected-account anchor | Channel + OAuth token, per-network capability matrix | Social profile, per-network option panels | Social profile, per-network guide sections | Social profile under Brand, per-network connection guides | Social profile, per-network troubleshooting | **Core (B)** |
| Compose → multi-network post, per-network adaptation | "Customize for each network" | Per-profile customization + options panels | Compose + custom variables, per-network posting guides | Planning composer + publishing by network | Smart Posts per-profile customization | **Core (B)** |
| Scheduled future time as first-class | Queue slots (Next Available/Prioritize/Set Date) | Date/time per profile, multiple dates, recommended times | Sprout Queue + scheduled, calendar | Planning + optimize scheduling | Optimal time | **Core (B)**; queue-with-slots is one implementation family |
| Post lifecycle w/ failure states | scheduled/published + notification fallback | scheduled/published/**failed**; delete published | draft/queued/scheduled/Needs Approval/Rejected/**Failed** | scheduling/publishing troubleshooting | troubleshooting category | **Core (B)**; exact state sets vary |
| Approval workflow | Team Collaboration category (docs not fetched at article level) | send for approval, multi-user, Everyone-must-approve | full multi-step workflows, external approvers, activity log | collaboration & approval section | Collaborate: tasks + approvals | **Common (B)** — agency-grade depth varies |
| Unified inbound inbox + reply | Community tab (comments, suggested replies) | Inbox: assign/review/labels/sentiment/moderation/bulk | Smart Inbox + reply approvals + Cases/Reviews | Inbox: read/reply only, no delete, no assignment | Activity + priority inbox | **Core (B)**; moderation/assignment depth is variant |
| Org container & client separation | Organization + users + permissions | Organization, teams | Users & Social Profiles, groups | **Brand** (client container) | White-label, client dashboards | **Core (B)**; container noun varies (org/brand/group) |
| Analytics/reporting module | Analyze feature (5-article category) | Analytics collection (25 articles) | Analytics & Reporting + Premium Analytics | Analytics + Reporting + Looker Studio | Reports pillar | **Common module (B)** — bundled in every sample, never the center |
| Listening (public conversation) | — | Advanced Listening (6 articles) | Social Listening category | Hashtag Tracker | — | **Optional (B)** — absent in 2 of 5 |
| Advocacy | — | Advocacy module | Employee Advocacy (separate product) + Send to Advocacy | — | — | **Optional/vendor-skewed** |
| Ads (boost / campaign mgmt) | — (boost not observed in fetched docs) | Facebook boost (custom plans) | Facebook Ad Accounts & promotions | Full Ads section (Meta + Google) | — | **Optional** |
| Link-in-bio page | Start Page | PulseLink | SproutLink | SmartLinks | — | **Optional (B)** — 4 of 5, independently recognizable feature |
| White label | — | — | — | White Label (agencies/integrators) | White-label accounts | **Optional (B)** — agency pole |
| Notification/manual publish fallback | Notification publishing (FB groups, IG personal) | Publish via mobile notification (IG/TikTok) | Mobile Publisher (Stories) | (not observed) | — | **Common (B)** — exists where network APIs restrict |
| AI assistance | (not observed in fetched docs) | Archie beta, AI writing assistant | AI & Automation category | Ask-AI in help center only | — | **Common, current-era (B)** — not definitional |

## Abstraction Levels

### L0 — Defining Invariant (minimal)

An SMM Platform is an operator-side console that runs an organization's **own** social presence on social networks it does not own. Removing anything below changes the Type:

1. **Connected accounts of the organization** — the org's social-network profiles attached to the platform through the network's own authorization machinery (tokens, network-side role requirements, expiry/reconnection). The platform acts on the networks on the org's behalf; it never replaces them and is always partially constrained by them. Remove → a content/campaign tool that cannot touch social at all.
2. **The multi-network post as managed unit** — an outbound content item composed inside the platform, addressed to selected connected accounts, adapted per network, and carried through a managed lifecycle ending in publication (with a failure state). Remove → a bare inbox or a measurement tool; the outbound publication engine is the anchor the market names first (Publish/Planning/Publishing pillar in every sample).
3. **The inbound response loop on those same accounts** — audience interactions (comments, mentions, messages, reviews) on the connected accounts arrive in a unified console and are answered from it. Remove → the Social Publishing Platform slice (outbound-only schedulers are a recognized market form); "management" without response stops being management.
4. **One-place multi-account operation** — calendar/queue/inbox consolidate all connected accounts so the whole presence is worked from a single console with shared team machinery (users/permissions/client separation). Remove → per-network native operation plus disconnected point tools.

Historical check (reasoned, not directly evidenced this pass — see Uncertainties): the founding generation of the category (late-2000s multi-account Twitter-era platforms) already exhibits connected accounts + scheduled multi-account posting + replying from one dashboard via then-open network APIs; the phrasing above (response loop rather than "unified inbox"; managed lifecycle rather than "approval workflow") is deliberately level-consistent with that generation. Precise ancestors were not researched from primary sources in this pass, so this check is recorded as an inference, and the final document avoids claiming anything about specific early products.

### L1 — Common Mature Structure

- Publishing calendar over all connected accounts (scheduled/published/failed visible, editable, exportable).
- Post lifecycle states (draft → optional approval → scheduled/queued → published / failed / rejected); queue-and-slots scheduling with per-account posting times; recommended/optimal times from engagement data.
- Approval workflows (multi-step, multi-approver, external/client approvers, approval activity trails) and per-account user permission ladders.
- Composer with per-network option panels, character limits, post-type variants (post/reel/story/poll/thread), previews, media from libraries and design tools (Canva-class), asset library, hashtag groups, link shortening/tracking, first-comment, alt text.
- Unified inbox across networks with reply, saved replies, assignment/review, labels, sentiment, search/filter, bulk actions, moderation (delete/hide — depth varies), automated moderation rules.
- Team/organization machinery: users, roles, per-account permissions, client/brand containers, audit/activity trails.
- Analytics & reporting module over the connected accounts (per-network metrics, reports/exports, sometimes competitor benchmarking).
- Bulk CSV post import; mobile apps for publishing + inbox; notification/manual-publish fallbacks where APIs restrict.

### L2 — Variant / Optional

- Social listening module (brand/keyword tracking) — present in 3 of 5 samples, sizes vary from hashtag tracker to full listening.
- Employee advocacy module.
- Paid amplification: post boosting, ad-account connection, ad campaign creation/management.
- Customer-care deepening: cases/tickets, bots, review management (drift toward Contact Center / Customer Service Types).
- Influencer marketing (sold as separate adjacent product by one sample).
- Link-in-bio pages; idea capture; UGC tools.
- White-label packaging (agency pole).
- AI assistance (writing, moderation, spam detection) — current-era common, not definitional.

### L3 — Vendor-specific (research notes only)

- Sprout: Cases + Bots + Reviews + Salesforce Service Cloud; NewsWhip; Premium Analytics; External Approvers (3 on Advanced); 90-day auto-reject of stale approvals; "Viral Post"; Approve Others toggle naming.
- Agorapulse: Archie (beta AI), custom inboxes, ad-comment sync, Advocacy module, "Everyone must approve" mode, X single-date ToS note.
- Buffer: Start Page, Ideas, lifetime free-plan channel caps, "Community" naming for engagement, notification-publishing scope.
- Metricool: Brand container noun, one-profile-per-platform-per-brand rule, Looker Studio connector, SmartLinks, MCP server, no-assignment/no-auto-reply inbox posture.
- Sendible: Smart Posts, priority inbox, white-label dashboards, UK support-hours framing.

## Vendor-specific Findings

See L3. Notable: only Metricool documents that its inbox cannot delete/hide or assign — so "moderation depth" and "assignment" are **variant**, not core. Only Sprout documents external approvers and a stale-approval auto-reject window — approval mechanics vary strongly by product. Only Buffer documents a lifetime per-network connection cap — plan metering is variant.

## Rejected Findings

- "An SMM platform is defined by its analytics" — rejected: analytics is bundled in every sample but is never the center; the measurement-center Type is separately recognized (sibling leaf).
- "An SMM platform includes social listening" — rejected: absent or minimal in 2 of 5 samples; observational stance is the listening Type's center.
- "Queue-based scheduling is the definition of scheduling" — rejected: fixed date/time and calendar scheduling satisfy the same structure; queues are one implementation family (Buffer, Sprout).
- "Deleting/hiding comments from the tool is definitional" — rejected: one sampled product explicitly cannot; the boundary is network-API-bound.
- "SMM = Hootsuite-like enterprise suite" — rejected: sampled SMB/simple products realize the same core with fewer modules; also no Hootsuite evidence was obtained.

## Boundary Findings

**vs Social Publishing Platform (§06 sibling, unprocessed).** Sharpest seam. Removal tests: remove the inbound response loop and the team-operation machinery → an outbound scheduling/publishing platform (the sibling's center); restrict the sibling to outbound only → it lacks the management loop. Working rule recorded for the sibling's pass: publishing-center vs presence-operating center. Keep both. (Directionally supported by all five samples: each sells the inbound loop as a first-class pillar — Community/Inbox/Engagement/Activity.)

**vs Social Media Analytics Platform (§06, processed 2026-09-07).** **Discharges that pass's joint-review flag from this side.** Center-of-gravity discriminator holds: measurement (metric time series over connected accounts feeding marketing decisions) vs operation (publishing + engagement actions changing the state of the accounts). Every sampled SMM product bundles an analytics/reporting module → module straddling is packaging, not Type merger; symmetrically, the analytics pass showed analytics products connecting the same accounts. Removal tests both directions: remove publishing+engagement action loops → analytics platform; remove measurement depth beyond basic post/account metrics → SMM platform. Keep both. The "audience history begins when tracking begins" rule recorded by the analytics pass applies to the bundled analytics modules here as well (shared substrate property, not a discriminator).

**vs Social Listening Platform (§06, processed 2026-09-07).** **Discharges that pass's flag from this side.** Observational center (standing queries over public conversation) vs operational center (acting on own connected accounts). Listening modules inside SMM products (Agorapulse Advanced Listening, Sprout Listening, Metricool Hashtag Tracker) are packaging; the SMM core runs fine without them (absent in 2 of 5 samples). Removal tests recorded both directions. Keep both.

**vs Customer-to-Business / Business Messaging Applications (§01.01).** Those Types center the conversation itself as the messaging surface with business-identity participants; in SMM the conversation is one management surface attached to social accounts, mediated by network APIs, alongside publishing. An SMM inbox is conversation *management over network accounts*, not a standalone messaging application.

**vs Customer Service Platform / Contact Center (§07).** Sprout's Cases/Bots/Reviews show the drift boundary: when the case becomes the managed unit with SLA/service machinery, the product is drifting toward customer-service Types; the social substrate remains the differentiator.

**vs Marketing Campaign Management Platform (§06).** Campaign orchestration across many channel types vs social-presence operations; campaign/campaign-dashboard features appear in SMM (Metricool campaign dashboards, labeling) but the campaign is not the organizing object — the account and the post are.

**vs Influencer Marketing Platform (§06).** Third-party creator partnerships vs own accounts; Sprout sells Influencer Marketing as a separate product with its own help center — a market-confirmed boundary.

**vs Content Planning Platform (§06, processed 2026-09-07).** The planning-platform pass documented that its Type's publishing is channel-dependent and often manual-marked; in SMM, publishing through connected accounts IS the defining closure. A content calendar alone (no connected accounts, no inbound loop) is not an SMM platform.

## Uncertainties

1. Hootsuite — the category's best-known incumbent — could not be reached (repeated timeouts). No claim in this research depends on it, but market-centering statements are avoided and the sample is five reachable products.
2. The historical check (founding-generation fit of L0) is reasoned from the structure of the evidence, not from primary sources of early products; the final document deliberately avoids naming or describing early products.
3. Sendible was observed at category/feature-name level only; its article-level mechanics (approval states, inbox states) were not fetched. Nothing single-source depends on it.
4. Exact network-imposed windows (e.g., Meta reply windows) are product-documented by one sample and treated as an example of a structural rule, not as universal constants.
5. Engagement depth on smaller networks (TikTok/YouTube comment management) is documented unevenly across samples; per-network capability scope varies over time and was not exhaustively tabulated.

## Final Synthesis

The Social Media Management Platform is the organization-side operating console for its own social presence. Its defining structure is four-fold and jointly held: connected org accounts (network-authorized, role-gated, token-mediated, partially constrained by the networks), the multi-network post carried through a managed lifecycle to publication (with failure states and per-network adaptation), the inbound response loop answered from the same console, and single-console multi-account operation with team machinery. Everything else the market associates with the category — analytics, listening, advocacy, ads, link-in-bio, AI, white label — is bundled module or variant, not definition. The network-API constraint is a structural fact of the whole Type: what the platform can do per network, per interaction, is bounded by what each network's official interface permits, which is why per-network capability matrices, connection-role requirements, token refresh, notification-publishing fallbacks, and reply-window rules recur across all products.
