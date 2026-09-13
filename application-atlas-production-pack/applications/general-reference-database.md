# General Reference Database

## Overview

A **General Reference Database** is a curated, searchable collection of multiple reference works — encyclopedias, dictionaries, handbooks, directories, quotation collections, atlases, almanacs — consulted entry by entry. Its purpose is consultation: a student, librarian, or general reader looks something up, retrieves the relevant entry or article, and takes away a citable unit of background knowledge tied to its named source work.

The defining core is small:

```text
Curated corpus of multiple reference works
└── Cross-work lookup (one search or browse path spans the corpus)
    └── Entry-level retrieval
        └── Source attribution (every entry belongs to a named, citable work)
```

Three properties distinguish the Type. The corpus holds **many** works, not one — otherwise the product is a single encyclopedia or dictionary. Retrieval returns **entries**, not whole works — otherwise the product is an eBook library. And every retrieved entry is **attributed to its source work** — otherwise it is an unattributable content index rather than a reference source. "Database" here is the library sense — a database *of reference material* — not a structured-data query system: the content is editorial prose, not tables or datasets.

## Users & Context

Primary users are people who need trustworthy background context rather than open-web results:

- **students** (school through university) starting a research project, building vocabulary of a topic, or collecting citable sources
- **librarians and library staff** assisting patrons, building research guides, and steering users toward vetted sources
- **general readers and patrons** in public libraries looking up a person, place, event, term, or quotation
- **educators** assembling course readings and pointing students at reference entries

The dominant context is institutional: a school, university, or public library licenses the database, and users reach it through that institution — a library card number, an access code, a campus sign-in, or an on-site network. A personal account, where offered, is for saving and organizing what one finds, not for owning access to the corpus. The typical session is short and task-driven: search, skim a few entries from different works, save or cite, leave.

## Core Model

### The Defining Core

**The work is the organizing unit of the corpus.** A reference database manages a collection of distinct reference works, each with its own title, publisher, and editorial identity. The works are heterogeneous by design — an encyclopedia article, a dictionary definition, a handbook chapter, a directory listing, a quotation, a map plate can all sit in one corpus. The mix is the point: different genres of reference authority answer different kinds of questions about the same topic.

**The entry is the unit of retrieval.** Users never check out or download a work as a whole; they retrieve the entry, article, or chapter that answers their question. An entry typically carries its headword or title, its body text, sometimes images or media, and — structurally essential — its source: which work it comes from, with the publication details needed to evaluate and cite it.

**Cross-work lookup is the signature interaction.** One search box, or one subject-browse path, spans the entire corpus. A query about a topic returns matching entries from many works side by side, so the user can compare how a specialized handbook, a general encyclopedia, and a dictionary each treat the subject. Faceted refinement — narrowing by subject, by work or title, by publication type, by era — is the common way to tame a broad corpus.

**Attribution closes the loop.** Because every entry is bound to its named source work, the database doubles as a citation source: mature products generate ready-made citations and export them to citation managers. This is what separates a reference database from an unattributable content aggregator.

### Standard Capabilities

Mature products commonly add, without these being part of the definition:

- **subject browse and A–Z indexes** alongside search, organized by discipline or alphabet
- **entry-page cross-references** — related entries, "see also" links, associated images and media
- **citation generation and export** to citation managers
- **personal collecting** — saved entries, folders, or resource packs under a personal account
- **sharing and export** — persistent links to entries or searches, email, PDF download, printing
- **accessibility support** — text-to-speech, translation, adjustable display
- **institutional access machinery** — library card or barcode login, access codes, single sign-on, network access
- **learning-system integration** — embedding into LMS platforms and indexing by library discovery services; MARC records for library catalogs
- **institution-side administration** — collection curation, usage reporting
- **reading-level or audience tiering** — the same corpus presented at different levels for different grades or patron groups

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Corpus ownership
Implementations:    a publisher's own works; an aggregation of many
                    publishers' works; titles an institution purchased
                    and hosts on the platform

Concept:            Entry form
Implementations:    born-digital web entries; faithful page images of
                    the printed work; both views over the same content

Concept:            Access
Implementations:    free web; institutional subscription; one-time
                    purchase with ongoing hosting; personal subscription
```

A reader who has only seen one implementation — say, a school's subscription database — should still be able to recognize a free web reference shelf or a CD-ROM-era bundled reference collection as the same Type.

## How It Works

### Look up a topic across the corpus

```text
Enter a search term (or open a subject or A–Z browse path)
→ the database returns matching entries from many works
→ refine with facets (subject, work, publication type, era)
→ open an entry
→ read it with its source work and citation visible
→ follow cross-references to related entries
```

This is the loop the whole product exists to serve. The result list is deliberately multi-work: seeing which works cover a topic is itself part of the answer.

### Take the entry away

```text
Open an entry
→ generate or copy its citation
→ save it to a personal collection, or export it
→ share a persistent link, download, or print it
```

Citation and export are first-class steps, not afterthoughts — the entry is meant to flow into a paper, a lesson, or a research guide.

### Explore associatively

Some products add visual or associative aids: a concept map that branches from one topic to related terms, or a tile view that clusters results into themes. These support the exploratory phase of research, when the user does not yet know the right terms.

### The institution curates; the publisher maintains

Two ongoing processes run behind the user-facing loop. The **publisher (or aggregator)** compiles, updates, and versions the works — users read entries but do not edit them. The **institution** shapes its instance: which works are in the collection, how they are organized and presented, and — in hosting-platform models — which purchased titles appear on which shelves. Usage reporting feeds renewal decisions.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Search & results

The primary entry surface.

- a prominent search box spanning the corpus; browse paths by subject and A–Z alongside
- a results list of entries from multiple works, each showing its source work
- primary actions: search, filter by facet, open an entry

### Entry / article page

The unit of consumption.

- headword or title, body text, images or media, cross-references to related entries
- the source work and its publication details, with citation output
- primary actions: read, follow a cross-reference, cite, save, share, print or download

### Work / title page

The corpus-browsing surface.

- a work's cover or title, its table of contents or entry structure, and its publication details
- primary actions: open the work and read within it, search within it, view its citation

### Personal collection

The user's saved workspace, where offered.

- saved entries or resource packs, organized for a project or course
- primary actions: save, organize, export, share

### Institution console

The staff surface, in institutional deployments.

- the collection: which works are present, how they are shelved or grouped
- usage and administration views
- primary actions: curate collections, review usage, manage settings

## Important Rules / Behaviors

### Consultation, not lending

Reference entries are consulted, not checked out. The researched products show no holds, queues, or loan periods around entries; access is entitlement-based — if your institution subscribes, you can consult the corpus along with everyone else at once. One researched product states this explicitly (unlimited simultaneous access, no holds or returns); the others show no lending semantics anywhere in their documented behavior.

### Entries are editorial artifacts

Users read entries; they do not edit them. Content is authored, reviewed, and updated by the publisher or aggregator. The user's writes are confined to their own layer: annotations, saved items, citations. In at least one researched product, in-platform annotations are session-scoped and persist only if exported — a reminder that the durable user data lives in exports and personal collections, not in the corpus.

### Attribution is structural

An entry without its source work is not a finished unit. Citation data travels with the entry — into exports, downloads, and citation managers — because the authority of the answer is inseparable from the work it came from.

### Access is mediated by the institution

In the dominant deployment, the right to consult comes from a library card, access code, campus sign-in, or institutional network — not from an individual purchase. Personal accounts layer saving and sharing on top; they do not confer corpus access by themselves. Free-web and personal-subscription models exist as variants.

### The corpus is bounded — and sometimes bridged

Search normally spans the licensed corpus, not the open web. Some products extend search beyond the corpus into the library's other databases (federated search); the results remain separated by source. AI answer features, where present, are documented as drawing only on the vetted corpus and returning linked, citable entries — the corpus remains the authority.

## Variants

- **Single-publisher reference suite** — one publisher bundles its own works (encyclopedia, dictionary, thesaurus, atlas, timelines) under one search; the encyclopedia often remains the center of gravity.
- **Multi-publisher aggregator** — the vendor licenses reference works from many publishers and cross-searches them as one corpus; breadth and neutrality of sourcing are the selling points.
- **Hosting platform for institution-owned titles** — the institution purchases reference and nonfiction works and hosts them on the vendor's platform, curating its own collection; ownership (with a hosting fee) replaces subscription.
- **Audience tiers** — academic libraries, K-12 schools (with grade-level corpus tiers), public libraries, and family/consumer editions of the same structure.
- **Scope variants** — the canonical corpus is general/multidisciplinary; subject-specific reference collections (history, health, literature, science) share the identical structure with a narrowed corpus.
- **Access economics** — free web, institutional subscription, purchase-plus-hosting, personal subscription.
- **Era-typical additions** — AI answer layers over the corpus; federated search into the library's wider holdings; rich accessibility stacks.
- **Historical form** — bundled reference collections on physical media (CD-ROM-era "bookshelves" of dictionary + thesaurus + encyclopedia + almanac + quotations + atlas) satisfy the same defining structure; the Type long predates its current cloud packaging.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Online Encyclopedia | one reference work's article corpus is the whole product; a reference database aggregates and cross-searches many works |
| Dictionary Application | lexical entries looked up by word form; a reference database holds topical entries across genres, dictionaries being one work type among several |
| Knowledge Graph Explorer | entities and relations traversed as a graph; here the object is documents (entries) retrieved and read |
| Digital Library Platform | delivers whole works for reading/borrowing, with loan semantics; a reference database delivers entries for consultation — the unit of delivery is the discriminator |
| Academic Search Engine | indexes periodical literature (journal articles, papers); a reference database holds editorial reference works |
| Public Data Portal | distributes datasets and statistics files; a reference database holds editorial prose entries (its "world data" pages are entries *about* data, not data services) |
| Information Portal / Directory Application | links out to external resources; a reference database holds the content itself |
| Answer Engine | synthesizes responses to questions; a reference database returns existing editorial entries — an AI answer layer on a reference corpus is capability drift, not a different corpus |

The closest seam is the eBook-platform pole: a hosting platform whose interaction is chapter-level cross-search, subject indexing, and citation export behaves as a reference database even when marketed as an eBook library; whole-work lending with holds would make it a digital library.

## Representative Products

- **Gale eBooks** (Gale, a Cengage company) — institution-owned reference/nonfiction eBook platform; chapter-level cross-search, dual page-image/text views, collection curation
- **Credo Reference** (Infobase) — multi-publisher general reference aggregator positioned as a research starting point, with concept-map exploration and federated search
- **Britannica Academic** (Britannica Education) — single-publisher higher-education reference suite bundling encyclopedia, thesaurus, world data, timelines, atlas, and primary sources
- **World Book Online** (World Book Inc.) — school/family reference center reached by library card or school sign-in, tiered for grades pre-K through high school

Oxford Reference (Oxford University Press) is the canonical named example of the single-publisher multi-work pole; its site could not be reached during research, so no product-specific claims are made about it.

## Sources

Research date: **2026-09-07**

- Gale — Gale eBooks product page: https://www.gale.com/ebooks
- Gale — Gale 101: Gale eBooks (official training webinar transcript): https://support.gale.com/doc/ebook-101
- Gale — Gale eBooks training materials index: https://support.gale.com/training/products/gvrl
- Infobase — Credo Reference product page: https://infobase.com/solution/credo/credo-reference/
- Britannica Education — Britannica Academic product page: https://britannicaeducation.com/solutions/higher-ed/britannica-academic/
- Britannica — Britannica Academic access gate: https://academic.eb.com/
- World Book — World Book Online access page: https://www.worldbookonline.com/

> Sourcing limitation: several candidate products (Oxford Reference, Credo's own platform, Encyclopedia.com, Infoplease, Bartleby, TheFreeDictionary, World Book's marketing site) were unreachable from the research environment. Britannica Academic's in-platform behavior sits behind an institutional access gate, and World Book evidence is limited to its public access surface. Claims about those products are kept at positioning level; precise operational details (corpus sizes, language counts, timeout values, plan limits) are intentionally not stated in this document and remain, where observed, in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
