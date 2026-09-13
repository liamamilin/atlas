# Professional Social Network

## Overview

A **Professional Social Network** is a member-built network of real professionals in which each member maintains a self-authored **professional profile** — a career record rather than a lifestyle page — connects with other identified professionals, and becomes discoverable and reachable for professional outcomes: hiring and being hired, business development, collaboration, and industry knowledge.

The defining structure is small:

```text
Professional Profile (career record, presented for evaluation by others)
└── Professional Connection Graph (relationships between identified real professionals)
    └── Professional-opportunity orientation (the network exists to produce work-related outcomes)
```

Everything else commonly associated with these products — the jobs marketplace, the content feed, endorsements and recommendations, company pages, recruiter tooling, identity verification, premium outreach — is a widespread capability built on top of this core. Early-generation professional networks operated with only profiles, invitation-based contacts, and peer recommendations, and still belonged to this Type; a product that loses any part of the core stops being one.

## Users & Context

The primary user is a **working professional** who maintains a profile as their professional presence on the internet — visible to employers, colleagues, peers, and potential counterparties — and uses the network to stay reachable as their career moves.

Around this primary user, mature networks serve several distinct consumption parties, all drawing on the same member graph:

- **recruiters and employers** — search members, evaluate profiles, and initiate contact about roles
- **sales and business developers** — find and reach people at target companies
- **peers and industry participants** — share professional content, discuss industry topics, and meet through groups and events
- **companies** — maintain employer/brand pages and market opportunities to members

Typical moments of use: updating the record after a role or skill change, accepting or sending connection invitations, searching for former colleagues and industry peers, reading professional content, being contacted about an opportunity, and looking for or evaluating jobs.

## Core Model

### The Defining Core

```text
Professional Profile
└── Connection Graph (identified professionals)
    └── Professional-opportunity orientation
```

Three properties, jointly held:

- **Professional profile** — a persistent, member-maintained record of the person's professional self: role, work history, education and skills (or their domain equivalent). Its defining property is that it is written for **evaluation by other parties** — employers assessing a candidate, a partner assessing a contact, a peer assessing credibility — not primarily for self-expression. Without this, the product is a general social network.
- **Professional connection graph** — person-to-person relationship edges between real, identified members. The graph is the trust and reachability fabric of the network: who can message whom, what profile detail is visible, and how people are introduced all derive from it. In mature products the edge is **consent-based** — an invitation or contact request that the recipient accepts or rejects. Without the graph, the product degenerates into a resume database or people directory.
- **Professional-opportunity orientation** — the profile and graph are organized around producing work-related outcomes: being discovered for a role, reaching a counterparty, learning from the industry. Because professional evaluation depends on authenticity, a **true-identity norm** is structural: members participate as their real professional selves. Without this orientation, the product is a general social network that happens to have CV fields.

### Standard Capabilities of Mature Products

These are widespread and expected, but they ride on the core rather than define it:

- **Degrees of connection** — the relationship between two members (direct, once-removed, further, or none) is a user-visible fact that shapes what they can do with each other.
- **Graph-gated messaging** — members message their direct relationships freely; reaching beyond the graph is a controlled or paid channel, and message requests exist for shared-context contacts (coworkers, group members).
- **A follow/broadcast layer** beside the consent graph — members publish posts and articles to an audience without a mutual relationship.
- **Network-building machinery** — member search by name/role/company/location/industry is common across the researched sample; some products add contact import, people-you-may-know suggestions, and school-based discovery of former classmates.
- **Profile-consumption transparency** — some products show members that their profile was viewed, and by whom at deeper tiers, because being evaluated is a normal expected event on the network.
- **Peer attestation** — some products attach written recommendations (commendations from people one has worked with, which the recipient typically accepts or dismisses) and skill endorsements to the profile as peer evidence.
- **Jobs and hiring flows** — a job marketplace where members apply with their profile as the application, plus network-mediated hiring signals (learning that a connection is hiring).
- **Company and employer presence** — followable company pages and employer-branding profiles.
- **Community surfaces** — a professional content feed, groups around shared professional interests, and events.
- **Visibility controls** — members govern who sees their profile sections, contact list, and photo, and how reachable they are.

### One Structure, Many Implementations

```text
Concept:                          Professional identity record
Implementations:                  CV-style profile, "business card" profile,
                                  publication-backed academic profile,
                                  real-name-verified identity record

Concept:                          Professional relationship edge
Implementations:                  invitation → accept (connection),
                                  contact request → accept/reject,
                                  colleague confirmation

Concept:                          Professional-opportunity flows
Implementations:                  jobs marketplace + recruiter tools,
                                  talent/recruiting platforms on the network,
                                  sales prospecting over the member graph,
                                  expert networks, employer branding
```

A reader who has only seen the global, jobs-centered implementation should still recognize a community-heavy regional network, a real-name-verified Chinese one, or an academic one as members of the same Type — and should recognize a job board or a people-search tool as *not* being one.

## How It Works

### Join and establish the professional record

```text
Create an account under one's real professional identity
→ compose the profile (headline, experience, education, skills)
→ tune visibility (who sees what)
→ the profile becomes discoverable to the network
```

The profile is durable and cumulative: it is edited as the career moves, and profile changes (new role, work anniversary) can surface as updates to the member's network.

### Build the network

```text
Import contacts / receive suggestions (people you may know, alumni, search)
→ send an invitation or contact request, usually with professional context
→ recipient accepts or declines
→ mutual relationship established
```

Connection is deliberately relationship-first: the network expects a real professional reason to connect, and unsolicited mass inviting is treated as abuse. A weaker follow action lets members subscribe to someone's public content without a mutual relationship.

### Be discovered and evaluated

```text
Other members, recruiters, or employers search or browse
→ they read the profile (experience, skills, attestations)
→ they may view, follow, message, or reach out about an opportunity
→ the member sees that the profile was viewed (in some products, by whom)
```

This loop is what the profile exists for: professional evaluation by parties the member does not yet know, mediated by search, suggestions, and the graph.

### Reach and be reached

```text
Within the graph: direct messaging
Shared context (coworkers, group members): message request → accept
Outside the graph: controlled or paid outreach channel
→ recipient responds or declines
→ ongoing exchange may turn into a relationship
```

Reachability scales with relationship: the closer the graph distance, the more open the channel. Out-of-network contact exists as a governed path, not an open one.

### Realize opportunities

```text
Opportunity flows ride on the same profile and graph:
- job seeking: search/apply with the profile; be found by recruiters
- hiring: source and contact candidates from the member graph
- business: find and reach counterparties at target organizations
- knowledge: publish and read professional content; groups; events
```

The characteristic pattern is that **commerce and opportunity are layered onto member identity**, not bolted beside it: a job application is the profile in motion; a hiring notification is the graph speaking.

## Interfaces

Described conceptually; names and layouts vary by product.

### Profile page (own and others')

- Purpose: present and evaluate the professional record.
- Typical information: headline/current role, experience history, education, skills, peer attestations where the product offers them, activity, contact info.
- Primary actions: edit sections, message, connect, follow; on others' profiles, give endorsements or request/write recommendations where offered.

### My Network / contacts

- Purpose: manage the personal connection graph.
- Typical information: pending invitations, suggestions, existing relationships.
- Primary actions: accept/decline invitations, send invitations, browse and search relationships, control contact-list visibility.

### Member search

- Purpose: find professionals by identity attributes (name, role, company, location, industry, school).
- Typical information: results with relationship degree indicators.
- Primary actions: view profile, connect, message, save.

### Feed

- Purpose: professional content and updates from the network — posts, articles, profile changes, followed companies.
- Primary actions: react, comment, share, publish, follow entities.

### Messaging

- Purpose: direct exchange with members, gated by relationship and settings.
- Typical information: conversations, requests from shared-context contacts.
- Primary actions: send, reply, accept/decline requests, block/report.

### Jobs surface

- Purpose: search and apply for roles; manage applications; receive network-mediated hiring signals.
- Primary actions: search, apply with profile, save, set open-to-work signals.

### Groups / events

- Purpose: professional communities and gatherings around industries and interests.
- Primary actions: join, post, RSVP, meet attendees.

### Employer/company page

- Purpose: the organization's presence — employer brand, openings, updates.
- Primary actions: follow, view jobs, view employees in one's graph.

### Settings / privacy

- Purpose: control identity, profile visibility, contact-list visibility, message reachability, notifications.

## Important Rules / Behaviors

- **True identity is a structural norm.** Members participate as their real professional selves; fake profiles, borrowed likenesses, and misrepresenting one's experience or affiliations violate the network's foundation, because every downstream behavior (evaluation, hiring, attestation) assumes the record is real.
- **The graph governs interaction.** Relationship degree or contact status determines whether two members can message directly, how much of a profile is visible, and how outreach can happen. The connection list is simultaneously a personal asset and a privacy surface — members can hide it.
- **Consent shapes the edge.** A relationship forms only when both sides accept; invitations carry professional context by design, and spamming strangers with invitations is treated as abuse and can restrict the account.
- **Evaluation is expected and somewhat symmetric.** Members accept that their profile is being read for professional judgment — and in many products can see who is reading. Reaching beyond one's graph is a governed, often paid, channel.
- **Professional conduct is enforced by policy.** These networks explicitly frame conduct as professional: harassment and romantic pursuit are prohibited (one archetype states plainly that it is a professional networking platform, not a dating site), and commercial content rules target spam rather than legitimate professional exchange.
- **Opportunity flows stay attached to identity.** Applications, recruiter outreach, and hiring signals reference the member's profile and graph position — separating them (anonymous applications, unattributed listings) is the boundary behavior of a job board, not a professional social network.

## Variants

- **Global archetype** — full stack: profile + graph + jobs marketplace + feed + groups + recruiter and sales products on top; monetized through premium consumer tiers and recruiter/business subscriptions.
- **Regional incumbents** — the same Type dominant in a region (e.g., a European DACH network), often with the recruiting side as the main commercial engine and thinner community surfaces.
- **Real-name-verified networks** — regional variants (notably in China) where verified professional identity is a headline capability, often combined with workplace communities, colleague circles, and company-review content.
- **Community-forward variants** — networks where professional topics, anonymous or semi-anonymous workplace discussion, and content carry more weight than the jobs marketplace.
- **Vertical/academic variants** — professional networks for a domain (e.g., science) where the profile's substance is publications and academic career, and the graph is the co-author/colleague fabric; the same core in domain form.
- **Jobs-heavy variants** — implementations where the job marketplace dominates the product surface; recognizably this Type as long as member profiles and the connection graph remain the substrate.

A variant stops being this Type when the career-record profile, the identified professional graph, or the professional-opportunity frame is removed — the failure modes are listed under Related Application Types.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Job Board | closest commercial neighbor | listings-first: posting + application workflow without a persistent member-authored identity or relationship graph; a professional network's jobs flow rides on its graph, and applications carry the profile |
| General Social Network | same genus, different frame | lifestyle identity, social sharing, entertainment; no career-record profile, no professional-evaluation consumption, no true-identity-as-structural-requirement |
| Social Profile Network | profile-directory neighbor | people/profile pages without the living connection graph and the professional-opportunity frame; a professional network without its graph degrades into this |
| Interest-based Social Network | content-frame neighbor | organized around interests and creative output rather than career identity and opportunity; portfolio-first products drift here |
| CRM / Sales Prospecting Platform | structural opposite on the B2B side | holds organization-owned records *about* people for the org's purposes; a professional network holds member-authored identities owned by the individuals |
| Candidate Search Platform / ATS | recruiter-side workflow | consumes candidate data and runs hiring workflow; the professional network supplies the substrate these tools often draw from |
| Dating Application | adjacent by exclusion | matchmaking between individuals for romantic connection; professional networks explicitly prohibit this use and organize relationships around work |

The most consequential boundary is with the **Job Board**, because mature professional networks all contain a jobs marketplace. The test is the substrate: if removing the member profile and connection graph leaves the product's job value intact, it is a job board; if the jobs flow collapses without the graph, it is a professional social network.

## Representative Products

- LinkedIn — global archetype; profile + connection graph + jobs + recruiter/sales products
- XING — European (DACH) regional incumbent; networking + jobs with a recruiting-heavy business side
- Maimai (脉脉) — Chinese regional network; real-name professional identity verification, workplace community, colleague circles, recruiting

These were chosen to span the market's structural space: the global archetype, a regional incumbent, and a real-name-verified regional variant with a different community emphasis.

## Sources

Research date: **2026-09-08**

- LinkedIn Help — Help root, "Build your professional network," "Various ways to connect," "Your Network and Degrees of Connection," "Your Profile" topic, "Connections" topic, "Jobs through social hiring": https://www.linkedin.com/help/linkedin
- LinkedIn Professional Community Policies: https://www.linkedin.com/legal/professional-community-policies
- XING Help Center — root, Networking (Contacts / Member search / Messages / Insights), "Add someone as a XING contact," "My profile": https://help.xing.com/hc/en-us
- Maimai (脉脉) product/about page: https://maimai.cn/

> Sourcing limitation: an academic-vertical professional network was included in the research plan, but its help center could not be reached from the research environment (connection errors, and HTTP 403 on the main site); encyclopedic sources for the historical check also timed out. Vertical and historical claims in this document are therefore stated at structural, non-dated strength and no precise operational facts rest on them. Precise product numbers (connection caps, time windows, endorsement limits, tier features) observed in single products were deliberately kept out of this document and recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes (`research/professional-social-network.md`).
