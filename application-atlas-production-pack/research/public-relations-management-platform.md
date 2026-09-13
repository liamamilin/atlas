# Research Notes — Public Relations Management Platform

Research date: **2026-09-06**

## Research Goal

Understand what a Public Relations Management Platform actually is as an Application Type: what objects exist inside it, what workflow a PR team runs through it, what rules govern media outreach, and where the boundary lies against the neighboring PR-cluster Types in DIRECTORY §06 (Media Relations Platform, Press Release Distribution Platform, Media Monitoring Platform, Social Listening Platform, Social Media Management Platform, Brand Reputation Management) and against Marketing Campaign Management / Email Marketing / CRM.

## Initial Boundary

- Under DIRECTORY §06 Marketing, Advertising & Growth, in the PR cluster. Sibling leaves: Media Relations Platform (unprocessed), Press Release Distribution Platform (processed 2026-09-06), Media Monitoring Platform (unprocessed), Social Listening Platform (unprocessed). Brand Reputation Management, Brand Management Platform, Brand Asset / Guideline Platform already processed.
- Working hypothesis before research: the PR function's work-management system — media contact database + campaign/activity organization + pitch/release outreach + coverage capture + reporting. The "broader suite" that the press-release-distribution pass pointed to.
- Likely confusions:
  - Media Relations Platform (journalist CRM + pitching slice) — probable heaviest overlap; joint-review candidate.
  - Press Release Distribution Platform (gated network broadcast slice) — boundary already documented from that pass ("PR Management = broader suite; distribution is one capability").
  - Media Monitoring Platform (listening slice) — module relationship.
  - Social Media Management Platform (social publishing) — different Type, sometimes bundled.
  - Marketing Campaign Management / Email Marketing (customer audiences, paid/owned outcomes) — different audience and outcome object.
  - CRM (generic relationship records) — PR contact management is CRM-shaped but PR-specific in audience, outbound unit, and outcome.

## Research Questions

1. What are the core objects (contacts, campaigns, pitches, stories, coverage) and how do they relate?
2. What does the PR workflow look like end to end (plan → target → create → send → track → coverage → report)?
3. How does the media contact database work (vendor-maintained vs customer-built; enrichment; consent)?
4. How is outreach sent and tracked (campaign vs 1:1 pitch; engagement tracking; deliverability)?
5. How is earned-media coverage captured and connected back to work and contacts?
6. What reporting does the platform produce (metrics, dashboards, executive/agency reporting)?
7. What roles/collaboration machinery exists (agencies vs in-house)?
8. What is the suite posture — which slices (distribution, monitoring, social, newsroom) are bundled vs separate products?
9. Where is the boundary with Media Relations / Distribution / Monitoring / Marketing campaign tools?
10. Would older/regional PR tooling (card files, clipping bureaus, mail-merged releases) still fit the definition?

## Representative Products

| Product | Tier / philosophy | Evidence quality |
|---|---|---|
| Cision (CisionOne) | Incumbent giant; monitoring+outreach+reporting suite; owns PR Newswire (distribution) | A/B — official product pages fetched (products, journalist-outreach, instant-insights) |
| Meltwater | Intelligence-first suite (media database + press distribution + PR reporting + monitoring + social) | A/B — official product pages fetched (suite, media-database, pr-reporting) |
| Prezly | Story/newsroom-first PR platform; PR-CRM framing; small independent vendor | A — Tier-1 help center fetched (start guide, campaigns, coverage) |
| Onclusive (Contact, ex-PRgloo) | Planning-forward suite (forward events calendar + contacts + newsroom + response desk) | B — official product page fetched; PRgloo redirects to Onclusive |
| Agility PR Solutions | Mid-tier all-in-one workflow platform ("entire PR lifecycle in one platform") | B — official product page fetched |
| Prowly (now Semrush AI PR Toolkit) | Self-serve AI toolkit (database + pitches + monitoring + benchmarking) | B — official page fetched; rebrand observed |
| Muck Rack | Journalist-database-first PR platform | ✗ — 403 on two attempts (root + /pr-software); abandoned per network rule; market context only |

Sampling rationale: incumbent suite (Cision) + intelligence-first suite (Meltwater) + story-first independent (Prezly) + planning-first (Onclusive) + workflow all-in-one (Agility) + self-serve (Prowly/Semrush) — six product philosophies across enterprise/mid-market/SMB tiers. Muck Rack's absence weakens the relationship-first pole; mitigated by Prezly's explicit "PR CRM" framing and Meltwater's "CRM-style relationship history" language.

## Sources

- Cision — https://www.cision.com/products/ ; https://www.cision.com/journalist-outreach/ ; https://www.cision.com/instant-insights-and-reporting/ (retrieved 2026-09-06)
- Meltwater — https://www.meltwater.com/en/suite ; https://www.meltwater.com/en/products/media-database ; https://www.meltwater.com/en/products/pr-reporting (retrieved 2026-09-06)
- Prezly — https://www.prezly.com/ ; https://support.prezly.com/ ; https://help.prezly.com/help/getting-started ; https://help.prezly.com/help/create--send-campaigns ; https://help.prezly.com/help/log--manage-coverage (retrieved 2026-09-06)
- Onclusive — https://www.prgloo.com/ (redirect page) ; https://onclusive.com/en-gb/what-we-do/pr-comms-tools/ → Media Contacts & Events Database page (retrieved 2026-09-06)
- Agility PR Solutions — https://www.agilitypr.com/ (retrieved 2026-09-06)
- Prowly / Semrush — https://www.prowly.com/ (retrieved 2026-09-06)
- Muck Rack — https://muckrack.com/ , https://muckrack.com/pr-software (403 ×2; inaccessible from research environment)

## Product Observations

### Cision (CisionOne)

Evidence: official product pages (products, journalist-outreach, instant-insights-and-reporting).

Key observations:

- Suite structured as modules: **Media Monitoring** (print/online/TV/radio/social/podcast/magazine, real time), **Instant Insights & Reporting** (custom dashboards, "dozens of metrics", executive-ready branded reports), **Journalist Outreach** (media database + pitching), **Social Listening & Management**, **Professional Services**, **CisionOne AI**, **AI Visibility**.
- Positioning: "all-in-one, real time communications platform" for "PR and communications teams"; G2 category badges include "PRCRM" (PR CRM).
- Journalist Outreach: "human-curated database of verified journalists and media outlets" (vendor figure: 500,000+ media profiles across 225 countries/territories — vendor claim); search tools, advanced filters, "insights into the topics journalists are covering"; branded media releases via "intuitive email builder and pre-saved templates"; AI-powered pitch recommendations; engagement tracking on media releases; "combined with your earned media coverage, see how a media release drove story pickup".
- Team alignment: "centralizing all journalist interactions in one convenient place. Build and share media lists, capture important phone and email conversations, assign tasks to the right team members, and when the time is right, generate reports".
- Reporting: measure reach, key-message uptake, sentiment, share of voice; competitor and industry trend tracking; "connect earned media results to business outcomes"; branded executive reports; "React Score" proprietary AI for harmful-content detection.
- Distribution is a **separate product line** (PR Newswire) linked from the same vendor — suite bundling across products, not one object model.
- Use cases listed: PR & corporate communications, brand reputation & crisis, public sector, campaign & event reporting, IR, regulatory compliance, online newsroom hosting, content amplification.

### Meltwater

Evidence: official product pages (suite, media-database, pr-reporting).

Key observations:

- Positioning: "Meltwater Intelligence Platform" — media, social, and AI signals unified; capabilities: Media Intelligence, Social Listening, AI Visibility Tracking, **Media Relations**, Influencer Marketing. Features list: Media Monitoring, Media Database, **Press Distribution**, **PR Reporting**, Social Media Analytics.
- Media database: journalist profiles "continuously updated" (vendor claims: AI crawlers + 90+ analysts; critical changes within 24–48 hours; bounce rate ~7–8%; 800,000+ contacts; Dow Jones exclusive content) — all vendor-stated figures, kept out of canonical claims.
- Discovery: natural-language search ("tech journalists covering AI regulation"), filters by beat/location/outlet/recent coverage; "analyzes what journalists are writing about and recommends the most relevant contacts"; AI-assisted list building and pitch suggestions.
- Outreach: email outreach with engagement tracking; bounce/open/click analytics; "CRM-style relationship history and tracking"; sending "from your own domain" for deliverability; import and enrich existing media lists; integrated press release distribution; GDPR-compliant posture.
- PR reporting: real-time dashboards across earned + social; share of voice; sentiment; automated report generation and distribution (scheduled, delivered to stakeholders); AI-generated executive summaries; customizable KPIs; white-label reporting for agencies; PPT/PDF export; BI integrations; dashboards shareable via links without login.
- Agency posture explicit (white-label, multi-account reporting); enterprise posture (Salesforce/Teams integrations, onboarding services).

### Prezly

Evidence: Tier-1 help center (start guide, campaigns, coverage) + product homepage. Richest operational evidence in the sample.

Key observations:

- Self-description: "PR software platform… manage contacts, publish press releases, host newsrooms, send campaigns, and measure results — all in one place"; "a PR CRM meets a press release editor and sender".
- **Key concepts (help center)**: Contacts (journalists, influencers, stakeholders; "details, preferences, and consent status"; tags/views/filters; engagement tracking), Stories (press releases and news updates; multimedia; translations), Sites (branded newsrooms; collections/categories; media galleries; press kits), Campaigns (mass emails to contact groups; personalization; reports; SPF/DKIM deliverability), Pitches (1:1 personalized emails; templates; open/click tracking), Coverage (track and report media mentions; linked to contacts and stories).
- **Campaign composer (4 steps)**: 1) Compose — sender address (platform address or custom domain; replies route accordingly), content with dynamic personalization fields (with fallbacks), multimedia embeds, embedded story cards (display options), mandatory unsubscribe link (GDPR; auto-added when a story is attached, manual otherwise — editor blocks sending without it), test sends. 2) Select recipients — search/filter, saved contact views, multi-select. 3) Review recipients — flags bounced/unsubscribed contacts, missing email addresses, duplicates; bounced contacts auto-reviewed daily; platform auto-removes bounced on send. 4) Send or schedule — immediate or scheduled; per-campaign tracking toggles (open rates, clicks) that **cannot be changed after sending**.
- **Campaign lifecycle rules**: sent campaigns cannot be deleted ("we need to keep those records"); drafts deletable; scheduled campaigns can be unscheduled back to draft; sent campaigns can be duplicated/re-sent to additional recipients; campaigns without an attached story are not associated with a newsroom.
- **Coverage**: log from a story (paste URLs — auto-imports title/image/intro — or upload files: pdf/doc/xls/images etc.); detail fields: publishing date, outlet (linked organization), author (matched against contacts), site, story; auto-suggestions for author/outlet/story matches; Coverage page with filters (type, site, outlet, date); coverage visible in contact/organization activity feeds; integrations pull in coverage from external providers (Talkwalker, Auxipress, Belga named).
- **Roles**: Admins (billing, IT settings, user roles), Editors (create/publish), Contributors (limited, possibly site-scoped). Agency/team collaboration posture.
- Users named: PR agencies, small businesses/startups, large companies, nonprofits, freelancers.
- Homepage philosophy: stories stay live in owned newsrooms (SEO/AI discoverability) instead of "one-off spark in someone's inbox"; outreach history per contact ("full history of every email sent, every story opened, and every piece of coverage earned. All tied directly to your contact records"); send "from your own domain, not generic@prblaster.com".
- No large proprietary journalist database — contacts are customer-built/imported; vendor offers a paid "curated list building service". This is a meaningful philosophy contrast with Cision/Meltwater/Onclusive/Agility.

### Onclusive (Contact — ex-PRgloo)

Evidence: PRgloo redirect page + Onclusive "Media Contacts & Events Database" product page.

Key observations:

- PRgloo.com now redirects: "PRgloo is now part of Onclusive" — consolidation observation.
- Product framed as "Strategic Media Outreach": "combines strategic PR planning, event intelligence and a verified journalist database… a platform built for proactive communications".
- Components: **Media Contact Database** (vendor figure: 300,000+ contacts; "regular verification and updates"; GDPR-compliant; "Integrated CRM capabilities"), **PR Manager Platform** ("self-service media contact and content distribution platform with workflow support": Response Desk for tracking engagement, Newsroom for content management, distribution tracking and analytics, contact history fully integrated), **Onclusive Planner Intelligence** (vendor figure: 250,000+ future events across 140 categories; "align your communications with the news agenda"; "avoid news conflicts"; plan "months ahead"; in-house research team), **Strategic Intelligence** (forward-looking planning insights).
- Distribution: "distribute press releases directly to journalists and influencers, with full tracking and branded newsrooms".
- Customer quotes evidence workflow integration ("query management and news distribution in one platform"; planning visibility "across our entire team").

### Agility PR Solutions

Evidence: official homepage/product page.

Key observations:

- Positioning: "the only all-in-one… platform to expertly weave AI into every step of the PR workflow"; FAQ: "manage your entire PR workflow from one intuitive platform"; "Manage your entire PR lifecycle in one platform".
- Solutions: **Media Relations** (Create/Target/Pitch: AI drafting of press releases and outreach emails; AI journalist discovery "analyzes your content to identify the most relevant journalists"; personalized pitches "from a single interface"), **Media Monitoring** (traditional + digital channels; "billions of news items indexed annually" — vendor claim), **Social Listening**, **Media Intelligence** (25+ reported metrics, dashboards, AI briefings), **Newswire** (distribution), **PR CoPilot** (AI suite), **Visibility Intelligence** (AI answer-engine presence).
- Use cases: custom reporting, crisis management, reputation & brand insights, executive briefings.
- Managed-services layer: advanced reporting, custom monitoring, full-service support (enterprise/government posture).
- Testimonials evidence daily workflow: media list building, journalist profiles with "what they write about", client reporting for agencies.

### Prowly (now Semrush AI PR Toolkit)

Evidence: official page (prowly.com now fronts the Semrush product).

Key observations:

- Rebrand observed: "Prowly is now the Semrush AI PR Toolkit" — market consolidation observation; self-serve posture ("Sign up", plan picker, free trial).
- Modules: **AI-Cited Media Database** (outlets that shape LLM responses; journalist profiles; audience/traffic data; AI search/keywords/filters), **Email Outreach and Analytics** (AI-drafted emails and press releases; engagement tracking; scheduled follow-ups based on recipient behavior; "automatically track which pitches earned media mentions"), **Media Monitoring** (news/blogs/forums; duplicate/irrelevant filtering; AI summaries; demographic reach), **Strategic Intelligence & Benchmarking** (PR gaps/opportunities report; competitor coverage; share of voice/sentiment/reach benchmarking; campaign dashboard).
- The "which pitches earned media mentions" automatic linkage is direct evidence of the outreach→coverage connection in a self-serve product.

### Muck Rack (unreachable)

403 on both attempts; abandoned. Known in the market as a journalist-database-first PR platform (media database + pitches + monitoring + reports). No claims drawn from it; retained as market context only.

## Cross-product Comparison

| Dimension | Cision | Meltwater | Prezly | Onclusive | Agility | Prowly/Semrush | Layer |
|---|---|---|---|---|---|---|---|
| Media contact records as managed objects (profiles, beats, outlets) | ✓ (Journalist Outreach DB) | ✓ (Media Database) | ✓ (Contacts; customer-built/imported) | ✓ (Contact DB) | ✓ | ✓ | Core |
| Vendor-maintained journalist database (discoverable, enriched) | ✓ | ✓ | ✗ (service offered instead) | ✓ | ✓ | ✓ | Common |
| Saved/shareable media lists; segmentation (tags/views/filters) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Core |
| Organized PR work (campaigns/activities linking contacts+content+results) | ✓ (campaign reporting) | ✓ (campaign tracking) | ✓ (Campaigns) | ✓ (campaign planning) | ✓ | ✓ (campaign dashboard) | Core |
| Outbound sending to selected contacts (pitches/campaigns/releases) | ✓ | ✓ | ✓ (Campaigns + Pitches) | ✓ (distribution) | ✓ | ✓ | Core |
| Engagement tracking on outreach (opens/clicks/replies/bounces) | ✓ | ✓ | ✓ (per-campaign toggles) | ✓ (Response Desk) | ✓ | ✓ | Core |
| Per-contact relationship history (CRM-style activity log) | ✓ ("centralizing all journalist interactions") | ✓ ("CRM-style relationship history") | ✓ (contact activity feed) | ✓ ("contact history fully integrated") | ✓ | ✓ | Core |
| Content creation (releases/stories, multimedia, AI drafting) | ✓ | ✓ | ✓ (Stories) | ✓ | ✓ (PR CoPilot) | ✓ | Common |
| Owned newsroom publishing | optional (use case/microsite) | ✗ (not core) | ✓ (Sites — core) | ✓ (Newsroom) | ✗ (own news site only) | ✗ | Common (core in story-first pole) |
| Earned-media coverage captured & linked back (auto monitoring and/or manual logging) | ✓ (monitoring + release→pickup) | ✓ (monitoring + pitch→mention) | ✓ (Coverage log + provider integrations) | ✓ (tracking) | ✓ (monitoring) | ✓ (pitch→mention auto-tracking) | Core |
| Automated media monitoring engine (news/social/broadcast) | ✓ (core module) | ✓ (core) | ✗ (via integrations) | separate product line | ✓ (core) | ✓ | Common |
| Reporting/dashboards (reach, sentiment, SOV, key messages; executive-ready; scheduled; white-label) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Core |
| Competitor benchmarking / share of voice | ✓ | ✓ | ✗ (not evidenced) | ✗ (not evidenced) | ✓ | ✓ | Common |
| Consent/GDPR machinery (unsubscribe, opt-in, consent status) | (GDPR posture claimed) | ✓ (explicit) | ✓ (explicit, enforced in composer) | ✓ (claimed) | (not evidenced) | (not evidenced) | Common |
| Roles/team collaboration (roles, shared lists, task assignment) | ✓ | ✓ | ✓ (Admin/Editor/Contributor) | ✓ | ✓ | ✓ | Common |
| Newswire distribution integration | ✓ (PR Newswire, separate product) | ✓ (Press Distribution feature) | ✗ | ✓ (direct-to-journalist; newswire not evidenced) | ✓ (Newswire) | ✗ | Variant |
| Social listening/publishing module | ✓ | ✓ | ✗ | ✓ (separate product) | ✓ | ✗ | Variant |
| Forward-events planning calendar | ✗ | ✗ | ✗ | ✓ (Planner Intelligence — distinctive) | ✗ | ✗ | Variant (single-product) |
| AI assistance (drafting, matching, summaries) | ✓ | ✓ | partial | partial | ✓ (PR CoPilot) | ✓ | Common (depth varies) |
| Agency posture (multi-client, white-label reporting) | ✓ | ✓ | ✓ (agencies named) | ✓ | ✓ | ✓ | Common |
| Self-serve vs enterprise contract | enterprise | enterprise | self-serve trial + plans | enterprise | enterprise + services | self-serve | Variant |

## Canonical Model (abstraction)

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a PR management platform:

```text
Media relationship records (journalists / outlets / influencers as managed objects)
└── Organized PR work (campaigns/activities that group contacts, content, and results)
    └── Outbound communications to selected contacts (pitches / releases / campaigns, engagement tracked)
        └── Earned-media coverage captured and connected back to the work and the contacts, made reportable
```

Four properties:

1. **Media relationship records** — the platform holds journalists/outlets/influencers as first-class managed objects (profiles, beats, outlets, history). Without this it is generic campaign management, not PR.
2. **Organized PR work** — outreach is organized into named units (campaigns/activities) that bind contacts, content, and results together, rather than ad-hoc sends. Without this it is a media database or a mail-merge tool.
3. **Outbound communications to selected contacts with tracked engagement** — the platform is the sending surface for pitches/releases/campaigns to media contacts and records how recipients engaged. Without this it is a monitoring platform.
4. **Earned-media coverage captured, connected back, and reportable** — coverage/mentions (auto-monitored and/or manually logged) are recorded as objects linked to the campaigns, stories, and contacts that produced them, and roll up into reporting. Without this it is an outreach sender, not a management system.

Removal tests: remove media contacts → marketing campaign management; remove organized work → media database / media relations slice; remove outbound → media monitoring; remove coverage+reporting → email outreach tool.

### L1 — Common Mature Structure

Very common in mature modern products, not required to recognize the Type:

- vendor-maintained, continuously enriched journalist database (search/filter by beat, topic, location, outlet, recent coverage; role-change alerts; recommendations)
- media list management (saved, shared, segmented lists; import/enrich of customer lists)
- pitch/campaign sending with personalization fields, templates, scheduling, test sends, own-domain sending for deliverability
- engagement analytics (opens, clicks, replies, bounces)
- per-contact activity/relationship history (CRM-style)
- content creation for outreach (press releases/stories with multimedia; increasingly AI-drafted)
- branded newsroom publishing (core in the story-first pole, optional elsewhere)
- automated media monitoring (news, social, broadcast) feeding coverage records
- manual coverage/clipping logging (offline clippings, file uploads) alongside automated capture
- reporting: dashboards and scheduled/executive-ready/white-label reports; reach, sentiment, share of voice, key-message metrics; competitor benchmarking
- team collaboration: roles/permissions, shared lists, task assignment, multi-client (agency) workspaces
- consent/GDPR machinery: unsubscribe enforcement, opt-in/consent status on contacts

### L2 — Variant / Optional Structure

- **Center-of-gravity poles** (same L0, different emphasis): monitoring/intelligence-first (Cision, Meltwater, Agility), relationship/CRM-first (Prezly's PR-CRM framing; Muck Rack per market position), story/newsroom-first (Prezly), planning-first with forward event calendars (Onclusive), self-serve AI toolkit (Prowly/Semrush).
- **Suite posture**: standalone PR suite vs module of a broader marketing/communications-intelligence platform vs point tools chained together; distribution (newswire), social listening, influencer modules bundled or sold separately.
- **Newswire/distribution integration** (press-release distribution as a bundled or sibling capability).
- **Database philosophy**: vendor-maintained proprietary database vs customer-built contacts with enrichment services.
- **Agency vs in-house posture**: multi-client workspaces, white-label reporting, billable reporting.
- **Customer tier / commercial model**: enterprise contracts + onboarding + managed services vs self-serve plans and free trials.
- **AI depth**: drafting, journalist matching, report summaries, harmful-content detection, AI-answer-engine (GEO) visibility tracking.
- **Regional/market variants**: regional media-market databases and language coverage; public-sector and IR postures.

### L3 — Vendor-specific (Research Notes only)

- Cision: CisionOne module names; React Score (harmful-content AI); Media Brief weekly roundup; vendor figures (500,000+ profiles, 225 countries); PR Newswire as separate product line; multiple legacy login surfaces (Communications Cloud, Next Gen/TrendKine, PR Edition/Vocus, Government Relations) evidencing acquisition history.
- Meltwater: Mira/Mira Studio AI; vendor figures (800,000+ contacts, 24–48h critical updates, ~7–8% bounce rate, 90+ analysts, 27,000+ customers); Dow Jones exclusive content; "one source of truth" framing.
- Prezly: 4-step campaign composer specifics; tracking toggles immutable after send; sent campaigns undeletable; unschedule→draft; duplicate-and-resend; bounced auto-review daily; coverage provider integrations (Talkwalker, Auxipress, Belga); curated list building service; site contact signature cards; "%"-personalization with fallbacks.
- Onclusive: Planner Intelligence (250,000+ events / 140 categories — vendor figure); Response Desk; PR Manager Platform naming; PRgloo→Onclusive consolidation.
- Agility: PR CoPilot; Visibility Intelligence; Bulldog Reporter newsletter; "billions of news items indexed annually" (vendor claim); 25+ metrics (vendor claim).
- Prowly/Semrush: AI-cited media database concept; automatic pitch→mention tracking; Semrush rebrand.

## Vendor-specific / Rejected Findings

- All database-size, update-latency, bounce-rate, and coverage-volume figures — vendor marketing claims; excluded from canonical document.
- "AI visibility / GEO tracking" — current-cycle L2 emphasis; the stable structure underneath (monitoring + reporting surface expansion) is already covered.
- Named exclusive content partners (Dow Jones/WSJ) — vendor-specific.
- React Score, Mira, PR CoPilot — branded AI features; L3.
- Prezly's exact composer mechanics (toggle immutability, daily bounce review) — product UI rules; kept in Research Notes; generalized only as "engagement-tracking choices are fixed at send time" style statements where safe (actually kept out of the final document entirely — single-product evidence).

## Boundary Findings

| Neighboring Type | Relationship | Distinction (removal test) |
|---|---|---|
| Media Relations Platform | closest sibling; heavy tooling overlap (both hold media databases and send pitches) | Media Relations centers the journalist relationship and the per-journalist pitch/outreach workflow. PR Management adds the full function loop: organized campaigns, coverage capture, and reporting across the PR function. Remove campaigns/coverage/reporting → Media Relations. **Joint-review flag**: media-relations leaf unprocessed; market vocabulary straddles ("media relations software" is used for full suites like Meltwater's capability page and Agility's solution page). |
| Press Release Distribution Platform | slice/capability | PRD's unit is one authored release broadcast through a gated platform-operated network with a per-release distribution record. PR Management's unit is the ongoing relationship/work/coverage loop; distribution appears only as an integrated or sibling capability (Cision↔PR Newswire, Agility Newswire, Meltwater Press Distribution). Remove the relationship/work loop, keep gated network broadcast → PRD. |
| Media Monitoring Platform | slice/module | Monitoring listens and measures after publication; no contacts, no outreach, no work organization. PR Management consumes monitoring as a coverage source (Prezly explicitly integrates external coverage providers instead of shipping its own engine). Remove contacts/outreach → Media Monitoring. |
| Social Listening Platform | slice/module | Social-conversation listening and analysis; bundled as a module in several suites (Cision, Meltwater, Agility, Onclusive) but a different Type standalone. |
| Social Media Management Platform | adjacent, sometimes bundled | Publishing/scheduling/engaging on social channels is the primary job there; PR suites bundle listening (not publishing-first) — Cision's "Social Listening & Management" is the deepest overlap observed; boundary held on primary job. |
| Marketing Campaign Management Platform | same "campaign" word, different world | Marketing campaigns target customers/prospects for commercial response; PR campaigns organize media-facing work for earned coverage. Different audience object, different outcome object. |
| Email Marketing Platform | same send+track shape, different audience | Opted-in customer audiences vs media contacts; promotional content vs pitches/releases; no earned-media coverage loop. |
| Brand Reputation Management | adjacent (both touch reputation) | Brand Reputation centers the review/rating loop over brand/location entities (per that pass). PR Management centers media relationships and earned coverage. Monitoring modules overlap; primary objects differ. |
| CRM (generic) | structural analogy | PR contact management is CRM-shaped (records, history, activity), and vendors say "PR CRM"; the audience (journalists), outbound unit (pitches/releases), and outcome (earned coverage) are PR-specific — a distinct Type, not a CRM variant. |

Notable in-Type gradient (not separate Types): the center-of-gravity poles listed under L2. Also notable: the market is consolidating (PRgloo→Onclusive; Prowly→Semrush; Cision's many legacy login surfaces) — packaging changes, not core changes.

## Historical / Market-Sample Check

- Pre-digital PR practice (media contact card files/rolodexes + mail-merged typed releases + clipping-bureau coverage + monthly client reports): all four L0 properties hold (relationship records, organized work, outbound, coverage+reporting). ✓
- Regional/national PR tools (European/Nordic/Asian media databases and release tools): same shape — contacts + lists + releases + clippings + client reporting. ✓ (reasoned from product structure; not separately fetched)
- Agency-side vs in-house tools: same objects, agency adds multi-client workspaces and white-label reporting (L2). ✓
- Modern AI-era positioning (AI drafting, AI-answer-engine visibility): new L2 emphases on the same L0. ✓

Conclusion: the definition is not over-fitted to the modern monitoring-suite implementation; the historical card-file+clipping-bureau practice fits the same four-part structure.

## Uncertainties

1. **Muck Rack unreachable** (403 ×2). The relationship-first pole rests on Prezly's "PR CRM" framing and Meltwater's "CRM-style relationship history" language; no claims about Muck Rack specifics anywhere.
2. **Evidence tier**: only Prezly provided Tier-1 help-center documentation; Cision/Meltwater/Onclusive/Agility/Prowly evidence is official-product-page level (Tier-2). No precise operational rules (limits, defaults, state machines) asserted for those products; vendor figures kept as claims in these notes only.
3. **"Campaign" object uniformity**: the organizing unit varies (email campaign in Prezly; reporting container in Cision; planning container in Onclusive). Documented at concept level ("organized PR work"); exact object semantics not generalized.
4. **Media Relations Platform boundary** is the least sharp seam in the cluster — flagged for joint review when that leaf is processed; candidate outcomes: two Types by scope (slice vs whole function) or a consolidation view.
5. **Newsroom publishing** is core in the story-first pole (Prezly, Onclusive) and absent/optional elsewhere — placed in L1/Common with the pole noted, not in L0.
6. **Prowly/Semrush rebrand** observed on the official page; deeper product docs now live under Semrush and were not fetched — Prowly used only as a self-serve market anchor.

## Final Synthesis

A Public Relations Management Platform is the PR function's system of record: it holds media relationships as managed records (journalists, outlets, influencers — from a vendor-maintained database, customer-imported lists, or both), organizes communications work into campaigns/activities, sends and tracks outbound pitches/releases/campaigns to selected contacts, captures earned-media coverage (via built-in monitoring, external coverage integrations, and/or manual clipping logs) connected back to the contacts, stories, and campaigns that produced it, and reports the whole loop as evidence of PR performance. Around this defining loop, mature products add: continuously enriched journalist databases, media list management, engagement analytics, per-contact relationship history, content creation with AI drafting, branded newsrooms, competitor benchmarking, team roles and agency workspaces, and consent/deliverability machinery. The market spans center-of-gravity poles (monitoring-first suites, relationship-first PR CRMs, story/newsroom-first platforms, planning-first platforms with forward event calendars, self-serve AI toolkits) and packaging postures (standalone suites vs modules of communications-intelligence platforms), with distribution (newswire), social listening, and influencer tools appearing as bundled or sibling capabilities. The Type is bounded from Media Relations Platforms (the relationship/pitching slice), Press Release Distribution Platforms (the gated network broadcast), Media Monitoring Platforms (the listening slice), and marketing campaign/email tools (customer audiences and commercial outcomes rather than media relationships and earned coverage).
