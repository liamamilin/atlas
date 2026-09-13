# Research Notes — Feed Management

Research date: 2026-09-08

## Research Goal

Understand what a Feed Management application is as an Application Type: its core objects (ingredients, rations, groups, loads, inventory), the daily feeding loop, how formulation and feed economics work, which rules and states matter, and where the boundary lies against neighboring Types (Dairy Farm Management, Livestock Management, Aquaculture Management, Farm Management Platform, Food Formulation Platform, Grain Management, feed-mill ERP).

Note on directory context: the leaf sits in §20 Agriculture, Food & Natural Resources between Swine Management and Aquaculture Management — i.e. the livestock-feed discipline, not the e-commerce "product data feed management" tools referenced in the PIM research pass (a pure homonym; recorded below under Boundary Findings).

## Initial Boundary Hypothesis

- Core use: manage the feed side of animal production — formulate rations, maintain feed supply/inventory, execute and record feeding to animal groups, track feed cost and loss.
- Users: nutritionists, feed managers/feeders, farm managers, feed-mill formulators and purchasing staff.
- Nearest neighbors: Dairy Farm Management / Livestock Management (feeding as a layer inside animal-centered systems), Aquaculture Management (feeding as execution inside the rearing loop), Food Formulation Platform (same recipe/nutrient-matrix machinery, different recipient), Grain Management (grain as commodity, not as fed supply), feed-mill ERP (business layer around feed manufacturing).
- Boundary expectations from sibling passes: dairy research concluded "ration formulation/feed inventory is a distinct discipline; the herd system links to it or embeds a feeding layer but its core is the animal, not the ration"; aquaculture research concluded "Feed Management concerns feed formulation/inventory for feed operations; aquaculture feeding is an execution/recording activity inside the rearing loop."

## Research Questions

1. What is the unit of record — the ration, the ingredient, the load, the group?
2. How does formulation work (nutrient targets, ingredient matrices, least-cost optimization, constraints)?
3. How does the feeding execution loop work (schedules, batches/loads, guided mixing, delivery to groups, weighback/intake)?
4. How is feed supply managed (inventory, procurement, shrink/loss)?
5. How does feed cost become visible (cost per ton/head/day, scenario simulation)?
6. What integrations matter (herd management pen counts, scales/mixer wagons, feeding robots, lab/NIR data, ERP/MES/LIMS, milk computers)?
7. What are the segment poles (on-farm vs feed-industry/mill) and do they share one core?
8. Where are the boundaries vs the neighbors listed above?
9. Would older / regional / platform-native products still fit the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| VAS FeedComp (US) | on-farm dairy feeding execution | dedicated dairy feed-management product; herd-integrated; official product pages fetched |
| BESTMIX / Adifo (BE) | feed-industry formulation + ERP | leading formulation & recipe management for feed mills/premix/aquafeed; official product pages fetched |
| WinFeed (UK) | minimal desktop formulation | lowest-cost pole; pure least-cost formulation tool; official site + docs fetched |
| Lely Vector + Horizon (NL) | automation-embedded feeding | ration/group logic inside a robotic feeding system; official product page fetched |
| (TMR Tracker, US) | on-farm TMR/feeding execution | unreachable after 2 fetch attempts — dropped per network rule; cited in sibling dairy research as the deep-pole reference |

Pole spread: execution-first (FeedComp) / formulation-first (BESTMIX, WinFeed) / automation-embedded (Lely); customer levels from single-farm desktop (WinFeed) to enterprise mill suites (BESTMIX); geographies US / EU / UK.

## Sources

- VAS — https://vas.com/ (Feed product line: FeedComp, WeighComp), https://vas.com/feedcomp/ — fetched 2026-09-08
- BESTMIX (Adifo Software) — https://www.adifo.com/en/ , https://www.adifo.com/en/products/bestmix-recipe-management-feed — fetched 2026-09-08
- WinFeed — http://www.winfeed.com/ (home, features, documentation links) — fetched 2026-09-08
- Lely — https://www.lely.com/en/innovation/automatic-feeding/ , https://www.lely.com/solutions/feeding/vector/ — fetched 2026-09-08
- Sibling research passes (internal): research/dairy-farm-management.md, research/aquaculture-management.md, research/product-information-management-pim.md

Source-access limitations: tmrtracker.com returned empty responses twice (abandoned). Trouw Nutrition NutriOpt domain is a parked storefront (no product docs). Afimilk feeding page 404. Claims below therefore rest on 4 fetched product sources + sibling-pass evidence; precision held accordingly.

## Product Observations

### VAS FeedComp (vas.com) — on-farm dairy pole

Evidence layer: A (directly observed on official pages)

- Positioned explicitly as "Simple, accurate feed management"; "bring your feeding program to the palm of your hand"; part of the VAS PULSE platform's separate FEED product line (FeedComp, WeighComp) beside the Dairy (DairyComp) line.
- Value framing: feed is "your most expensive input"; "Traceable — gain visibility into inventory, shrink and loss"; "Accountable — unite your entire team"; "Accurate — optimize pen feeding with always accurate counts from DairyComp".
- Stated workflow ("How FeedComp Works"):
  1. "Enter Your Rations — set up recipes, create a feeding schedule or make batch loads"
  2. "Mix with Guidance — follow real-time instructions to ensure every load is mixed correctly"
  3. "Track everything — automatically record ingredient usage, weighback pickups, animal intakes and inventories"
  4. "Optimize your feed program — identify where feed is being lost and make informed decisions"
- Deployment shape: "user-friendly mobile app and a Bluetooth-enabled scale"; cost savings via "reduce feed waste, track shrink and mix more accurately".
- Integration: pen counts pulled from herd management (DairyComp) so loads match actual animal numbers.

### BESTMIX Recipe Management / ERP Suite (adifo.com) — feed-industry pole

Evidence layer: A

- "Strategic software for feed, food and pet food producers"; industries: Feed & Ration, Aquafeed, Premix, Pet Food, Food, Trading, Meat Processing; 1500+ customers, 5000+ plants, 25000+ daily users (vendor figures, marketing — treat as scale signal only).
- Recipe Management: "formulate nutritionally precise and production-ready recipes"; "optimize every recipe for cost, quality, and compliance"; "automatically considers factors such as moisture loss, enzyme activity, and industry standard modelling"; "lowest possible cost per ton"; linking "nutrition science with real-world production constraints".
- Ingredient matrices: "frequently re-formulate based on the actual market situation"; "having up-to-date ingredient matrices in your formulation system is essential"; real-time sample data pulled into matrices without manual input; ingredient analysis variability handled via QC (tolerances, analytical schemes).
- Scenario/what-if: "reoptimize recipes instantly when raw material prices, nutrient values, or availability shift, simulating multiple scenarios".
- Precision-feeding bridge: "connects livestock performance data directly to feed formulation, enabling nutritionists to integrate insights from milk computers, feeding systems, and herd management software: transforming average-based feeding into true precision nutrition."
- Compliance/documentation: automatic generation of "compliant labels, product specifications, and declarations"; medicated feed labeling; annual updates of U.S. and Canadian compendia.
- Suite context: Quality Control module; ERP Suite with "ingredient contracts, … actual market prices, … what-if scenarios"; logistics/warehousing; ERP/MES/LIMS integration ("single source of truth across formulation, quality, and purchasing").
- Collaboration: cloud-based multilingual platform; nutritionists, formulators, planners "work together on shared recipes, specifications, and performance insights".

### WinFeed (winfeed.com) — minimal formulation pole

Evidence layer: A

- "Least Cost Feed Formulation" desktop package (Windows); "equally useful for ruminants, non-ruminants, poultry, pets and fish".
- Formulation modes: Linear (linear programming) and "Stochastic" (probability-based assurance of meeting nutrient requirements) — vendor claims world-first stochastic; treat as product claim.
- Objects: "unlimited number of Ingredients and Nutrients"; "Feed Store Files (Feedstuff Composition Database)"; formulas with "Marginal price, Shadow Price and Cost Analysis"; nutrient ratios; backward formula analysis.
- Batch output: "mixing sheet for any batch size" (demo cap 20 ingredients/nutrients); Excel import/export; pie/bar chart reports; formula synchronization/update of previous formulas.
- No inventory, procurement, feeding execution, or herd integration observed — pure formulation math + batch sheet. Positioned at universities as a teaching tool.

### Lely Vector + Horizon (lely.com) — automation-embedded pole

Evidence layer: A

- Hardware-defined feeding system: mixing and feeding robot + "feed kitchen where the feed is stored, selected, and loaded".
- Ration logic: "every animal group access to a fresh and precisely mixed ration based on their needs"; "precise feeding adapted to each group of animals"; precision framing.
- Execution accuracy claims: "feeding accuracy of the products loaded into the mixing and feeding robot of up to 98%"; reduces "rest feed".
- Management layer: "the associated management system" (T4C / now Horizon) "advises on feed kitchen designs… start up support on how to operate the Vector and the associated management system"; data "brought together in Lely Horizon" with feeding insights among farm data.
- Boundary signal: the software exists to run owned feeding hardware; ration/group management is embedded, not a standalone management discipline product.

### Sibling-pass evidence (internal, layer B)

- Dairy Farm Management research: feeding layer depth varies "from simple allocation tracking to linked dedicated feed-management products"; named the deep pole as separate feed products (TMR Tracker, FeedComp, AfiFeed); boundary statement: "the herd system links to it or embeds a feeding layer but its core is the animal, not the ration."
- Aquaculture research: "Feed Management concerns feed formulation/inventory for feed operations; aquaculture feeding is an execution/recording activity inside the rearing loop."
- PIM research: e-commerce "feed management" tools (product-data feeds for ad/exchange channels) are a different domain sharing the name — the PIM doc explicitly distinguishes them as downstream catalog syndication, unrelated to livestock feed.

## Cross-product Comparison

| Structure / capability | FeedComp (on-farm) | BESTMIX (mill) | WinFeed (desktop) | Lely Vector (embedded) |
|---|---|---|---|---|
| Feed items with composition + cost | ✓ (ingredients, usage, inventories) | ✓ (ingredient matrices, contracts, market prices) | ✓ (ingredients, nutrients, composition database) | ✓ (feed kitchen components) |
| Ration/recipe as plan bound to nutrient targets | ✓ ("Enter Your Rations", recipes) | ✓ (recipes, nutrient targets, compliance specs) | ✓ (formulas, nutrient requirements) | ✓ ("precisely mixed ration based on their needs") |
| Ration attached to a recipient (group/species/product) | ✓ (pens/groups via herd counts) | ✓ (animal types; feed products) | ✓ (species: ruminants/poultry/fish/pets) | ✓ (animal groups) |
| Quantified feed flow (batches/loads/mixing) | ✓ (batch loads, guided mixing, weighback) | ✓ (production-ready recipes; ERP production) | ✓ (mixing sheet per batch) | ✓ (robot loading/mixing/delivery) |
| Supply-side inventory & procurement | ✓ (inventories, shrink/loss) | ✓ (ingredient contracts, purchasing, forecasting) | — | partial (kitchen stock, rest feed) |
| Least-cost / optimization formulation | not observed (ration entry, not optimizer) | ✓ (cost per ton, reoptimization, what-if) | ✓ (linear programming, shadow prices) | not observed |
| Feeding schedule per group over time | ✓ (feeding schedule) | — (mill produces feed, doesn't feed) | — | ✓ (frequent feeding per group) |
| Execution recording: actual usage vs plan | ✓ (automatic recording, loss analysis) | indirect (production/QC data) | — | ✓ (loading accuracy, rest feed) |
| Feed cost analytics | ✓ (waste, shrink focus) | ✓ (cost per ton, margin framing) | ✓ (cost analysis, shadow price) | — |
| Livestock performance feedback into formulation | ✓ (herd integration for counts; herd+feed insights) | ✓ (milk computers, feeding systems, herd software → precision nutrition) | — | ✓ (group needs; Horizon insights) |
| Hardware integration (scales, mixer wagons, robots) | ✓ (Bluetooth scale) | — | — | ✓ (robot + kitchen, own ecosystem) |
| Compliance/label/spec documents | — | ✓ (labels, specs, medicated feed, compendia) | — | — |
| Multi-plant / multi-team cloud collaboration | — | ✓ (cloud, shared recipes, ERP suite) | — | — |

Reading: three structures are jointly held by all four — (1) feed items as records with composition and cost, (2) the ration/recipe as a nutrient-target plan bound to a recipient, (3) the ration realized as quantified feed (batches/loads) moving through supply to animals. Everything else varies by pole.

## Canonical Model

### L0 — Defining Invariant (jointly-held, minimal)

A Feed Management application manages the feed side of animal production as its own subject. Three structures are jointly held; removing any one destroys the Type:

1. **Feed items as managed records** — ingredients/commodities (and mixed feeds/premixes) held as identified records carrying nutrient composition and cost. Remove → generic recipe tool or grain ledger with no nutrition semantics.
2. **The ration as the feeding plan of record** — a recipe binding a mix of feed items to nutrient targets for a defined recipient (an animal group/species/life stage, or a feed product), maintained and revised over time. Remove → feed inventory/accounting without the "what should they eat" discipline.
3. **The quantified feed loop** — the ration converted into measured quantities (mixing sheets/batch loads/schedules), executed with actual usage moving through supply to delivered and consumed feed, making feed cost, usage, and loss computable. Remove → a nutrition calculator with no managed supply or execution; remove the supply side → a static ration calculator.

Load-bearing checks:
- 1 alone = composition database / commodity ledger
- 2 alone = ration calculator (nutrition math, below the Type)
- 3 alone = batch-weigh/mixing software
- 1+2 without 3 = thin formulation ancestor (formulation-only tools approach this boundary from below; WinFeed's mixing sheet is its minimal bridge into the Type)
- 2+3 without 1 = feeding board with no composition reality
- 1+3 without 2 = feed usage/inventory accounting without formulation

### L1 — Common Mature Structure

- Least-cost / constrained optimization formulation (linear programming; vendor-specific stochastic variants), with shadow-price / marginal-cost analysis
- Feeding schedules and per-group load plans; guided mixing on mobile clients connected to scales or mixer-wagon data
- Supply-side machinery: inventory (bins/silos/kitchens), purchases, shrink/loss (weighback) tracking
- Feed economics: cost per ton / per animal / per day, what-if scenario simulation against market prices
- Integration spine: herd/farm management (animal counts), weighing and mixing hardware, feeding automation, lab/NIR sample data updating ingredient matrices, ERP/MES/LIMS on the mill pole
- Livestock performance feedback (milk yield, growth) feeding back into rations — "precision feeding"
- Requirement/constraint machinery: nutrient requirement targets, inclusion limits, legal/compliance framing

### L2 — Variant / Optional Structure

- Segment poles: on-farm livestock operation (dairy, feedlot, swine, poultry) vs feed industry (mills, premix, aquafeed, pet food producers) — the same core realized at different points of the supply chain
- Execution substrate: manual + scale + app; mixer-wagon telemetry; fully robotic feeding with feed kitchens
- Regulatory posture: medicated feed labeling, national compendia updates (observed on the mill pole)
- Scale/deployment: single-farm desktop ↔ cloud multi-plant multi-team suites
- Species-specific nutrient models; grazing/pasture-oriented management (not evidenced in sample — uncertainty)
- Consultancy mode: external nutritionists managing rations across multiple client farms (implied by consultant framing; weak direct evidence)

### L3 — Vendor-specific (research notes only)

- FeedComp's Bluetooth-scale simple-setup packaging and PULSE platform integration; "FeedComp is great" placeholder article titles on the live page (site quality signal)
- BESTMIX: 9-week release cycle, €2–3M annual development investment, customer counts, "world's most advanced formulation system" claims, compendia update service details
- WinFeed: stochastic formulation as unique selling point; £100 pricing; demo limits (20 ingredients/nutrients)
- Lely: 98% loading accuracy claim, feed-kitchen block storage freshness claims, robot hardware details (magnets, slope limits)

## Vendor-specific Findings

- Stochastic (probability-based) formulation is currently a WinFeed differentiator; least-cost LP formulation is the common mature structure.
- Robotic feeding with a physical feed kitchen is a Lely-specific execution substrate; equivalent ration/group logic exists in other automation vendors (per sibling dairy research on robot ecosystems) but was not fetched.
- Compendia/label generation machinery is a mill-pole (BESTMIX) strength; no equivalent observed in on-farm products.

## Boundary Findings

- **vs Dairy Farm Management / Livestock Management**: the animal is the unit of record there (individual identity, lactation/reproduction/health events); feeding appears as a layer or event. Here the ration and the feed supply are the unit of record; animals appear as groups being fed. Test: remove ration-formulation and feed-supply management → it becomes herd management; remove the animal-individual identity and keep ration+supply+feeding loop → it stays Feed Management.
- **vs Aquaculture Management**: feeding there is an execution/recording activity inside the rearing loop; this Type owns formulation and feed supply as a discipline. Confirmed from both sides (aquaculture research pass states the same seam).
- **vs Farm Management Platform**: that Type is crop-centric (growing feed); this Type consumes feed into animals. Grain inventory as harvest/commodity = Farm/Grain territory; grain as fed ration component with nutrition = this Type.
- **vs Food Formulation Platform** (§20 sibling) and pet-food formulation: same recipe/nutrient-matrix machinery (BESTMIX literally serves both industries with one core). Distinction: feed rations are bound to living animal groups and a daily feeding/consumption loop with performance feedback; food/pet-food formulation targets saleable products. A formulation system with no animal-group ration attachment and no feeding loop is food-formulation territory even when the matrix math is identical.
- **vs feed-mill ERP**: BESTMIX's ERP Suite (contracts, logistics, warehousing) is the business layer around feed manufacturing; the formulation core (recipes, matrices, what-if) is this Type's territory where it stands alone.
- **Homonym (taxonomy note)**: "feed management" in e-commerce means product-data feed syndication to ad/exchange channels (see PIM research pass). Same words, unrelated domain; this leaf is the §20 livestock-feed discipline. No directory change needed — section context disambiguates, but the collision is worth remembering when reading external sources (searching this Type's name surfaces mostly commerce tools).
- **Rejected findings**: "feeding robotics" is not definitional (execution substrate varies: manual+scale → robot); "least-cost optimization" is not definitional (FeedComp enters rations; Lely manages them; only the mill/formulation pole optimizes) — it is common mature machinery, not the invariant; "compliance/labels" is mill-pole-specific, not Type-defining.

## Uncertainties

- TMR Tracker (the classic on-farm TMR deep-pole reference) could not be fetched; on-farm execution pole rests on FeedComp + Lely + sibling-pass citations. Assertions kept at cross-product strength, not single-product precision.
- Feedlot-specific feed management (beef yards: pen-riding, bunk reading, daily yard sheet) was not directly sampled; product memory suggests it follows the same ration+load+group core, but no source was fetched — no feedlot-specific claims are made in the final document.
- Grazing/pasture feeding management may form a variant with different supply semantics (no evidence either way).
- Whether pure formulation-only tools (no inventory, no execution recording) should count as the Type's lower bound or as a separate "Ration Formulation" Type is a genuine edge: WinFeed includes only a mixing sheet. The final document treats formulation-with-batch-output as the minimal form of the Type and flags the calculator-without-batch as below the Type.

## Final Synthesis

Feed Management is the livestock/feed-side system of record whose managed subject is the feed itself. Its world: feed items (ingredients and mixes) carrying nutrient composition and cost; rations as versioned recipes binding ingredient mixes to nutrient targets for defined recipients (animal groups, species/life stages, or feed products); and the quantified feed loop that turns rations into measured batches/loads, moves them through supply, and records what was actually delivered and consumed so that feed cost, usage and loss become computable. Around this core, mature products add least-cost optimization, feeding schedules, shrink/weighback tracking, feed-economics analysis, an integration spine (herd counts, scales/mixer wagons/robots, lab data, ERP), and performance feedback loops. The market realizes the Type at two poles of one supply chain — on-farm feeding execution and feed-industry formulation/manufacturing — with automation-embedded and minimal-desktop forms as variants. The animal is a group being fed here, not an individually-tracked subject (that is herd management's world); the recipient binding plus the feeding/consumption loop is what keeps food/pet-food formulation outside this Type.
