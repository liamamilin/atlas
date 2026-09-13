# Peer-to-peer Fundraising Platform

## Overview

A **Peer-to-peer Fundraising Platform** enables a nonprofit organization to mobilize its supporters as fundraisers: supporters create and own their own fundraising pages inside a context the organization provides — a campaign, an event, or a year-round invitation — solicit their personal networks through those pages, and every gift made through a supporter's page is credited to that supporter while the money settles to the organization.

The defining structure is small:

```text
Organization's fundraising context (campaign / event / standing invitation)
└── Supporter-held fundraising page (own story, own goal, org's branding)
    └── Donor gives through the page
        └── Gift credited to the fundraiser (and team), rolled up to the totals
            └── Money settles to the organization — never to the supporter
```

Everything commonly associated with modern peer-to-peer fundraising — team hierarchies, leaderboards, thermometers, badges, coaching email journeys, registration flows, fitness tracking — is widespread in current products but is not what makes the product a peer-to-peer fundraising platform. The walk-a-thon pledge sheet, where a supporter collects pledges from friends and turns the money in to the charity, already contains the whole defining structure.

When the organization itself runs the fundraising page and asks its own donors, the product is a different Application Type (Nonprofit Crowdfunding Platform or Online Donation Platform). When the supporter keeps the money, it is personal crowdfunding, not this.

## Users & Context

Three distinct user populations, with the supporter — not the organization — at the center of the fundraising work:

**Supporters / fundraisers** (the defining user): individuals who volunteer to raise money on the organization's behalf. They create a page, tell their own story in their own words, set a personal goal, share the page with family, friends, and colleagues, post updates, and thank the donors their page brought in. Many are people who might not give much themselves but have the time, passion, and reach to ask others.

**Team members and captains**: supporters organized into groups — a class, an office, a chapter, a company. Captains rally the group and often manage the team's pages without needing the organization's login.

**Organization staff** (development/fundraising team): set up the campaign, event, or invitation that supporter pages attach to; prepare branded page templates; recruit and coach fundraisers; review pages where review is enabled; monitor roll-ups and run reports.

**Donors**: give through a supporter's page. They are usually reached by the supporter's personal ask, not by the organization's own marketing — which is precisely the acquisition value of the Type: new donors arrive through personal relationships.

Typical contexts: walks, runs, and rides; giving and awareness days; do-it-yourself fundraising (birthdays, memorials, personal challenges); tribute and memorial pages; ambassador programs; virtual activity challenges.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product stops being a peer-to-peer fundraising platform:

- **The supporter-held fundraising page.** A persistent, individually identified page created and owned by a supporter — an individual or a team — carrying the supporter's own story, goal, photos, and updates. The page is built from a template the organization prepared, so it inherits the organization's branding and donation experience while the supporter supplies the words and the personal material. Without supporter ownership, the page is an organization-run campaign page (crowdfunding territory); without the organization's context and branding, it is a personal crowdfunding page.

- **The attribution-and-roll-up gift flow.** Donors give through a supporter's page. Each gift is recorded against that page — crediting the fundraiser, and the team, who brought the donor in — and rolls up in real time into the team, campaign, and organization totals. The money always settles to the organization's account; the supporter never holds or touches the funds. The attribution record ("who introduced whom") is what lets the organization thank both the donor and the fundraiser and steward the new relationship. Without attribution, the page is just a donation form with a name on it; without settlement to the organization, it is personal crowdfunding.

- **The delegated solicitation role.** The ask is made by the supporter to their own personal network. The platform hands the solicitation job to the supporter and equips it: a personal page link, one-tap sharing across email, SMS, and social channels with the supporter's own message, visibility of the page's donors, and thank-you and update tools. Without this, the organization is simply soliciting its own donors — the dynamic that distinguishes the sibling Types.

### What Mature Products Add

The following are standard capabilities of the current market — they make the model practical at scale but do not define it:

- **Team layer**: team pages with shared goals, captains who manage member pages, recruitment goals, and organization/company pages that gather all of a partner's teams and fundraisers under one banner.
- **Campaign or event home page**: the hub every page rolls up to — total raised, fundraiser and team leaderboards, and campaign momentum in one place.
- **Progress and momentum machinery**: fundraising thermometers and progress bars, donation counters, donor walls, countdown timers, impact metrics, and activity metrics (miles walked, hours logged).
- **Gamification**: milestone badges, leaderboards, contests, and matching gifts reflected automatically in the progress displays.
- **Supporter coaching**: onboarding email journeys, portal checklists ("set up your page, add a photo, make your first gift, share with five friends"), tips and templates, and segmented outreach to fundraisers — for example, nudging fundraisers who have not raised anything recently.
- **Org-side console**: campaign/event setup, page templates with automatic branding inheritance, participant management (search and filter by team, status, progress, sharing activity), custom fields, and reporting and exports by fundraiser, team, and campaign.
- **Registration configuration** for event-based campaigns: registration types, fees, discount codes, fundraising minimums, and guided paths from registration to page creation.
- **Donation-checkout machinery** shared with the donation-platform family: multiple payment methods, one-time and recurring gifts, donor-covered fees, offline gift entry counted in the totals, automatic receipts.
- **CRM soft credits**: the donor record and the fundraiser attribution flowing into the organization's donor system, so follow-up audiences can be built from real fundraiser and donor behavior.

### One Structure, Many Implementations

The core model is written in conceptual terms; products realize each concept differently:

```text
Concept:   Organization's fundraising context
Realizations:  timed campaign, walk/run/ride event with registration,
               giving day, year-round "start a fundraiser" invitation,
               tribute/memorial program, ambassador program

Concept:   Supporter-held page
Realizations:  individual page, team page with captain, organization/partner page

Concept:   Attribution
Realizations:  leaderboard ranking, per-fundraiser totals and exports,
               soft credits on donor records in the CRM
```

A reader who has only seen one implementation — say, a charity 5K where runners create pages — should still be able to recognize a year-round DIY program or a memorial-page program as the same Type from the core model.

## How It Works

### The organization opens the fundraising context

Staff configure the container supporter pages will attach to: a campaign or event with dates and goals, or a standing invitation that lives on the organization's site year-round. They prepare branded page templates with default copy, set donation amounts and receipt behavior, and decide how open participation is — an open "Start a Fundraiser" button, an invitation link shared with specific people, or registration through an event.

### Supporters create their pages

```text
Supporter signs up (or registers for the event / accepts the invitation)
→ creates a page in minutes from the org's template
→ sets a personal goal, tells their own story, adds photos or video
→ page goes live (immediately, or after org review where review is enabled)
```

The supporter brings the words and the photos; the design, donation experience, and money plumbing are the organization's.

### Supporters solicit their networks

```text
Share the personal link (email / SMS / social, pre-filled with the supporter's message)
→ donors visit the page and give
→ the supporter sees who gave, sends personal thank-yous
→ posts updates to keep the page alive
```

This loop — supporter asks, supporter stewards — is the engine of the Type. The organization's role during the campaign is to recruit fundraisers, coach them, and keep momentum visible.

### Gifts flow, credit, and roll up

When a donor gives on a fundraiser's page, one action updates everything: the gift credits the fundraiser and the team, the personal, team, and campaign totals all move together, the donor record is created or updated with the fundraiser attribution, a receipt is issued, and the money is settled toward the organization. Offline gifts a fundraiser collects in person are logged into the same totals.

### The organization monitors and reports

Staff watch roll-ups in real time, segment fundraisers for coaching, approve pages where review is on, and export fundraiser, team, and donation data for finance and board reporting. After the campaign, the donors the supporters brought in remain in the organization's records — the acquisition, not just the money, is the durable output.

### Core vs standard vs optional

**Defining core** — without these, not this Type:

- supporter-held fundraising page inside the organization's context
- gifts through the page credited to the supporter and rolled up to the organization
- money settling to the organization, never the supporter
- the supporter as the equipped solicitor of their own network

**Standard capabilities** — present in most mature products:

- team layer with captains; campaign/event home page as the roll-up hub
- thermometers, leaderboards, badges, donor walls, countdowns
- sharing tools with personalized previews; supporter donor lists and thank-yous
- coaching journeys and checklists; org-side participant management and reports
- registration flows for event campaigns; offline gifts; receipts; donor-covered fees
- CRM soft credits and exports

**Optional / variant** — depends on the program shape:

- page review/approval before going live
- donation cart (give to several fundraisers in one checkout)
- fitness/activity tracking integrations
- sync with social-platform fundraisers
- year-round DIY mode with no campaign container at all

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Campaign / event home page

The public hub of the fundraising context.

- total raised, goal progress, fundraiser and team leaderboards, recent-activity displays
- primary actions: donate to the campaign, browse fundraisers and teams, start a fundraiser

### Supporter fundraising page (public)

The unit of the whole Type — what the donor actually visits.

- the supporter's story, photo/video, personal goal, progress bar, donor wall, updates
- primary actions: give to this supporter's page, share the page

### Fundraiser dashboard (supporter-side)

The supporter's personal workspace.

- page progress, donor list, personal link and share tools, update posting, thank-you shortcuts
- primary actions: edit page, share, thank donors, post an update

### Organization console (staff-side)

The operating surface for the fundraising context.

- campaign/event setup, template and branding configuration, participant lists with search/filter, page review queues, coaching segments, reports and exports
- primary actions: launch context, recruit and message fundraisers, review pages, monitor roll-ups, export data

### Donation checkout

Shared with the donation-platform family: amounts, payment methods, recurring options, donor-covered fees, receipt issuance — reached from any supporter page or the campaign hub.

## Important Rules / Behaviors

### Money always goes to the organization

No matter which page a donor gives through, the funds settle to the organization's account. The supporter is a solicitor and a credit recipient, never a money holder. This is the structural line against personal crowdfunding.

### Every gift carries its fundraiser

Gifts made through a supporter's page are attributed to that supporter (and team) — visible in leaderboards and totals, and commonly written to the donor record as a soft credit. The organization can therefore answer "who introduced whom" — and thank both.

### Totals move together

Personal, team, and campaign totals are computed from the same gift records and update together in real time; there is no reconciliation layer between the supporter's page total and the organization's total.

### Branding is inherited, content is personal

Supporter pages are created from organization-prepared templates: the supporter supplies story, photos, and goal; the design, donation experience, and money handling stay the organization's. Some products let the organization review pages before they go public; others leave them self-serve.

### The supporter's reach drives acquisition

Donors reached through supporter pages are typically new to the organization — reached through personal relationships rather than the org's own channels. This is why the Type is marketed as network expansion, and why the donor record with its fundraiser attribution is treated as the durable asset.

### Offline participation counts

Gifts collected in person by fundraisers (cash, checks) are logged into the same totals and roll-ups, so the public picture reflects everything raised.

## Variants

The Type is realized across several program shapes; the core model holds across all of them:

- **Event-based (walks, runs, rides)** — registration creates the fundraiser; the event is the participation vehicle; fundraising minimums and team competition are common.
- **Giving and awareness days** — time-boxed campaigns activating ambassadors, departments, chapters, or board members around a shared goal.
- **DIY / third-party fundraising** — a year-round "start a fundraiser" invitation with no campaign container; supporters launch pages for birthdays, memorials, or personal challenges whenever they decide to.
- **Tribute and memorial pages** — supporters fundraise in honor or in memory of a loved one, with highly personalized pages.
- **Ambassador fundraising** — a selected group of committed supporters fundraisers with elevated expectations and tools.
- **Virtual and activity challenges** — supporters tie fundraising to personal activity (distance, streaks, hours), sometimes tracked through fitness integrations.

A variant remains a variant unless it changes the core: if the organization replaces the supporter as page owner and solicitor, the product has moved to the crowdfunding or donation-platform Types; if the supporter keeps the money, it has moved to personal crowdfunding.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Nonprofit Crowdfunding Platform | closest sibling | the organization runs the campaign page and donors give to it; the campaign container is definitional there and optional here; supporter pages appear there only as an optional overlay |
| Online Donation Platform | sibling | the organization runs a standing give capability and donors give to the org directly; the donation checkout layer is shared machinery, but here supporters hold the pages and do the asking |
| Fundraising Management Platform | sibling, org-side | org-side program machinery (planning, appeals, pipeline, performance) across the whole fundraising program; this Type is the supporter-facing campaign machinery |
| Donor Management System | adjacent, org-side | constituency database as system of record; this Type feeds it light donor records with fundraiser attribution |
| Nonprofit Event Management | overlapping for walks/runs | events center on registration and attendance; here the event is a participation vehicle for supporter-led fundraising; vendors sell them as separate product lines, and the seam is thin for endurance events |
| Personal/consumer crowdfunding | different beneficiary | money goes to the page owner for a personal cause; here money always settles to the organization and pages live in an org-controlled context |
| Social-media fundraising | adjacent, platform-native | supporters solicit on a social platform's machinery and the org receives little more than a payout; bridge integrations sync the two worlds |
| Church Giving Platform | adjacent | the center there is the ongoing congregational giving relationship; this Type is discrete campaign- and supporter-driven fundraising |

The boundary with Nonprofit Crowdfunding Platform is the most important one, because the two share thermometers, leaderboards, and campaign momentum machinery. The structural difference is page ownership and the solicitation role: the organization owns the page and does the asking there; the supporter owns the page and does the asking here.

## Representative Products

- CauseVox
- Bloomerang Fundraising (formerly Qgiv)
- OneCause
- Raisely
- Give Lively

The core model was checked against the sibling family (org-run crowdfunding and donation platforms whose supporter pages appear only as optional modules) and against consumer charity-fundraising platforms, to avoid defining the Type by one packaging pattern.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces (product pages):

- CauseVox — Peer-to-Peer Fundraising: https://www.causevox.com/peer-to-peer-fundraising/ ; DIY & Third-Party Fundraising: https://www.causevox.com/diy-fundraising/
- Bloomerang Fundraising (formerly Qgiv) — Peer-to-Peer Fundraising: https://www.qgiv.com/peer-to-peer-fundraising/
- OneCause — Peer-to-Peer Fundraising Software: https://www.onecause.com/solutions/peer-to-peer-fundraising-software/
- Raisely — Peer-to-Peer: https://www.raisely.com/peer-to-peer
- Give Lively — Peer-to-Peer Fundraising: https://www.givelively.org/peer-to-peer-fundraising

Cross-referenced sibling research (org-run crowdfunding and donation platforms, consumer charity-fundraising boundary): research/nonprofit-crowdfunding-platform.md, research/online-donation-platform.md.

> Sourcing limitation: the enterprise pole (Classy / GoFundMe Pro), the athletic-vertical pole (DonorDrive), and the free all-in-one pole (Givebutter) could not be fetched from the research environment (timeouts / blocked responses across passes); vendor help centers were likewise unreachable. All evidence is product-page level. Precise operational details (fee levels, approval rules, payout mechanics, page limits) are intentionally not stated in this document; such details remain unasserted rather than estimated.
