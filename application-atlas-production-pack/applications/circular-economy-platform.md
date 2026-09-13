# Circular Economy Platform

## Overview

A **Circular Economy Platform** is a multi-party software system for keeping physical products, components, and materials in productive use. Its world is organized around **circular objects** — identified goods or material lots held by participants — and the **loop pathways** that move or account for them toward restorative outcomes: reuse, redeployment, resale, recycling, recovery, or verified circular claims. Disposal is not the terminal success state here; it is the outcome the system exists to avoid or measure against.

Every circulation event is recorded, which is what turns reuse, recycling, and recovered content from anecdotes into auditable, reportable, claimable evidence.

The defining core is deliberately small:

```text
Circular objects (identified products, components, or material lots held by participants)
  └── Loop pathways (reuse, redeploy, resell, recycle, recover — instead of terminal disposal)
      └── Recorded circular outcomes (transfers, custody changes, recoveries, measured flows)
          └── Circularity visibility (impact metrics, indicators, credentials, audit trails)
```

Everything else commonly associated with these products — marketplaces, escrowed payments, logistics, digital product passports, indicator frameworks, regulatory report packs — is a standard capability of particular product shapes, not part of the definition.

## Users & Context

The primary users are organizations and trading participants whose goods or materials have remaining circular value:

- **Facilities, workplace, and asset teams** inside enterprises, universities, healthcare systems, and venues — they hold surplus furniture and equipment and must decide between repurchasing, redeploying, donating, selling, or discarding.
- **Corporate sustainability teams and their consultants** — they must measure and report how circular their products and material flows are, increasingly under reporting frameworks.
- **Manufacturer and brand compliance teams** — they must trace materials through multi-tier supply chains and share verifiable product-level data with customers and regulators.
- **Scrap traders, recyclers, and purchasers** — they buy and sell secondary materials as their core business.
- **Collector-network operators, producer-responsibility organizations, and brands** — they run or fund collection and need verified evidence of what was collected, by whom, and where it went.

Typical occasions of use: a building decommissioning, an internal move or clear-out, a periodic circularity assessment, a supply-chain data request, a scrap lot negotiation, an incentive-backed collection program.

## Core Model

### Circular objects

The managed object is always a **physical good or material positioned as recoverable** — a chair, a batch of stainless scrap, a battery's material content, a ton of collected plastic. It carries the attributes that make circulation possible: what it is, its condition or composition, its grade or specification, where and with whom it currently sits. Objects range from item-level assets to anonymous material lots to aggregate material flows inside products.

### Participants and custody

Objects have holders. Depending on the product shape, these are internal business units, member organizations of a network, verified trading companies, n-tier suppliers, or individual collectors with digital identities. Custody — who holds what, where — is the state the platform tracks.

### Loop pathways

Each object faces a choice of next loops:

```text
                  ┌── reuse / internal redeployment
Circular object ──┼── resale / external transfer
                  ├── recycling / material recovery
                  ├── verified circular claim (recycled content, custody)
                  └── disposal  ← the path the platform exists to avoid
```

The platform's job is to make the loop pathways visible and workable — surfacing what is available, matching supply with demand, moving custody, or evaluating how much of a material flow actually takes the restorative branches.

### Recorded circular outcomes

Whatever happens to an object, the platform records it as evidence: a transfer or sale with its approvals, a chain-of-custody record, a registered collection event, a measured restorative flow. These records aggregate into circularity visibility — items exchanged, material diverted from waste, recycled content traced, circularity indicators computed, impact credentials issued. The evidence trail is what allows organizations to prove — internally, to customers, or to regulators — that circulation actually happened.

### One structure, many implementations

The core model is conceptual. Different product shapes implement it differently:

```text
Concept:            Circular object
Implementations:    asset item (condition, location) · material lot (grade, spec) ·
                    material content of a product (composition) · collected-material quantity

Concept:            Participant / custody
Implementations:    org units in one company · verified marketplace members ·
                    n-tier suppliers · registered collectors

Concept:            Loop pathway
Implementations:    internal reuse marketplace · B2B trading venue ·
                    chain-of-custody tracking · circularity indicator models ·
                    deposit / premium incentive programs

Concept:            Circularity visibility
Implementations:    impact dashboards · compliance reports · product passports ·
                    escrowed trade records · verified impact credentials
```

### Capability tiers

**Defining core** — without these, the product is not a circular economy platform:

- circular objects held by identified participants
- loop pathways toward restorative outcomes
- recorded circular outcomes forming an evidence base

**Standard capabilities** — present across mature products, expected in the market:

- multi-party network with participant identities and verification
- object catalog: listing, browsing, and search by material, condition, location, or grade
- transfer machinery: requests, approvals, matching, negotiation
- circularity and impact metrics: diversion from waste, avoided emissions, recycled-content or circularity indicators
- audit and evidence trails behind every outcome
- data-quality handling for data supplied by others (reference values, supplier declarations, tamper-resistant logs)

**Optional / shape-dependent capabilities**:

- payment handling and escrow, price discovery
- logistics coordination (collection and delivery of goods/materials)
- digital product passports and permissioned data sharing
- reporting against specific frameworks and regulations
- incentive programs (deposits, premium payments)
- consulting and program-design services around the tool

## How It Works

Four characteristic loops cover the product family. They share one spine: **register the object → orient it to a loop → record the outcome → aggregate circularity.**

### The reuse loop (assets)

```text
Inventory what the organization owns
→ post an item as available (internal reuse, sale, or donation)
→ another unit or organization discovers it (search/browse)
→ request and approval
→ transfer of custody
→ outcome recorded (value recovered, waste avoided)
```

The point is to substitute reuse for repurchasing: the registry makes idle items visible, the approval workflow keeps governance, and the recorded outcome feeds impact reporting.

### The trade loop (secondary materials)

```text
Seller lists a material lot (type, grade, quantity)
→ buyers discover and negotiate
→ transaction secured through the platform
→ logistics arranged (collection from seller, delivery to buyer)
→ delivery confirmed; trade recorded
```

Here the platform acts as trusted intermediary: verifying participants, securing payment, and coordinating movement of the material.

### The traceability loop (supply chains)

```text
Request data from suppliers across tiers
→ collect declarations and evidence
→ maintain chain of custody / mass balance across transformations
→ share the result (product passport, permissioned disclosure)
→ claims become verifiable downstream
```

No goods change hands in the platform; what circulates is verified information about materials, attached to product identifiers.

### The measurement loop (circularity performance)

```text
Assemble material-flow and composition data
→ fill gaps with reference values where supplier data is missing
→ compute circularity indicators
→ compare scenarios and improvement options
→ report against chosen frameworks
```

The objects here are the organization's material flows; the loop orientation appears as the indicators themselves — how much input is restorative rather than virgin, how much output is recovered rather than wasted.

## Interfaces

Exact layouts vary by product. The recurring surfaces:

### Object catalog / exchange surface

- purpose: make available objects discoverable
- typical information: item or lot descriptions, condition/grade, quantity, location, holder
- primary actions: search and browse, post a listing, request, buy, or make an offer

### Registry / inventory view

- purpose: the system of record for what participants hold
- typical information: asset or material records with location, condition/composition, value context
- primary actions: add and update objects, attach documents and evidence, organize by site, team, or project

### Transfer / transaction surface

- purpose: move custody of an object with governance
- typical information: parties, terms, approvals, logistics status, payment state where trading
- primary actions: request or approve a transfer, negotiate, arrange logistics, confirm completion

### Traceability / custody view

- purpose: show where materials and claims come from
- typical information: supplier tiers, declarations and evidence, custody or mass-balance chains, product identifiers
- primary actions: request supplier data, review and verify evidence, publish or share passport data

### Measurement / reporting dashboard

- purpose: turn recorded outcomes into circularity visibility
- typical information: indicators, trends, comparisons, framework-aligned report views
- primary actions: run an assessment, build scenarios, generate reports

### Network administration

- purpose: govern participation in a multi-party system
- typical information: members, verification status, roles and permissions
- primary actions: invite and verify participants, manage teams and access

## Important Rules / Behaviors

- **Disposal is not the terminal success state.** A cleared building, a shipped scrap lot, a reported indicator — whatever the surface, the system treats an object's re-entry into use as the outcome worth achieving, and records disposal as the outcome being measured against.
- **Claims require evidence.** Impact numbers, custody claims, and circularity indicators are all backed by recorded events — transfers, logs, declarations. This evidence-first behavior is what separates these platforms from generic listings or generic ESG dashboards.
- **Trust is gated.** Participation and claims are conditioned on verification — of companies, of materials, of data sources. Who may post, buy, or claim what is controlled per participant.
- **Transfers are governed.** In reuse-oriented products, moving an item across units or organizations typically involves an approval step, keeping asset control with the owner organization.
- **Data gaps are handled explicitly.** Where information must come from other parties (suppliers, collectors), products handle missing data with declared reference values, structured declarations, or tamper-resistant capture — the provenance of every number stays inspectable.
- **Money is optional; security is not.** Trading-oriented shapes move real money through the platform and treat payment protection as central; other shapes carry no money movement at all. What all shapes protect is the integrity of the record.

## Variants

- **Asset reuse platform** — inventory plus internal/external exchange for durable goods; governance-heavy; impact reporting tied to avoided purchases and waste.
- **Secondary-material trading marketplace** — B2B venue for scrap and recyclables; verification, secured payment, and logistics are the core services.
- **Supply-chain traceability platform** — multi-tier data collection, chain of custody, and product passports; driven largely by regulation.
- **Circularity measurement platform** — indicator computation and framework reporting over material-flow data; often bundled with consulting services.
- **Collection-network platform** — verified collection events, incentives, and impact credentials; connects informal or distributed collectors to formal markets and producer-responsibility schemes.

Other common variation axes: regulation-driven (EU product-passport and reporting era) versus voluntary-framework versus market-driven products; closed internal networks versus open marketplaces; item-level versus lot-level versus aggregate-flow objects; and standalone tools versus tool-plus-services hybrids.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Recycling Operations Management | runs the recycler's own facility operations (intake, processing, outputs); a circular economy platform is the circulation and visibility layer *between* holders, not plant software |
| Waste Management Platform | routes discarded material to collection and treatment; terminal state is disposal/processing, whereas a circular economy platform treats re-entry into use as the success state |
| Sustainability Management Platform / ESG Reporting | measures organization-wide environmental, social, governance performance; a circular economy platform's managed world is the material loops themselves, with ESG reporting as one output |
| Carbon Accounting Platform | unit of account is the organization's greenhouse-gas inventory (activity data × emission factors); a circular economy platform's unit of account is material objects and flows |
| Recommerce Platform | brand-operated consumer resale of secondhand goods for value recovery; circular economy exchange shapes serve business/organizational participants and account outcomes as circulation, not brand revenue |
| Online Marketplace / Resale Marketplace | general trading venues for any goods; circular economy marketplaces trade goods with secondary-material identity and record circular outcomes |
| Inventory Management System | tracks what an organization owns for operational purposes; a circular economy registry exists to route items into reuse loops across parties and to account for the outcomes |

The sharpest everyday confusion is with waste and recycling software. The test: **whose operations does the software run, and what is the terminal success state?** Plant-operations software for processors is Recycling Operations Management; collection-and-disposal routing is Waste Management Platform; software that connects holders and moves or accounts objects toward their next use is a Circular Economy Platform.

## Representative Products

- **Rheaply** — asset inventory plus internal reuse and sustainable disposition for workplace and real estate teams (enterprises, universities, healthcare)
- **Circular IQ (CTI Tool)** — circularity measurement, gap analysis, and framework-aligned reporting for corporate sustainability teams
- **Circularise** — multi-tier supply-chain traceability, chain of custody, and digital product passports for manufacturers and brands
- **ScrapAd** — B2B marketplace for scrap and recyclable metals with member verification, secured payment, and logistics
- **Empower / Jörð.tech** — collection-network traceability, incentive programs, and impact credentials for the recycled-materials value chain

These five were selected to cover the distinct product shapes of the category; each is an instance of the same defining core with a different loop emphasis.

## Sources

Research date: **2026-09-07**

- Rheaply — homepage and Help Center: https://rheaply.com/ , https://support.rheaply.com/en/
- Circular IQ — homepage and baseline-assessment page: https://circular-iq.com/ , https://circular-iq.com/baseline-assesment/
- Circularise — homepage: https://www.circularise.com/
- ScrapAd — homepage (EN): https://scrapad.com/en/
- Empower Foundation / Jörð.tech — https://www.empower.eco/

> Sourcing limitation: deep operational documentation (help centers, product UIs) was reachable for one sampled product only; the others were observed through official product/marketing pages, and their application surfaces are login-gated. Accordingly, this document avoids precise operational details (indicator formulas, escrow mechanics, passport data schemas, numeric limits), and capability claims that could not be verified beyond vendor pages are stated at the level the sources support. One additional candidate source (a waste-flow analytics product) was unreachable after repeated attempts and is not cited.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical market-sample check are recorded in the paired Research Notes.
