# Research Notes — Music Distribution Platform

Directory leaf: §27 Media, Entertainment, Creator & Culture — Music Distribution Platform
Slug: music-distribution-platform
Research date: 2026-09-08
Methodology: v1.1

---

## Research Goal

Understand what a Music Distribution Platform really is as an Application Type: what objects exist inside it, what its defining structure is (vs. what is merely common in the current market), who uses it, how work flows through it, and where its boundaries lie against neighboring Types (Music Streaming Platform, Record Label Management, Music Publishing Management, Royalty Management Platform, Podcast Platform, Content Distribution Platform, Digital Goods Store, Music Promotion Platform).

## Initial Boundary

Hypothesis before research: a provider-side service used by rights holders (independent artists, labels, managers) to place recorded-music releases onto consumer streaming/download storefronts (Spotify, Apple Music, etc.), manage the release lifecycle (go-live dates, takedowns, corrections), and pass store-reported earnings back to the rights holder.

Nearest confusions identified up front:

- **Music Streaming Platform** — the consumer destination, not the supply chain.
- **Record Label Management** — label business operations; distribution is one thing a label does, the Type here is the distribution machinery itself.
- **Music Publishing Management** — compositions/songwriter-side royalties; adjacent, often bundled as an add-on, not the core.
- **Royalty Management Platform** — label/enterprise-side royalty accounting over contracts; the distributor's earnings reporting is a lighter, supply-chain-driven cousin.
- **Content Distribution Platform** (§27 sibling, processed 2026-09-07) — video provider→destination; that pass explicitly reserves the audio sibling ("tracks → streaming services") as this leaf.
- **Digital Goods Store** — direct sale to fans; no storefront network as the product.
- **Music Promotion Platform** — marketing services; commonly bundled, not definitional.

## Research Questions

1. What is the unit of record? (release? track? catalog?)
2. What are "stores"/destinations, and how heterogeneous are they?
3. What is the release lifecycle? (authoring → review → delivery → go-live → takedown)
4. What identity objects bind the supply chain? (UPC, ISRC, artist profiles)
5. How does money flow back? (reporting lag, statements, thresholds, payout methods, splits)
6. Who are the users, and how do artist-self-serve vs label/enterprise poles differ?
7. What rights/exclusivity posture does the platform take?
8. What rules and exceptions matter? (fraud, immutable metadata, renewal, geography)
9. Would older/physical-era and enterprise-deal versions still fit the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| TuneCore | artist self-serve, subscription/per-release pricing | largest self-serve tier; deepest public help center (Tier 1) |
| CD Baby | artist self-serve, one-time per-release fee; oldest indie distributor (since 1998) | different fee philosophy; physical-distribution history; strong Tier 1 help center |
| Symphonic Distribution | two-tier: DIY Starter + label/established-artist Partner | bridges self-serve and label poles; official FAQ with operational claims |
| The Orchard | enterprise label-side distributor (Sony) | enterprise/deal-based pole; validates the Type above the self-serve market |

DistroKid was planned as a fifth sample but distrokid.com and support.distrokid.com timed out twice each; abandoned per network-restriction rules. Findings that would have leaned on it are kept at reduced strength.

## Sources

**TuneCore (Tier 1 — official help center, fetched 2026-09-08):**
- Root: https://www.tunecore.com/
- Release Statuses: https://support.tunecore.com/hc/en-us/articles/21038578340884-Release-Statuses
- Go-live times: https://support.tunecore.com/hc/en-us/articles/115006685548-How-long-does-it-take-for-my-music-to-go-live-in-stores
- Create a new release: https://support.tunecore.com/hc/en-us/articles/115006689988-How-do-I-create-a-new-release
- Switch from another distributor: https://support.tunecore.com/hc/en-us/articles/115006504267
- Takedown: https://support.tunecore.com/hc/en-us/articles/115006684508
- Renewal/removal: https://support.tunecore.com/hc/en-us/articles/115006689408

**CD Baby (Tier 1 — official help center + product pages, fetched 2026-09-08):**
- Root: https://cdbaby.com/
- Distribution partners: https://cdbaby.com/music-distribution/digital-distribution-partners/
- Help center home: https://support.cdbaby.com/hc/en-us
- Payouts: https://support.cdbaby.com/hc/en-us/articles/211074743
- Sales/accounting: https://support.cdbaby.com/hc/en-us/articles/4414481317005
- Post-delivery changes: https://support.cdbaby.com/hc/en-us/articles/204469029

**Symphonic (Tier 2 — official site + FAQ; knowledge base home timed out once):**
- Root: https://symphonicdistribution.com/ (serves symphonic.com)
- FAQ: https://www.symphonic.com/faq/
- Knowledge base: https://support.symdistro.com/hc/en-us (timed out 2026-09-08)

**The Orchard (Tier 2 only — marketing/press; no public operational docs):**
- Root: https://www.theorchard.com/ ("What started as a revolutionary music distribution company…"; client portal "Workstation"; Sony Music footer)

**Sourcing limitations (recorded per evidence rules):**
- DistroKid unreachable (2 timeouts) — omitted; the "largest self-serve distributor" claim is market lore, not asserted here.
- The Orchard: marketing/press only; no operational help docs publicly fetchable — no workflow claims drawn from it; used only to confirm the enterprise pole exists.
- Symphonic: FAQ gives operational claims (exclusivity, ISRC/UPC, payout minimum, reporting lag) but the deep KB was unreachable; per-article evidence thinner than TuneCore/CD Baby.
- Pricing figures observed (TuneCore plans, CD Baby per-release fees, Symphonic Starter) are current-market facts, kept out of the canonical document.

---

## Product Observations

### TuneCore (evidence layer A unless noted)

- Self-serve: artist/label creates account, uploads releases. Pricing poles: annual unlimited plans and legacy pay-per-release (with 1/2/5-year renewal options). Plan level gates advanced fields (custom label name, territory restrictions).
- **Release authoring** ("How do I create a new release?"): Add Release → choose **Album or Single**; four sections: (1) Release Details — title, main artist with Spotify/Apple artist-profile links, language, genre, release date/time, optional label, recording location, territory restrictions, existing UPC/EAN; (2) Stores & Social Platforms — "Deliver to all current digital stores" or per-store checkboxes; (3) Tracks — per track: title, ≥1 songwriter, artist/contributor roles (**must credit at least one performer and one producer/engineer**), release history, copyright ownership, lyrics, optional TikTok start time, audio upload (stereo first; Dolby Atmos optional); (4) Artwork — upload or built-in creator, must meet guidelines. Progress tracker 4/4 → cart → checkout/distribute.
- **Release statuses** (official): Submitted for Review → Needs Action (denied pending fix; must reply to email) → Approved & Sent → Live → Incomplete/Ready to Go (unfinalized for changes) → Taken Down → Denied. "Live" status historically tied to iTunes delivery ("Sent" otherwise).
- **Review + delivery**: content review ~2 business days, then "sent to stores immediately"; each store then processes on its own clock — per-store approximate live times documented individually (from ~1–2 business days to 3–4+ weeks), no guarantee, TuneCore cannot expedite; curated services (Beatport, Pandora) can't guarantee placement at all. Recommends scheduling 3–4 weeks ahead; playlist-pitching submissions must be in stores ~2 weeks pre-date. No go-live notifications; preview clips may appear on some stores before the release date.
- **Identifiers**: UPC per album, ISRC per track; generated free if left blank. On switching distributors: same UPC/ISRC reusable **only if content is unchanged** (track changes/reorders break UPC reuse; re-records/remixes break ISRC reuse).
- **Takedown**: dashboard action "Takedown All Stores" (immediate) or "Cancel Renewal" (end of renewal period); stores process takedowns ~2–3 business days, some up to 3 weeks; **cannot take down individual tracks** — album granularity; per-store removal requires support.
- **Renewal/finality** (pay-per-release plans): annual renewal fee; lapse → release removed from stores; removal is final, not reversible; redistribute as a new release; **UPCs cannot be reused**. (Plan-specific economics; not canonical.)
- **Money**: earnings collected from stores; monthly payment cycle; "no commission on your music revenue" (unlimited plans); TuneCore Splits — automatic collaborator splits with no commission fee; Direct Advance (advances against future earnings, partner-powered); publishing administration sold separately; YouTube Content ID; cover-song licensing service.
- **Catalog transfer**: switch into TuneCore without losing streaming history; request takedown from the old distributor; overlap windows possible because store review timing differs.
- Marketing claims: 150+ stores, keep 100% of rights (no ownership claim), unlimited uploads on plans.

### CD Baby (evidence layer A unless noted)

- One-time fee per release ($9.99 single / $14.99 album; no annual fees — current-market fact); revenue share: artist keeps over 90% ("we only make money when you make money"); since 1998; has paid over $1B to artists (marketing figures, layer B).
- **Destination network** (partners page): 150+ "streaming and download services"; the enumerated list is strongly heterogeneous: interactive streaming (Spotify, Apple Music, TIDAL, Deezer, Qobuz), download (iTunes, Amazon), social/UGC (TikTok, Facebook/Instagram, YouTube), regional services (NetEase, Tencent, KKBox, Saavn, Anghami, Boomplay, AWA, Claro música), discovery (Shazam — delivered via Apple), non-music contexts (Peloton, AMI jukeboxes), and **B2B content providers** (7digital, Audible Magic, Tuned Global, InProdicon, Kdigital) that themselves power other services. Physical distribution + disc manufacturing remain product lines.
- **Help center structure** (categories = the Type's own anatomy): Getting Started; Account & Billing; **Managing your releases** ("creation to submission to inspection"); **Managing your distribution** ("delivery and platform availability"); **Earnings & Payments**; Legal/Policy & Trust; Promotion & Marketing; Social Video Monetization; Submitting Art.
- **Post-delivery immutability** (official matrix): once "delivered", metadata is locked. Allowed anytime: add stores, change distribution options, change territories, cancel distribution. Limited windows (mostly with a paid priority tier): title/artist typo fixes, explicit-tag changes, audio *corrections* (errors only, not new mixes), release-date changes (>2 weeks away). Never: artwork changes, audio *changes* (new mixes/remasters), songwriter/producer edits, **UPC/ISRC corrections**.
- **Money chain** (official): payouts occur "once we receive the revenue generated by your releases from our partners". Statement structure: categories (Digital Distribution Sales / Social Video Monetization Royalties / legacy direct sales) → partner → track → time frame; **QTY (streams/downloads/playbacks) × Unit (per-unit take) = Payable, after partner and CD Baby cuts**; streaming vs download semantics explained; sub-cent rounding to $0.00.
- **Payout mechanics**: tax info required (default withholding if absent/invalid); **Pay Point** = user-set minimum balance that triggers automatic payout; method minimums and fees; weekly payout cycle (changes take effect by weekly deadline); payment history states "On its way" → "Delivered"; returned payments re-credited to balance next cycle. Geographic restrictions exist.
- **Fraud**: "Artificial Streams" earnings lines zeroed when a partner judges streams manipulated; **Artificial Streams Penalty Fee** passed through to the account; cannot be appealed by CD Baby.
- **Non-distributor revenue exception**: non-interactive radio (iHeartRadio) plays are paid via **SoundExchange, not CD Baby** — a named revenue stream that bypasses the platform.
- Writer/publisher splits entered per release for metadata purposes (songwriter/publisher fields; separate publishing-administration service exists).

### Symphonic Distribution (evidence layer A for FAQ claims; site Tier 2)

- Two poles: **Starter** (DIY, flat annual fee, "keep 100% of royalties", reduced share on YouTube/UGC partners) and **Partner** (labels/established artists, percentage of royalties, catalog management, DSP playlist pitching, dedicated client manager by approval). Application review ~5 business days for Partner-type applications.
- **Exclusivity posture** (official FAQ): "If a release is submitted to DSPs through Symphonic, that release cannot be re-distributed via another distributor until the end of the contractual term… the exclusivity only applies to specific distributed content and not to the artist or label themselves." — release-level term exclusivity, not ownership transfer.
- **Identifiers**: every release requires ISRC per track + UPC for the release; platform can generate them.
- **Audio formats**: WAV, FLAC, AIFF, high-quality MP3 accepted; WAV 16-bit+ recommended.
- **Catalog migration**: TransferTrack — batch transfers from multiple distributors; requires ISRCs, UPCs, metadata, audio to match existing releases; streams/playlists/stats preserved; typically 5–10 business days.
- **Money**: monthly payments; minimum payout threshold $50 (publishing admin $5); "Royalties are generally processed monthly, though they may take 2–3 months to arrive from streaming platforms" — **partner reporting lag is explicit**; payment/tax info required before payout; unclaimed balances remain until collected.
- Services around the core: video distribution, YouTube/SoundCloud monetization, publishing administration, sync licensing (separate brand), AI mastering, rights management, royalty advances, physical distribution. SplitShare: free unlimited collaborator splits with analytics and automatic payments.
- Scale claim: delivers to "over 200 digital service providers" including Tencent, TikTok, Meta, Snapchat, SoundCloud, Beatport, Peloton, audiobook/AI services (ElevenLabs, Udio logos on partner wall).
- Client-facing portal: SymphonicMS dashboard (payments, requests, releases).

### The Orchard (evidence layer B/C — Tier 2 only)

- Positions itself as "a revolutionary music distribution company" evolving into a broader creator-services company; client portal named "Workstation"; part of Sony Music (footer/legal). Serves labels and rights holders at enterprise scale; also distributes film/TV content (press). No public pricing, no public operational docs.
- Use: confirms the enterprise/deal-based pole of the same Type (release supply chain + label services under negotiated agreements) and that the Type spans from $9.99 self-serve to enterprise deals.
- No workflow claims drawn from The Orchard due to source limits.

---

## Cross-product Comparison

| Dimension | TuneCore | CD Baby | Symphonic | The Orchard |
|---|---|---|---|---|
| Unit of record | Release (Single/Album) of tracks | Release ("album/single" per pricing) | Release (ISRC per track, UPC per release) | catalog of releases under agreement (inferred) |
| Destination network | "150+ stores", per-store selection incl. social platforms | 150+ streaming/download/social/B2B partners, enumerated | "200+ DSPs" incl. regional + AI/audiobook surfaces | global network under label deals (no public list) |
| Release review before delivery | explicit Content Review (~2 business days) | explicit approval before delivery ("finalized and approved") | implied (Trust & Safety; Partner application review explicit) | unknown (no docs) |
| Go-live control | future release date; per-store timing varies; no guarantee | release date; changeable >2 weeks out | scheduled releases (implied) | n/a |
| Takedown | dashboard immediate or at renewal end; album granularity | cancel distribution anytime (matrix) | takedown possible (FAQ implies; KB unreachable) | per contract |
| Earnings pass-back | store revenue → account; monthly payouts | partner revenue → statements (QTY × Unit = payable); weekly auto-payout | monthly payments; 2–3 month partner lag; $50 threshold | per contract; statement via Workstation |
| Fee model | annual unlimited plans; legacy per-release + renewal | one-time per release + revenue share | flat Starter / percentage Partner | negotiated deal (percentage, standard for enterprise) |
| Rights posture | "keep 100% of your rights", no ownership claim | keeps rights; rev-share | release-level term exclusivity, no ownership | label agreement (rights retained by label) |
| Collaborator splits | TuneCore Splits (no commission) | songwriter/publisher metadata; split payments across accounts (article exists) | SplitShare (unlimited, free) | label handles (n/a) |
| Add-ons | Content ID, publishing admin, mastering, cover licensing, advances, Accelerator | physical, publishing admin, social video monetization, promotion tools | video, Content ID, publishing, sync, mastering, advances, physical | label services suite |
| Catalog transfer in/out | documented in-switch procedure | change-distribution-options anytime; old releases updatable only narrowly | TransferTrack batch migration preserving ISRC/UPC | client migrations (standard industry practice, not documented publicly) |
| Fraud posture | GenAI framework + fraud policy; artificial-streaming article promoted | artificial streams zeroed + penalty fee | Trust & Safety program | unknown |

**Stable across all researched products (B-layer):** release as the managed unit; store/destination network selectable per release; delivery-after-review pipeline with scheduled go-live; takedown reversibility; store-reported earnings itemized per store/track and paid out after the platform's share; identifiers (UPC/ISRC) binding the chain; catalog portability in/out; rights remain with the rights holder for the term.

**Variable across products (C/L2 layer):** fee model; payout cadence and thresholds; exclusivity terms; depth of add-on services; self-serve openness vs application/deal gating.

---

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Removing any one collapses the Type into a neighboring kind of software:

1. **The release as the unit of record** — a packaged body of recordings (single, EP, album) assembled by a rights holder from audio files + track/release metadata + artwork + contributor/songwriter credits, identified by standard codes (UPC for the release, ISRCs for tracks), owned by the rights holder, persisting as the platform's central managed object. *Remove →* a file host or audio tool; no supply-chain subject exists.
2. **The managed destination network** — a curated, maintained set of consumer storefronts and services (streaming DSPs, download stores, social/UGC platforms, regional services, B2B content providers) onto which any release can be placed, selectable per release. The platform holds the store relationships so users don't have to. *Remove →* direct-to-fan selling (Digital Goods Store) or a bare CDN.
3. **The delivery-and-availability lifecycle** — release submitted → platform review/approval → delivered to selected destinations → goes live per a scheduled release date → remains live for a term → takedown removes it; corrections/changes are managed after delivery under strict rules. *Remove →* a catalog database with no supply chain.
4. **The earnings pass-back** — consumption/sales reported by destinations flow back through the platform, are itemized to the rights holder (per store, per track, per period, net of the platform's share), accumulate on the account, and are paid out to the rights holder under configured payment/tax settings. *Remove →* a delivery utility with no economic loop; the "distribution" business disappears.

Jointly-held tests: 1+2 without 3 = storefront directory, nothing ships; 1+3 without 2 = generic content delivery; 2+3 without 1 = an ingestion pipeline for content of no recorded ownership; 1+4 without 2+3 = an accounting shell; 3+4 without 1 = logistics for unowned content.

**Historical/market-sample check:** the physical era still fits — CD Baby (1998) as a mail-order/physical distributor with the same record-deliver-collect loop (release = album/CD; destinations = retail accounts; delivery = physical supply chain; earnings = sales statements), and The Orchard's origin as a digitizer delivering label catalogs to early download services. The definition holds without self-serve upload, without streaming, without subscription pricing — so none of those enter L0. The analog ancestor (a regional distributor taking records to retail chains and settling sales statements) also fits, which confirms the abstraction is not over-fitted to the modern DSP era.

### L1 — Common Mature Structure

Present in essentially all mature current products, but not definitional:

- per-release/per-track analytics and audience data across destinations
- release links/artifact surfacing (store URLs, pre-save/pre-order)
- collaborator/royalty splitting on earnings
- scheduling aids: recommended lead times, pre-order/pre-save windows
- YouTube/UGC Content ID monetization as a monetization extension
- cover-song licensing assistance
- publishing administration as a companion service
- catalog transfer/migration tooling (preserving identifiers and stream history)
- label/multi-artist account structures
- fraud enforcement around artificial streaming

### L2 — Variant / Optional Structure

- **Fee model poles**: flat annual subscription with unlimited releases / one-time per-release fee (sometimes with paid renewals) / percentage-of-royalties (self-serve to enterprise gradient)
- **Customer tier**: DIY artist self-serve vs application-gated partner tier vs enterprise label deals with dedicated account management
- **Physical distribution** as a companion line (CD/vinyl manufacturing + physical retail) — legacy but alive
- **Openness**: instant self-serve accounts vs reviewed applications
- **Exclusivity terms** per release/term; territory restrictions per release
- **Payment mechanics**: payout cadence (weekly/monthly), thresholds, methods, geography limits
- Regional market depth (Asia-Pacific, MENA, LatAm networks), audiobook/AI-service destinations

### L3 — Vendor-specific (Research Notes only)

- TuneCore: "Release Statuses" state names; iTunes-anchored "Live" status semantics; 1/2/5-year renewal options; plan-gated advanced metadata fields; Direct Advance (partner-powered); Accelerator program; per-store live-time tables; GenAI content framework; GrimesAI collaboration handling; Dolby Atmos upload ordering; TikTok start-time field.
- CD Baby: "Pay Point" naming and weekly payout cycle; FastForward paid priority tier and its change-window matrix; Artificial Streams Penalty Fee; legacy direct-store sales category; HearNow/Show.co promotion brands; disc manufacturing arm.
- Symphonic: SplitShare™; TransferTrack™; Starter-vs-Partner structure; real-time TikTok analytics claim; Bodega Sync; regional site network (LatAm/Brasil/APAC/Europe).
- The Orchard: Workstation portal; Sony ownership; Magic Star children's/family division; film/TV distribution arm.

## Vendor-specific Findings

- Annual renewal fee + final takedown-on-lapse is TuneCore pay-per-release economics — pricing-model-specific, not canonical (CD Baby's one-time model has no such renewal; Symphonic's is annual flat or percentage).
- CD Baby's penalty fee for artificial streams is product-specific; the general "partner fraud determinations suppress earnings" behavior is cross-product.
- TuneCore's "Live"-status-tied-to-iTunes quirk is a product implementation detail.
- The Orchard's multi-media (film/TV) extension is a company scope choice, not part of the music-distribution Type.

## Rejected Findings

- "150+ / 200+ stores" — marketing-scale claims; kept as observed per-product facts, not canon (network size is a competitive variable).
- "Keep 100% of royalties / over 90%" — fee-model outcomes, not structure; varies by plan and product.
- "3–4 weeks ahead" scheduling advice — TuneCore's recommendation; not a standard.
- "Monthly payments" — true of TuneCore/Symphonic today, but CD Baby pays weekly; cadence is a variant.
- "$50 minimum payout" — Symphonic-specific value.
- "Distribution = upload to Spotify" — the consumer-facing simplification; the Type's network is far broader (download, social/UGC, regional, B2B, non-music surfaces).
- Physical manufacturing/merch, mastering, sync, publishing admin, playlist pitching — optional add-ons, excluded from the defining core (all four sampled products sell some of these; none defines the Type).

## Boundary Findings

- **vs Music Streaming Platform**: the streaming service is the *destination*; the distribution platform is the *supply chain* serving it. A distribution platform has no consumer listening surface.
- **vs Record Label Management**: labels *use* distributors; label management systems run A&R/roster/release-planning/campaign operations. The distribution platform's object world is release→destination→earnings, not roster→campaign→P&L. (Boundary flagged for the unprocessed record-label-management pass.)
- **vs Music Publishing Management**: publishing concerns compositions/songwriters; the distribution platform handles *recordings* (masters). Songwriter/publisher fields exist in releases as delivery metadata; publishing royalty collection is a separate companion service. (Flagged for the unprocessed music-publishing-management pass.)
- **vs Royalty Management Platform**: distributor earnings reporting is supply-chain-derived and rights-holder-facing; royalty management systems compute contractual royalties over catalogs/deals with rich accounting. The distributor's statement is an input to such systems, not their substitute.
- **vs Podcast Platform**: same "deliver audio to directories" shape, but the object world differs (episodes/shows vs releases with commercial identifiers) and the money loop differs (mostly no per-store royalty pass-back in podcast distribution). Same family shape, different Type — consistent with the content-distribution-platform pass's finding.
- **vs Content Distribution Platform (video)**: same provider→many-destinations shape; medium and object world differ (channels/EPG/VOD assets vs releases/UPC/ISRC). Separate Types; cross-referenced both ways by that pass.
- **vs Digital Goods Store / direct-to-fan (e.g., artist storefronts)**: direct-to-fan sells to fans from one's own storefront; the distribution platform's defining move is placing releases on *third-party* storefronts via managed relationships.
- **vs Music Promotion Platform**: promotion (playlists, ads, pitching) is an add-on revenue line here but its core object world (campaigns, audiences) is different.
- **"去掉什么就变成另一个 Type" 判据**: remove the destination network → delivery/CDN tool; remove the earnings loop → upload/delivery utility; remove the release-of-record → ingestion pipeline; remove third-party destinations and sell direct → digital goods store; make the destination the user's own product → music streaming platform.

## Uncertainties

- The Orchard's operational workflow is undocumented publicly; the enterprise pole's shape (deal terms, statement delivery, delivery specs) is inferred from the market pattern, held at C-layer strength.
- Symphonic's release-level review process is implied (Trust & Safety category, Partner application review) but not directly documented in fetched pages.
- DistroKid unverified; anything that might be DistroKid-specific (e.g., features unique to it) is absent from this pass.
- Whether release-level exclusivity clauses are universal across the industry or Symphonic-specific in wording: TuneCore/CD Baby marketing emphasizes no ownership but doesn't publish exclusivity terms in fetched pages; treated as variable contract terms.
- Pre-save/pre-order mechanics vary by store and product; not canonized.
- Exact store counts change constantly; all counts are point-in-time marketing figures.

## Final Synthesis

A Music Distribution Platform is the recorded-music supply chain as software: the rights holder assembles a **release** (audio + metadata + artwork, identified by UPC/ISRC); the platform places that release onto its managed network of **storefronts and services** through a **review-and-delivery lifecycle** with scheduled go-live and reversible takedown; and the **money that the stores report flows back through the platform**, itemized per store/track, accumulating to the rights holder's account and paid out after the platform's share — with the platform never taking ownership of the recordings. Everything else the modern market sells alongside it (analytics, splits, Content ID, publishing admin, mastering, promotion, physical, advances) is mature optional structure; the fee model (flat, per-release, percentage) and the customer tier (DIY to enterprise) are variant axes. The Type is distinct from the consumer streaming platforms it feeds, from the label/publishing/royalty management systems its users may also run, and from direct-to-fan selling — the defining move is placing releases on third-party storefronts at scale and settling the resulting money back to the rights holder.
