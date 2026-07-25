#!/usr/bin/env python3
"""envision-pdf — render markdown/HTML to a brand-locked PDF.

Subscribes to the `envision-brand` standard: applies the 2026 palette,
Helvetica Neue, the green-chevron logo, tabular numerals, and the no-em-dash
rule, then prints to PDF via headless Chrome (the validated pipeline).

Usage:
  render.py INPUT.md  -o OUT.pdf [--title "..."] [--meta "..."] [--footer "..."]
  render.py INPUT.html -o OUT.pdf            # body fragment -> wrapped in brand shell
  render.py INPUT.html -o OUT.pdf --raw      # already a full branded HTML doc -> render as-is

Flags:
  --title    cover doctitle (large headline on the dark cover band)
  --meta     cover docmeta line (e.g. "Envision Construction LLC . Confidential . Draft . 20 June 2026")
  --footer   footer HTML (e.g. 'Confidential. <a href="https://www.envsn.com">envsn.com</a>')
  --tagline  default "BUILD WITH INTELLIGENCE."
  --wordmark default "ENVISION"
  --raw      treat INPUT as a complete HTML document; only normalize dashes + render
"""
import argparse, base64, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
CSS_PATH = os.path.join(ASSETS, "brand.css")
LOGO_PATH = os.path.join(ASSETS, "envision_icon_green.png")


def logo_data_uri():
    with open(LOGO_PATH, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")


def md_to_html(md):
    try:
        import markdown  # python-markdown if present
        return markdown.markdown(md, extensions=["tables", "fenced_code", "attr_list", "sane_lists"])
    except Exception:
        pass
    if shutil.which("pandoc"):
        p = subprocess.run(["pandoc", "-f", "gfm", "-t", "html"], input=md.encode("utf-8"),
                           capture_output=True)
        if p.returncode == 0:
            return p.stdout.decode("utf-8")
    sys.exit("ERROR: need the python 'markdown' module or pandoc to convert markdown.")


def normalize_dashes(s):
    # The brand forbids em dashes; normalize em/en dashes to plain hyphens.
    s = s.replace("&mdash;", "-").replace("—", "-")
    s = s.replace("&ndash;", "-").replace("–", "-")
    return s.replace("  -  ", " - ")


def find_chrome():
    for p in ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
              "/Applications/Chromium.app/Contents/MacOS/Chromium"):
        if os.path.exists(p):
            return p
    w = shutil.which("google-chrome") or shutil.which("chromium")
    if w:
        return w
    sys.exit("ERROR: Google Chrome / Chromium not found for --print-to-pdf.")


def build_html(content, title, meta, footer, tagline, wordmark):
    css = open(CSS_PATH, encoding="utf-8").read()
    cover = ('<div class="cover"><div class="identity"><span>'
             f'<img src="{logo_data_uri()}" alt="Envision" '
             'style="height:26px;vertical-align:middle;margin-right:10px">'
             f'<span class="wordmark" style="vertical-align:middle">{wordmark}</span></span>'
             f'<span class="tagline">{tagline}</span></div>')
    if title:
        cover += f'<div class="doctitle">{title}</div>'
    if meta:
        cover += f'<div class="docmeta">{meta}</div>'
    cover += "</div>"
    foot = f'<div class="footer">{footer}</div>' if footer else ""
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f"<style>{css}</style></head><body>"
            f'<div class="page">{cover}<div class="body">{content}</div>{foot}</div>'
            "</body></html>")


def main():
    ap = argparse.ArgumentParser(description="Render to a brand-locked Envision PDF.")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--title", default="")
    ap.add_argument("--meta", default="")
    ap.add_argument("--footer", default="")
    ap.add_argument("--tagline", default="BUILD WITH INTELLIGENCE.")
    ap.add_argument("--wordmark", default="ENVISION")
    ap.add_argument("--raw", action="store_true")
    a = ap.parse_args()

    src = open(a.input, encoding="utf-8").read()
    if a.raw:
        html = src
    elif a.input.lower().endswith((".html", ".htm")):
        html = src if "<html" in src.lower() else build_html(src, a.title, a.meta, a.footer, a.tagline, a.wordmark)
    else:
        html = build_html(md_to_html(src), a.title, a.meta, a.footer, a.tagline, a.wordmark)

    html = normalize_dashes(html)
    out = os.path.abspath(a.output)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tf:
        tf.write(html)
        tmp = tf.name
    try:
        r = subprocess.run([find_chrome(), "--headless", "--disable-gpu", "--no-pdf-header-footer",
                            f"--print-to-pdf={out}", f"file://{tmp}"], capture_output=True, text=True)
    finally:
        os.unlink(tmp)
    if not os.path.exists(out):
        sys.exit(f"ERROR: render failed.\n{(r.stderr or '')[-600:]}")
    print(f"OK -> {out} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
