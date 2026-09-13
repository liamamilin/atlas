# Configure Price Quote / CPQ

## Overview

A **Configure Price Quote (CPQ) application** is a seller-side sales application in which a saleable offer is assembled under rules, priced by the system, and committed as a quote. It exists because complex B2B selling — configurable products, bundles, services, subscriptions, negotiated discounts — regularly produces the same three questions: *what exactly are we selling, at what price, and committed to which buyer?* CPQ answers them with rules and computation instead of memory and spreadsheets.

The defining structure is a triple:

```text
Configure — assemble an offer from a seller-maintained catalog,
            guided by rules for what can be combined
Price     — compute the price of that offer from stored price data
            and pricing rules, recalculated as the configuration changes
Quote     — hold the configured, priced offer as a stateful record
            addressed to a specific buyer, render it as the buyer-facing
            output, and hand the accepted result onward
```

Everything commonly bundled with modern CPQ — guided selling flows, price books, CRM and ERP integration, e-signature, approval automation, subscription and renewal machinery, buyer self-service configurators, AI suggestions — is widespread in current products but is not what makes a product a CPQ. A tool with only quote documents is a proposal tool; a tool with only a product configurator is a catalog guide; a tool with only computed feasibility is a calculator. The three structures together are the Type.

## Users & Context

CPQ is used by organizations that sell configurable, bundled, or otherwise non-trivially priced offerings — equipment, software and subscriptions, services, telecom, and anything whose "correct" combination and price exceed what a rep can reliably hold in their head.

Primary users:

- **Sales representative** — assembles the offer for a specific deal: selects and configures products, adjusts quantities and options, applies discounts, and produces the quote for the buyer. Most quoters work inside their CRM context; the quote travels with the deal.
- **Sales operations / administrator** — maintains what makes quoting trustworthy: the product catalog and its options and bundles, the rules for valid combinations, the pricing rules, and the discount policies. In configuration-heavy businesses this role works with product and engineering teams on the models themselves.

Secondary users:

- **Manager / finance approver** — reviews quotes that cross discount or margin thresholds and approves or rejects them.
- **Channel partner / distributor** — quotes on the vendor's behalf, typically against partner-scoped catalogs and price books.
- **Buyer** — in some deployments, configures and requests quotes themselves through a self-service web or e-commerce surface.
- **Downstream consumers** — order management, contracting, and billing functions receive the accepted quote as their input.

## Core Model

### The Defining Core

```text
Product Catalog (products, options, bundles, models)
└── Configuration of a specific offer
    │   governed by rules: valid combinations, required components
    └── Computed Price
        │   base/option prices + pricing rules + discount rules,
        │   recalculated as the configuration changes
        └── Quote (stateful offer record for a specific buyer)
            │   rendered as the buyer-facing output
            │   revised through negotiation; governed internally
            └── Accepted outcome → order / contract
```

- **Product catalog.** The seller-maintained inventory of what can be sold: individual products, options and attributes, bundles, and reusable product models. The catalog is not just a price list — it encodes structure (what attaches to what, what substitutes for what) that configuration operates on.
- **Configuration.** The interactive assembly of a specific offer for a specific deal: picking products, choosing options, adding bundle components, setting quantities and terms (such as contract duration). Rules constrain the assembly — required components are added automatically, incompatible combinations are blocked or corrected. The output is a set of quote lines that together describe what is being sold.
- **Computed price.** The system, not the rep, derives the numbers: base and option prices, quantity or term effects, customer- or segment-specific conditions, and discounts are applied and the totals recalculated in real time as the configuration changes. Mature products make the calculation path transparent (how the list price became the net price), which is what lets a rep defend the number in a negotiation.
- **The quote.** A persistent, identified offer record addressed to a specific buyer. It holds the configuration, the computed prices, and the commercial terms; it can be rendered as a buyer-facing document; it is revised as the deal is negotiated; and on acceptance it becomes the commercial source of truth that downstream systems consume. The quote is both a *record* (stateful, revisable, synced into the sales system of record) and an *output* (the document the buyer actually sees and accepts).

### Standard Capabilities

Mature products commonly add the following. They make CPQ practical; removing any one of them leaves the Type intact.

- **Quote document generation** — branded, template-driven buyer-facing output with pricing tables and terms, typically exportable as PDF or similar, commonly with integrated electronic signature for acceptance.
- **Guided selling** — step-by-step configuration flows, validation prompts, and cross-sell/upsell suggestions, so reps without deep product knowledge still assemble correct offers.
- **Price variation machinery** — price books, customer- or segment-specific pricing, volume-tier pricing, multi-currency support.
- **Discount governance** — discount thresholds and policies; quotes that exceed them route automatically to approvers, while within-policy quotes proceed without gating. Approval conditions commonly consider discount levels, margins, product selections, and deal attributes.
- **Quote lifecycle** — draft → internal approval (when required) → sent → viewed → accepted or declined, with revisions along the way and status reflected back in the seller's records.
- **Integration spine** — CRM (deal and customer context in; quote status out), product and pricing data upstream (ERP or platform-owned), e-commerce and self-service channels, and APIs for programmatic quoting.
- **Administration consoles** — catalog and bundle management, rule and pricing rule builders, approval workflow designers, all operated by non-engineering staff in mature deployments.
- **Reporting** — quote acceptance rates, deal velocity, discount and margin analytics.
- **Renewals and amendments** — machinery for extending, amending, or cancelling what was sold, dominant where offerings are subscription- or contract-based.

## How It Works

### Build the selling machinery (admin/sales ops, before any deal)

```text
Model the catalog
→ define products, options, attributes
→ assemble bundles and reusable product models
→ write the rules: required components, incompatible combinations
→ load price data and pricing rules (books, tiers, customer conditions)
→ configure discount policy and approval routing
```

This is the investment that distinguishes CPQ from a document template: the seller's selling knowledge is encoded as rules the system can enforce.

### Quote a deal (sales rep)

```text
Open the deal in the CRM context
→ start a quote
→ configure: select products, choose options, adjust quantities/terms
   (rules add required items, block incompatible ones;
    prices recalculate continuously)
→ apply discounts within policy — or trigger approval when not
→ render the buyer-facing quote document
→ send (and, where used, collect e-signature)
```

### Negotiate and resolve (rep + approver + buyer)

```text
Buyer pushes back
→ revise the configuration, quantities, or discounts
→ price recalculates; governance re-evaluates
→ reissue the quote (prior versions retained)
→ acceptance recorded
→ quote handed to order capture / contracting as the commitment
```

The loop — configure, price, present, negotiate, re-price — is the daily work of the application. Its end state is deliberately designed: CPQ ends when the offer becomes a commitment, and the accepted quote is the clean handoff to everything downstream.

## Interfaces

Conceptual surfaces; names and layouts vary by product.

### Quote editor / quote lines

The rep's central working surface, commonly resembling a spreadsheet of line items.

- typical information: lines with products, options, quantities, unit and net prices, discounts, contract terms, totals
- primary actions: add/configure products, adjust quantities and options, apply discounts, recalculate, save revision

### Configuration wizard / configurator

The guided flow that assembles a valid offer.

- typical information: option choices presented step by step, live visualization in configuration-heavy products, validation messages
- primary actions: select options, respond to suggestions, resolve flagged conflicts

### Quote document (buyer-facing)

The rendered offer the buyer sees and signs.

- typical information: branding, configured items and prices, terms and conditions, validity
- primary actions: send, download as PDF, collect e-signature

### Approval queue

The approver's surface for quotes that crossed a policy threshold.

- typical information: quote content, the condition that triggered review (e.g., discount level, margin)
- primary actions: approve, reject, request changes

### Administration console

Where the selling machinery is maintained.

- typical information: catalog items, bundles, rules, pricing rules, approval definitions
- primary actions: create/edit models and rules, publish changes, manage permissions

### Self-service configurator (where deployed)

A buyer-facing web surface exposing the same catalog, rules, and price computation to customers requesting quotes directly.

## Important Rules / Behaviors

**Only valid configurations may be quoted.** Rules determine which combinations, options, and required components constitute a sellable offer; the system enforces them at selection time, blocking or auto-correcting invalid assemblies. This rule-enforcement — not the UI — is what makes quoted offers trustworthy enough to hand to order capture.

**The price is derived, not typed.** Quote prices and totals come from the system's computation over stored price data and pricing rules. Reps influence price through policy channels (discounts, terms), not by editing numbers. Mature products expose the calculation path so sellers can explain it.

**Discounts are governed.** Discount and pricing policies define what a seller may commit to alone; crossing the policy routes the quote into an approval flow, typically with automatic routing to the right reviewers. Within-policy quotes move without gating. The approval mechanism itself is a common capability rather than a defining one — light deployments may have none — but where selling discipline matters, it is the control point of the whole tool.

**The quote is stateful and revisable.** A quote is not a static file: it persists with the deal, absorbs negotiation as revisions, carries its status (draft, awaiting approval, sent, accepted, declined), and its accepted form is what downstream systems treat as the commercial commitment. Prior versions are commonly retained.

**The Type ends at commitment.** CPQ produces and resolves the offer; order capture, contracting, and billing consume its output. It works with ERP and billing systems, but managing the order or the invoice is outside its center.

## Variants

- **CRM-embedded CPQ** — quoting lives natively inside the seller's CRM; the dominant packaging in the current market, but not definitional (standalone and document-platform add-on forms exist).
- **Enterprise suite CPQ** — standalone products positioned as the bridge between CRM and ERP, converting quotes into clean orders and carrying multichannel, multilingual, high-volume loads.
- **Document-first / lightweight CPQ** — quoting added to a document or proposal platform, deeply integrated with one or more CRMs; the configuration and pricing rule machinery is present but deliberately simple to adopt.
- **Manufacturing / engineer-to-order CPQ** — configuration models maintained in step with engineering; the system may validate that a quoted configuration is manufacturable and hand configuration data toward ERP/PLM/design tools; on-premise deployment survives in this segment.
- **Subscription-era CPQ** — recurring and consumption pricing, contract terms, renewals, amendments, and asset-based selling as first-class quote content.
- **Channel variants** — partner quoting with partner-scoped catalogs and price books; buyer self-service configurators and e-commerce RFQ surfaces.
- **AI-era additions** — quote drafting and summarization, configuration suggestions, discount and win-probability guidance; increasingly common, structurally optional.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Customer Relationship Management / CRM | container | CRM holds relationships, deals, and pipeline; CPQ produces the priced offer that moves through the pipeline. CRM-embedded packaging is common, but the offer machinery is its own Type. |
| Proposal Management | adjacent; closest seam | Proposal tools center on presenting an offer and capturing the buyer's decision (documents, deal rooms, acceptance); CPQ centers on computing a correct commercial offer (valid configuration + price under rules). They meet at the pricing table — proposal tools ship quote tables as a capability, CPQ ships document rendering as a capability. |
| Sales Document Automation | adjacent | Template → data assembly → tracked delivery to signature is a document-production loop; CPQ's center is the configuration and pricing rules engine, with document output as one step. |
| Sales Pricing Application | adjacent | CPQ computes prices at quote time from stored price data; pricing management as a discipline (setting and governing prices themselves) is its own center. The seam deserves joint treatment. |
| Deal Desk / Commercial Approval Platform | adjacent | CPQ embeds approval gates in the quoting flow; cross-functional deal policy-making is a broader center of gravity. |
| Sales Order Capture / Order Management | downstream | The accepted quote is their input; managing the resulting order is theirs, not CPQ's. One-way handoff. |
| Billing Platform | downstream | Billing charges what CPQ sold; CPQ hands off upstream and does not manage invoices or payment collection. |
| Product Configuration Management (Manufacturing) | namesake-adjacent, different side | Engineering/manufacturing-side configuration builds the product definition (BOM, variants); CPQ configures the *offer to sell it* at a price. The engineer-to-order CPQ variant bridges both sides but keeps the commercial quote loop at its center. |
| B2B E-commerce Platform | channel overlap | Commerce platforms expose self-service configuration and quoting to buyers; CPQ's center is seller-side negotiation machinery (governance, approvals, rep-driven assembly). A commerce configurator is one channel of CPQ, not the whole Type. |
| Insurance Quote Platform | industry analog | Insurance quoting rates a risk submission against external carriers' rating bases; CPQ configures the seller's own catalog. Similar word, different machinery. |

## Representative Products

- **Salesforce CPQ** (now packaged within Salesforce revenue-management offerings) — CRM-embedded market leader; rules-based and constraint-based configuration, unified catalog and pricing engine, discount approval chains, subscription and asset lifecycle machinery.
- **Oracle CPQ** — enterprise standalone suite; guided selling for sellers, partners, and customers; price books and multitier pricing; automated approvals; quote-to-order conversion into ERP.
- **PandaDoc CPQ** — document-platform add-on pole; admin-defined bundles and rulesets, formula-driven quote rules, conditional approvals, deep CRM two-way sync or standalone operation.
- **Tacton CPQ** — manufacturing-first pole; valid-option-only configuration at scale, prices computed for never-before-built variants, engineering-feasibility validation at the point of sale, cloud or on-premise deployment.

## Sources

Research date: **2026-09-07**

- Oracle — CPQ product page: https://www.oracle.com/cx/sales/cpq/
- Salesforce — CPQ / revenue management product page (incl. "What is CPQ" FAQ): https://www.salesforce.com/products/cpq/overview/
- PandaDoc — CPQ product page: https://www.pandadoc.com/cpq-software/
- PandaDoc — CPQ documentation: Using Rules and Formulas in Quotes: https://www.pandadoc.com/docs/cpq/how-to-guides/quote-rules-formulas/use-quote-rules-formulas/
- PandaDoc — CPQ documentation: Using Conditional Approvals: https://www.pandadoc.com/docs/cpq/how-to-guides/approvals/setup-approval-rules/
- PandaDoc — CPQ documentation: Product Bundles: https://www.pandadoc.com/docs/cpq/category/product-bundles/
- Tacton — CPQ platform page: https://tacton.com/products/tacton-cpq/

> Sourcing limitation: operational documentation libraries for Oracle CPQ and Salesforce CPQ were not reachable from the research environment (documentation-site paths returned errors; the Salesforce help portal rendered as an application shell), and SAP CPQ, DealHub, and Verenia could not be accessed at all. Vendor product pages and PandaDoc's CPQ documentation were the reachable evidence layer. Accordingly, this document makes no claims about numeric limits, thresholds, defaults, exact state names, or product-specific approval parameters; lifecycle and governance mechanics are described at the strength the sources support. Vendor-cited performance figures were treated as claims and excluded.
