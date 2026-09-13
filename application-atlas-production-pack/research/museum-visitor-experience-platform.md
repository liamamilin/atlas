# Research Notes — Museum Visitor Experience Platform

Research date: 2026-09-08
Leaf: Museum Visitor Experience Platform (§26, Travel/Hospitality/Events family)
Slug: museum-visitor-experience-platform

## Research Goal

Understand what the museum-facing "visitor experience" software category actually is, from real products: what the institution authors, what the visitor consumes, on which surfaces, and where the Type's boundaries run — especially against the admission-business Type (Attraction Management System, §26) that pre-flagged this leaf, the collection-publishing Type (Digital Collection Portal, §27), and the museum collections/CMS family (§27).

## Pre-hung Flags This Pass Must Discharge

1. **attraction-management-system sibling-leaf cluster flag (§26, processed 2026-09-06/07):** the AMS pass recorded that "Museum Visitor Experience = visitor experience layer" among segment-/layer-variants of the admission-business Type, and required each sibling to confirm slice-vs-variant-vs-independent-Type status. The AMS document's own Related-Types table already positions this leaf as "adjacent, complementary — visitor-facing interpretation and experience layer, not the admissions business." This pass must confirm or contest that from real product evidence.
2. **museum-collections-management counterparty note (§27, processed 2026-09-08):** this leaf listed as an unprocessed sibling that should treat the collections document as counterparty. Expected clean seam (custody vs visitor-facing interpretation).

## Initial Boundary (hypothesis before research)

- Hypothesis: the Type is the museum-operated digital layer that shapes what visitors experience before/during/after the physical visit — digital guides, audio tours, in-gallery interactives — authored by the institution and consumed on visitors' own devices, museum-loaned devices, or on-site screens.
- Most likely confusions: (a) admission/ticketing platforms (AMS, Attraction Ticketing, Event Ticketing); (b) public publishing of collection records (Digital Collection Portal); (c) museum collections management suites; (d) generic website/app builders.

## Research Questions

1. What is the core content object? (guide/tour/stop; what is a stop bound to?)
2. Who authors content, and through what surface? Is the CMS part of the product?
3. On which surfaces do visitors consume? (own phone — app/PWA/web; venue-loaned devices; on-site kiosks/touchscreens)
4. How does content align with the physical encounter? (QR, number/codes, image recognition, GPS/beacons, maps, browse/search)
5. What media are carried? Is audio definitional or just dominant?
6. Is admission selling/entry validation part of any sampled product? (expected: no)
7. What visitor-relationship machinery exists (analytics, surveys, messaging) and is it core or optional?
8. Do products operate single-institution (white-label) or multi-institution (network) postures — and is posture definitional?
9. Historical check: does the definition survive the keypad audio-guide-device era (and printed-guide ancestors)?
10. Where exactly do the AMS / Digital Collection Portal / collections-CMS seams run?

## Representative Products

Selected for market representation, document accessibility, and deliberately different product philosophies and client tiers:

| Product | Philosophy / posture | Tier / model |
|---|---|---|
| Bloomberg Connects | free shared multi-museum app; institution-authored guides in a common app | nonprofit/civic institutions, philanthropy-funded, free |
| STQRY (Apps / Kiosk / Fleet / Marketplace / Collect) | commercial white-label SaaS; same platform sells visitor-phone apps, on-site kiosks, and venue device fleets as separate product lines | single institutions through enterprise, subscription |
| Smartify | "digital experience platform for museums" — apps + devices + AI + CMS + surveys + revenue services | 1200+ cultural organisations, mixed model |
| Guide-ID (Podcatcher Pro) | dedicated screen-free audio-guide hardware + Tour Editor platform + mobile PWA companion | museums/exhibitions/heritage, hardware + platform |

(izi.TRAVEL — free self-service storytelling platform — was selected as a fifth sample but its site timed out twice; abandoned per network rules and held at market-anchor level only. See Sources.)

## Sources

All fetched 2026-09-08 unless noted.

- Bloomberg Connects — homepage https://www.bloombergconnects.org/ ; FAQ https://www.bloombergconnects.org/faq/ ; For Partners (features + process) https://www.bloombergconnects.org/for-partners/ (the /features/ URL serves this page) — all fetched successfully.
- STQRY — homepage https://stqry.com/ ; STQRY Apps https://stqry.com/products/stqry-apps ; STQRY Kiosk https://stqry.com/products/stqry-kiosk ; STQRY Fleet https://stqry.com/products/stqry-fleet — all fetched successfully.
- Smartify — homepage https://www.smartify.org/ ; Partners page https://www.smartify.org/partners/ — fetched successfully. Deeper product/solution/article pages (products/cms, solutions/connect-with-your-visitors, articles/how-visitors-discover-more...) returned 404 ×3 — abandoned per network rules; Smartify held at partner-page strength.
- Guide-ID — homepage https://www.guide-id.com/ ; Platform https://www.guide-id.com/products/platform/ — fetched successfully.
- izi.TRAVEL — https://izi.travel/ and https://izi.travel/en both timed out ×2 — abandoned; market-anchor level only, no product claims.

## Product Observations

### Bloomberg Connects

Evidence layer A (official pages fetched directly).

- Self-description: "The arts and culture app… explore expert-curated content and guides to over 1500 museums, galleries, sculpture parks, gardens, and cultural spaces" (homepage). Free to download and free to use; created by Bloomberg Philanthropies.
- Guides are institution-authored: "your team builds your own guide in our easy-to-use Content Management System (CMS)" (For Partners). Onboarding is cohort-based (a multi-week process with content sessions and group calls) — vendor process detail.
- Content: "exclusive audio and video content about works of art and objects, hear from artists and curators… current and past exhibitions" (FAQ). "The guides feature audio, video, photography, and text" (FAQ).
- Surfaces: one shared iOS/Android app carrying hundreds of institutions' guides (FAQ: "access cultural institutions from around the world in one central app"). Use is explicitly both on-site and remote: "Use the app at participating cultural institutions to enhance your on-site experience or use the app remotely" (FAQ).
- Maps: "Help visitors navigate exhibition spaces, plus explore outdoor areas with integrated Google Maps" (For Partners).
- Multilingual: "over 50 languages" (For Partners). Accessibility: voiceover, captions, transcripts, image zoom, font adjustment (homepage + FAQ).
- Partner-facing data: "our community of partners have access to real-time data to better understand their audiences and make operational decisions" (For Partners).
- No admission selling or entry validation appears anywhere in the FAQ or partner material; headphones guidance is the closest operational note. Partner eligibility: physical space open to the public, nonprofit/civic status — venue-experience orientation confirmed.

### STQRY

Evidence layer A (official product pages fetched directly).

- Family structure: five product lines on one builder — STQRY Apps ("create beautiful, easy to use mobile guide and tour apps"), Kiosk ("digital labels and engaging interactives" on touchscreens), Fleet ("on-site hardware… download content to your shared devices"), Marketplace ("create, publish, and monetize your guided tours"), Collect ("digitize, store and publish your collections online") (homepage).
- Apps: web-based tour builder (add images, audio, text, map info, custom features) → publish to mobile web, iOS, Android → visitors use content "anywhere, even offline"; real-time content updates from the builder (Apps page).
- Content model: "Multiple Tours and Collections — show multiple routes or tours and publish your entire collection, easily categorizing by place, theme, or any custom option" (Apps page). Media: audio, images, video, 360, AR. Mapping: satellite/street/terrain or custom maps including indoor maps; "display your user's GPS location and nearby points of interest." Triggers: "Geofenced Alerts and iBeacons… location-based notifications… iBeacons triggering content as visitors approach" (Apps page).
- Engagement/commerce: quizzes and games; "Premium Content — support free tours, offer in-app purchases, and provide content that can be unlocked with a code"; sponsorship/advertising integration; analytics console "track location traffic and click behavior" (Apps page).
- Kiosk: "create digital labels and richly interactive storytelling elements"; web-based kiosk builder; themeable/customized displays; deploy to "as many touch screens as required"; accessibility (voiceover, image descriptions); 55+ languages incl. RTL and indigenous languages (Kiosk page).
- Fleet: venue-owned/loaned devices (any iOS/Android hardware); Fleet app provisioned by scanning a QR code or entering an app key; locked-down devices (settings, language, screen dimming, data sync); charging docks; MDM support; OTA updates; visitor mode vs driver mode (vehicle tours) (Fleet page).
- Same builder drives Apps, Kiosk, Fleet — one content base, multiple surfaces.

### Smartify

Evidence layer A at partner-page level (deeper pages unreachable).

- Self-description: "Smartify is the digital experience platform for museums, galleries and cultural destinations" (Partners page). "Trusted by 1200+ amazing cultural organisations."
- Solution axes (Partners page): Enhance with AI ("personalised experiences, object recognition, translations and more"); Connect with visitors ("Engage audiences before, during and after a visit with built-in messaging and surveys"); Improve access ("Digital guides for everyone. Audio descriptions, sign language tours…"); Grow revenue ("branded apps and device rental to premium and paid-for content"); Engage audiences ("audio, video and immersive AR"); Track performance ("Turn visitor behaviour into actionable insights… in one platform").
- Products listed: Custom apps ("across mobile, web and on-site devices. No downloads required, no app-store friction"), Content production, Marketing, AR/VR, Hardware, CMS, Web and mobile apps.
- Discovery methods (article teaser on Partners page, verbatim): "Smartify gives visitors four intuitive ways to discover more about what's on display: object recognition, numpad, search and QR code."
- Consumer app exists alongside the partner platform (app.smartify.org; "Try the Smartify app") — dual posture: institution platform + public multi-museum app.

### Guide-ID (Podcatcher)

Evidence layer A (official pages fetched directly).

- Dedicated screen-free audio-guide device: "Podcatcher Pro — the Audio guide that invites your visitors to discover your stories through a screen-free, and immersive experience"; "designed to trigger audio with a single movement"; "self-service audio guide pickup" (homepage).
- Platform: "Tour Editor Platform: the place where you access to manage your hardware and enhance your tour content while getting visitor data" (Platform page). Content: "Create new content or upload and repurpose existing materials… smart tools… automatically generate, adapt, and optimize content, while built-in translation supports 40+ languages. Publish tours effortlessly, manage devices and accessories from one place, and monitor device status in real time" (Platform page).
- Analytics: "see what they listen to… where your visitors go, what routes they take, where they stop and listen" (Platform page). AI/TTS voiceovers and script adaptation tools (Platform page).
- Mobile companion: "Mobile Solution — Made for Accessibility… supports sign language videos and on-screen text captions based on audio tour scripts" (homepage).
- Client quotes (Platform page) name the "Tour Editor's CMS" and 24/7 editing; a client describes replacing a prior "bulky, expensive, difficult to maintain" audio tour system (USS Midway story) — evidence of the device-era lineage this Type digitizes.

## Cross-product Comparison

| Dimension | Bloomberg Connects | STQRY | Smartify | Guide-ID |
|---|---|---|---|---|
| Core content object | guide (institution's, in shared app) | tours/collections of stops; kiosk story layouts; device tours | guides over collection/exhibition content | audio tour of stops |
| Stop binding | works of art, objects, spaces | places/points of interest, exhibition elements | objects on display ("what's on display") | exhibit stops in a route |
| Narration/content media | audio, video, photography, text | audio, images, video, 360, AR | audio, video, AR, text | audio-first (device), captions/sign-language on mobile |
| Authoring | institution's team in vendor CMS | web-based builder (one builder → apps/kiosks/devices) | vendor CMS (+ content production service) | Tour Editor CMS |
| Visitor surfaces | visitors' own phones (shared app) | own phone (app/PWA/web), venue devices (Fleet), on-site touchscreens (Kiosk) | own phone (app/web, "no downloads"), on-site devices, consumer app | venue-issued dedicated device + mobile PWA |
| Spatial alignment | maps (indoor/outdoor) | GPS/POI maps, indoor maps, geofences, iBeacons | object recognition, numpad, search, QR | device pickup + stop codes (movement-triggered) |
| Multilingual | 50+ languages | 55+ languages | translations (AI-assisted) | 40+ languages |
| Accessibility | voiceover, captions/transcripts, zoom, font | voiceover, image descriptions | audio descriptions, sign-language tours | sign-language video, text captions (mobile) |
| Analytics/visitor data | real-time partner data | location traffic + click analytics | visitor behaviour insights | routes, stops, listening behaviour, device status |
| Engagement extras | curated editorial framing | quizzes, badges, push messaging | messaging, surveys | — |
| Commerce | none (philanthropy-funded) | in-app purchases, premium/code-locked content, sponsorship | premium/paid content, device rental | device/platform fees (B2B) |
| Admission/ticketing | absent | absent | absent | absent |
| Posture | shared multi-institution network app | white-label per institution (+ Guide/Marketplace shared surfaces) | both (partner platform + consumer app) | single institution (device fleet) |

## Canonical Abstraction

### L0 — Defining Invariant (candidate)

Three jointly-held structures. Remove any one and the product stops being recognizable as this Type:

1. **The institution-authored interpretive guide** — a persistent tour/guide assembled by the venue's own staff, composed of discrete stops/stories each bound to an exhibit, object, space, or point of interest in (or around) the venue. (Remove → a generic media/website builder or a content-production service; nothing "visits" anything.)
2. **The interpretive content carried by each stop** — narrated or otherwise interpretive media explaining/annotating what the visitor encounters; audio is the dominant and historically founding medium, with text/image/video as routine companions. (Remove → a wayfinding/map product or a label substitute with no interpretation.)
3. **The operated visitor consumption surface with per-stop access** — a surface the platform operates (visitor's own phone, venue-issued device, or on-site screen) through which a visitor reaches the right stop for what is in front of them — by code, scan, recognition, location, or browsing — before, during, or after the visit. (Remove → an authored content archive with no visitor-facing product; the platform collapses into its CMS or a design service.)

Jointly-held is load-bearing: 1+2 without 3 = a content archive/CMS; 1+3 without 2 = a map/label layer; 2+3 without 1 = generic audio/video publishing.

### L1 — Common Mature Structure (cross-product, layer B)

- Web-based authoring CMS with real-time publishing and content collaboration/permissions (Bloomberg CMS, STQRY builder, Guide-ID Tour Editor, Smartify CMS).
- Multiple tours/collections per institution, categorizable (STQRY explicit; Bloomberg/Smartify multi-guide; Guide-ID multiple tours).
- Multilingual delivery with translation tooling, increasingly AI/TTS-assisted narration (all four).
- Accessibility pack: voiceover/audio description, image descriptions/alt text, captions/transcripts, sign-language options (all four; sign-language named by Smartify and Guide-ID mobile).
- Maps and location awareness: outdoor map integration, indoor/custom maps, GPS + nearby points of interest (Bloomberg, STQRY).
- Location/object triggers: QR codes, number/codes (numpad), AI object recognition, search, geofenced alerts, iBeacons (STQRY, Smartify; Bloomberg implicitly via browse/maps).
- Rich media beyond audio: video, image galleries, 360, AR (STQRY, Smartify, Bloomberg).
- Visitor analytics: consumption, routes, stops, clicks, device status — partner-facing (all four).
- Venue-device fleet machinery when devices are loaned: provisioning, lockdown, charging, status monitoring (STQRY Fleet, Guide-ID).
- Engagement overlays: quizzes/games/badges, push messaging, surveys/messaging (STQRY, Smartify).

### L2 — Variant / Optional Structure

- Delivery philosophy: BYO-phone (app/PWA/web) vs venue-issued dedicated device vs on-site kiosk/touchscreen labels — one vendor may sell all three as separate product lines (STQRY), another stakes the brand on a dedicated device (Guide-ID), another on a shared free app (Bloomberg).
- Posture: white-label single-institution vs shared multi-institution network app vs both (Bloomberg = network; STQRY = white-label with shared Guide/Marketplace surfaces; Smartify = both).
- Business model: philanthropy-funded free (Bloomberg), SaaS subscription with plan tiers (STQRY), mixed with device rental and paid content (Smartify), hardware+platform (Guide-ID), free self-service (izi.TRAVEL, unverified).
- Commerce hooks: premium/code-unlocked content, in-app purchases, sponsorship, monetized tour marketplaces — content monetization, never admission.
- Collection-data connection: separate companion products digitize/publish collection records (STQRY Collect); content may import object data/images but no custody or cataloging machinery belongs to this Type.
- Visitor-relationship machinery: built-in messaging and surveys spanning before/during/after visit (Smartify) — present but not universal.
- Scope beyond museums: the same platforms serve heritage sites, gardens, cities, universities, tours — the museum is the anchor segment, not the boundary.
- Hardware accessories and services: content production, translations, audio production, bulk upload (STQRY services; Smartify content production).

### L3 — Vendor-specific (Research Notes only)

- Bloomberg Connects: cohort onboarding process (multi-week, peer cohorts, training/marketing support), nonprofit/civic eligibility policy, published scale stats (users/partners/countries).
- STQRY: plan tiers and per-device/per-kiosk license fees, App Concierge service, Studio AI tools (Connect/Translate/Voice), single-use download codes, driver mode for vehicles.
- Smartify: ISO 27001/Cyber Essentials posture, Smartify Originals content line, AAA-rated accessibility claim.
- Guide-ID: Podcatcher Pro device specifics (single-movement trigger, sticker codes), Demo Kit program, accessories line.
- Precise pricing numbers observed on STQRY pages are vendor-specific and deliberately not carried into the final document.

## Rejected Findings

- **"Audio guides are the Type"** — rejected as too narrow: the founding medium and still the norm, but the sampled products carry text/image/video/360/AR; the invariant is the interpretive content layer, with audio the dominant realization.
- **"Apps are the Type"** — rejected: Guide-ID's center is a dedicated non-phone device; STQRY Kiosk is an on-site touchscreen surface. The invariant is the operated consumption surface, not the phone.
- **"Museum-only"** — rejected: all sampled products serve the wider attraction/heritage/destination space; the directory leaf is the museum-anchored instance of the experience-layer pattern. The museum binding is the leaf's audience scope, not a structural invariant. (Kept as scope framing, not as an L0 leg.)
- **"AI object recognition is the modern trigger, so it's core"** — rejected: only one sampled product names it; QR, numpad codes, search, and location triggers are equally first-class; the keypad code entry of the device era is the same function. Trigger mechanism = implementation variable.
- **"Visitor analytics/CRM is definitional"** — rejected as L1: analytics are universal in the sample but a minimal product (printed-era analog, small audio-guide deployments) still satisfies the core without them; surveys/messaging is single-product-weighted (Smartify) and held optional.
- **"Guides must be curated by professional interpreters"** — rejected as role-detail: what matters is institution-authorship (venue's own team), not a specific job title.

## Boundary Findings

1. **vs Attraction Management System (§26) — DISCHARGES THE PRE-HUNG SIBLING-CLUSTER FLAG: independent Type, adjacent-complementary; NOT a slice or segment variant of the admission business.** Evidence: zero admission machinery in any sampled product — no admission products, no transactions issuing entry entitlements, no entry validation/redemption anywhere in four products' official material (Layer A, 4/4). Conversely the AMS sample's defining core (admission products → sale → entitlements → entry validation) is absent here, and the AMS document itself positions this leaf as "adjacent, complementary — visitor-facing interpretation and experience layer, not the admissions business." Removal tests both ways: remove the interpretive guide/consumption layer from an attraction platform → it remains an admission system (AMS passes); remove admission from a visitor-experience platform → it remains fully functional (this Type passes; commerce hooks like premium content are content monetization, not admission). The two Types share venues and sometimes vendors' target markets but have disjoint centers of gravity. The original AMS-pass hypothesis ("segment- or layer-variant of the admission-business Type") is CONFIRMED as an adjacent layer, i.e., an independent Type — the same resolution the family-entertainment-center pass reached for its leaf.
2. **vs Digital Collection Portal (§27): records-first public publishing vs experience-first interpretive layer.** The portal publishes collection-item records for discovery (the item record is the unit); this Type delivers interpretation aligned to the physical encounter (the stop/story is the unit). Clean complementarity: records governed/published there can feed stops here. Vendor-structural evidence: STQRY ships its collection publishing as a separate product line (Collect) beside the guide platform — the market itself splits the surfaces.
3. **vs Museum Collections Management / CMS family (§27): custody vs visitor experience.** The collections system is the object's system of record (accession, location, loans, condition); this Type holds no custody machinery and consumes imagery/stories at most. Clean seam; counterparty note from museum-collections-management discharged as expected-clean.
4. **vs Exhibition Planning / Installation / Logistics (§27 cluster): object/display workflows vs visitor-facing interpretation.** Those Types manage the display occasion and the objects; this Type addresses the visitor during/around the display. No shared record spine.
5. **vs Event Ticketing Platform / Event Mobile App (§26):** no performance/seat inventory here; an event app serves an event's attendees (agenda/logistics), while this Type serves a venue's standing interpretive layer. Museums commonly run admission on AMS-class platforms and interpretation here.
6. **vs generic website/app builders (§04.16) and CMS (§02.07):** generic builders lack the guide/tour object, the stop↔exhibit binding, venue-device operation, and spatial triggers; those are the structural discriminators, not styling.
7. **Within-Type form-factor split (device vs app vs kiosk) is a variant axis, not a Type boundary** — the same content model (stops, narration, per-stop access) is realized on all three; STQRY runs all three from one builder, Guide-ID pairs device with a mobile PWA.

## Historical / Market-Sample Check

- Device-era audio guides (keypad wand/handset systems — rented device, number-entry codes at exhibit labels, recorded narration per stop) satisfy all three L0 legs: authored tour of stops bound to exhibits, narration content, operated consumption surface with per-stop access. No apps, GPS, AI, cloud, or even kiosks required. In-sample corroboration: Guide-ID's positioning is the modern form of exactly this lineage, and a client story documents replacing a prior-generation device system (Layer A).
- Printed exhibition guides/gallery text sheets are the pre-digital ancestor of the interpretive layer but lack the operated consumption surface and per-stop access machinery (they are the content without the platform) — they bound the Type's lower edge rather than satisfying it. Analog radio/phone-based guide dials (dial-in number per stop) are a transitional form satisfying the legs conceptually.
- The definition therefore names no device type, no app, no AI, no recognition technology, no cloud, and no specific trigger mechanism.

## Uncertainties

- **izi.TRAVEL unreachable** (timeouts ×2): the free self-service platform pole is held at market-anchor level only; no claims about its operation are made. Its absence does not affect the L0, which is corroborated 4/4 on directly observed products.
- **Smartify depth**: partner-page evidence only (deeper pages 404). Claims about Smartify's CMS internals, surveys mechanics, or hardware are held at solution-axis level, not operational level.
- **Market naming**: no vendor in the sample uses the exact leaf label "Museum Visitor Experience Platform"; market vocabulary includes "digital experience platform for museums" (Smartify), "audio guide"/"tour" platforms (STQRY, Guide-ID), "digital guides" (Bloomberg). The directory leaf is read as the museum-anchored instance of this experience-layer Type; recorded as a naming note for the taxonomy owner.
- Whether some platforms bundle admission/ticketing as optional integrations could not be excluded beyond the sample (none observed in fetched material); the boundary claim is limited to "no admission machinery observed in the sample," not "impossible."
- Zoom/interactivity depth of in-gallery kiosk interactives (touch-game design) is vendor marketing territory; held at capability level.

## Final Synthesis

The Museum Visitor Experience Platform is the museum-operated interpretation layer of the visit: the institution's own team assembles guides — ordered or browsable sets of stops bound to exhibits, objects, spaces, and points of interest — carrying narrated (dominantly audio) interpretive media, and publishes them through a surface the platform operates: the visitor's own phone, museum-issued devices, or on-site screens, with per-stop access aligned to the physical encounter via codes, scans, recognition, location, or browsing. Everything else — languages, accessibility packs, maps and triggers, rich media, analytics, device fleets, quizzes, surveys, commerce hooks, multi-museum networks — is mature capability or variant, not definition. The Type's centers of gravity are disjoint from the admission business (§26 AMS), from collection-record publishing (§27 portal), and from custody systems (§27 collections family); its closest market kinship is with the wider attraction/heritage guide-platform space, of which the museum is the anchor segment.

Taxonomy verdict for the pre-hung flag: **independent Type** (adjacent, complementary to the admission-business Type) — keep the leaf.
