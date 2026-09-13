# Research Notes — Record Label Management

Date: 2026-09-09
Directory leaf: Record Label Management (§27 Media, Entertainment, Creator & Culture)
Slug: record-label-management

## Research Goal

Understand what software of the "Record Label Management" type actually is from real products: what objects exist inside a label's business system (roster, catalog, releases, contracts, royalties, campaigns), who uses it, how the label's operating loop (sign → plan → release → promote → collect → settle) is realized in systems, and where its boundary lies against Music Distribution Platform, Music Publishing Management, Royalty Management Platform, Performing Rights Management, Music Promotion Platform, Artist Booking Platform, and generic accounting software.

Sibling context inherited (ratified from processed passes):

- music-distribution-platform (2026-09-08): "labels *use* distributors; label management systems run A&R/roster/release-planning/campaign operations. The distribution platform's object world is release→destination→earnings, not roster→campaign→P&L." (Boundary flagged for this pass.)
- music-publishing-management (2026-09-08): composition-vs-recording seam confirmed structural — publishing systems keep works as the ownership unit with recordings linked only as embodiments (ISRC), while distribution/label systems center masters/releases; label mechanical reporting TO publishers is the mirror flow; same vendors deliberately serve both sides (Curve, Reprtoir) — cross-reference, not merge.
- artist-booking-platform (2026-09-06): AmpSuite product-mismatch note — the domain now serves Beatport's label-management suite ("distribution, royalty accounting, publishing, contracts for record labels"), incidentally confirming the market separates booking from label tooling.
- music-promotion-platform (2026-09-08): "labels manage catalogs and campaigns; the promotion platform is the platformized form of the traditional plugger/PR pitching function."
- performing-rights-management (2026-09-09): society-side vs rights-owner-side; PROs appear in rights-owner income loops as pay sources.

## Initial Boundary

Working hypothesis at start: a Record Label Management application is the record label's internal business-operations system — the system of record for the label's artists (roster), its recordings (catalog/releases), its marketing activity, and its money (contracts, royalties, artist statements). Nearest confusions:

- Music Distribution Platform (the delivery pipeline labels use — often bundled into label suites);
- Music Publishing Management (the composition side — often bundled as a second rights side);
- Royalty Management Platform (the generic royalty engine — the money loop overlaps);
- Artist Booking Platform / Talent Agency Management (the live/representation side — different object world);
- Accounting Software (royalty accounting is specialized, not general bookkeeping).

## Research Questions

1. What are the core objects? Is the center the roster (artists), the catalog (recordings), the release, the contract, or the campaign?
2. How does an artist enter the label's world (A&R/demo intake) and how is the deal held (contract as document vs computable data)?
3. How are releases planned, assembled, delivered, and tracked? Is distribution part of the Type or a hand-off?
4. How does the money loop work: income ingestion → matching → calculation (splits, recoupment, escalations, cross-collateralization) → statements → payments?
5. What roles exist (label manager, A&R, marketing, royalty officer, accountant) and what external parties face the system (artists, distributors, publishers, societies)?
6. Which capabilities are definitional vs common vs variant: distribution bundling, demo intake, promotion tools, publishing side, artist portals, analytics?
7. Where exactly are the seams vs the sibling Types listed above?

## Representative Products

Selected for market representation + documentation quality + different product philosophy + different customer tier:

| # | Product | Owner/positioning | Philosophy pole | Customer tier | Evidence |
|---|---|---|---|---|---|
| P1 | AmpSuite | Beatport | "label management software" suite: distribution + marketing + royalty accounting + publishing/neighbouring rights + artist dashboard | indie labels → label groups → distribution companies | A (homepage only; subpages 404/403) |
| P2 | Label Engine | Create Music Group | label ops platform: distribution + accounting + promotion + demo management | "thousands of labels and distributors" | A (homepage; subpages redirect to home) |
| P3 | Reprtoir | independent (FR) | all-in-one workspace for labels & publishers: catalog + release builder + royalty accounting + contracts; hands delivery off to distributors/DSPs | 350+ teams, labels & publishers | A (Tier-1 documentation site + API reference) |
| P4 | Curve Royalty Systems | Jamen Capital + Merlin (acquired 2026) | royalty-accounting specialist for labels & publishers (recording + publishing royalties); no distribution, no release ops | 800+ labels, publishers, rights holders (incl. Domino, Cooking Vinyl, Mad Decent, Backlot/UMG) | A (official site + feature pages; KB index observed) |
| P5 | Labelworx | independent (UK, since 2007) | distribution partner + label tool suite (RoyaltyWorx, DemoWorx, PromoBox) for indie electronic labels | indie electronic labels | A (homepage; LMS login-gated) |

Dropped: IndieFlow (all-in-one label management; unreachable — timed out twice), Musicwork (transport error), DistroKid/TuneCore/CD Baby (distribution-platform products, covered by the sibling pass), LabelRadar (demo-submission exchange; noted as AmpSuite-family A&R surface).

## Sources

Primary (fetched 2026-09-09):

- AmpSuite — https://ampsuite.com (homepage; /labels/manage/royalties → 404; www.beatport.com/labels/manage → 403)
- Label Engine — https://www.labelengine.com (homepage; service subpages redirect to homepage)
- Reprtoir — https://www.reprtoir.com (homepage) + documentation site https://docs.reprtoir.com/ (llms.txt index; pages fetched: about-reprtoir, releases, artists, about-royalty-accounting, contracts-overview) + API reference index
- Curve Royalty Systems — https://www.curveroyaltysystems.com (homepage) + https://www.curveroyaltysystems.com/features/recording-royalties
- Labelworx — https://labelworx.com (homepage; LMS at lms.labelworx.com login-gated)

Reused sibling evidence (fetched on those passes):

- research/music-publishing-management.md (Curve knowledge-base observations; dual-side packaging)
- research/music-distribution-platform.md (boundary statement)
- research/artist-booking-platform.md (AmpSuite migration note)

## Product A — AmpSuite (Beatport)

### Key observations (evidence layer A — official homepage)

- Self-label: "Label tools made simple. An all-in-one hub… This is Ampsuite."; "Beatport's label management software for the music industry."
- One-sentence scope: "Royalties, distribution, promotion, contracts and more are handled in one dashboard, so your releases, roster and business stay aligned." — names roster, releases, and business money in one breath.
- Modules: **Distribution** ("network of digital stores and streaming platforms, including Beatport"); **Marketing** ("our marketing team helps get your music in front of listeners on Beatport, Spotify, Apple Music, Amazon, TikTok, YouTube and more"); **Royalty accounting** ("automates the entire process by importing distributor statements, calculating royalties and creating detailed reports for your artists, labels and licensors"); **Publishing and Neighbouring rights** ("set up publishing entities, register works globally and integrate recording registrations for complete rights management").
- "Integrated platform — Combining distribution, marketing, publishing, royalty accounting and content management."
- Audience breadth: "Made for every client — Whether you are an independent record label or a distribution company." Quote-form role list: Label, Label Group, Distributor, Artist, Artist Management, A&R Team, Music Supervisor, Accountant, Royalty Officer, Publisher, Songwriter.
- External-facing surface: "Give your artists a dashboard so they can access updates themselves."
- Catalog migration: "Move your back catalog — Easy catalog ingestion directly from the Beatport store."
- Family surfaces: LabelRadar (demo management / A&R submission), Hype (label growth), Beatport Tickets.
- Limitation: subpages unreachable (404/403) — operational workflow detail not directly observable; module internals held at positioning strength.

## Product B — Label Engine (Create Music Group)

### Key observations (evidence layer A — official homepage)

- Self-label: "Label Engine empowers thousands of labels and distributors to maximize their earnings and increase their global footprint."
- Four named services: **Distribution** ("Upload your music instantly to Apple Music, Spotify, Beatport, iTunes, Amazon, TikTok, YouTube, and hundreds of other digital stores"); **Accounting** ("accounting & royalty processing system lets you process statements and pay your artists within seconds, not hours"); **Promotion** ("promotional tools get your tracks to the people that matter most"); **Demo Management** ("Get all your artist demos in one place, accept and reject tracks in seconds with our instant communication tools").
- Multi-imprint evidence (customer testimonial): Insomniac Music Group "grew our business from one label to now over twenty imprints" — label groups/imprints are a real customer structure.
- Limitation: all service subpages redirect to the homepage — module internals undocumented; "within seconds" is a vendor claim, not observed workflow.

## Product C — Reprtoir

### Key observations (evidence layer A — Tier-1 documentation + API reference)

- Self-label: "All-in-one workspace for record labels and music publishers"; "One Platform to Handle All Things Music Business"; teams "manage assets, releases, playlists, contacts, operations, rights, sales, statements, analytics, and more." SaaS, desktop web.
- **Catalog objects**: Albums, Tracks, Videos, Works, Products — held as assets in Catalogs (containers), with Tags; identifiers carried per asset (UPC, ISRC, ISWC, provider-specific codes); bulk importers (spreadsheets, Spotify, YouTube, Shopify, audio/video files, FTP); metadata enrichment; Audio AI auto-tagging.
- **Party objects**: Artists (name, legal name, country, Spotify/Apple/YouTube IDs, IPI, ISNI, tags, associated rights-holders; "usually created on the fly when adding Assets"), Record Labels (an API object; changelog: "Producers renamed to Record Labels"), Songwriters, Music Publishers, Contributors, Contacts, Companies (statement providers, clients, rights-holders).
- **Release object** (delivery-facing): "A Release represents the delivery-ready version of an Album… one Release equals one delivery instance." Created from an Album, inherits metadata/audio/artwork, adds Recipient (Reprtoir Distribution, DSP, or Distributor), territories, pre-order and release dates. Statuses: Draft → Submitted → Released → Taken Down; validation errors surfaced per release. Delivery channels: Reprtoir Distribution, Direct-to-DSP Delivery, Direct-to-Distributor Delivery (Believe, The Orchard documented as recipients). Release Builder product line: "creating pre-formatted (meta)data packages compatible with distributors."
- **Contract object**: "an active accounting object that governs how money flows" — not a passive document. Money In contracts (identify the Payer of an Income; mandatory when creating incomes; not linked to assets) vs Money Out contracts (define royalty splits and terms; must be linked to Assets to calculate royalties). Templates by rights type: Label Contracts (audio/video assets), Publisher Contracts (works), Other. Cross-collateralization groups multiple Money Out contracts for recoupment.
- **Royalty accounting loop** (documented end-to-end): revenues/costs recorded against Contracts → each movement generates internal Operations (debit/credit entries) → automated recoupments and cross-collateralization across contracts of the same rights-holder → Contract Balance visible at any time → at period end, balances close and transfer to the Rights-Holder Balance → Statements generated from the Rights-Holder Balance → issued statements lock the period and appear in the rights-holder's portal → Payments tracked against statements. "This workflow ensures full traceability from raw revenues to final payouts."
- **Royalty accounting definition** (vendor's own): "a specialized accounting practice… It relies on contractual logic rather than simple invoices or sales records. It must account for advances, royalty splits, recoupments, cross-collateralization, deductions, escalations, minimum guarantees, and territory or usage specific rules." Positioning: "not a replacement for general accounting software… a structured layer on top of general accounting."
- **Prerequisites** (vendor-documented): catalog assets with identifiers; parties present (statement providers, clients, rights-holders); contracts configured and linked to assets; organization currency set.
- **Statement ingestion**: "180+ statement providers already supported" — retailers, distributors, aggregators, performance/mechanical/neighbouring rights organizations (documented per-provider: Spotify, Beatport, Believe, The Orchard, Symphonic, DistroKid, PIAS, ADA, Ingrooves, UMG, WMG, SACEM, The MLC, Music Reports, Traxsource, Shopify…). Processing pipeline documented: download → prepare → import → mapping → error rules/quarantine → review before calculation → calculation → final review; reprocessing and revert accounting exist.
- **Other income classes**: sync (track/work), license (track/album/video/work), sale product, direct incomes; Expenses: fees, advances.
- **External-facing surfaces**: Rights-Holders Portal (statements, balances); withholding-tax documentation (Form 5000-class) for paying foreign rights-holders.
- **Other modules**: Playlists/Music Sharing (create, share, public pages, traffic analytics); Reprtoir Inbox (send/receive assets with collaborators); Sales Analytics; CWR import/export (publishing society delivery); team settings; API with full CRUD on albums/tracks/works/videos.

## Product D — Curve Royalty Systems

### Key observations (evidence layer A — official site + recording-royalties feature page; KB index observed)

- Self-label: "Music Royalty Software"; "A Complete Royalty System for Record Labels and Music Publishers"; "Make royalties better."
- Problem statement (vendor's own): "Record label royalty management runs on volume and precision. Ingesting sales data from multiple distributors, calculating on complex contract terms, generating statements that hold up to scrutiny and doing all of it at the pace your royalty cycle demands."
- **Contract database**: "From simple profit shares, to complex royalty terms for specific uses, sources or price categories"; "Manage deductions and mechanical deductions from your artists, as well as managing cost recoupment rates per contract"; "Rate escalations can be managed, tracking and escalating on specific terms"; "The contract database can be configured to match your royalty reporting needs. You decide which channels, formats, price tiers, territories etc. to target & make available in your contract terms. You can break out any income stream or cost & set specific rates."
- **Ingestion**: "Curve can ingest any data from any DSP, Distributor or any source, in its original format. Use our template library, or tell the system how to read the data. Configure once, and the system remembers how to read your files."
- **Statements + Creator Dashboard**: "Clear and concise statements lets your artists and composers know exactly where they stand"; "grant your artists or composers access to retrieve their royalty statements, data & analytics" ("no longer stuck emailing 100-page PDFs").
- **Payments**: Royalty Payments feature; payment rails via CurrencyCloud (footer legal).
- **Mechanicals (mirror seam to publishing)**: "Manage your mechanical reporting to publishers for US mechanicals. Create mechanical reports for AP1 reporting to MCPS from sales uploaded into the system."
- **Dual-side**: "Curve works equally well for Publishers as owners of Masters copyrights. Cascading IP chains capture all the controlled & uncontrolled rights of your works."
- **Posture options**: Curve Services (fully managed royalty processing on the client's behalf); Curve Lite (edition for independent record labels); user privileges "View, Edit or Restricted access for each of the main areas."
- **What it lacks**: no distribution pipeline, no release planning, no promotion tools, no demo intake — the royalty pole of the sample.
- Scale claim: "over 800 labels, publishers and rights holders" (marketing figure); acquired by Jamen Capital and Merlin (announced Jun 2026, completed Aug 2026).

## Product E — Labelworx

### Key observations (evidence layer A — official homepage)

- Self-label: "the world's largest independent digital distribution partner for indie electronic music labels"; © 2007-2026 ("almost 20 years") — the oldest generation in the sample.
- Services: **Distribution** (delivery network "major DSPs alongside emerging platforms"), **Promo** (PromoBox), **RoyaltyWorx** (royalty accounting), **DemoWorx** (demo management), **Elevate** (label development).
- "360 Label Management — We can support you with every aspect of the day-to-day running of your label and lighten your workload so that you can focus on signing great music." — services-plus-software posture.
- "Stress-Free Accounting — …take full control of your label's finances to pay your artists on time, streamline the way you manage complex royalty data, and keep on top of contracts."
- Client system accessed at lms.labelworx.com ("LMS" — label management system naming).
- Adjacent revenue machinery: monetised UGC management (TikTok/Instagram/Twitch Content ID), playlist promotion, YouTube Content ID audits, "Accurate Data & Insights."
- Limitation: LMS internals login-gated; observations held at homepage strength.

## Cross-product Comparison

| Dimension | AmpSuite | Label Engine | Reprtoir | Curve | Labelworx | Strength |
|---|---|---|---|---|---|---|
| Self-label | "label management software" | labels & distributors platform | "workspace for record labels and music publishers" | "royalty system for record labels and music publishers" | distribution partner + label services | — |
| Catalog of record (controlled recordings as managed assets) | ✔ "content management" + back-catalog ingestion | ◐ implicit via distribution | ✔✔ explicit (albums/tracks/works/videos/products, catalogs, identifiers, bulk import) | ◐ recordings held for royalty matching | ◐ implicit | B (5/5 in some form; deep in 1) |
| Artists/rights-holders as managed parties | ✔ roster named + artist dashboard | ✔ artists paid | ✔✔ artists as contributor records + rights-holders + companies/contacts | ✔ contract parties + creator dashboard | ✔ artists paid | B (5/5) |
| Contracts as structured money terms | ✔ named module | ◐ not surfaced | ✔✔ full engine (money in/out, splits, recoupment, cross-collateral, escalations, templates) | ✔✔ contract database (profit shares, deductions, recoupment rates, escalations, per-channel/territory terms) | ✔ "keep on top of contracts" | B (4/5 surfaced; deep in 2) |
| Settlement loop (income → calculate → statements → pay) | ✔ import distributor statements → calculate → reports for artists/labels/licensors | ✔ process statements → pay artists | ✔✔ full documented pipeline (ingest→map→review→calculate→balances→statements→portal→payments) | ✔ ingest→calculate→statements→payments (+payments rails) | ✔ RoyaltyWorx "pay your artists on time" | B (5/5) |
| Release operation (release records, dates, delivery) | ✔ via distribution module | ✔ via distribution module | ✔✔ release instances with lifecycle (Draft→Submitted→Released→Taken Down) + delivery channels | ✖ none | ✔ via distribution network | B (4/5) |
| Distribution pipeline bundled | ✔ (incl. Beatport) | ✔ | ◐ optional channels (own distribution / direct-to-DSP / hand-off packages to Believe, The Orchard) | ✖ | ✔ | variant axis (3 bundled / 1 optional / 1 absent) |
| A&R / demo intake | ✔ LabelRadar (family) | ✔ demo management module | ◐ Inbox (asset exchange, not demo-specific) | ✖ | ✔ DemoWorx | B (3/5 + 1 family) |
| Promotion tools | ✔ marketing module | ✔ promotion tools | ◐ playlists/music sharing | ✖ | ✔ PromoBox + playlist promotion | B (3–4/5) |
| Publishing/neighbouring-rights side | ✔ module (set up publishing entities, register works) | ✖ not surfaced | ✔ works + CWR + publisher contracts | ✔ publishing royalties + mechanicals to publishers (AP1/MCPS) | ✖ not surfaced | variant (dual-side packaging) |
| External party portal | ✔ artist dashboard | ✖ not surfaced | ✔ rights-holders portal | ✔ creator dashboard | ✖ not surfaced | B (3/5) |
| Analytics | ◐ not surfaced | ◐ not surfaced | ✔ sales analytics + playlist analytics | ✔ analytics in dashboard | ✔ "data & insights" | B (3/5) |
| Customer tier | indie labels → distribution companies | thousands of labels & distributors | 350+ teams (labels & publishers) | 800+ labels/publishers/rights holders (incl. major-adjacent) | indie electronic labels | — |

Reading of the table:

- The **catalog + parties + contracts + settlement loop** complex is present in all five products in some form, with depth concentrated in Reprtoir and Curve (the two products whose public documentation is richest). This is the Type's stable center.
- The **release operation** is present in four of five (all but Curve) — the dominant market shape, but not universal; Curve demonstrates a label-serving system without it.
- The **distribution pipeline** is the most variable structure: bundled (3), optional/hand-off (1), absent (1). It cannot be definitional.
- **A&R demo intake, promotion tools, publishing side, portals, analytics** are common-to-variant add-ons, each absent from at least one sampled product.

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The label's catalog of record** — the recordings the label controls (releases/tracks/albums, commercially identified) held as persistent managed assets, together with the artists and contributors behind them. Remove → an upload tool or campaign tracker with no memory of what the label owns.
2. **The deal structure over that catalog** — the label's contractual relationships with its artists/rights-holders (and its pay sources) held as structured, computable money terms (splits, advances/recoupment, deductions, escalations) bound to catalog assets. Remove → a catalog database with no business relationships, or contract documents that compute nothing.
3. **The settlement loop** — income from exploitation attributed to catalog and deals, calculated on the deal terms, and settled as statements and payments to rights-holders. Remove → a delivery utility or catalog DB with no economic loop; a loop without catalog+deals → a generic royalty calculator.

Jointly-held load-bearing tests:

- 1 alone = catalog/asset database.
- 2 without 1 = royalty calculator over nothing.
- 3 without 1+2 = accounting shell.
- 1+2 without 3 = royalty system without settlement (Curve-shaped — the seam toward Royalty Management Platform).
- 1+3 without 2 = delivery + accounting with no contractual artist settlement (distributor-shaped).
- 2+3 without 1 = deal pipeline with nothing to exploit.

### L1 — Common Mature Structure

- **The release-to-market operation** — releases as operational units with dates and status (plan/assemble → deliver or prepare for delivery → available → takedown), realized either through a bundled distribution pipeline or through hand-off packages for external distributors. Present in 4/5; the dominant shape but not the definition (Curve lacks it).
- **Rights-holder/artist self-service portal** — statements, balances, analytics exposed to the label's artists (3/5).
- **Analytics/sales reporting** over the catalog and income (3/5).
- **Multi-label / imprint structures** — label groups operating several imprints in one system (testimony evidence + Reprtoir record-labels object + AmpSuite "Label Group" role).
- **Team/permission machinery** — role-based access for label staff (Curve privileges; Reprtoir team settings).

### L2 — Variant / Optional Structure

- **Distribution posture** — bundled pipeline vs hand-off packages vs none (the sample's sharpest variant axis).
- **A&R / demo intake** — demo inboxes and submission tooling (3/5 + LabelRadar in AmpSuite's family).
- **Promotion tooling** — promo sends, playlist pitching, pre-save/marketing utilities (3–4/5).
- **Publishing/neighbouring-rights side** — works, CWR, publisher contracts, mechanical reporting to publishers (dual-side packaging in 3/5).
- **Managed-services posture** — the vendor runs the royalty process on the label's behalf (Curve Services; Labelworx "360 Label Management").
- **Genre/scene specialization** — electronic-music networks (Labelworx, AmpSuite/Beatport).
- **Scale editions** — lite editions for small labels (Curve Lite).
- **UGC/Content ID monetization** as an income side (Labelworx).

### L3 — Vendor-specific (research notes only)

- AmpSuite: Beatport-store integration and back-catalog ingestion from Beatport; quote-form role taxonomy; LabelRadar/Hype/Tickets family packaging.
- Label Engine: marketing-scale stats (26M+ tracks delivered, 1B+ royalties processed, 15M+ promos sent, 45K+ demos received); Create Music Group ownership.
- Reprtoir: Audio AI auto-tagging and similarity search; Reprtoir Inbox asset exchange; withholding-tax documentation suite (Form 5000/5003); "one Release = one delivery instance" object design; "Producers renamed to Record Labels" API changelog; desktop-web-only posture.
- Curve: CurrencyCloud/Visa payment rails; cascading IP chains; AP1/MCPS mechanical reports; Curve Lite; Curve Services; Jamen Capital + Merlin acquisition (2026).
- Labelworx: PromoBox; monetised-UGC service; lms.labelworx.com naming; Elevate label-development service.

## Vendor-specific Findings

- AmpSuite's Beatport integration and its "distribution company" audience are Beatport-positioning facts, not Type structure.
- Label Engine's "pay your artists within seconds" is a speed claim, not an observed workflow.
- Reprtoir's Release-as-delivery-instance design (one release per recipient) is a product architecture choice; the canonical release is the label's product unit, of which delivery instances are one realization.
- Curve's AP1/MCPS mechanical reporting is a UK/US regulatory realization of the mirror seam to publishers.
- Labelworx's UGC/Content-ID services are adjacent revenue machinery, not label-management structure.

## Rejected Findings

- **"Distribution is definitional"** — rejected. 3/5 bundle a pipeline, 1/5 makes it optional/hand-off, 1/5 lacks it entirely. The sibling distribution pass independently drew the same wall. Held as the Type's most variable structure.
- **"The roster is a first-class object separate from contracts"** — rejected as L0. In the deepest samples the artist-label relationship is realized through party records + contracts; "roster" is the business word for that party population. Held inside the deal-structure leg.
- **"UPC/ISRC/ISWC identifiers are definitional"** — rejected; they are the current common implementation of "commercially identified" assets (era machinery).
- **"Label management includes publishing"** — rejected as definitional; dual-side packaging is a variant (see music-publishing pass).
- **Marketing-scale claims** (26M tracks, 1B royalties, 800+ clients, 350+ teams, "thousands of labels") — kept attributed to vendors, never canonized.
- **"Royalty accounting replaces general accounting"** — rejected; Reprtoir explicitly positions it as a specialized layer on top of general accounting.

## Boundary Findings

- **vs Music Distribution Platform** (ratified from the sibling pass, confirmed this pass): the distribution platform's object world is release→destination→earnings pass-back to the rights-holder account; the label system's object world is catalog+deals+settlement+operations. Labels *use* distributors: 3/5 sampled label systems bundle a pipeline, Reprtoir builds hand-off packages for distributors (Believe, The Orchard documented), Curve has none. Remove the deal/settlement structure from a bundled product → it becomes a distribution platform; remove the destination network from a label suite → it stays a label system (Reprtoir proves it).
- **vs Music Publishing Management** (ratified): masters/releases vs works/compositions. Dual-side products (Curve, Reprtoir, AmpSuite) serve both; the mirror flow is label→publisher mechanical reporting (Curve documents AP1/MCPS mechanical reports generated from sales). Cross-reference, not merge.
- **vs Royalty Management Platform** (UNPROCESSED sibling — flag for that pass): the money loop (ingest→calculate→statements→payments) is shared machinery. Discriminator recorded from this side: the subject. Record Label Management holds the label's catalog + roster + deals + release operations as its center; an industry-agnostic royalty platform computes over arbitrary licensee/product bases with no label operations. Curve-class music royalty specialists sit on this seam (royalty-only, no release operations, music-specific subject) — that pass should decide whether music-specialized royalty systems belong to its Type or to this one; this pass holds them as the money-leg pole of the label-tool family, adjacent to the seam.
- **vs Performing Rights Management** (ratified): society-side vs rights-owner-side. Societies/PROs appear in this Type's income loop as pay sources (Reprtoir documents SACEM/MLC/PRO-class statement ingestion).
- **vs Music Promotion Platform** (ratified): the promotion platform is a two-sided curated-submission exchange with independent curators; label systems' promotion tools are in-house campaign utilities for the label's own releases. Different object worlds.
- **vs Artist Booking Platform / Talent Agency Management** (ratified): live-performance transactions and representation vs recorded-music catalog economics. AmpSuite's own migration from booking tooling to label management confirms the market separates these.
- **vs Media Rights Management**: the rights system of record holds structured grants (licensing in/out with scopes) and resolves availability; label systems hold deals over their own catalog for settlement. Sync licensing touches both; the label system's center remains roster/catalog/settlement.
- **vs Accounting Software**: royalty accounting is contractual logic (splits, recoupment, cross-collateralization), not general bookkeeping; Reprtoir explicitly positions it as "a structured layer on top of general accounting," with outputs designed to integrate into standard systems.
- **"去掉什么就变成另一个 Type" 判据**: remove catalog+deals+settlement → a distribution pipeline or promo tool; remove the settlement loop → a catalog/delivery tool (distribution-platform or catalog-DB territory); remove the catalog binding → a generic royalty calculator (royalty-management territory); replace the masters subject with works → music publishing management; make the royalty base industry-agnostic → royalty management platform; make the transactions live-performance → artist booking.

## Uncertainties

- AmpSuite's operational depth (release workflow, contract modeling, royalty calculation internals) is undocumented publicly (subpages 404/403; Beatport 403) — held at homepage/positioning strength.
- Label Engine's module internals are undocumented (subpages redirect to homepage).
- Labelworx's LMS internals are login-gated; RoyaltyWorx/DemoWorx details not directly observed.
- Curve's catalog/release object depth is inferred from royalty-matching needs and the publishing pass's KB observations, not from a fetched catalog-documentation page — held at B/C layer.
- Whether a pure "release-planning-without-distribution" label product exists as a distinct market shape (IndieFlow-class, unreachable) — unverified; one reason the release operation is held at L1 rather than L0.
- Enterprise major-label systems (Counterpoint-class) not directly documented — enterprise variant held at lineage strength (carried from the publishing pass).
- Exact statement-provider counts (180+) and client counts (800+, 350+) are point-in-time marketing figures.

## Final Synthesis

A Record Label Management application is the record label's business system of record. Its defining core is three jointly-held structures: the label's **catalog of record** (the controlled recordings — releases/tracks, commercially identified — with their artists and contributors); the **deal structure** over that catalog (the label's contracts with its artists and rights-holders held as structured, computable money terms — splits, advances and recoupment, deductions, escalations); and the **settlement loop** (exploitation income ingested from heterogeneous pay sources, matched to the catalog, calculated on deal terms, and settled as statements and payments to rights-holders, with balances, period closes, and portals). Around that core, mature products add the release-to-market operation (release records with dates and status, delivered through a bundled pipeline or handed off as packages to external distributors), artist/rights-holder self-service portals, analytics, A&R demo intake, promotion tools, and — in some products — the publishing/neighbouring-rights side. The distribution pipeline is the Type's most variable structure (bundled / hand-off / absent), which is exactly what separates this Type from the Music Distribution Platform: labels use distributors, and the label system is what remains when the destination network is taken away. The Type is bounded against publishing management by the masters-vs-works seam, against royalty platforms by its label-operations subject, against performing-rights management by the society-side wall, against promotion platforms by the exchange-vs-in-house-tool seam, and against general accounting by royalty accounting's contractual logic.
