# Learning Experience Platform / LXP

## Overview

A **Learning Experience Platform (LXP)** is an organization-operated learning platform built around the learner's own development experience. It assembles learning content from many sources into one discovery surface, lets members of the organization's population find and follow learning on their own initiative, and accumulates what each person learns on a personal development profile. Organizational direction — assigned pathways, required learning, HR-driven auto-enrollment — is supported as an overlay alongside the learner-directed loop.

The defining core is deliberately small:

```text
Organization-provisioned learning population
└── Unified multi-source content ecosystem
    (third-party providers, open-web curation, learner-contributed items,
     vendor-curated libraries, org-authored/imported courseware)
    └── Learner-directed discovery and consumption
        (browse / search / follow / consume)
        └── Per-person development profile of record
            (completions accumulate → skill signals / achievements → recommendations)
    (organization-directed assignments run alongside as an overlay)
```

Everything else the market associates with LXPs — skills taxonomies and ratings, AI recommendations, curated pathway libraries, social and collaborative learning, gamification, learning in the flow of work — is standard mature structure layered on that core, not part of the definition. Early LXP-era products with no AI and no skills engine satisfy the core.

In today's market the Type is realized in three packagings: standalone pure-play products, unified platforms that also carry full learning-management machinery, and LXP-posture modules inside corporate learning suites. When the center of gravity shifts to administration — enrollment management, compliance records, certification validity — the product is a corporate learning management platform of the Employee Learning Platform family; the boundary is one of emphasis, not of disjoint structure (see Related Application Types).

## Users & Context

Primary users:

- **Learners (employees)** — the platform's center of gravity. They browse and search the content ecosystem, follow curated pathways, consume items (reading an article, watching a video, taking a course), mark their own completions, build and rate their skills, and watch their development profile accumulate.
- **L&D / learning administrators** — operate the platform as a product: connect content providers, import and author content, curate pathways and academies, target content to audiences, assign required learning, and monitor engagement and skills data.
- **People managers** — view their team's learning activity and skills, validate self-assessments, approve or recommend learning, and use team dashboards.

Secondary users:

- **Subject-matter experts** — contribute internal expertise: co-authoring courses, answering questions in content forums, surfacing as recommended experts through skills data.
- **Moderators / community managers** — keep discussion spaces healthy where collaborative learning is used.

Typical context: workforce upskilling and reskilling, onboarding programs, leadership development, and the broader goal of continuous, self-directed learning at work. The platform typically coexists with an HR system (source of the population) and often with a corporate LMS (whose course completions flow into the LXP's profile). Administrators use the platform continuously; learners use it habitually, on web, mobile, and increasingly inside work tools (chat apps, browser extensions).

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as an LXP:

- **Organization-provisioned learning population.** Learners exist as identified people inside the platform, sourced from the organization — synchronized from HR/identity systems, organized by org structure into groups or branches. The population is the organization's own people (or, in extended-enterprise deployments, its customers and partners served the same way), not anonymous visitors. Without this, the product is a public content site or a consumer course platform.

- **Unified multi-source content ecosystem.** The platform's supply of learning comes from beyond the organization's own authoring, assembled into one addressable surface: third-party provider catalogs, open-web content (articles, videos, podcasts) curated by the organization or captured by learners, learner-contributed items, vendor-supplied curated pathways, and — alongside these — internally authored or imported courseware. The unit of consumption is the individually consumable content item, not only the formal course. Without this, the product is an org-authored course catalog — the content model of a plain LMS.

- **Learner-directed development loop over a per-person profile of record.** The learner initiates: they browse recommendations, search, follow a pathway, consume an item, and record the completion — either by marking it complete themselves or by having the completion verified from the source system (a connected course provider or LMS). Completions accumulate durably on the person's profile, where they generate skill signals, achievements, and points, and feed further recommendations. Organization-directed assignment exists as a supported overlay (assigned plans and pathways, required learning, auto-enrollment driven by HR data), but the engine of the product is the learner's own loop. Without the accumulating profile, the product is a content portal with no memory; without the learner-directed loop, it is an assignment-driven training system.

### The Content Ecosystem

The ecosystem is the LXP's supply side, and its breadth is what separates it from a single-library course catalog. Content enters from five typical sources:

1. **Connected third-party providers** — external course libraries integrated so that their catalogs appear in the platform's discovery surface and their completions flow back into learner profiles.
2. **Open-web curation and capture** — articles, videos, podcasts, and documents found on the web, added by curators or captured by learners themselves (browser-extension capture and bookmarking are common mechanisms).
3. **Learner-contributed content** — resources and know-how shared by employees in groups, channels, and communities.
4. **Vendor-curated libraries** — ready-made pathway collections supplied by the platform vendor.
5. **Org-authored and imported courseware** — internally produced courses and standards-packaged e-learning, sometimes co-created with subject-matter experts and AI-assisted authoring.

Curation containers organize this supply: curated collections of required and optional items (pathways), evolving collections that are periodically refreshed (plans), audience-specific content channels, and branded academies for cohorts or campuses.

### The Development Profile

The profile is the LXP's record of record. It is the learner's durable, accumulating evidence of development:

- a **collection** of completed content items across all sources,
- **skill signals** generated by what the person has learned,
- **skills** the person has added and had rated (by themselves, peers, or managers, where the organization enables it),
- **achievements** such as points, badges, and streaks,
- and, in mature products, a **career view** — role history, target roles, and the skill gaps between here and there.

The profile is learner-facing by design: it is the person's development story, not an administrative compliance file. Recommendations and skill-gap views are computed from it.

### Standard Capabilities

Mature products commonly add the following. They make the LXP practical; they do not define the Type.

- **Skills layer** — skills attached to both people and content; self/peer/manager ratings; AI tagging of content with skills; focus-skill selection; content recommendations and target-job mapping driven by skills.
- **AI personalization (era-current)** — recommendations keyed to role, skills, and gaps; conversational search and AI companions; adaptive sequences that skip content the learner has already mastered.
- **Social and collaborative learning** — groups and communities, in-content forums and Q&A, reactions and upvotes, expert finder, user-generated content with moderation.
- **Gamification** — points, badges, leaderboards, challenges.
- **Assignment and required learning** — assigned pathways and plans, required-learning lists, HR-driven auto-enrollment, manager approval steps.
- **Manager surfaces** — team activity and skills dashboards, recommendations a manager can push to team members.
- **Analytics** — engagement, content usage, and skills-developed reporting for L&D.
- **Flow-of-work delivery** — mobile apps, chat-app integrations, browser capture extensions.
- **Scheduled learning** — events, sessions, and classroom-style activities alongside self-paced consumption.

### One Structure, Many Implementations

The core model is conceptual; products realize each concept differently:

```text
Concept:  Provisioned learning population
Implementations:  HR/identity-system synchronization; SSO; groups mirroring
                  the org structure; HR-driven auto-enrollment

Concept:  Multi-source content ecosystem
Implementations:  provider integrations; standards-based import (SCORM/xAPI);
                  open-web curation; browser capture; learner-shared channels;
                  vendor-curated pathway libraries; AI-surfaced content

Concept:  Completion evidence
Implementations:  learner-marked completion; provider-verified completions
                  sent back from source systems; LMS-integration data flows

Concept:  Development profile of record
Implementations:  profile pages holding collections, skill signals, points;
                  skills pages with ratings; career/target-role views

Concept:  Curation containers
Implementations:  pathways, plans, paths with sessions, channels, playlists,
                  branded academies
```

A reader who has only seen one packaging — for example, an LXP module inside a learning suite — should still be able to recognize a standalone pure-play product as the same Type from this model.

## How It Works

The platform runs a small number of recurring loops.

### 1. Establish the population

```text
Connect identity/HR source (or maintain users directly)
→ learners appear as identified records organized into groups
→ audiences and visibility scopes are set
```

Population changes (joiners, movers, leavers) propagate from HR systems.

### 2. Assemble the content ecosystem

```text
Connect content providers and import packaged courseware
→ curate open-web resources; enable learner capture and sharing
→ author internal courses (often with subject-matter experts)
→ organize everything into channels / catalogs / collections
```

### 3. Curate and target

```text
Build pathways and academies from ecosystem content (required + optional items)
→ target content and containers to audiences, groups, or roles
→ set required learning and assignments where the organization directs learning
→ optionally: HR data triggers auto-enrollment
```

### 4. Discover and learn

```text
Learner opens home surface
→ sees recommendations keyed to role, skills, and gaps; sees assigned learning
→ searches or browses; follows a pathway or playlist
→ consumes items (reads, watches, takes a course, attends a session)
→ records the completion (marks it, or the provider verifies it back)
```

### 5. Grow the profile

```text
Completed items accumulate on the personal profile
→ skill signals and achievements update
→ skills are added, self-rated, validated, reviewed
→ recommendations and skill-gap views adapt
```

### 6. Oversee and measure

```text
Managers view team activity, skills, and completions; validate ratings; nudge learning
→ L&D monitors engagement, content performance, and skills-developed analytics
→ curation and targeting are adjusted in response
```

### Tiers of capability

**Defining core** — without these, not an LXP:

- organization-provisioned learning population
- unified multi-source content ecosystem
- learner-directed discovery and consumption
- per-person development profile of record

**Standard mature structure** — present in most modern products:

- curation containers (pathways, plans, channels, academies)
- skills layer (ratings, tagging, focus skills, target roles)
- AI-driven recommendation and personalization
- social/collaborative learning with expert contribution
- gamification
- assignment/required-learning machinery with manager surfaces
- engagement and skills analytics
- flow-of-work delivery (mobile, chat apps, capture extensions)
- scheduled sessions and events

**Variant / optional** — depends on packaging and deployment:

- full compliance and certification machinery (usually the LMS half of unified products)
- vendor-supplied curated content subscriptions
- extended-enterprise populations and branded academies
- credential ingestion and issuance
- multilingual and offline delivery

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Learner home

The primary entry surface, and the product's signature screen.

- personalized recommendations keyed to role, skills, and skill gaps
- assigned and required learning, deadlines
- featured and trending content, curated collections
- primary actions: start an item, follow a pathway, search

### Search and browse

- unified search across the whole ecosystem (internal, provider, and captured content)
- filtering by skill, topic, format, provider
- primary actions: find content, filter, save

### Content item card

The unit-of-consumption surface.

- title, source, format, duration, related skills
- primary actions: consume, mark complete, save, share, rate

### Pathway / collection page

- ordered or grouped items with required/optional marking and progress status
- following behavior: the pathway attaches to the learner's profile as items complete
- primary actions: follow, consume items, track progress

### Profile page

The learner's development record, visible to them (and, per the organization's rules, to managers).

- collection of completed learning across all sources
- skills and skill signals; achievements and points
- career view where configured (roles, targets, gaps)
- primary actions: add/remove skills, request or give ratings, review history

### Skills page

- the learner's skills, focus-skill selection, rating requests
- content suggestions per skill

### Groups and communities

- audience spaces mirroring org structure or interest areas
- shared content, discussions, questions and answers, expert contributions

### Assignments / required learning

- the overlay surface: what the organization has directed this person to learn
- primary actions: open assigned learning, complete, report a problem

### Manager view

- team members' activity, completions, and skills
- approval and validation steps; recommended learning to push

### Administration and curation console

- provider connections, content import, authoring tools
- pathway/academy building, audience targeting, assignment setup
- engagement and skills analytics

### Flow-of-work surfaces

- mobile app, chat-app integration, browser capture extension

## Important Rules / Behaviors

### Self-declared completion is legitimate evidence

For much of the ecosystem's content — an article, a video, a podcast — the learner marks the item complete themselves, and the platform accepts this as a record. Content owned by connected systems behaves differently — completions arrive as verified data from the source (course providers, LMS-hosted courses), and the learner is redirected to the source system to consume it. The two evidence classes coexist: breadth of self-directed learning on one side, system-of-record verification on the other.

### The profile accumulates and persists

Completed learning attaches to the person's profile and stays there across sources and time — this accumulation is what makes the profile a development record rather than a session log. It is also what makes recommendations and skill views meaningful: they are computed from the accumulated record.

### Curation containers have completion rules of their own

A curated collection completes when its required items are complete (optional items and visibility-scoped items excluded); the platform tracks progress toward that. Some products treat evolving collections as deliberately never "completable" — in those, following the collection can itself satisfy an assignment. Exact mechanics vary by product.

### The assignment overlay is real but secondary

Organizations do direct learning: assignments, required learning, HR-driven auto-enrollment, manager recommendations. But in this Type the directed flow rides on the same content ecosystem and profile as the self-directed flow — the learner follows the same pathways, consumes the same items, and their completions land in the same profile.

### Skills connect content to people — with configurable rigor

Skills are attached to content (increasingly by AI tagging) and to people (self-declared, validated, or rated by peers and managers, depending on what the organization enables). The configured rigor is an organizational choice, and recommendations follow from whatever standing exists.

### Content visibility is audience-scoped

Not all ecosystem content is visible to everyone; visibility follows group membership, role, audience targeting, and sometimes item-level curation decisions. This scoping is also the platform's governance surface for licensed provider content.

### Coexistence with the learning-management estate

The platform is designed to sit beside HR and learning-management systems, not to replace them: the population comes from HR/identity systems, and completions for externally hosted courses flow in from those systems. In pure-play deployments the LXP is therefore not the compliance system of record; in unified products the compliance machinery exists but is the LMS half of the same platform.

## Variants

- **Pure-play LXP** — standalone product centered entirely on the learner-experience core (discovery, ecosystem, profile, skills); typically deployed alongside an existing corporate LMS rather than replacing it.
- **Unified LMS + LXP platform** — one product carrying both the learner-experience surface and full learning-management machinery (enrollment, compliance, certifications); vendors in this packaging name and document LMS and LXP as distinct surfaces.
- **Suite-embedded LXP posture** — the experience layer shipped as named modules of a corporate learning suite (community, channels, content marketplace, gamification, skills) on top of the suite's LMS core.
- **Academies and branded portals** — curated, audience-specific instances (onboarding campuses, leadership academies) built from the same core.
- **Extended-enterprise LXP** — the same machinery pointed at customers, partners, or members instead of employees.
- **AI-era posture** — conversational AI companions, AI-curated libraries, AI authoring for subject-matter experts; an era-current layer across all packagings rather than a separate Type.

A variant remains a variant as long as the defining core — provisioned population, multi-source ecosystem, learner-directed loop over a per-person profile — still describes it.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Employee Learning Platform / Corporate LMS | deepest seam | same population and records machinery, opposite center of gravity: the LMS centers on organization-directed offerings, enrollments, completion records, and compliance evidence; the LXP centers on learner-directed discovery over an aggregated ecosystem and the development profile. Modern products blur the seam (unified platforms ship both; pure-play LXPs ingest LMS completions) — the boundary is flagged for joint review: research on that family read the LXP as a posture of it, while this research supports keeping both Types with an explicitly acknowledged overlap |
| LMS (education) | different frame | students, academic terms, grades and credit, institution-owned pedagogy vs workforce development profiles; the record's downstream consumer differs (transcript vs career/skills file) |
| MOOC Platform / Educational Content Platform | content-adjacent | public consumer enrollment in structured courses vs organization-provisioned populations with tracked development profiles; an LXP typically consumes MOOC-style content rather than being one |
| Skills Management Platform / Competency Management Platform | capability relationship | skills platforms hold assessed skill/competency standing as the record of record; the LXP holds learning activity and uses a skills layer for discovery and recommendations; gap data flows into the LXP as assignment and recommendation drivers |
| Content Curation Platform | superficially similar | curation for general audiences with no provisioned population, no per-person learning records, and no development loop |
| Customer Training / Academy Platform | audience variant | identical machinery pointed at customers/partners rather than employees; LXP posture can appear inside customer academies |
| Employee Experience Platform | domain relationship | EX platforms aggregate several workforce domains (learning among them); the LXP is the single-domain system whose outputs they may surface |
| eLearning Authoring Tool | capability relationship | authoring exists inside LXPs (often SME- and AI-assisted), but dedicated authoring tools center the authoring workflow itself |
| Digital Credential Platform | plumbing relationship | external credentials flow into profiles and completions may issue credentials; credentialing is not the LXP's center |

## Representative Products

- **Degreed** — pure-play, skills-first LXP for large enterprises; content items from connected providers and open web, pathways and plans, skills with ratings, assignments and required learning, points, AI-curated library
- **360Learning** — unified platform naming LMS and LXP as separate product surfaces; collaborative-learning pole (SME authoring, in-course forums, expert finder) plus skills profiles, target-job mapping, and aggregated content
- **Docebo** — corporate learning suite realizing the LXP posture as named modules (communities, channels, content marketplace, gamification, skills) on top of its LMS core

The defining core was checked against the suite-embedded packaging (Docebo) and the unified packaging (360Learning) to avoid over-fitting the Type to the pure-play implementation.

## Sources

Research date: **2026-09-08**

- Degreed — https://degreed.com/ (positioning; product line including "Degreed Learning (LXP)"); Degreed Knowledge Center — https://degreed.zendesk.com/hc/en-us (Product Guides: learner and admin sections; "Content, Pathway, and Plan Completions"; "Skills Overview"; "Assignments"; "Content Items")
- 360Learning — https://www.360learning.com/ and https://www.360learning.com/product/lxp/ (positioning; vendor LMS/LXP FAQ); 360Learning Knowledge Base — https://support.360learning.com/hc/en-us (Learn / Create / Share / Manage users / Manage groups / Manage skills / Track analytics)
- Docebo — Docebo Help & Support — https://help.docebo.com/ (platform packaging; "Communities and social learning" category: social learning, community hub, channels, playlists, gamification)

> Sourcing limitations: several LXP-pole products could not be reached from the research environment on 2026-09-08 (Fuse, Learn Amp; also Cornerstone's LXP line per the paired sibling research), so the social-collaboration pole and acquired-pure-play lineage are under-observed; 360Learning's help-center sub-pages were JS-rendered and its LXP feature detail is evidenced at product-page level. Claims in this document are calibrated to that evidence: precise numeric limits, latency figures, and product-specific completion mechanics observed in single products are kept in the paired Research Notes rather than asserted here.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.

