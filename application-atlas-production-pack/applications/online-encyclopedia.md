# Online Encyclopedia

## Overview

An **Online Encyclopedia** is a single reference work — a corpus of topical articles about subjects (people, places, events, concepts, works, fields) — published as an application. The user looks a subject up or browses to it, and reads a hosted article that the work's editorial process has authored, reviewed, and kept current.

The defining core is small:

```text
One named reference work (editorially governed, planned topical scope)
└── Topical article corpus (each article describes a subject)
    └── Subject-directed retrieval (lookup + systematic browse)
        └── Hosted article, consumed in place, kept current over time
```

Four properties. If any one is removed, the product is no longer recognizable as an encyclopedia:

- **Topical article corpus** — content is organized as articles about subjects, not entries per word, not links to elsewhere, not datasets.
- **One named work with a planned topical scope** — the article corpus is the whole product under one editorial identity; the work systematically aims to cover its subject domain (it may span language editions or reading levels without becoming several products).
- **Subject-directed retrieval into hosted articles** — search plus systematic navigation delivers an article as the unit of consumption, read inside the application.
- **Editorially governed, kept current** — articles are authored, reviewed, and revised under an editorial process accountable for the work, whether that process is a professional staff, scholarly editors and referees, or a governed contributor community.

Everything else commonly associated with modern encyclopedias — media libraries, quizzes, reading-level tiers, citation tools, AI answer features — is widespread but not part of the definition. Print-era works digitized, installed disc-era encyclopedias, regional and national encyclopedias, and community-edited ones all satisfy the same core.

## Users & Context

The primary user is any reader who needs trustworthy background knowledge about a subject:

- **students** building context for a topic and collecting citable background sources
- **general readers** checking a person, event, place, or concept they encountered in news, reading, or conversation
- **educators and librarians** steering learners toward a vetted starting point
- **professionals and researchers** orienting in an unfamiliar area of a field

The typical session is short and subject-driven: a question about a topic arises, the user searches or browses, reads one or a few articles, follows cross-references to related subjects, maybe cites or saves, and leaves. There is no transaction, no collaboration workspace, and no feed. The dominant surface is the web; institutional deployments (schools, libraries, universities) are a major access context, with personal consumer use alongside.

## Core Model

### The Defining Core

**The article is the unit of content.** An encyclopedia article describes a subject — its nature, history, context, and significance — in continuous prose organized for reference reading. This separates the encyclopedia from a dictionary (whose corpus is keyed to word forms and describes words, not subjects), from a portal (which points elsewhere), and from a data service (which distributes datasets).

**The work is the organizing frame.** The product is one encyclopedia: a named reference work with its own editorial identity and a planned, systematic topical scope — the work intends to cover its domain, which is why reference works maintain a planned topic list rather than publishing whatever arrives. A mature product may carry language editions or reading-level editions of the same work, and may wrap supplementary reference genres around it, but the encyclopedia remains the single managed object and the center of gravity. This is the sharpest boundary with a general reference database, whose managed object is a collection of many works.

**Retrieval is subject-directed and the article is hosted.** The user reaches an article by searching the work's titles and text, or by systematic navigation — alphabetical, thematic, or structured-table-of-contents browsing. The result is not a pointer to somewhere else; the article itself is presented and read inside the application. This separates the encyclopedia from a search engine (outbound references) and from a portal (routing out).

**An editorial process stands behind the corpus.** Articles are authored, reviewed, and revised under governance that is accountable for the work before publication and over its life. Who holds that governance varies — professional editors, scholarly editors and referees, or a contributor community operating under editorial policy — but the governance itself is constitutive: remove it and the product is an open posting site, not a reference work. Currency maintenance is part of the same leg: the corpus is kept current as the world it describes changes.

### What an Article Carries

Mature products structure articles consistently. Exact fields vary; this anatomy is conceptual:

- **Title and subject identity** — the article is individually addressable by its subject
- **Body prose** — the substantive description, commonly structured into sections with in-page navigation
- **Cross-references** — links to related articles; mature works cross-reference as new articles are added, so the corpus stays knit together
- **Attribution apparatus** — source references or bibliographies, and named authorship or editorial verification, because the work's authority depends on it
- **Revision metadata** — publication and revision information, so a reader can judge currency
- **Media** — images, maps, audio, video where the product's audience calls for them

### Standard Capabilities

Mature products commonly add, without these being part of the definition:

- **currency machinery** — continuous revision cycles, and in scholarly and citation-heavy contexts, fixed editions or archives so that a living article can still be cited stably
- **editorial-side contribution machinery** — commissioning, draft submission, review and refereeing, accept/reject decisions, revision tracking, and automatic cross-reference maintenance
- **access machinery** — institutional login, library card access, single sign-on, and learning-system integration in school and library deployments
- **audience apparatus** — reading-level editions of the same work, read-aloud, translation, age-appropriate interfaces
- **supplemental surfaces around the article corpus** — varying by product: media libraries, quizzes, day-in-history features, biographies verticals, educator collections
- **citation aids** — ready-made citation formats for entries

### One Structure, Many Implementations

```text
Concept:            Editorial governance
Implementations:    professional staff editors; scholarly editors and referees;
                    contributor community under editorial policy

Concept:            Currency
Implementations:    continuous revision; fixed periodic editions with archives;
                    edition-based releases

Concept:            Scope
Implementations:    general-purpose work; subject-specific work
                    (same structure, narrowed domain)

Concept:            Access
Implementations:    free (donation- or grant-funded); consumer free/paid split;
                    institutional license; subscription

Concept:            Delivery
Implementations:    web/cloud product; installed or disc-based legacy form;
                    platform-bundled editions
```

A reader who has only seen one implementation — say, a free community-edited encyclopedia — should still be able to recognize a subscription institutional school encyclopedia or a scholarly refereed work as the same Type.

## How It Works

### Look up a subject

```text
Enter a subject in the search box (or open a browse path:
alphabetical, thematic, or table of contents)
→ results present matching articles within the work
→ open an article
```

Search spans the work's own corpus — not the open web. Suggestions and alternate-title handling are common; the goal is to get from a subject in the reader's mind to the article about it.

### Read the article

```text
Article opens at its title
→ body sections, navigated in-page
→ media, references, and revision information alongside
→ follow cross-references to related articles
→ return to the starting point or continue outward
```

Chained reading through cross-references is a signature interaction: articles link to their related subjects, so one lookup can become a short associative path through the work.

### Cite what was read

Where the work supports citation, the article carries its attribution and revision data, and the product generates or exposes a citable form. In scholarly contexts this extends to fixed editions or archives that give a citation a stable target even though the article keeps changing.

### Maintain the work

Behind the reading surface runs the editorial loop that makes it a living reference work:

```text
Plan the topic list for the domain
→ commission or solicit an article for a topic
→ author drafts it
→ editors or referees review; revisions follow
→ publish the article
→ keep it current: revise in response to new knowledge
  and reader feedback; retire or update what falls behind
→ cross-reference new articles into the existing corpus
```

The shape of this loop varies by editorial model — a professional staff, a refereed scholarly community, or a contributor community with editorial policy — but planning, review, publication, and revision are common to the Type, and distinguish it from publishing that simply accepts whatever is submitted.

### Core vs Common vs Optional

**Defining core** — without these, not an encyclopedia:

- topical article corpus about subjects
- one named work with a planned topical scope
- subject-directed retrieval into hosted articles
- editorial governance with maintained currency

**Common in mature products, not definitional** — most modern products carry these, but none of them is what makes the product an encyclopedia:

- cross-references and related-article links
- attribution apparatus (references, authorship, revision metadata)
- citation aids; fixed editions or archives where citations matter
- institutional access machinery and learning-system integration
- media enrichment and audience-tier editions
- editorial-side commissioning, review, and revision machinery

**Variant / optional** — depends on model, market, and era:

- editorial governance holder (professional / scholarly / community)
- general vs subject-specific scope
- access economics (free, free/paid split, subscription, institutional)
- delivery medium (web, installed/disc legacy, platform-bundled)
- language editions; suite packaging with supplementary reference genres
- AI answer features over the corpus (era-current capability drift, not a new corpus)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Search & entry surface

The front door.

- a prominent search box scoped to the work; browse entry points alongside
- primary actions: search, open a browse path, reach today's or featured content where offered

### Results

- articles from the work matching the subject, commonly with title, snippet, and media thumbnail
- primary actions: open an article, refine the query

### Article page

The unit of consumption.

- title, body sections, in-page navigation, media, cross-references, references/attribution, revision information
- primary actions: read, follow a cross-reference, cite, share or save where offered, print or export where offered

### Browse navigation

- alphabetical, thematic, or structured table-of-contents paths over the planned topic space
- primary actions: move through the domain systematically rather than by query

### Access surface

In institutional deployments, the gate in front of the corpus.

- login with institutional credentials, library card, or platform sign-in
- primary actions: authenticate, restore access, reach the product

### Editorial-side surfaces

Where the editorial model exposes them (scholarly and community models typically do):

- author and editor workspaces for drafts, review, revision, and status tracking
- contributor discussion and policy surfaces

## Important Rules / Behaviors

### Publication follows editorial governance

Nothing enters the corpus as a finished article except through the work's editorial process — review, refereeing, or policy-governed community editing. Reader feedback flows back into that process (corrections, suggestions to authors or editors) rather than into direct editing of the record copy.

### The article is a living record, and citations must survive it

The corpus is revised over time; a well-run work gives readers a way to know what they are looking at (revision metadata) and, where citations matter, a stable target to cite (fixed editions or archives). The tension between "always current" and "stably citable" is a structural rule of the Type, solved differently by different products.

### Retrieval is bounded to the work

Search spans the encyclopedia's own corpus. Encyclopedias do not index the open web; extending search beyond the work is an optional bridging capability, and results from beyond the corpus remain visibly separate.

### The work is consulted, not owned

Access to the corpus is entitlement-based (open, licensed, or subscribed) with no lending semantics — no holds, loans, or returns around articles. Personal accounts, where offered, layer saving and preferences on top and do not gate the corpus itself in open or institutionally licensed deployments.

### Coverage is planned, not incidental

The work maintains a planned topical scope — an intended map of its domain — against which its coverage grows. This is what makes an encyclopedia systematic background knowledge rather than an accumulation of whatever content happens to arrive.

## Variants

- **Professionally staff-edited general encyclopedia** — a standing editorial team writes, updates, and verifies the corpus for a broad audience; consumer free/paid or subscription access.
- **Scholarly refereed encyclopedia** — subject experts author entries, editors referee before publication, authors maintain currency, and fixed editions serve citation; commonly open access funded by institutions and donations; typically subject-specific in scope.
- **Community-edited encyclopedia** — a contributor community under editorial policy maintains the corpus on a wiki-like substrate; free access.
- **School- and family-tiered encyclopedia** — the same work presented at graded reading levels with age-appropriate interfaces, media, and literacy supports; institutional (school/library) access with sign-on and learning-system integration.
- **Regional and national encyclopedias** — the same structure with a country- or region-defined scope.
- **Encyclopedia-led suites** — the encyclopedia at the center, wrapped with supplementary reference genres, media libraries, or educator tools under one product.
- **Historical forms** — digitized print editions and installed disc-era encyclopedias satisfy the same defining core; the web is the current delivery, not the definition.

## Related Application Types

| Application Type | Distinction |
|---|---|
| General Reference Database | aggregates and cross-searches **many** reference works at entry level; the encyclopedia is **one** work whose article corpus is the whole product |
| Dictionary Application | corpus keyed to word forms, entries describe words; encyclopedia's corpus is keyed to subjects, articles describe subjects |
| Wiki Application | open member editing of a shared page set is the point; an encyclopedia's frame is a published reference work under editorial governance — a wiki can host an encyclopedia, but the editorial-work frame, not the editing substrate, defines this Type |
| Answer Engine | composes or computes an answer at question time as the deliverable; the encyclopedia delivers pre-authored articles — an AI answer layer over an encyclopedia corpus is capability drift, not a different corpus |
| Knowledge Question Answering Application | grounded question-answering over an owner's knowledge base; deliverable is a composed answer, not the article |
| General Web Search Engine | returns outbound references to documents it does not host; the encyclopedia hosts and presents its own corpus |
| Knowledge Graph Explorer | exposes a traversable entity–relationship graph; the encyclopedia presents human-readable articles |
| Digital Library Platform | delivers whole works with loan/borrow semantics; the encyclopedia is consulted in place with no lending |
| Information Portal | gateway that routes outward and rotates ephemeral pointers; the encyclopedia is the content destination with stable article records |
| Expert Q&A Platform | produces an answer from an expert after a specific question; encyclopedia articles exist before any question |

The closest seam is the General Reference Database: products drift toward suites on both sides, and the deciding test is whether the product is one named work (encyclopedia) or a cross-searched collection of works (reference database). The second-most-important seam is the wiki boundary: when the editing substrate, not the published-work frame, defines the product, it belongs to Wiki Application.

## Representative Products

- **Encyclopædia Britannica** — the professional staff-edited general encyclopedia; continuously updated, fact-checked corpus for a broad audience
- **Stanford Encyclopedia of Philosophy** — the scholarly pole: expert-authored, refereed, citation-stable reference work, open access, subject-specific scope
- **Britannica School** — the school-tier pole: one encyclopedia at multiple reading levels with institutional access
- **World Book Online** — the K-12/family institutional pole, encyclopedia-led with a reference-center wrapper

The community-edited pole (exemplified by Wikipedia) is acknowledged as a major market realization; it could not be directly examined during research and no product-specific claims are made about it.

## Sources

Research date: **2026-09-08**

- Encyclopædia Britannica, Inc. — corporate site: https://corporate.britannica.com/
- Encyclopædia Britannica, Inc. — Britannica brand page: https://corporate.britannica.com/our-brands/brand-eb
- Britannica Education — Britannica School product page: https://britannicaeducation.com/solutions/prek-12/britannica-school/
- Stanford Encyclopedia of Philosophy — home page: https://plato.stanford.edu/
- Stanford Encyclopedia of Philosophy — About the SEP: https://plato.stanford.edu/about.html
- Stanford Encyclopedia of Philosophy — Editorial Information: https://plato.stanford.edu/info.html
- Stanford Encyclopedia of Philosophy — entry page (sample): https://plato.stanford.edu/entries/qualia/
- World Book, Inc. — World Book Online access page: https://www.worldbookonline.com/

> Sourcing limitation: the consumer encyclopedia sites for Britannica (britannica.com) and Wikipedia were not reachable from the research environment (403 / repeated timeouts), and The Canadian Encyclopedia returned 403. Evidence for the professional consumer pole is therefore positioning-level (corporate and product pages), the community-edited pole is treated as a market anchor only, and no precise operational details (access quotas, exact search behavior, interface specifics behind logins) are asserted anywhere in this document. Detailed observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
