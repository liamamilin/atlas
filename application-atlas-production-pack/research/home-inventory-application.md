# Research Notes — Home Inventory Application

Leaf: Home Inventory Application (DIRECTORY.md §29 Home, Family, Personal & Local Services — home/family cluster, between Household Chore Application and Home Maintenance Application)
Slug: home-inventory-application
Research date: 2026-09-08
Methodology: v1.1

## Research Goal

Understand what "Home Inventory Application" software actually is in the real market: what the household catalogs, what structures exist inside such an application (item records, locations, values, documents), what the record is used for and by whom, how the inventory is built and kept current, and where its boundaries lie — especially against Home Management Application, Home Maintenance Application and Home Improvement Planner (§29 siblings), business/retail inventory systems (§05/§10), asset registries (§10/§14), collection-catalog apps, and professional contents documentation used in insurance claims.

## Initial Boundary

Working hypothesis going in: a consumer-side application that catalogs the possessions of a household — per-item records with photos and details, organized by room/location — principally so the household can document what it owns for insurance, recovery, estate, and "knowing what we have and where it is" purposes.

Nearest types identified up front:

- Home Management Application (§29 sibling, unprocessed) — whole-home hub; inventory may appear as one module inside it.
- Home Maintenance Application (§29 sibling, unprocessed) — recurring upkeep of the home and its systems vs a record of possessions.
- Home Improvement Planner (§29 sibling, processed 2026-09-08) — that pass recorded the removal test "home without project+money = home binder/inventory", i.e. this leaf is the possessions-record remainder of the home/family cluster.
- Inventory Management System / Retail Inventory (§05.12/§10) — business stock with quantities, SKUs, reorder semantics.
- Enterprise Asset Registry / IT Asset Management (§10/§14) — organizational assets with custody and lifecycle.
- Collection-catalog applications (book/media catalogers; no dedicated directory leaf) — single-type collections with collector metadata.
- Estate Planning Application (§08) — legal documents; inventory may feed it.
- Professional contents documentation (restoration/insurance field tools; no dedicated directory leaf) — a professional documents someone else's property for a specific claim.

Open questions for this pass: does the home-inventory Type have a defining structure of its own, or is it (a) a consumer Variant of generic inventory software, (b) a module of Home Management, or (c) merely an insurance-claims utility? And how much of the modern feature set (photos, rooms, QR labels, cloud sync) belongs in the definition vs the common mature layer?

## Research Questions

1. What is the subject of record — the item, the home, the collection, or the claim?
2. What does a per-possession record carry across products (identity, photos, purchase details, serials, value, condition, documents)?
3. How is the collection organized — rooms/locations, categories, collections, tags — and is location organization definitional or common?
4. What does "inventory" imply beyond item records — aggregate views (counts, total value), completeness stance, upkeep over time?
5. What is the record FOR — insurance claims, coverage checking, estate, moving, recovery, organization — and which of these purposes are structural vs optional?
6. How is the inventory built and kept current (walk-through capture, quick entry, barcode/receipt capture, import)?
7. Who shares the record (household members, advisors, insurers) and what privacy postures exist?
8. Where are the exact seams vs business inventory, asset registries, home-management suites, maintenance apps, and professional claims documentation?
9. Historical/market-sample check: would paper-era, regional, or platform-native inventory practice (a written household inventory list kept for insurance) still fit the definition?

## Representative Products

Sample (5 researched in depth + 1 boundary specimen; different product philosophies and different market layers):

1. **Sortly** — cloud inventory platform whose center of gravity is now small-business inventory, with a dedicated Home Inventory solution face (organizing, moving, collections). Visual, folder/photo/QR-based, freemium. Represents the general-inventory-platform-with-a-home-face pole and the business-crossover boundary.
2. **Homebox** — open-source, self-hosted home inventory ("the inventory and organization system built for the Home User"). Web UI, Docker deploy, privacy-first. Represents the self-hosted/open-source pole; explicitly contrasts itself with enterprise IT asset management (Snipe-IT) and spreadsheets.
3. **Binary Formations Home Inventory (Mac)** — 17-year desktop consumer product (Mac App Store Editors' Choice; no longer sold, replaced by Under My Roof in 2021). Deep per-item catalog with insurance-policy machinery, coverage analysis, estate/heir assignment, maintenance scheduling, moving reports. Represents the desktop deep-catalog, insurance-first consumer pole.
4. **Under My Roof** (Binary Formations, 2021) — the current-generation successor: Mac/iPhone/iPad, iCloud sync and sharing, item details, home details, documents, renovations, maintenance, collections, insurance policies and claims tracking. Represents the modern Apple-ecosystem subscription pole and the drift toward home management.
5. **HomeBinder** — home-management binder distributed free-for-life through home inspectors, lenders, and real-estate agents; carries a Home Inventory feature ("help safeguard household items by keeping a detailed inventory") beside maintenance, documents, appliances, pros, and finance tabs. Represents the suite-module pole.

Boundary specimen (researched to draw the professional-side seam, not counted as a core sample):

6. **Encircle (Contents)** — restoration-industry field documentation platform; its Contents module inventories, packs out, and prices a claimant's personal property for insurance claims (schedule of loss, carrier reports). The user is the restoration company, not the household.

Rejected during sampling (product mismatch / unreachable):

- **HomeZada** — home-management suite with an inventory module; homezada.com returned 403 on both attempts this pass (and 403 ×2 + transport errors in the 2026-09-08 home-improvement-planner pass). Abandoned per the network rule; suite-module evidence rests on HomeBinder and Under My Roof instead.
- **Nest Egg (nesteggapp.com)** — name collision: the domain now hosts a children's investment/estate platform (Nest Egg Advisors). The former iOS home-inventory app could not be verified; excluded.
- **BluePlum (blueplum.com)** — name collision: the domain hosts a European cabinetry company. The former Mac home-inventory app could not be verified; excluded.
- **homeinventory.app** — timed out twice; abandoned (URL guess for Binary Formations, whose actual site is binaryformations.com).

## Sources

All fetched 2026-09-08. Evidence layer recorded per observation: A = directly observed on an official source for that product; B = cross-product commonality; C = canonical inference.

- Sortly — root page (https://www.sortly.com/) and Home Inventory solution page (https://www.sortly.com/solutions/home-inventory-software/), including its feature list and sub-use-case links (Organizing, Moving, Collections). (A)
- Homebox — docs root (https://homebox.software/en/), Quick Start (https://homebox.software/en/quick-start/), User Guide: Items (https://homebox.software/en/user-guide/items/) and Locations (https://homebox.software/en/user-guide/locations/). Tier-1 operational documentation. (A)
- Binary Formations Home Inventory — product page (https://binaryformations.com/products/home-inventory/) and FAQ (https://binaryformations.com/support/home-inventory-faq/). (A)
- Under My Roof — product site (https://undermyroof.app/). (A)
- HomeBinder — root page (https://www.homebinder.com/). (A; the 2026-09-08 home-improvement-planner pass additionally verified the homeowner-dashboard Knowledge Base article listing the binder tabs.)
- Encircle — root page (https://www.getencircle.com/) and Contents solution page (https://www.getencircle.com/solutions/contents/). (A; boundary specimen only)
- Failed/abandoned per network rule: homezada.com (403 ×2), homeinventory.app (timeout ×2), nesteggapp.com and blueplum.com (fetched successfully but are different products — name collisions).

## Product Observations

### Sortly — general-inventory platform with a home-inventory face

Key observations (all A):

- Positioning: root site sells "Simple Inventory Management Software" for small businesses ("supplies, materials, tools, and equipment"); a dedicated solution page sells the same product as "Home Organizing Inventory Software … easy enough for the whole family."
- **Home-inventory pitch**: "Create a digital inventory for your belongings and valuables … document and track the things that matter to you" — from children's toys and holiday decorations to coin collections and antiques.
- **Item records**: "Enter your items and track key details about them, such as quantity, location, and cost"; "Document unique details about each item such as location, color, size, value, and more"; custom fields for anything product-specific.
- **Photos**: "Upload high-resolution photos so you can track item condition and appearance"; "visually track inventory by adding photos."
- **Organization**: "Organize inventory folders by location, type, and more"; custom folders; home sub-use-cases are Organizing (belongings in your home or in storage), Moving, Collections.
- **QR/barcode**: "Generate and print barcodes and QR codes — so you know exactly what's in that box without having to open it"; in-app scanning; label generation.
- **Aggregate views**: "Inventory summary reports allow you to quickly see the total quantity and value of your inventory based on selected filters"; "Know the total value of your home inventory with custom reports"; PDF/CSV export.
- **Sharing**: "Invite your family and friends to update inventory thanks to multiple user licenses"; customizable user access; activity history.
- **Sync/offline**: cloud-based automatic sync across devices; offline mobile access.
- **Business machinery present in the same product** (not home-specific): low-stock alerts, purchase orders, QuickBooks integration, check-in/check-out, pick lists, Jobs, SSO, API.
- Reading: the home-inventory face is the same item/folder/photo/report structure the business product uses, pointed at household possessions. No insurance-claims machinery is advertised on the home page; the stated outputs are total-value reports and organized lists.

### Homebox — self-hosted open-source pole

Key observations (all A; Tier-1 user guide):

- Positioning: "A simple home inventory management software … the inventory and organization system built for the Home User"; 100% open source, self-hosted, "no cloud sync, no third-party access."
- **Items are the core**: "Items make up the core of Homebox … Items represent the actual things that you wish to track and manage within your inventory system. Each item can have various attributes such as name, description, quantity, location, and any custom fields"; images and file attachments attach to items; "Advanced" edit mode exposes "purchase details, warranty, sold details, and custom fields."
- **Locations as containers**: "Locations … represent the physical or logical places where your items are stored, such as rooms in a house, shelves in a warehouse, or categories in a collection"; locations nest ("a hierarchical structure that reflects real-world storage systems"); items are placed inside locations; a location cannot be placed inside an item.
- **Containment semantics**: "Deleting a location will also delete all items stored within it. Make sure to move any items you want to keep to a different location before deleting."
- **Aggregate value**: the location detail page header shows "total value of contained items."
- **Templates/labels/QR**: item templates with default fields; flexible labels; "Generate QR codes for quick item lookup."
- **Multi-collection**: "Manage multiple separate inventories within one instance. Perfect for tracking items across different groups, households, or locations."
- **Sharing**: other users see your items only via an invite link ("Generate Invite Link" in the user profile); multi-user support "share collections with family, colleagues, or roommates."
- **Import/export**: CSV import/export for bulk operations; "Bill of Materials — export comprehensive BOMs for your inventory"; full REST API.
- **Self-positioning against neighbors**: "Spreadsheets … become unwieldy … can't easily attach photos or documents … don't support features like location hierarchies, templates, or QR codes"; "Snipe-IT is enterprise-grade IT asset management … for home users, it's overkill … HomeBox is purpose-built for home users."
- Reading: the same three-part shape — per-item records, home-anchored location hierarchy, a maintained searchable whole — realized with zero insurance machinery and zero business stock machinery. The spreadsheet and the enterprise asset manager are named as the two neighbors it refuses to be.

### Binary Formations Home Inventory (Mac) — desktop deep-catalog, insurance-first pole

Key observations (all A):

- Positioning: "the ultimate tool to document your home & belongings"; press quotes center on insurance claims ("an awesome tool to have if you're making an insurance claim"; "could land you a better settlement should you need to file a claim"). No longer sold; replaced by Under My Roof (2021) after 17 years on the market (since 2005).
- **Item records**: "Store make, model, serial numbers, purchase price and date, photos, receipts, warranty information (manufacturer's, extended, and other types of warranties), and much more"; dated notes for modifications/repairs; file attachments (owner's manuals); unlimited photos/receipts; multi-page receipts scanned into single PDFs.
- **Organization**: navigate "by location, category, collection, tag, or view all your items in a single list"; customizable categories, conditions, locations, collections; category-level field layouts and custom fields; per-room notes/photos/receipts ("store notes, photos, receipts, and file attachments for each location (room)").
- **Insurance machinery (deep)**: store policy information for homeowners/renters/auto/other policies; "Coverage analysis features flag items not adequately covered by your insurance at the property, category, and item level"; sub-categories for riders (jewelry, musical instruments); include/exclude items by coverage; "Run a report to review with your insurance agent"; "Have all the required details about your property and possessions available to you should you need to file a claim."
- **Estate**: "Create a list of heirs and assign items to each heir for estate planning"; generate a report "showing the items each heir should receive and add it to your will as an addendum."
- **Reports**: custom saved reports (cover sheet, content, sort/total fields) to PDF/print; built-in coverage-analysis report; warranty-expiration report; "moving report provides you an in/out checklist for making sure all your items are moved from one home to another"; value timeline by month; value/count snapshots by category, location, collection, tag, condition, warranty.
- **Home record (adjacent extension)**: Home View stores year built, purchase price, assessment history, home photos, improvement/repair notes, home-related receipts and documents (lot surveys, HOA covenants); maintenance scheduling synced to Calendar/Reminders.
- **Capture**: drag-and-drop photos/receipts; scanner; Continuity Camera; "Home Inventory Inbox" — receipts sent from email/browser into a holding area, later converted to items; Photo Entry Mode ("add new items in rapid succession with just a photo and a name"); Remote Entry helper app (add items over WiFi, offline mode, UPC/EAN barcode scanning); CSV import.
- **Data posture**: each inventory is its own file (multiple inventories, each with its own currency and policy); local file + backups to cloud-synced folders; password protection (explicitly not encryption); single-user file (not designed for multi-machine concurrent access).
- **Collections**: custom collections with default category/location, photos, and valuation "by the sum of the values of all items in the collection, or a combination of both."

### Under My Roof — current-generation Apple-ecosystem pole

Key observations (all A):

- Positioning: "Manage your home and everything in it"; the vendor describes it as "a complete rewrite of Home Inventory … and new home management features that really take it beyond an inventory app."
- **Platform/sync**: Mac, iPhone, iPad; iCloud sync across devices; iCloud sharing with family members ("you are in control of who you share your inventory with and the access they have"); privacy stance: "We (Binary Formations) do not have access to your inventory."
- **Item details**: "From purchase and warranty information to photos and receipts to descriptions and serial numbers, you can store all of the relevant information about your belongings."
- **Home details**: "assessment history, warranty information, square footage (area), photos, and more."
- **Documents**: attach manuals, mortgage/rental agreements, receipts; built-in camera document scanning.
- **Renovations & modifications**: track renovations/modifications to home and belongings with contractor info, cost, before/after photos, receipts, "individual parts and supplies used."
- **Maintenance**: "Create maintenance schedules for your home and any items that need them … keep track of the maintenance and repair histories for your home and possessions."
- **Collections**: "a collector's dream with flexible valuation methods, photos, receipts, notes."
- **Insurance & claims**: "Enter your insurance policy and coverage information and Under My Roof will let you know if you are adequately insured … coverage addendums for specific items, deductibles based on coverage categories, and maximum single item values. Should you ever need to file an insurance claim, Under My Roof can keep track of all of the relevant information regarding the process, including damage information and expenses" — for property and other (health, auto) policies.
- **Business model**: subscription ($34.99/yr or $4.99/mo), free tier limited to 10 items; cancelled subscriptions retain view access to existing data.
- Reading: the inventory core persists (belongings + details + collections + insurance), wrapped in home-management extensions (home record, renovations, maintenance, documents) — the deliberate drift the vendor itself names.

### HomeBinder — suite-module pole

Key observations (all A on the fetched page; dashboard-tab detail corroborated by the home-improvement-planner pass's Tier-1 KB fetch):

- Positioning: "HomeBinder keeps everything about your home in one simple and secure platform"; distributed only through authorized partners (home inspectors, mortgage lenders, real-estate agents); free for life; binder pre-loaded with the inspection report; transferable when the home is sold.
- **Home Inventory as one feature among many**: "Home Inventory — Help safeguard household items by keeping a detailed inventory" — listed beside Maintenance Reminders, Home Improvements, Document Storage, Appliance Recalls, Service Providers.
- **Appliance records**: "Store make and model numbers to get notified if there's ever a recall" (recall notifications tailored to the home).
- **Documents/photos**: the home's paper trail stored digitally; photos tied to the property; the planner pass's KB fetch recorded a Docs/Pics tab carrying "home inventory for insurance purposes."
- Reading: inventory exists here as a module inside a home-management binder whose center is the home's information (inspection report, maintenance, documents, pros, finance). The possessions catalog is present but not the center — the cleanest suite-module specimen available this pass (HomeZada unreachable).

### Encircle Contents — professional boundary specimen

Key observations (all A):

- Positioning: restoration-industry platform ("Restoration Field Documentation to Estimate"); Contents module: "Document, pack out, track and price damaged personal property in one pass, then generate a schedule of loss report your adjuster can approve."
- **The record belongs to the job, not the household**: contents are inventoried inside a restoration job for a specific claim; reports go to "adjusters, carriers, and property owners"; the platform's other modules (field documentation, moisture readings, floor plans, scoping, Xactimate estimates) serve the restoration workflow.
- **Item-level machinery that mirrors home inventory**: AI item descriptions from photos ("automatically identifying items from a single photo … descriptions, brand names, and model numbers"), condition documentation ("time-stamped, geo-tagged record of the item's condition"), room organization ("automatically labeled and organized by room"), QR box labeling, inventory/schedule-of-loss/photo/box/carrier reports.
- Reading: structurally this is a per-possession record organized by room with photos and reports — but the subject is the claimant's damaged property, the owner of the record is the restoration company, and the lifecycle is the claim. It demonstrates where the home-inventory Type ends: the household is not the record's owner or its purpose.

## Cross-product Comparison

| Structure | Sortly | Homebox | BF Home Inventory | Under My Roof | HomeBinder | Encircle Contents (specimen) |
|---|---|---|---|---|---|---|
| Per-possession item record with details | ✓ (name, quantity, location, cost, custom fields) | ✓ (name, description, quantity, location, custom fields; advanced: purchase/warranty/sold) | ✓ (make/model/serial/price/date/warranty/notes) | ✓ (purchase, warranty, photos, receipts, serials) | ✓ (detailed inventory; appliance make/model) | ✓ (AI descriptions, brand, model, condition) |
| Photos per item | ✓ | ✓ | ✓ | ✓ | ✓ (property photos; item photos implied) | ✓ |
| Home/household scope anchor | ✓ (home solution face) | ✓ ("built for the Home User") | ✓ | ✓ | ✓ (one binder per home) | ✗ (claimant's property, job-owned) |
| Location/room organization | ✓ (folders by location) | ✓ (nested locations; rooms named as example) | ✓ (locations/rooms; per-room records) | ✓ (implied by heritage + home model) | ✓ (rooms in property details) | ✓ (by room) |
| Purchase details (price/date/source) | ✓ (cost) | ✓ (advanced mode) | ✓ | ✓ | ✓ (appliances) | (pricing for claim) |
| Serial/model numbers | (custom fields) | ✓ | ✓ | ✓ | ✓ (recall alerts) | ✓ (AI-extracted) |
| Receipts/documents attached | (not explicit on home page) | ✓ (attachments) | ✓ (receipts, scanned PDFs, inbox) | ✓ (camera scanning) | ✓ (docs tab) | (reports) |
| Warranty tracking | (date-based alerts) | ✓ (advanced mode) | ✓ (+ expiration report) | ✓ | (recall notifications) | ✗ |
| Per-item value + aggregate value | ✓ (summary report: total quantity and value) | ✓ (location total value) | ✓ (snapshots, timeline) | ✓ (coverage analysis implies) | (not directly evidenced) | ✓ (pricing/schedule of loss) |
| Reports/exports | ✓ (PDF/CSV) | ✓ (CSV, BOM, QR) | ✓ (custom PDF/print reports) | (user guide; not on fetched page) | (seller report) | ✓ (carrier-ready reports) |
| Insurance orientation | (not advertised on home face) | ✗ | ✓✓ (policies, coverage analysis, claims) | ✓✓ (policies, adequacy, claims tracking) | ✓ ("for insurance purposes") | ✓✓ (claims workflow) |
| Sharing | ✓ (user licenses, family/friends) | ✓ (invite link) | ✗ (single-user file) | ✓ (iCloud sharing) | ✓ (share binder) | ✓ (team, real-time) |
| QR/barcode | ✓✓ (labels + scanning) | ✓ (QR lookup) | ✓ (scan to add) | (not on fetched page) | ✗ | ✓ (scan-to-pack) |
| Maintenance machinery | (date-based alerts) | (notifiers) | ✓ (schedules → Calendar/Reminders) | ✓ (schedules + histories) | ✓ (reminders) | ✗ |
| Estate/heirs | ✗ | ✗ | ✓ (heirs, will addendum) | (not on fetched page) | ✗ | ✗ |
| Moving support | ✓ (moving use case, move summary report) | ✗ | ✓ (moving report) | (not on fetched page) | ✗ | ✗ |
| Collections | ✓ (collections use case) | (labels) | ✓ (valued collections) | ✓ (flexible valuation) | ✗ | ✗ |
| Home record beyond possessions | ✗ | ✗ | ✓ (home view, assessment history) | ✓ (home details, renovations) | ✓✓ (binder center) | ✗ |
| Business-stock machinery | ✓✓ (product center) | ✗ (explicitly refused) | ✗ | ✗ | ✗ | ✗ |
| Deployment | cloud SaaS + mobile | self-hosted (Docker/binary) | local Mac file + backups | device + iCloud | vendor cloud | vendor cloud + offline mobile |

Reading of the matrix:

- The per-possession record, the household scope, and the maintained-whole behaviors (aggregate value/counts, upkeep, search/browse) are present in every core sample — including the two with zero insurance machinery (Sortly home face, Homebox) and the suite module (HomeBinder).
- Location/room organization is present in every sample, but its form varies widely (folders, nested location tree, rooms, property details) and the paper-era form (a flat list) lacks it entirely — common mature structure, not defining.
- Insurance machinery is deep in two samples (BF, UMR), present as purpose-language in two (HomeBinder, Encircle-specimen), and absent in two (Sortly home face, Homebox) — dominant motivation, not defining structure.
- Home-record extension (assessment history, renovations, maintenance) appears in the two Binary Formations products and HomeBinder — the drift toward Home Management, strongest exactly where the vendor or distribution names the product "home management."
- Business-stock machinery (reorder, SKUs, purchase orders) appears only where the product's center is business inventory (Sortly) — the crossover marker, not the Type's structure.

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as a home inventory application:

1. **The item of record for a physical possession** — a persistent, individually identified record per owned thing, carrying descriptive/documentation attributes. The attribute set is product-chosen (name, category, photos, purchase details, serial/model, condition, value, documents, notes); the per-possession record itself is the invariant. Remove → a photo gallery, a notes app, or a home dashboard with no per-thing memory.
2. **The household's possessions as the bounded scope** — the collection is anchored to the user's own home/household (one or more residences, including storage units and off-site boxes as extensions of the home). It is not a business's stock, an organization's asset base, or a single-type collection. Remove → generic inventory software, an asset registry, or a collection catalog.
3. **The maintained whole** — the inventory is a standing, evolving picture of the household's possessions as a totality: built up deliberately (often room by room), kept current as things are acquired, moved, and disposed of, and answerable as a whole (browse/search, counts, total value). Remove → a one-off documentation exercise (a single photo shoot, a valuables log), not an inventory.

Joint load-bearing:

- 1 alone = generic database/notes records with no home meaning
- 2 without 1+3 = a home binder/dashboard with rooms but no item detail
- 1+2 without 3 = scattered item notes; no inventory character
- 1+3 without 2 = business/asset inventory or a single-type collection catalog
- 2+3 without 1 = a home-value dashboard with no per-possession memory

### L1 — Common Mature Structure

Present in essentially all mature current products; expected by the market but not required to recognize the Type:

- location/room organization (rooms, containers, shelves, nested hierarchies; "where it lives" as a first-class attribute)
- photos per item
- purchase details (price, date, source)
- serial/model numbers
- receipts and document attachments (manuals, warranties)
- per-item value and aggregate views (total value, counts by category/location)
- reports/exports (PDF/CSV inventory lists)
- search/browse across the collection (by location, category, tag)
- sharing with household members
- QR/barcode support (scan to add; label generation in some products)
- warranty tracking

### L2 — Variant / Optional Structure

Depends on segment, era, deployment, and purpose:

- insurance machinery depth: policy storage, coverage analysis, claims tracking (deep in the insurance-first pole; absent in the self-hosted pole)
- estate/heir assignment
- maintenance scheduling and histories (drift toward Home Maintenance)
- moving support (checklists, location-change reports)
- collections management (collector-oriented usage)
- home-record extension: property details, assessment history, renovation logs (drift toward Home Management)
- business/asset-tracking crossover (the platform pole)
- deployment and data posture: cloud SaaS vs self-hosted vs local file vs device+iCloud; freemium/subscription vs one-time purchase vs free OSS
- capture style: structured forms vs photo+name quick entry vs barcode/receipt-driven entry

### L3 — Vendor-specific Structure

Stays in Research Notes (examples): Sortly's Jobs/pick lists/purchase orders/QuickBooks/low-stock/check-in-check-out/SSO/API; Homebox's entity types/templates/notifiers/BOM/OIDC/API; Binary Formations' Inbox/Photo Entry Mode/Continuity Camera/Remote Entry & Mobile Backup helper apps/currency conversion/maps; Under My Roof's claims-process tracking with damage info and expenses, deductible-by-category; HomeBinder's recall alerts/Repair Pricer/Seller Report/binder transfer/Assistant; Encircle's AI descriptions/scan-to-pack/schedule of loss/Xactimate integration.

## Historical / Market-Sample Check

Applied before freezing L0:

- **Paper-era practice**: the written household inventory — a list of the household's possessions with descriptions and values, kept up to date and produced to an insurer after a loss (a practice insurance consumer guidance has long recommended) — satisfies all three L0 structures: per-possession entries (1), household scope (2), a maintained whole with total value (3). It has no photos-as-structure, no QR, no cloud, no PDF reports, and often no room organization (a flat list). Therefore none of those can sit in L0.
- **Platform-native / thin realizations**: a spreadsheet of possessions (item rows, values, locations) satisfies the three structures; both Sortly ("Say goodbye to messy spreadsheets") and Homebox ("Why Not Use Something Else: Spreadsheet") name it as the incumbent being replaced. The spreadsheet is the thin pole of the same Type, not a different Type — confirming the core is the three structures, not any app machinery.
- **Regional/era products**: older desktop home-inventory programs (the Binary Formations product dates to 2005, file-based, single-user, no cloud) satisfy the core fully; cloud sync, sharing, and mobile capture are era-current additions, not definitions.
- **Differently-purposed usage**: a collector cataloging one collection, or a mover boxing one apartment, uses a subset of the same structures; the Type's center remains the whole household's possessions, with those uses as variants.

Conclusion: the L0 holds across paper, spreadsheet, desktop-file, cloud, and self-hosted realizations. No re-abstraction needed beyond what is already in the L0 wording (attributes abstracted; location organization held at L1).

## Vendor-specific Findings

- Sortly's home-inventory face is a solution page on an SMB inventory platform; its consumer pitch emphasizes organizing/moving/collections and total-value reports, not insurance claims. Its business machinery (reorder, POs, QuickBooks) belongs to the platform's center, not to this Type.
- Homebox deliberately positions against both spreadsheets and enterprise IT asset management (Snipe-IT) — direct vendor-language evidence for two of this Type's boundaries.
- Binary Formations' insurance machinery is the deepest in the sample (policy riders, category/single-item coverage maximums, coverage analysis at property/category/item level, claim-readiness language); its estate/heir feature and maintenance sync are adjacent extensions inside the same product.
- Under My Roof extends into claims-process tracking (damage information, expenses) — beyond coverage analysis, toward the insurance workflow itself.
- HomeBinder's inventory is one tab in a binder distributed through home-inspection professionals; its appliance make/model capture exists to power recall alerts — a home-management motivation, not an inventory motivation.
- Encircle's contents machinery (AI descriptions, scan-to-pack, schedule of loss) is the professional mirror image of consumer home inventory: same item/room/photo/report structures, opposite owner and purpose.

## Boundary Findings

- **vs Home Management Application (§29 sibling, unprocessed)**: home management is the whole-home hub (documents, maintenance, projects, finance, pros); inventory is the possessions catalog. Suite products (HomeBinder, HomeZada, Under My Roof) embed inventory as a module. Seam: the centered object — if the possessions catalog is the product, it's this Type; if it's one tab beside maintenance/documents/finance, it's home management. Under My Roof straddles by the vendor's own description ("beyond an inventory app"); its inventory core remains load-bearing.
- **vs Home Maintenance Application (§29 sibling, unprocessed)**: maintenance = recurring care of the home and its systems (task schedules, histories); inventory = the record of possessions. Overlap: appliance records and maintenance schedules appear inside inventory products (BF, UMR, HomeBinder) as adjacent capabilities. Seam: recurring-work machinery vs possession records. Removal test: strip maintenance from BF/UMR → still a home inventory; strip item records from HomeBinder → still a home binder.
- **vs Home Improvement Planner (§29, processed)**: consistent with that pass's removal test ("home without project+money = home binder/inventory") — this Type carries no project scope and no money plan; renovation logging in UMR/BF is a record-keeping adjacency, not planning machinery.
- **vs Inventory Management System / business inventory (§05.12/§10)**: business inventory manages stock for sale/operations — quantities, SKUs, reorder thresholds, warehouses, many identical units. Home inventory manages unique possessions — no reorder semantics, no stock states. Sortly straddles (its center is SMB inventory; the home face reuses the same structures); the seam is the subject (household possessions vs trade stock), not the item/folder/report machinery.
- **vs Enterprise Asset Registry / IT Asset Management (§10/§14)**: organizational assets with custody, assignment, lifecycle, depreciation vs household possessions with ownership and value. Homebox's own comparison page draws this seam in vendor language ("Snipe-IT is enterprise-grade IT asset management … for home users, it's overkill").
- **vs collection-catalog applications (no dedicated leaf)**: single-type collections with collector metadata vs all household possessions. Collections management inside home-inventory products (Sortly, BF, UMR) is a variant usage of the same item record, not a separate Type.
- **vs professional contents documentation (Encircle-class; no dedicated leaf)**: same per-item/room/photo/report structures, but the record is owned by the restoration/claims professional, covers only the claimant's damaged property, and lives inside a claim lifecycle. Seam: whose record it is and what it exists to prove.
- **vs Estate Planning Application (§08)**: estate planning produces legal instruments (wills, trusts); the inventory's heir assignment (BF) produces a report to attach to a will — an export, not a legal instrument.
- **vs Photo Album / Notes / Bookmark-class personal collection apps (§02.13)**: those hold media/links/documents without per-possession structured records; the home inventory's item record with attributes is the discriminator.

## Uncertainties

- **HomeZada** could not be fetched (403 ×2 this pass; 403 + transport errors in the sibling pass). The suite-module pole therefore rests on HomeBinder (marketing page + sibling pass's KB article) and Under My Roof's self-described home-management drift. HomeZada's inventory module may add evidence when reachable; no claim in this pass depends on it.
- **Sortly's consumer depth**: the home-inventory face is a solution page; whether the consumer tier carries insurance-specific outputs beyond total-value reports is not evidenced. No insurance claim is attributed to Sortly.
- **HomeBinder's per-item field depth** was not directly evidenced this pass (the fetched page describes the feature in one line; the tab-level detail comes from the sibling pass's KB fetch). Assertions about HomeBinder are kept at feature-list strength.
- **Under My Roof's exact item/location model** is inferred from the product page plus its documented heritage (a rewrite of Home Inventory); the user-guide PDF was not fetched. Location organization for UMR is marked "implied" in the matrix.
- **Market-share and prevalence claims** were not researched; none are made.
- **Encircle's former free homeowner app** ("Encircle Home") could not be verified on the current site; Encircle is used only as the professional boundary specimen.

## Final Synthesis

A Home Inventory Application is the household's record of its possessions: a per-item catalog of the things a household owns — what each thing is, what it cost/is worth, where it lives, and the documentation that proves it (photos, receipts, serials, manuals) — anchored to the household's own home, maintained as a standing whole, and produced outward when the household needs to prove, recover, divide, or move what it owns.

The defining core is small and old: item records + household scope + a maintained whole. Everything else the market associates with the category — room-by-room organization, photos, QR labels, cloud sync, sharing, insurance-policy machinery, coverage analysis, estate reports, moving checklists, maintenance schedules — is common mature structure or variant machinery layered on that core. The Type's two strongest external signals both come from vendors themselves: inventory platforms market a "home inventory" face onto the same item/folder/report structures (Sortly), and self-hosted projects define themselves against the spreadsheet and the enterprise asset manager (Homebox) — confirming that the Type lives between generic record-keeping and organizational asset management, owned by the household.
