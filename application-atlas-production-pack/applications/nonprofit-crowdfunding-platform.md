# Nonprofit Crowdfunding Platform

## Overview

A **Nonprofit Crowdfunding Platform** is a fundraising application through which an organization raises money for a specific cause or project by running it as a **public campaign**: a persistent, identified fundraising container with its own public page, to which many individuals contribute money as gifts, and whose running result is publicly visible so that momentum attracts further donors.

It solves a problem the standing "Donate" button cannot: turning one specific need — a building project, disaster relief, new equipment, a program launch — into a self-reinforcing public effort, where each gift makes the next one more likely.

The defining core is deliberately small:

```text
Campaign (public fundraising container of record)
└── Crowd contributions bound to the campaign
    (per-donor capture, gift semantics, funds paid out to the organization)
    └── Public progress and share-out
        (visible running result + built-to-be-spread machinery)
```

Everything else the market associates with it — goal thermometers, deadlines, matching gifts, perks, supporter pages, giving days, donor databases, receipting — is standard or optional machinery wrapped around that core, not what makes the product this Type. If the campaign container, the crowd-facing money capture, or the public progress dynamic is removed, the product stops being a crowdfunding platform: it becomes a donation form, a payment page, or an awareness post respectively.

## Users & Context

**Organization side (the operators):**

- **fundraiser / development staff** — create the campaign page, write the story, configure the goal and duration, run the promotion, and steward donors during and after the campaign. In small organizations this is often one person wearing all hats.
- **organization leadership / finance** — connect the payment account that receives the funds, reconcile payouts, and pull reports on what was raised.
- **communications / marketing** — share the campaign out through email, social channels, and the organization's website embeds.

**Crowd side (the public):**

- **donors** — visit the campaign page, read the story, give once or recurring, optionally display their name and a message, and receive a receipt where the regime provides one.
- **sharing supporters** — spread the campaign link through their own networks; in many products they can go further and run their own small fundraiser pages on the campaign's behalf.

Typical context: small and mid-sized nonprofits without dedicated infrastructure run campaigns on free or low-cost platforms; larger organizations run crowdfunding as one campaign type inside a broader fundraising suite. Campaigns are commonly tied to a concrete project, an urgent need, or a calendar moment (year-end, giving days).

## Core Model

### The Defining Core

**1. The campaign — the public fundraising container of record.**
A campaign is a persistent, named fundraising effort for a specific cause or project. It carries a public page that tells the story — text, photos, video — and solicits contributions. It is run by an organization for its mission (or, in some products, by a campaigner who routes the funds to an eligible registered organization). The campaign is the unit to which everything else attaches: donations, progress, updates, and donor recognition all belong to *this* campaign. Without the campaign container, the product is just a donate form.

**2. Crowd contributions bound to the campaign.**
Individuals give money to the specific campaign through the platform's checkout. Each contribution is recorded against the campaign — amount, donor, recognition preference — and the money is paid out to the organization's own account. The contributions are **gifts to a cause**, not purchases or investments: perks or tokens of appreciation may be offered, but the transaction is a donation. Without the money capture, the product is an awareness page; without the org-destination, it drifts into personal crowdfunding.

**3. Public progress and share-out.**
The campaign's running result — the total raised, and in most products a goal target and supporter counts — is visible to prospective donors on the public page, alongside evidence that others have given (donation counts, recent-donor lists). The campaign is built to be spread: share links, embeddable forms, promotion tools, and updates keep it moving outward through networks. Mature products treat this as the point of the whole exercise: people give more readily when they can see that others already have. Remove the public progress machinery and the crowd dynamic — the thing that makes this *crowd*funding — disappears.

These three are held jointly. A campaign page without money capture is a petition. A checkout without a public container is a payment form. A public total without a campaign behind it is a tip jar. The combination — public cause container + crowd money capture + visible momentum — is what the market recognizes as nonprofit crowdfunding.

### Standard Capabilities of Mature Products

These are near-universal in current products. They make the core practical, but a product would still be this Type without any single one of them.

- **Donation checkout** — preset and custom amounts, one-time and recurring gifts, multiple payment methods, an option for donors to cover processing fees, an optional donor message.
- **Storytelling editor** — drag-and-drop campaign pages with story sections, photos, video, and impact metrics ("what a gift achieves, not just what it costs"); organization branding and custom domains; embeddable forms for the organization's own website.
- **Progress implementations** — goal thermometer, countdown timer, donation counter, recent-donor feed. These are the concrete widgets that realize defining core #3.
- **Donor recognition display** — donors appear on the page by name and message, or anonymously, at their choice.
- **Charitable receipting** — receipts for eligible registered organizations; rules vary by country and are only as broad as the platform's jurisdictions.
- **Campaign updates and supporter messaging** — progress posts and bulk email keep donors and sharers engaged during the campaign.
- **Offline gift entry** — checks and cash received outside the platform are logged into the same public total.
- **Matched giving** — a matching arrangement that multiplies or unlocks gifts, counted into the visible progress.
- **Reports and exports** — raised-to-date, donation lists, campaign performance.
- **Payouts** — funds flow through connected payment-provider accounts to the organization's bank.
- **Campaign operations** — duplication of past campaigns, pre-launch preparation, duration extension.
- **Post-campaign donor retention** — donors land in the organization's own records (built-in or integrated), so one campaign feeds the next. A widely articulated philosophy in this market: the campaign ends; the donor relationships stay with the organization.

### One Structure, Many Implementations

```text
Concept:   Public campaign progress
Implementations:  goal thermometer, running total, donation counter,
                  countdown timer, recent-donor feed, leaderboard (giving days)

Concept:   Contribution capture
Implementations:  hosted checkout page, embedded website form,
                  text-to-give entry, manual offline-gift entry

Concept:   Organization beneficiary
Implementations:  registered charity with its own payment account,
                  platform-collected payouts, fiscal sponsorship routing
                  to a registered organization

Concept:   Share-out surface
Implementations:  social share links, embeddable widgets, QR codes,
                  email campaigns, supporter-run fundraiser pages
```

A reader who has only seen one implementation (say, a thermometer-widget campaign page) should be able to recognize the others — including older, non-thermometer, open-ended campaigns — as the same Type.

## How It Works

### Create and connect

```text
Create the campaign
→ name it, set an optional goal target and duration
→ build the public page: story, photos, video, impact metrics
→ connect the organization's payment account for payouts
→ optional: perks/impact levels, matching arrangement, fund designations,
   supporter fundraiser pages
```

### Prepare and launch

```text
Pre-launch preparation
→ brief team members and (optionally) supporter fundraisers
→ prepare launch communications
→ launch: the page goes public
→ share the link out: social channels, email, website embed, QR
```

### The crowd loop

```text
A visitor arrives (shared link, social post, org website)
→ reads the story
→ sees the momentum: total raised, goal, recent donors, countdown
→ gives through checkout (amount, frequency, cover-fees choice,
   recognition choice)
→ receipt issued where the regime provides one
→ the gift is recorded against the campaign and the public total moves
```

This loop is the engine. Every recorded gift updates the visible progress, and the visible progress is what persuades the next visitor — which is why the progress machinery is part of the defining core rather than a nicety.

### Sustain

```text
Post updates and message supporters
→ add offline gifts to the total
→ extend the deadline if the campaign needs more runway
→ watch reports; promote through tracked channels
```

### Close and steward

```text
Campaign ends (deadline passes, or the campaign runs open-ended)
→ funds have been paying out to the organization's account throughout
→ donors remain in the organization's records
→ thank-yous, project updates, and the next campaign's invitation
  draw on the same list
→ the campaign page is closed or archived (removed from public view)
```

## Interfaces

The product has a built-in duality: a **public face** for the crowd and a **working surface** for the organization.

### Public campaign page

The face of the campaign.

- story sections with media, impact metrics, branding
- progress display (total, goal, counts, recent supporters)
- primary actions: give, share, (in some products) start a supporter fundraiser

### Donation checkout

The giving surface, hosted on the platform or embedded on the organization's site.

- amount selection (presets/custom), frequency (one-time/recurring)
- donor contact details, recognition display choice
- cover-the-fees toggle, payment method selection
- optional: gift designation to a specific fund, perk selection

### Campaign builder

The organization's editing surface.

- page editor (sections, media, branding)
- settings: goal, duration, matching, designations, perks, supporter pages
- team-member and fundraiser-page management

### Dashboard and reports

The organization's operating view.

- raised-to-date, donation counts, donor lists, exportable reports
- updates composer and supporter messaging
- promotion tracking

### Money and settings

- payout/payment-account connection
- receipting configuration
- fee-model visibility for the organization

## Important Rules / Behaviors

### Flexible funding is the dominant regime

In the researched sample, the organization keeps everything raised regardless of whether the goal is met — the pattern one platform names "keep what you get." An unmet goal does not forfeit the funds. All-or-nothing funding, where money is returned if the goal fails, is characteristic of consumer/rewards crowdfunding and was absent from the nonprofit sample. Goals are motivating devices, not payment conditions.

### Goals and deadlines are configuration, not requirements

Products commonly encourage a goal and a deadline — visible targets raise more — but campaigns can run open-ended, and durations can often be extended. The campaign container persists; the target is one of its settings.

### Money flows to the organization's own account

Payouts go to the organization (or the fiscally-sponsored registered organization) via connected payment-provider accounts. The platform's economics sit on top as platform fees, processing costs, or subscription/tip models — the fee structure varies widely, but the destination of the funds does not.

### Receipting is jurisdiction-dependent

Charitable receipts are issued only within the tax regimes the platform supports and only for eligible registered organizations. Campaigners without eligible status can in some products route donations through a registered organization (fiscal sponsorship). Receipt rules differ by country; nothing in the core requires receipting at all.

### Donor recognition is donor-controlled

Whether a donor's name and message appear publicly is the donor's choice, with anonymity structurally supported. The recent-donor feed that powers the crowd dynamic is built from consenting display, not from exposing all donors.

### The public total is reconcilable, not just automatic

Offline gifts (checks, cash, event collections) can be entered manually so the public total reflects everything raised. This makes the visible number an organization-maintained record, not merely a payment-processor echo.

### Campaign lifecycle

```text
draft / pre-launch → live → (extended) → ended → archived
```

Archiving removes the campaign from public view; the donor records and reports survive it. The campaign ends; the donor relationships remain with the organization.

### Eligibility gates the crowd

Platforms enforce acceptable-use and country/region rules on who may run campaigns, and (where receipts are involved) eligibility of the receiving organization.

## Variants

- **Crowdfunding-native platforms** — the campaign is the whole product, typically for small-to-mid nonprofits and grassroots causes, often with free or near-free economics funded by tips, processing spread, or optional paid tiers.
- **Crowdfunding inside a fundraising suite** — crowdfunding is one campaign type among donation forms, events, auctions, and peer-to-peer; in some suites it is documented inside the peer-to-peer product rather than as a top-level module.
- **Free/subscribed suites with donor CRM attached** — the campaign ships together with donor management and email marketing, on the theory that each campaign should end with a stronger donor base.
- **Giving days / GivingTuesday events** — many organization campaigns run under one branded event umbrella with leaderboards and community-wide totals; a community foundation or university typically operates the event.
- **Campaigns with perks or impact levels** — optional recognition tiers at given amounts ("what your gift achieves"), borrowed from rewards crowdfunding in spirit but not transactional.
- **Campaigns with supporter fundraiser pages** — the peer-to-peer overlay, where individuals and teams raise toward the campaign's total.
- **Open-ended vs deadline campaigns; fiscally-sponsored campaigns; regional receipting regimes** (e.g., jurisdiction-specific tax-deduction schemes) — configuration and regional variants of the same core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Online Donation Platform | closest sibling Type | a standing, evergreen give-capability centered on the donation transaction; here the campaign container with public crowd progress is the center. Most crowdfunding platforms also ship standing donation forms — suite overlap, not the same Type |
| Peer-to-peer Fundraising Platform | sibling Type | supporters run their own fundraising pages and solicit their networks; here the organization runs the campaign and donors give to it. Supporter pages appear here only as an optional overlay rolling up to the org's campaign |
| Fundraising Management Platform | broader sibling | org-side machinery for the whole fundraising program (planning, appeals, pipeline, performance); here the center is the donor-facing public campaign capture flow |
| Donor Management System | adjacent sibling | org-side constituency system of record; this Type feeds it after the campaign but does not center on it |
| Nonprofit CRM | broader record system | relationship spine across donors, members, volunteers; donation/campaign machinery is one slice |
| Nonprofit Event Management | adjacent | event logistics and ticketing are the center there; cause-giving machinery is the center here, even when a run/walk event hosts the campaign |
| Personal / rewards crowdfunding (consumer platforms, outside the nonprofit family) | different Type | beneficiary is an individual or a product promise; money goes to the page owner's bank account or against rewards; here the beneficiary is an organization-for-cause, money flows to the organization, and gifts are donations (optionally receipted) |

The first three boundaries are the load-bearing ones, and they grid on two questions: **who runs the fundraiser** (the organization, or its supporters), and **what is the record center** (the transaction, the campaign, or the whole program). This Type is: organization-run, campaign-centered, crowd-facing.

## Representative Products

- **CauseVox** — connected nonprofit fundraising platform with crowdfunding as a named use case; org-donor-ownership philosophy
- **Chuffed** — crowdfunding-native platform for nonprofits, charities, social enterprises and grassroots causes; zero-platform-fee economics; global coverage
- **Mightycause** — free nonprofit fundraising platform built around campaigns, donor management, and giving-day events
- **Qgiv (now Bloomerang Fundraising)** — mid-market fundraising suite where crowdfunding-class campaign machinery lives inside peer-to-peer fundraising

The consumer/personal line (e.g., GoFundMe-class personal crowdfunding, JustGiving's personal-cause crowdfunding product) was examined to hold the beneficiary boundary: personal-cause crowdfunding routes money to the page owner's own bank account and is a different Type, even when hosted by a charity-rooted platform.

## Sources

Research date: **2026-09-08**

- CauseVox — Nonprofit Crowdfunding: https://www.causevox.com/nonprofit-crowdfunding/ ; platform overview: https://www.causevox.com/
- Chuffed — Support documentation: https://docs.chuffed.org/ (categories: Basics of Crowdfunding; Eligibility; Campaign Basics; Managing your campaign; Perks and Impact Levels; Payments & Fees; Receipts, Tax Deductibility and Gift Aid); homepage: https://www.chuffed.org/
- Mightycause — homepage: https://www.mightycause.com/ ; pricing: https://www.mightycause.com/pricing
- Qgiv / Bloomerang Fundraising — platform overview: https://www.qgiv.com/ ; Peer-to-Peer Fundraising: https://www.qgiv.com/peer-to-peer-fundraising/
- JustGiving (boundary reference) — Crowdfunding (personal causes): https://www.justgiving.com/for-crowdfunding ; help center index: https://help.justgiving.com/

> Sourcing limitation: several prominent vendor help centers could not be fetched from the research environment on 2026-09-08 (including the enterprise-suite pole rebranded under the GoFundMe family, and two free-platform vendors). Assertions are therefore calibrated to the four reachable products and to product-page-level documentation for one of them; precise numeric details (fee percentages, payout cycle lengths, duration caps) observed for single products are intentionally not stated as Type-wide facts in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
