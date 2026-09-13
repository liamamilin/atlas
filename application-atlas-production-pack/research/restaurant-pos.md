# Research Notes — Restaurant POS

## Research Goal

Understand the stable operational core of a Restaurant POS — the operator-facing transaction system of a food-and-beverage operation — and hold its boundaries against the neighboring Types the directory places around it: Retail POS, Restaurant Management System, Restaurant Online Ordering, Kitchen Display System, Restaurant Menu Management, Restaurant Inventory Management, Restaurant Reservation Platform, Self-service Restaurant Ordering.

This pass must also discharge the seams pre-hung by earlier passes:

1. **retail-point-of-sale** (§05.10, processed): "the two Types share the entire transaction spine (catalog-configured order → transaction → payment) and differ in sale semantics (immediate paid sale + returns vs table/check/service-period lifecycle); vendors ship both as modes of single products, so the boundary is semantic, not structural." This pass must ratify from the restaurant side.
2. **restaurant-online-ordering** (§26, processed): seam drawn as composing actor (customer vs staff) + surface; "online ordering hours do not restrict POS ordering, the POS screen receives online orders, and staff-entered off-premise orders are a POS function; shared catalog/order stream in suite products is bundling, not identity." This pass must ratify from the POS side.
3. **restaurant-menu-management** (§26, processed): menu of record maintained there; "POS order entry" named as a consuming surface. This pass must hold the catalog-of-record vs operational-catalog seam.
4. **restaurant-inventory-management** (§26, processed): "restaurant-pos (sales = depletion input, does not own the stock record)". This pass must hold that seam.
5. **restaurant-management-system** (§26, processed): management layer vs transaction surface; POS-anchored pole (Toast) bundles both. This pass must hold that seam.

## Initial Boundary

Target:

> Restaurant POS (directory leaf, §26 Travel/Hospitality/Food Service)

Working hypothesis (from the v1.0 example document + workflow example):

> Restaurant POS is a restaurant-specific transaction system centered on constructing an order/check from a menu, applying dining-service semantics, taking payment and closing the transaction.

Key unknowns going in:

- Is the check (vs order) distinction structural across products, or Toast-shaped?
- Are tables/covers/courses definitional or variant-dependent (quick service runs without them)?
- Where exactly is the line to Retail POS, given vendors ship both as modes of one product?
- Does the legacy/enterprise terminal generation (Oracle line) share the same core?
- What is POS-owned vs consumed-from-siblings (menu catalog, stock, reservations)?

## Research Questions

1. What objects does the transaction world consist of (menu, item, modifier, order, check, payment), and how do they relate?
2. What is the order/check lifecycle, and which states are universal vs product-specific?
3. Which restaurant service semantics attach to the order (dining option, table, covers, seat, course, server), and which are variant-dependent?
4. How does the order reach the kitchen (routing, coursing, fire/send/hold), and where does KDS begin?
5. Which money rules matter (discounts, comps, service charges, tips, splits, voids, refunds, cash management, end-of-day)?
6. Which permissions/roles gate which actions?
7. What does the POS consume from sibling Types (menu catalog, stock status, reservations, online orders) and what does it feed them (sales, depletion, actuals)?
8. What varies by service model (full-service / quick-service / bar) without changing the Type?

## Representative Products

| Product | Why selected | Segment / philosophy | Evidence depth |
|---|---|---|---|
| Toast | restaurant-native POS platform; explicit order/check/table workflow; largest US restaurant-platform pole | SMB → mid-market → enterprise (its own segment definitions: SMB 1–10 sites, mid-market 11–50, enterprise 50+) | Tier 1 — official platform guide (doc.toasttab.com), 6 pages fetched |
| Square for Restaurants | generalist POS vendor's restaurant edition; modes architecture shows restaurant semantics as a layer on a shared spine | micro → SMB | Tier 1 — official Support Center, 4 articles fetched |
| Oracle Simphony (MICROS line) | enterprise/legacy-lineage pole; workstation-generation POS still current; hotel-F&B heritage | enterprise, global, hotel + restaurant | Tier 1 — official Oracle Help Center (guide preface + workstation chapter + doc index) |
| SpotOn Restaurant | payments-led SMB restaurant POS; FOH/BOH split; independent-restaurant tier | SMB / independent | Tier 1 — official help center index (concept set); article bodies did not render (dynamic content) — index-level evidence |

Rejected/abandoned: Lightspeed Restaurant (403 on lightspeedhq.com and transport error on help.lightspeedhq.com — failed again this pass after 2 attempts; dropped per network rule; consistent with the restaurant-management-system pass's recorded limitation), TouchBistro (403), Clover (JS-only page, no content).

## Sources

Research date: 2026-09-09

### Toast (official platform documentation)

- Platform guide index — https://doc.toasttab.com/doc/platformguide/index.html
- Order information — https://doc.toasttab.com/doc/platformguide/platformOrdersOverview.html
- Tracking the order state — https://doc.toasttab.com/doc/platformguide/adminOrderStates.html
- Menu hierarchy — https://doc.toasttab.com/doc/platformguide/adminMenuHierarchy.html
- Access permissions reference — https://doc.toasttab.com/doc/platformguide/adminPermissions.html
- Glossary — https://doc.toasttab.com/doc/platformguide/adminGlossary.html
- How orders are created and updated — https://doc.toasttab.com/doc/platformguide/platformOrdersCreateUpdate.html

### Square for Restaurants (official Support Center)

- Set up your food & beverage business with Square — https://squareup.com/help/us/en/article/6407-get-started-with-square-for-restaurants
- Create and update menus — https://squareup.com/help/us/en/article/6424-create-menus-with-square-for-restaurants
- Use modes with Square Point of Sale — https://squareup.com/help/us/en/article/8458-use-modes-with-square-point-of-sale
- Manage checks (comp/void/reassign/move) — https://squareup.com/help/us/en/article/8166-comp-void-and-reassign-checks-with-square-for-restaurants

### Oracle Simphony (official Oracle Help Center)

- Restaurants documentation index — https://docs.oracle.com/en/industries/food-beverage/
- Simphony documentation index — https://docs.oracle.com/en/industries/food-beverage/simphony/index.html
- POS User Guide preface — https://docs.oracle.com/en/industries/food-beverage/simphony/sipou/c_preface.htm
- POS User Guide, Basic Workstation Operations — https://docs.oracle.com/en/industries/food-beverage/simphony/sipou/c_workstation.htm

### SpotOn Restaurant (official help center)

- SpotOn Restaurant section index — https://help.spoton.com/page/spoton-restaurant.md
- Front of House (FOH) article index — https://help.spoton.com/page/spoton-restaurant-frontofhouse.md
- Table Orders / Send Orders (article body did not render — dynamic content) — https://help.spoton.com/space/SK/1025868019/

## Product Observations

### Toast (evidence layer A — direct, official platform guide)

**Transaction model.** "An order is the basic building block of a restaurant transaction. Each order specifies: the items that a guest purchases; the amount that the guest is charged; how the guest receives the order; how the guest pays for the order." Each order contains one or more **checks** ("a party of guests might request separate checks so that each guest can pay separately"). Each check includes: menu item selections and prices, applicable taxes, discounts (item-level and check-level), service charges, guest information, and the payments made. Outside the checks, the order tracks: the **dining option** ("associated with a specific dining behavior — in-person, takeout, curbside pickup, delivery"), the responsible employee, the table (for in-person dining), delivery address/instructions, curbside vehicle info.

**Order states.** Open (created, not paid/completed) → Paid (credit-card-specific: "the credit card was charged… but the payment is not yet finalized… not… adjusted… to add a tip") → Closed ("completed and fully paid for, including any tips, and the server has closed it"). Cash orders go open → closed with no paid state. Closed orders can be purged from devices, viewed in the admin web, and reopened (reopening a check on a closed order changes only the check state). Orders closed for a period become "restricted."

**Menu model.** Hierarchy: Menus → menu groups → (sub-groups) → menu items → modifier groups → modifiers. Modifiers are supported by an underlying "item reference" (an existing menu item can be re-used as a modifier); nested modifier groups allowed; entities shareable/re-usable across menus under stated rules. Pricing strategies: base, time-specific, menu-specific, location-specific, open price, fixed, sequence, size. Portions; courses; prep stations; sales categories; tax rates; POS button name/color; alcohol labeling. Menu item inventory: stock status/count with an "86 report." Changes must be **published** to become visible to employees/guests. Ordering-channel visibility configurable per entity.

**Ordering screens.** Send ("notify the kitchen to begin preparing"), Hold ("retain guest order information without sending"), Stay ("send an order to the kitchen without closing the ordering screen"), Fire ("start cooking or preparing"). Table Service Mode and Quick Order Mode are separate mode permissions; both screens carry Previous Checks and Lookup.

**Kitchen routing.** Prep stations ("the area in the kitchen where a certain type of food is prepared… identifies the location of a KDS device or kitchen printer that displays or prints orders"); items/groups inherit prep-station assignment; KDS expediter screens; "all day" counts; integral vs independent modifiers affect prep timing.

**Money machinery.** Discounts (incl. BOGO), comps ("give a menu item away for free, typically done by the owner or manager"), service charges vs gratuities vs tips (distinct glossary entries), auto-gratuity, customer/guest credit, house accounts, gift cards, open items ("items not included in a menu, such as corkage fees"), balance due, subtotal. Cash: drawers with active/open/closed states, starting balance, cash in/out/drop/pay out, blind vs full drawer access, drawer lockdown, large over/under threshold, shift review ("ensures that all checks are closed, cash held by the server… is returned… tips and gratuities are given to the employee"), Z report / Close Out Day, business day cutoff. Card payments: authorization → capture → settled; auto-capturing of uncaptured payments at end of business day; offline/background payments when connectivity is lost.

**Permissions.** Permissions grouped into **jobs** assigned to employees. Mode permissions gate the main surfaces (Table Service, Quick Order, KDS, Payment Terminal, Pending Orders/Orders Hub, Delivery). Additional POS permissions gate actions: Apply Cash Payments, Cash Drawer Access, View/Edit Other Employees' Orders, Add/Update Service Charges, No Sale, Key in Credit Cards, Offline CC Processing, Change Table, Change Server, Split Checks, Void Items/Orders, Void/Refund Payments, Unlinked Refunds, Edit Sent Items, Other Payment Types, Open Items, Tax Exempt, Age Verification Override, Throttle Online Orders. Manager permissions: Discounts, Bulk Transfer/Void/Close, Shift Review, Close Out Day, Cash Drawers (Blind/Full), Pay Out, Find Checks. Restaurant-admin permissions: Sales Reports, Edit Full Menu, Tables, Employee Info, House Accounts, Customer Credits & Reports, Local Menu Edit (multi-location).

**Multi-device/multi-channel.** Orders created on the POS app "are automatically replicated to the other devices in the same network. You can create an order on one device and then update it on another device." Orders also arrive from online sources and the orders API. Line busting (handhelds in QSR lines) documented in glossary.

**Self-definition.** Glossary: "A point of sale system is the hardware, software, and support that manages sales transactions, including itemization, credit card processing, and receipt printing." Toast POS device = "a tablet or handheld device that runs the Toast POS app"; Toast Web = administration site.

### Square for Restaurants (evidence layer A — direct, official Support Center)

**Setup model.** Menu creation is step 3 of onboarding: "A menu is a specific set of display groups and items that appear on your point of sale for a certain period of the day or a certain shift. Your menus should correspond with the physical menus in your restaurant." Multiple menus for dayparts. Sign-in via device codes (shared 12-digit) or team-member credentials; passcodes per team member.

**Modes.** "The Square Point of Sale app comes with a set of pre-configured modes… Full service, Quick service, and Bar modes — Square for Restaurants; Retail mode — Square for Retail; Bookings mode — Square Appointments; Services mode — Square Invoices; Standard mode — Square Point of Sale." Restaurant semantics are delivered as modes of the same app — direct evidence for the retail-pos pass's "vendors ship both as modes of single products."

**Menu model.** Menus = buyer-facing organization (menu groups + items) with channel visibility (restaurant POS modes, online ordering, kiosks, ordering profile, delivery apps) and time-based availability (menu hours, dayparts; menu-group hours override menu-level hours; out-of-hours menus visible but orderable only with service-settings permission or override passcode). **Categories are separate**: "Categories handle the reporting, routing, and internal operations, while menus handle what customers see and when they see it" — categories drive kitchen routing to printers/KDS. Item-level and modifier-set-level channel visibility. Drafts = menus with no channels assigned.

**Checks.** "Manage checks" article: four actions on a check before it closes — **Comp** ("remove the cost from an item… for food or drinks already in progress or delivered"; comped items still show in sales and inventory reporting), **Void** ("when an item is entered incorrectly… and the food or drinks have not been made or delivered yet"), **Reassign** ("when one team member ends their shift… needs to pass the check to another clocked-in team member"), **Move** (items between courses or to other checks; merge checks; drag-to-merge on the floor plan). Open Checks is a device-profile setting. Floor plan: "A check with a cover count set — even without items added — is saved and persists on the floor plan… a table appears occupied as soon as a server sets covers."

**Related surfaces.** Dining options, floor plan, predefined tickets/ticket groups, order-ready texts, coursing with KDS, seats management.

### Oracle Simphony (evidence layer A — direct, official Oracle Help Center; guide-level depth)

**Self-definition.** "Oracle Simphony is a cloud-based Point-of-Sale (POS) solution that provides business management capabilities using a single tool with vast integration capabilities to property management systems, paperless kitchen display systems, credit card interfaces, and reporting applications." Audience: "Oracle Simphony workstation operators."

**Workstation operations.** "A workstation is a physical device that allows you to perform point of sale (POS) operations such as adding menu items to an order, recording payments, clocking in and clocking out employees, printing guest checks and customer receipts, and generating reports." Warning messages exist for "unsent checks and unposted OPERA connection transactions" — the **guest check** is the unit that must be sent/posted; the PMS (OPERA) integration is a posting path.

**Documentation map.** Configuration: Transaction Processing (Simphony Configuration), KDS, back-office applications (Labor Management, Gift and Loyalty, Inventory Management), Payments. User guides: POS Employee, POS Manager, Frontline Manager. Fiscal: Spain VERIFACTU invoicing-software declaration. Interfaces: PMS (OPERA) specification, Generic POS Interface, Transaction Services APIs. Hardware: "Oracle MICROS workstations and tablets."

Reading: the enterprise/legacy-lineage generation carries the same core — menu items added to an order, guest checks, payment recording, receipts, reports — with the restaurant/hotel service context (PMS posting, KDS) around it.

### SpotOn Restaurant (evidence layer A at index level — official help center; article bodies not rendered)

**Concept set (FOH article index).** Order types; Table Orders / Send Orders; Start a Tab; Find an Order / Tab; Quick Sale / Order; Cancel Order; Change Order Type; Combine Orders; Split Checks; Split Payment Types; Split an Item Between Guests; Move Items Between Guests; Move Items to Another Check; Moving Guest Checks; Transfer Check Between Servers; Auto Coursing; Modify Item During Order; Remove / Void Item from Order; Close $0 Check; Pre-Authorize Credit Card; Refunds; Rekeys & Voids; Gratuity / Tips; Adjust Tips Process; Assign Cash Drawer; House Accounts; Gift Cards; Loyalty; Scheduled Orders; Delivery Orders & Driver Management; Pause Online Ordering; End of Day Process; Close Out Report Settings; View & Print Server Reports; Login & Station Setup; Station Themes; Item/Ticket/Show Commands menus; Item Search; Edit Menu Items & Price; Enable / Edit Quantity on Hand; Add/Edit/Remove Guests; SMS Text Messaging (Dine-In) FOH Flow.

**BOH section** covers Order Types, Printer Settings, Table Layouts, Table Status. **Add-ons**: SpotOn Order (online ordering with "direct POS integration"), SpotOn Reserve (reservations), SpotOn Teamwork (scheduling/payroll/tips), Loyalty.

Reading: the FOH concept set is the same check/tab/order/tender world as Toast and Square — tabs, splits, transfers, coursing, pre-auth, cash drawers, end-of-day — realized in a payments-led product for independents.

## Cross-product Comparison

| Finding | Toast | Square Rest. | Oracle Simphony | SpotOn | Layer | Canonical decision |
|---|---|---|---|---|---|---|
| Menu-configured order entry (items + prices + modifiers/options) | ✓ (menu→group→item→modifier group→modifier) | ✓ (menus→groups→items; modifier sets) | ✓ ("adding menu items to an order") | ✓ (Menu section; Modify Item During Order) | A×4 | **Defining core** |
| Order as the composed transaction | ✓ (explicit: "basic building block") | ✓ (checks/orders; order types) | ✓ (order on workstation) | ✓ (order types; orders) | A×4 | **Defining core** |
| Check/tab as the settlement unit (amount due, taxes, discounts, payments) | ✓ (explicit: order contains 1+ checks) | ✓ (checks; comp/void/reassign/move) | ✓ (guest checks; unsent-check warnings) | ✓ (checks; split/move/transfer/combine; Close $0 Check) | A×4 | **Defining core** |
| Payment + closure completing the transaction | ✓ (open→paid→closed) | ✓ (checkout; open checks close) | ✓ ("recording payments… printing guest checks and customer receipts") | ✓ (payments; End of Day) | A×4 | **Defining core** |
| Split / merge / transfer checks | ✓ (Split Checks permission; transfer; bulk ops) | ✓ (move/merge/reassign) | (not fetched at article depth) | ✓ (split/move/transfer/combine) | A×3 | Common mature |
| Discounts / comps / voids with reasons + permission gating | ✓ (Discounts permission; comp glossary; void permissions) | ✓ (comp/void with reason; permissions) | (config-level) | ✓ (Discounts; Rekeys & Voids) | A×3 | Common mature |
| Tips / gratuities / service charges | ✓ (tip/gratuity/service-charge distinct) | ✓ (gratuity/tips section) | (gift & loyalty; not tip-fetched) | ✓ (Gratuity/Tips; Adjust Tips) | A×3 | Common mature (region-dependent) |
| Dining options (dine-in/takeout/delivery) on the order | ✓ (explicit) | ✓ (dining options) | (order types implied) | ✓ (Change Order Type; order types) | A×3 | Common mature |
| Tables / floor plan / covers / seats | ✓ (table, seat, service area, revenue center) | ✓ (floor plan; covers hold tables) | (hotel heritage; not fetched) | ✓ (Table Orders; Table Layouts/Status; guests) | A×3 | Common mature; **full-service variant** |
| Courses / coursing | ✓ (assign courses; fire by prep time) | ✓ (move item to different course; coursing with KDS) | — | ✓ (Auto Coursing) | A×3 | Common mature; full-service variant |
| Kitchen routing (prep stations / categories → printers/KDS) | ✓ (prep stations; KDS routing) | ✓ (categories → printers/KDS) | ✓ (KDS configuration; "paperless kitchen display systems") | ✓ (Printer Settings; BOH) | A×4 | Common mature |
| Order states open → (paid) → closed | ✓ (explicit; cash skips paid) | ✓ (open checks; close) | ✓ (unsent → sent/posted) | ✓ (open tabs; close; End of Day) | A×4 | Common mature; exact state names product-specific |
| Reopen / void / refund after closure | ✓ (reopen checks; void/refund payments; unlinked refunds) | ✓ (comp/void before close; refunds) | — | ✓ (Refunds; Rekeys & Voids) | A×3 | Common mature |
| Cash management (drawers, shift review/closeout, end-of-day) | ✓ (deep: drawers, blind access, lockdown, Z report) | ✓ (drawer assignment implied; end-of-day) | ✓ (workstation ops; reports) | ✓ (Assign Cash Drawer; End of Day; Server Reports) | A×4 | Common mature |
| Employee roles & permission gating (passcodes, manager overrides) | ✓ (jobs + granular permissions) | ✓ (team permissions; passcodes; override passcode) | ✓ (POS Employee vs POS Manager guides) | ✓ (Employees & Users; Login & Station Setup) | A×4 | Common mature |
| Dayparted menus / menu schedules | ✓ (custom menu schedules; time-specific pricing) | ✓ (menu hours; dayparts) | — | — | A×2 | Common (2/4 observed) |
| Item availability / 86 / quantity on hand | ✓ (stock status; 86 report) | (sold-out via ordering; not POS-fetched) | — | ✓ (Quantity on Hand) | A×2 | Common (2/4 observed) |
| Online orders arriving into the POS order stream | ✓ (orders from website/API replicated to devices) | ✓ (menus/channels; ordering profile) | — | ✓ (Pause Online Ordering; SpotOn Order "direct POS integration") | A×3 | Common mature (bundling with Online Ordering Type) |
| Reservations/waitlist attached | ✓ (Toast Tables permission; Log Into Toast Tables App) | — | ✓ (OPERA PMS posting) | ✓ (SpotOn Reserve) | A×3 | Optional / variant |
| Loyalty / gift cards / house accounts / customer credits | ✓ (all) | ✓ (gift cards; loyalty in ecosystem) | ✓ (Gift and Loyalty back office) | ✓ (all) | A×4 | Optional |
| Delivery dispatch / driver management | ✓ (Delivery Mode permission) | (courier config in ordering) | — | ✓ (Delivery Orders & Driver Management) | A×2 | Optional (Delivery Management Type) |
| Inventory/waste modules beside the transaction core | ✓ (Waste Tracking screen; menu-item inventory) | (comp shows in inventory reporting) | ✓ (Inventory Management back office) | ✓ (Quantity on Hand) | A×4 | Optional (Inventory Type owns the stock record) |
| Multi-location configuration (shared menus, inheritance, local edit) | ✓ (enterprise module; Local Menu Edit; inheritance) | ✓ (menus across locations; team access rules) | ✓ (property/client deployment) | — | A×3 | Optional / scale variant |
| Integrated payments as the money rail | ✓ (native processing; offline/background) | ✓ (native) | ✓ (credit card interfaces; payments platform) | ✓ (payments-led company) | A×4 | Common mature; **not definitional** (processing is a separate Type) |
| Hardware form | tablet/handheld | phone/tablet app + hardware | MICROS workstations and tablets | PAX/A920/Aries8 class | A×4 | Variant — form factor not definitional |

## Canonical Abstraction

### Level 0 — Defining Invariant

The smallest structure without which the product is not a Restaurant POS:

1. **Menu-configured order entry by restaurant staff** — an authorized employee composes the guest's request as an order by selecting from the operation's configured menu (items carrying prices and customization options) on the restaurant's own transaction surface. Remove → a payment terminal / cash register / customer self-service channel; the composing actor and the menu configuration are what make it a restaurant POS.
2. **The check as the accumulating settlement unit** — the order's charges (items, modifiers, taxes, adjustments) accumulate on a check/tab that is the unit of amount due; the check persists until settled and is subject to splits, merges, transfers, discounts, comps, voids. Remove → a stream of immediate paid sales with no settlement container (= Retail POS sale semantics), or a kitchen ticket with no money.
3. **Payment and controlled closure** — payments settle the check (fully or by splits), and closing the check completes and records the transaction; closure is gated (balance settled; permissions for exceptions). Remove → an order-routing tool with no settlement, or a payment link with no order.

Jointly held: 1 alone = menu/kitchen ticketing; 2 without 1 = a bill with no menu semantics; 3 without 1+2 = a payment terminal; 1+2 without 3 = order entry that never settles; 2+3 without 1 = generic check presentment.

The sale-semantics contrast with Retail POS (ratifying that pass's finding from this side): retail's spine is *immediate paid sale* (payment completes the transaction at the moment of sale; returns reverse it). The restaurant spine is *order → check → payment → close*, where the check is a container that can stay open across a service period, be re-opened after closure, and be split/merged/transferred while open. Quick-service pay-first flows compress the timeline but keep the structure (the check is created and closed in one motion). The boundary is semantic, not structural — the same vendor ships both as modes of one product (Square's mode list is direct evidence).

### Level 1 — Common Mature Structure

Present across the sampled products; expected in the market; not required for recognition:

- **Service context on the order** — dining options (dine-in / takeout / delivery / curbside), responsible server, tables/floor plan, covers, seats, courses; ownership transfer (change server / reassign / transfer checks).
- **Kitchen routing** — items carry routing targets (prep stations / categories / printers / KDS screens); send/fire/hold semantics; coursing.
- **Money adjustments** — discounts, comps, voids with reasons, service charges, gratuities/tips (region-dependent), price overrides; all permission-gated.
- **Check surgery** — split checks, split payments, merge, move items between checks/guests/seats, transfer between servers.
- **Order lifecycle states** — open → paid (card flows) → closed; reopen; void/refund after closure; restricted/purged aged orders.
- **Cash management** — drawers (assign, blind/full close, drops, pay-outs), shift review, end-of-day / Z report / business-day cutoff.
- **Roles and permissions** — job/role-based permission sets; manager overrides; passcode entry; per-mode access (table service / quick order / payment terminal / kitchen).
- **Availability control** — item 86 / out-of-stock / quantity on hand at the point of sale.
- **Receipts and guest-facing display**; order and sales reporting; end-of-day closeout reports.
- **Offline resilience** (cloud generation) — orders/payments taken during outages, processed on reconnect.

### Level 2 — Variant / Optional Structure

Depends on segment, service model, geography, scale:

- **Service-model variants** — full-service (tables/covers/seats/courses central), quick-service (counter, pay-first, line busting), bar (open tabs, pre-authorization), cafe/fast-casual, food truck. Same core; different emphasis.
- **Bundled adjacent channels** — online ordering, kiosk, QR, delivery dispatch: orders land in the POS order stream, but each is its own Type.
- **Guest commerce modules** — loyalty, gift cards, house accounts, customer credits, marketing.
- **Reservations/waitlist integration** (host stand; hotel PMS posting at the hotel-F&B pole).
- **Inventory/waste/labor modules** — the POS feeds them (sales, depletion, time entries) but does not own their records.
- **Multi-location/enterprise configuration** — shared menus with inheritance, location-scoped edit rights, settings copy.
- **Fiscal compliance machinery** — country-specific invoicing/fiscal declarations (e.g., Spain's VERIFACTU at Oracle).
- **Payment-rail posture** — integrated native processing vs third-party processors; tips/customary-gratuity machinery is region-dependent.
- **Hardware form** — tablet/handheld vs fixed workstation vs phone app.

### Level 3 — Vendor-specific (Research Notes only)

- **Toast**: Toast Web admin; Toast Tables (waitlist/reservations); MyToast employee app + Team Chat; Delphi digital menu boards; Toast IQ (AI menu ops); clawback/tip withholding; RMA hardware process; Benchmarking; order purge service; auto-capture timing; "auction" (mis-routed tickets); "dupe"/"rail"/"wheel" kitchen slang in glossary; segment definitions (SMB 1–10 / MM 11–50 / Enterprise 50+ sites).
- **Square**: modes as pre-configured device profiles; device codes (12-digit shared sign-in); WoFlow menu import/upload; AI starter menu; Real Time Check View beta; covers-hold-table behavior; ordering profile channel; category-vs-menu split (reporting/routing vs buyer-facing).
- **Oracle Simphony**: OPERA PMS interface + posting; CAPS (Check and Posting) database; MICROS workstation hardware line; JavaScript/Kiosk extensibility APIs; Simphony Configuration transaction processing; VERIFACTU fiscal declaration; Learning Subscription.
- **SpotOn**: SpotOn Order / Reserve / Teamwork product family; Aries8/PAX hardware; SMS dine-in flow; station themes; rekeys.

## Historical / Market-Sample Check

- **Paper-era practice** (conceptual, high confidence): a handwritten guest check (prices taken from the menu), a cash drawer with a starting bank, manual end-of-day reconciliation — satisfies all three L0 legs at analog level. The check *is* the paper artifact the digital check descends from; Toast's own glossary preserves the vocabulary (guest check, dupe, rail, wheel, 86).
- **Legacy terminal generation**: Oracle Simphony (MICROS lineage, copyright 2010–2026) documents the workstation generation still in service — menu items added to an order, guest checks printed, payments recorded, PMS posting, KDS. Fits the core with no cloud/tablet/app-store requirement.
- **Toast's own generic definition** of a POS ("hardware, software, and support that manages sales transactions, including itemization, credit card processing, and receipt printing") names no cloud, tablet, or integrated-payment requirement.
- **Regional variance**: tipping/gratuity machinery is US-centric in the sample; the L0 carries no tip requirement. Quick-service pay-first and bar tab models both fit. Kiosk-heavy and QR-heavy markets still run a staff-facing transaction core behind the customer surfaces.

Conclusion: the definition is not over-fitted to the current cloud-tablet generation.

## Boundary Findings

### vs Retail POS (§05.10) — RATIFIED from this side

Shared spine: catalog-configured order → transaction → payment. Difference is **sale semantics**: retail = immediate paid sale + returns; restaurant = order → open check (service period) → payment → close, with service context (dining options, tables, servers), tips, and check surgery. Direct evidence that the boundary is semantic, not structural: Square ships Full service / Quick service / Bar modes *and* Retail mode as pre-configured profiles of the same POS app; Toast's Quick Order mode compresses the flow but keeps the order/check structure. No directory change.

### vs Restaurant Online Ordering (§26) — RATIFIED from this side

Composing actor + surface: the POS order is composed by **staff** on the restaurant's transaction surface; the online order is composed by the **customer** on the customer's own surface. Toast documents orders arriving from the website/API into the same replicated order stream; SpotOn documents pausing online ordering from the FOH; Square treats online ordering as a channel of the same menus. Staff-entered phone/off-premise orders are a POS function (Toast's Quick Order + dining options; Square's order types). Shared catalog/order stream in suite products is bundling, not identity.

### vs Restaurant Menu Management (§26)

Menu management owns the **menu of record** (catalog maintenance, pricing strategy, channel publication). The POS consumes it: Toast's menu builder lives in the admin web and must be *published* to reach POS devices; Square's menus are edited in the Dashboard and assigned to POS channels. The POS holds the operational catalog that drives order entry; it does not own catalog maintenance as its center. (This pass confirms the menu-management pass's "POS order entry = consuming surface" framing.)

### vs Kitchen Display System (§26)

The POS routes; the KDS fulfills. Toast: prep stations are *configured in the POS platform* and KDS devices display the routed orders; the KDS mode is a separate permission assigned to cooks/expediters. Oracle ships KDS as separate configuration documentation. The kitchen's production workflow (bump, all-day counts, expo) is the KDS Type's center.

### vs Restaurant Inventory Management (§26)

The POS sale is the **depletion input**; the stock record lives in the inventory system. The POS's own item-availability features (Toast stock status/86 report, SpotOn quantity-on-hand) are *availability control at the point of sale*, not a stock system of record — no receiving, counts, or valuation at this grain. Comp/void showing "in inventory reporting" (Square) is reporting integration, not ownership.

### vs Restaurant Management System (§26)

Transaction surface vs management layer. The RMS pass already held: POS anchoring is a packaging variant (Toast bundles POS + management; back-office poles run POS-free via integration). From this side: the POS's center is the live transaction (order/check/payment), not the plan-to-actual control loop; its reporting is transactional (sales, labor, cash), not managerial planning.

### vs Restaurant Reservation Platform (§26)

A reservation commits a table at a time; the POS runs the meal transaction. Integration is documented (Toast Tables permission; SpotOn Reserve; OPERA posting at the hotel pole) but the reservation lifecycle (bookings, waitlist, deposits) is not POS-owned.

### vs Self-service Restaurant Ordering (§26)

Kiosk = customer-operated venue device; POS = staff-operated transaction surface. Toast ships Kiosk as a separate product consuming the same menu hierarchy; Square treats kiosk as a channel. The composing-actor seam is the same one that separates POS from online ordering.

### vs Payment Processing / Gateway (§08)

The POS orchestrates the transaction and records tenders; processing moves the money. Integrated native processing is common-mature (all four sampled products are payments-led or payments-integrated) but not definitional — Toast's offline/background payment machinery exists precisely because processing can fail independently of the POS.

## Uncertainties

- **Order vs check object boundaries** vary by product; Toast makes the distinction explicit (order contains checks); other products' docs conflate "order" and "check" (SpotOn uses both terms; Square uses "check" in restaurant modes and "order" generically). The conceptual split (what must be fulfilled vs what must be settled) is a useful canonical reading, asserted at inference strength.
- **Exact state names** are product-specific (Toast: open/paid/closed; cash skips paid). The canonical lifecycle is written at concept level.
- **Simphony article-level detail** (menu configuration UI, tender flows) not fetched — its evidence is guide-preface/workstation-chapter strength. No Simphony-specific operational claims made beyond the fetched text.
- **SpotOn article bodies** did not render (dynamic content) — its evidence is index-level (concept set), not procedure-level. No SpotOn-specific procedural claims made.
- **Lightspeed Restaurant** unreachable again this pass (403 + transport error) — the hospitality-POS European pole remains under-observed; no claims made.
- **Tip/gratuity machinery** observed only in US-centric products; regional variation not directly sampled.
- Whether "open price" items (no menu price, entered at sale) weaken the menu-configured leg was considered: open items are an exception path (permission-gated in Toast: "Open Items" permission; Toast's own glossary calls them items "not included in a menu"), so the menu-configured leg stands as the primary rule with a documented exception path.

## Final Synthesis

A Restaurant POS is the **restaurant's operator-facing transaction system**: staff compose the guest's request as an order from the configured menu (items, prices, modifiers), the charges accumulate on a check that is the settlement unit (open across the service period, subject to splits, merges, transfers, discounts, comps, voids), payments settle the check, and closure completes and records the transaction. Around that core, mature products add the service context (dining options, tables, covers, seats, courses, server ownership), kitchen routing (prep stations, coursing, fire/hold), money machinery (tips, service charges, cash drawers, shift review, end-of-day), role-based permissions with manager overrides, availability control, and reporting. The Type's sale semantics — an open, surgically editable settlement container between order and payment — are what distinguish it from Retail POS's immediate paid sale, even though vendors ship both as modes of single products. Everything else — online ordering, kiosks, delivery dispatch, loyalty, inventory, labor, reservations — arrives as bundled channels or modules whose records those sibling Types own.
