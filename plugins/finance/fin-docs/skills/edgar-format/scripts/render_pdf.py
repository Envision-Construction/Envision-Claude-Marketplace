#!/usr/bin/env python3
"""
render_pdf.py — render extracted JSON to an EDGAR-styled PDF.

Pipeline: extracted JSON → HTML (via render_html.render) → PDF.

Prefers WeasyPrint (pure-Python, CSS-paged-media compliant). Falls back to
wkhtmltopdf if WeasyPrint isn't installed. If neither is available, prints a
clear install hint and exits non-zero — we do NOT silently produce a
broken-looking PDF.

The CSS @page rules in assets/edgar.css drive Letter paper, 1" margins, and
page numbering — render_pdf.py adds no inline styles.

Usage:
    python3 render_pdf.py <extracted.json> <output.pdf>
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import render_html  # type: ignore  # sibling module


def _try_weasyprint(html_str: str, out_path: Path) -> bool:
    try:
        from weasyprint import HTML  # type: ignore
    except ImportError:
        return False
    HTML(string=html_str, base_url=str(render_html.SKILL_ROOT)).write_pdf(out_path)
    return True


def _try_wkhtmltopdf(html_str: str, out_path: Path) -> bool:
    if not shutil.which("wkhtmltopdf"):
        return False
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(html_str)
        tmp_html = Path(fh.name)
    try:
        subprocess.run(
            [
                "wkhtmltopdf",
                "--page-size", "Letter",
                "--margin-top", "1in",
                "--margin-bottom", "1in",
                "--margin-left", "0.75in",
                "--margin-right", "0.75in",
                "--enable-local-file-access",
                str(tmp_html),
                str(out_path),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
    finally:
        tmp_html.unlink(missing_ok=True)
    return True


def render(extracted: dict, out_path: Path, watermark: bool = False) -> None:
    html_str = render_html.render(extracted, inline_css=True, watermark=watermark)

    if _try_weasyprint(html_str, out_path):
        return
    if _try_wkhtmltopdf(html_str, out_path):
        return
    raise SystemExit(
        "PDF rendering requires WeasyPrint or wkhtmltopdf.\n"
        "Install one of:\n"
        "  pip install weasyprint\n"
        "  brew install --cask wkhtmltopdf\n"
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("extracted", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--watermark", action="store_true",
                    help="stamp '[INTERNAL MOCK FILING — NOT A REAL OR FILABLE SEC DOCUMENT]' "
                         "on the cover page (default: off — clean output for client-ready use)")
    args = ap.parse_args(argv)
    data = json.loads(args.extracted.read_text(encoding="utf-8"))
    render(data, args.output, watermark=args.watermark)
    print(f"wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
