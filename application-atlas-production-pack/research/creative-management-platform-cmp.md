# Research Notes — Creative Management Platform / CMP

Research date: 2026-09-08
Slug: `creative-management-platform-cmp`
Directory section: 06 Marketing, Advertising & Growth

---

## Research Goal

Understand what a Creative Management Platform (CMP) actually is as an Application Type — the managed objects, the production workflow, the delivery mechanics, and the boundaries with the neighboring ad-tech Types (especially Dynamic Creative Optimization Platform, Ad Server, DSP, and design tools) — well enough that a person who has never used one can model how it works.

## Initial Boundary (working hypothesis before research)

- Hypothesis: a CMP is the creative production/management layer of digital advertising: it turns brand assets into large sets of ad-ready creative variants (sizes, formats, markets, messages), manages their approval/versioning, and packages them for delivery into the ad ecosystem (ad tags, direct platform integrations, exports, or own serving).
- Likely confusions: DCO platform (per-impression decisioning), ad server (delivery/targeting/pacing), design tools (single-artwork production), DAM/brand asset platforms (storage of approved assets), social media management (social scheduling).

## Research Questions

1. What is the managed "object of record" in a CMP — what does a creative consist of in the system?
2. How does scale production work (master → many variants: sizes, formats, markets, languages, messages)?
3. How do creatives leave the platform (tags, direct integrations, exports, own serving)? Who hosts what?
4. Where does data-driven/dynamic creative sit — when is it CMP and when is it DCO?
5. What workflow/governance exists (approvals, brand locks, naming conventions, roles)?
6. What analytics exist and at what granularity?
7. Who uses it (roles, agency vs in-house, designer vs marketer)?
8. Where are the boundaries with DCO, ad server, design tools, DAM, social management?

## Representative Products

Chosen for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Tier / posture | Philosophy observed |
|---|---|---|
| Bannerflow | Mid-market/enterprise SaaS, in-house creative ops + agencies | "Creative Automation Platform"; integrate-out posture: build & host creatives, hand delivery decisioning to your ad server/DSP |
| Bannerwise | SMB/mid-market self-serve SaaS | Explicitly self-labeled "Creative management platform"; simplest articulation of the build→scale→publish loop |
| Celtra | Enterprise | Production + activation + serving + insights loop; GenAI brand governance; DPA catalogs; premium rich media serving |
| Nexd | Specialist CMP, programmatic focus | Layout-library-first, lightweight rich media/video, tag-based trafficking to DSP/SSP/network/trading desk/own ad server; own serving |

Google Web Designer / Google Marketing Platform Studio was considered as a platform-native sample; both Google support domains timed out repeatedly and were abandoned (see Sources).

## Sources

| Source | Layer | Date |
|---|---|---|
| https://www.bannerflow.com/ (product site) | A (official, marketing tier) | 2026-09-08 |
| https://support.bannerflow.com/en/ (help center) + collections (Creative Studio, Campaign Manager, Social Campaign Manager, Publish Your Ads, Analytics, Feeds and Dynamic Ads, Account/Brand Settings) | A (official operational docs) | 2026-09-08 |
| https://support.bannerflow.com/en/articles/5302766-all-supported-ad-networks | A | 2026-09-08 |
| https://support.bannerflow.com/en/articles/3353613-manage-your-publish-options | A | 2026-09-08 |
| https://www.bannerflow.com/features/ad-versioning | A (official, marketing tier) | 2026-09-08 |
| https://www.bannerflow.com/features/dynamic-creative-optimization | A (official, marketing tier) | 2026-09-08 |
| https://www.bannerwise.io/ (product site, self-label "Creative management platform") | A | 2026-09-08 |
| http://help.bannerwise.io/en/collections/2173211-beginner-s-guides | A (official operational docs) | 2026-09-08 |
| http://help.bannerwise.io/en/articles/3749398-all-ways-to-publish-your-ads | A | 2026-09-08 |
| http://help.bannerwise.io/en/articles/3749725-generating-other-sizes-of-your-ads | A | 2026-09-08 |
| https://celtra.com/ (product site) | A (official, marketing tier only — operational help center not fetched) | 2026-09-08 |
| https://www.nexd.com/ + https://www.nexd.com/campaign-manager/ | A (official, marketing tier) | 2026-09-08 |
| G2 "Creative Management Platforms" category badges displayed on nexd.com | B (market-category evidence via vendor-displayed badges) | 2026-09-08 |

Access limitations:
- support.google.com and marketingplatform.google.com timed out repeatedly (2 attempts each); Google platform-native sample dropped.
- Celtra help/support center not fetched; Celtra observations rest on its marketing site (Tier 2) and named-customer quotes displayed there.
- Nexd feed/dynamic capability not directly observed in fetched pages.

---

## Product Observations

### Bannerflow

Evidence layer: A (official site + help center, directly fetched).

Key observations:

- Self-labeling: "AI-powered creative automation platform"; features marketed under Create / Scale / Optimize. (Note: category label drift from "CMP" to "Creative Automation Platform" is visible on the vendor side.)
- Feature set (official): Creative Studio (HTML5 + video ad design, AI-assisted); Scaling & Versioning ("transforms one master creative into every size, format, and market-ready variation"); Dynamic Ads with Feeds ("turn live product data into thousands of dynamic, on-brand ad variations"); Translation & localization (AI-powered translation with brand control); Collaboration (reviews/approvals, version control); Publishing & Scheduling across channels/markets; Real-Time campaign management ("make real-time updates to live campaigns without rebuilding or republishing"); Real-Time Data (creative performance); Creative Optimization (test/scale top performers); DCO feature with an explicit division of labor (below).
- Versioning FAQ (official): "Ad versioning creates channel, audience, and market-specific variations from one master creative. Templates and brand controls ensure every version stays consistent"; automated resizing "preserves layout intent, focal points, safe areas, and copy balance"; bulk editing applies "copy swaps, brand tweaks, or price changes across hundreds of creatives at once"; versioning usable for A/B testing; brand kits + locked components + structured approvals keep consistency; real-time bulk update of prices/CTAs/promos across all versions without rebuilding.
- DCO boundary FAQ (official, load-bearing for Type boundary): "Most optimization tools focus on delivery. Bannerflow focuses on the creative layer that makes personalization possible… Your DCO engine or DSP then applies rules such as geolocation, device, time, and audience to serve the right message… In short, you own the data and media. Bannerflow owns the creative." Also: requires customer's own audience/data source (CDP/DMP/CRM/ad server/feed); Bannerflow helps design templates, shape the feed, tag segments "DCO-ready"; templates "lock fonts, colors, layouts, and legally required elements".
- Publishing architecture (help center, Tier 1): publish options are configured at account level; each publish option is either a **tag** or an **API (direct integration)**; options scoped to brands; per-account ad naming conventions; permission-gated (user role without permission cannot manage publish options); plan-gated via Customer Success Manager.
- Supported destinations (help center): direct integrations (Adform, Adition, Flashtalking, Meta, Google Ad Manager, Campaign Manager 360, TikTok, YouTube, affiliate platforms, etc.); ad tags for a long list of DSPs/SSPs/ad servers/networks (TheTradeDesk, MediaMath, AppNexus/Xandr, Criteo, RTB House, Taboola, Yahoo, etc.); dynamic image tags; DOOH/in-store signage networks (Clear Channel, JCDecaux, etc.); HTML5 full-creative exports for ad servers "when Bannerflow is not hosting the ads"; social networks (Meta, TikTok, LinkedIn direct; Reddit, Snapchat social dynamic); custom onsite publishing on own website.
- Support-center module map: Getting Started; Creative Studio; Campaign Manager; Social Campaign Manager; Publish Your Ads; Analytics; Feeds and Dynamic Ads; Account and Brand Settings.
- Channels claimed: Display, Social, DOOH, In-store, Onsite. Audiences: creative teams, performance teams, marketing leaders; organizations: fully in-house, in-house + agency hybrid, agencies.
- Feed mechanic (official marketing): "Connect your feeds and keep every version updated and in sync automatically."

### Bannerwise

Evidence layer: A (official site + help center, directly fetched).

Key observations:

- Self-labeling: "Creative management platform" (site title tag). Product pillars: Creative enablement (drag-and-drop editor, no coding), Creative automation (autoscaling, "edit all sizes at once or individually", "+90 languages supported"), Creative personalization (dynamic ads via rules & conditions, feed support for all industries, social & display networks).
- Ad types (official): Animated HTML5 ads; Dynamic Display Ads; Dynamic Product Ads (social, e.g. Facebook DPA); in-banner video ads.
- Production model (help center): ads are built in an editor with elements, animations, slides; **sizes are selected at ad setup or added later, including custom sizes (name/width/height)**; an algorithm can auto-generate the next size, reproducing "all slides, elements, and animations from your existing ad set or template", after which elements usually need manual repositioning to be "pixel-perfect"; "generating a complete ad set" is a first-class operation. Unit of organization: the ad / ad set.
- Dynamic mechanics (help center): add a feed (display or social), bind dynamic elements to feed fields, define **dynamic rules & conditions** and **ad layouts** per rule; generate the Social Dynamic Product Ad feed. Facebook DPA connects to Bannerwise.
- Publishing (help center, Tier 1, load-bearing): three export paths — (1) **download** ads and self-upload to the network; (2) **push directly** to an advertising network or DSP ("directly upload your ads and push them to the right campaign"); (3) **generate third-party tags (3PAS)** — "small pieces of code that load in an ad that is stored on an ad server"; hosting choice is explicit (self-host via download vs platform-host via tags). IAB standard specifications are cited as governing ad validity (the article's stated numbers — e.g. 150 KB file size, 30 s duration, 3× loop — are product-stated and dated; do not generalize).
- Audiences (official): Brands, digital marketing agencies, creative agencies; roles: marketers, designers.
- Stats claimed (marketing): 1M+ ad sets published; 1500+ daily users; rated "best support in CMP category" on G2.

### Celtra

Evidence layer: A on marketing-tier facts (official site directly fetched); no operational docs fetched — treat workflow detail as weaker evidence.

Key observations:

- Positioning: "Where creative becomes a performance system — from GenAI-powered production to activation and real-time insights… connects the entire creative lifecycle into one scalable operating model."
- Platform pillars (official): **Creative Automation** (launch complex omnichannel campaigns, AI-led automation); **Dynamic Product Ads** (custom on-brand image and video catalog ads); **Creative Enablement** ("create and serve premium rich media and video ads").
- Scale of serving (official, self-claimed): 450+ enterprise customers; 20M+ ads created annually; **104B+ impressions delivered annually** — i.e. the platform itself serves creatives, not only builds them. Customer quote (Publisher Collective, on site): "design, serve and track a wide variety of different creative types… the user interface for tracking and trafficking ads".
- Live-data creatives (official): "Deploy live-data creatives that respond to pricing, inventory, and market shifts in real-time across 100+ media platforms"; crypto.com quote about live banners reflecting price changes "within 15 minutes" (product-stated anecdote; not generalized).
- Performance intelligence (official): "Score creatives before launch, track which elements drive results, and improve your creative and media strategy with every campaign."
- Automated brand governance (official): "Automated brand governance ensures compliance at scale" for GenAI generation.
- Customers quoted: Unilever ("global partner for Creative Automation… modular and automated digital creative production"), Puma (catalog ads), On (video from catalogs across languages/regions), Wolt (real-time variation previews for feedback), InDrive ("launch thousands of creatives"), McDonald's Nordics, Hearst (publisher side).
- Roles (official): marketing leaders, media teams, creative teams; also **media owners & operators** (publisher-side demand) — a wider audience than the other samples.
- Services: Creative Services (production/consulting), success management, technical services, consulting/training — enterprise delivery model with managed-service component.

### Nexd

Evidence layer: A on marketing-tier facts (official site + Campaign Manager page directly fetched).

Key observations:

- Self-labeling: "CREATIVE MANAGEMENT PLATFORM — build programmatic rich media and video ads"; G2 badges for the "Creative Management Platforms" category displayed on site (market-category evidence that CMP is an active G2 category).
- Production model (official): layout-library-first — "select a layout, then drag-and-drop your video and image assets. Add a CTA… and you're done"; 50+ desktop and mobile layouts; "no developer or a creative agency is required"; every creative has a shareable preview link.
- Manage (official): "Complete control of campaign production and tracking — collaborate, analyze, review, and optimize, all in one place."
- Export (official, load-bearing wording): "Painlessly traffic your rich media ads via DSP, SSP, ad network, trading desk, or your own ad server, thanks to portable, hassle-free, **tag-based publishing**."
- Serving: Nexd serves impressions itself (live campaigns/impressions counters on site; "our ad serving is using 100% renewable energy"; Green Web Foundation certification claim).
- Analytics (official): per-creative engagement ("intentional interactions"), load rate, viewability, CO₂ savings; aggregated summaries per ad type/device and granular per-creative data by date; automated real-time and scheduled reports with shareable URL; export options.
- Differentiator posture: lightweight/fast ads vs "old-fashioned HTML5"; sustainability angle.

---

## Cross-product Comparison

| Aspect | Bannerflow | Bannerwise | Celtra | Nexd |
|---|---|---|---|---|
| Self-label | Creative Automation Platform | Creative Management Platform | Creative Automation / DPA / Creative Enablement | Creative Management Platform |
| Unit of production | master creative → versions; set/campaign containers | ad + ad set with size list | campaigns/packs of creatives ("thousands of creatives") | creative inside campaign, from layout |
| Scale mechanism | auto-resize + versioning + bulk edit + translation | autoscale sizes incl. custom sizes; edit-all-sizes; 90+ languages | AI/modular automated production | layout library + drag-drop assets |
| Feed-driven dynamic | yes (feeds; "DCO-ready" feeds) | yes (dynamic display + social DPA, rules & conditions) | yes (DPA catalog ads; live-data creatives) | not directly observed |
| Delivery packaging | per-destination publish options: tags, API direct integrations, HTML5 export, DOOH, onsite | download / push direct / third-party tags (3PAS) | activation across "100+ media platforms"; own serving | tag-based trafficking to DSP/SSP/network/trading desk/own ad server |
| Who hosts/serves | hosts creatives; audience decisioning explicitly NOT theirs | hosts (tags load ads stored on its ad server); or user self-hosts via download | serves impressions itself | serves impressions itself |
| Creative-level analytics | real-time performance data; optimization | present in product pillar set (not fetched in detail) | pre-launch scoring + element-level post-launch | engagement, load rate, viewability per creative |
| Governance | brand kits, locked components, structured approvals, version control | brand guideline emphasis; (approval detail not observed) | automated brand governance/compliance | review/collaborate |
| Channels | display, social, DOOH, in-store, onsite | display + social (HTML5, video, DPA) | display, video, social, premium rich media | rich media display + video (programmatic) |
| Users | creative/performance teams, marketing leaders; in-house + agency | marketers + designers; brands + agencies | marketing, media, creative teams; media owners/operators | media traders, designers (per G2 reviews shown) |
| Customer tier | mid-market → enterprise brands | SMB → mid-market | enterprise | mid-market/specialist |

### Stable commonalities (evidence layer B — across all four sampled products)

1. **The ad creative is the managed unit of record** — a persistent, identified, versioned advertising artifact (not a generic design file), organized in ad sets/campaigns.
2. **Multi-variant production is the organizing purpose** — one master design systematically becomes the many versions a campaign runs: sizes, formats, channels, markets, languages, messages. Auto-generation is the modern standard implementation (Bannerflow, Bannerwise), but the Type's purpose is variant production, not any particular automation mechanism.
3. **Delivery-chain-ready output** — every product's terminal act is packaging creatives so they can actually run: tags, direct integrations, downloads, or own serving. Ad standards (IAB-derived specs cited by Bannerwise) and per-network packaging (Bannerflow) govern this output.
4. **Creative-level feedback loop** — performance/engagement measured per creative and used to decide what to produce more of (Bannerflow real-time data/optimization; Celtra scoring; Nexd engagement analytics; Bannerwise ROI-focused use cases).
5. **Brand governance over volume** — brand kits/locks/approval (Bannerflow), brand-guideline emphasis (Bannerwise), automated brand governance (Celtra).
6. **Dual audience of designers + marketers** (all four); agency and in-house brand as the two organization poles (all four).
7. **Non-coding editor posture** — "without coding skills" (Bannerwise), "no developer or creative agency required" (Nexd), "without code" (Bannerflow DCO FAQ).

### Where products diverge (implementation/positioning axes)

- **Integration-out vs serve-your-own**: Bannerflow explicitly delegates audience decisioning/optimization to the ad server/DSP and hosts creatives only; Bannerwise offers hosting + tags or download; Celtra and Nexd serve impressions themselves. Both postures coexist inside the same Type.
- **Freeform editor-first vs layout-library-first**: Bannerflow/Bannerwise start from a designed master; Nexd starts from a curated layout library.
- **Category label**: same functional core sold as "creative management platform" (Bannerwise, Nexd, G2 category) or "creative automation platform" (Bannerflow, Celtra).
- **Channel breadth**: display+social core everywhere; DOOH/in-store/onsite as extensions (Bannerflow); publisher-side rich media products (Celtra Creative Enablement, Nexd).
- **AI posture**: current-generation differentiator (AI design help, AI translation, GenAI brand-governed generation) — layered on all poles but not definitional.

---

## Abstraction Levels

### L0 — Defining Invariant

A Creative Management Platform is recognizable by exactly three jointly-held properties:

1. **The ad creative as a managed unit of record** — the system persists, identifies, versions, and organizes advertising creatives (ad slots' artifacts: display banners, rich media, video, social ad units), not merely design files or brand assets.
2. **Systematic multi-variant production as the organizing purpose** — the system exists to turn one design/master into the many concrete versions a campaign runs (sizes × formats × channels × markets × messages), whether generated automatically or produced in a structured in-tool flow.
3. **Ad-ecosystem-ready output** — the terminal deliverable is packaged for the advertising delivery chain: ad tags pointing at hosted creatives, direct push into ad platforms' ad accounts, platform serving, or standards-compliant export for upload into an ad server — the creative must be consumable by ad delivery, not just viewable.

Remove 1 → a design or asset tool. Remove 2 → a single-artwork ad design tool or an ad-scheduling surface. Remove 3 → a generic design/creative production tool with no advertising delivery semantics. All three are held by all four sampled products.

### L1 — Common Mature Structure (present in essentially all mature products; not definitional)

- Visual ad editor (canvas, elements, layers, animations/slides; non-coding posture)
- Brand layer: brand kits, locked template elements, approval workflows, version control
- Asset library as production input
- Size/format scaling machinery (auto-resize, edit-all-sizes, custom sizes)
- Localization/multi-language production
- Feed-driven dynamic creative (map data fields to creative elements; rules/conditions)
- Campaign container for organizing/publishing creatives (incl. naming conventions)
- Social ad platform integrations alongside display networks
- Creative-level analytics/performance reporting
- Role separation of creative vs performance/marketing users

### L2 — Variant / Optional Structure

- Who serves: platform-hosted creatives trafficked to external ad servers (Bannerflow, Bannerwise) vs platform serving impressions itself (Celtra, Nexd)
- Channel scope: DOOH, in-store digital signage, onsite personalization (some products)
- Publisher-side audience: media owners/operators as customers (Celtra, Nexd posture)
- Managed creative services attached to the platform (Celtra)
- Pre-launch creative scoring / AI prediction (Celtra; Bannerflow optimization)
- Catalog/DPA depth (retail/e-commerce variant)
- Sustainability/weight optimization posture (Nexd)
- Free trial/self-serve (Bannerwise, Nexd) vs demo-gated enterprise (Bannerflow, Celtra)

### L3 — Vendor-specific (research notes only)

- Bannerflow's publish-option typology (tag vs API; brand scoping; naming conventions; CSM-plan gating)
- Bannerwise's specific IAB spec numbers (150 KB / 30 s / 3× loop) and "single view / all view" size workflow
- Celtra's claimed operational metrics (450+ customers, 20M+ ads/yr, 104B+ impressions/yr) and crypto.com's "15 minutes" banner freshness anecdote
- Nexd's WebGL/GPU rendering and CO₂ accounting machinery
- G2 badge claims ("best support in CMP category", Leader badges)

---

## Historical / Market-Sample Check (§24 reasoning)

- Would Flash-era rich media production/hosting systems (DoubleClick Studio lineage, Sizmek/MediaMind, PointRoll-style rich media vendors) fit the L0? Creative units built in-tool, versioned per size/placement, hosted by the platform, trafficked via tags into ad servers, with per-creative reporting — all three L0 legs hold. Variant production then relied more on structured manual in-tool flows than auto-generation, which is why L0 leg 2 is phrased as "systematic multi-variant production" rather than "automatic generation". *Confidence: reasoning-based; Google's own docs were unreachable (timeouts), so this check is not backed by a fetched source — flagged as an uncertainty.*
- Platform-native/ad-server-attached creative systems (e.g. Google Marketing Platform Studio + Web Designer) appear to occupy the same core from the ad-server side (host + tag + per-creative reporting; authoring as companion). Not verified — recorded as uncertainty; do not promote to an asserted finding.
- Older display-ad production tools without delivery packaging (pure banner designers) fail leg 3 and are correctly excluded — the boundary has been stable across eras.

## Vendor-specific Findings

See L3 above; none promoted into the canonical core.

## Boundary Findings

- **vs Dynamic Creative Optimization Platform (separate directory leaf)**: sharpest boundary. DCO owns **serve-time, per-impression decisioning** (which creative version for which impression, driven by audience/context data and rules). CMP owns **production/management/packaging of the creative layer** (build the variations, shape the feed, tag segments, keep brand rules). Bannerflow's own DCO FAQ draws this exact line ("You own the data and media. Bannerflow owns the creative"), and requires the customer to bring a CDP/DMP/ad server for decisioning. Both categories share feed-driven dynamic templates — the shared capability is feed population; the discriminator is who/what decides at impression time. A CMP that adds full serve-time decisioning is drifting into the DCO leaf.
- **vs Ad Server / Ad Delivery Platform**: the ad server decides which creative serves to which placement and handles pacing/targeting/impression reporting; the CMP produces and packages the creatives the ad server serves. Bannerwise's 3PAS description ("tags load an ad stored on an ad server") and Bannerflow's "your ad server or DSP handles audience decisioning and optimization" articulate the seam. Variant overlap: Celtra/Nexd bundle narrow serving for their own rich media — the serving is a facilitation of leg 3, not entry into the ad-server Type (no independent targeting/pacing/exchange function observed).
- **vs Graphic Design / Template-based Design Platform**: design tools produce artwork for general design purposes with file export as the end state; a CMP's creative is an ad unit bound to the delivery chain (click-through semantics, ad specs, trafficable tags, campaign naming) and its organizing purpose is campaign variant production. The "no developer or agency required" positioning marks the seam against dev-built HTML5 and agency production, not against general design tools.
- **vs Brand Asset / Guideline Platform (DAM)**: DAM is the governed store of approved assets and guidelines; the CMP *consumes* those assets as production inputs and adds brand locks as guards. Brand kits inside a CMP are governance guards, not the object of record (the creative is).
- **vs Social Media Management Platform**: SMM's primary surface is the social calendar/organic+paid posting; in a CMP social is one delivery destination among many (direct Meta/TikTok/LinkedIn integrations observed) and the object is the ad creative set, not the content calendar.
- **vs Marketing Campaign Management Platform**: MCM plans/audiences/budgets across channels; the CMP is the creative production layer feeding those campaigns. Campaign object exists inside a CMP but only as the organizational container for creatives and publishing, not as budget/planning control.

## Taxonomy Observations (for STATUS Boundary Issues)

1. **Naming drift**: vendors have largely rebranded the same functional core from "Creative Management Platform" to "Creative Automation Platform" (Bannerflow, Celtra), while G2 retains a "Creative Management Platforms" category (Nexd badges; Bannerwise "rated best support in CMP category"). The leaf remains valid as a Type; the alias should be expected when searching the market.
2. **CMP ↔ DCO coupling**: high overlap in marketed features (feeds, dynamic, personalization). Recommendation for the DCO leaf's pass: per-impression decisioning/assembly as the discriminator; treat creative production/packaging as out of scope.

## Uncertainties

- Celtra observations rest on marketing-tier sources only; operational details (workflow UI, approval mechanics) unverified.
- Google platform-native sample (Web Designer/Studio) not verified due to repeated network timeouts; the historical/platform-native fit of the L0 is reasoning-based, not source-backed.
- Bannerwise analytics and approval detail not fetched (help-center collections list them but articles were not opened).
- Nexd feed/dynamic capability not directly observed.
- Precise specs (IAB numbers) are product-stated and dated; not generalized anywhere.

## Final Synthesis

A Creative Management Platform is the creative production-and-management layer of digital advertising. Its defining core: (1) the ad creative as a persistent, versioned unit of record; (2) systematic production of the many variants a campaign needs from one master design; (3) terminal output packaged for the ad delivery chain (tags, direct integrations, exports, or own serving). Around this core, mature products add the editor, brand governance, feeds/dynamic templates, localization, campaign containers, creative-level analytics, and — currently — AI assistance. The Type sits upstream of and alongside ad servers/DSPs/social ad platforms; it is distinct from DCO (which owns impression-time decisioning), from design tools (which end at artwork), and from DAM (which stores inputs). Market labels vary ("creative management" vs "creative automation") but the functional core is stable across all four sampled products and, by structural reasoning, across the older rich-media generation.
