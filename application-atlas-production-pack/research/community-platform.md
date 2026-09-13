# Research Notes — Community Platform

## Research Goal

Understand the Application Type "Community Platform" (DIRECTORY §01.06 Community & Discussion) from real products: what the software's world consists of, who operates it and who participates in it, how work flows, which states and rules matter, and where its boundaries lie against the sibling leaves (Online Forum, Q&A Community, Discussion Board, Interest Community Platform, Private Community Platform) and against adjacent Types (Community Chat Platform, Social Network, Member/Alumni/AMS systems, Paid Community Platform, Research Panel Platform).

## Initial Boundary

Working hypothesis before research:

1. "Community platform" is a recognized software market category (G2: online community management software), not just a generic umbrella: software an **organization** licenses to build and operate **its own** branded community for a bounded member population.
2. The operator (organization) and the members (end users) are two structurally different roles — this two-sided structure is the candidate defining fact.
3. Nearest confusions: Online Forum (venue of boards), Community Chat Platform (live rooms under a container), Social Network (general-purpose network), Member Community Platform / Alumni Management / AMS (segment systems of record), Paid Community Platform (creator monetization pole), Research Panel Platform (operator-structured research participation).

## Research Questions

1. What is the top-level unit of the software — the community? Who creates it and who joins it?
2. What surfaces exist inside the container (discussions, groups, events, content, directory, messaging)?
3. How do members join, onboard, participate, get recognized, and leave?
4. What does the operator's side look like (setup, member management, moderation, analytics, automation, branding)?
5. How is engagement measured and tied to organizational goals?
6. Which capabilities are definitional vs common vs variant vs vendor-specific?
7. Where are the boundaries: vs forum (venue), vs chat (live rooms), vs social network (public graph), vs segment systems (alumni/association), vs paid communities (monetization), vs insight communities (research participation)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| Hivebrite | all-in-one organization-operated community engagement platform (Build→Launch→Engage→Grow→Optimize lifecycle framing); associations / nonprofits / higher-ed alumni / business | organizations (2,000+ claimed) |
| Higher Logic (Thrive Community + Vanilla) | engagement suite; Thrive = association member communities, Vanilla = B2B/B2C customer communities; "community-first, only community software" | associations + enterprises |
| Circle | modern all-in-one SaaS for creators and brands: community + events + courses + payments + email + branded app under one brand | creators / brands / SMB |
| Discourse | open-source discussion-first community platform; self-host or managed hosting; "community and forum software" | tech companies, open source, startups→enterprise |

## Sources

Research date: 2026-09-07.

Fetched successfully:

- Hivebrite — official homepage (hivebrite.com → hivebrite.io), full page incl. Build/Launch/Engage/Grow/Optimize, pillars, features, industries, comparisons, security badges. (Tier 2)
- Higher Logic Vanilla — official platform page (higherlogic.com/vanilla/): features, FAQ. (Tier 2)
- Higher Logic Thrive Community — official support KB "Getting Started with Higher Logic Thrive Community" (support.higherlogic.com). (Tier 1)
- Circle — official homepage (circle.so). (Tier 2)
- Discourse — official homepage, /features, /about (discourse.org). (Tier 2, operationally detailed)

Unreachable / limitations:

- Circle help center: help.circle.co and docs.circle.co — transport errors ×2 each path; abandoned per network rule. Circle evidence is product-page level only; no operational detail asserted for Circle beyond its own page claims.
- Hivebrite /product-overview/ path — 403 (WordPress WAF); homepage served fully. Hivebrite help center not attempted this pass; the alumni-management pass (2026-09-06) already recorded Hivebrite help-center timeouts.
- meta.discourse.org article URL (what-is-discourse/52665) — 404 (stale link); discourse.org/about used instead.

Consequence: no precise numeric limits, plan gating details, or default configuration values are asserted anywhere; product-specific details stay in these notes.

## Product A — Hivebrite

### Key observations (evidence layer A unless noted)

- Self-labels: "Community Engagement Platform", "The community platform built for impact", G2 badge "Best Community Platform". Sells to organizations: Associations, Non-profit, Higher Ed (alumni), Business. Claims 2,000+ organizations.
- The homepage frames the operator's work as a five-stage lifecycle — this is the vendor's own model of the Type:
  - **Build**: branding and theming; no-code page builder; custom user profiles and fields; roles and permissions.
  - **Launch**: signup, SSO and activation; email invitations; payment and memberships; branded mobile app; map directory.
  - **Engage**: forums; events; messaging; content and people recommendations; AI global search.
  - **Grow**: groups and sub-communities; email campaigns and automated digests; multi-channel announcements (push, email, in-app); mentoring and peer-to-peer programs; API and integrations.
  - **Optimize**: analytics & dashboards; engagement scoring / ladder; multi-channel re-engagement (push, WhatsApp, email); automations & AI workflows; moderation.
- Footer "Pillars": Brand / Organize / Engage / Empower / Monetize — monetization is a first-class pillar for this vendor.
- Highlighted features: Groups ("unite members around shared topics and interests"), Member Directory ("puts it on the map. Literally" — map-based directory), Mentoring, AI Matching (continuous 1:1 matching for video conversations), Journeys, white-label mobile app ("Your members stay connected under your brand, not ours").
- The vendor itself polices the Type's seams in its resource library: "Community platform vs chat tools (like Slack & Discord)"; "Five Signs Your Community is Ready to Graduate from a Social Media Group to a Private Community Platform"; "Veterans deserve better than Facebook groups"; "How to choose the right type of online community for your organization".
- Comparisons footer names the category peers: vs Higher Logic, vs Mighty Networks, vs Circle, vs Bettermode.
- Security/compliance surface: ISO 27001, GDPR, CCPA, PCI DSS badges; customer success and professional services offered as part of the product ("community building is too important to go it alone").

## Product B — Higher Logic (Thrive Community + Vanilla)

### Key observations

Tier 1 (support KB, Getting Started with Higher Logic Thrive Community):

- "Higher Logic Thrive Community gives your organization or business the tools that you need to create **private, secure communities** that drive communication, collaboration, and engagement among your members and customers."
- Setup structure confirms the operated-container model: **Site design & settings** (Site Management: navigation & content, password policy, Terms & Conditions, site setup, analytics, advertisements; Community Management: email templates, community discussions and libraries, community types, admin tasks) → **Users** (Member Management: admin levels, moderation, security groups, managing users) → **Modules** (Blogs, Discussions, Ideation — "keep your members engaged with one another"; Mentoring / Mentor Match; Volunteering / Volunteer Manager) → **Events** (Event Manager: event types, payment providers, presenters, registrants).

Tier 2 (Vanilla platform page):

- Self-labels: "customer community software" for B2B/B2C; "We are community-first, meaning we only provide community software—it is not an add-on to another solution."
- Feature blocks: Self-Service and Collaborative Support (federated search across external platforms; Q&A and discussions; networking and virtual events); Content, Design, and Moderation Tools (drag-and-drop layout editor, widget library, accessibility); User Engagement (gamification: badges, points, leaderboards; polling; product feedback process); Automation and AI (automation rules triggered by user behavior/post activity/time; AI-powered insights: sentiment, community health; MCP integration to ChatGPT/Claude/Cursor); Community Analytics (pre-built reports, custom reports, data downloads); Admin and Security (admin dashboard, profiles with role-based permissions, ranked statuses, privacy settings, AI Bot Shield).
- Integrations: direct connectors plus Zapier/Salesforce.
- FAQ polices the seam vs generic group surfaces: "Many online communities start as Slack channels or LinkedIn groups for customers. However, to give your community a home and allow it to grow, we recommend investing in a customer community platform."
- Solutions nav shows the goal taxonomy of customer communities: Customer Success, Customer Support (case deflection), Marketing (advocacy), Product (feedback); and for associations: Member Engagement / Acquisition / Retention.

## Product C — Circle

### Key observations (product-page level only; help center unreachable)

- Self-labels: "Build a home for your community, events, and courses — all under your own brand." Audience: creators, coaches, brands (Jay Shetty, Tim Ferriss, etc.).
- Product surface set: Community (spaces; discussions; posts and comments with rich media; personalized feed; automated moderation; search with unlimited history; gamification; analytics; directory), Chat, CRM, Events, Live streams, Courses, AI Agents, Email Marketing (broadcasts, automations, audience CRM, segmentation), Payments (branded checkout; one-time purchases, memberships, recurring subscriptions; access groups; affiliates), Website Builder (landing/sales pages connected to memberships), branded iOS/Android app.
- The all-in-one pole: the platform unifies audience, content, and monetization around the community container ("Keep your payments where your content and members are").
- Community philosophy quote from a customer: "nothing does community like Circle" — positioning is community-first with courses/payments attached.

## Product D — Discourse

### Key observations

- Self-labels: "the customizable, scalable community platform powering more than 22,000 communities that create knowledge through conversation"; also "the best community and forum software" (about page) — the vendor straddles the forum/community-platform vocabulary deliberately.
- Use cases: support hub, team workspace, product feedback, developer community — the customer-community goal taxonomy again.
- Building blocks: Customize (themes/branding, searchable public knowledge base, groups and roles); Connect (topics, built-in real-time chat channels, private messaging, email participation); Manage (moderation tools, AI-assisted management, admin dashboard with community health metrics); Grow (SSO and social logins, gamification, SEO).
- Distinctive structures: **trust system** ("As members become trusted regulars over time, they earn abilities to help maintain their community"; about page: "the community builds a natural immune system to defend itself from trolls, bad actors, and spammers — and the most engaged forum members can assist in the governance"); community moderation via flagging; post approval; invite-only mode; private spaces; badges; reply-via-email; mailing-list support; comprehensive API; 100% open source (GPLv2), self-host or managed hosting, "Your data, your control".
- Async-first philosophy: features page opens with "Conversations, not pages" and positions chat as the informal layer whose content "can be quoted in topics where the discussion can continue over time". Customer quote: "if you want the conversation forgotten, put it on Slack. If it matters, put it on Discourse."
- Compare pages name the competitive set: Bettermode, Circle, Discord, Gainsight, Khoros, Reddit, Salesforce, Slack, Vanilla — i.e., the vendor positions simultaneously against community-platform peers, chat tools, a public forum (Reddit), and a CRM/success suite.
- Founded 2013 explicitly to fix the weaknesses of existing forum software; prioritizes "clarity, civility, and long-term knowledge over quick reactions and fleeting engagement".

## Cross-product Comparison

| Structure | Hivebrite | Higher Logic Thrive/Vanilla | Circle | Discourse | Strength |
|---|---|---|---|---|---|
| Operated community container (org creates/brands/owns) | ✓ community hub, Build stage | ✓ "create private, secure communities" | ✓ "home… under your own brand" | ✓ community site, self-host/hosted | 4/4 |
| Managed member population (join machinery + member management) | ✓ signup/SSO/activation, invitations, payments | ✓ member management, security groups | ✓ access groups, payments | ✓ SSO/social login, invite-only, post approval | 4/4 |
| Member profiles | ✓ custom profiles and fields | ✓ profiles w/ permissions, ranked statuses | ✓ directory | ✓ profiles, groups | 4/4 |
| Participatory discussion surface | ✓ forums | ✓ discussions (+Q&A) | ✓ discussions/posts+comments | ✓ topics in categories | 4/4 |
| Groups / sub-spaces inside the container | ✓ groups and sub-communities | ✓ security groups, community types | ✓ spaces | ✓ categories, private spaces, usergroups | 4/4 |
| Moderation toolkit | ✓ (Optimize stage) | ✓ moderation, admin levels, AI Bot Shield | ✓ automated moderation | ✓ flag queue, post approval, trust system | 4/4 |
| Roles / permissions | ✓ roles and permissions | ✓ admin levels, role-based permissions | ✓ access groups | ✓ groups/roles, trust levels | 4/4 |
| Operator analytics / admin dashboard | ✓ analytics & dashboards, engagement scoring | ✓ pre-built/custom reports, admin dashboard | ✓ analytics | ✓ admin dashboard, site analytics | 4/4 |
| Branding / customization | ✓ theming, page builder, white-label app | ✓ layout editor, widget library | ✓ customization, branded app | ✓ theming engine, plugins | 4/4 |
| Search | ✓ AI global search | ✓ federated search | ✓ search w/ unlimited history | ✓ search (+knowledge base) | 4/4 |
| Notifications / email participation | ✓ digests, campaigns, re-engagement | ✓ email templates (+marketing products) | ✓ email hub, push | ✓ reply via email, mailing lists | 4/4 |
| Gamification / earned recognition | ✓ engagement scoring / ladder | ✓ badges, points, leaderboards, ranked statuses | ✓ gamification | ✓ badges, trust system | 4/4 |
| Member-to-member messaging | ✓ messaging | (not directly observed) | ✓ messaging, chat | ✓ personal messaging | 3/4 |
| Events | ✓ core | ✓ Event Manager (payments, presenters, registrants) | ✓ events, live streams | ✗ native (plugin ecosystem) | 3/4 |
| AI assistance | ✓ agents, search, matching | ✓ insights, search assistant, sentiment, MCP | ✓ agents, summaries | ✓ AI plugin (summarize, toxicity, translation) | 4/4 (current market) |
| Integrations / API | ✓ API, CRM, MCP | ✓ Salesforce, Zapier, MCP | ✓ APIs & headless | ✓ comprehensive API, plugins | 4/4 |
| Content publishing beyond discussion | ✓ page builder, recommendations | ✓ blogs, libraries, knowledge base | ✓ website builder, posts | ✓ knowledge base, wiki posts, blog integration | 4/4 (depth varies) |
| Monetization (payments/memberships) | ✓ payments and memberships; Monetize pillar | event payment providers only | ✓ one-time/memberships/subscriptions | ✗ | 2/4 → variant |
| Courses / eLearning | ✗ (mentoring instead) | (not observed this pass) | ✓ courses | ✗ | 1/4 → optional |
| Mentoring / volunteering programs | ✓ mentoring, AI matching | ✓ Mentor Match, Volunteer Manager | ✗ | ✗ | 2/4 → segment-shaped variant |
| Real-time chat channels | ✗ (messaging = DMs) | (not observed) | ✓ chat | ✓ chat channels | 2/4 → optional |
| White-label mobile app | ✓ | (not observed) | ✓ | ✗ (Discourse Hub app) | 2/4 → variant |
| Open-source / self-host | ✗ | ✗ | ✗ | ✓ | 1/4 → deployment variant |
| Ideation / product feedback | ✗ | ✓ Ideation, product feedback process | ✗ | ✓ (voting plugin) | 2/4 → optional |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

```text
Operated community container
└── Managed member population
    └── Shared participatory member spaces
```

1. **Operated community container** — a named, branded community that an organization (distinct from the members) creates, owns, and operates. "Operated" carries the minimal governance sense: someone outside the member body controls the container's existence, structure, and rules. Remove the operator → a self-organizing chat or an anonymous public surface; the software category (sold to organizations) stops existing.
2. **Managed member population** — identified members with profiles whose joining and leaving is controlled (signup/invitation/application/SSO/purchase at the operator's discretion; removal/banning possible). Remove managed membership → an anonymous comment surface or public feed.
3. **Shared participatory member spaces** — one or more places inside the container where members post content and converse with each other (discussion threads being the canonical form). Remove member participation → a broadcast/marketing site, not a community.

Historical check (§24): Ning (2005, operator-built social networks with groups/forums/blogs), Yahoo! Groups (2000, owner-managed membership + shared message/file spaces), and even BBS-era boards (sysop-run, account-holding users, message bases) all satisfy the three invariants. The definition does not depend on SaaS, cloud, AI, gamification, events, or monetization. Passed.

### L1 — Common Mature Structure (present across the sample, not definitional)

- Discussion surfaces organized into spaces (forums/categories/spaces) with topics/posts and replies
- Member profiles and (in most) a browsable member directory
- Groups / sub-spaces / sub-communities inside the container
- Roles and permissions (admin / moderator / member ladders; security groups)
- Moderation toolkit (flag queues, removal, banning; pre-approval in some products)
- Operator analytics: admin dashboard, engagement reports, data export
- Gamification / earned recognition (badges, points, ranks, trust levels, engagement scoring)
- Branding and layout customization (theming, page/layout editors, custom domains)
- Search across members and content
- Notifications and email participation (digests, campaigns, reply-by-email)
- Member-to-member messaging
- Integrations and API (CRM sync, SSO, automation hooks)
- AI assistance (search, summarization, moderation support, matching) — now standard across the current market
- Events (3/4 — common but not universal; Discourse relies on plugins)

### L2 — Variant / Optional Structure

- Monetization: paid memberships, gated access, event payments (Hivebrite, Circle; event payments in Higher Logic) — the seam toward Paid Community Platform
- Courses / eLearning attached to the community (Circle)
- Mentoring / volunteering program modules (Hivebrite, Higher Logic Thrive — association/nonprofit-shaped)
- Ideation / product-feedback machinery (Higher Logic, Discourse plugins)
- Real-time chat channels alongside discussions (Discourse, Circle)
- White-label branded mobile apps (Hivebrite, Circle)
- Knowledge-base / article libraries (Discourse, Higher Logic, Hivebrite page builder)
- Access posture: public and SEO-indexed vs private/gated/invite-only (Discourse supports both modes; Higher Logic markets "private, secure communities") — the seam toward Private Community Platform
- Audience segment: customer communities (support/success/advocacy/feedback), association member communities, alumni communities, creator/fan communities, developer communities, internal/employee communities
- Deployment: multi-tenant SaaS vs open-source self-hosted (Discourse)
- Scale shape: single community vs multi-community/chapter structures (Higher Logic "community types", Hivebrite sub-communities)

### L3 — Vendor-specific (research notes only)

- Hivebrite: Build→Launch→Engage→Grow→Optimize lifecycle framing; Brand/Organize/Engage/Empower/Monetize pillars; AI Matching (Orbiit heritage) for 1:1 video conversations; Journeys; map-based member directory; engagement scoring/ladder; WhatsApp re-engagement channel; ISO 27001/PCI DSS badge set; 2,000+ organizations claim.
- Higher Logic: two-product split (Thrive for associations/member engagement; Vanilla for customer communities); "community-first, only community software" positioning; Mentor Match and Volunteer Manager module names; Ideation module; AI Bot Shield; federated search; ranked statuses; MCP integration to ChatGPT/Claude/Cursor; Smart Campaigns (AI email); Vanilla Forums heritage (founded 2009 Montreal, acquired 2021).
- Circle: "70k+ reviews" badge claims; Email Hub; website builder with funnels; branded app builder ("in under 10 minutes" customer claim); access groups tied to payments; Circle AI agents with "50+ specialized skills"; creator-roster marketing (Jay Shetty, Tim Ferriss, Ali Abdaal…).
- Discourse: trust system with earned abilities; "Conversations, not pages" infinite-scroll topic design; GPLv2 single open-source version; Discourse Hub mobile apps; official compare pages vs 9 competitors; Carwow "put it on Discourse" positioning quote; founded 2013 by Atwood/Ward/Saffron.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model. Notably, two vendors' own marketing polices the Type's boundaries (Hivebrite's "community platform vs chat tools" and "graduate from a social media group" resources; Vanilla's "Slack channels or LinkedIn groups… give your community a home" FAQ; Discourse's compare pages vs Slack/Discord/Reddit) — strong evidence that the market itself treats chat tools, social-media groups, and public forums as adjacent rather than identical.

## Boundary Findings

1. **vs Online Forum (§01.06 sibling, unprocessed)** — the sharpest in-family seam. The sampled market straddles: Discourse self-describes as both "community platform" and "forum software"; orgs have run customer communities on classic forum software for two decades. The defensible structural line: a **forum** is a standing public venue organized around boards/topics, where registration is typically open and the discussion venue is the whole world; a **community platform** is an organization-operated container whose world is the managed member population plus multiple surface families (discussions, groups, events, content, directory) plus operator management and engagement measurement. Nesting: board (surface) ⊂ forum (venue) ⊂ community platform (operated container). Removal tests: remove the operator/management layer → a public forum remains; remove everything but boards → a forum remains; a community platform without forum-style boards (groups/events/content only) is still a community platform. ALIAS-RISK note for the online-forum pass: the two leaves describe overlapping market families; candidate outcomes are keep-both on the venue-vs-container emphasis or a documented overlap zone.
2. **vs Discussion Board (§01.06, processed)** — clean nesting: the discussion board is the topic+reply surface/tool; the community platform is the container that hosts one or more such surfaces among others. Discharges nothing from discussion-board's flags but confirms its tool-vs-venue line extends one level up to container.
3. **vs Q&A Community (§01.06 sibling, unprocessed)** — Q&A organizes participation around question/answer pairs with accepted answers; the community platform organizes around the operated container. Q&A exists as a capability inside community platforms (Higher Logic "Q&A and discussions"; Discourse accepted-answers plugin) — format vs container. Flag for that leaf's pass.
4. **vs Interest Community Platform (§01.06 sibling, unprocessed)** — interest-based consumer communities organize discovery around interests; the community platform leaf is operator-centric and segment-agnostic. Interest communities are frequently *run on* community platforms. VARIANT-RISK: interest-community-platform may be an audience-axis variant of this Type. Flag for its pass.
5. **vs Private Community Platform (§01.06 sibling, unprocessed)** — access posture (private/gated) is a variant of this Type, not a separate structure: Higher Logic markets "private, secure communities" as the default posture while Discourse supports public SEO-indexed communities; Hivebrite markets "private community platform" as a positioning of the same product. VARIANT-RISK: alias/variant candidate. Flag for its pass.
6. **vs Community Chat Platform (§01.01, processed)** — DISCHARGED from this side: none of the four sampled community platforms is chat-centric. Chat appears only as a side surface (Discourse chat channels explicitly subordinate to topics; Circle chat alongside spaces), while the primary object remains asynchronous content under an operated container. The community-chat pass's seam (live rooms under a container vs asynchronous content) holds with direct evidence. Hivebrite, Vanilla FAQ, and Discourse all explicitly position against chat tools (Slack/Discord) — the market polices this seam itself.
7. **vs Research Panel Platform (§06, processed)** — DISCHARGED from this side: the recorded structural test (operator-structured research participation vs member-initiated conversation/content) holds. Insight communities are operator-structured research instruments (recruited members, seeded activities) and stay documented as a panel-platform variant; community platforms host member-initiated conversation/content. Capability overlap exists (ideation/product-feedback modules collect structured member input) but the organizing structure remains the member conversation container, not a research program.
8. **vs Social Network (§01.05)** — a social network's primary surface is the public profile/feed/follow graph with open discovery; the community platform is a bounded, operated container with managed membership. Consumer communities that drift toward open discovery/profile-first surfaces leave this Type.
9. **vs Member Community Platform (§25, unprocessed) / AMS (§25, processed)** — the AMS owns the constituent registry, membership records, and dues; community is one module there (removal test: remove community → AMS remains). Member Community Platform is the membership-organization segment of this Type — joint-review flag for its pass.
10. **vs Alumni Management (§23, processed)** — alumni management owns the alumni register and the institution-run engagement loop; alumni communities are a segment realization of the community platform. Hivebrite straddles (community platform marketed under /alumni-management-software) — the same straddle the alumni pass recorded. Seam: register/relationship system of record vs community container.
11. **vs Paid Community Platform (§27, unprocessed)** — the fulfillment-structure seam recorded by the creator-cluster passes applies: in the creator pole, a purchase converts into venue access and monetization organizes the product; in this Type, monetization is a variant capability (2/4 sample) while the operated container organizes the product. Joint-review flag for its pass.
12. **vs Self-service Support Portal / Customer Portal (§07)** — customer communities serve support goals (case deflection is a named Vanilla solution) but the organizing structure is member-generated discussion, not company-authored content plus case/ticket access. Support-community is a segment variant, not a portal.

## Uncertainties

- Circle's operational depth (roles model, moderation mechanics, SSO specifics) is unverified — help center unreachable; only product-page claims recorded.
- Higher Logic Thrive's full module list (eLearning, chapters, job boards) not exhaustively observed this pass; only KB-indexed modules recorded.
- Whether "engagement scoring" is universal or segment-shaped: observed in Hivebrite (scoring/ladder) and Higher Logic (ranked statuses); Discourse realizes it as the trust system; Circle as generic "gamification". Treated as common (L1) with realization variance, not definitional.
- Events: absent natively in Discourse (plugin ecosystem) — kept out of L1's universal set and marked 3/4 common.
- The exact market boundary between "community platform" and "community engagement platform" (Hivebrite's term) — treated as one category with marketing variation.

## Final Synthesis

The Community Platform is the **organization-operated community container** Type: software an organization licenses to create, brand, populate, govern, and measure its own community for a managed member population. Its world has two structurally different roles — the operator (organization staff: community manager, admin, moderator) who builds spaces, manages membership, moderates, and measures engagement against organizational goals; and the members (customers, association members, alumni, creators' audiences, developers) who join through controlled mechanisms and participate in shared spaces. The defining core is deliberately small: operated container + managed member population + participatory member spaces. Everything else the market associates with the category — forums, groups, events, directories, gamification, analytics, AI, monetization, mobile apps — is standard capability layered onto that container. The Type sits above the forum (venue) and the discussion board (surface) in a nesting relationship, beside the chat container (live rooms) with an async-content seam, and segment realizations (customer, member, alumni, creator communities) remain variants rather than separate Types.
