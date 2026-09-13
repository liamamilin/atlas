# Research Notes — Content Distribution Platform

Research date: 2026-09-07
Leaf: Content Distribution Platform (DIRECTORY §27 Media, Entertainment, Creator & Culture, between Media Asset Management / MAM and Media Rights Management)
Slug: content-distribution-platform

## Research Goal

Determine what the market actually means by "Content Distribution Platform" in the media/entertainment context, which real products constitute the Type, what the canonical object model and workflows are, and where the boundaries run against neighboring Types (Video Streaming Platform, CDN Management, MAM, Broadcast Management System, Music/Podcast distribution siblings, ad platforms).

## Initial Boundary (hypothesis before research)

The leaf sits in the B2B media-operations cluster of §27. Hypothesis: a provider-side platform used by content owners (broadcasters, studios, sports rights holders, channel operators) to package and deliver content to many external consumer-facing platforms (FAST services, vMVPDs, SVOD, owned apps, social), with per-destination delivery tracking. Nearest confusions: CDN Management (network layer), MAM (asset layer), Video Streaming Platform (the destination itself), Music Distribution Platform / Podcast Platform (audio siblings with their own leaves), and the marketing-world usage of "content distribution" (native-ad syndication — different industry, §06).

## Research Questions

1. What objects exist inside such a system? (assets, channels, schedules, destinations, delivery records, metadata, ad configs)
2. Who operates it, and what roles appear on both sides of the pipe?
3. What is the core workflow from content to "live on a destination"?
4. What lifecycles/states exist (asset states, channel states, delivery states)?
5. What rules constrain delivery (destination specs, approval gates, rights, refresh expectations)?
6. What interfaces do operators actually use?
7. How do the sampled products differ in philosophy (suite vs pure distribution vs services vs marketplace)?
8. Where exactly is the boundary vs CDN Management, MAM, and the destination platforms?

## Representative Products

| Product | Why selected | Pole represented |
|---|---|---|
| Amagi | Market-leading "media industry cloud"; explicit Distribution product family + FAST marketplace | full suite (preparation + distribution + marketplace + monetization) |
| Wurl (AppLovin) | "Global FAST Pass" — channel origination + distribution + monetization; largest claimed CTV distributor | origination+distribution with ad-monetization depth |
| Frequency | Frequency Studio + CONNECT; only sampled product with a public operational documentation portal | channel origination + distribution network, doc-rich |
| Vubiquity (Amdocs) | Services-led media supply chain; "preferred fulfillment vendor" for major OTT platforms | managed-service / fulfillment pole (no self-serve console observed) |

Dropped: Peach (byAccedo) — peach.tv now shows "Peach is now closed"; product defunct, excluded from sample.

## Sources

Tier 1 (official operational documentation):
- Frequency Documentation portal — https://docs.frequency.com/ (User Guides: CONNECT, INGEST, MANAGE, BUILD, GRAPHICS, LIVE, SCHEDULE, ANALYZE, ACCOUNT; Content Delivery Guidelines; Metadata Specifications; Distribution Specifications; Developer APIs) — fetched 2026-09-07
- Frequency CONNECT User Guide — https://docs.frequency.com/en/user-guides/connect-user-guide.html — fetched 2026-09-07

Tier 2 (official product pages):
- Amagi — https://www.amagi.com/ , /products/amagi-connect , /products/linear-distribution — fetched 2026-09-07
- Wurl — https://www.wurl.com/ , /products/global-fast-pass/ — fetched 2026-09-07
- Vubiquity — https://www.vubiquity.com/ — fetched 2026-09-07
- Frequency — https://frequency.com/ — fetched 2026-09-07

Not fetched / not reachable:
- Wurl support center (https://support.wurl.com/hc/en-us) — not attempted after product-page FAQ proved rich; console-level operational detail for Wurl not directly observed
- Amagi support portal (https://support.amagi.tv/) — not fetched; Amagi evidence is product-page level
- Vubiquity service detail pages — root page only; services-led vendor, no public console documentation observed

## Product Observations

### Amagi (evidence: A on product pages; B where cross-confirmed)

- Positions itself as "The Media Industry Cloud" for "content providers and distributors"; serves Broadcasters, Content Owners, Distributors (FAST platforms, vMVPDs, device OEMs), Advertisers, Sports.
- Amagi NOW platform organized as Production / Preparation / **Distribution** / Monetization. Distribution family: Linear Distribution, VOD Distribution, FAST Distribution (Amagi CONNECT), Social Publishing, FASTKit.
- **Linear Distribution**: "trusted fiber, satellite, and IP network — reaching major broadcast and cable headends and Points of Presence (PoPs)"; capabilities: expansive coverage (thousands of PoPs), quality of service (multiple acquisition and distribution routes, SLAs), 24/7 global monitoring. Claims 170+ platforms reachable (linear-distribution page) and "300+ streaming platforms and pay-TV operators reachable from a single feed" (home page).
- **Amagi CONNECT (FAST Distribution / FAST Marketplace)**: "an end-to-end FAST marketplace" — content owners discover platforms and distribute; platforms discover and acquire content. Capabilities: expedite deal closure, revenue reporting and reconciliation (billing, invoicing), "real-time tracking and transparency: monitor content distribution/acquisition and delivery/fulfillment status in real time for seamless order fulfillment, rights management, and localization services". Connection-request mechanics between partners. FAQ: 400+ channels and 50+ platforms with published profiles; ad inventory split via two industry-standard models — inventory share vs revenue share.
- Claims (marketing layer): 9,000+ channel deliveries; 26B+ ad impressions annually via THUNDERSTORM SSAI.

### Wurl (evidence: A on product page incl. FAQ)

- "Global FAST Pass" = "the industry's trusted platform for launching, distributing, and monetizing FAST channels"; menu labels the category "Channel Distribution".
- Three pillars on product page: Originate or restream channels (recorded or live content + graphics via scheduler); Distribute across 65+ platforms ("Wurl handles transcoding, storage, ad markers, multi-language captions, and more"); Enable ads and monetize (ad insertion, exclusive demand).
- FAQ (high-value operational evidence):
  - "Wurl does not negotiate distribution agreements. We support and can connect the parties... Once deals are in place, Wurl can manage the rest."
  - Supports Wurl-originated AND third-party channels: "asset onboarding, transcoding, scheduling, metadata delivery (EPG), closed captioning, DRM, ad routing and insertion, impression validation, inventory split management, and advanced performance reporting."
  - Two channel-delivery modes: **new playout** (content ingest → scheduling → configuration/delivery) vs **restream** (skip ingest/scheduling; stream + EPG validation only; timeline roughly one-third to one-half of a full launch).
  - Delivers to vMVPDs (e.g., YouTube TV) as part of the network.
  - Pricing: flat monthly fee per channel covering distribution to 50+ streamers; usage fees — CDN GB for DTC streamers, flat connector fee per stream for headend streamers.
  - Content guidance: ~200 hours minimum to sustain a 24/7 schedule; platforms expect ongoing refreshes (monthly/quarterly) — vendor guidance, not a platform-enforced rule.
- Adjacent monetization products: AdPool (demand), ContentDiscovery (AI viewer acquisition), Transmit (in-stream ad formats). Programming Strategy Team = managed scheduling service. Live operations: real-time stream control, on/off switching, live ad-break insertion.

### Frequency (evidence: A — full public documentation portal; strongest operational evidence in sample)

- Frequency Studio = "multi-tenant SaaS platform" for creating, programming, distributing streaming channels. Tools: INGEST (feeds: S3, MRSS; videos; files; metadata best practices), MANAGE (series management, program templates, **rights management**, localized metadata, advanced metadata filters, automation programs), BUILD (manual playlists, search/filtering), SCHEDULE (calendar interface, playlist-to-schedule, repeat scheduling, schedule blocks, switch-to-live), GRAPHICS+ (overlays, tickers, squeezebacks), LIVE (live sources, live events, manual ad insertion, deliver-and-distribute, validate/protect live events), ANALYZE (dashboards, export), ACCOUNT (user/brand/linear-channel management).
- **CONNECT User Guide** (the distribution machinery — direct quotes):
  - "Connect is a suite of tools designed to track and deliver channels to distributors. It enables end-to-end monitoring from content ingestion to linear playout."
  - Dashboard alerts: **Playout Alerts** (critical: technical difficulties, static/black image, no audio for over a minute), **Scheduling Alerts** (critical when a live channel's schedule has fewer than 1 day of programming left; warning under 15 days), **Ingestion Alerts** (feed error states; per-item ingestion errors with named causes: missing description, no audio metadata, blank thumbnail, invalid file format, upscaling).
  - **Streams tab**: "displays the current status of all deliveries to distributors, from planned to live." Delivery lifecycle stages: **Plan → Configure → Validate → Submit → Approve → Live**. Configure includes "the video feed distribution path..., the EPG URL, the SSAI ad tags and CDN status". Validate = "pass/fail status of a stream's validation steps to ensure that the stream is up to the standards and specifications of the distributor". Approve = "received and approved for QA by the distributor, and a target live date". Live = "live on the distributor's platform and data is available to view in Analyze".
  - **Distribution Matrix**: "the status of each channel for every distributor."
  - **Monitor**: real-time playout tiles for all channels (screenshot refresh every 6 seconds), historical screenshots over the past four days, filtering by status/errors/channel.
  - **Distributors section**: "a comprehensive list of active and available distributors to which Frequency can deliver content."
- Distribution Specifications: Origination Channels Output Specification (video stream format, metadata format); Video Streams Outputs; **Scheduling Outputs (EPG)** with "EPG Formats per Distributor"; Dynamic Ad Insertion with "Distributor Advertising Integration Models".
- Content Delivery Guidelines: required/optional video specs and metadata; MRSS ingestion; S3 ingestion; broadcast creative guidelines.
- Distribution network: "Integrated with more than 200 destinations, including FAST platforms, vMVPDs and O&O applications, while supporting advertising enablement, CDN flexibility and head-end delivery." Pricing: flat monthly fee per channel, "no connector fees"; deliver to one or multiple distributors for the same price.
- Managed Channel Services (MCS): human-operated channel creation/operation service.

### Vubiquity (evidence: A on root page; services-led, no console observed)

- "Global technology-led solution provider for the media and entertainment industry, offering both managed services and products" — media supply chain + content licensing + OTT video.
- Services: VOD Packaging and Delivery ("content processing, transcode, packaging & delivery services"), Localization, Mastering, Library Clean-Up, FAST Programming and Delivery ("turnkey service to create, launch & monetize FAST channels"), Media Suite AI, MetaVU Title Management (SaaS metadata platform), Content Licensing.
- "Preferred fulfillment vendor for the world's biggest OTT platforms" (Netflix, Prime Video, Apple logos shown).
- Interpretation: the same provider→destination delivery work performed as a managed service rather than a self-serve platform. Confirms the services pole of the market; console-level object model not directly observed (evidence limitation).

### Peach (dropped)

- peach.tv returns a closure notice ("Peach is now closed"). Historically a content-distribution service for delivering video to OTT platforms; excluded from the sample. No claims based on it.

## Cross-product Comparison

| Dimension | Amagi | Wurl | Frequency | Vubiquity |
|---|---|---|---|---|
| Provider-side content inventory | Media Management (NOW platform) | asset onboarding | INGEST/MANAGE (feeds, videos, files, metadata) | packaging/mastering services |
| Distribution product | linear channels, VOD, social | FAST channels (new playout or restream) | linear channels (24/7 + live events) | FAST channels, VOD packages |
| Destinations | streaming platforms + pay-TV + broadcast headends/PoPs | 65+ streaming platforms incl. vMVPDs | 200+ destinations: FAST, vMVPD, O&O apps, headends | major OTT platforms (fulfillment) |
| Per-destination delivery record | CONNECT fulfillment status tracking | per-channel distribution incl. EPG/captions/DRM/ad routing | **Streams** with Plan→Configure→Validate→Submit→Approve→Live + Distribution Matrix | managed (not observed) |
| Destination-spec validation | implied (fulfillment status) | "everything needed to prepare channels for launch" | explicit Validate stage vs distributor specs; EPG formats per distributor | service-level |
| EPG/schedule outputs | scheduling product (Planner) | metadata delivery (EPG) | Scheduling Outputs (EPG), formats per distributor | service-level |
| Ad integration | THUNDERSTORM SSAI + ADS PLUS | ad routing/insertion, SSAI, inventory split | SSAI ad tags in Configure; DAI integration models | FAST monetization service |
| Monitoring | 24/7 global monitoring | impression validation, reporting | Monitor (live tiles, alerts, history) | service-level |
| Marketplace/discovery | Amagi CONNECT marketplace | "connect the parties" (no negotiation) | CONNECT "new distribution opportunities" | content licensing service |
| Delivery substrate | fiber/satellite/IP + streaming | streaming (CDN GB / headend connectors) | streaming + head-end delivery, CDN flexibility | platform fulfillment |
| Operating model | self-serve platform + managed services | self-serve + programming services | self-serve SaaS + Managed Channel Services | managed services |
| Commercial model | marketplace rev/inventory split | flat per-channel + usage fees | flat per-channel | service contracts |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **Provider-side content inventory** — the operator's content (assets and/or assembled channels) held as managed objects in the platform.
2. **External consumer-facing destinations** — a catalog of distribution endpoints (streaming platforms, broadcast headends) that are outside the operator's own service.
3. **Per-destination delivery as a managed, tracked object** — each delivery to each destination is a discrete record with a lifecycle (prepare → configure to destination spec → validate → submit → destination approval → live), carrying destination-specific packaging (formats, EPG/metadata, ad integration).
4. **Delivery status & monitoring** — the operator can see, per destination, whether the content is live and healthy.

Test: remove destinations → playout/MAM system; remove per-destination delivery tracking → CDN/file transfer; remove provider-side content management → bare transport service; remove content (keep only ads) → ad platform. All four properties are needed.

### L1 — Common Mature Structure

- Ingest machinery with validation and error states (feeds: MRSS/S3/upload; named failure causes)
- Metadata management (required/optional fields, localized metadata, regional parental ratings, genres, series structures)
- Channel origination/playout for the linear pole (scheduling calendar, playlists/programming blocks, live sources, graphics, switch-to-live)
- VOD packaging (transcode, packaging, delivery) for the VOD pole
- EPG/schedule outputs, formatted per destination
- Ad integration (SSAI/DAI, cue points/ad markers, per-destination integration models, inventory/revenue split)
- Real-time monitoring (playout health, alerts: playout/scheduling/ingestion) and per-destination analytics
- Marketplace/discovery layer connecting providers and destinations (connection requests, profiles)
- Multi-tenant SaaS console + developer APIs
- Managed-services layer (programming strategy, full-service channel ops)

### L2 — Variant / Optional Structure

- Delivery substrate: streaming platforms (FAST/vMVPD/SVOD/O&O/social) vs broadcast headends (fiber/satellite/IP) — both exist in-sample
- Product form: origination+distribution suite vs pure distribution/restream vs services-led fulfillment vs marketplace-led
- Content scope: linear-only, VOD-only, or both; live-event-heavy (sports/news) vs library channels
- Channel mode: newly originated playout vs restream of an existing feed
- Commercial models: flat per-channel fee, usage fees (CDN GB, per-stream connector), inventory share vs revenue share
- Rights management embedded in the manage layer (window/territory constraints on what can go where)
- Social publishing as an additional destination class (Amagi Social Publishing)

### L3 — Vendor-specific (research notes only)

- Frequency: tool names (INGEST/MANAGE/BUILD/SCHEDULE/GRAPHICS+/LIVE/ANALYZE/ACCOUNT); CONNECT stage names Plan/Configure/Validate/Submit/Approve/Live; Monitor 6-second screenshot refresh; 4-day screenshot history; rescue slate; Fusion Schedule; Schedule Automator; "no connector fees" pricing claim; 200+ destinations / 350M viewers claims
- Wurl: Global FAST Pass / AdPool / ContentDiscovery / Transmit product names; AppLovin exclusive demand; 65+ platforms and 4B hours/month claims; ~200-hours content guidance; restream ≈ 1/3–1/2 of full launch timeline; DTC CDN-GB vs headend connector fee split
- Amagi: Amagi NOW / Cloudport / Thunderstorm / ADS PLUS / CONNECT names; 400+ channels & 50+ platform profiles on CONNECT; inventory-share vs revenue-share FAQ; 9,000+ channel deliveries / 26B+ ad impressions / 300+ platforms claims
- Vubiquity: MetaVU, Media Suite AI; "preferred fulfillment vendor" positioning for Netflix/Prime/Apple

## Rejected Findings

- "A content distribution platform negotiates distribution deals" — rejected as definitional. Wurl explicitly states it does not negotiate; Amagi CONNECT automates connection requests and billing but the commercial agreement remains between parties. Marketplace/discovery is common (L1), deal-making is not the platform's defining act.
- "A content distribution platform is a CDN" — rejected. CDN flexibility/substrate appears in-sample (Frequency "CDN flexibility", Wurl CDN usage fees) as an underlying transport choice, not the managed object. The managed object is the content product and its per-destination delivery, not cache/network config.
- "Distribution requires channel origination/playout" — rejected as definitional. Wurl's restream mode and Vubiquity's VOD packaging/delivery deliver content that the platform never originates. Origination is the dominant modern pattern (L1) but not the invariant.
- "Distribution is FAST-only" — rejected. In-sample substrates include broadcast headends (Amagi fiber/satellite/IP; Frequency head-end delivery) and vMVPDs; FAST is the current growth market, not the definition.
- "Consumer-side aggregation is part of this Type" — rejected. Aggregation for viewers is a different Type (§02.08 Content Aggregator); the platform-side marketplace is a supply-side matching layer.

## Boundary Findings

- **vs Video Streaming Platform**: the streaming platform is the *destination* — a consumer-facing service with its own app/UX/subscriptions. The distribution platform is provider-side plumbing; it has no consumer surface. The relationship is commercial: destinations are the distribution platform's counterparties (and Amagi explicitly serves "Distributors" as customers of its marketplace). Remove the consumer app and the distribution platform stands; remove the distribution pipe and the streaming platform stands.
- **vs CDN Management (§14)**: CDN management's managed object is network-level delivery configuration (zones, cache rules, TLS, origins) for arbitrary web/media traffic. The content distribution platform's managed object is the content product and its per-destination delivery lifecycle (EPG, ad integration, submission/approval). A CDN is a substrate the distribution platform may sit on.
- **vs Media Asset Management / MAM**: MAM centers on organizing/storing assets; the distribution platform centers on moving packaged content products to external destinations. Ingest/manage layers overlap (Frequency MANAGE, Amagi Media Management) — the delta is the destination side. A MAM without destinations is not a distribution platform.
- **vs Broadcast Management System / Channel origination**: BMS runs a broadcaster's own air (traffic, scheduling, playout for own channels). Distribution platforms embed origination (Cloudport, Studio) as *preparation for outward delivery to many destinations*; the center of gravity is the outward pipe, not the single own-air operation.
- **vs Music Distribution Platform / Podcast Platform (§27 siblings)**: same provider→many-platforms shape in the audio medium (tracks/episodes → streaming services/directories). Different object world (no channels/EPG/SSAI in the same sense). The directory gives them separate leaves; this leaf documents the video/streaming-centered Type the sampled market calls "content distribution".
- **vs Ad Delivery Platform / SSP (§06)**: ads appear here only as a monetization layer attached to distributed content (SSAI/DAI, inventory split). The managed object is content, not ad impressions.
- **vs Content Aggregator / Curation (§02.08)**: consumer-side aggregation for viewing vs supply-side delivery for distribution. Opposite sides of the same pipe.
- **vs Press Release Distribution Platform / marketing "content distribution" (§06)**: same words, different industry and object world (press releases / marketing content / native ads). The name collision is recorded for taxonomy awareness.
- **"Remove what to become another Type" test**: remove external destinations → MAM/playout; remove per-destination lifecycle → CDN/managed file transfer; remove content inventory → ad platform/transport; remove the provider side (serve viewers directly) → Video Streaming Platform.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?
- Traditional broadcast distribution services (satellite/fiber feeds to cable headends and PoPs) — still sold today (Amagi Linear Distribution) and structurally identical: content inventory, destinations (headends), per-destination delivery, monitoring. Fits.
- FTP/manual VOD delivery fulfillment vendors (Vubiquity's packaging & delivery lineage) — fits: inventory, destinations, per-destination delivery, status (as a service).
- Program syndication (delivering a show feed to many stations) — fits conceptually; not directly sampled (noted as uncertainty).
The L0 therefore does not over-fit to the modern FAST era: marketplace, SSAI, per-distributor EPG formats, and self-serve consoles are L1 common structure, not definitional.

## Uncertainties

- Wurl console-level object model not directly observed (product page + FAQ only); its lifecycle stage names, if any, are unknown. Lifecycle evidence rests on Frequency's documented Plan→Configure→Validate→Submit→Approve→Live; cross-product support for the *concept* (per-destination delivery states) comes from Amagi CONNECT's fulfillment-status tracking and Wurl's "prepare channels for launch" language, but exact stage sets may differ per product.
- Vubiquity evidence is root-page level; its fulfillment workflow detail is not documented publicly. Treated as the services pole without console claims.
- Whether destination-side (distributor) tooling is part of the same Type is unresolved: Amagi CONNECT gives platforms acquisition profiles, and Frequency CONNECT lists distributors, but no sampled product documents a full distributor-side operations console. Recorded as an open question rather than a claim.
- Numeric claims (200+/65+/300+ destinations, 4B hours, 9,000+ channels) are vendor marketing figures; kept out of the final document.
- Podcast/music distribution products were not sampled (separate leaves); the audio-sibling boundary is asserted from directory structure, not product research.

## Final Synthesis

A Content Distribution Platform is the provider-side system of record for getting a content owner's video content onto many external consumer-facing destinations. Its world has two sides joined by managed deliveries: on the provider side, a content inventory (ingested assets with metadata, assembled into channels or VOD packages); on the destination side, a catalog of external platforms and headends; between them, one delivery record per content-product-per-destination, carrying destination-specific packaging (formats, EPG, ad integration) and moving through a lifecycle that ends only when the destination has approved and launched the content, after which the platform's job shifts to monitoring health, refreshing content, and reporting performance per destination. Origination/playout, marketplaces, SSAI, and managed services are the modern common structure around this core; the core itself is the two-sided inventory→destination pipe with tracked, spec-gated, approval-gated deliveries.
