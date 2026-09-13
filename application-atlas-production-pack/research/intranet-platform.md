# Research Notes — Intranet Platform

## Research Goal

Understand what an Intranet Platform actually is as an Application Type: what objects exist inside it (sites, pages, news, documents, navigation, components), who builds and operates it, who consumes it, how content is organized/targeted/discovered, how permissions and governance work, and where the boundary lies against adjacent Types — especially Employee Communication Platform (§09, processed), Employee Portal (§10, processed), Enterprise Wiki / Knowledge Base (§02.06), Enterprise Content Management (§10, processed), Enterprise Search Platform (§10, processed), Internal Knowledge Search (§10, processed), Employee Experience Platform (§09, processed), Collaborative Workspace (§03.12, processed), and the public corporate website.

This leaf carries three flags from prior passes that must be resolved or confirmed from this side:

1. employee-communication-platform vs intranet-platform — center-of-gravity gradient (push/targeted distribution vs pull destination); same vendors ship both; Gartner MQ "Intranet Packaged Solutions" places comms-suite products in the intranet category.
2. employee-portal vs intranet-platform / employee-service-portal / employee-service-management — portal is the aggregated entry surface, typically built ON intranet machinery (Powell help center: "Use Powell Intranet to build a complete employee portal"; Microsoft: SharePoint home site is the intranet's "main entry-point").
3. employee-experience-platform vs §09/§10 siblings — EX is a consolidation posture; intranet is one foundation domain (Simpplr "intranet as the foundation", Workvivo "modern intranet").

## Initial Boundary

Initial hypothesis (before research):

- Core use: an organization-operated, authenticated internal web estate — the place employees visit for company news, pages, resources, documents, people, and access to tools. The platform supplies the machinery to build and govern that estate.
- Primary builders/operators: intranet owners, IT admins, site owners, internal comms, department content owners. Primary consumers: all employees (pull).
- Known market ambiguity: the same vendors sell both an intranet and a communication platform; "intranet" is also used loosely for "digital workplace" and "employee hub". The definition must anchor on structure, not labels.
- Adjacent types to separate: Employee Communication Platform (push distribution), Employee Portal (aggregated front door), Enterprise Wiki (open co-authoring), ECM (content system of record), Enterprise Search / Internal Knowledge Search (retrieval-first), Collaborative Workspace (bounded team container), public CMS (audience).
- Directory context: §10 Enterprise Operations & Administration; siblings include Enterprise Content Management, Enterprise Search Platform, Internal Knowledge Search, Employee Portal, Enterprise Request Management, Policy Management.

## Research Questions

1. What are the core objects? (sites, pages, news/posts/channels, documents/resources, navigation, components/widgets, people, tool links)
2. Who builds the estate, with what machinery, and what roles exist on the operator side?
3. How do employees consume it? (visit/navigate/search/subscribe; pull vs push)
4. How do permissions decide what employees see (content, navigation, search results)?
5. How does audience targeting/personalization work, and how does it differ from comms-platform distribution?
6. What employee actions happen inside the intranet vs handed off to other systems?
7. What governance machinery exists (lifecycle, ownership, review, archival)?
8. How does the estate scale (one site vs many sites/hubs/spaces)?
9. Historical check: would portal-server-era, on-prem, and hand-built-era intranets fit the same definition?
10. Where exactly are the lines vs ECP, Employee Portal, Wiki, ECM, Search?

## Representative Products

| Product | Philosophy | Customer tier | Why sampled |
|---|---|---|---|
| Microsoft SharePoint (Microsoft 365) | Suite-native toolkit: assemble an intranet from sites, pages, web parts, hub sites | Enterprise on M365 estates | Largest-reach intranet platform; the "build-your-own" pole; Tier-1 docs publicly fetchable |
| Staffbase (App/Intranet) | Comms-suite intranet module: the web surface of an app-first employee platform; frontline-inclusive | Large enterprise, frontline-heavy | Shows the intranet inside a communication-suite product line; strong Tier-1 help center |
| LumApps | Standalone SaaS intranet-first vendor (Google/Microsoft-native), repositioning as "AI Employee Hub" | Mid-size to enterprise | The turnkey SaaS pole; Gartner MQ / Forrester Wave intranet leader |
| Simpplr | AI-first turnkey SaaS intranet, "intranet as the foundation" of employee experience | Mid-size to enterprise | The modern AI-era pole; same analyst categories |

Cross-references (from processed passes, reused as evidence, not re-fetched):

- Powell Intranet — intranet-in-a-box on Microsoft 365; Tier-1 help center ("build a complete employee portal"), templates/webpart catalogs, three experiences (standard/contribution/administration) — from research/employee-portal.md.
- Liferay DXP — standalone portal-platform machinery (sites, pages, widgets, organizations/roles, SSO/LDAP/SCIM) from which intranets/portals are built — from research/employee-portal.md.
- Microsoft SharePoint home site / Viva Connections — "landing destination, news hub, and the main entry-point to your organization's intranet" — from research/employee-portal.md.
- ContactMonkey glossary definition of "intranet" (pull, private, organization-wide website) — from research/internal-communication-application.md.

Abandoned / not sampled: Interact Software (www.interact.software failed with transport errors on two attempts — abandoned per the network-restriction rule); Happeo (not needed; sample already full); Simpplr help center and LumApps docs (JS shells — see Source-access limitations).

## Sources

Research date: 2026-09-07. Fetched live unless noted.

- Microsoft Learn — Intelligent intranet introduction (SharePoint in Microsoft 365): https://learn.microsoft.com/en-us/sharepoint/intranet-overview
- Microsoft Learn — Planning your SharePoint hub sites: https://learn.microsoft.com/en-us/sharepoint/planning-hub-sites
- Staffbase Support Portal — Content Management category (menu, pages, news, widgets, plugins structure): https://support.staffbase.com/hc/en-us/categories/25325356852754-Content-Management
- Staffbase Support Portal — Staffbase Product Glossary: https://support.staffbase.com/hc/en-us/articles/34983080575506-Staffbase-Product-Glossary
- Staffbase Support Portal — Overview of the Intranet Menu: https://support.staffbase.com/hc/en-us/articles/360010002239-Overview-of-the-Intranet-Menu
- LumApps — Employee Intranet platform page: https://www.lumapps.com/platform/employee-intranet
- LumApps — homepage (positioning): https://www.lumapps.com/
- Simpplr — Modern Intranet / AI Intranet page: https://www.simpplr.com/modern-intranet/
- Simpplr — homepage (positioning, analyst categories): https://www.simpplr.com/

**Source-access limitations:**

- help.simpplr.com and docs.lumapps.com render only a JavaScript shell from this environment; Simpplr and LumApps observations therefore rest on official product/marketing pages (Tier-2). Positioning and feature-surface claims are safe; operational mechanics (exact targeting semantics, permission implementation, versioning behavior) are unverified for these two products and claims about them are kept weak.
- www.interact.software failed with transport errors twice and was abandoned. Interact is NOT used for any claim.
- Analyst-category context (Gartner Magic Quadrant for Intranet Packaged Solutions; Forrester Wave: Intranet Platforms Q2 2026; G2 Employee Intranet Software) is taken from vendor pages citing those reports; the reports themselves were not accessed.

## Product Observations

### Microsoft SharePoint (Microsoft 365)

Evidence layer: A (official Tier-1 documentation, directly fetched).

Key observations:

- Scope framing: "Your intranet might include your organization's main landing page, portals for corporate communications, and individual sites for departments or divisions (like IT or HR)." The intranet is an estate of sites, not one page.
- Documented role model: **organization intranet owners** (overall direction/coordination), **IT pros/admins** (backend configuration), **business owners and site owners** (create/maintain portions), **content authors** (create/manage content on sites and pages).
- Lifecycle stance: "Intranets are a constant work in progress and are never really considered done… otherwise your intranet starts losing value on the day that you launch" — governance/maintenance is part of the product's own guidance.
- Traditional→intelligent framing: "Hierarchical collection of websites" → "Dynamic collection of experiences and services provided by independent site collections"; static FAQ → community-generated content; "Corporate news dominates the newsfeed" → "Personalized news and content is targeted to specific audiences."
- Hub sites: "the 'connective tissue' you use when organizing families of team sites and communication sites together." Three benefits: shared navigation and brand, roll-up of content and search, a home destination for the hub. Sites are peer site collections; hubs "model relationships as links, rather than hierarchy or ownership" so the intranet can absorb reorganizations.
- Building blocks: **Team sites** (collaborate; all members are authors; M365 group), **Communication sites** (communicate; "broadcast a message, tell a story, share content for viewing (but not editing)"; small number of authors, many readers; policies "determined by the organization"), **Hub sites** (connect).
- What successful intranets include (Microsoft's own enumeration): Communication (home page with news, overall navigation, links to key tools), Content (functional parts — HR, Legal, IT "offer their services to the rest of the organization"), Actions and activities (links to time-tracking, expense forms, manager approvals), Collaboration (team places, communities), Culture (profiles, communities, clubs, branding), Mobility, Search ("find content even if they don't know where it lives").
- Audience targeting: files, news, pages, navigation, links, and web parts can be targeted to specific audiences (IdP groups); multiple home experiences per audience (frontline vs desk).
- Security trimming: "Information surfaced on the hub site is security trimmed: if you don't have access to the content, you won't see it." Association with a hub does not change a site's permissions. News flows up from associated sites to the hub.
- Governance plan named as a first-class deliverable: roles and responsibilities, guidelines, compliance and retention, provisioning sites, content-management expectations.
- Numeric specifics (hub count cap 2000, sites web part ≤99, navigation recommendation ≤100, hub search scope ≈2000 sites) — product-specific, kept in notes only.

### Staffbase (App/Intranet)

Evidence layer: A (official help center + glossary, directly fetched).

Key observations:

- The product line is literally named **"App/Intranet"** — one platform delivered as a mobile app and a desktop web intranet. Glossary: "The intranet is the web-based Staffbase platform accessed via desktop browser, providing a central hub for news, pages, collaboration, and company information."
- Content objects (glossary definitions):
  - **Page**: "a content area used to share long-lasting information, resources, or media" — built in a Content Designer from **Blocks**, reusable via **Page Templates**, with AI Page Generation; per-page **Page Editor** role.
  - **News**: "publishing articles, announcements, and updates to employees through channels"; a **Channel** is "a defined stream of news posts, typically organized by topic, audience, or department"; **News Pages** aggregate posts by channel/category/audience.
  - **Widget**: "a web component that adds a specific content block to pages and news posts" (Link Tiles, Link List, Tasks Hub, Microsoft 365 widgets…).
  - **Plugin**: "a mini-application that adds specific functionality" — News, Pages, Chat, Communities, Forms, Event Registration, Meal Plan, Quiz Calendar, Learning.
  - **Menu**: "the primary navigation structure that lets users access different areas of the App or Intranet"; intranet horizontal menu with flyouts to three levels; items are pages, news channels, plugins, folders.
  - **Launchpad**: "a hub… that gives users quick access to links, integrated tools, and external apps."
  - **Space**: "a self-contained area of the platform with its own content, administrators, and audience, used in distributed or multi-brand setups" — the multi-subsidiary/multi-brand scope mechanism.
- Permission-driven navigation: "users only see content in the menu they have access to, by default" — menu visibility follows content permissions; per-device menu-item visibility also exists.
- Dual-surface architecture: **Studio** (operator side: setup, creation, maintenance; roles Administrator / Managing Editor / System-wide Editor / per-page, per-channel, per-plugin editors) vs **User View** (what employees see).
- Identity: SSO, CSV import, SCIM; **Access Code** ("allows users to register… without an email address, typically used for onboarding employees without individual work accounts") — employment-based identity without corporate email; **Public Area** exists for unregistered visitors (separate vertical menu, up to 5 levels).
- Targeting: **User Groups** (manual / conditional attribute-rule / open self-subscribed) + **Profile Fields** "used for targeting content and managing permissions."
- Engagement layer: Chat, Communities, Comments (with moderation: hide/approve/remove), Reactions, Hashtags, Event Registration, Surveys.
- Measurement: per-page and per-news analytics (visitors, views, reach, engagement), Campaigns, Editorial Calendar, alignment surveys.
- Best-practice guidance confirms the destination concept: "On desktop devices, the employee app can serve as the front door intranet that gives access to deeper levels of content"; recommended ≤8 top-level menu topics; keep work and social content separated.
- Compliance surfaces: Legal Documents with target users and confirmation dialogs; multi-language and RTL support; on-demand translation.

### LumApps

Evidence layer: A for the fetched product pages, but Tier-2 (marketing pages only; docs/help center unreachable — JS shell).

Key observations:

- Positioning has drifted across labels but the intranet category persists: legal/JSON self-description "the connected employee hub & intranet solution"; homepage headline now "The leading AI Employee Hub"; the dedicated platform page is titled "Employee Intranet" — "The intranet where work gets done and people connect — combining communication, collaboration, and knowledge in one place."
- Explicit modern-vs-traditional framing: "Traditional intranets were built to publish information, not support daily work. Content gets missed, tools are disconnected…" — modern intranet = Access (news, documents, resources in one experience, personalized content, AI-powered search), Align (consistent desktop+mobile experience; targeted communication), Act ("launch tools, submit requests, and complete tasks directly… with automated workflows and micro-apps").
- Product-page FAQ definition: "An employee intranet is a private, secure network that serves as a company's digital hub… It consolidates various communication channels, internal resources, and business apps into a single, easily accessible platform."
- Feature surface: SSO-connected tools (Microsoft 365, Google Workspace, Workday, Slack); AI search "while respecting permissions"; mobile access incl. frontline; personalized campaigns (AI-assisted drafting; deliver across web/mobile/email); Communities; intranet analytics ("user behavior, engagement, and content performance"); real-time translation (200+ languages claim); **Micro-Apps** (low-code forms for HR requests, IT ticket status, payslips); Agent Hub for company-approved AI agents.
- Analyst-category membership: Gartner Magic Quadrant for Intranet Packaged Solutions; Forrester Wave: Intranet Platforms Q2 2026 (Leader); ClearBox "Leading Product".
- Vendor-claimed scale (7M+ employees) is a marketing number, recorded here only.

### Simpplr

Evidence layer: A for the fetched product pages, but Tier-2 (help center unreachable — JS shell).

Key observations:

- Self-label: "#1 Rated Employee Intranet Software – AI Intranet"; "AI-powered intranet for modern enterprises — Multichannel communications, enterprise search, and AI assistance in one unified experience."
- Four pillars on the intranet page:
  - **Internal communications**: campaigns with Comms AI; targeted landing pages/experiences "for specific audiences, roles, regions, and moments"; delivery "using roles, regions, attributes, or custom targeting rules"; newsletters whose dynamic blocks "pull directly from intranet content."
  - **Employee engagement**: community spaces, recognition/rewards, surveys + sentiment signals, one-to-one and group messaging "built directly into the intranet."
  - **Enterprise knowledge**: permission-aware enterprise search "from every connected system"; synthesized answers; content owners "create, organize, tag, govern, and keep information accurate"; Q&A/discussions turned into discoverable knowledge; knowledge-gap detection.
  - **Work orchestration**: EX agent answering/routing; app tiles "to trigger actions across connected HR, IT, workplace, and business apps"; task tracking; Agent Studio; APIs/connected workflows.
- Governance sentence (product's own FAQ): "Simpplr uses permissions, audience rules, content ownership, approvals, and AI controls… employees only see content and answers that are right for them."
- FAQ contrast: "Traditional intranets often become static content sites. Simpplr connects communication, knowledge, engagement, and everyday work in one AI-powered intranet."
- Analyst-category membership: 3–4x Leader, Gartner MQ for Intranet Packaged Solutions; Forrester Wave: Intranet Platforms Q2 2026; G2 Employee Intranet Software leader.
- Vendor-claimed metrics (2M+ active users, 95% retention, 282% ROI) are marketing numbers, recorded here only.

### Cross-referenced products (from processed passes)

- **Powell Intranet** (Tier-1 help center via employee-portal pass): "Use Powell Intranet to build a complete employee portal"; reusable **Templates catalog** and **Webpart catalog**; three operator experiences (Standard User / Contribution / Administration); "one branded home for news, HR & IT, and search"; HR/IT requests "connected straight to ServiceNow and Workday"; search results carry ownership/validation "receipts"; mobile app with frontline section. Intranet-in-a-box pole on an M365 tenant.
- **Liferay DXP** (Tier-1 docs via employee-portal pass): Sites are "customizable spaces for building personalized digital experiences… applications for building custom solutions, such as portals, intranets"; content/widget pages, fragments, themes, staging/publications; users/organizations/user groups/roles; SSO/LDAP/MFA/SCIM. The platform-machinery pole: the vendor ships the machinery; the intranet is what the customer assembles.
- **SharePoint home site** (Tier-1 via employee-portal pass): "a user experience that serves as a landing destination, news hub, and the main entry-point to your organization's intranet" — the curated home is one surface built on the site estate.
- **ContactMonkey glossary** (via internal-communication-application pass): intranet = "A private, organization-wide website employees use to access company news, documents, and resources" (pull) — used by a comms vendor to separate the two Types.

## Cross-product Comparison

| Dimension | SharePoint (M365) | Staffbase (App/Intranet) | LumApps | Simpplr | Powell / Liferay (x-ref) |
|---|---|---|---|---|---|
| Population & identity | Tenant/Entra employment identity; audiences from IdP groups | SSO/CSV/SCIM; Access Codes for no-email frontline; public area exists | SSO (M365/Google); employment-based | SSO (Okta etc.); permissions + audience rules | M365 tenant identity / directory (LDAP/SSO/SCIM) |
| Building machinery | Sites + pages + web parts; hub sites connect families; communication vs team sites | Pages (Content Designer, Blocks, Templates) + Widgets + Plugins; Menu structure | Branded hub; customizable interface; Micro-Apps (low-code) | Low-code configuration; targeted landing pages; Agent Studio | Templates/Webparts (Powell); Sites/pages/widgets (Liferay) |
| Content types | News, pages, documents, events, links | News posts in channels; long-lived Pages; files; forms | News, documents, resources, communities | News/pages, knowledge (owned/governed), Q&A | Pages/portlets; content articles |
| Navigation / IA | Hub shared navigation; app bar global nav; security-trimmed | Menu with flyouts (≤3 levels); visibility follows permissions; device-specific | One branded hub with sections | Personalized hubs per audience | Site navigation machinery (both) |
| Targeting / personalization | Audience targeting for news/pages/files/links/web parts; multiple home experiences | User groups (manual/conditional/open) + profile fields | Target content by role/location/team; personalized feeds | Audience/role/region targeting; audience rules | Audience targeting (Powell); personalization capability (Liferay) |
| Search | Hub search scopes; org-wide start page | Search results page; M365 search integration | AI search across connected tools, permission-respecting | Permission-aware enterprise search across connected systems | Platform search machinery |
| Actions / tool access | Links to systems; card-based actions (via Viva Connections) | Launchpad; plugin forms; Navigator (ServiceNow forms) | Micro-Apps; submit requests; workflows | App tiles across HR/IT/workplace apps; EX agent | Guided requests to ServiceNow/Workday (Powell) |
| Engagement layer | Viva Engage communities; likes/save | Chat, Communities, reactions, comments+moderation, events | Communities, social wall | Spaces, recognition, surveys, messaging | Community/social features (Powell) |
| Measurement | (via Viva/analytics suite; not central in fetched docs) | Page/news analytics, reach, engagement, campaigns | Intranet analytics (behavior, engagement, content) | Campaign reach/attention/sentiment; adoption; content insights | Engagement analytics (Powell, marketed) |
| Governance | Documented governance plan; permissions; compliance/retention; provisioning | Roles (admin/managing editor/plugin editors); comment moderation; legal-document confirmations; trash | Security & compliance surface | Permissions, audience rules, content ownership, approvals, AI controls | Governance product (Powell); roles/permissions/staging (Liferay) |
| Devices | Web + Teams + mobile app | Desktop web intranet + mobile app (one platform) | Desktop + mobile app; frontline access | Web + mobile + email/chat/newsletters channels | Responsive web; mobile app (Powell) |
| Comms features bundled | News targeting; Viva suite adjacency | Email product, SMS, signage alongside intranet | Campaigns, newsletters | Comms AI, newsletters, crisis comms | Comms publishing (Powell) |
| Substrate | Suite-native (tenant) | SaaS suite module (App/Intranet line) | Standalone SaaS | Standalone SaaS | In-a-box on tenant / self-hosted platform |

Cross-product commonalities (evidence layer B unless noted):

1. **Authenticated organization-internal population**: access is employment-based in every sample (tenant/directory/SSO/HR sync/org-issued accounts). Public openings, where they exist (Staffbase public area), are special surfaces, not the population.
2. **Site/page building machinery usable by non-developers**: pages/sites assembled from reusable components (web parts, blocks, widgets, templates, portlets) with templates and editors; present in every sample including both cross-referenced poles.
3. **Organization-published pull content**: designated organizational publishers (comms, HR, site owners, content authors) create news and long-lived pages/resources; employees visit and read. This is the destination behavior that all products center.
4. **Org-curated navigation / information architecture**: menus, hub navigation, personalized hubs; visibility follows permissions ("users only see content in the menu they have access to" — Staffbase; "security trimmed" roll-ups — SharePoint).
5. **Audience targeting/personalization** of content and surfaces (groups/attributes/roles): all four primary samples.
6. **Search embedded** over the intranet, increasingly across connected systems and permission-aware: all samples.
7. **Tool access and actions**: launchers/tiles/links/micro-apps and request hand-offs into HR/IT/business systems: all samples.
8. **Governance machinery**: operator roles (admin/owner/editor/contributor), permissions, approval/review, ownership/validation metadata, lifecycle (publish/archive/trash): all samples.
9. **Engagement layer** (communities/spaces, comments, reactions, events): all samples.
10. **Measurement** of page/news reach and engagement for the operating teams: all samples.
11. **Mobile companion + desktop web, branding, multi-language**: all samples.
12. **Comms features increasingly bundled** (newsletters, campaigns, targeted email) — the ECP gradient, visible in all four primary samples.
13. **AI assistance** (permission-aware answers, page generation, compose, agents): current-era common, not definitional.

Divergences:

- **Substrate philosophy**: SharePoint is a toolkit (the customer assembles an intranet from sites/hubs; there is no single turnkey intranet object); LumApps/Simpplr are turnkey SaaS (one branded hub out of the box); Powell is in-a-box on a tenant; Liferay is raw platform machinery; Staffbase delivers the intranet as the web surface of an app-first suite.
- **Where "the intranet" lives**: a curated home site (SharePoint home site), the hub itself, the platform root, or a space; products differ.
- **Scope model**: multi-site estates with hub association (SharePoint) vs spaces with their own admins/audiences (Staffbase) vs sections of one hub (Simpplr/LumApps).
- **Public-area openings**: documented for Staffbase only; treated as product-specific.
- **Docs depth**: SharePoint and Staffbase document operational mechanics publicly; LumApps/Simpplr do not (from this environment).

## Abstraction Levels

### L0 — Defining Invariant

1. **Organization-internal authenticated population** — the platform serves one organization's own members; access is employment-based (directory/SSO/HR-sourced identity or organization-issued accounts, including no-email access codes for frontline workers). Not public registration.
2. **Organization-operated building and governance machinery** — the platform provides the means for the organization to create, structure, and govern internal web surfaces: pages/sites composed from reusable components, arranged by navigation, administered through roles and permissions, with a content lifecycle. This is what makes it a *platform* rather than a single delivered page.
3. **A standing internal destination for pull consumption** — authorized organizational publishers place content (news and announcements, long-lived pages, resources/documents, people, tool links) on those surfaces for employees to visit and consume on their own initiative. The intranet is where employees go; it is not primarily a channel that pushes to them.

Test: remove the internal population → a public corporate website/CMS. Remove the building machinery (one fixed, pre-built curated home) → an employee portal (an aggregated front door, not a buildable estate). Remove the pull-destination primacy (make targeted delivery + reach measurement the product) → an employee communication platform. Remove organization authorship/governance (all members co-author freely) → a wiki / collaborative workspace. Remove the site estate entirely (only a pushed news feed remains) → a comms feed.

Historical/market-sample check: portal-server-era platforms (Liferay's documented portal heritage; the on-prem SharePoint portal era) satisfy all three invariants — authenticated internal users, site/page/portlet building machinery, pull publishing. Turnkey SaaS intranets satisfy them. A tenant-embedded M365 intranet satisfies them. A frontline deployment with no corporate email satisfies them (organization-issued access codes, mobile surface). The 1990s hand-built static intranet website is the pre-Type artifact the platform replaced — the Type's floor is the portal-era platform, not the hand-built page, and the check passes for every era in which the *platform* existed. Regional/on-prem/open-source variants all fit. Modern packaging (feeds, communities, AI, micro-apps, mobile apps, newsletters) is NOT in the L0.

### L1 — Common Mature Structure

- News/announcements publishing organized in channels/streams, with audience targeting.
- Long-lived pages and resource areas; document/file access.
- Permission-aware internal search (increasingly across connected systems, with AI answers).
- Org-curated navigation/information architecture whose visibility follows permissions.
- Audience groups/attributes (from HR/identity sources) driving targeting of content and surfaces.
- Tool access and in-place actions: app launchers, link collections, embedded widgets, micro-apps/tiles, request hand-offs into HR/IT/business systems.
- Employee directory / profiles.
- Engagement layer: communities/spaces, comments (with moderation), reactions, events.
- Measurement: page/news analytics, reach, engagement, adoption reporting.
- Governance: roles (admin / intranet owner / site owner / editor / contributor), approval and review workflows, ownership/validation metadata, lifecycle (publish, archive, delete/restore), compliance surfaces (e.g., policy/legal acknowledgements).
- Branding/theming, multi-language support, desktop + mobile access.
- Identity/HR integrations: SSO, directory sync (SCIM/LDAP), HRIS feeds.
- Collaboration-suite embedding (Teams/SharePoint/Google Workspace surfaces).
- AI assistance: permission-aware answers, page generation, drafting, agents (current-era common, recent).

### L2 — Variant / Optional Structure

- Substrate pole: suite-native toolkit (assemble on M365/Google) vs turnkey SaaS intranet vs intranet-in-a-box on a tenant vs self-hosted portal platform vs comms-suite intranet module.
- Center of gravity: knowledge/content home vs comms-heavy vs engagement/culture-heavy vs work-hub (actions, micro-apps, agents).
- Desk/office-first vs frontline-inclusive (no-corporate-email access, mobile-first, shift/location targeting).
- Single global intranet vs multi-brand/multi-subsidiary scope (spaces).
- Public/extranet openings alongside the internal estate.
- AI depth (answers → agents → AI governance controls).
- Deployment: SaaS vs self-hosted vs tenant-embedded.

### L3 — Vendor-specific (Research Notes only)

- SharePoint: hub-site association model, hub-to-hub association, "news flows up" rule, boosted news, Spotlight/Resources caps, hub numeric limits (2000 hubs; sites web part ≤99; nav ≤100 recommended; hub search scope ≈2000), home-site-as-hub choice, SPFx extensibility.
- Staffbase: plugin catalog (Meal Plan, Quiz Calendar, Event Registration…), Access Codes, Public Area with 5-level vertical menu, Spaces, Legal Documents confirmation flows, bottom navigation bar, Navigator AI assistant.
- LumApps: Micro-Apps, Agent Hub, 200+ languages claim, 7M+ employees claim.
- Simpplr: Agent Studio, AI Control Center, Comms AI, EX Agent, sentiment signals.
- Powell: Templates/Webpart catalogs, Governance product, Seasonal Themes, Social Wall.
- Liferay: widget vs content pages, staging/publications, organizations/accounts/user-groups model, personal sites.

## Vendor-specific Findings

- Permission-driven menu visibility is documented directly for Staffbase ("users only see content in the menu they have access to, by default") and security-trimmed roll-ups for SharePoint. The generalized finding — visibility follows permissions across content, navigation, and search — is cross-product; the exact mechanics are product-specific.
- Audience snapshot vs dynamic membership for published content is a known product-level design difference inherited from the ECP pass (Firstup snapshot rule vs Staffbase conditional groups). Not re-researched here; not asserted either way.
- The "public area" (unauthenticated visitors seeing a defined subset) is documented for Staffbase only; treated as product-specific.
- Vendor adoption/scale figures (LumApps 7M+, Simpplr 2M+/95%/282%) are marketing claims, recorded here only.

## Boundary Findings

1. **vs Employee Communication Platform (§09, processed)** — center-of-gravity gradient, not a wall. ECP = organization-authored items pushed to workforce segments across channels with reach measurement; intranet = a standing internal destination employees visit (pull) plus the machinery to build it. The same vendors ship both: Staffbase's App/Intranet line carries push machinery (News/Email/Campaigns/SMS/signage) and pull machinery (Pages/Menu/Plugins/Launchpad) in one platform; Simpplr bundles newsletters/Comms AI on an intranet foundation; Gartner MQ "Intranet Packaged Solutions" covers these same products. Test: remove targeted distribution + measurement → what remains is an intranet; remove the buildable destination estate → what remains is a comms platform. CONFIRMS the ECP pass flag from this side.
2. **vs Employee Portal (§10, processed)** — machinery vs front door. The portal is the single aggregated, curated entry surface; the intranet platform is the machinery for the broader estate of internal sites/pages. The portal is typically built ON the intranet machinery (Powell: "Use Powell Intranet to build a complete employee portal"; Microsoft: home site = "main entry-point to your organization's intranet"). Test: strip the unified entry-point framing (keep many sites, no curated home) → intranet platform; strip the building machinery (keep one curated home) → employee portal. CONFIRMS the employee-portal pass flag from this side.
3. **vs Enterprise Wiki / Knowledge Base (§02.06)** — authoring model. The wiki centers open co-authoring by all members; the intranet centers organization-published content under designated authors/owners with governance. Modern intranets embed wiki-like spaces, and workspace products document "use as intranet" as an overlay (collaborative-workspace pass); the direction of authorship control is the discriminator.
4. **vs Enterprise Content Management (§10, processed)** — surface vs system of record. ECM is the governed repository holding business content with metadata/records/retention; the intranet is the publishing/communication surface employees visit. SharePoint spans both; the ECM pass records that the publishing surface is a common capability, not the ECM definition. Test: remove the repository/records machinery → intranet; remove the publishing/employee-destination primacy → ECM.
5. **vs Enterprise Search Platform / Internal Knowledge Search (§10, processed)** — search is one embedded capability of the intranet; those Types center retrieval as the product. A portal-less search platform is not an intranet; an intranet without search remains an intranet (historically true). Consistent with both prior passes.
6. **vs Employee Experience Platform (§09, processed)** — the intranet is one foundation domain inside EX consolidation postures (Simpplr "intranet as the foundation", Workvivo "modern intranet"); EX is the umbrella, not a sibling structure. CONFIRMS the EX pass flag from this side.
7. **vs Collaborative Workspace (§03.12, processed)** — org-wide publishing estate vs bounded team working container; team sites exist inside intranet platforms (SharePoint's own building blocks distinguish them).
8. **vs Public corporate website / CMS (§02.07)** — audience and authentication: employees vs public visitors; internal resources vs marketing content. Staffbase's public area shows the edge case: a defined subset can be opened to unauthenticated visitors without changing the Type.
9. **vs Employee Service Portal (§09, processed)** — the service portal centers the request loop (catalog → case → fulfillment); inside an intranet it appears as one service stream (tiles/micro-apps handing off to HR/IT systems). Consistent with the ESP pass.
10. **"Digital workplace" / "employee hub"** — marketing umbrella labels used by the same vendors (LumApps "AI Employee Hub"); not distinct structures. Positioning drift does not move a product out of this Type while the core holds.

## Taxonomy Observations

- The leaf stands as a distinct Type: an analyst category exists for it (Gartner MQ Intranet Packaged Solutions; Forrester Wave: Intranet Platforms; G2 Employee Intranet Software), multiple vendors lead with intranet identity, and the structure (buildable/governable internal site estate + pull destination for an employment-based population) is not reducible to any sibling.
- The three prior flags are confirmed from this side and remain **gradient/center-of-gravity seams**: intranet↔ECP (push vs pull, same vendors, bundled products) and intranet↔Employee Portal (machinery vs front door, portal built on intranet machinery). Joint review across the three leaves is still the right instrument; this pass adds the intranet-side evidence and removal tests but does not restructure the directory.
- Suites that name their product line "App/Intranet" (Staffbase) make the seam visible: one platform, two behaviors. The Type boundary inside such suites follows the center of gravity, which is a documentation posture, not a wall.

## Uncertainties

- LumApps and Simpplr operational mechanics (targeting semantics, permission implementation, content versioning, approval chains) are unverified — their help centers/docs are JS shells from this environment; claims about them rest on official product pages and are written at feature-surface strength.
- Interact Software could not be reached (two transport errors); a governance-heavy independent vendor is therefore not in the direct sample. No claim depends on it.
- Whether public-area openings exist beyond Staffbase — unverified; treated as product-specific.
- Whether the SharePoint "news flows up" roll-up direction has equivalents elsewhere — not researched; kept product-specific.
- Numeric limits are recorded only where a vendor documents them; none are generalized.
- Pricing, packaging tiers, and implementation-service models were not researched.

## Final Synthesis

An Intranet Platform is best understood as **the organization's internal web estate plus the machinery that builds and governs it**: an authenticated, employment-based population; site/page construction from reusable components under roles, permissions, and lifecycle governance; and a standing pull destination where the organization publishes news, resources, documents, people, and tool access for employees to visit and consume on their own initiative. The defining core is small — internal population, building/governance machinery, pull destination — and everything else commonly associated with the category (news channels, communities, analytics, micro-apps, AI answers, mobile apps, bundled newsletters) is mature market structure layered on that core. The strongest boundary signals are: audience = the organization's own employees (not the public), structure = a buildable, governed estate of internal surfaces (not one fixed home), and mode = a destination employees visit (not a channel that pushes to them). Where the product's center of gravity moves to targeted distribution and reach measurement it becomes an Employee Communication Platform; where it reduces to a single curated front door it becomes an Employee Portal; the intranet platform is the machinery those surfaces are typically built on.
