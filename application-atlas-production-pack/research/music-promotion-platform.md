# Research Notes — Music Promotion Platform

Research date: 2026-09-08

## Research Goal

Establish what a Music Promotion Platform actually is in the current market: its defining structure, its two-sided economics, its lifecycle, and its boundaries against the neighboring music-industry types (Music Distribution Platform, Influencer Marketing Platform, fan-facing "music marketing" tools) and generic marketing types (Social Media Management, PR, Influencer Campaign Management).

## Initial Boundary

Working hypothesis before research:

- Core use: getting recorded music heard — artists/labels/publicists pitch tracks to playlist curators, blogs/media, radio, and creators; placements and feedback result.
- Users: independent artists, labels, managers, publicists (demand side); playlist curators, bloggers, radio producers, content creators, A&R (supply side).
- Closest neighbors: Music Distribution Platform (stores + earnings), Influencer Marketing Platform (generic creators), Social Media Management Platform (artist's own channels), marketing campaign tools.
- Main unknowns: (1) does the leaf's market meaning include fan-facing campaign tools (pre-save/smart links, e.g. the Feature.fm family)? (2) is "curator pitching" the whole story or just one family?

## Research Questions

1. What objects exist in these systems (track/release, submission, campaign, curator, placement, feedback)?
2. Who are the two sides and what exactly is exchanged?
3. What is the lifecycle of a submission/campaign, including pre-release use?
4. How are curators vetted and compensated? What response/coverage guarantees exist and how are they enforced (credits, refunds)?
5. How are results tracked and reported?
6. Where is the boundary vs distribution (store supply chain), vs influencer marketing (sponsored content), vs fan-campaign/link tools, vs booking?

## Representative Products

Selected for market representativeness + different product philosophy + different tiers:

| Product | Role in sample | Philosophy / tier |
|---|---|---|
| SubmitHub | artist-driven submissions at scale | freemium credit economy; blogs + playlists + influencers; US |
| Groover | artist-driven submissions, guaranteed feedback | paid credits ("Grooviz"); strong EU/French label & radio network |
| Playlist Push | premium managed matching | campaign budgets, heavily vetted curator/creator network, pay-for-review; US |
| Musosoup | inverse marketplace | curators come to the artist with offers; campaign fee; coverage guarantee; UK |
| Feature.fm | boundary probe | self-styled "music marketing platform" — smart links / pre-save / fan data; structurally different |

Musosoup self-titles "Music Promotion Platform"; Playlist Push self-titles "Music Promotion Services"; Groover "Music Promotion with Results"; SubmitHub "the most-transparent place to promote your music". Feature.fm self-titles "music marketing platform" — the label split in the market itself tracks the structural split found here.

## Sources

All Layer A (directly observed) unless noted; fetched 2026-09-08:

- SubmitHub — homepage https://www.submithub.com/ ; nav of https://www.submithub.com/promotion (page body is JS-rendered; only navigation structure retrievable)
- Groover — homepage https://groover.co/en/ (includes full FAQ: how it works, credits, curator categories, screening, refund rules)
- Playlist Push — homepage https://www.playlistpush.com/ ; Spotify promotion page https://www.playlistpush.com/spotify-playlists-promotion (workflow, pay-for-review, Artist Protection Fund, pricing FAQ, vetting)
- Musosoup — homepage https://musosoup.com/ ; https://musosoup.com/artists-how-it-works (6-step lifecycle, paid/free offers, coverage guarantee)
- Feature.fm — homepage https://feature.fm/ (product line, positioning, business tier)

Not fetched (out of scope after stop conditions met): SubmitHub and Playlist Push deep help centers, Groover help center articles, Musosoup comparison blog posts, curator-side signup flows.

## Product Observations

### SubmitHub

- Positioning: "The most-transparent place to promote your music. Get your music reviewed and promoted by 1,700+ quality-checked Spotify playlisters, music bloggers, and influencers. More than one million artists, publicists and labels have used SubmitHub." [A]
- Two-sided: public "List of curators" page and "Apply to be a curator" application. [A]
- Nav structure (the promotion surface): Promote a song / Submit to curators / Hire influencers / Marketplace. [A]
- Adjacent bolt-ons in the same account: Ads (Create Meta Ad, Links, Ads Studio), Free tools (Playlist Checker, AI Song Checker, What's My Genre?), For artists (Hot or Not, Bot checker, Popularity Checker, Playlist finder). [A]
- Curator kinds named: Spotify playlisters, music bloggers, influencers. Demand side named: artists, publicists, labels. [A]
- Limits: homepage + nav only; no lifecycle detail retrievable (JS-rendered pages). Details below L1 confidence.

### Groover

- Positioning: "Music Promotion with Results"; "Get your music heard by the right people"; "Direct and fast access to curators, playlists and music pros"; 3,000+ curators/pros; 600,000+ artists & pros. [A]
- Three-step flow: (1) Pick your music pros — "Browse 3,000+ curators, labels and blogs. Choose only the ones that fit your sound"; (2) Add your song — "Upload your song or demo with a short pitch. It lands straight in their inbox"; (3) Get guaranteed feedback — "You'll hear back with insights or new opportunities within a week – or we refund your credits." [A]
- Credit economy: "Grooviz are credits on Groover… Contacting a curator/pro costs 2 Grooviz. Top-tier curators may cost more (4–6 Grooviz)"; "What happens if a curator doesn't reply? Your credits will be refunded and you'll be able to contact any other curator." [A]
- Curator taxonomy on the supply side: Visibility Curators (media outlets, blogs, radio stations and shows, playlisters, YouTube/Twitch channels — "If they like your track, they'll share it with their audience"), Partners (record labels, bookers, managers, sync supervisors, publishers — "looking for their next big discovery"), Advice (managers, coaches, mentors — "selected for their ability to offer valuable feedback"). [A]
- Curator screening: "carefully selected music enthusiasts screened by the Groover Team", judged on "degree of influence", "quality of the content they produce", "the artists they support and their editorial line". [A]
- Eligible content: "unfinished / unreleased / scheduled for future release / already released (even older catalog tracks)"; submission needs a YouTube, SoundCloud, or Audiomack link. [A]
- Audience: "Groover helps artists and their representatives (label managers, PR agents, publishers etc.) get their music heard"; labels actively listed (Ninja Tune, PIAS, Because Music, etc.). [A]
- Outcome language: "Playlists, press, radio, labels deals – all from one campaign"; cumulative stats: "more than 3,000 active music curators and pros have given more than 4 million pieces of feedback, 1 million+ shares (reviews, playlist adds etc.) and 1,000+ signatures on record labels." [A]
- Filterable curator discovery: "refine your search using filters like music genres, curator types, and countries." [A]

### Playlist Push

- Positioning: "Real Music Promotion Service, No Bots"; "Over 50,000 independent and major label artists use our promotion services to get their music on Spotify playlists and in TikTok videos"; founded 2017, US-based. [A]
- Two campaign products: Spotify Playlist Promotion ("Pitch your song to independent music curators that manage organic playlists on Spotify", 4,000+ verified playlists, from $280) and TikTok Video Promotion ("Submit your song to influencers and creators to use in their videos", 3,300+ vetted creators, from $350). [A]
- Artist workflow (five steps): "Submit your song" (campaigns can start as early as 2 weeks before release) → "Select targeting & budget" ("Pick the genres, moods and languages that fit your song. See how many playlists match, then choose how many you want to reach") → "Your song is sent to playlists" ("We deliver your submission to your targeted group of real Spotify playlist curators for placement consideration") → "You receive curator responses… they'll keep coming until your budget runs out" → "Review your results — detailed final campaign reporting with advanced analytics." [A]
- Pay-for-review model: "You are paying for a professional review and guaranteed consideration. While we cannot buy placements (this would violate Spotify's Terms of Service)… If a curator fails to provide a qualitative, professional review of your music, the cost of that specific submission is automatically returned to your account balance" (Artist Protection Fund; homepage: "If a curator does not review your track before the 14-day deadline, you automatically receive that money back as a credit"). A rejection still consumes the review fee. [A]
- Anti-guarantee rule stated explicitly: "avoid any company that guarantees placements or streams, as that model relies on manipulation"; "that does not guarantee your music will be added to those playlists." [A]
- Targeting engine: "Playlist DNA" — "Your Playlist DNA is your track's genres, moods, and language… We match that against thousands of active playlists." [A]
- Curator vetting: "Each curator goes through a rigorous vetting process to prove their engagement is authentic, streams are organic"; "Over 99% of curator applications are turned down. Once a curator is admitted, their playlists are continuously reviewed"; bot-detection technology monitoring playlist listener activity. [A]
- Curator-side economy: "Get paid to review songs submitted to your playlists. Up to $15 per review" (playlist owners); "Earn money making videos with new music you actually like. Paid per video" (TikTok creators). [A]
- Reporting: "Detailed Live Reporting — Access advanced analytics and placement data on your live reporting dashboard"; sample campaign report shows playlist adds, streams, success ratio. [A]
- Feedback as deliverable: "many provide detailed written feedback on the production, vocals, and mix." [A]
- Pre-release: "Pre-Release Campaign… allows you to secure curator commitments up to 14 days before your song drops"; unreleased audio uploaded securely to the platform and delivered to curators to review ahead of launch. [A]
- Self-declared category map: "While platforms like SubmitHub require artists to manually pitch to individual curators, our genre-matching system automates the targeting process. Compared to SoundCampaign…" — confirms one category with a structural axis (manual pitch vs automated match). [A]
- Region restriction: "Playlist Push runs on a network of curators and creators who we pay for reviews and videos, and we can only do that in countries where we have a supported way to pay people out." [A]

### Musosoup

- Positioning: page title "Musosoup | Music Promotion Platform"; "Connecting the world's best artists with global music curators"; 85k artists, 3k curators, 120 countries. [A]
- Inverse marketplace: "Instead of pitching curators yourself, Musosoup lets curators discover your release and contact you with coverage opportunities. You review the offers and choose the ones that are right for you." [A]
- Six-step lifecycle: (1) Submit your music free — "add a link to your music or upload an MP3"; (2) Await approval — "We listen to all submissions… up to 24 hours"; (3) Activate your account — "pay the campaign fee"; (4) Complete campaign details; (5) Start generating coverage — "Curators approach you with offers for coverage—both paid and free—or you can explore and secure promotions directly on our marketplace", available "From 90 days prior to release date"; (6) Complete your campaign — "See all your coverage and the curators you've worked with, all in one place in your campaign report." [A]
- Coverage kinds: "playlist placements, blog reviews, interviews, radio airplay, and social media features." [A]
- Guarantee: "Guaranteed Coverage or Your Money Back… If you don't receive any [coverage], we'll refund your campaign fee—no questions asked." [A]
- Explicit anti-positioning vs the per-submission credit model: "Pay for results, not for feedback… artists don't need thousands of curators or to pay for listens or feedback"; "We believe musicians deserve better than costly, risky PR or platforms where they pay curators with no coverage guarantee." [A]
- Cross-product comparison posts published by the vendor: "Musosoup vs Submithub", "Musosoup vs Groover" (titles observed in footer). [A]
- Platform-side quality gate: Musosoup itself listens to/approves submissions before campaigns run (distinct from the curator review). Policies published on AI music and botted playlists. [A]
- Additional promo services sold on a marketplace within a campaign: "social media shout-outs, press features, and playlist pitching." [A]

### Feature.fm (boundary probe — different family)

- Self-positioning: "The #1 music marketing platform for independent artists"; "Marketing, built for music." [A]
- Product line: Artist Bio Links, Release Links, Pre-Save Links, Future Save, Contest & Unlock Pages, Tour and Event Links, Podcast Links, Short Links, Fan Base Management ("collect, organize and sync fan contact info"), Analytics & Insights ("Track fan behaviors across your links… send it all to your ad retargeting platforms"). [A]
- Business tier: "labels, managers, marketers and distributors who manage their marketing efforts across artist rosters and utilize aggregated data at scale." [A]
- No curator network, no submission-review-decision loop anywhere in the product surface. [A]
- Conclusion: structurally a fan-activation/link-campaign tool, not a curated-submission exchange. This is the "music marketing platform" family (Feature.fm / Show.co / Linkfire / ToneDen per market usage) — adjacent, not this Type.

## Cross-product Comparison

| Dimension | SubmitHub | Groover | Playlist Push | Musosoup |
|---|---|---|---|---|
| Unit submitted | song to curators | song or demo (even unfinished) | song (incl. unreleased audio, pre-release) | single/EP/album (link or MP3) |
| Curator network | playlisters, bloggers, influencers (quality-checked, self-applied) | playlisters, blogs/media, radio, YouTube/Twitch, labels, bookers, managers (team-screened) | Spotify playlist curators + TikTok creators (rigorously vetted, >99% rejected) | blogs/magazines, playlists, radio, social curators (platform + artist vet offers) |
| Initiation | artist picks curators | artist picks curators | platform auto-matches by genre/mood/language | curators initiate offers to artists (plus marketplace) |
| Exchange unit | per-submission credit (free + premium tiers) | per-contact credits ("Grooviz") | campaign budget; pay-per-review | campaign fee + optional paid offers |
| Guarantee | transparency emphasis; curator quality check | feedback guaranteed or credits refunded | review guaranteed or fee credited back (no placement guarantee, ToS-based) | coverage guaranteed or campaign fee refunded |
| Curator compensation | (not directly observed in fetched pages) | receives credits/earnings; price tiers by demand | paid per review (stated rate ceiling); creators paid per video | offers may be paid or free; "sustainable curator" framing |
| Outcome record | submissions/responses in account | feedback + shares (reviews, playlist adds) + label signatures | live campaign dashboard: reviews, adds, streams, success ratio | campaign report: all coverage + curators worked with |
| Platform-side quality gate | curator quality check | curator team screening | vetting + continuous monitoring + bot detection | platform listens to every submission before activation; AI/bot policies |
| Pre-release use | (not directly observed) | unreleased/scheduled submissions allowed | pre-release campaigns ~2 weeks ahead; commitments secured pre-drop | campaigns from 90 days pre-release |
| Adjacent bolt-ons | ads studio, links, AI checkers, artist checkers | — (career-outcome framing) | playlist analyzer tool | in-campaign marketplace for extra services |

Layer B (cross-product commonality, 4/4 promotion-family products):

- A recording (track or release) is the submitted unit; released and unreleased music are both promotable.
- An independent third-party curator network is the supply side; every product vets/screens curators and frames quality/authenticity as a selling point ("no bots" is a whole industry-wide theme).
- The review-decision loop: submissions receive a human curator response — accept/feature (placement, review, airplay, offer) or decline — recorded in the artist's account.
- Accountability mechanics: explicit terms for what a submission costs and what happens when curators don't respond or don't cover (refund/credit-back rules in all four).
- Campaign-level result tracking: dashboard/report surface aggregating responses and coverage.
- Feedback is a first-class product: guaranteed deliverable (Groover), paid deliverable (Playlist Push), explicit non-guarantee (Musosoup), quality-check framing (SubmitHub).

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the product stops being a music promotion platform:

1. **The submitted recording** — a track or release, released or unreleased, submitted by its maker or representative as the unit of promotion. Remove → generic marketing tool with no music-submission core.
2. **The independent curator network** — third parties who control channels of music exposure (playlists, blogs/media, radio, creator channels, label rosters) and are reachable through the platform. Remove → ads platform, distribution platform, or contact-list app.
3. **The review-decision loop** — each submission is put to curators who respond with a recorded decision: feature/cover on their own channel, or decline, with feedback commonly attached. The placement decision belongs to the curator, not the platform. Remove → guaranteed-placement (payola-style) service, or unaccountable cold pitching.
4. **The platform-governed terms of exchange** — explicit rules for what a submission costs, what a curator owes in response, and what is refunded/credited/guaranteed when terms aren't met. Remove → a message board; the accountability that all four sampled products lead with disappears.

Jointly load-bearing: 1 alone = upload form; 2 alone = directory; 3 without 1+2 = review tool; 4 without 1–3 = billing; 1+2 without 3 = pitching void (the exact thing these products claim to fix); 1+3 without 4 = unmoderated pitch board; 2+3 without 1 = industry-opportunity listings without a recording substrate.

### L1 — Common Mature Structure

- curator profiles with genre tags, channel stats, and search/filter discovery
- campaign object bundling many submissions toward one release/goal
- written feedback as a deliverable attached to responses
- curator vetting/quality machinery (application screening, bot/streaming-authenticity detection, continuous monitoring)
- campaign reporting (responses, placements/coverage lists, performance metrics)
- pre-release submission windows (platform-specific spans measured in days–weeks)
- two-sided consoles (artist-side campaign management; curator-side review inbox)
- genre/mood/language targeting or matching between tracks and curators

### L2 — Variant / Optional Structure

- initiation direction: artist→curator pitch (SubmitHub, Groover) / curator→artist offers (Musosoup) / platform auto-match (Playlist Push)
- pricing shape: per-submission credits, campaign fee, campaign budget; free tiers possible
- guarantee type: feedback guarantee vs review-or-refund vs coverage-or-refund (mutually exclusive positions vendors market against each other)
- curator compensation model: platform-paid review fees / credits / paid-or-free offers
- channel mix emphasis: streaming playlists / short-video creators / blogs & press / radio / labels & industry pros
- customer tier: DIY indie artist ↔ labels, managers, publicists (all sampled products serve both ends to a degree)
- adjacent bolt-ons present in some products: ad-creation studios, link tools, AI song checkers, playlist analyzers, artist-bot checkers, in-campaign service marketplaces

### L3 — Vendor-specific (kept out of the final document)

- Groover: "Grooviz" currency (1 = €1), 2-Grooviz per contact, 4–6 for top curators, 7-day response deadline, curator category names (Visibility/Partners/Advice), platform stats (4M+ feedback, 1M+ shares, 1,000+ label signatures), 600k+ users
- Playlist Push: "Artist Protection Fund", "Playlist DNA", 14-day review deadline, ~2-week pre-release start, $280/$350 entry prices, "up to $15 per review", >99% rejection rate, 1,700/4,000/3,300-style network counts, region-availability rule tied to curator payouts, 2017 founding
- SubmitHub: 1,700+ curators, 1M+ users, Hot or Not / Bot checker / AI Song Checker product names, Ads Studio, Marketplace
- Musosoup: £42-class campaign fee, 24h platform approval, 90-day pre-release window, 85k/3k/120-country stats, paid-vs-free offer blog framing, "#SustainableCurator", AI-music and botted-playlist policies
- Feature.fm: full product-line names (Future Save, Contest & Unlock Pages), business tier

## Vendor-specific Findings

- Playlist Push is the only sampled product that names its compliance rationale explicitly (cannot buy placements; Spotify ToS). The no-guaranteed-placement rule is plausibly industry-wide (Musosoup's playlisting is free-of-charge-to-curator and guarantee is coverage-not-placement; Groover's curator decision is editorial), but the explicit ToS statement is Playlist Push's. Held at: common pattern, strongest evidence single-product.
- Musosoup is the only sampled product with a platform-side content gate before campaign activation (they listen to every submission). Others vet curators, not artists' tracks, before exposure.
- SubmitHub's lifecycle detail (response windows, credit costs, guarantee mechanics) was not retrievable — homepage/nav only. Claims about it are kept minimal.
- SubmitHub and Playlist Push both extend beyond music curators into influencer hiring (SubmitHub "Hire influencers"; Playlist Push TikTok creator campaigns) — the TikTok creator product is the clearest overlap with Influencer Marketing Platform and is documented as a variant channel, not the core.

## Boundary Findings

- **vs Music Distribution Platform**: distribution moves a packaged release through a managed store network and passes earnings back; promotion pitches a recording to curators for editorial consideration, and money flows artist→platform→curator (not revenue back from exposure). A distribution platform can offer playlist pitching as an optional add-on (the sibling doc records exactly this). Remove the curator review-decision loop and promotion becomes distribution; remove the store network and distribution becomes promotion. Boundary held.
- **vs Influencer Marketing Platform**: generic influencer platforms run brand→creator sponsored-content campaigns for products; here the supply side is music curators whose deliverable is editorial feature/coverage of a recording on their own channel, with review/feedback as a distinct paid deliverable. Overlap exists at the TikTok-creator campaign edge (Playlist Push TikTok product; SubmitHub influencer hiring) — recorded as a variant, with the music-curator editorial deliverable as the distinguishing line.
- **vs fan-facing "music marketing platforms" (Feature.fm family)**: smart links, pre-save campaigns, bio links, fan CRM and retargeting have no curator, no submission, no decision loop — a structurally different Type that the market labels "music marketing" rather than "promotion". The directory has no dedicated leaf for that family; it maps loosely toward marketing-campaign/link-tooling territory. Recorded as a taxonomy observation, not silently merged.
- **vs Artist Booking Platform**: booking transacts live-performance engagements; promotion seeks exposure for recordings. Sibling doc confirms the seam.
- **vs Record Label Management / PR tools**: labels manage catalogs and campaigns; a publicist is an agent, not a platform. The promotion platform is the platformized form of the traditional plugger/PR pitching function (see historical check).
- **vs Social Media Management Platform**: SMM operates the artist's own channels; promotion operates other people's channels via curator decisions.
- **"What would make it a different Type" test**: remove curator independence/decision (pay for guaranteed placement) → payola/placement service, not this Type; remove curators entirely (ads to audiences) → advertising; remove music (submit any content to bloggers) → influencer/PR pitching platform.

### Historical / Market-Sample Check

- Pre-internet radio plugging: a paid agent (plugger) carries a label's new record to radio stations/shows; each producer decides adds; outcomes tracked; service sold with relationships and follow-up, never with guaranteed adds. Satisfies all four L0 legs (submission unit, curator network = stations, decision loop, governed terms). L0 mentions no software, no credits, no streaming.
- Sonicbids (2003, press-kit submissions to bookers), Music Xray (2008, submissions to industry professionals), ReverbNation "Opportunities" (submit to labels/playlists/press): submit-to-curator marketplaces with decision loops — satisfy the model.
- Musosoup/Playlist Push/Groover/SubmitHub (2013–present) are the streaming-era realization.
- Conclusion: the canonical abstraction (curated review-decision exchange over recordings) is era-stable; credits, dashboards, pre-release windows, and genre-matching engines are modern machinery, not definitional.

## Uncertainties

- SubmitHub operational detail (credit costs, response windows, guarantee wording) not directly observed — its L1 membership is inferred from nav structure + market category, held weaker than Groover/Playlist Push/Musosoup claims.
- Curator-side payout mechanics observed only for Playlist Push (per-review rate ceiling) and partially Groover (credit refunds); SubmitHub/Musosoup curator compensation described only indirectly.
- Whether SubmitHub formally guarantees a response (common market belief) was not verified from official pages — deliberately not asserted in the final document.
- Show.co, Linkfire, ToneDen (fan-campaign family) not fetched; the family-level boundary rests on Feature.fm's directly observed product line plus market naming conventions.
- SoundCampaign referenced by Playlist Push as a competitor but not researched (product reportedly wound down; sample sufficient without it).

## Final Synthesis

A Music Promotion Platform is a two-sided system in which makers or representatives of recordings submit tracks (released or unreleased) to a network of independent music curators — playlist owners, blogs/media, radio, creators, industry professionals — who review each submission and record a decision to feature it on their own channel or decline it, commonly with written feedback, under platform-governed terms that make the exchange accountable (what a submission costs, what a curator owes, what is refunded or guaranteed). The curator's editorial decision — not paid placement — is the deliverable; vetting of curators and authenticity of their audiences is a core industry theme; results accumulate in campaign reports. Direction of initiation, pricing shape, guarantee type, curator compensation, and channel mix are variant axes. Fan-facing campaign/link tools ("music marketing platforms"), store distribution, generic influencer marketing, booking, and label management are adjacent Types with clean structural seams.
