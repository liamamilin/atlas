# CLI Accounting Tool

## Overview

A **CLI Accounting Tool** is a command-line double-entry bookkeeping application in which the ledger lives as plain-text files on disk and every interaction — recording transactions, querying balances, generating reports — happens through terminal commands. The user writes financial events in a human-readable text syntax; the tool parses, balances, and aggregates them on demand. There is no GUI, no cloud service, no database: the text file is the system of record, version-controllable with Git, diffable with any text tool, and portable across machines.

The defining core is deliberately small:

```text
Plain-text ledger file (the system of record)
└── Double-entry transaction entries (date, payee, accounts, amounts)
    └── Command-line query and report engine
```

Everything else commonly associated with CLI accounting — investment tracking, multi-currency support, budgeting, web interfaces, CSV/OFX import — is optional structure that makes the ledger practical for real-world use, not what makes the product a CLI accounting tool.

## Users & Context

The primary user is a **technically literate individual or small-business operator** who prefers text-based workflows over graphical interfaces: software developers, system administrators, data-minded professionals, and privacy-conscious users who want full control over their financial data without depending on a cloud service. This user typically values version control, scriptability, portability, and the ability to inspect and modify raw data directly.

Secondary users include household finance managers who track personal finances in a plain-text file synced via Git, freelancers and consultants who maintain their own books without accounting-software overhead, and power users migrating from spreadsheets who want double-entry structure without GUI complexity.

Typical context: the user edits a text file in their preferred editor, adds transaction lines in periodic batch-entry sessions, and runs commands to check balances or generate reports. The ledger file lives in the user's home directory or a synced folder; there is no server, no subscription, no account to create.

## Core Model

### The Defining Core

Three properties. Remove any one and the product is no longer recognizable as a CLI accounting tool:

- **Plain-text ledger file as system of record** — every financial event is stored as human-readable text in one or more files on disk. The file format is the product's native language: a specific syntax for dates, payees, accounts, amounts, and metadata. The file is the ledger; there is no separate database, no cloud backend, no proprietary binary format. Without this property the product is a GUI accounting application or a cloud bookkeeping service.

- **Double-entry bookkeeping mechanics** — every transaction touches at least two accounts with balanced debits and credits. The tool enforces this at parse time: unbalanced transactions produce errors, not silent corruption. The user may or may not think in debit/credit terms (some tools let them write " Expenses:Food $20 " and infer the contra-entry), but the engine maintains balanced books. Without this property the product is an expense tracker or a single-entry cashbook.

- **Command-line query and report engine** — all interaction with the ledger happens through terminal commands: running a command against a ledger file produces filtered, sorted, or aggregated output (balances, registers, reports) on stdout. There is no GUI window, no dashboard, no web interface. The user pipes output through standard UNIX tools (grep, sort, awk, less) for custom analysis. Without this property the product is a text editor plugin or a file format without an application.

### Standard Capabilities

These make the core practical; they are not what makes the product a CLI accounting tool:

- **Transaction syntax with metadata** — a readable, writable format for recording transactions: date, optional cleared/pending status, payee or description, and indented posting lines with account names and amounts. Metadata (tags, notes, links) attaches to transactions or postings via a consistent syntax. The format is designed for humans to type and read, not just for machines to parse.
- **Account hierarchy** — accounts are organized in a hierarchical namespace (Assets:Bank:Checking, Expenses:Food:Groceries). The hierarchy lets users drill down from broad categories to specific sub-accounts and controls how reports aggregate.
- **Period and filter queries** — commands accept date ranges, account filters, payee patterns, and tag filters to slice the ledger. The user can ask "what did I spend on food in August?" or "show me all transactions involving the credit card" without opening a file.
- **Report generation** — balance sheets, income/expense statements (profit and loss), and register views (transaction history) computed from the ledger on demand. Reports are plain-text output, not PDFs or dashboards; some tools support output formatting (HTML, CSV, JSON) as a secondary mode.
- **Multi-file ledgers** — the ledger can be split across multiple files (one per year, one per account type, one per business) and the tool aggregates them. This supports modular organization and version control without forcing everything into one monolithic file.
- **Reconciliation workflow** — tools provide commands to mark transactions as cleared or reconciled, and to compare ledger state against external statement data (often imported as a separate text file). Reconciliation is the user's mechanism for verifying the ledger matches reality.
- **Syntax checking and error reporting** — the tool parses the ledger file and reports structural errors (unbalanced transactions, duplicate dates, malformed amounts) before producing any output. This is the first line of defense for data integrity.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Ledger file format
Implementations:    Ledger syntax · hledger journal · Beancount format ·
                    plain-text files with custom parsers

Concept:            Query language
Implementations:    Ledger period expressions · hledger grep-like filters ·
                    Beancount Python-based queries

Concept:            Report output
Implementations:    plain-text stdout tables · HTML · CSV/JSON · XML/XBRL
```

A reader who has only seen one implementation should still recognize another as the same Type from the core model alone.

## How It Works

### Set up the ledger

```text
Choose a tool (ledger, hledger, beancount, or another)
→ create a plain-text journal file (e.g. journal.dat, ledger.journal, main.beancount)
→ define the chart of accounts by writing transactions that use them
  (accounts are declared implicitly through usage, or explicitly in a header)
→ optionally: set a default currency, commodity, or price database
→ start entering transactions
```

There is no setup wizard, no account-creation flow, no onboarding screen. The user creates a file and starts writing. The chart of accounts grows organically as transactions reference new accounts.

### The ongoing loop: record → query → reconcile

This is the defining workflow, repeated continuously:

```text
RECORD      open the journal file in a text editor
            → add a new transaction block:
              date payee/description
                Account:Subcategory    $amount
                Account:Other          -$amount
            → save the file

QUERY       run a command in the terminal:
            ledger -f journal.dat balance
            hledger -f journal.dat balance assets
            bean-check journal.dat && bean-report journal.dat balances
            → inspect the output (text table on stdout)
            → pipe through grep, awk, or less for custom views

RECONCILE   export or view bank statement (as text/CSV)
            → run a reconciliation command or diff the statement
              against the ledger's register
            → mark matching transactions as cleared (status flag)
            → investigate discrepancies: missing entries, wrong amounts,
              duplicates
```

The loop is fundamentally text-driven: edit a file, run a command, read the output. There is no mouse, no button, no form. The user's shell is the interface.

### Reporting period

```text
Month-end or year-end:
→ run period-specific queries:
    ledger -f journal.dat balance --begin 2026-01-01 --end 2026-01-31
    hledger -f journal.dat incomestatement -p 'this month'
→ review the income/expense statement and balance sheet
→ check that the ledger balances to zero (trial balance)
→ optionally: generate output in other formats (CSV for a spreadsheet,
  HTML for sharing, XBRL for tax filing)
```

### Capability tiers

**Defining core** — without these, not a CLI accounting tool:

- plain-text ledger file as system of record
- double-entry bookkeeping mechanics
- command-line query and report engine

**Standard capabilities** — present in most mature products:

- human-readable transaction syntax with metadata
- hierarchical account namespace
- period and filter queries
- balance sheet, income/expense, and register reports
- multi-file ledger support
- reconciliation workflow
- syntax checking and error reporting

**Optional / variant** — depends on product and community:

- price database and historical price queries (for investment tracking)
- multi-currency with automatic exchange-rate handling
- budgeting and balance assertions
- scheduled/recurring transaction generation
- web or TUI (terminal UI) front-ends that sit atop the same engine
- output in HTML, CSV, JSON, XML/XBRL formats
- Python/R/etc. library access to parsed ledger data
- integration with tax-filing tools

## Interfaces

The following surfaces are described conceptually; exact command names and syntax vary by product.

### Journal editor

Not a built-in editor — the user's own text editor (vim, emacs, VS Code, nano) is the transaction-entry surface. The journal file is a plain text file that any editor can open and modify.

- typical information: date, payee/description, indented posting lines with account names and amounts, optional metadata (tags, notes, status flags)
- primary actions: write a new transaction block, edit an existing one, insert a metadata line, split a transaction

### Command-line interface

The primary interaction surface for all queries and operations.

- typical information: command name, ledger file path, date range, account filter, query expressions, output format options
- primary actions: run balance queries, run register queries, run income/expense reports, parse and validate the journal, reconcile transactions, export data

### Query output

Text tables printed to stdout, showing balances, transaction histories, or financial statements. The output is designed for human reading and for piping through UNIX tools.

- typical information: account names with indented hierarchy, balances in the default commodity, date ranges, running totals, cleared/pending status
- primary actions: read, pipe to grep/sort/awk, redirect to a file, format as CSV/HTML/JSON

### Ledger file (the data)

The ledger file itself is both data store and configuration. It is the artifact the user manages, versions, and backs up.

- typical information: the complete financial record as human-readable text
- primary actions: version-control with Git, diff to see changes, merge branches, share via cloud storage

## Important Rules / Behaviors

### The text file is the only source of truth

There is no database to fall out of sync, no cloud state to conflict with local state. The ledger file contains everything; if the file is correct, the reports are correct. If the file is corrupted or incomplete, the reports reflect that honestly. This is both the type's greatest strength (transparency, auditability, portability) and its greatest risk (no undo beyond version control).

### Transactions must balance

A transaction whose debits do not equal its credits is rejected at parse time. The tool will not produce reports from an unbalanced ledger. This is the fundamental data-integrity mechanism: the user cannot accidentally record a one-sided entry.

### Accounts are implicit, not pre-configured

Unlike GUI accounting software that ships a default chart of accounts, CLI tools let accounts emerge through usage: the first time the user writes "Expenses:Food:Groceries" in a transaction, that account exists. Some tools support explicit account directives, but none require them.

### Metadata is embedded, not stored separately

Tags, notes, links, and status flags live inside the journal file alongside the transaction they describe. There is no separate metadata store. This keeps the file self-contained: anyone who has the file has the complete record.

### Version control is the native audit trail

Because the ledger is a plain text file, Git provides a complete, immutable history of every change: who edited what, when, and what the previous state was. This replaces the audit-trail machinery that GUI accounting software builds into its database.

### Reports are computed, not stored

Running a balance or report command recomputes the result from the raw ledger data every time. There are no pre-computed summaries to fall out of sync. If a transaction is edited, all subsequent reports reflect the change immediately. This is the opposite of a database-backed system where reports may be cached or materialized.

### Clearing and reconciliation are user-driven flags

The user marks transactions as cleared (or reconciled) by adding a status flag in the journal file (e.g., `*` for cleared, `!` for pending). The tool respects these flags in reports and reconciliation commands. There is no automatic bank-feed import or machine-learning categorization — the user is the sole operator.

## Variants

- **By language ecosystem** — Ledger (C++, mature), hledger (Haskell, actively maintained), Beancount (Python, validation-heavy), and various other implementations. Each has a distinct syntax and philosophy but shares the core model.
- **By primary use case** — personal/household finance, small-business bookkeeping, investment tracking with cost basis, multi-currency international finance.
- **By sophistication** — minimal tools that parse and balance without fancy queries, vs. full-featured tools with query languages, price databases, budgets, and reporting plugins.
- **By output format** — text-only stdout tools, tools that generate HTML/CSV/JSON, tools that produce XBRL for tax compliance.

A variant remains a variant as long as the core model — plain-text double-entry ledger files queried via command line — still applies. When the ledger moves to a database, the interface becomes a GUI or web app, or the user is replaced by an automated import pipeline, the product belongs to a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Accounting Software | closest sibling | GUI/cloud-first, database-backed, wraps the ledger with invoicing, bank feeds, tax, and multi-user workflows; a CLI tool has no GUI, no bank feeds, and no operational layer — the text file and the command are the entire product |
| Bookkeeping Application | adjacent | centers on the capture-classify-reconcile workflow with bank feeds and collaboration; a CLI tool centers on the ledger file and the query engine, with no automated import or professional collaboration surface |
| Personal Finance Management Application | different entity and interface | personal money picture across institutions with aggregation and budgeting; a CLI tool is ledger-file-centric with no bank aggregation, no account linking, and no consolidated overview beyond what queries produce |
| Spreadsheet | different model | a grid of addressable cells with formulas; a CLI tool has structured transactions in a defined syntax, double-entry enforcement, and a query engine — not free-form computation |
| Expense Tracking Application | weaker cousin | logs expenses without double-entry mechanics or a full ledger; a CLI tool maintains balanced books with assets, liabilities, income, and expenses |
| General Ledger System | enterprise relative | the same engine core (CoA + journal + trial balance) at enterprise scale with multi-entity consolidation; a CLI tool is single-ledger, single-user, file-based |
| Tax Preparation Application | downstream consumer | consumes financial data and produces tax filings; a CLI tool produces reports but does not prepare or file returns |

The most important boundary is with Accounting Software: the two share double-entry bookkeeping mechanics, but the GUI/cloud/database/operational layer is what makes accounting software a different product category. The second is with Bookkeeping Application, where the overlap is real for solo users, but the bank-feed and collaboration surfaces define the bookkeeping type.

## Representative Products

- **Ledger** — the original CLI double-entry tool (C++, started 2003, BSD license); the syntax that inspired the category. https://ledger-cli.org
- **hledger** — Haskell rewrite of Ledger with broader feature set and multiple output formats (text, CSV, HTML, JSON, SQL). https://hledger.org
- **Beancount** — Python-based, validation-first plain-text double-entry ledger; supports Fava as a web front-end. https://beancount.github.io
- **acc** — minimal plain-text accounting in Rust; single-binary CLI with a ledger-compatible subset. https://github.com/rudolfschmidt/acc
- **Fava** — read-only web front-end that renders Beancount ledgers (the ecosystem's standard visualization companion, still file-centric). https://beancount.github.io/fava/

## Sources

Research date: **2026-09-12**

- Ledger — official website: https://ledger-cli.org ; Features page: https://ledger-cli.org/features.html ; Documentation: https://ledger-cli.org/docs.html
- hledger — official website: https://hledger.org ; Start page: https://hledger.org/start.html
- Beancount — official website: https://beancount.github.io ; Documentation: https://beancount.github.io/doc/
- Plain text accounting community hub: https://plaintextaccounting.org (ecosystem tool listing used to verify products)
- acc — official repository: https://github.com/rudolfschmidt/acc
- Fava — official site: https://beancount.github.io/fava/
- The Plaintext Accounting movement — community hub: https://plaintextaccounting.org

> Sourcing limitation: The Ledger documentation site (ledger-cli.org) was reachable and provided core feature and syntax information. hledger and Beancount documentation was accessible via their official sites. Precise operational details (version numbers, performance benchmarks, exact command syntax) are intentionally kept at the conceptual level in this document; product-specific evidence is recorded in the paired Research Notes.
