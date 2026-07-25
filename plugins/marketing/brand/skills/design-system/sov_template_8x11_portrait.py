from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame,
    Table, TableStyle, Paragraph, Spacer, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
import os

# ── 2026 Brand Colors ──────────────────────────────────────────────────────────
GREEN       = colors.HexColor("#007A53")
LIGHT_GREEN = colors.HexColor("#CAE8E0")
BLACK       = colors.HexColor("#000000")
DARK_GREY   = colors.HexColor("#111111")
GREY        = colors.HexColor("#929296")
LIGHT_GREY  = colors.HexColor("#E6E6E6")
BG          = colors.HexColor("#F5F5F5")
WHITE       = colors.white

PAGE_W, PAGE_H = letter   # 8.5 x 11 portrait

MARGIN_L      = 0.55 * inch
MARGIN_R      = 0.55 * inch
MARGIN_TOP    = 0.50 * inch
MARGIN_BOT    = 0.45 * inch
HEADER_BAR_H  = 0.055 * inch
FOOTER_RULE_Y = MARGIN_BOT
FOOTER_TEXT_Y = MARGIN_BOT - 0.15 * inch

ICON_PATH     = "/mnt/skills/user/envision-brand/SKILL.md"   # placeholder check
# Use the icon from our previous work session if available
_icon_candidates = [
    "/tmp/envision_icon_green.png",
    "/mnt/skills/organization/envision-brand-2026/envision_icon_green.png",
]
ICON_PATH = next((p for p in _icon_candidates if os.path.exists(p)), None)

PROJECT      = "Higher Living: Athens, AL"
PROJECT_NUM  = "26-05050"
PAGE_NUM     = "22"
DATE_STR     = "May 5, 2026"
BID_TYPE     = "GMP — BAFO"

# ── Recreate icon if not found ─────────────────────────────────────────────────
if not ICON_PATH:
    from PIL import Image as PImg
    import numpy as np
    # Try to regenerate from brand guidelines
    try:
        from reportlab.lib.utils import ImageReader
        import subprocess
        result = subprocess.run(
            ['pdftoppm', '-jpeg', '-r', '600', '-f', '5', '-l', '5',
             '/mnt/user-data/uploads/2026_04_14_-_Envision_Brand_Guidelines.pdf',
             '/tmp/logo_regen'],
            capture_output=True
        )
        if result.returncode == 0:
            img = PImg.open('/tmp/logo_regen-05.jpg').convert('RGBA')
            w, h = img.size
            crop = img.crop((int(w*0.135), int(h*0.458), int(w*0.196), int(h*0.572)))
            data = np.array(crop, dtype=float)
            r, g, b = data[:,:,0], data[:,:,1], data[:,:,2]
            darkness = 255 - (r*0.299 + g*0.587 + b*0.114)
            alpha = np.clip(darkness*1.4, 0, 255)
            out = np.zeros((*data.shape[:2], 4), dtype=np.uint8)
            out[:,:,0] = 0; out[:,:,1] = 122; out[:,:,2] = 83; out[:,:,3] = alpha.astype(np.uint8)
            PImg.fromarray(out).save('/tmp/envision_icon_green.png')
            ICON_PATH = '/tmp/envision_icon_green.png'
    except Exception as e:
        print(f"Icon generation skipped: {e}")

# ── Page chrome ────────────────────────────────────────────────────────────────
def on_page(canv, doc):
    canv.saveState()
    w, h = PAGE_W, PAGE_H

    # Green bar — full width top
    canv.setFillColor(GREEN)
    canv.rect(0, h - HEADER_BAR_H, w, HEADER_BAR_H, fill=1, stroke=0)

    # Header: page label top-left
    label_y = h - MARGIN_TOP
    canv.setFont("Helvetica-Bold", 8.5)
    canv.setFillColor(BLACK)
    canv.drawString(MARGIN_L, label_y, PAGE_NUM)
    canv.setFont("Helvetica", 8.5)
    canv.drawString(MARGIN_L + 0.22*inch, label_y, "- SCHEDULE OF VALUES")

    # Header: logomark top-right
    if ICON_PATH and os.path.exists(ICON_PATH):
        icon_h = 0.26*inch
        icon_w = icon_h * (622/753)
        icon_x = w - MARGIN_R - icon_w
        icon_y = label_y - icon_h + 0.04*inch
        canv.drawImage(ICON_PATH, icon_x, icon_y,
                       width=icon_w, height=icon_h, mask="auto")

    # Footer rule
    canv.setStrokeColor(LIGHT_GREY)
    canv.setLineWidth(0.5)
    canv.line(MARGIN_L, FOOTER_RULE_Y, w - MARGIN_R, FOOTER_RULE_Y)

    # Footer text — four left-anchored items
    fy = FOOTER_TEXT_Y
    canv.setFont("Helvetica-Bold", 8.5)
    canv.setFillColor(BLACK)
    canv.drawString(MARGIN_L, fy, "ENVISION")

    canv.setFont("Helvetica", 8.5)
    canv.setFillColor(GREY)
    canv.drawString(MARGIN_L + 1.10*inch, fy, PROJECT)
    canv.drawString(MARGIN_L + 3.40*inch, fy, PROJECT_NUM)

    canv.setFont("Helvetica-Bold", 8.5)
    canv.setFillColor(GREEN)
    canv.drawRightString(w - MARGIN_R, fy, "ENVSN.COM")

    canv.restoreState()

# ── Styles ─────────────────────────────────────────────────────────────────────
def S(name, **kw):
    base = dict(fontName="Helvetica", fontSize=7.5, leading=9.5,
                textColor=BLACK, spaceAfter=0, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name, **base)

s_th0_l  = S("t0l", fontName="Helvetica-Bold",    fontSize=8.5, textColor=WHITE)
s_th0_r  = S("t0r", fontName="Helvetica-Oblique", fontSize=8,   textColor=WHITE,  alignment=TA_RIGHT)
s_th1    = S("t1",  fontName="Helvetica-Bold",    fontSize=7.5, textColor=WHITE,  alignment=TA_CENTER)
s_th1_l  = S("t1l", fontName="Helvetica-Bold",    fontSize=7.5, textColor=WHITE)
s_th1_r  = S("t1r", fontName="Helvetica-Bold",    fontSize=7.5, textColor=WHITE,  alignment=TA_RIGHT)

s_div    = S("dv",  fontName="Helvetica",          fontSize=7.5, textColor=GREY,   alignment=TA_CENTER)
s_desc   = S("dc",  fontName="Helvetica",          fontSize=7.5, textColor=BLACK)
s_desc_b = S("dcb", fontName="Helvetica-Bold",     fontSize=7.5, textColor=BLACK)
s_num    = S("nm",  fontName="Helvetica",          fontSize=7.5, textColor=BLACK,  alignment=TA_RIGHT)
s_num_b  = S("nmb", fontName="Helvetica-Bold",     fontSize=7.5, textColor=BLACK,  alignment=TA_RIGHT)
s_dash   = S("ds",  fontName="Helvetica",          fontSize=7.5, textColor=GREY,   alignment=TA_RIGHT)
s_pct    = S("pc",  fontName="Helvetica",          fontSize=7.5, textColor=GREY,   alignment=TA_RIGHT)
s_tot_l  = S("tl",  fontName="Helvetica",          fontSize=7.5, textColor=WHITE,  alignment=TA_RIGHT)
s_tot_v  = S("tv",  fontName="Helvetica-Bold",     fontSize=7.5, textColor=WHITE,  alignment=TA_RIGHT)
s_grand  = S("gr",  fontName="Helvetica-Bold",     fontSize=8.5, textColor=WHITE)
s_grand_v= S("gv",  fontName="Helvetica-Bold",     fontSize=8.5, textColor=WHITE,  alignment=TA_RIGHT)
s_meta_l = S("ml",  fontName="Helvetica",          fontSize=7.5, textColor=BLACK)
s_meta_v = S("mv",  fontName="Helvetica-Bold",     fontSize=7.5, textColor=BLACK)
s_meta_r = S("mr",  fontName="Helvetica",          fontSize=7.5, textColor=GREY)
s_meta_rv= S("mrv", fontName="Helvetica-Bold",     fontSize=7.5, textColor=BLACK,  alignment=TA_RIGHT)

def fc(v):
    if v is None or v == 0 or v == '': return "-"
    if isinstance(v, str) and v.lower() in ('incl', 'incl in above', '-'): return v
    try: return f"${float(v):,.0f}"
    except: return str(v)

def fp(v):
    try: return f"{float(v)*100:.2f}%"
    except: return "-"

# ── Data ───────────────────────────────────────────────────────────────────────
# Line items: (div, description, cost_single, pct)
line_items = [
    # Building divisions — all zero for this land dev project
    ("0.1",  "Professional Services",                                 0,          0),
    ("1.0",  "General Requirements",                                  33310,      0.003786),
    ("1.1",  "Final / Cleanup",                                       16771,      0.001906),
    ("2.0",  "Demolition",                                            0,          0),
    ("3.0",  "Concrete",                                              0,          0),
    ("4.0",  "Masonry",                                               0,          0),
    ("5.0",  "Structural Steel",                                      0,          0),
    ("5.1",  "Misc. Metals",                                          0,          0),
    ("6.0",  "Rough Carpentry & Wood Framing",                        0,          0),
    ("6.5",  "Millwork Package",                                      0,          0),
    ("7.0",  "Waterproofing",                                         0,          0),
    ("7.1",  "Fireproofing",                                          0,          0),
    ("7.2",  "Thermal Insulation",                                    0,          0),
    ("7.4",  "EIFS & Siding",                                         0,          0),
    ("7.6",  "Roofing",                                               0,          0),
    ("7.7",  "Metal Panels",                                          0,          0),
    ("8.0",  "Doors, Frames & Hardware",                              0,          0),
    ("8.1",  "Overhead Doors",                                        0,          0),
    ("8.2",  "Glass & Glazing",                                       0,          0),
    ("9.0",  "Drywall / Framing",                                     0,          0),
    ("9.2",  "Tile",                                                  0,          0),
    ("9.3",  "Flooring",                                              0,          0),
    ("9.4",  "Paint & Wallcovering",                                  0,          0),
    ("10.0", "Specialties",                                           0,          0),
    ("10.1", "Bathroom Accessories",                                  0,          0),
    ("10.2", "Metal Shelving",                                        0,          0),
    ("10.3", "Canopies",                                              0,          0),
    ("11.0", "Appliances",                                            0,          0),
    ("14.0", "Elevators",                                             0,          0),
    ("21.0", "Fire Suppression — Sprinkler",                          0,          0),
    ("22.0", "Plumbing",                                              0,          0),
    ("23.0", "HVAC",                                                  0,          0),
    ("26.0", "Electrical",                                            0,          0),
    ("26.1", "Low Voltage",                                           0,          0),
    ("26.2", "Access Control",                                        0,          0),
    # Sitework
    ("31.0", "Earthwork",                                             2299224,    0.261306),
    ("32.0", "Site Concrete (Curb & Gutter, Common Area Sidewalks)",  669909,     0.076135),
    ("32.0", "Asphalt Paving",                                        1256292,    0.142777),
    ("32.05","Site Improvements (Walking Trails — Removed)",          0,          0),
    ("32.1", "Landscape, Hardscape & Irrigation",                     106071,     0.012055),
    ("32.2", "Fence & Gates",                                         7536,       0.000856),
    ("33.0", "Domestic Water Utilities — Owner Furnished Pipe",       519991,     0.059097),
    ("33.0", "Sanitary Sewer Utilities — Owner Furnished Pipe",       1431569,    0.162697),
    ("33.0", "Storm Sewer Utilities — Owner Furnished Pipe",          849526,     0.096548),
    ("33.0", "Electrical Conduit — Owner Furnished Conduit",          415800,     0.047256),
    ("33.1", "Pump Station (Allowance)",                              600000,     0.068190),
]

SUBTOTAL     = 8205998
GEN_COND     = 509661
GEN_LI_RATE  = 0.008
GEN_LI       = 65648
BIZ_LIC_RATE = 0.0005
BIZ_LIC      = 4103
CONST_FEE_RT = 0.030
CONST_FEE    = 263562
OWNER_CREDIT = -250000
DESIGN_CONT  = 0
GRAND_TOTAL  = 8798973

# ── Build ───────────────────────────────────────────────────────────────────────
def build():
    out = "/home/claude/Envision_SOV_HigherLiving_Athens.pdf"

    frame_top = PAGE_H - MARGIN_TOP - 0.20*inch
    frame_bot = FOOTER_RULE_Y + 0.20*inch
    frame_h   = frame_top - frame_bot
    frame_w   = PAGE_W - MARGIN_L - MARGIN_R

    frame = Frame(MARGIN_L, frame_bot, frame_w, frame_h,
                  leftPadding=0, rightPadding=0,
                  topPadding=5, bottomPadding=4)

    doc = BaseDocTemplate(out, pagesize=letter,
                          leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=MARGIN_TOP + 0.20*inch,
                          bottomMargin=FOOTER_RULE_Y + 0.20*inch)
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=on_page)])

    W = frame_w
    # Column widths: DIV | Description | Cost | % of Total
    C_DIV  = 0.52 * inch
    C_COST = 1.15 * inch
    C_PCT  = 0.68 * inch
    C_DESC = W - C_DIV - C_COST - C_PCT

    story = []

    # ── Project metadata ───────────────────────────────────────────────────────
    meta_data = [
        [Paragraph("The following documents are part of this proposal:", s_meta_l),
         "", "",
         Paragraph("Site Area", s_meta_r),
         Paragraph("122.02 acres", s_meta_rv)],
        [Paragraph("1.)  Drawings Dated",       s_meta_l),
         Paragraph("March 11, 2026",   s_meta_v), "",
         Paragraph("# of Lots",             s_meta_r),
         Paragraph("230",                   s_meta_rv)],
        [Paragraph("2.)  Specifications Dated", s_meta_l),
         Paragraph("N/A",              s_meta_v), "",
         Paragraph("Bid Type",               s_meta_r),
         Paragraph(BID_TYPE,                 s_meta_rv)],
        [Paragraph("3.)  Schedule Dated",       s_meta_l),
         Paragraph("March 18, 2026",   s_meta_v), "",
         Paragraph("Proposal Date",          s_meta_r),
         Paragraph(DATE_STR,                 s_meta_rv)],
        [Paragraph("4.)  Geotech Report Dated", s_meta_l),
         Paragraph("August 4, 2025",   s_meta_v), "",
         Paragraph("Structure Type",         s_meta_r),
         Paragraph("N/A (Land Dev.)",         s_meta_rv)],
    ]
    mc_l  = W * 0.38
    mc_v  = W * 0.22
    mc_sp = W * 0.06
    mc_rl = W * 0.18
    mc_rv = W * 0.16
    meta_tbl = Table(meta_data, colWidths=[mc_l, mc_v, mc_sp, mc_rl, mc_rv])
    meta_tbl.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("TOPPADDING",    (0,0), (-1,-1), 1.5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 1.5),
        ("LINEBELOW",     (0,-1), (-1,-1), 0.5, LIGHT_GREY),
    ]))
    story.append(meta_tbl)
    story.append(Spacer(1, 7))

    # ── Main SOV table ─────────────────────────────────────────────────────────
    tbl_data = [
        # Row 0: dark grey header — project + date
        [
            Paragraph(f"<b>{PROJECT}</b>", s_th0_l),
            "",
            Paragraph(f"<i>{DATE_STR}</i>", s_th0_r),
            "",
        ],
        # Row 1: column labels — green
        [
            Paragraph("DIV",           s_th1),
            Paragraph("Description",   s_th1_l),
            Paragraph("Cost Estimate", s_th1_r),
            Paragraph("% of Total",    s_th1_r),
        ],
    ]
    tbl_cmds = [
        # Header row 0
        ("SPAN",         (0,0), (1,0)),
        ("SPAN",         (2,0), (3,0)),
        ("BACKGROUND",   (0,0), (-1,0),  DARK_GREY),
        ("LEFTPADDING",  (0,0), (-1,0),  7),
        ("RIGHTPADDING", (0,0), (-1,0),  7),
        ("TOPPADDING",   (0,0), (-1,0),  5),
        ("BOTTOMPADDING",(0,0), (-1,0),  5),
        # Column header row 1
        ("BACKGROUND",   (0,1), (-1,1),  GREEN),
        ("LINEBELOW",    (0,1), (-1,1),  0.5, WHITE),
        ("LEFTPADDING",  (0,1), (-1,1),  5),
        ("RIGHTPADDING", (0,1), (-1,1),  5),
        ("TOPPADDING",   (0,1), (-1,1),  4),
        ("BOTTOMPADDING",(0,1), (-1,1),  4),
        # Body
        ("FONTSIZE",     (0,2), (-1,-1), 7.5),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",  (0,2), (-1,-1), 5),
        ("RIGHTPADDING", (0,2), (-1,-1), 5),
        ("TOPPADDING",   (0,2), (-1,-1), 2.5),
        ("BOTTOMPADDING",(0,2), (-1,-1), 2.5),
        ("INNERGRID",    (0,2), (-1,-1), 0.25, LIGHT_GREY),
        ("BOX",          (0,0), (-1,-1), 0.5,  LIGHT_GREY),
    ]

    # Track rows with zero cost for grey styling
    zero_rows = []

    for div, desc, cost, pct in line_items:
        r = len(tbl_data)
        is_zero = cost == 0
        if is_zero:
            zero_rows.append(r)
        tbl_data.append([
            Paragraph(div,          s_div),
            Paragraph(desc,         s_desc),
            Paragraph(fc(cost),     s_dash if is_zero else s_num),
            Paragraph(fp(pct) if not is_zero else "—", s_dash if is_zero else s_pct),
        ])

    # Grey out zero rows
    for r in zero_rows:
        tbl_cmds.append(("TEXTCOLOR", (0,r), (-1,r), GREY))

    # Subtotal row
    r_sub = len(tbl_data)
    tbl_data.append([
        "",
        Paragraph("<b>AIA Subtotal</b>", s_desc_b),
        Paragraph(fc(SUBTOTAL),           s_num_b),
        Paragraph(fp(0.9326),             s_num_b),
    ])
    tbl_cmds += [
        ("BACKGROUND",  (0, r_sub), (-1, r_sub), BG),
        ("LINEABOVE",   (0, r_sub), (-1, r_sub), 0.75, DARK_GREY),
        ("LINEBELOW",   (0, r_sub), (-1, r_sub), 0.75, DARK_GREY),
    ]

    # Fee rows
    fee_rows = [
        ("General Conditions",       "",          GEN_COND,     GEN_COND/SUBTOTAL),
        ("General Liability Insurance", f"{GEN_LI_RATE*100:.1f}%", GEN_LI, GEN_LI/SUBTOTAL),
        ("SDI",                      "",          0,            0),
        ("Business License",         f"{BIZ_LIC_RATE*100:.2f}%", BIZ_LIC, BIZ_LIC/SUBTOTAL),
        ("Construction Fee",         f"{CONST_FEE_RT*100:.1f}%", CONST_FEE, CONST_FEE/SUBTOTAL),
        ("Owner Credit",             "",          OWNER_CREDIT, OWNER_CREDIT/SUBTOTAL),
        ("Design Contingency",       "0.0%",      0,            0),
    ]

    for i, (label, rate, cost, pct) in enumerate(fee_rows):
        r = len(tbl_data)
        lbl_str = f"{rate}  {label}" if rate else f"       {label}"
        is_zero = cost == 0
        is_neg  = cost < 0
        v_style = s_tot_v
        tbl_data.append([
            Paragraph(lbl_str, S("fl", fontName="Helvetica", fontSize=7.5,
                                  textColor=WHITE, alignment=TA_RIGHT)),
            "",
            Paragraph(fc(abs(cost)) if not is_neg else f"({fc(abs(cost))})",
                      S("fv", fontName="Helvetica-Bold" if not is_zero else "Helvetica",
                              fontSize=7.5, textColor=WHITE, alignment=TA_RIGHT)),
            Paragraph(fp(abs(pct)) if not is_zero else "—",
                      S("fp", fontName="Helvetica", fontSize=7.5,
                              textColor=WHITE, alignment=TA_RIGHT)),
        ])
        tbl_cmds += [
            ("SPAN",       (0,r), (1,r)),
            ("BACKGROUND", (0,r), (-1,r), GREEN),
        ]

    # Grand total row
    r_grand = len(tbl_data)
    tbl_data.append([
        Paragraph("GRAND TOTAL", s_grand),
        "",
        Paragraph(fc(GRAND_TOTAL), s_grand_v),
        Paragraph("100.00%",       s_grand_v),
    ])
    tbl_cmds += [
        ("SPAN",       (0, r_grand), (1, r_grand)),
        ("BACKGROUND", (0, r_grand), (-1, r_grand), DARK_GREY),
        ("TOPPADDING",   (0, r_grand), (-1, r_grand), 5),
        ("BOTTOMPADDING",(0, r_grand), (-1, r_grand), 5),
        ("LINEABOVE",    (0, r_grand), (-1, r_grand), 0.5, WHITE),
    ]
    # Fee + total row padding
    r_fee_start = r_sub + 1
    tbl_cmds += [
        ("LEFTPADDING",   (0, r_fee_start), (-1, r_grand), 7),
        ("RIGHTPADDING",  (0, r_fee_start), (-1, r_grand), 7),
        ("TOPPADDING",    (0, r_fee_start), (-1, r_grand-1), 3),
        ("BOTTOMPADDING", (0, r_fee_start), (-1, r_grand-1), 3),
        ("LINEBELOW",     (0, r_fee_start), (-1, r_grand-1), 0.3, colors.HexColor("#FFFFFF50")),
    ]

    sov = Table(tbl_data,
                colWidths=[C_DIV, C_DESC, C_COST, C_PCT],
                repeatRows=2)
    sov.setStyle(TableStyle(tbl_cmds))
    story.append(sov)

    doc.build(story)
    print(f"Done → {out}")

build()
