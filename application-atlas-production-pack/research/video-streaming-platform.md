# Research Notes — Video Streaming Platform

Leaf: Video Streaming Platform (DIRECTORY.md §27 Media, Entertainment, Creator & Culture)
Slug: video-streaming-platform
Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what a Video Streaming Platform actually is as an Application Type — from real products, not from the "OTT/SVOD" marketing vocabulary: what objects exist inside it, what the viewer does, how access is governed, what varies by product/business model, and where its boundaries run against the neighboring Types already processed in §27 (music-streaming-platform, podcast-platform, content-distribution-platform, media-asset-management-mam, media-rights-management, media-subscription-management, media-audience-management) and §01.05/§01.08 (short-form-video-social-platform, social-live-streaming-platform).

## Initial Boundary (hypothesis before research)

- Core guess: viewer-facing on-demand catalog of professionally produced/licensed video, played back on the platform under a monetization/access model (subscription/ads/transaction).
- Nearest neighbors likely confused with it:
  - Music Streaming Platform (same structure, different medium)
  - Podcast Platform (video podcasts straddle the medium)
  - Short-form Video Social Platform (video, but UGC post-feed social loop)
  - YouTube-class long-form UGC platforms (no dedicated directory leaf — potential taxonomy gap)
  - Social Live Streaming Platform (live vs on-demand; user-originated vs operator catalog)
  - Content Distribution Platform / Media Asset Management / Media Rights Management / Media Subscription Management (operator-side machinery that feeds or bills the viewer-facing service)
- Obvious unknowns: whether personal viewing state is definitional or only common; whether live linear channels (FAST) are a variant or a different Type; how episodic release structures relate to podcast show/episode semantics.

## Research Questions

1. What is the unit of the catalog — title? episode? season? How are films vs series organized?
2. Who supplies the catalog content, and who decides what is available where/when?
3. What access/entitlement models exist, and how are they enforced at the title level?
4. What persistent state does the viewer have (history, resume, watchlist), and under what identity?
5. What does the viewing loop look like end-to-end (acquire access → discover → select → playback → return)?
6. How do episodic releases, reservations/reminders, and "watch ahead" mechanics work?
7. Where do downloads, subtitles/dubs, device surfaces, and quality tiers sit — core or variable?
8. What happens when rights expire (catalog churn)? What does the viewer lose?
9. What is NOT this Type: live social broadcasts, UGC feeds, linear broadcast, music, podcasts, B2B media machinery?

## Representative Products

Selected for market representation + different product philosophy + different monetization model + different geography/tier:

| Product | Orientation | Why sampled |
|---|---|---|
| Netflix | global pure-play subscription (SVOD), originals+licensed mix | the archetype of the catalog-on-demand-subscription shape |
| Disney+ | franchise/house-of-brands SVOD, bundle packaging | catalog organized around owned franchises; bundle/gift machinery |
| Prime Video | ecosystem-bundled subscription + transactional (rental/purchase) + add-on channels | most heterogeneous monetization in one surface |
| Pluto TV | FAST — free, ad-supported, channel-first | the anti-subscription philosophy; linear flows inside an on-demand product family |
| iQIYI (iq.com) | regional (Chinese/Asian content) hybrid: free-with-ads + tiered VIP membership | regional tier; richest reachable official documentation in this pass |

## Sources

Attempted (official, Tier 1/2):

- Netflix — https://help.netflix.com/en/ (403), https://www.netflix.com/ (403) — NOT reachable
- Prime Video — https://www.primevideo.com/help (503) — NOT reachable
- Disney+ — https://help.disneyplus.com/ (empty), https://www.disneyplus.com/ (geo-block page REACHED: official footer surfaces observed — Help center, Supported Devices article, Subscriber Agreement, Disney Bundle, Gift Disney+) — PARTIALLY reachable
- Pluto TV — https://support.pluto.tv/ (JS shell), https://www.plutotv.com/ (geo-block) — NOT reachable
- Tubi — https://help.tubi.tv/hc/en-us (transport error) — NOT reachable
- iQIYI — https://www.iq.com/ (REACHED, full home surface), https://intl-help.iq.com/... (REACHED, official FAQ help center: Account / Payment / Automatic renewal / VIP rights / Playback / Download / Subtitle categories) — FULLY reachable

App Store listing surfaces (apps.apple.com product pages) redirected to a regional storefront today page — not usable.

**Sourcing limitation (recorded per evidence rules):** the research environment is regionally constrained; 4 of 5 sampled products' official operational documentation was unreachable (403 / 503 / geo-block / JS shell). Only iQIYI provides directly observable operational documentation, plus URL-level official observation of Disney+'s footer surfaces. Product-specific operational facts for Netflix, Prime Video, Pluto TV, and Tubi are therefore NOT asserted from product evidence; those products are named for market orientation only. All cross-product findings below are held at intrinsic-structure strength, calibrated by the processed sibling passes (music-streaming-platform, podcast-platform, short-form-video-social-platform, social-live-streaming-platform all documented structurally adjacent or counterparty Types), and the final document uses calibrated wording ("commonly", "typically", "some products") rather than product-attributed precision.

---

## Product Observations

### iQIYI (iq.com) — evidence layer A (directly observed, official surface)

Home/navigation surface (iq.com):

- Catalog organized by content category: For You (personalized home), Trending (ranking), Drama, Movie, Anime, Variety Show, More.
- Popular Searches + search history; search bar prominent.
- Personal areas attached to the login account: Me — My Account (settings), Watch Later, History, Reservation, Subtitle Translation; Login/Signup gate.
- VIP entry: "Join VIP" with privileges page (Watch on multiple devices, 1080P, Advanced viewing, Skip AD), voucher code redemption.
- Content items surfaced with type/region/genre metadata and descriptions ("Thailand BL&GL Urban Thai Romance…"), new-episode badges.

Official FAQ help center (intl-help.iq.com):

- **Account**: account with unique User ID; link email/phone for security; password management; surfaces = mobile app, PC website (iq.com), TV apps (Apple TV, Android TV, Roku TV). Account security and login recovery flows documented.
- **Payment / membership**: purchase of VIP membership per surface with surface-specific payment methods (Google/Apple in-app on mobile, bank card on PC web, Roku Pay on Roku); VIP subscription is bound to the purchasing account and cannot be transferred; voucher codes and coupon codes redeemable against purchase; promotions with display rules; auto-renewal charged within a defined pre-renewal window and cancellable per payment channel.
- **VIP rights (tiered membership)**: Standard VIP vs Premium VIP differ on: number of concurrent screens, resolution ceiling, and one express-viewing privilege ("Express Package — watch final episodes ahead of others"; Standard instead has "Advanced viewing"). Shared rights: multiple terminals, VIP skip-ads, Dolby audio, VIP Download, exclusive content, blockbusters. After VIP expiry the account "can still enjoy all our free content" — free tier exists and carries ads (skip-ads is a VIP privilege).
- **Playback**: playback error/feedback flow referencing specific series+episode; Watch Later bookmarking ("Me – My List"); **catalog churn by copyright**: "Why cannot I find the videos previously available now?" — answered with copyright/territory reasons and an explicit note about not using VPN proxies (territorial licensing enforced); skip intro/outro as a per-title-available playback feature; resolution switch on the player.
- **Download**: downloads gated by membership tier and by per-title copyright; downloaded member-exclusive videos become unplayable when membership expires ("Due to copyright protection policies…"); downloads exist only inside the app; TV/PC surfaces do not offer downloads.
- **Subtitles**: multiple subtitle languages selectable on the player; subtitle availability varies by title (AI translation limits); dubbing/subtitle production as an ongoing supply process.

### Disney+ — evidence layer A− (official surface partially observed)

- Geo-block page reached (official Disney+ domain): footer exposes official surfaces — Help center, "Supported Devices" help article, Subscriber Agreement, Closed Captioning inquiries, Children's Online Privacy Policy (kids surface exists), "Disney Bundle" (packaging with sibling services), Gift Disney+ (gifting), Partner Program.
- Confirms at URL level: device-support matrix as a first-class concern, subscriber-agreement-gated access, kids/children privacy surface, bundling as packaging, gifting as purchase form. Content of help articles NOT fetched — no product-specific operational facts asserted.

### Netflix / Prime Video / Pluto TV / Tubi — evidence layer 0 (market orientation only)

- Official documentation unreachable this pass (403/503/geo/JS). No product-specific operational claims are recorded for these products. Market-orientation knowledge (subscription-first vs FAST/ads vs transactional mixes) is used only at the level of "these are recognized market shapes", cross-checked against the processed sibling passes.

### Structural cross-check from processed sibling passes (counterparty evidence)

- music-streaming-platform L0: platform-operated catalog of recordings + on-demand selection/playback + persistent personal listening state. Music pass ratified: podcast = episodic shows to a standing follower; music = individual selectable recordings from a catalog.
- podcast-platform: video podcasts straddle medium but keep show/episode structure — pre-hung flag for this pass.
- social-live-streaming-platform: supply seam (user-originated live broadcasts vs licensed/produced catalog) — pre-hung flag for this pass; that pass also recorded "live-event/media streaming is NOT this Type".
- content-distribution-platform: its external destinations include "FAST platforms, vMVPDs, SVOD, O&O apps" — i.e., the video streaming platform is a DESTINATION of provider-side distribution.
- media-subscription-management: subscription/access + revenue lifecycle as the media system of record — operator-side machinery.
- media-rights-management: rights grants (territory/window/exclusivity) as the upstream system that determines catalog availability.
- short-form-video-social-platform: short video post + discovery feed + creation loop + social participation loop — the UGC social shape.

---

## Cross-product Comparison

| Dimension | Observed pattern | Evidence |
|---|---|---|
| Catalog unit | Films as single titles; series as title→season→episode hierarchy; specials/documentaries as titles | iQIYI (Drama/Movie/Anime/Variety categories, episode numbering, "final episodes") + market orientation; music pass analog (track/album) ratified at category level |
| Catalog supply | Operator-acquired (licensed) and operator-commissioned (original/produced) content; viewers never upload the catalog | iQIYI copyright explanations (A); structural |
| Availability | Territorial + time-windowed; titles appear and disappear as rights change | iQIYI FAQ "videos previously available now" + VPN note (A); media-rights-management pass documents the grant machinery upstream |
| Access models | Subscription membership (tiered), free-with-ads, transactional purchase/rental, free-registration hybrids — often combined | iQIYI (free+VIP tiers, A); Disney+ bundle/gift (A−); market shapes of Netflix/Prime/Pluto held at orientation level |
| Entitlement enforcement | Per-title gating: some titles members-only; ad load tied to tier; download rights tied to tier + per-title copyright | iQIYI (A) |
| Personal state | History, Watch Later/My List, Reservation (upcoming-episode reminders), resume/continue surfaces | iQIYI (A); universal in subscription-centric products per sibling-structure reasoning (B, weakened) |
| Discovery | Personalized home (For You), category/genre browse, trending/ranking, search | iQIYI (A); music pass analog ratified |
| Episodic release | Titles release episodes on schedules; reservation/reminders; paid "watch ahead" privileges exist in some products | iQIYI (Reservation, Express Package/Advanced viewing, A) |
| Surfaces | Web, mobile apps, connected-TV apps under one account | iQIYI (A); Disney+ supported-devices article exists (A−) |
| Downloads | In-app licensed playback, tier-gated, expiring with membership, per-title availability | iQIYI (A) — the download is a licensed convenience, NOT ownership |
| Localization | Subtitles/dubs as platform-managed layers with per-title availability | iQIYI (A); Disney+ closed-captioning surface (A−) |
| Live/linear | Linear channels and live events exist inside some products as variants | market orientation + social-live pass's "NOT this Type" note; no direct doc evidence this pass — held as variant |

## L0 — Defining Invariant

Three jointly-held structures. Removing any one stops the product being recognizable as a Video Streaming Platform:

1. **The platform-operated video catalog of record** — a persistent, curated collection of professionally produced or operator-commissioned video held as identifiable titles (films; series organized into seasons and episodes), carrying per-title metadata and operator-managed availability, and organized for browsing and search. The operator decides what is in the catalog; the viewer cannot upload into it. (Remove → user-generated video platform / search-and-link surface.)

2. **On-demand streaming playback of catalog titles on the platform itself** — the viewer selects a specific title or episode and the platform delivers the video itself for immediate, viewer-controlled playback (play/pause/seek), continuing across sessions and devices. The platform is the delivery surface for the actual video, not a pointer to somewhere else. (Remove → TV-guide/discovery surface, storefront without playback, or linear broadcast.)

3. **Access governed by the platform's access model** — what a viewer may watch is determined by their standing with the operator (subscription membership, free-with-advertising, transactional rental/purchase, registered-free), enforced per title. The catalog is monetized under a stated model; it is not open web content. (Remove → open/unmonetized video site, or a rights marketplace between businesses.)

Jointly-held load-bearing test:

- 1 alone = a title database / listings guide (JustWatch-class) or a rights catalog
- 2 alone = a generic video player / file player
- 3 alone = a billing plan with nothing to watch
- 1+2 without 3 = open unmonetized video site (drifts toward UGC/link surfaces)
- 1+3 without 2 = storefront/guide that never plays the video
- 2+3 without 1 = playback machinery over no managed catalog (kiosk)

## L1 — Common Mature Structure

Present across mature modern products; expected by the market but not definitional:

- Persistent viewer account with personal state: viewing history, resume/continue-watching, watchlist ("My List"/Watch Later), and (varies) ratings — durable and cross-device.
- Personalized discovery: recommendation-driven home rows, category/genre browsing, trending/ranked surfaces, search over the catalog.
- Series/episodic structure with release scheduling: new episodes arriving over time, reservation/reminders for upcoming episodes; some products sell "watch ahead" privileges.
- Multi-surface delivery: web, mobile apps, connected-TV apps under one account identity.
- Offline downloads as licensed in-app playback — tier-gated, per-title availability, expiring with the entitlement.
- Localization layers: subtitles, dubs, and per-title availability of them.
- Playback conveniences: resolution/quality switching, skip intro/outro (per-title availability).
- Multiple viewer profiles and kids-specific experiences with parental controls. *(Held at weakened strength this pass: ubiquitous in market orientation, but not directly re-verified in fetched docs beyond Disney+'s children's-privacy footer surface; final document uses hedged wording.)*

## L2 — Variant / Optional Structure

- Monetization mix: pure subscription / ad-supported tiers / fully free-with-ads (FAST) / transactional rental & purchase / hybrid — including ad-tier additions to subscription products.
- Supply philosophy: licensed-catalog-first vs originals-first vs franchise-first.
- Linear-flavored capabilities inside the on-demand product: FAST channels, live events (sports, live comedy), channel-style programming.
- Ecosystem packaging: bundling with sibling services, telco/commerce bundles, gifting, add-on channel marketplaces (reselling other services inside the platform).
- Regional strategy: territory-specific catalogs, regional content slates, language/dub depth.
- White-label/platform variants: services operated inside device ecosystems or operator set-top environments.

## L3 — Vendor-specific (research notes only, not in final document)

- iQIYI: Standard vs Premium VIP rights lists (concurrent-screen counts, resolution ceilings, "Express Package" final-episode watch-ahead, "Advanced viewing"); voucher/coupon redemption flows; per-surface payment methods (Roku Pay on Roku, bank card on PC web); auto-renewal charged within a pre-renewal window; Reservation feature; Subtitle Translation personal area; per-title AI-translation limits; downloads unavailable on TV/PC web surfaces.
- Disney+: brand-hub organization of the catalog (market knowledge, not re-verified), Disney Bundle sibling-service packaging (observed at URL level), gifting.
- Netflix/Prime Video/Pluto TV/Tubi: no product-specific facts recorded this pass (docs unreachable).

## Vendor-specific Findings (summary)

All precise numbers, tier names, and feature gates observed in iQIYI's help center are iQIYI product facts and stay here. The final document carries only the generalized patterns they evidence (tiered membership gating features; downloads expiring with entitlement; territorial availability), with calibrated wording.

## Boundary Findings

**Flag discharges (pre-hung by sibling passes):**

1. **vs Social Live Streaming Platform (§01.08) — RATIFIED from this side.** The supply seam holds: user-originated live broadcasts (a creator streams to a watching audience) = Social Live Streaming; an operator-acquired/produced on-demand catalog = Video Streaming Platform. "Live-event/media streaming is NOT this Type" is confirmed from this side: live channels/events inside a video streaming product are variant capabilities (L2), not the defining core; and a live sports feed alone is not the Video Streaming Platform Type. Remove the on-demand curated catalog+playback → social live territory; remove user-originated live → this Type stands.
2. **vs Podcast Platform (§27) — RATIFIED from this side.** Medium alone does not decide; the consumption structure does. Content consumed primarily as a standing show whose episodes arrive to a follower = podcast even in video form; a video streaming platform may carry such shows as catalog items without changing Type. The Video Streaming Platform's center is catalog-selectable titles (films/episodes watched by selection, not by standing show subscription). Remove show/follower semantics → this Type stands; remove the catalog and keep standing-show arrival → podcast territory.
3. **vs Media Subscription Management (§27) — seam confirmed.** The viewer-facing service where access is consumed vs the operator-side subscription/billing/access-lifecycle machinery. The video streaming platform's plan management surface is one entitlement realization; the revenue machinery is the other Type. Remove the viewer catalog/playback → subscription machinery remains.

**Structural boundaries:**

4. **vs Music Streaming Platform (§27):** same structural shape (operator catalog + on-demand selection + personal state), different medium and content organization (audio recordings in albums/artist discographies vs video titles in series/seasons/episodes). Medium is the seam ratified by the music pass; bundling both directions (services adding podcasts/video) does not merge Types.
5. **vs Short-form Video Social Platform (§01.05):** UGC post-feed social loop (creation tool, discovery feed over the platform-wide pool, participation signals) vs operator-curated professional catalog consumed by selection. Remove the creation loop + UGC supply → this Type; remove the catalog curation and add creator posts → short-video social.
6. **vs YouTube-class long-form UGC platforms (TAXONOMY GAP — recorded, no directory change):** creator-uploaded catalog, channel subscription and social circulation sit between §01.05 social leaves and this Type; no dedicated directory leaf exists. The center of gravity (user uploads + channel/follow graph) is NOT this Type; this pass treats operator-curated supply as definitional partly because of this boundary.
7. **vs Internet Radio Platform / linear broadcast:** continuous scheduled flow vs on-demand selection. Channel-first pure-linear video products (FAST at their purest) drift toward broadcast territory; inside mixed products linear channels are a variant.
8. **vs Content Distribution Platform (§27):** provider-side packaging/delivery of channels/VOD products TO destinations (the destinations include video streaming platforms) vs viewer-facing consumption. Counterparty relationship per that pass's model.
9. **vs Media Asset Management (§27):** internal custody/metadata/search of the media corpus vs viewer-facing service. MAM manages the source assets a platform's catalog is built from.
10. **vs Media Rights Management (§27):** upstream grants (territory/window/exclusivity) that determine what the catalog may carry; the streaming platform is an exploiting surface of those grants.
11. **vs Media Audience Management (§27):** the organization's audience person records/segments/activation vs the viewer's own account/profile inside the service.
12. **vs Video Editor / NLE (§04.06):** authoring tools vs distribution/consumption platform.
13. **vs Personal Cloud Drive (§03.15):** personal files vs operator-licensed catalog; the platform's downloads are licensed in-app playback, never user-owned files (iQIYI A-evidence).
14. **vs DVD-by-mail / physical rental (historical):** physical distribution without on-demand playback is NOT this Type — confirms that delivery of the video itself on demand is load-bearing.

## Historical / Market-Sample Check

- Cable/set-top VOD and pay-per-view (pre-smartphone era): operator catalog + on-demand playback + subscription/PPV entitlement — satisfies all three legs with no app, no algorithmic recommendation, no downloads. Delivery substrate (managed IP/cable vs internet streaming) is implementation, not definition.
- Early download-to-rent stores: account-bound entitlements, expiring rentals — fits (playback delivery on demand under entitlement); persisting personal state beyond the entitlement was weak, supporting the decision to hold detailed state at L1 while entitlement stays L0.
- Regional ad-supported licensed-catalog sites: free-with-ads access model over curated catalogs — fits leg 3 without subscriptions.
- FAST/linear-first products: on-demand sections + account are present even when channels lead — the three legs still hold in the product family; a channels-only product with no on-demand catalog would fall below the Type bar (drift to broadcast).
- Conclusion: the definition survives older, regional, and platform-native forms; "streaming" is the dominant modern delivery realization, not the invariant itself — the invariant is on-demand delivery of an operator-governed catalog under an access model.

## Uncertainties

1. Profiles/parental controls: ubiquitous in market orientation; only weakly evidenced this pass (Disney+ children's-privacy footer). Kept hedged in the final document.
2. Live channels/events: no direct official doc evidence this pass; held as variant based on market orientation + social-live pass counterparty note.
3. Whether a fully channels-only, no-on-demand FAST product should be inside this Type: this pass draws the Type bar at "on-demand catalog required"; flagged for future joint review if a FAST-specific pass ever runs.
4. Exact mechanics of add-on channel marketplaces (reselling third-party services): market-orientation level only.
5. Netflix/Prime Video/Pluto TV/Tubi product facts: none recorded (docs unreachable).

## Final Synthesis

A Video Streaming Platform is the viewer-facing service whose defining core is exactly three jointly-held structures: (1) the platform-operated catalog of professionally produced/commissioned video titles organized as films and series/seasons/episodes with operator-managed availability; (2) on-demand streaming playback of those titles on the platform itself, viewer-controlled and continuing across sessions/devices; (3) viewer access governed by the platform's access model (subscription membership, advertising-funded, transactional, or free-registration hybrids), enforced per title. Personal state (history/resume/watchlist), personalized discovery, downloads, subtitles/dubs, multi-device delivery, and profiles are the common mature layer; monetization mix, supply philosophy, linear/live capabilities, and packaging are variants. The Type is the destination side of content-distribution, the exploiting surface of media rights, the consumer side of media subscription machinery, and the medium-sibling of music streaming — with the supply seam (operator catalog vs user-originated) separating it from social live and short-form social Types.
