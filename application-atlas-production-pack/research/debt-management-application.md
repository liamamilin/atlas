# Research Notes — Debt Management Application

> Leaf: Debt Management Application (DIRECTORY §08 Finance, Banking, Insurance & Investment)
> Slug: debt-management-application
> Research date: 2026-09-08
> Prior context: the debt-collection-management pass left a FORWARD FLAG expecting this leaf to be consumer-side ("the individual managing/repaying their own debts — payoff-planner / debt-management-program territory, opposite side of the table"). This pass verifies that expectation.

---

## Research Goal

Understand what a "Debt Management Application" really is as an Application Type: what the system's world is made of, who uses it, how repayment work actually flows through it, and where its boundaries sit against budgeting/PFM tools (same user), collection/servicing systems (same subject matter, opposite seat), and one-shot calculators (same content, less structure).

## Initial Boundary (hypothesis at start)

- Hypothesis: person-side (first-party) application for tracking one's own debts and planning/managing their payoff. Adjacent traps:
  - Budgeting Application / Personal Finance Management (same user, different organizing object)
  - Net Worth Tracker (liabilities as snapshot balances, no payoff plan)
  - Debt Collection Management / Collections Platform (organizations pursuing debts owed by others — opposite seat; the forward flag)
  - Loan Management System / Mortgage Servicing Platform (lender/servicer-side records)
  - Debt *settlement* and debt *consolidation* services (adjacent services, different intent: reduce what is owed / replace debts with a new loan — not payoff management of existing debts)

## Research Questions

1. What is the unit of record — is each debt an individually structured record? What fields?
2. What is the plan, exactly? What does it order, what does it allocate, what does it project?
3. Is there an execution/tracking loop (recorded payments → updated balances → progress)? Or is plan generation the whole product?
4. How is repayment capacity represented (budget / total monthly payment)?
5. How do payoff strategies work and are they definitional or a parameter?
6. Are there program-mediated forms (credit counseling DMP) and do they satisfy the same core?
7. What are the exception behaviors (short payments, purchases on the debt, deferred payments, skipped months)?
8. Where exactly is the seam to budgeting apps and to organization-side debt systems?

## Representative Products (sample + rationale)

| Product | Shape | Why sampled |
|---|---|---|
| Undebt.it | web pure-play debt payoff planner + tracker, manual entry, freemium | market archetype of the self-directed Type; unusually complete official docs (how-it-works tour + FAQ knowledge base) |
| PowerPay (Utah State University Extension) | free web debt-elimination tool, account-based, non-commercial | long-lived (user review references 2008), academic/extension pole, non-profit distribution channel |
| GreenPath Debt Management Program (DMP) | nonprofit credit counseling program with client portal | the program-mediated pole — "debt management" in the consumer-credit-industry sense; consumer interacts via counseling + secure portal |
| Vertex42 Debt Reduction Calculator | spreadsheet (Excel/Google Sheets) plan generator | the thin pole: plan + printable schedule without an ongoing record; useful boundary specimen |

Considered and dropped: Money Management International (403 twice — see Sources/limitations), Qoins and ChangEd (site empty / domain for sale — likely defunct), PocketGuard debt-payoff page (403), app-store listings (Play Store timeout ×2; App Store region-redirected). The mobile-app pole is therefore documented as a market shape but without direct Tier-1 evidence this pass.

## Sources

Fetched 2026-09-08:

- Undebt.it — home page, "How Undebt.it Works" tour, FAQ/Help Center index — https://undebt.it/ , https://undebt.it/how-undebt.it-works.php , https://undebt.it/faq.php (Tier 1, strong)
- PowerPay — landing + How-To — https://extension.usu.edu/powerpay/ , https://extension.usu.edu/powerpay/how-to.php (Tier 1, moderate: positioning + module list + scenario questions; detailed mechanics not fetched)
- GreenPath — Debt Management Program page (mechanics, FAQ, fees, portal reference) — https://www.greenpath.com/debt-management-plans/ (Tier 1/2, strong)
- Vertex42 — Debt Reduction Calculator page (tutorial, strategies, snowball mechanics) — https://www.vertex42.com/Calculators/debt-reduction-calculator.html (Tier 1, strong)

Unreachable / dropped (limitations):

- moneymanagement.org — 403 on two URLs; abandoned per network rule
- qoins.io — empty responses twice; changedapp.com — domain parked for sale (product presumed defunct); both dropped
- pocketguard.com/debt-payoff/ — 403
- play.google.com search — timeout ×2; apps.apple.com US listing — redirected to regional Today page
- Consequence: the mobile-app pole (round-up/automation apps, mobile payoff trackers) and PFM-embedded debt features have no directly-fetched evidence this pass. Claims about that pole are kept generic and marked unverified; no precise features asserted.

## Product A — Undebt.it (web pure-play payoff planner + tracker)

### Key observations (evidence layer A = directly observed)

- Self-definition: "Free Debt Payoff Planner & Tracker" — "See exactly when you'll be debt-free... Build a personalized snowball or avalanche plan, track every payment, and watch your payoff date move closer." Tagline of the tracking leg: "Track it, don't just plan it."
- Three-step onboarding: 1) add debts (balances, interest rates, minimum payments); 2) choose strategy (snowball or avalanche) + extra payment (budget); 3) track progress (payoff date, payments, plan updates).
- Debt account record: name/creditor, balance, interest rate, minimum payment, due date. "credit cards, loans, medical bills, anything with a balance and a payment." No limit on number of debts.
- Explicit no-bank-connection posture: "No bank login required"; "Undebt.it doesn't connect to your bank or credit card account, so personal information like account numbers and passwords are NOT collected." Manual entry model.
- Repayment capacity: the "budget" amount = "the total amount you can currently afford to pay each month (the minimum payments on all debts plus whatever extra you can afford)."
- Snowball amount is calculated, not directly set: "the difference between your total budget amount minus the sum of your minimum payments."
- Rollover semantics explicitly documented: all plans are "rollover" plans — "extra payments are rolled from one debt to the next and so on"; the concept "generically popularized by Dave Ramsey's Debt Snowball."
- Eight payoff orders: Debt Snowball (lowest balance first), Debt Avalanche/Stacking (highest rate first), Debt Hybrid (debt-to-interest ratio), Cash Flow Index, Highest Monthly Payment, Highest Credit Utilization, Highest Monthly Interest Paid, and two Custom-order modes. All free; switchable anytime; comparison page shows methods side by side on the user's own data.
- Dashboard as "the heart": when each debt will be paid off, interest totals, payment manager ("easily record your payments... keep you on track so you won't be late"), partial payments supported, amounts adjust.
- Debt Snowball Table: month-by-month plan — payment per debt per month, current month highlighted (paid/remaining), snowflakes shown, running balance, monthly interest; exportable to Excel.
- Payment recording updates balances and due dates automatically; multiple payments per month; full sortable/exportable payment & purchase history per account, kept "for the life of the account."
- Debt Snowflakes: extra/one-time payments (tax refund, bonus) added into the plan; "negative snowflake" allowed for months the user plans to short-pay. Snowflake allocation to a specific debt is configurable.
- Exceptions handled in FAQ: skip a month; pay less than scheduled; partial payments; deferred student loan (not due for months); promo (intro) interest rates; multiple interest rates on one account; exclude an account from the plan; bi-weekly payments as a workaround on a monthly model; purchases added to a debt account (balance grows again); mortgage tracking supported; "highest balance" vs "balance" distinction for progress display.
- Progress page: which debts are paid off, how far along active debts are, time to debt-free, monthly interest.
- Credit utilization page (per-account utilization + pie charts of rate/loan-type distribution) — credit-score-adjacent extra.
- Account scope: one set of accounts per registration; partner-sharing article exists.
- Commercial shape: free core (since 2012) + paid Undebt.it+ (bill tracker, payoff snapshots, Debt Blaster, what-if scenarios, YNAB integration, calendar sync, savings challenge, "Undebt.AI"). YNAB sync = boundary evidence (budgeting lives in a separate Type's product).
- No downloadable app yet (2026 refresh is mobile-web; dedicated apps announced for Q4 2026) — product-specific.
- Calculators usable without any account; share-link stores the plan in the link itself.

## Product B — PowerPay (USU Extension)

### Key observations (layer A, moderate depth)

- Self-definition: "tools to develop a personalized, self-directed debt elimination plan. Discover how quickly you can become debt free, and how much you can save in interest costs by following your debt reduction plan." "Debt management tool without any cost to consumers worldwide."
- Core module: "PowerPay — How soon can I be out of debt? Eliminate debt faster by making power payments." (PowerPay's own name for the rollover/extra-payment concept.)
- Surrounding modules: Spending Plan (spending vs expert recommendations), PowerSave (savings projections), Calculators, Education Center (articles/fact sheets) — financial-education wrapper, non-commercial mission.
- Scenario questions advertised on the how-to page: tax refund toward elimination; extra monthly dollars; emergency fund as part of the plan; debt consolidation what-if; 0% intro-rate balance moves — what-if framing as first-class.
- Account-based (login/signup at powerpay.org); free; donor-supported.
- Longevity: user review references discovering the site in 2008 "for maintaining it for so long" — long-lived tool (historical depth for the Type).

## Product C — GreenPath Debt Management Program (program-mediated pole)

### Key observations (layer A)

- The industry meaning of "debt management": a Debt Management Program/Plan (DMP) run by a nonprofit credit counseling agency. "consolidates your credit card debt and other unsecured debts into one easy monthly payment. Each payday, you deposit funds into your secure GreenPath account, and we pay your creditors on your behalf."
- Consumer path: free debt counseling session first (certified counselor reviews debts/income/expenses) → enrollment → agency proposes concessions to creditors ("In most cases, we can work with your creditors to reduce your interest rate. Actual interest rates will vary by client and creditor.") → one monthly deposit → agency disburses to creditors.
- Program mechanics: "Collection calls stop once creditors agree to the plan." Timeline: "most complete the program in 3 to 5 years." Eligibility: unsecured debt — credit cards, department store cards, medical bills, personal loans.
- Consumer-facing software surface: "24/7 online access to your account through our secure debt management portal" + Client Success Team ("tracking your DMP progress") + private online support community. Client portal linked as "My Portal."
- Fees are program facts, vendor-stated: one-time enrollment fee and monthly fee varying by state/amount (GreenPath cites averages; keep product-specific).
- Explicit distinctions drawn by the vendor itself: DMP ≠ debt settlement ("designed to pay off the entire amount you owe in 3 to 5 years" vs forgiveness for a lump sum); DMP ≠ debt consolidation loan ("focuses on creating a manageable repayment strategy" vs a new single loan).
- Organization facts: nonprofit "since 1961"; NFCC member — the DMP form predates consumer software; supports the historical check.

## Product D — Vertex42 Debt Reduction Calculator (spreadsheet thin pole)

### Key observations (layer A)

- Spreadsheet for Excel/Google Sheets: enter creditor names, balances, interest rates, minimum payments + one total monthly payment → summary of when each debt pays off under the chosen strategy; second worksheet = printable payment schedule "to keep track of your progress"; snowball growth chart (Excel versions).
- Snowball mechanics documented independently (cross-confirms Undebt.it): snowball = total monthly payment − total minimums; "After you pay off your first debt, you no longer need to make the minimum payment on that debt. So, that payment amount gets rolled into your snowball"; when the snowball exceeds the target's remaining balance it splits to the next debt.
- Strategies: Debt Snowball (lowest balance first), Debt Avalanche (highest interest first), No Snowball (anti-strategy, minimums only), User-Specified/Custom order, Debt Snowflaking (extra payments column).
- Caveat documented: fixed minimum payment assumption — credit-card minimums fall as balances fall, so "you may want to update the calculator every few months."
- Companion template family: "Debt Payoff Charts and Trackers" (visual progress tracking templates) — the tracking leg exists in the spreadsheet world as separate manual artifacts.
- Professional variant: Pro/commercial license marketed to financial advisors "to help advise clients" — a professional use of the same structure.
- References PowerPay and Dave Ramsey as the ecosystem's shared vocabulary.

## Cross-product Comparison

| Structure | Undebt.it | PowerPay | GreenPath DMP | Vertex42 | Evidence |
|---|---|---|---|---|---|
| Individual debt records (balance, rate, minimum) | yes (manual entry) | yes (implied by tool purpose + calculators) | yes (held by agency; consumer sees plan) | yes (worksheet rows) | A×4 |
| Repayment capacity as a single stated amount | "budget" = minimums + extra | plan input (advertised via extra-dollar scenarios) | one monthly deposit amount | "total monthly payment" | A×4 |
| Ordering/allocation plan (strategy or fixed) | 8 named orders + custom | "power payments" | agency-structured disbursement plan | named strategies + custom order | A×4 |
| Payoff schedule / month-by-month projection | Debt Snowball Table | projected debt-free date & interest savings | 3–5 year program timeline (vendor-stated) | payment schedule | A×4 |
| Recorded payments / deposits updating state | payment manager + history, balances/due dates update | not directly observed this pass | deposits recorded via portal (portal depth not observed) | no — print-to-track only | A×2, thin ×1 |
| Progress views (paid off, remaining, date) | progress page + snapshots | "see my debt reduction visually" (user review) | DMP progress tracking via portal | payoff summary + charts | A×3 |
| Rollover of freed minimums into next target | explicit | "power payments" | implicit in agency disbursement | explicit | A×3 |
| Extra/one-off payments as first-class | Debt Snowflakes (incl. negative) | tax-refund scenario | not applicable (fixed program payment) | snowflaking column | A×3 |
| Strategy choice as user-facing parameter | yes, switchable, comparable | yes (what-ifs) | no — agency-structured (variant) | yes | A×3 |
| Concession negotiation with creditors | no | no | yes (definitional to the DMP form) | no | A×1 — variant |
| Bank/account sync | explicitly none | not observed | n/a (agency deposits) | n/a | A×1 — variant posture |
| Credit-score/utilization features | utilization page | no | credit-score effects discussed in FAQ | credit repair edition (sibling template) | A×2 — optional |

Reading: the three jointly-held structures are present in every sampled product, including the program-mediated and spreadsheet poles. Named strategy vocabularies (snowball/avalanche/…) are market-common but parameter-level, not definitional — the DMP form satisfies the plan leg without user-chosen ordering. The tracking leg separates the Type from calculators (Vertex42 is the demonstrably thin pole: plan + print, no ongoing record).

## Abstraction Hierarchy

### L0 — Defining Invariant (deliberately small)

A Debt Management Application exists for a person (first-party debtor) and holds exactly three jointly-needed structures:

1. **The person's own debts as liabilities of record** — persistent, individually addressable records per debt carrying who is owed, the current balance, and payoff-relevant terms (interest rate, minimum payment). Remove → expense/budget tracking or a net-worth snapshot (liabilities without payoff semantics).
2. **A repayment plan over those debts** — a defined order/schedule for retiring the debts within a stated repayment capacity, held as the organizing object the product works from. Remove → a debt inventory/balance list.
3. **Repayment tracked against the plan** — actual payments/deposits recorded, balances updated, progress surfaced (paid-off debts, remaining, projected completion), plan adjusted. Remove → a one-shot calculator.

Jointly-held is load-bearing: plan+tracking without the debts of record = a generic schedule tool; records+tracking without a plan = a balance tracker; records+plan without tracking = a calculator. The first-party seat (the user is the debtor) is the discriminator against organization-side debt Types.

Historical/market-sample check (§24): the core holds for pre-software practice — a household debt ledger with a written payoff order and a payment log satisfies all three legs with no app, cloud, or named strategy; the credit-counseling DMP (a formal structure since at least the 1960s per GreenPath's founding-era claim) satisfies it in program-mediated form; the spreadsheet era satisfies it thinly (plan leg strong, tracking leg manual). Named strategy vocabulary (snowball/avalanche), mobile apps, and automation are era-current realizations, not invariants.

### L1 — Common Mature Structure

- Strategy selection among named payoff orders (snowball, avalanche, hybrid/cash-flow variants, custom order) with side-by-side comparison on the user's own data (A×3 of 4 self-directed poles; parameter not core)
- Month-by-month payoff schedule/table with per-debt and per-month interest
- Payment recording with per-account payment history; balances and due dates updating from recorded payments
- Projected debt-free date and interest-savings figures
- Progress views and visualizations (paid-off list, % complete, charts)
- What-if scenarios (extra monthly amount, one-off windfall payments)
- Payment calendar / due-date awareness; reminders (observed as product features at varying depth)
- Support for many debt types (credit cards, loans, medical, student loans) and account exclusion from the plan

### L2 — Variant / Optional Structure

- Data-entry posture: manual entry (no bank connection) vs account sync — sampled products include an explicit no-sync privacy posture; sync posture unverified elsewhere this pass
- Program-mediated administration (credit counseling DMP): third party holds the plan, negotiates concessions, receives one consolidated deposit and disburses; consumer role becomes enroll + deposit + track via portal. Fees/concession variability are program facts
- Automation of payments (round-up/micro-payment mobile apps) — market shape known but not directly evidenced this pass; unverified
- PFM/budgeting-embedded debt-payoff features — boundary zone (see below)
- Bill/expense tracking add-ons, savings challenges
- Credit-score/utilization features
- Shared household/partner account
- Professional/advisor-facing use (advisor licenses; counselor-administered programs)
- AI assistance (era-current, product-specific instance observed)

### L3 — Vendor-specific (research notes only)

Undebt.it: Debt Snowflakes naming, negative snowflakes, Debt Blaster, 52-week savings challenge, Plan.it, Undebt.AI, payoff snapshot image packs, no-app-mobile-web posture with Q4 2026 app plans, one-account-set-per-registration rule. PowerPay: PowerSave, Spending Plan module, Money Master course, donor-supported free model. Vertex42: creditor-count limits by edition (10/20/40), stair-stepper strategy (credited to Carlotta Thompson), commercial advisor license. GreenPath: state-variable fee schedule with cited averages, 3–5 year completion claim, NFCC/HUD certifications, Client Success Team naming, support community.

## Vendor-specific Findings

See L3 above. None of these are promoted into the canonical model. The "8 payoff methods" figure is Undebt.it's menu, not a Type constant; fee figures and the 3–5 year claim are GreenPath's own program statements, cited as vendor-specific.

## Boundary Findings

- **vs Budgeting Application / Personal Finance Management**: same user, different organizing object. A budget allocates income across spending categories; a debt management application structures liabilities with payoff semantics (rate, minimum, payoff order, projected retirement) and makes the payoff plan the object the whole product hangs from. Undebt.it operationalizes the seam: no expense tracking in the core, no bank connection, and budgeting integration sold as a premium bridge to a separate YNAB product; the vendor even publishes on "how budgeting and debt management are related" as an adjacent-topic relationship. Embedded debt-payoff features inside budgeting products sit in the boundary zone (variant pole, not the Type's center).
- **vs Net Worth Tracker**: liabilities as one snapshot figure vs debts as individually managed payoff projects. Remove the plan+tracking legs and this Type collapses into a net-worth/liability view.
- **vs Debt Collection Management / Collections Platform** (forward-flag seam, verified): opposite sides of the table. Collection software is organization-side: the system's subject is *other people's* debts the organization is owed or pursues on behalf of creditor clients, with agency objects (client creditors, placements, commissions, compliance). A Debt Management Application is person-side: the user's own debts as the debtor. No agency objects appear anywhere in the sampled person-side products. Keep-both; the seam is anchored in the object model and seat, consistent with the collection pass's expectation.
- **vs Loan Management System / Mortgage Servicing Platform**: those are lender/servicer-side records of loans they own or service (contract, billing, escrow). Here the person is the borrower tracking debts owed to others.
- **vs Credit Management Platform**: seller-side trade credit extended to customers — commercial, organization-side, different object (customer credit accounts vs personal liabilities).
- **vs Debt settlement / consolidation services** (market services, not directory leaves): settlement negotiates reduced payoff for lump sums; consolidation replaces debts with a new loan. GreenPath's own FAQ documents both distinctions; a debt management application manages repayment of existing debts in full. Settlement-flavored apps would be a different Type's territory.
- **Thin-pole boundary (calculator)**: a plan generator with a printable schedule and no ongoing record (Vertex42, PowerPay-style calculators without accounts) sits at the Type's lower boundary — same content, one leg missing. Recognizably "a calculator", not "a debt management application".

## Taxonomy note

The leaf name "Debt Management Application" is ambiguous in the market: self-directed payoff planner/tracker (app-store/web naming) vs "debt management program/plan" (the credit-counseling DMP industry meaning). Research shows these are two realizations of one consumer-side core (self-directed vs program-mediated), so the leaf stands as one Type with a program-mediated variant. No directory change needed; recorded here for future passes.

## Uncertainties

1. Mobile-app pole (payoff tracker apps, round-up/automation apps like the ChangEd/Qoins class): no direct Tier-1 evidence this pass (sites defunct/parked, store listings unreachable). Shape recorded as market-known; any capability detail is unverified and was not promoted into the final document.
2. PFM-embedded debt features (budgeting apps with loan accounts/payoff planners): boundary-zone shape known from market; not directly evidenced this pass.
3. PowerPay's execution depth (whether it records ongoing payments beyond plan generation): landing/how-to pages observed; powerpay.org app pages not fetched. Kept at positioning-level claims only.
4. GreenPath client portal's exact surfaces (statements? payment schedule? counselor messaging): portal referenced and "tracking your DMP progress" claimed, but the portal itself was not entered. Kept generic.
5. Whether automated-payment products belong inside this Type or form their own adjacent Type — deferred; flagged for a future pass if that market segment re-emerges with reachable documentation.

## Final Synthesis

A Debt Management Application is the person-side system of record for getting out of debt. Its world is small and stable across four very different realizations (pure-play web app, university extension tool, counseling-agency program, spreadsheet): the user's own debts held as individual liability records; a repayment plan that orders and allocates a stated repayment capacity across those debts until each retires; and a tracking loop in which recorded payments move balances, surface progress, and adjust the plan. Freed minimums roll into the next target (the rollover engine every sampled implementation shares, whatever it calls it — snowball, power payments, agency disbursement). Strategy vocabularies, automation, concessions, bank sync, and score features are market layers around this core, not the core.
