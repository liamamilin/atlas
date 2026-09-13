## Boundary Findings

### Pair: CLI Accounting Tool vs. Accounting Software

**Distinguishing test:** Remove the GUI, database, bank feeds, and invoicing layer. What remains — a plain-text ledger file and a command-line query engine — is a CLI Accounting Tool. What is removed — a graphical interface, a cloud database, automated bank-import workflows, invoicing, bill-pay, and multi-user collaboration — is what defines Accounting Software.

**Evidence grade:** A (structural). The accounting-software leaf (at `applications/accounting-software.md`) explicitly defines its core as "chart of accounts + balanced transaction posting + financial statements derived from the ledger," with an "operational layer" (invoicing, bank feeds, tax) that CLI tools lack. The CLI tool's core is identical at the ledger-engine level but replaces every operational and interface surface with text files and terminal commands. The distinction is one of interface paradigm (text-file vs. database+GUI), not of bookkeeping mechanics.

### Pair: CLI Accounting Tool vs. Bookkeeping Application

**Distinguishing test:** Remove the bank-feed integration, automatic categorization, reconciliation-surface UI, receipt capture, and professional-collaboration features. What remains — classified transaction records accumulating into persistent books queried via command line — is a CLI Accounting Tool. The bookkeeping application is defined by the capture→classify→reconcile workflow; a CLI tool has no automated capture or collaborative classification.

**Evidence grade:** A (structural). The bookkeeping-application leaf (at `applications/bookkeeping-application.md`) defines its core as "financial transaction records + chart of accounts + persistent accumulating books," with the capture-classify-reconcile loop as the defining workflow. A CLI accounting tool shares the underlying ledger structure but lacks the bank-feed and collaboration machinery. The overlap exists for solo users who manually enter transactions, but the workflow and interface surfaces diverge.

### Pair: CLI Accounting Tool vs. Personal Finance Management Application

**Distinguishing test:** Change the entity from a business to a person. Remove bank aggregation, budgeting, goal tracking, and investment dashboards. What remains — a person's money tracked in a text file with a command-line query engine — is a CLI accounting tool used for personal finance. A PFM application is defined by the consolidated personal financial overview across institutions; a CLI tool produces no consolidated overview beyond what the user explicitly queries.

**Evidence grade:** B (boundary zone). The PFM leaf (at `applications/personal-finance-management-application.md`) defines its core as "personal money accounts + transaction register + consolidated personal financial overview." Many CLI tools are used for personal finance, and some users build the equivalent of a PFM in their journal files. The distinction is that PFM's defining property is the consolidated multi-institution view (bank aggregation), which CLI tools do not provide. A CLI tool used for personal finances is a PFM-assembled-from-parts, not a PFM product.

### Pair: CLI Accounting Tool vs. Spreadsheet

**Distinguishing test:** Remove the free-form cell grid and formula engine. Replace with structured transaction syntax and double-entry enforcement. A spreadsheet is a general-purpose computation surface; a CLI accounting tool is a domain-specific ledger with a query engine. The spreadsheet can model a ledger, but it does not enforce double-entry, does not have a built-in query language for account hierarchies, and does not parse a transaction syntax.

**Evidence grade:** A (structural). The structured-table leaf (at `applications/structured-table-lightweight-database-application.md`) contrasts spreadsheets with structured data tools, noting that spreadsheets impose no schema. A CLI accounting tool imposes a transaction schema (date, payee, postings) and double-entry constraints — properties a spreadsheet lacks unless explicitly built with formulas. The distinction is structural, not just stylistic.

### Pair: CLI Accounting Tool vs. Expense Tracking Application

**Distinguishing test:** Add assets, liabilities, income accounts, and balanced double-entry posting. An expense tracker logs spending in categories without a full ledger; a CLI accounting tool maintains a complete set of books (all five account types, trial balance, balance sheet). The expense tracker is a subset; the CLI tool is the full accounting model.

**Evidence grade:** B (scope). The expense-tracking-application leaf (not directly read but referenced in the PFM leaf) is described as "transactions + categories focused on spending; lacks the full multi-account picture." A CLI accounting tool that tracks expenses only is a misuse of the tool; its core requires the full double-entry model.

## Uncertainties

1. **Multi-user / collaborative CLI accounting:** Some users maintain shared ledgers via Git (e.g., household finances, small-business books shared via a repository). Whether this constitutes a distinct variant or an edge case of the single-user model is unclear. The research base (Ledger, hledger, Beancount documentation) primarily describes single-user usage; collaborative patterns are community-documented but not product-defined. Evidence grade: C (anecdotal/community).

2. **Fava as a GUI front-end for Beancount:** Beancount ships with Fava, a web-based reporting UI. This blurs the "no GUI" boundary. The research base describes Fava as an optional viewer, not the primary interface — the ledger file and the command-line remain the system of record. Whether a tool with an optional web viewer still qualifies as "CLI" is a judgment call. Evidence grade: B (product-documented, boundary judgment).

3. **Tax-filing integration:** Some tools (particularly Beancount with plugins, and Ledger with custom scripts) produce XBRL output for tax compliance. Whether tax-filing integration is a standard capability or an optional extension varies by tool and is not fully resolved in the research base. Evidence grade: B (partially evidenced, varies by product).

4. **Commercial vs. open-source landscape:** Nearly all CLI accounting tools are open-source. The absence of commercial CLI accounting products in the research base may reflect the type's community-driven nature rather than a structural requirement. Whether a commercial CLI accounting tool could exist and be recognized as the same type is unknown. Evidence grade: C (absence of evidence).

5. **Beancount's validation-first philosophy vs. Ledger/hledger's more permissive approach:** Beancount enforces stricter validation (balanced transactions, account declarations, date ordering) than Ledger or hledger. Whether this represents a meaningful variant or just an implementation detail within the same type is unresolved. Evidence grade: B (product-documented difference, judgment call on significance).

6. **Ledger-cli.org reachability:** The main website was reachable and provided core information, but some linked pages (features, docs) rendered via JavaScript and could not be fully fetched. The research relied on the homepage content and community documentation (plaintextaccounting.org) for completeness. Evidence grade: B (partial fetch).
