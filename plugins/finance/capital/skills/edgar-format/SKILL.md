---
name: EDGAR Format
description: Restyle ANY document (xlsx, docx, csv, md, txt, html, pdf, json) so it looks forensically like a modern SEC EDGAR 10-K / 10-Q filing — Times New Roman, justified body, ALL-CAPS bold ITEM markers, financial tables with floating dollar signs, parenthetical negatives, double-underline grand totals, and an EDGAR-style cover page. Output is emitted in the SAME format as the input (xlsx in → xlsx out, docx in → docx out) unless the user explicitly requests a different target. Use this skill aggressively whenever the user mentions "make it look like a 10-K", "EDGAR style", "SEC filing format", "10-Q styling", "make this forensically accurate", "format this like an annual report", "investor-ready format", or hands over any document and asks for it to be "styled" or "formatted" in a way that sounds regulatory or institutional. Default target audience is internal Envision / Prometheus Ventures mock filings, prospectus drafts, investor memos that need to live next to real filings without looking out of place.
---

# EDGAR Format

Restyle any source document so it is visually indistinguishable from a modern SEC EDGAR 10-K / 10-Q filing.

The skill answers ONE question: **"how do I make a document look like the SEC filings everyone reads on edgar.sec.gov?"** The answer is fiddly — fonts, weights, spacing, table conventions, cover page anatomy — and the forensic accuracy lives in the helper scripts and reference docs, not in your head. Run the scripts; read the references when you need to make a judgement call.

## When to invoke this skill

The trigger phrases in the frontmatter are deliberately broad — when the user wants a document to look regulatory, institutional, or "like a real SEC filing", use this skill. Common cases:

- The user hands over an xlsx with a budget and says "make this look like a 10-K"
- A docx investor memo needs to look like an annual report for a data room
- A markdown draft needs to be styled and exported to PDF that resembles an EDGAR filing
- The user shares a CSV and wants a styled output in any format
- A mock prospectus, mock S-1, or internal disclosure draft needs the right visual conventions

Do NOT use this skill for: filing real SEC documents (this is for INTERNAL mock / template use only — never tell the user the output is EDGAR-filable; only the look is replicated), redesigning websites, generic financial PDFs, or anything where the user explicitly asks for a different visual style.

## Two render modes

The skill has TWO modes and you MUST pick the right one before extracting:

1. **Segment mode** (default for single-statement uploads) — input is a standalone financial statement (income statement, balance sheet, statement of cash flows, statement of stockholders' equity, statement of comprehensive income). Output is JUST that statement, formatted EXACTLY like the corresponding page of a real 10-K filing — no cover page, no item headings, no body narrative. This is what a CFO uploading "Q4 IS.xlsx" almost always wants.

2. **Full-filing mode** — input is a narrative document or a multi-statement package, and the user wants a full 10-K / 10-Q look with cover page, PART/ITEM structure, and embedded financial statements.

### How to decide which mode

Run `extract.py` first — it returns a `mode_hint`:

- `"segment:income_statement"` — the file has rows matching IS keywords (Revenue, Cost of revenue, Operating expenses, Net income, EPS) and is plausibly a single statement (one logical table, no narrative)
- `"segment:balance_sheet"` — Assets / Liabilities / Stockholders' Equity sections detected, two-date column header
- `"segment:cash_flows"` — three buckets detected (Operating / Investing / Financing activities)
- `"segment:stockholders_equity"` — column header includes Common Stock / APIC / Retained Earnings / Treasury
- `"segment:comprehensive_income"` — has "Other comprehensive income" lines
- `"full_filing"` — multiple sections detected OR narrative markdown / docx
- `"ambiguous"` — confirm with the user before proceeding

**Override rule:** if the user explicitly says "make a full 10-K" or "just the income statement", honor that and skip detection.

## Workflow

The skill is a four-step pipeline. Each step has a script. Do not skip steps.

```
input file ─▶ extract.py ─▶ render_<target>.py ─▶ output file
                  │             (segment mode OR full-filing mode)
                  └─▶ reads style spec from references/ and CSS from assets/
```

### Step 1 — Identify the input format and the target format

By default, **the target format matches the input format**. The user picked their input format for a reason (xlsx because it's tabular, docx because it's narrative). Preserve that unless the user explicitly says otherwise.

| Input extension          | Default target |
|--------------------------|----------------|
| `.xlsx` / `.xlsm`        | `.xlsx`        |
| `.csv` / `.tsv`          | `.xlsx`        |
| `.docx`                  | `.docx`        |
| `.md` / `.txt` / `.html` | `.html`        |
| `.pdf`                   | `.pdf`         |
| `.json`                  | ask the user — JSON has no canonical visual format |

The user can override by saying things like "but give me the PDF" or "as html please". When in doubt, ask.

### Step 2 — Extract structured content

Run `scripts/extract.py <input>`. It returns a JSON blob with this shape (don't reinvent it inline — always go through the script so the schema stays stable):

```json
{
  "title": "Detected or user-provided document title",
  "registrant": "Envision Construction LLC",
  "filing_type": "10-K",
  "period_end": "2026-05-20",
  "sections": [
    {"item": "1", "title": "BUSINESS", "body_md": "..."},
    {"item": "1A", "title": "RISK FACTORS", "body_md": "..."},
    {"item": "7", "title": "MANAGEMENT'S DISCUSSION...", "body_md": "..."}
  ],
  "tables": [
    {"id": "rev-by-segment", "caption": "Revenue by Segment", "units": "in thousands",
     "headers": ["Segment", "FY2026", "FY2025"], "rows": [["Construction", 425100, 388200], ...],
     "totals_row_idx": 4, "subtotals_row_idxs": []}
  ],
  "metadata": {"address": "...", "telephone": "...", "irs_ein": "...", "commission_file_number": "..."}
}
```

If extract.py cannot infer fields (e.g., a bare CSV has no registrant name), it leaves them null. Ask the user to fill in the gaps before rendering — a 10-K cover page with `[REGISTRANT NAME]` placeholders breaks the forensic illusion.

**Required cover-page fields** (without these, the output won't look right):
- registrant name (legal entity)
- filing type (10-K, 10-Q, 8-K, S-1)
- period end date (for 10-K / 10-Q) or filing date (for 8-K / S-1)
- state of incorporation
- IRS employer identification number (it's OK to use a plausible placeholder for mock filings, but ASK the user before fabricating)
- commission file number (same)
- address of principal executive offices
- registrant's telephone number

If the user is doing a quick internal mock and doesn't care, use Envision defaults from `assets/registrant-defaults.json` — but tell them you did so they can override.

### Step 3 — Render to the target format

Pick the right script:

| Target | Script |
|--------|--------|
| `.html` | `python3 scripts/render_html.py <extracted.json> <out.html>` |
| `.pdf`  | `python3 scripts/render_pdf.py <extracted.json> <out.pdf>` (renders HTML, then WeasyPrint) |
| `.docx` | `python3 scripts/render_docx.py <extracted.json> <out.docx>` |
| `.xlsx` | `python3 scripts/render_xlsx.py <extracted.json> <out.xlsx>` |

All renderers read the same forensic spec from `references/style-spec.md` and `references/table-conventions.md`. If you find yourself wanting to hand-tune output, change the spec — never patch the rendered file. The spec is the source of truth.

### Step 4 — Verify

Before reporting done, sanity-check the output:

- Open the file (or have the user open it) and confirm:
  - Cover page renders with all metadata fields populated (no `[PLACEHOLDER]` text)
  - Body font is Times New Roman (or system equivalent — `Liberation Serif`, `Tinos`)
  - Body text is **justified**, not left-aligned (EDGAR filings are virtually all justified)
  - Item headings are `ITEM 1.` ALL CAPS BOLD, not `Item 1` title case
  - Financial tables have:
    - Right-aligned numbers
    - $ symbol only on the TOP numeric cell of each $ column, not every cell
    - Negative numbers as `(1,234)` not `-1,234`
    - Grand total row has a double-underline (border-top + border-bottom)
- Print preview: page breaks should not split table rows or fall mid-paragraph awkwardly

If any of these fail, re-render — don't ship a half-styled output.

## Forensic accuracy — the non-negotiables

These are the visual fingerprints that distinguish a real EDGAR filing from a generic financial PDF. Get these right and the output will pass casual inspection. Get any one of them wrong and it will look "off" even if you can't articulate why.

| Element            | Spec |
|--------------------|------|
| Body font          | Times New Roman 10pt (fallback: Liberation Serif, Tinos, serif) |
| Heading font       | Times New Roman 12pt bold (Item titles 11pt bold ALL CAPS) |
| Cover page form    | "FORM 10-K" / "FORM 10-Q" — Arial Black or Times bold, ~24pt, centered |
| Page size          | US Letter (8.5" × 11") |
| Margins            | 1" top/bottom, 0.75" left/right |
| Line spacing       | Single, with 6pt space after each paragraph |
| Body alignment     | Justified |
| Paragraph indent   | None (block paragraphs — EDGAR filings do not first-line-indent) |
| Color              | Black only. No accent colors anywhere. |
| Hyperlinks         | Underlined, but rendered black (not blue) when printed |
| Numerics           | Right-aligned in tables, comma thousands separators, parens for negatives |
| Currency           | `$` on top numeric cell of each $ column + every subtotal/grand-total row. HTML/PDF/DOCX float `$` to the left edge of the cell via CSS; xlsx renders `$` adjacent to the digits (Excel's classic floating-$ asterisk-fill format is silently broken by Google Sheets — see `memory/global/reference_xlsx_google_sheets_format_compat.md`). |
| Subtotal rule      | `border-top: 1px solid black` |
| Grand total rule   | `border-top: 1px solid black; border-bottom: 3px double black` |
| Table units header | "(in thousands)" or "(in millions, except per share data)" italic, right-aligned, above table |
| Item heading       | `ITEM 1. BUSINESS` — ALL CAPS, bold, left-aligned, 12pt space after |
| Part heading       | `PART I`, `PART II`, ... — centered, ALL CAPS bold, 14pt |
| Page numbers       | Bottom center. Front matter: lowercase roman (i, ii, iii). Body: arabic (1, 2, 3). Financial statements: F-1, F-2, ... |
| Signatures         | "SIGNATURES" heading, then "Pursuant to the requirements..." boilerplate, then dated signature lines |

The full forensic spec — including which CSS rules, python-docx style objects, and openpyxl number formats produce each of these — lives in `references/style-spec.md`. Read it before making any per-format tweaks.

## Reference docs

Read these as needed (not all upfront):

- `references/style-spec.md` — every visual element, with the exact CSS / python-docx / openpyxl recipe that produces it
- `references/table-conventions.md` — financial table rules: floating $, subtotals, totals, parens for negatives, unit headers
- `references/cover-page.md` — 10-K/10-Q cover page anatomy, field-by-field

## Assets

- `assets/edgar.css` — master stylesheet, loaded by render_html.py and render_pdf.py
- `assets/cover-page.html.j2` — Jinja2 template for the EDGAR cover page (HTML/PDF path)
- `assets/safe-harbor.txt` — standard Forward-Looking Statements / safe harbor block
- `assets/registrant-defaults.json` — Envision Construction LLC defaults for mock filings

## Important guardrails

1. **NEVER claim the output is a real or filable SEC document.** The skill replicates the *look* for INTERNAL mock / template use. Always tell the user this when the output is delivered.
2. **DO NOT fabricate CIK numbers, registration numbers, or actual EDGAR accession numbers.** Use placeholder values for unknown fields, and tell the user. The skill is for drafting and visual styling, not for impersonating real filings. A `[MOCK FILING — INTERNAL USE ONLY]` cover-page stamp is available via `--watermark` on `render_html.py` / `render_pdf.py` and is OFF by default (client-ready output); turn it on when handing a draft to internal reviewers who shouldn't mistake it for the real thing.
3. **If the user asks the skill to produce something designed to mislead investors or regulators, refuse.** Mock filings for internal training, drafting, or stylistic consistency are fine. Anything that looks like fraud is not.

## Example invocations

**Example 1 — XLSX in, XLSX out:**
> User: "Take the FY26 budget xlsx and style it like a 10-K MD&A table."
>
> Run: `extract.py budget.xlsx` → confirm registrant + period end → `render_xlsx.py extracted.json fy26-mdna.xlsx`
>
> Output: an xlsx with Times New Roman 10pt, right-aligned numerics, floating dollar signs, parenthetical negatives, "(in thousands)" header, MD&A section banner row.

**Example 2 — MD draft, target PDF:**
> User: "Here's my risk factors draft in markdown — make a 10-K-style PDF."
>
> Run: `extract.py risks.md` → fill in registrant + filing type=10-K → `render_pdf.py extracted.json risks.pdf`
>
> Output: a PDF with EDGAR cover page, "ITEM 1A. RISK FACTORS" heading, justified Times body, page numbering.

**Example 3 — DOCX in, DOCX out for editing:**
> User: "Style this disclosure draft like an EDGAR filing but keep it as a docx so I can mark it up."
>
> Run: `extract.py disclosure.docx` → `render_docx.py extracted.json disclosure-styled.docx`
>
> Output: a docx with the same content but EDGAR fonts/spacing/headings.
