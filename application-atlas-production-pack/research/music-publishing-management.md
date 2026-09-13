# Research Notes — Music Publishing Management

## Research Goal

Understand what software of the "Music Publishing Management" type actually is from real products: what objects it manages (works/compositions vs recordings), who uses it, how the publishing business loop (catalog → entitlement → income → distribution) is realized in systems, and where its boundary lies against Royalty Management Platform, Record Label Management, Music Distribution Platform, and Performing Rights Management.

## Initial Boundary

- Working hypothesis: this Type is the **publisher-side system of record for musical works (compositions)** — managing the work catalog, the writer/publisher ownership structure of each work, and the money that flows from the work's exploitation.
- Likely confusions:
  - **Royalty Management Platform** (generic, cross-industry) — shares the money loop.
  - **Record Label Management / Music Distribution Platform** — shares catalog + royalty mechanics but centers on **sound recordings (masters)**, not compositions.
  - **Performing Rights Management** — PRO/CMO-side (the society), not the rights-owner side.
  - **Music Promotion Platform** — pitching/curators, no entitlement or collection core.
- The composition vs recording seam is the suspected load-bearing differentiator inside the music domain.

## Research Questions

1. What is the central object — "song", "work", "composition" — and how is it kept distinct from recordings/tracks?
2. How are writers (composers/authors) and publishers recorded? What party identifiers exist (IPI/CAE, society memberships)?
3. How are shares recorded (writer share vs publisher share, controlled vs uncontrolled, owned vs collected, per-territory)?
4. How does income flow: from which pay sources, via what ingestion, matched to what, calculated against what, distributed to whom?
5. How does registration/delivery to societies (PRO/CMO, CWR) work and is it definitional or optional?
6. What contract/deal machinery exists (writer contracts, co-publishing, sub-publishing, administration, advances, recoupment, escalations)?
7. What external-facing surfaces exist (writer portals, licensing front-ends)?
8. What user roles operate the system?
9. Where exactly does this Type stop and Royalty Management Platform / Record Label Management begin?

## Representative Products

Selected for market coverage across customer tier and product philosophy:

| Product | Pole | Why selected |
|---|---|---|
| Songtrust | Self-serve publishing administration for songwriters/independent rightsholders (Downtown company) | consumer/prosumer end; collection-as-a-service; strong public help center |
| Curve Royalty Systems | Royalty accounting + rights management for labels AND publishers (independent/indie-to-mid, 800+ clients claimed) | publishing royalty accounting depth; full public knowledge base |
| Reprtoir | All-in-one SaaS workspace for small/indie labels & publishers (France) | modular catalog + royalty accounting; unusually complete public documentation |
| Synchtank | Music operations platform (catalog + rights + sync licensing + royalties via IRIS) for publishers, libraries, labels, broadcasters | sync-licensing-centered philosophy; B2B mid/enterprise |

Deliberately not sampled (access constraints): enterprise systems used by major publishers (e.g., Counterpoint Systems class); Kobalt's internal platform. Historical check done conceptually (see Historical Check below).

## Sources

All accessed 2026-09-08.

**Songtrust (official)**
- https://www.songtrust.com/ (positioning)
- https://www.songtrust.com/platform-features (features: global collection network, song registration, YouTube claims, ISRC lookup, royalty report dashboard, sync, access management, song monitoring, payment & tax dashboard)
- https://www.songtrust.com/how-global-royalty-collection-works (65+ societies, quarterly payouts, pay-source taxonomy)
- https://help.songtrust.com/knowledge (help center index)
- https://help.songtrust.com/knowledge/account-registration (songwriters, splits, ISRC/ISWC, registration process, identity verification)
- https://help.songtrust.com/knowledge/collecting-royalties (royalty types: mechanical, performance, sync, print, unallocated/black box, DART, neighboring rights; writer vs publisher share)
- https://help.songtrust.com/knowledge/whats-the-difference-between-the-writers-share-and-publishers-share (administration agreement semantics)

**Curve Royalty Systems (official)**
- https://www.curveroyaltysystems.com/ (positioning, feature set)
- https://www.curveroyaltysystems.com/features/publishing-royalties (CWR, IP chains, contracts, statements, template library, composer dashboard)
- https://help.curveroyaltysystems.com/ (knowledge base index: Curve For Publishers categories)
- https://help.curveroyaltysystems.com/article/116-how-to-add-works-composers-publishers (catalogue = Releases/Tracks/Works/Composers/Publishers; controlled flags; CAE/IPI; linked contracts; participation rates)
- https://help.curveroyaltysystems.com/article/199-ip-chains (IP chain layers; owned vs collected mechanical/performance; validation at 100%; unfit-for-delivery handling; partner-specific chains)

**Reprtoir (official)**
- https://www.reprtoir.com/ (positioning)
- https://www.reprtoir.com/catalog-management (works/tracks/videos/contributors; ISWC/ISRC/UPC/GRid)
- https://www.reprtoir.com/royalty-accounting (contracts on assets; split rates; statement providers; quarantine; balances; statements; payments; rights-holder portal)
- https://docs.reprtoir.com/ (documentation index — llms.txt)
- https://docs.reprtoir.com/docs/works.md (work record fields, per-society identifiers)
- https://docs.reprtoir.com/docs/contracts-overview.md (Money In vs Money Out contracts)
- https://docs.reprtoir.com/docs/publishing.md (CMO filing use case: chain of rights, controlled/uncontrolled)

**Synchtank (official)**
- https://www.synchtank.com/ (positioning; asset management / rights management / licensing & sync / royalty management / data & delivery)
- https://www.synchtank.com/platform (core platform: catalog management, metadata search, user permissions, playlists; modules incl. SyncUp, IRIS royalty management, cue sheets, DDEX delivery)
- https://www.synchtank.com/solutions/music-publishers (publisher solution: control catalog, composition shares, front-end, modules)
- https://www.synchtank.com/faq (rights holders vs rights users positioning)
- https://support.synchtank.net/ (support site: Asset Platform, Royalty Platform (IRIS))

## Product A — Songtrust

### Key observations (Evidence layer A unless noted)

- **Positioning**: "music publishing administration… global song royalty collection". Client is the songwriter/artist/business; ownership retained, administration rights transferred via an administration agreement.
- **Objects**:
  - *Song (composition)* registered in the account: title, writers, splits, music/lyrics ownership question, ISWC article guidance.
  - *Songwriter* records: legal name, IPI/CAE number discussed extensively; outside writers (co-writers not on the platform) supported; band/publishing entities supported; multiple publishing entities question.
  - *Recordings (ISRC)* linked to songs; ISRC lookup tool via Spotify; multiple recordings per song; covers/remixes/arrangements handled by rules.
  - *Royalty income* by type: performance, mechanical, sync, print, YouTube micro-sync, unallocated ("black box"), DART; help center explicitly explains recording-generated royalties and neighboring rights as adjacent, separately-collected categories.
- **Workflow**: add song details → team validates and prepares metadata → delivered to societies **when royalty activity appears** (weekly monitoring status; "Monitoring" state) → royalties flow in from 65+ performance/mechanical societies (ASCAP, BMI, The MLC, etc.) → quarterly payout → Royalty Report Dashboard (where/when/which songs; export).
- **Splits**: help articles "Where Do I Add Publisher and Writer Splits", "How Do I Decide on Splits", "How Do I Register a Song Where I Control 100% of the Publishing But I Am Not the Only Writer", co-publishing share registration.
- **Writer vs publisher share** (key domain semantics): PRO pays the writer's share directly to the writer; the publisher's share is collected by the publisher/administrator. Songtrust as admin collects the publisher share on behalf of the client. (Article verbatim: "Every composition has two sets of rights: the writer's share and the publisher's share.")
- **Surfaces**: signup/account, song registration screens, royalties dashboard, YouTube claims tool (opt-in Content ID delivery; per-channel exclusion), payment & tax dashboard, "Access" feature (multi-login permission sharing for bandmates/managers/businesses).
- **Business model**: commission on collected royalties (help article title references "only take 15" — treat as single-source marketing/help-title evidence; see Uncertainties); no royalty advances (FAQ title).

## Product B — Curve Royalty Systems

### Key observations

- **Positioning**: "complete royalty system for record labels and music publishers"; publishing positioned as core capability, "not a bolt-on".
- **Catalog structure** (publishing side): five interlinked components — **Releases, Tracks, Works, Composers, Publishers**. Works are the publishing core; Tracks/Releases optionally mapped to Works so ISRC/performer/catalogue numbers ride along in CWR deliveries.
- **Party records**:
  - Composer: name (first/middle/surname for CWR), CAE/IPI number, controlled flag (default worldwide, per-work override), per-society memberships and identifiers, optional Publisher Agreement Number (ICE deliveries), linked contract that auto-funnels income.
  - Publisher: internal name + CWR delivery name, main CAE/IPI, controlled flag, performance/mechanical/sync society memberships, linked contract for admin/sub-publishing royalties.
- **Work record**: title + alternates, main identifier (unique and stable across deliveries — societies use it to distinguish new registration vs revision; auto-assign option), ISWC, Tunecode, territories represented, IP chain, linked contracts with participation rates, optional track mapping.
- **IP chain** (the entitlement structure): layers Territory → Publisher → Composer; per party: category (Original / Sub-Publisher / Administrator; writer role: lyrics / music / arrange / adapt / translate), controlled flag, **Owned Mechanicals / Owned Performance** vs **Collected Mechanicals / Collected Performance** (collected may differ from owned; composer collects own writer share directly). Examples given for original publishing, sub-publishing, admin agreement, multi-writer/multi-publisher.
- **Validation**: owned and collected totals must equal 100; validated at save with green tick/red cross; works unfit for CWR delivery are **excluded from deliveries but still accounted normally**.
- **Partner-specific IP chains**: separate chain per delivery partner (e.g., ASCAP vs BMI composer linkage; UNISON digital mechanicals vs PRO digital performance).
- **Income side**: ingest any data from any PRO/publisher in original format; template library ("configure once"); CRD income files; income templates; income upload → calculation on contract terms → writer statements; escalations to raise/lower rates over time; writer contracts category; period & writer statements; payments add-on; creator (composer) dashboard for statements/analytics.
- **Label side adjacent**: recording royalties, mechanical reporting **to** publishers (the mirror image of publishing mechanicals).
- **Admin**: client-managed access; view/edit/restricted privileges per main area.

## Product C — Reprtoir

### Key observations

- **Positioning**: all-in-one SaaS workspace for record labels and music publishers; modular: Catalog Management, Music Sharing, Release Builder, Royalty Accounting, Contracts, Contacts.
- **Work record**: title, language, alt titles, catalog, ISWC, work reference, composers/authors/arrangers, original publishers / co-publishers / sub-publishers / administrators, creation year, duration, lyrics; identifiers tab with per-society codes (ASCAP, BMI, SACEM, PRS Tunecode, SOCAN, SUISA, The MLC, HFA, ICE, Kobalt, Sony Song No., Songtrust Code, etc.); royalties tab (associated contracts); CWR tab; **associated tracks** (work ↔ track linking, incl. automatic linking).
- **Party records**: songwriters, music publishers, contributors, artists, record labels as first-class lists.
- **Contracts** (documented deeply): Money In (who pays the organization; mandatory for incomes; not asset-linked; no royalty calc) vs Money Out (who the organization pays; must be linked to assets; defines splits and terms; "the backbone of royalty accounting"). Publisher Contracts template for Works, Label Contracts for audio/video. Cross-collateralization via contract groups; deduction rules; escalation rules; recoupment logic; minimum payout; custom royalty periods; opening balances (migration); VAT.
- **Royalty accounting pipeline**: statement ingestion from 120+ providers (DSPs, distributors, aggregators, performance/mechanical/neighboring rights orgs — BMI, GEMA, HFA, PRS, PPL, The MLC, SACEM…); statement mapper; quarantine for unfixable rows; error rules; review before calculation → calculation → final review; operations; contract balances; rights-holder balances; statements; payments; reprocessing; revert accounting; rights-holder portal (isolated external accounts).
- **Income taxonomy**: streams, downloads, neighboring, performances, mechanicals, licenses, synchronizations, direct; income types incl. synchro work incomes, license work incomes, sale product incomes, direct incomes.
- **Publishing use cases documented**: Publishing / Co-Publishing / Sub-Publishing / Publishing Administration; CMO filing via CWR declaring the full chain of rights — controlled and uncontrolled shares, contributors and their affiliations; ownership boxes (worldwide).
- **CWR**: importer, exporter, settings, senders, CISAC reference data (receiver codes, society codes, TIS territories).

## Product D — Synchtank

### Key observations

- **Positioning**: "music asset and rights management platform"; serves rights holders (labels, publishers, libraries) and rights users (broadcasters, production companies, DSPs). Explicitly **not** aimed at independent artists/songwriters (FAQ).
- **Core platform**: catalog management centralizing **sound recordings and compositions** "built to industry standards"; composition **shares** UI (ownership splits visible at composition level); advanced metadata search; user permissions; playlist creation/sharing with branded front-end sites for clients/partners to discover works and request licensing.
- **Rights management**: "connect ownership, rights, territories, restrictions and agreements directly to your music catalog."
- **Licensing & sync**: SyncUp CRM (opportunities → quotes → licenses → deal pipeline); micro-licensing (automated e-commerce transactions); productions & cue sheets.
- **Royalty management**: via the IRIS royalty platform (own support section "Royalty Platform (IRIS)"; "royalty calculation, accounting, and reporting"). On the music-publishers page a newer "Royalties" module is flagged "upcoming" — see Uncertainties.
- **Data & delivery**: DDEX and custom-format deliveries; library ingest; data suite analytics.
- **Modular packaging**: modules added as needs grow — royalty depth is purchasable, sync/catalog is the anchor.

## Cross-product Comparison

| Dimension | Songtrust | Curve | Reprtoir | Synchtank |
|---|---|---|---|---|
| Central object | Song (composition) | Work | Work | Composition |
| Works vs recordings separation | Yes (songs ↔ ISRC recordings) | Yes (Works ↔ Tracks/Releases) | Yes (Works ↔ Tracks; auto-link) | Yes (compositions + recordings) |
| Writer/publisher party records | Yes (songwriters, publishing entities, IPI/CAE) | Yes (Composers, Publishers, CAE/IPI, society memberships) | Yes (songwriters, music publishers, contributors) | Creators/rights info (party depth less documented) |
| Share/entitlement structure | Publisher & writer splits per song; music/lyrics ownership | IP chain: territory → publisher → composer; owned vs collected mechanical/performance; controlled flags | Royalty splits per work; chain of rights controlled/uncontrolled; co-/sub-publishing roles | Composition shares (ownership splits) |
| Controlled vs uncontrolled | Implied via administration scope; outside writers | Explicit, per territory | Explicit in CWR filing docs | "Ownership… territories, restrictions" (less explicit in public docs) |
| Society registration/delivery | Core service (validate → deliver at societies; monitoring) | CWR deliveries to delivery partners; optional for accounting-only use | CWR import/export; CMO filing use case | Not documented as society registration; DDEX/data delivery instead |
| Income ingestion | Collection network (65+ societies), quarterly payouts | Any PRO/publisher format; template library; CRD | 120+ statement providers; mapper; quarantine | Via IRIS royalty platform (modular) |
| Calculation & distribution | Admin collects & pays out; dashboard | Contracts/participation → writer statements → payments | Money-out contracts → balances → statements → payments | Royalty calculation/accounting/reporting (IRIS) |
| Contract machinery | Administration agreement (service terms) | Writer contracts, escalations, linked contracts | Money in/out, recoupment, escalations, cross-collateralization | Agreements connected to catalog (depth in IRIS) |
| External portals | Access feature (permission sharing); client dashboard | Creator (composer) dashboard | Rights-holder portal | Branded front-end sites; artist portal |
| Adjacent surfaces | YouTube Content ID micro-sync; sync admin option | Label-side recording royalties & mechanicals to publishers | Playlists/sharing, release builder, distribution | Sync licensing CRM, micro-licensing, cue sheets, AI search |
| Business model | Service commission on collected royalties | Licensed SaaS (+ managed services) | SaaS subscription | SaaS, modular |

### Convergent findings (cross-product, Evidence layer B)

1. **The work (composition) is the center of gravity**, kept clearly distinct from sound recordings; recording linkage exists for identification/matching (ISRC) and delivery completeness.
2. **Entitlement is recorded per work as shares among writers and publishers**, with a controlled/uncontrolled distinction and a writer-share vs publisher-share semantics; publisher role variants (original, co-, sub-, administrator) recur in 3/4 sampled (Synchtank less documented).
3. **Income from many heterogeneous pay sources** (societies, mechanical bodies, licensees, sub-publishers, DSP-adjacent sources) is ingested, matched to works/shares, calculated, and distributed onward via statements and payments.
4. **Society-facing registration/delivery machinery (CWR-class)** is the standard mechanism for making works earn in the collective system — common and prominent, but **optional in at least one product** (Curve: accounting-only use skips IP chains/deliveries; Synchtank documents no society-delivery loop).
5. **External transparency surfaces for writers/rights holders** (portals/dashboards) appear in all four, in different forms.
6. **Catalog organization at scale**: bulk import, identifiers per society, search/filtering — universal.

## Canonical Model (synthesis)

### Defining core (L0 — deliberately minimal)

1. **The musical-work catalog of record** — persistent, individually identified records for compositions (title, identifiers, contributors), managed as the system's primary objects and kept distinct from sound recordings.
2. **The work-level entitlement structure** — who is entitled to each work and in what proportion: writers with their shares, publishers controlling shares (with controlled/uncontrolled and original/co-/sub-/administrator role distinctions), so that income can be routed.
3. **The publishing income loop** — income generated by the work's exploitation (society distributions, mechanicals, synchronization, sub-publishing receipts) is brought into the system, attributed to works and their shares, and distributed onward to writers/rights holders through statements and payments.

Jointly-held load-bearing: (1) alone = a works metadata database; (2) without (1) = party/split bookkeeping with nothing to hang on; (3) without (1)+(2) = generic royalty accounting (Royalty Management Platform territory); (1)+(2) without (3) = a rights registry with no economic loop; (1)+(3) without (2) = royalty accounting with no entitlement model; (2)+(3) without (1) = a contract-to-payment pipeline not bound to works.

### Common mature structure (L1)

- Party records for writers and publishers with PRO/CMO affiliations and society identifiers (IPI/CAE, per-society work codes).
- Registration/delivery of works to societies in industry formats (CWR-class), with validation rules (shares totalling 100%) and uniqueness/stability of work identifiers.
- Recording linkage (works ↔ recordings via ISRC; releases/albums) for matching and delivery completeness.
- Multi-source income ingestion (statement importers, mapping templates, quarantine/error handling).
- Deal machinery: writer contracts, participation rates, escalations, deductions, advances/recoupment, minimum payout, cross-collateralization.
- Income classification by right type (performance / mechanical / sync / print / micro-sync) and source.
- Writer/rights-holder portals; analytics dashboards.
- Bulk catalog tooling (spreadsheet import/export, mass edit, identifiers management).

### Variant / optional structure (L2)

- Customer pole: self-serve administration for songwriters (service + commission) vs publisher-side licensed software vs modular operations platforms.
- Sync licensing workflow depth (opportunity→quote→license pipelines, micro-licensing, branded discovery front-ends).
- YouTube/micro-sync claims machinery (opt-in Content ID delivery; per-channel exclusions).
- Label-side adjacency (recording royalties; mechanical reporting to publishers) in dual-purpose systems.
- Cue sheets/production usage reporting; DDEX data delivery; catalog ingestion of acquired libraries.
- Neighboring rights as an adjacent collection lane (sometimes supported, sometimes explicitly out of scope).
- Multi-catalog/multi-organization setups; regional sub-publishing networks and territorial control splits.
- Historical/enterprise deployment (on-premises royalty suites at major publishers) — inferred lineage, not directly sampled (see Uncertainties).

### Vendor-specific (L3 — research notes only)

- Curve: partner-specific IP chains, "Insert Into IP Chain", Curve Lite, payments via CurrencyCloud, green-tick delivery fitness states.
- Songtrust: "Monitoring" song status, ISRC Lookup Tool via Spotify, weekly royalty-activity monitoring, identity-verification flow.
- Reprtoir: Reprtoir Sheets, Metadata Collector bot, Audio AI tagging, Organization Portal, serverless processing claims.
- Synchtank: SyncUp, IRIS, AI Stems, Library Ingest, Data Suite module names; "54+ million assets" claim.

## Historical / Market-Sample Check (§24-style)

- Pre-digital analog workflow: a publisher's song ledger / copyright registry (works registered with title, writers, shares), session **split sheets** (writer shares agreed and recorded), society/paper statements allocated to works, and royalty disbursements to writers — satisfies all three defining legs with no software, no ISWC, no CWR, no cloud.
- Early digital publishing royalty systems (1980s–90s era, e.g., the class of systems later run by major publishers) kept the same three structures.
- Modern sampled products add identifiers, formats, portals, licensing workflows — all classified as L1/L2, none required by the definition.
- The definition names no specific society, standard (ISWC/CWR/DDEX), income type mix, or business model (commission vs license), and no deployment model.

## Vendor-specific / Rejected Findings

- Rejected as definitional: society registration (optional in Curve; absent in Synchtank's public docs), CWR specifically, YouTube claims, sync licensing CRM, playlists/front-ends, escalation/recoupment machinery (a royalty-accounting refinement, not the Type), the 15%-class commission (single-source business-model detail), "65+ societies" style network claims.
- Rejected as overfit: works-tracks auto-linking, per-society identifier picklists, owned-vs-collected four-way split (a rigorous implementation of the entitlement concept — canonical abstraction is simply "owned/entitled share" + "collected share").

## Boundary Findings

- **vs Royalty Management Platform (generic)**: shares the income→statement→payment loop. The publishing Type is distinguished by its subject: compositions and the writer/publisher share structure under music rights semantics. Remove the work/entitlement core and the system collapses into generic royalty software.
- **vs Record Label Management / Music Distribution Platform**: those center on masters, releases, artist deals, and DSP delivery. Publishing tools center on works. The overlap is real and deliberately served by dual-side products (Curve, Reprtoir: recording royalties AND publishing royalties; label mechanical reporting *to* publishers is the mirror seam).
- **vs Performing Rights Management**: PRO/CMO-side systems administer public performance rights for the whole market (membership, distributions from the society out); publishing management is rights-owner-side, managing one catalog and its receipts across many pay sources.
- **vs Music Promotion Platform**: promotion = pitching to curators/audiences; publishing management = entitlement + collection; no overlap in core loop.
- **vs Intellectual Property Management / Media Rights Management**: generic IP systems lack the music-specific rights taxonomy (writer/publisher shares, PRO/CMO network, mechanical/sync right types); media rights management covers broader media assets without the society-collection loop.
- **"Remove what to become another Type" test**: remove works orientation → record label/royalty tool; remove entitlement structure → MAM/catalog DB; remove income loop → rights registry; generalize the subject → royalty management platform.

## Uncertainties

1. **Synchtank royalty depth**: public docs show royalty management as a modular capability (IRIS platform with its own support section), while the music-publishers page describes a newer "Royalties" module as "upcoming". Assertion strength for Synchtank's royalty loop kept moderate.
2. **Songtrust commission rate**: a help-center article title references "only take 15"; treated as single-source, marketing-adjacent evidence; not promoted to the final document.
3. **Enterprise/major-publisher systems** (Counterpoint-class) not directly researched; enterprise variant described only at lineage level.
4. **Writer-share payment mechanics** (whether societies pay writers directly varies by territory and by reciprocal vs direct affiliation): documented conceptually by Songtrust; territory-specific mechanics not verified across the sample.
5. **Party-record depth at Synchtank** (writer/publisher registries comparable to Curve/Reprtoir) not confirmed from public docs.
6. No precise numeric claims (payout schedules, limits, rate percentages) were promoted from any source; all such details stayed vendor-specific.

## Final Synthesis

Music Publishing Management software is the **publisher-side system of record for compositions**: it keeps the work catalog, records who owns/controls each work and in what shares (writers vs publishers, controlled vs uncontrolled), and runs the money loop that turns exploitation of those works into attributed, calculated, and distributed income. Around that core, mature products add society registration (CWR-class delivery), party registries with society identifiers, multi-format income ingestion, contract machinery, writer portals, and — in some philosophies — sync licensing workflows or self-serve collection services. The Type is bounded against generic royalty platforms by its work/entitlement subject, against record-label tools by the composition-vs-recording seam, and against PRO-side performing rights management by being rights-owner-side rather than society-side.
