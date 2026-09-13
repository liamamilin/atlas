# Value-based Care Platform

## Overview

A **Value-based Care Platform** is the operating machinery for payer–provider payment arrangements in which reimbursement depends on measured quality and cost performance rather than on volume of services alone. It holds each such arrangement as a persistent record — the parties, the covered population, the payment model, the financial terms, the measures performance will be judged on, and the performance period — measures the provider organization's actual performance against that arrangement's own rules using aggregated claims and clinical data, and carries the arrangement's financial resolution: projecting, tracking, and reconciling the savings, incentives, or fixed payments the arrangement earns or owes as the period unfolds.

The defining structure is small:

```text
Value-based arrangement (contract of record)
└── Covered population, attributed to providers
    └── Performance measured against the arrangement's rules
        │    (quality + cost measures, risk-adjusted, benchmarked)
    └── Financial resolution under the arrangement's terms
         (savings / losses / incentives / fixed payments)
```

Everything else commonly associated with these products — cloud data lakes, HEDIS measure libraries, star-ratings programs, AI coding suggestions, managed actuarial services — is widespread in current products but is not what makes one a value-based care platform. The underlying structure long predates the "value-based care" label: a 1990s capitation agreement with utilization budgets and withhold reconciliation, or an early-2000s pay-for-performance bonus pool, satisfies the same core with none of the modern machinery.

When the center of gravity shifts to managing the population itself (stratify → gap → outreach → measure at population scope), the product is a Population Health Management platform. When it shifts to the plan's own clinical programs (case management, disease management), it is Payer Care Management. When it shifts to claim-level billing, it is Revenue Cycle Management. This Type is the arrangement-and-performance machinery between them.

## Users & Context

The primary users are healthcare organizations operating under, or paying under, arrangements that tie money to measured performance:

- **Provider organizations taking on risk** — accountable care organizations (ACOs), clinically integrated networks, integrated delivery networks, physician groups and IPAs/MSOs, and community health centers — that earn shared savings, incentive payments, or capitation revenue and must know, continuously, where they stand.
- **Health plans and other paying parties** — commercial plans, Medicare Advantage and Medicaid managed-care plans, self-funded employers and their TPAs — that define arrangements, share performance data with provider partners, and administer the resulting payments.
- **Hybrid payer–provider organizations** that sit on both sides of their own arrangements.

Typical roles: value-based-care and finance executives deciding which contracts to sign and how they are trending; actuaries and analysts modeling contract terms and projecting outcomes; contract managers maintaining the arrangement portfolio; quality and population-health teams closing the gaps the measures require; practice and network leaders acting on provider-level performance.

The working context is shaped by the arrangement itself: a defined performance period, measure-reporting deadlines, data arriving continuously from payers (member rosters, claims, care-gap files) and from internal EHRs, and settlement or audit moments at which the platform's numbers meet the counterparty's.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being this Type.

**1. The value-based arrangement as the unit of record.**
A persistent, identified payment arrangement between a paying party and a provider organization. It carries:

- the parties (payer side and provider organization, sometimes with downstream sub-arrangements to practices or individual providers)
- the covered population and how members are attributed to providers
- the payment model and its financial terms — shared savings with or without downside risk, per-member-per-month capitation, bundled or episodic payment, pay-for-performance bonuses
- the quality and cost measures performance will be judged on, with their benchmarks or targets
- the performance period and its settlement mechanics

This is the object every other structure hangs on. Products model it explicitly: contract builders, contract setup and configuration tools, "map the contract landscape" onboarding. A portfolio of such arrangements — across payers, lines of business, and payment models — is the platform's memory.

**2. Arrangement-bound performance measurement.**
The platform assembles the data needed to score the arrangement and computes performance against its rules:

- **Multi-source data aggregation** — claims from payers, clinical data from EHRs, commonly plus pharmacy, lab, and social-determinants sources, normalized into one picture.
- **Attribution** — which members count toward which provider under this arrangement. Attribution determines whose performance is being measured and follows the arrangement's method (plan rosters, claims-based assignment, primary-care attribution); it shifts as eligibility rolls change.
- **Measure computation** — the arrangement's quality measures (standard libraries such as HEDIS-class and electronic clinical quality measures, plus custom sets) and cost measures (total cost of care, utilization, episode costs), computed per the arrangement's specifications.
- **Risk adjustment** — normalizing for how sick the covered population is, so that comparisons across providers and periods mean what they appear to mean.
- **Benchmarking and tracking** — performance against the arrangement's targets and against regional or national peers, tracked across the performance period rather than only at its end.

**3. The arrangement's financial resolution.**
The platform carries the arrangement's money content and keeps it reconciled with measured performance:

- projecting what an arrangement will pay or earn, before and during the period (revenue forecasting, what-if modeling of terms)
- tracking the running financial position — savings or losses accumulating against targets, incentive thresholds within reach or missed
- computing and reconciling the outcome — shared-savings calculations, incentive distributions, per-member or per-episode payment administration, funds flow — including support for the audit-and-submission moments where the organization's own numbers must meet the counterparty's

The depth varies by product: some operate the payments themselves (adjudicating capitation and bundles, streaming funds flow); others compute, project, and reconcile while the paying party runs the payment run. The invariant is that the arrangement's money is a computed, tracked object — not a footnote to the performance dashboards.

### Standard Capabilities

Mature products commonly add, on top of the core:

- **Risk stratification and coding capture** — identifying high-risk members and missed diagnostic coding (risk-adjustment capture), because both drive the money.
- **Care-gap worklists** — the measures translate into per-patient gaps (screenings due, chronic-care visits, documentation), routed to care teams for closure; closure improves the score, the score moves the money.
- **Payer↔provider data exchange** — plan rosters and claims flowing in; supplemental clinical data and gap-closure evidence flowing back; care-gap reconciliation files aligning what each side believes about a patient.
- **Drill-down performance views** — the same measures surfaced at contract, network, practice, and provider grain, with role-tailored dashboards for finance, clinical, and operations stakeholders.
- **Scenario modeling** — "what if" simulation of contract terms, population mix, and network configuration before signing or at renewal.
- **Network and utilization analytics** — referral patterns, leakage, and utilization drivers examined as levers on contract performance.

### One Structure, Many Implementations

The core model is conceptual. Current products realize each concept differently:

```text
Concept:   Payment arrangement
Realized as:  shared-savings agreement · capitation agreement ·
              bundled/episodic payment · pay-for-performance bonus pool

Concept:   Attribution
Realized as:  plan-provided rosters · claims-based assignment algorithms ·
              primary-care attribution rules

Concept:   Measures
Realized as:  HEDIS-class measure sets · electronic clinical quality measures ·
              star-ratings measure families · custom contract-specific sets

Concept:   Financial resolution
Realized as:  savings projection and reconciliation · incentive tracking ·
              capitation/PMPM payment administration · bundle pricing and
              unbundling · funds-flow distribution
```

A reader who has only seen one implementation — say, a Medicare shared-savings program dashboard — should still be able to recognize a commercial capitation administration product, or a bundled-payment adjudication platform, from the core model.

## How It Works

The canonical loop runs once per arrangement and repeats across the portfolio:

**1. Establish the arrangement.**
Before signing, the organization models the deal: choose the payment model, define the population and attribution method, select the measures and benchmarks, set the risk corridor (upside-only vs shared losses), and simulate outcomes under "what if" scenarios. The configured arrangement becomes the record of record.

**2. Assemble the data.**
Claims, member rosters, and care-gap files arrive from the paying party; clinical data flows from EHRs and internal systems. The platform normalizes both into one population picture and applies attribution, fixing who counts toward whom.

**3. Measure performance.**
Throughout the period, the platform computes the arrangement's quality and cost measures, risk-adjusts them, and compares them to targets and benchmarks — surfacing not just a score but the drivers behind it (which gaps, which utilization, which coding gaps).

**4. Act to improve.**
Measurement becomes work: care-gap worklists route to care teams, coding and documentation gaps route to providers, utilization outliers route to management. Closure is tracked back into the measures. (In many deployments the actual outreach and care management happen in a linked care-management or population-health product; the platform supplies the arrangement-bound targets and tracks the results.)

**5. Settle.**
At and after period end, the platform computes the financial outcome under the arrangement's terms — savings or losses, earned incentives, payment obligations — reconciles it against the counterparty's calculation, supports the audit and submission process, and (where the product operates payment) administers the resulting payments and funds flow. The result feeds the next negotiation cycle.

The loop is continuous across a portfolio: while one arrangement is being settled, the next is being measured, and the next is being negotiated.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Contract / arrangement workspace

The arrangement's home surface.

- the arrangement's terms: parties, payment model, population, measures, benchmarks, risk terms, period
- primary actions: create and configure an arrangement, model scenarios, compare contract types against a population, track status across the portfolio

### Performance dashboards

The measurement surface, layered by grain.

- contract-level scorecards (quality composite, cost position, projected settlement), drill-down to network, practice, and provider
- typical information: measure rates vs targets, total cost of care vs benchmark, risk scores, gap-closure progress, savings trajectory
- primary actions: filter by cohort, drill into a driver, export or distribute scorecards

### Measure & gap worklists

The action surface where measurement becomes work.

- per-patient care gaps with their evidence (what the EHR shows vs what the plan reports), prioritized by measure impact
- primary actions: work a gap, document the service, reconcile conflicting evidence, submit supplemental data

### Financial views

The money surface.

- savings/loss position against targets, incentive thresholds, projected settlement, payment and funds-flow activity where operated
- primary actions: adjust projections, examine variance drivers, prepare reconciliation or audit support

### Data-exchange surfaces

The collaboration surface between the parties.

- incoming: member rosters, claims files, plan-reported gaps
- outgoing: supplemental clinical data, gap-closure evidence, performance reports
- primary actions: monitor feed health, resolve data discrepancies, manage what is shared with which partner

### Executive reporting

Board- and leadership-facing summaries of portfolio performance: which arrangements are winning, which are at risk, what the money says.

## Important Rules / Behaviors

**Performance is judged against the arrangement's own rules.** The same measure can score differently under two arrangements with different specifications, denominators, or benchmarks. The arrangement of record — not a generic standard — defines what "good" means for the money attached to it.

**Attribution decides whose numbers count.** A member attributed to provider A is provider A's performance and cost. Attribution follows the arrangement's method and shifts with eligibility rolls, so the measured population is a moving set; products surface attribution state because disputes about it are money disputes.

**Risk adjustment is load-bearing.** Comparing raw costs or unadjusted quality across populations misleads in ways that directly change settlements. Coding completeness (capturing the diagnoses that document patient risk) is therefore a first-class activity, not clerical cleanup.

**Both sides compute.** The counterparty runs its own calculation. Reconciliation between the organization's numbers and the payer's is a standing activity, and the audit/submission process is where discrepancies become recovered or lost dollars. Products support preparing for and surviving that moment.

**The payment model bounds the money.** Upside-only arrangements make settlement a bonus question; arrangements with downside risk make it a liability question. The same measured performance resolves differently under different terms — which is why the terms live in the record of record.

**Data completeness moves scores.** Measures are computed from whatever data exists; clinical evidence not submitted to the payer is performance not credited. Supplemental-data submission and care-gap reconciliation are structural behaviors of the Type, not optional extras.

## Variants

Common shapes of the Type:

- **Provider-side performance platforms** — the dominant shape: a provider organization (ACO, system, physician group) operating its at-risk arrangements, measuring itself before the payer does.
- **Payer-side arrangement administration** — the paying party's view: defining arrangements, exchanging data with provider partners, administering capitation and bundle payments and funds flow.
- **Both-sides / neutral platforms** — one platform serving payers, providers, and sometimes self-funded employers, often with payment-adjudication machinery at the center.
- **Payment-model specialists** — products centered on one family: bundled/episodic payment programs, or capitation administration, or shared-savings performance.
- **Safety-net and small-provider editions** — the same machinery scaled to community health centers and small practices, where payer-data integration and measure libraries do the heavy lifting.
- **Software + managed services** — many products pair the software with actuarial consulting, contract-negotiation support, or full program administration; others remain software-only.

A variant stays a variant while the core model holds. If a product abandons the arrangement of record — measuring populations or quality with no contract, no terms, no money attached — it has become a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Population Health Management | adjacent, commonly bundled | population-first loop (stratify → gap → act → measure at population scope); no arrangement of record — measurement is not bound to a contract's terms or money |
| Payer Care Management | adjacent, co-deployed | the plan's clinical-program operating layer (case/disease management programs with members as care subjects); not the payer↔provider arrangement machinery |
| Healthcare Revenue Cycle Management | adjacent downstream | claim-level billing loop (encounter → claim → payment) for fee-for-service revenue; this Type operates arrangement-level money (savings, incentives, capitation, bundles) |
| Provider Network Management | adjacent upstream | the payer's network configuration machinery (contracting, credentialing, fee schedules, adequacy); this Type operates the payment arrangements and performance once the network exists |
| Healthcare Quality Management | adjacent | organization-level quality-program governance; both consume quality measures, but here the measures are defined and scored per arrangement, tied to settlement |
| Utilization Management | neighboring module | review machinery (prior authorization, medical necessity); appears in this space as a bundled module, never as the center |
| Health Plan Administration System | data supplier | the payer's system of record (enrollment, claims, benefits); this platform consumes its data and holds no enrollment or claims of record |
| Contract Lifecycle Management (generic) | different domain | generic legal/commercial contract authoring and obligations; lacks the healthcare measurement machinery (attribution, measures, risk adjustment) and payment-model economics |

The most important boundary is with Population Health Management, because the two are sold side by side and often bundled. The working discriminator is the unit of record: the arrangement (with its terms, measures, and money) versus the population (with its registry, gaps, and outreach loop). Vendors themselves draw this line — the same vendors sell the population platform and the value-based-care machinery as separate products.

## Representative Products

- **Arcadia** — provider-side healthcare data platform; Contract IQ for VBC contract creation, modeling, and management; long-standing value-based-care managed-services line
- **Health Catalyst** — provider-side analytics vendor; Value-Based Care Performance solution and VBC Intelligence product for contract-level performance
- **Azara Healthcare** — safety-net / community-health-center tier; Value-Based Care Reporting with payer integration on its DRVS population platform
- **Cedar Gate Technologies** — payment-model-centric platform serving payers, providers, and self-funded employers; bundles and capitation adjudication, VBC analytics, actuarial services
- **Innovaccer** — healthcare data-activation platform; value-based-care suite with actuarial contract management, serving providers and regional plans

The core model was checked against the payer-side posture (ZeOmega's Jiva platform, where value-based-care reporting appears as a capability of a payer care-management platform) to avoid over-fitting to the provider-side shape.

## Sources

Research date: **2026-09-09**

- Arcadia — Contract IQ: https://arcadia.io/contract-iq ; Value-based care software: https://arcadia.io/value-based-care-software ; Platform: https://arcadia.io/platform
- Health Catalyst — Value-Based Care Performance: https://www.healthcatalyst.com/healthcare-analytics/population-health-value-based-care/value-based-care ; Population Health & VBC overview: https://www.healthcatalyst.com/healthcare-analytics/population-health-value-based-care
- Azara Healthcare — Value-Based Care Reporting: https://www.azarahealthcare.com/vbc-reporting-with-payer-integration ; https://www.azarahealthcare.com/
- Cedar Gate Technologies — Platform: https://www.cedargate.com/ ; Value-Based Care Analytics: https://www.cedargate.com/platform/analytics/value-based-care-analytics/
- Innovaccer — Value Based Care: https://innovaccer.com/value-based-care ; Contract Management: https://innovaccer.com/products/contract-management
- ZeOmega — https://www.zeomega.com/

> Sourcing limitation: official product and solution pages were reachable; vendor help-center / user-guide documentation was not. Operational specifics (exact settlement workflows, reconciliation file formats, attribution update cadences, measure-submission mechanics) are therefore not stated precisely in this document; the financial-resolution depth is described as a range (projection-and-reconciliation support through full payment adjudication) because only part of the sampled market documents the deep pole. Detailed evidence and product-by-product observations are recorded in the paired Research Notes.
