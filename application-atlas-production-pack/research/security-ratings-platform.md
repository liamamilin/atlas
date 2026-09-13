# Research Notes — Security Ratings Platform

Research date: 2026-09-09

## Research Goal

Understand what a Security Ratings Platform really is from real products: what is rated, how the rating is produced, what users do with it, and where its boundary lies against neighboring Types (Third-party Cyber Risk Platform, Attack Surface Management, Vulnerability Management, Cyber Risk Quantification).

## Initial Boundary

Working hypothesis before research:

- A Security Ratings Platform produces a standardized, continuously refreshed grade/score of an organization's cybersecurity posture — the "credit score" mental model applied to security.
- Primary users: security teams (self-assessment), third-party risk teams (vendor monitoring), executives/boards (communication), insurers, M&A.
- Likely confusions: TPRM platforms (bundle ratings), ASM (shares the outside-in data collection), CRQ (shares the "quantify risk" language), vulnerability management (shares "findings" vocabulary).

## Research Questions

1. What is the rated object, and how is an organization identified (domain, IP, subsidiary)?
2. What is the rating artifact — scale, grade form, comparability, history?
3. What signals feed the rating, and who collects them (platform vs self-attestation)?
4. How does the rating decompose (categories/factors/findings) so it can be explained?
5. What do users do: monitor, alert, remediate, dispute, share, report?
6. What rules matter: attribution correctness, decay, normalization, algorithm updates, adjustment workflows?
7. Where are the boundaries vs TPRM / ASM / VM / CRQ?

## Representative Products

| Product | Why sampled | Positioning observed |
|---|---|---|
| BitSight | Category pioneer; ratings-first heritage; strong methodology docs | Ratings as the core; platform apps for TPRM, self (SPM), insurance, national CERT |
| SecurityScorecard | Major vendor; A-F grade philosophy; "more than just ratings" TPRM suite | Ratings as one use case inside a TPRM platform |
| UpGuard | Different philosophy: transparent subtractive scoring, published algorithm mechanics | "Cyber Risk Posture Management" suite with ratings as a platform capability |
| RiskRecon (Mastercard) | Ratings-focused; financial-services/insurance angle; risk-appetite tuning | "Cybersecurity ratings and insights"; CRQ sold as a separate product |
| Panorays | Mid-market TPCRM pole; rating bundled with questionnaires + business context | Third-party cyber risk platform whose rating is one merged input |

Sample covers: pioneer vs challenger, ratings-first vs TPRM-bundled, enterprise vs mid-market, different scoring philosophies (relative letter grades vs absolute subtractive score vs risk-appetite-tuned).

## Sources

Tier 1 (official operational documentation — all fetched 2026-09-09):

- BitSight Knowledge Base: help.bitsight.com — "What is a Bitsight Security Rating?", "How are Bitsight Security Ratings Calculated?", Methodologies category, home page
- SecurityScorecard Help Center: support.securityscorecard.com — "How SecurityScorecard calculates your scores", "Manage and validate your Digital Footprint"
- SecurityScorecard product pages: securityscorecard.com (home, /solutions/use-cases/security-ratings/)
- UpGuard product page: upguard.com/product/security-ratings; upguard.com home; help.upguard.com (root)
- RiskRecon: riskrecon.com home; riskrecon.com/cybersecurity-risk-rating-model
- Panorays: panorays.com home; panorays.com/cyber-posture-rating-explained/

Access notes: bitsight.com marketing root returned 403 (help center used instead — no loss, help center is the stronger source). RiskRecon's rating-scale details live in a downloadable white paper PDF that was not fetched; RiskRecon scale specifics are therefore NOT asserted anywhere. UpGuard help center root fetched but no ratings-specific article pulled; UpGuard rating mechanics come from the official product page (still vendor-official, Tier 1/2 boundary).

## Product Observations

### BitSight (evidence layer A unless noted)

- "Bitsight Security Ratings describe an entity's cybersecurity posture, serve as a measure of their risk... using a data-driven, outside-in approach to rate an entity's security effectiveness."
- Daily ratings from an automated service leveraging 1 year of supporting data.
- Scale 250–900 (effective range 300–820); rating categories Advanced (740–900), Intermediate (640–730), Basic (250–630) with published inventory distributions (60%/35%/5%, average 720) — vendor-published, time-varying statistics.
- Rating = aggregation of all risk-vector letter grades with different weights, normalized for the entity. 10-point rounding "so that any change in the rating can be traced back to at least one risk vector" — explainability engineered into the number.
- Risk categories and weights: Compromised Systems 26%, Diligence 71.5%, User Behavior 2.5%, Public Disclosures (weighted only if they occur).
- Risk vectors (named, individually documented): DKIM Records, TLS/SSL Certificates, TLS/SSL Configurations, Open Ports, Web Application Security, Patching Cadence (reconfigured to "Critical Vulnerabilities Management"), DMARC, Domain Squatting, File Sharing, Security Incidents, etc. Algorithm updates are versioned and announced (RAU26, July 2026).
- Letter grades A–F per risk vector, relative to the Bitsight inventory and normalized by company size; N/A for informational vectors.
- Finding grades: GOOD / FAIR / WARN / BAD / NEUTRAL; findings feed vector letter grades.
- "We do not engage in any hacking or any intrusive network penetration testing. Our collected data is externally observed from various sources in the public internet."
- Findings have decay and lifetime; impact continues over a decay period or until remediation/decommissioning is confirmed. Sinkhole findings can be investigated and appealed.
- Rating drops ≥10 points are highlighted next to a 1-year historical trend graph.
- Parent–subsidiary relationships have their own rating-calculation article.
- Platform applications: Continuous Monitoring (third-party portfolio), Vendor Risk Management, Security Posture Management (self), Trust Management Hub (questionnaires), Cyber Insurance, National Cybersecurity (CERTs/national security orgs).

### SecurityScorecard (evidence layer A unless noted)

- "Security ratings are objective, external assessments of an organization's cybersecurity posture, represented by letter grades." A–F mapped to numeric 100–0; grade corresponds to breach likelihood (vendor claim: F ≤60 is 13.8× more likely to breach than A 90–100).
- 10 factors: Network Security, DNS Health, Patching Cadence, Endpoint Security, IP Reputation, Application Security, Cubit Score, Hacker Chatter, Information Leak, Social Engineering. Factor score from severity and quantity of issues/findings.
- Issues discovered in "exposed network assets during our recurring internet scans"; each issue type has High/Medium/Low severity with weights; positive and informational issue types do not impact the score.
- Three operations: (1) signal collection — scans the entire IPv4 space, sensors/sinkholes/honeypots across three continents, external public/commercial feeds; (2) attribution — signals associated with IPs/domains, matched to an organization via its Digital Footprint; (3) signal analysis — ML-assisted derivation of findings (CVE identification, malware characterization).
- Digital Footprint: "a real-time visualization of all IP addresses and domains attributed to your organization." Users validate it: review, claim assets, refute/remove assets, add missing assets. Removed assets stop impacting the score; claiming alone does not change the score. Management order: domains → IPs → issue findings.
- Size normalization: logarithmic scale; modified z-score comparing each organization to others with the same Digital Footprint size; calibration over two months of data. Scores updated daily; algorithm recalibrated quarterly, with published scoring-update release notes.
- Breach penalties affect the score (separate article).
- Portfolio analytics (group by criticality/geography/subsidiary), Automatic Vendor Detection (3rd/4th party via DNS and web crawling), Rule Builder (event triggers → notify/report), remediation plans, executive/board reporting.
- Ratings use case framed for "contractual, insurance or brand reasons"; self-monitoring is a distinct use case; "provides a common language for risk"; "every rated entity can see exactly what drives their score"; signal provenance down to the specific IP, timestamp, and vulnerability that triggered a rating change.

### UpGuard (evidence layer A unless noted)

- "Security ratings are a data-driven, objective, and dynamic measurement of an organization's security posture."
- Data collection: "non-invasive, passive data collection... at scale and on-demand"; in-house research team updates the rating algorithm over time.
- Rating out of 950, produced per internet-facing web property; the algorithm is subtractive (start at 950, points deducted per failed check, deduction sized by severity/weight).
- Organization rating = Gaussian weighted average of individual asset scores, weighting lower scores most ("an organization's security is only as strong as its weakest link").
- 10 risk categories; checks derived from OWASP, CVSS, ISO 27001, NIST CSF; severity classification table published.
- "Incorporate risks from security questionnaires" into ratings — questionnaire-derived signals are explicitly part of the rating input set.
- Adheres to the US Chamber of Commerce "Principles for Fair and Accurate Security Ratings" (linked).
- Value framing: quantitative measure, dynamic indicator, changes between time periods, continuous monitoring, objective comparison against competitors, board-level communication.
- Suite context: Vendor Risk (TPRM), Breach Risk (ASM), User Risk, Trust Exchange, Risk Automations — ratings are a platform capability, not the whole product.

### RiskRecon / Mastercard (evidence layer A unless noted)

- "Cybersecurity ratings and insights that make it easy to understand and act on your risks. Automated risk assessments tuned to match your risk appetite."
- Rating model founded on "the prevalence and severity of issues and the value at risk in the systems in which the issues exist" — issue prioritization is contextualized by what the affected system does.
- Use cases documented: third-party risk teams (vendor selection, holding vendors accountable), supply chain (nth-party), own enterprise & subsidiary monitoring, M&A teams (latent liabilities), internal security analysts (internet risk surface), CISOs/boards (benchmark vs peers and competitors).
- Asset attribution "independently certified to 99.1% accuracy" (vendor claim); "we don't hide any of the assessment details. It's all visible to you and your vendors."
- Custom-tuned assessments: each assessment fitted to the customer's risk appetite; value at risk automatically determined per system from the data types it collects and its functionality.
- Automated workflows: vendor risk action plans containing only the issues the customer cares about; collaboration workflow to share action plans with vendors; automatic tracking and reporting of each vendor's remediation progress.
- Risk Priority Matrix, breach events, compliance indicators, board-level reporting, advanced filtering.
- FAQ explicitly frames the approach: "Products like RiskRecon are outside looking in"; also documents a one-time report mode for quick assessments (e.g., in RFPs).
- Portfolio shape: Cyber Ratings, Privacy Ratings, Assessments are separate solution lines; Cyber Quant (financial CRQ) is a separate product — packaging evidence for the ratings/CRQ boundary.

### Panorays (evidence layer A unless noted)

- "Cyber Posture Rating from 0–100, representing the risk level attributed to its external digital perimeter," produced non-intrusively, typically within hours, continuously updated.
- Methodology: hundreds of Tests run on the evaluated company's assets; each Test yields findings and a Test rating (0–100, or N/A when not performable); the final rating aggregates Test ratings directly (not via category ratings, to preserve N/A and critical-finding effects).
- Three test layers: Network & IT, Application, Human (employee attack surface, security-team presence).
- Asset discovery: automatic from a single seed (usually the primary domain) → domains, subdomains, IPs.
- Non-intrusive: performed without engaging the assessed company; no consent required; no active exploitation; probes include benign checks (e.g., empty email to verify a destination exists) plus public feeds (botnet activity).
- Dispute flow: the supplier is invited into the platform, clicks "claim dispute" with comments; Panorays validates internally within 24 hours, accepts/rejects, and the rating auto-updates.
- Assessment Template versioning: the list of tests/severities/weights is a single enabled template; every change is documented and monitored because it affects ratings.
- Test development: industry best practices (OWASP, NIST) + research team; new tests deployed in hidden mode against the company database to tune severity/weight (documented DNSSEC example); calibration considers company size and industry standards.
- The Cyber Posture Rating is combined with the Smart Questionnaire results and the business context of the relationship to produce the supplier risk view — the rating is one merged input in a TPCRM platform.
- Continuous monitoring with live alerts on security changes or breaches for the company and third parties; remediation plans; vendor collaboration; portfolio management.

## Cross-product Comparison

| Dimension | BitSight | SecurityScorecard | UpGuard | RiskRecon | Panorays |
|---|---|---|---|---|---|
| Rated entity | organization ("entity"), parent–subsidiary handling | organization = Scorecard over a Digital Footprint | organization via its internet-facing web properties | organization (domains) | organization seeded from a domain |
| Rating artifact | numeric 250–900 + per-vector A–F | A–F letter mapped to 0–100 | numeric 0–950 | rating (scale in unfetched white paper) | numeric 0–100 |
| Computation shape | weighted aggregation of risk-vector grades, size-normalized | modified z-score vs same-size peers, weighted factors | subtractive per asset, Gaussian weighted mean to org | prevalence × severity × value-at-risk | aggregation of per-Test ratings |
| Signal posture | externally observed only (explicit no-intrusion statement) | external scans + sensors/sinkholes + external feeds | non-invasive passive scanning + questionnaire risks | "outside looking in" | non-intrusive external probes + public feeds |
| Decomposition | risk categories → risk vectors → findings with grades | 10 factors → issue types → findings | 10 categories → checks | issues with severity + value context | tests → findings |
| Refresh | daily | daily | continuous | continuous | continuous (initial assessment in hours) |
| History | 1-year trend, ≥10-point drops flagged | daily updates, quarterly recalibration, release notes | changes between time periods | trend/benchmark reporting | continuous updates |
| Attribution correction | remediation verification, sinkhole appeals | claim / refute / remove / add assets | algorithm transparency | certified attribution, full visibility | claim dispute with 24h validation |
| Portfolio layer | Continuous Monitoring app (vendor portfolio) | portfolios + automatic vendor detection | Vendor Risk product | portfolio management + action plans | portfolio management |
| Alerts | alerting capabilities | Rule Builder event triggers | continuous monitoring alerts | alerts | live alerts |
| Benchmarking | vs inventory, size-normalized grades | vs industry, size-normalized | vs competitors | industry distributions | vs dataset + trusted-company set |
| Bundled TPRM | VRM app + Trust Management Hub | full TPRM platform | Vendor Risk product | Assessments line | full TPCRM platform |
| Distinct rating lines | insurance-tuned, national | (use-case packaging) | — | Privacy Ratings | — |

Convergent observations (evidence layer B):

1. All five rate organizations, not assets; assets are attributed to the organization and rolled up.
2. All five compute the rating by the platform from signals the platform collects/curates; none is a self-attestation questionnaire in disguise.
3. All five decompose the rating into an explainable structure (categories/factors/vectors/tests → findings) and market transparency as a fairness requirement.
4. All five refresh the rating over time and expose history/trend.
5. All five operate on a common scale that supports comparison across entities (benchmarking is a first-class feature).
6. All five bundle or neighbor TPRM workflow around the rating — the rating is the measurement; the vendor relationship is a surrounding product.
7. All five include alerting on rating/posture changes.
8. All five provide remediation guidance or action plans tied to findings.
9. All five publish or reference a methodology (algorithm updates, white papers, principles) — methodology governance is part of the product.

Divergent observations (implementation, not Type):

- Scale form: letter grades (SSC, BitSight per-vector) vs numeric ranges (BitSight 250–900, UpGuard 0–950, Panorays 0–100).
- Aggregation philosophy: relative/normalized (BitSight, SSC z-score vs peers) vs absolute subtractive (UpGuard) vs context-weighted (RiskRecon value-at-risk) vs test-aggregated (Panorays).
- Whether questionnaire-derived signals enter the rating (UpGuard: yes, explicitly; Panorays: rating kept separate from questionnaire but merged into the supplier risk view; others: external signals dominant).
- Human/social layer as a rated dimension (SSC factors, Panorays human layer, BitSight User Behavior category — present but weighted very differently).

## Canonical Abstraction

### L0 — Defining Invariant

Four jointly-held structures. Remove any one and the product stops being a security ratings platform:

1. **The rated entity as unit of record.** A standing record for an identified organization — the organization is what is rated, identified through a digital footprint of domains/IPs/assets attributed to it (with parent–subsidiary roll-ups in mature products). Remove → asset inventory / domain monitor.
2. **A platform-computed standardized rating.** A communicable grade or score of that organization's security posture, computed by the platform on the platform's common scale — the platform is the rating authority; the rating is not self-attested, and the shared scale is what makes entities comparable. Remove → findings feed or self-assessment.
3. **Signal-based computation with decomposition.** The rating is computed from security signals attributed to the entity and decomposes back into findings/factors that explain it — every rating change is traceable to observed evidence. Remove → an opaque number, or a questionnaire score.
4. **A refreshed standing rating.** The rating is recomputed as signals accrue and its history is tracked — a living measurement, not a one-shot report. Remove → point-in-time assessment report / audit.

Jointly-held load-bearing checks:

- 1 alone = digital-asset inventory
- 2 without 3 = unexplainable number
- 3 without 2 = external scanning/findings feed (ASM territory)
- 4 without 1–3 = a time series of nothing
- 1+2 without 3 = score nobody can explain or dispute
- 1+3 without 2 = monitoring feed without a rating
- 2+3 without 1 = ratings of nothing in particular
- 1+2+3 without 4 = one-time assessment report (a delivery mode, not the platform)

### L1 — Common Mature Structure

- Portfolio management: group rated entities (vendors, subsidiaries, business units); automatic vendor discovery from the customer's own footprint.
- Alerts/notifications on rating changes, new findings, breaches.
- Benchmarking against industry/peer/size cohorts.
- Rating history and trend visualization.
- Remediation plans / prioritized issues derived from findings.
- Attribution validation and finding dispute workflows (claim/refute assets, dispute findings, remediation verification).
- Rating communication: board/executive reports, sharing ratings with stakeholders, contractual/insurance use.
- Questionnaire integration adjacent to the rating.
- Compliance/framework mapping of findings.
- Methodology governance: versioned algorithm updates, published methodology, release notes.

### L2 — Variant / Optional Structure

- Rating scale form: letter grades vs numeric ranges; absolute vs relative-to-cohort meaning.
- Primary use-case posture: self-monitoring first vs vendor-portfolio first vs insurance underwriting vs national/CERT scale.
- Data-source emphasis: botnet/sinkhole sensors, dark-web/hacker-chatter monitoring, breach/incident feeds, email-security configurations, human/social exposure.
- Inside-out supplements: questionnaire-derived risks blended into ratings; customer-supplied evidence.
- Customer-specific tuning: risk-appetite weighting (RiskRecon-style), portfolio-specific thresholds.
- One-time report mode as a delivery option.
- Distinct rating lines for adjacent domains (privacy ratings).
- Deployment posture: SaaS platform vs data-feed/API delivery of ratings into other systems.

### L3 — Vendor-specific Structure (Research Notes only)

- BitSight: 250–900 scale with 300–820 effective range; Advanced/Intermediate/Basic categories with published distributions; risk-vector taxonomy with named vectors and per-vector letter grades; GOOD/FAIR/WARN/BAD/NEUTRAL finding grades; RAU-versioned algorithm updates; SPM/VRM/Trust Hub/Insurance/National application split.
- SecurityScorecard: A–F mapped to 0–100; the named 10-factor list (incl. Cubit Score, Hacker Chatter); modified z-score methodology; Digital Footprint claim/refute machinery; Rule Builder; TITAN AI packaging; 13.8× breach-likelihood claim.
- UpGuard: 0–950 subtractive scoring; Gaussian weighted mean aggregation; per-web-property scoring; adherence to the US Chamber "Principles for Fair and Accurate Security Ratings".
- RiskRecon: prevalence × severity × value-at-risk model; Risk Priority Matrix; risk-appetite tuning; 99.1% attribution certification claim; Mastercard suite adjacency (Cyber Quant, Threat Protection).
- Panorays: Cyber Posture Rating 0–100; Test-based methodology with N/A semantics; Network & IT / Application / Human layers; Assessment Template release management; 24-hour dispute validation SLA; Risk DNA branding.

## Vendor-specific Findings

- All breach-correlation multipliers (13.8×, 1.5–2×, 2–3×, 5×) are vendor-published claims about their own datasets — recorded as claims, not cross-product facts.
- BitSight's rating-category distributions (60/35/5) describe its own inventory at a point in time.
- Panorays' "only platform that considers human behavior" is a marketing claim contradicted by SSC factors and BitSight's User Behavior category — rejected.
- RiskRecon's rating scale specifics were not directly observed (white paper not fetched) — no scale claims made for RiskRecon.

## Boundary Findings

1. **vs Third-party Cyber Risk Platform.** The ratings platform's center is the rating artifact and its computation; the TPRM platform's center is the vendor-relationship lifecycle (inventory, onboarding, questionnaires, remediation collaboration, tiering, contracts). Every sampled product bundles TPRM workflow around its rating — the market treats the rating as the measurement engine inside broader third-party programs. Seam test: remove the standing computed rating → TPRM platform; remove the vendor-lifecycle workflow → pure ratings platform. Both directory leaves are justified; the seam is documented, not merged.
2. **vs Attack Surface Management.** ASM's unit of record is the discovered asset/exposure; the ratings platform's unit is the rated organization. Ratings platforms consume ASM-like signal collection as an input stage. Remove the entity-level rating and its scale → ASM. Several sampled products ship ASM modules beside the rating (UpGuard Breach Risk, Panorays External Attack Surface) — packaging, not identity.
3. **vs Vulnerability Management.** VM scans authorized/internal assets and drives an internal remediation workflow; ratings observe externally without consent and produce an entity-level grade. Shared vocabulary ("findings", "severity") but different authority model and unit.
4. **vs Cyber Risk Quantification.** CRQ expresses risk as monetary loss estimates/distributions; ratings express posture as a grade on a common scale. RiskRecon sells Cyber Quant as a separate product beside its ratings — direct packaging evidence that the market treats them as distinct capabilities.
5. **vs Security Program Management / GRC.** Program management tracks the organization's own security activities and controls; ratings measure externally observable posture of any entity, including ones the operator does not control.
6. **vs Supplier/Vendor Risk Management (procurement side).** Procurement VRM manages supplier relationships commercially; the cyber ratings platform supplies the security-posture measurement that may feed it.

## Historical / Market-Sample Check

The Type is young — the market category consolidated in the 2010s (BitSight founded 2011, SecurityScorecard 2013; analysts now track a "Cybersecurity Risk Ratings Platforms" category). There is no long lineage of products under this exact name. The check therefore asks whether the definition over-fits to the current dominant implementation:

- Requiring daily refresh, letter grades, specific numeric scales, billion-IP scanning, AI, or cloud SaaS would exclude simpler realizations. The L0 deliberately requires only "recomputed as signals accrue, history tracked".
- A national CERT rating service, an insurer's standing security grade computed from observed signals, or a regional ratings feed delivered via API would satisfy all four L0 legs without any of the era machinery.
- Point-in-time artifacts (one-off audit reports, PCI-style quarterly pass/fail scans, questionnaire-based vendor grades) fail the refreshed-standing-rating leg and are correctly outside the Type — they are the "before" state the category positions itself against (every sampled vendor contrasts continuous ratings with "point-in-time snapshots" and "annual questionnaires").
- The check passes: the L0 is era-neutral.

## Uncertainties

- RiskRecon's exact rating scale and grade bands were not directly observed (methodology white paper not fetched). No scale claims are made for RiskRecon.
- Whether any major product computes ratings purely from inside-out (customer-installed sensor) data was not researched; the sample is uniformly outside-in-dominant, with questionnaire blending documented at UpGuard. The L0 is written as "platform-collected signals" to stay safe.
- The precise mechanics of how questionnaire results alter ratings (vs sitting beside them) vary and were only partially documented (UpGuard explicit; Panorays keeps the posture rating separate from the questionnaire-merged supplier view).
- Vendor-published breach-correlation statistics could not be independently verified and are treated as vendor claims.

## Final Synthesis

A Security Ratings Platform is the system of record for standardized, continuously refreshed ratings of organizations' cybersecurity posture. Its defining structure is four-legged: a rated organization held as a standing record (identified via an attributed digital footprint); a platform-computed rating on the platform's common scale (the platform, not the rated party, is the rating authority); signal-based computation that decomposes into attributable findings so the rating is explainable and disputable; and refresh-over-time with tracked history. Everything else — portfolios, alerts, benchmarking, remediation plans, questionnaire blending, insurance/contractual sharing, TPRM workflow around the rating — is mature structure layered on that core. The Type's neighbors are cleanly separable by unit of record and authority model: ASM (asset as unit), VM (internal authorized remediation), TPRM (vendor relationship as unit), CRQ (money as output), program management (own activities as unit).
