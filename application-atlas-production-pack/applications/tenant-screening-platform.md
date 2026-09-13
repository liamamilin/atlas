# Tenant Screening Platform

## Overview

A **Tenant Screening Platform** is the rental side's consumer-report machinery: it compiles a rental applicant's credit, criminal, eviction, identity, and income records into reports that a landlord or property manager uses to decide whether to rent to that person.

The defining structure is small:

```text
Screening request (an identified applicant, bound to a requester and a rental context)
└── Consumer-report production (records compiled from bureaus, courts, registries, bank/payroll sources)
    └── Subject-authorized, purpose-bound release (the applicant's authorization gates the pull;
        the report is delivered to the party evaluating the tenancy)
```

Everything else commonly associated with tenant screening — packaged report bundles, rental-specific scores, income verification, dashboards, tenant-paid economics, jurisdiction-specific filtering — is widespread in current products but is not what makes the product a screening platform. The rental decision itself is not part of the platform's job: it produces reports and the compliance machinery around them; the accept/decline decision stays with the requester.

When the center of gravity shifts to the application form and its decision flow, the product is the sibling Rental Application Platform; when it shifts to the tenancy, rent cycle, and portfolio, it is Residential Property Management.

## Users & Context

Primary users:

- **Independent landlords** — screen one or a few applicants at a time, often with no screening infrastructure of their own; the platform is their entire consumer-report capability.
- **Property managers** — screen continuously as part of a leasing pipeline, often inside a wider management suite; volume and consistency matter.
- **Real estate agents** — screen on behalf of landlord clients, frequently through MLS-integrated workflows.

The evaluated party is the **rental applicant** — an identified prospective tenant who authorizes the screening, verifies their identity, and (commonly) pays for it. The applicant is an active participant in the flow, not just a subject of data.

The context is the leasing moment: a unit is vacant or about to be, an applicant has expressed interest, and the requester must decide quickly whether to sign a lease. Screening sits between the application (declared qualifications) and the lease signing, and its output is decision evidence for the requester.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being a tenant screening platform:

- **The screening request as the unit of record.** A persistent, identified request to evaluate a specific applicant person for a rental decision. It binds the applicant to the requesting party (landlord, manager, or agent) and typically to a property or application context, carries the requested report package, and lives through a managed lifecycle: requested → applicant authorization → report production → report ready → used in the decision. Either side can initiate: the requester invites the applicant, or the applicant starts the screening themselves. Without a managed request, the product is just a data lookup.
- **Consumer-report production.** The platform's core machinery: compiling the applicant's records from data sources — credit bureaus, courts, criminal registries, sex-offender registries, bank and payroll connections — into packaged report products whose composition serves the tenancy decision. Credit history and eviction records sit at the center; criminal records are standard; income and employment verification is the common extension. Without this machinery, the product is an application form or a decision note.
- **The subject-authorized, purpose-bound release.** The report is produced and delivered only under the applicant's authorization (or the applicable regime's lawful basis), bound to the purpose of evaluating their tenancy application. The applicant is a rights-holding data subject: they can see their own report and dispute inaccuracies. The requester carries use-obligations: when a report is used against the applicant, adverse-action duties follow. The requester side is itself gated — an account with verified contact details at minimum, and at some products full identity verification before reports can be viewed. Without this gate, the product is unregulated data brokering.

### Standard Capabilities

Mature products commonly add:

- **Tiered report packages** — bundles combining credit, criminal, eviction, and income components, with optional add-ons.
- **Rental-specific risk score** — a score built to predict rental behavior (such as eviction risk) rather than lending risk, included alongside or instead of a generic credit score.
- **Income verification** — bank-connection data, payroll-provider data, or uploaded documents checked for tampering and employer validity; some products instead flag which applicants need manual income verification.
- **Applicant identity verification** — knowledge-based questions and identity attributes entered by the applicant; the sensitive identifiers (such as a social security number) are entered by the applicant, never collected by the landlord.
- **Request tracking** — a dashboard of screening requests with per-applicant statuses and an archive of completed reports.
- **Adverse-action support** — notice templates at minimum; at the mature pole, an accept/decline action that generates and delivers the required notice automatically, including conditional-acceptance handling where jurisdictions require it.
- **Subject access and dispute** — the applicant can view their own report, obtain a copy after a denial, and dispute inaccurate records.
- **Who-pays choice** — the screening fee is commonly charged to the applicant, with a landlord-pay option; jurisdictions may cap or prohibit applicant fees.
- **Jurisdiction-aware filtering** — what may be returned varies by location: criminal and eviction coverage differs, some jurisdictions require conditional acceptance before criminal records are released, some allow income-substitute evidence for voucher holders, and some mandate acceptance of reusable "portable" reports.
- **Application adjacency** — screening usually attaches to a rental application, but most products can also run a screening from an email address or phone number alone.

## How It Works

### The canonical screening flow

```text
Requester sets up an account (identity/contact details; verified where required)
→ Initiate a screening request for an applicant
   (invite by email or phone; choose the report package and who pays)
→ Applicant authorizes the screening and verifies their identity
   (enters their own sensitive identifiers; pays if tenant-paid)
→ Platform compiles the reports from data sources
   (jurisdiction rules filter what may be returned)
→ Requester reviews the report and decides
   (accept / decline / conditional; adverse-action notice if declined on report grounds)
→ Applicant retains rights
   (view own report, dispute inaccuracies, free copy after denial)
```

Two initiation directions exist. In the **requester-initiated** flow, the landlord invites the applicant and the report generates once the applicant has authorized, verified, and (where applicable) paid. In the **applicant-initiated** flow, the applicant orders the screening themselves — increasingly as a portable report they can reuse across applications within a validity window where the regime allows it.

### What the platform does and does not do

The platform compiles, packages, filters, and delivers. It does not decide: every researched product delivers the report to the requester, who accepts, declines, or sets conditions. The platform's compliance role is to make the requester's lawful use of the report easy — consent capture, jurisdiction filtering, adverse-action notices, dispute handling — not to make the rental decision.

### Failure and exception paths

- **Applicant does not complete** — the report cannot generate until the applicant authorizes, verifies identity, and pays (when tenant-paid); requests sit in an invited/started state.
- **Credit freeze** — a frozen credit file blocks the pull until the applicant lifts it; a fraud alert does not block but adds verification steps.
- **Identity verification failure or expiry** — the applicant may need to redo verification if the request ages; unresolved mismatches stall the report.
- **No credit file** — thin-file applicants pass through with little data; income verification and rental references become the weight-bearing evidence.
- **Jurisdiction restriction** — the platform returns fewer or modified records (or none for a component) in restricted jurisdictions, and may withhold a component entirely (for example, credit reports where voucher-substitute rules apply).

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Requester dashboard

The requester's primary surface.

- lists screening requests with per-applicant status (such as invited / started / ready) and completed report history
- primary actions: initiate a screening request, open a report, accept or decline the applicant, resend or remind

### Report view

The decision surface for one applicant.

- typically opens with a summary snapshot, then sections for credit (score, payment history, collections), criminal records, eviction records, and income where included
- primary actions: read section detail, share or print, act on the applicant

### Request-initiation surface

Where a screening begins.

- enter the applicant's email or phone, select the report package, choose who pays
- primary actions: send invitation, attach to a property or application

### Applicant-side flow

The subject's surface, usually mobile-web.

- receive the request, authorize, complete identity verification, enter payment where applicable, view their own report
- primary actions: approve, verify, pay, access report, dispute

### Compliance surfaces

- adverse-action notice generation (template or automated), conditional-acceptance handling, jurisdiction rule documentation

## Important Rules / Behaviors

- **No report without the subject's authorization.** The pull is gated on the applicant's consent; sensitive identifiers flow from the applicant, not through the requester. This is the structural gate that separates a screening platform from a people-search tool.
- **The decision stays with the requester.** The platform reports; the landlord decides. Products that automate the decline notice are executing the requester's decision, not making their own.
- **Jurisdiction rules shape the report itself.** What may be returned — and whether it may be considered at all — varies by location: coverage gaps, lookback limits, conditional-acceptance requirements, fee caps, voucher-substitute rules, and portable-report mandates. A report is a filtered artifact, not a raw data dump.
- **Adverse-action obligations attach to use.** Denying (or conditioning) an applicant because of report content triggers notice duties naming the reporting source, with copy and dispute rights for the applicant.
- **Reports are freshly pulled per request.** A screening reflects the data sources at pull time; identity verification has a limited validity, and reused (portable) reports are accepted only within regime-defined windows.
- **Soft pulls are the norm.** Screening inquiries typically do not affect the applicant's credit score.
- **Per-report, per-applicant economics.** Pricing is per screening request; the fee is commonly tenant-paid, which makes the applicant's completion (including payment) part of the flow itself.

## Variants

- **By hosting form** — standalone screening products; screening modules inside landlord toolsets; screening modules inside property-management suites (the leasing pipeline's report step); screening embedded in rental listing venues (attached to the application flow).
- **By verification philosophy** — fully automated instant reports vs human-reviewed screening, where trained screeners verify identity and records to reduce false matches and omit non-compliant records.
- **By initiation and payer** — landlord-invited with tenant-paid fee (dominant in the independent-landlord segment); landlord-paid; applicant-initiated portable reports reused across applications.
- **By customer tier** — independent landlords; agents through MLS integrations; professional managers; enterprise operators with API integration, tiered screening workflows, and dedicated support.
- **By data supply** — some platforms are the data source itself (bureau-owned products); most are integrators over bureau, court, registry, bank, and payroll data vendors, and the supplier mix differs by product.
- **By regime** — the researched sample is US-market, where consumer-report law shapes the flow; other markets run analogous referencing structures under their own regimes. The defining core above is written in regime-agnostic terms.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Rental Application Platform | sibling, most easily confused | its record is the application: the applicant's declared qualifications and the decision flow. This Type's record is the screening request and the report machinery. The decoupling is visible in products that sell applications without reports and report-only orders |
| Background Check Platform | same regulatory grammar, different package | organization-initiated screening for employment eligibility centers criminal/court/registry screens; this Type centers credit + eviction + income for a tenancy decision, with tenant-initiated and tenant-paid flows common |
| Residential Property Management | container | the suite's record is the tenancy and portfolio; embedded screening is this Type at module grain inside the leasing pipeline |
| Property Showing Platform | upstream neighbor | pre-screening there is a scheduling gate over viewing requests (questions or hard gates), not report machinery |
| Employment Verification Platform | component supplier | employment/income facts verified as one report component here; that Type's record is the employment record and verification request itself |
| Identity Verification | component | identity checks gate the flow on both sides but are not this Type's record |
| Credit Scoring Application | component supplier | rental-specific scores are produced as report components, bound to rental risk rather than lending |
| Tenant / Resident Portal | different subject | serves the existing resident's occupancy; this Type evaluates the prospective applicant before any tenancy exists |

## Representative Products

- TransUnion SmartMove — bureau-native screening sold by the data source itself
- RentSpree — standalone screening product with landlord and agent/MLS distribution
- TurboTenant — screening embedded in a free landlord toolset, tenant-paid
- RentPrep — human-reviewed screening service with an enterprise tier
- Zillow Rental Manager — screening embedded in a rental listing venue

The defining core was checked across these poles to avoid over-fitting to any one hosting form, data supplier, or payer model.

## Sources

Research date: **2026-09-10**

- TransUnion SmartMove — https://www.mysmartmove.com/ (how it works, report products, packages, FAQ, adverse-action and dispute resources)
- RentSpree — https://www.rentspree.com/tenant-screening ; help center: https://support.rentspree.com/en/screening-restrictions-and-limitations
- TurboTenant — https://www.turbotenant.com/tenant-screening/ (product page and screening FAQ)
- RentPrep — https://rentprep.com/ (packages, verification process, add-ons, enterprise tier)
- Zillow Rental Manager Help Center — https://help.zillowrentalmanager.com/hc/en-us/articles/4404822950291 ; https://help.zillowrentalmanager.com/hc/en-us/articles/360058413693

> Sourcing limitation: enterprise-suite screening products (large property-management platforms) could not be reached directly this pass; their structure is corroborated through suite-embedded observations recorded in the paired Research Notes. All sampled products are US-market; regime-specific rules are described only where the sampled products document them, and the defining core is phrased regime-agnostically.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
