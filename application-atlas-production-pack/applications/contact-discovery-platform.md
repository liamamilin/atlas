# Contact Discovery Platform

## Overview

A **Contact Discovery Platform** is a sourcing application whose job is to produce contact records an organization does not yet have. The user states who to find — as a set of criteria or as a specific identity — and the platform's external data supply of business people (and commonly companies) yields matching records with verified reachability data: work emails, direct-dial phone numbers, titles, employers, locations. The records are then taken away into the user's own tools — a CRM, an ATS, a spreadsheet, an outreach campaign.

The defining core is small:

```text
External supply of business contact records the customer does not own
└── Sourcing act: criteria- or identity-driven yield of net-new records
    └── Record set with verified reachability data as the deliverable
        └── Taken away into the customer's own tools
```

Everything else commonly associated with these products — fifty-filter search consoles, credit systems, browser extensions, intent signals, AI assistants, compliance certifications — is standard mature machinery or a variant posture, not what makes the product a contact discovery platform.

The boundary is deliberate: a contact discovery platform does not complete records the customer already holds (that is data enrichment), does not run the outreach that follows (that is prospecting workflow and sales engagement), and does not deliver selling decisions about whom to pursue and when (that is sales intelligence). It ends where the sourced records change hands.

## Users & Context

The primary user is anyone whose work begins with "I need to reach people I don't yet know":

- **sellers and SDRs** building outbound target populations — the dominant use case
- **recruiters** sourcing candidates, often delivered into an ATS rather than a CRM
- **founders, marketers, and agency teams** building invitation lists, partner lists, or market maps

Usage is individual-centric with team seats: one person runs searches and takes records away, while organizations govern access, share lists, and meter usage. The work context is the start of the funnel — before any relationship, deal, or conversation exists. The platform is opened to answer "who is out there that matches this, and how do I reach them," not to work an existing book of contacts.

## Core Model

### The Defining Core

**1. An external supply of business contact records the customer does not own.**
The platform's defining asset is a maintained body of structured records about business people — name, title, employer, location, employment history — and, in most products, parallel company records with firmographics (industry, size, revenue, technology usage, funding). Crucially the supply carries **reachability data**: verified email addresses and direct-dial phone numbers. Without reachability data the product would be a market-mapping tool; without the supply it would be a filter UI over nothing. The supply exists in three documented forms: a proprietary database maintained by the vendor, an aggregation of many external data providers, and AI-directed research that compiles records on demand.

**2. The sourcing act as the primary job.**
The customer expresses who to find, and the platform produces matching records the customer did not previously hold. The expression takes several documented forms:

- **criteria-driven search** — attribute filters (role, seniority, geography, industry, company size, technology, funding) applied against the supply
- **identity-driven lookup** — a specific person sought by name and company, or by a profile URL
- **in-context capture** — a browser extension that reveals and saves a record while the user browses a professional network or company site
- **list import** — uploading identities (profile URLs, company URLs, emails) for the platform to resolve into records
- **expansion and AI-directed sourcing** — lookalike seeds from existing good records, or natural-language descriptions turned into searches

The direction matters: records flow *from the market to the customer*. This is the opposite loop from enrichment, which starts from records the customer holds and completes them.

**3. The yielded record set as the unit of value, delivered out.**
The deliverable is the records themselves — with contact details attached — exported, synced, or pushed into the customer's own tools: CSV downloads, CRM sync, ATS delivery, outreach-tool handoff, API responses. The platform does not run the outreach, own the resulting relationships, or rank what to do next. A sourced record set is transient by nature: once taken away, its life continues in the customer's systems.

### Standard Capabilities

Mature products commonly add the machinery that makes the three-part core practical:

- **Broad filter families** — role/title/function/seniority, geography down to postal code, industry with standard classification codes, company size and revenue, funding, technology usage, founding year
- **Verification machinery** — verification states or confidence grades on emails and phones; verification applied at reveal or at export; accuracy guarantees backed by credit refunds for bad data
- **Search-unmetered, yield-metered economics** — browsing and filtering are typically free; credits are consumed when contact data is revealed, looked up, or exported; several products explicitly do not charge when nothing valid is found
- **Dedup and exclusion** — excluding records already taken (previous downloads, CRM-synced contacts), uploaded exclusion lists, keyword excludes, suppression-list filtering
- **Saved searches** for reuse; alerts on new matches in the family's fuller implementations
- **Browser extension** for capture in context, including saving a record before any contact data is available
- **Lists as containers** for the yield — created at save time, used for bulk operations and downloads
- **Delivery machinery** — CSV, native CRM sync, ATS delivery, outreach-tool handoff, REST API (search, lookup, bulk), webhooks, and supply to AI agents
- **Previews before the metered reveal** — partial contact data or availability indicators in search results; ordering that surfaces decision-makers
- **Compliance posture** — regional exclusion toggles, opt-out and suppression support, certification programs, professional-use scoping
- **AI assistance** — natural-language search, AI verification, AI-agent supply

### One Structure, Many Implementations

The core model is conceptual. Common implementations vary per concept:

```text
Concept:            External supply
Implementations:    proprietary database, provider-network aggregation,
                    AI-researched compilation, hybrid

Concept:            Sourcing act
Implementations:    database search, identity lookup, extension capture,
                    URL/list import, lookalike expansion, AI-directed search

Concept:            Reachability data
Implementations:    verified work email, personal email, direct-dial mobile,
                    office phone — with confidence grades or verification states

Concept:            Delivery out
Implementations:    CSV download, CRM sync, ATS delivery, outreach-tool handoff,
                    REST API, webhooks, AI-agent supply
```

A reader who has only seen one implementation — say, a filter-based database search — should still recognize an extension-led capture tool or an API-first lookup service as the same Type.

## How It Works

### The sourcing loop

```text
State who to find
→ apply criteria (filters, facets) or a specific identity
→ review candidates (previews, availability indicators, decision-maker ordering)
→ reveal / verify contact data (credits consumed; verification applied)
→ take the records away (export, CRM/ATS sync, campaign import, API)
→ exclude what was taken, so the next search yields only net-new records
```

The loop is the product. Everything before the reveal is discovery; the reveal converts a candidate into a usable record; the delivery moves the record into the customer's world; the exclusion machinery keeps the next loop net-new.

### The identity-lookup loop

A narrower, equally defining flow: the user seeks one specific person (name + company, or a profile URL). The platform resolves the identity against its supply and returns verified contact data. In API-first products this is the primary surface — a search endpoint returns candidate matches without contact info, and a separate lookup endpoint retrieves the contact data for the chosen match.

### The capture loop

The user browses a professional network or company site; the extension surfaces available contact data for the person on screen; one action saves the record — with contact data, or without it (a record can exist before its reachability data is found) — into a list, a CRM, or a campaign.

### Core vs common vs optional

**Defining core** — without these, not a contact discovery platform:

- external supply of business contact records with reachability data
- criteria- or identity-driven sourcing yielding net-new records
- record-set delivery out of the platform

**Standard capabilities** — present in most mature products:

- filter families, verification machinery, credit metering on the yield, dedup/exclusion, saved searches, extension capture, lists as containers, API and bulk delivery, previews, compliance posture, AI assistance

**Common variants** — depend on audience, region, supply model, and packaging:

- supply model (owned database vs provider aggregation vs AI research)
- audience extension (recruiting with ATS delivery; healthcare-credential verticals)
- suite bundling (verification, warmup, campaigns, light CRM around the discovery core)
- regional compliance orientation; freemium vs enterprise tiering
- email-led vs phone-led reachability emphasis

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Search console

The primary entry surface.

- filter panels organized by record attribute (person, company, location, industry, technology), often with dynamic facet options that update as filters are applied
- results table with identity columns and contact-data availability indicators
- primary actions: refine criteria, save the search, select records, save to list, reveal contact data, export

### Record detail

The single-record surface.

- full identity profile: employment history, location, company context
- contact-data section with verification states or grades
- primary actions: reveal, verify, save, export, find similar

### Browser extension

The in-context surface over professional networks and websites.

- contact-data availability for the person on screen
- primary actions: reveal, save to list or CRM, add to campaign

### Lists and downloads

The take-away surface.

- sourced record sets with bulk operations, column selection, verification applied at download
- primary actions: download, sync to CRM/ATS, exclude from future searches

### API and developer surface

The programmatic surface, primary in API-first products.

- search endpoints (criteria → candidate matches without contact data), lookup endpoints (identity → contact data), bulk operations, webhooks, usage metering

## Important Rules / Behaviors

### The yield is metered; the search is not

Across the researched sample, browsing and filtering are typically unmetered while contact-data retrieval consumes credits — and several products explicitly do not charge when no valid contact data is found. The economic unit is the yielded record, not the query.

### Net-new is enforced, not just intended

Discovery products carry machinery that keeps results net-new: excluding previously downloaded records (in one sampled product by default), excluding CRM-synced contacts, uploaded exclusion lists, and suppression-list filtering. Without this, the same records would be re-sourced and re-charged.

### A record can exist before its contact data

Capture-without-data is a documented pattern: a record saved from a profile URL with no email attached, to be completed later. The record and its reachability data are separable layers.

### Verification gates delivery

Contact data is verified at reveal or at export, with states or grades exposed to the user; accuracy guarantees with credit refunds are the commercial expression of the same discipline. Reachability data decays as people change jobs, so refresh and reverification are structural concerns.

### Compliance shapes the supply

Regional exclusion toggles (excluding an entire economic area's records), suppression and opt-out support, and professional-use scoping are structural: they determine which records can be sourced and delivered at all, not just how the product is marketed.

### The platform ends at the handoff

Once records are delivered, the platform's job is done. It does not run the sequences, own the relationships, or decide what to do next — neighboring Types own those jobs.

## Variants

- **Search-first database** — the filter console over a large proprietary database is the product; accuracy guarantees and credit refunds as differentiators
- **Identity-lookup / API-first** — resolve specific people (and companies) on demand; programmatic access as the primary surface; supply to AI agents
- **Extension-led capture** — the browser overlay over professional networks is the primary sourcing surface, with a search portal alongside
- **Suite-embedded discovery** — discovery as the entry layer of an outreach suite (verification, warmup, campaigns, light CRM bundled around it)
- **Aggregation pole** — no owned database; sourcing runs across many external providers plus AI research
- **Recruiting-oriented** — candidates instead of buyers; ATS delivery; credential and license verticals (healthcare)
- **Compliance-led regional pole** — phone-verified regional data, do-not-call coverage, certification bundles as market differentiators
- **Freemium self-serve vs enterprise** — daily free credits and self-signup vs governed team deployments with admin machinery

## Related Application Types

| Application Type | Distinction |
|---|---|
| Sales Data Enrichment Platform | opposite loop direction: enrichment starts from records the customer already holds and completes them (match-and-append write-back); discovery starts from the market and yields net-new records. Same vendors commonly ship both as separate pillars |
| Sales Prospecting Platform | sourcing act vs surrounding workflow: prospecting adds the standing prospect list worked over time, qualification/prioritization, and handoff into the outbound motion as its purpose; discovery is the sourcing step itself, use-agnostic, and can exist with lists as transient containers. Every prospecting product ships discovery; discovery-primary products need not do prospecting |
| Sales Intelligence Platform | records vs decisions: intelligence delivers selling decisions over a managed target population (whom to pursue, when, with what context); discovery delivers the records themselves. Signals appear on both sides as filters — a documented overlap zone |
| Lead Generation Platform | seller-chosen targets from an external supply vs buyer-initiated demand captured through forms, ads, and content |
| CRM / Lead Management Platform | system of record for owned relationships and pipeline vs external sourcing of records that don't yet exist in the organization; list building inside a CRM over owned records is not discovery |
| Directory Application | per-lookup reference surface over standing entity records (find one business or person) vs organizational sourcing of record sets with export, verification, dedup, and team machinery; lookup-style products straddle this seam |
| Sales Engagement Platform / Outreach Sequencing | sourcing ends at the record handoff; engagement owns per-prospect outreach execution. Some products bundle both — packaging, not Type |
| ABM Platform | target-account selection overlaps, but ABM orchestrates marketing activation and measurement over named accounts; discovery equips individual users to source people and records |

The prospecting seam is the softest in this family — the two Types share the sourcing step, and vendors blur the naming in both directions. The directory keeps them apart by primary job: discovery names the act, prospecting names the workflow around it.

## Representative Products

- **UpLead** — search-first B2B database with accuracy-guarantee positioning
- **RocketReach** — identity-lookup pole, API-first, broad-market including recruiting and healthcare
- **Snov.io** — SMB freemium suite with discovery as its entry layer
- **ContactOut** — extension-led capture plus search portal, dual sales/recruiting audience

The core model was cross-checked against the wider sales-data family documented in sibling leaves (Apollo, Hunter, Lusha, Cognism, Clay) to avoid over-fitting to any single product philosophy.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces:

- UpLead — Help Center (contact search, exclusions, lead-management collection) — https://support.uplead.com/en/ ; product pages https://www.uplead.com/ , https://www.uplead.com/prospector/
- RocketReach — API documentation (people search, lookup, bulk, webhooks, MCP) — https://docs.rocketreach.co/ , https://rocketreach.co/api
- Snov.io — Knowledge Base (LinkedIn Search) — https://snov.io/knowledgebase/how-to-use-linkedin-search-to-find-emails/ ; product structure https://snov.io/
- ContactOut — product pages and FAQ — https://contactout.com/

Family context carried from the sibling leaves' research (same date): research notes for Sales Data Enrichment Platform, Sales Intelligence Platform, and Sales Prospecting Platform (Apollo, Hunter, Lusha, Cognism, Clay observations).

> Sourcing limitations: ZoomInfo's official domains were unreachable (403) in the sibling passes on the same date and were not retried here; the enterprise owned-database pole is therefore represented indirectly, with no product-specific claims. Cognism remains evidenced at positioning level only (help center unreachable in prior passes; not retried). One Snov.io product page timed out and was abandoned per research rules. Precise vendor numbers (database sizes, credit caps, accuracy percentages, refresh intervals) are recorded in the paired Research Notes and intentionally not stated as general facts in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
