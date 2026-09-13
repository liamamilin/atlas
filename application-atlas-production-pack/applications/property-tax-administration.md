# Property Tax Administration

## Overview

A **Property Tax Administration** system is a government's system of record for property tax money. It receives certified taxable values from the assessment side, applies the jurisdiction's levies to produce each property's tax bill, records payments against those bills across every collection channel, pursues delinquent balances under statutory charges, and settles the collected money to the taxing entities entitled to it.

The defining structure is deliberately small:

```text
Certified taxable values (from the assessment side)
└── Levy-driven billing
    (taxing entities + rates/levies applied per property → the tax bill)
    └── The tax bill/account of record
        (liability per property × tax year: amount due, payments,
         penalties and interest, status)
        └── Collection & settlement loop
            (payments by every channel → delinquency machinery →
             distribution to the taxing entities)
```

Remove the bill and there is no liability to collect. Remove the levy machinery and the product is generic invoicing. Remove collection and settlement and it is a bill printer.

The professional division underneath the software is worth stating plainly: the assessing office determines **value**; the levying bodies — county, municipality, school district, special districts — set **rates and levies**; the tax administration office **applies both**. It computes, bills, collects, and distributes. It originates neither the value nor the rate. Everything commonly bundled with these products — cashiering hardware, taxpayer portals, escrow-agent portals, business and tourist taxes, business intelligence — is standard capability or variant machinery, not part of what makes the product what it is.

## Users & Context

**Internal operators** work for the collecting authority — a county treasurer, tax collector, tax commissioner, or a municipal revenue office:

- **tax clerks / cashiers**: take payments at the counter and by mail, issue receipts, answer account inquiries
- **billing staff**: run bill cycles, produce and print bills, process corrections, refunds, and supplements
- **delinquency / tax-sale staff**: manage delinquent accounts, statutory notices, payment plans, and lien or deed processes
- **office leadership (treasurer / collector)**: oversee settlement to taxing entities, reconciliation, and reporting

**External parties**:

- **property owners and taxpayers**: look up bills, pay online or in person, sign up for e-billing and reminders
- **mortgage servicers, escrow agents, and banks**: submit bulk payment files against large numbers of parcels
- **taxing entities** (counties, municipalities, school districts, special districts): receive distributions of collected money and settlement reports
- **state oversight bodies**: receive statutory reports

The work environment is a high-volume, audit-heavy annual cycle rather than a continuous transaction stream: levies and rates are configured, bills are run and mailed, the collection season peaks, delinquency machinery engages, and money is settled out to the entities — then the cycle repeats for the next tax year.

## Core Model

### The Defining Core

**The tax bill/account of record.** The individually identified liability record — one property (or taxpayer account) for one tax period — carrying the amount due, the payments and credits applied, the statutory charges (interest, penalties, fees), and the current status. It is the object every workflow touches: bills are produced from it, payments post to it, delinquency is computed from it, corrections amend it, and settlement draws on it. Mature systems keep the full history per account — payments to date, corrected bills, notes and documents — because the record is the office's official account of who owes what.

**Levy-driven billing against taxable values.** The jurisdiction's taxing entities and their rates or levies are maintained in the system and associated with properties. A single property commonly sits inside several taxing bodies at once — county, city, school district, special districts — and one tax bill aggregates all of their levies. The calculation applies these levies to the **taxable values** received from the assessment side, together with billing-time adjustments the jurisdiction provides (deductions, credits, exemptions applied at billing, special assessments). This levy machinery is the Type's specificity: it is what makes the output a property tax bill rather than an invoice.

**The collection-and-settlement loop.** Payments arrive through every channel the office offers — over the counter, by mail, in bulk files from banks and escrow agents, and online — and are recorded against the bills. Balances that remain unpaid past the statutory date become delinquent and accrue further charges; the office notices, pursues, and (where the regime provides) enforces through tax lien or tax deed processes. Collected money is not the office's to keep: it is distributed and settled to the entitled taxing entities according to their shares, with settlement reporting. This loop — collect the money, then settle it out — is what makes the system a revenue administration rather than a payment page.

### Capabilities Shared by Mature Products

These are standard in current products but do not define the Type:

- **cashiering** — over-the-counter and remote/batch payment entry with real-time interest, penalty, and fee calculation; receipts
- **payment channels** — online payments (card, e-check, digital wallet), mail/lockbox, bank tape files, escrow-agent and mortgage-servicer portals
- **delinquency machinery** — delinquency determination, additional interest/penalty/fee calculation, notices, payment plans, write-offs
- **tax-sale machinery** — lien certificate sales, tax-defaulted property deed sales, deed applications (where the jurisdiction's regime provides)
- **escrow/bulk payment processing** — payment files from mortgage companies and tax-paying agents, duplicate-payment prevention, refund handling
- **corrections machinery** — court orders, additions and abatements, supplements, bill transfers, protested payments, waivers, corrected bills
- **distribution/settlement engines** — apportionment by entity share, check printing, ACH transfers, settlement and disbursement reporting
- **public portal** — inquiry, e-billing and reminders, payment, forms, report downloads
- **reporting** — by tax year, political subdivision, and tax type; collector's and delinquent books; full audit trails; statutory reports
- **adjacent local revenue** — business tax and licenses, special assessments, tourist/occupancy tax, motor-vehicle cashiering, often in the same platform
- **GIS integration, dashboards, business intelligence, workflow and event logs**

### One Structure, Many Implementations

The core is written conceptually. Realizations vary:

```text
Concept:   The bill/account of record
Variants:  parcel-anchored real property bills ↔ broader taxpayer accounts
           (business, personal property, tourist tax); single year ↔
           multi-year history with delinquent years alongside current

Concept:   Levy machinery
Variants:  rate/millage tables ↔ levy and fund structures; billing-time
           exemptions/deductions ↔ exemption-free regimes; special
           assessments and surtaxes as separate lines on the same bill

Concept:   Collection & settlement
Variants:  counter + mail ↔ full digital channels; delinquent balances
           pursued by penalty/interest only ↔ lien sales ↔ deed sales;
           settlement by check runs ↔ automated ACH apportionment
```

## How It Works

The system's rhythm is the **tax year cycle**. A typical pass through it:

### 1. Receive values and configure levies

```text
Certified taxable values arrive from the assessment side
→ ownership changes and supplements update the billing population
→ taxing entities, rates/levies, and special assessments configured for the year
```

### 2. Calculate and produce bills

```text
Levies applied to each property's taxable value
→ deductions/credits and special assessments applied
→ bill run produces the year's tax bills (printed in the jurisdiction's formats,
   commonly bar-coded)
→ bills mailed; receipts generated
```

### 3. Collect

```text
Payments arrive: counter, mail, online, bank tape files, escrow-agent files
→ each payment posted against the bill/account
→ receipts issued; partial payments tracked
→ duplicate-payment checks and refunds processed (bulk escrow flows)
```

### 4. Track delinquency and enforce

```text
Unpaid balances pass the statutory date → delinquent
→ interest/penalties/fees accrue; notices generated
→ payment plans or write-offs where allowed
→ where the regime provides: tax lien certificate sale or
   tax-defaulted deed sale; deed applications processed
→ bankruptcy/litigation filings constrain collection
```

### 5. Distribute and settle

```text
Collected money apportioned to the entitled taxing entities
→ checks printed / ACH transfers executed
→ settlement and disbursement reports produced (by entity, district, year)
→ reconciliation with the office's financial system
```

### 6. Correct and adjust (ongoing)

```text
Court orders, additions, abatements, supplements, protested payments
→ corrected bills produced; history preserved
→ refunds issued where money must go back
```

### Core vs Standard vs Optional

**Defining core** — without these, not a property tax administration system:

- the tax bill/account as the persistent liability record
- levy-driven billing against taxable values (taxing entities, rates/levies, one bill aggregating multiple entities)
- the collection-and-settlement loop (multi-channel payments, delinquency tracking, distribution to taxing entities)

**Standard capabilities** — present in most mature products:

- cashiering, online payment, escrow/bulk payment processing, delinquency machinery, corrections, distribution engines, public portals, reporting/audit trails, adjacent local revenue, GIS and BI overlays

**Optional / variant** — depends on jurisdiction and posture:

- tax-sale machinery (regime-dependent), bankruptcy/litigation case handling, installment/discount schemes, bill print/mail as a vendor service, deployment model, the breadth of adjacent revenue lines

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Cashiering / collection screen

The clerk's primary surface for taking money.

- typical information: account/bill lookup (by parcel number, bill number, owner, bar code), amount due, accrued charges, payments to date
- primary actions: post a payment, calculate interest/penalties/fees, issue a receipt, handle partial payment, note the account

### Bill run and billing engine

The billing staff's surface over the year's bill population.

- typical information: bill batches by year/subdivision/type, bill formats, print queues
- primary actions: run calculations, generate/print bills, produce corrected bills, generate notices and receipts

### Levy and rate maintenance

The configuration surface for the jurisdiction's taxing structure.

- typical information: taxing entities, rates/millage, funds, special assessments, billing-time deductions/credits
- primary actions: maintain entities and rates, associate entities with property classes, configure calculations

### Delinquency workbench

- typical information: delinquent accounts by year, accrued charges, notice status, payment plans, bankruptcy flags
- primary actions: determine delinquency, calculate charges, generate notices, arrange payment plans, write off, prepare tax-sale files

### Tax sale processing

- typical information: sale candidates, lien certificates, bidders/investors, deed applications
- primary actions: run or support the sale, record certificates and transfers, process deed applications

### Distribution / settlement

- typical information: collected totals by entity, apportionment shares, disbursement batches
- primary actions: execute distributions (checks/ACH), produce settlement reports, reconcile

### Taxpayer portal

The public surface.

- typical information: bills by parcel/address, amounts due, payment history, e-billing enrollment
- primary actions: search, view, pay, sign up for e-billing/reminders, download receipts

### Escrow / agent portal

The bulk-payer surface for mortgage companies, tax-paying agents, and banks.

- typical information: parcel tax files, payment status, exceptions
- primary actions: retrieve tax files, submit payment files, resolve exceptions and refunds

### Reporting

- typical information: collections by year/subdivision/type, delinquent books, settlement reports, audit trails
- primary actions: generate, review, export, file

## Important Rules / Behaviors

### The office applies value × levy; it sets neither

The taxable value comes from the assessment side; the rates and levies come from the levying bodies. The tax administration office's calculation is the application of both. This division is the structural seam to the assessment system, which produces the certified values the billing engine consumes.

### One bill, many taxing entities — and the money flows back

A bill aggregates the levies of several taxing bodies for the same property. Collected money is therefore apportioned back to those entities according to their shares, with settlement reporting. The system is the settlement authority between taxpayers and taxing entities, not merely a payment collector.

### Delinquency accrues by statute; enforcement is regime-dependent

Unpaid balances accrue interest, penalties, and fees on the jurisdiction's schedule, and notices follow. What happens next varies by regime: some jurisdictions sell tax lien certificates to investors, some sell tax-defaulted property deeds, some pursue other remedies. The delinquency machinery is universal; the enforcement endpoint is not.

### Corrections are governed events

After billing, amounts change only through named processes — court orders, additions, abatements, supplements, refunds, protested payments — each producing corrected bills while preserving the audit trail. This is what makes the account an official record rather than a spreadsheet.

### Duplicate payments and refunds are a named problem

Bulk escrow flows mean multiple parties may pay the same bill. Mature products explicitly prevent duplicate escrow payments and streamline refunds; a reduction in refunds and duplicate payments is a documented outcome offices buy these tools for.

### Bankruptcy and litigation constrain collection

Filings open cases that restrict or redirect collection activity; mature products carry bankruptcy/litigation case handling beside the delinquency machinery.

### Money is settled, not just received

Distribution — check runs, ACH transfers, settlement and disbursement reporting by entity, district, and year — is part of the loop, reconciled with the office's financial system.

## Variants

- **office scope** — county treasurer, tax collector, or tax commissioner; combined offices vs the separate appraisal-district + tax-office model (in some states the value operation and the money operation are separate organizations with separate systems)
- **regime machinery** — lien-certificate states vs tax-deed states vs regimes without tax sales; installment and discount schemes; billing-time exemptions and credits
- **suite posture** — standalone collection system ↔ integrated land-records suite spanning appraisal to collection ↔ collection specialist paired with separate payment/auction products
- **deployment** — on-premises installations and cloud/SaaS offerings both documented
- **adjacent-revenue breadth** — from property-tax-only to platforms that also bill and collect business taxes, licenses, tourist/occupancy taxes, and motor-vehicle items
- **bill production** — in-system printing vs vendor-operated print/mail services

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Property Assessment System | upstream producer | assessment produces the **value** of record (mass appraisal, the certified roll); this Type produces the **money** of record (levies, bills, payments, distribution). The certified taxable values are the hand-off artifact. Suite vendors sell them as separate product lines, and in some states they are separate offices |
| Land Records / Cadastre System | sibling on the parcel spine | land records holds the **rights** record (deeds, instruments); this Type holds the money record. Ownership changes flow in as billing inputs |
| Tax Administration System | generic sibling | the generic Type is a revenue authority's machinery for all tax types; this Type is the parcel-anchored, roll-fed, levy-and-distribution variant. Adjacent local taxes (business, tourist) are commonly bundled here, but the parcel/roll anchor defines the leaf |
| Government Revenue Management | broader | revenue accounting and collections across sources; this Type is the property-tax-specific machinery |
| Utility Billing | surface-adjacent | both "bill → collect → delinquent", but utility billing is metered recurring service billing with no roll input and no taxing-entity distribution |
| Payment Gateway / Payment Processing | bundled capability | payment rails appear as modules or separate product lines; the Type's center is the liability record, the levy, and the settlement, not the rails |
| Mortgage Servicing Platform | private-side counterpart | servicers pay property taxes from escrow through this system's escrow/agent portals; the servicer's own escrow machinery is a different Type |
| Government GIS | adjacent | GIS maintains parcel geometry; map layers may display tax data, but they do not hold the money of record |

The most important boundary is the parcel-spine trio: **rights (land records) — value (assessment) — money (taxation)**. Each Type owns one operation over the same parcels, and each consumes the others' outputs.

## Representative Products

- DEVNET — Edge Billing & Collection (the Collector solution inside an integrated land-records suite spanning appraisal to collection)
- Aumentum Technologies — Aumentum Tax (levy management, billing, collection, cashiering, distribution within a multi-state property tax platform)
- Catalis — Tax Billing & Collections (cloud property tax collection beside CAMA, escrow, and oversight product lines)
- Grant Street Group — TaxSys (cloud-hosted tax billing, collection, and distribution for large counties, with lien/deed auction platforms)
- Harris Govern — Property Tax & Collections (tax billing, cashiering, delinquency, and levy/distribution within appraisal-and-collections suites)

The definition was checked against the paper-era tax office (tax books, rate levies, handwritten receipts, published delinquent lists, tax sales) and against non-US property-tax collection regimes at the conceptual level, so that no modern machinery (online payment, escrow portals, SaaS, BI) is treated as part of what makes the Type what it is.

## Sources

Research date: **2026-09-09**

- DEVNET — Billing & Collection: https://www.devnetinc.com/billing-collections/ ; company: https://www.devnetinc.com/
- Aumentum Technologies — Aumentum Tax: https://www.aumentumtech.com/tax-collection ; company: https://www.aumentumtech.com/
- Catalis — Billing & Collections: https://catalisgov.com/tax-cama/billing-collections/ ; Escrow Payment Management: https://catalisgov.com/tax-cama/escrow-payment-management/ ; Property Tax Oversight: https://catalisgov.com/tax-cama/property-tax-oversight/ ; Tax & CAMA: https://catalisgov.com/tax-cama/
- Grant Street Group — Tax Collection (TaxSys): https://www.grantstreet.com/tax-collection ; company: https://www.grantstreet.com/
- Harris Govern — Property Tax & Collections: https://www.harrisgovern.com/tax-collection-software/ ; company: https://www.harrisgovern.com/
- IAAO (International Association of Assessing Officers) — General Assessment FAQs (via the paired property-assessment-system research): https://www.iaao.org/industry-data/general-assessment-faqs/

> Sourcing limitation: official pages of Tyler Technologies (a major platform vendor in this market) could not be reached from the research environment (HTTP 403, recorded in the sibling assessment pass) and are used as a market anchor only, with no structural claims drawn from them. All sampled evidence is official vendor product/solution pages; no help-center-level operational documentation was reachable, so precise operational parameters (penalty schedules, sale windows, installment counts, settlement calendars) vary by jurisdiction and are intentionally not stated in this document. The sampled evidence is North America-weighted; non-US property-tax collection regimes are covered at the conceptual level only.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample check are recorded in the paired Research Notes.
