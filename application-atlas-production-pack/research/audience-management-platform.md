# Research Notes — Audience Management Platform

## Research Goal

Determine whether "Audience Management Platform" (§06 Marketing, Advertising & Growth) names an independent Application Type, an alias of an existing Type, or a capability phrase whose referent belongs to neighboring Types. This leaf carries two pre-hung joint-review flags:

1. **data-management-platform-dmp (§06, processed 2026-09-08)** — TAXONOMY TENSION: "the DMP IS the market's established audience-management platform for advertising — the sampled DMPs' entire capability set is audience management (build/manage/activate targetable audiences), so a separately defined 'Audience Management Platform' leaf risks being an alias of DMP or a capability slice of it". Candidate dispositions offered: (a) alias of DMP, (b) audience-centric capability slice (audience build/manage without the DMP's collection/marketplace/activation machinery), (c) martech-adjacent audience tools (email/social audiences) distinct from ad-tech DMP.
2. **media-audience-management (§27, processed 2026-09-08)** — the media-industry usage of the exact phrase "audience management" is realized by Omeda under the §27 leaf; the §06 pass should decide alias-of-DMP / capability-slice / martech-audience-tools and explicitly scope out (or absorb) the media-industry reading.

## Initial Boundary

Initial hypothesis (before research): "Audience management" is a function, not a product category. In ad-tech the phrase historically names what DMPs do; in martech it names a CDP capability; in media it names Omeda-class platforms (§27); in email it names contact lists; in social advertising it names native ad-platform audience builders. Nearest neighbors: DMP (same function, advertising form), CDP (profile-of-record sibling), media-audience-management (§27), email-marketing-platform, marketing-automation-platform, DSP (downstream consumer), social-listening/audience-intelligence (different function).

Unknowns at start: whether any standalone product category self-identifies as "Audience Management Platform" with a structure distinct from DMP/CDP; whether the capability-slice reading (audience management without activation) has market support.

## Research Questions

1. Which real products self-identify with the exact phrase "Audience Management Platform" (or "Audience Manager/Studio")? What are they, structurally?
2. What defining structure, if any, is shared across the phrase's users?
3. Is that structure the same as, or different from, the DMP's defining core (managed segment-of-record + multi-source aggregation + activation into advertising)?
4. Does the capability-slice reading (audience build/manage WITHOUT activation machinery) exist in the market?
5. Where does each reading of the phrase land: advertising / martech / media / mobile / B2B / email / social-ad-native?
6. Disposition: alias, capability slice, or distinct Type?

## Representative Products

Selected to span the phrase's observed readings (market usage of the exact phrase + different product philosophies + different customer contexts):

- **Adobe Audience Manager** — the flagship product literally named "Audience Manager"; enterprise suite DMP.
- **Salesforce Audience Studio (Krux)** — the second "audience"-named flagship; historical sample (sunset), evidences the classic third-party-data form and the category's decline.
- **Singular** — "Audience Management & Activation Platform" as a capability of a mobile measurement/attribution (MMP) platform; the mobile/attribution reading.
- **Omeda** — "Audience Management Platform for Media"; the media-industry reading (already documented under §27 media-audience-management).
- **Leadspace** — the B2B reading: launched as "the first B2B Audience Management Platform" (2017); since repositioned.

Boundary/industry samples: cdp.com glossary (industry glossary; CDP-vendor-published), Treasure Data blog (CDP vendor), Gartner "Audience Intelligence Platforms" category page (a different category), TechTarget / LiveRamp docs (sunset evidence).

## Sources

Research date: **2026-09-10**

- Adobe — Audience Manager developer page ("Audience Manager is a data management platform…") — https://developer.adobe.com/audience-manager — fetched directly (Layer A)
- Adobe — Audience Manager User Guide overview ("Three functions of a Data Management Platform (DMP)") — https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/overview/aam-overview — via search excerpt (Layer A content, search-mediated)
- Adobe — Audience Manager product page (steering to Real-Time CDP) — https://business.adobe.com/products/audience-manager.html — via search excerpt (Layer A content, search-mediated)
- Adobe — "Audience Management | Adobe Real-Time CDP" page — https://business.adobe.com/uk/products/real-time-customer-data-platform/audience-management.html — via search excerpt (Layer A content, search-mediated)
- Singular — Audience Management page + FAQ — https://www.singular.net/audience-management — fetched directly (Layer A)
- Omeda — Platform page ("The Foundational Core — The Audience Management Platform") + FAQ — https://www.omeda.com/platform , https://www.omeda.com/customer-data-platform/audience — fetched directly (Layer A; first fetch of /platform timed out, retry succeeded)
- Leadspace — 2017 launch press release ("first B2B Audience Management Platform") — https://www.digitalcommerce360.com/2017/04/05/leadspace-launches-first-b2b-audience-management-platform — via search excerpt (Layer A content, search-mediated)
- Leadspace — current site ("GTM Data Intelligence Cloud") — https://www.leadspace.com/ — fetched directly (Layer A)
- TechTarget — "Salesforce to pull plug on Audience Studio DMP" (2021-07-15) — https://www.techtarget.com/enterprise-software/news/252504052/ — via search excerpt (Layer A content, search-mediated)
- LiveRamp — "Salesforce Audience Studio DMP (Krux) End of Life is February 1, 2024" — https://docs.liveramp.com/connect/en/announcement--salesforce-audience-studio-dmp--krux--end-of-life-is-february-1,-2024--1-29-24-.html — via search excerpt (Layer A content, search-mediated)
- DESelect — "Preparing for Salesforce Audience Studio Sunset" — https://deselect.com/blog/salesforce-audience-studios-sunset — via search excerpt (Layer A content, search-mediated)
- CDP.com glossary — "Audience Management Platform" — https://cdp.com/glossary/audience-management-platform — fetched directly (Layer A; **CDP-vendor-published** [Treasure Data], bias noted)
- Treasure Data blog — "CDP vs DMP: The DMP Era Is Over" — https://www.treasuredata.com/blog/cdp-vs-dmp — via search excerpt (**CDP-vendor-published**, bias noted)
- Gartner Peer Insights — "Audience Intelligence Platforms" category — https://www.gartner.com/reviews/market/audience-intelligence-platforms — via search excerpt (Layer A content, search-mediated)
- Lytics — https://www.lytics.com/ — fetched directly; **site retired** (redirect notice: "This site will be retired on September 30th, 2026. Visit Contentstack") — no product documentation reachable (Source-access Limitation)

## Product Observations

### Adobe Audience Manager (Evidence Layer A)

- Self-description (developer.adobe.com, verbatim): "Audience Manager is a **data management platform** that helps you build unique audience profiles so you can identify your most valuable segments and use them across any digital channel." Three stated functions: understand your audiences (combine all data sources), create new segments ("continually discover and organize new, valuable segments for smarter targeting and personalization"), advertise effectively ("targeting specific segments on any platform").
- User-guide overview (experienceleague): "bring your audience data assets together… collect commercially relevant information about site visitors, create marketable segments, and serve targeted advertising and content"; "you are not tied to a data seller, exchange, or demand-side platform… completely agnostic when it comes to our partners' data assets". Documents the "Three functions of a Data Management Platform (DMP)": **Data In** (collects first-party data from channels and devices — web analytics, CRM, device data, e-commerce), **Audience Creation** (unifies data into audience profiles; look-alike models; segments; supplement with second- and third-party data), **Data Out** (activates segments by pushing to DSPs, campaign management systems, other marketing platforms).
- Product page (business.adobe.com): "Adobe has always been a leader in data management platforms, and Adobe Audience Manager has been crucial… Now Adobe is leading the way as we enter a world with fewer third-party cookies… Introducing Adobe Real-Time CDP, the advanced customer data platform (CDP)…" — the vendor is steering the DMP toward its CDP.
- "Audience Management" now also exists as a marketed **capability of Adobe Real-Time CDP** ("Empower your teams to quickly create, manage and optimise intelligent audiences using natural language prompts…").
- Reading: the product named "Audience Manager" IS a DMP; the phrase "audience management" has migrated onto the CDP as a capability name.

### Salesforce Audience Studio / Krux (Evidence Layer A, historical)

- TechTarget (2021-07-15): "Salesforce has apparently pulled the plug on its Audience Studio data management platform… 'Salesforce can confirm that Audience Studio is no longer available for purchase'… Salesforce built its DMP from the $700 million cash-and-stock acquisition of Krux in 2016… In a statement, Salesforce put new emphasis on its customer data platform (CDP), which traffics in first-party data."
- LiveRamp partner documentation: "Salesforce Audience Studio DMP (Krux) End of Life is February 1, 2024… All existing first-party, Data Marketplace custom, and Data Marketplace syndicated distributions to Salesforce Audience Studio will be turned off."
- DESelect (description of the product while live): "the data management platform (also called DMP) that allows organizations to aggregate and segment data from many sources… Marketers can upload first-, second- and third-party data from sources such as website analytics tools, social media, and CRMs to create detailed audience segments based on attributes such as demographics, behavior, and purchase history. Once users assemble these segments, they can put the data to use across different channels such as email, social media, and display advertising…"
- Reading: the second flagship "audience"-named product was a DMP; sunset under third-party-cookie/privacy pressure; vendor redirected to CDP.

### Singular (Evidence Layer A)

- Page title: "Audience Management & Activation Platform" — but the page is a **capability page of Singular's MMP/attribution platform** (nav places it under "Activation" alongside Marketing ETL / Reverse ETL).
- Verbatim: "Turn your attribution data into target audiences automatically. Build segments from real user behavior, sync them to every major ad network, and stop wasting spend on users you've already won, lost, or excluded."
- "The audience layer your attribution data was built for. Most audience tools live downstream of a CDP or a data warehouse, disconnected from attribution. With Singular, your audiences are built from the same user-level data that powers your reporting, refreshed continuously, and synced to every ad network you run."
- Audience builder: "Flexible rule-based segmentation across any combination of attribution signals, in-app events, ad revenue cohorts, geo, install source, or LTV tier. Create lookalike seeds, suppression lists, retargeting pools, or VIP cohorts in one interface. **Save and version segments** as your strategy evolves."
- Distribution: "Native integrations with the major DSPs and ad networks. Singular pushes the segment, the network ingests it, and the audience is live, no CSV exports, no manual uploads… Hourly refresh where partners support it, daily where they don't."
- Refresh: "Auto-sync keeps every segment current as users convert, churn, or change cohort."
- Suppression: "Exclude active users, recent installers, lapsed paid users, fraud-flagged installs, or any audience trait you define."
- Compliance: "No PII leaves the platform. Hashed IDs only."
- FAQ (verbatim): "Audience management is the practice of **building, refreshing, and distributing user segments to ad networks and channels** for targeting, suppression, retargeting, or lookalike modeling." / "A CDP… is a system of record that unifies first-party customer data from every product touchpoint… A DMP… is the older, third-party-data-focused tool largely deprecated by privacy changes. **Audience management for marketing is narrower and more action-focused**: build segments from attribution and behavioral signals, distribute them to ad networks for paid media activation, refresh them continuously."
- Reading: audience management as a capability of a measurement platform — the DMP loop (segment-of-record → activation to ad systems) executed over the platform's OWN attribution data. The vendor itself distinguishes it from both CDP and DMP and calls it "narrower and more action-focused".

### Omeda (Evidence Layer A)

- Root page title: "Audience Management Platform for Media | Omeda". "Your audience members are people, not email addresses. Omeda unifies every signal into one profile — so subscriptions, marketing, and ad revenue all work from the same source of truth."
- Platform page: "The Foundational Core — The Audience Management Platform. Omeda's core foundation allows media teams to create a unified, actionable audience view." Four pillars: **Know Your Audience** (identity resolution across channels; behavioral website audience tracking; connect unknown visitors to known profiles), **Grow Your Audience** (forms and first-party data capture; personalized content; conversion-focused on-site engagement), **Organize & Activate** (audience builder and segmentation; data ingestion and integrations; audience refinement and reuse), **Understand & Govern** (first-party data insights; AI task assistant; permissions, privacy, and compliance controls).
- Extensions: Newsletters & Marketing Automation (email service provider, journeys, lead scoring); Subscriptions & Product Management (promotions, payments, entitlements, renewals). "Everyone starts with the core Audience Management Platform to unify audience data."
- FAQ (verbatim): "Omeda is an audience management platform built for media companies. It connects identity, engagement data, subscriptions, newsletters, and events into a **single audience record**. Media, publishing, and events teams use this data to segment audiences, activate campaigns, and understand which behaviors drive revenue." / "How is Omeda different from a traditional customer data platform? Most CDPs serve ecommerce brands. Omeda was built for media companies."
- Reading: the media-industry usage of the exact phrase. Structurally CDP-shaped (profile-of-record: "single audience record" per person; known + anonymous resolution) but domain-bound to media (content engagement, subscriptions, events; monetization via subscriptions + ad revenue). This is the §27 media-audience-management leaf's territory — that pass already sampled Omeda and drew the seam (media audience records anchored in content engagement serving media monetization vs generic cross-industry commerce profiles).

### Leadspace (Evidence Layer A)

- 2017 launch press release (digitalcommerce360, verbatim): "Leadspace today launched the **first Audience Management Platform for B2B marketing**… Featuring audience discovery, audience data management and audience modeling, the new Leadspace platform combines first-party data with third-party data from more than 40 sources, uses advanced predictive modeling and AI to enrich data in real time… consistently used across sales, marketing and advertising channels."
- Current site (2026): "The Leadspace **GTM Data Intelligence Cloud**™… Unify buyers, accounts, and signals into one continuously updated intelligence layer… Step 1: Sense (gathers signals across proprietary datasets, intent, technographics, and your first-party systems and updates profiles continuously). Step 2: Decide (AI models identify ICP fit, intent spikes, buying groups, territory alignment, and routing priorities…). Step 3: Activate (Intelligence flows into Salesforce, Marketo, HubSpot, Eloqua, Snowflake, BigQuery, and more…)."
- Reading: the B2B usage of the phrase (2017) did not stick as a category name; the product converged into B2B data-intelligence / CDP-adjacent positioning (unified profiles + signals + activation into CRM/marketing-automation/warehouse).

### Industry glossary — CDP.com (Evidence Layer A; CDP-vendor-published, bias noted)

- Definition (verbatim): "An audience management platform (AMP) is a technology solution that enables organizations to **create, organize, enrich, and activate customer audiences** across marketing and advertising channels."
- History (verbatim): "Throughout the 2010s, Data Management Platforms (DMPs) **dominated audience management**… As browsers phased out third-party cookies… the DMP model collapsed. Oracle shut down its BlueKai DMP in 2024. Lotame pivoted to first-party data… the AMP category is **converging with Customer Data Platforms**."
- AMP vs DMP vs CDP comparison table (data foundation / identity type / retention / identity resolution / channel scope / AI / privacy / use-case breadth).
- FAQ (verbatim): "Do I need an audience management platform if I have a CDP? **In most cases, no.** Modern CDPs include comprehensive audience management capabilities — segmentation, activation, suppression, and measurement — as core features."
- Bias caveat: CDP.com is published by Treasure Data (a CDP vendor); its "AMP converges into CDP" framing serves CDP positioning. Used as directional evidence of industry usage, not as dispositive structural evidence.

### Treasure Data blog (Evidence Layer A; CDP-vendor-published, bias noted)

- Verbatim: "Oracle shut down its entire advertising division — BlueKai, Datalogix, Moat, and Grapeshot — on September 30, 2024. Salesforce declared End of Life for Audience Studio (formerly Krux) on February 1, 2024… **What remains is the function, not the product category.** Audience enrichment, lookalike modeling, and programmatic targeting still happen — but they happen inside CDPs and ad platforms… The standalone DMP as a category is effectively over."

### Gartner "Audience Intelligence Platforms" (Evidence Layer A, boundary sample)

- Category definition (verbatim): "technology solutions that allow marketers, advertisers, content creators and other professionals to **gather, analyze, and interpret data about their target audiences**… collect data from various sources, including social media, website analytics, CRM systems and market research to create a comprehensive understanding of audience demographics, behaviors, interests and preferences." Sample vendors: Sprinklr Insights, Pulsar, Talkwalker.
- Reading: a DIFFERENT category — audience understanding/analysis (social/consumer intelligence), not audience management (building and activating targetable audiences). Boundary note only.

### Lytics (Source-access Limitation)

- Site fetched 2026-09-10: retirement notice only ("Lytics has moved to Contentstack. This site will be retired on September 30th, 2026"). Lytics was known to market an "audience-first" CDP positioning, but no product documentation was reachable on the research date. The martech reading therefore rests on cdp.com + Adobe RT-CDP + Singular FAQ, not on Lytics first-hand. No Lytics-specific claims are made in the final document.

## Cross-product Comparison

| Dimension | Adobe Audience Manager | Salesforce Audience Studio (hist.) | Singular | Omeda | Leadspace |
|---|---|---|---|---|---|
| Self-description | "data management platform" | DMP (per vendor statements + press + partner docs) | "Audience Management & Activation Platform" (MMP capability page) | "Audience Management Platform for Media" | 2017: "first B2B Audience Management Platform"; 2026: "GTM Data Intelligence Cloud" |
| Central object | audience profiles → segments | audience segments | segments (saved + versioned) | "single audience record" per person (profile-of-record) | unified buyer/account profiles |
| Data foundation | first-party collection + second-/third-party supplement | first-/second-/third-party upload | platform's own attribution data only | first-party media engagement (web, newsletters, subscriptions, events) | 1st party + 3rd party (40+ sources, 2017); proprietary datasets + intent + technographics (2026) |
| Identity substrate | anonymous + known, cross-device | anonymous cookies | hashed device advertising IDs only ("No PII leaves the platform") | known + anonymous, resolved to one record | people/accounts with identity hierarchies |
| Activation surface | DSPs, campaign management systems, marketing platforms | email, social, display advertising | ad networks + DSPs (native sync, continuous refresh) | email, social, search, site personalization (via extensions) | CRM, marketing automation, warehouses |
| Suppression | within segment logic | (not documented in sampled sources) | first-class (suppression lists) | within segmentation | within targeting |
| Measurement | audience insights | campaign analytics | ROAS feedback from same attribution data | audience health/growth/engagement dashboards | pipeline/conversion outcomes |
| Status (2026-09-10) | live; vendor steering to Real-Time CDP | sunset (sales stopped 2021; EOL 2024-02-01) | live capability | live | live, repositioned |

**Cross-product commonality (Layer B):** every product/reading that uses the phrase shares one structure —

1. a **managed audience as a persistent named object** (saved, versioned, reusable; membership computed from rules/models over audience data — never a one-off query or a hand-enumerated list as the defining form);
2. an **audience data foundation** feeding the definition (collected, onboarded, acquired, or enriched);
3. **activation outward** to systems/channels that act on the audience (advertising targeting, messaging, personalization), with **suppression** as the complement;
4. **measurement feeding back** into refinement.

**Layer C (canonical inference):** this shared structure is exactly the DMP's defining core as documented by the DMP pass (managed audience segment as unit of record + multi-source audience data aggregation + audience activation into advertising/media systems). The readings differ only in era/realization: data foundation (third-party-cookie-open vs first-party-led vs own-attribution-only), identity substrate (anonymous vs hashed vs resolved known profiles), activation surface (advertising systems vs owned channels vs both), and central object (segment-of-record vs profile-of-record with audience capability).

## Abstraction Hierarchy

### L0 — Defining Invariant

The audience-management structure, three jointly-held properties:

1. **The managed audience as the unit of record** — a named, persistent, targetable group of addressable people, defined by qualification rules and/or models over audience data; membership computed and maintained, the audience held as a reusable object (organized in a library/taxonomy). Remove → a data store or an analytics/insights tool.
2. **An audience data foundation feeding the definition** — behavioral collection, file onboarding, acquired third-party data, enrichment (scores, overlays, lookalike expansion). Remove → hand-enumerated lists, not managed audiences.
3. **Activation outward** — delivery of the audience to systems/channels that act on it (ad platforms, messaging tools, personalization), with suppression as the constitutive complement. Remove → audience insights with no operational loop.

All three jointly = the DMP's defining core. **This identity is the alias finding.**

### L1 — Common Mature Structure

- dedicated audience-builder interface with rule composition and versioning
- model-based expansion (lookalike seeds, propensity)
- suppression lists as first-class objects
- destination catalogs with native sync and automatic/continuous refresh
- audience insights (size, composition, overlap, performance)
- library/taxonomy organization of audiences
- consent/privacy controls and governance (permissions, compliance)

### L2 — Variant / Optional Structure

- data foundation posture: third-party-cookie-open (classic) vs first-party-led (modern) vs own-attribution-only (measurement-platform form)
- identity substrate: anonymous cookies/device IDs vs hashed identifiers vs resolved known profiles
- activation surface: advertising systems only vs owned channels only vs both
- central object: segment-of-record (DMP form) vs profile-of-record with audience capability (CDP/media form)
- domain binding: generic vs media vs B2B
- packaging: standalone product vs suite module vs capability of another Type (MMP, email platform, ad platform)

### L3 — Vendor-specific (Research Notes only)

- Singular: hourly/daily refresh cadences per partner support; named destination network list; "no PII leaves the platform" hashed-IDs-only posture.
- Omeda: extension packaging (Newsletters & Marketing Automation; Subscriptions & Product Management); Omeda MCP / AI task assistant; "State of Audience in Media" report franchise.
- Leadspace: "GTM Data Intelligence Cloud" branding; buying-group/ICP models; sub-90-second lead-to-account matching claim (marketing figure, excluded from final doc).
- Adobe: Profile Merge Rules, Audience Marketplace naming (documented in the DMP pass); RT-CDP natural-language audience creation.
- cdp.com's "90 days (typical)" DMP retention figure — vendor-published, unverified against primary DMP documentation; NOT carried into the final document.

## Vendor-specific Findings

See L3 above. Additionally: Adobe's steering of Audience Manager toward Real-Time CDP and Salesforce's redirection from Audience Studio to its CDP are vendor lifecycle facts, not Type structure; they evidence the category's migration, not its definition.

## Rejected Findings

1. **"AMP is an established independent product category distinct from DMP and CDP"** — REJECTED. No analyst taxonomy examined carries it as such (Gartner's nearest category, "Audience Intelligence Platforms", is a different function). The industry's own glossary describes AMP as converging with CDPs. Both flagship products carrying "audience" names self-identify as DMPs.
2. **Capability-slice disposition (b): "audience build/manage without the DMP's collection/marketplace/activation machinery"** — REJECTED. Every observed market usage includes activation as constitutive: Singular FAQ ("building, refreshing, and distributing user segments to ad networks"), cdp.com definition ("create, organize, enrich, and activate"), Omeda ("segment audiences, activate campaigns"), Adobe ("use them across any digital channel"). A slice without activation is just segmentation — a capability of many systems, not a standalone category.
3. **Martech-tools disposition (c) as a separate Type** — REJECTED as an independent Type; the readings dissolve into existing/pending Types: CDP audience capability, email contact audiences (email-marketing-platform's "opt-in contact audience of record"), ad-platform native audience builders (single-platform signals — the DMP doc's own boundary line).
4. **"Audience Intelligence Platforms = Audience Management Platforms"** — REJECTED. Gartner's category is about understanding audiences (social/consumer intelligence: Sprinklr, Pulsar, Talkwalker), not building and activating targetable audiences.

## Boundary Findings

| Neighboring Type | Relationship | Distinction / "remove what to become the other" |
|---|---|---|
| Data Management Platform / DMP | **same defining structure — alias** | The DMP is the market's established name for the advertising form of audience management. The "Audience Management Platform" name adds no structure the DMP lacks. Remove the advertising-specific bindings (third-party openness, ad-system activation) and generalize → the abstract audience-management structure; realize it in advertising → DMP. |
| Customer Data Platform / CDP | closest sibling, different central object | CDP's central object is the persistent individual profile of record; audience management is a capability layer over profiles. The phrase's first-party/known-identity reading lands here. CDP leaf unprocessed — ratification pending. |
| Media Audience Management (§27) | domain sibling; the media reading of the exact phrase | Realized by Omeda: unified audience record anchored in content engagement, serving media monetization (subscriptions + ad revenue). Keep-both confirmed from this side; the media reading is explicitly scoped OUT of §06. |
| Email Marketing Platform | channel sibling, different Type | "Audience" as the opt-in contact list of record; campaign + bulk-send machinery is the center. The email pass already defined its own audience leg. |
| Demand-side Platform / DSP | downstream consumer | Buys media using audiences; never manages them. One of the audience platform's destinations. |
| Marketing Automation Platform | adjacent orchestrator | Person database + reusable automated programs; orchestration is the center, not the audience object. |
| Marketing Analytics / Attribution (MMP) | adjacent measurement | Measurement is the center; audience management is a capability built on its own data (Singular). |
| Ad-platform native audience builders | embedded variant | Single-platform signals only; the DMP doc's boundary line applies ("restrict data to a single platform's own signals and it becomes that platform's native audience builder"). |
| Audience Intelligence Platforms | different Type | Understanding/analyzing audiences (social/consumer intelligence) vs building and activating targetable audiences. |

## Uncertainties

1. **CDP-side ratification pending.** The CDP leaf (customer-data-platform-cdp) is unprocessed (timed-out run 2026-09-08). The segment-of-record vs profile-of-record seam was drawn by the DMP pass; this pass adds that the phrase's first-party/known-identity reading lands on the CDP as an audience capability. The CDP pass should ratify.
2. **Lytics unreachable** (site retired to Contentstack). The martech reading is evidenced indirectly (cdp.com glossary, Adobe RT-CDP page, Singular FAQ). No Lytics-specific claims made.
3. **Vendor bias in industry sources.** cdp.com and the Treasure Data blog are CDP-vendor-published; their "AMP converges into CDP" framing serves CDP positioning. The alias finding does NOT rest on them — it rests on vendor self-identification of the "audience"-named products as DMPs (Adobe verbatim; Salesforce via press + partner EOL docs) plus the absence of any independent AMP category in analyst taxonomies.
4. **Absence-of-evidence note.** No standalone "Audience Management Platform" product category was found in the analyst taxonomies and market surfaces examined. This is absence of evidence for an independent category, not proof; recorded as such.
5. **Historical precision.** Sunset dates (Audience Studio sales stopped July 2021; EOL February 1, 2024; Oracle ad division shutdown September 30, 2024) come from TechTarget, LiveRamp docs, and the Treasure Data blog; the first two are corroborated across independent sources, the Oracle date rests on the vendor blog + cdp.com glossary and is used only in Research Notes.

## Final Synthesis

**Disposition: (a) ALIAS of Data Management Platform / DMP.**

"Audience Management Platform" names the audience-management **function**, whose defining structure is exactly the DMP's defining core (managed audience/segment as unit of record + audience data foundation + activation outward). The market realizes the function in:

- the **DMP** (advertising form — the established category name; both "audience"-named flagship products self-identify as DMPs);
- the **CDP** (first-party/known-identity form — audience management as a capability over persistent profiles);
- **§27 media-audience-management** (media form — Omeda; the media-industry usage of the exact phrase);
- **channel-platform capabilities** (MMP/attribution audience builders, email contact audiences, ad-platform native audience builders).

No standalone product category with this name and an independent structure was found. The capability-slice reading has no market support (activation is constitutive everywhere). Recommendation: retain the DMP leaf as the Type; record this leaf as its alias; scope the media reading to §27 and the first-party reading to the CDP leaf. No directory change made from this side.

The final document is written as a full Application Document covering the phrase's referent from its own lens (the audience-management structure and its realizations), with the alias relationship stated in natural language, following the precedent of the ai-software-engineering-agent alias document.
