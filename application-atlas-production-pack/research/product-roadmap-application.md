# Research Notes — Product Roadmap Application

## Research Goal

Understand the "Product Roadmap Application" as an Application Type: what objects exist inside it (roadmaps, bars/items/entries, lanes/swimlanes, milestones, views, versions, portfolios), what the unit of record is, what the primary work loop is, who uses it and for which audiences, which capabilities are common but not defining, and where the Type's boundary sits.

This pass carries **two joint-review obligations** from processed sibling passes:

1. **product-management-platform** (processed 2026-09-09): "the roadmap-application pass must confirm whether a pure roadmap-artifact tool without the feature-record core exists before the seam is finalized" — that pass's position: in PM platforms the roadmap is a view over feature records + time commitments, never the record; the roadmap-first ProductPlan pole still holds items with status/progress + tracker sync.
2. **product-discovery-platform** (processed 2026-09-09): flagged the center-of-gravity seam with product-management-platform and product-roadmap-application; its side-position: "A roadmap application's unit of record is the plan/roadmap itself."

## Initial Boundary

Initial hypothesis: a Product Roadmap Application is a tool whose center is the **roadmap artifact** — a maintained, time-ordered plan of initiatives for a product (or portfolio of products), organized for communication to stakeholders. Neighbors to test:

- Product Management Platform (plan of record + delivery coordination; roadmap as a view)
- Product Discovery Platform (idea decision workspace)
- Requirements Management Platform (specs for committed work)
- Project/Agile PM (generic work execution)
- Project Portfolio Management (investment governance)
- Presentation/diagramming/whiteboard tools (one-shot roadmap graphics)
- Generic Gantt/timeline charting tools

Key tension to resolve: the market population of "roadmap tools" includes both roadmap-first standalone products and record-backed PM platforms with roadmap views. Is this one Type with two architectures, or a PM-platform alias?

## Research Questions

1. What is the unit of record — the roadmap artifact itself, or feature records that roadmap views visualize? (THE joint-review question)
2. What objects exist: roadmap, bar/item/entry, lane/swimlane/container, milestone/key date, view, version, portfolio view, legend?
3. What is the primary loop: plan construction → maintenance → communication?
4. Is delivery coordination (tracker sync) definitional or an input integration?
5. Who builds roadmaps, and who are the audiences? How do audience-specific views work?
6. What access/permission models surround sharing?
7. What time semantics exist (granularity, date-less buckets, fiscal years)?
8. Where exactly is the seam vs Product Management Platform, Product Discovery Platform, and generic timeline/Gantt/presentation tooling?

## Representative Products

Selected for market representativeness, documentation quality, and coverage of the architecture spectrum:

| Product | Pole | Why sampled |
|---|---|---|
| **ProductPlan** | roadmap-first standalone (the market's original "roadmap software" pole) | dedicated roadmap tool; Tier 1 support center accessible |
| **Tempo Strategic Roadmaps (Roadmunk)** | roadmap-first standalone #2 | dedicated roadmap tool, now inside Tempo's portfolio; deep Tier 1 docs |
| **Aha! Roadmaps** | suite-straddle (roadmap product inside a PM suite) | Aha! sells Roadmaps as a separate product from Ideas/Discovery — the vendor-drawn seam case |
| **airfocus (by Lucid)** | middle pole (prioritization + roadmaps inside an item/workspace model) | item/field/view architecture; help center migrated to Lucid |
| **Productboard** | counter-pole (PM platform with roadmap-as-view) | confirms the record-backed architecture from this side; also sampled by the PM-platform pass |

ProdPad (outcome-roadmap pole) was sampled by the product-management-platform pass; its evidence is reused via that pass's research notes rather than re-fetched.

## Sources

Research date: **2026-09-09**. All fetches live.

Tier 1 (official operational documentation):

- ProductPlan Support Center — https://support.productplan.com/ (sections: Roadmapping, Strategy, Launch, Product Intelligence)
  - Your Roadmap Taxonomy — https://support.productplan.com/your-roadmap-taxonomy
  - Getting Started Guide — https://support.productplan.com/getting-started-guide
  - Sharing Your Roadmap — https://support.productplan.com/sharing-your-roadmap
- Tempo Help Center, Strategic Roadmaps (Roadmunk) — https://help.tempo.io/roadmaps/latest
  - Roadmaps (section) — https://help.tempo.io/roadmaps/latest/building-roadmaps
  - Roadmapping Basics — https://help.tempo.io/roadmaps/latest/roadmapping-basics
  - Views — https://help.tempo.io/roadmaps/latest/views
  - Exploring the Item Card — https://help.tempo.io/roadmaps/latest/exploring-the-item-card
  - Publishing Roadmaps — https://help.tempo.io/roadmaps/latest/publishing-roadmaps
  - Working with Version Control for Roadmaps — https://help.tempo.io/roadmaps/latest/working-with-version-control-for-roadmaps
- Productboard Support — https://support.productboard.com/
  - Fundamentals of Productboard — https://support.productboard.com/hc/en-us/articles/27858826222355-Fundamentals-of-Productboard
  - Quick start guide: Roadmaps — https://support.productboard.com/hc/en-us/articles/29983922254739-Quick-start-guide-Roadmaps
- Lucid Help Center, airfocus section (article index) — https://help.lucid.co/hc/en-us/categories/14652566349972

Tier 2 (official product pages):

- ProductPlan — https://www.productplan.com/
- Tempo Strategic Roadmaps (formerly Roadmunk) — https://roadmunk.com/ (migrated to tempo.io)
- Aha! Roadmaps — https://www.aha.io/product/roadmaps (note: /roadmaps 404'd; corrected URL used)
- airfocus — https://airfocus.com/

Sibling-pass research notes used as counterparty context:

- research/product-management-platform.md (§Boundary Findings, §Final Synthesis)
- research/product-discovery-platform.md (§Boundary Findings, §Final Synthesis)

Source-access limitations:

- airfocus individual help articles were not read (help center migrated into the Lucid Help Center); the airfocus item/workspace/field/view model rests on the Lucid help article index (Tier 1 titles) plus Tier 2 marketing. Same limitation was recorded by the product-discovery-platform pass.
- Aha! support knowledge base was not fetched; Aha! evidence is Tier 2 (product page) plus the sibling pass's prior Aha! evidence.
- Roadmunk marketing pages now live under tempo.io after the Roadmunk→Tempo migration; product naming ("Strategic Roadmaps (formerly Roadmunk)") confirmed from both surfaces.

## Product A — ProductPlan

### Key observations (evidence layer A unless noted)

**Roadmap-centric object hierarchy (Tier 1, Getting Started Guide):** "ProductPlan has a built in hierarchy of information (**Roadmap > Lanes > Containers > Bars**)." The Portfolio View sits at the top, combining multiple roadmaps.

- **Lanes** — high-level categories: teams, products/sub-products, strategic goals.
- **Containers** — group related bars: themes, releases, epics, long-term projects.
- **Bars** — "your specific initiatives... stories, projects, tasks, or any other initiatives or deliverables."
- **Legend** — color semantics answering "what are you communicating": Strategic Goals, Status, Priority, Phases; admins can create a **shared legend** applied across roadmaps for standardization.
- **Tags** — flexible categorization (product owners, geographies, teams, release dates, dependencies, status); filtering by tags creates audience-specific views.
- **Custom Dropdown Fields** — admin-created standardization fields, single/multi-select, applied across all roadmaps.
- **Custom Views** — saved views sorting by Lanes/Legends/objectives/tags/custom fields, shared with different audiences.
- **Portfolio Views** — consolidate multiple roadmaps into one view; common uses: one roadmap per product, one per PM, version-based before/after comparisons.

**Layouts (Tier 1):** default **Timeline** or **List** (Kanban-style columns organized by completion date — Quarters/Months/Sprints/Tags/Objectives/custom fields); per-user toggles between Timeline / List / **Table Layout** / **Prioritization Board** ("This feature is a unique experience for each user"). Time granularity guidance: start at Months/Quarters; custom views for Sprint/Weekly.

**Planning flow (Tier 1):** "How do the **Parked Section, Planning Board and Roadmap** fit together? Collectively, these three components will help you plan, build and communicate your strategy... move information from your backlog to planned." So ProductPlan carries a backlog/parking layer and a prioritization board feeding the roadmap — but the roadmap is the hub the guide is organized around.

**Sharing (Tier 1, Sharing Your Roadmap):** "You can securely share your Roadmap or **Version**..." Editor vs Viewer access; invited non-users get View Only accounts; **Private Links** (no sign-in); **embedding** in webpages, Confluence, Jira, ADO, MS Teams; **Roadmap Folders**; "Roadmaps are private until shared."

**Versions:** first-class — roadmap *versions* are shareable objects and portfolio-view inputs ("Create a version of your roadmap at the beginning and end of a quarter... Combine these together with one color per roadmap").

**Strategy & other modules (Tier 1 index):** Strategy (Objectives & Key Results) recommended before roadmapping; Launch Management ("plan, track and communicate your upcoming launches that live alongside your roadmaps"); Initiatives; Product Intelligence (research surveys, ideas + signals).

**Integrations (Tier 2 + support index):** real-time Jira and Azure DevOps integrations; "Parent/child relationships maintained across initiatives, epics, and stories in Jira, ADO, and ProductPlan in real-time"; unassigned-work drawer for dragging items onto the roadmap.

**Positioning (Tier 2):** self-labels "Product Intelligence Platform" (2026); roadmap software heritage ("860K roadmaps built", "23M+ initiatives planned"); comparison table claims are marketing and were not used as structural evidence.

## Product B — Tempo Strategic Roadmaps (Roadmunk)

### Key observations

**Roadmap-as-container with items and views (Tier 1, Views article):** "The true power of Strategic Roadmaps is the ability to create **multiple visualizations of your roadmap items** tailored to specific needs and audiences... Strategic Roadmaps has two types of visualization: **Timelines and Swimlanes**. Visualizations are saved as **roadmap views**, each with its own set of filters and pivots."

- **Timelines** — "the more traditional way of visualizing a roadmap, showing a time-oriented view of items such as initiatives and objectives **punctuated by milestones**"; pivot on up to two fields as headers; color and label fields; time scale weeks/months/quarters/years.
- **Swimlanes** — "a 'no-dates' roadmap or a more agile roadmap... pivoted on themes, sprints, or epics"; can use coarse time periods (Quarter/Year) or **time buckets** ("e.g., Soon or Future") as the "time" pivot.
- **Table view** also exists.

**Item model (Tier 1, Exploring the Item Card):** every item has an **Item Card** holding all of the item's data:

- Context Sub-Panel: Overview (description + attachments), **Linked Items** (In-Roadmap, Cross-Roadmap, and Integrated item links), **Sub-Items** (parent/child), **Ideas** (connected ideas).
- Details Sub-Panel: **Fields** (Dates, **Buckets**, **Key Dates**, assigned field values), **Activity** (update log + comments).
- Field order is roadmap-specific and retained in published views and portfolio views.
- Published roadmaps show context + fields but **not** the Activity tab or internal comments.

**Publishing (Tier 1 section):** Sync roadmaps to calendars; add company logo & vision statement; export data to CSV; **publish roadmaps to URL, PNG, or HTML**; embed in Confluence.

**Version control (Tier 1):** "create version control of your roadmaps **using naming conventions and sharing permissions**" — i.e., duplicate the roadmap, rename by date/version/audience, restrict permissions on the original. Roadmap-level change tracking "is not available yet." So Roadmunk's versioning is a documented manual practice, not a first-class version object (contrast ProductPlan).

**Feedback & Ideas (Tier 1 doc tree + Tier 2):** Idea Manager — "log your team's ideas and move them in and out of your roadmap"; feedback collection linked to ideas; prioritization frameworks/templates; "Create a customer-driven backlog... by linking collected feedback to ideas."

**Permissions (Tier 2 FAQ):** Account admins / Collaborators (create and edit roadmaps) / Reviewers (submit feedback, view and comment); "stakeholders without a Roadmaps license have unlimited access to viewing exported roadmaps."

**Integrations (Tier 2):** Jira, Azure DevOps, Asana, Monday.com, Trello, GitHub, GitLab, SSO; "Convert your Jira data into a live roadmap" (with Structure PPM).

**Positioning (Tier 2):** "Roadmapping software for teams of all sizes... boardroom-ready roadmaps. Capture customer feedback, prioritize what to build next, and build impressive roadmaps to communicate your strategy." "Create multiple roadmap views from the same dataset." Portfolio roadmaps: "Roll up multiple roadmaps into one shareable view."

## Product C — Aha! Roadmaps

### Key observations

**Record-backed roadmaps (Tier 2 product page):** "Drag and drop goals, initiatives, releases, and features into place — then adjust the details until everything looks right. **As you add and move bars around, you also create and link real product data within your account.**" Roadmap bars are linked to records (goals/initiatives/releases/features) — the suite's record model underlies the roadmap.

**Roadmap types (Tier 2):** portfolio roadmap ("coordinating release plans across multiple products... even if those releases belong to different business units"); strategic roadmap ("top-down view of your initiatives... Color the bars by status and show which goals the initiatives link to"); **Now, Next, Later roadmap** ("summarizing early product plans without promising specific delivery dates... Automatically group features into now, next, and later buckets"); features roadmap ("Choose exactly which releases and features you want to show"); custom roadmap ("customize just about everything — including what you want to display, start and end dates, and how you group your roadmap bars. Add color and key milestones").

**Communicate triad (Tier 2):** Visualize ("visual timeline for achieving your plans") / Customize ("Set the time frame and choose exactly what details to display") / Communicate ("Share your roadmap as an image, PDF, or secure webpage").

**Suite context (Tier 2 nav):** Aha! Roadmaps product includes Strategy, OKRs, Frameworks, Ideas, Whiteboards, Prioritization, Prototypes, Requirements, Capacity, Dependencies, Releases, Roadmaps, Reports, Presentations, Documents, AI assistant. Aha! sells Roadmaps as a separate product from Aha! Ideas and Aha! Discovery (vendor-drawn seam, consistent with the sibling passes' evidence).

## Product D — airfocus (by Lucid)

### Key observations

**Item/workspace/field/view architecture (Tier 1 help index via Lucid Help Center):** Workspaces (with item types + hierarchy, workspace groups, **portfolios** centralizing items from multiple workspaces), Items (activity log, item links, Docs), Fields (status, time period, people, single/multi-select, t-shirt sizing), Views (list, **timeline**, chart, document, dashboard), Apps (Priority Ratings, Capacity Planning, **Portal**, Item Mirror, Insights), Integrations (Jira, Azure DevOps, MCP server, webhooks, Zendesk...), Collaborate ("Share priorities and roadmaps in airfocus").

**Positioning (Tier 2):** "The Intelligent Product Management Tool" / "Product Intelligence Platform"; modules: Objectives & OKRs, **Roadmaps** ("Align your team and set a clear direction"), Prioritization, Feedback & Insights, Portal. Roadmaps are one module of an item-model PM tool — the middle pole between roadmap-first and record-backed-grid.

Evidence caveat: individual help articles not read (Lucid migration); model asserted at existence level from the Tier 1 article index.

## Product E — Productboard (counter-pole)

### Key observations

**Boards are views; the hierarchy is the record (Tier 1, Fundamentals):** "A board is a set of tools and filters that help you answer a question... **Creating, duplicating, or deleting a board has no effect on the data it displays.**" The **product hierarchy** (Products > Components > Features > Subfeatures) is "the backbone of your workspace... you can't use Productboard without it." "Data is anything used to describe an aspect of an entity... Like entities, data is universal."

**Roadmaps = timeline + columns boards (Tier 1, Quick start guide: Roadmaps):** "two board types (**timelines** and **columns**) are specialized for communicating plans to internal audiences. We'll refer to both board types together as **roadmaps**." Roadmaps can center on any item type: Objectives, Initiatives, Products/Components/Features, Releases ("Milestones, launch phases, or abstract time measurements (like Now-Next-Later)"). "**The data you see on roadmaps are the same data you see on other boards**, so changing data in one place will change it in the other. **It's usually better to edit and organize your data on grid boards, then use roadmaps for visualization and alignment.**" "Roadmaps aren't designed for external communication, but portals are."

**Audience-first method (Tier 1):** "Who is this roadmap built for?... What will they want to learn from it?... How much detail do they need?" Board controls: layout, items, filters, columns, groups (swimlanes), granularity; card attributes customization; roadmaps inherit access from teamspaces.

**Vendor-drawn boundaries (Tier 1, Fundamentals):** "Features aren't feedback"; "Subfeatures aren't bugs... You're better off doing that in a project management tool like Jira."

## Cross-product Comparison

| Dimension | ProductPlan | Roadmunk (Tempo) | Aha! Roadmaps | airfocus | Productboard |
|---|---|---|---|---|---|
| Roadmap artifact | first-class container (Roadmap > Lanes > Containers > Bars) | first-class container (roadmap → items → views) | roadmap views linked to suite records | timeline view over workspace items | timeline/columns boards over the product hierarchy |
| Unit of record | the roadmap (bars created on it) | the roadmap (items created on it) | suite records (goals/initiatives/releases/features) | items in workspaces | features in the product hierarchy |
| Entry time semantics | timeline granularity (months/quarters; custom sprint/weekly views); list columns by completion date | dates, Buckets (Soon/Future), Key Dates; weeks→years scales | dates, releases, Now-Next-Later buckets | time period fields | dates/date ranges; releases incl. abstract buckets (NNL) |
| Grouping scheme | Lanes + Containers | swimlanes + pivots (two header fields) | grouping configurable per roadmap | workspace hierarchy + groups/swimlanes | swimlanes/groups + columns |
| Color/meaning layer | Legend (goals/status/priority/phases; shared legend) | color-by-field in views | color bars by status | field-driven | status shapes; card attributes |
| Audience views | Custom Views shared per audience; per-user layout toggles | saved views with filters/pivots; lockable | "tailor it to specific audiences" | views + Portal app | boards saved/shared; teamspace access; portals for external |
| Sharing/publishing | Share dialog, View Only invites, private links, embeds (Confluence/Jira/Teams), folders | publish to URL/PNG/HTML, calendar sync, CSV export, Confluence embed, logo/vision branding | image, PDF, secure webpage | share priorities and roadmaps; Portal app | shared board links; portals for external audiences |
| Portfolio roll-up | Portfolio View (combine roadmaps; version-based comparisons) | Portfolio roadmaps (roll up multiple roadmaps) | portfolio roadmap across products | portfolios centralizing workspaces | (hierarchy spans products; no separate portfolio-object evidence this pass) |
| Versions | first-class Version objects (shareable, portfolio inputs) | manual duplicate + naming conventions (documented practice) | not evidenced this pass | not evidenced this pass | not evidenced this pass |
| Ideas/feedback capture | Ideas + Signals module; Parked Section | Idea Manager (ideas in/out of roadmap; feedback linked) | Aha! Ideas as separate product | Insights app | insights (feedback) boards |
| Prioritization layer | Planning Board / Prioritization Board | prioritization frameworks in Idea Manager | Prioritization module | Priority Ratings app | Grid boards |
| Strategy linkage | Strategy module (Objectives & Key Results) | (not evidenced this pass) | goals/initiatives linkage | Objectives & OKRs module | Objectives as item type |
| Tracker sync | Jira + Azure DevOps real-time; parent/child maintained | Jira, ADO, Asana, Monday, Trello, GitHub, GitLab | Jira two-way (suite integrations) | Jira, ADO, webhooks | Jira sync (status flows to features) |
| Delivery-coordination center? | no — sync feeds the roadmap | no — sync feeds the roadmap | partial (suite spans plan→develop) | no | no — explicitly pushes bugs/tasks to Jira |
| External-audience posture | private links + embeds; View Only accounts | published URLs; reviewers; unlicensed viewers of exports | secure webpages | Portal app | portals (roadmaps explicitly internal) |

### Stable commonalities (B-layer, cross-product)

1. A persistent, named, shareable **roadmap artifact** is the object of work in every sampled product (container in ProductPlan/Roadmunk; saved board/view in Productboard/Aha!/airfocus).
2. **Plan entries positioned in time** — dates/date-ranges or time buckets (Now/Next/Later, Soon/Future) — grouped by lanes/swimlanes/containers/columns.
3. **Audience-specific views** over the same underlying plan data, with filters/pivots and saved state.
4. **Communication channels as first-class surfaces**: share dialogs, live links, embeds, image/PDF/HTML export, calendar sync, CSV.
5. **Role ladder separating builders from viewers/commenters** (editor/viewer; collaborator/reviewer; teamspace inheritance; view-only accounts).
6. **Status/progress semantics on entries** (legend colors, status fields, color-by-status).
7. **Milestones/key dates** (Roadmunk Key Dates + timeline milestones; Aha! milestones; ProductPlan containers/bars usage includes milestone-like grouping).
8. **Portfolio roll-up** of multiple roadmaps (ProductPlan, Roadmunk, Aha!; airfocus portfolios at workspace grain).
9. **Tracker integrations** pulling delivery data onto the plan (all five).
10. **Capture layers feeding the plan** (ideas/feedback/parked backlogs) — present in all five, weighted differently.

### Architecture split (the key finding)

Two realizations of the same Type:

- **Roadmap-as-container** (ProductPlan, Roadmunk): entries are created on the roadmap; the roadmap is created, duplicated, versioned, shared, published, and combined — the roadmap IS the record container. No separate feature population exists that roadmap views merely visualize.
- **Roadmap-as-view** (Productboard, Aha! Roadmaps, airfocus): records live in a product/workspace hierarchy; the roadmap is a saved view/board over those records; editing data on the roadmap edits the records everywhere.

Both keep the roadmap artifact as the persistent, shareable object of work — the difference is where the record layer lives. This split is the seam vs the Product Management Platform.

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as a Product Roadmap Application:

1. **The roadmap as a maintained plan artifact of record** — a persistent, named, owned plan object that users create, organize, maintain over time, and revisit; the roadmap is the object of work (as container or as saved view over plan records). Remove → a feature list/backlog with no plan artifact, or a PM platform where the roadmap is incidental.
2. **Time-positioned plan entries with grouping** — the roadmap holds entries (initiatives/bars/items) each carrying identity, a time placement (dates/ranges or coarse buckets like Now/Next/Later), and a grouping scheme (lanes/swimlanes/containers) with a color/meaning layer. Remove → a strategy list or goal list with no time dimension — not a roadmap.
3. **Audience-facing communication of the plan** — the roadmap is built to be shown: audience-specific views/filters, share/publish channels (live links, embeds, image/PDF/HTML), and viewer/commenter access for non-editing stakeholders. Remove → a private planning grid or internal plan document — PM-platform grid or spreadsheet territory.

Jointly-held load-bearing:

- 1 alone = an empty plan shell / a private plan document
- 2 without 1 = a one-shot timeline graphic (presentation/Gantt-drawing pole; nothing maintained behind it)
- 3 without 1+2 = a communication surface with no plan behind it
- 1+2 without 3 = a private planning grid (PM-platform grid / spreadsheet roadmap nobody sees)
- 1+3 without 2 = a dashboard with no time-positioned plan
- 2+3 without 1 = a static roadmap picture (slide/Office-timeline pole)

### L1 — Common Mature Structure

- milestones / key dates
- status & progress on entries
- portfolio roll-up of multiple roadmaps
- tracker integrations (Jira/Azure DevOps-class) pulling delivery data onto the plan
- idea/feedback capture feeding the plan
- prioritization/backlog layers (parked sections, planning boards, scoring)
- strategy/objective linkage
- CSV export, calendar sync
- permission ladders (editor/viewer/reviewer; teamspace inheritance)
- saved views with filters/pivots; per-user layout state

### L2 — Variant / Optional Structure

- version snapshots (first-class version objects in some products; manual duplicate-and-rename practice in others — uneven, do not canonicalize)
- Now/Next-Later date-less horizon style vs date-committed style
- external-audience posture (published URLs vs portals vs private links)
- launch management, presentations, OKR modules, capacity planning, AI assistance, portals
- deployment posture (SaaS-dominant in-sample; no self-host pole sampled)

### L3 — Vendor-specific (research notes only)

- ProductPlan: Roadmap > Lanes > Containers > Bars hierarchy; shared legends; Parked Section/Planning Board; first-class Versions; Launch Management; Strategy module; per-user layout toggles; "Product Intelligence Platform" rebrand; marketing counters (860K roadmaps, 23M+ initiatives).
- Roadmunk/Tempo: Item Card sub-panels (Context/Details); Buckets and Key Dates field types; publish to URL/PNG/HTML; calendar sync; logo/vision branding; version control as documented naming-convention practice; reviewer role; unlicensed viewers of exports; description limit 10,000 chars and 10MB/file attachment limit (precise limits — not for the final document); Idea Manager.
- Aha!: record-linked bars ("as you add and move bars around, you also create and link real product data"); roadmap type gallery (portfolio/strategic/NNL/features/custom); suite split (Roadmaps vs Ideas vs Discovery vs Develop); Elle AI; presentations.
- airfocus: workspaces/item types/portfolios; Priority Ratings, Capacity Planning, Portal, Item Mirror, Insights apps; MCP server; Lucid acquisition and help-center migration.
- Productboard: boards-vs-data doctrine ("creating... a board has no effect on the data"); one product hierarchy; no undo; teamspaces; Spark AI; portals for external; "roadmaps aren't designed for external communication."

## Vendor-specific Findings

- Vendor self-labels are unreliable for typing: ProductPlan now self-labels "Product Intelligence Platform"; airfocus self-labels "product management tool"; Aha! sells "Roadmaps" as a suite product. Typing must follow structure, not labels.
- ProductPlan and Roadmunk — the two roadmap-first poles — both carry thin record semantics on entries (fields, status, owners, sub-items, Jira sync). "Pure artifact with no records" does not exist in-sample; the correct discriminator is roadmap-as-container vs roadmap-as-view, not "artifact vs records."
- Versioning is uneven: ProductPlan first-class versions vs Roadmunk's documented manual practice. Held at L2.
- Productboard explicitly routes external sharing to portals and calls its roadmaps internal-communication boards — an audience-posture variant, not a Type difference.

## Rejected Findings

- **"The roadmap application is just a PM platform alias."** Rejected: roadmap-first poles exist where the roadmap is the container and the object of work (ProductPlan's own hierarchy; Roadmunk's roadmap→items→views with publishing as a top-level concern). Confirmed the sibling pass's open question affirmatively — see Boundary Findings.
- **"The roadmap is the unit of record in ALL roadmap tools."** Rejected as universal: in Productboard/Aha!/airfocus the record layer lives outside the roadmap. The invariant is the maintained roadmap artifact as the object of work; the container-vs-view split is the architecture axis.
- **"Delivery coordination (tracker sync) is definitional."** Rejected: sync is an input integration feeding the plan in the roadmap-first poles; the plan-to-delivery coordination loop (delivery status flowing back into a committed plan of record) is the PM platform's defining loop. Paper/spreadsheet-era roadmaps satisfy the Type with no sync.
- **"Versions are definitional."** Rejected: uneven across the sample (first-class vs manual practice).
- **"Portfolio roll-up is definitional."** Rejected as L0: single-roadmap usage satisfies the Type; roll-up is common mature structure.
- **"Idea/feedback capture is definitional."** Rejected: capture layers are optional and vary from module (Roadmunk Idea Manager) to separate product (Aha! Ideas); the decision-workspace machinery belongs to Product Discovery Platform.
- **"A roadmap application must be visual/timeline-first."** Rejected: list/table layouts and date-less bucket roadmaps are first-class in-sample (ProductPlan List View; Roadmunk swimlanes "no-dates"; Aha! NNL). The invariant is time placement (dates OR buckets), not a visual timeline per se.

## Boundary Findings

1. **vs Product Management Platform (§12 sibling, processed 2026-09-09) — JOINT REVIEW DISCHARGED from this side.** The sibling's open question — "does a pure roadmap-artifact tool without the feature-record core exist?" — is answered **yes, with a refinement**: ProductPlan and Roadmunk hold the roadmap as the primary container/record (ProductPlan: "built in hierarchy of information Roadmap > Lanes > Containers > Bars"; Roadmunk: items created on roadmaps, publishing as a top-level concern, roadmap duplication/versioning/sharing as the core operations). No separate feature population exists that their roadmap views merely visualize. The refinement: these poles are not record-free artifacts — entries carry fields/status/owners and tracker sync — so the seam is not "artifact vs records" but **roadmap-as-record-container + communication center vs feature-record plan-of-record + delivery-coordination center**. In the roadmap application the primary loop is build → maintain → communicate the plan; tracker sync is an input. In the PM platform the primary loop is plan-to-delivery coordination; the roadmap is one view over feature records (Productboard: "better to edit and organize your data on grid boards, then use roadmaps for visualization and alignment"). **Keep-both RATIFIED**; the market population is a gradient (Aha! sells Roadmaps beside Ideas/Discovery; Tempo sells Strategic Roadmaps beside Structure PPM; vendors self-label loosely), and the seam is the center of gravity, not a hard wall. This refines the sibling pass's sketch ("remove the delivery-coordination loop, keep only the communication artifact → roadmap territory") — the roadmap application is not a mere communication artifact; it holds plan entries as records.
2. **vs Product Discovery Platform (§12 sibling, processed 2026-09-09) — seam confirmed from this side.** In roadmap applications, ideas/feedback (Roadmunk Idea Manager, ProductPlan Ideas/Parked Section) are capture layers feeding plan entries; there is no comparative-evaluation machinery or recorded build/don't-build decision lifecycle as the center. The discovery pass's side-position ("a roadmap application's unit of record is the plan/roadmap itself") holds for the roadmap-first poles and is refined by the container-vs-view split for record-backed products. No conflict with the ratified keep-both.
3. **vs Requirements Management Platform (§12 sibling, UNPROCESSED).** Roadmap applications hold plan lines (initiatives/bars), not specifications; no spec/requirement objects surfaced in any sampled product's roadmap core. Seam noted for that pass; nothing to discharge from this side.
4. **vs Project Management Application / Agile PM / Gantt charting (§03.07/§12).** Generic project execution centers tasks/schedules/dependencies per project; roadmap applications center the product plan artifact and its communication. Generic Gantt/timeline tools can draw roadmap-shaped pictures but lack the maintained product-plan semantics (legend/status/ownership/audience views) — canonical inference (C-layer), adjacent pole not fetched.
5. **vs Project Portfolio Management (§03.07, processed).** PPM governs investment across projects (funding, gates, run-state); roadmap applications communicate product plans. Portfolio *views* in roadmap tools roll up plan artifacts for visibility; they do not govern investment. Seam consistent with the PPM pass's investment-loop center.
6. **vs Presentation/Diagramming/Whiteboard tools.** One-shot roadmap graphics (slides, whiteboard templates) lack the maintained artifact + record layer; the roadmap application's artifact persists, is maintained against reality, and is re-served live. Adjacent pole (Office-Timeline-class) not fetched — held as canonical inference.
7. **vs Customer Feedback Management (§07, processed).** Feedback items are evidence inputs; roadmap entries are plan lines. Consistent with the CFM pass's "feedback item ≠ planned work item."
8. **"去掉什么就变成另一个 Type" 判据：** remove the roadmap-as-container and add the delivery-coordination loop over feature records → Product Management Platform; remove the plan center and add evaluation/decision machinery over ideas → Product Discovery Platform; remove product-plan semantics (generic tasks/projects, dependencies/critical path) → Project Management / Gantt territory; remove the maintained record layer (one-shot graphics) → presentation/diagramming tooling; move the center to investment governance → Project Portfolio Management; move the center to precise specifications → Requirements Management Platform.

## Historical / Market-Sample Check

- **Paper-era roadmap**: a wall chart or slide deck of initiatives laid across quarters, maintained by the product lead, presented in roadmap reviews — satisfies all three L0 structures with no software, views machinery, or integrations.
- **Spreadsheet-era (2000s) practice**: an Excel roadmap (rows = initiatives, columns = quarters, color = status) circulated to executives and updated after each planning cycle — satisfies; the spreadsheet was the maintained artifact, entries were time-positioned rows, circulation was the communication. (Consistent with the PM-platform pass's spreadsheet-roadmap lineage note.)
- **Gantt lineage**: the roadmap timeline descends from Gantt-chart practice; the Type is definable without any specific visual machinery (list layouts and date-less buckets are first-class in-sample).
- **Poles all fit**: roadmap-first standalone (ProductPlan, Roadmunk), suite roadmap product (Aha! Roadmaps), item-model middle pole (airfocus), record-backed counter-pole (Productboard) — none require era-specific machinery in the core.
- Conclusion: the definition is era-robust; nothing in L0 names cloud, AI, views machinery, or any specific framework. The historical check passes.

## Uncertainties

- airfocus individual help articles not read (Lucid migration); its model rests on the Tier 1 article index + Tier 2 marketing. Existence-level only; no operational claims made.
- Aha! support KB not fetched; the record-linked-bars finding rests on the Tier 2 product page plus the sibling pass's prior Aha! evidence. No precise Aha! workflow claims made.
- ProductPlan version mechanics (how versions are created/snapshotted) not step-verified; existence-level from the Sharing and Getting Started articles.
- Roadmunk scenario planning: no direct evidence in fetched docs; not claimed.
- Craft.io, Dragonboat, ProdPad roadmaps not fetched this pass (ProdPad covered by the PM-platform pass); the sample lacks an outcome-roadmap-first pole fetched first-hand.
- The adjacent presentation/Gantt-tool pole (Office-Timeline-class) not fetched; the boundary judgment there is canonical inference, held at reduced strength.
- Self-hosted/on-prem roadmap tools not sampled; deployment posture held as uncertainty.
- Roadmap-level change history: Roadmunk documents item/field activity feeds but states roadmap-wide change tracking "is not available yet"; ProductPlan/Productboard roadmap-level audit not evidenced this pass. Held as uneven/uncertain.

## Final Synthesis

A Product Roadmap Application is the product organization's **plan-communication system**: its center is the **roadmap** — a persistent, maintained plan artifact holding **time-positioned plan entries** (initiatives/bars/items placed on dates or coarse time buckets, grouped into lanes/swimlanes/containers with a color/meaning layer) — and its defining loop is **build → maintain → communicate**: entries are created or pulled in from trackers and idea capture, the plan is adjusted against reality, and audience-specific views are shared live (links, embeds, exports, presentations) with viewer/commenter access for stakeholders. The Type realizes two architectures: **roadmap-as-container** (dedicated roadmap tools where entries are created on the roadmap and the roadmap is duplicated, versioned, published, and rolled up into portfolios) and **roadmap-as-view** (roadmap boards saved over plan records inside broader product-management tools). Mature products add milestones, status/progress, portfolio roll-ups, tracker sync, idea/feedback capture, prioritization boards, strategy linkage, versions, and permission ladders — none of which define the Type. The seam vs the Product Management Platform is the center of gravity: the roadmap application's record container is the plan artifact and its loop ends in stakeholder communication; the PM platform's record is the feature and its loop ends in shipped work. The seam vs the Product Discovery Platform: ideas feed the plan here; ideas are decided there.
