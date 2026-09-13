# Research Notes — Meal Planning Application

## Research Goal

Understand the Meal Planning Application as an Application Type: the objects inside it, the planning loop users run, how plans turn into provisioning, what role nutrition plays, and where the boundary sits against Food / Calorie Tracking, Nutrition Coaching, Family Organizer, recipe-centric products, Institutional Foodservice Management, and meal-kit commerce.

## Initial Boundary

Working hypothesis before research:

- Core purpose: decide ahead of time what to eat on future occasions (typically a week), organize dishes/recipes into that schedule, and turn the plan into shopping.
- Users: household cooks, busy families, individuals following a diet; possibly professionals building plans for clients.
- Nearest neighbors: Food / Calorie Tracking Application (future plan vs past log — the sharpest seam, flagged by the tracker pass as a joint-review candidate), Nutrition Coaching Platform (coach-mediated), Family Organizer (household hub with embedded meal loop), recipe applications (no directory leaf), grocery/shopping-list tools (no directory leaf), Institutional Foodservice Management (professional menu planning), Subscription Commerce (meal kits).
- Unknowns: whether shopping-list generation is definitional or only common; how strongly nutrition computation belongs; whether auto-generation is definitional or a pole; whether professional use is in-type.

## Research Questions

1. What is the object of record — the plan, the meal entry, or the recipe?
2. How is a plan structured (dates, meal-time slots, servings, week horizon)?
3. Where does the food content come from (web clipping, manual entry, curated library)?
4. How does the plan turn into provisioning (list derivation, aggregation, on-hand suppression)?
5. What role does nutrition play (targets, auto-generation, display)?
6. What plan-assembly modes exist (drag-and-drop, auto-generation, curated plans, templates/menus)?
7. What rules govern the plan↔list coupling (merging, serving-size propagation, date ranges)?
8. Who are the users (solo, household, professional) and what variants exist?
9. Where exactly is the seam vs Food / Calorie Tracking (joint-review discharge), Nutrition Coaching, Family Organizer, recipe products, institutional foodservice, meal kits?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Mealime | mobile-first, preference-driven auto-generation (consumer; weekly loop) | auto-planning pole; plan→shop→cook structure |
| Paprika Recipe Manager | recipe-library-centric desktop/mobile, one-time purchase | recipe-manager-anchored pole; full user guide available |
| Plan to Eat | calendar-first web planner, subscription | calendar pole; extensive Tier-1 help documentation |
| Eat This Much | nutrition-target-driven automatic planner | diet-target pole; professional tier |
| eMeals | (intended) editor-curated subscription plans | abandoned — fetch failed twice; see Sources |

Poles cover: auto vs manual assembly, recipe-centric vs calendar-centric, one-time purchase vs subscription, consumer vs professional posture.

## Sources

Fetched 2026-09-08 (WebFetch, official surfaces):

- Mealime — https://www.mealime.com/ (root; positioning, plan→shop→cook, personalization options, auto grocery list, cooking mode; page also states the product will shut down 2026-10-21)
- Paprika — https://www.paprikaapp.com/ (root; feature overview) and https://www.paprikaapp.com/help/mac/ (full macOS user guide; section structure, recipe fields, grocery mechanics, pantry, meal planner, menus)
- Plan to Eat — https://help.plantoeat.com/ (help index) and https://learn.plantoeat.com/help/meal-planner (planner article index), https://learn.plantoeat.com/help/shopping-list (shopping-list article index)
- Eat This Much — https://www.eatthismuch.com/ (root; automatic planner, targets, pantry, grocery lists, professionals tier, medical disclaimer)

Accessibility limitations:

- eMeals — root returned HTTP 403 twice-class failure pattern (403 on root, 404 on support subdomain); abandoned per the failure rule after 2 attempts. No claims about eMeals are based on fetched evidence; no memory-based substitution was made. The "editor-curated plan subscription" variant is therefore described only in hedged form in the final document and marked unverified here.
- Plan to Eat root returned 403; the help center (help.plantoeat.com → learn.plantoeat.com) was fully reachable and is the source used.
- Evidence layer for all four researched products: A (directly observed official documentation). No Tier-3 sources were needed.

## Product A — Mealime — Key observations

- Positioning: "Meal planning made easy"; the product homepage structures the entire app as a three-step loop: **1. Plan → 2. Shop → 3. Cook**. (A)
- Planning: "Plan your meals for the entire week in minutes. With over 200 personalization options" — plan personalization shown as Plan Type (Classic / Vegetarian), Allergies (Shellfish, Gluten-Free), Dislikes (No tofu, No olives), Servings (for 2 / for 4). (A)
- Shopping: "Automatic grocery list based on your weekly meal plan. All your ingredients auto-sorted into categories." "Grocery shop once per week with an organized, 'done for you' shopping list." (A)
- Cooking: recipe instructions with hands-free mode; recipes positioned around ~30-minute weeknight cooking. (A)
- Business lifecycle note: the homepage states Mealime will shut down on 2026-10-21 (market churn observation, not a Type property). (A)

## Product B — Paprika Recipe Manager — Key observations

- Self-description: "an app that helps you organize your recipes, make meal plans, and create grocery lists." (A)
- Six main sections (macOS guide): **Recipes**, **Browser** (web clipping), **Groceries**, **Pantry**, **Meals** (the planner), **Menus** (reusable multi-day menus). (A)
- Recipe fields: name, difficulty, servings, prep/cook/total time, rating, categories, source + source URL, description, notes, nutritional info, ingredients, directions, photos. Nutritional info is an optional text field, not computed. (A)
- Meal planner: daily / weekly / monthly views; adding a meal = choose Recipe / Note / Menu + date + meal type (Breakfast, Lunch, Dinner, Snack "etc." — meal types customizable with color and time); drag-and-drop from recipe sidebar; moving/copying meals. (A)
- Grocery list: "automatically attempt to consolidate similar items" (2 eggs + 3 eggs = 5 eggs, toggleable in settings); aisle sorting (milk→Dairy, spinach→Produce) with customizable aisles; multiple lists; custom items; mark-as-purchased checkoff; filter by purchased state or by recipe. (A)
- Pantry: quantity, purchase date, expiration date, in/out of stock; "Ingredients placed in your pantry will automatically be unchecked when you add recipes or meal plans to your grocery list"; Move to Pantry from grocery list. (A)
- Plan→list coupling: meal planner action "Add to Grocery List" over selected meals/week/month; scaled recipe ingredients preserve scaling in the list. (A)
- Menus: reusable collections of recipes/notes; multi-day menus (Day 1–7) fill the planner from a start day; menus can be added to the grocery list directly. (A)
- Assumed-on-hand example: "if you already have salt at home, you can uncheck it before adding the recipe to the grocery list." (A)
- Business model: one-time purchase per platform; optional cloud sync account. (A)
- Lifecycle detail (product-specific): deleted recipes go to Trash; meals/grocery items delete immediately. (A)

## Product C — Plan to Eat — Key observations

- Help center organizes the whole product into three top-level areas: **Recipe Book**, **Meal Planner**, **Shopping List** (mirroring the plan→shop loop). (A)
- Meal Planner (Website): "Online meal planning calendar for custom meal plans." Drag recipes "onto a specific date and mealtime"; ingredients and notes can be planned directly on the planner; leftovers can be planned; menus are "reusable collections of planned items"; template menus; bulk edit (copy/move/swap/delete); search planner; print weekly or monthly plan; share plan to calendar via iCalendar; track nutrition on the planner ("Nutrition facts from your recipes is easily tracked"); customize meal-time sections; custom date selection including past dates. (A)
- Serving-size propagation: "Update the serving size of recipes on your Planner to immediately update your Shopping List." (A)
- Shopping List (Website): "The shopping list automatically generates an organized list of ingredients based on the recipes and ingredients on your meal planner." Categories "act like the aisles of your grocery store"; ingredients auto-assigned to categories; merge rules ("Ingredients merge when their title and unit match"); manual merge; add/remove items; date range of the list ("To ensure you are seeing the correct list of items, check the date range of your list"); Staples list ("a static list of frequently purchased items that can be used as a kitchen inventory"); reset list; share/print; send to grocery delivery or pickup; bulk-shop configuration. (A)
- Recipe acquisition: clipper/import from the web, including Instagram, Facebook, Yummly; Recipe Book = "store recipes from your own collection and around the Web." (A)
- Freezer: batch-cook tracking (servings, number of meals, date frozen). (A)
- Professional posture: "Coaching and Business Use — Get information on using Plan to Eat with clients." (A)
- Nutrition is a tracking/display layer over the plan, not the organizing principle. (A)

## Product D — Eat This Much — Key observations

- Self-label: "The Automatic Meal Planner." (A)
- Positioning: "creates personalized meal plans based on your food preferences, budget, and schedule. Reach your diet and nutritional goals with our calorie calculator, weekly meal plans, grocery lists and more." (A)
- Plan inputs (on-site generator): preferred diet (Anything/Keto/Mediterranean/Paleo/Vegan/Vegetarian), calorie target, number of meals per day, macro minimums (carbs/fat/protein). (A)
- Pantry: "Add what you already own to the virtual pantry and our algorithms will use it up with priority" — food-waste framing. (A)
- Grocery list: "Review your meals for the week and the grocery list automatically updates. Then get it delivered with our Instacart or AmazonFresh integration." (A)
- Decision framing: "Make the important decisions ahead of time and on your own schedule. Then there's nothing to worry about when it's time to eat." — future-facing intent framing. (A)
- Professional tier: "Eat This Much Pro — For Health & Fitness Professionals. Powerful, fast meal planning to level up your business." (A)
- Compliance posture: "not a substitute for professional medical advice" disclaimer. (A)

## Cross-product Comparison

| Structure | Mealime | Paprika | Plan to Eat | Eat This Much | Strength |
|---|---|---|---|---|---|
| Forward meal plan bound to dates | ✓ week | ✓ day/week/month | ✓ dates + mealtimes | ✓ week | B (4/4) |
| Planned meals reference recipes/dishes | ✓ (their recipe library) | ✓ (user recipe collection) | ✓ (user recipe book + planned notes/ingredients) | ✓ (their recipe/food database) | B (4/4) |
| Shopping list derived from plan | ✓ automatic | ✓ planner→list action + per-recipe | ✓ automatic generation from planner | ✓ automatic update | B (4/4) |
| List organized by aisle/category | ✓ | ✓ (customizable aisles) | ✓ (categories as aisles) | (not observed on page) | B (3/4) |
| Ingredient aggregation/merging | ✓ (categories sorted) | ✓ (2+3=5 eggs, toggleable) | ✓ (title+unit match merge) | (not observed) | B (3/4) |
| On-hand suppression (pantry/staples) | (not observed) | ✓ pantry auto-uncheck | ✓ staples list | ✓ virtual pantry priority | B (3/4) |
| Servings scaling coupled to list | ✓ servings setting | ✓ scaling preserved | ✓ serving-size propagation | (implied by targets; not explicit) | B (3/4) |
| Meal-time slots (breakfast/lunch/dinner/snack) | ✓ | ✓ customizable types | ✓ customizable sections | ✓ meals-per-day count | B (4/4) |
| Week as dominant horizon | ✓ | ✓ (also month/day) | ✓ (also month) | ✓ | B (4/4), monthly exists |
| Recipe acquisition by web clipping | (curated library instead) | ✓ browser + clipboard | ✓ clippers (IG/FB/Yummly) | (curated/food DB instead) | B (2/4) — pole-dependent |
| Auto-generation of the plan | ✓ personalization-driven | — (manual assembly) | — (manual assembly) | ✓ target-driven | B (2/4) — pole, not invariant |
| Nutrition targets driving the plan | — | — | — | ✓ calorie/macro | A — single-product pole |
| Nutrition display/tracking on plan | (health framing only) | ✓ optional recipe field | ✓ planner nutrition tracking | ✓ (target context) | B — common optional |
| Reusable templates/menus | — | ✓ menus (multi-day) | ✓ menus/templates | (pattern reuse implied) | B (2/4) |
| Leftovers / freezer planning | — | — | ✓ leftovers + freezer | ✓ food-waste framing | B/A partial |
| Grocery delivery handoff | — | — | ✓ send to delivery/pickup | ✓ Instacart/AmazonFresh | B (2/4) optional |
| Export plan to calendar / print / share | — | ✓ calendar export, print, email | ✓ iCalendar, print, share | — | B (2/4) optional |
| Professional/clients posture | — | — | ✓ coaching/business use | ✓ Pro tier | B (2/4) optional tier |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The forward meal plan as the object of record** — meals assigned to future dates and eating occasions, held persistently and revisable. The plan — not the recipe library, not a log of what was eaten — is the center of the product. Remove → calendar or recipe library; the planning gone.
2. **Planned meals carry food substance** — each planned meal references a recipe or dish with ingredient content (the thing that will actually be cooked/eaten), not merely a calendar event label. Remove → generic calendar.
3. **The plan drives provisioning** — the application derives a consolidated shopping list from the planned meals (ingredients aggregated across them), making the plan executable in a store. Remove → a menu display; the operational loop gone (all four sampled products hold this leg; a menu-only planner falls below the Type — judgment recorded in Uncertainties).

Jointly-held is load-bearing:
- 1 alone (dates + meal labels, no food content) = calendar/to-do surface.
- 2 alone (recipe collection) = recipe manager.
- 3 alone (list tooling) = shopping-list app.
- 1+2 without 3 = menu board (below-Type per this pass's judgment).
- 1+3 without 2 = nothing to aggregate from (list of generic items).
- 2+3 without 1 = recipe→list tooling with no planning (recipe-manager territory).

### L1 — Common Mature Structure

- meal-time slots (breakfast/lunch/dinner/snack), typically customizable
- serving counts / serving scaling coupled to the shopping list
- shopping list organized by aisle/category; ingredient aggregation across meals
- on-hand suppression via pantry / staples list
- recipe acquisition: web clipping/import (planner-agnostic poles) or curated libraries (auto-planner poles)
- reusable menus / template plans
- print / share / export (calendar handoff, email)
- week as the dominant planning horizon (monthly and daily views common)
- nutrition as a display/tracking layer over recipes and plans

### L2 — Variant / Optional Structure

- auto-generation machinery: preference-driven (allergies/dislikes/plan-type profile) or target-driven (calories/macros/meals-per-day)
- pantry stock-tracking depth (quantities, expiration dates, in/out of stock)
- leftovers and freezer/batch-cook planning
- grocery delivery/pickup handoff (Instacart/AmazonFresh-class integrations, send-to-service)
- professional plan-building tier (plans built for clients)
- household sharing/sync across family members (only weakly evidenced in sample; see Uncertainties)
- business model: one-time purchase vs subscription vs freemium
- multi-week/monthly planning depth

### L3 — Vendor-specific (Research Notes only)

- Mealime: "200+ personalization options" claim; hands-free cooking mode; shutdown date 2026-10-21; 4.5M+ users claim.
- Paprika: six-section structure with built-in Browser; clipboard fallback clipping tools; .paprikarecipes format; import from legacy recipe formats (MasterCook, MacGourmet, MealMaster, Living Cookbook, YummySoup); grocery consolidation toggle; Trash semantics for recipes vs immediate delete for meals/groceries; per-platform purchase.
- Plan to Eat: Staples list; Freezer with date-frozen tracking; title+unit merge rule; date-range debugging articles; Mini Planner; iCalendar share; bulk-shop configuration.
- Eat This Much: on-site calorie/TDEE calculators; macro minimums UI; diet-style landing pages; partner API; medical disclaimer; press-review badges.

## Vendor-specific / Rejected Findings

- **Auto-generation is NOT definitional.** Two of four sampled products (Paprika, Plan to Eat) are manual-assembly planners with no auto-generation at all; the two auto-planners differ from each other (preference-driven vs target-driven). Anti-overfitting: "meal planners auto-generate" would be overfitting to the mobile-consumer pole.
- **Nutrition math is NOT definitional.** Paprika treats nutrition as an optional recipe text field; Plan to Eat tracks it as an optional planner layer; only Eat This Much makes targets the organizing input. The calorie-target machine belongs to the diet-target variant, and partially to the Food / Calorie Tracking seam.
- **Web clipping is NOT definitional** (absent where the vendor supplies the recipes).
- **One-time purchase / subscription / cloud sync** — business-model detail, not Type structure.
- **"Healthy eating" framing** (Mealime) — marketing posture, not structure.
- Historical/market-sample check (analog ancestor): the paper weekly menu-planner pad with an attached grocery list, plus a recipe box or clipped recipes, satisfies all three L0 legs — no cloud, mobile, AI, barcode, or delivery integration in the definition. 2000s desktop recipe organizers with calendar planners satisfy the legs. The definition names no era-specific mechanism. **Historical check passed.**

## Boundary Findings

| Neighbor | Relationship | Test / distinction |
|---|---|---|
| Food / Calorie Tracking Application | sharpest seam | plan of what to eat (future, prescriptive; recipe-granularity ingredients; plan is the object of record) vs log of what was eaten (past, descriptive; consumption entries resolved into nutrients; log is the object of record). Nutrition direction differs: planner nutrition is plan-level display (optional); tracker nutrition is per-consumed-entry and definitional there. Products blend on both sides (trackers embed plans/diet modes; planners show nutrition and ETM uses targets) → center-of-gravity seam, keep-both. Joint-review flag from the tracker pass DISCHARGED: this pass confirms the seam from the planner side; both passes dated 2026-09-08; no conflict evidence found. |
| Nutrition Coaching Platform | adjacent | coach as actor, client relationships, programming/adherence vs self-serve household planning. Professional plan-building tiers (ETM Pro, PTE coaching use) sit on this seam — the plan-building machinery is the same; the coaching relationship machinery is not. Flag for the coaching pass. |
| Family Organizer | adjacent overlap | household hub holds meal planning as one loop among calendar/lists/chores (family-organizer pass: "meal planning with recipe→shopping-list and meal→calendar loops" as standard capability, "meal-planning emphasis" as variant). Dedicated planner: the meal plan is the system of record; household coordination is not. Center-of-gravity. |
| Recipe applications (no directory leaf) | supporting-structure vs center | recipe discovery/library apps center on finding/storing recipes; meal planners reference recipes as plan inputs. Recipe-centric products that carry the full plan loop (Paprika) remain in-type. Taxonomy observation: no Recipe leaf exists in DIRECTORY.md, so recipe-manager-with-planner products are absorbed here. |
| Grocery / shopping-list tools (no directory leaf) | below-Type | list without plan+recipes = leg 3 alone. |
| Institutional Foodservice Management | different world | professional menu planning binds menus to census, production quantities, diet orders, money and compliance (per its pass); household meal planning binds dishes to home dates and a shopping trip. Same vocabulary ("menu planning"), different object economy. |
| Subscription Commerce (meal kits) | adjacent commerce | meal-kit services plan for the customer and deliver ingredients (transaction venue); meal planners give the user the deciding machinery and a list. Vendor-decided subscription vs user-owned plan. |
| Calendar Application | surface overlap | calendars hold meal-time events but carry no food semantics, no recipe substance, no list derivation. Plan export to calendar is a handoff, not the Type. |

## Uncertainties

1. **Leg-3 judgment**: the sample holds plan→list 4/4 and the analog ancestor couples them, but a deliberately thin menu-only planner was not sampled (none found in the reachable market); this pass treats menu-only as below-Type and notes the judgment for a future reviewer.
2. **Editor-curated subscription plans** (eMeals pole): source inaccessible; variant described only in hedged form; existence in the market is widely known but was NOT verified from official documentation this pass.
3. **Household/family sharing depth** (shared plan editing, member assignment): not observed in the fetched surfaces; kept out of the final document rather than asserted.
4. **Nutrition-computation depth in auto-planners** (per-recipe nutrition data sources): beyond the fetched pages; kept qualitative.
5. Mealime's shutdown (2026-10-21) means the sampled evidence will decay; the product remains a valid A-layer source for 2026-09-08.

## Final Synthesis

The Meal Planning Application is the household's forward-deciding food application. Its world holds three things together: a plan of meals on future days and occasions, food substance (recipes/dishes) beneath every planned meal, and a consolidated shopping list derived from that plan. Everything else — auto-generation, nutrition targets, pantry tracking, delivery handoff, professional tiers, business models — varies by product philosophy along a spectrum from "you assemble the plan from your recipes" (recipe-library and calendar poles) to "the system assembles the plan to hit your targets" (auto-generation and diet-target poles). The defining seam against food tracking is temporal and semantic: intent (plan) vs act (log); against coaching it is agency (self-serve vs coach-mediated); against the family organizer it is the center of record (the plan vs the household).
