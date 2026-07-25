#!/usr/bin/env python3
"""
render_html.py — render extracted JSON to an EDGAR-styled HTML document.

The HTML drives BOTH the .html output AND the .pdf output (via WeasyPrint in
render_pdf.py). All visual rules live in assets/edgar.css — this script does
no inline styling; it just emits semantic class names that the CSS targets.

Forensic invariants enforced here:
  - Statement title block (registrant / title / units note)
  - Period header right-aligned over numeric columns
  - Column year headers with bottom rule (class: edgar-col-year)
  - Row classes drive subtotal / grand_total / banner / section_header / spacer
  - Floating $ only on the FIRST data row and every subtotal/grand_total row
    (CSS handles the visual; renderer just sets .edgar-dollar)
  - Negative numbers rendered as (1,234) not -1,234
  - Em dash for None values

Usage:
    python3 render_html.py <extracted.json> <output.html>
"""
from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path
from typing import Any

SKILL_ROOT = Path(__file__).resolve().parent.parent
CSS_PATH = SKILL_ROOT / "assets" / "edgar.css"


# ---------------------------------------------------------------------------
# Number formatting — same conventions as render_xlsx.py
# ---------------------------------------------------------------------------

def _fmt_int(v: float) -> str:
    """Format whole-number values with thousands separator + parens for negative."""
    if v < 0:
        return f"({int(round(-v)):,})"
    return f"{int(round(v)):,}"


def _fmt_decimal(v: float) -> str:
    """Format with 2 decimals (per-share figures)."""
    if v < 0:
        return f"({-v:,.2f})"
    return f"{v:,.2f}"


def _is_eps_label(label: str) -> bool:
    l = label.lower()
    return "per share" in l or l.strip() in {"basic", "diluted"}


def _is_share_count_label(label: str) -> bool:
    l = label.lower()
    return "weighted-average" in l or "weighted average" in l or "shares outstanding" in l


# ---------------------------------------------------------------------------
# Segment renderer
# ---------------------------------------------------------------------------

def _render_segment(segment: dict[str, Any], metadata: dict[str, Any]) -> str:
    period_labels: list[str] = segment.get("period_labels", []) or []
    n_periods = max(len(period_labels), 1)
    rows = segment.get("rows", []) or []

    out: list[str] = []
    out.append('<section class="edgar-segment">')

    # Title block
    registrant = (metadata.get("registrant") or "").strip()
    if registrant:
        out.append(f'  <div class="edgar-registrant">{html.escape(registrant)}</div>')
    out.append(f'  <div class="edgar-title">{html.escape(segment.get("title", ""))}</div>')
    units = segment.get("units_note", "")
    if units:
        out.append(f'  <div class="edgar-units">{html.escape(units)}</div>')

    # Table
    out.append('  <table class="edgar-table">')

    # Period header
    period_header = segment.get("period_header", "")
    if period_header:
        out.append('    <tr class="edgar-period-row">')
        out.append('      <td class="edgar-label"></td>')
        out.append(
            f'      <td class="edgar-period-header" colspan="{n_periods}">{html.escape(period_header)}</td>'
        )
        out.append('    </tr>')

    # Year/date column headers
    out.append('    <tr class="edgar-col-header-row">')
    out.append('      <th class="edgar-label"></th>')
    for label in period_labels or [""]:
        out.append(f'      <th class="edgar-col-year">{html.escape(label)}</th>')
    out.append('    </tr>')

    # Body rows
    first_data_row_written = False
    current_section = ""
    for r in rows:
        label = r.get("label", "") or ""
        role = r.get("role", "data")
        indent = int(r.get("indent", 0) or 0)
        values = r.get("values", []) or []

        if role == "spacer":
            out.append(f'    <tr class="edgar-spacer"><td colspan="{n_periods + 1}">&nbsp;</td></tr>')
            continue

        row_class = {
            "data": "edgar-data",
            "subtotal": "edgar-subtotal",
            "grand_total": "edgar-grand-total",
            "section_header": "edgar-section-header",
            "banner": "edgar-banner",
            "text_only": "edgar-text-only",
        }.get(role, "edgar-data")

        display_label = label.upper() if role == "banner" else label

        # Track section context for EPS vs shares disambiguation
        if role == "section_header":
            current_section = label.lower()

        out.append(f'    <tr class="{row_class}">')
        out.append(
            f'      <td class="edgar-label edgar-indent-{min(3, indent)}">{html.escape(display_label)}</td>'
        )

        if role in {"banner", "section_header", "text_only"}:
            # No numeric cells — just a colspan blank for layout consistency
            out.append(f'      <td colspan="{n_periods}">&nbsp;</td>')
            out.append('    </tr>')
            continue

        # Decide formatter for this row
        section_is_shares = "shares outstanding" in current_section or "weighted-average" in current_section
        section_is_eps = "per share" in current_section or "earnings per" in current_section
        if section_is_shares or _is_share_count_label(label):
            fmt = _fmt_int
        elif section_is_eps or _is_eps_label(label):
            fmt = _fmt_decimal
        else:
            fmt = _fmt_int

        # Floating $ on first data row + every subtotal/grand_total row
        floats_dollar = role in {"subtotal", "grand_total"} or not first_data_row_written

        for i, v in enumerate(values):
            classes = ["edgar-num"]
            if floats_dollar and i == 0:
                # Per the spec the $ is anchored to the leftmost numeric column;
                # apply .edgar-dollar to every $-floating numeric cell so the
                # CSS ::before pseudo-element renders the symbol left-anchored.
                classes.append("edgar-dollar")
            elif floats_dollar:
                classes.append("edgar-dollar")
            cell_class = " ".join(classes)
            if v is None:
                content = "&mdash;"
            else:
                content = html.escape(fmt(float(v)))
            out.append(f'      <td class="{cell_class}">{content}</td>')
        out.append('    </tr>')

        if role == "data" and any(v is not None for v in values):
            first_data_row_written = True

    out.append('  </table>')
    out.append('</section>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Cover page (full-filing mode)
# ---------------------------------------------------------------------------

def _render_cover_page(metadata: dict[str, Any], watermark: bool = False) -> str:
    out: list[str] = []
    out.append('<section class="edgar-cover">')
    out.append('  <div class="edgar-cover-title-bar">United States<br/>Securities and Exchange Commission</div>')
    out.append('  <div class="edgar-cover-subtitle">Washington, D.C. 20549</div>')
    out.append(f'  <div class="edgar-form-type">FORM {html.escape((metadata.get("filing_type") or "10-K").upper())}</div>')
    registrant = metadata.get("registrant") or "[REGISTRANT NAME]"
    out.append(f'  <div class="edgar-registrant-name">{html.escape(registrant)}</div>')

    for field_label, key in [
        ("State of Incorporation:", "state_of_incorporation"),
        ("IRS Employer ID:", "irs_ein"),
        ("Commission File Number:", "commission_file_number"),
        ("Principal Executive Offices:", "address"),
        ("Registrant's Telephone Number:", "telephone"),
        ("Period of Report:", "period_end"),
    ]:
        val = metadata.get(key) or "[NOT PROVIDED]"
        out.append(
            f'  <div class="edgar-cover-field"><strong>{html.escape(field_label)}</strong> '
            f'{html.escape(str(val))}</div>'
        )

    if watermark:
        out.append(
            '  <div class="edgar-cover-field" style="margin-top:0.5in;font-style:italic;font-size:9pt;">'
            '[INTERNAL MOCK FILING — NOT A REAL OR FILABLE SEC DOCUMENT]'
            '</div>'
        )
    out.append('</section>')
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Document assembly
# ---------------------------------------------------------------------------

def render(extracted: dict[str, Any], inline_css: bool = True, watermark: bool = False) -> str:
    metadata = extracted.get("metadata") or {}
    segments = extracted.get("segments") or []
    mode_hint = extracted.get("mode_hint", "")

    head_parts: list[str] = ['<!doctype html>', '<html lang="en"><head>',
                             '<meta charset="utf-8">',
                             '<title>EDGAR-styled document</title>']
    if inline_css:
        css = CSS_PATH.read_text(encoding="utf-8")
        head_parts.append(f'<style>{css}</style>')
    else:
        head_parts.append(f'<link rel="stylesheet" href="{CSS_PATH}">')
    head_parts.append('</head><body>')

    body_parts: list[str] = []

    if mode_hint == "full_filing":
        body_parts.append(_render_cover_page(metadata, watermark=watermark))
        # In full-filing mode the renderer should also emit body sections —
        # for now we render any segments inline after the cover.
        for seg in segments:
            body_parts.append(_render_segment(seg, metadata))
    else:
        # Segment mode (or unknown) — render all detected segments back to back
        for seg in segments:
            body_parts.append(_render_segment(seg, metadata))

    return "\n".join(head_parts + body_parts + ['</body></html>'])


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("extracted", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--external-css", action="store_true",
                    help="link the CSS file instead of inlining it (default: inline)")
    ap.add_argument("--watermark", action="store_true",
                    help="stamp '[INTERNAL MOCK FILING — NOT A REAL OR FILABLE SEC DOCUMENT]' "
                         "on the cover page (default: off — clean output for client-ready use)")
    args = ap.parse_args(argv)

    data = json.loads(args.extracted.read_text(encoding="utf-8"))
    html_str = render(data, inline_css=not args.external_css, watermark=args.watermark)
    args.output.write_text(html_str, encoding="utf-8")
    print(f"wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
