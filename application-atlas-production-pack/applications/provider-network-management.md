# Provider Network Management

## Overview

A **Provider Network Management** application is the health plan's (payer's) system for managing its contracted network of healthcare providers: who the providers are, whether they may participate in the plan's network, on what terms, and how the network is maintained, monitored, and presented to members.

The defining core is small:

```text
Provider (the network-participant record of record)
└── Participation relationship (effective-dated in-network status
    under contract terms, scoped to a network/product)
    └── Admission-and-maintenance lifecycle
        (apply → credential → contract → participate → maintain → exit)
```

Everything else commonly associated with the category — provider data management as a discipline, network adequacy analysis, provider directories, sanctions monitoring, delegation to credentialing vendors, AI-assisted verification — is widespread in current products but is not what makes the application what it is. A payer operating with provider files, credential files, contract files, and a printed directory satisfies the same core.

The boundary in one sentence: this application administers the **provider side of the payer's world**. It is not the payer's system of record for members and benefits, not the claims engine, and not the provider's own billing or credentialing stack.

## Users & Context

Primary users sit on the payer's network operations side:

- **Network managers / network development teams** — decide which providers the plan needs, recruit them, and oversee the network's shape against access goals.
- **Credentialing analysts and credentialing committees** — run the verification and approval gate through which a provider enters the network.
- **Contracting specialists** — negotiate and administer participation agreements and their reimbursement terms.
- **Provider data management teams** — keep the provider record accurate, current, and attested.
- **Compliance staff** — oversee regulatory obligations around credentialing standards, directory accuracy, and network adequacy.

Secondary participants: **credentialing verification organizations (CVOs) and delegated provider groups**, which execute credentialing work on the plan's behalf under delegation agreements; and **providers themselves**, who interact through application, attestation, and roster-update surfaces.

The work environment is payer back-office operations under regulatory pressure: credentialing must meet recognized verification standards, directories must be accurate because members rely on them to find care, and the network must demonstrably give members adequate access. These pressures shape the application's rules more than any single workflow does.

## Core Model

### The Provider Record

The central object is the **provider**: a persistent, individually identified record for each healthcare professional, group/practice, or facility in the plan's world. A provider record carries identity (identifiers, name), qualifications (licenses, certifications, education, training, work history, malpractice history), practice attributes (specialty, taxonomy, languages), and operational data (practice locations, contact details, affiliations, availability). Everything else in the application — credentialing status, contracts, participation, directory listings — attaches to this record.

Provider records are hierarchical in practice: an individual clinician typically belongs to a group or practice, which operates at one or more locations, and may be affiliated with facilities. The record must represent all of these levels because participation, verification, and directory listing happen at different grains (a clinician is credentialed; a practice location is listed; a group is contracted).

### The Participation Relationship

A provider "in the network" is not a fact about the provider alone — it is a **relationship** between the provider and a specific network of the plan, held under managed terms:

- **Effective-dated**: participation has a beginning, and commonly defined renewal, amendment, and end points. Status changes do not erase history; they take effect at dates.
- **Product- and geography-scoped**: a provider may participate in one product line or market of the plan and not another. Network membership is per network, not global to the plan.
- **Term-bearing**: the relationship rests on a contract — an agreement carrying reimbursement terms (commonly expressed through fee schedules rather than flat dollar rates), effective dates, amendment provisions, and termination provisions.

This participation status is the application's most consequential output: downstream operations consume it. Claims adjudication applies it to decide whether a claim is in-network. Member services and directories present it. Provider-facing tools depend on it. The application is therefore the **producer and maintainer** of network status for the rest of the payer's operations.

### The Credentialing Gate

Entry into the network is controlled. The typical gate:

```text
Application
→ Primary source verification (licenses, education, training,
   work history, malpractice, sanctions — verified against
   authoritative sources, not taken from the applicant)
→ Review and approval (commonly a credentialing committee
   or designated authority)
→ Credentialing status recorded on the provider record
```

Two structural properties matter. First, verification is **primary-source**: qualifications are confirmed with the issuing bodies, not accepted from the provider's paperwork. Second, the gate **repeats**: credentialing is not one-time; providers are re-credentialed on a recurring cycle, and their standing is monitored continuously (sanctions, exclusions, license actions) between cycles.

Execution of the gate is delegable — plans commonly route credentialing work to credentialing verification organizations or to delegated provider groups — but the gate itself, its standards, and its records remain the plan's. Delegation changes who does the work, not whether the work exists.

### What the Lifecycle Adds Up To: a Managed Network

The network itself — the plan's set of participating providers for a given product — is not a static list. Because every provider in it passed through the admission gate and remains subject to the maintenance loop, the network is a population that is actively administered. What mature products do with that population:

- **Shape it** — decide what specialty mix and geographic coverage the network needs, and recruit toward those goals.
- **Measure it** — assess whether the network gives members adequate access (distance/time to care, specialty coverage), against the plan's regulatory and strategic standards.
- **Present it** — publish accurate provider directories so members can find participating providers, with the accuracy of those directories treated as an obligation, not a courtesy.

These population-management capabilities vary in depth from plan to plan and era to era — a payer can run the admission-and-maintenance lifecycle with only files, spreadsheets, and a printed directory — but the direction is constant: the network is something the plan *manages*, not something it merely lists.

### One Structure, Many Implementations

The core model is conceptual. Common implementations vary:

```text
Concept:            Provider identity
Implementations:    national provider identifiers, internal plan IDs,
                    group/tax IDs for organizations

Concept:            Qualification verification
Implementations:    in-house verification teams, credentialing
                    verification organizations, industry data
                    cooperatives with provider-maintained profiles

Concept:            Participation terms
Implementations:    negotiated contracts with fee schedules,
                    percentage-of-benchmark rate references,
                    product-specific amendments

Concept:            Network presentation
Implementations:    printed/legacy directories, plan websites,
                    member app search, API-delivered directories
```

## How It Works

### Bringing a provider into the network

```text
Identify a need (network gap, market entry, adequacy shortfall)
→ Recruit / provider applies
→ Credentialing: application completed, qualifications verified
   against primary sources, discrepancies resolved
→ Approval by the credentialing authority or committee
→ Contract negotiated and executed (terms, fee schedule, dates)
→ Participation becomes effective as of the contract date
→ Provider appears in the plan's network and directory
```

The order matters: credentialing approval and contracting are distinct gates, and participation begins only when both are in place with an effective date. Delays in either directly delay the provider's ability to serve — and be paid by — the plan.

### Keeping the participation current

```text
Provider data changes (locations, status, group moves)
→ captured via attestation, outreach, or data feeds
→ validated and applied to the provider record
→ directory updated

Re-credentialing cycle comes due
→ verification repeated
→ approval renewed or participation ended

Monitoring alerts (sanction, exclusion, license action)
→ investigated
→ participation suspended or terminated if warranted
```

The maintenance loop is continuous, not annual: between re-credentialing cycles the provider record is kept current through attestation (providers or their groups confirm their data on a cadence), monitoring feeds, and updates from the provider's side.

### Ending participation

Termination is a first-class flow, not an afterthought: contracts end or are terminated, providers retire or leave a group, sanctions force removal. When participation ends, the effective-dated status changes, and the provider must leave the network's member-facing surfaces — a stale listing is one of the category's named failure modes (the "ghost network" problem: directories listing providers who are not actually available or participating).

### Shaping and measuring the network

```text
Define network goals (specialty mix, coverage areas, access standards)
→ assess current network against those goals
→ identify gaps
→ recruit and contract toward the gaps
→ re-measure
```

This loop runs above the individual-provider lifecycle: it is how the plan decides which admissions to pursue, and it closes back into the admission workflow.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Provider record workspace

The anchor surface for one provider (or group).

- identity, qualifications, documents, locations, affiliations, participation status and history, credentialing status and dates
- primary actions: update data, review verification results, view participation history, initiate changes

### Credentialing workflow board

The operations surface for the admission gate.

- application pipeline with per-file status (received, in verification, ready for review, in committee, approved/declined), verification results and flagged discrepancies, committee queues and materials
- primary actions: advance a file, request information, record committee decisions, schedule re-credentialing

### Contract repository

The terms surface.

- contracts and amendments with effective dates, reimbursement terms and fee-schedule references, product/geography scope, renewal and termination provisions
- primary actions: add amendment, track renewal windows, review terms by payer/product

### Network analysis surface

The population-level view.

- network composition by specialty and geography, access/adequacy measures against defined standards, gap identification, recruitment targets
- primary actions: define goals, run assessments, model recruitment scenarios

### Directory management surface

The publication surface.

- what members will see per provider: locations, contact, specialty, languages, telehealth availability; attestation status and freshness per record
- primary actions: request attestation, verify accuracy, publish updates, remove terminated providers

### Monitoring and alerts

- sanctions/exclusion/license-action alerts, expiring credentials and contracts, stale directory data
- primary actions: investigate, suspend, remediate

### Provider-facing intake and attestation

- application forms, data-confirmation requests, document upload — increasingly pre-populated from existing verified data so providers confirm rather than re-enter

## Important Rules / Behaviors

- **No participation without the gate.** A provider does not enter the network on recruitment alone: credentialing approval and an executed contract with an effective date are both required. The two gates are distinct and sequenced.
- **Participation is effective-dated and scoped.** Network status is true for a provider, a network/product, and a time period — not globally and not forever. Downstream systems must be able to ask "in-network for whom, where, and when."
- **Verification is primary-source and recurring.** Qualifications are verified with issuing sources at admission and re-verified on a cycle; standing is monitored between cycles. A lapsed verification is a compliance failure even if nothing else changed.
- **Delegation does not transfer accountability.** When credentialing is delegated to a verification organization or a provider group, the plan remains responsible for the gate's standards and records; delegation agreements and oversight are part of the machinery.
- **Directory accuracy is an obligation.** The directory is the members' map of the network; inaccurate entries (providers not accepting patients, wrong locations, departed providers) are a recognized industry failure mode with regulatory and trust consequences. Attestation and verification loops exist because self-reported data goes stale.
- **Monitoring can override participation.** A sanction, exclusion, or license action surfaced by monitoring can suspend or end participation regardless of where the provider is in its contract term.
- **The provider record is shared infrastructure.** The same record feeds claims, provider services, and directories; errors propagate downstream (misdirected claims, wrong directory entries), which is why data quality is treated as an enterprise concern rather than a directory concern.

## Variants

- **Full-lifecycle network platforms** — credentialing, contracting, provider data, network design, and compliance in one payer-side system, often paired with services (a vendor operating as the plan's credentialing office).
- **Credentialing/enrollment operations platforms** — the verification and onboarding machinery as the product's center, sold to payers and provider organizations alike; the same machinery appears on the provider side (a group managing its payer contracts and enrollments), which is the mirror posture of this Type rather than a different structure.
- **Industry data cooperatives** — shared, provider-maintained credentialing and directory data that many plans draw from, with verification and monitoring layered on top; the plan's own application consumes rather than collects.
- **Network-scale connectivity platforms** — payer–provider networks that add provider data management, attestation, and credentialing intake to their transaction backbone.
- **Payer-suite embedded modules** — provider management inside a plan's core administration system; the participation machinery exists there too, but the system's center remains the member/benefit record.
- **Regime-specific postures** — government-program network building (e.g., Medicare Advantage network construction with adequacy demonstration), state-specific licensing flows, Medicaid program requirements.
- **Member-facing bundling** — directory data extended with search, cost, and scheduling experiences for members; when member engagement becomes the center, the product has drifted toward the care-access category.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Health Plan Administration System | adjacent (same payer, different center) | the payer's system of record for members, eligibility, benefits, premiums, and obligations; carries a provider master for settlement but the participation lifecycle is not its center |
| Payer Claims Processing | consumer of this Type's output | adjudicates claims using network status as an input; does not administer the participation lifecycle |
| Provider Claims Management / Revenue Cycle | opposite seat | the provider's side of billing and claim submission; network administration is not its concern |
| Utilization Management / Prior Authorization Platform | sibling machinery | clinical review of requested services; shares provider records but no participation machinery |
| Provider-side credentialing & enrollment (capability; no separate leaf) | mirror posture | same verification machinery serving the practitioner's ability to practice and bill; the distinguishing question is whose network is being administered |
| Patient Portal / member-facing directory experiences | downstream surface | presents network data to members; when search/cost/scheduling becomes the center, it is a care-access product, not network management |
| Health Information Exchange | different layer | clinical data movement between organizations; no participation or contracting semantics |

The most important boundary is with the **Health Plan Administration System**: both live inside the payer and both hold provider data, but the administration system's center is the member population and the plan's benefit obligations, while this Type's center is the provider population and the participation lifecycle. The provider record is a shared object across an integration seam — not evidence that the two are one application.

## Representative Products

- **Andros** — payer-side provider network management services and platform (credentialing CVO, network design and development, provider data management)
- **Medallion** — credentialing, enrollment, and roster operations platform serving payers and provider organizations
- **Kyruus Health** — care-access platform for health plans (provider data solutions and member-facing directory/search)
- **DataSpring, powered by CAQH** — industry provider-data cooperative (credentialing suite, primary source verification, sanctions monitoring, directory management, adequacy data)
- **Availity** — payer–provider network with Provider Lifecycle Solutions (provider data management, directory attestation, credentialing intake)

The core model was checked against the paper-era payer practice (provider files, credential files, contract files, printed directories) and against the payer-suite embedded-module posture, to avoid defining the Type by the current standalone-platform implementation.

## Sources

Research date: **2026-09-09**

Primary vendor surfaces (official product pages):

- Andros — https://andros.co/ , https://andros.co/network-lifecycle-platform/ , https://andros.co/strategic-network-design/
- Medallion — https://www.medallion.co/ , https://www.medallion.co/solutions/payer-contract-management
- Kyruus Health — https://kyruushealth.com/ , https://kyruushealth.com/health-plans/
- DataSpring (formerly CAQH) — https://dataspring.com/ , https://dataspring.com/solutions/provider-data/credentialing-suite , https://dataspring.com/solutions/provider-data/directory-management
- Availity — https://www.availity.com/ , https://www.availity.com/provider-lifecycle-solutions/

> Sourcing limitation: the adequacy-analytics market leader (Quest Analytics) and the primary standards/regulatory bodies (NCQA, CMS) were not reachable from the research environment on 2026-09-09 (access denied). Regulatory drivers (credentialing standards, directory accuracy rules, network adequacy standards) are therefore described at concept level from vendor compliance statements, and no precise adequacy metrics, standard citations, or numeric thresholds are asserted in this document. Vendor marketing figures are excluded.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
