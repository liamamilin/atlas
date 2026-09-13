# Research Notes — Tool Management

Research date: 2026-09-10
Directory leaf: Tool Management (§16 Engineering, Manufacturing & Industrial)
Slug: tool-management

## Research Goal

Understand what "Tool Management" software actually is as an Application Type in its industrial/manufacturing sense: what objects exist inside it (tools, cribs, transactions, tool data), what users do with them, how the tool flow works, what rules and states matter, and where its boundaries lie against neighboring Types — Equipment Administration Platform, CMMS, Calibration Management, Inventory Management System, Construction Equipment Management, CAM / CNC Programming, Enterprise Asset Management / Registry.

This leaf was flagged from six sibling passes:
- CMMS pass: "Tool Management / Calibration Management: narrow specializations that commonly ride inside a CMMS."
- Calibration Management pass: "tool cribs overlap (GAGEtrak ships a Crib module; gage issue/return is circulation). Tool management's center is tooling availability/consumption in production; calibration management's center is measurement trustworthiness."
- Equipment Administration Platform pass: "Tool management is the manufacturing/trades overlay of the same structure (tool cribs, calibration, machine-adjacent tooling)… Likely best treated as a segment overlay / near-variant; flagged lightly." Also: "Factory tool cribs — fit with the tool-management overlay; identity + handover + condition remain the core."
- Construction Equipment Management pass: "small tools vs heavy machines… Population becomes only small tools → tool management."
- Construction Materials Management pass: "tools are small durable reusable assets; materials are consumed. Population becomes reusable small tools → tool management."
- CAM pass / CNC Programming pass: "CAM references tools; Tool Management administers physical tool inventory. Different objects."

The central question for this pass: **is Tool Management merely an overlay of Equipment Administration Platform (records + handover + lifecycle), or does it hold defining structures of its own?**

## Initial Boundary

Hypothesis at start: industrial Tool Management is the management of an organization's physical production tooling — hand tools, power tools, machine/cutting tooling, gauges — as identified records, operating their circulation between a tool crib/storeroom and the people, jobs, and machines that use them, plus the tooling-specific supply economics (wear, regrind, reorder, chargeback). A second, machining-specific pole ("tool data management") manages cutting-tool assemblies and their production data (geometry, offsets, tool life) for CAM/CNC/presetting.

Likely confusions:
- Equipment Administration Platform (§10) — same skeleton (item records + handover + lifecycle); the "near-variant" flag must be resolved.
- CMMS (§16) — tools as assets with check-in/out inside maintenance software.
- Calibration Management (§16) — gage crib issue/return vs measurement-fitness semantics.
- Inventory Management System (§10) — crib stock of consumables vs general goods.
- Construction Equipment Management (§17) — heavy machines vs small tools.
- CAM / CNC Programming (§16) — consumers of tool data vs the system of record for tooling.
- Name collision: "tool management" in IT contexts (managing software tools) — out of scope; the directory places this leaf in the industrial section and all sibling passes read it as industrial tooling.

## Research Questions

1. What is the unit of record — the individual tool, the tool type/stock item, or the tool assembly? Which granularities coexist?
2. What is the core transaction loop? (issue/checkout, return, transfer, …) What surfaces execute it (crib attendant, kiosk, vending machine, scanner)?
3. Is there a supply/consumption loop (stock levels, reorder, consumption per issue, cost allocation)? Is it definitional or common?
4. What tooling-specific lifecycle events exist (wear, regrind/sharpen, repair, recalibration, recertification, scrap)?
5. What does the machining "tool data management" pole add (tool assemblies/components, geometry/measured data, tool life, CAM/CNC/presetter interfaces)? Is it the same Type or a different one?
6. How do tools bind to production (jobs, cost centers, machines, work orders)?
7. What role does hardware play (vending machines, smart cabinets, scanners, RFID)?
8. Where exactly is the seam against Equipment Administration Platform, CMMS, Calibration Management, and Inventory Management?
9. Historical check: does the paper-era tool crib (card file, sign-out board, regrind rotation, reorder practice) satisfy the proposed core?

## Representative Products

Selected for market representation, documentation accessibility, different product philosophies, different customer tiers, and coverage of both market poles:

| Product | Pole | Vendor / lineage | Customer tier | Evidence quality |
|---|---|---|---|---|
| CribMaster | Tool crib / vending / indirect materials | Stanley Black & Decker brand; since 1992/1996; 12K+ installations claimed | Enterprise (aerospace, automotive, MRO — e.g., Boeing case study) | Official SBD pages via search (direct fetch timed out ×2); third-party case study |
| ToolHound | Tool crib / tracking (software-first) | ToolHound Inc. (Canada); since 1985 | Mid-market industrial, construction, mining, utilities, oil & gas | Official site fetched (2 pages) |
| TDM Systems | Machining tool-data + crib | TDM Systems GmbH (Walter subsidiary, Sandvik Group); ~35 years | SME to global machining manufacturers | Official site fetched (3 pages) |
| Zoller TMS / webTMS | Machining tool-data + storage | ZOLLER (Germany); hardware+software system | Machining manufacturers, EU-centered, global | Official pages fetched + search excerpts |
| Limble CMMS (tools feature) | Boundary witness (CMMS module) | Limble CMMS | Mid-market maintenance teams | Official help-center article fetched |

Stop condition: after five products the two poles were each covered by two independent vendors, the CMMS seam was witnessed, and further fetches repeated existing patterns.

## Sources

Fetched directly (Tier 1/2):
- ToolHound — https://www.toolhound.com/ and https://www.toolhound.com/products/toolhound-system-overview (fetched 2026-09-10)
- TDM Systems — https://www.tdmsystems.com/en , /en/solutions/tool-management/what-is-tool-data-management/ , /en/solutions/shopfloor-management/tdm-tool-crib-module/ (fetched 2026-09-10)
- ZOLLER — https://www.zoller.info/en_DE/solutions/tool-management/software (fetched 2026-09-10); /en_DE/tool-management and /us/solutions/tool-management via search excerpts
- Limble CMMS — https://help.limblecmms.com/en/articles/7020225-using-tools-in-limble (fetched 2026-09-10 via search excerpt, official help center)

Reached via search excerpts only (official vendor surfaces; direct fetch timed out ×2 — abandoned per network rules):
- CribMaster — http://cribmaster.com/ , http://storage.stanleyblackanddecker.com/cribmaster/products/software , /cribmaster/solutions/storeroom-and-tool-crib-management , /cribmaster/solutions/low-touch-tool-vending , /cribmaster/products/software/cm-web , /cribmaster/about-cribmaster ; https://stanleyblackanddecker.com/brands/industrial/cribmaster

Tier 3:
- Reliable Plant — "Lean inventory control solution saves Boeing time and money" (https://www.reliableplant.com/Read/4891/lean-inventory-control-boeing) — independent description of CribMaster at Boeing Mesa.

**Source-access limitation:** cribmaster.com timed out twice and was abandoned. CribMaster evidence rests on official Stanley Black & Decker web pages reached through search plus one independent trade-press case study. No help-center/user-manual-grade operational documentation was fetched for any crib-pole product. Accordingly: no exact transaction-type lists, state vocabularies, numeric limits, or default values are asserted anywhere; vendor numeric claims are quoted as vendor claims and kept out of the final document.

## Product Observations

### CribMaster (Stanley Black & Decker) — crib/vending pole

Evidence layer: A (official pages, via search) + Tier 3 case study.

- Self-positioning: "Smart and Automated Inventory Management Solutions"; "Make sure the right tools & consumables are in the right place, at the right time"; "intelligent inventory and asset management solutions… improve the performance of manufacturing facilities and job sites"; 12K+ customers, 36 countries (vendor claim).
- Scope: "customizable storage for inventory of all sizes and types for everything from small inserts and bits, gloves and masks to cumbersome industrial equipment and I.T. and office consumables" — tooling + PPE + indirect materials.
- Software suite: "the brains behind your inventory management hardware… control over your indirect materials and asset flow… Track inventory issued from the store room or crib, view usage reports to reduce stock-outs and lower your indirect material spend, manage the amount and frequency that employees can issue items, and more."
- Components (module names, L3): CM Client (desktop backbone "connected to your inventory database"), CM Cloud, CM Web ("issue, return, receive and counting of items – all tracked by user, location and cost centers"), CM Mobile (smartphone scanner; "Remote Vend – Issue and Return from Your Mobile Phone"), CM ATR ("Automated Tool Room… point-of-use vending application that employees on the floor will use to issue and return items. ATR records each transaction and monitors inventory levels, alerting your Supply Chain or Operations team when it's time to replenish").
- Hardware anchor: industrial vending machines, smart RFID toolboxes/cabinets/portals (AccuPort), WeighStation (smart scales), FlexSense bin sensors ("automate replenishment of open stock"), Access+ badge-access locks; "17 UNIQUE solutions for point-of-use inventory dispensing", "33 TRANSACTION TYPES" (vendor claims).
- History: "began as Winware Inc., a simple software solution designed to track inventory usage among employees"; first software release for toolroom management 1996; RFID toolroom automation 2004.
- ERP integration: "can easily integrate with a variety of different ERP/IRP's… when it comes to monitoring the inventory activity."
- Boeing Mesa case (Tier 3): "a state-of-the-art inventory management system created specifically for managing tools and inventory in the manufacturing environment… uses bar coding and a collection of manned tool cribs and point-of-use dispensers to monitor tool inventory and usage, track consumption, issue purchase orders and provide numerous reports… tie together its tool cribs and dispensers, as well as the campus' electrical tool recertification group, the tooling receiving group and the buying group"; "nearly 1,000 issues, returns and counts… every day"; tool recertification group = tooling-specific service loop.
- British Airways Maintenance case: software-based management of "5,000 parts and 1,000 types of tooling that moved through their maintenance facility every day."

### ToolHound — crib/tracking pole, software-first

Evidence layer: A (official site, fetched).

- Self-positioning: "tool inventory management" since 1985; industries: construction, maintenance, petrochemical, mining, power generation, utilities, oil & gas.
- Core loop: "In its most basic form, the ToolHound inventory management system operates similar to a library to facilitate the quick and accurate check out and return of tools, equipment, and consumables from your tool room. But it's much more than that. Depending on the modules chosen, ToolHound manages scheduled service and calibration, purchasing and replenishment, self check out and return, and tool and equipment rentals."
- Circulation: "tracks the issue and return of tools to contractors and employees, as well as the transfer of equipment between various job sites and tool room locations"; "As tools are checked in and out, the ToolHound database is automatically updated to reflect an up-to-the-minute picture of all the valuable assets being tracked."
- Identification: "Durable bar code labels and RFID tags"; "In most situations, a combination of bar codes and RFID tags provide the best solution"; RFID enables "a self-serve tool crib application."
- Supply economics: "Alert when the inventory level for an item is low"; "Recapture tooling costs with automated billing for usage"; "Manage tool purchasing and resale"; Purchasing Module "monitors item availability and usage to create purchase orders."
- Service: Service Module "Monitors and schedules maintenance of items needing repair, maintenance or calibration."
- Rental (construction pole): Transaction Rental Module ("rental rates, discounts, billing and sales reporting based on tool issues"); Transfer Rental Module ("internal rental rates and manual charges for flexible bill-by-project reporting based on tool transfers to jobs").
- Self-service: Kiosk ("workers can checkout and return their own tools using a simple-to-use touch screen computer and bar code or RFID reader").
- Deployment: web-based; ToolHound Cloud (vendor-hosted) or On Premise (client-hosted).
- Multi-site: "whether at one location or multiple job sites"; "nation-wide inventory and… transaction history."

### TDM Systems (Sandvik/Walter) — machining tool-data pole + crib

Evidence layer: A (official site, fetched ×3 pages).

- Self-positioning: "the leading software provider for managing tool data in the metal cutting industry"; "100% Tool Management"; ~35 years; wholly-owned Sandvik subsidiary.
- Vendor's own definition (What is Tool Data Management?): "Cutting tools need to be on the right machine at the right time… A uniform database for tools is an indispensable prerequisite… The TDM software solutions organize and integrate tool data in all phases of planning and production. They represent the **link between ERP, PLM, and MES**. Firstly, they record the master data in a **central database**. TDM makes the information on items and tool assemblies, including 2D drawings and 3D graphics, available for CAM and simulation systems. Secondly, the software physically organizes tool circulation at shopfloor level. It thereby establishes the necessary transparency regarding tool inventories, as well as the condition and current location of tools."
- Homepage capability list: "Assembly and classification of items and tool assemblies; Transparency on the shopfloor; Connection to crib systems; Transparency in tool crib management and simple crib entries; Simple and cost-efficient tool ordering process; Interfaces to most common presetters; Simple connection to common CAD/CAM systems; Control of tooling costs; Independent of the manufacturers – any tool from any manufacturer supported."
- "TDM supports your processes and organizes tool circulation."
- Tool Crib Module: "The right tool at the right time in the right location… organize your crib inventories efficiently and maintain complete cost control… It keeps track of all movements and thereby guides you securely through the tool cycle in production. The module is an important basic function in the holistic Tool Lifecycle Management process. It records the inventories of tools and production equipment… also processes information on their condition and location… supports ordering processes, controls and manages automated and manual crib systems, and ensures optimum crib inventory levels."
- Crib mechanics: "organizes items and tool assemblies by inventory and crib location, taking into account the current location of the tool… can be used with both manual and automatic crib systems. Barcode scanners are supported"; "The structure of the crib and cost centers has a variable configuration"; "connection to automated crib systems or vending machines"; "TDM takes into account both new and used articles, and users can define wear parts"; "users can book new entries and movements of the tools between crib, production costs centers, and repairs, as removals including stating the reasons"; "bookings at various data levels: From individual items, through tool assemblies and their parts lists, all the way up to complete tool lists and difference lists"; "intuitive minimum stock check facilitates prompt order management"; "availability check reduces tool-related machine downtimes"; "crib controlling offers transparency through creating of statistics."
- Wider module ring (L3): Feeds & Speeds Manager, Gauge & Calibration Management, Fixture Management, NC-Program Manager, Facility & Maintenance Management, Multi Plant Management, Machine Web Client, Shopfloor Manager, ScanEasy, Range Calculator, TDMstoreasy, Purchase Requisition Module, Data & Graphic Generator, Collision Data Generator, WebCatalog, ToolsUnited; interfaces: CAM, MES, FMS, machine integration, presetter, tool crib, ERP.
- Products: TDM ClassiX (on-premise), TDM Global Line (on-premise, medium-large), TDM appCom, TDM iCut.

### ZOLLER TMS / webTMS — machining tool-data pole, hardware+software system

Evidence layer: A (official pages fetched + search excerpts).

- Self-positioning: "Tool Management Solutions for Manufacturers"; "Unlock the potential between your tool store and CNC machine"; combines "four levels into one unit: Smart Cabinets…, TMS Tool Management Solutions and WebTMS (software solutions), and numerous CAM interfaces."
- Data scope: "Master data, storage location data, geometry measurement data, tool life - everything can be called up at any time for production planning"; "from the management of your tool store and NC program management to tool requirement optimization and the automatic updating of tool life data"; "Standardized data according to DIN/ISO"; "Order management"; "3D storage location management."
- Software structure (L3 names): TMS Core ("the start point for digital tool management") + add-ons: z.Stock ("Ensures clear transparency in the tool warehouse"), z.CAM Integration, z.Resources ("Manages all additional resources"), z.Shopfloor ("Seamless, efficient tool lifecycle directly on the shop floor"), z.Connectivity ("connection between tool measurement, tool management and the machine"), z.Integration ("Vendor-neutral tool management solution"); webTMS ("Call up tool data, check the location of the tools, or check the stock and decide what needs to be reordered").
- Hardware ring: smart tool cabinets (twister, autoLock, toolOrganizer, keeper), z.Storage dispenser, assembly stations (zTower, toolStation), tool carts, zidCode data transfer ("Your tools are automatically transferred from the tool preparation area to the CNC machine – or to the tool magazine. And back again."); presetting & measuring machines feed measured geometry into the system.
- Vendor claim: "Savings potential for tool costs 20%" (kept out of final document).

### Limble CMMS tools feature — boundary witness (CMMS module)

Evidence layer: A (official help center).

- "Adding your tools to Limble helps you keep track of where your organization's tools are, who is using them and for what purpose, and overall equipment usage."
- "Creating a tool does not require a special set-up; **tools are simply assets marked as tools**. The benefit of tools being assets is that you can set up preventative maintenance or calibration schedules, track depreciation, and associate them with tasks."
- Check in/out: "Limble keeps a log of when a tool is checked in or out, who is using the tool, and what the tool is needed for." Optional checkout approval workflow; permission-gated.
- Association with tasks/work orders (PM templates and open tasks).
- **No stock/replenishment/consumption accounting for tools** observed in the tool feature — tools are assets with custody logs, not a managed supply. This is exactly the CMMS shape the sibling pass predicted.

## Cross-product Comparison

| Dimension | CribMaster | ToolHound | TDM Systems | Zoller TMS | Limble (witness) |
|---|---|---|---|---|---|
| Tooling population of record | items + assets (tools, PPE, indirect materials) | individual tools/equipment/consumables, labeled | items + **tool assemblies** of components + production equipment | components + complete tools + additional resources | tools = assets marked as tools |
| Issue/return circulation | issue/return/receive/count; crib + vending + mobile | checkout/return "like a library"; transfers between sites/rooms | crib bookings: entries, movements crib↔cost centers↔repairs, removals with reasons | shopfloor tool lifecycle; storage-location management | check in/out with log |
| Consumption/replenishment | usage reports, stock-out reduction, replenishment alerts, spend control | low-stock alerts, purchasing module, billing for usage | wear parts, min-stock check, ordering, cost control | stock transparency, reorder decisioning, order management | absent |
| Cost allocation | by user, location, cost center | billing for usage; rental rates; bill-by-project | bookings to production cost centers; tooling-cost control | (tool-cost framing) | absent |
| Tooling-specific service loop | tool recertification group (Boeing case) | Service Module: repair/maintenance/**calibration** | movements "to repairs"; Gauge & Calibration module (separate) | tool measurement/presetting feeds | PM/calibration schedules on tool-assets |
| Production binding | jobs/workers at point of use | contractors/employees, job sites | cost centers, machines, "right tool on the right machine at the right time" | tool store ↔ CNC machine; production planning | task/work-order association |
| Tool production data (geometry/offsets/tool life) | absent | absent | central: master data, 2D/3D graphics, for CAM/simulation; presetter/machine interfaces | central: geometry measurement data, tool life, DIN/ISO, CAM interfaces, zidCode to machine | absent |
| Identification hardware | barcode, RFID, vending, scales, bin sensors, badge locks | barcode + RFID labels, scanners, kiosk | barcode/chips; manual + automated cribs | chips (idChip), smart cabinets, zidCode | QR (asset-level) |
| Multi-site | enterprise-wide, global | multi job-site/nation-wide | Multi Plant Management | multi-device/web access | multi-site (CMMS-level) |
| Deployment | CM Cloud / on-prem client | Cloud or on-premise | on-premise (ClassiX/Global Line) | local packages + webTMS cloud | cloud SaaS |
| Rental management | — | Transaction + Transfer Rental modules | — | — | — |
| PPE / indirect materials breadth | central ("gloves and masks… IT consumables") | consumables included | production equipment breadth | aids/test equipment in cabinets | — |

Reading of the comparison (evidence layers):
- **B (cross-product commonality, 4/4 dedicated products):** tooling population of record; issue/return circulation with recorded transactions; consumption/replenishment with reorder; cost allocation to users/cost centers/jobs; identification via labels/chips; multi-location; reporting.
- **Pole-specific (2/4, machining pole only):** tool assemblies/components; geometry/measured data; tool life; CAM/CNC/presetter/machine interfaces; standardized data exchange.
- **Pole-specific (crib/construction pole):** rental management; PPE/indirect-materials breadth.
- **Witness contrast:** the CMMS tool module holds population + check-in/out (+ asset maintenance) but lacks the supply/consumption economics — supporting that the supply loop is what the dedicated Type adds.

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The tooling population of record.** The organization's production tooling held as persistent identified records: tool/item types carried as stock positions, individually identified physical units (labeled/barcoded/chipped), and — in the machining pole — tool assemblies composed of components. Each record carries location, custody, and status/condition.
   *Remove → a spreadsheet stock list or an anonymous sign-out sheet; nothing for the circulation to operate on.*

2. **The issue/return circulation loop.** Recorded transactions move tools between storage (tool crib, storeroom, cabinets, vending/point-of-use dispensers) and the points of use (people, jobs/cost centers, machines), advancing custody and availability and leaving an attributable trail (who took what, when, for what). Self-service capture (kiosk, vending, RFID) is a common surface, not the structure.
   *Remove → a static asset register or stock list; the "who has what" accountability and the crib operation disappear.*

3. **The tooling supply & consumption loop.** Tooling is managed as a consumed and decaying supply, not merely held: usage/consumption is recorded per issue; tools cycle through wear → service (repair/regrind/recalibration/recertification) → return to stock or scrap; minimum-stock/reorder machinery replenishes the population; and usage is charged back (to users, cost centers, jobs/projects).
   *Remove → a checkout tracker with no supply economics (the CMMS tool-module shape), or a stockroom with no circulation accountability.*

Jointly-held is load-bearing:
- 1 alone = tool inventory spreadsheet / asset list
- 2 without 1 = sign-out sheet with nothing behind it
- 3 without 1+2 = purchasing/replenishment over untracked stock (generic inventory tooling)
- 1+2 without 3 = library-style checkout tracker (equipment-administration / CMMS-tool-module shape)
- 1+3 without 2 = storeroom stock management with no custody accountability
- 2+3 without 1 = transactions and reorders with no identified population

### L1 — Common Mature Structure (present across the sample, not definitional)

- Barcode/RFID/chip identification of tools + mobile scanners/kiosks as capture surfaces (4/4 dedicated products)
- Service/maintenance/calibration scheduling attached to tools (ToolHound Service Module; CribMaster recertification case; TDM repairs + separate gauge/calibration module; Limble PM/calibration on tool-assets)
- Purchasing/replenishment module (ToolHound Purchasing; CribMaster replenishment alerts + purchase orders; TDM Purchase Requisition; Zoller order management)
- Usage-based cost allocation / chargeback (all four dedicated products)
- Multi-location / multi-crib / multi-plant operation (4/4)
- Usage reporting / crib controlling statistics (4/4)
- ERP integration for inventory/purchasing activity (CribMaster, TDM; Zoller via ERP data transfer)
- Rental management for tools (ToolHound — construction pole; likely common in that segment, unverified breadth)

### L2 — Variant / Optional Structure

- **Machining tool-data pole** (TDM, Zoller): tool assemblies/components with bills of components; geometry/measured data from presetters/measuring machines; tool-life data; CAM/CNC/simulation/machine interfaces; standardized exchange (DIN/ISO); tool catalogs/marketplaces. Absent in the crib pole — a pole differentiator, not a Type requirement.
- **Point-of-use dispensing hardware** (CribMaster vending/scales/bin sensors; Zoller smart cabinets/dispensers): the software Type is the record/transaction system; hardware is a capture/storage surface.
- **Industry overlays**: construction (job-site transfers, rental billing), power generation/utilities/mining/oil & gas (ToolHound industries), aerospace MRO tooling (CribMaster case), metal-cutting machining (TDM/Zoller).
- **PPE / indirect-materials breadth** (CribMaster): the crib pole shades into indirect-material (MRO/PPE) inventory management.
- **Deployment**: cloud SaaS vs on-premise vs vendor-hosted; desktop client vs web vs mobile.
- **Gage crib overlap**: measurement instruments circulate through the same issue/return machinery (calibration semantics belong to Calibration Management).

### L3 — Vendor-specific (Research Notes only)

- CribMaster: CM Client/Cloud/Web/Mobile/ATR naming; Remote Vend; Access+; ProStock; FlipTop; WeighStation; AccuPort; FlexSense; "33 transaction types"; "17 point-of-use solutions"; 12K+ customers/36 countries; "25 to 40%" consumable-spend reduction claim; Winware lineage; 1996/2004/2014–2023 timeline.
- ToolHound: module names (Purchasing, Service, Kiosk, Transaction Rental, Transfer Rental); "cut tool crib expenses by 30%" customer testimonial; "since 1985"/"40 years" claims.
- TDM Systems: ClassiX/Global Line/appCom/iCut product names; Tool Crib Module, TDMstoreasy, ScanEasy, Range Calculator, Shopfloor Manager, Purchase Requisition Module, Feeds & Speeds Manager, Gauge & Calibration Management, Fixture Management, NC-Program Manager, Multi Plant Management, WebCatalog, ToolsUnited, z.One-equivalents; "up to 30% time savings in tool allocation" claim; "35 years"; "only provider… exclusively tool data" claim; Sandvik/Walter ownership.
- Zoller: TMS Core + z.Stock/z.CAM Integration/z.Resources/z.Shopfloor/z.Connectivity/z.Integration add-on names; Bronze/Silver/Gold packages; webTMS; zidCode; idChip; smart cabinet product names (twister/autoLock/toolOrganizer/keeper/z.Storage); "20% tool-cost savings" claim.
- Limble: "tools are simply assets marked as tools"; permission #196 'Asset Check In/Out' and #197 'Bypass Tool Check Out Approval'.

## Vendor-specific Findings

See L3. None promoted to the canonical model. Notably:
- The vending/point-of-use hardware anchor (CribMaster's center of gravity) is an implementation surface for the same transaction loop; a tool management product without any vending hardware (ToolHound software-first; TDM/Zoller software+crib) satisfies the core.
- The CNC tool-data leg is the machining pole's differentiator; the crib pole runs the full core without it.
- Rental management is a construction-segment extension (ToolHound), not observed in the machining pole.

## Boundary Findings

1. **vs Equipment Administration Platform (§10) — the flagged "near-variant" question. RESOLVED as distinct-but-adjacent.** The two Types share the skeleton (identified item records + recorded handover + lifecycle state). Tool Management's additional defining leg is the **supply & consumption loop** (stock positions, consumption per issue, wear/regrind/recalibration cycles, reorder, usage-based chargeback) plus **production binding** (issue destinations are jobs/cost centers/machines; availability gates production). Equipment Administration centers the custody/readiness loop over general shared equipment (AV, education, construction, healthcare) without supply economics as the spine. Removal tests: strip the supply/consumption loop from a tool-management product → an equipment-administration/checkout-tracker shape (exactly what the Limble witness shows); add supply economics + production binding to an equipment pool → it is operating as tool management. Products straddle (Timly markets both vocabularies on one site — recorded by the sibling pass); the seam is the supply loop, and the flag is discharged with keep-both.
2. **vs CMMS (§16).** CMMS centers maintenance work management (assets + work orders + history); tools ride inside as assets with check-in/out (Limble evidence, verbatim). Tool Management centers the crib circulation + supply loop; tool repair/regrind is a loop endpoint (send out, receive back), not a work-order spine. Removal test: make maintenance work orders the center over the tool population → CMMS. The "rides inside a CMMS" sibling claim is confirmed as a module-level relationship, not Type identity.
3. **vs Calibration Management (§16).** Gage crib issue/return is circulation machinery this Type provides; calibration semantics (procedures, intervals, as-found/as-left, certificates, traceability) are the other Type. TDM itself packages "Gauge & Calibration Management" as a separate module — vendor-confirmed seam. A gage crib inside tool management without calibration semantics stays here; measurement-fitness machinery → Calibration Management.
4. **vs Inventory Management System (§10).** The crib pole manages consumable stock (inserts, gloves, masks) with min/max/reorder — inventory-like. The seam: the tooling population's individual identity + circulation + production binding. A pure goods stockroom without identified circulating units → Inventory Management; CribMaster's indirect-materials breadth is a documented gradient, not a merge.
5. **vs Construction Equipment Management (§17).** Heavy machines/fleet (telematics, utilization, maintenance) vs small tools; mixed-fleet products track small tools as an adjacent population (sibling pass verbatim). Population becomes only small tools → this Type.
6. **vs CAM / CNC Programming (§16).** CAM consumes tool assemblies/data inside programs; Tool Management is the system of record for tooling data and inventory that CAM/presetting/machines draw from (TDM: "link between ERP, PLM, and MES… available for CAM and simulation systems"). Sibling passes recorded the same seam from their side.
7. **vs Enterprise Asset Management / Registry (§16/§10).** EAM holds whole-life governance over major assets; the registry holds holdings. Tooling is a high-churn, low-unit-cost, circulating population managed as supply — different object economics. Tooling records may feed an EAM/registry; the circulation+supply loop is not EAM structure.
8. **Name collision note.** "Tool management" in IT/software contexts (managing developer tools, AI agent tool registries) is a different subject entirely; the directory leaf is the industrial Type and this pass documents only that.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0?

- **Paper-era tool crib (mid-20th century practice):** a crib inventory list/card file of tools (population of record), a sign-out board/card system run by the crib attendant (circulation loop), a regrind/sharpen rotation with scrap decisions and reorder when stock ran low, with departmental chargeback (supply & consumption loop). Satisfies all three legs with no barcode, RFID, vending, cloud, or CNC interfaces. ✓
- **Regional/European machining practice (TDM/Zoller pole)** satisfies the same three legs plus the tool-data leg; the definition does not depend on the data leg. ✓
- **Construction job-site practice** (tools moving between sites and contractors) satisfies the three legs with job sites as issue destinations. ✓
- The L0 does not depend on: vending hardware, RFID/barcode, cloud delivery, CAM/CNC interfaces, rental modules, PPE breadth, or any specific transaction-type vocabulary.

## Uncertainties

1. **CribMaster direct fetch failed** (timeout ×2, abandoned). Evidence is official-vendor-page strength via search plus one independent case study. No operational manual-grade detail asserted for CribMaster anywhere.
2. **No Tier-1 help-center/user-manual documentation fetched for any crib-pole product.** Exact transaction-type lists, state vocabularies, permission models, and numeric limits are unknown; none are asserted. CribMaster's "33 transaction types" is a vendor claim, unenumerated.
3. **Reservations/booking** (present in Equipment Administration products) were not observed in any fetched tool-management page; not asserted either way.
4. **Rental management breadth**: observed only in ToolHound (construction pole); whether rental is common across the crib pole is unverified — held as pole/segment variant.
5. **The exact population boundary of the crib pole** (tools only vs tools + PPE + indirect materials) varies by vendor; CribMaster is broadest. Held as a gradient.
6. **Zoller/TDM numeric benefit claims** (20% cost, 30% time) are vendor marketing — recorded here, excluded from the final document.
7. Whether a pure tool-data system *without* physical circulation exists as a product (tool catalogs like ToolsUnited/WebCatalog are data services, not management systems) — treated as the pole's outer edge, not a separate Type.

## Final Synthesis

Tool Management (industrial) is the **production-tooling supply system of record**: it holds the organization's tooling as an identified population (tool/item types with stock, individually labeled units, and — in the machining pole — tool assemblies of components), operates the circulation of those tools between crib/storage and the people, jobs/cost centers, and machines that use them through recorded issue/return/transfer transactions, and runs the tooling supply & consumption loop — usage recorded per issue, wear/repair/regrind/recalibration cycles, minimum-stock/reorder replenishment, and usage-based cost allocation. Around this core, mature products add barcode/RFID identification with scanners/kiosks, service & calibration scheduling for tools, purchasing modules, multi-location operation, usage reporting, and ERP integration. The market splits into two poles sharing the same core: the **crib/tracking pole** (CribMaster, ToolHound — general industrial tooling, often with PPE/indirect materials, vending/point-of-use hardware, construction rental) and the **machining tool-data pole** (TDM Systems, Zoller — cutting-tool assemblies with geometry/measured data and tool life, delivered to CAM/CNC/presetting). The CMMS tool module (population + check-in/out, no supply economics) is the documented "minus-one" shape that confirms the supply loop as the Type's distinguishing leg; the Equipment Administration Platform "near-variant" flag is resolved the same way — shared skeleton, differentiating supply/consumption + production binding. The paper-era tool crib satisfies the core without any modern machinery.
