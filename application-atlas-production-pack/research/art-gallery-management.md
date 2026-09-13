# Research Notes — Art Gallery Management

Research date: 2026-09-06
Slug: `art-gallery-management`
Directory leaf: "Art Gallery Management" (§27 Media, Entertainment, Creator & Culture)

---

## Research Goal

Understand what software for running a commercial art gallery actually does — its central objects, workflows, states and rules — well enough to write a vendor-neutral Application Document that distinguishes this Type from Museum Collections Management, Artwork Consignment Management, generic CRM, and retail inventory/POS.

## Initial Boundary

Working hypothesis before research:

- A gallery management system is the operational system of a commercial art gallery: artwork inventory (often held on consignment from artists/estates), physical custody/location tracking, collector/client relationship records, sales (offer → invoice → payment → certificate), and artist settlement.
- Nearest neighbors: Museum Collections Management (non-commercial, permanent collection), Artwork Consignment Management (sibling leaf, narrower), CRM, Retail POS / Retail Inventory Management, Exhibition Planning Platform, Online Auction Platform.
- Risk of confusion: the market phrase "art management software" is also used by collection-stewardship products (museums, corporate collections) that do not sell — the commercial sale loop is expected to be the boundary.

## Research Questions

1. What does the central artwork record carry (attribution, edition, imagery, price, provenance, documents)?
2. How is physical custody/location modeled (gallery, storage, artist studio, client on approval, fair)?
3. How does the sale loop work: offer/quotation → hold/approval → invoice → payment → certificate?
4. How does consignment work: consign-in, terms/percentages, returns, settlement to the consignor?
5. How are collectors/clients managed (interests, purchase history, follow-ups)?
6. What interfaces exist (web database, mobile presentation apps, viewing rooms, website sync)?
7. What roles/permissions and audit behaviors exist?
8. What variants exist (artist studio edition, collector edition, marketplace participation)?
9. Historical check: do older / non-SaaS gallery systems (FileMaker-era databases, spreadsheet-run galleries) satisfy the same core?

## Representative Products

Selected for market representability, documentation quality, different geographies/tiers and product philosophies:

| Product | Geography / tier | Philosophy | Evidence accessed |
|---|---|---|---|
| **Artlogic** | UK; solo dealer → large/multi-location galleries; also artist & collector editions | All-in-one platform: management database + websites + sales pipeline + marketing + payments | Product pages (Tier 2) + support help centre (Tier 1) incl. Artist Payables article |
| **Art Galleria** | AU/global; SMB gallery tiers (Starter/PRO/Unlimited) | Cloud art-inventory database first; sales/marketing tools around it; strong PDF/label output | Product pages (Tier 2): overview + for-galleries |
| **ArtCloud** | US; small–large galleries (also artists, jewelry/boutique vertical) | Manager + integrated website builder + own marketplace; POS-flavored sales suite | Product pages (Tier 2): home + Manager for Galleries |

Considered and excluded:

- **ArtBinder** (US, mobile-first inventory + sales app): www.artbinder.net and artbinder.net both returned empty responses twice → abandoned per network-limitation rule. Recorded as a source-access limitation; no claims about it are made.
- **Veevart**: product mismatch — now positions as "museum management software / official OS for cultural institutions" (fundraising, membership, ticketing, shop, front desk) built on Salesforce. Historically gallery-oriented; today it belongs to the museum-operations side. Used only as a boundary data point.
- **Artfundi**: product mismatch — now positions as enterprise art-collection stewardship (financial institutions, corporate collections, museums/archives, foundations/estates): custody, provenance, condition, valuations, audit. No commercial sale loop marketed. Used only as a boundary data point.
- **Gallery Systems / TMS**: museum-side (belongs to Museum Collections Management), not sampled.

## Sources

Tier 1 (official operational documentation):

- Artlogic Support Help Centre — https://support.artlogic.net/hc/en-gb (structure: Management [Database; Artworks & Artists incl. Prints & Editions, Artwork financial details, Locations; Contacts; Documents & Lists; Financial; Users & Security], Sales [Managing offers; Sales Pipeline: Offers / funnel & leads / reporting], Marketing, Websites [Viewing Rooms, Online Sales], Mobile Apps [Artlogic App, Private Views], Integrations [Artsy, Articheck, Arta])
- Artlogic Support — "How to Create Artist Payables Documents from Advanced Reports" — https://support.artlogic.net/hc/en-gb/articles/15406651760028
- Artlogic Support — "Merger with exhibit-E, galleryManager and ArtBase" (promoted article listing; historical context)

Tier 2 (official product pages):

- Artlogic — https://www.artlogic.net/ ; https://www.artlogic.net/products/gallery/management
- Art Galleria — https://www.artgalleria.com/ ; https://www.artgalleria.com/for-galleries
- ArtCloud — https://artcloud.com/ ; https://artcloud.com/manager-for-galleries

Tier 3: none needed; official material was sufficient for the core model.

## Product Observations

### Artlogic

Evidence layer: A (direct, official pages) unless noted.

Key observations:

- Positioning (FAQ): "Art management software is a single system for cataloguing artworks, managing contacts and sales, and publishing them online… combines an inventory database, a CRM, website builder, marketing and payments." Gallery-management FAQ: "software that centralises a gallery's inventory, contacts, consignments, sales and documents"; "It records every artwork with images, provenance, location and price, links works to collectors and sales, and keeps documents in one place."
- Artwork management: "from consignment through to final sale"; capture details, images, pricing; exhibitions, proposals, inventory lists; multi-location support; customizable permissions. Feature bullets: multiple currencies; shipping and multi-location; upload documents and images; prints and editions; consignments and loans; provenance and condition reports.
- Consignment & location (FAQ): "Artlogic tracks consignment terms, owners, current locations and movement history alongside your owned stock, so you can answer where any work is and on what basis at any moment." (Direct evidence that owned stock is the base and consignment is a tracked basis layer.)
- CRM: purchase history; related and grouped contacts; categories and interests; contact narratives; contact lists; event and RSVP tracking.
- Finance: integrated invoicing; multiple billing entities; credit notes; online payment links (Artlogic Pay); tax rate handling; margin scheme.
- Sales: Sales Pipeline with Offers, sales funnel & leads, reporting & insights (help-centre sections); Sales App — "present artworks and send personalised offers directly from your iPhone or iPad."
- Artist settlement (Tier 1, Artist Payables article): "Artist Payables is a tool that allows you to track your inventory from Consignment to Invoicing to Statement. When consigning a new work by an artist, Payables allows you to track what you may owe the artist once the work has been sold." Report fields include Invoice Number, Sale Date, Invoice Value, Sales Tax, **Due Consignor** (`[consignor_due]`). Caveat: the article itself says the named Artist Payables tool "is not yet at Artlogic" and documents a workaround via Advanced Reports — the *concept and fields* are evidenced; the named tool is not shipped as such.
- Documents/reports (help centre related articles): document templates, sales reports, insurance reports, location reports, condition reports (also via Articheck integration), advanced reports; artwork lists.
- Websites: CMS synced with database; Viewing Rooms; View on a Wall (online exhibition visualisation); online store; art-fair preparation guide (Private View Links etc.).
- Mobile: Artlogic App; Private Views app (presenting to collectors).
- Users & security: Users & Security section; roles and permissions; 2FA; cloud backups; modification history / restoring deleted records (video titles).
- Integrations: Artsy (marketplace), Articheck (condition reports), Arta (art shipping/logistics).
- Audience packaging: separate Gallery / Artist (Studio Management) / Collector (Collection Management, PrivateViews presentation) product lines; solutions for solo dealer, medium, large/multi-location.
- Historical: January 2022 merger with exhibit-E, galleryManager and ArtBase; ArtBase is a FileMaker Pro-based database (help-centre category "ArtBase → FileMaker Pro"). Evidence that the previous generation of this software category was a FileMaker database with the same object world.

### Art Galleria

Evidence layer: A (direct, official pages).

Key observations:

- Positioning: "art inventory software… for galleries, artists and collectors"; "manage your complete artwork inventory, artist profiles, contacts, and easily generate invoices, stylish marketing materials and collection catalogs."
- Database: "Catalog your full art inventory, current and sold"; "Track locations, consignments, exhibitions, collections and more"; unlimited hi-res images and documents per record; custom fields (add/rename/reorganize); artist profiles.
- Locations & consignments (Track section): "List all locations you deal with (galleries, studios, storage places) and track where your art is at all times." "Manage consignments with ease. Print or email professional consignment reports. Check-in and check-out artworks to physical locations."
- Sales: invoices with artwork details in client's language/currency; track received payments; integrated payment processor (online, in-person, over the phone); **Offers CRM** — "Send offers from your inventory and track offer details, staff, follow ups and status. Once an offer is accepted, easily convert it into an invoice with one click" (marked Beta, add-on); sales reporting; custom reporting.
- Pricing & availability managed per artwork ("Manage pricing, specials and availability for each artwork").
- Private Rooms: invite-only online viewings of selected works; PDF catalogs; inquiries to inbox; mailout announcements.
- Artist portals: "Allow artists and collaborators to upload and submit artworks directly to your gallery. You can review, accept and reject submissions with full workflow support." (Tiered: 1 portal on Starter, 10 on PRO, unlimited on Unlimited.)
- Documents: PDF catalogs; artwork cards/labels with QR codes and barcodes (label designer; wall and inventory labels); price lists and floor sheets; **certificates of authenticity** ("Automate the process of creating certificates of authenticity").
- Reports: sales; inventory; consignment; insurance (incl. valuation figures).
- Integrations: website auto-update (Squarespace, Wix, WordPress, WooCommerce, Shopify); accounting (QuickBooks, Xero); Mailchimp.
- Mobile: iPhone/iPad/Android apps (portfolio, QR scan to retrieve artwork details, contacts and locations, share); Apple TV "AG Slides" display app.
- Multi-user access (invite/suspend); "By default, all your information is private and secure"; cloud-based.
- Pricing tiers (evidence of SMB packaging): Gallery Starter $65/mo (500 artworks, single user), Gallery PRO $135/mo (5,000 artworks, 3 users), Gallery Unlimited $270/mo (unlimited, 5 users) — billed annually; numbers are plan facts, not Type facts.

### ArtCloud

Evidence layer: A (direct, official pages).

Key observations:

- Positioning: "an Artlogic company" (group ownership noted; product remains distinct); "all-in-one sales and marketing platform"; Manager for Galleries = "comprehensive business software with everything you need to run an art gallery."
- Inventory: "Create rich inventory records for original artworks, editions, merchandise and services with multiple photos, price, description, cost information, location, etc."; Edition Management; Quicklists (custom inventory lists for client proposals, exhibitions, special projects); multiple locations with individual branding, contact information and tax rates.
- Staff: individual staff permissions, event logging, history tracking.
- Exhibitions: "Manage Exhibitions with press announcements, included inventory, show dates and installation photos, easily published to integrated websites or the ArtCloud Marketplace."
- CRM: robust contact records — contact information, interests (catalogued "by artist, medium, and more"), purchase history automatically logged, follow-up opportunities, reminders, interaction tracking; email integration (Google/Office 365).
- Sales & marketing: templates for Tear Sheets, Price Lists, Certificates of Authenticity, Wall Tags; email campaigns from database without double entry; "Capture every Opportunity with sales pipeline tracking, To-Do's to schedule follow ups and Custom Offers"; auto-populated email templates for inquiries; **"Keep track of items on hold, on approval and purchased with our full point of sale suite."** Invoicing & POS with Stripe payments.
- Analytics: real-time reports on sales, outstanding payments, taxes, items on approval; consignment reports (weekly/monthly/custom); historical sales by staff member with sales commissions due; top selling artists; highest value collectors; export to spreadsheet, PDF, QuickBooks.
- Artist management / consignment: "Manage consignments with your artist dashboard and connected artist accounts"; "inviting your artists to submit artwork records directly for review and acceptance into inventory"; "Send integrated consignment contracts and artwork returns"; "Define consignment percentages and terms for each artist and/or work"; "Track consignment payments due and paid, calculated automatically from invoice history"; share customizable reports with artists (inventory, sales & tax, engaged collectors).
- Websites: drag-and-drop builder synced with database ("no double data entry"); "Publish inventory instantly — updates as availability status changes"; Follow Artist; Virtual Install; built-in e-commerce.
- Marketplace: ArtCloud Marketplace (artcloud.market) as a sales channel; also ships a jewelry/boutique vertical ("for Jewelry").

## Cross-product Comparison

| Structure | Artlogic | Art Galleria | ArtCloud | Assessment |
|---|---|---|---|---|
| Artwork inventory records (per specific work; images, price, details) | ✔ ("records every artwork with images, provenance, location and price") | ✔ ("catalog your full art inventory, current and sold") | ✔ ("rich inventory records for original artworks, editions…") | Core (all 3) |
| Custody / location tracking | ✔ (locations, movement history, location reports, multi-location) | ✔ (locations: galleries/studios/storage; check-in/check-out) | ✔ (location on records; multiple locations) | Core (all 3) |
| Availability / status of each work | ✔ (availability status drives website) | ✔ (pricing & availability per artwork) | ✔ (hold / on approval / purchased; availability-driven website) | Core (all 3) |
| Client/collector records linked to sales & interests | ✔ (purchase history, interests, narratives) | ✔ (contacts & sales; grouped) | ✔ (interests by artist/medium, purchase history) | Core (all 3) |
| Offer/quotation → invoice → payment | ✔ (Sales Pipeline: Offers; invoicing; payment links) | ✔ (Offers CRM → one-click invoice; payment processor) | ✔ (Opportunities, Custom Offers, invoicing & POS/Stripe) | Core (all 3) |
| Consignment (in, terms, returns, settlement) | ✔ (consignment terms/owners; consignments & loans; Due Consignor field; consignment→invoicing→statement) | ✔ (consignment reports; check-in/out) | ✔ (contracts, returns, percentages/terms, payments due & paid from invoice history) | Common mature (all 3 sampled, but owned-stock-only dealers fit the Type without it) |
| Artist records / relationships | ✔ (Artists module) | ✔ (artist profiles) | ✔ (artist management, artist accounts) | Common (all 3) |
| Artist submission intake | not observed | ✔ (artist portals, review/accept/reject) | ✔ (artists submit records for review/acceptance) | Common (2 of 3) — mark as common, not universal |
| Editions / prints | ✔ (Prints & Editions) | not explicit (custom fields) | ✔ (Edition Management) | Common (2 of 3) |
| Exhibitions binding artworks | ✔ (exhibitions, proposals) | ✔ (exhibition calendar; artworks associated) | ✔ (exhibitions with included inventory, dates, photos) | Common (all 3) |
| Certificates of authenticity | ✔ (document templates; blog guidance) | ✔ (automated certificates) | ✔ (certificate templates) | Common (all 3) |
| Documents: price lists, tear sheets, labels/wall tags | ✔ (document templates, labels) | ✔ (price lists, floor sheets, labels with QR/barcode) | ✔ (tear sheets, price lists, wall tags) | Common (all 3) |
| Condition & provenance | ✔ (provenance & condition reports; Articheck) | not observed as first-class | not observed as first-class | Optional |
| Sales pipeline / opportunities with staff attribution | ✔ (pipeline, funnel, leads) | ✔ (offer staff, follow-ups) | ✔ (opportunities, staff commissions) | Common (all 3) |
| Roles & permissions, audit/history | ✔ (roles & permissions, 2FA, modification history) | ✔ (multi-user invite/suspend) | ✔ (staff permissions, event logging) | Common (all 3) |
| Reporting (sales/tax/consignment/insurance/collectors) | ✔ (sales, insurance, location, accounts reports) | ✔ (sales, inventory, consignment, insurance) | ✔ (sales, tax, consignment, top collectors/artists, commissions) | Common (all 3) |
| Website sync / online viewing rooms | ✔ (CMS, Viewing Rooms, View on a Wall, online store) | ✔ (website auto-updates; Private Rooms) | ✔ (synced builder; availability-driven; e-commerce) | Common (all 3) |
| Mobile presentation app | ✔ (Artlogic App, Private Views) | ✔ (iOS/Android + Apple TV) | not observed | Common (2 of 3) |
| Payment processing | ✔ (Artlogic Pay links) | ✔ (integrated processor) | ✔ (Stripe POS) | Common (all 3) |
| Accounting integration/export | ✔ (accounts reports & exports; margin scheme) | ✔ (QuickBooks, Xero) | ✔ (QuickBooks export) | Common (all 3) |
| Own marketplace channel | ✔ (Artsy integration) | not observed | ✔ (ArtCloud Marketplace) | Optional |
| Multi-currency / multi-entity / tax regimes | ✔ (currencies, billing entities, margin scheme) | ✔ (language/currency, exchange rates) | ✔ (per-location tax rates) | Common (all 3) |
| Artist/collector sibling editions | ✔ (Artist, Collector products) | ✔ (for Artists, for Collectors) | ✔ (for Artists, for Jewelry) | Variant structure |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software is not recognizable as gallery management:

```text
Gallery-operated artwork inventory
└── Artwork record = one specific physical work
    (artist attribution + commercial identity: title, medium/dimensions,
     edition where applicable, imagery, price)
    └── Custody & availability state
        (where the work physically is; whether and on what basis it is
         available: gallery stock / consigned / held / on approval / sold)
    └── Sale disposition
        (offer or quotation → invoice → payment, converting that specific
         work into a recorded sale to an identified client)
        └── Client record linked to the sale
            (who bought what; the gallery's relationship memory)
```

Four invariants:

1. **Artwork records as unique physical objects** — one record per specific work (not interchangeable SKUs). Without this it is generic retail inventory.
2. **Custody & availability state per artwork** — the work's physical whereabouts and its commercial status. Without this it is a plain database/CRM.
3. **Sale disposition of artworks** — the offer→invoice→payment loop that ends a work's availability. Without this it is collection stewardship (museum/collection management).
4. **Client records linked to artworks and sales** — identified buyers with purchase history. Without this, invoicing has no counterparty and the gallery has no relationship memory.

Historical check: a FileMaker-era gallery database (ArtBase lineage) and a spreadsheet-run gallery both satisfy this core (works list, location notes, sold list, client ledger). Cloud sync, websites, mobile apps and payment links are NOT part of the definition.

### L1 — Common Mature Structure

Present in essentially all mature modern products; expected by the market but not definitional:

- consignment management (consign-in, terms/percentages, returns, settlement statements / amounts due to consignor, consignment reports)
- artist records and artist relationship management (artist submission portals in 2 of 3 sampled products)
- editions / prints handling (2 of 3 sampled)
- sales pipeline: opportunities/offers with follow-ups and staff attribution/commissions
- document generation: invoices, certificates of authenticity, price lists, tear sheets, wall labels, condition reports, insurance reports
- exhibition records binding artworks, dates and display context
- multi-location support
- roles & permissions, event/audit history
- reporting: sales, tax, consignment, insurance, top collectors/artists
- website/publication sync (availability-driven updates, online viewing rooms, e-commerce)
- mobile presentation surfaces (present works, send offers, QR lookup)
- integrated payment processing and accounting export/integration
- multi-currency / multi-entity / regional tax handling

### L2 — Variant / Optional Structure

- audience packaging: gallery vs artist-studio vs collector/collection editions of the same platform (all 3 sampled vendors ship sibling audiences)
- marketplace participation (own marketplace or marketplace integrations) vs website-only
- vertical spillover to adjacent high-value-object retail (jewelry/boutique)
- scale packaging: solo dealer → multi-location enterprise; per-plan artwork/user caps
- presentation surfaces: private online rooms, virtual wall views, TV/display slideshows
- legacy substrate: FileMaker/desktop databases vs cloud SaaS
- regional tax regimes (e.g., margin schemes, per-location tax rates)

### L3 — Vendor-specific (research notes only)

- Artlogic: Artlogic Pay; Private Views app; View on a Wall; Articheck/Arta/Artsy integrations; 2022 merger with exhibit-E/galleryManager/ArtBase; "Artist Payables" as a documented workaround (tool not yet shipped per its own help article); 90-day–2-year backup windows; Expert-plan account management.
- Art Galleria: "Private Rooms" naming; AG Slides Apple TV app; 80+ document types claim; plan caps (500/5,000/unlimited artworks; 1/10/unlimited artist portals); Offers CRM in Beta as add-on; 14-day trial; concierge CSV import.
- ArtCloud: Copilot (curated business suggestions); Quicklists; Virtual Install; Follow Artist; ArtCloud Marketplace; Stripe-based POS; jewelry vertical; Artlogic group ownership.

## Vendor-specific Findings

See L3 above. None of these enter the canonical model. Notably, the consignment-settlement *concept* (track what is owed to the consignor once a consigned work sells) is cross-product (Artlogic Due Consignor field; ArtCloud payments due & paid calculated from invoice history; Art Galleria consignment reports), while each vendor's named tooling differs.

## Boundary Findings

1. **vs Museum Collections Management** — the sharpest boundary. Museums hold a permanent collection under a non-commercial mission (accession/deaccession, conservation, loans, scholarship); galleries hold commercial stock whose terminal state is a sale. Test: remove the sale/consignment commercial loop → what remains is a collection management system. Market evidence: Veevart (formerly gallery-side, now "museum operations" on Salesforce) and Artfundi (enterprise collection stewardship: custody, provenance, condition, valuations, audit — no sale loop marketed) both occupy the non-selling side; both were examined and excluded from the sample for this reason.
2. **vs Artwork Consignment Management (sibling leaf)** — consignment is one module inside gallery management (all 3 sampled products implement it as such). The sibling leaf, if it stands alone, would center the consignor↔gallery relationship (agreements, consign-in/out, settlements) without the gallery's full inventory/CRM/sales world. Test: strip inventory, clients and direct sales, keeping only the consignment relationship → consignment management. Flag for joint review when that leaf is processed.
3. **vs CRM (generic)** — the client side of gallery software is a CRM, but generic CRMs lack artwork inventory, custody and consignment semantics; the artwork↔client link (interest by artist/medium, purchase history) is gallery-specific.
4. **vs Retail POS / Retail Inventory Management** — artworks are unique objects with custody chains and supply-basis (owned vs consigned), sold through relationship-driven, often remote, invoiced transactions rather than immediate counter tender. ArtCloud bundles a POS suite, but as one sales surface inside the gallery model, not the defining one.
5. **vs Exhibition Planning Platform** — in gallery software the exhibition is a container that binds inventory to a display/sales context (dates, included works, press, installation photos); exhibition planning as a standalone Type centers the exhibition lifecycle itself (typically institutional/public).
6. **vs Online Auction Platform** — auction houses sell through a bidding model with lot/hammer mechanics; galleries sell at (often negotiable) fixed prices through private offers. Different core transaction structure.
7. **vs Artist studio management** — same vendors ship a sibling product; the studio variant lacks consignment-in (the artist is the source of supply) and centers production/portfolio. Variant relationship, not a separate structure of this leaf.

## Uncertainties

- ArtBinder (mobile-first sales model) could not be fetched (two empty responses); its inclusion might have strengthened the mobile-surface evidence. No claims depend on it.
- Exact settlement arithmetic (commission split formulas, tax treatment of the consignor share) is not evidenced at formula level; only the existence of percentage terms, "due consignor" amounts and settlement statements is evidenced. Kept qualitative.
- Artist submission portals observed in 2 of 3 products; treated as common, not universal.
- Editions/prints as first-class structures observed in 2 of 3; same treatment.
- Whether every product exposes condition/provenance as first-class fields (only Artlogic clearly does among the sampled); treated as optional.
- Artlogic's "Artist Payables" named tool is documented as a workaround; the underlying fields are real but the named module is not confirmed as shipped.

## Final Synthesis

An Art Gallery Management application is the operating system of a commercial art gallery. Its world is built around artwork records that each represent one specific physical work; every artwork carries a custody/availability state (where it is, and whether it is available, held, on approval, or sold) and a supply basis (gallery-owned or consigned). The system moves works through a relationship-driven sale loop — offer or quotation, optional hold/approval, invoice, payment, certificate — to identified collector clients, and when a sold work was consigned it tracks what is owed back to the consignor. Around this spine sit the mature structures the market expects: artist records and intake, exhibitions, document generation (certificates, price lists, tear sheets, condition and insurance reports), sales pipeline with staff attribution, roles/permissions with audit history, reporting, website/viewing-room publication synced to availability, mobile presentation surfaces, payments and accounting handoff. The defining boundary is commercial disposition: remove the sale loop and the software becomes collection management; remove custody and inventory and it becomes a CRM; restrict it to the consignor relationship only and it becomes consignment management.
