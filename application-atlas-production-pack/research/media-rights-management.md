# Research Notes — Media Rights Management

## Research Goal

Understand what the market means by "media rights management" software (§27 Media, Entertainment, Creator & Culture), establish the defining structure of this Application Type, and separate it from the neighboring money system (Royalty Management), the neighboring custody system (Media Asset Management), the neighboring delivery system (Content Distribution Platform), and generic legal/contract systems.

## Initial Boundary

Working hypothesis at start: the phrase is ambiguous between two readings:

1. **Business rights management** — the media organization's system of record for content rights: acquisitions, license grants, territories/channels/windows, availability, conflicts, expiries. This is operator-facing software with a rights department sitting at it.
2. **Digital rights management (DRM) enforcement technology** — encryption/licensing technology controlling playback and copying of media (Widevine/FairPlay/PlayReady-class). This is infrastructure, not an application with an operator workflow.

The directory places this leaf between "Media Asset Management / MAM" and "Royalty Management Platform", beside "Music Publishing Management" and "Performing Rights Management" — all business-side rights systems. The researched market corroborates reading 1: vendors that sell to this space use "rights management" for the business-permission system of record. Notably, FADEL's own product copy uses "Digital Rights Management" to mean **usage-rights data on assets** ("Know your rights – what content can be used how, when and where"), not encryption. No sampled vendor surface sells a playback-enforcement product under the "media rights management" name. Reading 2 would also fail the historical check (enforcement tech is inherently digital-era). Decision: define this Type as the business rights system of record; record the DRM reading as a taxonomy note.

## Research Questions

1. What are the core objects? (titles/properties/works/assets, agreements, grants, territories, windows, platforms)
2. How does an acquisition flow into a recorded grant?
3. How does the system answer "may this be exploited here, now, on this channel?" — and its inverse "what is available to sell?"
4. What state does a grant carry (window, exclusivity, scope) and how do expiry/renewal/takedown loops work?
5. How is the money layer (advances, guarantees, royalties, cash in/out) related — core or attached?
6. Where is the boundary with Royalty Management, MAM, Content Distribution, CLM, and DRM technology?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Rightsline (incl. the RSG Media RightsLogic and FilmTrack lines now under the same platform) | Enterprise media & entertainment: studios, broadcasters, streamers, publishers | The clearest documented avails/conflict/deal machinery; market consolidation signal (rsgmedia.com resolves to Rightsline; Rightsline footer carries FilmTrack pages) |
| FADEL (IPM Suite + Brand Vision) | Cross-industry licensor/licensee/publisher + brand-content clearance | Different philosophy: licensing-lifecycle suite spanning media, publishing, toys, sports; plus the content-workflow clearance pole (rights bound to assets inside DAM/creative toolchains) |
| Klopotek (Contracts, Rights & Royalties / Rights Sales Solution) | Book & journal publishing | Different industry vocabulary and workflow: acquired rights vs available-to-sell, subsidiary rights sales pipeline, rights accounting with author shares |
| Vubiquity (Content Licensing service) | Negative probe / services pole | Rights licensing delivered as a managed service (curation/licensing for telcos & OTTs) rather than operator software — the periphery of the Type |

## Sources

Fetched 2026-09-08 (all Tier 2 — official vendor product/marketing pages; Tier 1 help centers attempted but unreachable):

- Rightsline — root, /solutions/rights/, /features/avails-and-conflict-engine/ (https://www.rightsline.com/)
- FADEL — root, /ipm-suite/, /brand-vision/ (https://fadel.com/)
- Klopotek — root, /contracts-rights-and-royalties (https://www.klopotek.com/)
- Vubiquity — root, /service/content-licensing/ (https://www.vubiquity.com/)
- RSG Media — https://www.rsgmedia.com/ (redirects to Rightsline)
- docs.rightsline.com and help.rightsline.com — transport errors (not retried)

## Product A — Rightsline (Rightsline platform, incl. RightsLogic/FilmTrack heritage)

### Key observations (Evidence layer A)

- Positioning: "The #1 Rights & Royalties Software Platform… powering IP commerce". Rights Management = "Simplifies, tracks, and manages IP workflows across development, acquisition, distribution and exploitation."
- Central repository "captures every IP asset you own, manage, have licensed, or can sell" — the catalog spans owned, managed-in, and sellable-out IP.
- Core pitch: "See what you own, what you've sold, and where you have new revenue opportunities."
- **Avails & Conflict Engine (ACE)**: multi-dimensional availability across "Territory, Language, Platform, Time"; real-time recalculation "as rights are added, changed, or removed"; "flexible conflict logic… how overlaps, exclusivities, and restrictions are treated"; results with subgrids and heatmapped summaries showing "which rights contributed to each result"; cross-module awareness ("contracts, titles, rights, and royalties all connected").
- Deal workflow: Rights Explorer with "lightning-fast Avails search partnered alongside Conflict Check to ensure no double-selling"; "DateMath™ with Relative Rights Profiles to define strategic rights windows with date-based alerts"; "approve deals and generate contracts with Docusign"; avails → deal memo → contract "seamlessly, with zero re-entry or data loss."
- Cash layer: "calculates allocations and generates accounting documents while tracking payment milestones and currency exchange rates" (cash in / cash out).
- Feature list on the rights page: Catalog & Inventory Management, Availability Reporting, Conflict & Collision Checks, Workflow Engine, Partner/Statement Portals, Opportunity tracking, Fulfillment processing, Self-service reporting, Allocation and Amortization calculations, extensive API, Date Alerts, Rights Windowing with Date Math.
- Granular role-based permissions; configurable workflows "no engineers needed"; Report Builder; integration partners.
- Customer stories span studios, broadcasters (ABC Australia "inventory management"), streamers (Spotify "contract and rights management"), publishers (Vista Higher Learning "rights negotiations"), music licensing body (PPL "music royalties and licensing").

## Product B — FADEL (IPM Suite; Brand Vision)

### Key observations (Evidence layer A)

- IPM Suite positioning: "Rights & Royalty Management for Midmarket to Enterprise Licensors, Licensees & Publishers."
- Three audiences: **Licensors** (outbound: "Check conflicts, collisions, and compliance; manage rights and royalties across licensees"), **Licensees** (inbound: manage licensed content and parts, automate royalty processing, "manage audits and track violations"), **Publishers** (rights and permissioning of content).
- **Deal Management**: "Negotiate deals, capture even the most complex agreement terms… deal history for a complete audit trail."
- **Rights Management**: "Structure rights hierarchies, advances, guarantees, payment schedules, and royalty rates. Easily search deals and check for collisions and clearance." FAQ: "Define and enforce rights by property, region, and media type; prevent conflicts with collision checking and hole analysis."
- **Royalty Management**: usage/sales processing, royalty calculation and validation, statement generation, minimum-guarantee recoupment; **Accounting Engine** integrates ERP AP/AR/GL.
- Also: product approvals (licensor approval of licensed products), forecasting, licensee/statement portals, DAM module, AI analytics (AIVA), **Contract Ingestion** ("reads any format, extracts rights and obligations, and instantly creates parties and agreements").
- **Brand Vision** (content workflow): Talent & Agreement Management ("single 'rights' source for talent, agreements… Enrich DAM assets with usage rights"); "Digital Rights Management" defined as "Know your rights – what content can be used how, when and where"; **Clearance Check** ("Clear asset usage rights for your campaigns before distribution"); AI content tracking of published images/video to "flag for renewal or takedowns"; workflow engine covering "approvals, expiration alerts, rights requests, takedowns, and renewals"; "Defend Against Claims" (usage-rights reports); connectors into external DAM systems (Aprimo, Bynder, AEM, Cloudinary, …) — the rights layer sits **on top of** asset stores rather than replacing them.
- Case studies: Pearson ("global system of record for content rights… automated rights clearance… traceability and compliance… agreement management and streamlined royalty calculations"); Comcast ("clearance checks and expiration reporting… self-service rights management"); AI case study "find expired content across 275 sites".

## Product C — Klopotek (Contracts, Rights & Royalties; Rights Sales Solution)

### Key observations (Evidence layer A)

- Publishing-industry suite ("400+ publishers"; HarperCollins, Taylor & Francis testimonials). CRR = contracts, rights, royalties as one module family beside Title Management.
- **Contract Management**: acquisition of IP "from authors, agencies, or other publishers"; overview "of all active projects with status information on rights acquisition, negotiated terms, and monetary aspects"; contract wizard (parties, agency, works/product lists, "agreements for granular content" — components of works); templates; status changes tracked; 360° contract dashboard.
- **Rights Sales Solution** — the outbound leg: "rights managers require a clear overview of which rights have been acquired from an author, and which rights remain available to sell"; problem framing: "ambiguous information about restrictions and the lack of an automated tracking system"; guides the whole sales process "from checking rights availability to sales reporting."
- **Rights Sales Manager**: acquired vs available rights overview; tracks "registered interest and options to the point of contract negotiations and agreement"; payment history; revenue/activity reporting; notes "the increased granularity of the digital rights sphere"; once agreement reached, "track payments and statements due."
- **Rights Sales Contract Manager**: sales contracts auto-generated from negotiated terms; parties, validity, payments, royalty terms, rights; linked acquisition contracts; templates.
- **Rights Accounting Manager**: "sub right claims, incoming payments and generating shares [for the authors]"; licensee statements stored; invoices/claims for installments (advances) and royalty statements; dunning levels.
- **Intercompany / International Publishing Deals**: move rights "flexibly through all legal entities" of a group, report to the author "in one single royalty statement."
- Author Management: royalty recipients, statements to authors/agents (Authors Online).

## Product D — Vubiquity (negative probe)

### Key observations (Evidence layer A, negative)

- Formerly documented as software (AVMS rights/availability suite); current site presents **Content Licensing** as a managed service: "delivering content strategies, licensing rights and entertainment solutions for Telcos, OTTs", curation from "hundreds of content suppliers in 50+ languages", plus media supply-chain services.
- No documented operator software surface for rights records on the current site.
- Interpretation: rights work has a services-delivery variant; the Type documented here is the software system of record that such services either run on behalf of clients or connect to. No product-level claims drawn from Vubiquity.

## Cross-product Comparison

| Structure | Rightsline | FADEL | Klopotek | Assessment |
|---|---|---|---|---|
| Content/IP item catalog (titles, properties, works, assets) | "every IP asset you own, manage, have licensed, or can sell" | properties/characters; assets (Brand Vision) | works/titles, granular content components | **Defining core** (B) |
| Agreements/deals as source of rights, with status + audit trail | deal → contract generation, deal history | Deal Management, audit trail, AI ingestion | Contract Manager, wizard, status tracking | **Defining core** (B) |
| Structured grants: counterparty × scope (territory/region, media/channel/platform, language) × window × exclusivity × money terms | Relative Rights Profiles, DateMath windows; Territory/Language/Platform/Time | rights hierarchies "by property, region, and media type"; advances/guarantees/schedules | acquired rights by scope; validity; royalty terms; installments | **Defining core** (B) |
| Availability resolution ("what may be exploited where/when" / "what is available to sell") | ACE avails engine, real-time recalculation | clearance checks; collision + hole analysis | Rights Sales Manager acquired-vs-available | **Defining core** (B) |
| Conflict/double-sale prevention | Conflict Check "ensure no double-selling"; flexible conflict logic | collision checking; compliance | restriction clarity named as the problem solved | **Defining core** (B) |
| Date alerts / expiry / renewal / takedown loops | date-based alerts; date alerts feature | expiration alerts, renewals, takedowns, content tracking | options & registered-interest tracking; statements due | **Defining core** (B) |
| Royalty/participation computation engine | module ("Simplify Royalties", 25B royalties processed claims) | full royalty engine + statements + MG recoupment | rights accounting (claims, shares, statements) | **Common attached layer** — depth varies; suites bundle it |
| Portals for external parties (licensees/agents/authors) | partner/statement portals | licensee portal, statement portal | Authors Online | Common (B) |
| ERP/finance integration | allocations, accounting documents | Accounting Engine → AP/AR/GL | royalty runs feeding finance | Common (B) |
| AI contract ingestion / content tracking | AI module marketed | AIVA agents | Kleo assistant (webinars) | Era-current implementation, not defining (B, weak) |
| Services-delivered operation (no operator software) | — | — | — | Peripheral variant (Vubiquity) |

## Canonical Model

Three jointly-held structures; remove any one and the product stops being this Type:

```text
Rights-bearing content catalog            (the things rights attach to)
└── Structured rights grants of record    (agreement-derived: counterparty × scope × window × exclusivity)
    └── Exploitation-resolution machinery (availability answers, conflict checks, window/expiry alerts)
```

1. **Rights-bearing content catalog.** Persistent identified records for the exploitable content items — titles, series, episodes, works, properties/characters, images, footage. The catalog holds what is owned, licensed-in, and sellable. Remove → a contract repository or title list without rights semantics.
2. **Structured rights grants as queryable data.** Each grant binds a counterparty to a content item under a scope — media/channel/platform, territory, language, time window, exclusivity — plus attached money terms (advances, guarantees, rates, payment schedules). Grants derive from agreements/deals and are maintained as data, not as documents only, with amendments and audit trails. Both directions exist: grants the organization holds (inbound) and grants it sold (outbound). Remove → a document store; a title database; a CLM system.
3. **Exploitation-resolution machinery.** The system continuously answers "may this item be exploited in this territory, on this channel/platform, at this time — exclusively or not?" and the inverse "which rights remain available to sell or licence?" — recomputing as rights are added, changed, or expire; flagging conflicts (double-selling, exclusivity collisions, holes) before deals are approved; and alerting on windows opening, closing, and content needing renewal or takedown. Remove → a ledger that records but cannot resolve; the spreadsheet pre-history.

Jointly-held is load-bearing: 1 alone = catalog/contract list; 2 alone = contract store; 3 alone = a calculator over nothing; 1+2 without 3 = a rights archive that can't answer daily questions; 1+3 without 2 = availability guesses with no record of the terms; 2+3 without 1 = contract math with nothing to exploit.

### Abstraction Hierarchy

**L0 — Defining Invariant**
- rights-bearing content catalog of record
- structured grants (counterparty × scope × window × exclusivity [+ money terms]) derived from agreements, held as data
- exploitation-resolution machinery (availability, conflicts, expiry alerts)

**L1 — Common Mature Structure** (present across the sample; not definitional)
- royalty/participation computation, statements, MG recoupment, cash in/out documents
- portals for external parties (licensees, agents, authors)
- ERP/finance integration
- workflow engine (approvals, rights requests)
- reporting/dashboards; APIs; role-based permissions
- AI contract ingestion (extract rights/obligations → parties + agreements)

**L2 — Variant / Optional Structure**
- industry posture: film/TV avails-centric; publishing rights-sales-centric (acquired vs available, options, sub-rights); brand/character licensing with product approvals; corporate content clearance bound to DAM assets
- direction emphasis: licensor-side (outbound selling), licensee-side (inbound compliance + royalty payout), or both
- bundled DAM, CRM, forecasting, analytics
- services-delivered operation (rights work outsourced)
- regional/publishing-group machinery: intercompany rights transfer between legal entities

**L3 — Vendor-specific** (research notes only)
- Rightsline: DateMath™, Relative Rights Profiles, ACE heatmaps/subgrids, DocuSign generation, Rights Explorer
- FADEL: AIVA agents (contract ingestion, AI reviewer), PictureDesk, connector exchange to named DAMs
- Klopotek: STREAM web apps, Contract 360°, Intercompany/International Publishing Deals app, Authors Online, dunning levels

### Historical / Market-Sample Check (§24 reasoning)

Paper-era rights department: a rights card/ledger per title recording grants by territory, channel and term; contract files; the ledger consulted before any sale to avoid double-selling; a tickler file for expiries and options; inquiries answered by lookup ("can we still show this in X until when?"). All three L0 legs are present at analog level: the catalog (title cards), the grants as structured ledger entries (not just filed contracts), and the resolution function (manual lookup + tickler). The AI-era machinery (contract ingestion, content tracking) is not needed to satisfy the core. The definition therefore names no platform, no algorithm, no specific dimension vocabulary beyond the conceptual scope of a grant. The DRM-technology reading of the leaf name would fail this check (inherently digital), corroborating the business-rights reading.

## Vendor-specific Findings

See L3 above; none promoted into the canonical document beyond neutral examples.

## Boundary Findings

- **vs Royalty Management Platform (§27 sibling, unprocessed)**: the money-computation engine over usage/sales (splits, statements, payment cycles) vs the permission-of-record and availability system. Overlap is real: every sampled rights suite carries a royalty/accounting layer, and advances/guarantees sit on the grant. Adopted seam: the grant record + resolution machinery is the center here; royalty computation over reported usage is the center there. Joint review requested when that leaf is processed.
- **vs Media Asset Management (§27, processed 2026-09-08)**: MAM holds custody of the media corpus (masters/proxies, storages, movement). Rights management holds the permission terms — no file custody. Evidence: FADEL Brand Vision explicitly *enriches* external DAM assets with rights data and connects to DAMs rather than storing masters; the MAM pass itself listed DRM/watermarking as non-definitional capabilities. Complementary: MAM supplies asset identity; the rights system returns clearance state.
- **vs Content Distribution Platform (§27, processed 2026-09-07)**: that pass recorded "embedded rights windows" as a variant there. Seam: distribution owns the delivery pipeline to destinations; rights owns the terms deciding what *may* be delivered where/when. Embedded rights windows in a distribution product are consumed constraints, not a maintained rights system of record.
- **vs Music Publishing Management / Performing Rights Management (§27 siblings, unprocessed)**: music-industry systems center works/writers/shares and society distributions. This Type is the general content-rights system of record across film/TV/publishing/brands; the music-specific leaves are expected to be domain siblings or variants — flag for those passes.
- **vs Contract Lifecycle Management (§11)**: CLM = legal document lifecycle (drafting, negotiation, signature, obligations) over any contract type; rights management = rights semantics over a content catalog (scope dimensions, availability math). The agreement here is the *source* of structured grants, not the end artifact.
- **vs Intellectual Property Management (§11)**: legal IP portfolios (patents, trademarks, prosecution) vs commercial exploitation permissions over content items.
- **vs DRM enforcement technology**: copy-protection/encryption (Widevine-class) is technical enforcement, not an operator application; it consumes no rights-grant semantics. No sampled vendor surface sells enforcement under this leaf's name; FADEL uses "Digital Rights Management" for usage-rights data. Recorded as a taxonomy note.
- **Remove-test summary**: remove the content catalog → CLM/contract repository; remove grant structure → title database; remove resolution machinery → rights archive/spreadsheet; add media-file custody → drifting into MAM; make royalty computation the center → Royalty Management.

## Uncertainties

- No Tier-1 (help-center) documentation was reachable for any sampled product (docs.rightsline.com and help.rightsline.com transport errors; FADEL support portal requires login; Klopotek detail is on product pages with strong app-level descriptions). Assertions about exact field sets, permission models, or status vocabularies are therefore kept at conceptual strength.
- The exact packaging split between "rights" and "royalties" modules inside suites (Rightsline, FADEL, Klopotek) varies and may be plan-dependent; the boundary with Royalty Management Platform remains provisional until that leaf is processed.
- Rightsline's absorption of RSG Media (RightsLogic) and FilmTrack is evidenced by domain redirects/footer links; detailed per-lineage product differences were not researched.
- Sports-rights and footage/archive-rights specialists were not sampled; their fit with the canonical model is inferred from the shared vocabulary (territory/channel/window), not verified.
- Vubiquity's former AVMS software detail was not reachable; the services-pole reading rests on the current site only.

## Final Synthesis

A Media Rights Management application is the media/content organization's **rights system of record**: it catalogs the exploitable content items, records the rights held over them as structured grants derived from agreements (who may do what, where, on which channel, until when, exclusively, against which money terms), and continuously resolves exploitation questions — what is available to sell or use, where conflicts and holes are, what is expiring — so that the organization exploits content inside its granted terms and monetizes what remains. The royalty engine, the DAM, the distribution pipeline, and the contract department all sit adjacent: money computed over usage, media held in stores, delivery run by distribution systems, documents drafted by legal — but the permission-of-record and the availability answer live here.
