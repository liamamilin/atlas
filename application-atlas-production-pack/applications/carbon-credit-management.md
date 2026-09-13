# Carbon Credit Management

## Overview

A **Carbon Credit Management** application is an organization-side system of record for carbon credits treated as managed assets. It tracks which credits the organization holds, where each credit came from (project, standard, vintage), how it was acquired, and how it was eventually used — retired against an emissions claim, delivered to a buyer, or transferred — while keeping the registry-linked evidence that makes each credit's provenance and use defensible to auditors, regulators, and stakeholders.

The defining core is small:

```text
Credit (identified unit tied to a project / standard / vintage)
└── Portfolio / inventory (the organization's holdings)
    └── Recorded transactions (acquire → hold → transfer / deliver → retire or sell)
        └── Evidence trail (registry references, retirement records, certificates)
```

Everything else commonly associated with these products — project marketplaces, scientific diligence, RFP workspaces, AI-assisted analysis, API integrations, framework-specific reporting — is widespread in current products but is not what makes the software a carbon credit management application. A compliance-market participant tracking holdings and surrenders in a registry account, or an early voluntary-market buyer maintaining a spreadsheet of serial numbers alongside registry confirmations, satisfies the same core without any of those features.

When the software's center of gravity shifts to measuring the organization's own emissions, it becomes a Carbon Accounting Platform; when it shifts to market execution and price discovery, it becomes a Carbon Trading Platform.

## Users & Context

**Buyer side** (the dominant pole):

- sustainability / climate leads: define what the portfolio must achieve, which project types and volumes fit the company's claims and budget, and when credits should be retired
- procurement / carbon buyers: source projects, compare offers, negotiate contracts (spot purchases or multi-year offtake agreements)
- finance and audit stakeholders: rely on purchase records, retirement records, and registry references as evidence for disclosures and internal sign-off
- executives / board reporting: consume portfolio status and impact summaries

**Supplier side** (a distinct pole served by some products):

- carbon project developers and their commercial teams: manage the credits their projects generate as sellable inventory — from forecast volumes through verification and issuance, through pricing, sales channels, contracts, and delivery to buyers

Typical context: corporate net-zero and climate-commitment programs, voluntary carbon market participation, and increasingly regulatory disclosure regimes that require auditable claims about offsetting and removal purchases. The work is characterized by long time horizons (credits bought today may be delivered or retired years later), scarcity and quality risk (not all credits are equal, and future vintages may fail to materialize), and high evidentiary standards (a credit's value collapses if its provenance cannot be proven or if it is claimed twice).

## Core Model

### The defining core

**Credit.** The central object: a unit of verified climate benefit (avoidance or removal, typically denominated in tonnes of CO₂-equivalent). A credit is never anonymous — it is bound to an identified source project, an issuing standard or registry, and a vintage (the year the benefit was generated or verified). These identity attributes are what make credits trackable, comparable, and claimable.

**Portfolio / inventory.** The organization's holdings of credits as a persistent managed collection. On the buyer side this is a portfolio of acquired credits across projects and vintages; on the supplier side it is the developer's sellable inventory, organized in batches. Mature buyer-side products track the whole portfolio — including credits purchased outside the platform — so the portfolio, not the transaction, is the unit of management.

**Transaction.** Credits move through recorded events: acquisition (purchase, forward agreement, offtake contract, or issuance into inventory), transfer or delivery between parties, and disposition — retirement or cancellation (the buyer's terminal act that consumes the credit against a claim) or sale/delivery (the supplier's terminal act). Each event is recorded against the credit, so the portfolio always answers "what do we hold, where did it come from, what happened to it."

**Evidence trail.** Registry references (registry IDs), retirement records, certificates, and purchase records attached to credits. This is what separates credit management from generic commodity inventory: the credit's entire value depends on verifiable, non-double-counted provenance, so the system must be able to produce, for any credit, the chain from project to registry entry to retirement.

### Standard capabilities around the core

Mature products commonly add:

- **Project catalog** — rich, standardized profiles of available projects: type (avoidance vs removal; nature-based vs engineered), location, methodology, co-benefits, indicative availability and pricing
- **Quality vetting / diligence layer** — structured evaluation of projects against published criteria (additionality, verification, permanence, leakage risk, co-benefits), increasingly assisted by AI over standardized project data
- **Procurement machinery** — RFP-style sourcing across many suppliers, offer collection and comparison, negotiation support, and contracting (single contract spanning multiple projects; spot vs multi-year offtake)
- **Retirement management** — initiating and recording retirements with registry-linked records, and surfacing certificates and retirement evidence for claims and audits
- **Delivery risk management** — monitoring projects at key stages, early warning of delays, and replacement protections when a future vintage fails to deliver
- **Reporting and audit posture** — exportable, audit-ready records aligned to disclosure frameworks and internal sign-off
- **Dashboards** — portfolio status, impact totals, spend, and market/price context
- **Human expertise layer** — embedded strategists, in-house climate scientists, or advisory services alongside the software

### One structure, many implementations

```text
Concept:   Credit identity
Implementations:  registry serial / registry ID, project + standard + vintage attributes, batch IDs

Concept:   Portfolio custody
Implementations:  buyer portfolio (incl. off-platform purchases), supplier inventory batches

Concept:   Disposition
Implementations:  registry retirement / cancellation (buyer), delivery to buyer (supplier)

Concept:   Evidence
Implementations:  registry-linked retirement records, certificates, purchase records, audit exports
```

## How It Works

### The buyer loop

```text
Define strategy (claim needs, budget, project-type criteria)
→ source and vet projects (catalog, diligence, offers)
→ contract and purchase (spot, forward, or multi-year offtake)
→ take delivery of credits into the portfolio
→ retire credits against claims (registry-linked record)
→ report and defend the portfolio (audit-ready evidence)
```

The loop is continuous rather than one-shot: portfolios are built and rebalanced over years, future vintages are contracted before they exist, and retirement typically happens against a specific reporting period or claim.

### The supplier loop

Observed in supplier-side commerce products; the buyer loop is the dominant form in the market.

```text
Forecast credit volumes from project activity
→ measure and verify (credits move toward issued status)
→ issue credits into inventory (batched)
→ set pricing and publish to sales channels
→ sell (proposals, contracts, payments)
→ deliver credits to buyers
```

Supplier-side products manage the same object — the credit — from the opposite end: their terminal event is delivery to a buyer rather than retirement against a claim.

### Retirement is the buyer's terminal event

A held credit is an asset; a retired credit is a used asset. Retirement (or cancellation, depending on registry terminology) permanently consumes the credit against a claim and produces the record that evidences the claim. Products differ in whether they execute the retirement with the registry on the buyer's behalf or record a retirement performed elsewhere — but in both cases the retirement record, linked to the registry entry, is what the portfolio exists to produce.

### Delivery risk is a first-class concern

A large share of credits — especially removals — are bought as future vintages under forward or offtake agreements. Mature products therefore treat delivery as a managed state: monitoring project progress, surfacing delays early, and in some products providing replacement commitments when a project fails to deliver. A portfolio's true position is not just what is held but what is contracted-but-not-yet-delivered.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Portfolio dashboard

The primary buyer surface.

- what the organization holds, by project, type, vintage, and status (held / contracted / delivered / retired)
- impact totals, spend, and coverage against claim needs
- primary actions: inspect credits, plan retirements, export evidence

### Project catalog / sourcing workspace

Where sourcing happens.

- project profiles with type, location, methodology, co-benefits, availability, and price context
- diligence summaries and quality evaluations
- primary actions: shortlist projects, request offers, compare suppliers

### Procurement / offers workspace

- RFP-style requests to multiple suppliers, collected offers, negotiation and offer tracking
- contracting across multiple projects, spot vs multi-year structures
- primary actions: issue RFP, review offers, negotiate, contract

### Retirement / evidence records

- per-credit registry references, delivery status, and retirement records
- certificates and exportable audit packages
- primary actions: initiate or record retirement, retrieve registry-linked evidence, export for disclosure

### Supplier consoles (supplier-side products)

- inventory by batch and stage of maturity (from forecast volumes through verification to issued credits; exact stage names vary by product)
- pricing per batch, synchronized across sales channels
- sales pipeline, proposals, contracts, payments, and delivery planning
- primary actions: update inventory stage, set price, publish to channels, manage a sale through delivery

### API (some products)

- programmatic purchase and retirement for embedded use cases (e.g., offsetting tied to transactions), with structured project metadata and real-time status

## Important Rules / Behaviors

### Retirement is irreversible

Once a credit is retired (or cancelled), it is consumed. It cannot be resold or claimed again. This irreversibility is the mechanism that prevents double counting and is why the retirement record is the portfolio's most important output.

### One credit, one claim

The system's integrity depends on each credit being claimed at most once. Identity attributes (registry ID, project, vintage) plus the evidence trail exist to enforce and demonstrate this.

### Credits must remain traceable to their registry

A credit held in the portfolio is a mirror of an authoritative registry entry. Products keep registry references attached to every credit so that any holding can be verified against the registry of issuance — including credits acquired outside the platform.

### Future vintages can fail

Credits contracted for future delivery are a promise, not a holding. Delivery risk (project underperformance, delay, reversal risk for nature-based projects) is managed explicitly — through monitoring, staged payments weighted toward delivery, and replacement protections in some products.

### Quality is not uniform

Credits vary enormously in integrity. The vetting/diligence layer — criteria, scientific review, standardized project data — exists because acquiring a low-quality credit creates claim risk, not just financial risk. Portfolio composition (project types, geographies, vintages) is a managed decision, not an accident of availability.

### Evidence must be audit-ready

Because credits increasingly support regulatory disclosures, the records the system produces — purchase records, registry references, retirement records — are expected to stand up to auditor and regulator scrutiny without manual reconstruction.

## Variants

- **Buyer-side portfolio management** — the dominant form: strategy, sourcing, diligence, purchase, retirement, reporting for corporate buyers
- **Supplier-side credit commerce** — software for project developers to run inventory, pricing, sales channels, and delivery as a commercial operation
- **Dual-sided platforms** — products serving both buyers and suppliers, with the credit as the shared object
- **Standalone vs suite module** — dedicated credit platforms vs a marketplace/credits module inside a broader sustainability or carbon-accounting platform
- **Instrument scope** — carbon-only vs broader environmental attributes (renewable energy certificates, sustainable aviation fuel certificates, clean power)
- **Acquisition model** — open marketplace vs curated portfolios vs bespoke procurement services vs API-embedded purchasing
- **Voluntary vs compliance posture** — voluntary-market portfolio management vs compliance-market holding and surrender tracking
- **Advisory depth** — software-only vs software bundled with embedded strategists or scientific advisory teams

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Carbon Accounting Platform | adjacent, often co-deployed | measures the organization's own emissions (Scopes 1–3, activity data, emission factors); credit management tracks offset instruments as assets. Remove the credits and accounting still stands; remove the measurement and credit management still stands |
| Carbon Trading Platform | adjacent | market execution and price discovery (exchanges, order books, speculation) vs custody, lifecycle, and claims evidence; overlap exists at procurement, but the defining job differs |
| Renewable Energy Certificate Management | sibling | identical structural pattern (tracked attribute units, retirement against claims, registry linkage) applied to energy attributes rather than carbon; different instruments, registries, and claim semantics |
| ESG Reporting Platform | downstream consumer | consumes credit data as one input among many for disclosures; does not manage the credits themselves |
| Decarbonization Planning Platform | upstream | plans emission reductions; credit management handles the offset instruments for residual emissions after reduction |
| Registry systems (standards-body infrastructure) | authoritative counterpart | registries issue and retire credits authoritatively; credit management is the organization-side system of record that mirrors and references them |

The sharpest boundary is with Carbon Accounting: the two are frequently bundled in one sustainability platform, but they manage different objects — the organization's emissions versus the offset instruments held against them.

## Representative Products

- **Patch** — buyer-side enterprise platform spanning strategy, sourcing, diligence, purchase, and portfolio management with registry-linked retirement records
- **Cloverly** — dual-sided: buyer purchasing with retirement management and an embedded API, plus Catalyst, commerce software for project developers
- **Carbon Direct** — science-led buyer-side carbon management with curated and bespoke removal portfolios and purchase/retirement tracking
- **Watershed** — broad sustainability platform whose Marketplace module provides vetted projects, portfolio building, and centralized purchase records integrated with the company's carbon footprint

## Sources

Research date: **2026-09-07**

- Patch — https://www.patch.io/ , https://www.patch.io/how-it-works , https://www.patch.io/rfp
- Cloverly — https://www.cloverly.com/ , https://www.cloverly.com/catalyst/commercial-credit-operations , https://www.cloverly.com/buyers
- Carbon Direct — https://www.carbon-direct.com/ , https://www.carbon-direct.com/solutions/remove
- Watershed — https://www.watershed.com/ , https://www.watershed.com/platform/marketplace

> Sourcing limitation: research relied on official product and marketing pages; help-center-level operational documentation was not reachable from the research environment, and Patch's developer docs returned a JavaScript shell. Precise operational details (numeric limits, pricing, default settings, exact retirement workflows per registry) are intentionally not stated in this document; vendor-specific claims and numbers remain in the paired Research Notes. Assertions are calibrated to product-page evidence.
