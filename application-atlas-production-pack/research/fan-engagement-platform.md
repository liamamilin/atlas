# Research Notes — Fan Engagement Platform

## Research Goal

Understand what a Fan Engagement Platform is as an Application Type: who operates it (which organizations), what objects exist inside it (fan profile, audience/segment, engagement activity/campaign, engagement surface, participation data, loyalty, sponsorship measurement), how the engage → capture → enrich → re-engage loop works, which capabilities are definitional vs common vs variant, and where the Type's boundary sits — above all against CRM (sports CRM), Customer Data Platform, Marketing Automation, Loyalty Program Management, Social Media Management, the creator-economy Fan Membership Platform / Creator Subscription Platform leaves, and media/content-orchestration platforms.

## Initial Boundary

Working hypothesis before research:

- Core use: organization-side software for sports teams, leagues, venues, and entertainment properties to build direct relationships with individual fans — a fan database/profile layer, engagement activities (campaigns, activations, content, loyalty) run on owned digital surfaces, participation data captured back into profiles, and commercial conversion (ticket leads, sponsorship value, revenue).
- Primary users: marketing/CRM/digital, ticket sales, and sponsorship teams at rights holders (teams, leagues, venues, colleges, federations); fans are the consumer-facing participants, typically free participants (not paying subscribers).
- Nearest neighbors: CRM / sports CRM (relationship-record + sales center), Customer Data Platform / CDP (identity resolution + segments as data infrastructure), Marketing Automation Platform (generic campaign loop), Loyalty Program Management (points/rewards center), Social Media Management Platform (third-party-network engagement), Fan Membership Platform / Creator Subscription Platform (creator-side, fan-pays model), Event/Attendee Management (event-centric), Sports Club Management (§28 — club internal operations), Media Asset Management / Content Distribution (media orchestration).
- Known unknowns: is the fan-facing mobile app definitional? Is loyalty/rewards definitional? Is gamification definitional? Is the sports domain definitional (venues/performing arts are in-sample)? Is a fan-facing surface definitional at all (data/intelligence-first products may have none)? Where exactly is the seam vs CRM and vs CDP? Does the "fan engagement" label also name a creator-economy Type (label collision)?

## Research Questions

1. Who is the operating organization, and who are the fan-facing participants? Is participation free or paid?
2. What is the central object — the fan profile, the campaign/activation, or the audience?
3. What does the engagement loop look like end-to-end (data consolidation → profile → segment → activity → participation → capture → re-engage → commercial outcome)?
4. Is a fan-facing surface (team app, embedded web engine) definitional, or do data-first products satisfy the Type without one?
5. Are loyalty/rewards, gamification, and check-ins definitional or common?
6. How is fan data sourced (integrations with ticketing/merch/CRM/F&B), resolved, and enriched? Who owns it?
7. What commercial outcomes close the loop (ticket leads, sponsorship value, revenue)? Is revenue orientation definitional?
8. How do sponsorship/partnership teams use the platform (sponsored placements, impressions, valuation)?
9. Which poles exist (full-suite vs activation-engine vs intelligence/CDP-first vs content-orchestration)?
10. What is the cadence of use (year-round vs event-driven)?
11. Historical check: do fan-club-era practices (membership lists, direct mail, season-ticket-holder databases) fit the proposed core?
12. Where are the boundaries vs CRM, CDP, marketing automation, loyalty management, social media management, the creator-economy membership leaves, and media orchestration?

## Representative Products

Selected for market representation, documentation availability, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Evidence quality |
|---|---|---|---|
| FanThreeSixty | full-suite engagement platform (fan data platform + team app + email + texting + sales CRM) | mid-market (college athletics, USL soccer, speedways, Broadway/performing arts, HS associations) | Tier 2 product pages directly fetched (home, Fan Data Platform, Mobile App, What Sets Us Apart) (Layer A) |
| FanCompass | activation-engine pole (white-label embedded mobile-web "Fan Engagement Engine", campaign-first) | SMB/mid (200+ colleges, clubs, leagues) | Tier 2 product pages + FAQ directly fetched (home, FC CORE, FAQ, integrations) (Layer A) |
| KORE (KORE Intelligence Platform by Two Circles) | enterprise intelligence/CDP-first pole (Audience Intelligence + Partnership Intelligence) | enterprise (NFL, NBA, Real Madrid, major venues) | Tier 2 platform pages directly fetched (home, Audience Intelligence); help center requires sign-in (Layer A, limitation recorded) |
| Greenfly | content-orchestration pole — boundary probe (short-form media orchestration; fan engagement via content/UGC, no fan database at center) | mid → enterprise (40+ leagues, 500+ teams) | Tier 2 product pages directly fetched (home, UGC Crowdsourcing); helpdesk unreachable (Layer A, limitation recorded) |

Abandoned / unreachable samples (network rule):

- StellarAlgo (fan data platform / sports-CDP pole) — www.stellaralgo.com and stellaralgo.com both 403 twice; abandoned. The data-first pole is nonetheless evidenced structurally by FanThreeSixty's Fan Data Platform and KORE Audience Intelligence.
- Greenfly helpdesk (greenfly.zendesk.com) — 403 + transport error; abandoned. Greenfly evidence is Tier 2 marketing/product pages only.
- KORE help center (help.koresoftware.com) — requires sign-in; no public operational documentation. KORE evidence is Tier 2 platform pages only.

Label-collision check (not a sample of this Type): Passes (passes.com) — self-labels "the all-in-one platform for creator monetization, engagement & growth"; core model is creator-side monetization (memberships, paid DMs, 1:1 calls, livestreams, group chats, merch; creator keeps up to 90%). This is the creator-economy sense of "fan engagement" and belongs to the Fan Membership Platform / Creator Subscription Platform territory, not this leaf. Fetched to resolve the directory-label ambiguity (Layer A).

## Sources

- FanThreeSixty — home: https://www.fanthreesixty.com/ ; Fan Data Platform: https://www.fanthreesixty.com/fan-data-platform ; Mobile App: https://www.fanthreesixty.com/mobile-app ; What Sets Us Apart: https://www.fanthreesixty.com/what-sets-us-apart (all fetched 2026-09-07)
- FanCompass — home: https://www.fancompass.com/ ; FC CORE: https://www.fancompass.com/fc-core ; FAQ: https://www.fancompass.com/faq ; Integrations: https://www.fancompass.com/tech-fc-core (all fetched 2026-09-07; Inspiration Gallery page fetched but its tabbed content is JS-rendered and not readable)
- KORE — home: https://www.koresoftware.com/ ; Audience Intelligence: https://www.koresoftware.com/platform/audienceintelligence (fetched 2026-09-07); help center https://help.koresoftware.com requires sign-in (limitation)
- Greenfly — home: https://www.greenfly.com/ ; UGC Crowdsourcing (+Engage): https://www.greenfly.com/platform/engage-crowdsourcing-ugc/ (fetched 2026-09-07); helpdesk https://greenfly.zendesk.com/hc/en-us unreachable (403, transport error)
- StellarAlgo — https://www.stellaralgo.com/ and https://stellaralgo.com/ both 403 (limitation)
- Passes (label-collision check only) — https://www.passes.com/ (fetched 2026-09-07)

Source-access limitations:

- All four sampled products expose Tier 2 product/marketing pages; none of the sampled vendors exposes a public Tier 1 operational manual for this Type (FanThreeSixty has no public help center; FanCompass FAQ is the closest to Tier 1; KORE help center is sign-in-gated; Greenfly helpdesk unreachable). Operational-detail claims are therefore kept at the strength of product-page + FAQ evidence; precise numeric limits, plan gating, and workflow specifics are not asserted in the final document beyond what the fetched pages directly state.
- StellarAlgo (the named "fan data platform" pole) unreachable; the pole is covered structurally, not by direct observation.
- Sample is US-market-heavy (FanThreeSixty, FanCompass, KORE's US league roster); KORE/Greenfly show international clients (Real Madrid, FC Barcelona, Bundesliga, PSG). Regional products were not sampled; claims kept implementation-neutral.

## Product Observations

### FanThreeSixty — evidence layer A (Tier 2 product pages)

- Self-label: "All-in-one Fan Data Platform & CRM Solution"; "all-in-one engagement platform specifically designed for the sports and entertainment industries". Mission language: help organizations "create impactful engagements that drive revenue".
- Product suite (nav): **Fan Data Platform**, **Mobile App**, **Email**, **Texting**, **Sales CRM**. Industries: Sports Organizations, Entertainment Venues.
- Four pillars on home: Fanbase Development ("understand who your fans truly are… maximize their entire fan journey"), Fan Engagement ("engage your fans in a more intentional way that speaks to them"), Business Efficiency ("aligning your entire organization on one platform"), Revenue Growth.
- Fan Data Platform page — core objects:
  - **Single Fan Profiles**: "all of your disparate pieces of data are filtered from multiple sources down to one snapshot… about one singular person"; continuous audits; proprietary intelligence consolidates fan data; continual enrichment.
  - **Audiences**: segmentation as "the foundation of understanding and connecting with people intentionally"; deep insights into engagement, spending habits, demographics; "120+ Audiences" delivered from day one (vendor claim); custom audience builder; audiences "continually refreshed" (vs static lists), enabling "automated workflows and triggers".
  - **Integrations**: ticketing, merchandise, food & beverage vendors; "hundreds of integrations across our clients"; custom import capabilities.
  - **Campaigns**: "track revenue and sales activities… how your marketing efforts such as emails, programs, and communications influence ticket sales".
  - **Forms**: collect fan information/feedback across channels (same form embedded on website, mobile app, social); responses as "actionable lead lists for your sales team".
  - **Sponsorship**: "sell digital sponsorable assets within each of our communication channels"; real-time impressions; per-impression measurement; "sell sponsorships based on your data valuation".
  - ML models named: lead scoring, at-risk renewal identification, last-minute buyer targeting, donor propensity, RFM analysis.
- Mobile App page:
  - "build a digital home for your diverse fanbase all year round"; personalized content per user; exclusive features for daily engagement.
  - Vendor metrics (claims): 1.4M registered mobile users across the platform; ~4 weeks app deployment; 225,000+ average monthly mobile users.
  - Digital tickets in app; check into events from the app; push notifications for event changes; ticket-fraud reduction framing.
  - **Loyalty Program**: "reward fans with our point system for attendance, extended stays, and sponsorship activations"; **check-in at any venue** (watch parties, away games, sponsorship activations); tailored rewards/offers to high-value or multi-event fans; Apple Wallet membership card.
  - Sponsored content placements; fanbase development through app identification; live video, trivia, prize giveaways as engagement features.
  - **App Manager**: self-service content management without app-store updates.
  - App + Fan Data Platform integration framed as revealing the "full potential fanbase".
- What Sets Us Apart page:
  - Data ownership: "**Your data is yours**"; hundreds of attributes per profile; daily integration management; AI/data-science-built behavior-based audiences; trigger-based automations; dedicated account manager.
  - Vendor claims: 600+ daily data quality checks per client; 120+ algorithms from day one; AI identifies fans with "up to 25 times higher likelihood of purchasing tickets" (vendor claim, recorded as such).
- Client roster (market-structure evidence): college athletics (Kansas, USF, Rice, Wright State), USL soccer clubs (many), NASCAR speedways (SMI chain), Broadway Across America theaters, performing arts centers, high-school athletic associations, Little League World Series, Special Olympics, Kansas City Symphony. Integrations named: Tessitura (arts ticketing/CRM), Salesforce.

### FanCompass — evidence layer A (Tier 2 product pages + FAQ)

- Self-label: "Convert Fan Engagement into Revenue"; "Engage Fans. Capture Data. Generate Revenue."; FC CORE = "white-labeled, mobile-web fan engagement engine that centralizes fan access, data, and revenue in one always-on destination".
- Three-part pitch: **Engage Fans** (dynamic activations that "build deeper relationships with every interaction"), **Capture Data** ("continuously captures first-party, progressive fan data at scale, fueling CRM, ticketing, sponsorship, and marketing teams"), **Generate Revenue** ("qualified sales leads directly to your ticketing, marketing, and sponsorship teams").
- FC CORE product page:
  - "fully white-labeled, mobile-web technology that plugs into your tech stack in minutes".
  - "Create and launch unlimited engaging activations that keep fans coming back while building richer, more actionable fan profiles with every interaction."
  - Continuous engagement fuels "zero & first-party data, activates sponsors, and delivers qualified ticket leads".
  - "integrates directly into 100+ CRM technologies and SMS systems".
  - Tiers: FC CORE (engine), FC CORE+ (adds full-service managed support: strategy, execution, graphic design, metrics reporting), FC CORE PREMIUM (adds multilingual translation, season-to-season reporting, SSO, paid social promotion for sponsored campaigns), FC CORE ENTERPRISE (adds "Enterprise Multi-Engine Org View" for leagues/organizations with multiple properties — org-level campaigns plus per-property engines).
  - Nielsen Sports Digital Valuation Calculator (proprietary, with FC CORE+): sponsorship media-value rate card for brand partners.
- FAQ (operational evidence):
  - Revenue paths: "ticket leads/sales, marketing leads, sponsored campaigns, and data collection".
  - Deployment: embedded or i-framed into the organization's website, microsite, or official team app; "no visible FanCompass branding"; "no apps to download or messy re-directs"; mobile-first (desktop/tablet/phone).
  - Setup: "within a matter of hours" once web/app admin is connected.
  - Cadence: "Campaigns should be run year-round. Continuously, during the season and monthly, at minimum, during the off-season."
  - No limit on number of campaigns; simultaneous campaigns encouraged (cross-promotion through one entry point).
  - Management effort: "roughly thirty minutes to an hour each week" to set up and maintain campaigns.
  - Integration: "open API platform with the ability to integrate into any CRM, Data Warehouse, Marketing Tools".
- Integrations page: Salesforce, HubSpot, Microsoft Dynamics, KORE, Ballpark, SAP, Okta (SSO), Sidearm Sports, YinzCam (team-app platform), Deltatre, Metabase, MailChimp, Google/Meta/LinkedIn/X/Weibo — CRMs, team-app vendors, social platforms, data tools.
- Case-study framing (vendor claims): sponsor-branded activations (Knorr × Liga MX/USL clubs) with engagement/impression metrics; "200+ colleges, clubs, and leagues".

### KORE (KORE Intelligence Platform by Two Circles) — evidence layer A (Tier 2 platform pages; help center sign-in-gated)

- Self-label: "The Operating System for the Business of Sport"; "KORE Intelligence Platform by Two Circles"; "Intelligence That Drives Better Business Decisions" — "AI-powered intelligence built for the sports and entertainment industry… grow stronger fan and partner relationships".
- Two modules: **Audience Intelligence** and **Partnership Intelligence**.
- Audience Intelligence page:
  - Challenge framing: "Fan data lives across multiple systems, making it difficult to build a complete picture of your audience, personalize engagement, and measure what matters."
  - Solution: "brings together fan data from across your organization, giving every team a deeper understanding of who your fans are, what they care about, and how to build stronger relationships."
  - How-we-help: Know Fans Best ("complete view of every fan with connected data"); Grow Fan Relationships ("more relevant experiences that increase engagement, loyalty, and lifetime value"); Understand Fan Behavior ("trends, preferences, and opportunities through AI powered intelligence"); Make Smarter Decisions ("trusted audience intelligence that drives action").
  - Connected systems diagram: CRM, Ticketing, Digital, Ecommerce, Marketing → KORE Audience Intelligence ("single source of connected data").
  - Audience (FAQ): "Rights holders, leagues, teams, federations, and brands"; insights shared across "marketing, commercial, partnerships, and leadership teams".
- Home page: customer quotes emphasize fan understanding ("more than knowing who bought a ticket… how they engage, what brings them back") and partnership/sponsorship measurement; PWHL quote on centralized commercial platform for sponsorship operations.
- Client roster: NFL, NBA, NASCAR, Real Madrid, FC Barcelona, MLB/NHL/NFL teams, Madison Square Garden, brands (Verizon, U.S. Bank).
- Note: KORE historically marketed "fan engagement CRM"; current positioning is intelligence-first with a partnership (sponsorship) intelligence module — the enterprise data/insight pole of this space. No fan-facing surface is marketed; engagement execution happens in the organization's connected systems.

### Greenfly — evidence layer A (Tier 2 product pages; boundary probe)

- Self-label: "Short-Form Media Automation & Distribution Software"; "short-form media orchestration platform"; "Create. Collect. Organize. Distribute. Monetize."; "Trusted by Over 40 Leagues and 500 Teams" (vendor claim).
- Platform modules (nav): AI-Powered Organization, Media Collection, Content Distribution, Remote Media Creation, UGC Crowdsourcing, Media Aggregation, Group Communications, Analytics & Measurement, Mobile App.
- Core model: collect media from creators/photographers at events in real time; AI subject-ID and intelligent routing into galleries; personalized channels/galleries per individual or group; distribute to athletes, staff, sponsors, broadcasters; measure social impact and sponsor activation value.
- Fan-facing side: **Greenfly +Engage (UGC Crowdsourcing)** — fans/followers/public submit original photos/videos via a custom branded webpage or embeddable widget on the organization's website or mobile app; every submission "includes the transfer of perpetual, license-free usage rights"; contact info collected "for your CRM or mailing list, to notify winners"; submissions reviewed/approved in-platform, searchable, exportable, distributable.
- Role framing: "Digital Marketing — Fan Engagement" is one of three role pages (with Corporate Partnerships, Broadcast + Media Rights); "Turn on Your Fan Engagement Machine" — fan engagement achieved by expanding content reach through athletes/partners/broadcasters onto digital platforms.
- Boundary-relevant: no fan database or fan profile is the center; the fan is reached through social/broadcast distribution of content; the persistent objects are media assets, galleries, channels, and contributor groups. Fan contact capture exists only at the UGC-activation edge.

### Passes — label-collision check (Layer A; not a sample of this Type)

- Self-label: "The all-in-one platform for creator monetization, engagement & growth"; "a platform for creators to scale their content and own their audiences".
- Core model: creator-side monetization — memberships (tiered recurring access), paid DMs, 1:1 calls, livestreams, group chats, merch & digital sales, discounts/trials; creator keeps up to 90% (vendor claim); mass DMs to fans; content vault/scheduler; earnings dashboard; instant payouts.
- The word "engagement" appears, but the objects are creator revenue streams and fan-paid access — not an organization-run engagement loop over a fan database. Confirms the label collision: creator-economy "fan engagement" products belong to Fan Membership Platform / Creator Subscription Platform leaves.

## Cross-product Comparison

| Dimension | FanThreeSixty | FanCompass | KORE | Greenfly |
|---|---|---|---|---|
| Operating organization | sports & entertainment properties (colleges, USL clubs, speedways, Broadway/arts venues, HS associations) | colleges, clubs, leagues (200+ claimed) | rights holders, leagues, teams, federations, brands (enterprise) | leagues, teams, federations, colleges, TV networks, brands |
| Central object | single fan profile (Fan Data Platform) | fan profile built "with every interaction" via activations | "complete view of every fan" (connected data) | media asset / gallery / channel (NOT a fan record) |
| Fan-facing surface | organization's branded mobile app (+ email, texting) | white-label mobile-web engine embedded in org's website/microsite/app; no app download | none marketed (execution in connected systems) | branded UGC submission pages/widgets; content distributed via social/broadcast |
| Engagement activities | campaigns, forms, app content (trivia, live video, giveaways), loyalty points, check-ins | unlimited simultaneous activations/campaigns, year-round | "relevant experiences" (execution delegated to org systems) | content campaigns, UGC creation campaigns |
| Data capture | first-party consolidation from ticketing/merch/F&B/CRM; enrichment; data-quality audits | progressive zero/first-party data per interaction; flows into CRM/SMS | connected data from CRM/ticketing/digital/ecommerce/marketing | contact info captured with UGC submissions (edge only) |
| Segmentation | 120+ prebuilt audiences + custom builder, auto-refreshing, triggers | leads/segments flowed to CRM and marketing tools | AI-powered audience intelligence; cross-team sharing | audience = distribution groups (athletes/staff/partners), not fan segments |
| Loyalty/rewards | points for attendance/stays/activations; Apple Wallet card | not marketed as core | not marketed | not applicable |
| Sponsorship | sellable digital sponsorable assets; real-time impressions; data valuation | sponsored campaigns; Nielsen Sports Digital Valuation | Partnership Intelligence module (separate) | sponsor content access; activation measurement |
| Commercial outcome | ticket sales influence, premium sales, renewals, donor propensity | ticket leads/sales, marketing leads, sponsored campaigns, data | engagement → loyalty/LTV; partnership revenue | fan reach, sponsor activation value, broadcast tune-in |
| Sales/CRM relationship | bundles a Sales CRM product; feeds Salesforce | feeds 100+ CRMs (Salesforce, HubSpot, Dynamics…); open API | connects to CRM as data source | exports contacts to CRM/mailing lists |
| Multi-property | per-organization | Enterprise Multi-Engine Org View (league-level) | league/federation scale | league-wide (40+ leagues) |
| White-label | org-branded app | "no visible FanCompass branding" | n/a (no fan surface) | org-branded submission pages |
| Service model | dedicated account manager; client success | self-serve engine; CORE+/PREMIUM add full-service | enterprise; Two Circles consultancy heritage | customer-success led |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a Fan Engagement Platform. Three properties held jointly:

1. **The fan as a persistent, identified individual record held by the operating organization** — a fan profile assembled from first-party data (ticketing, merchandise, communications, forms, digital behavior), resolved across sources and enriched over time. Remove it → anonymous audience analytics or social-media metrics, not a fan engagement platform.
2. **Organization-run engagement activities on surfaces the organization controls** — campaigns, activations, content programs, forms, loyalty actions that the organization designs and launches to invite fan participation (on its app, website, email/SMS, or embedded widgets). Remove them → a passive database or analytics tool.
3. **The engagement loop with captured participation** — each fan interaction is recorded back against the fan record (first-party data capture), enriching profiles and refreshing segments that drive the next round of targeted engagement, oriented toward commercial outcomes (ticket leads/sales, sponsorship value, revenue). Remove the loop → a one-off campaign tool or a form builder.

Supporting cross-product evidence: fan profile (FanThreeSixty "Single Fan Profiles"; FanCompass "richer, more actionable fan profiles with every interaction"; KORE "complete view of every fan"); organization-run activities (FanThreeSixty campaigns/app content/loyalty; FanCompass "unlimited engaging activations"; KORE "deliver more relevant experiences"); capture→segment→re-engage loop (FanThreeSixty auto-refreshing audiences + triggers; FanCompass "data and qualified leads flow seamlessly into your existing systems"; KORE "connected data… drives action"). Commercial orientation present in all sampled self-descriptions ("drive revenue", "Convert Fan Engagement into Revenue", "maximize revenue", "unlock new revenue streams").

Historical check (§24): fan-club-era practice — a membership/season-ticket-holder list (identified fan records), club-run outreach (newsletters, mail, fan events), and recorded responses feeding future outreach — satisfies all three properties without any mobile app, loyalty points, or gamification. The modern app/loyalty/gamification stack is the current dominant implementation, not the definition. Passes.

### L1 — Common Mature Structure

Present in most mature products; not required to recognize the Type:

- **Unified fan database with identity resolution** — consolidating ticketing, merchandise, F&B, CRM, and digital sources into single fan profiles; ongoing data-quality work (deduplication, audits, enrichment).
- **Audiences / segmentation** — prebuilt + custom segment builders; auto-refreshing (behavior-based) segments; trigger-based automations.
- **Direct engagement channels** — organization-branded mobile app, email, SMS/texting, push notifications.
- **Campaign/activation management** — a builder for engagement activities run year-round (in-season continuous, off-season at lower cadence), unlimited simultaneous campaigns.
- **Forms / lead capture** — fan information collection across channels, feeding sales lead lists.
- **Loyalty & rewards** — points for attendance/check-ins/activations, perks, membership cards (FanThreeSixty direct; common category-wide per market usage).
- **Gamified participation features** — trivia, predictions, contests, prize giveaways, exclusive content.
- **Sponsorship activation & measurement** — sellable sponsored placements in engagement channels, impression tracking, media-value valuation.
- **Predictive analytics / ML** — lead scoring, propensity (ticket/donor), at-risk renewal identification, RFM.
- **Integration spine** — CRMs, ticketing, marketing tools, data warehouses; open APIs; SSO.
- **White-labeling** — fan-facing surfaces carry the organization's brand, not the vendor's.
- **Cross-team operation** — marketing, ticketing sales, sponsorship, and leadership working from the same fan data.

### L2 — Variant / Optional Structure

Depends on segment, scale, deployment, business model:

- **Packaging pole**: full-suite platform (data + app + email + SMS + CRM in one vendor) vs activation engine (embedded white-label web engine; execution integrations carry the channels) vs intelligence/CDP-first layer (data + insight; execution stays in the org's systems) vs content-orchestration (adjacent Type — see Boundary Findings).
- **Fan-facing surface form**: native team app vs embedded mobile-web engine vs no fan-facing surface at all (intelligence pole).
- **Customer tier**: mid-market (colleges, USL clubs, venues) vs enterprise (major leagues, federations, global clubs).
- **Multi-property structure**: league/federation-level org views over per-property engines.
- **Service model**: self-serve SaaS vs full-service managed activation (vendor runs campaigns).
- **Domain tuning**: professional sports, college athletics, performing arts/venues, motorsports, high-school associations, federations, esports.
- **Geography**: US-centric market realization; international clubs/federations served by enterprise vendors.

### L3 — Vendor-specific Structure

(Research Notes only — not for the final document.)

- FanThreeSixty: "Fan Data Platform™" and "Mobile App™" trademarks; 120+ audiences / 120+ algorithms / 600 daily data-quality checks (vendor claims); Snowflake-backed "Data Hub"; Apple Wallet membership cards; 1.4M registered app users / 4-week deployment / 225k monthly app users (vendor claims); Tessitura integration emphasis.
- FanCompass: FC CORE / CORE+ / PREMIUM / ENTERPRISE tier ladder; Nielsen Sports Digital Valuation Calculator; "Multi-Engine Org View"; "plugs into your tech stack in minutes"; 30–60 min/week campaign maintenance claim; YinzCam/Sidearm/Deltatre team-app integrations.
- KORE: Two Circles rebrand ("The Operating System for the Business of Sport"); Partnership Intelligence as a co-equal module; sign-in-gated help center.
- Greenfly: +Engage UGC product; AI subject-ID/routing; 1GB submission file-size claim; perpetual usage-rights transfer framing; contributor mobile app.
- Passes (label-collision check): 90% creator revenue share; instant payouts — creator-economy, not this Type.

## Vendor-specific Findings

- Loyalty points tied to sponsorship activations (rewarding fans for engaging with sponsors) is directly documented only in FanThreeSixty — treat as product-specific/common-not-core.
- Nielsen-validated sponsorship rate cards directly documented only in FanCompass — product-specific.
- Bundled sales CRM inside the engagement platform directly documented only in FanThreeSixty — product-specific; the market norm is feeding external CRMs (FanCompass 100+ integrations; KORE CRM-as-data-source).
- League-level multi-engine org views directly documented only in FanCompass (Enterprise) — product-specific, though league-scale customers exist across vendors.
- AI purchase-likelihood multipliers ("25× more likely", "4× more spend") are vendor marketing claims — recorded, not asserted.

## Rejected Findings

- **"Fan engagement platform = sports CRM"** — rejected. CRM centers on relationship records and sales/service workflows; fan engagement platforms center on the engagement activity loop and explicitly hand leads/data to CRMs (FanCompass → 100+ CRMs; FanThreeSixty markets "fueling the Salesforce engine"). One sampled vendor bundles a sales CRM, but that is packaging, not the Type.
- **"Fan engagement platform = sports CDP"** — rejected as the full definition. Identity resolution + segments + activation (CDP structure) is the data layer of the Type (KORE Audience Intelligence, FanThreeSixty FDP), but the sampled activation-engine product (FanCompass) satisfies the Type with a lighter data layer plus the engagement loop, and the Type adds fan-facing engagement activities that a CDP does not define.
- **"A fan-facing mobile app is definitional"** — rejected. FanCompass explicitly requires no app download (embedded mobile-web engine); KORE markets no fan-facing surface. The app is the dominant L1 channel, not the invariant.
- **"Loyalty/rewards points are definitional"** — rejected. Directly documented in one sampled product (FanThreeSixty); FanCompass and KORE do not market loyalty as core. Common-not-core.
- **"Gamification (trivia/predictions) is definitional"** — rejected. Appears as app content features (FanThreeSixty) and activation variety (FanCompass "infinite types of digital activations"), but no sampled product defines itself by it.
- **"Content distribution to social platforms is the Type"** — rejected (Greenfly probe). A platform whose center is media assets/galleries/distribution serves fan engagement goals but is a media-orchestration application; the fan-record + engagement-loop core is absent.
- **"Fan engagement = creator-economy fan monetization"** — rejected (Passes check). Creator-side platforms monetize fan access (memberships, paid DMs); the organization-side engagement loop over a fan database is a different Type already covered by Fan Membership Platform / Creator Subscription Platform leaves.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove / add to cross) |
|---|---|---|
| Customer Relationship Management / CRM (incl. sports CRM) | adjacent, feed-forward | CRM's center is the relationship record + sales/service pipeline; fan engagement's center is the engagement activity loop. Fan engagement platforms generate engagement data and qualified leads and hand them to CRMs (FanCompass → 100+ CRMs; FanThreeSixty → Salesforce). Remove the engagement-activity loop and lead hand-off, keep relationship + sales workflows → CRM. One vendor bundles a sales CRM (product-level overlap, Type-level distinct). |
| Customer Data Platform / CDP | overlapping data layer | CDP is identity resolution + segments + activation as generic data infrastructure; fan engagement adds domain semantics (attendance, check-ins, season renewals, sponsorship activations) and the fan-facing activity loop. A sports CDP (StellarAlgo pole; KORE Audience Intelligence) is the data-first pole of this Type or a CDP applied to fans — the engagement loop is the discriminator. |
| Marketing Automation Platform | generic vs vertical | Same campaign loop shape, but generic marketing automation lacks fan-domain objects (attendance, check-ins, season tickets, sponsorship assets) and venue/sports semantics. Fan engagement platforms are effectively vertical marketing/engagement systems for rights holders. |
| Loyalty Program Management | component vs whole | Loyalty (points/rewards/tiers) is one L1 component inside fan engagement; fan engagement spans data, content, campaigns, channels, and sponsorship. Remove everything but the points ledger → Loyalty Program Management. |
| Social Media Management Platform | third-party vs owned | SMM engages audiences on third-party networks; fan engagement platforms build the organization's own identified fan relationships on owned/direct surfaces. Content-distribution-centric products (Greenfly) sit between: they orchestrate content FOR social distribution — media orchestration, not fan records. |
| Fan Membership Platform / Creator Subscription Platform (creator economy) | label collision, different operator | Operator is an individual creator; fans PAY for membership/content/DMs; monetization is direct fan payment; platform is two-sided marketplace-ish. Fan Engagement Platform: operator is an organization (rights holder); participation is free; monetization is indirect (engagement → data → ticket/sponsorship revenue). Remove payment and the creator, add the organization's fan database → this Type. |
| Event Management / Attendee Management | event-centric vs continuous | Event tools center a dated occasion's attendee lifecycle; fan engagement centers a continuous year-round relationship that spans many events, seasons, and off-seasons. |
| Sports Club Management (§28) | internal ops vs fan-facing | Club management runs the club's internal operations (members, teams, scheduling, facilities); fan engagement runs the fan-facing commercial relationship for professional/entertainment properties. |
| Media Asset Management / Content Distribution | adjacent pole (Greenfly) | Center objects are media assets, galleries, channels, contributor groups; fans reached via distribution. Remove the fan record + engagement loop → media orchestration. Serves fan engagement as a goal, not as a core model. |
| Mobile Marketing Platform | channel-generic vs fan-domain | Push/SMS campaign tooling is a channel inside fan engagement; fan engagement adds the fan profile, attendance/fandom semantics, and sponsorship monetization. |

## Uncertainties

- **StellarAlgo unreachable** — the named "fan data platform" pole is evidenced only structurally (via FanThreeSixty FDP and KORE Audience Intelligence). If StellarAlgo's model differs materially (e.g., no engagement activities at all, pure CDP), the L2 packaging-pole description would need adjustment; the L0 is unaffected because the pole is covered by two observed products.
- **No Tier 1 operational manuals sampled** — all evidence is Tier 2 product pages + one FAQ. Workflow specifics (how a campaign is configured step-by-step, how identity resolution is operated, how loyalty redemption works) are not directly documented; the final document deliberately stays at the structural level and avoids precise operational claims.
- **Loyalty prevalence** — loyalty/rewards is directly documented in one sampled product; its prevalence across the market is inferred from category usage (multiple vendors market loyalty modules) but not directly observed in this sample. Kept as common-not-core with qualified wording.
- **Geographic breadth** — sample is US-heavy; international fan engagement products (e.g., European club vendors) were not sampled. Claims kept implementation-neutral.
- **Creator-economy overlap depth** — the label collision is confirmed (Passes), but whether any creator-economy product genuinely matches this Type's core model (organization-style engagement loop) was not researched; assumed none, flagged for future passes.
- **KORE's exact execution capabilities** — with the help center sign-in-gated, whether KORE ships execution tooling (campaigns/channels) vs pure intelligence is not directly observable; treated as the intelligence pole with qualified wording.

## Final Synthesis

A Fan Engagement Platform is an organization-side application for sports teams, leagues, venues, and entertainment properties to build and maintain direct relationships with individual fans. Its defining core is three properties held jointly: (1) the fan as a persistent, identified individual record assembled from first-party data; (2) organization-run engagement activities — campaigns, activations, content, forms, loyalty actions — launched on surfaces the organization controls; and (3) the engagement loop in which every participation is captured back into the fan record, enriching profiles and refreshing segments that drive the next round of targeted engagement, oriented toward commercial outcomes (ticket leads/sales, sponsorship value, revenue).

Around that core, mature products add a common structure: unified fan databases with identity resolution and data-quality operations; auto-refreshing audiences; direct channels (team app, email, SMS/push); year-round campaign management; forms/lead capture; loyalty and gamified participation; sponsorship activation with impression measurement; predictive scoring; and a deep integration spine into CRMs, ticketing, and marketing systems — with white-labeled fan surfaces and cross-team operation.

The Type spans four packaging poles: the full-suite platform (data + channels + CRM), the activation engine (embedded white-label web engine feeding existing systems), the intelligence/CDP-first layer (connected fan data + insight, execution in connected systems), and — at the boundary — content-orchestration platforms that serve fan engagement through media distribution without holding fan records. The creator-economy "fan engagement" label names a different, already-covered Type (fan-paid membership/subscription monetization); the collision is recorded.

Boundaries held: vs CRM (engagement loop + lead hand-off vs relationship/sales record), vs CDP (fan-domain engagement loop vs generic data infrastructure), vs marketing automation (vertical fan semantics vs generic campaigns), vs loyalty management (component vs whole), vs social media management (owned identified relationships vs third-party reach), vs event management (continuous relationship vs event lifecycle), vs club management (fan-facing commercial vs internal operations), vs media orchestration (fan record + loop vs media assets + distribution).
