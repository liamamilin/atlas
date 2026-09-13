# Net Worth Tracker

## Overview

A **Net Worth Tracker** is a person-side financial application that holds what an individual (or household) owns and owes as valued records, computes the single difference between total assets and total liabilities — net worth — and keeps that figure over time so wealth has both a level and a direction.

The defining core is deliberately small:

```text
Assets and liabilities held as valued records (the personal balance sheet)
└── Computed net worth figure (assets − liabilities, kept current)
    └── History accumulated as values are refreshed over time
```

Everything else commonly associated with the category — bank and brokerage connectivity, live market prices, automated property and vehicle valuations, budgets, goals, advisor sharing — is widely present in current products but is not what makes a product a net worth tracker. A paper household ledger with two columns struck and re-struck every year, or a spreadsheet updated monthly, is the same Application Type; a bank app that shows one institution's balances is not, and a budgeting app is a different Type that usually carries a net worth view inside it.

The organizing object is a **stock** (wealth at a point in time), not a **flow** (money moving through a period). That single distinction separates this Type from the personal-finance applications it is most often confused with.

## Users & Context

The primary user is an individual managing their own wealth — checking where they stand financially, watching the direction of their wealth over months and years, and seeing how individual assets and debts compose the whole. Households are a common unit: partners combine accounts into one shared picture.

Secondary participants vary by product and segment:

- **Partner/spouse** — joins the household's shared view; common in consumer products.
- **Advisor, accountant, or trusted family member** — granted read or scoped access in products that support sharing; typical for larger or more complex wealth.
- **Professionals serving the person** — some products provide a formal way for an advisor to work inside a client's picture.

Typical contexts of use: an occasional deliberate check-in (monthly, quarterly, after a major life event — a home purchase, a job change, a market swing) rather than a daily transactional session. The emotional register of the Type is longitudinal: "am I moving in the right direction", "what changed since last quarter", "what happens if this debt goes down". A daily-spending loop belongs to other Types.

## Core Model

### The Defining Core

**The personal balance sheet.** The unit of record is the person's own holding, on either side of the sheet:

- An **asset record** is something the person owns, carried at a money value: cash and bank balances, brokerage and retirement positions, crypto, real estate, vehicles, business interests, personal property — anything ownable.
- A **liability record** is something the person owes, carried at a money value: mortgages, car loans, student loans, credit card balances, other personal debts.

Records are individually identified and independently valued. Both sides are required: without liabilities the product is an investment or portfolio tracker; without the asset side it is a debt tracker. The records describe the person's own situation — the person is the subject and the audience.

**The computed net worth figure.** The application synthesizes the records into one headline number: total assets minus total liabilities. This computation is the product's reason for existing — a connected list of accounts without the synthesis is an account aggregator, not a net worth tracker. The figure is derivable at every level: per asset class, per side, per linked pair (a home minus its mortgage), and for the whole sheet. It can legitimately be negative; a person whose liabilities exceed their assets still has a meaningful net worth.

**Net worth over time.** Values are refreshed — automatically where possible, by hand where not — and the accumulated history turns the figure into a trend. Reading the *direction* of wealth is as central as reading its *level*: the same number last quarter versus this quarter is the product's most important comparison.

### Standard Capabilities of Mature Products

These are present in most current products and make the Type practical, without defining it:

- **Account connectivity** — linking banks, brokerages, credit cards, and loan accounts so balances and holdings arrive and refresh without manual entry.
- **Market-priced positions** — securities and crypto valued from live market prices, either through connected holdings or by entering a symbol and quantity.
- **Estimated valuations for non-traded assets** — property estimated from its address, vehicles from their identifying number, using regional pricing data. Where the data doesn't cover a region or asset, the record falls back to manual valuation.
- **Manual entry** — adding any asset or debt as a plain record when it cannot be connected; cost or a rough estimate is accepted as the starting value.
- **Composition breakdown** — the sheet grouped into classes (cash, investments, property, other assets; debts), so the headline number decomposes visibly.
- **History at two levels** — the net worth trend at the top, and per-record value history underneath (what the house was worth at each past update).
- **Drill-down** — from headline → class → account/asset → value history.

### One Structure, Many Implementations

```text
Concept:   A valued record on the person's balance sheet
Implementations:  connected account, ticker position, address-estimated
                  property, VIN-estimated vehicle, manual row

Concept:   Keeping values current
Implementations:  automatic account sync, live price feeds, automated
                  estimates, periodic manual updates (some products add
                  staleness reminders or refresh schedules for manual rows)

Concept:   Wealth history
Implementations:  automatic snapshots from synced values, saved history of
                  each manual update, editable past values
```

## How It Works

### Build the balance sheet

```text
Add asset and debt records
→ connectable ones: link the institution or enter a symbol/address
→ everything else: create a manual record with a value (cost or estimate acceptable)
→ organize into classes or sections
```

Onboarding is the construction of the sheet itself. There is no account-opening workflow with an institution and no plan to configure — the product starts empty and becomes useful as the person's holdings accumulate in it.

### Keep values current

```text
Connected records: refreshed from the data source
Traded positions: repriced from the market
Estimated assets (property, vehicles): repriced when fresh data is available
Manual records: updated by the person — periodically, on reflection,
                or when prompted by a staleness reminder where offered
```

This is the maintenance loop that distinguishes the Type from a one-time calculator. Some products make the manual-refresh obligation explicit — visually marking records whose value has gone stale, scheduling periodic reminders, or allowing the correction of a record's value as of a past date so the history stays honest.

### Read the picture

```text
Open the overview
→ headline net worth (and its change since last period)
→ composition: assets by class, liabilities by type
→ drill into a class → an account or asset → its value history
→ compare across time: month, year, since a life event
```

The reading loop is glance-and-drill: the headline answers "where do I stand", the composition answers "what is it made of", the history answers "where is it going".

### Maintain records across life events

```text
Buy a home → add the property; where the product supports pairing,
             link its loan so equity becomes visible
Sell an asset → mark it sold / close it out (its history remains)
Loan balance falls → the liability record shrinks, and any linked
                     equity view rises with it
New account opens → connect it; it joins the sheet
```

Records carry a light lifecycle — added, valued, refreshed, eventually sold or archived rather than silently deleted — because the history of what was owned and what it was worth is part of the product's value.

## Interfaces

Surfaces are described conceptually; layouts and names vary by product.

### Net worth overview (dashboard)

The primary entry surface.

- headline net worth figure and its change over the selected window
- composition of assets and liabilities (by class, by account)
- net worth trend chart over time
- primary actions: change the time window, drill into a class or account, add a record

### Balance sheet list (assets & liabilities)

The working surface where records live.

- rows or cards per asset and debt, grouped by class or section
- current value per record, with freshness indicators where offered
- primary actions: add, edit, archive, mark sold; in some products, link a liability to the asset it finances

### Record detail / value history

One holding's story.

- current value, source of valuation (connected, priced, estimated, manual)
- history of past values, editable in some products
- in products that support pairing: the financed asset alongside its loan, with derived equity

### Connectivity & records settings

- linked institutions and their status (connections do break; reconnection is a normal task)
- manual records and their refresh behavior

### Sharing / participants (where supported)

- who can see the sheet, and how much (household member, advisor, accountant)
- household aggregation: combining each partner's connected accounts into one picture

## Important Rules / Behaviors

### Valuation is heterogeneous by nature

Different records are valued by different mechanisms with different reliability: market prices for traded assets, regional data models for property and vehicles, human judgment for everything else. Consequences the user actually experiences:

- estimated values (property, vehicles) are approximations, often limited to the regions the pricing data covers; outside them, values are whatever the person enters
- manual values stay fixed until the person changes them — the sheet does not know an asset was sold or repriced unless told
- some products surface this explicitly with staleness markers or refresh reminders for manual records

### The headline is only as complete as the sheet

Net worth is computed from the records that exist. Omitted accounts, unentered property, or unlinked debts do not lower the number — they make it silently wrong. Products counter this with breadth (connect many institutions) and with explicit manual-entry paths for the rest.

### History is preserved, not overwritten

An updated value replaces the current figure, not the past. Per-record history and the top-level trend survive value changes, corrections of past values, and the sale or archiving of assets. Without this, "over time" — the Type's central comparison — would not exist.

### Connectivity is a normal failure mode

Aggregated connections break (credential changes, institution-side changes) and arrive stale. Handling broken and re-connected feeds is a routine part of using the Type, not an exception path.

### The person is the seat of action

The product observes and computes; it does not transact. Moving money, trading, or paying down a debt happens at the institution; the tracker reflects the consequence in the records and the headline. (Flow-adjacent machinery such as budgets or payment integrations appears in some products — see Variants and Related Types.)

## Variants

- **Net-worth-first wealth dashboards** — the balance sheet is the whole product: broadest asset coverage (private interests, crypto, collectibles), manual-valuation machinery, complex ownership, sharing with advisors; flow machinery deliberately absent.
- **Investment-led wealth dashboards** — free dashboards centered on connected investment accounts, with net worth as the headline "vital sign" and deeper investment analytics alongside; commonly paired with an advisory business upstream.
- **PFM-embedded net worth** — full personal-finance products (budgets, transactions, goals) that carry net worth as a first-class view; the balance sheet is one surface among several.
- **Mobile-first consumer trackers** — the same sheet optimized for glance reading on a phone, often with automated property estimates and simplified classes.
- **Spreadsheet / manual pole** — the thin historical form: self-maintained tables updated periodically; no connectivity, no market data, all three defining structures intact.
- **Complex-wealth form** — multi-entity structures (trusts, holding companies), per-owner shares, nested views, multi-currency; aimed at affluent households and family offices.
- **Advisor-shared form** — the sheet extended with professional participants under scoped access.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Personal Finance Management Application | organizes money movement (transactions, cash flow, budgets); carries a net worth view, but the balance sheet is not its organizing center |
| Budgeting Application | plans and allocates future spending flows; holds no whole-wealth balance sheet |
| Expense Tracking Application | records past spending flows; no assets/liabilities synthesis |
| Debt Management Application | holds the same liability records but organizes around repayment plans and payoff progress, not around the whole wealth figure |
| Portfolio Management System | investment holdings and performance with professional/managerial semantics (attribution, benchmarks); no non-financial assets or personal debts |
| Retail Trading Platform | executing trades is primary; balance sheet tracking is not the surface |
| Retirement Planning Application | projects a future financial state; the tracker holds the current state and its history |
| Crypto Wallet / DeFi Portfolio Application | custody and interaction with a specific asset class; appears inside a tracker only as priced positions |
| Wealth Management Platform / Financial Advisor Platform | advisor-side seat managing clients' wealth; the tracker is person-side |
| Estate Planning Application | structures the disposition of wealth; the tracker records what exists |
| Digital / Mobile Banking Application | one institution's own balance view for its customer; not a cross-institution personal sheet |

The boundary with Personal Finance Management is the load-bearing one. The practical test: remove the flow machinery (budgets, transactions, categories) from a mature PFM — if a valued record of everything owned and owed, a computed total, and its history remain and still make sense as a product, that residue is this Type. Conversely, a net-worth-first product with no flow machinery at all remains complete as this Type while failing as a PFM.

## Representative Products

- Kubera — net-worth-first personal balance sheet for complex, multi-asset wealth
- Empower (Personal Dashboard) — investment-led free wealth dashboard with net worth as a named tool
- Monarch Money — full PFM with net worth as a headline household view
- Copilot Money — mobile-first consumer PFM presenting net worth across accounts, investments, and property

## Sources

Research date: **2026-09-08**

- Kubera — homepage (https://www.kubera.com/); Help Center (https://help.kubera.com/), incl. "How do I add assets to Kubera?", "How do I link a mortgage to my home to see my equity?", "Mark as Stale…"
- Empower — Net Worth tool page (https://www.empower.com/tools/net-worth); homepage (https://www.empower.com/)
- Monarch Money — homepage (https://www.monarchmoney.com/); Help Center (https://help.monarch.com/hc/en-us), incl. "Using Reports"
- Copilot Money — homepage (https://copilot.money/); Help Center (https://help.copilot.money/), incl. "Dashboard Tab Overview"

> Sourcing limitations: Empower's operational help-center articles were not reachable from the research environment (product pages only); Copilot's net worth mechanics were evidenced mainly at product-page depth; app-store-only tracker products and the spreadsheet pole were not product-documented. Claims above are calibrated accordingly: precise numeric limits, default refresh intervals, and per-product valuation coverage are intentionally not asserted. Detailed observations and per-product evidence are recorded in the paired Research Notes.
