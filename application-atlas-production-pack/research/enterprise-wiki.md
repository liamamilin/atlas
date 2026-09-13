# Research Notes — Enterprise Wiki

Research date: 2026-09-07

## Research Goal

Understand the **Enterprise Wiki** as an Application Type from real products: what the wiki pattern contributes, what the "enterprise" layer adds (identity, permissions, governance, scale), what the core object model is (page / link / revision / container), how members actually work in it day to day, and where the boundary lies against the sibling Wiki Application, Knowledge Base Application, Help Center, and the processed neighbors Collaborative Workspace, Intranet Platform, Enterprise Content Management, Internal Knowledge Search, and Collaborative Document Editor.

## Initial Boundary

- **Hypothesis:** an Enterprise Wiki is the wiki pattern (interlinked pages, open member editing, durable revision history) operated as an organization's internal knowledge system, with organization-scoped identity/access control and governance machinery on top.
- **Nearest neighbors:** Wiki Application (§02.06 sibling, unprocessed), Knowledge Base Application (§02.06 sibling, unprocessed), Help Center (§02.06 sibling, unprocessed), Collaborative Workspace (§03.12, processed — flagged joint review), Intranet Platform (§10, processed), Enterprise Content Management (§10, processed), Internal Knowledge Search (§13, processed), Collaborative Document Editor (§03.01, processed).
- **Prior flag to discharge:** the collaborative-workspace pass recorded a real straddle ("Confluence is wiki-heritage yet positions as a team workspace") and recommended joint review when wiki-application and enterprise-wiki are processed. This pass addresses the enterprise-wiki side.
- **Open taxonomy question going in:** is Enterprise Wiki a distinct Type or an audience/deployment variant of Wiki Application?

## Research Questions

1. What is the core object model — page, link, revision, container — and how do the objects relate?
2. What does "open editing" mean in an organizational context — who may edit, and what makes that safe?
3. How is content organized and discovered (containers, page trees, labels, links, search, recent changes)?
4. What enterprise machinery is standard (identity/SSO/LDAP, permission levels, admin, audit, analytics, export)?
5. What page lifecycle exists (draft, publish, move, archive, delete/restore, templates)?
6. Do sampled products still self-identify as "wiki", or has market language drifted (knowledge base, workspace)?
7. Where are the boundaries: vs public/community wikis, vs knowledge bases, vs intranets, vs ECM, vs workspaces?
8. Historical check: do 1990s/2000s-era classic wikis satisfy the same definition, or is the definition over-fitted to modern SaaS?

## Representative Products

| Product | Philosophy / position | Customer tier | Why sampled |
|---|---|---|---|
| Confluence (Atlassian) | commercial market leader; space/page-tree governance; suite integration | enterprise (cloud + self-managed Data Center) | dominant commercial enterprise wiki; wiki heritage (2004) |
| TWiki | classic open-source "structured wiki" / application-wiki platform | enterprise self-hosted (behind firewalls) | the original "enterprise wiki" self-label; 1998 lineage rooted in Ward Cunningham's WikiWikiWeb; historical check |
| Foswiki | classic open-source collaboration platform (TWiki fork) | enterprise self-hosted, LDAP-integrated | second classic pole; structured data + programmable pages; TWiki-compatible |
| Slite | modern SaaS "self-maintaining AI knowledge base" | SMB → mid-market → enterprise tiers | modern cloud-native pole; AI-era knowledge-health machinery; self-labels as knowledge base, not wiki |
| Nuclino | modern lightweight unified workspace ("collective brain") | SMB / teams | speed/simplicity pole; knowledge + docs + projects unified |

Rejected/limited samples (recorded as source-access limitations, no claims made): **MediaWiki** (mediawiki.org timeout ×2), **XWiki** (xwiki.org timeout + 403), **DokuWiki** (dokuwiki.org timeout ×2). These would have covered the public-wiki-engine pole and the file-based pole; the classic pole is instead covered by TWiki/Foswiki, whose own documentation states their WikiWikiWeb lineage.

## Sources

Fetched (Tier 1 official documentation unless noted):

- Confluence Data Center documentation home — https://confluence.atlassian.com/doc/
- Confluence — Spaces — https://confluence.atlassian.com/doc/spaces-139459.html
- Confluence — Permissions and restrictions — https://confluence.atlassian.com/doc/permissions-and-restrictions-139557.html
- Confluence — Pages and blogs — https://confluence.atlassian.com/doc/pages-and-blogs-320602215.html
- Confluence — use-cases section — https://confluence.atlassian.com/doc/confluence-use-cases-283641068.html
- TWiki — home / "What is TWiki" — https://twiki.org/
- Foswiki — home — https://foswiki.org/
- Foswiki — About — https://foswiki.org/Home/About
- Slite — product home (Tier 2) — https://slite.com/
- Slite — Help Center index — https://slite.com/help
- Slite — Doc Verification article — https://slite.com/help/F9erHftuXmOHY0
- Nuclino — product home (Tier 2) — https://www.nuclino.com/
- Nuclino — Help Center index — https://help.nuclino.com
- Nuclino — Workspaces section — https://help.nuclino.com/f639f8d2-workspaces

Source-access limitation: MediaWiki, XWiki, and DokuWiki official sites were unreachable (timeouts/403, abandoned after 1–2 attempts each per the network rule). No claim in either document depends on those products. Confluence evidence is Data Center documentation (the cloud documentation home was referenced but not separately fetched); Slite/Nuclino evidence is product-page + help-center level, so product-specific operational details for those two are kept conservative.

## Product A — Confluence (Atlassian) — evidence layer A

Official Data Center documentation, directly observed.

- **Positioning:** "Confluence is where you create, organize, and discuss work with your team." Documented use-case guides: knowledge base, intranet, technical documentation, software teams — the product explicitly spans several neighbor Types.
- **Containers:** Spaces are "Confluence's way of organizing content into meaningful categories"; two varieties — site spaces (in the Space Directory) and personal spaces (per user, private or public). Suggested uses: team spaces (QA, HR, Engineering, Support), project spaces, personal space. Space admins control who can view/edit; space creator automatically gets space admin; spaces can be archived, deleted, copied, exported (Word/PDF/HTML/XML), made public.
- **Permissions — three levels:** global permissions (site-wide: log in, create space — assigned by administrators); space permissions (per-space, independent, managed by space admins; grant/revoke view/add/edit/delete for groups, users, even anonymous); page restrictions ("**Pages are open for viewing or editing by default**, but you can restrict either viewing or editing to certain users or groups"); restrictions inherit down the page hierarchy; space admins can see and remove restrictions. Explicit rationale: "Confluence is at its best when everyone can participate fully."
- **History as the safety mechanism:** "Confluence keeps a history of all changes to pages and other content, so it's easy to see who has changed what, and reverse any changes if you need to."
- **Pages and blogs:** pages "for information to last and evolve over time" vs blog posts for point-in-time updates; every space has a page tree and a blog; features include drafts, labels, move/reorder (hierarchy), copy, delete/restore, page templates and blueprints, links/anchors, **undefined page links** (links to not-yet-existing pages), page history and page comparison views, tasks on pages, page layouts, import.
- **Other machinery:** files/attachments with Office preview; macros ("from formatting to dynamic content"); collaboration (comments, mentions, notifications, watch pages/spaces); analytics (space/page views, active users); search section; Team Calendars; add-ons/integrations (Jira); administrator's guide (users, license); Data Center scaling; GDPR guides.

## Product B — TWiki — evidence layer A

Official twiki.org home page ("What is TWiki"), directly observed.

- **Self-label:** "TWiki is a flexible, powerful, and easy to use **enterprise wiki**, enterprise collaboration platform, and web application platform. It is a Structured Wiki, typically used to run a project development space, a document management system, a knowledge base, or any other groupware tool, on an intranet, extranet or the Internet."
- **Enterprise motivation, stated verbatim:** "TWiki fosters information flow within an organization… and **eliminates the one-webmaster syndrome of outdated intranet content**." Deployment list includes "to replace a static intranet. Content is maintained by the employees" and "as a knowledge base and FAQ system."
- **Open editing:** "TWiki looks and feels like a normal Intranet or Internet web site. However it also has an **Edit link at the bottom of every topic (web page); everybody can change a topic or add content by just using a browser**."
- **Core mechanics:** WikiWord auto-linking ("Web pages are linked automatically"); simple text formatting ("write text like you would write an e-mail"); **Webs** ("Pages are grouped into TWiki webs… separate collaboration groups"); full-text search; file attachments; **revision control** ("All changes to pages and attachments are tracked. Retrieve previous page revisions and differences thereof. Find out who changed what and when"); **access control** ("Define groups and impose fine grained read and write access restrictions based on groups and users"); rename/move/delete pages via browser; web-based user registration.
- **Structured wiki layer:** TWiki Forms ("classify and categorize unstructured web pages and to create simple workflow systems"); variables/macros (dynamic TOC, include other pages, embedded search results); Plugins (400+ extensions); "Application Wiki" — contributors build web applications (change request, meeting minutes with action items, FAQ, call-center status board).
- **Awareness machinery:** e-mail notification of changes (WebNotify); recent changes (WebChanges) with RSS export; web statistics (most popular pages, top contributors); Referred-By backlinks.
- **Conflict handling:** automatic merge when several users edit simultaneously; manual resolution guidance when a conflict cannot be merged.
- **Preferences:** four levels — site, web, user, page.
- **Heritage:** roots in JosWiki; "inspired by the brilliant idea of the original Wiki Wiki Web by Ward Cunningham." Installed "mainly behind corporate firewalls"; success stories at Motorola, SAP, BT, CERN, Morgan Stanley, etc.

## Product C — Foswiki — evidence layer A

Official foswiki.org home + About page, directly observed.

- **Self-label:** "The Free Enterprise Collaboration Platform." "Foswiki is a platform, so you and your team members can **collaborate and edit pages directly in the web browser**."
- **Three-part self-description:** **Wiki** (share knowledge; edit pages collaboratively; "If needed, protect pages with flexible access controls"; "Versioned documents and attachments with revision history"; "Enterprise LDAP integration") + **Structured Data** (store data in pages; advanced search to extract data; create applications: status boards, to-do lists, inventory systems, employee handbooks, bug trackers) + **Programmable Pages** (Excel-like macros; extract/display data tabularly/graphically/as XML; mashups with web APIs).
- **Note the phrasing:** access protection is optional ("if needed") — open editing is the default posture, protection the exception. Same posture as Confluence's "open by default" and TWiki's "everybody can change a topic."
- **Other:** WYSIWYG editor (TinyMCE); 200+ extensions; TWiki-compatible with seamless migration path; runs self-hosted (Linux/Mac/Windows/USB/appliance); localized in 20 languages; webs organize the site; security focus (CSRF protection).

## Product D — Slite — evidence layer A (product page + help center)

- **Self-label (market-language drift):** "The self-maintaining **AI knowledge base**" — not "wiki". Positioned as "single source of truth for your team knowledge"; migration targets listed: Notion, Confluence, ClickUp, Quip, OneNote.
- **Content model:** docs organized in **channels** and **collections**; editor with slash commands, AI assistance, rich blocks; templates.
- **Knowledge-health machinery (directly observed, Doc Verification article):** per-doc verification statuses — **Verified** (with a set verification period; expiry turns status to **Verification expired** and notifies the owner), **Outdated** (flagged by any member; deprioritized in AI results, excluded from the agent), **Verification requested** (teammates prompt the owner), **No status** (default). Role table: Owner/Admin verify if they can read; Member verify if they can edit; Reader can request verification / flag outdated; Guest neither. **Knowledge Management Panel** for at-scale management (filter by owner/status/channel; bulk-verify, reassign ownership, archive outdated docs).
- **AI layer:** Slite Agent watches connected tools (Slack, Linear, GitHub, codebase), detects "knowledge drift", drafts doc updates, routes to the right expert for approval ("humans stay in the loop"); AI search ("Ask") across the KB and connected tools — cited answers, ranked verified-first, permission-aware ("every query inherits the user's permissions"); **MCP server** exposes the KB to external agents (search/read/edit/verify/archive operations listed).
- **Enterprise machinery:** SSO, SCIM, granular role-based permissions, reader-only seats; full audit logs, version history, draft states, "every write attributed"; SOC 2 Type II, HIPAA, GDPR, EU hosting; import from Notion/Confluence/Google Drive; pricing tiers Basic/Pro/Enterprise.
- **Help-center guide structure:** Getting Started; Write & Organize; Admin & Settings; Find and Search; Slite (AI) Agent; Keep Knowledge Healthy; Collaborate & Share; Integrations & Automations; Privacy & Security; Analytics.

## Product E — Nuclino — evidence layer A (product page + help center index/section)

- **Self-label:** "Your team's collective brain… bring knowledge, docs, and projects together in one place." Emphasis: unified space, super simple, blazingly fast (quick setup, instant search, hotkeys).
- **Content model (help center):** Teams → **Workspaces** → **Collections** → **Items**; Views; Search; Canvas (visual board); Sidekick (AI assistant); API; Apps & Integrations; Access & Security; Import & Export.
- **Workspace semantics (Workspaces section, directly observed):** public vs private workspaces; add/join/leave members; member roles; change workspace privacy/access settings; publish a workspace; duplicate/export/delete workspace; trash; fields; default views; star/sort.
- **Observation:** Nuclino's organizing unit is the workspace/collection with items — closer to the workspace pole than the classic wiki pole; included deliberately as the lightweight modern boundary sample.

## Cross-product Comparison

| Aspect | Confluence | TWiki | Foswiki | Slite | Nuclino |
|---|---|---|---|---|---|
| Unit of content | Page | Topic | Topic | Doc | Item |
| Organizing container | Space (site/personal) | Web | Web | Channel / Collection | Workspace / Collection |
| Interlinking | page links, anchors, undefined-page links | WikiWord auto-links, Referred-By backlinks | auto-links (wiki heritage) | links between docs | links between items |
| Open editing | "open for viewing or editing by default"; restrictions optional | "everybody can change a topic" | protect "if needed" | member editing; every write attributed | member editing in team workspaces |
| Version history | page history + comparison views; restore | revision control, diffs, who changed what | versioned docs + attachments | version history, audit logs | (not directly observed — not claimed) |
| Access control | global / space / page restrictions | groups, fine-grained read/write | flexible access controls + LDAP | SSO/SCIM, roles, reader-only seats | workspace privacy/access, member roles |
| Organization identity | admin-managed users/groups, login | web-based registration | enterprise LDAP | SSO/SCIM | accounts/teams (SSO not directly observed) |
| Search | dedicated search section | full-text search | advanced search | AI search (Ask), verified-first, cited | instant search |
| Change awareness | watch pages/spaces, notifications | WebNotify e-mail, recent changes, RSS | (notify machinery in heritage) | (notifications; agent-driven review) | (not directly observed) |
| Templates | page templates, blueprints | templates/skins | (templates in heritage) | templates gallery | templates |
| Structured data | macros | TWiki Forms + variables | forms/structured data, Excel-like macros | — (collections/fields not claimed) | fields, views |
| Application building | macros + plugins | Application Wiki (change request, FAQ…) | applications (status boards, handbooks, bug trackers) | — | — |
| Blogs | blog posts per space | — | — | — | — |
| Analytics | analytics (views, active users) | web statistics (top pages/contributors) | statistics (heritage) | analytics section | — |
| Export/import | Word/PDF/HTML/XML export; import | RSS export | XML output | import from Notion/Confluence/Drive | import & export, workspace export |
| AI | (cloud-era AI not in DC docs fetched) | — | — | Agent, Ask, MCP | Sidekick |
| Deployment | Cloud + Data Center (self-managed) | self-hosted (Perl CGI) | self-hosted (Perl) | SaaS (EU hosting option) | SaaS |
| Self-label today | "document collaboration" | "enterprise wiki" | "enterprise collaboration platform" | "AI knowledge base" | "collective brain" |

### Stable commonalities (evidence layer B)

Across all five sampled products:

1. A corpus of **pages** (page/topic/doc/item) as the unit of knowledge.
2. **Links between pages** as a first-class structure (auto-linking, backlinks, red/undefined links in the classic products; doc-to-doc links in modern ones).
3. **Open member editing** — any member with access can create/edit directly in the browser; editing is the default posture, restriction the exception (stated verbatim in Confluence, TWiki, Foswiki; structural in Slite/Nuclino).
4. **Attributed, durable change history** (explicit in Confluence, TWiki, Foswiki, Slite).
5. **Organizing containers** with their own access settings (spaces/webs/channels/workspaces).
6. **Organization-scoped access** — the corpus is entered through organizational identity and is not public by default (login/registration/LDAP/SSO; "behind corporate firewalls" TWiki; private workspaces Nuclino; SSO Slite).
7. **Search** over the corpus.
8. **Templates** for recurring page types.
9. **Administration machinery** (users/groups/roles, container-level permissions).

### L0 — Defining Invariant

Four properties. If any one is removed, the product stops being recognizable as an Enterprise Wiki:

1. **Interlinked page corpus** — the unit of knowledge is a page; pages reference each other; the corpus's structure is emergent (grown by contributors through links and light hierarchy), not fixed by a schema or a publication pipeline. Remove → document repository / ECM / blog.
2. **Open member editing** — any member with access may create and edit pages directly, without an author/publication gate. Remove → published documentation / CMS / help center (few authors, many readers).
3. **Durable attributed version history** — every change is recorded (who/what/when), diffable and reversible; the mechanism that makes open editing safe inside an organization. Remove → shared notepad; open editing becomes reckless.
4. **Organization-scoped access** — the corpus belongs to a defined organization; entry is gated by organizational identity, and access is governed at site/container/page levels. Remove → the general (public/community/personal) Wiki Application.

Historical check (§24 discipline): TWiki (1998 lineage, Perl CGI, markup-era, self-hosted, rooted in Cunningham's WikiWikiWeb) and Foswiki satisfy all four properties without WYSIWYG, cloud delivery, AI, spaces terminology, or templates-as-features. The definition does not over-fit to the modern SaaS era. Pass.

Anti-overfitting note: "spaces" (Confluence) vs "webs" (TWiki/Foswiki) vs "channels/collections" (Slite) vs "workspaces" (Nuclino) are implementations of one concept — the organizing container. The container is L1 (common mature structure), not L0: a wiki without named sub-containers (one flat corpus) is still a wiki.

### L1 — Common Mature Structure

- Organizing containers (spaces / webs / channels / collections / workspaces) with per-container permissions
- Page hierarchy (tree) plus labels/categories/tags
- Full-text search; recent-changes / what's-new streams
- Page templates (and template galleries in modern products)
- File attachments on pages
- Change notification (watch/subscribe; e-mail or in-app)
- Backlinks and undefined-page ("red") links inviting page creation
- Rich/WYSIWYG editor (markup underneath in classic products)
- Usage analytics (views, top contributors)
- Export (PDF/Word/HTML/XML) and import/migration tooling
- Administration: user/group management, global permissions, audit trail
- Enterprise identity integration (SSO / SCIM / LDAP)

### L2 — Variant / Optional Structure

- **Structured-data / application-wiki layer**: forms, fields, macros embedded in pages; using the wiki as a platform for lightweight apps (trackers, handbooks, status boards) — TWiki/Foswiki pole
- **Blogs inside the wiki** (Confluence blog posts)
- **Suite/marketplace integration** (issue trackers, calendars, office-file preview)
- **AI-era knowledge-health layer**: AI search/answers with citations, agent-drafted maintenance with human approval, verification/trust states with expiry, MCP/agent exposure — Slite pole; era-typical, not definitional
- **Compliance posture**: SOC 2/HIPAA/GDPR, EU hosting, audit logs (enterprise tiers)
- **Deployment**: cloud SaaS vs self-hosted; scaling editions (Data Center)
- **Selective opening**: public spaces / published workspaces for outsiders; anonymous access options
- **Personal spaces** (per-member private area)
- **Use-case packaging**: knowledge base, intranet, technical documentation, software teams

### L3 — Vendor-specific (research notes only)

- **Confluence**: spaces/site+personal split, blueprints, Team Calendars, Confluence Markup, Data Center edition, Jira integration depth
- **TWiki**: webs, WikiWord, TWiki Forms, TWiki Variables, 4-level preferences, automatic edit merging, plugin API (400+ extensions)
- **Foswiki**: Excel-like macros, TWiki compatibility plugin, 20-language localization, USB-stick/appliance deployment
- **Slite**: Slite Agent (drift detection + drafted updates), doc verification status set (verified/expired/outdated/requested), Knowledge Management Panel, MCP server, channels
- **Nuclino**: Canvas, Sidekick, views, fields, public/private workspace toggle, publish-workspace

## Vendor-specific Findings

See L3 above. Additionally: Slite's verification machinery (statuses, expiry, role table, verified-first ranking) is the most fully articulated "knowledge health" system in the sample — treated as a modern variant layer, not a Type requirement (no other sampled product documents an equivalent status machine; Confluence/TWiki/Foswiki rely on history + watch + statistics instead).

## Rejected Findings

- **"Enterprise wiki = Confluence-style spaces + page trees"** — rejected: TWiki/Foswiki organize into webs and predate spaces; the container concept is L1, the specific space model is vendor-specific.
- **"Wiki = WYSIWYG editing"** — rejected: TWiki's editing is markup-based ("write text like you would write an e-mail"); WYSIWYG is an editor implementation.
- **"Enterprise wiki requires SSO/SCIM"** — rejected as definitional: TWiki/Foswiki use web registration/LDAP; SSO/SCIM is the modern identity implementation of the L0 "organization-scoped access".
- **"AI maintenance/verification is what makes a wiki enterprise-grade"** — rejected: single-product (Slite) articulation; era-typical variant.
- **"Enterprise wiki is a knowledge base"** — rejected as identity: products self-label as knowledge bases (Slite) and document KB use cases (Confluence), but the sampled structures remain emergent interlinked page corpora, not curated article sets with answer-oriented lifecycle. Boundary recorded, not merged.
- **Nuclino as a pure Enterprise Wiki** — partially rejected for classification: its workspace/collection model and docs+projects scope drift toward Collaborative Workspace; retained as a boundary-informing lightweight sample.

## Boundary Findings

1. **vs Wiki Application (§02.06 sibling, unprocessed)** — the wiki pattern (L0 items 1–3) is shared. The discriminator for this leaf is L0 item 4: the corpus is scoped to an organization's members via organizational identity and governance. Public/community wikis (Wikipedia-style), fan/community wikis, and personal wikis lack the organizational scope and belong to Wiki Application. **Taxonomy note:** Enterprise Wiki is arguably an audience/deployment variant of Wiki Application rather than a fully distinct Type; the directory carries both leaves, so this pass documents the enterprise-scoped realization and recommends joint review when wiki-application is processed.
2. **vs Collaborative Workspace (§03.12, processed)** — boundary held on organizing principle, consistent with that pass: emergent interlinked topic-page graph with open editing (wiki) vs governed container holding heterogeneous content with membership (workspace). Confluence straddles (wiki heritage; markets as team workspace; ships KB/intranet use cases). The joint-review flag from the collaborative-workspace pass is **discharged from this side**: the seam test ("topic-page graph → wiki; team container with membership → workspace") is confirmed against wiki-side evidence.
3. **vs Knowledge Base Application (§02.06 sibling, unprocessed)** — real overlap in market language (Slite self-labels "AI knowledge base"; Confluence documents "use as a knowledge base"). Structural distinction: KB = curated, owned, review-managed article set answering questions; wiki = emergent interlinked pages maintained by open member editing. Flag for joint review when knowledge-base-application is processed.
4. **vs Help Center (§02.06 sibling)** — Help Center is the customer-facing published help surface (external audience); the enterprise wiki is internal (member audience). A wiki can *host* help-center content (Confluence use case), but the audience and governance differ.
5. **vs Intranet Platform (§10, processed)** — intranet = organization-published pull destination (news/pages/resources, publisher-governed estate); wiki = member-authored interlinked pages. TWiki states the contrast classically ("eliminates the one-webmaster syndrome of outdated intranet content"); Confluence documents "use as your intranet" as a use case. Boundary held on who authors: org publishers vs any member.
6. **vs Enterprise Content Management (§10, processed)** — ECM = controlled capture/intake, organization-defined metadata, records retention/disposition; wiki = open member authoring with emergent structure. Controlled intake vs open editing is the seam.
7. **vs Internal Knowledge Search (§13, processed)** — that Type is the discovery/answer layer over a multi-source corpus; the enterprise wiki is one of the authoring/publishing systems such a layer indexes. A wiki's built-in search is single-system (consistent with that pass's finding).
8. **vs Collaborative Document Editor (§03.01, processed)** — freeform long-form document composition vs a corpus of interlinked topic pages maintained over time.
9. **vs Team Messaging** — conversations/messages vs pages/corpus; different unit, different persistence semantics.

## Uncertainties

- MediaWiki, XWiki, DokuWiki could not be fetched; the public-wiki-engine and file-based poles are covered structurally (via TWiki/Foswiki lineage and the general wiki pattern), not by direct evidence. No product-specific claims are made about them.
- Market-language drift: only the classic OSS products self-label "enterprise wiki"; the commercial/modern products self-label as document collaboration (Confluence), AI knowledge base (Slite), collective brain (Nuclino). The leaf name is a heritage term; the structural pattern persists underneath. Recorded as a taxonomy-relevant observation.
- Nuclino's version-history and SSO details were not directly observed (help-center sections exist but were not fetched); no claims made for Nuclino on those points.
- Confluence Cloud specifics (AI features, cloud-only capabilities) were not fetched; Confluence evidence is Data Center documentation.
- Slite/Nuclino evidence is product-page + help-center level; deeper operational mechanics (e.g., exact permission matrices beyond what was fetched) are not asserted.

## Final Synthesis

An **Enterprise Wiki** is an organization-internal knowledge system built on the wiki pattern: a corpus of **interlinked pages** that any member can **create and edit directly** (open member editing), where every change is preserved in **durable, attributed, reversible version history**, and where the corpus is **scoped to the organization** — entered through organizational identity and governed by layered access control (site → container → page).

Around this defining core, mature products add a consistent standard layer: organizing containers with per-container permissions, page trees and labels, search and recent-changes streams, templates, attachments, change notifications, backlinks/red links, analytics, export/import, and administration with enterprise identity integration. Products vary on optional structure: the structured-data/application-wiki layer (classic OSS pole), suite integration and blogs (commercial pole), and the AI-era knowledge-health layer — AI search with citations, agent-drafted maintenance with human approval, verification states with expiry, and agent-facing exposure (modern SaaS pole).

The Type's sharpest seams: the general Wiki Application (same pattern, no organizational scope), the Knowledge Base Application (curated answers vs emergent corpus), the Collaborative Workspace (governed container vs emergent page graph), the Intranet Platform (org-published estate vs member-authored pages), Enterprise Content Management (controlled intake vs open editing), and Internal Knowledge Search (discovery layer vs authoring system).
