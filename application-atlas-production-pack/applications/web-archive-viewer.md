# Web Archive Viewer

## Overview

A **Web Archive Viewer** is an application for locating, selecting, and viewing stored captures of web pages as they existed at past points in time — rather than the live web.

Where a web browser answers "what does this page say now?", a Web Archive Viewer answers "what did this page say at a chosen moment in the past, and what did it look like?". The application holds — or connects to — an archive of frozen copies of web resources, lets the user pick among those copies in the time dimension, and presents the chosen copy as a readable page.

The defining core is small:

```text
Original web resource (its URL)
└── Stored capture (a frozen copy, identified by its capture time)
    └── Capture set for the URL (the archive's time dimension)
        └── Time selection (choose a capture by date)
            └── Replay surface (the capture presented for reading,
                with its original URL and capture time visible)
```

Everything else commonly associated with the best-known products — crawler harvesting at web scale, calendar-style date pickers, one-click "save this page now" capture, full-text search, analytics — is widespread but not part of what makes the application this Type. The viewer also does not need to be a hosted public service: it exists as hosted archives, self-hosted institutional software, and local desktop tools that replay archive files on the user's own machine.

## Users & Context

The primary user is anyone who needs to see a web page's past state:

- **General users** returning to a page that has moved, changed, or disappeared — a dead link, a redesigned site, a deleted post.
- **Journalists, fact-checkers, and researchers** verifying what a page claimed at a specific moment, or studying how a site changed over time.
- **Legal and compliance professionals** establishing the prior state of a web resource as reference material.
- **Librarians, archivists, and digital-preservation staff** providing access to collections of harvested web content — the viewer is the public access surface of institutional web archiving.
- **Site owners and developers** inspecting earlier versions of their own or competitors' pages.

The context of use is reading and verification, not editing: the user consumes frozen content. Sessions typically begin from a URL the user already has (or from search over the archive), pass through a time-selection step, and end in reading a replayed page. Institutional users additionally work inside curated collections with access rules.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product is no longer a Web Archive Viewer:

- **Stored captures of web resources.** The system holds persistent frozen copies of web pages — resources that exist or existed on the live web. A capture is inert: its content does not change after it is taken. Without stored captures there is nothing to view and the application collapses into an ordinary browser or proxy.
- **Time-addressed access.** Each capture is identified by its original URL together with its capture time, and the user selects among captures in the time dimension — a list of dated snapshots, a timeline, or a date-based lookup. Without the time dimension the product is a single-copy mirror or a generic file viewer; the "archive" is gone.
- **Replay presentation.** The selected capture is rendered as a viewable page, and its archived identity — the original URL and the capture time — is visible to the user while reading. Without presentation the product is a catalog of captures, not a viewer.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical but do not define it:

- **Shareable archived addresses.** A dominant shared pattern embeds the capture time in the URL of a replayed page, so an archived page can be cited and re-opened at exactly the same capture. (This URL grammar is an implementation convention, not the invariant — the invariant is time-addressing itself.)
- **Replay marking.** A banner or top-frame strip around the replayed page that makes clear the content is archived, typically showing the original URL and the capture datetime.
- **Link rewriting.** Links inside a replayed page are rewritten so that following them resolves to other captures in the archive instead of escaping to the live web — implemented server-side, client-side, or both.
- **Nearest-capture resolution.** When the user asks for a date, the system serves the capture nearest to it; archives capture pages irregularly, so the served capture's time may differ noticeably from the requested one.
- **Search.** At minimum, lookup of captures by URL; mature products commonly add full-text search across the archived pages and resources.
- **Collection layer.** Captures are organized into named collections, or into a personal index of loaded archive files, giving the archive browsable structure beyond individual URLs.
- **Export.** Downloading captures or search results as standard archive files.

### One Structure, Many Implementations

The core model is conceptual. Implementations differ on every layer:

```text
Concept:            Stored captures
Implementations:    crawler-harvested collections, on-demand user snapshots,
                    archive files (WARC/WACZ-class formats) loaded locally

Concept:            Time-addressed access
Implementations:    timestamp-embedded URLs, dated snapshot lists,
                    datetime negotiation against a time gate

Concept:            Replay presentation
Implementations:    framed replay (page in a frame under an archive header),
                    frameless replay with an inserted banner,
                    interactive in-browser replay of captured resources
```

A reader who has only seen one hosted archive should still be able to recognize a local file-based viewer or an institutional replay system as the same Type from the core model.

## How It Works

### Locate captures for a URL

```text
Enter a URL (or search the archive by words / browse a collection)
→ the archive reveals which captures exist for that resource
→ and when they were taken
```

The result is the resource's capture set: a dated list or timeline of what the archive holds. Coverage is never guaranteed — pages that were never captured simply have no entries, and gaps between captures are normal.

### Choose a point in time

```text
Pick a date (or accept the default / follow a shared archived link)
→ the system resolves the request to the nearest available capture
→ the served capture's actual time is shown to the user
```

Because captures are sparse and irregular, the capture the user lands on may be from a noticeably different moment than the one requested; the visible capture time is the honest answer.

### Replay the capture

```text
Open the selected capture
→ the archived page is rendered in the viewer
→ a banner or header marks it as archived and shows
   the original URL and capture time
→ links in the page are rewritten to resolve to other captures
```

The replayed page is a frozen copy: its text, images, and layout are as captured. Navigation stays inside the archive — clicking links moves the user to other captures of the linked pages, at or near the same point in time.

### Navigate and inspect

```text
Follow rewritten links between captures
→ search within the archive (by URL, or full text where offered)
→ inspect individual archived resources (images, scripts, files)
   where the viewer exposes them
```

### Optional: capture and export

Some products let the user create new captures on demand (submit a page to be archived, or record pages while browsing them), and most mature products let the user export captures or search results as standard archive files. Capture is a companion capability, not the viewer's defining act — several products of this Type replay archives they did not create.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### URL / time entry

The primary entry surface.

- a URL field (and commonly a date control) that queries the archive for a resource's captures
- typical information: whether captures exist, how many, and their dates
- primary actions: submit a URL, pick a date, open the nearest capture

### Replay surface

The core reading surface: the archived page itself, framed or annotated by archive chrome.

- typical information: the replayed page content, plus a banner or header showing the original URL, the capture datetime, and archive navigation
- primary actions: move to earlier/later captures of the same page, return to the capture list, share the archived address

### Search

A real surface because the archive is a body of historical content, not just one page.

- URL lookup in all products; full-text search across archived pages and resources in mature products
- primary actions: search, filter by date or collection, open a result's capture

### Collection / library view

The organizational surface of the archive.

- typical information: named collections or loaded archive items, with titles, dates, and descriptions
- primary actions: browse a collection, open a page within it, (in personal tools) load or unload archive files

### Resource inspection

A closer look at what an archive item contains, offered by many viewers.

- typical information: the individual resources held for a page or collection — images, stylesheets, scripts, documents — listed by URL and type
- primary actions: search resources by URL, open a resource, view its metadata

### Access-control surfaces (institutional archives)

Institutional deployments commonly sit the viewer behind governance rules.

- typical information: which captures are open, embargoed, or restricted; login state
- primary actions: authenticate, request access, view what the rules allow

## Important Rules / Behaviors

### Captures are frozen

A capture's content does not change once taken; the archived state is promised to be stable. This is what makes archived pages citable and comparable across time.

### Nearest match, not exact match

Archives capture pages irregularly. A request for a specific date resolves to the nearest available capture, and the served capture's time may differ significantly from the requested one. The capture's actual datetime is therefore always surfaced to the user.

### Replay is not byte-identical

The replayed page is a faithful copy of the captured content, but the replay machinery itself modifies the page's plumbing: URLs are rewritten so navigation stays in the archive, and archive chrome (banner or frame) is added. Older content may additionally be served through emulation. The content is frozen; the delivery is engineered.

### Live-web leakage is the characteristic failure

A replayed page may still reference resources the archive does not hold. Mature replay systems intercept and redirect such references back into the archive; where interception cannot catch them (for example, absolute references to other domains), the replayed page can partially reach the live web — which silently breaks the "you are seeing the past" guarantee. Users verifying past states are advised to treat any live-sourced element with suspicion.

### Coverage is partial by nature

No archive holds everything. Absence of captures is a normal result, not an error; and the absence of a capture between two dates means the page's state in that gap is simply unknown.

### Access can be governed

Institutional archives commonly apply embargo windows (captures hidden until a future date), exclusion rules, and user-based access, reflecting legal-deposit and licensing constraints. A capture that exists may still not be viewable by a given user.

## Variants

Common forms of the Type:

- **Global public crawler archive** — a hosted service that continuously harvests the web at scale and offers public replay of everything it holds (the most familiar public pattern).
- **On-demand snapshot service** — a hosted service centered on user-submitted captures of individual pages, replayed from its own store.
- **National / institutional curated archive** — a library or archive harvesting defined scopes (its country's web, themed collections), with curated collections, embargo, and access rules; the viewer is the public access layer.
- **Self-hosted replay software** — the replay engine as installable software that institutions run over their own harvested collections, often paired with a search interface.
- **Local / serverless viewer** — a desktop app or browser-based tool that replays standard archive files (WARC/WACZ-class) on the user's own machine, offline, with no service involved.
- **Cross-archive aggregator** — a layer that, for a given URL and datetime, searches multiple archives at once and routes the user to whichever holds the best capture.
- **Research-oriented replay** — replay bundled with analytics over the archive: full-text search, link graphs, trend visualizations, image search.

A variant remains a variant as long as the defining core — stored captures, time-addressed access, replay presentation — is intact.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Web Browser | renders the live web; no capture store and no time selection. A browser can display an archived address, but the archive structure lives outside it. Proxy-style replay can mimic browser UX — the seam is the content source (stored past vs live present). |
| Read-it-later Application | holds a personal copy of a page for later reading; no maintained time-addressed capture set and no shared archive dimension. |
| Bookmark Manager | stores references (and sometimes personal copies) to pages; the object is a link in a personal collection, not a dated capture in an archive. |
| General Web Search Engine | its primary object is the live web; cached copies, where offered, are transient byproducts of search, not maintained, citable, time-addressed captures. |
| Digital Library Platform | curates document collections with bibliographic identities (books, articles, theses); the unit here is the captured web resource addressed by URL and time. National web archives are curated institutions whose access surface is this Type. |
| Website mirror / static copy | serves one copy as if live, with no original-URL + datetime addressing and no capture history. |
| Wiki / CMS / version-control systems | version their *own* content; a Web Archive Viewer's object is the external web at large. A prior version of one's own page is versioning, not web archiving. |

The closest boundary is the Web Browser's: both render web pages in a browser-grade surface. The structural difference is entirely in what is being rendered — a frozen, dated capture from a store of past states, versus whatever the server returns now.

## Representative Products

- **Wayback Machine (Internet Archive)** — the best-known global public crawler archive with public replay; other replay systems describe themselves by reference to it.
- **archive.today** — independent on-demand snapshot service.
- **ReplayWeb.page (Webrecorder)** — local-first, serverless viewer that replays WARC/WACZ archive files in the browser.
- **pywb and SolrWayback** — the widely adopted self-hosted replay systems used by national libraries and archives.
- **Conifer (Rhizome)** — user-driven capture-and-revisit service (collections closed to new capture in 2026; retained as a formative example).

The defining core was checked against this spread deliberately: a hosted crawler archive, an on-demand snapshot service, self-hosted institutional software, a local file-based viewer, and a user-capture service all satisfy it, while none of the implementation specifics (crawler harvesting, URL grammar, banner style, hosting model) is required by it.

## Sources

Research date: **2026-09-09**

- RFC 7089 — *HTTP Framework for Time-Based Access to Resource States -- Memento* — https://datatracker.ietf.org/doc/html/rfc7089
- Memento project guide — https://mementoweb.org/guide/ , https://mementoweb.org/guide/quick-intro/
- ReplayWeb.page — https://webrecorder.net/replaywebpage/ , https://replayweb.page/docs/user-guide/ (incl. loading / locations / exploring pages)
- pywb documentation — https://pywb.readthedocs.io/en/latest/ (incl. Configuring the Web Archive)
- SolrWayback — https://github.com/netarchivesuite/solrwayback (README)
- IIPC — https://netpreserve.org/web-archiving/playback/
- Conifer — https://conifer.rhizome.org/

> Sourcing limitation: on 2026-09-09 the direct product surfaces of the Wayback Machine (archive.org help and web.archive.org), archive.today (archive.ph / archive.is), the UK Web Archive, the Memento Time Travel aggregator UI, Wikipedia, and loc.gov could not be fetched from the research environment (repeated timeouts / blocks; each source abandoned after repeated failures). Evidence for the Wayback Machine and archive.today is therefore limited to the example archived URLs quoted in RFC 7089, which establish their time-addressed capture access; no UI details, coverage figures, or feature claims are stated for them in this document. Claims about banner marking, link rewriting, and nearest-capture behavior are calibrated to the sources that were directly fetched (RFC 7089, pywb, SolrWayback, ReplayWeb.page, IIPC).

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
