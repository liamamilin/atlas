# Security Ratings Platform

## Overview

A **Security Ratings Platform** produces and operates a standardized rating of an organization's cybersecurity posture — a common-scale grade or score computed by the platform itself, in the way a credit bureau computes a credit score, and recomputed over time as new evidence arrives.

The defining structure is small:

```text
Rated organization (identified through an attributed digital footprint)
└── Platform-computed rating on a common scale
    └── Computed from security signals attributed to that organization
        └── Decomposes into findings that explain the rating
            └── Recomputed over time, with tracked history
```

Everything else the market associates with the category — vendor portfolios, alerts, peer benchmarking, remediation plans, questionnaire blending, insurance and contractual sharing — is standard capability layered on that core, not what makes the product a ratings platform.

The rating is the platform's judgment, not the rated organization's self-attestation. This authority model is the Type's sharpest boundary: questionnaires measure what an organization says about itself; a security rating measures what can be observed about it.

## Users & Context

The same rating artifact serves several distinct audiences, and mature products are built around this multiplicity:

- **Security teams rating their own organization** — using the external view to find exposed-asset issues, benchmark against industry peers, and track posture over time. The rated organization is often also a user: it logs in to see its own rating, inspect the findings behind it, and dispute what is wrong.
- **Third-party risk teams rating vendors and partners** — maintaining a portfolio of rated entities, tiering vendors by rating, monitoring for regressions, and pushing remediation. This is the most common commercial context.
- **Executives and boards** — consuming the rating as a communicable, comparable summary of security posture ("a common language for risk"), with trend and peer comparison.
- **Insurers, brokers, and M&A teams** — using ratings to underwrite cyber policies, assess acquisition targets, and evaluate counterparties.
- **The rated party itself** — a vendor that receives a rating it did not ask for, and needs a way to see, understand, and dispute it.

The work environment is a web platform organized around entities and their ratings; the rated party frequently interacts through a dedicated portal or report rather than a full account.

## Core Model

### The Defining Core

**Rated entity.** The unit of record is an organization — a company, subsidiary, or domain-owning entity — held as a standing record. The platform identifies the organization through a *digital footprint*: the set of domains, IP addresses, and internet-facing assets attributed to it. Attribution is performed by the platform from public data (DNS records, certificate data, WHOIS-style sources), and mature products let the organization review and correct it. Parent–subsidiary relationships are commonly handled as roll-ups between entity records.

**The rating.** A single, communicable grade or score of the entity's security posture, expressed on the platform's own scale. Scales differ by product — letter grades, numeric ranges, or both side by side — but the rating always has three properties: it is computed by the platform (the platform is the rating authority), it uses a scale shared across all rated entities (which is what makes entities comparable and benchmarkable), and it summarizes posture as a single value a non-specialist can read.

**Signals and findings.** The rating is computed from security signals the platform collects about the entity's internet-facing presence and security-relevant behavior. Each signal is *attributed* to an entity (this IP belongs to that organization) and evaluated as a *finding* — an observed issue with a severity. Findings roll up through an intermediate structure (risk categories, factors, or test results, named differently per product) into the rating. The decomposition is the rating's explanation: every rating can be traced back to the observations that produced it, which is what makes the rating disputable rather than oracular.

**Refresh and history.** The rating is a living measurement. As new signals arrive, the rating is recomputed; its value over time is retained and displayed as a trend. This is the property that separates the Type from point-in-time assessments: an annual questionnaire or a one-off audit produces a document, while a ratings platform maintains a standing, updating measurement.

### Standard Capabilities

Mature products commonly add the following around the core. They make the rating operational, but a product lacking them can still be recognized as a ratings platform.

- **Portfolios** — grouping rated entities (vendors, subsidiaries, business units) so posture can be monitored at program scale; automatic discovery of vendors from the customer's own footprint is common.
- **Alerts** — notifications when a rating drops, a new critical finding appears, or a breach event is detected.
- **Benchmarking** — comparison of an entity's rating against industry, peer, or size-matched cohorts. Size normalization is a standard fairness mechanism: larger organizations naturally have more findings, so ratings are commonly computed relative to organizations of similar footprint size.
- **Remediation plans** — prioritized, finding-derived action lists, often shareable with the rated vendor, with progress tracking.
- **Attribution validation and dispute** — surfaces where the rated party claims or refutes assets, disputes findings, and submits evidence; accepted disputes update the rating.
- **Rating communication** — board-ready reports, shareable summaries, and exports used in contracts, insurance renewals, and customer assurance.
- **Methodology governance** — published scoring methodology, versioned algorithm updates, and release notes; because algorithm changes move ratings, mature products document them.
- **Questionnaire integration** — security questionnaires either feed signals into the rating or sit beside it in the same platform, depending on the product.

### What the Signals Cover

The specific signal set is a product decision, but across the researched sample the recurring themes are:

- email-security configurations (SPF/DKIM/DMARC-class records)
- TLS/SSL certificate and configuration hygiene
- exposed services and open ports
- software version currency and patching cadence
- IP reputation and compromised-system indicators (botnet/malware activity)
- web application security posture
- leaked credentials or exposed data
- publicly disclosed security incidents

The dominant collection posture is *outside-in*: the platform observes what is publicly observable, without the rated organization's consent or involvement. Some products additionally blend questionnaire-derived or customer-supplied signals into the rating.

## How It Works

The platform runs a continuous loop; users enter it at different points depending on which side of the rating they are on.

### The rating loop (platform-side)

```text
Collect signals (scanning, sensors, feeds, public data)
→ attribute signals to organizations (build/maintain digital footprints)
→ evaluate findings (severity, confidence)
→ compute/refresh each entity's rating (weighted aggregation, size-normalized)
→ retain history
```

Attribution is the load-bearing step: a finding only affects an entity's rating if the asset it was observed on is attributed to that entity. Misattribution is a known failure mode, which is why correction surfaces exist.

### The monitored-entity loop (security team rating itself)

```text
Open your entity's rating
→ review the digital footprint (claim, refute, add assets)
→ inspect findings by category, prioritized by rating impact
→ remediate internally
→ observe the rating recover as findings decay or clear
→ track trend and peer benchmark
```

### The vendor-monitoring loop (third-party risk team)

```text
Assemble a vendor portfolio (manually or via automatic discovery)
→ read each vendor's rating; tier vendors by criticality
→ set alerts for rating drops and new findings
→ generate/share remediation plans with vendors
→ track vendor progress; escalate or accept residual risk
→ report portfolio posture upward
```

### The rated-party loop (a vendor that has been rated)

```text
Receive or look up your rating
→ inspect the findings and assets behind it
→ dispute misattributed assets or wrong findings
→ fix what is real
→ rating updates as the platform re-observes
```

### Core vs Common vs Optional

**Defining core** — without these, not a security ratings platform:

- rated organization as a standing record with an attributed digital footprint
- platform-computed rating on a common, comparable scale
- signal-based computation that decomposes into attributable findings
- refresh over time with tracked history

**Standard capabilities** — present in most mature products:

- portfolios and vendor discovery
- alerts on rating and finding changes
- benchmarking with size normalization
- remediation plans and progress tracking
- attribution validation / finding dispute
- rating reports and sharing
- methodology publication and versioned updates

**Common variants** — depend on product and segment:

- rating scale form (letter vs numeric; absolute vs cohort-relative)
- primary use-case emphasis (self-monitoring vs vendor monitoring vs insurance vs national scale)
- questionnaire signals blended into the rating vs kept beside it
- customer-specific risk-appetite tuning
- one-time report mode as a delivery option
- adjacent rating lines (e.g., privacy ratings)

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Entity rating page (scorecard)

The central surface for one rated organization.

- current rating, rating history/trend, rating category or band
- decomposition into categories/factors with per-area grades
- primary actions: drill into findings, view digital footprint, generate a report

### Findings list

The evidence surface behind the rating.

- individual findings with asset, observation time, severity, and rating impact
- remediation guidance per finding
- primary actions: dispute a finding, mark for remediation, filter by category/severity

### Digital footprint / asset inventory

The attribution surface.

- domains, IPs, and assets attributed to the entity, with relationship context
- primary actions: claim an asset, refute/remove an asset, add a missing asset

### Portfolio view

The program surface for many rated entities.

- rated entities grouped by vendor list, subsidiary tree, or business unit, with ratings and deltas
- tiering by criticality; filtering and sorting by rating
- primary actions: add entities, set monitoring/alerts, assign owners, export summaries

### Benchmark / trend views

Comparative surfaces.

- rating vs industry or peer cohort; movement over time
- primary actions: adjust comparison cohort, export for reporting

### Alerts and rules

- configured triggers on rating changes, new findings, or breach events, routing notifications to teams or systems

### Dispute / validation portal

The rated party's surface.

- the rating, its findings, and the assets behind them, with a dispute/claim workflow and status tracking

### Methodology / transparency pages

- published explanation of what is measured, how findings are weighted, and how the scale works; versioned update notes

## Important Rules / Behaviors

### The platform is the rating authority

The rating is computed by the platform from its own signal collection. The rated organization cannot simply declare a score; its influence runs through evidence — correcting attribution, disputing findings, and actually remediating, after which the platform re-observes and the rating moves.

### Attribution correctness gates everything

A finding affects an entity only through attribution of the underlying asset. Mature products therefore treat footprint validation as a first-class workflow. In the researched sample, removing a misattributed (refuted) asset stops its impact on the rating, while claiming an asset for visibility does not by itself change the score.

### Findings persist and decay

An observed issue does not vanish from the rating the moment it is fixed. Findings commonly carry a lifetime or decay period — the rating continues to reflect them until the platform re-observes the corrected state or the finding ages out. This damps volatility and prevents "fix-and-instantly-recover" gaming.

### Size normalization is structural

Because larger organizations accumulate more findings, ratings are commonly normalized against organizations of comparable footprint size. A raw finding count is not a posture measure.

### Algorithm updates move ratings

The scoring methodology is versioned and updated over time (new checks added, weights retuned). Because this changes ratings without any change in the rated entities, mature products announce and document updates. A rating is comparable across entities at a point in time more strictly than across methodology versions.

### The rating measures observable posture, not internal assurance

The rating summarizes what is externally observable about an organization's security posture. It is not an audit of internal controls, and products are explicit that they do not perform intrusive testing against the rated entity. Two organizations with equal internal security can carry different ratings if their external footprints differ.

### Disagreement has a defined path

Because misattribution and false positives are real, products provide dispute workflows with defined outcomes — the platform validates the dispute and the rating updates automatically when it is accepted. The dispute path, not unilateral override, is the only way the rated party changes its rating.

## Variants

- **Self-monitoring-first deployments** — an organization rating primarily its own entity and subsidiaries, using the platform as an external mirror of its posture.
- **Vendor-portfolio-first deployments** — the classic third-party risk shape: a portfolio of rated suppliers, tiering, alerting, and remediation collaboration.
- **Insurance-grade usage** — ratings consumed in cyber insurance underwriting and renewal; some products maintain insurance-tuned rating lines.
- **National / CERT scale** — ratings operated over a national or sector-wide population of entities for situational awareness.
- **Adjacent rating lines** — the same machinery applied to a neighboring domain, such as privacy posture.
- **Data-feed delivery** — ratings delivered via API/data exports into other systems rather than consumed only in the platform's own interface.
- **One-time report mode** — a single assessment report for a specific decision (e.g., an RFP), offered by some products alongside the standing rating.

A variant remains a variant while the four-part core holds. When the vendor-relationship workflow (onboarding, questionnaires, contracts, remediation collaboration) becomes the center and the rating becomes one input among several, the product has moved into Third-party Cyber Risk Platform territory — the most common bundling direction in this market.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Third-party Cyber Risk Platform | closest sibling; heavily bundled | its unit is the vendor relationship and its lifecycle (inventory, onboarding, questionnaires, remediation collaboration); the rating is one measurement inside it. Remove the standing computed rating → TPRM; remove the vendor-lifecycle workflow → ratings platform |
| Attack Surface Management | upstream data sibling | its unit is the discovered asset/exposure; it inventories and monitors an organization's external assets. The ratings platform consumes such signals and aggregates them into an entity-level rating. Remove the rating → ASM |
| Vulnerability Management | shared vocabulary, different authority | scans authorized/internal assets with consent and drives internal remediation; ratings observe externally without consent and grade the entity |
| Cyber Risk Quantification | shares "quantify risk" language | outputs monetary loss estimates and distributions; ratings output a posture grade on a common scale. Vendors sell them as separate products |
| Security Program Management | internal vs external | tracks the organization's own security activities and control implementation; ratings measure externally observable posture of any entity, including ones the operator does not control |
| Supplier Risk Management (procurement) | consumer of ratings | manages supplier relationships commercially; the ratings platform supplies the security-posture measurement that may feed it |
| Security Compliance Platform | adjacent governance | tracks compliance state against frameworks/regulations; a rating is a posture measurement, not a compliance determination |

## Representative Products

- BitSight
- SecurityScorecard
- UpGuard
- RiskRecon (Mastercard)
- Panorays

The sample spans the category's pioneer, its largest challenger, a transparent-scoring challenger, a financial-services-oriented ratings specialist, and a mid-market third-party-risk platform that treats the rating as one merged input — deliberately covering both ratings-first and TPRM-bundled product philosophies.

## Sources

Research date: **2026-09-09**

- BitSight — Bitsight Knowledge Base: "What is a Bitsight Security Rating?", "How are Bitsight Security Ratings Calculated?", Methodologies category — https://help.bitsight.com/
- SecurityScorecard — Help Center: "How SecurityScorecard calculates your scores", "Manage and validate your Digital Footprint" — https://support.securityscorecard.com/hc/en-us ; product pages: https://securityscorecard.com/ , https://securityscorecard.com/solutions/use-cases/security-ratings/
- UpGuard — "Security ratings" product page — https://www.upguard.com/product/security-ratings ; https://www.upguard.com/
- RiskRecon (Mastercard) — https://www.riskrecon.com/ ; "Updated RiskRecon Cybersecurity Risk Rating Model" — https://www.riskrecon.com/cybersecurity-risk-rating-model
- Panorays — "Cyber Posture Rating Explained" — https://panorays.com/cyber-posture-rating-explained/ ; https://panorays.com/

> Sourcing limitations: BitSight's marketing site was not reachable (403); its Knowledge Base was used instead, which is the stronger source for operational detail. RiskRecon's rating-scale specifics are published in a downloadable methodology white paper that was not retrieved in this pass; no scale-specific claims about that product are made above. Vendor-published breach-correlation statistics are recorded as vendor claims, not cross-product facts. Precise numeric scales, factor lists, and weights are product-specific and are deliberately not stated as Type-level facts.
