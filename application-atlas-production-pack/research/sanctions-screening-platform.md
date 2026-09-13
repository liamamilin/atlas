# Research Notes — Sanctions Screening Platform

## Research Goal

Understand what a Sanctions Screening Platform actually is and how it works as an Application Type: what objects exist inside it, who uses it, what screening and alert-disposition workflows look like, which behaviors are defining versus merely common in the current market, and where its boundaries run against AML / transaction monitoring, fraud detection, KYC / identity verification, and global trade management.

## Initial Boundary

Initial hypothesis before research:

- Core use: checking named parties (customers, counterparties, payment details) against sanctions / watchlist data, and managing the resulting potential matches to recorded decisions.
- Users: compliance analysts and screening teams at regulated institutions, overseen by MLRO / CCO roles.
- Closest neighbors: AML Platform, Transaction Monitoring Platform, Fraud Detection Platform, KYC / KYB Platform, Identity Verification, Global Trade Management (restricted-party screening), watchlist data vendors.
- Known seam from a previous pass (global-trade-management): GTM covers restricted-party screening of goods trade; financial sanctions screening covers payments/onboarding — respect that seam rather than re-litigating it.
- Unknowns going in: whether payment screening is part of this Type or a sibling; whether ongoing/delta rescreening is definitional; how strongly audit/retention machinery belongs in the core; how the data-vendor boundary works (data sold without platform).

## Research Questions

1. What is the system's "world model" — lists, subjects, matches, dispositions, cases?
2. What screening modes exist (onboarding/ad-hoc, batch, ongoing/delta, real-time payment)?
3. How does matching actually work (fuzzy name matching, secondary identifiers, filters, thresholds) and how is it made explainable?
4. What is the alert disposition workflow (assignment, false-positive elimination, escalation, comments, approvals)?
5. What audit/evidence machinery exists (audit trail, certificates, reporting, retention)?
6. How do list updates propagate (rescreening, monitoring, acknowledgment)?
7. What data categories are covered (sanctions, PEP, RCA, adverse media, enforcement, internal lists)?
8. Which roles exist (analyst, team lead, admin; outsourced review)?
9. Which interfaces does the user actually face?
10. Where does the Type end vs AML/transaction monitoring, fraud, KYC/IDV, GTM, and pure data vendors?

## Representative Products

| Product | Pole | Evidence reached |
|---|---|---|
| LSEG World-Check One | enterprise data+platform bundle (screening software + proprietary World-Check data); usage-point packages; global bank tier | Product pages (root WC page, World-Check One page) — Tier 2 |
| ComplyAdvantage Mesh | API-first SaaS fincrime suite; SMB starter tier (entity-capped plans) through enterprise | Root site, Customer Screening product page, full public API reference (docs.complyadvantage.com) — Tier 1+2 |
| FinScan (Innovative Systems) | specialist screening workbench with data-quality heritage; insurance/MSB/shipping/mid-market breadth; on-prem/cloud/hybrid | Root site, Sanctions Screening page, Payment Screening page — Tier 2 |

Market anchors researched but **not reachable** (no claims rest on them):

- LexisNexis Risk Solutions Bridger Insight XG — risk.lexisnexis.com returned 403 (2 attempts incl. product path).
- Dow Jones Risk & Compliance — risk.dowjones.com transport error; dowjones.com/risk-compliance/ 404.
- Moody's Grid — moodys.com risk-compliance/grid.html 404 (1 attempt).

## Sources

All fetched 2026-09-07:

- ComplyAdvantage — https://complyadvantage.com/ ; https://complyadvantage.com/mesh/aml-customer-screening/ ; API Reference https://docs.complyadvantage.com/ (full text saved; includes Concepts, Searches, Monitoring, Webhooks)
- LSEG World-Check — https://www.lseg.com/en/risk-intelligence/screening-solutions/world-check-kyc-screening ; https://www.lseg.com/en/risk-intelligence/screening-solutions/world-check-kyc-screening/one-kyc-verification
- FinScan — https://www.finscan.com/ ; https://www.finscan.com/sanctions-watchlist-screening ; https://www.finscan.com/payment-screening
- Previous-pass cross-reference: research/global-trade-management.md boundary ("goods transactions vs payments/onboarding"); STATUS.md fraud-detection-platform joint-review flag (AML/transaction-monitoring siblings).

Evidence-quality note: most Tier-1 operational documentation reached for one product only (ComplyAdvantage API reference). World-Check One and FinScan evidence is Tier-2 product-page level; detailed operational claims for those two are held at concept level. Marketing metrics below are recorded as vendor claims, not findings.

## Product A — LSEG World-Check One

### Key observations (evidence layer A unless noted)

- Positioning: "World-Check One brings advanced data and screening software together… sanctions, PEPs and reputational risks." Combines purpose-built screening software with the proprietary World-Check database (data+platform bundle pole).
- Data coverage of the underlying database: PEPs, close associates, family members; state-owned entities; global sanctions lists (incl. narrative and implicit sanctions); regulatory and law-enforcement lists; adverse media; sanctioned securities; optional sets: Iran economic interest, UBO, vessels, "Sanction Sets for payment screening". Data updated daily by a global research team.
- Key features listed: advanced name-matching algorithms with secondary identifiers; PEP and sanctions screening; adverse media checks with AI-powered relevance filtering; UBO verification (via Dun & Bradstreet data); vessel due diligence (via IHS Maritime); integrated identity verification; EDD reports; batch screening and Zero Footprint API integration; multi-language UI; ongoing monitoring and rescreening; case management and collaboration tools.
- Audit posture: "Every action is logged and date-stamped, creating a full audit trail." ISAE 3000 accreditation cited.
- Workflow: "routing, risk tagging and status tracking"; configurable screening/matching settings enabling "risk-based decision automation and prioritisation of alerts based on customer risk levels"; implicit-sanctions keywords; independently configurable auto-resolution settings.
- Delivery modes of the same data: API (data + matching into existing workflows), Data File (into third-party or proprietary workflow platforms), Zero Footprint Screening API (cloud tool for single payments/transactions where "system tracking, ongoing screening, batch upload, and audit trail functions" can be switched off — no permanent record kept).
- Commercial shape: online tiered packages with usage points (trial ~3,000 / ~5,556 screens; custom enterprise packages) — vendor-claimed numbers.
- Salesforce integration for onboarding/monitoring; Screening Resolution Service: outsourced expert match review — vendor-specific.
- World-Check On Demand: API-first real-time records access; World-Check Verify (with AWS): embedded instant screening for payments.
- FAQ-level process claims: batch screening supported; near real-time verification; used at onboarding and for third-party due diligence.

## Product B — ComplyAdvantage Mesh

### Key observations (evidence layer A unless noted)

- Suite shape: Mesh = financial crime risk applications (Customer Screening, Company Screening, Ongoing Monitoring, Transaction Monitoring, Payment Screening, Fraud Detection) over proprietary risk intelligence (sanctions & watchlists, PEPs & RCAs, adverse media). Screening is one application in a fincrime suite — packaging pole.
- Customer Screening page: AI entity resolution; flexible screening configurations ("risk-based parameters… thresholds tailored to customer segments, geography, or business lines"; "custom screening logic — which sources apply to different entity types or onboarding scenarios"); case workflows with "decision checkpoints and approval hierarchies"; risk-based case routing ("prioritize high-exposure cases and route low-risk alerts for bulk processing"); full audit trail "from data sourcing to alert generation"; ongoing monitoring with dynamic risk ratings; reporting automation with "complete screening history and decisions"; insights dashboards (team performance, cases per risk level, screenings completed, hits, hit rate, average profiles per hit); bulk case assignment/decisions; case filtering by owner/type/stage/creation date/risk.
- Data-velocity claims (vendor-claimed): sanctions list changes "within minutes"; daily PEP monitoring; 10M+ pages/day adverse-media processing; proprietary predicate-crime taxonomy with LLM classification into risk subcategories.
- Integration: real-time API, batch processing, SFTP; ISO27001/SOC2 claims; starter plan capped at 2,000 monitored entities (vendor-claimed).
- API reference (Tier 1, directly observed):
  - Search is the case: `POST /searches` creates a search; results include `match_status` ("potential_match" observed; updatable to "false_positive" / "true_positive" via PATCH), `risk_level` ("high"/"medium"/"low"/"unknown" observed), `assignee_id`, tags, comments; "searches are treated as cases which are assigned to users and need to be resolved".
  - `client_ref` (customer reference) enables whitelisting: previously dismissed identical results are not re-reported for the same client unless the underlying results change ("auto-whitelisting").
  - Blacklisting: internal lists uploaded through the UI, screened in addition to official sources.
  - Matching: `fuzziness` (0.0–1.0), `exact_match` switch; match-type explanations returned per hit: name_exact, aka_exact, name_fuzzy, aka_fuzzy, phonetic_name/aka, equivalent_name/aka ("Robert"→"Bob"), unknown (e.g., acronym); plus year_of_birth, removed personal title/suffix, removed organisation prefix/suffix, removed clerical marks. Entity-type-aware matching (person vs company prefix/suffix handling, initials vs acronyms).
  - Filters: types (sanction, warning, fitness-probity, pep + pep-class-1..4, adverse-media taxonomies incl. FATF-aligned variants), birth_year, remove_deceased, country_codes, entity_type (person/company/organisation/vessel/aircraft). Notable rule: sanctions entities "will always appear regardless of the country filter" — sanctions hits override country filtering; country filtering applies to PEP/adverse-media-type results.
  - Entity payload: name, aka (multi-language transliterations), associates (with relationship), fields (date/place of birth, nationality, address, OFAC ID…), media entries, sources, types, last-updated timestamp.
  - Monitored searches: start/stop monitoring, monitor differences, acknowledge changes; webhooks match_status_updated / search_status_updated / monitored_search_updated.
  - Certificate endpoint: `GET /searches/{id}/certificate` — exportable screening certificate.
  - Throttling defaults (600/min standard, 300/min sandbox) — vendor-claimed operational numbers.

## Product C — FinScan

### Key observations (evidence layer A unless noted)

- Positioning: sanctions, payments & KYC screening in one platform, "powered by precise matching & built on clean data" (data-quality heritage pole). Parent Innovative Systems.
- Sanctions & watchlist screening: "Screen customers, counterparties, and jurisdictions with precision matching and configurable rules to identify and resolve sanctions alerts across the customer lifecycle." Pillars: continuous real-time coverage (automatic global list updates; ongoing screening across lifecycle), data & matching precision (normalize inputs, suppress duplicates), fewer alerts/faster investigations (alerts prioritized by risk, clear scoring logic, explainable matches), regulatory defensibility (complete audit trails).
- List coverage: global sanctions lists, watchlists, PEP sources, beneficial ownership data, related risk datasets; "managed compliance lists" service page exists.
- Definition anchor (FAQ): "Sanctions and watchlist screening is the process of identifying individuals and entities that appear on sanctions lists, watchlists, and related risk lists to identify and prevent prohibited business relationships and transactions."
- Ongoing-screening rationale: "Because sanctions lists change frequently, effective programs screen at onboarding and continuously throughout the customer lifecycle."
- Governance: "Configurable rules, workflows, and controls ensure consistent decisioning, clear accountability, and defensible compliance operations"; "local operational workflow flexibility within centralized governance and control structures".
- Investigation: "Analysts see exactly why an alert was triggered, how it was scored, and what actions are required"; monitor alert queues, assign/reassign, document investigation steps, upload findings.
- Payment Screening page: screen domestic/cross-border payments in real time against sanctions/watchlists to "detect and block high-risk transactions before they settle"; screens at any point pre-/in-/post-processing; extracts "names, BICs, account numbers, free-text fields"; rails: SWIFT, ISO 20022, SEPA, CIPS, FedNow, Fedwire, ACH, RTP, instant payments + universal API for proprietary formats; rules-based conditional screening (payment details trigger specific screening rules or higher review); organize review by time-sensitivity (SLAs, processing deadlines); "immutable audit trail"; deployment on-premise/cloud/hybrid; pre-built connectors (core banking, payment gateways) and SWIFT-certified plugins; real-time API or scheduled batch.
- Case-study-shaped vendor claims (not generalizable): overnight batch of 375M records across 14 sources; false-positive reductions (62–80%); 60 ms end-to-end latency; data cleansing surfacing 400+ previously missed OFAC-listed customers; 560K duplicate alerts removed.

## Cross-product Comparison

| Structure | World-Check One | ComplyAdvantage Mesh | FinScan | Strength |
|---|---|---|---|---|
| Maintained sanctions/watchlist/risk-list data | World-Check database (sanctions, PEP/RCA, SOEs, enforcement, adverse media, securities, vessels) | proprietary intelligence (OFAC/UN/HMT/EU/DFAT-crawled sanctions, PEP/RCAs, adverse media, enforcement) | global sanctions, watchlists, PEP sources, UBO, related risk datasets; managed lists | Core — A×3 |
| Screened subjects from the institution's business population | KYC screening of customers/third parties at onboarding; batch | customer & company screening; monitored entities | customers, counterparties, jurisdictions across customer lifecycle | Core — A×3 |
| Fuzzy name matching + secondary identifiers | "advanced name-matching algorithms with secondary identifiers"; configurable algorithms; secondary matching | fuzziness/exact-match; match-type explanations; DOB/country filters; entity-type-aware | precision matching on imperfect data; culturally-sensitive screening; noise-word handling | Core — A×3 |
| Potential matches surfaced as alerts | alerts; prioritization; routing/risk tagging/status tracking | hits; match_status potential_match; case queue | alerts; queues; risk-aligned routing | Core — A×3 |
| Disposition workflow to recorded outcome | case management & collaboration; configurable auto-resolution | assignment, status, comments, bulk decisions, whitelisting, true/false_positive | assign/reassign, document steps, upload findings | Core — A×3 |
| Audit trail / evidence | every action logged & date-stamped; ISAE 3000 | comprehensive audit trail from data sourcing to alert generation; certificate endpoint | complete/immutable audit trails; explainable decisions | Core — A×3 |
| Ongoing monitoring / rescreening on list change | ongoing monitoring and rescreening; daily data updates | monitored searches w/ acknowledge; monitoring webhooks | ongoing screening across lifecycle; automatic list updates | Common — A×3 (held out of core: historical onboarding-only screening satisfies the Type) |
| Batch screening | yes | batch/SFTP | overnight batch (case studies) | Common — A×3 |
| Real-time API screening | API; On Demand; Verify (payments) | real-time API | real-time API, pre/in/post-processing | Common — A×3 |
| Internal/custom lists | (not directly observed on reached pages) | blacklisting via UI | internal lists; internal-list screening | Common — A×2 (B: absent-from-page is not evidence of absence) |
| False-positive suppression across repeated screening | (not directly observed) | whitelisting keyed on client_ref | duplicate-alert suppression (case-study level) | Common — A×1 direct (CA); others B/C — wording kept qualified |
| Payment/transaction screening mode | Sanction Sets for payment screening; Zero Footprint API (single payments) | Payment Screening application | Payment Screening (rails, free-text fields, conditional rules) | Common — A×3 |
| Risk scoring / prioritization | risk-based prioritisation by customer risk level | dynamic risk ratings; hit-rate analytics | risk-aligned prioritization; scoring logic | Common — A×3 |
| Analytics/reporting on the screening operation | workflow oversight | insights dashboards (hit rate etc.); examiner reports | alert-queue management | Common — A×3 |
| Adverse media / UBO / vessels / identity verification as bundled enrichment | UBO (D&B), vessels (IHS), IDV, EDD reports | adverse media taxonomy; entity resolution | UBO verification; ID verification; adverse media | Common/Optional — A×3 |
| Integration spine | API/Data File/Salesforce | API/batch/SFTP | API/batch/connectors/SWIFT plugins | Common — A×3 |
| Screening certificate export | (not observed) | certificate endpoint | (insurance certificates in case study = trade docs, different sense) | Optional — single product (A×1) |
| Zero-footprint (no-record) screening mode | Zero Footprint API | — | — | Vendor-specific (L3) |
| Outsourced match review service | Screening Resolution Service | — | — | Vendor-specific (L3) |
| Agentic/LLM alert resolution | AI relevance filtering (adverse media) | agentic workflows ("up to 85% autonomous" — vendor claim) | AI mentioned in marketing only | Common trend, Optional — wording qualified |
| Usage-point / entity-count commercial tiers | usage-point packages | starter plan entity cap | demo-gated | Packaging variant |

## Canonical Model (synthesis direction)

The Type is a compliance-side system of record for "is this party prohibited?" determinations. Its world:

```text
Watchlist & risk-list data (kept current by vendor research + regulator lists)
        ↑ matched against
Screened subjects (customers, counterparties, payment parties of the institution)
        ↓ produces
Potential matches (hits / alerts) — fuzzy by nature, explained per match
        ↓ resolved by
Recorded dispositions (true/false positive, escalation) — retained as compliance evidence
```

## L0 — Defining Invariant

Smallest structure without which the product stops being recognizable as a Sanctions Screening Platform:

1. **Watchlist data of record brought into the platform** — sanctions, watchlist, and related risk-list content (regulator lists and/or vendor-researched records), kept current by the platform. Remove → a fuzzy-matching library or generic search engine.
2. **A screened population belonging to the institution** — named parties (persons/entities, commonly also payment-message parties) drawn from the institution's business relationships, screened against that data. Remove → a list database or news lookup service.
3. **Potential matches surfaced and managed to recorded dispositions** — every hit (or a configured subset) is reviewed — by a human or under configured auto-resolution — and resolved to a recorded outcome (e.g., true/false positive, escalation), retained as the institution's compliance evidence. Remove → a batch matcher producing disposable output.

The disposition+evidence leg is load-bearing: all three sampled products make audit trail/defensibility a headline; the regulatory posture (screening obligations, examiner scrutiny) is the reason the Type exists as a managed system rather than a script.

§24 historical check: pre-software practice (manually checking customer names against photocopied regulator lists and filing the review), 1990s–2000s batch OFAC-compliance software, and regional products all satisfy the three invariants without real-time APIs, AI, adverse media, cloud delivery, or continuous monitoring. Therefore none of those belong in L0.

## L1 — Common Mature Structure

Present across the sampled modern products, not required for the definition:

- ongoing monitoring / delta rescreening when lists or subjects change (with acknowledgment flows)
- both batch and real-time API delivery (plus file/SFTP)
- internal / custom lists screened alongside official sources
- alert prioritization & risk scoring; configurable screening parameters per segment/geography/line of business
- false-positive suppression across repeated screening (whitelisting keyed to the subject), with change-sensitive re-alerting
- explainability machinery: per-match match-type explanation, secondary identifiers (DOB, nationality, document numbers), matched-field breakdown
- investigation aids: assignment/reassignment, comments/notes, findings upload, bulk actions, approval hierarchies
- operation analytics: hit rate, alerts by risk level, team performance; examiner-facing reporting
- payment/transaction screening as a second screening mode (message fields, rails, pre/in/post-processing placement)
- enrichment data families: PEP classification tiers, adverse media, RCA/associates, UBO, vessels
- integration spine: CRM/onboarding/core-banking connectors, webhooks
- AI/ML assist: relevance filtering, entity resolution, agentic alert handling (era-typical)

## L2 — Variant / Optional Structure

- **Packaging pole**: data+platform bundle (World-Check One) vs SaaS fincrime suite with screening as one application (ComplyAdvantage) vs specialist workbench with data-quality services (FinScan) — vs data-only delivery (World-Check Data File sold into third-party workflow platforms: the capability without the platform).
- **Subject scope**: customer/entity screening only; customer + payment screening; payment-screening-led deployments.
- **Deployment**: cloud SaaS vs on-premise vs hybrid (FinScan explicitly all three; ComplyAdvantage cloud SaaS).
- **Customer tier**: starter/entity-capped plans and usage-point trial packages vs enterprise contracts.
- **Industry tuning**: banks, fintech, insurance, MSBs, casinos/gaming, charities/NGOs, shipping, healthcare, credit-card issuers (FinScan industry pages; World-Check testimonials include gaming operators).
- **Regulatory regime emphasis**: OFAC/HMT/EU/UN/DFAT coverage; local workflows under centralized governance; multi-language UI/data.
- **AI posture**: from none to AI relevance filtering to agentic auto-resolution.

## L3 — Vendor-specific

- Zero Footprint screening (LSEG): switch off tracking/monitoring/batch/audit-trail for single-transaction screening — an explicit no-record mode.
- Screening Resolution Service (LSEG): outsourced expert match review.
- World-Check On Demand / World-Check Verify (LSEG-AWS) product identities; usage-points commercial model.
- ComplyAdvantage API specifics: match_type taxonomy labels, threshold 600/min, certificate endpoint, `search_profile` IDs configured in UI, blacklisting upload mechanics, agentic "85%" claim.
- FinScan claims: 80% false-positive reduction, <100 ms, 10x speed; SWIFT-certified plugins.
- All numeric marketing metrics above are vendor-claimed and recorded here only.

## Vendor-specific Findings → deliberately NOT definitional

Certificates, zero-footprint mode, outsourced review, agentic AI, usage-point pricing, specific match-type vocabularies, specific rails lists, specific plan caps.

## Boundary Findings

1. **vs AML Platform / Transaction Monitoring Platform**: nearly identical machinery shape (records → rules/scoring → alerts → cases → dispositions — see the fraud-detection-platform pass's joint-review flag). The honest distinction is objective and output: transaction monitoring detects suspicious *behavior patterns* in transaction flows and produces suspicious-activity reporting; sanctions screening makes deterministic *list-membership* determinations on named parties and produces screening evidence. Vendors ship both in one suite (ComplyAdvantage nav: Screening and Transaction Monitoring as separate applications; FinScan: AML Solution vs Sanctions Screening pages). Keep separate Types; joint review recommended when the AML/transaction-monitoring leaves are processed.
2. **vs KYC / KYB Platform and Identity Verification**: KYC answers "who is this person/entity really" (documents, biometrics, registry data); sanctions screening answers "is this party prohibited" (list matching). Screening is commonly one check inside KYC onboarding; identity verification is sold as an add-on module by two of three sampled vendors — capability bundling, not Type identity.
3. **vs Fraud Detection Platform**: per the earlier pass's flag — loss-prevention decisions with fraud economics vs regulatory compliance evidence. Same alert-case skeleton, different arbiter (bank's money vs regulator's list).
4. **vs Global Trade Management / Customs Compliance**: GTM performs restricted-party screening on goods-trade transactions (importer/exporter side; prior pass explicitly reserved "payments/onboarding" to this Type). Here, party/payment screening for financial relationships is the defining core; in GTM it is one gate inside a trade compliance system.
5. **vs Watchlist data vendor**: when only the data file is sold (World-Check Data File into third-party workflow platforms), the screening/management machinery is absent — that is the capability the platform consumes, not the platform Type.
6. **vs Adverse-media / Media Monitoring**: adverse media is a data category and optional screening mode here; a pure negative-news monitoring product without list screening drifts toward media monitoring.

## Uncertainties

- Detailed operational docs for World-Check One and FinScan were not reached (product-page evidence only); their internal state vocabularies (exact disposition labels, monitoring cadence) are unverified — final document deliberately avoids asserting them.
- LexisNexis Bridger Insight XG, Dow Jones Risk & Compliance, Moody's Grid unreachable; on-premise enterprise workbench pole is therefore described structurally (from FinScan's deployment statement) without naming specific products as evidence.
- Whether "screening certificate" exports are common beyond ComplyAdvantage is unknown (kept Optional, single-product).
- Internal/custom-list support at World-Check One was not directly observed (platform certainly large enough that absence cannot be inferred) — kept qualified.
- Exact retention periods (e.g., 5-year regulatory norms) were not documented on reached pages — no precise retention claim is made.

## Final Synthesis

A Sanctions Screening Platform is a compliance-side system of record for prohibited-party determinations: it maintains current sanctions/watchlist/risk-list data, screens the institution's named parties (customers, counterparties, and, in most modern deployments, payment messages) against that data with fuzzy, explainable matching, and manages every potential match to a recorded, retained disposition. Batch and real-time delivery, ongoing delta rescreening, internal lists, whitelisting of cleared matches, risk-based prioritization, and audit-grade evidence machinery are the mature market's standard equipment; data+platform bundling vs suite module vs specialist workbench, payment-screening scope, deployment mode, industry and regime tuning are the variant axes. The Type's edges: it makes list-membership decisions (not behavior-pattern detections — AML/transaction monitoring), on named parties (not documents/biometrics — KYC/IDV), for compliance evidence (not loss prevention — fraud), on financial relationships (not goods-trade transactions — GTM).
