# Advocacy Platform

## Overview

An **Advocacy Platform** is organization-operated software for mobilizing a defined supporter base to take policy-directed actions — contacting decision-makers, signing petitions, posting publicly — and for tracking that participation as measurable evidence of mobilization.

The defining core is small:

```text
Organization-authored campaign
└── mobilized supporter population
    └── policy-directed action
        ├── supporter → target matching (typically by location)
        ├── action execution toward the target
        └── participation record reported to the organization
```

An organization — a nonprofit, association, union, chamber, or campaign group — authors an appeal (the campaign). People in its supporter base act on it through an action page. The platform resolves which decision-makers each supporter should reach, carries the action out (sends the email, places the call, counts the signature), and reports participation back to the organization.

Everything else commonly associated with the category — multi-channel tactics, AI message drafting, paid supporter acquisition, bill tracking, donation appeals — is a widespread but optional extension, not what makes the product an advocacy platform.

When the organization-side campaign disappears and any citizen can engage government directly, the product becomes a civic engagement or petition platform. When supporters disappear and only professional staff engage policy, it becomes government-affairs software. When the targets become customers rather than decision-makers, it becomes marketing software.

## Users & Context

**Operators (the organization's staff):**

- advocacy / government-relations / campaign staff — build campaigns, define targets, author messages, monitor participation
- communications staff — design action pages, write supporter-facing copy, send campaign updates
- agency or consultants — run advocacy campaigns on behalf of client organizations, often managing several clients in one console

**Action takers (the mobilized base):**

- supporters, members, employees, or coalition partners — take actions with minimal friction, usually through nothing more than a short form

**Typical context:** policy moments with a deadline or a decision point — a bill moving through a legislature, a regulatory comment period, a budget decision, an election. Campaigns are often launched at short notice in response to current events, run for days or weeks, then archived. The organization's goal is volume of constituent communication (and visible support), directed at the officials who can decide.

## Core Model

### The defining core

**Campaign** — the organization-authored container for one mobilization effort. A campaign has a cause, a demand or ask, a target set, an action type, and a lifespan (draft → live → archived). It is the unit the organization creates, configures, shares, and measures. Mature products offer several campaign types — email, petition, call, social, letter-to-the-editor — but the campaign container itself is the constant.

**Supporter** — an identified person in the organization's mobilizable base: a member, list subscriber, employee, or coalition contact. Supporters are imported, captured through actions, and re-contacted for future campaigns. The supporter base is both an audience and an asset: growing it ("supporter growth", advocate acquisition) is an explicit goal of the category.

**Target (recipient)** — the policy-side destination of the action: a legislator, official, regulator, or an organization-defined decision-maker. Targets come from two sources: the platform's maintained datasets of officeholders (covering defined jurisdictions and government levels), and custom targets the organization adds itself. A campaign's target set can mix both.

**Action** — one supporter's participation in one campaign: an email sent to their representatives, a call placed and patched through, a petition signature, a social post staged for publishing, a letter submitted for review. The action is the unit of participation; it is executed by the platform (or staged for the supporter to execute) and recorded.

**Participation record & analytics** — every action is captured and aggregated: counts per campaign, per target, per channel; exports; conversion and engagement reporting. This is the organization's evidence of mobilization and its feedback loop for strategy.

```text
Organization staff
  └── Campaign (typed: email / petition / call / social / letter / video)
        ├── Target set (dataset-derived and/or custom)
        ├── Message content (talking points, templates, variations)
        └── Action page (hosted link or embedded form)
              └── Supporter (from the org's base)
                    ├── location entered → matching targets resolved
                    ├── action executed → email / call / signature / post
                    └── participation recorded → analytics & follow-up
```

### Concept vs implementation

The core model is conceptual; products implement each piece differently:

```text
Concept:   Target resolution
Implementations:  maintained civic datasets looked up by the supporter's
                  postal code/zip/address; org-selected fixed target lists;
                  custom targets added by the org; fallback targets when
                  a lookup finds no match

Concept:   Action execution
Implementations:  platform-sent email on the supporter's behalf;
                  telephone patch-through (the system rings the supporter,
                  plays an introduction, connects to each office);
                  counted signature with periodic recipient notification;
                  pre-filled social post the supporter publishes

Concept:   Supporter identity
Implementations:  email address, phone number, postal address — whatever
                  the action form captures; full accounts are usually
                  not required
```

### Standard capabilities

Mature products commonly add, beyond the defining core:

- **Multiple action channels** from one campaign model — email to officials, petitions, patch-through calls, social campaigns, letters to editors, video messages, polls
- **Message authoring layer** — talking points and scripts shown to supporters, editable templates, and message variation/rotation so many supporters don't send identical text (a deliverability concern: legislative offices filter form emails)
- **Thank-you follow-up** — a configurable thank-you page and/or email after the action
- **Supporter messaging** — the organization emails or texts its base with campaign alerts and progress
- **Moderation/approval** — supporter-generated content (letters, videos) can require staff review before delivery
- **CRM and list integration** — syncing supporters and activity into systems like Salesforce; contact import/export
- **Campaign reuse** — templates, cloning, archiving
- **Team and multi-organization management** — staff roles; agency consoles for managing several clients or chapters

## How It Works

### 1. Build the campaign

```text
Create campaign → choose action type
→ configure targets (dataset-derived, fixed list, or custom; set a fallback)
→ author the message (talking points / template / variations)
→ design the action form and pages
→ review, test, launch
```

Configuration is stepped and guided. Target selection distinguishes location-derived targets (each supporter's own representatives) from fixed targets (the same officeholders for everyone). Message authoring separates what the organization wants said (talking points, template text) from what the supporter personally adds. Some products add a launch checklist and a test mode (a test email, a test call) before the campaign goes live.

### 2. Mobilize

```text
Campaign goes live at a URL
→ share the link (email, SMS, social) or embed the form on the org's website
→ supporters arrive at the action page
```

The action page is the supporter's entire experience: context and appeal, a short form (name, contact details, address), the message or talking points, and the action button. It is either hosted by the platform or embedded as a widget in the organization's own site.

### 3. Supporter acts

```text
Supporter enters location details
→ platform resolves their targets (their representative, MP, regulator)
→ supporter takes the action:
     email — sent to the resolved targets, personalized or templated
     call  — the system rings the supporter, plays an introduction,
             patches through to each office in turn
     petition — signature counted (some products notify targets in batches)
     social — a pre-filled post is staged for the supporter to publish
→ thank-you page / email
```

The defining interaction loop is: **location in → targets out → action executed → confirmation**. The supporter does the political act; the platform does the logistics.

### 4. Record and follow up

```text
Participation recorded per campaign
→ analytics: counts, channels, locations, conversion
→ exports and CRM sync
→ org follows up: thank-yous, campaign updates, next campaign
→ campaign archived when finished
```

### Core vs common vs optional

**Defining core** — without these, not an advocacy platform:

- organization-authored campaign
- mobilized supporter population
- policy-directed action
- supporter→target matching
- action execution toward the target
- participation record reported to the organization

**Standard capabilities** — present in most mature products:

- multi-channel action types (email, petition, call, social)
- target datasets with jurisdiction coverage + custom targets
- message authoring with variation
- hosted or embeddable action pages
- analytics, exports, CRM sync
- thank-you follow-up, supporter messaging
- moderation for supporter-generated content
- campaign lifecycle management (draft → live → archived, cloning)

**Optional / variant** — depends on segment and product:

- SMS-to-supporters and mobile keywords; regulations-comment submission; video messages; polls; donation/campaign funding; pledges; lead capture
- paid supporter-acquisition services
- bill tracking and government-affairs adjacency
- AI message generation and AI-driven recommendations
- multi-language action pages; jurisdiction-specific datasets
- self-service vs sales-led onboarding; agency multi-client consoles

## Interfaces

### Organization console

The staff surface. Typical areas:

- **Dashboard / campaign list** — all campaigns with status (draft/live/archived) and headline numbers
- **Campaign builder** — the stepped configuration flow (targets → message → design → review), with previews of the action page and emails, and a test mode
- **Submissions / analytics** — participation counts, per-channel and per-target breakdowns, exports; deeper engagement analytics in some products
- **Supporter management** — the supporter base: import, export, messaging, CRM sync
- **Settings** — team members, organizations/clients, branding, integrations

### Action page

The supporter surface — hosted link or embedded widget:

- campaign context and appeal
- short form (identity + location fields)
- message text / talking points
- the action control (send / call me / sign / post)
- social share prompts

### Thank-you surface

A post-action page and/or email — confirmation, share prompts, sometimes a next ask.

### Call flow

Where call campaigns are offered, a phone-mediated surface: the platform calls the supporter, plays a recorded or text-to-speech introduction, connects them to each target office in turn, and lets them move to the next call without hanging up.

## Important Rules / Behaviors

### Targeting depends on supporter location

Location-derived targeting requires the supporter to provide an address or postal code; the platform resolves targets from its datasets. A **fallback target** may be configured for when a lookup finds no match. Organizations can also fix the target set so every supporter contacts the same offices.

### Repeat participation is often bounded

Depending on the product, a supporter may be limited in how many times they can repeat an action in one campaign, with limits differing by action type and configurable by the organization. The intent is to protect targets from perceived spam and keep petition counts honest.

### Deliverability shapes message design

Because legislative offices filter identical form emails, mature products encourage or automate **message variation** — rotating subject lines and bodies, or generating variations — so that high-volume campaigns still land.

### Some content is moderated

Supporter-authored content that goes to third parties under the organization's name — letters to editors, videos — commonly passes through staff approval before delivery.

### Recipient visibility is a design decision

Whether supporters see which officials they are contacting is configurable; some products hide recipient details by default to keep the action simple.

### Custom targets must be publicly reachable

Organization-added targets use publicly available contact information; the platform is not a private channel into officials' offices.

### Campaigns have a lifecycle

Draft → configured → live → archived. Cloning a campaign copies its configuration for the next push; finished campaigns are archived but their participation records remain.

### Feature depth is often tiered

Products commonly gate capabilities (advanced analytics, supporter messaging, some action types) by plan level; entry tiers are typically free or cheap, with association/enterprise tiers above.

## Variants

- **Nonprofit & charity campaigns** — cause mobilization toward legislators and ministers; petitions and email dominate
- **Association & chamber member mobilization** — associations activate their member base (often professionally) on industry policy; calls and email volume matter
- **Union member engagement** — bargaining and legislative pushes to a member base
- **Corporate grassroots advocacy** — companies mobilize employees, customers, or retirees as constituents; same structure, different supporter source
- **Agency-managed advocacy** — consultancies run campaigns for many client organizations from one console
- **Movement / activist self-service** — low-cost, self-serve campaign pages for small groups and individual organizers
- **Regional coverage variants** — datasets and action semantics differ by jurisdiction (US federal/state/local, Canadian parliamentary, UK, Australia); multi-language action pages where required

A variant remains a variant unless it changes the core loop; corporate grassroots advocacy, for example, keeps the entire defining core and only changes who the supporters are.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Petition / Public Comment Platform | public discovery surfaces where anyone finds and signs; an advocacy platform's petitions are distributed by an organization to its own base, inside a broader mobilization console |
| Civic Engagement Platform | citizen-side engagement with government (follow legislation, contact reps) with no organization authoring campaigns or mobilizing a base |
| Nonprofit CRM / Donor Management System | relationship and donation records over time are the core; advocacy platforms sync supporters into CRMs but their core is the campaign→action→target loop |
| Email Marketing Platform | sends organization→audience messages; advocacy's defining flow is supporter→target, with location matching and multi-channel execution |
| Legislative Tracking Platform / Government Affairs tools | professional staff-side monitoring and lobbying; suites may bundle both, but supporter mobilization is the advocacy platform's defining structure |
| Customer Advocacy Platform | same word, different domain: mobilizes customers for references, reviews, and referrals — commercial outcomes, no policy targets or civic datasets |
| Online Donation / Fundraising Platform | the transaction is money; here the transaction is an action toward a decision-maker (donation appeals inside advocacy platforms are optional) |
| Volunteer Management System | volunteers are scheduled for operational work; supporters are activated for policy pressure |

The closest boundary is with **petition platforms** and **civic engagement platforms**, because all three touch "citizens contacting government". The structural difference is who operates the surface: an advocacy platform is operated by an organization for its own mobilization; petition and civic platforms are public or citizen-side surfaces.

## Representative Products

- **New/Mode** — nonprofit/union advocacy & engagement platform; multi-channel actions (email, petition, call, letter-to-editor, social), civic target datasets, free entry tier
- **One Click Politics** — advocacy software for associations, corporations, chambers, and agencies; multi-action widgets, patch-through calls, regulations-comment submission, agency dashboards
- **Actionable** — self-service advocacy platform for small organizations and individual organizers; template-driven campaign pages with real-time reporting

Other widely cited products in this category (Quorum/Phone2Action, VoterVoice, Action Network) could not be directly researched for this document; see Sources.

## Sources

Research date: **2026-09-06**

- New/Mode — product pages: https://www.newmode.net/ , https://www.newmode.net/solutions , https://www.newmode.net/email ; knowledge base: https://support.newmode.net/ (incl. "Email & Petition Campaigns", "Creating your Call Campaign", "How do New/Mode datasets work?", "Supporter Submission Limits", "Advocacy Action In-Depth Guides")
- One Click Politics — https://oneclickpolitics.com/ , https://oneclickpolitics.com/advocates-actions/
- Actionable (CSAG) — https://countable.com/

> Sourcing limitation: only New/Mode yielded operational help-center documentation. One Click Politics and Actionable were researched from official product pages only (their knowledge bases were unreachable). Several other category vendors (Quorum/Phone2Action, VoterVoice, Action Network, Muster, Capitol Canary, Rally Congress) were unreachable from the research environment. Accordingly, product-specific numeric limits and defaults are intentionally not stated in this document, and cross-product claims are calibrated to the three-product sample. Detailed observations are recorded in the paired Research Notes.
