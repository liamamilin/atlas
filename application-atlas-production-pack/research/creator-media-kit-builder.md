# Research Notes — Creator Media Kit Builder

Research date: 2026-09-07
Slug: creator-media-kit-builder
Directory leaf: Creator Media Kit Builder (§27 Media, Entertainment, Creator & Culture)

---

## Research Goal

Understand what a Creator Media Kit Builder actually is as an application: what artifact it produces, for whom, what content model it enforces, what the tool owns vs. what the user owns, how the finished kit is distributed and controlled, and where its boundaries lie against neighboring creator-economy and document-authoring Types.

## Initial Boundary

Working hypothesis before research:

- A "media kit" in the creator economy is a self-promotional document a creator (influencer, YouTuber, podcaster, streamer, musician, freelancer) sends to brands, agencies, and industry professionals to pitch themselves for paid collaborations (sponsorships, UGC deals, bookings, press coverage).
- A Creator Media Kit Builder is an authoring application that helps a creator assemble this document — typically template-based, increasingly with auto-synced platform stats.
- Nearest neighbors suspected: Resume Builder (same authoring family, different domain), Link-in-Bio Platform (audience-facing vs. brand-facing), Creator Sponsorship Management (deal workflow vs. pitch artifact), Influencer Marketing Platform (§06, brand-side), Brand Asset / Guideline Platform (§06, organization-side "media kit" in the press/rate-card sense), portfolio builders.
- Key ambiguity: does the musician "electronic press kit" (EPK) belong to this Type or is it a sibling? Does a general design tool with media-kit templates (Canva/Visme pole) count as this Type?

## Research Questions

1. What is the media kit artifact in each product — web page, PDF, both? Who is the stated reader?
2. What content model do builders enforce? Which sections are standard (identity/bio, audience stats, demographics, performance, content examples, past collaborations, services, rates, contact)?
3. How is content produced: manual entry, auto-sync from connected social accounts, AI generation?
4. What does the tool own (templates, layout, rendering) vs. the user (content, branding)?
5. How is the finished kit distributed (shareable link, PDF download, embed) and access-controlled (password, gating)?
6. What adjacent machinery exists (brand-deal inbox, outreach AI, pricing calculator, invoicing) and where is the seam?
7. Does the musician EPK fit the same Type or a sibling?
8. Historical check: pre-auto-sync media kits (static PDF templates, physical press kits) — do they still fit the same definition?

## Representative Products

Selected for market representativeness, documentation quality, and distinct product philosophies / customer tiers:

1. **Beacons** (beacons.ai) — creator-economy native platform; Media Kit is a flagship product inside a Link-in-Bio + Brand Collabs suite; auto-synced stats; free consumer entry. Deepest documentation found (dedicated help-center subcategory).
2. **Bandzoogle** (bandzoogle.com) — musician website platform with a dedicated EPK / press-kit builder; represents the older press-kit heritage and the "artifact as page of a professional site" philosophy.
3. **Visme** (visme.co) — general business design/document tool with a dedicated "Media Kit Maker"; represents the design-tool pole and the broader (organization + influencer) PR usage of the same artifact family.
4. **Canva** — design-platform template pole; **unreachable** (site blocks non-browser clients; 2 attempts). Characterized only via Beacons' official description of the "static template" path.
5. **Linktree** — link-in-bio pole; **unreachable** (2 timeouts). No claims made.

## Sources

Tier-1 (official operational documentation / product pages), all fetched 2026-09-07:

- Beacons Help Center — Brand Collabs 💸 → Media Kit 📺 category: https://help.beacons.ai/en/categories/1088065-brand-collabs-💸
  - "Why do I need a Media Kit?" — https://help.beacons.ai/en/articles/4704129
  - "How to Create your Media Kit" — https://help.beacons.ai/en/articles/4703937
  - "Media Kit - Header Block" — https://help.beacons.ai/en/articles/4704001
  - "Connect your Socials to your Media Kit" — https://help.beacons.ai/en/articles/4704257
  - "Customize the Design of my Media Kit" — https://help.beacons.ai/en/articles/4704385
  - "Media Kit Permissions" — https://help.beacons.ai/en/articles/4705345
  - "Brand/Sponsorship Outreach 101" — https://help.beacons.ai/en/articles/4704321
  - Category listing also shows: "Media Kit Contact Form" (4704513), "Disconnect your Socials" (4704449), "Brand Partnerships" (4704193), "Analytics - Media Kits" (4704897), "Brand Deal Profile" (4704833), "Pricing Calculator" (4704705), "AI Brand Outreach" (4704641), "Invoicing" (4704577), "W-9 Generator" (4704769)
- Bandzoogle — EPK feature page: https://www.bandzoogle.com/features/epk (plus https://www.bandzoogle.com/features)
- Visme — Media Kit Maker product page: https://www.visme.co/media-kit-maker/

Unreachable / limitations:

- Canva (www.canva.com) — returns "unsupported client" block page to the fetcher (2 attempts: /create/media-kits/, /help/media-kit/). Not directly evidenced; characterized only through Beacons' official article, which names Canva (with Google Slides, Notion) as the from-scratch template path requiring manual stat updates.
- Linktree (linktree.com) — request timeouts (2 attempts). No claims.
- Beacons root site (beacons.ai) — 403; help center fully reachable, so product evidence is Tier-1 help-center documentation.

---

## Product A — Beacons (creator-economy native pole)

### Key observations (Evidence layer A — official help center)

**Definition given by the vendor:**
- "A media kit is a one-page digital resume that shows brands your audience, engagement, and past partnerships in one place, so they can decide whether to work with you in under a minute."
- "A media kit is a digital portfolio that tells brands what they need to know about you and why they should work with you. It's your pitch."
- Media kits highlight: who you are as a creator; analytics and stats from your social accounts; your rates; details on past brand partnerships.

**The brand-expected section table (vendor-published content model):**

| Section | What it covers |
|---|---|
| Intro / Bio | who you are, your niche, your content style |
| Audience | follower counts, demographics, top locations across platforms |
| Performance | engagement rate, average views, reach |
| Content examples | pieces representing best work |
| Past brand work | logos, testimonials, results from previous collaborations |
| Rates / services | what you offer and, optionally, pricing |
| Contact | how a brand reaches you or requests a deal |

**Creation flow:** account → Brand Collab menu → Media Kit; unlocking the kit requires connecting at least ONE social media account; then customize.

**Stats auto-sync:** connect Instagram, TikTok, YouTube, Twitch (also Snapchat per a separate article); stats refresh automatically once connected; additional platforms (LinkedIn, Apple Music, "many more") can be added manually to a "Total Followers" figure; X (Twitter)/Facebook not supported as integrations at time of writing (Nov 2025 edit).

**Header block content:** profile image, display name, pronouns, location, "About You", content categories ("What best describes you? examples: finance, tech, dancing, food").

**Design ownership:** tool-owned layout; user customizes cover image (upload or Unsplash search), colors (presets + color picker), layout, font. "Show or hide specific stats."

**Distribution & access:**
- Shareable as one link (email, DM, application form).
- Media Kit Permissions: General Access toggle (anyone with the link can view) + opt-in to "share it with relevant opportunities in our network" (marketplace distribution).
- 5 locking options: Unlocked / Email gate (visitor submits email; collected emails viewable) / Brand Deal Offer gate (visitor submits a brand deal request) / Password / Approved access (approved accounts only; requests emailed to creator).
- Custom domain for the media kit is a paid (Pro) feature; core kit free.

**Usage workflow (outreach article):** send the kit link by email, brand contact/partnership forms, brand social DMs, LinkedIn messages, agencies, creator peers; templates for creator-sent and manager-sent pitches; follow-up cadence advice; kit used in rate negotiations ("back that up with specifics: engagement rates, demographics, past collaborations with real numbers").

**Adjacent machinery in the same suite (seam markers):** Brand Deal Profile (structured profile for brand partnership applications), AI Brand Outreach (personalized pitch emails), Pricing Calculator (what to charge brands), Invoicing, W-9 Generator, Media Kit view analytics (views over 1/3/7/30 days/all, with a vendor disclaimer about data discrepancies).

**Explicit positioning vs. the design-tool path:** "Unlike a static PDF, slide deck, or Canva template, Beacons builds yours directly inside your existing Link-in-Bio page and pulls live stats from your connected social accounts, so you're not manually re-exporting a new version every time your following changes." Also: "If you're building one from scratch: tools like Canva, Google Slides, or Notion offer free templates, but you'll need to manually update your stats yourself every time they change."

**Rates optional:** "Does a media kit need to include pricing? No — many creators leave rates out so they can tailor a quote to the specific campaign, usage rights, and deliverables instead."

**Product-specific constraint:** the media kit requires a Beacons Link-in-Bio account ("the media kit is part of your Beacons account and lives inside your existing page").

## Product B — Bandzoogle EPK (musician press-kit heritage pole)

### Key observations (Evidence layer A — official product page + FAQ)

**Definition given by the vendor:**
- EPK = "electronic press kit"; historically a physical package (photos, bio, CD) distributed to music industry professionals; the EPK is its electronic version.
- "An EPK is a Onesheet page, website or digital file used by musicians to promote their music. Similar to a portfolio or resume, it allows musicians to provide their essential information to industry professionals—music bookers, venues, journalists, bloggers, playlist curators, labels, managers, radio programmers and more—in one convenient package."
- Purpose: "Get more gig bookings, press, and playlist placements."

**Reader:** industry professionals (bookers, venues, journalists, playlisters, labels, managers, radio programmers) — commercial/institutional decision-makers, not fans.

**Assembly:** templates ("free EPK templates") + "no-code visual design editor. Easily drop in your text and media content, and rearrange it"; preset "Onesheet layouts" for three named purposes: booking and advancing shows (talent buyers/venues), promoting to press and media (journalists, playlisters, radio), pitching to industry pros (labels, management, publishers).

**Content blocks (the EPK content model):** music player (singles/albums/playlists), images (single/gallery/slideshow), contact form ("for industry pros to reach you directly by email"), text bio (long-form), press quotes (testimonials, incl. a GigSalad reviews integration), embedded videos (YouTube/Vimeo), gig calendar (incl. Bandsintown integration), social media links, download links (MP3s, high-res images, riders).

**Distribution:** hosted online with shareable URL or custom domain; optional password protection; "When you need to send a PDF version, download your Onesheet EPK as a file in one click."

**Relationship to the website:** "Start with a Onesheet, grow to a website" — plans allow a single-page EPK (low-cost plan) up to a multi-page website; "some musicians choose to create a full website to use as their EPK"; EPK can be a standalone page, a page within a larger website, or an offline PDF.

**What an EPK should include (vendor FAQ):** sampling of best work — music in a player, short bio, professional photos and album art, embedded videos, summary of recent achievements and reviews, social and streaming links, contact information; "other specific content depending on who you're sending it to and why."

**Notable absence:** no follower-count / demographics auto-sync machinery anywhere in the EPK documentation. Audience evidence in the music-industry form is work samples + achievements + reviews, not platform stats.

## Product C — Visme (general design/business-document pole)

### Key observations (Evidence layer A — official product page)

**Positioning:** "Professional Media Kit Maker for Promoting Your Brand" — lives under the Documents product; "perfect for PR exposure, influencer outreach or any of your custom media kit needs."

**Stated users/purpose:** "A media kit is an essential PR tool for organizations, brands and influencers to share their message... They can help you get mentioned in publications, create collaborations with other brands, collaborate with influencers and more." Note the broader-than-creator audience: organizations and brands make media kits too (company/PR kits).

**Assembly:** pre-designed media kit / "electronic press kit" templates, fully customizable; drag-and-drop editor "made with the non-designer in mind"; brand fonts and colors (Brand Kit integration, paid plan); stock photos, icons, animated illustrations; data widgets & tables ("insert brand accolades... visualize numbers, statistics and your expertise").

**Workflow (vendor's 5 steps):** log in → Documents tab → Media Press Kit icon → pick template → customize colors/fonts/illustrations → "Add your social media and any specific contact information" → download as PDF to print or email to potential partners.

**Distribution:** download as PDF or JPG; generate a shareable link; embed on a landing page/website; print for physical copies.

**Notable absence:** no social-account stat auto-sync; no gating/access machinery; no creator-specific section semantics (the content model is generic template content: text boxes, visuals, data widgets).

## Product D — Canva (design-platform template pole) — UNREACHABLE

- www.canva.com blocks the research fetcher ("unsupported client" interstitial) on both attempted URLs (2 attempts). Per source-access rules, no product claims are made.
- Indirect characterization (Evidence layer B, via Beacons' official article): Canva is named as the canonical "build one from scratch with a design tool" path — free templates, static output, manual stat updates. This positions the design-tool pole as: template + manual content + manual re-export; no stat sync, no gating, no brand-deal machinery.

## Product E — Linktree — UNREACHABLE

- Two request timeouts. No claims made. The link-in-bio pole's media-kit features remain unverified in this pass.

---

## Cross-product Comparison

| Dimension | Beacons | Bandzoogle EPK | Visme |
|---|---|---|---|
| Artifact form | web page (one-page "digital resume") inside the creator's link-in-bio account; shareable link | hosted web page (Onesheet or multi-page) + one-click PDF of the Onesheet | multi-page document; PDF/JPG download + shareable link + embed |
| Stated reader | brands (decide "in under a minute") | industry professionals (bookers, venues, journalists, labels, playlisters) | organizations, brands, influencers; PR / influencer outreach |
| Content model | header (name/pronouns/location/categories), audience stats, performance, content examples, past brand work, rates/services (optional), contact form | bio, music player, images, videos, press quotes, gig calendar, social/streaming links, asset download links, contact form | template-defined sections; text, visuals, data widgets; social + contact info |
| Content production | auto-sync from connected socials + manual entries + manual platform adds | fully manual | fully manual |
| Design ownership | tool-owned layout; user sets cover/colors/layout/font; show/hide stats | tool-owned templates + no-code editor; user drops and rearranges blocks | tool-owned templates + drag-and-drop; brand fonts/colors |
| Access control | open / email gate / brand-deal-request gate / password / approved accounts; network-sharing opt-in | open or password-protected URL | none documented |
| Stats semantics | central (follower counts, demographics, engagement, reach; auto-updating) | absent (work samples + achievements instead) | generic data widgets (manual) |
| Rates/pricing | optional section + pricing calculator (adjacent tool) | not part of EPK model | not documented |
| Kit-view analytics | documented (views over selectable windows) | not documented for EPK | not documented |
| Adjacent machinery | brand-deal inbox/profile, AI outreach, invoicing, W-9, link-in-bio, store, email | full musician website/store/tour/mailing-list platform | full design suite, brand kit, AI tools |

### What is shared (candidate common structure)

1. A single self-promotional document artifact — the media kit — whose reader is an external commercial decision-maker (brand, agency, booker, journalist, label), never the creator's own audience.
2. A pitch-shaped content model organized around: who the creator is (identity/niche), the reach/audience or work evidence they bring, what they offer (services; rates optional), past work/social proof, and how to make contact.
3. Tool-owned assembly: the application supplies templates/layout/rendering; the user supplies and arranges content; no manual page-layout engineering.
4. A finished distributable output: a shareable hosted page and/or a downloadable file (PDF), sent by email/DM/form.
5. Branding controls (colors, fonts, imagery) so the kit matches the creator's identity.
6. Contact capture aimed at the commercial reader (contact form or contact info).

### What varies (implementation / segment)

- Stats auto-sync from connected platforms (Beacons only in this sample; explicitly the differentiator Beacons claims vs. the static-template path).
- Access gating beyond a password (email gate, deal-request gate, approved accounts — Beacons).
- Marketplace/network distribution of the kit (Beacons opt-in).
- PDF export (Bandzoogle, Visme documented; not evidenced for Beacons).
- Artifact hosting shape: standalone page vs. page-inside-platform vs. file.
- Industry content vocabulary: influencer stats vs. music EPK blocks vs. generic PR kit.
- Rates presentation and pricing guidance.

---

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

A Creator Media Kit Builder is a creator-facing authoring application whose defining structure is:

1. **The media kit artifact** — one self-promotional document whose reader is an external commercial decision-maker (brand, agency, or industry professional) evaluating the creator for a commercial relationship. Not the creator's own audience; not a private working document.
2. **A commercial-pitch content model** — the kit's content is organized around the creator's identity/niche, their reach or audience evidence, work samples and past-collaboration proof, their offer (services, optionally rates), and how to make contact. The pitch orientation is invariant; the exact section vocabulary varies by industry form.
3. **Tool-owned assembly and rendering** — the builder supplies templates and layout; the creator supplies, curates, and arranges content; the tool renders the finished document.
4. **A finished distributable artifact** — the output is a shareable hosted page and/or a downloadable file that the creator sends to commercial counterparties.

Remove the external commercial reader → it becomes a link-in-bio page or fan-facing profile (different Type). Remove the pitch content model → it is a generic document/design editor. Remove tool-owned assembly → it is advice or a blank design canvas, not a builder. Remove distribution → the pitch never reaches its reader.

### L1 — Common Mature Structure

Present in most mature products, not required for the definition:

- template gallery with industry-appropriate designs
- section/block model with show/hide, add/remove, rearrange
- branding controls (cover image, colors, fonts, logo)
- contact/booking capture (form or contact details)
- content-example gallery (images, embedded video, music players in the EPK form)
- past-collaboration / testimonial / press-quote section
- social and streaming profile links
- shareable link and/or PDF export
- password protection of the hosted page (documented at two of three sampled products)
- kit-view analytics (documented at one product; treat as common-trending, not universal)

### L2 — Variant / Optional Structure

- **Stats auto-sync** from connected social platforms (Instagram/TikTok/YouTube/Twitch/Snapchat-class integrations) with manual platform adds — the modern creator-native implementation; manual stat entry remains a fully valid form.
- **Gated access tiers** — email gate, brand-deal-request gate, approved-accounts list (documented at one product; product-specific until corroborated).
- **Marketplace/network distribution** — opt-in sharing of the kit with a platform's brand network (one product).
- **Rates presentation** — optional section; some products add pricing-guidance calculators.
- **Artifact shape** — one-page onesheet vs. multi-page document vs. full-site-as-kit; standalone vs. embedded in a link-in-bio/website platform; custom domain as paid upgrade.
- **Industry forms** — influencer/creator-collab form (stats-led), musician EPK/press-kit form (work-sample-led: music player, gig calendar, riders, press quotes), organization/PR media-kit form (company-side; adjacent to this Type's creator focus).
- **AI assistance** — AI-generated outreach emails, AI design/copy helpers (era-typical, optional).
- **Companion money/ops machinery** — invoicing, tax forms, pricing calculators, brand-deal inboxes (suite-adjacent, not the builder itself).

### L3 — Vendor-specific Structure (research notes only)

- Beacons: kit requires a Beacons account and lives inside the Link-in-Bio page; 5 named locking options; "Total Followers" manual platform adds; X/Facebook integration absent (as of Nov 2025); Unsplash cover-image source; free core with Pro custom domain; Brand Deal Profile as a separate object; W-9 generator; named view-analytics windows (1/3/7/30/all) with a data-discrepancy disclaimer.
- Bandzoogle: "Onesheet" preset layouts for three named purposes (booking/advancing, press promotion, industry pitching); GigSalad reviews integration; Bandsintown gig-calendar integration; plan ladder (single-page EPK plan → full website); "download your Onesheet EPK as a file in one click"; 70,000-musician claim.
- Visme: media kit maker reached via Documents tab → "Media Press Kit" icon; Brand Kit integration gated to a paid plan; PDF/JPG/embed/print outputs; organization-and-influencer dual positioning; large user-count marketing claims.

### Anti-overfitting check (historical / market-sample)

- The physical press kit (photos + bio + CD) → electronic press kit → static PDF/slide template (Canva/Slides/Notion path) → auto-synced hosted page (Beacons) all satisfy the L0 structure. The definition therefore does not depend on: auto-synced stats, hosted-page form, gating, or rates sections.
- Phone-number-style analog: auto-synced platform stats are the *current dominant implementation* of "audience evidence," not the definition — the EPK form proves audience evidence can be work samples + achievements.
- The vendor's own family metaphor ("a one-page digital resume"; EPK "similar to a portfolio or resume") confirms this Type belongs to the candidate-side document-authoring family, instantiated for the creator economy.

---

## Vendor-specific Findings

(See L3 above; none promoted to the canonical document.)

## Boundary Findings

1. **vs Resume Builder** (processed 2026-09-07): same authoring family — candidate-side document, user-owned content, tool-owned rendering, portable/shareable artifact. Difference is domain and reader: resume = career-document vocabulary (experience, education, skills) read by employers; media kit = creator-commercial vocabulary (audience reach, services, past collabs, rates) read by brands/industry. A resume has no audience-metric semantics; the media kit's evidence core is reach. Beacons itself calls the kit "a one-page digital resume" — family resemblance is vendor-acknowledged.
2. **vs Link-in-Bio Platform**: the link-in-bio page faces the creator's own audience (fans); the media kit faces commercial counterparties. Beacons ships both in one account and treats them as distinct surfaces with distinct content (links/store vs. stats/pitch). If the primary reader is fans → link-in-bio; if brands/industry → media kit. The media kit builder can be embedded in a link-in-bio product without collapsing the two Types.
3. **vs Creator Sponsorship Management**: the media kit is the pitch artifact; sponsorship management is the deal workflow (inbound requests, negotiation, deliverables, payment). Beacons bundles both under "Brand Collabs" — the help-center seam is visible (Media Kit articles vs. Brand Deal Profile / invoicing / outreach articles). The kit does not manage deals.
4. **vs Influencer Marketing Platform (§06)**: brand-side campaign machinery; such platforms may render creator "media cards" for brand evaluation — the consumption side of the same data. The creator media kit builder is creator-side authoring.
5. **vs Brand Asset / Guideline Platform (§06) and the organization/PR "media kit"**: "media kit" also names an organization-side artifact (company press kit, advertising rate card) published to press/partners. Different user (org comms vs. creator), different reader (press vs. brand partners). Visme straddles both readings; the directory leaf is the creator-side specialization.
6. **vs general design tools with media-kit templates (Canva/Visme pole)**: a design tool with a media-kit template category is not, as a whole, this Type — the user owns layout, there is no creator-commercial content model (no stats semantics, no brand-deal orientation), and the same tool serves unrelated documents. Visme's media kit maker is the boundary case: it has the artifact + tool-owned assembly, but its content model is generic and its stated users include organizations. The creator-specific content model (audience/reach semantics + brand-deal orientation) is what makes the dedicated Type.
7. **Musician EPK**: treated as a **variant** of this Type (press-kit form), not a separate Type — the L0 structure holds with industry-specific content vocabulary. No separate EPK leaf exists in the directory.

## Uncertainties

- Canva's own media-kit flow could not be inspected (blocked); the design-tool pole is evidenced via Visme plus Beacons' official characterization. Canva-specific claims are avoided.
- Linktree unreachable; whether major link-in-bio platforms ship their own media-kit builders is unverified.
- Whether Beacons offers PDF export was not documented in fetched articles; no claim is made (its documented distribution is link-first).
- Exact stat-refresh mechanics, supported metric sets per platform, and any numeric limits were not documented at the fetched depth; no precise numbers asserted.
- Visme's creator-specific depth (vs. its organization/PR positioning) is unclear; treated as the general-design boundary pole.
- Kit-view analytics prevalence across the market is unknown (documented at one product).

## Final Synthesis

The Creator Media Kit Builder is the creator-economy instantiation of the candidate-side document-authoring family (sibling of the Resume Builder): a creator-facing authoring application that assembles a **media kit** — one self-promotional document addressed to external commercial decision-makers (brands, agencies, industry professionals) — from a **commercial-pitch content model** (identity/niche, audience/reach evidence, work samples and past collaborations, offer with optional rates, contact), rendered by **tool-owned templates** into a **finished distributable artifact** (shareable hosted page and/or downloadable file), with access control where the kit is hosted.

Around this core, mature products add template galleries, section show/hide and rearrangement, branding controls, contact capture, testimonial/past-work sections, and password protection; modern creator-native products add auto-synced platform stats, gated access tiers, network distribution, kit analytics, and adjacent deal machinery (outreach AI, pricing calculators, invoicing). Industry forms vary: the influencer stats-led kit, the musician EPK (work-sample-led), and the organization PR kit (adjacent, org-side).

The sharpest seams: fan-facing link-in-bio pages (different reader), sponsorship/deal workflow systems (different job), brand-side influencer platforms (different side of the table), and generic design tools with media-kit templates (no creator-commercial content model).
