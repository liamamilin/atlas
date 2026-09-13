# Research Notes — Online Encyclopedia

## Research Goal

Understand what an **Online Encyclopedia** actually is as an application type: its defining core, its content unit (the topical article), its retrieval and browsing model, its editorial machinery, and its boundaries with the neighboring reference/knowledge types — especially General Reference Database, Dictionary Application, Wiki Application, Answer Engine, and General Web Search Engine.

## Initial Boundary

Working hypothesis at start:

- It is a single reference work — a topical article corpus about subjects (people, places, events, concepts) — delivered as an application, retrieved by lookup and browse, maintained by an editorial process.
- Closest neighbors: General Reference Database (many works cross-searched), Dictionary Application (word-keyed entries), Wiki Application (open member editing), Answer Engine (composed answer as deliverable), Search Engine (outbound references).
- Main taxonomic tension: Wikipedia (community-edited, wiki-substrate) vs Britannica (professional editorial). The definition must hold across both poles.
- Known directory context: the leaf sits in 02.05 Reference & General Knowledge, next to General Reference Database, Dictionary Application, Knowledge Graph Explorer.

## Research Questions

1. What is the unit of content, and what makes a topical article different from a dictionary entry or a database record?
2. Is the product one reference work or a collection of works? How is the single-work identity expressed (language editions, reading levels, supplements)?
3. How is the corpus organized and navigated (search, alphabetical, thematic/TOC, categories)?
4. What does the article contain (anatomy), and what metadata travels with it (authorship, revision dates, citation, archival editions)?
5. What is the editorial model, and what machinery maintains currency (commissioning, review, revision, versioning/archives)?
6. Who uses it and in what context? What access models exist (free, subscription, institutional)?
7. Where are the boundaries with each neighbor type, and what "remove" test separates them?
8. Would older / regional / community-edited / subject-specific forms still satisfy the definition?

## Representative Products

| Product | Pole | Evidence status |
|---|---|---|
| Encyclopædia Britannica (corporate + brand pages; consumer site 403) | professional staff-edited, general audience, freemium | Tier 2 fetched (corporate.britannica.com) |
| Stanford Encyclopedia of Philosophy (SEP) | scholarly, expert-authored, open access, subject-specific | Tier 1 fetched (home, about, editorial info, one entry) |
| Britannica School (Britannica Education) | K-12 institutional, leveled editions | Tier 2 fetched (product page) |
| World Book Online | K-12/family institutional encyclopedia-led suite | Tier 2 fetched (access gate only) |
| Wikipedia | community-edited, wiki-substrate, free | **unreachable (timed out twice) — market anchor only, no product-specific claims** |
| The Canadian Encyclopedia | regional/national pole | 403 — dropped |

Sampling rationale: four directly evidenced products cover three distinct editorial philosophies (professional staff, scholarly expert-volunteer, K-12 institutional verification) and multiple customer tiers (consumer free/paid, school, library, academic). Wikipedia covers the community pole as an anchor. This follows the §21 anti-overfitting concern: no single editorial model is baked into the definition.

## Sources

Fetched 2026-09-08:

- Britannica corporate site: https://corporate.britannica.com/ (root)
- Britannica brand page: https://corporate.britannica.com/our-brands/brand-eb
- Britannica School product page: https://britannicaeducation.com/solutions/prek-12/britannica-school/
- SEP home: https://plato.stanford.edu/
- SEP About: https://plato.stanford.edu/about.html
- SEP Editorial Information: https://plato.stanford.edu/info.html
- SEP entry (Qualia): https://plato.stanford.edu/entries/qualia/
- World Book Online access gate: https://www.worldbookonline.com/

Unreachable / abandoned (per network rules):

- https://en.wikipedia.org/wiki/Wikipedia:About — timed out twice → market anchor only
- https://www.britannica.com/ — 403 (whole consumer domain) → consumer-site behavior not directly observed
- https://www.thecanadianencyclopedia.ca/en — 403 → regional pole not directly observed
- https://plato.stanford.edu/entries/zombie/ — 404 (bad slug, replaced by /entries/qualia/)

Prior relevant research in this repo (for boundary consistency, not as product evidence):

- applications/general-reference-database.md + research/general-reference-database.md (explicit seam: "an encyclopedia is one reference work — its article corpus is the whole product")
- applications/dictionary-application.md (seam: topical articles vs lexical entries)
- STATUS.md entries: answer-engine, knowledge-question-answering-application, expert-q-a-platform, information-portal (seam language)
- research/knowledge-graph-explorer.md (seam: articles vs traversable statement graph)

## Product Observations

### Encyclopædia Britannica (corporate + brand pages) — evidence layer A (positioning-level)

- Self-description (brand page): "a dynamic, continuously updated, rigorously fact-checked information source for students, teachers, and lifelong learners."
- Editorial model directly stated: "Every year, Britannica's worldwide team of editors and contributors write, update, and revise tens of thousands of articles."
- Professional identity reinforced by a "Distinguished Contributors" roster (named public figures, academics) and institutional partners (universities, societies, national encyclopedia).
- Content-surface extensions surfaced on the corporate page: Biographies, Videos, Quizzes, "On This Day" — supplementary browsing surfaces around the article corpus.
- Scale claims: 7B+ page views annually, 150+ countries, 150M+ students, 20+ languages offered (marketing figures — recorded, not relied on).
- Consumer site (britannica.com) itself was unreachable (403): free/subscription split, article-page anatomy, and search behavior of the consumer product were NOT directly observed. No claims made at that precision.

### Stanford Encyclopedia of Philosophy — evidence layer A (operational documentation, richest source)

From the home page:

- Self-definition: "organizes scholars from around the world in philosophy and related disciplines to create and maintain an up-to-date reference work."
- Editorial governance: Co-Principal Editors, Editorial Board, Editorial Information, "How to Cite the SEP."
- Browse surfaces: Table of Contents, What's New, Random Entry, Chronological, Archives; plus a search box ("Search Tips").
- Institutional support model: SEPIA for Libraries (academic library membership); ISSN + Library of Congress catalog data — it is a cataloged serial reference work.
- Mirror sites at universities worldwide.

From About:

- "As of Summer 2023, has nearly 1800 entries online" — one work, one entry set.
- "Each entry is maintained and kept up-to-date by an expert or group of experts in the field. All entries and substantive updates are refereed by the members of a distinguished Editorial Board before they are made public."
- "Our dynamic reference work maintains academic standards while evolving and adapting in response to new research."
- **Fixed editions for citation**: "You can cite fixed editions that are created on a quarterly basis and stored in our Archives (every entry contains a link to its complete archival history, identifying the fixed edition the reader should cite)."
- **Planned topical coverage**: "The Table of Contents lists entries that are published or assigned. The Projected Table of Contents also lists entries which are currently unassigned but nevertheless projected."
- Publishing model machinery (all directly documented): password-protected author interface (templates, private draft submission, remote revisions); subject-editor interface (add topics, commission, referee, accept/reject, side-by-side diff view of original vs updated); principal-editor administrative interface (add people/entries, assign, invite, track deadlines, publish); a tracking system logging actions, monitoring every entry's state, deadlines, automatic reminders; software that **dynamically cross-references the SEP when new entries are published** and checks for broken links; **automatic quarterly archives as the basis for scholarly citation**; mirrors.
- **Explicit self-distinction from journals** (their own argument, valuable for the Type definition): journals (1) don't update published articles, (2) "do not aim to publish articles on a comprehensive set of topics," (3) don't cross-reference concepts across articles, (4) serve narrow specialists, (5) publish on a synchronized schedule rather than maintaining asynchronous per-entry update cycles. An encyclopedia is the opposite on all five.
- Also distinguished from subscription-gated resources ("costly and behind a subscription wall") and from projects "lack[ing] a system of archives for stable, scholarly citation."

From Editorial Information (policies):

- Contributions "normally solicited by invitation from a member of the Editorial Board"; unsolicited pre-proposals judged by qualification (accredited PhD + refereed works on the topic) and fit to the planned topic list.
- "All entries, whether solicited or approved, will be refereed by one or more of the subject editors... or by one or more external referees."
- Readers "are encouraged to contact authors directly with comments, corrections, and other suggestions."
- Authors "remain responsible to maintain their entries and to keep them current," updating bibliographies; entries not revised within a negotiated timetable "may be retired from the active portion of the Encyclopedia and left in the Encyclopedia Archives."
- Publication ethics adopted from journal-editor codes; corrections/clarifications published in a timely way.
- Copyright: authors retain copyright, license publication to the Lab; Terms of Use grant users read/download/print/link rights with distribution limits; open access (no charge to authors or readers).

From the entry page (Qualia) — canonical article anatomy, directly observed:

- Title; publication line: "First published Wed Aug 20, 1997; substantive revision Fri Sep 19, 2025" — per-entry revision metadata.
- Entry Contents table (numbered sections), in-page anchor navigation.
- Bibliography section; Academic Tools; Other Internet Resources; **Related Entries** (cross-references to sibling entries).
- "Author and Citation Info" link (per-entry authorship and citation data); "Back to Top"; Entry Navigation.
- Long-form scholarly prose authored by named experts.

### Britannica School (Britannica Education product page) — evidence layer A (product positioning)

- One product, one encyclopedia, four **reading levels**: Early Elementary (PreK–2), Elementary (3–5), Middle (6–8), High (9–12) — "Its four levels are tailored to age, ability, and curiosity, with unique interfaces and tools."
- Corpus claims: "139,000+ fact-checked articles," "136,000+ images, videos, and audio clips," "100+ interactive experiences."
- Editorial verification: "curriculum-aligned content verified by Britannica's expert editorial team"; "Every fact is verified."
- Supports: audio read-aloud, translation, adjustable reading levels; SSO + LMS compatibility; statewide access; educator collections/lessons around the article corpus.
- Marketing framing "more than a digital encyclopedia, it's a living learning platform" — suite drift acknowledged; the encyclopedia article corpus remains the core asset.

### World Book Online (access gate) — evidence layer A (limited: gate only)

- Page title self-identifies: "World Book Online Reference Center | Online Reference Book | Online Encyclopedia"; description: "Core reference collections; documents, selections, online reference books in major subject areas."
- Institutional access machinery directly observed: Login ID/Password, Google sign-in, "Enter library card or bar code number."
- School-ecosystem integrations displayed: Clever, Classlink, Canvas, Schoology, G Suite.
- Audience claim: "an engaging, verified, and trustworthy digital resource for grades pre-K through high school."
- Interior (article pages, search behavior) behind login — not observed. Note: the "reference center" wording shows suite drift (encyclopedia-led work plus supplementary reference works); the encyclopedia remains the named center. Same pattern as Britannica Academic in the General Reference Database research.

### Wikipedia — market anchor, evidence layer C only (unreachable)

- Planned anchor for the community-edited pole; timed out twice and was abandoned per the network rule.
- No product-specific claims are made about it in either output file. It is referenced only as the well-known realization of the community pole (an encyclopedia maintained by a contributor community under editorial policies on a wiki substrate), a status that requires no precise operational detail.
- Cross-check of precedent: research/metasearch-engine.md handled the same situation by reasoning structurally and not citing Wikipedia.

## Cross-product Comparison

| Dimension | Britannica | SEP | Britannica School | World Book | Wikipedia (anchor) |
|---|---|---|---|---|---|
| Unit of content | topical article | topical entry (scholarly article) | topical article (leveled) | topical article | topical article |
| One named work | yes (Encyclopædia Britannica) | yes (SEP, ISSN-cataloged) | yes (one work, four levels) | yes (World Book encyclopedia + reference-center wrapper) | yes (one project, language editions) |
| Editorial process | professional staff + contributors; "fact-checked," continuously revised | expert authors; refereed by Editorial Board before publication; authors maintain currency | "verified by expert editorial team" | "verified" | community editorial governance |
| Retrieval | search + browsable verticals (biographies, etc.) | search + TOC + chronological + random + archives | level interfaces + navigation | login-gated interior (not observed) | search + categories |
| Article anatomy | (consumer page not observed) | title, author, pub/revision dates, TOC, bibliography, related entries, citation info | articles + media + read-aloud/translation | not observed | citations, revision history |
| Versioning | "continuously updated" | quarterly fixed archival editions + per-entry revision history | continuous | not observed | continuous revision |
| Access | free/paid consumer poles | open access, donation/library-funded | institutional (school/state), SSO/LMS | institutional (login/card) | free |
| Media richness | videos, quizzes, images | text-centric scholarly prose | images/video/audio, interactives | not observed | images/media |
| Supplements around the work | biographies vertical, quizzes, On This Day | PDF editions, mirrors | educator collections, assessments | reference-center wrapper | (not asserted) |

Cross-product commonalities (layer B) that hold across all directly evidenced products:

1. Topical article as the unit — every product's content is organized as articles about subjects, not word entries, links, or datasets.
2. One named editorial work — every product is one encyclopedia (with levels/editions/supplements), not a multi-work aggregation.
3. Editorial accountability before/at publication and ongoing revision — professional staff (EB), refereed scholarly editors (SEP), verified-by-team (School/World Book); revision and currency maintenance are explicit in every directly observed self-description.
4. Subject-directed retrieval into hosted articles — search and systematic browse paths; the article is consumed in place.
5. Article-level extras cluster around the same anatomy: cross-references/related entries, bibliographic/attribution apparatus, revision metadata.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (jointly-held; each leg's remove-test)

1. **Topical article corpus about subjects** — persistent, individually addressable articles, each describing a subject (person, place, event, concept, work, field). Remove → word-keyed corpus = Dictionary Application; link-pointing surface = portal/directory; dataset distribution = data portal.
2. **One named reference work with a planned topical scope** — the product is a single editorially coherent encyclopedia whose article corpus is the whole product; the work has an identity (name, editorial authority), a defined subject domain it systematically aims to cover, and may span language editions or reading levels without becoming multiple products. Remove (many works under one search) → General Reference Database; (no work identity / no planned scope) → blog or content farm.
3. **Subject-directed retrieval into hosted articles** — lookup (search over the work's titles/text) plus systematic navigation (alphabetical/thematic/structured) delivers an article as the unit of consumption, read in place inside the application. Remove (results are outbound references) → search engine; (content not hosted) → portal.
4. **Editorially governed compilation with maintained currency** — articles are authored, reviewed, and revised under an editorial process accountable for the work (professional staff, scholarly editors and referees, or community editorial governance), with the corpus kept current over the work's life. Remove (unreviewed open posting) → UGC community/Q&A territory; (frozen unmanaged text) → static archive/document dump.

Jointly-held is load-bearing:

- 1 alone (no single work) = aggregated topical content platform / Q&A archive.
- 2 without 1+4 = a named publication with no reference-work structure (magazine).
- 3 without 1+2 = search engine.
- 4 without 1+2 = editorially governed journal (SEP's own contrast).
- 1+2 without 3 = book dump without a finding apparatus.
- 1+3 without 2+4 = cross-work topical corpus = General Reference Database.
- 2+3 without 1 = empty navigation shell.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Article anatomy beyond the body: cross-references/"related entries," bibliographies/source references, images and media, revision/publication metadata, citation aids.
- Enriched retrieval: search suggestions, within-work scoped results, A–Z and categorical browse, random-article discovery.
- Currency machinery: continuous revision cycles or fixed editions/archives for stable citation (SEP quarterly archives; Britannica continuous updates — both observed as different solutions to the same requirement of citing a living work).
- Contribution machinery on the editorial side: commissioning, drafts, review/refereeing, accept/reject, revision tracking, deadlines, cross-reference generation (SEP documents the full pipeline).
- Reader-side collection: none dominant in the sample (SEP offers nothing personal; institutional products put saving behind My Research–style accounts — World Book gate mentions a "My Research account"). Held as optional institutional-layer capability, not definitional.
- Access machinery: institutional login, library card, SSO, LMS/Clever-class integrations, statewide licenses (observed on School + World Book).
- Supplements around the work: media libraries, quizzes, "On This Day," biographies verticals, educator collections.

### L2 — Variant / Optional Structure

- Editorial model: professional staff-edited / expert-authored-refereed / community-edited.
- Scope: general-purpose vs subject-specific (SEP = philosophy; the structure is identical with a narrowed domain).
- Audience tier: general adult vs school-leveled editions (four reading levels in one product) vs scholarly.
- Access economics: free with donation funding, free/paid consumer split, institutional licensing, subscription.
- Delivery medium: web/cloud (current), installed/disc (CD-ROM-era historical form), platform-bundled.
- Language editions (one project, many languages).
- Suite packaging: encyclopedia-led products that wrap supplementary reference works or learning tools around the article corpus (World Book Reference Center, Britannica School's educator layer, Britannica Academic's bundle).

### L3 — Vendor-specific (research notes only)

- SEP: ISSN/Library of Congress cataloging, university mirror network, SEPIA library fund, Friends-of-SEP PDF editions, the exact diff-view referee tooling, "How to Cite" page.
- Britannica: Distinguished Contributors program, On This Day/Quizzes verticals, corporate scale metrics, state-access program.
- World Book: specific LMS/integration vendor list, My Research account naming.
- Britannica School: exact article/media counts, four named level bands.

## Historical / Market-Sample Check

- **Print-era encyclopedias digitized** (e.g., archived historic editions): satisfy all four L0 legs — topical articles, one named work with planned scope, alphabetical/lookup retrieval, editorial compilation. Delivery-medium recency is not in the core.
- **CD-ROM-era encyclopedias** (installed products of the 1990s, e.g., the well-known consumer encyclopedias of that era): satisfy the core on a non-networked medium; "online" describes the current dominant delivery, not the structure. This mirrors how the repo handled CD-ROM-era reference collections.
- **Regional/national encyclopedias** (a national biography or country encyclopedia): satisfy — scope variant, same structure. (Canadian Encyclopedia 403 — reasoned, not cited.)
- **Community-edited pole** (Wikipedia): satisfies if the community's editorial governance (policies, review, reversion) counts as the editorial process — it does under the abstraction "editorially governed"; the governance holder is a variant.
- **Leveled/school editions**: one work at multiple reading levels — the work identity holds; levels are editions, not separate works.
- Conclusion: the definition survives era, region, medium, and editorial-model variation. The one era-bound temptation — "continuously updated" — is deliberately NOT definitional (edition/archival model satisfies; continuous revision is a common modern posture).

## Vendor-specific Findings

See L3 above. None promoted to the canonical document beyond neutral, name-free capability examples.

## Boundary Findings

- **vs General Reference Database** — sharpest seam. Encyclopedia = ONE work; its article corpus is the whole product. Reference database = a corpus of MANY works cross-searched at entry level with per-entry source-work attribution. Remove the single-work leg → reference database. Suite drift is real in both directions (Britannica Academic bundles thesaurus/world data/atlas and was classified there as encyclopedia-led suite; World Book's "Reference Center" wrapper shows the same from this side). The center-of-gravity test decides: encyclopedia-led vs corpus-led.
- **vs Dictionary Application** — topical article about a subject vs lexical entry keyed to a word form. Same lookup-box interaction, different corpus organization and content type.
- **vs Wiki Application** — a wiki substrate can host an encyclopedia (the community pole), but the Type-defining frame is the published reference work under editorial governance with planned topical scope, not open member editing of a shared page set. A wiki whose pages are not held to reference-work editorial governance and topical-scope planning is a Wiki Application. JOINT REVIEW recommended when wiki-application is processed (see Boundary Issues).
- **vs Answer Engine / Knowledge Question Answering Application** — encyclopedia's deliverable is the existing article (browse/lookup-first); answer engines compose/select an answer at question time as the deliverable. An AI answer layer over an encyclopedia corpus is capability drift, not a different corpus (parallel to the reference-database doc's wording).
- **vs General Web Search Engine** — encyclopedia hosts and presents its own corpus; a search engine returns outbound references to documents it does not host. (The search-engine doc already uses "the product is an encyclopedia" as its own negative test.)
- **vs Knowledge Graph Explorer** — human-readable articles vs traversable typed entity-relation graph; structured-data siblings (e.g., Wikidata-class resources) belong to the graph side.
- **vs Digital Library Platform / Web Archive Viewer** — a living maintained work consulted in place vs whole-work lending/borrowing or static archived page snapshots; no loan semantics and no frozen-page frame here (the fixed-edition archive serves citation stability, not archival display).
- **vs Expert Q&A / Q&A Community** — pre-authored articles exist before the question; Q&A produces an answer after the question.
- **vs Information Portal** — portal routes outward and rotates ephemeral pointers; encyclopedia is the content destination with a stable article record.

## Uncertainties

1. Wikipedia (community pole) not directly evidenced — the community-edited form enters the definition only as a reasoned anchor; no operational claims (edit mechanics, policy names, quotas) are made anywhere.
2. Consumer britannica.com unreachable — consumer-pole article anatomy, free/paid gating, and search UX are not asserted; Britannica evidence is positioning-level (corporate/brand/product pages).
3. World Book interior behind login — only the access gate is evidenced; no interior behavior claims.
4. Whether reading-level tiers should count as one work or several — decided as one work with levels (Britannica School presents itself as one product with four levels); residual risk noted.
5. Reader-side personal features (saving, annotations) are weakly evidenced (one gate mention of a "My Research account") — kept out of standard-capability claims except as institutional-layer option.
6. AI answer layers over encyclopedia corpora are era-expected but were not observed in fetched sources — deliberately not claimed.

## Final Synthesis

An Online Encyclopedia is best modeled as **one editorially governed, systematically planned reference work whose whole product is a corpus of topical articles about subjects, retrieved by subject-directed lookup and browsing and consumed as hosted articles kept current over the work's life**. The four L0 legs (topical article corpus · single named work with planned scope · subject-directed retrieval into hosted articles · editorial governance with maintained currency) are jointly-held and each passes its remove-test against a named neighbor Type. Editorial model (professional/refereed/community), scope (general/subject), audience tier (general/school/scholarly), access economics, delivery medium, and language editions are variants. Currency machinery — continuous revision or fixed citation editions — is the mature layer's most distinctive capability and is deliberately NOT definitional. The sharpest boundary is with the General Reference Database (one work vs many); the wiki seam (community-edited encyclopedias) is resolved by placing editorial governance and work identity, not the editing substrate, inside the definition; JOINT REVIEW with wiki-application recommended.
