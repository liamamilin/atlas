# Research Notes — Artwork Consignment Management

Research date: 2026-09-06
Slug: `artwork-consignment-management`
Directory leaf: "Artwork Consignment Management" (§27 Media, Entertainment, Creator & Culture)

---

## Research Goal

Understand what software for managing artwork consignments actually does — its central objects, workflows, states and rules — well enough to write a vendor-neutral Application Document, and to resolve the boundary question flagged by the art-gallery-management pass: is a standalone consignment-management Type supported by the market, or is consignment always a module/capability inside gallery and artist suites?

## Initial Boundary

Working hypothesis before research:

- Artwork consignment = an owner (artist, estate, collector, or another dealer) places specific works with a seller (gallery, dealer, representative, auction house) who does not take ownership; the seller sells or exhibits on the owner's behalf under recorded terms (commission split, duration, return conditions), and the owner is owed the consignor share when a work sells.
- The software, if standalone, would center the consignor↔consignee relationship: consignment agreements/lists, consign-in and consign-out, per-work consignment status, returns, sale attribution, settlement.
- Nearest neighbors: Art Gallery Management (consignment as one module), Consignment Management Platform (general resale, non-unique goods), Museum Loan Management (custody movement without commercial split), Auction Management System (lot-based consignor relations), Artist studio/portfolio tools (consignor side), CRM.
- Prior flag (research/art-gallery-management.md §Boundary Findings): in all 3 sampled gallery products consignment is one module inside the full inventory/CRM/sales world; structural test = strip inventory, clients and direct sales, keeping only the consignment relationship.

## Research Questions

1. Who operates consignment software, and from which side of the relationship (consignor vs consignee)?
2. What is a consignment record: agreement, list of works, terms, dates?
3. What is the lifecycle of a consigned work: offered → accepted → delivered/received → on consignment → sold / returned → settled?
4. How are terms modeled (commission percentages/splits, per-artist defaults, per-work overrides)?
5. How does settlement work: amounts due to the consignor, payment tracking, statements?
6. How are movements and custody tracked (locations, check-in/check-out, third-party placement)?
7. Do standalone products exist, or is the capability always packaged inside gallery/artist suites?
8. What does the consignor-side experience look like (connected accounts, portals, submissions)?
9. Historical check: would older, spreadsheet- or FileMaker-era consignment tracking satisfy the same core?

## Representative Products

Selected for market representability, documentation quality, different geographies/tiers and different sides of the relationship:

| Product | Geography / tier | Philosophy | Side sampled | Evidence accessed |
|---|---|---|---|---|
| **ArtCloud** | US; galleries + artists (also jewelry vertical) | All-in-one manager with **connected artist accounts** — both sides of the consignment in one system | Consignee + consignor | Tier 1 Knowledge Base (Consignment section, Receive & Manage Artist Consignments, Send a Gallery Consignment) + Tier 2 product pages |
| **Artlogic** | UK; solo dealer → large galleries; artist & collector editions | All-in-one platform; consignment tracked as a basis layer over owned stock; settlement via payables fields/reports | Consignee (+ artist edition) | Tier 1 Support article (Artist Payables / Advanced Reports) + Tier 2 product pages (gallery + artist) |
| **Art Galleria** | AU/global; SMB tiers for galleries and artists | Cloud art-inventory database first; consignments as tracked movements with reports | Consignee + consignor | Tier 2 product pages (for-galleries, for-artists) |

Considered and excluded:

- **Artwork Archive** (US; artist-side inventory with consignment tracking): www.artworkarchive.com returned 403 twice (features page and root) → abandoned per network-limitation rule. Recorded as a source-access limitation; no claims about it are made.
- **ArtBinder**: unreachable in the prior gallery pass (two empty responses); not retried.
- **Veevart / Artfundi**: product mismatch (museum operations / collection stewardship) per the prior pass; boundary data points only.
- **General resale consignment products** (retail consignment shops): belong to the Consignment Management Platform leaf (05.19), not sampled here.

Search-engine discovery attempted and abandoned: DuckDuckGo HTML endpoint timed out; Bing returned region-polluted results (no usable hits). No dedicated standalone "artwork consignment" product was identified through reachable official sources; the sampled market implements the capability inside gallery/artist suites.

## Sources

Tier 1 (official operational documentation):

- ArtCloud Knowledge Base — https://help.artcloud.com/knowledge (structure: Manager–Inventory incl. **Consignment** section; Manager–Artists incl. Artist Record–Consignment / –Payments; Analytics incl. **Artist/Consigner Payments**, Commission; ArtCloud for Artists incl. **Gallery Connections and Consignments**)
- ArtCloud KB — "How to Create a Consignment List" — https://help.artcloud.com/knowledge/how-to-create-a-consignment-list (Consignment–Inbound / Third Party Consignment / Inventory Return; terms auto-population; send-to-accept; agreement export)
- ArtCloud KB — "Receive and Manage Artist Consignments" — https://help.artcloud.com/knowledge/receive-and-manage-artist-consignments (accept/deny; record creation; sale notification; return semantics; field-transfer limits; per-account divergence)
- ArtCloud KB — "Send a Gallery Consignment" — https://help.artcloud.com/knowledge/send-a-gallery-consignment (consignor-side creation; gallery connection requirement; sold-inventory caveat)
- Artlogic Support — "How to Create Artist Payables Documents from Advanced Reports" — https://support.artlogic.net/hc/en-gb/articles/15406651760028 ("track your inventory from Consignment to Invoicing to Statement"; Due Consignor field `[consignor_due]`; named tool documented as not-yet-shipped workaround)

Tier 2 (official product pages):

- ArtCloud — https://artcloud.com/manager-for-artists ; https://artcloud.com/consignment-reports
- Artlogic — https://www.artlogic.net/products/artist/management (artist edition: "from creation to consignment, shipping and beyond")
- Art Galleria — https://www.artgalleria.com/for-galleries ; https://www.artgalleria.com/for-artists (Consignments: "Manage consignments with ease. Print or email professional consignment reports. Check-in and check-out artworks to physical locations."; "keep tabs where your artworks are and when they're due back")

Prior in-repo evidence (same products, gallery-side module detail, gathered 2026-09-06):

- research/art-gallery-management.md (Artlogic consignment terms/owners + movement history; Art Galleria consignment reports + check-in/out; ArtCloud consignment contracts, percentages/terms, payments due & paid from invoice history)

Tier 3: none needed beyond the above.

## Product Observations

### ArtCloud

Evidence layer: A (direct, official KB + product pages) unless noted.

Key observations:

- Product packaging: one Manager product line sold to Galleries, Artists, and Jewelry; artist accounts and gallery accounts are **connected** ("ArtCloud Artist Accounts can send and receive inventory from connected Gallery Accounts").
- Consignment Lists are the central consignee-side object, created from the Quicklist dashboard, Inventory dashboard, or a dedicated Consignment dashboard. Three list types:
  - **Consignment – Inbound**: "inventory records coming to the gallery from the Artist or Consigner." Overview carries title, start date, end date (both optional), consigner, and terms. "If you enter the Artist as the Consigner, the Artist's Consignment terms will populate in the terms of the Consignment list automatically" (per-artist default terms stored on the artist record).
  - **Third Party Consignment**: "artworks going to another gallery or representative from the gallery to sell/display artworks on an artist's behalf" — i.e., re-consignment onward. Recipient contact + terms; same creation flow.
  - **Inventory Return**: returning consigned works to the artist/consigner, with return terms (default return-to-artist terms configurable).
- Works are added to a list from inventory; the list can be **sent to the artist/consignee to accept**, and the **consignment agreement can be exported or printed** from the list's actions menu.
- After a third-party consignment, items change location: "the newly consigned artworks will say 'On Consignment' in the location column. You can filter your inventory by items on consignment."
- Connected-account flow (Tier 1): artist sends a Gallery Consignment → gallery receives a notification → a **Consignment Record** is created → gallery can **accept or deny** → on acceptance, **Inventory Records are created for each item** in the gallery account. "You cannot delete the artist's consignment after accepting their inventory."
- Two-sided record divergence: the same work exists in both accounts with different views — artist-side location reads "On Consignment to [gallery name]", gallery-side reads "gallery"; inventory numbers differ per account numbering; gallery-side acquisition date = consignment acceptance day. Edits in one account do **not** propagate to the other ("Communicate with your artists about changes").
- Field-transfer limits on consign-in: signature placement, tags, provenance, private notes, insurance value, shipping price, financial notes, expenses, history do **not** transfer to the gallery-created records.
- Sale attribution: "When you place a consigned piece on an Invoice Record and close the invoice, ArtCloud notifies the artist of the sale. In the artist's account, the item's status updates to inactive, and the location changes from 'On consignment to [gallery name]' to 'Sold by [gallery name].'"
- Returns: "ArtCloud Gallery Accounts cannot directly return inventory to Artist Accounts. Instead, create an Inventory Return Consignment to mark the inventory as 'Returned to Artist.'" The return does not auto-update the artist's account; coordination is procedural.
- Status caveat (Tier 1): "ArtCloud doesn't prevent you from consigning sold inventory. Make sure to communicate the status of any consigned inventory with your gallery."
- Settlement: Consignment Reports page — "Instantly calculate consignment payments… customize and send out specialized consignment reports directly to designers, vendors, or artists via export or email… understanding your profit margin with various splits… simplifying the creation and management of consignment agreements… supporting smoother operations and better consignor relationships." KB Analytics section includes **Artist/Consigner Payments** and **Commission** reports; Artist Record has **Consignment** and **Payments** tabs. Prior gallery-pass evidence: "Track consignment payments due and paid, calculated automatically from invoice history"; "Define consignment percentages and terms for each artist and/or work"; "Send integrated consignment contracts and artwork returns."

### Artlogic

Evidence layer: A (direct, official support article + product pages) unless noted.

Key observations:

- Gallery-side positioning (prior pass, Tier 2): "Artlogic tracks consignment terms, owners, current locations and movement history alongside your owned stock, so you can answer where any work is and on what basis at any moment." Owned stock is the base; consignment is a tracked **basis layer** (owner + terms + location + movement history).
- Settlement (Tier 1): "Artist Payables is a tool that allows you to track your inventory from **Consignment to Invoicing to Statement**. When consigning a new work by an artist, Payables allows you to track what you may owe the artist once the work has been sold." Report fields include Invoice Number, Sale Date, Invoice Value, Sales Tax, **Due Consignor** (`[consignor_due]`). Caveat stated in the article itself: the named Artist Payables tool "is not yet at Artlogic"; the documented path is a workaround via Advanced Reports — the **concept and fields are evidenced**, the named module is not confirmed as shipped.
- Artist edition (Tier 2): studio management covers "your artworks from creation to consignment, shipping and beyond" — the consignor side is packaged inside the artist product line (inventory, contacts, invoicing/payments, documents).
- Prior-pass gallery evidence: consignments and loans as feature bullets; provenance and condition reports; document templates; accounts reports & exports.

### Art Galleria

Evidence layer: A (direct, official product pages).

Key observations:

- Gallery side: "Manage consignments with ease. Print or email professional consignment reports. Check-in and check-out artworks to physical locations." Locations: "galleries, studios, storage places… track where your art is at all times." Consignment reports among the report suite (sales, inventory, consignment, insurance).
- Artist side: "Send your artworks to exhibitions with professional consignments and keep tabs where your artworks are and when they're due back." "Consignment reports: Create professional consignments reports to send to exhibitors and track where your artworks are at all times."
- Artist portals (prior pass): artists submit artwork records directly; gallery reviews, accepts or rejects with workflow support — the intake side of the consignor relationship.
- Settlement computation not directly observed on the fetched pages (consignment reporting is; "payments due" machinery was not evidenced for this product). Treated accordingly in the comparison.

## Cross-product Comparison

| Structure | Artlogic | Art Galleria | ArtCloud | Assessment |
|---|---|---|---|---|
| Consignor (owner) as a tracked party with relationship record | ✔ (consignment owners; artist records) | ✔ (artist profiles; contacts) | ✔ (artist records; connected accounts) | Core (all 3) |
| Consignee placement of specific works under recorded terms | ✔ (consignment terms/owners) | ✔ (consignments; check-in/out) | ✔ (Consignment Lists with terms; per-artist defaults) | Core (all 3) |
| Per-work consignment state / location ("on consignment", where, due back) | ✔ (locations + movement history; "on what basis at any moment") | ✔ ("keep tabs where your artworks are and when they're due back"; check-in/out) | ✔ ("On Consignment" location; filterable) | Core (all 3) |
| Consignment agreement as a produced document | ✔ (consignment terms; document templates) | ✔ ("print or email professional consignment reports") | ✔ (export/print consignment agreement; send to accept) | Common (all 3; formality varies) |
| Returns of consigned works as recorded events | ✔ (consignments & loans; returns) | ✔ (check-in/out; "when they're due back") | ✔ (Inventory Return lists; "Returned to Artist") | Core (all 3) |
| Sale attribution of a consigned work (who sold it; notify consignor) | ✔ (Consignment→Invoicing→Statement chain) | not directly observed | ✔ (invoice close → artist notified; "Sold by [gallery]") | Common (2 of 3 direct; 1 implicit) |
| Settlement: amount due to consignor computed from sales | ✔ (Due Consignor field; statement) | not directly observed (consignment reports only) | ✔ (payments due & paid from invoice history; Artist/Consigner Payments; instant consignment-payment calculation) | Common (2 of 3 direct) — treated as core-adjacent with qualitative wording |
| Commission/split terms per consignor and/or per work | ✔ (consignment terms) | not directly observed | ✔ (percentages & terms per artist and/or work; "various splits") | Common (2 of 3 direct) |
| Third-party / onward consignment (gallery → other gallery) | ✔ ("consignments and loans") | not observed | ✔ (Third Party Consignment list type) | Common (2 of 3) |
| Connected consignor accounts / submission portals | ✔ (artist edition; not a connected-account flow) | ✔ (artist portals: submit → review → accept/reject) | ✔ (connected artist accounts; send/accept consignments) | Common (all 3, different depths) |
| Consignment reporting (shareable with consignors) | ✔ (payables/statement reports) | ✔ (consignment reports to exhibitors) | ✔ (customizable consignment reports; toggle shared columns) | Common (all 3) |
| Two-sided record divergence (per-account views of the same work) | not observed (single-database model) | not observed (single-database model) | ✔ (explicit per-account location/numbering/date semantics) | Vendor-specific (ArtCloud connected-account architecture) |
| Accept/deny gate on incoming consignments | not observed | ✔ (review, accept/reject submissions) | ✔ (accept or deny consignment record) | Common (2 of 3) |
| Block consigning already-sold works | not observed | not observed | ✘ (explicitly not prevented) | Vendor-specific observation |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software is not recognizable as artwork consignment management:

```text
Consignor (owner who retains title to the work)
└── Consignee (party authorized to sell or exhibit on the owner's behalf)
    └── Consignment of specific works (unique items, item-level tracking)
        └── Recorded terms of the placement
            (commercial basis: commission/split; duration; return basis)
        └── Per-work consignment state
            (placed → on consignment at a location → sold or returned)
```

Five invariants:

1. **A consignor who retains ownership** — the work's title stays with the owner until a sale; the software's world is built around this retained-ownership placement. Without it, the software is plain inventory or a purchase/order system.
2. **A consignee authorized to sell or exhibit** — the receiving party acts on the owner's behalf. Without a distinct authorized party, there is no consignment relationship to manage.
3. **Specific works as consigned items** — consignment is tracked per unique work (one record per physical piece), not per SKU. Without item-level tracking it is generic goods consignment, not artwork consignment.
4. **Recorded terms of placement** — the commercial basis (commission/split, duration, return conditions) is part of the managed record. Without recorded terms, custody tracking exists but consignment (a commercial arrangement) does not.
5. **Per-work disposition state ending in sold or returned** — every consigned work is tracked to one of the two terminal dispositions, and the disposition is attributed (which sale, which return). Without disposition tracking, the relationship cannot be operated or settled.

Historical check: a spreadsheet- or FileMaker-era gallery (the ArtBase lineage documented in the prior pass) tracks exactly this core — a consignment list per artist, terms/percentage notes, works out/sold/returned columns, and an owed-to-artist figure. Cloud sync, connected accounts, portals and payment processing are NOT part of the definition.

### L1 — Common Mature Structure

Present in essentially all mature modern implementations; expected by the market but not definitional:

- settlement machinery: amounts due to the consignor computed from recorded sales, payment tracking (due vs paid), statements/payables reports (directly evidenced in 2 of 3 sampled products; reporting-only in the third)
- consignment agreements as generated documents (create, export/print, send for acceptance)
- check-in/check-out and location tracking of consigned works (galleries, studios, storage, fairs, third-party locations)
- third-party / onward consignment (works passed from one seller to another on the owner's behalf)
- per-consignor default terms with per-work overrides (commission percentages, durations)
- consignor records with relationship context (artist/estate/collector profiles)
- connected consignor accounts or submission portals (consignor initiates; consignee reviews/accepts)
- consignment reporting shareable with consignors (weekly/monthly/custom; column-level control)
- returns management (return lists, default return terms, return forms)
- sale attribution and consignor notification when a consigned work sells
- insurance values and custody documentation attached to consigned works (depth varies)

### L2 — Variant / Optional Structure

- operating side: consignee-operated (gallery/dealer manages consignments-in), consignor-operated (artist studio tracks works placed out), or both sides connected in one system
- auction-house consignor relations as an adjacent lot-based variant (estimates, reserves, hammer-price settlement) — different transaction mechanics
- general-resale consignment (interchangeable retail goods, consignor accounts, POS-integrated payouts) — a different Type sharing only the consignment concept
- depth of custody documentation (condition reports, provenance, insurance schedules)
- marketplace participation and website publication of consigned stock
- standalone product vs module packaging (see Boundary Findings — the dominant market form)

### L3 — Vendor-specific (research notes only)

- ArtCloud: connected artist/gallery accounts with a one-time inventory transfer at invitation; accept/deny Consignment Records; explicit per-account divergence semantics (location strings, numbering, acquisition date = acceptance day); field-transfer exclusion list; Inventory Return Consignment as the only return path (no direct return); no block on consigning sold inventory; Consignment Reports page (instant payment calculation, column toggles, share to designers/vendors/artists); Copilot, Quicklists, Stripe POS, ArtCloud Marketplace, jewelry vertical; Artlogic group ownership.
- Artlogic: "Artist Payables" named tool documented as not-yet-shipped (workaround via Advanced Reports); `[consignor_due]` field; Consignment→Invoicing→Statement chain; Artlogic Pay; Private Views app; ArtBase/FileMaker lineage (prior generation of the category).
- Art Galleria: "Private Rooms"; AG Slides Apple TV app; plan caps (artwork/user counts per tier — plan facts, not Type facts); concierge CSV import; Offers CRM in Beta.

## Vendor-specific Findings

See L3 above. None of these enter the canonical model. The consignment-settlement *concept* (track what is owed to the consignor once a consigned work sells) is cross-product where directly observable (Artlogic Due Consignor; ArtCloud payments due & paid from invoice history), while each vendor's named tooling differs. ArtCloud's connected-account architecture (two-sided records with deliberate divergence) is a vendor design, not a Type requirement — single-database implementations (Artlogic, Art Galleria) satisfy the same core with one side operating the system.

## Boundary Findings

1. **vs Art Gallery Management (sibling leaf)** — the central question for this leaf. In all sampled products, consignment is implemented as one module inside the gallery's full inventory/CRM/sales world (confirmed again in this pass: ArtCloud Consignment section inside Manager–Inventory; Artlogic consignment as a basis layer over owned stock; Art Galleria consignments inside the inventory database). The structural test from the prior pass holds: strip inventory, clients and direct sales, keeping only the consignor↔consignee relationship → what remains is exactly this leaf's core. However, **no standalone dedicated artwork-consignment product was identified in reachable official sources** — the relationship is always shipped inside a gallery or artist suite (or as connected accounts between two suites). Assessment: probable narrower-sibling/Capability relationship; this document describes the consignment-centered structure honestly while flagging the packaging reality. Flagged for joint review (consistent with the prior pass's flag).
2. **vs Consignment Management Platform (05.19 Resale)** — general resale consignment centers interchangeable retail goods: consignor accounts, intake pricing, POS-integrated sales, expiry/discount policies, payouts. Artwork consignment centers unique high-value objects: agreements, custody, sale attribution, settlement of the consignor share. Shared concept (ownership-retaining placement), different object worlds.
3. **vs Museum Loan Management / Museum Object Movement** — both track custody of specific objects at external locations, but loans carry no commercial split and no sale disposition; consignment is defined by the commercial terms and the sold/returned settlement outcome. Remove the commercial terms and settlement → loan management remains.
4. **vs Auction Management System** — auction consignor relations are lot-based (intake, estimates, reserves, hammer mechanics, buyer's premium); gallery-context consignment is fixed-price placement of works with a commission split. Adjacent structures around the same ownership-retaining concept; the auction side belongs to the auction leaf.
5. **vs Artist studio management** — the consignor-side variant overlaps heavily: artist studio tools center production/portfolio with consignment-out as one capability (Artlogic artist edition: "creation to consignment"). The consignment-centered view (this leaf) centers the relationship, not the studio.
6. **vs CRM** — consignor records are relationship records, but the center is the consignment (works, terms, disposition, settlement), not a relationship pipeline.

## Uncertainties

- **Artwork Archive** (major independent artist-side consignment tracker) unreachable (403 ×2). Its mechanics could not be verified; no claims are made about it. Its inclusion would likely have strengthened the consignor-side evidence.
- No dedicated standalone artwork-consignment product identified through reachable official sources; search-engine discovery failed (DuckDuckGo timeout; Bing region-polluted). The "standalone vs module" question is answered only for the sampled market.
- Settlement arithmetic (split formulas, tax treatment of the consignor share, payment timing) is not evidenced at formula level in any sampled product; only the existence of percentage terms, due-consignor amounts, and statements is evidenced. Kept qualitative.
- Art Galleria's settlement computation was not directly observed (consignment reporting only); sale attribution likewise not directly observed for that product.
- Auction-side consignor management not sampled (belongs to the auction leaf); boundary stated conceptually.
- Artlogic's "Artist Payables" named tool is documented as a workaround; the underlying fields and chain are real but the named module is not confirmed as shipped.

## Final Synthesis

Artwork Consignment Management is software that operates the consignment relationship between the owner of an artwork (the consignor — artist, estate, collector, or another dealer) and the party authorized to sell or exhibit it (the consignee — gallery, dealer, representative). Its world is built from specific works placed under recorded terms: each consigned work is tracked item-by-item from placement through acceptance, display location, and disposition (sold or returned), with the system maintaining what each disposition means for the two parties — above all, the amount owed to the consignor when a consigned work sells, settled against recorded sales. Around this spine sit the mature structures the market expects: generated consignment agreements, check-in/check-out and location tracking, onward (third-party) placement, per-consignor default terms, connected consignor accounts or submission portals, shareable consignment reports, and returns management. The defining boundary: remove the commercial terms and settlement and only custody/loan tracking remains; remove the consignment relationship itself and the software is the gallery's (or artist's) full operating system — which is how the current market predominantly packages this capability: as a module inside gallery management on the consignee side and artist studio tools on the consignor side, with connected accounts linking the two. No standalone dedicated product was found in the reachable sample; the Type is documented as the consignment-centered structure, with the packaging reality recorded as a boundary issue for joint review.
