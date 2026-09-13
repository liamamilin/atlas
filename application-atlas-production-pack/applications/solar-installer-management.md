# Solar Installer Management

## Overview

A **Solar Installer Management** application is the solar installation company's project system of record: it holds customers and the sites where systems are installed, carries each solar project from first contact through a sale-driven lifecycle (lead → system design → proposal → signed contract → permitting and utility approval → installation → permission-to-operate), derives the project's equipment and price content from a system design for the specific site, tracks the external approvals that legally gate construction and operation, coordinates the installation work, and resolves the project's money — customer payment or a financing arrangement.

The defining core is small:

```text
Customer (with the installation site)
└── Solar project of record
    │   lead → design → proposal → signed contract
    │   → permitting + interconnection → installation
    │   → permission-to-operate
    ├── The site's system design as the content basis
    │   (array layout + equipment + production estimate
    │    feed the proposal and the bill of materials)
    ├── The external-approval path
    │   (construction permit with the jurisdiction;
    │    grid interconnection / permission-to-operate
    │    with the utility — tracked as project state)
    ├── Installation execution
    │   (milestones, tasks, site visits, crews)
    └── Commercial resolution on the project
        (contract execution; cash / loan / lease-PPA money path)
```

Everything else commonly associated with these products — pipeline boards, AI design engines, AHJ requirement databases, lender integrations, customer portals, lead-capture funnels — is standard capability that mature products add, not what makes the product a solar installer management system. An installer running on a customer card file, a hand-drawn array layout, a paper permit application, a crew wall calendar, and an invoice book already satisfies the defining core.

The Type is structurally distinct from generic business-management software in three ways: the project's content derives from a **designed engineered system with a production promise** (not typed-in line items), the project carries a **tracked external-approval path** (permit plus grid connection — without it the system cannot legally be built or turned on), and the money leg is **financing-dominated** (loans and third-party ownership are embedded in the sale, not bolted on). The market reflects this: solar is served by a dedicated software ecosystem built around exactly these structures, not by a configuration of a horizontal field-service vendor.

## Users & Context

Primary users:

- **Sales rep / solar consultant** — works leads, often builds the first design and proposal in front of the customer, presents production and savings, gets the contract signed.
- **System designer / engineer** — produces or refines the site's system design: array layout, equipment selection, shading and production analysis, electrical diagrams where required.
- **Operations / project coordinator** — moves sold projects through the post-sale path: orders or requests plan sets, tracks permit and utility approvals, schedules site visits and installations, manages change orders, keeps customers informed.
- **Install crew** — executes the physical installation; work is scheduled and tracked as milestones and tasks on the project.
- **Owner / manager** — monitors the pipeline, installation throughput, and project economics.

Secondary participants:

- **Customer (homeowner or building owner)** — receives the design-backed proposal, signs the contract, follows installation status, commonly through a portal or shared proposal.
- **Authority having jurisdiction (permitting office)** — external reviewer of the permit plan sets; the product prepares and tracks the application, it does not adjudicate.
- **Utility** — external approver of the grid interconnection; permission-to-operate is the project's terminal event.
- **Lenders and financing partners** — providers of the loan, lease, or power-purchase arrangements presented on proposals and processed behind signed contracts.
- **Permitting / engineering service partners** — suppliers of plan sets, engineering reviews, and stamps, engaged from inside the project when the installer does not produce them in-house.

Typical context: residential solar installation companies dominate the market; several products extend the same structures to commercial and small industrial systems. The office works in a web dashboard organized around a project pipeline and an installation tracker; sales reps and designers work in design and proposal surfaces; customers interact through proposals, signing links, and status portals. The lifecycle phrase the industry itself uses — from first knock to permission-to-operate — describes the arc the system exists to carry.

## Core Model

### The Defining Core

**Customer with the installation site.** A record of the person or organization the system is for, bound to the property where it will be installed. The project binds to the site's address; the utility account and the billing party usually sit here too.

**Solar project of record.** The unit of work and the center of the system. One project represents one customer's solar (and commonly storage) installation at one site. A project carries:

- the customer, the site address, and the utility context
- the system design: array layout, equipment selection, production estimate
- the proposal and the signed contract
- the approval path: permit state and interconnection/permission-to-operate state
- the installation work: milestones, tasks, schedules
- photos, notes, documents, and activity history
- the money: pricing, financing arrangement, payments
- change orders when the as-built diverges from the as-sold

The lifecycle is **sale-driven with a regulated tail**: projects enter as leads, are won through a design-backed proposal and signed contract, then pass through the external approvals and the installation before reaching permission-to-operate — the point at which the system is legally connected and the installer's job is done.

**The site's system design as the content basis.** The project's equipment and price content derives from a system design for the specific site: panels placed on the actual roof (or ground), equipment selected, and production estimated from shading and irradiance analysis against the site's orientation and the customer's consumption. The design is what the proposal promises — expected production, bill offset, savings — and what the bill of materials is computed from. Mature products realize this with in-product 3D design engines, integrated third-party design tools, done-for-you design services, or manual entry; the conceptual structure is the same: **the designed system, not free-typed line items, is what the project sells and builds**.

**The external-approval path.** A solar installation is gated by two external approvals, and the project tracks both as first-class state:

- **the construction permit** with the authority having jurisdiction — permit plan sets (site plans, array layouts, electrical single-line diagrams, structural details), engineering reviews and stamps where required, and the permit application itself;
- **the grid connection** with the utility — the interconnection application and, at the end, permission-to-operate.

Approval documents are generated in-product (from the design, against jurisdiction requirement databases), procured from permitting and engineering partners engaged from inside the project, or produced by the installer's own staff. What is definitional is not who produces them but that **the approvals live on the project as tracked state** — a project is not finished when it is built, but when it is approved and turned on.

**Installation execution.** The sold project converts into scheduled, tracked work: site visits, installation events, milestones and tasks assigned to teams or crews. Progress is recorded against the project, customers see status through portals, and divergences from the as-sold design are handled as change orders.

**Commercial resolution on the project.** The project carries its contract — executed by e-signature — and its money path: customer cash payment, a loan, or a third-party ownership arrangement (lease or power-purchase agreement). Pricing is carried on the project from the proposal onward; at the operations-heavy pole, the required documents are compiled into complete signing packets and transactions are processed through the platform with deals routed across lenders.

### Standard Capabilities of Mature Products

These are widespread in current products and make the core practical, but a product lacking some of them can still be recognized as this Type:

- **Sales pipeline** — projects organized as cards in customizable stages from lead through sold and installed, with kanban or table views, assignable actions, and due dates.
- **Design-backed proposals** — interactive proposals presenting the design's outcome: production, savings, utility-bill offset, financing options; sent, presented, and signed digitally.
- **Financing integrations** — loans and third-party ownership (lease/PPA) presented on the proposal and processed behind the contract, with cash-deal escrow and lender routing at the products that operate the money flow; credit soft-pulls and title checks at the operations-heavy pole.
- **Permitting machinery** — jurisdiction requirement databases, automatic generation of permit plan sets and single-line diagrams from the design, engineering stamps, and request workflows to permitting service partners.
- **Customer portals** — a per-project surface where the customer sees the proposal, documents, and real-time installation status.
- **Lead capture** — instant-estimate and AI-assisted funnels that turn a site address into a first design and quote.
- **Storage / battery extension** — batteries designed, sold, and permitted as part of the same project flow.
- **Bill of materials and equipment purchasing** — BOMs generated from the design; equipment catalogs and supplier purchasing at some products.
- **Incentives** — tax credits and regional incentive schemes handled inside pricing and proposals.
- **Change orders** — tracked when the installation diverges from the as-sold design.
- **Roles and permissions, calendars, reporting, integrations** — team roles, schedule views, dashboards over pipeline and installs (depth varies by product), CRM/accounting integrations, and APIs.
- **Dealer and channel machinery** — dealers or sales organizations working on shared accounts with per-partner branding, pricing, and equipment settings.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  The designed system
Implementations:  in-product 3D design engines with shading
                  analysis, integrated third-party design tools,
                  done-for-you design services, manual entry

Concept:  The approval path
Implementations:  in-product plan-set generation against
                  jurisdiction databases, permitting/engineering
                  partner services engaged from the project,
                  automated permitting services, installer-produced
                  paperwork tracked as project state

Concept:  Installation execution
Implementations:  milestone trackers from contract to PTO,
                  task management with assignment, calendars
                  holding site visits and installs, customer-
                  visible status portals

Concept:  The money
Implementations:  cash (with escrow at some products),
                  lender-routed loans, third-party ownership
                  (lease/PPA), e-signed contracts, pricing
                  carried from proposal to project
```

A reader who only encounters one implementation — say, an AI design tool with a proposal builder — should still be able to recognize the fuller installer-management systems from the core model, and vice versa.

## How It Works

The canonical flow of a solar installation project:

```text
Lead (referral / canvassing / web funnel / instant estimate)
→ create the project on the pipeline
→ design the system for the site
   (array layout from imagery or site visit; shading and
    production analysis; equipment selection; bill of materials)
→ build and present the proposal
   (production, savings, bill offset; financing options shown)
→ contract signed (e-signature)
→ financing arranged (loan / lease / PPA / cash)
→ approvals:
    permit plan sets prepared (generated from the design or
    requested from a permitting partner)
    → permit application tracked with the jurisdiction
    → interconnection application tracked with the utility
→ installation scheduled and executed
   (milestones, tasks, crews; photos and progress recorded;
    change orders if the as-built diverges)
→ final approvals complete → permission-to-operate
→ project closes; system handed over
```

Four loops are worth distinguishing:

**The sales loop (per lead).** Leads enter from referrals, canvassing, web funnels, and instant-estimate tools; the first design is often produced before any site visit. The design-backed proposal — showing what the system will produce and what it will save — is the pivot that wins the sale, and the signed contract authorizes the post-sale path.

**The approval loop (per sold project).** After the sale, the project's critical path often runs through external parties: plan sets must match the jurisdiction's requirements, the permit must be issued, and the utility must approve the interconnection. The system tracks each approval's state on the project, generates or procures the required documents, and keeps the project moving while waiting.

**The installation loop (per sold project).** The sold project converts into scheduled work — site visits, install days, milestones — executed by crews or teams and documented against the project. Because the proposal promised a specific designed system, divergences surface as change orders rather than silent substitutions.

**The money loop (per project).** The contract and the financing arrangement are executed at the sale; customer payments and lender payouts follow the project's progress, with cash-deal escrow processed through the platform at the products that operate the money flow; pricing and costs stay visible on the project. In third-party-ownership deals the contracting counterparty differs, but the money still resolves against the same project record.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Project pipeline

The sales side's primary surface.

- project cards in stage columns (lead → design → selling → sold), table and kanban views, filters and saved views
- primary actions: create project, move stage, assign, open project

### Project record

The record of one installation; the most information-dense surface.

- customer and site, design, proposal and contract, permit and interconnection states, milestones and tasks, documents and photos, money, change orders, activity history
- primary actions: design, build proposal, request plan set, track approval, schedule work, add documents, record change order

### Design surface

- the site in 2D/3D imagery, array placement, equipment selection, shading and production analysis, bill-of-materials output
- primary actions: model the site, place arrays, choose equipment, run production analysis, push to proposal

### Proposal builder

- design-derived production and savings presentation, financing options, e-signature state
- primary actions: build, present, send, collect signature

### Approval tracker

- permit and interconnection states on the project, plan-set requests and their status, jurisdiction requirements
- primary actions: generate or request plan set, submit application, update approval state

### Installation tracker / calendar

- milestones from contract to permission-to-operate, tasks with assignees and due dates, site visits and install events, customer-visible status
- primary actions: schedule, assign, update milestone, record completion, raise change order

### Customer portal

- the customer's view of their project: proposal, documents, contract, real-time installation status

### Reporting / dashboard

- pipeline conversion, installation throughput and cycle time, approval bottlenecks, project economics

## Important Rules / Behaviors

### The sale is the pivot — and the design is the promise

A project is not "sold" until the contract is signed; the signature is what authorizes the post-sale path. And because the proposal promised a specific designed system with a specific production estimate, the design is the commitment the installation must deliver: divergences are handled as change orders, and design accuracy before the sale is what prevents them.

### The project is not done when it is built

The terminal event is permission-to-operate: the system is built, inspected, approved by the utility, and turned on. Permit and interconnection states are tracked on the project as first-class state, and installation scheduling commonly waits on them. A built-but-unapproved system is an unfinished project.

### Approvals are external; the system prepares and tracks

The product does not grant permits or approve interconnections — the jurisdiction and the utility do. What the product does is generate or procure the application documents from the project's own design data, submit or hand off to permitting partners, and track each approval's state so the project's critical path stays visible.

### The money path is chosen at the sale

Cash, loan, or third-party ownership changes who pays and who owns the system, and the contract machinery compiles the documents each path requires. The arrangement is carried on the project and resolved as the project progresses.

### The as-built can diverge from the as-sold

Site discoveries, equipment substitutions, and customer changes are recorded as change orders against the project rather than silently absorbed, keeping the contract, the permit documents, and the installed system reconciled.

### Roles gate configuration and economics

Day-to-day project work is open to sales, design, and operations roles; business-wide configuration — pricing, equipment catalogs, workflows, financing setup, partner settings — is restricted to admin-level roles. Dealer and channel partners see the account through per-partner settings.

## Variants

- **Residential installation** — the market's center of gravity: homeowner-funded systems sold through design-backed proposals, commonly financed.
- **Third-party-ownership sales** — lease and power-purchase agreements where a financing party owns the system; the contracting counterparty and money path change, the project structure does not.
- **Commercial / C&I installation** — larger systems, longer approval paths, commercial design tooling; drifts toward construction-project machinery at this pole.
- **Storage-led and electrification extensions** — batteries, and at some products heat pumps or EV charging, sold and delivered through the same project flow.
- **Design-led vs operations-led products** — some products center on the design and proposal engine; others center on the post-sale project tracker and integrate design from outside; both realize the same project arc.
- **Done-for-you services** — plan sets, engineering stamps, and permit packages procured from service partners engaged inside the product, vs self-service generation.
- **Regional regimes** — the approval path's vocabulary varies by market (permitting authority and utility interconnection in North America; connection schemes and incentive accreditation elsewhere); the tracked-approval structure is the invariant.
- **Trade-agnostic pole** — installers running generic CRM and spreadsheet tooling with point products for design and financing; the boundary with generic business management.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Small Business Field Service Management | closest sibling; shared spine | generic dispatched service jobs vs solar's designed-system content basis, tracked external-approval path, and financing-dominated money leg; generic tools serve solar installers only as fragmented point tooling |
| Roofing Contractor Management | closest structural sibling | both sale-driven production businesses with a trade-specific technical definition of the work; roofing quantifies from measurements of an existing surface and resolves through retail/insurance payment, solar designs an engineered system with a production promise and resolves through approvals and financing |
| Solar Asset Management | different seat, downstream | the asset owner/operator's system for running the built system (production monitoring, performance, O&M); this Type ends at permission-to-operate and handover |
| Home Improvement Contractor Management | trade sibling (generalist pole) | both sale-driven home-improvement work with production behind the sale; solar adds the designed-system basis, the approval path, and financing depth |
| CRM | front half only | leads, pipeline, and proposals without design, approvals, execution, or project money |
| Construction Project Management | adjacent at the commercial pole | multi-organization contractual project coordination vs the installer's own sale-to-PTO business system |
| Permit Management (government-side) | different seat | the authority's permit-office system adjudicates; here the permit is one approval state on the installer's project, with the application prepared and tracked |
| Solar design tools and permitting service bureaus | capability suppliers | design without the project system; permitting without the project — both integrate into this Type |
| Local Service Marketplace | demand-side adjacent | consumer discovery and quote requests; a marketplace lead becomes a project here |
| Electrical Service Management | trade sibling | shared family spine only; that Type centers on dispatched electrical service visits, not the sale→design→approve→install→PTO project arc |

The most important boundary is with generic field-service and business management: the two share the entire customer→project→execution→money spine. The durable difference is structural, not cosmetic — the designed system as the project's content basis, the external-approval path as tracked project state ending in permission-to-operate, and the financing-dominated money path — and it is strong enough that the market maintains a dedicated solar software ecosystem alongside generic tools.

## Representative Products

- **Aurora Solar** — design-led platform spanning sell, design, finance, and deliver, with plan-set services and an AHJ requirement database; strong in residential, with a commercial product line
- **OpenSolar** — free all-in-one platform (leads, design, sell, manage) with a project-management CRM and permitting integrations; global small-and-mid installer base
- **Solargraf** — design, proposal, and permitting all-in-one with done-for-you permit services and engineering stamps; residential and commercial
- **Enerflo** — operations-led "operating system" connecting CRM, design tools, financing, contracting, and an install tracker from contract to permission-to-operate; US residential

The core model was checked across four products with different philosophies (design-led, free-all-in-one, permitting-led, operations-led) so that no single vendor's packaging defines the Type.

## Sources

Research date: **2026-09-09**

- Aurora Solar (Tier 2, official site): https://www.aurorasolar.com/ — root incl. product structure; https://aurorasolar.com/aurora-for-installers/ — installer page (lead-to-install, AHJ database, dealer accounts); https://aurorasolar.com/plan-sets/ — Plan Sets Service. (Tier 1, help center): https://help.aurorasolar.com/hc/en-us — category structure (Design, Proposals & Documents, Pricing and Financing incl. Incentives, Utility Rates, Storage, Heat Pumps, Plan Sets, Integrations)
- OpenSolar (Tier 2, official site): https://www.opensolar.com/ — root incl. product nav; https://www.opensolar.com/project-management-crm/ — projects, workflows, scheduling; https://www.opensolar.com/permitting/ — permitting integrations (plan sets, PE stamps, permit applications, interconnection, PTO); https://www.opensolar.com/auto-design/ — design engine and BOM generation
- Solargraf (Tier 2, official site): https://solargraf.com/ — root incl. pillars and audiences; https://www.solargraf.com/solar-permitting — permitting machinery (AHJ database, single-line diagrams, permit packages, PE stamps)
- Enerflo (Tier 2, official site): https://enerflo.io/ — root incl. full feature sections (sales process, design integrations, financing, contracting, customer portals, install tracker, reporting)

> Sourcing limitation: OpenSolar's help center and Sunbase's site could not be reached (timeouts / empty responses), so OpenSolar is asserted at official-product-page depth and Sunbase was dropped from the sample. Jobber's solar industry page returned HTTP 403 (consistent with prior research passes), so the trade-agnostic pole is evidenced indirectly rather than by a fetched generic product. Post-install monitoring handoff, crew-management depth, and invoicing detail were not documented in any fetched source and are deliberately not claimed. No precise numeric limits, prices, or vendor-specific statistics are stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
