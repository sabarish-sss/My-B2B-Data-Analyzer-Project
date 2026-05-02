import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="B2B Business Data Analyzer",
    page_icon="📊",
    layout="wide"
)

# ── Clean Professional Blue Dark Theme ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', system-ui, sans-serif !important; }
.stApp            { background: #080d14 !important; }
.block-container  { padding: 0 !important; max-width: 100% !important; }
#MainMenu, footer, header { visibility: hidden; }

.pg { max-width: 1300px; margin: 0 auto; padding: 0 48px; }

.sec {
    display: flex; align-items: center; gap: 12px;
    font-size: 9.5px; font-weight: 700; letter-spacing: .18em;
    text-transform: uppercase; color: #2a4a6e;
    padding-top: 30px; padding-bottom: 14px;
}
.sec::after { content:''; flex:1; height:1px; background:#0e1c2e; }

.kpi-row { display:grid; grid-template-columns:repeat(4,1fr); gap:14px; padding-bottom:22px; }
.kpi {
    background: #0b1420; border: 1px solid #112238; border-radius: 14px;
    padding: 20px 22px; display:flex; align-items:center; gap:16px; min-width:0;
}
.kpi-ico { width:44px; height:44px; border-radius:10px; flex-shrink:0; display:flex; align-items:center; justify-content:center; font-size:19px; }
.ico-a { background:#0a1f3a; }
.ico-t { background:#051a1a; }
.ico-r { background:#1a0d1a; }
.ico-s { background:#0d1830; border:1px solid #112238; }
.kpi-body { flex:1; min-width:0; }
.kpi-lbl  { font-size:9.5px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; color:#2a4a6e; margin-bottom:4px; }
.kpi-val  { font-size:28px; font-weight:700; letter-spacing:-0.03em; line-height:1; }
.v-a { color:#4d9ef7; }
.v-t { color:#2ee8c4; }
.v-r { color:#e85090; }
.v-s { color:#9bbce0; }
.kpi-sub  { font-size:11px; color:#2a4a6e; margin-top:5px; }
.kpi-bar  { height:2px; background:#0e1c2e; border-radius:2px; margin-top:11px; overflow:hidden; }
.kpi-fill { height:100%; border-radius:2px; }

.bk-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px; padding-bottom:22px; }
.bcard   { background:#0b1420; border:1px solid #112238; border-radius:14px; padding:22px 24px; }
.bcard-title { font-size:9.5px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:#2a4a6e; margin-bottom:18px; }

.iss-row { display:flex; align-items:center; gap:11px; margin-bottom:13px; }
.iss-row:last-child { margin-bottom:0; }
.iss-ico  { width:31px; height:31px; border-radius:8px; flex-shrink:0; display:flex; align-items:center; justify-content:center; font-size:13px; }
.iss-body { flex:1; min-width:0; }
.iss-name { font-size:12.5px; color:#9bbce0; margin-bottom:5px; }
.iss-track{ height:4px; background:#0e1c2e; border-radius:2px; overflow:hidden; }
.iss-fill { height:100%; border-radius:2px; }
.iss-cnt  { font-size:13px; font-weight:600; color:#c8ddf4; flex-shrink:0; min-width:20px; text-align:right; }

.donut-wrap   { display:flex; align-items:center; gap:26px; }
.donut-legend { flex:1; }
.leg-item     { display:flex; align-items:center; gap:9px; margin-bottom:12px; font-size:12.5px; }
.leg-item:last-child { margin-bottom:0; }
.leg-dot  { width:9px; height:9px; border-radius:50%; flex-shrink:0; }
.leg-name { flex:1; color:#9bbce0; }
.leg-val  { font-weight:600; color:#c8ddf4; }
.leg-pct  { font-size:11px; color:#2a4a6e; min-width:32px; text-align:right; }

.alrt-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:14px; padding-bottom:22px; }
.alrt      { border-radius:12px; padding:18px 20px; display:flex; flex-direction:column; }
.alrt-n    { font-size:30px; font-weight:700; letter-spacing:-0.03em; line-height:1; margin-bottom:6px; }
.alrt-t    { font-size:12.5px; font-weight:600; margin-bottom:3px; }
.alrt-d    { font-size:11.5px; line-height:1.5; opacity:.65; }
.alrt-g    { background:#051a1a; border:1px solid #0a3a30; }
.alrt-g .alrt-n, .alrt-g .alrt-t { color:#2ee8c4; }
.alrt-g .alrt-d { color:#6de8d4; }
.alrt-a    { background:#061428; border:1px solid #0d2e58; }
.alrt-a .alrt-n, .alrt-a .alrt-t { color:#4d9ef7; }
.alrt-a .alrt-d { color:#80baf8; }
.alrt-r    { background:#180d20; border:1px solid #361040; }
.alrt-r .alrt-n, .alrt-r .alrt-t { color:#e85090; }
.alrt-r .alrt-d { color:#e090b8; }

.pill { display:inline-flex; align-items:center; padding:2px 9px; border-radius:20px; font-size:11px; font-weight:500; white-space:nowrap; }
.p-g { background:#051a1a; color:#2ee8c4; border:1px solid #0a3a30; }
.p-r { background:#180d20; color:#e85090; border:1px solid #361040; }
.p-a { background:#061428; color:#4d9ef7; border:1px solid #0d2e58; }
.p-b { background:#0a1428; color:#7ab8f7; border:1px solid #10305e; }
.p-x { background:#0b1420; color:#2a4a6e; border:1px solid #112238; }
.muted { color:#2a4a6e; }

.tbl-wrap { padding-bottom:52px; }
.ptable {
    width:100%; border-collapse:collapse; font-size:12.5px;
    background:#0b1420; border:1px solid #112238; border-radius:12px; overflow:hidden;
}
.ptable thead tr { background:#080d18; }
.ptable th {
    padding:12px 15px; text-align:left;
    font-size:9.5px; font-weight:700; letter-spacing:.10em; text-transform:uppercase;
    color:#2a4a6e; border-bottom:1px solid #112238; white-space:nowrap;
}
.ptable td { padding:12px 15px; border-bottom:1px solid #0e1c2e; color:#9bbce0; vertical-align:middle; line-height:1.4; }
.ptable tbody tr:last-child td { border-bottom:none; }
.ptable tbody tr:hover         { background:#0d1828; }
.r-can      { border-left:3px solid #2ee8c4; }
.r-restock  { border-left:3px solid #4d9ef7; }
.r-notfound { border-left:3px solid #e85090; }
.r-can td:first-child, .r-restock td:first-child, .r-notfound td:first-child { padding-left:12px; }
.mono { font-family:'JetBrains Mono',monospace; font-size:11.5px; }

.input-wrap { padding-bottom:28px; }

.stTextArea textarea {
    background:#080d18 !important; border:1px solid #112238 !important;
    border-radius:10px !important; color:#c8ddf4 !important;
    font-family:'DM Sans',sans-serif !important;
    font-size:13.5px !important; padding:14px 16px !important; line-height:1.7 !important;
}
.stTextArea textarea:focus { border-color:#4d9ef7 !important; box-shadow:0 0 0 3px rgba(77,158,247,.12) !important; }
.stFileUploader > div      { background:#080d18 !important; border:1.5px dashed #112238 !important; border-radius:10px !important; }
.stFileUploader label      { color:#2a4a6e !important; font-size:12.5px !important; }
.stButton > button {
    background:linear-gradient(135deg,#1457c8 0%,#4d9ef7 100%) !important;
    color:#ffffff !important; border:none !important; border-radius:10px !important;
    font-family:'DM Sans',sans-serif !important;
    font-size:13.5px !important; font-weight:700 !important;
    padding:11px 28px !important; width:100% !important; letter-spacing:.01em !important;
    transition:opacity .15s !important;
}
.stButton > button:hover { opacity:.85 !important; }
.stDownloadButton > button {
    background:#0b1420 !important; color:#4d9ef7 !important;
    border:1px solid #0d2e58 !important; border-radius:10px !important;
    font-family:'DM Sans',sans-serif !important;
    font-size:12.5px !important; font-weight:500 !important; padding:9px 22px !important;
}
.stSuccess { border-radius:10px !important; font-size:12.5px !important; }
.stWarning { border-radius:10px !important; font-size:12.5px !important; }
.stError   { border-radius:10px !important; font-size:12.5px !important; }
.stMarkdown p, .stMarkdown li { color:#9bbce0 !important; font-size:13.5px !important; }
div[data-testid="column"]                              { padding:0 !important; }
div[data-testid="column"] + div[data-testid="column"]  { padding-left:12px !important; }
</style>
""", unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────────────────────────────────────
def pill(text, style="x"):
    cls = {"g":"p-g","r":"p-r","a":"p-a","b":"p-b","x":"p-x"}.get(style,"p-x")
    return f'<span class="pill {cls}">{text}</span>'

def availability_pill(text):
    t = str(text).lower()
    if t == "available":    return pill(text, "g")
    if t == "out of stock": return pill(text, "r")
    return '<span class="muted">—</span>'

def decision_pill(text):
    t = str(text).lower()
    if "can purchase" in t: return pill(text, "g")
    if "restock" in t:      return pill(text, "a")
    if "not found" in t:    return pill(text, "b")
    if "not checked" in t:  return '<span class="muted">—</span>'
    return pill(text, "x")

def category_pill(text):
    t = str(text).lower()
    if "delivery" in t or "quality" in t:     return pill(text, "r")
    if "pricing" in t or "availability" in t: return pill(text, "a")
    return pill(text, "x")


# ── Core logic (unchanged) ────────────────────────────────────────────────────
def analyze_feedback(text):
    text = text.lower()
    if any(w in text for w in ["late","delay","slow"]):
        return "Delivery Issue","Improve logistics speed"
    elif any(w in text for w in ["bad quality","damaged","broken","poor"]):
        return "Quality Issue","Improve product quality"
    elif any(w in text for w in ["price","cost","expensive","high"]):
        return "Pricing Issue","Review pricing strategy"
    elif any(w in text for w in ["out of stock","not available","unavailable"]):
        return "Availability Issue","Increase stock levels"
    else:
        return "General Feedback","Review manually"

def find_product(feedback_text, products_df):
    feedback_text = feedback_text.lower()
    for _, row in products_df.iterrows():
        if str(row["Product"]).lower() in feedback_text:
            qty = int(row["Available Quantity"])
            return row["Product"], ("Available" if qty > 0 else "Out of Stock"), qty, row["Quality"], row["Price"]
    return "Not Found","Unknown","Unknown","Unknown","Unknown"

def generate_results(feedback_list, products_df=None):
    results = []
    for fb in feedback_list:
        fb = str(fb).strip()
        if not fb: continue
        category, action = analyze_feedback(fb)
        product = availability = quantity = quality = price = decision = "Not Checked"
        if products_df is not None:
            product, availability, quantity, quality, price = find_product(fb, products_df)
            if availability == "Available":
                decision = "Can Purchase"
            elif availability == "Out of Stock":
                decision = "Cannot Purchase - Restock Needed"
                action   = "Restock product immediately"
            else:
                decision = "Product Not Found"
        results.append({
            "Feedback":fb, "Category":category, "Product":product,
            "Availability":availability, "Available Quantity":quantity,
            "Quality":quality, "Price":price, "Decision":decision, "Action Needed":action,
        })
    return pd.DataFrame(results)


# ── SVG donut ─────────────────────────────────────────────────────────────────
def make_donut_svg(segments):
    total = sum(v for _,v,_ in segments) or 1
    r, cx, cy, sw = 44, 60, 60, 18
    circ = 2 * 3.14159 * r
    off, arcs = 0, ""
    for _, val, color in segments:
        pct  = val / total
        dash = round(pct * circ, 2)
        gap  = round(circ - dash, 2)
        arcs += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" '
                 f'stroke-width="{sw}" stroke-dasharray="{dash} {gap}" '
                 f'stroke-dashoffset="-{round(off,2)}" stroke-linecap="butt"/>')
        off += pct * circ
    return (f'<svg width="120" height="120" viewBox="0 0 120 120" style="transform:rotate(-90deg);flex-shrink:0">'
            f'<circle cx="60" cy="60" r="44" fill="none" stroke="#0e1c2e" stroke-width="18"/>'
            f'{arcs}</svg>')


# ── Dashboard ─────────────────────────────────────────────────────────────────
def show_dashboard(df_result, df_products=None):
    total_fb     = len(df_result)
    can_purchase = (df_result["Decision"] == "Can Purchase").sum()
    cannot_purch = (df_result["Decision"] == "Cannot Purchase - Restock Needed").sum()
    not_found    = (df_result["Decision"] == "Product Not Found").sum()
    top_issue    = df_result["Category"].value_counts().idxmax() if total_fb else "—"
    fulfill_pct  = round(can_purchase / total_fb * 100) if total_fb else 0
    restock_pct  = round(cannot_purch / total_fb * 100) if total_fb else 0

    st.markdown(
        '<div class="pg"><div class="sec">Overview</div><div class="kpi-row">'

        '<div class="kpi"><div class="kpi-ico ico-a">📋</div><div class="kpi-body">'
        '<div class="kpi-lbl">Total Feedback</div>'
        f'<div class="kpi-val v-a">{total_fb}</div>'
        '<div class="kpi-sub">items analyzed</div>'
        '<div class="kpi-bar"><div class="kpi-fill" style="width:100%;background:#4d9ef7"></div></div>'
        '</div></div>'

        '<div class="kpi"><div class="kpi-ico ico-t">✅</div><div class="kpi-body">'
        '<div class="kpi-lbl">Can Purchase</div>'
        f'<div class="kpi-val v-t">{can_purchase}</div>'
        f'<div class="kpi-sub">{fulfill_pct}% fulfillment rate</div>'
        f'<div class="kpi-bar"><div class="kpi-fill" style="width:{fulfill_pct}%;background:#2ee8c4"></div></div>'
        '</div></div>'

        '<div class="kpi"><div class="kpi-ico ico-r">🔴</div><div class="kpi-body">'
        '<div class="kpi-lbl">Restock Needed</div>'
        f'<div class="kpi-val v-r">{cannot_purch}</div>'
        f'<div class="kpi-sub">{restock_pct}% blocked orders</div>'
        f'<div class="kpi-bar"><div class="kpi-fill" style="width:{restock_pct}%;background:#e85090"></div></div>'
        '</div></div>'

        '<div class="kpi"><div class="kpi-ico ico-s">⚠️</div><div class="kpi-body">'
        '<div class="kpi-lbl">Top Issue Type</div>'
        f'<div class="kpi-val v-s" style="font-size:16px;margin-top:3px">{top_issue}</div>'
        '<div class="kpi-sub">most reported category</div>'
        '</div></div>'

        '</div></div>',
        unsafe_allow_html=True
    )

    cat_counts = df_result["Category"].value_counts().to_dict()
    cat_cfg = {
        "Delivery Issue":     ("#e85090","🚚","#180d20"),
        "Quality Issue":      ("#e85090","🔧","#180d20"),
        "Pricing Issue":      ("#4d9ef7","💰","#061428"),
        "Availability Issue": ("#4d9ef7","📦","#061428"),
        "General Feedback":   ("#2a4a6e","💬","#0b1420"),
    }
    max_cat = max(cat_counts.values(), default=1)
    iss_html = ""
    for cat, cnt in cat_counts.items():
        color, icon, bg = cat_cfg.get(cat, ("#2a4a6e","💬","#0b1420"))
        pct = round(cnt / max_cat * 100)
        iss_html += (
            f'<div class="iss-row">'
            f'<div class="iss-ico" style="background:{bg}">{icon}</div>'
            f'<div class="iss-body">'
            f'<div class="iss-name">{cat}</div>'
            f'<div class="iss-track"><div class="iss-fill" style="width:{pct}%;background:{color}"></div></div>'
            f'</div><div class="iss-cnt">{cnt}</div></div>'
        )

    dec_segs = []
    if can_purchase > 0: dec_segs.append(("Can Purchase",   can_purchase, "#2ee8c4"))
    if cannot_purch > 0: dec_segs.append(("Restock Needed", cannot_purch, "#4d9ef7"))
    if not_found    > 0: dec_segs.append(("Not Found",      not_found,    "#e85090"))
    donut_svg = make_donut_svg(dec_segs) if dec_segs else ""

    leg_html = ""
    for label, val, color in dec_segs:
        pct = round(val / total_fb * 100) if total_fb else 0
        leg_html += (
            f'<div class="leg-item">'
            f'<div class="leg-dot" style="background:{color}"></div>'
            f'<div class="leg-name">{label}</div>'
            f'<div class="leg-val">{val}</div>'
            f'<div class="leg-pct">{pct}%</div>'
            f'</div>'
        )

    st.markdown(
        '<div class="pg"><div class="sec">Breakdown</div><div class="bk-grid">'
        f'<div class="bcard"><div class="bcard-title">Issue Categories</div>{iss_html}</div>'
        f'<div class="bcard"><div class="bcard-title">Purchase Decisions</div>'
        f'<div class="donut-wrap">{donut_svg}<div class="donut-legend">{leg_html}</div></div>'
        '</div></div></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="pg"><div class="alrt-grid">'
        f'<div class="alrt alrt-g"><div class="alrt-n">{can_purchase}</div>'
        f'<div class="alrt-t">Ready to Fulfill</div>'
        f'<div class="alrt-d">Products in stock and available for immediate purchase.</div></div>'
        f'<div class="alrt alrt-a"><div class="alrt-n">{cannot_purch}</div>'
        f'<div class="alrt-t">Restock Required</div>'
        f'<div class="alrt-d">Items are out of stock — procurement action needed.</div></div>'
        f'<div class="alrt alrt-r"><div class="alrt-n">{not_found}</div>'
        f'<div class="alrt-t">Product Not Found</div>'
        f'<div class="alrt-d">Feedback mentions products missing from catalog.</div></div>'
        f'</div></div>',
        unsafe_allow_html=True
    )

    rows_html = ""
    for _, row in df_result.iterrows():
        fb_text  = str(row["Feedback"])
        fb_short = fb_text[:65] + ("&#8230;" if len(fb_text) > 65 else "")
        dec      = str(row["Decision"])
        cls      = ("r-can"      if dec == "Can Purchase"
                    else "r-restock"  if "Restock"  in dec
                    else "r-notfound" if "Not Found" in dec else "")
        rows_html += (
            f'<tr class="{cls}">'
            f'<td title="{fb_text.replace(chr(34),chr(39))}" style="max-width:200px">{fb_short}</td>'
            f'<td>{category_pill(str(row["Category"]))}</td>'
            f'<td class="mono" style="color:#c8ddf4">{row["Product"]}</td>'
            f'<td>{availability_pill(str(row["Availability"]))}</td>'
            f'<td class="mono" style="color:#2a4a6e;text-align:center">{row["Available Quantity"]}</td>'
            f'<td style="font-size:11.5px;color:#c8ddf4">{row["Quality"]}</td>'
            f'<td class="mono" style="color:#c8ddf4">{row["Price"]}</td>'
            f'<td>{decision_pill(str(row["Decision"]))}</td>'
            f'<td style="font-size:11.5px;color:#2a4a6e">{row["Action Needed"]}</td>'
            f'</tr>'
        )

    st.markdown(
        '<div class="pg"><div class="sec">Detailed Results</div><div class="tbl-wrap">'
        '<table class="ptable"><thead><tr>'
        '<th>Feedback</th><th>Category</th><th>Product</th><th>Availability</th>'
        '<th>Qty</th><th>Quality</th><th>Price</th><th>Decision</th><th>Action Needed</th>'
        f'</tr></thead><tbody>{rows_html}</tbody></table>'
        '</div></div>',
        unsafe_allow_html=True
    )


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:#0b1420;border-bottom:1px solid #112238;padding:26px 0 22px;">
  <div style="max-width:1300px;margin:0 auto;padding:0 48px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
    <div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
        <div style="width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,#1457c8,#4d9ef7);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="2,12 6,7 9,10 14,4"/>
          </svg>
        </div>
        <span style="font-family:'DM Sans',sans-serif;font-size:18px;font-weight:700;color:#c8ddf4;letter-spacing:-0.02em;">B2B Data Analyzer</span>
      </div>
      <div style="font-family:'DM Sans',sans-serif;font-size:12.5px;color:#2a4a6e;max-width:460px;line-height:1.65;">
        Convert unstructured customer feedback into structured business decisions
        using product availability, quantity, quality, and pricing data.
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── Input section ─────────────────────────────────────────────────────────────
st.markdown('<div class="pg"><div class="sec">Input</div><div class="input-wrap">', unsafe_allow_html=True)

feedback_text = st.text_area(
    "Customer feedback",
    placeholder=(
        "Enter each feedback on a new line\n\n"
        "Example:\n"
        "The laptop delivery was extremely slow\n"
        "Mouse is out of stock again\n"
        "Keyboard price is too high\n"
        "Monitor quality is poor"
    ),
    height=170,
    label_visibility="collapsed",
)

fcol1, fcol2 = st.columns(2, gap="medium")
with fcol1:
    st.markdown(
        '<div style="display:flex;align-items:center;gap:7px;margin-bottom:6px;">'
        '<span style="font-size:12.5px;font-weight:500;color:#9bbce0;">📄 Feedback CSV</span>'
        '<span style="font-size:10px;color:#2a4a6e;background:#0b1420;border:1px solid #112238;border-radius:20px;padding:2px 8px;">required: Feedback column</span>'
        '</div>',
        unsafe_allow_html=True)
    feedback_file = st.file_uploader("Feedback CSV", type=["csv"],
                                     label_visibility="collapsed",
                                     help="CSV must have a 'Feedback' column")
with fcol2:
    st.markdown(
        '<div style="display:flex;align-items:center;gap:7px;margin-bottom:6px;">'
        '<span style="font-size:12.5px;font-weight:500;color:#9bbce0;">📦 Product Data CSV</span>'
        '<span style="font-size:10px;color:#2a4a6e;background:#0b1420;border:1px solid #112238;border-radius:20px;padding:2px 8px;">required: Product column</span>'
        '</div>',
        unsafe_allow_html=True)
    product_file = st.file_uploader("Products CSV", type=["csv"],
                                    label_visibility="collapsed",
                                    help="CSV must have: Product, Available Quantity, Quality, Price")

analyze_clicked = st.button("▶  Run Analysis", use_container_width=True)
st.markdown('</div></div>', unsafe_allow_html=True)


# ── Run: manual text ──────────────────────────────────────────────────────────
if analyze_clicked:
    if feedback_text.strip():
        fb_list     = [l for l in feedback_text.split("\n") if l.strip()]
        df_products = pd.read_csv(product_file) if product_file else None
        df_result   = generate_results(fb_list, df_products)
        st.success(f"Analysis complete — {len(df_result)} feedback items processed.")
        show_dashboard(df_result, df_products)
    else:
        st.warning("Please enter at least one line of feedback before running analysis.")


# ── Run: both CSVs ────────────────────────────────────────────────────────────
if feedback_file is not None and product_file is not None:
    df_feedback = pd.read_csv(feedback_file)
    df_products = pd.read_csv(product_file)

    if "Feedback" not in df_feedback.columns or "Product" not in df_products.columns:
        st.error("Feedback CSV must have a 'Feedback' column and Product CSV must have a 'Product' column.")
    else:
        st.markdown('<div class="pg"><div class="sec">Uploaded Data Preview</div></div>', unsafe_allow_html=True)
        pc1, pc2 = st.columns(2, gap="medium")
        with pc1:
            st.caption("Feedback data")
            st.dataframe(df_feedback, use_container_width=True, height=220)
        with pc2:
            st.caption("Product data")
            st.dataframe(df_products, use_container_width=True, height=220)

        df_result = generate_results(df_feedback["Feedback"], df_products)
        st.success(f"CSV analysis complete — {len(df_result)} feedback items processed.")
        show_dashboard(df_result, df_products)

        st.download_button(
            label="⬇  Download Business Insights CSV",
            data=df_result.to_csv(index=False),
            file_name="business_insights.csv",
            mime="text/csv",
        )