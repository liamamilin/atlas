# Research Notes — Performing Rights Management

## Research Goal

Understand what software of the "Performing Rights Management" type actually is from real products: the society-side (PRO/CMO/MRO) administration of public performance rights — who uses it, what objects it manages (members, works/recordings, licenses, usage, distributions), how the collective loop (license → collect → usage → match → calculate → distribute) is realized in systems, and where its boundary lies against Music Publishing Management, Royalty Management Platform, Media Rights Management, Music Distribution Platform, and usage-monitoring vendors.

## Initial Boundary

- Working hypothesis (inherited from sibling passes): this Type is the **society-side** system — the performing rights organization's own machinery for administering public performance rights for a whole market, not the rights-owner side. music-publishing-management recorded: "rights-owner-side catalog management across many pay sources vs society-side administration of public performance rights for the whole market — the PRO appears in this Type's income loop as a pay SOURCE". music-distribution-platform recorded that industry-body collection (SoundExchange-class) deliberately sits outside the distributor's earnings loop.
- Alternative reading considered and rejected: "performing rights management" as rights-holder-side performing-rights administration (Songtrust-class) — that is inside music-publishing-management's self-serve variant, already documented there.
- Likely confusions:
  - **Music Publishing Management** — publisher-side; the society is a pay source in its income loop.
  - **Royalty Management Platform** — generic contractual royalty computation; the society's distribution is collective/usage-based, not contract-term computation.
  - **Media Rights Management** — grant-of-record lifecycle; the society's center is the money loop + attribution.
  - **Usage monitoring vendors** (BMAT/Tunesat-class) — the observation layer societies buy, not the Type itself.
  - **Works registries** (Songview-class) — data platform without the money loop.

## Research Questions

1. What is the society's system world: members, works/recordings, licenses, usage, distributions — how do they relate?
2. How do rights holders enter the system (membership/affiliation) and how do works/recordings get registered or claimed?
3. How are music users licensed (blanket, per-program, statutory) and how does money come in?
4. How is usage captured (census vs sample, station reports, DSP files, monitoring/MRT, setlists, cue sheets)?
5. How does matching work (usage → works/recordings) and what happens to unmatched usage?
6. How are distributions calculated and paid (rules, weighting, cycles, statements)?
7. How does international reciprocity work (affiliated societies, in/out flows)?
8. What portals exist for members and licensees?
9. Can society machinery be outsourced or shared (multi-society service providers, monitoring vendors)?
10. Would pre-digital societies satisfy the definition (historical check)?

## Representative Products

Selected for market coverage across rights subject, licensing philosophy, jurisdiction, and position in the value chain:

| Product | Pole | Why selected |
|---|---|---|
| ASCAP | Large US PRO (compositions), negotiated blanket/per-program licensing, not-for-profit | the archetypal PRO; exceptionally detailed public payment-system documentation (11 steps, census/sample table) |
| SoundExchange | US sound-recording digital performance society; statutory (compulsory) license collector | different rights subject (recordings + performers) and different licensing philosophy (statutory, not negotiated); digital-native (2003) |
| APRA AMCOS | Australian/NZ society (APRA performing rights + AMCOS mechanicals); century-old | different jurisdiction; explicit 5-step distribution process and data-source taxonomy published; reciprocal administration for affiliates |
| BMAT | Usage monitoring/matching vendor serving CMOs (and broadcasters, DSPs, publishers, labels) | the observation layer pole — proves monitoring is a capability societies outsource, not the Type itself |
| Songview (boundary anchor) | Joint ASCAP/BMI (+GMR/SESAC) copyright data platform | pure registry/reconciliation without a money loop — the "registry alone is not the Type" anchor |

Deliberately not sampled (access constraints): ICE (multi-society licensing/processing JV — icelicensing.com and iceoperations.com both timed out twice); PRS for Music (JS-heavy site, help portal returned a Salesforce CSS error, content paths 404); GEMA/SACEM (language/JS constraints). Historical check done conceptually (see Historical Check).

## Sources

All accessed 2026-09-09.

**ASCAP (official)**
- https://www.ascap.com/about (PRO role, not-for-profit, 1.1M+ members, 20M+ songs licensed, ~90 cents per dollar)
- https://www.ascap.com/help/royalties-and-payment/payment (payment system: 11 steps, follow-the-dollar, track/match/process/pay "more than a trillion performances each year")
- https://www.ascap.com/help/royalties-and-payment/payment/whocollect (blanket vs per-program licenses; 700,000+ licensees taxonomy)
- https://www.ascap.com/help/royalties-and-payment/payment/surveys (census vs sample per medium; APM matching platform)
- https://www.ascap.com/songview (joint copyright data platform; 38M+ works; ingest→reconcile→publish loop)
- Member portal navigation (Member Access: Dashboard, Earnings/Statements/Tax Forms, Works/Cue Sheets/Register a Work/Agreements/OnStage, Profile/Payment Preferences/Designated Users)
- Licensee logins (TV/Cable/Media portal, My ASCAP License general licensing, Radio login)

**SoundExchange (official)**
- https://www.soundexchange.com/about/ (sole US administrator of the Section 114 sound recording license; $13B+ distributed; 850,000+ music creators; SXDirect/Licensee Direct/MDX; international partners 72/91)
- https://www.soundexchange.com/what-we-do/for-digital-service-providers/ (3,000+ DSPs; Licensee Direct: calculate, certify, submit; statutory license eligibility; ISRC search 32M+ recordings)
- https://www.soundexchange.com/what-we-do/for-artists-labels-and-producers/ (registration; Search & Claim recordings; unclaimed royalty lists; Letters of Direction; rates set by Copyright Royalty Board; monthly payments)

**APRA AMCOS (official)**
- https://www.apraamcos.com.au/ (role, 128,000+ members, portals incl. cue sheet clients, works search, Performance Reports, APRA quarterly/AMCOS quarterly/international monthly)
- https://www.apraamcos.com.au/music-creators/membership-explained/distribution-overview (5-step distribution process; census-where-cost-effective/sample-otherwise; ~86 cents per dollar; what royalties are collected for)
- https://www.apraamcos.com.au/music-licences/music-licensing-explained/where-does-my-money-go (licence fee setting by use type; data sources taxonomy incl. MRT; admin costs deducted)

**BMAT (official)**
- https://www.bmat.com/ (positioning: "Operating System for the Music Industry"; serves CMOs, publishers, labels, broadcasters, DSPs, venues, artists; 27B matches daily claim; $2B/yr distributed on its metadata claim; 4,746 companies)
- https://www.bmat.com/cmo/ (CMO-facing products: Vericast fingerprinting monitoring, DSP Processing, Atlas distribution platform, ReSol claim-conflict resolution, member dashboards, Vericast Ads; client logos incl. PRS, SGAE, SIAE, SoundExchange, GVL, KODA, FILSCAP)

## Product A — ASCAP

### Key observations (Evidence layer A unless noted)

- **Role**: US PRO, not-for-profit, founded 1914; licenses 20M+ songs/scores to businesses that play music publicly; pays royalties to songwriters, composers, publishers. "Track, match, process and pay on more than a trillion performances each year."
- **Licensing side**: collects license fees from **licensees** (music users). Most pay a **blanket license** (any music in the ASCAP repertory); some local TV stations opt for **per-program** licenses. 700,000+ licensees spanning: TV networks, local TV, cable/MVPDs, A/V streaming (Netflix, Disney+, Hulu…), music streaming (Spotify, Apple Music…), commercial and non-commercial radio, satellite radio, PBS/NPR, social platforms, game/VR platforms, podcast networks, websites/apps, background music services, colleges/universities, concert venues, symphony orchestras, fitness brands, and "hundreds of thousands" of general licensees (bars, restaurants, hotels, theme parks…). Separate licensee portals per segment (TV/Cable/Media portal, general licensing portal, radio portal).
- **Usage capture**: published **census vs sample** table per medium — e.g., network TV census; local TV mostly sample; radio: 2,000+ stations monitored by Media Monitors (census), others sample; audio streaming: census for performances that auto-match to an ASCAP work ID or exceed a play threshold, sample otherwise; A/V streaming: census for programs auto-matching a cue sheet on file or exceeding view thresholds; live concerts: member-submitted setlists (OnStage) + top-grossing tours census. Explicit policy: as technology gets cheaper, expand census.
- **Matching**: digital data from radio/streaming processed by the **Audio Performance Management (APM)** platform, which "matches performance data to the works registered in ASCAP's databases".
- **Distribution**: "Follow the Dollar" principle — licensing fees collected from TV networks go to TV music creators, streaming fees to streaming performances, etc. ~90 cents of every dollar distributed. Published "Survey and Distribution System" rules document (DRD) governing writer/publisher distribution formulas and weighting. Special monetary programs (Plus Awards) and performance periods/payment methods documented as steps 5 and 9 of the payment system.
- **Member portal (Member Access)**: Dashboard, Messages, Earnings (interactive earnings, Statements, Tax Forms), Works (Cue Sheets, Register a Work, Saved/Drafted Works, Agreements, Plus Awards, OnStage), Profile (Payment Preferences, Designated Users). Work registration online; cue sheet surface; agreements surface.
- **Public repertory**: ASCAP Repertory Search (titles, writers, publishers); **Songview** — joint platform with BMI (expanding to GMR/SESAC): ingests ownership data from each PRO, reconciles per agreed rules, publishes back to each PRO's searchable database; 38M+ works; "authoritative view of public performance copyright ownership and administration shares".

## Product B — SoundExchange

### Key observations

- **Role**: independent non-profit; **the sole organization designated by the U.S. government to administer the Section 114 sound recording license** — collects and distributes **digital performance royalties for sound recordings** (featured artists + rights owners) from non-interactive services (Pandora, SiriusXM, iHeartRadio, thousands more). $13B+ distributed to date; 850,000+ registered music creators. Monthly payments.
- **Licensing side (statutory, not negotiated)**: DSPs are **required by law** to pay for streaming musical content; non-interactive services are **eligible to use the statutory license**. Rates set by the **U.S. Copyright Royalty Board** (not negotiated by SoundExchange). 3,000+ DSPs. **Licensee Direct** service: DSPs "calculate, certify, and submit digital performance royalties" — i.e., the licensee side computes its own obligation and reports it, with usage data (playlists of all recordings played) accompanying payment.
- **Repertoire side**: creators/owners **register** (free) and then **search & claim their recordings** in SoundExchange's database (ISRC-based; 32M+ recordings searchable); rights owners can **submit recordings** not found. Unclaimed royalties maintained as public searchable lists (unregistered artists, partially unregistered artists, unregistered performers, unregistered sound recording owners). **Letters of Direction**: artists redirect a share of royalties to producers/mixers/engineers.
- **Distribution**: royalties (accompanied by playlists of all recordings played) paid by services to SoundExchange; distributed to featured performers and rights owners; monthly cycle. International: 72 partners / 91 agreements collect overseas performance royalties.
- **Surfaces**: SXDirect (creator portal + mobile app: claim recordings, track catalog, review payments), Licensee Direct (DSP portal), Music Data Exchange (MDX — sound recording/publishing data exchange between labels and publishers), ISRC search site.
- **Affiliates**: SXWorks and CMRRA provide back-end administrative solutions for publishers (adjacent, publishing-side).

## Product C — APRA AMCOS

### Key observations

- **Role**: APRA (Australasian Performing Right Association) + AMCOS (Australasian Mechanical Copyright Owners Society); grants licences for live performance, broadcast, communication, public playing or reproduction of members' musical works; distributes licence fees to 128,000+ members and affiliated societies worldwide. A century old ("A century of song").
- **Licensing side**: licence schemes by industry/use (TV/radio, online, events, education, production music, physical formats); fees "determined according to the nature and type of music use" — value-of-use logic (streaming service vs café). **OneMusic**: joint licensing initiative with PPCA (sound recording side) so businesses get one joint public-performance licence. Also administers and collects performing/reproduction rights royalties **on behalf of international affiliate societies** for all their music used in ANZ/Pacific territory (reciprocal representation).
- **Distribution process (published, 5 steps)**: 1) license businesses; 2) collect music data from multiple sources (radio/TV stations, streaming services, live performances, background music services, more); 3) **auto-match data to songs/compositions in the database**; unidentified songs matched to copyright owners by a research team; 4) calculate royalties according to published **distribution rules and practices**; 5) pay royalties to members and overseas societies.
- **Data-source taxonomy**: station reports; DSP/streaming/VoD/website/label reports; **Music Recognition Technology (fingerprinting/audio recognition)**; curated-music providers (e.g., fitness); background-music suppliers' playlist reports; **setlists** from gigs/festivals (member-submitted Performance Reports, incl. covers so original writers get paid).
- **Distribution policy**: "balance using accurate music use data and the cost of collecting that data" — census where cost-effective, sample/similar-source data where not; invests in data-matching systems. ~86 cents per dollar distributed (13.26% expense-to-revenue).
- **Payment cycles**: domestic quarterly; international monthly (dependent on affiliates' own cycles); AMCOS quarterly. Minimum payment threshold exists (single-source precise number — see Uncertainties).
- **Portals**: Writer Portal (songwriters/composers), Publisher portal, Production music clients, **Cue sheet clients** (separate login class); public works search (registered song/work catalogue); mobile app.

## Product D — BMAT

### Key observations

- **Positioning**: "Operating System for the Music Industry" — a vendor serving **CMOs (societies)**, publishers, labels, broadcasters, DSPs, venues, artists. Not a society; sells the observation/matching layer.
- **CMO-facing products**: **Vericast** (audio fingerprinting monitoring of broadcast/media), **DSP Processing** (streamline digital usage processing "to nail digital distributions without manual work"), **Atlas** (distribution maximization platform for CMOs), **ReSol** (digital claiming conflict resolution), **Vericast Ads** (music in advertising monitoring), member-facing usage dashboards ("grant your members customised access to their usage-data"), **Cued** (cue sheets), BackOffice, Reportal TV/Radio.
- **Claims**: 27 billion matches daily; "$2 billion distributed every year thanks to the metadata we provide"; 4,746 companies. Client logos include PRS, SGAE, SIAE, SoundExchange, GVL, KODA, FILSCAP, AGEDI, CAPIF, HKRIA.
- **Interpretation**: the monitoring/matching/claiming layer is a **buyable capability** — societies outsource parts of leg 2 (usage capture/matching). This product is NOT the Type; it documents where the Type's boundary sits.

## Product E — Songview (boundary anchor)

- Joint data platform of ASCAP + BMI (expanding to GMR + SESAC): ingests song ownership information from each PRO, "processes and reconciles that information based on agreed-upon rules", sends reconciled data back out to each PRO's public searchable databases; 38M+ works; checkmark = data consistent across PROs.
- **Interpretation**: a cross-society **registry/reconciliation layer** with no licensing, collection, or distribution loop — demonstrates that the repertoire registry alone (leg 1) is not the Type.

## Cross-product Comparison

| Dimension | ASCAP | SoundExchange | APRA AMCOS | BMAT | Songview |
|---|---|---|---|---|---|
| Position | society (PRO) | society (sound-recording CMO) | society (PRO + mechanicals) | vendor to societies | joint data platform |
| Rights subject | compositions (performing right) | sound recordings + performers (digital performance right) | compositions (performing + mechanical/reproduction) | music usage of any kind | compositions (ownership shares) |
| Rights-holder relationship | membership (writers + publishers) | registration + claim of recordings | membership (writers + publishers) | n/a | ingests from member societies |
| Licensing mode | negotiated blanket + per-program | statutory license (rates set by Copyright Royalty Board) | negotiated industry schemes + joint initiative (OneMusic) | n/a | n/a |
| Money loop | collects from 700k+ licensees → distributes ~90% | collects from 3,000+ DSPs → distributes monthly | collects licence fees → distributes ~86% | none (claims $2B/yr distributed *on its metadata*) | none |
| Usage capture | census + sample per medium; monitoring partners; OnStage setlists; cue sheets | DSP usage reports (playlists of all plays) with payment | station reports, DSP reports, MRT, background music, setlists | fingerprinting monitoring, DSP processing, cue sheets | n/a |
| Matching | APM platform matches usage to registered works | ISRC-based search & claim; unmatched → unclaimed lists | auto-match to database + human research team | 27B matches/day claim; ReSol for conflicts | reconcile ownership across societies |
| Distribution rules | published DRD (formulas, weighting) | statutory allocation featured artist/rights owner | published distribution rules & practices | n/a | n/a |
| Member surfaces | Member Access portal (works, cue sheets, statements, agreements, OnStage) | SXDirect + app (claim, catalog, payments) | Writer/Publisher portals, Performance Reports, app | member usage dashboards (white-label) | public repertory search |
| Licensee surfaces | 3 segment portals + license finder | Licensee Direct (calculate/certify/submit) | licence schemes site, OneMusic | DSP reporting products | n/a |
| International | international royalties step; foreign societies | 72 partners / 91 agreements | reciprocal administration for affiliates in/out | multi-territory monitoring | n/a |

### Convergent findings (cross-product, Evidence layer B)

1. **All three societies run the same collective loop**: license/collect from music users → capture usage evidence → match to the registered repertoire → calculate per published rules → distribute to rights holders (and to/from affiliated societies). ASCAP documents it as an 11-step payment system; APRA AMCOS as a 5-step process; SoundExchange as the statutory variant of the same loop.
2. **The repertoire registry is built from rights holders' own acts**: membership + work registration (ASCAP, APRA) or registration + claim of recordings (SoundExchange). The society administers rights it does not own.
3. **Usage capture is explicitly a census-vs-sample economic trade-off**, stated as policy by ASCAP (expand census as technology cheapens) and APRA AMCOS (balance accuracy vs cost). Capture mechanisms converge on: station reports, DSP usage files, fingerprinting/MRT monitoring, member-submitted setlists, cue sheets.
4. **Matching is a named, resourced function** in every society (APM platform; auto-match + research team; ISRC search & claim + unclaimed lists); unmatched usage is handled as a distinct class (research teams, unclaimed royalty lists).
5. **Distribution follows published rules** (ASCAP DRD; APRA AMCOS distribution rules & practices; SoundExchange statutory allocation), with money kept per-source ("Follow the Dollar") and administration costs deducted before distribution.
6. **International reciprocity is structural**: societies collect on behalf of affiliated societies' repertoire in their territory and distribute foreign collections to their members (APRA explicit; SoundExchange partner network; ASCAP international step).
7. **Two-sided portals are universal**: member/rights-holder portals (registration, works/recordings, statements, payment details) and licensee surfaces (license purchase/finder, reporting, payment).
8. **The observation/matching layer is outsourcable** (BMAT) and the registry layer is shareable across societies (Songview) — neither is the Type itself.

## Canonical Model (synthesis)

### Defining core (L0 — deliberately minimal)

1. **The represented repertoire of record** — a persistent registry of works or sound recordings with their identified rights holders and shares, built from rights holders who have authorized the organization to administer their public-performance rights (membership/affiliation agreements, or statutory designation). The organization administers rights it does not own. *(remove → a usage database or a bare works registry — Songview-class)*
2. **The usage-to-rights-holder attribution chain** — evidence of public performance/broadcast/streaming use of the repertoire (station reports, DSP usage files, monitoring, setlists, cue sheets — census or sample) is matched to the registry and attributed to specific rights holders according to their shares; unmatched usage is handled as a distinct class. *(remove → a licensing shop splitting money by flat membership, or a monitoring vendor — BMAT-class)*
3. **The collective licensing-and-distribution loop** — revenue collected from music users for performance of the repertoire (negotiated blanket/per-program schemes or statutory/compulsory licenses) is held per source, administration costs deducted, and the remainder distributed to rights holders as recurring royalties under published distribution rules. *(remove → a rights registry or monitoring service with no money loop)*

Jointly-held load-bearing: (1) alone = works registry (Songview); (2) alone = usage monitoring/matching vendor (BMAT); (3) without (1)+(2) = a collection agency with no fair attribution; (1)+(2) without (3) = registry + matching with no economic loop; (1)+(3) without (2) = a flat-split fund, not usage-based; (2)+(3) without (1) = royalty processing over unregistered repertoire.

### Common mature structure (L1)

- Member/rights-holder portals: join/register, register works or claim recordings, statements, payment/tax details, designated users, agreements.
- Licensee surfaces: license finders/rate schedules, segment-specific licensee portals (reporting + payment), joint licensing initiatives.
- Public repertory search (works/recordings databases).
- Census + sample survey mix per medium; fingerprinting/MRT monitoring; cue sheet intake; live setlist programs.
- Published distribution rules (formulas, weighting, per-source pools); statement cycles (monthly/quarterly).
- International reciprocity machinery (affiliate collections in/out).
- Unmatched-usage handling (research teams, unclaimed lists, black-box pools).
- Special programs layered on usage data (awards, top-tour surveys).

### Variant / optional structure (L2)

- Rights subject: compositions (PRO) vs sound recordings + performers (neighboring-rights class) vs both (APRA+AMCOS under one roof).
- Licensing mode: negotiated blanket/per-program vs statutory/compulsory collection (rates set externally).
- Census vs sample depth per medium (economic choice, varies by society and medium).
- Machinery ownership: society-operated vs shared/outsourced (multi-society service providers — ICE/Armonia-class, not directly documented; monitoring vendors; joint data platforms).
- Mechanical/reproduction rights adjacency (AMCOS, The MLC-class) inside the same organization.
- Production music licensing as a distinct scheme; joint society initiatives (OneMusic-class).
- Claim-conflict resolution machinery (ReSol-class).

### Vendor-specific (L3 — research notes only)

- ASCAP: APM platform name, OnStage, Plus Awards, DRD document, Media Monitors/MediaRadar monitoring partnerships, three separate licensee portals, "trillion performances" claim.
- SoundExchange: SXDirect/Licensee Direct/MDX product names, ISRC search tool, Letters of Direction program, four unclaimed-lists taxonomy, CMRRA/SXWorks affiliates.
- APRA AMCOS: OneMusic, Performance Reports, passwordless login, cue-sheet-client portal class, $10 minimum payment threshold (single-source precise number), 13.26% expense ratio.
- BMAT: Vericast/Atlas/ReSol/Cued/BackOffice product names; "27 billion matches daily", "$2B distributed on our metadata", "4,746 companies" claims.
- Songview: 38M+ works claim; four-PRO expansion.

## Historical / Market-Sample Check (§24-style)

- Pre-digital analog workflow (ASCAP 1914, APRA ~a century): paper membership agreements; works registered on index cards/ledgers; broadcasters filed **cue sheets**; radio surveyed by **sample logbooks**; venues paid **blanket licences**; distributions calculated by clerks per published rules and paid by cheque — satisfies all three defining legs with no software, no ISRC/ISWC, no fingerprinting, no portals.
- SoundExchange (2003, digital-native) shows the statutory-collector variant fits the same three legs without negotiated licensing.
- The definition names no specific technology (fingerprinting, APM-class platforms), no specific standards (ISWC/CWR/DDEX), no census-vs-sample ratio, no business model (not-for-profit ratio), no jurisdiction, no deployment model.
- Modern sampled products add portals, monitoring vendors, joint data platforms, claim-conflict tools — all classified as L1/L2, none required by the definition.

## Vendor-specific / Rejected Findings

- Rejected as definitional: negotiated blanket licensing specifically (SoundExchange is statutory), census specifically (sample is equally in-type), fingerprinting/MRT specifically (station reports and setlists predate it), member portals (a surface, not the structure), not-for-profit status and payout ratios (business model), ISRC/ISWC identifiers, cue sheets specifically (one capture mechanism among several), international reciprocity as a defining leg (structural but a society can exist without foreign flows — held L1), Songview-class reconciliation (cross-society layer).
- Rejected as overfit: "Follow the Dollar" as a named principle (ASCAP-specific phrasing of the general per-source pooling behavior), the 11-step/5-step enumerations (pedagogical orderings of the same loop), unclaimed-lists taxonomy (SoundExchange-specific realization of unmatched-usage handling).

## Boundary Findings

- **vs Music Publishing Management**: rights-owner side (one catalog, many pay sources, contract machinery) vs society side (market-wide repertoire, collective licensing, usage-based distribution). The PRO appears in the publishing income loop as a pay source. Confirmed from this side: societies' own systems center the collective loop, not a single owner's catalog.
- **vs Royalty Management Platform (generic)**: generic contractual royalty computation over licensees/products vs the society's collective attribution machinery (usage matching, shares, per-source pools, published distribution rules). Remove the usage-attribution chain and the society collapses into generic royalty software.
- **vs Media Rights Management**: grant-of-record lifecycle (availability, conflicts, expiry) vs the collection-attribution-distribution loop. A society holds rights records, but its center is the money loop.
- **vs Music Distribution Platform / Record Label Management**: masters→stores pipeline and label operations vs society-side collection. Confirmed from the sibling pass: SoundExchange-class collection deliberately sits outside the distributor's earnings loop.
- **vs usage monitoring vendors (BMAT/Tunesat-class)**: the observation/matching layer is a capability societies outsource — a vendor serving the Type, not the Type.
- **vs works registries (Songview-class)**: registry + reconciliation without the money loop is not the Type.
- **vs Music Promotion Platform**: no overlap in core loop.
- **"Remove what to become another Type" test**: remove the represented repertoire → monitoring/royalty processing vendor; remove the attribution chain → flat-split collection agency; remove the money loop → works registry; narrow the subject to one owner's catalog → music publishing management.

## Uncertainties

1. **Multi-society service-provider pole (ICE/Armonia-class)** not directly documented — both candidate domains timed out twice; the "outsourced society machinery" variant is held at lineage strength (inferred from BMAT's vendor position + Songview's shared-platform existence).
2. **PRS for Music / European societies** not directly documented (JS-heavy site; help portal error); European variant inferred from cross-product commonality + BMAT's published client relationships (logo-level evidence only).
3. **Internal back-office depth** (matching engines, distribution engines) is not publicly documented in detail; the workflow is evidenced from the societies' own public explanations, not internal manuals. Assertion strength kept at "documented loop" level.
4. **Precise numbers** (90 cents, 86 cents, 13.26%, $10 threshold, 700k licensees, 38M works, 32M ISRCs, 27B matches) are vendor-published claims — kept product-specific, not promoted to the canonical document.
5. **Distribution-rule internals** (weighting formulas, per-media pools) — ASCAP publishes a DRD PDF that was not fetched; held at "published distribution rules exist and govern calculation" strength.
6. **Writer-share vs publisher-share payment mechanics** vary by territory/affiliation type (documented in the publishing pass from Songtrust); not re-verified here across societies.

## Final Synthesis

Performing Rights Management software is the **society-side system of record and money loop for public performance rights**: it keeps the registry of represented works or recordings with their rights holders and shares, runs the attribution chain that turns observed or reported usage into rights-holder-level performances, and operates the collective loop that licenses music users, collects fees, and distributes them as royalties under published rules. Around that core, mature implementations add member and licensee portals, census/sample survey machinery, monitoring integrations, cue-sheet and setlist intake, international reciprocity, and unmatched-usage handling. The Type is bounded against music publishing management by the society-vs-rights-owner seam, against generic royalty platforms by its collective usage-attribution machinery, against media rights management by its money-loop center, and against monitoring vendors and shared registries by the fact that those are capabilities the society buys or shares — not the Type itself.
