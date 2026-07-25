---
name: Branded PDF
description: Render any markdown or HTML into a brand-locked Envision PDF (investor one-pagers, cover memos, lender packages, decks-as-PDF, HNI materials). Subscribes to the brand:standard 2026 standard - applies Helvetica Neue, the #007A53/#111111 palette, the green-chevron logo, tabular numerals, and the no-em-dash rule, then prints to PDF via headless Chrome. Use when asked to "make a branded PDF", "render the one-pager/memo", "Envision PDF", or to produce any Envision-facing PDF deliverable.
---

# Envision PDF (brand-locked renderer)

This skill is the **rendering layer** of the Envision brand. It takes content
(markdown or HTML) and produces a PDF that conforms to the 2026 standard, using
the same HTML -> headless-Chrome pipeline validated on the Erebor financing
package (one-pager + cover memo).

## Subscribes to `brand:standard`

The canonical brand standard lives in the **`brand:standard`** skill. This skill
does not redefine the brand; it applies it. **Before authoring copy**, invoke
`brand:standard` and follow it for voice, color, typography, logo, and the
tagline rules. If `assets/brand.css` here ever disagrees with `brand:standard`,
`brand:standard` wins - update the CSS to match.

What this renderer enforces automatically:
- **Type:** Helvetica Neue (Helvetica/Arial fallback), tight tracking on display.
- **Palette:** Black `#000`, Dark `#111111`, Grey `#929296`, Light Grey `#E6E6E6`, Green `#007A53`, Light Green `#CAE8E0`. Green is the only accent. No Signal Yellow on HNI/investor docs.
- **Logo:** green-chevron icon + ENVISION wordmark on the dark cover band, embedded as a base64 data URI (no external asset dependency).
- **Numerals:** tabular in every table.
- **No em dashes:** em/en dashes are normalized to plain hyphens at render time (Avi's investor-voice rule).

## Usage

```bash
python3 scripts/render.py INPUT -o OUTPUT.pdf [flags]
```

| Input | Behavior |
|---|---|
| `INPUT.md` | Converted to HTML and wrapped in the brand shell (cover + body + footer). |
| `INPUT.html` (body fragment) | Wrapped in the brand shell. |
| `INPUT.html` (full `<html>` doc) | Rendered as-is (only dash-normalized). |
| `--raw` | Force render-as-is for a complete branded HTML doc. |

Flags: `--title` (cover doctitle), `--meta` (cover metadata line, use ` . ` or
`&middot;` as separators), `--footer` (footer HTML), `--tagline` (default
`BUILD WITH INTELLIGENCE.`), `--wordmark` (default `ENVISION`).

### Examples

```bash
# Markdown memo -> branded PDF
python3 scripts/render.py memo.md -o ~/Downloads/Envision_Memo.pdf \
  --title "Erebor Facility - Summary" \
  --meta "Envision Technology Holdings, LLC &middot; Confidential &middot; Draft &middot; 20 June 2026" \
  --footer 'Confidential, for discussion with Erebor. &middot; <a href="https://www.envsn.com">envsn.com</a>'

# A hand-built, already-branded HTML one-pager -> PDF, untouched layout
python3 scripts/render.py onepager.html -o ~/Downloads/OnePager.pdf --raw
```

## Markdown conversion

Uses the python `markdown` module if installed (tables, fenced code, attr_list);
otherwise falls back to `pandoc -f gfm -t html`. One of the two must be present.

## When NOT to use this skill

- **SOV / schedule / structured form PDFs** -> use the pdfme template
  `sov_template_8x11_portrait.py` in the `brand:design-system` skill instead;
  it is purpose-built for 8.5x11 tabular schedules.
- **Brand-image / identity boards** -> `brandkit`.
- **Reading/extracting an existing PDF** -> `firecrawl-parse` (opposite direction).
- **Artifacts for another portfolio entity** (Loxsle, Enspire, Atlas, etc.) -
  each has its own identity; do not apply the Envision brand.

## Files

- `scripts/render.py` - the renderer (markdown/HTML -> branded PDF via Chrome).
- `assets/brand.css` - the brand CSS (rendering layer; mirror of `brand:standard` tokens).
- `assets/envision_icon_green.png` - the green-chevron logo, embedded at render time.

## Maintenance

When `brand:standard` changes (palette, type, logo, tagline), update
`assets/brand.css` and `assets/envision_icon_green.png` to match, then re-render a
known doc to confirm fidelity. The skill autosearch index is rebuilt on
SessionStart; after editing this SKILL.md, open a new session or run
`node ~/.claude/hooks/lib/skill-embed-cli.mjs --verbose` for an immediate refresh.
