# Research Notes — Link-in-Bio Platform

Research date: **2026-09-08**

## Research Goal

Understand what a Link-in-Bio Platform actually is as an Application Type: its defining core structure, its standard capabilities, its variants, and its boundaries against neighboring Types (Landing Page Builder, Visual Website Builder, Social Profile Network, and the §27 creator-commerce cluster that surrounds it in the directory).

## Initial Boundary

Directory location: §27 Media, Entertainment, Creator & Culture (between UGC Creator Marketplace and Creator Storefront). Processed siblings with pre-hung seams that constrain this pass:

- **Creator Media Kit Builder** (processed): "the link-in-bio page faces the creator's own audience (fans); the media kit faces commercial counterparties" — reader-of-page is the discriminator.
- **Creator Storefront** (processed): "remove products/checkout → link-in-bio; keep them → storefront with a bio-link acquisition surface."
- **Digital Product Commerce Platform** (processed): "link-in-bio's defining object is the aggregated link profile; commerce may be attached… the defining object there is the product-with-deliverable and its purchase→delivery loop."
- **Creator Affiliate Dashboard** (processed): "link aggregation for social profiles; monetization optional. No program relationships, no commission records → not this Type, even when it carries affiliate links."
- **Landing Page Builder (§04.16, unprocessed)** and **Visual Website Builder (§04.16, unprocessed)**: expected seams on the no-code-page side.

Working hypothesis entering research: a self-service service that hosts a small personal page aggregating multiple outbound links, addressed by a stable URL placed in a social profile's link slot, with no-code assembly and click measurement.

## Research Questions

1. What is the defining object model — page, blocks, links? Is the link list the center?
2. How is the page addressed and distributed (username URL, social bio slot, QR)?
3. What does authoring look like (templates, themes, block editing, publish flow)?
4. What is the standard operating loop (create → share → measure → iterate)?
5. What analytics are standard vs plan-gated?
6. How far does commerce extend before the product becomes a different Type (storefront / digital-product / affiliate)?
7. Is "one page per identity" invariant, or does the market vary (multi-profile, multi-page)?
8. What states and rules matter (link visibility, pinning, scheduling, moderation, username disputes)?
9. Historical/market-sample check: would pre-Instagram personal hub pages (About.me era) satisfy the definition? Does the definition over-fit the Instagram one-link constraint?
10. Boundaries: vs landing page builder, website builder, profile network, shortener, bookmark manager, and the processed §27 siblings.

## Representative Products

Selected for market spread, product philosophy, and customer level:

| Product | Pole | Customer level | Docs reached |
|---|---|---|---|
| **Later (Linkin.bio)** | link-in-bio as a module of a social-media-management suite; page built around linked social posts | social media managers, brands, creators | Yes — Zendesk help center (Tier 1) |
| **Campsite.bio** | independent minimalist link-in-bio; link-type taxonomy | creators, small business, agencies (organizations) | Yes — Intercom help center (Tier 1) |
| **Taplink** | page-builder-heavy, mobile-first, commerce machinery inside the page | services, creators, small stores | Main site only (Tier 2); tutorials/FAQ URLs 404 |
| **Linktree** | category originator / market leader | consumer → enterprise | **Not reachable** (help center ×2, main site, archive) — limitations recorded below |
| **Beacons** | creator-economy suite with link-in-bio at the core | creator businesses | **Not reachable this pass** (403/transport); partially evidenced via the processed creator-media-kit pass |

## Sources

- Later Help Center — https://help.later.com/hc/en-us (root), Analyze & Engage category, Link in Bio section (19 articles listed): https://help.later.com/hc/en-us/sections/360007925473-Link-in-Bio
- Later — "What is Link in Bio?": https://help.later.com/hc/en-us/articles/4409203074967-What-is-Link-in-Bio
- Later — "Create a Link in Bio Page": https://help.later.com/hc/en-us/articles/360042743314-Create-a-Link-in-Bio-Page
- Taplink — product/site: https://taplink.cc/en/ (positioning, features, plans)
- Campsite.bio — product/site: https://campsite.bio/
- Campsite.bio Help Center — https://support.campsite.bio/en/
- Campsite — "Getting started with Campsite.bio": https://support.campsite.bio/en/articles/6818213-getting-started-with-campsite-bio
- Campsite — "How links work on Campsite.bio": https://support.campsite.bio/en/articles/7317946-how-links-work-on-campsite-bio
- Campsite — "Plan features": https://support.campsite.bio/en/articles/7922505-plan-features
- Cross-reference: research/creator-media-kit-builder.md (Beacons Link-in-Bio observations, fetched 2026-09-07 by that pass); boundary pre-hangs in research/creator-storefront.md, research/digital-product-commerce-platform.md, research/creator-affiliate-dashboard.md

### Source-access limitations

- **Linktree**: help.linktree.com transport error ×2; linktree.com and web.archive.org timed out. No Linktree-specific operational claims are made anywhere in this pass; Linktree is retained in Representative Products as the market-defining product, with its role asserted at market level only.
- **Beacons**: beacons.ai 403; docs.beacons.ai / faq.beacons.ai transport errors. Evidence limited to what the sibling media-kit pass documented on 2026-09-07 (its help-center fetches succeeded that day).
- **Milkshake**: milkshakeapp.com transport error (mobile-app-first pole left weakly evidenced).
- **Taplink**: marketing site reachable (Tier 2); tutorial/FAQ paths 404 — no Tier-1 operational detail asserted for Taplink.

## Product Observations

### Later (Linkin.bio) — evidence layer A (direct, official help center)

Positioning and purpose:

- "Link in Bio is like a mini-website built into your social profile… you can drive traffic to the most relevant products and pages."
- Core pitch: "No need to continually update the link in your bio… your Link in Bio page will show them exactly where to find products, sites, and more."
- Available to all Later users; paid tiers remove Later branding ("bannerless page") and add analytics depth.
- The product explicitly educates its own boundary: "Link in Bio is not the same as Instagram's product tagging feature. It does not tag your posts right on your Instagram profile."

Identity and addressing:

- "You can choose your own Link in Bio username (which forms your page URL) and change it once every 30 days."
- Dedicated article exists for "Link in Bio Username Availability & Dispute Process."
- Number of Link in Bio pages = number of Social Sets included in the plan (multi-page is plan-bound).

Page objects (documented as blocks):

- Profile: avatar (JPG/PNG; recommended 130×130), profile name (≤30 chars), bio (≤115 chars, no line breaks).
- Social links: dropdown of supported platforms + email; click counts visible; click-data window plan-gated (3 months free/starter; 1 year growth+).
- Buttons: text + destination URL; show/hide toggle; drag-to-reorder; color/shape/style/shadow customization.
- Linked social posts: a feed block of the user's Instagram/TikTok posts; links added to posts (single link per TikTok post; up to 5 links per Instagram post per the linked article); "clickable, shoppable feed."
- Featured media: most recent linked post enlarged, or a YouTube video, or custom media; "No Featured Media" option.
- Banners: "Featured Banner," "Multi-Item Banner" articles exist.
- Email collection: "Collect Emails With Link in Bio" article exists.

Page states and settings:

- "Make Page Private" toggle — page in an unpublished state while still editable.
- SEO data: custom title tag (≤70 chars) and meta description (≤160 chars) on paid plans, with search-preview.
- UTM parameters on links (paid).

Distribution loop (documented step-by-step):

- Copy the Linkin.bio URL from the management page (mobile share sheet → Copy Link) → open Instagram → Edit Profile → Links → Add external link → paste → optional title. Explicit note: "If you already have a website link on your Instagram profile page, replace it with your Link in Bio link."
- Placement guides exist for other platforms (TikTok article present).

Analytics:

- "Start Tracking… monitor your Link in Bio Analytics to track views and clicks."
- Plan-gated depth (article "Link in Bio Features By Plan").

Monetization-adjacent:

- "Add Mavely Affiliate Links to Link in Bio" — affiliate-link integration documented; commerce is otherwise outbound (links to products/pages).

### Campsite.bio — evidence layer A (direct, official help center)

Positioning:

- "A Link in Bio tool for Instagram, TikTok, and more… Convert more followers into customers with a link in bio tool created just for you."
- "Get a high conversion, mobile-optimized landing page setup in minutes."
- Use cases listed: agencies, creators/influencers, non-profits, organizations, small business, social media managers.

Core object — the link (documented "Link Anatomy"):

1. drag handle to reorder
2. editable fields: label + URL
3. optional image thumbnail
4. show/hide toggle ("The toggle is to show or hide your link from your profile")
5. type icon (opt-in form, image grid, feed, contact details…)
6. per-link actions: click stats, scheduling, pinning, and others

Link-level state rules:

- "My link isn't showing up on my profile — Make sure you've enabled your link."
- "Pinned links cannot be re-ordered."
- Archive links (plan feature); changes propagate with a stated 2–3 minute delay.

Link types (free): Divider, Title, Text, Carousel, Contact details, Request, Support/Tip Jar, Embed, Image grid.
Link types (Pro): Group, Form, Opt-in form, Feed.

Profile page objects:

- Profile photo (min 300×300), preset themes or custom themes (fonts, colors, backgrounds, button settings).
- Social accounts row at the bottom of the page.
- Profile QR code (free).
- Embed your profile on your website (free) — a documented distribution surface beyond social bios.
- Sensitive-content lock, age lock (free); code lock (Pro).
- Profile cover image (Pro).

Distribution loop:

- "Adding your Campsite link to any of the social media platforms you use… copy your Campsite URL" with per-platform placement articles (Instagram, Facebook Profile, Facebook Page, TikTok, Twitter).

Analytics (plan-gated):

- Free: 14 days of analytics — views, clicks, CTR, custom date ranges.
- Pro: 60 days — adds Reach, top links, top referrers, top events.
- Pro+: all-time storage, filters (referrer, country, device, UTM campaign), named reports (overview, channel, events, insights, tracking, leaderboard), CSV export.

Structure and collaboration:

- Pro: one profile (more at added cost); Pro+: six profiles, four collaborators.
- Organizations: "manage your team members and their access to your profiles… all under a single invoice" — agency posture.
- Marketing plumbing (Pro): meta tags customization, UTM parameters, Google Tag Manager/Analytics, TikTok/Facebook/Pinterest/Google Ads pixels, weekly insights email.
- Link scheduling (Pro); highlight a link; bulk link editing; "Make My Bio Link Wizard."
- Era-typical extras documented: MCP connection ("Connect Claude to your Campsite.bio account (MCP)"); image design via Canva integration article.

### Taplink — evidence layer B→A- (official product site, Tier 2; operational docs not reached)

Positioning:

- "More Than Just Link In Bio Tool — create a mobile-friendly website in a few clicks and share it in your bio."
- Names the category trigger itself: "All social networks have limitations. The Instagram BIO is limited to 150 characters… Instagram and other social networks allow posting only 1 link in a profile. With Taplink you can place any number of links."
- "Create a micro-landing page, that tells your audience about you and your product."
- Audience segments marketed: services (book/pay on the page), creators & influencers, goods & stores ("online store in 20 minutes"), everyone (freelancers, artists).

Structure/features claimed:

- Unlimited links; text and FAQ blocks; custom blocks; images/videos/music; price lists.
- Smart links to messaging apps (open a conversation in one tap) and to social network apps.
- Forms; payment acceptance "via any popular payment system"; digital products (Business plan); internal pages ("If one page is not enough… create as many pages as needed"); countdown timer; scheduled display of blocks (Pro); custom HTML (Pro).
- Design: "one of 300 ready-to-use templates or… unique design"; examples addressed as taplink.cc/<username>.
- Stats: page views on free; clicks analytics on Pro.
- Business machinery: CRM, automated emails, lead and payment notifications, export leads to popular CRMs.
- Other: shared access, QR code, custom domain + SSL (Business), marketing add-ons, social media pixel support (Pro).

### Linktree — evidence layer: none (unreachable)

No operational evidence obtained. Market role (category originator, most widely recognized product) is common knowledge but is deliberately not converted into product-specific claims.

### Beacons — evidence via sibling pass only

From the processed creator-media-kit pass (its own 2026-09-07 fetches of Beacons' help center): Beacons ships Link-in-Bio as its flagship product; the media kit "lives inside your existing [Beacons Link-in-Bio] page"; the account couples page + store + brand-deal surfaces. Used here only to corroborate the suite-embedded variant, not for link-in-bio operational specifics.

## Cross-product Comparison

| Dimension | Later Linkin.bio | Campsite.bio | Taplink |
|---|---|---|---|
| Self-description | "mini-website built into your social profile" | "mobile-optimized landing page" / "your space on the web" | "mobile-friendly website… micro-landing page" |
| Addressing | username forms the page URL; rename throttled (30 days); dispute process | campsite.bio/username; subdomain + custom domain paid | taplink.cc/username; custom domain (Business) |
| Primary content unit | blocks incl. buttons + linked social posts feed | ordered link list with typed links | blocks incl. links, text, media, price lists |
| Link object | text + URL + show toggle + order | label + URL + thumbnail + show/hide toggle + type + stats/schedule/pin/archive actions | link blocks (label/URL), "smart" deep links |
| Profile header | avatar + name + bio (char limits documented) | profile photo + theme | page header content |
| Publish model | edit in management page; private/unpublished toggle | enable toggle per link; ~2–3 min propagation; archive | edit and publish on hosted page |
| Themes/design | premade themes, custom colors, button styles | preset + fully custom themes (fonts/colors/backgrounds) | 300+ templates, custom design |
| Social icon row | yes (dropdown + email) | yes (bottom of page) | yes ("social networks" smart links) |
| Analytics | views + clicks; plan-gated depth; UTM | views, clicks, CTR (+Reach, top links/referrers, filters, export at higher tiers); windowed storage | page views (free), clicks analytics (Pro) |
| Email capture | yes (dedicated feature) | opt-in form link (Pro) | forms + automated emails + CRM (Business) |
| Commerce | outbound only (+affiliate links via Mavely) | outbound only (Tip/Support link type) | payments + digital products + price lists on-page (Business) |
| Multi-page | page count = plan Social Sets (few) | one profile default; extra profiles paid; no multi-page single-profile model claimed | internal pages: multi-page supported |
| Post-grid of social feed | yes — defining feature of its page | image grid / feed link types (sync IG posts) | not central |
| Collaboration | plan Social Sets imply team structure | collaborators (Pro+); Organizations for agencies | shared access |
| Beyond-social distribution | — | embed profile on a website; QR code | QR code |
| Moderation/trust surfaces | username dispute process | sensitive-content lock, age lock, code lock; content rules | content rules page; report violation |

Stable across all three (evidence layer B): hosted micro-page at a stable username-addressed URL; ordered block/link stack as primary content; no-code assembly with themes; profile header; social links row; link-level show/hide + reorder; click/view measurement; bio-slot distribution loop; branding/domain removal as paid upgrades; creators + small business as core users, agencies/teams as an extension.

## Canonical Model

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being recognizable as this Type:

1. **The hosted micro-page of record** — one public page per identity (a single scrolling page in the typical case), served by the platform at a stable address, commonly a username URL on the platform's domain (custom domain as an upgrade). Remove → a website builder (multi-page sites, unstable/own addressing) or a link shortener (no page at all).
2. **Link-aggregation content model** — the page's content is an ordered stack of blocks whose primary and defining unit is the tappable outbound link (label → destination URL), not authored content, a catalog, or a feed. Remove → blog / personal homepage / social profile.
3. **No-code tool-owned assembly and instant hosting** — the owner composes the page from tool-provided blocks and themes and publishes to the live URL with no engineering and no separate deployment step. Remove → a hand-built personal website (the pre-history).
4. **Profile-slot distribution posture** — the page is built to occupy the single external-link slot of a social profile (or an equivalent personal surface: email signature, QR, embedded tile), so that one URL channels the profile's existing audience to all of the owner's destinations. Remove → a campaign landing page builder, which distributes via ads/SEO against conversion goals.

Jointly-held is load-bearing: (1+2 without 3) = a hand-maintained links page; (2+3 without 4) = a generic landing/post tool; (1+3 without 2) = a profile/bio page with nothing to aggregate; (3+4 without 1+2) = a URL shortener with bio marketing.

### Historical / market-sample check (per §24 discipline)

- Pre-Instagram personal hub pages (About.me-era single personal pages: bio + photo + links, username URL, template-assembled, parked in profiles/signatures) satisfy all four legs. The category name ("link in bio") comes from the modern one-link-per-profile constraint of platforms like Instagram — which Taplink itself names as the trigger — but the constraint is the *trigger*, not the *definition*. The canonical posture is "one stable personal URL aggregating all destinations, placed where a profile allows," which predates and outlives any specific platform's rule set.
- The definition does not require: Instagram specifically, any particular social platform, click analytics (L1), commerce blocks (L2), a post-grid of social content (L2), mobile-app-only authoring (L2), or one-page-per-account rigidity (L2).
- A purely analog pre-history is thin (the Type is web-native by nature); the closest analog form is a printed "all my links" card/QR or a business's link directory page — it satisfies legs 1–3 and the distribution leg in weakened form. The web-native About.me generation is the accepted historical anchor.

### L1 — Common Mature Structure (evidence layer B, 3/3 sample)

- Profile header: avatar/photo, display name, short bio text.
- Theme/template system with customization (colors, fonts, backgrounds, button styles); hide-platform-branding and custom domain as paid upgrades.
- Social icon links row (other profiles + email contact).
- Per-link engagement analytics (clicks; page views; CTR commonly) with plan-gated depth, windows, filters, export.
- Link-level controls: show/hide toggle, drag reorder, pinning, archiving; some products: per-link scheduling/rotation.
- QR code for the page URL.
- Email capture (dedicated feature or opt-in block).
- Media/mention blocks beyond bare links: embedded media, featured items, social-post grids/feeds, messaging deep links.
- Marketing plumbing: UTM parameters, ad/analytics pixels, meta tags/SEO fields.
- Collaboration/multi-profile: additional profiles or pages, collaborators, organization/workspace management for agencies and teams.
- Trust/moderation surfaces: content rules, username disputes, sensitive-content/age gates.

### L2 — Variant / Optional Structure

- **Suite posture**: standalone product ↔ module inside a social-media-management suite (Later) ↔ core of a creator-economy suite (Beacons) ↔ commerce-forward page platform (Taplink).
- **Page shape**: single page ↔ multi-page (internal pages) ↔ multi-profile management as the growth path.
- **Content philosophy**: pure ordered link list ↔ post-grid mirroring the user's social feed ↔ page-builder-heavy blocks.
- **Commerce depth**: outbound links only ↔ tip/support link ↔ on-page payments/digital products (where the seam toward commerce Types is approached — see Boundary Findings).
- **Authoring surface**: web admin ↔ mobile-app-first ↔ both.
- **Locks/gating**: sensitive content, age gate, code lock.
- **Affiliate support**: native affiliate-link integrations.
- **Secondary distribution**: embed the page on an external website.

### L3 — Vendor-specific (research notes only; not promoted)

- Later: username change throttled to once per 30 days; up to 5 links per Instagram post (TikTok posts one); page count tied to Social Sets; bio length ≤115 chars, name ≤30 chars; click-data windows by plan (3 mo free / 1 yr growth); "bannerless" paid page.
- Campsite: analytics storage windows (14d/60d/all-time); free image grid limited to 12 images with manual sync vs Pro auto-sync each minute; one profile on Pro, six on Pro+, four collaborators; pinned links not reorderable; 2–3 minute propagation delay; named Pro+ reports; MCP (Claude) connection; Canva image-design article; weekly insights email.
- Taplink: 300+ templates; "30+ tools"; Basic/Pro/Business plan ladder with payments/CRM/digital products on Business; example pages taplink.cc/<name>.
- Linktree: no evidence obtained this pass; nothing asserted.

## Vendor-specific Findings

(See L3 — all retained here; none promoted to the canonical document.)

## Rejected Findings (considered and not promoted)

- **"This Type = solving Instagram's one-link rule"** — rejected as definition: the constraint is the category's historical trigger (named by Taplink itself) but the canonical posture is the stable aggregated personal URL for any profile-like surface; pre-Instagram hub pages fit the core.
- **"Commerce/payments are part of the Type"** — rejected: two of three sampled products keep commerce outbound; Taplink's on-page payments/digital products are the heavy pole and approach commerce Types. Commerce depth is L2.
- **"The page must mirror the user's social posts"** — rejected: that is Later's post-grid philosophy; Campsite/Taplink pages are link-stack-first. L2 variant.
- **"One page per account is invariant"** — rejected: Later ties page count to plan units; Campsite sells additional profiles; Taplink supports internal pages. The invariant is the stable addressable page, not the count. L2.
- **"Mobile-app authoring is definitional"** — rejected: web admin dominates the sample; mobile-app-only (Milkshake pole) could not be verified. L2.
- **"Analytics are definitional"** — considered and placed in L1: every sampled product ships click/view measurement at every tier, but a page without stats would still be recognized as this Type; measurement is the standard operating loop, not the defining structure.

## Boundary Findings

### vs Landing Page Builder (§04.16, unprocessed)

Closest no-code-page neighbor. Shared: hosted no-code pages, templates, tracking pixels, UTM. Different: (a) content model — aggregation of many outbound links vs a single conversion goal (form/signup/purchase); (b) distribution — the profile's link slot and the owner's existing audience vs ads/SEO/campaign traffic; (c) binding — page anchored to a personal identity/username vs a campaign or brand property. Diagnostic: remove the profile-slot posture and multi-destination aggregation → Landing Page Builder. **Flagged for joint review when §04.16 is processed** (recorded in STATUS.md).

### vs Visual Website Builder / Blogging Platform (§04.16/§02.07)

Website builders and blogs produce content-first, multi-page sites with arbitrary layout and their own navigation. The link-in-bio page is a constrained, single-scroll, link-first micro-page. Taplink's "mobile-friendly website" language shows the straddle pressure; its page-builder blocks are the same family of machinery, but the constrained aggregation shape is what holds the Type.

### vs Social Profile Network (§01.05)

No follow graph, no feed, no discovery, no network. The page is a destination; its readers arrive from an external profile. A profile page inside a social network is the property of the network; the link-in-bio page is the owner's cross-platform aggregate.

### vs URL/link shortener utility

A shortener wraps one destination for measurement; the link-in-bio page is itself the destination aggregating many. Some shorteners offer link pages — the seam is the page+blocks model, not the redirect.

### vs Bookmark Manager (§02.13)

Bookmark managers aggregate links privately for the person; the link-in-bio page publishes selected destinations publicly for the person's audience. Different reader, different visibility model.

### vs processed §27 siblings (pre-hung seams honored)

- **Creator Media Kit Builder**: reader of the page — fans/audience → this Type; brands/commercial counterparties → media kit. One account can host both (documented in the Beacons suite).
- **Creator Storefront**: products + platform-hosted checkout + fulfillment → storefront; a bio link *to* a storefront is this Type's distribution loop feeding the storefront's.
- **Digital Product Commerce Platform**: product-with-deliverable + purchase→automated-delivery loop → that Type; linking out to such a shop → this Type.
- **Creator Affiliate Dashboard**: program enrollment + tracked creator assets + commission ledger → that Type; an affiliate link as one entry on the page → still this Type.
- **Tip/support**: a tip-jar link type exists (Campsite) but tips-as-product (Creator Tip Platform) are not the defining object here.

### "去掉什么就变成另一个 Type" tests

- Remove link aggregation (page becomes content-first) → personal website/blog/profile page.
- Remove the profile-slot distribution posture → Landing Page Builder.
- Remove no-code hosting (hand-built page) → personal homepage (the pre-history).
- Remove the page (wrap a single destination) → URL shortener.
- Add catalog + checkout + fulfillment → Creator Storefront / Digital Product Commerce.
- Add program enrollment + commission ledger → Creator Affiliate Dashboard.
- Add follow/discovery/feed → Social Profile Network.

### Taxonomy observation

The Type is legitimate and distinct. Two notes for the record: (1) the market increasingly ships this Type as a module of larger suites (SMM platforms, creator-commerce suites) rather than only standalone — the Type is defined by the surface, not the packaging; (2) the seam vs Landing Page Builder (§04.16, unprocessed) should be jointly reviewed when that leaf is processed; the diagnostic above is proposed as the seam.

## Uncertainties

1. **Linktree unreachable** — the category leader's operational specifics are unverified; market-level claims only.
2. **Beacons unreachable this pass** — suite-posture evidence borrowed from the sibling pass's successful fetches; no independent operational detail.
3. **Milkshake unreachable** — the mobile-app-only authoring pole is asserted only as a market position, not documented.
4. **Taplink operational depth** (publish mechanics, per-block behavior, plan limits) — not verified beyond the product site; no precise Taplink claims in the final doc.
5. Free-tier profile counts and several numeric limits across products are unknown; none asserted.
6. Whether "single scrolling page" holds for every product (Taplink multi-page is the counter-pole) — handled as L2 variance, single-page held as the typical shape, not an invariant.
7. Historical breadth: About.me-generation anchor is reasoned from the market sample and category naming, not from a fetched primary source (its sites were not fetched this pass).

## Final Synthesis

A **Link-in-Bio Platform** is a self-service web application that lets an individual publish, without code, a single stable-addressed public micro-page whose content is an ordered stack of blocks dominated by tappable outbound links — the page intended to occupy the external-link slot of the person's social profile so that one URL carries the profile's audience to all of their destinations — with the platform hosting the page and, as the standard operating loop, measuring the page's views and each link's engagement so the owner can rearrange, add, retire, and re-point destinations over time.

Around this core, mature products add a profile header, themes and branding controls, social icon rows, per-link state controls (hide, pin, archive, schedule), QR codes, email capture, media and social-feed blocks, UTM/pixel plumbing, plan-gated analytics depth and export, multi-profile/collaboration for teams and agencies, and trust surfaces (content rules, username disputes, content locks). Variants span standalone products, modules inside SMM suites, and cores of creator-economy suites; single-page vs multi-page; link-list vs post-grid vs page-builder-heavy; outbound-only vs on-page commerce. The seams that matter: reader-of-page (fans → this Type; brands → media kit), transaction machinery (present → commerce Types; absent → here), program attribution (present → affiliate dashboard; absent → here), and distribution posture (profile slot → here; campaigns/ads → landing page builder).
