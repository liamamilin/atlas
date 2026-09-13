# Research Notes — Private Community Platform

## Research Goal

Understand the Application Type "Private Community Platform" (DIRECTORY §01.06 Community & Discussion) from real products: what the software's world consists of, who operates it and who is admitted, how the closed boundary is built and enforced, how work flows, which states and rules matter, and where the boundaries lie — especially against the parent sibling Community Platform (§01.06, processed, which pre-hung a VARIANT-RISK flag on this leaf), Member Community Platform (§25, processed), Online Forum (§01.06, processed), Interest Community Platform (§01.06, processed), Community Chat Platform (§01.01, processed, joint-review flag), and Paid Community Platform (§27, unprocessed).

## Initial Boundary

Working hypotheses before research:

1. The market uses "private community platform" as a distinct category label (Hivebrite's resource library markets the category repeatedly; Higher Logic Thrive markets "private, secure communities"; the creator-era platforms gate communities by default).
2. "Private" plausibly means: the venue is closed to the general public — non-members can neither read the community nor join freely; entry runs through controlled gates (invitation, application review, payment/membership, SSO/eligibility).
3. The Community Platform pass's flag says gated/private access is "a configuration of this Type" (Discourse supports public-indexed and invite-only modes). The open question this pass must answer: is closed access merely a posture setting (→ variant/alias), or is there a load-bearing structure unique to this leaf (→ keep-both sibling)?
4. Nearest confusions: Community Platform (parent core), Member Community Platform (membership anchoring), Paid Community Platform (purchase→access organizing), Online Forum (public venue), Community Chat Platform (live rooms), Interest Community Platform (venue of many joinable units), Social Network (public graph).

## Research Questions

1. What do vendors themselves mean by "private" in "private community platform" — closed access? confidentiality? verified identity? exclusivity?
2. Is the closed venue the product's native posture in the sampled products, or a configuration of a general-purpose product?
3. What admission machinery is first-class (invitation, application/review, purchase/membership, SSO/eligibility)? Is the gate a structural workflow or a toggle?
4. Does a public surface coexist with the closed venue (storefront/marketing), and what is its role?
5. What does the closed posture organize beyond the Community Platform core (admission queues, access levels, member privacy, trust & safety)?
6. Which capabilities are definitional vs common vs variant vs vendor-specific?
7. Where are the boundaries vs the sibling Types listed above, and can removal tests hold in both directions?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| Hivebrite | organization-operated "community engagement platform"; markets the "private community platform" category itself; member-based organizations (associations, nonprofits, higher-ed alumni, business) | organizations |
| Higher Logic Thrive Community | association/enterprise communities; Tier-1 KB states the product's purpose verbatim: "create private, secure communities" | associations + enterprises |
| Circle | all-in-one creator/brand platform: gated community + courses + payments + public website under the operator's brand | creators / brands / SMB |
| Mighty Networks | creator/entrepreneur pole: hosts sell memberships; funnel → membership → closed community | creators / entrepreneurs |
| Discourse | counter-pole (not a closed-native product): general-purpose open-source community platform where the closed posture exists as explicit, named site configuration | open source → enterprise |

## Sources

Research date: 2026-09-08.

Fetched successfully:

- Hivebrite — official homepage (hivebrite.com → hivebrite.io), full page incl. Build/Launch/Engage stages, highlighted features, industries, and the resource-library index with its "private community platform" resource titles. (Tier 2)
- Higher Logic — official support KB "Getting Started with Higher Logic Thrive Community" (support.higherlogic.com/hc/en-us/articles/360032690892). (Tier 1)
- Circle — official homepage (circle.so), full page incl. Community/Chat/CRM/Events/Courses/Payments/Website Builder blocks. (Tier 2)
- Mighty Networks — official homepage (mightynetworks.com), full page incl. host/membership framing and funnel copy. (Tier 2)
- Discourse — official features page (discourse.org/features), full page incl. the Admin capability list. (Tier 2)

Unreachable / limitations:

- Hivebrite /features/ and /downloads/social-media-to-private-platform/ — 403 (WAF). The "private community platform" resource articles are therefore evidenced at title level only (titles read directly from the homepage's resource index); no article content asserted.
- Circle help center (help.circle.co) — transport error (third failure across passes, consistent with the Community Platform pass's ×2 record); abandoned per network rule. Circle evidence stays at product-page level.
- meta.discourse.org "setting up a private Discourse instance" how-to URL — 404 (stale/guessed link); abandoned. Discourse closed-posture evidence rests on the official features page's Admin list ("Make your site invite-only", "Easily add private spaces", "Email invitations").

Consequence: no precise numeric limits, plan-gating details, or default configuration values are asserted anywhere; all posture/gate descriptions below are capability-level, not mechanism-level.

## Product A — Hivebrite

### Key observations (evidence layer A unless noted)

- Self-labels: "Community Engagement Platform — The community platform built for impact"; sells to member-based organizations: Associations, Non-profit, Higher Ed (alumni), Business.
- Operator lifecycle framing (the vendor's own model): **Build** (branding and theming; no-code page builder; custom user profiles and fields; roles and permissions) → **Launch** (signup, SSO and activation; email invitations; payment and memberships; branded mobile app; map directory) → **Engage** (forums; events; messaging; content and people recommendations; AI global search) → **Grow** (groups and sub-communities; email campaigns and automated digests; multi-channel announcements; mentoring and peer-to-peer programs; API and integrations) → **Optimize** (analytics & dashboards; engagement scoring/ladder; multi-channel re-engagement; automations & AI workflows; moderation).
- The Launch stage is the admission machinery: signup with SSO and activation, email invitations, payment and memberships — i.e., multiple gate types offered as first-class launch features.
- Highlighted features: Groups, Member Directory (map-based), Mentoring, AI Matching (1:1 connections), white-label mobile app.
- The vendor actively markets the "private community platform" category in its resource library (titles read directly from the homepage index):
  - "Five Signs Your Community is Ready to Graduate from a Social Media Group to a Private Community Platform"
  - "Maximize Your Community's Potential with a Private Community Platform"
  - "Leveraging Private Community Platforms: Empowering Venture Capital Firms in a Global Network"
  - "[Infographic] 5 Fears When Switching From Facebook to a Private Community Platform"
  - "8 Tips to Help You Successfully Transition Your Facebook Community to a Private Community Platform"
  - "Public vs. private social media"
  - "Community platform vs chat tools (like Slack & Discord)"
  - "Creating Trust and Safety in Your Online Community | Protect Your Members"
- Reading: for this vendor the "private community platform" is the destination category an organization migrates to from open social surfaces (Facebook groups/social media) — the migration framing confirms the closed boundary is the category's defining characteristic in the vendor's own market story. (Article content unreachable; title-level evidence only.)

## Product B — Higher Logic (Thrive Community)

### Key observations

Tier 1 (support KB, Getting Started with Higher Logic Thrive Community, fetched 2026-09-08):

- "Higher Logic Thrive Community (**Thrive Community**) gives your organization or business the tools that you need to create **private, secure communities** that drive **communication**, **collaboration**, and **engagement** among your members and customers." — the product's stated purpose is private communities for members AND customers.
- Setup structure (the operator's world): **Site design & settings** (Site Management: site navigation & content, password policy, Terms & Conditions, site setup, analytics, advertisements; Community Management: email templates, community discussions and libraries, community types, admin tasks) → **Users** (Member Management: admin levels, moderation, security groups, managing users) → **Modules** (Blogs, Discussions, Ideation; Mentoring/Mentor Match; Volunteering/Volunteer Manager) → **Events** (Event Manager: event types, payment providers, presenters, registrants).
- **Security groups** are the access-control machinery inside the closed venue — per-space/per-group access is managed as a standing administrative object.
- "Community types" implies multi-community structures under one site (e.g., separate communities per chapter/audience — the KB indexes the concept without this pass observing details).

Tier 2 (from the Community Platform pass's official platform-page fetch, 2026-09-07, re-cited):

- "We are community-first, meaning we only provide community software—it is not an add-on to another solution."
- Customer-community goal taxonomy (success/support/advocacy/feedback) and the seam-policing FAQ: "Many online communities start as Slack channels or LinkedIn groups… give your community a home."

## Product C — Circle

### Key observations (product-page level; help center unreachable ×3 across passes)

- Self-labels: "Build a home for your community, events, and courses — all under your own brand." Audience: creators, coaches, brands.
- Community surface set: spaces; discussions; posts and comments with rich media; personalized feed; automated moderation; search with unlimited history; gamification; analytics; directory. Plus Chat, CRM, Events, Live streams, Courses, AI Agents, Email Marketing (broadcasts, automations, audience CRM, segmentation), Payments, Website Builder, branded iOS/Android apps.
- **The closed-venue + public-storefront structure is explicit on the page**: the Website Builder block promises "Design stunning websites, landing pages, and sales pages that flow effortlessly into your courses, memberships, and community" and "Instant member access after signup or purchase"; the Payments block lists "one-time purchases, memberships, recurring subscriptions… access groups". Homepage carousel: "Drive more revenue with **paywalls**".
- Reading: the public web surface (site/landing/sales pages) exists to convert outsiders into admitted members; the community itself is the gated inside ("access groups", paywalls). Purchase is one gate implementation; "access groups" carry the boundary inside the venue.

## Product D — Mighty Networks

### Key observations (product-page level)

- Self-labels: "The Community Platform That Delivers — Community. Courses. Events." Customers are "**hosts**"; the page is organized around hosts selling memberships ("$48 avg monthly price of memberships sold by our Hosts"; revenue calculator "Annual revenue from 30 members at $48/month" — vendor's own representative example, kept here as their claim only).
- **The purchase gate is the organizing story**: "Funnel — Challenges and mini-courses let prospective members get a taste of the membership" → "Membership — Monthly themes, weekly events, daily questions make up the core value of the membership" → "Bonuses — …adds urgency and drives conversion." Product nav: Community, Courses, Members, Marketing, Payments, Admin, AI Cohost.
- Member-participation emphasis: "84% of content on Mighty is created by members, not hosts"; "People Magic… They meet each other." Native mobile apps and branded apps (Mighty Pro) are the differentiating pitch.
- Reading: a closed community whose admission is sold; the operator (host) owns the brand and the member relationship; marketing surfaces exist to fill the gate.

## Product E — Discourse (counter-pole, configuration evidence)

### Key observations

- Self-labels: "the customizable, scalable community platform…" / "the best community and forum software" — a general-purpose product whose communities are commonly **public and SEO-indexed**: the features page lists "SEO optimized for Google indexing and searching" under Configure, and the vendor's own compare set includes Reddit (public forum).
- The closed posture exists as explicit, named **configuration** of the same product — the Admin capability list on the features page: "Make your site invite-only", "Easily add private spaces", "Email invitations", "Post approval", plus SSO and social login under Connect. Chat channels exist as an informal layer explicitly subordinate to topics ("chat messages can be quoted in topics where the discussion can continue over time").
- Reading: "closed venue" is a first-class, recognizable posture that a general-purpose community platform can be switched into — this is precisely what the Community Platform pass flagged. The counter-pole confirms the posture is real and nameable, while the private-native products (A–D) make the posture their identity.

## Cross-product Comparison

| Structure | Hivebrite | Higher Logic Thrive | Circle | Mighty Networks | Discourse (counter-pole) | Strength |
|---|---|---|---|---|---|---|
| Operated community container (org/creator creates, brands, owns) | ✓ | ✓ | ✓ "under your own brand" | ✓ hosts own brand | ✓ | 5/5 |
| Managed member population (join/leave operator-controlled) | ✓ signup/SSO/invitations/payments | ✓ member management, admin levels | ✓ access groups | ✓ Members + Payments | ✓ invite-only/SSO | 5/5 |
| Participatory member spaces (members create the content) | ✓ forums/groups | ✓ discussions/blogs | ✓ posts+comments, "built for member engagement" | ✓ "84% member-led activity" | ✓ topics | 5/5 |
| **Closed-venue posture (whole venue not publicly readable/joinable)** | ✓ private-category marketing; member-org populations | ✓ "private, secure communities" (Tier 1) | ✓ paywalls, access groups; public surface is storefront | ✓ membership-gated community | posture available as configuration, not native | 4/4 closed-native + 1 config pole |
| Multiple gate implementations offered | ✓ invitations, SSO, payment/memberships | ✓ security groups, SSO (platform page) | ✓ signup/purchase | ✓ purchase/membership | ✓ invite-only, SSO | 5/5 |
| Public storefront surface converting to admission | ✓ (organization's own marketing; not product-observed this pass) | (not observed) | ✓ website builder → "instant member access after signup or purchase" | ✓ funnels → membership | ✗ (public archive is the venue in public mode) | 2/4 → common in creator poles |
| Groups / sub-spaces with access levels | ✓ groups, sub-communities | ✓ security groups | ✓ spaces, access groups | ✓ (Members surface) | ✓ private spaces | 5/5 |
| Moderation toolkit | ✓ | ✓ | ✓ automated moderation | (not directly observed) | ✓ flag queue, post approval | 4/5 |
| Roles / permissions | ✓ | ✓ admin levels | ✓ | ✓ Admin | ✓ groups/roles | 5/5 |
| Operator analytics / engagement measurement | ✓ scoring/ladder | ✓ site analytics | ✓ analytics | ✓ (Admin) | ✓ admin dashboard | 5/5 |
| Events | ✓ core | ✓ Event Manager | ✓ events, live streams | ✓ weekly events framing | ✗ native (plugins) | 4/5 |
| Member-to-member messaging | ✓ | (not directly observed) | ✓ messaging, chat | (not directly observed) | ✓ personal messaging | 3/5 |
| Monetization as a gate | ✓ payment and memberships | event payment providers only | ✓ paywalls, subscriptions | ✓ the core business model | ✗ | 3/5 → variant (creator poles) |
| Courses / eLearning | ✗ (mentoring instead) | (not observed) | ✓ courses | ✓ courses | ✗ | 2/5 → optional |
| Mentoring / volunteering / matching | ✓ mentoring, AI matching | ✓ Mentor Match, Volunteer Manager | ✗ | ✗ | ✗ | 2/5 → segment-shaped variant |
| Branding / white-label / branded apps | ✓ | (not observed this pass) | ✓ branded app | ✓ Mighty Pro apps | ✗ (Hub app) | 3/5 → variant |
| Chat channels inside the venue | ✗ (messaging = DMs) | (not observed) | ✓ chat | (not observed) | ✓ chat | 2/5 → optional |
| Open-source / self-host | ✗ | ✗ | ✗ | ✗ | ✓ | 1/5 → deployment variant |
| SEO-indexed public community | ✗ | ✗ | ✗ | ✗ | ✓ default | 1/5 — the counter-pole's identity |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

```text
Operated community container            (shared with the Community Platform core)
└── Managed member population           (shared)
    └── Shared participatory member spaces  (shared)
        └── Closed venue                (the leaf's distinguishing leg)
```

1. **Operated community container** — a named, branded community that an organization or creator (distinct from the members) creates, owns, and governs. (Inherited unchanged from the Community Platform core.)
2. **Managed member population** — identified members with profiles whose joining and leaving runs through operator-controlled mechanisms, with approval/suspension/removal available. (Inherited unchanged.)
3. **Shared participatory member spaces** — places inside the container where members — not only the operator — post content and converse, the discussion thread being the canonical form. (Inherited unchanged.)
4. **Closed venue** — the distinguishing leg: the venue as a whole is closed to the general public. Non-members can neither read the community nor join freely; entry runs through operator-defined gates (invitation, application/review, eligibility, payment/membership, or SSO at the operator's discretion), and where a public surface exists it is a storefront that converts outsiders into admission candidates, not the venue itself. Remove this leg → an open community platform / public forum territory. Add this leg to any operated community container → a private community platform.

Jointly-held is load-bearing (legs 1–3 alone = the parent Community Platform Type, whose realized range includes public SEO-indexed communities; leg 4 alone = a gated content site with nothing communal). The leaf is NOT a strict subset of the parent's L0: the parent's L0 does not imply closedness (its own sample spans public-indexed Discourse communities and private Higher Logic communities), so the closed-venue leg is a genuine addition, not a re-description — this discharges the parent pass's alias question on the side of variant/sibling.

Anti-overfitting: "private" does NOT mean any specific mechanism. No particular gate type (invitation, application, payment, SSO), no identity-verification workflow, no specific privacy feature set is in the core — these are implementations of the gate, exactly as phone number is an implementation of personal addressable identity in IM. The closed-native sample (Hivebrite, Thrive, Circle, Mighty) satisfies leg 4 with four different gate mixes.

Historical check: Ning-era operator-built networks with invite-only/privacy settings (operator + managed population + participatory groups/forums + closed posture) satisfy all four legs; owner-approved closed mailing groups (the Community Platform pass already accepted owner-managed mailing-group communities for its core) satisfy the closed posture at analog level; sysop-approved BBS boards satisfy it too. The definition names no SaaS, cloud, AI, payments, or mobile. Passed (conceptual — no direct archive fetch attempted this pass).

### L1 — Common Mature Structure (present across the sample, not definitional)

- Multiple gate implementations offered side by side (invitation links/emails, application with operator review, purchase/membership, SSO/activation) — admission as a first-class operator workflow
- Member profiles and a member directory (browsable; map-based in one product)
- Groups / sub-spaces with per-space access levels (security groups / access groups / private spaces)
- Discussion surfaces organized into spaces (forums/discussions/topics)
- Moderation toolkit (flag queues, pre-approval postures, removal/banning) and roles/permissions ladders
- Operator analytics: dashboards, engagement measurement/scoring, data export
- Events (native in 4/5)
- Member-to-member messaging
- Notifications, digests, email participation
- Branding/white-label incl. branded mobile apps (3/5)
- Search across members and content
- Integrations/API/CRM sync; AI assistance (search, agents, automation) — current-market standard

### L2 — Variant / Optional Structure

- Monetization as the gate itself: paid memberships/recurring subscriptions/paywalls (creator poles: Circle, Mighty; Hivebrite payment-and-memberships) — seam toward Paid Community Platform
- Attached public storefront machinery: website/landing/sales pages and funnels wired to admission (Circle website builder; Mighty funnels)
- Courses / eLearning attached to the venue (Circle, Mighty)
- Mentoring / volunteering / 1:1 matching programs (Hivebrite, Thrive — association/nonprofit-shaped)
- Multi-community / chapter / community-type structures (Thrive community types; Hivebrite sub-communities)
- Trust/gamification systems inside the closed population (Discourse trust system; Circle gamification; Hivebrite engagement ladder)
- White-label mobile apps (Hivebrite, Circle, Mighty Pro)
- Deployment: multi-tenant SaaS vs open-source self-hosted (Discourse)
- Audience segments: member-based organizations (alumni/associations), customer communities, creator audiences, professional/peer networks (e.g., the VC-network resource title), employee/internal communities
- Public-facing SEO posture — deliberately absent from this Type (the counter-pole's identity)

### L3 — Vendor-specific (research notes only)

- Hivebrite: Build→Launch→Engage→Grow→Optimize lifecycle framing; Brand/Organize/Engage/Empower/Monetize pillar set; AI Matching (1:1 video conversations); Journeys; map-based member directory; engagement scoring/ladder; WhatsApp re-engagement; G2 "Best Community Platform" badge claims.
- Higher Logic: "private, secure communities" purpose statement; Site Management/Community Management/Member Management KB taxonomy; security groups as the access object; Mentor Match / Volunteer Manager / Ideation module names; "community-first, only community software" positioning; two-product split (Thrive associations / Vanilla customer communities).
- Circle: "70k+ reviews" badge claims; AI agents with "50+ specialized skills"; Email Hub; website-builder→membership flow copy; "Instant member access after signup or purchase"; paywall carousel framing; creator-roster marketing.
- Mighty Networks: "hosts" customer vocabulary; Community Design™ framework; AI Cohost; "People Magic"; "84% member-led activity"/"59% return weekly" engagement claims; $500M host-earnings and $48-membership representative figures (vendor claims).
- Discourse: trust system with earned abilities; "Conversations, not pages"; invite-only/private-spaces/post-approval as named admin capabilities; compare pages vs Slack/Discord/Reddit/Bettermode/Circle/Khoros/Vanilla/Gainsight/Salesforce.

## Vendor-specific Findings

None of the L3 items entered the canonical model. Two market observations worth keeping: (1) the "private community platform" category label is policed by vendors themselves as the destination an organization migrates to from open social surfaces (Hivebrite's Facebook-group→private-platform resource cluster; Thrive's "private, secure communities" purpose statement; Circle/Mighty's gated-community defaults) — the closed boundary is the category's market-level defining characteristic; (2) the counter-pole (Discourse) demonstrates the same posture as a switchable configuration, which is why the leaf must be defined by the venue's posture, not by a product family.

## Boundary Findings

1. **vs Community Platform (§01.06, processed) — the parent; DISCHARGES its VARIANT-RISK flag from this side.** Shared legs: operated container + managed population + participatory spaces (this pass re-confirmed all three 5/5). Distinguishing leg: the closed venue. The parent's own sample spans public-indexed (Discourse default) and private (Higher Logic) postures, so closedness is not implied by the parent's L0 — not an alias by the strict-subset test. Removal tests hold both ways: remove the closed leg → public community platform/forum remains; add the closed leg to any operated container → private community platform. Verdict: **keep-both as posture-defined siblings** (member-community-platform / mobile-pos precedent: shared core + one load-bearing distinguishing leg); consolidation candidate (the parent could absorb this as an access-posture variant) recorded for a taxonomy pass. Evidence strength for the distinguishing leg: Tier-1 verbatim purpose statement (Thrive), vendor's own category resources (Hivebrite, title-level), product-page posture (Circle paywalls/access groups, Mighty membership gate).
2. **vs Online Forum (§01.06, processed)** — the public-venue sibling: a forum is a standing venue with typically open registration; the private community platform is a closed venue. A private community can contain forum-style boards (surface nesting board ⊂ forum ⊂ container holds from this side). Seam: open registration/public archive vs controlled admission/no public archive.
3. **vs Community Chat Platform (§01.01, processed) — DISCHARGES the joint-review flag from this side.** The flag asked whether 01.06 processing encounters chat-centric community products. None in this sample: chat appears only as a side surface (Circle chat; Discourse chat channels explicitly subordinate to topics), and one sampled product's own resource library polices the "community platform vs chat tools" seam (Hivebrite). The live-rooms-vs-async-content seam holds; a private posture on a chat server remains that Type, not this one.
4. **vs Member Community Platform (§25, processed)** — the membership-anchored sibling. Its distinguishing leg: population = the organization's own members, member standing as the identity/access axis, community operated as a member benefit with engagement measured toward renewal. This leaf's distinguishing leg: the closed boundary regardless of what the gate binds to (creator audience, customers, alumni, employees, peers) and regardless of whether a membership program exists. Overlap zone: association/alumni communities are both member-anchored AND closed (Hivebrite straddles; consistent with that pass's "openness is operator posture not structure" — there the member relationship is the axis even when opened; here the closed boundary is the leaf's content). Joint-review note recorded for STATUS.
5. **vs Paid Community Platform (§27, unprocessed)** — the creator-cluster fulfillment seam: there, purchase→venue access organizes the product; here payment is one gate mechanism among several (invitation, application, SSO), and the organizing object is the closed venue. Mighty/Circle are monetization-heavy closed-venue poles and remain here; flag for that pass.
6. **vs Interest Community Platform (§01.06, processed)** — a venue of MANY member-joined communities with member-side discovery vs ONE operated closed container; the closed posture is orthogonal to the multi-community structure. Interest communities run on community-platform/private-platform software are instances of those Types.
7. **vs Social Network (§01.05)** — open public profile/feed/follow graph with open discovery vs bounded admitted population. Hivebrite's "Public vs. private social media" and Facebook-group-migration resources police this seam from the market side.
8. **vs Chat tools (Slack/Discord class)** — not a Type in the directory but the market's sharpest everyday confusion; the same three vendors police it explicitly (Hivebrite resource; Thrive/Vanilla FAQ; Discourse compare pages). Chat containers organize live conversation; this Type organizes the closed member venue with persistent participatory content.
9. **vs Self-service Support Portal / Customer Portal (§07)** — customer communities serve support goals but the organizing structure is member-generated discussion in a closed venue, not company-authored content plus case/ticket access.
10. **vs Intranet / Employee Communication (§10/§09)** — employee communities are a segment realization; the seam is the broader internal-communications/intranet surface family vs the community container whose world is member participation and engagement measurement.

## Uncertainties

- Hivebrite's "private community platform" resource articles are title-evidenced only (403 on content); the category's vendor-side definition could not be read in full. No article content is asserted above.
- Circle's operational depth (role model, admission queue mechanics, per-space privacy levels) unverified — help center unreachable ×3 across passes; only product-page claims recorded.
- Higher Logic's gate implementations beyond security groups/SSO (e.g., approval queues) not observed this pass; kept capability-level.
- Mighty Networks' member-management and moderation mechanics not directly observed (homepage-level evidence only).
- Whether an application/review admission workflow is universal across the Type is unverified — recorded as a common gate implementation with low precision, not asserted as definitional or universal.
- Historical check is conceptual (Ning/closed lists/sysop boards); no archive fetched.
- No numeric limits or defaults asserted anywhere; all figures appearing above are vendor marketing claims recorded in research notes only.

## Final Synthesis

The Private Community Platform is the **closed-venue realization of the operated community container**: software an organization or creator uses to run a community whose world — membership, content, spaces — is by design not open to the general public. It inherits the Community Platform's core (operated container, managed member population, shared participatory spaces) and adds one load-bearing structure: the closed venue, where entry runs through operator-defined gates and any public surface is a storefront for admission rather than the venue itself. Because the venue is closed, admission becomes a first-class operator workflow (invitations, applications, eligibility, payment, SSO), the member/non-member boundary becomes the software's organizing boundary (per-space access levels, member privacy, trust & safety), and engagement is measured over an admitted population rather than over public traffic. The leaf stands as a posture-defined sibling of Community Platform (keep-both; consolidation candidate recorded), beside the public Online Forum, the membership-anchored Member Community Platform, and the chat container — with the purchase-gate pole left to Paid Community Platform.
