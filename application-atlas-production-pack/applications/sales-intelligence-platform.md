# Sales Intelligence Platform

## Overview

A **Sales Intelligence Platform** maintains external intelligence about business companies and people, and delivers it to a selling organization as decision support: which companies and buyers merit attention, what has changed that makes now the time to reach out, and the context a seller needs to act. The seller's targets are held in the platform as a managed population — saved companies, saved people, organized lists, reusable buyer profiles — and the platform continuously converts its intelligence supply into signals, recommendations, and research surfaces focused on that population.

The problem it solves is market blindness. A CRM knows what a company has already done; it knows nothing about the companies it has not touched yet, and it goes stale about the ones it has. Sellers historically filled the gap with manual research — scanning news, funding announcements, job boards, and professional networks one company at a time. A sales intelligence platform industrializes that research: a vendor-maintained body of business intelligence, kept current, focused on the customer's target market, and pushed to sellers as timely, actionable context.

The defining core is deliberately small:

```text
External entity intelligence supply (vendor-maintained)
        ↓ focused on
Managed target population (saved companies & people, lists, buyer profiles, territories)
        ↓ converted by
Decision-delivery loop (who merits attention → what changed → what context)
        ↓ acted on through
Handoff into the revenue stack (CRM, engagement, outreach)
```

Everything else commonly associated with the category — contact databases, intent data, AI summaries, browser extensions, credit metering, CRM sync — is widespread in current products but is not what makes the product a sales intelligence platform. A vendor that only sells data feeds into other systems is a data provider, not this Type; a tool that only completes records the customer already holds is an enrichment platform, not this Type.

## Users & Context

Primary users:

- **Sellers (account executives, account managers)** — consume the platform as a standing research and prioritization surface: build and monitor their book of target accounts, act on alerts about their saved companies and contacts, and research an account before a conversation.
- **Sales development reps** — use targeting machinery to build prospect lists within their territory, work recommended leads, and hand records into outreach tools.
- **Sales managers and revenue leaders** — organize the target population across the team (territories, shared lists, buyer profiles), monitor coverage and usage, and rely on prioritization machinery to keep sellers working the right accounts.

Secondary users:

- **Revenue / GTM operations** — configure targeting criteria and data governance, manage integrations and permissions, monitor usage and data quality.
- **Marketing teams** — consume the same account intelligence for account-based campaigns; in several products the same target lists and signals serve both motions.

The work environment is the existing revenue stack: the CRM remains the system of record for relationships and deals, and the intelligence platform feeds it — through record creation, embedded profile surfaces inside CRM pages, and sync. Sellers typically move between the platform's web app, a browser extension over professional networks and company websites, and the CRM.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product stops being recognizable as a sales intelligence platform.

**1. The external entity intelligence supply.** The platform's foundation is a maintained store of structured intelligence about business entities — companies and the people at them — that the vendor, not the customer, compiles and keeps current. It typically spans several families:

- company attributes: industry, size, revenue range, locations, structure, web presence;
- people attributes: role, seniority, function, employment history, location, and (in database-led products) reachable contact data with verification states;
- technology and spend indicators: what a company uses and buys;
- event intelligence: funding, hiring activity, leadership additions, job changes, news, and research-intent indicators.

The supply is a lens over data the customer does not own. Without it, the product would be reporting on the customer's own records — CRM analytics, not market intelligence.

**2. The managed target population.** The customer's selling targets live in the platform as saved, organized, shareable objects: saved companies and saved people, lists that group them, saved searches that define them by criteria, reusable buyer profiles (function, seniority, geography) that describe whom to look for inside an account, and territory structures that partition the market across a team. This population is what focuses the general supply into *the customer's* market. Without it, the product degenerates into a lookup service or a data publisher.

**3. The decision-delivery loop.** The platform continuously converts supply plus population into seller-facing answers to three questions:

- **Who merits attention?** — qualification and recommendation machinery: suggested companies and people, fit scoring, ranked account lists; some products add lookalike discovery from existing customers.
- **What changed that makes now the time?** — a timing layer of dated change events on saved targets — job changes, hiring surges, funding, leadership additions, company news, research-intent spikes, website visits — delivered as alerts, digests, or feeds.
- **What context do I act with?** — account and people intelligence views: company profiles, decision-maker identification, organization and stakeholder maps, and (increasingly) AI-generated summaries and briefs; where the substrate supports it, relationship paths into the account through colleagues' connections.

The unit of consumption is the selling decision and the prepared conversation — not a completed record. Without this loop, the product is a data supply without an application: a data provider, not a platform.

### Standard Capabilities

Mature products commonly add, beyond the defining core:

- **Search and filtering** over the supply against ideal-customer criteria (industry, size, seniority, function, geography, technology, funding).
- **Saved searches and shared lists** with per-user or team-wide visibility, so targeting criteria become repeatable team assets.
- **Signal and alert delivery** with configurable cadence (immediate feed, daily/weekly digest).
- **Recommendation and scoring machinery** that ranks companies and people by fit and likelihood to engage, combining signals with configurable weights.
- **Account and people research pages** aggregating firmographics, contacts and decision-makers, organization structure, news, technology, and — where the substrate supports it — relationship paths.
- **Handoff into the revenue stack**: saving records into the CRM, exports, embedded profile surfaces inside CRM pages, and activity sync.
- **A browser extension** that surfaces intelligence over professional networks, company websites, and CRM records while the seller works there.
- **Contact-data access with verification states and usage metering** in database-led products; the graph-native pole substitutes platform messaging reach instead of contact export.
- **Team and governance machinery**: shared lists and searches with access levels, territory-scoped access, admin consoles, usage reporting.
- **AI assistance**: account and lead briefs, message drafting, research agents, and supply of the same intelligence to third-party AI tools.

A note on terminology: vendor vocabulary is not consistent. The word "signal" names a saved targeting-criteria set in one product, a dated change event in another, and a marketing umbrella for both in a third. Conceptually three distinct things are always present: **targeting criteria** (who fits), **change events** (what changed), and **delivered triggers** (what the seller is told, and when). This document uses those neutral terms.

## How It Works

The canonical loop runs from market definition to handoff, and then never stops:

### 1. Define the market

The organization translates its ideal customer profile into targeting criteria: filters over the intelligence supply (industry, size, geography, technology, seniority), reusable buyer profiles describing the people worth reaching inside an account, and territory structures partitioning the market across teams. Criteria are saved and shared so the whole team works from the same definition.

### 2. Build the target population

```text
Search the supply with saved criteria
→ review results (fit indicators, available data, recommendations)
→ save companies and people as targets
→ organize them into lists / assign to territories and owners
```

Recommendation machinery accelerates this step: suggested companies and people based on the customer's existing targets and customers, and ranked account lists by likelihood to buy; some products add lookalike discovery from the best current accounts.

### 3. Monitor for timing

Once targets are saved, the platform watches them. Change events — a contact changing jobs, an account accelerating hiring, a funding round, a new senior hire, rising research interest in a relevant topic, employees visiting the customer's website — are delivered as alerts on the homepage, in email digests, or inside the CRM. The timing layer is anchored to the target population: alerts fire on saved companies, saved people, and saved search criteria, not on the whole market.

### 4. Prioritize

Scores and rankings combine fit criteria and signals into a working order: which accounts to work first, which contacts within an account match the buyer profile, which alerts deserve action. Prioritization may be a simple ranked list or a configurable scoring model with weighted signals.

### 5. Research and prepare

Before outreach, the seller opens the account or person view: company profile, decision-makers and stakeholders, organization maps, recent news and signals, technology profile, and — in current products — an AI-generated brief. Where the substrate supports it, relationship machinery identifies warm paths in: colleagues who share a connection with the target.

### 6. Act and hand off

The decision becomes action in the systems where selling happens: save the person into the CRM, export a list, push records into an engagement tool for sequences, or reach out directly through platform messaging where the product offers it. Embedded surfaces bring the intelligence inside CRM records so the seller does not leave the system of record.

### 7. Keep it current

People change jobs, companies change shape. The supply is refreshed continuously, records carry currency indicators, and job-change tracking re-surfaces known contacts at new employers. The loop returns to step 3: a monitored target generates events indefinitely.

### What it does not do

The platform does not own relationships, deals, or customer conversations — the CRM and engagement tools do. It does not execute outreach programs (that is the engagement layer some suites bundle), and it does not, in its defining form, complete the customer's existing records — that is the enrichment job the same vendors usually also sell.

## Interfaces

### Search results (people / companies)

The targeting surface.

- filterable result lists over the intelligence supply, with fit and data-availability indicators per row
- primary actions: refine filters, save a search, save results as targets, export

### Saved lists / account hub

The managed-population surface.

- the customer's saved companies and people, grouped into lists, with owner and coverage visible
- primary actions: create and share lists, assign owners, review membership, monitor changes across the population

### Account (company) page

The research surface for one target company.

- firmographics, news and signals, contacts and decision-makers, organization and stakeholder maps, technology and spend indicators; where the substrate supports it, relationship paths into the account
- primary actions: save the account, identify and save contacts, log notes, act on alerts

### Lead (person) page

The research surface for one target person.

- role, seniority, employment history, shared connections, recent activity, contact data where offered
- primary actions: save as target, save to CRM, draft outreach, reveal contact data (in database-led products)

### Alerts feed / home

The timing surface.

- dated events on saved targets, grouped by type (account changes, people changes, engagement, recommendations); some products allow bookmarking or flagging of individual alerts
- primary actions: review, act on an alert (open the target, contact, save), adjust alert settings

### Browser extension

The in-context surface.

- intelligence about the company or person on screen, overlaid on professional networks, company websites, and CRM pages
- primary actions: view fit and signals, save or push the record, reveal contact data

### CRM-embedded surfaces

The delivery surface inside the system of record.

- profile intelligence and alerts rendered on CRM record pages; record creation and sync
- primary actions: view intelligence without leaving the CRM, create/update records

### Admin & usage

The governance surface.

- territory and access configuration, sharing rules, data and integration settings, usage and coverage reporting

## Important Rules / Behaviors

### The timing layer is anchored to saved targets

Alerts and change events fire on the managed population — saved companies, saved people, saved search criteria — not on the entire market. Building the population is therefore not optional bookkeeping; it is what activates the platform's monitoring.

### The platform is a lens, not the system of record

Relationships, deals, and activities live in the CRM. The intelligence platform feeds records into the CRM and embeds surfaces inside it; conflicts are resolved in favor of the CRM as the customer's record. Intelligence about the market is the platform's to maintain; knowledge about the customer's own pipeline is not.

### Intelligence decays; currency is part of the product

People change jobs and companies change shape, so the supply is maintained continuously and records carry currency indicators. Dated change events are the valuable form of intelligence — an alert is only useful while it is fresh, which is why delivery cadence and recency are first-class product properties.

### Contact data is metered and carries quality states

In database-led products, revealing contact data consumes usage allowances, and returned data carries verification states (verified/unverified email, phone verification). Teams therefore target high-value segments rather than revealing indiscriminately. Graph-native products substitute platform messaging reach for contact export, with its own metering.

### External data, external responsibilities

The intelligence describes real, identifiable business people and companies. Compliance posture — lawful sourcing, deletion-request handling, do-not-call coverage in calling-oriented markets — is a first-class purchasing criterion, and the customer is responsible for lawful use of the data in outreach.

### Targeting is a governed team asset

Saved searches, lists, and buyer profiles are shared with explicit access levels; territories partition the market and can scope which sellers may work which prospects; admins monitor usage and coverage. The target population is an organizational structure, not a personal scratchpad.

## Variants

- **Compiled-database pole** — the vendor compiles and verifies its own contact and company database; contact reveal and credits are central; discovery and enrichment are bundled siblings of the intelligence loop.
- **Graph-native pole** — intelligence is derived from a professional network's own member, connection, and content graph; relationship paths and platform messaging replace contact export as the way in.
- **Provider-network and co-op poles** — the supply is aggregated from third-party providers or a data co-op (notably intent data), with the platform as the lens and delivery surface.
- **Contact-data depth** — full contact export with metering vs no-export relationship intelligence; the seam changes the product's economics and its compliance posture.
- **Suite drift** — intelligence-only products vs suites that bundle engagement (sequences, dialer, deals) or ship enrichment as a separate pillar; the intelligence loop remains the center in all of them.
- **Regional compliance orientation** — European-market products lead with phone-verified data, do-not-call coverage, and audited certifications; the compliance posture is the differentiator rather than a feature.
- **Segment tiers** — self-serve SMB (extension-led, free tiers) through enterprise (governance, data-as-a-service delivery, procurement-level compliance review).
- **AI posture** — AI as an assistive layer (briefs, drafts) through AI-native repositioning, plus supply of the same intelligence to third-party AI assistants.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Sales Data Enrichment Platform | same family, opposite direction | enrichment starts from records the customer already holds and completes them (match-and-append into CRM); sales intelligence starts from the market and equips selling decisions over a managed target population; the same vendors usually sell both |
| Contact Discovery Platform | same family, narrower job | discovery sources net-new records the customer does not hold (search → produce records for outreach lists); intelligence maintains standing decision support over the target population; discovery-style search is one capability inside intelligence products |
| Sales Prospecting Platform | downstream workflow | prospecting is the outreach-preparation workflow (build lists → find contacts → hand to engagement); intelligence is the layer that decides which accounts, when, and with what context |
| ABM Platform | bundled sibling, different owner | ABM orchestrates marketing activation and account-level measurement over a target account list; sales intelligence serves sellers with data, signals, and context; suites bundle both |
| Competitive Intelligence Platform | different entity focus | CI tracks competitors and the market for strategy and deal defense; sales intelligence tracks prospect targets for selling decisions; they meet at account triggers |
| Lead Generation Platform | adjacent upstream | lead generation captures net-new demand (forms, ads, campaigns); intelligence equips decisions about the existing market; website-visitor identification sits at the seam, delivered as a targeting signal |
| Customer Relationship Management / CRM | downstream host | CRM owns relationships, deals, and the record; intelligence feeds CRM records and embeds surfaces inside it; CRM remains the system of record |
| Revenue Intelligence Platform | inward mirror vs outward lens | revenue intelligence mirrors the organization's own in-flight deals (CRM sync + captured engagement + pipeline health); sales intelligence looks outward at the market |
| Conversation Intelligence Platform | different data direction | conversation intelligence analyzes the seller's own customer conversations; sales intelligence supplies intelligence about external prospects |
| B2B Data Providers / DaaS | supply without application | a data supply delivered into other systems, with no managed target population and no seller-facing decision loop, is a data provider, not this Type |

The family seam is with enrichment, discovery, and prospecting: all four jobs share one external data substrate, vendors bundle all of them, and vendor naming ("sales intelligence") is applied loosely across the family. What keeps them distinct Types is the primary job — completed records vs sourced records vs outreach workflow vs selling decisions — and the boundary table above states each seam explicitly.

## Representative Products

- **LinkedIn Sales Navigator** — graph-native pole: intelligence over the professional network's member, connection, and content graph; saved accounts/leads with a rich alert taxonomy, relationship mapping, and platform messaging instead of contact export.
- **Apollo.io** — database-led mid-market suite: compiled contact database with search, saved searches and alerts, ICP-scoped signals and scores, plus bundled engagement and enrichment.
- **Lusha** — asset-light data-and-intelligence layer: verified contact/company data with a documented real-time signal set, plus AI recommendations, lookalikes, and ICP ranking (SMB/mid-market, extension-led).
- **Cognism** — European, compliance-first premium vendor whose flagship product line is literally named "Sales Intelligence": target lists and personas assigned to teams, buying signals, phone-verified mobiles, and CRM/engagement handoff.

The enterprise owned-database leader (ZoomInfo) could not be directly examined this pass — its official domains were unreachable from the research environment — so no claims about it are made here; it is nonetheless a central market reference for the Type.

## Sources

Research date: **2026-09-07**

- LinkedIn Sales Navigator Help — Glossary; Save lead and account searches; Sales Navigator alerts — https://www.linkedin.com/help/sales-navigator/answer/a122541 , https://www.linkedin.com/help/sales-navigator/answer/a102024 , https://www.linkedin.com/help/sales-navigator/answer/a105133
- LinkedIn Sales Navigator — product page — https://business.linkedin.com/sell/sales-navigator
- Apollo — Developer docs (index, Capabilities, Find People Using Filters) — https://docs.apollo.io/ , https://docs.apollo.io/docs/capabilities.md , https://docs.apollo.io/docs/find-people-using-filters.md
- Apollo — Knowledge base (Save, Share, and Set Alerts for Searches; Create and Use a Signal; category structure) — https://knowledge.apollo.io/hc/en-us/articles/4409803718669 , https://knowledge.apollo.io/hc/en-us/articles/13152837789837 , https://knowledge.apollo.io/hc/en-us
- Lusha — Knowledge Hub (Search Layer; Deep Intelligence) — https://docs.lusha.com/search-layer , https://docs.lusha.com/deep-intelligence
- Cognism — Sales Intelligence product page — https://www.cognism.com/sales-intelligence
- Bombora — product site (boundary reference: self-described data company, not a platform) — https://bombora.com/

> Sourcing limitations: ZoomInfo's official domains were unreachable from the research environment (403), consistent with the prior sales-data-enrichment pass, so the enterprise owned-database pole is represented indirectly and no claims are made about it. Cognism is evidenced at product-page level only (its help center was unreachable in the prior pass and was not retried). Two Apollo knowledge-base articles on buying intent returned 403 on direct fetch; that capability is evidenced via the knowledge-base structure and cross-references, and its specifics are not asserted. Precise vendor numbers (filter counts, list-size caps, alert retention, database scale claims, refresh intervals) observed in vendor documentation were deliberately kept out of this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the family-boundary analysis (including the joint-review resolution with the sales-data-enrichment pass) are recorded in the paired Research Notes.
