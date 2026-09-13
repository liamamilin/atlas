# Research Notes — Restaurant Menu Management

Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Restaurant Menu Management application actually is, from real products: what the menu is as a managed object, what maintenance operations exist, how the menu reaches the surfaces that consume it, who performs this work, and where the Type's boundary sits against Restaurant POS, Restaurant Online Ordering, Restaurant Food Cost Management, Restaurant Management System, and generic product-catalog (PIM) software.

## Initial Boundary (hypothesis before research)

- Core use hypothesis: build, organize, price, and maintain the restaurant's menu as a structured catalog, and keep the surfaces that present/consume it (POS order entry, guest digital menus, online ordering, delivery platforms) in step with it.
- Likely users: owner/GM, menu manager, chef, marketing.
- Likely nearest neighbors: Restaurant POS (menu configuration for order entry), Restaurant Online Ordering (customer-side ordering), Restaurant Food Cost Management (costed recipes behind items), Restaurant Management System (multi-domain layer), Digital Product Catalog / PIM (generic product info).
- Key unknowns:
  1. Is there a standalone product population, or is menu management always a POS module?
  2. Do delivery-platform menu syndication tools belong to this Type?
  3. Do QR/digital guest-facing menu builders belong to this Type?
  4. Is multi-channel publication definitional or just the current market's dominant shape?

## Research Questions

1. What is the menu object in these systems? (hierarchy, items, sections/groups, modifiers/options, pricing fields)
2. How are multiple menus handled (dayparts, locations, channels, brands)?
3. What maintenance operations exist (create/edit/organize/price, availability/86, scheduling, bulk operations)?
4. How does the menu reach consuming surfaces (POS, web/QR menus, kiosks, delivery platforms, digital menu boards)? What are the publish/sync semantics?
5. Who uses it, and what permissions/approval structure surrounds menu changes?
6. What rules and constraints govern menu content (required modifiers, min/max selections, visibility composition, tax, reporting categories)?
7. What exceptions matter (mid-service 86, sync failures, price mismatch across channels, off-hours access)?
8. Where is the boundary: when is menu management just a POS module, and when is it its own Type?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Customer tier | Why selected |
|---|---|---|---|
| Toast | POS-embedded menu management, deep hierarchy + publishing machinery | SMB → enterprise, US full/quick service | Richest official operational documentation of the menu object model |
| Square for Restaurants | POS-embedded menu management, unified "menus hub" simplicity | SMB, multi-channel SMB | Different philosophy: menus as the single hub across channels/locations |
| Checkmate (EveryWare) | Standalone multi-channel menu management / syndication layer above POS | Enterprise chains (QSR/fast casual) | Proves the standalone population; brand-level centralization |
| MenuTiger | Guest-facing QR/digital menu platform with ordering | Small independents, cafes | Tests whether guest-facing menu publishing is in-Type |

Rejected/failed samples: TouchBistro (help center JS-rendered, unreachable content), Lightspeed (not attempted after TouchBistro failure; two POS-embedded poles already covered), ItsaCheckmate help center (transport error; product pages used instead).

## Sources

Tier 1 (official operational documentation — fetched successfully):

- Toast platform guide (doc.toasttab.com):
  - Menu hierarchy: https://doc.toasttab.com/doc/platformguide/adminMenuHierarchy.html
  - Publishing overview: https://doc.toasttab.com/doc/platformguide/platformPublishingOverview.html
  - Menu item inventory overview (86): https://doc.toasttab.com/doc/platformguide/adminMenuItemInventoryOverview.html
  - Ordering channel visibility: https://doc.toasttab.com/doc/platformguide/adminSpecifyingOrderingChannelVisibility.html
  - Menus section index (nav observed): menu builder, multi-location menu builder, POS layout view, menu manager, menu visibility, menu pricing, pricing strategies, portions, items database, bulk imports, digital menu boards, Toast IQ menus
- Square Support Center:
  - Items and inventory topic: https://squareup.com/help/us/en/topic/items-and-inventory
  - Create and update menus: https://squareup.com/help/us/en/article/6424-create-menus-with-square-for-restaurants
  - Manage menus across locations and sales channels: https://squareup.com/help/us/en/article/8553-manage-your-menus-across-locations-and-sales-channels

Tier 2 (official product pages — fetched successfully):

- Checkmate root: https://www.itsacheckmate.com/
- Checkmate EveryWare: https://www.itsacheckmate.com/solutions/everyware
- MenuTiger root: https://www.menutiger.com/
- MenuTiger features: https://www.menutiger.com/features

Unreachable / limitations:

- Toast operator support center (central.toasttab.com) — JS shell only; article content not fetchable. Mitigated by using doc.toasttab.com platform guide (official, static).
- Toast marketing feature page (toasttab.com/local/features/menu-management) — HTTP 403.
- Square developer docs (developer.squareup.com/docs/catalog-api...) — 404 on attempted paths; not retried further.
- Checkmate help center (support.itsacheckmate.com) — transport error; EveryWare evidence is product-page tier only.
- TouchBistro help center (help.touchbistro.com) — JS/CSS error, no content.
- MenuTiger: no operational help docs fetched; evidence is product-page tier.

Per the evidence rules: claims below are labeled by evidence layer. A = directly observed in an official source for a specific product. B = cross-product commonality. C = canonical inference. MenuTiger-sourced claims stay product-specific because only marketing-tier pages were reachable.

## Product Observations

### Toast (doc.toasttab.com platform guide) — evidence layer A

Menu object model:

- Hierarchical structure: *Menus* (top level: e.g. Food, Drinks, Lunch, Dinner, Happy Hour, Bar) → *menu groups* (Appetizers, Salads, Entrees, Desserts) → *menu items*; menu groups can contain *sub-groups*.
- *Modifier groups* → *modifiers* customize items (Cheese: Cheddar/Provolone; Temperature: Rare/Medium/Well Done). Modifier groups can be assigned to menu groups (inherited by all items, disableable per item) or to individual items; items can combine inherited + own modifiers.
- Modifiers are backed by an underlying "item reference" — a modifier option may reference an existing menu item (Fries as a Sandwich Sides modifier option); the platform creates a reference item when none exists.
- Nested modifier groups (Side Salad modifier containing a Salad Dressing modifier group).
- Sharing/re-use rules: menu groups cannot be shared among menus; menu items can be shared by multiple menu groups; modifier groups shareable across groups/items; modifiers shareable; existing menu groups/items re-usable as modifier sources.
- "All Toast products use this structure, including Toast Online Ordering, Toast Takeout (Local by Toast) app, Toast Mobile Order & Pay, Toast Kiosk, and the Toast POS app. Third-party integrations that retrieve restaurant menu data from the Toast platform also use this structure."
- Two authoring workflows: classic menu builder (full features) and newer "menu manager" (bulk-oriented, evolving, documented limitations: no sub-groups or nested modifier groups yet).

Menu builder capabilities (section index directly observed): custom schedule for a menu; determining where a menu item is used; inheritance; images on items; stock status and count; POS button name and color; alcohol labeling; prep stations; courses; sales categories; tax rates and tax behavior; time-based ordering rules for online orders; ordering channel visibility; advanced pricing strategies.

Multi-location: menu builder for multi-location restaurants; *versioned configurations* of a menu item (per-location versions); saving changes to multiple versions of an item.

Menu manager: bulk edits, change sets, publishing menu manager changes, export, search/filtering, views, price levels, permissions.

Menu visibility (directly observed):

- Every menu entity (menu, group, subgroup, item, modifier group) has channel visibility settings; visible = available for ordering on that channel.
- Channels: POS; Kiosk/Order & Pay (requires POS enabled first); Toast Online Ordering + Takeout app; customer invoices / catering (always enabled); online ordering partners (DoorDash, Uber Eats, Grubhub — per-partner restriction available for menus only); digital menu board (Delphi, menus only, defaults Off); view-only website menu (menus only, defaults Off).
- Visibility settings are not inherited, but hiding a parent hides its children on that channel regardless of child settings.
- Required modifier groups: if the group is not visible on a channel, it is missing from orders on that channel even though marked Required.
- Minimum-modifier groups: the number of modifiers visible on a channel must meet or exceed the group's minimum-selection setting, or guests/servers cannot satisfy the requirement.
- Complementary per-partner menu visibility on the "Third party ordering" page; changes take effect only after publish.

Menu pricing (section index directly observed): pricing menu items and modifiers; price editor; price levels; discounts; pricing strategies: base, time-specific, menu-specific, location-specific, open price, fixed, sequence, size, size/sequence, stacking.

Menu item inventory / 86 (directly observed):

- Status values: In Stock (default), Out of Stock ("86ing" the item — button shows 0, item cannot be added to orders), Quantity (limited supply; count auto-decrements when orders are sent to kitchen; auto-transitions to Out of Stock at 0).
- Status changes propagate to POS devices when published; an "86 report" lists out-of-stock/low items; auto-refresh exists.

Publishing (directly observed):

- Saved menu changes are not reflected on POS devices or API results until published.
- Multi-location: must publish to all locations where the change applies.
- "There is no rollback feature for publishing" — revert = manually change back and re-publish.
- Publishing center: permissions, saving vs publishing distinction, manual and scheduled publishing, change sets.

Other observed surfaces: portions (with pricing), items database + export, bulk menu imports (CSV spreadsheet with operation IDs), Delphi digital menu boards (create a menu for a digital menu board), Toast IQ menus (AI: look up menu info, check/update stock, create/update entities, reorganize structure, confirm changes and publish).

### Square for Restaurants (squareup.com help center) — evidence layer A

- Definition (quoted): "A menu is a specific set of menu groups and items that will appear on your restaurant POS modes, online ordering, kiosks, and delivery apps for a certain period of the day or a certain shift. Your menus should correspond with the physical menus in your restaurant."
- "Menus serve as the central hub for managing what you sell across all channels and locations."
- Creation paths: upload a file/photo/URL of an existing menu (third-party integration), import from another platform (Toast, DoorDash named), AI-generated starter menu (answer questions about menu type/cuisine/size), manual creation.
- Structure: menu → menu groups → items. Item fields include name, kitchen-facing name, price; items carry description, calories, dietary preferences, allergens (staff-visible on POS via press-and-hold).
- Categories vs menus split (quoted): "Categories handle the reporting, routing, and internal operations, while menus handle *what* customers see and *when* they see it." Categories: reporting, kitchen routing (printers/KDS), standard-mode POS layout. Menus: buyer-facing organization, channel visibility, time-based availability, location-specific offerings.
- Channels: Point of sale (restaurant modes), Online sites, Kiosk, Ordering profile, Delivery apps (DoorDash, Uber Eats, and other delivery apps).
- Locations: menus assigned to one or many locations; per-item location and sales-channel columns; team members with items permissions can only edit menus/items for locations they are assigned to; editing a menu requires access to all its locations.
- Modifier sets have their own channel visibility; unassigned modifier sets do not appear on a channel even if the item and menu do.
- Items must be added to a menu AND menu group to appear on customer-facing channels.
- Menu hours / dayparting: distinct menus for lunch vs dinner, happy hour, limited-time offers; multiple time periods per day; menu group hours override menu-level hours (must stay within menu hours). Behavior by surface: web/ordering profile — always visible, orderable only in hours; kiosk — hidden outside hours; POS menu picker — shows "Not available until [time]", override by staff with service-settings permission or via passcode.
- Drafts: a menu with no sales channels assigned is effectively a draft; publishing = assigning channels and saving.
- Duplicate menus are independent copies; third-party delivery channels are not auto-added to duplicates.
- Rearrange menus across channels (drag-and-drop ordering).
- Related article titles observed (existence, not content): mark items and modifiers as sold out; item price overrides for multiple locations; time-based categories; schedule item updates for online store; kiosk menu editing; combos; printer routing by category.

### Checkmate — EveryWare (itsacheckmate.com) — evidence layer A for product pages (Tier 2)

- Page title: "EveryWare: Unified Restaurant Menu Management"; site nav: "EveryWare — Unified channel and menu management" under the "Manage" pillar. The vendor itself names the category "Restaurant Menu Management".
- Positioning: "an enterprise solution that sits above your POS, automating menu updates, pricing, and promotions across all platforms"; "10+ digital channels, all managed manually" as the problem statement.
- FAQ (quoted): "It sits as a layer above your POS, syncing menu details between the POS and ordering sites. Changes can be made to item details, pricing, and a host of other variables that are then passed to all your digital menus at once."
- First-party and third-party channels updated through one interface.
- Differentiation vs "typical menu management systems" (quoted): "Typical menu management systems operate at a location level, requiring separate management for each location's menu. EveryWare gives restaurants centralized control of menu management at a brand level... It can automate the implementation of planned menu changes and allow multiple menus to exist for different digital channels."
- Dynamic menu management: instant changes to availability, pricing, and promotions across channels; channel-specific menus; per-channel promotions.
- Integration hub: add new digital channels "with just a few clicks"; integrates with existing POS.
- Change propagation: "Changes are usually applied within a few minutes" (vendor FAQ — treat as vendor claim, not a Type-level fact).
- Customer tier: enterprise brands (Arby's, Wendy's, Five Guys, Buffalo Wild Wings, Sonic, White Castle named); QSR / fast casual / pizza use cases; white-glove onboarding and 24/7 support.
- Help center exists (support.itsacheckmate.com) but was unreachable from the research environment — operational workflow details not verified.

### MenuTiger (menutiger.com) — evidence layer A for product pages (Tier 2); claims kept product-specific

- Self-labels: "restaurant menu maker", "All-In-One Free Menu Maker And Restaurant Management System", "digital menu", "interactive restaurant menu".
- QR code menu: guests scan to browse, order, and pay; dynamic QR codes (editable menu, ordering, payments, analytics) explicitly distinguished from static QR codes linking to a non-editable PDF.
- "Modify menus and prices in real-time with an interactive restaurant menu."
- Menu builder: "Build, edit, and optimize your menu any time"; menu translation into multiple languages; featured/recommended items; promotions editable at any time.
- Menu analytics: "analyzes your most popular dishes, identifies slower options, and recommends adjustments" to optimize the menu.
- Ordering dashboard with order states (pending / preparing / ready); POS integration; purchase analytics/inventory; print templates (posters, table tents, coasters).
- Subscription pricing by features/tables/stores.
- No operational help documentation fetched; menu-management mechanics (availability control, scheduling) not directly verified for this product.

## Cross-product Comparison

| Dimension | Toast | Square for Restaurants | Checkmate EveryWare | MenuTiger |
|---|---|---|---|---|
| Menu of record | Hierarchical entities: menu → group (→ subgroup) → item; modifier groups/modifiers with item references | Menu → menu groups → items; categories kept for reporting/routing | Syncs "menu details between the POS and ordering sites" (layer above POS) | Interactive menu (categories/items) behind QR/web surfaces |
| Consuming surfaces | POS, kiosk, online ordering, takeout app, order & pay, catering, invoices, delivery partners, digital menu boards, view-only web menu | POS modes, online sites, kiosk, ordering profile, delivery apps | 10+ first- and third-party channels | QR web menu/ordering, website, POS via integration |
| Availability control | 86 status: In Stock / Out of Stock / Quantity with auto-decrement and auto-86; 86 report | "Mark items and modifiers as sold out" (article observed); time-based availability | Availability changes pushed across channels | Real-time menu/price updates (mechanism unverified) |
| Time scheduling | Custom menu schedules; time-based ordering rules; scheduled publishing | Menu hours, menu-group hours, time-based categories, scheduled item updates | "Automate the implementation of planned menu changes" | Happy-hour menu content (blog tier only) |
| Pricing machinery | Pricing strategies (base/time/menu/location/open/size/sequence...), price levels, price editor | Price overrides per location; bulk price edit | Instant price updates across all platforms | Real-time price updates |
| Multi-location | Versioned per-location item configurations; publish per location | Menus assigned to locations; item-level location columns; permission scoping | Brand-level centralization vs "typical" location-level tools | Subscription scoped by stores |
| Publish semantics | Explicit publish step; change sets; scheduled publishing; no rollback | Draft = no channels assigned; publish = assign channels + save | Changes "passed to all your digital menus at once" | Real-time |
| Import/migration | Bulk CSV import; items database export | Upload file/photo/URL; import from Toast/DoorDash; AI starter menu | White-glove onboarding | Templates |
| Item content depth | Images, POS button name/color, alcohol labeling, portions, tax behavior | Description, calories, dietary preferences, allergens, kitchen-facing name, images | Item details, pricing, promotions | Description, images, translation, featured items |
| Kitchen/ops linkage | Prep stations; courses; sales categories | Printer routing via categories; kitchen-facing names | — | Order states to kitchen dashboard |
| Analytics | 86 report; sales categories | Reporting categories | Insights (separate product) | Menu analytics (popular/slow dishes, recommendations) |
| AI | Toast IQ menus (lookup, stock, create/update, reorganize, publish) | AI-generated starter menu | — | AI-assisted setup (homepage claim) |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The Type is recognizable only when all three of these jointly hold:

1. **The menu of record** — a persistent structured catalog of the restaurant's sellable offerings: items organized into sections/groups, each item carrying its ordering attributes (price and customization options; description/content in mature products). Remove it → scattered POS item entries or a generic product catalog (PIM territory).
2. **Menu maintenance as managed operations** — dedicated management surfaces for creating, editing, organizing, pricing, and scheduling menu content and controlling item availability over time. Remove it → a static printed menu or a one-time configuration, not management.
3. **Operational publication** — the maintained menu drives at least one operational surface that presents it for ordering or display (POS order entry, guest web/QR menu, kiosk, delivery platform, digital menu board). Remove it → a private catalog nothing consumes, or a menu design document (DTP territory).

Jointly-held load-bearing tests:

- 1 alone = item/product catalog (PIM) or bare POS item database
- 2 without 1 = menu design tool (desktop publishing territory)
- 3 without 1+2 = one-off publishing (static QR to a PDF — MenuTiger's own FAQ excludes this from menu management)
- 1+2 without 3 = back-office catalog with no consumption path
- 1+3 without 2 = a published menu nobody maintains
- 2+3 without 1 = channel pushes with no stable record

Anti-overfit: multi-channel publication is NOT L0 — single-surface menu management (a menu catalog feeding only the POS order screen) satisfies the Type; multi-channel is the common modern structure (L1). Guest-facing ordering is NOT L0 — staff-facing POS consumption satisfies it. QR delivery is NOT L0.

### L1 — Common Mature Structure

Observed across the sample (B unless noted):

- Multi-channel publication with per-channel visibility control (Toast A, Square A, Checkmate A)
- Multi-location management: menu-to-location assignment, per-location overrides/versioning, location-scoped permissions (Toast A, Square A, Checkmate A)
- Dayparting / scheduled menus: menu hours, time-based availability, happy-hour/LTO menus (Toast A, Square A; Checkmate "planned menu changes" A)
- Modifier/option groups with constraints (required, minimum selections) and inheritance (Toast A, Square A)
- Item availability control with propagation to orderable surfaces — the "86" pattern (Toast A, Square A article title, Checkmate A)
- Pricing machinery beyond base price: price levels, per-location overrides, time/menu/location-specific pricing (Toast A, Square A, Checkmate A)
- Import/migration into the menu of record: bulk import, import from other platforms, file/photo upload (Toast A, Square A)
- Item content: description, images, kitchen-facing names, dietary/allergen/calorie fields (Toast A, Square A)
- Kitchen/operations linkage: prep stations, printer routing, courses, reporting categories (Toast A, Square A)
- Draft → publish lifecycle with explicit propagation semantics (Toast A, Square A; Checkmate's "passed to all digital menus at once" A)
- Menu analytics on item performance (MenuTiger A-product-page; Toast 86 report A; Checkmate Insights separate product A)

### L2 — Variant / Optional Structure

- Product-form variants of one Type: POS-embedded module (Toast, Square) vs standalone syndication layer above POS (Checkmate) vs guest-facing digital menu platform (MenuTiger)
- AI menu generation/assistance (Square AI starter A, Toast IQ A, MenuTiger claim A-product-page)
- Digital menu boards as a managed channel (Toast Delphi A; Checkmate digital menu boards A)
- Promotions/featured items managed at menu level (Checkmate A, MenuTiger A-product-page)
- Menu engineering / profitability analytics (MenuTiger A-product-page; only product-page tier — keep optional)
- Nutrition/allergen content depth (Square calories/allergens A; deeper nutrition computation belongs to Nutrition Analysis territory)
- Multilingual menus (MenuTiger A-product-page)
- Combos (Square A article title), portions (Toast A), alcohol labeling (Toast A), open price (Toast A), view-only web menu (Toast A)
- White-glove managed service posture (Checkmate A)
- Print-template outputs adjacent to the digital menu (MenuTiger A-product-page)

### L3 — Vendor-specific (research notes only)

- Toast: Delphi digital menu boards (branded), Toast IQ (branded AI), classic menu builder vs menu manager duality, change sets, "Local by Toast" app naming, modifier "item reference" mechanics, publishing-center permissions
- Square: "ordering profile" channel, WoFlow-powered import, restaurant modes (quick/full service/bar), POS display groups vs menu groups distinction, override passcode for off-hours menus
- Checkmate: EveryWare/hotspot/Reconcile product names, "99% reduction in order errors" marketing metrics, "changes applied within a few minutes" FAQ claim
- MenuTiger: QR Tiger parent brand, subscription tiers by tables/stores, static-vs-dynamic QR framing

## Rejected Findings

- "Menu management = POS menu configuration" — rejected as the Type definition: the Checkmate pole is a standalone layer above the POS, and MenuTiger's pole has no POS order-entry role at all. POS-embedded is a packaging variant.
- "Multi-channel publication is definitional" — rejected: single-surface consumption (POS-only) satisfies the Type; multi-channel is the dominant modern shape but not the invariant.
- "Guest-facing ordering is definitional" — rejected: Toast/Square menu management is staff-facing configuration; the guest ordering transaction belongs to Online Ordering.
- "Menu design/branding (layout, typography, print templates) is part of the Type" — rejected: it is adjacent DTP work; MenuTiger ships templates as an adjunct, but the Type's center is the operational menu of record, not the designed document.
- "Recipe/plate-cost management is part of the Type" — rejected: that is Restaurant Food Cost Management territory (seam recorded by that pass: guest-facing menu vs costed recipe behind it).
- "Menu analytics is definitional" — rejected: only MenuTiger leads with it; Toast/Square treat reporting as a side capability.

## Boundary Findings

| Neighboring Type | Relationship | Distinction / removal test |
|---|---|---|
| Restaurant POS | packaging overlap (bundled in sampled POS products) | POS's defining core is the order/check/payment transaction; menu management is the configuration layer governing what can be sold and where. Remove order/payment execution → menu management remains. Remove the maintained menu of record → POS still transacts but nothing governs the menu. |
| Restaurant Online Ordering | consumer of the menu; adjacent | Online Ordering's center is customer-side order capture/checkout; menu management is supplier-side catalog maintenance. Remove the ordering transaction → menu management stands (Toast/Square poles). Remove the maintained catalog → online ordering has nothing to sell. |
| Restaurant Food Cost Management | downstream neighbor | Food cost manages costed recipes/plate cost behind menu items (money/ingredient center); menu management manages the guest/staff-facing offering (item/price/availability center). Remove costed recipes + variance loop → menu management intact. Remove the menu of record → food cost loses its commercial anchor. (Seam pre-recorded by the food-cost pass; ratified here.) |
| Restaurant Management System | broader multi-domain layer | Management system spans ≥2 operating domains (menu, labor, stock, cost) with a plan-to-actual loop; menu management is the single menu domain. Remove the multi-domain span → menu management remains as a sibling. (Seam pre-recorded by the management-system pass, which named this leaf as a single-domain sibling; ratified here.) |
| Kitchen Display System / KDS | adjacent consumer | KDS's center is kitchen production flow; menu management supplies routing attributes (prep stations, printer categories) but does not run production. |
| Digital Product Catalog / PIM | generic analog | PIM manages product information for commerce generally; the restaurant menu carries restaurant service semantics — modifiers with required/min-max constraints, dayparts, 86 availability, kitchen routing, channel visibility. Remove the service semantics → generic PIM. |
| Nutrition Analysis Application | adjacent specialist | Nutrition computation is the center there; menu management may carry nutrition fields as item content (Square calories/allergens) without computing them. |
| Menu design / DTP tools | out of Type | Producing a designed menu document (print/PDF) with no operational consumption is desktop publishing, not menu management. Static QR-to-PDF is explicitly the non-managing case (MenuTiger FAQ). |

## Uncertainties

- Checkmate EveryWare operational workflow (how mapping to each delivery platform is configured, error handling on failed syncs) — help center unreachable; only product-page tier evidence. All Checkmate mechanics stay at product-page strength.
- MenuTiger menu-management mechanics (availability control, scheduling, modifier constraints) — not verified; product treated as the guest-facing publishing pole on product-page evidence only.
- Whether "menu engineering" (profitability/popularity matrix) is a standard capability of the Type — only MenuTiger-adjacent evidence in-sample; kept optional.
- Whether every POS-embedded menu manager has an explicit publish step — Toast and Square differ (explicit publish vs save-and-assign-channels); propagation semantics are product-dependent, so the final document states the concept (changes take effect on consuming surfaces through a publish/sync step) without fixing one mechanism.
- Legacy POS generations (back-office menu programming in older POS products) were not directly sampled; the historical check below is therefore conceptual, not source-backed.

## Historical / Market-Sample Check

Question: would older, regional, platform-native, or differently positioned products still fit the proposed L0?

- A single-location restaurant POS from the pre-multi-channel era, with a back-office screen where the owner programs items, prices, and modifier options, and the order screens consume that catalog: satisfies L0 leg 1 (menu of record), leg 2 (maintenance operations), leg 3 (publication to the POS order-entry surface). Multi-channel, QR, AI, and syndication are absent — all correctly L1/L2, not L0. ✔
- A printed-menu era restaurant: no software, no menu of record as a managed catalog — not a software Type at all; the paper menu + kitchen 86 board is the conceptual ancestor. ✔ (lineage, not membership)
- Regional variation: QR-menu-heavy markets (MenuTiger pole) and delivery-platform-heavy markets (Checkmate pole) both satisfy L0 without sharing each other's surfaces. ✔
- The L0 does not depend on any era-, region-, or vendor-specific implementation. Historical check passed.

## Final Synthesis

A Restaurant Menu Management application is defined by three jointly-held structures:

1. **The menu of record** — the restaurant's menu held as a persistent structured catalog (sections → items; items carrying price and customization options), not as a document and not as scattered transaction-side entries.
2. **The maintenance loop** — dedicated management operations over that catalog: creating and organizing items, pricing them (including time-, menu-, and location-scoped pricing), scheduling menus (dayparts, limited-time offers), and controlling item availability (the 86 pattern).
3. **Operational publication** — the catalog drives at least one consuming surface (POS order entry, guest web/QR menu, kiosk, ordering profile, delivery platform, digital menu board), with per-channel/per-location visibility control and a publish/sync step that carries changes into operation.

The market realizes this one Type in three product forms: embedded in the POS (order-entry-centric), standalone above the POS (multi-channel syndication and brand-level governance), and guest-facing digital menu platforms (QR/web menus with ordering). These are packaging and surface variants, not separate Types.

The Type's identity is restaurant service semantics: modifiers with selection constraints, dayparts, 86 availability, kitchen routing, and channel visibility have no analog in generic product-catalog software; the transaction itself (order/check/payment) belongs to the POS, and the customer-side ordering experience belongs to Online Ordering.
