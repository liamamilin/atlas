# Customer Advocacy Platform

## Overview

A **Customer Advocacy Platform** is a brand-side system of record for operating a customer advocacy program: it maintains a managed population of customer advocates, defines specific advocacy actions the brand wants from them, and runs each ask through a managed loop — targeting, participation, review, and recording — so the resulting advocacy (reference calls, reviews, testimonials, case studies, referrals, speaking, community contributions) can be delivered to the sales, marketing, and customer teams that need it, and measured against business outcomes.

The defining core is small:

```text
Advocate population of record
└── Advocacy ask (a specific requested action)
    └── Managed ask → participation loop
        (target → participate with proof → review/approve → record)
```

Everything else the market associates with the category — points, badges, leaderboards, reward catalogs, reference-request routing, advocate hubs, communities, revenue-influence dashboards, AI advocate sourcing — is widespread in current products but is not what makes the product an advocacy platform. A rewards-less reference program run from a spreadsheet satisfies the same core; the platform replaces the spreadsheet, not the program.

When the only ask is "refer someone" and the machinery centers on offer design, conversion attribution, and reward fulfillment, the product is a Referral Marketing Platform. When the reward attaches to the customer's own repeat purchases, it is Loyalty Program Management. When the participants are employees, external creators, or policy targets, it is a different Application Type entirely.

## Users & Context

Primary operators:

- **Customer advocacy / customer marketing program manager** — owns the advocate population, defines asks and activities, reviews completions, manages recognition, and reports program health. This role is the platform's primary seat.
- **Reference manager** (B2B pole) — a specialization focused on fulfilling reference requests from sales: finding the right advocate, getting approvals, scheduling, and closing the loop.

Internal consumers:

- **Sales reps** — request reference customers and customer proof for specific opportunities, often directly from the CRM.
- **Marketers** — request case studies, quotes, reviews, speakers, and social amplification.
- **Customer success / account managers** — nominate advocates, approve use of their accounts, and keep advocate information current.

The advocates themselves:

- **Customers** (sometimes also partners or long-time users) who agree to perform advocacy actions. They interact through an advocate portal or hub, through email, or inside the brand's customer community.

The typical context is a B2B or consumer brand with an installed customer base large enough to sustain a program, where word-of-mouth evidence — a credible customer willing to talk to a prospect, post a review, or tell their story — materially affects sales and marketing outcomes.

## Core Model

### The Defining Core

**Advocate population of record.** The platform's foundation is a set of identified customers held as managed program members. Each advocate record carries who the person is (tied to their account/company), what they can credibly speak to (products used, industry, use cases, expertise), their program standing (active or inactive), their preferences (which activity types and topics they opt into, through which channels), any use limits, and their participation history. Advocates are recruited deliberately — nominated by internal users, identified from recently won deals, or enrolled through onboarding — because not every customer is suited or willing.

**Advocacy ask.** The unit of work is a brand-defined request for a specific advocacy action. Asks take many forms: take a reference call with a prospect, write a review on a third-party site, provide a testimonial or quote, participate in a case study or customer story, refer a peer, speak at an event or webinar, share brand content socially, answer questions in the community, join a customer advisory board, test a beta, or give product feedback. An ask specifies what to do, how to submit proof of completion, and (commonly) what recognition it carries.

**Managed ask → participation loop.** Asks do not float freely; they are targeted to suitable advocates based on segment, preferences, and fit, then offered through the advocate's preferred channel. The advocate responds — accepts, completes the action, and submits proof (a link to the review or post, a file, a confirmation). Completions pass a review or approval gate before being credited. Every participation is recorded against the advocate and the program, which is what makes overuse protection, recognition, and measurement possible.

If any of the three is removed, the product stops being an advocacy platform: without advocate records it is an anonymous campaign tool; without asks it is a contact database; without the managed loop it is one-off outreach with no program memory.

### Standard Capabilities

Mature products commonly add the following around that core. They make the program practical; they do not define the Type.

- **Recognition and rewards** — points, badges, levels, leaderboards, and reward catalogs; appreciation gifts fulfilled through gifting services. Some products also award points to internal users (for nominating advocates, arranging activities, or keeping profiles current) to drive internal adoption.
- **Advocate portal / hub** — the advocate-facing surface listing available activities, accepting submissions with proof, showing points and progress, and offering the rewards catalog.
- **Advocate sourcing and recruiting** — nominations from any internal user, automated follow-up with recently won customers to assess willingness, internal campaigns to gauge referenceability, and automated profile-refresh workflows.
- **Reference-request management** (strongest in the B2B pole) — internal users submit requests from the CRM, email, or chat; requests route to the program team; the customer's account team approves use before the customer is approached; fulfillment is tracked; past and pending requests are visible so the same customers are not overused.
- **Advocacy content management** — the outputs (stories, quotes, videos, reviews) are stored as verified, tagged customer content that can be searched and shared with prospects through microsites or sales-content portals.
- **Program measurement** — activity counts, engagement scores, request fulfillment rates and times, reasons requests went unfulfilled, coverage gaps in the advocate pool, and attribution of advocacy activity to pipeline and revenue.
- **Integrations** — CRM (as the source of accounts, opportunities, and request intake), marketing automation, customer-success platforms, community platforms (advocacy opportunities embedded inside the community), gifting services, sales-enablement portals, and third-party review sites.
- **AI assistance** (current generation) — listening for advocate signals across communities and call recordings, matching advocates to requests, drafting content, and agent-style handling of requests and nominations.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Advocate population of record
Realized as:  program-member tags on CRM contacts/accounts, standalone
              advocate profiles, portal accounts with tier tags

Concept:  Advocacy ask
Realized as:  challenges, activities/activity types, reference requests,
              advocacy opportunities, campaigns

Concept:  Review/approval gate
Realized as:  manual admin review queues, automated approval rules,
              account-team approval for reference use, post-activity
              outcome feedback
```

A reader who has only seen one style — say, a gamified advocate hub — should still be able to recognize a request-driven reference desk as the same Type from the core model.

## How It Works

### Build the advocate population

```text
Identify candidates (nominations, won-deal follow-up, engagement signals)
→ invite / enroll the willing ones
→ capture profile: products, industry, expertise, topics, preferred channels
→ set standing (active) and any use limits
→ keep profiles current over time
```

### Run the ask → participation loop

```text
Define the ask (action, instructions, proof format, recognition)
→ target suitable advocates (segment, preferences, history)
→ offer through the portal, email, community, or chat
→ advocate completes the action and submits proof
→ program team reviews: approve, or reject with feedback and resubmit
→ participation recorded; recognition credited
```

The review gate matters: submissions can be rejected (wrong hashtag, product not visible, customer not approved for external use), and rejected submissions return to the advocate for correction. Multi-part asks are credited only when every required part is approved.

### Fulfill a reference request (B2B pole)

```text
Sales rep requests a reference from the CRM opportunity
→ request routed to the program team (or auto-notified)
→ program team searches advocates by industry/product/region/expertise
→ account team (AE or CSM) approves use of the customer
→ invitation sent to the advocate; response tracked
→ reference fulfilled (typically a live call; some products also offer recorded reference formats)
→ outcome feedback captured (happened / went well / declined / deferred)
→ participation and revenue influence recorded
```

### Recognize and measure

Completed advocacy earns recognition — points redeemable from a catalog, badges, levels, public acknowledgment, or gifts. The program side watches the health of the whole system: how many advocates are active, how fast requests are fulfilled, which requests failed and why, where the advocate pool has coverage gaps (no banking references, no advocates for a new product), and how much pipeline and revenue advocacy activity influenced.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Program console (operator side)

The program manager's home. Typical information: advocate list with standing, attributes, and history; activity/ask catalog; request queues; review queues. Primary actions: create and target asks, review and approve submissions, manage requests, record outcomes, configure rewards.

### Advocate portal / hub

The advocate's surface. Typical information: available activities with instructions and recognition offered, submission forms with proof formats (link, text, file upload, or picking a recent social post), points balance, badges and progress, rewards catalog, personal profile and preferences. Primary actions: browse and accept activities, submit completions, redeem rewards, update preferences.

### Requester surfaces (internal)

Where sales and marketing ask for advocacy. Typically lightweight: a request form on the CRM opportunity, a chat bot, or email intake; status of the request visible to the requester. Reference search — filtering advocates by industry, product, region, and past activities — is the matching surface behind it.

### Reporting / program health

Dashboards over the program: active advocates, acts of advocacy, content produced, fulfillment rate and time, unfulfilled-request reasons, coverage gaps, engagement leaderboards, and revenue-influence views tying advocacy to pipeline and closed business.

## Important Rules / Behaviors

### Advocate consent and preferences govern targeting

Advocates opt into activity types and topics and choose channels. Asks are offered "on their terms" — a customer who has not opted into public reviews should not receive review asks. Preferences are a structural control, not a courtesy.

### Use limits and overuse protection

Advocate goodwill is a finite resource. Products track each advocate's past and pending participations, support per-advocate use limits and per-activity completion caps, and surface overuse before another ask is made. Reference requests additionally require the customer's account team to approve use before the customer is approached.

### Completion passes a review gate

Proof of completion is reviewed before credit: approve, or reject with a reason and allow resubmission. For reference activity, the loop closes with outcome feedback (did the call happen, how did it go), because an unfulfilled or failed request is a program signal, not just a missing record.

### Advocate data has a shelf life

Profiles decay — people change roles, products, and willingness. Mature products automate profile refresh; some also track advocates' job changes, because reference search is only as good as the data behind it.

### Rewards are gated by approval

Recognition is credited after the review gate, not at submission. Points accumulate to a balance redeemable from a catalog; some programs also reward internal users for program work (nominating, arranging, updating profiles) to sustain adoption on the operator side.

### The program serves commercial outcomes

Advocacy activity is recorded in a form that can be tied to business results — the opportunity a reference supported, the deal influenced by a customer story, the referral that became a lead. Program reporting speaks the language of pipeline and revenue, not just participation counts.

## Variants

- **Gamified advocate hub** — challenges, points, badges, and community-style engagement at the center; asks pushed to a broad advocate population (common in enterprise B2B customer marketing).
- **Request-driven reference desk** — the sales reference request is the center of gravity; advocate database, search, routing, approval, and fulfillment tracking; lighter gamification (common in CRM-centric B2B organizations).
- **Self-serve ambassador / advocate programs** — consumer-brand flavored; activity catalogs, tiers, social-share and UGC activities, referral tracking, branded mobile apps; self-serve administration.
- **Customer-evidence platforms** — focused on capturing and structuring customer proof (stats, quotes, stories) for use in marketing and sales; adjacent to this Type, under-represented in this research sample.
- **Community-embedded advocacy** — advocacy opportunities offered inside the brand's customer community rather than (or alongside) a standalone portal.
- **Multi-program platforms** — the same product also running referral, loyalty, affiliate, or influencer programs; the advocacy core coexists with sibling program machinery.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Referral Marketing Platform | the referral program is the whole world: offer design, the advocate's personal trackable identity, attributed conversion, reward fulfillment. Here, referral is one ask among many, managed against advocate records |
| Loyalty Program Management | rewards attach to the customer's own repeat purchases; here rewards attach to contributions to the brand's commercial motion (evidence, references, referrals) |
| Influencer Marketing Platform | participants are external creators with audiences, engaged for content collaboration and campaigns; here participants are the brand's own customers providing proof |
| Affiliate Management Platform | participants are registered external partners earning commissions on tracked sales; different population, enrollment, and economics |
| Employee Advocacy (adjacent market) | employees share brand content from their own networks; here customers provide evidence. Vendors ship these as separate products |
| Voice of Customer Platform / Customer Feedback Management | the primary object is the feedback signal (surveys, NPS, verbatims) analyzed at scale; here the primary object is the advocacy action. Feedback and beta tests appear as one activity type |
| Advocacy Platform (nonprofit/civic) | same word, different domain: mobilizes supporters toward policy decision-makers (legislators, regulators) with civic action types; no policy targets or civic datasets here |
| Review Platform | consumer-facing discovery surface where reviews are read; here the brand side mobilizes customers to write reviews on such platforms |
| Customer Community Platform | member-to-member discussion is the primary object; advocacy opportunities may be embedded in a community, but the advocate record and ask loop are this Type's core |
| Customer Relationship Management / CRM | holds the customer relationship and commercial history; advocacy holds the program — advocate standing, asks, activities, outputs, and governance. Advocate records typically ride on CRM accounts and contacts |
| Sales Enablement / content platforms | distribute sales content, including customer proof produced here; they are a distribution surface, not the advocate system of record |

The sharpest seam is with the Referral Marketing Platform, because the same vendors often ship both and referral is a native activity here. The working test: participant population plus program scope — a system whose only ask is referral and whose machinery is offer/attribution/reward fulfillment is a referral platform; a system managing many ask types against a standing advocate population is this Type.

## Representative Products

- Influitive — enterprise advocate-hub pole; gamified challenges, broad use-case framing (reviews, references, referrals, stories, social, feedback)
- SlapFive — enterprise "customer marketing & advocacy system of record" pole; reference automation, advocate & proof records, revenue-influence analytics
- ReferenceEdge (Point of Reference) — Salesforce-native reference-management pole; advocate database, request routing, close-the-loop, dual-sided rewards
- BrandChamp — self-serve ambassador/advocate pole for consumer brands; activity lifecycle, tiers, rewards catalog, referral tracking

## Sources

Research date: **2026-09-08**

- BrandChamp Knowledge Base — https://support.brandchamp.io/ ; "Walk Through - Creating a Social Media Activity" — https://support.brandchamp.io/article/28-walk-through-creating-a-social-media-activity ; "Walk Through - Completing and Approving an Activity" — https://support.brandchamp.io/article/29-walk-through-completing-and-approving-an-activity
- BrandChamp — https://brandchamp.io/
- Influitive — https://influitive.com/ ; https://influitive.com/customer-advocacy-platform/ ; https://influitive.com/customer-advocacy-software/features/ ; https://influitive.com/dictionary/
- SlapFive — https://www.slapfive.com/ ; https://www.slapfive.com/customer-advocacy/ ; https://www.slapfive.com/customer-reference-management-software/ ; https://www.slapfive.com/platform/
- ReferenceEdge (Point of Reference) — https://www.referenceedge.com/

> Sourcing limitation: only BrandChamp published reachable operational documentation (help-center articles) at research time. Influitive's support help center is closed, SlapFive's help center was unreachable, and ReferenceEdge publishes no public knowledge base, so evidence for the B2B pole rests on official product pages. Claims about that pole's internal mechanics are stated at conceptual strength; no precise numeric limits, state names, or defaults are asserted. One candidate product in the customer-evidence sub-pole could not be reached and remains under-sampled.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
