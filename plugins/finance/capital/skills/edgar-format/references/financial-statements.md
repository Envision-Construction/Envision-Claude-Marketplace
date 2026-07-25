# Financial Statement Segment — Forensic Reference

This document is the single source of truth for how each financial statement segment is rendered. If the visual output disagrees with this doc, fix the renderer — not the doc.

The five recognized statement types and their canonical names:

| `statement_type` value     | Canonical EDGAR title                                |
|----------------------------|-------------------------------------------------------|
| `income_statement`         | CONSOLIDATED STATEMENTS OF OPERATIONS                |
| `comprehensive_income`     | CONSOLIDATED STATEMENTS OF COMPREHENSIVE INCOME      |
| `balance_sheet`            | CONSOLIDATED BALANCE SHEETS                          |
| `cash_flows`               | CONSOLIDATED STATEMENTS OF CASH FLOWS                |
| `stockholders_equity`      | CONSOLIDATED STATEMENTS OF STOCKHOLDERS' EQUITY      |

The word "CONSOLIDATED" is conventional but optional — Envision LLC mock filings can omit it (we don't have consolidated subsidiaries in a public-company sense). The renderer takes a `consolidated: bool` flag for this.

## Universal layout rules

Every statement segment follows the same outer template:

```
                                                                    [page top, margin 1"]

    [registrant name]                                                [centered, Times Bold 11pt]
    CONSOLIDATED STATEMENTS OF OPERATIONS                            [centered, Times Bold 10pt, ALL CAPS]
    (In thousands, except per share data)                            [centered, Times Italic 9pt]

                          Years Ended December 31,                   [right-aligned over period columns, Times 10pt]
                       2026          2025          2024              [right-aligned col headers, Times Bold 10pt]
                       ─────         ─────         ─────             [single underline above each col header]

    Revenue          $ 1,234,567   $ 1,100,000   $  950,000          [line item left, numbers right; $ floats only on TOP row]
    Cost of revenue     800,000       720,000       640,000          [no $ — only the topmost numeric row gets a floating $]
                       ─────         ─────         ─────             [single underline above subtotal]
    Gross profit        434,567       380,000       310,000          [subtotal row — same font weight as body]

    Operating expenses:                                              [section header, Times 10pt regular, NO bold, NO indent]
       Selling, general and administrative   120,000  100,000  85,000  [sub-line items indented one step (0.25")]
       Research and development               60,000   55,000  48,000
       Depreciation and amortization          22,000   20,000  18,000
                                              ─────    ─────   ─────
    Total operating expenses     202,000   175,000   151,000          [subtotal: single underline above]

    Income from operations        232,567   205,000   159,000

    Interest expense              (12,000)   (10,000)   (8,000)       [negatives in parens, NOT minus sign]
    Other income, net               2,500      1,500     1,000
                                  ─────      ─────     ─────
    Income before income taxes    223,067   196,500   152,000
    Income tax provision          (55,767)   (49,125)  (38,000)
                                  ─────      ─────     ─────
    Net income                  $ 145,789  $  127,440  $  98,500      [GRAND TOTAL: $ float + double underline below]
                                ════════   ════════    ════════       [double underline rendered as border-top + border-bottom]


    Earnings per common share:                                        [subsection header]
       Basic                    $    1.45  $    1.27   $   0.98       [per share numbers — 2 decimals, $ on top row]
       Diluted                  $    1.43  $    1.25   $   0.97

    Weighted-average common shares outstanding:
       Basic                       100,544    100,346     100,510      [share count: thousands, no $]
       Diluted                     101,943    101,952     101,547

                                                                     [page bottom: page number centered]
                                       F-3
```

Rendering invariants every renderer MUST satisfy:

1. **Title block** (3 lines) sits at the top with ~24pt space before the period header.
2. **Period header** (e.g., "Years Ended December 31,") is right-aligned over the numeric columns — NOT centered over the page.
3. **Column years** are right-aligned, with a single horizontal rule underneath.
4. **Line items** are left-aligned in the label column; **numbers** are right-aligned.
5. **Indentation**: top-level lines flush left, sub-lines indent 0.25" per level. EDGAR filings use up to 3 indent levels in practice.
6. **Dollar sign placement**: a `$` appears ONLY on (a) the topmost numeric data row of each column, and (b) every subtotal and grand total row. NEVER repeat `$` on every row. In HTML/PDF/DOCX, the `$` floats to the left edge of the column with whitespace between it and the digits (true classic EDGAR look — done in CSS). In xlsx, the `$` sits adjacent to the digits because Excel's floating-`$` asterisk-fill accounting format (`_($* #,##0_)`) is silently broken by Google Sheets on xlsx import; the renderer deliberately uses a dual-compatible format that loses the float but renders identically in Excel and Sheets. Background: `memory/global/reference_xlsx_google_sheets_format_compat.md`.
7. **Negative numbers**: rendered as `(1,234)` — opening paren, number, closing paren. The closing paren occupies the position of the rightmost character (same as a positive number's rightmost digit), so a column of negatives still aligns at the right edge.
8. **Subtotal rule**: a single horizontal rule appears ABOVE the subtotal row, spanning the full width of each numeric column (not extending into the label column).
9. **Grand total rule**: a double horizontal rule appears BELOW the grand total row, plus a single rule above (the row above is usually the subtotal line that fed into it).
10. **No bold in body**. The grand total is NOT bold. The only bold text in the segment is the title (line 2 of the title block) and the column year headers. EDGAR's visual emphasis is achieved through rules, not weight.
11. **No color**. Black on white only. No accent fills, no gray rows.
12. **Trailing "F-N" page number** is centered at the bottom — F-1 is balance sheet by convention, F-2 income statement, F-3 comprehensive income, F-4 stockholders' equity, F-5 cash flows. If we're rendering a single segment, label it F-1 unless the user specified.

## Statement-specific specs

### Income Statement (`income_statement`)

**Canonical line ordering** (omit lines that aren't in the source data — don't fabricate):

1. **Revenue / Net revenues / Net sales** — first numeric row, gets floating `$`
2. **Cost of revenue / Cost of sales / Cost of goods sold** — usually a single line; some filings break it into product/service
3. **Gross profit** — subtotal: `Revenue − Cost of revenue`, single rule above
4. **Operating expenses:** — section header (not a numeric row)
   - SG&A (or "Selling, general and administrative")
   - R&D ("Research and development")
   - D&A ("Depreciation and amortization") — sometimes split, often embedded in COGS/SG&A
   - Restructuring, impairment, gain/loss on sale — only if material
5. **Total operating expenses** — subtotal of the indented operating expense lines
6. **Income from operations** / **Operating income** — subtotal: `Gross profit − Total opex`
7. **Other income (expense), net** — items below the operating line:
   - Interest income (positive)
   - Interest expense (negative — in parens)
   - Other income/expense net
8. **Income before income taxes** — subtotal
9. **Income tax provision** — typically negative (in parens) on a profitable filing
10. **Net income** — GRAND TOTAL, floating `$`, double underline below
11. **(blank row)**
12. **Earnings per common share:** — section header
    - Basic (with `$`)
    - Diluted (with `$`)
13. **(blank row)**
14. **Weighted-average common shares outstanding:** — section header
    - Basic
    - Diluted

Units: `(In thousands, except per share data)` — almost universal. Some filings use `(In millions, except per share data)`. Detect from the magnitude of the numbers.

**Decimal precision rules:**
- Dollar amounts: 0 decimals (whole units of "thousands" or "millions")
- EPS: 2 decimals
- Share counts: 0 decimals (already in thousands)

### Balance Sheet (`balance_sheet`)

**Two-column layout** (current period and prior period) with as-of date headers:

```
                                 December 31,     December 31,
                                    2026             2025
                                 ─────────        ─────────
    ASSETS
    Current assets:
       Cash and cash equivalents          $  245,000    $  180,000
       Short-term investments                 50,000        45,000
       Accounts receivable, net              125,000       110,000
       Inventory                              80,000        72,000
       Prepaid expenses and other            18,000        15,000
                                          ─────────    ─────────
    Total current assets                    518,000       422,000

    Property and equipment, net             340,000       310,000
    Operating lease right-of-use assets      45,000        48,000
    Goodwill                                120,000       120,000
    Intangible assets, net                   60,000        72,000
    Other assets                             15,000        12,000
                                          ─────────    ─────────
    Total assets                         $ 1,098,000   $   984,000
                                         ═══════════   ═══════════

    LIABILITIES AND STOCKHOLDERS' EQUITY
    Current liabilities:
       Accounts payable                   $   95,000    $   88,000
       Accrued liabilities                    62,000        55,000
       Current portion of long-term debt      25,000        20,000
       Operating lease liabilities, current   12,000        11,000
                                          ─────────    ─────────
    Total current liabilities               194,000       174,000

    Long-term debt, net                     180,000       200,000
    Operating lease liabilities, noncurrent  35,000        38,000
    Deferred tax liabilities                 22,000        20,000
    Other long-term liabilities              15,000        14,000
                                          ─────────    ─────────
    Total liabilities                       446,000       446,000

    Commitments and contingencies (Note 8)
                                                                  [literal text, no numbers]
    Stockholders' equity:
       Common stock, $0.001 par value             100            99
       Additional paid-in capital            315,000       310,000
       Retained earnings                     337,000       228,000
       Accumulated OCI                          (100)         (99)
                                          ─────────    ─────────
    Total stockholders' equity              651,900       537,900
                                          ─────────    ─────────
    Total liabilities and stockholders'
        equity                           $ 1,098,000   $   984,000
                                         ═══════════   ═══════════
```

Statement-specific invariants:

- **Section banner rows**: `ASSETS` and `LIABILITIES AND STOCKHOLDERS' EQUITY` are ALL CAPS, left-aligned, regular weight (not bold). Single blank row above, no rule.
- **Subsection banners**: `Current assets:`, `Current liabilities:`, `Stockholders' equity:` are title case with trailing colon, NOT indented.
- **Indented data rows**: Items within a subsection indent 0.25".
- **Subtotals**: `Total current assets`, `Total assets`, `Total current liabilities`, `Total liabilities`, `Total stockholders' equity` — single rule above.
- **Grand totals**: `Total assets` and `Total liabilities and stockholders' equity` — double underline BELOW (in addition to single rule above). These two MUST be numerically equal (the balance sheet balances).
- **Commitments and contingencies** line: literal text with no numeric value — a textual placeholder row, no underline.
- **Per-share par value**: Common stock par value (e.g., `$0.001`) appears as a parenthetical description, not in the number column.
- **No `$` on intermediate sub-line rows** — only top-of-section and grand totals.

Units: `(In thousands, except share and per share data)`.

### Statement of Cash Flows (`cash_flows`)

**Three-section indirect-method layout:**

```
                                              Years Ended December 31,
                                              2026         2025         2024
                                            ─────        ─────        ─────
    Cash flows from operating activities:
       Net income                          $ 145,789    $  127,440   $   98,500
       Adjustments to reconcile net income to
         net cash provided by operating activities:
          Depreciation and amortization      22,000        20,000        18,000
          Stock-based compensation           18,000        16,000        14,000
          Deferred income taxes               3,000         2,500         2,000
          Other non-cash items                1,500         1,200         1,000
       Changes in operating assets and liabilities:
          Accounts receivable                (15,000)      (12,000)      (10,000)
          Inventory                           (8,000)       (6,000)       (5,000)
          Prepaid expenses                    (3,000)       (2,500)       (2,000)
          Accounts payable                     7,000         6,000         5,000
          Accrued liabilities                  7,000         5,000         4,000
                                            ─────        ─────        ─────
    Net cash provided by operating activities  178,289       157,640      125,500

    Cash flows from investing activities:
       Purchases of property and equipment   (50,000)      (42,000)      (38,000)
       Purchases of investments               (60,000)      (50,000)      (40,000)
       Maturities of investments               55,000        45,000        35,000
       Acquisitions, net of cash acquired           —       (15,000)            —
                                            ─────        ─────        ─────
    Net cash used in investing activities    (55,000)      (62,000)      (43,000)

    Cash flows from financing activities:
       Proceeds from issuance of long-term debt        —     100,000             —
       Repayments of long-term debt          (20,000)      (30,000)      (15,000)
       Proceeds from stock option exercises    2,000         1,500         1,200
       Repurchases of common stock           (40,000)      (30,000)            —
       Dividends paid                              —             —             —
                                            ─────        ─────        ─────
    Net cash provided by (used in) financing activities  (58,000)     41,500      (13,800)

                                            ─────        ─────        ─────
    Net increase in cash and cash equivalents  65,289      137,140       68,700
    Cash and cash equivalents, beginning       180,000       42,860      (25,840)  [period — last period's closing]
                                            ─────        ─────        ─────
    Cash and cash equivalents, end of period  $ 245,289   $  180,000    $  42,860
                                            ═════════    ══════════    ═════════

    Supplemental disclosures of cash flow information:
       Cash paid for interest               $  12,500    $   10,200    $   8,100
       Cash paid for income taxes           $  52,000    $   46,000    $   35,000
```

Statement-specific invariants:

- **Three section headers** in order: operating, investing, financing. Each formatted as `Cash flows from <X> activities:` — colon-terminated, left-aligned, regular weight, no bold.
- **Section subtotals**: `Net cash provided by operating activities`, `Net cash used in investing activities`, `Net cash provided by (used in) financing activities` — single rule above each. The "provided by" vs "used in" wording flips based on sign; "provided by (used in)" hedge phrasing is used when sign is mixed across periods.
- **Net change row**: `Net increase in cash and cash equivalents` or `Net decrease in cash and cash equivalents` — single rule above.
- **Beginning / ending balance**: two rows. Ending row gets the floating `$` and double underline below.
- **Supplemental disclosures**: separate block at the bottom. Each row gets a `$` (not floating — every row).
- **Zero values** rendered as an em dash `—`, NOT as `0`, `0.00`, or blank. This is a hard EDGAR convention.

Units: `(In thousands)`.

### Statement of Stockholders' Equity (`stockholders_equity`)

Multi-column matrix layout — one column per equity component plus a Total column:

```
                              Common      Additional      Retained    Accumulated     Total
                              Stock       Paid-in Capital Earnings    OCI             Equity
                            ────────    ──────────────   ─────────    ───────────    ─────────
    Balance, December 31, 2024   $  99    $  310,000     $  228,000   $   (99)       $  537,900
    Net income                       —             —        127,440         —           127,440
    Stock-based compensation         —        16,000              —         —            16,000
    Stock option exercises           1         1,500              —         —             1,501
    Repurchase of stock             (1)      (17,500)             —         —           (17,501)
                            ────────    ──────────────   ─────────    ───────────    ─────────
    Balance, December 31, 2025   $  99    $  310,000     $  355,440   $   (99)       $  665,340
    Net income                       —             —        145,789         —           145,789
    ...
    Balance, December 31, 2026   $ 100    $  315,000     $  337,000   $  (100)       $  651,900
                            ════════    ══════════════   ═════════    ═══════════    ═════════
```

Statement-specific invariants:

- **Column headers** wrap to two lines in narrow columns (common stock, APIC). Render with `text-align: right`, `vertical-align: bottom`, and `white-space: normal`.
- **"Balance" rows** are the visual anchors — single rule above, floating `$` on each numeric column, double underline below only for the FINAL balance row.
- **Activity rows** show changes; em dash for zero impact on a column.
- **Total column** to the right sums each row across all equity components.

### Statement of Comprehensive Income (`comprehensive_income`)

Short standalone statement that picks up at Net income:

```
                                       Years Ended December 31,
                                       2026          2025          2024
                                       ─────         ─────         ─────
    Net income                       $  145,789    $  127,440    $   98,500
    Other comprehensive income (loss), net of tax:
       Foreign currency translation         (50)          (30)          (20)
       Unrealized gains (losses) on
         available-for-sale securities       100            80            50
                                         ─────         ─────         ─────
    Total other comprehensive income (loss), net of tax  50          50            30
                                         ─────         ─────         ─────
    Comprehensive income            $   145,839    $  127,490    $   98,530
                                    ═══════════    ══════════    ═══════════
```

## Detection heuristics (for `extract.py`)

When scanning a source file (xlsx, csv, docx, etc.) to decide statement type, look for these signature row labels (case-insensitive substring match):

| Signature labels                                                              | → statement_type        |
|-------------------------------------------------------------------------------|--------------------------|
| `revenue`, `net sales`, `cost of revenue`, `gross profit`, `operating expenses`, `net income`, `earnings per share`, `EPS`, `diluted`, `weighted-average shares` | `income_statement`       |
| `total current assets`, `total assets`, `total liabilities`, `stockholders' equity`, `accumulated deficit`, `retained earnings`, `accounts receivable` | `balance_sheet`          |
| `cash flows from operating activities`, `net cash provided by`, `cash flows from investing activities`, `cash flows from financing activities`, `supplemental disclosures` | `cash_flows`             |
| `balance, december 31`, `balance, beginning of year`, `additional paid-in capital`, `treasury stock`, `accumulated other comprehensive` | `stockholders_equity`    |
| `other comprehensive income`, `foreign currency translation`, `comprehensive income`, `available-for-sale securities` | `comprehensive_income`   |

Scoring: count signature label hits per type. Highest score wins. If two types tie or both score 0, return `ambiguous` and ask the user.

If the file is multi-sheet xlsx, run detection per sheet. A workbook with sheets named "IS", "BS", "CFS" should produce three segment outputs (one per sheet), bundled into a single output workbook with three sheets matching the EDGAR title.
