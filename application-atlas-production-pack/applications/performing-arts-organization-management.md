# Performing Arts Organization Management

## Overview

A **Performing Arts Organization Management** application is an arts organization's audience-and-revenue system of record. It holds one unified database of the organization's patrons, sells admission to the organization's own performances and events through its own channels (box office and online), and runs the ongoing relationship loop — fundraising, memberships, and targeted communication — over the transaction history those sales and donations create.

The defining structure is the combination of three things in one system:

```text
Unified patron record
└── Ticketing for the organization's own events (box office + online)
    └── Recorded transactions feeding the relationship loop
        └── Fundraising / membership / marketing over the patron base
```

Remove the unified patron relationship and the product becomes a ticketing platform; remove ticketing and it becomes a donor CRM; remove the relationship loop and it becomes a bare box office terminal. The Type is defined by holding all three together for the organization's own audience.

## Users & Context

The operating user is the organization itself — a theatre company, orchestra, opera, dance company, performing arts center, or a broader arts-and-culture institution (museums, festivals, presenting organizations). Several functions share one system:

- **Box office staff** — sell tickets, process exchanges and returns, print tickets, take payments at the counter
- **Patron services / front of house** — handle subscriber and member inquiries, access control at the door
- **Development / fundraising staff** — manage donor records, run campaigns, cultivate gifts, track solicitations
- **Marketing staff** — segment the patron base, run email campaigns, manage contact preferences
- **Leadership / finance** — reporting on sales, donations, and reconciliation

The characteristic context is a recurring performance season: the same audience returns show after show, which is why the patron relationship — not the individual ticket — is the center of the system.

## Core Model

### The unified patron record

One persistent record per audience member sits at the center. Everything the person does with the organization attaches to it: ticket purchases, donations, memberships, subscriptions, communications received, contact preferences. The record is the join point between departments — the box office, the development office, and marketing all see (their permitted view of) the same person. Mature products provide customer lists, tags, and segmentation built on this record.

### Events, tickets, and orders

The organization configures its own events — performances, often organized in series or seasons — with dates, seating plans where applicable, and pricing. Selling produces orders: tickets (or admissions) plus any associated items, paid by the patron's chosen method, with returns and exchanges as first-class operations. Sales happen through the organization's own channels: the staffed box office (with ticket printers and scanners) and the online purchase path on the organization's website.

### Subscriptions, packages, and memberships

The season-subscription model — a patron committing to a package of performances in advance — is the sector's signature revenue structure, and mature products support it natively alongside single-ticket sales. Membership schemes (with benefits and renewal cycles) run on the same patron record.

### Donations and fundraising

Fundraising operates on the same database: donation records, campaigns, and donor cultivation tracked against the patron's giving history and ticket-buying behavior. The ticketing history is itself fundraising intelligence — who attends, how often, at what level.

### Communication and segmentation

The recorded history feeds outbound communication: patron segments (by attendance, giving level, preferences) receive email campaigns and mailings, with contact preferences managed per patron.

### Concept vs implementation

```text
Concept:                    Common implementations:
unified patron record  →    proprietary CRM database, Salesforce-native platform
selling channel        →    staffed box office + integrated web checkout, website-embedded components
cultivation loop       →    email campaigns, membership schemes, donation appeals, subscriber renewals
```

## How It Works

### Sell a ticket

```text
Patron identifies themselves (at the counter or by account online)
→ select event / performance / seats
→ order composed (tickets, fees, associated items)
→ payment taken
→ tickets issued (printed, mobile, or held at will-call)
→ transaction recorded on the patron's history
```

### Run the season

The organization sets up its season — events, seating, pricing, subscription packages — before sales open. Subscribers book their packages, single sales follow, and the box office works the ongoing cycle of exchanges, group sales, and access control on performance nights.

### Cultivate the audience

```text
Recorded purchases + donations build the patron's history
→ staff segment the patron base (lists, tags, giving/attendance levels)
→ campaigns and appeals go out (renewals, donation asks, season announcements)
→ responses (renewed subscription, gift, membership) record back on the patron
→ the cycle repeats across seasons
```

This loop — transaction history feeding cultivation feeding new transactions — is what makes the system a relationship system rather than a sales terminal.

### Core vs common vs optional

**Defining core** — unified patron record; selling admission to the organization's own events; the relationship loop over recorded transactions.

**Common mature structure** — reserved seating; subscriptions/packages/series; membership schemes; donations and campaigns; email marketing with contact preferences; reporting and payment reconciliation; ticket printing/scanning; gift vouchers.

**Optional / variant** — education program management; agent/third-party selling; merchandise and retail breadth; admissions-based (museum-style) selling; campus multi-department models; e-commerce website product vs website-integration approach.

## Interfaces

Described conceptually; exact layouts vary by product.

### Event / season setup

Purpose: configure what is being sold. Typical information: events, performances, seating plans, price zones, offers, subscription packages. Primary actions: create events and series, build seating plans, set pricing and offers, open and close sales.

### Box office / order processing

Purpose: sell and serve at the counter. Typical information: event availability, patron lookup, current order, payment methods. Primary actions: find or create the patron, build the order, take payment, print or issue tickets, exchange, refund.

### Patron record

Purpose: the single view of one audience member. Typical information: contact details, purchase history, donation history, memberships, communication preferences, tags. Primary actions: update details, view or add transactions, record a donation, manage preferences, segment.

### Fundraising / campaigns

Purpose: run donor cultivation. Typical information: campaigns, solicitation status, giving levels, donor lists. Primary actions: create campaigns, record gifts, track solicitations, build donor segments.

### Marketing / communication

Purpose: reach the right patrons. Typical information: segments, campaign content, contact preferences, response analysis. Primary actions: build a segment, send a campaign, manage preferences, analyze results.

### Reporting

Purpose: sales, donation, and reconciliation visibility. Typical information: sales by event/performance, revenue by channel, donations by campaign, accounting-date-based financial reports.

## Important Rules / Behaviors

- **One person, one record.** The system's value depends on purchases, gifts, and communications resolving to the same patron; duplicate handling and record merging are structural concerns.
- **The patron history is the asset.** Ticketing history is deliberately retained and reused for fundraising and marketing; the system is not a pass-through seller.
- **Contact preferences are enforced.** Patron communication choices (opt-ins/opt-outs) govern what marketing may be sent — a structural rule, not an afterthought.
- **Sales channels share one inventory and one record.** Box office and online sales draw on the same event configuration and write to the same patron database.
- **Exchanges and returns are normal operations**, not exceptions — subscription holders routinely swap performance dates.
- Exact numeric limits, fee structures, and tax handling (e.g., charitable-gift tax relief) vary by product and jurisdiction and are not standardized across the Type.

## Variants

- **Large-institution unified platform** — enterprise deployments spanning ticketing, fundraising, membership, education, retail, and admissions for major arts centers and orchestras
- **Mid-market cloud platform** — theatres and smaller companies on cloud products with strong website integration
- **CRM-platform-native** — ticketing built as a module on a general-purpose CRM substrate
- **Ticketing-first expansion** — products that began as ticketing and added fundraising/marketing as connected layers
- **Admissions-based institutions** — museums and attractions running the same patron model over admissions rather than performances
- **Campus model** — higher-education deployments combining performing arts, athletics, and events across departments

## Related Application Types

| Application Type | Distinction |
|---|---|
| Event Ticketing Platform | sells tickets to many organizers' events as a service/marketplace; no unified patron relationship owned by one organization |
| Nonprofit CRM / Donor Management System | donations and donor relationships primary; no admission selling |
| Theater Production Management | the production side — making and running shows (company, schedules, reports); here the unit of record is the patron relationship, not the production |
| Venue Management System | booking and operating the building and its spaces; an organization without its own venue still uses this Type |
| Event Management Platform | conference/event lifecycle and attendee management, not recurring performance seasons and donor cultivation |
| Membership Management System | membership schemes only; here membership is one layer over the unified patron record |
| Marketing Automation Platform | generic campaign tooling; here marketing is bound to the organization's own ticketing and giving data |

## Representative Products

- Tessitura
- Spektrix
- PatronManager
- AudienceView

## Sources

Research date: **2026-09-10**

- Tessitura — https://www.tessituranetwork.com/ (official product pages)
- Spektrix — https://support.spektrix.com/hc/en-us (official support centre)
- PatronManager — https://patronmanager.com/ (official product pages)
- AudienceView — https://www.audienceview.com/ (official product pages)

> Sourcing limitation: official operational manuals were not fetched for all products; workflow descriptions are calibrated to what official product and support pages directly show. Precise vendor-specific details (fee structures, limits, region-specific tax handling) are intentionally omitted and remain in the Research Notes.
