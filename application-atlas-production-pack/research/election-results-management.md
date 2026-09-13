# Research Notes — Election Results Management

Research date: 2026-09-07
Slug: election-results-management
Directory location: §24 Government, Public Sector & Civic

## Research Goal

Understand what Election Results Management actually is from real products: what the central objects are (results, contests, reporting units, batches), how results enter and accumulate, how they are adjudicated, reconciled, audited, and reported, where the lifecycle ends (canvass/certification? publication?), and where the boundary sits relative to the sibling Types Election Management System (upstream) and Voter Registration System (the roll). The prior election-management-system pass explicitly flagged joint review with this leaf; this pass honors that flag from the results side.

## Initial Boundary (pre-research hypothesis)

- Election Results Management = election-authority-side software for the counting/reporting half of the election lifecycle: results intake from counting processes, tabulation/accumulation per contest and reporting unit, adjudication of ambiguous ballots where machine-read, reconciliation/ballot accounting, progression toward official outcomes (canvass/certification context), and reporting outward (canvass reports, state exports, public election-night reporting).
- Sibling leaves in DIRECTORY.md §24: Election Management System (definition → ballot styles → votable artifacts; ends where tabulation begins — established in the sibling pass) and Voter Registration System (the roll of eligible voters). This leaf should NOT absorb either.
- Adjacent: Government Transparency Portal (generic publication surfaces), Government Open Data Portal (results data files), post-election-audit tooling (adjacent capability space), online-voting platforms (casting-side).
- Likely boundary pressure: vendors co-package the EMS and the results half in one certified voting system family, and at least one vendor (Clear Ballot) places its central-count tabulation product under an "Election Management" navigation bucket. Recorded in the EMS pass; expected to re-appear here.

## Research Questions

1. What is the central managed object — the result? At what granularity (contest × choice × reporting unit)?
2. How do results enter the system: memory media, electronic transmission, central-count scanning, manual tally entry?
3. What does tabulation mean operationally — batches, accumulation, real-time totals, scan/tabulation separation?
4. What is adjudication, when does it occur, and how is it governed (logs, attribution)?
5. Is reconciliation/ballot accounting part of the Type, and what does it compare?
6. How do results progress from unofficial to official? Is canvass/certification machinery inside the software?
7. What does public reporting look like (election night reporting, exports, drill-down)?
8. What audit/verification support exists (independent retabulation, image audits, RLA-adjacent tooling)?
9. What governance machinery exists (roles, audit logs, two-person practices)?
10. Historical/regional check: do paper-era tally/canvass practice, centralized national commissions, and transmission-based models fit the definition?

## Representative Products

| Product | Vendor | Pole | Why selected |
|---|---|---|---|
| ClearCount (+ VerifyNow) | Clear Ballot | browser-based central-count tabulation + independent audit, transparency-first philosophy | EAC-certified family; richest reachable results-side documentation; county buyer tier |
| Verity Central (within Verity/Vanguard family) | Hart InterCivic | voting-system-embedded central scan/adjudication | shows scan/tabulate separation, contest-by-contest adjudication, batch workflow inside a certified voting system |
| Total Vote — Election Night Reporting module | KNOWiNK | statewide suite module for public results publication | shows ENR as a distinct product line beside registration/election management; state-level pole |
| Turing / Electoral Operations System / ENR (Comitia, formerly Scytl domain) | Grupo MSA (scytl.com now resolves to Comitia) | international/LATAM pole: vote-counting technology, central electoral-operations monitoring, election night reporting | non-US regional realization; national-scale context (Paraguay deployment named) |
| results.enr.clarityelections.com (Clarity Elections ENR network) | SOE Software | public ENR portal infrastructure | existence evidence for a dedicated ENR portal network widely used by US counties; root page fetched was a shell — no operational claims |

Selection principles: market representation (central-count modernizer, embedded voting-system family, statewide suite, international specialist, ENR portal network), different philosophies (transparency/audit-first vs ecosystem-embedded vs publication-first), different customer tiers (county vs state vs national), different geographies (US + LATAM). Dominion and ES&S — the two largest US voting-system vendors — were unreachable (HTTP 403 in the sibling pass, same day); per source-access rules they were not retried and no operational claim rests on them.

## Sources

Fetched successfully (2026-09-07):

- Clear Ballot — ClearCount product page, VerifyNow product page:
  - https://www.clearballot.com/products/clearcount
  - https://www.clearballot.com/products/verifynow
- Hart InterCivic — Verity benefits page, Verity Central (by-mail central count) page:
  - https://www.hartintercivic.com/better-elections/
  - https://www.hartintercivic.com/vbm/
- KNOWiNK — homepage (Total Vote modules incl. Election Night Reporting; EAC/ESTEP context):
  - https://knowink.com/
- Comitia (scytl.com domain now resolves to Comitia, Grupo MSA) — EN homepage with solution list:
  - https://www.scytl.com/ and https://www.scytl.com/en/
- SOE Software Clarity ENR portal root (shell page only):
  - https://results.enr.clarityelections.com/
- U.S. Election Assistance Commission — Election Management Guidelines landing page (chapter list):
  - https://www.eac.gov/election-officials/election-management-guidelines

Prior-pass fetches of the same date usable as corroboration (election-management-system research notes):

- https://www.clearballot.com/ , /products , /products/cleardesign , /solutions/vote-by-mail (incl. VerifyNow "ballot inventory tool, ensures ballot reconciliation, and improves canvassing and transparency" wording)
- https://www.hartintercivic.com/ , /solutions/ , /vanguard-family/

Attempted and abandoned (per source-access rules):

- https://www.eac.gov/sites/default/files/electionofficials/EMG/EAC_Election_Management_Guidelines_508.pdf — response exceeds 5 MB fetch limit.
- https://www.eac.gov/sites/default/files/electionofficials/EMG/Ch18_Canvassing_and_Certifying_an_Election.pdf — 404 (URL guess).
- https://www.ncsl.org/elections-and-campaigns/canvass-and-certification-of-election-results — 403.
- https://www.soesoftware.com/ — empty response.
- https://www.scytl.com/brochures/Comitia_Brochure_ENG_GENERAL_Digital_v2.pdf — response exceeds 5 MB.
- https://www.hartintercivic.com/verity-count/ — 404 (URL guess; no count-specific product page found on the public site).
- Dominion Voting Systems and ES&S — 403 in sibling pass (same day); not retried.

Source-access limitation: official operational documentation for the canvass/certification stage (EAC EMG PDF) could not be fetched; NCSL explainer blocked. The lifecycle claims below about canvass/certification are therefore calibrated: the existence of the official process stages is documented via the EAC EMG chapter list (Canvassing and Certifying an Election; Post-Election Audits; Recounts) and via product-side customer quotes mentioning reconciliation and canvassing, but product-internal canvass-workflow depth is NOT directly observed and is kept out of strong claims.

---

## Product A — Clear Ballot (ClearCount + VerifyNow)

### Key observations (Layer A — fetched 2026-09-07)

- ClearCount is presented by the vendor under the navigation bucket "ELECTION MANAGEMENT" (same bucket as ballot design) with the section heading "Tabulation & Reporting — Offering unparalleled transparency to election officials nationwide." Umbrella-labeling pressure, again.
- **Vote Visualization**: "By analyzing both inside and outside the vote target area, every vote is counted as intended." Ballot-mark analysis beyond the target area.
- **High-resolution ballot images**: "ClearCount scanning technology reads pen ink of any color and produces the highest resolution ballot images on the market." Every scanned ballot becomes an inspectable image.
- **Real-Time Reporting**: "Create a variety of reports as results are accumulated and export files into different formats for state reporting." Two outward directions: local reports and state reporting formats.
- **Digital Adjudication**: "Preserve voter intent by digitally adjudicating ballots while keeping detailed logs of all changes." Adjudication is logged and attributable.
- Customer evidence (Clinton County, NY): system used for "absentee ballot counting process… enhances the transparency of the vote counting process by allowing observers of the procedure to clearly see ballots with questionable votes or markings."
- Customer evidence (Pierce County, WA): "Clear Ballot products have saved us time and money, as well as improved reconciliation and accuracy. The transparency of voter intent resolution and ballot auditing has been applauded by both political parties, as well as candidates."
- VerifyNow (vendor category "AUDITING"): "automated, fully independent audits of from 1% to 100% of ballots without the inefficiency, inaccuracy and lack of security of a hand count." Two audit modes: ballot image audit (images sent after the election, retabulated in software) and physical ballot audit (ballots scanned on separate high-speed scanners, retabulated automatically). Output: results comparison against the certified voting system, threshold reports.
- VerifyNow positioning from the sibling pass: "independent results verification… provides a ballot inventory tool, ensures ballot reconciliation, and improves canvassing and transparency."
- Public audit transparency (Maryland): "Clear Ballot partnered with Maryland to create a public portal where community members can view reports and Vote Visualization dashboards from the statewide audit for all twenty-four jurisdictions."
- Recount support (Maryland Board of Elections quote): "helps us resolve recount issues and allows for more targeted recounts… informs election administrators on ballot design issues that can lead to voter confusion."
- Independent verification accuracy (Brevard County, FL quote): "99.992% accuracy between the certified voting system and the automated independent audit system" (product-specific number — L3, not asserted in the final document).

## Product B — Hart InterCivic (Verity Central within the Verity/Vanguard family)

### Key observations (Layer A — fetched 2026-09-07)

- "Verity Central is a high-speed scanning solution for centralized vote capture." Central count of by-mail ballots.
- **Scan/tabulate separation**: "Central scans without tabulating, so you can start scanning weeks before polls close on Election Day. No more late nights at the scanner." Scanning (capture) is deliberately decoupled from tabulation (counting) — results do not exist until tabulation is run.
- **Adjudication**: "Verity Central provides contest-by-contest resolution for all voter intent issues with clear, color-coded flags and easy-to-understand instructions." Adjudication is contest-scoped, queue-shaped work.
- **Auditability**: "a complete record of all resolution decisions captured in an audit log for end-to-end transparency"; "With endless image filters, you can easily locate exactly the ballot images you want. Plain-language processing notes clearly show exactly how voter selections are recorded."
- **Batch management**: "Manage your batches seamlessly. No outstacking or rescanning required. Scan multiple precinct styles and/or multiple languages in the same batch, in any orientation." Batches are the intake unit; heterogeneous styles in one batch.
- **Scalable topology**: "options for multiple, networked scanning stations connected to a central server, you can cost-effectively add capacity as needed."
- **Parallel work**: "Have some team members scanning while others adjudicate." Scanning and adjudication are separate roles/workstations.
- Family context (from this and the sibling pass): Verity is a comprehensive election technology solution; the results half lives inside the same certified family as ballot marking, precinct scanning, and election building ("Verity paper-based solutions never encode voter choices in any digital seal for tabulation. Votes are captured from the same human-readable text that voters use to verify their choices.").

## Product C — KNOWiNK (Total Vote — Election Night Reporting module)

### Key observations (Layer A — fetched 2026-09-07)

- Total Vote is "a centralized voter registration and election management system"; its modules include Voter Registration, Election Management, **Election Night Reporting**, and GIS-based address management.
- ENR module wording: "Voters, candidates and the news media all want fast, accurate results on Election Night. We can help you display Election Night Reporting results that are easy for the public to understand and available to anyone, anywhere, on most devices." Public-facing results publication is a distinct product line beside the EMS/VR modules — supports the EMS/ERM boundary (the EMS family markets its reporting half separately).
- Regulatory context (from the vendor's EAC certification release): the EAC's ESTEP program "addresses election technologies not covered by the Voluntary Voting System Guidelines (VVSG), including electronic poll books, electronic ballot delivery systems, election night reporting systems, and voter registration systems." I.e., ENR systems are recognized as a separate certification technology family from VVSG voting systems (which contain tabulation).

## Product D — Comitia (scytl.com domain; Grupo MSA) — international pole

### Key observations (Layer A — fetched 2026-09-07)

- The scytl.com domain now serves **Comitia** ("part of Grupo MSA"), a Madrid/Buenos Aires-headquartered electoral technology provider with a 12-city international footprint. The historical Scytl brand has been folded into this offering; treat product-name continuity with caution.
- Solutions list includes: **Turing** — "Electoral technology for vote counting"; **Electoral Operations System** — "System for the centralization and monitoring of information in electoral processes"; **Electoral Information and Training Solutions** — bullets "Online voter education, **Election night reporting**, Software online training"; plus BUE (electronic ballot), Notebox (polling-station management), InVote (online voting).
- Case studies: Paraguay (18,000+ voting machines, 4.6M+ voters, six consecutive years), Salta/Argentina (Notebox polling-station management in national legislative elections), Tierra del Fuego (internet voting).
- Interpretation (Layer C caution): the international realization packages vote counting, central operations monitoring, and public results reporting as distinct named solutions for national electoral bodies — a different packaging from the US county voting-system model, but the same functional trio appears (count → monitor/consolidate → report publicly).

## Unreachable / shell market context (no operational claims rest on these)

- **Dominion Voting Systems / ES&S** — the two largest US voting-system vendors; both sites returned 403 (sibling pass, same day). Their results modules are named market context only.
- **SOE Software Clarity ENR network** — https://results.enr.clarityelections.com/ fetched; root returned a shell page ("ENR Home Page For Google Analytics"). Existence of the public ENR portal network is corroborated by the domain's role, but no operational detail was observed.
- **EAC Election Management Guidelines PDF** — exceeds fetch limit; only the chapter list is directly observed (chapters: Documentation and Audit Trail; Post-Election Audits; Canvassing and Certifying an Election; Recounts — alongside Ballot Building and Pre-Election Testing on the preparation side).

---

## Cross-product Comparison

| Dimension | Clear Ballot (ClearCount/VerifyNow) | Hart (Verity Central) | KNOWiNK (Total Vote ENR) | Comitia (ex-Scytl domain) |
|---|---|---|---|---|
| Results intake | central-count scanning with images | central-count scanning ("centralized vote capture") | (ENR module consumes tabulated results; intake machinery not on fetched page) | counting technology (Turing) + central operations monitoring |
| Accumulation granularity | contests × reporting units; reports "as results are accumulated" | batches → central server; contest-scoped adjudication | not observed | not observed (monitoring framing) |
| Adjudication | digital adjudication "with detailed logs of all changes" | contest-by-contest resolution, color-coded flags, workstation-separated from scanning | not observed | not observed |
| Scan/tabulate separation | implied (tabulation software) | explicit: "scans without tabulating" | n/a | not observed |
| Reconciliation | "improved reconciliation" (customer); VerifyNow "ensures ballot reconciliation" | not directly named on fetched page | n/a | not observed |
| Audit/verification | independent retabulation audits (image or physical), threshold reports, public audit portal | audit log of all resolution decisions; image filters; plain-language processing notes | n/a | "auditable platforms" positioning |
| Outward reporting | varied reports + "export files into different formats for state reporting" | audit-facing outputs; reporting machinery not detailed on page | public ENR "easy for the public to understand… on most devices" | election night reporting within information solutions |
| Packaging | products inside certified voting system family + separate audit product | results half inside certified voting system family | ENR as suite module beside VR + EMS | national-scale solutions for electoral bodies |
| Buyer tier | counties of all sizes; one statewide audit program | counties/jurisdictions | statewide + county | national electoral commissions |
| Vendor-bucket labeling | ClearCount under "ELECTION MANAGEMENT" nav bucket | family marketed as election technology; no separate results category | ENR named as its own module | counting/monitoring/reporting as separate named solutions |

Layer B findings (cross-product commonality, ≥2 products or product+regulatory evidence):

- Results are accumulated and reported per contest across reporting units (ClearCount, Hart batch/contest model, ENR module's premise).
- Adjudication of voter intent on scanned ballots, with logged, attributable decisions (ClearCount, Hart).
- Audit logging / decision records as first-class machinery (ClearCount, Hart; consistent with the high-integrity posture observed across the election family in the sibling pass).
- Batches as the operational intake unit for central counting (Hart explicit; ClearCount scanning workflow consistent).
- Outward reporting in two directions: internal/canvass reports + standardized exports for higher-level reporting (ClearCount "state reporting formats"; KNOWiNK ENR public display; the state roll-up direction).
- Public election-night reporting exists as a distinct capability/product line (KNOWiNK module; Comitia ENR bullet; Clarity portal network existence; EAC/ESTEP recognizes "election night reporting systems" as a technology family).
- Post-election audit/verification support as a capability adjacent to tabulation (ClearCount VerifyNow; EAC EMG "Post-Election Audits" chapter).

Layer B qualified (2 of 4, or single-product direct):

- Scan/tabulation separation as a deliberate operational control (Hart explicit; ClearCount consistent but not stated as a control).
- Ballot-image capture as the substrate of modern central count (ClearCount, Hart) — older media-based flows not directly observed.
- Independent retabulation audit products (Clear Ballot only — single-product direct).
- Public audit dashboards/portal (Clear Ballot + Maryland — single-product direct).

Layer C inference (canonical abstraction, argued not observed): the Type is organized around the lifecycle of the result — capture of counted outcomes → contest-scoped accumulation → resolution of ambiguity → reconciliation against ballot accounting → progression to official standing → outward reporting at increasing levels of finality and publicity.

## Canonical Model (Layer C)

### L0 — Defining Invariant

Three structures. Removing any one makes the product stop being Election Results Management:

1. **Contest-scoped result records tied to reporting units** — the system of record holds vote accumulations organized by contest (office/ballot question) and choice (candidate/option), within reporting units (precincts, districts, batches) of the election that produced them. The managed unit is the result — never the ballot (that is election/ballot production) and never the voter (that is the roll).
2. **Intake from the counting process** — results enter from whatever counted the votes: counting-device media, central-count scanning, electronic transmission, or manual entry of tallies. The system consumes the output of casting/counting; it does not define the election or produce votable artifacts.
3. **Aggregation to official outcomes with outward reporting** — results roll up across reporting units into jurisdiction-wide totals, progress toward a final/official standing, and are reported outward: canvass-facing reports, standardized exports to higher election authority, and/or public election-night reporting.

Justification for minimality:

- **Adjudication is NOT L0.** Hand-tally and media-based eras/jurisdictions accumulate results without image adjudication; it is the dominant modern pattern for central-count paper, not the definition.
- **Ballot imagery is NOT L0.** Same reasoning — an implementation substrate of modern central count.
- **Reconciliation/ballot accounting is NOT L0** (kept L1): strongly expected in mature practice and in official guidance, but the minimal definition survives without software-enforced reconciliation (paper-era canvass abstracts aggregated tallies without it).
- **Public interactive ENR is NOT L0.** Outward reporting is definitional, but its public-interactive form (drill-down sites) is a modern publication variant; a flat export or printed abstract satisfies the structure.
- **Certification-stage formalism is NOT L0 as software machinery.** Progression toward a final/official standing is definitional; the specific legal canvass-board workflow is jurisdiction machinery that the software may or may not orchestrate.
- **Election definition/ballot production is NOT L0** (upstream sibling), **the voter roll is NOT L0** (sibling Type).
- **Historical check:** a pre-computer election office receiving precinct tally sheets, aggregating them per contest into a canvass abstract, reconciling totals by hand, and publishing the official result satisfies all three structures without software. Centralized national commissions consolidating transmitted tallies into a national count and publishing it satisfy them at national scale. The definition does not depend on images, networks, or certification regimes.

### L1 — Common Mature Structure

- Batch-managed central counting (batches as intake units; heterogeneous ballot styles/languages per batch; no outstacking/rescanning patterns)
- Adjudication workflow for machine-read ambiguity: contest-by-contest queues, flags, attributed decisions with full logs; scanning and adjudication as separable workstations/roles
- Scan/tabulation separation as an operational control (capture decoupled from counting, enabling early scanning without early totals)
- Reconciliation / ballot accounting (ballots cast vs counted vs votes per contest; ballot inventory)
- Results reporting: varied internal/canvass reports as results accumulate; export into standardized formats for state/higher-authority reporting
- Public election-night reporting (contest/precinct-structured public display, multi-device)
- Audit logging and role-based controls across the results workflow (high-integrity government domain posture, consistent with the sibling pass)
- Ballot-image capture with inspectable filters and plain-language processing notes (modern central-count substrate)
- Post-election audit/verification support (independent retabulation, image or physical ballot audits, threshold reporting)
- Recount support (targeted recounts, recount-grade re-examination)
- Multi-election operation over time (results history per election)

### L2 — Variant / Optional Structure

- Packaging pole: results/tabulation half inside a certified voting system (dominant US realization) vs standalone central-count products vs ENR-specialist publication products vs statewide-suite modules vs national-scale solutions for electoral bodies (international)
- Counting context: precinct-count (totals by precinct at the source) vs central count (by-mail/absentee focus) vs hybrid
- Scale and topology: single county vs state roll-up (counties submit upward) vs national consolidation; media vs networked stations vs transmission
- Legal-lifecycle machinery: unofficial → canvass → certified progression; whether the software orchestrates canvass-board workflow is jurisdiction-dependent
- Public transparency posture: interactive public ENR with drill-down vs flat exports/files vs public audit dashboards
- Alternative voting methods: ranked-choice and other alternative-method tabulation/reporting
- Audit model: image-based retabulation vs physical re-scan vs hand-count comparison; 1%–100% audit scopes (product menus vary)
- Government model: decentralized county model vs centralized national commission model

### L3 — Vendor-specific (research notes only)

- Clear Ballot: ClearCount/VerifyNow naming; Vote Visualization trademark; "highest resolution ballot images on the market"; 1%–100% audit range; "America's first 100% statewide audit" (Maryland portal, 24 jurisdictions); Brevard "99.992% accuracy" quote; "first browser-based central count" (sibling pass); Fujitsu/ibml scanner integrations (sibling pass).
- Hart: Verity Central naming; "scans without tabulating, so you can start scanning weeks before polls close"; color-coded flags; "endless image filters"; plain-language processing notes; networked scanning stations.
- KNOWiNK: ENR module wording; Total Vote suite naming; Poll Pad certification statistics (not results-related).
- Comitia (ex-Scytl): Turing/Notebox/BUE/InVote naming; Paraguay deployment figures (18,000+ machines, 4.6M+ voters); brochure unreachable.
- None of these numbers or claims are asserted in the final document.

## Historical / Market-Sample Check

- **Paper-era practice** (precinct tally sheets → hand aggregation → canvass abstract → official publication) satisfies the three L0 structures without software-era features → definition survives.
- **All-mail jurisdictions** (several named Clear Ballot customers are Oregon/Washington counties) run the same structures with central count of by-mail ballots as the dominant intake → confirms precinct-count logistics is not definitional.
- **Decentralized county model vs centralized national commissions**: the Comitia/LATAM sample shows counting + central monitoring + public reporting packaged for national bodies; the US sample shows the same functions inside county voting systems and ENR products → definitional robustness across government models.
- **Media-based older systems** (memory-card upload of DRE/precinct-scanner totals into a central accumulator): not directly observed in this pass, but their existence is common knowledge in the family and they fit structure 2's "whatever counted the votes" phrasing; the definition deliberately does not require images or networks. Confidence: adequate for L0; the L1 image-centric items are marked as modern-common, not definitional.
- The two largest US vendors were unreachable; the check leans on the four reachable samples plus reasoning, same limitation as the sibling pass.

## Boundary Findings

- **vs Election Management System (upstream sibling):** EMS = election definition → geography/ballot styles → votable artifacts and configured processes ("makes voting possible"). Election Results Management = intake of what was counted → contest-scoped accumulation → adjudication/reconciliation → official outcomes → reporting ("counts what was voted"). The handoff is well-defined: the EMS hands over votable ballots and configured processes; this Type takes over when votes have been cast and counted. Boundary pressure is real: Clear Ballot buckets its central-count tabulation product (ClearCount) under the same "ELECTION MANAGEMENT" navigation bucket as ballot design, and vendors ship both halves in one certified family; KNOWiNK, by contrast, markets ENR as a module separate from its Election Management module. Same umbrella-labeling issue recorded in the sibling pass — re-recorded here from the results side. Test: if the product's world is contests/ballot styles/production, it is EMS; if it is vote totals accumulating per reporting unit, it is this Type.
- **vs Voter Registration System (sibling):** the roll (voter records, eligibility, registration lifecycle) vs the count (results). Interaction is indirect only (reporting-unit structure may derive from the roll's geography). Test: voter records vs vote totals.
- **vs Election Night Reporting as a standalone surface:** ENR is the public-publication capability of this Type when it consumes tabulated results. The EAC/ESTEP recognizes "election night reporting systems" as a certification technology family separate from VVSG voting systems — i.e., regulation treats ENR systems as their own category. Within the Atlas directory, a pure public ENR portal without tabulation is a partial realization of this Type (a publication slice), not a separate directory leaf. Recorded as nuance; not split.
- **vs Government Transparency Portal:** transparency portals are generic publication surfaces over government data; results reporting is election-specific (contests, reporting units, unofficial→official progression, legal publication duties). A transparency portal publishing results files is downstream output, not this Type.
- **vs Government Open Data Portal:** results exports/data files may flow into open-data portals; the portal publishes, this Type produces and manages the results.
- **vs post-election-audit tooling:** independent retabulation/audit products are an adjacent capability space (one sampled vendor markets one); audit consumes results and ballot artifacts. In this directory (no audit-tooling leaf), audit support is kept as an optional capability of this Type, flagged as adjacent rather than definitional.
- **vs online-voting / e-voting platforms:** casting-side systems; they produce counts but are not the election authority's results system of record. Adjacent.
- **"Remove what to become another Type" test:** remove result intake from counting and keep ballot definition/production → Election Management System. Remove contest-scoping and keep generic datasets → a reporting/dashboards Type. Remove the official-outcome progression and keep only public display → a transparency/publication surface. Remove aggregation and keep only per-unit capture → a transport/collection mechanism, not results management.

## Uncertainties

1. **Canvass/certification workflow depth inside products:** the EAC EMG PDF (authoritative process guidance) exceeds the fetch limit; only its chapter list is observed. Product-internal canvass orchestration (canvass-board workflow, certification paperwork) was not directly observed; Pierce County's "improved reconciliation" and VerifyNow's "improves canvassing" hint at support but do not document machinery. Final doc uses qualified wording.
2. **State-side consolidation machinery** (how state offices ingest county exports and aggregate statewide): direction evidenced by "export files into different formats for state reporting" and by statewide ENR, but the state-side system-of-record workflow was not observed.
3. **Transmission-based national models** (results transmission portals in African/Asian/LATAM commissions): only the Comitia catalog-level view observed; no operational documentation.
4. **Dominion/ES&S results modules:** unreachable (403 ×2 in sibling pass; not retried). Their tabulation/reporting modules are market context only.
5. **Media-based (non-image) legacy flows:** inferred as historical baseline; not directly documented in fetched sources.
6. **Precinct-count reporting paths** (totals produced at the polling place and transmitted/transported): covered by the L0 "intake from the counting process" abstraction, but no fetched page documents a precinct-transmission workflow directly.

## Final Synthesis

Election Results Management is the election authority's counting-side system of record: it takes what the casting/counting processes produced (device media, scanned central-count batches, transmissions, or entered tallies), holds it as contest-scoped results tied to reporting units, accumulates it into jurisdiction-wide totals, resolves voter-intent ambiguity where machine-read ballots require it (with logged, attributable decisions), reconciles results against ballot accounting, moves totals toward official standing, and reports outward at increasing levels of finality and publicity — canvass reports, standardized exports to higher authority, and public election-night reporting. Its defining trio — contest-scoped result records, intake from the counting process, aggregation to official outcomes with outward reporting — is stable across paper-era, all-mail, precinct-count, central-count, and national-commission realizations. Around that trio, mature products add batch-managed central counting, adjudication workflows with audit logs, scan/tabulation separation, image-based inspection, audit/verification support, recount support, and interactive public reporting. The market's dominant US realization embeds the results half inside a certified voting system; other realizations are standalone central-count products, statewide ENR suite modules, and national-scale electoral-technology solutions. Sibling Types hold: Election Management System (prepares the vote — ends where tabulation begins), Voter Registration System (the roll), with this Type's boundary drawn at "counts what was voted and makes the outcome official and public."
