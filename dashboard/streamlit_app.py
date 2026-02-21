import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="KPI Intelligence Center",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

* { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #080C14;
    color: #E2E8F0;
}

.stApp { background-color: #080C14; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D1421 0%, #080C14 100%);
    border-right: 1px solid rgba(99, 179, 237, 0.1);
}

section[data-testid="stSidebar"] .stMarkdown p {
    color: #94A3B8;
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* Main header */
.dashboard-header {
    background: linear-gradient(135deg, #0D1421 0%, #111827 100%);
    border: 1px solid rgba(99, 179, 237, 0.15);
    border-radius: 16px;
    padding: 32px 40px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}

.dashboard-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #63B3ED, #4FD1C5, #F6AD55);
}

.dashboard-title {
    font-family: 'Syne', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #F1F5F9;
    margin: 0;
    letter-spacing: -0.5px;
}

.dashboard-subtitle {
    font-size: 13px;
    color: #64748B;
    margin-top: 4px;
    font-weight: 300;
    letter-spacing: 0.05em;
}

.live-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(72, 187, 120, 0.1);
    border: 1px solid rgba(72, 187, 120, 0.3);
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 11px;
    color: #48BB78;
    font-weight: 500;
    letter-spacing: 0.05em;
}

.live-dot {
    width: 6px; height: 6px;
    background: #48BB78;
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

/* KPI Cards */
.kpi-card {
    background: linear-gradient(135deg, #0D1421 0%, #111827 100%);
    border: 1px solid rgba(99, 179, 237, 0.1);
    border-radius: 14px;
    padding: 22px 24px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s;
}

.kpi-card:hover { border-color: rgba(99, 179, 237, 0.3); }

.kpi-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 0 0 14px 14px;
}

.kpi-blue::after   { background: linear-gradient(90deg, #63B3ED, #4299E1); }
.kpi-teal::after   { background: linear-gradient(90deg, #4FD1C5, #38B2AC); }
.kpi-amber::after  { background: linear-gradient(90deg, #F6AD55, #ED8936); }
.kpi-red::after    { background: linear-gradient(90deg, #FC8181, #F56565); }
.kpi-purple::after { background: linear-gradient(90deg, #B794F4, #9F7AEA); }

.kpi-label {
    font-size: 11px;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 500;
    margin-bottom: 8px;
}

.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 700;
    color: #F1F5F9;
    line-height: 1;
    margin-bottom: 8px;
}

.kpi-delta {
    font-size: 12px;
    font-weight: 500;
}

.delta-up   { color: #48BB78; }
.delta-down { color: #FC8181; }
.delta-neu  { color: #94A3B8; }

/* Section headers */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: #CBD5E0;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: rgba(99, 179, 237, 0.1);
}

/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    background: #0D1421;
    border-radius: 10px;
    padding: 4px;
    gap: 4px;
    border: 1px solid rgba(99, 179, 237, 0.1);
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 8px;
    color: #64748B;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    padding: 8px 20px;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #1E3A5F, #1A3550) !important;
    color: #63B3ED !important;
}

/* Table styling */
.dataframe {
    background: #0D1421 !important;
    border: 1px solid rgba(99, 179, 237, 0.1) !important;
    border-radius: 10px !important;
}

/* Insight cards */
.insight-card {
    background: rgba(99, 179, 237, 0.05);
    border: 1px solid rgba(99, 179, 237, 0.15);
    border-left: 3px solid #63B3ED;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 10px;
    font-size: 13px;
    color: #CBD5E0;
    line-height: 1.6;
}

.insight-card.warning {
    background: rgba(246, 173, 85, 0.05);
    border-color: rgba(246, 173, 85, 0.15);
    border-left-color: #F6AD55;
}

.insight-card.success {
    background: rgba(72, 187, 120, 0.05);
    border-color: rgba(72, 187, 120, 0.15);
    border-left-color: #48BB78;
}

/* Selectbox & slider */
.stSelectbox > div > div {
    background: #0D1421;
    border: 1px solid rgba(99, 179, 237, 0.2);
    border-radius: 8px;
    color: #E2E8F0;
}

.stMultiSelect > div > div {
    background: #0D1421;
    border: 1px solid rgba(99, 179, 237, 0.2);
    border-radius: 8px;
}

/* Divider */
hr { border-color: rgba(99, 179, 237, 0.08) !important; }

/* Footer */
.footer {
    text-align: center;
    color: #334155;
    font-size: 11px;
    padding: 20px;
    letter-spacing: 0.05em;
}
</style>
""", unsafe_allow_html=True)

# ── Load & Prepare Data ──────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("data/sales_data_sample.csv", encoding="latin1")
    df.columns = df.columns.str.strip()
    for col in ["SALES", "PRICEEACH", "QUANTITYORDERED", "MSRP"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["PROFIT"]    = df["SALES"] * 0.45
    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")
    df["MONTH"]     = df["YEAR_ID"].astype(str) + "-" + df["MONTH_ID"].astype(str).str.zfill(2)
    return df

df_all = load_data()

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding: 20px 0 10px;'>
        <div style='font-family: Syne, sans-serif; font-size: 18px; font-weight: 800; color: #F1F5F9;'>KPI Intel</div>
        <div style='font-size: 11px; color: #334155; margin-top: 2px;'>Sales Intelligence Center</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**FILTERS**")

    years = sorted(df_all["YEAR_ID"].dropna().unique().astype(int).tolist())
    selected_years = st.multiselect(
        "Year",
        options=years,
        default=years,
        key="year_filter"
    )

    product_lines = sorted(df_all["PRODUCTLINE"].dropna().unique().tolist())
    selected_products = st.multiselect(
        "Product Line",
        options=product_lines,
        default=product_lines,
        key="product_filter"
    )

    deal_sizes = sorted(df_all["DEALSIZE"].dropna().unique().tolist())
    selected_deals = st.multiselect(
        "Deal Size",
        options=deal_sizes,
        default=deal_sizes,
        key="deal_filter"
    )

    st.markdown("---")
    st.markdown("**NAVIGATION**")
    st.markdown("📊 Overview")
    st.markdown("📦 Products")
    st.markdown("🌍 Regions")
    st.markdown("📈 Trends")
    st.markdown("💼 Deal Analysis")

    st.markdown("---")
    st.markdown("""
    <div style='font-size: 10px; color: #1E293B; text-align: center;'>
        KPI Reporting System v2.0<br>Samuel Oyedokun
    </div>
    """, unsafe_allow_html=True)

# ── Apply Filters ────────────────────────────────────────────
df = df_all.copy()
if selected_years:
    df = df[df["YEAR_ID"].isin(selected_years)]
if selected_products:
    df = df[df["PRODUCTLINE"].isin(selected_products)]
if selected_deals:
    df = df[df["DEALSIZE"].isin(selected_deals)]

# ── Plotly Theme ─────────────────────────────────────────────
CHART_BG    = "#080C14"
PAPER_BG    = "#0D1421"
GRID_COLOR  = "rgba(99,179,237,0.06)"
FONT_COLOR  = "#94A3B8"
ACCENT      = "#63B3ED"
TEAL        = "#4FD1C5"
AMBER       = "#F6AD55"
GREEN       = "#48BB78"
RED         = "#FC8181"
PURPLE      = "#B794F4"

COLORS = [ACCENT, TEAL, AMBER, GREEN, RED, PURPLE, "#F687B3", "#68D391"]

def chart_layout(fig, title="", height=380):
    fig.update_layout(
        title=dict(text=title, font=dict(family="Syne", size=14, color="#CBD5E0"), x=0, xanchor="left"),
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=CHART_BG,
        font=dict(family="DM Sans", color=FONT_COLOR, size=12),
        height=height,
        margin=dict(l=16, r=16, t=48, b=16),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            bordercolor="rgba(99,179,237,0.1)",
            font=dict(size=11)
        ),
        xaxis=dict(gridcolor=GRID_COLOR, linecolor="rgba(99,179,237,0.1)", tickfont=dict(size=11)),
        yaxis=dict(gridcolor=GRID_COLOR, linecolor="rgba(99,179,237,0.1)", tickfont=dict(size=11)),
    )
    return fig

# ── KPI Calculations ─────────────────────────────────────────
total_revenue = df["SALES"].sum()
total_profit  = df["PROFIT"].sum()
profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
total_orders  = df["ORDERNUMBER"].nunique()
avg_order     = total_revenue / total_orders if total_orders > 0 else 0
num_customers = df["CUSTOMERNAME"].nunique()
cac           = round(500 / num_customers * 100, 2) if num_customers > 0 else 0

# YoY Revenue Growth
rev_by_year = df_all.groupby("YEAR_ID")["SALES"].sum()
if len(rev_by_year) >= 2 and 2004 in rev_by_year and 2003 in rev_by_year:
    yoy_growth = ((rev_by_year[2004] - rev_by_year[2003]) / rev_by_year[2003]) * 100
else:
    yoy_growth = 0

# Retention
c2004 = set(df_all[df_all["YEAR_ID"] == 2004]["CUSTOMERNAME"])
c2005 = set(df_all[df_all["YEAR_ID"] == 2005]["CUSTOMERNAME"])
retained  = len(c2004 & c2005)
retention = round((retained / len(c2004)) * 100, 1) if len(c2004) > 0 else 0

# ── Header ───────────────────────────────────────────────────
st.markdown(f"""
<div class="dashboard-header">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <div class="dashboard-title">Sales Intelligence Center</div>
            <div class="dashboard-subtitle">
                Showing data for {', '.join(str(y) for y in sorted(selected_years)) if selected_years else 'No years selected'} 
                &nbsp;·&nbsp; {len(df):,} transactions &nbsp;·&nbsp; {num_customers} customers
            </div>
        </div>
        <div class="live-badge">
            <div class="live-dot"></div> LIVE DATA
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── KPI Cards Row ─────────────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class="kpi-card kpi-blue">
        <div class="kpi-label">Total Revenue</div>
        <div class="kpi-value">${total_revenue/1e6:.2f}M</div>
        <div class="kpi-delta delta-up">↑ {yoy_growth:.1f}% YoY growth</div>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card kpi-teal">
        <div class="kpi-label">Total Profit</div>
        <div class="kpi-value">${total_profit/1e6:.2f}M</div>
        <div class="kpi-delta delta-up">↑ {profit_margin:.1f}% margin</div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card kpi-amber">
        <div class="kpi-label">Avg Order Value</div>
        <div class="kpi-value">${avg_order:,.0f}</div>
        <div class="kpi-delta delta-neu">→ {total_orders:,} total orders</div>
    </div>""", unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card kpi-red">
        <div class="kpi-label">Cust. Acq. Cost</div>
        <div class="kpi-value">${cac:,.0f}</div>
        <div class="kpi-delta delta-neu">→ {num_customers} customers</div>
    </div>""", unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class="kpi-card kpi-purple">
        <div class="kpi-label">Retention Rate</div>
        <div class="kpi-value">{retention}%</div>
        <div class="kpi-delta {'delta-up' if retention >= 50 else 'delta-down'}">
            {'↑ Strong' if retention >= 50 else '↓ Needs attention'} retention
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Tabs ─────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊  Overview",
    "📦  Products",
    "🌍  Regions",
    "📈  Trends & YoY",
    "💼  Deal Analysis"
])

# ════════════════════════════════════════════════════════════
# TAB 1 — OVERVIEW
# ════════════════════════════════════════════════════════════
with tab1:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="section-header">Monthly Revenue & Profit</div>', unsafe_allow_html=True)
        df_monthly = df.groupby("MONTH").agg(revenue=("SALES","sum"), profit=("PROFIT","sum")).reset_index().sort_values("MONTH")

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df_monthly["MONTH"], y=df_monthly["revenue"],
            name="Revenue", fill="tozeroy",
            fillcolor="rgba(99,179,237,0.08)",
            line=dict(color=ACCENT, width=2.5),
            mode="lines+markers",
            marker=dict(size=5, color=ACCENT)
        ))
        fig.add_trace(go.Scatter(
            x=df_monthly["MONTH"], y=df_monthly["profit"],
            name="Profit", fill="tozeroy",
            fillcolor="rgba(79,209,197,0.06)",
            line=dict(color=TEAL, width=2, dash="dot"),
            mode="lines+markers",
            marker=dict(size=4, color=TEAL)
        ))
        fig.update_xaxes(tickangle=45, tickfont=dict(size=9))
        chart_layout(fig, height=340)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-header">Revenue Split</div>', unsafe_allow_html=True)
        df_deal = df.groupby("DEALSIZE")["SALES"].sum().reset_index()
        fig = go.Figure(go.Pie(
            labels=df_deal["DEALSIZE"],
            values=df_deal["SALES"],
            hole=0.65,
            marker=dict(colors=[ACCENT, TEAL, AMBER], line=dict(color=CHART_BG, width=3)),
            textfont=dict(size=11),
            textinfo="label+percent"
        ))
        fig.add_annotation(
            text=f"${total_revenue/1e6:.1f}M",
            x=0.5, y=0.5, showarrow=False,
            font=dict(family="Syne", size=18, color="#F1F5F9")
        )
        chart_layout(fig, height=340)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-header">Top 10 Customers</div>', unsafe_allow_html=True)
    df_cust = df.groupby("CUSTOMERNAME").agg(
        revenue=("SALES","sum"),
        orders=("ORDERNUMBER","count"),
        profit=("PROFIT","sum")
    ).reset_index().sort_values("revenue", ascending=False).head(10)
    df_cust["margin"] = (df_cust["profit"] / df_cust["revenue"] * 100).round(1)
    df_cust["revenue_fmt"] = df_cust["revenue"].apply(lambda x: f"${x:,.0f}")
    df_cust["profit_fmt"]  = df_cust["profit"].apply(lambda x: f"${x:,.0f}")
    df_cust["margin_fmt"]  = df_cust["margin"].apply(lambda x: f"{x}%")
    st.dataframe(
        df_cust[["CUSTOMERNAME","revenue_fmt","profit_fmt","margin_fmt","orders"]].rename(columns={
            "CUSTOMERNAME":"Customer","revenue_fmt":"Revenue",
            "profit_fmt":"Profit","margin_fmt":"Margin","orders":"Orders"
        }),
        use_container_width=True, hide_index=True
    )

# ════════════════════════════════════════════════════════════
# TAB 2 — PRODUCTS
# ════════════════════════════════════════════════════════════
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">Revenue by Product Line</div>', unsafe_allow_html=True)
        df_prod = df.groupby("PRODUCTLINE").agg(revenue=("SALES","sum"), profit=("PROFIT","sum"), orders=("ORDERNUMBER","count")).reset_index().sort_values("revenue", ascending=True)
        fig = go.Figure(go.Bar(
            x=df_prod["revenue"], y=df_prod["PRODUCTLINE"],
            orientation="h",
            marker=dict(
                color=df_prod["revenue"],
                colorscale=[[0,"#1A3550"],[0.5,ACCENT],[1,"#90CDF4"]],
                line=dict(color="rgba(0,0,0,0)")
            ),
            text=df_prod["revenue"].apply(lambda x: f"${x/1e3:.0f}K"),
            textposition="outside",
            textfont=dict(size=11, color="#CBD5E0")
        ))
        chart_layout(fig, height=360)
        fig.update_layout(yaxis=dict(tickfont=dict(size=12)))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-header">Profit Margin by Product</div>', unsafe_allow_html=True)
        df_prod["margin"] = (df_prod["profit"] / df_prod["revenue"] * 100).round(1)
        fig = go.Figure(go.Bar(
            x=df_prod["margin"], y=df_prod["PRODUCTLINE"],
            orientation="h",
            marker=dict(
                color=df_prod["margin"],
                colorscale=[[0,"#1A3550"],[0.5,TEAL],[1,"#81E6D9"]],
            ),
            text=df_prod["margin"].apply(lambda x: f"{x}%"),
            textposition="outside",
            textfont=dict(size=11, color="#CBD5E0")
        ))
        chart_layout(fig, height=360)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-header">Product Performance Over Time</div>', unsafe_allow_html=True)
    df_pt = df.groupby(["MONTH","PRODUCTLINE"])["SALES"].sum().reset_index()
    fig = px.line(df_pt, x="MONTH", y="SALES", color="PRODUCTLINE",
                  color_discrete_sequence=COLORS, markers=False)
    fig.update_traces(line=dict(width=2))
    fig.update_xaxes(tickangle=45, tickfont=dict(size=9))
    chart_layout(fig, height=320)
    st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════
# TAB 3 — REGIONS
# ════════════════════════════════════════════════════════════
with tab3:
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown('<div class="section-header">Revenue by Country</div>', unsafe_allow_html=True)
        df_country = df.groupby("COUNTRY").agg(revenue=("SALES","sum"), orders=("ORDERNUMBER","count")).reset_index().sort_values("revenue", ascending=False)
        fig = px.choropleth(
            df_country, locations="COUNTRY", locationmode="country names",
            color="revenue", hover_name="COUNTRY",
            color_continuous_scale=[[0,"#0D1421"],[0.3,"#1E3A5F"],[0.7,ACCENT],[1,"#90CDF4"]],
            hover_data={"revenue": ":,.0f"}
        )
        fig.update_layout(
            paper_bgcolor=PAPER_BG, plot_bgcolor=CHART_BG,
            geo=dict(bgcolor=CHART_BG, lakecolor=CHART_BG, landcolor="#111827",
                     showframe=False, showcoastlines=True, coastlinecolor="rgba(99,179,237,0.2)"),
            coloraxis_colorbar=dict(tickfont=dict(color=FONT_COLOR), title=dict(font=dict(color=FONT_COLOR))),
            margin=dict(l=0,r=0,t=40,b=0), height=360
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-header">Top Countries</div>', unsafe_allow_html=True)
        fig = go.Figure(go.Bar(
            x=df_country.head(10)["revenue"],
            y=df_country.head(10)["COUNTRY"],
            orientation="h",
            marker=dict(color=COLORS[:10]),
            text=df_country.head(10)["revenue"].apply(lambda x: f"${x/1e3:.0f}K"),
            textposition="outside",
            textfont=dict(size=10, color="#CBD5E0")
        ))
        chart_layout(fig, height=360)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-header">Territory Performance</div>', unsafe_allow_html=True)
    df_terr = df.groupby("TERRITORY").agg(
        revenue=("SALES","sum"), profit=("PROFIT","sum"), orders=("ORDERNUMBER","count")
    ).reset_index().dropna()
    col1, col2, col3 = st.columns(len(df_terr))
    for i, (_, row) in enumerate(df_terr.iterrows()):
        with [col1,col2,col3][i % 3]:
            margin = row["profit"]/row["revenue"]*100
            st.markdown(f"""
            <div class="kpi-card" style="text-align:center; margin-bottom:10px;">
                <div class="kpi-label">{row['TERRITORY']}</div>
                <div class="kpi-value" style="font-size:20px;">${row['revenue']/1e3:.0f}K</div>
                <div class="kpi-delta delta-up">{margin:.1f}% margin · {int(row['orders'])} orders</div>
            </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# TAB 4 — TRENDS & YOY
# ════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="section-header">Year-over-Year Revenue Comparison</div>', unsafe_allow_html=True)

    df_yoy = df_all.groupby(["YEAR_ID","MONTH_ID"])["SALES"].sum().reset_index()
    df_yoy["MONTH_NAME"] = pd.to_datetime(df_yoy["MONTH_ID"], format="%m").dt.strftime("%b")

    fig = go.Figure()
    year_colors = {2003: ACCENT, 2004: TEAL, 2005: AMBER}
    year_dashes = {2003: "solid", 2004: "dot", 2005: "dash"}

    for year in sorted(df_yoy["YEAR_ID"].unique()):
        d = df_yoy[df_yoy["YEAR_ID"] == year].sort_values("MONTH_ID")
        fig.add_trace(go.Scatter(
            x=d["MONTH_NAME"], y=d["SALES"],
            name=str(year),
            line=dict(color=year_colors.get(year, ACCENT), width=2.5, dash=year_dashes.get(year,"solid")),
            mode="lines+markers",
            marker=dict(size=6)
        ))
    chart_layout(fig, height=360)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">Annual Revenue Summary</div>', unsafe_allow_html=True)
        df_annual = df_all.groupby("YEAR_ID").agg(
            revenue=("SALES","sum"), profit=("PROFIT","sum"), orders=("ORDERNUMBER","count")
        ).reset_index()
        df_annual["growth"] = df_annual["revenue"].pct_change() * 100
        df_annual["margin"] = df_annual["profit"] / df_annual["revenue"] * 100

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Bar(
            x=df_annual["YEAR_ID"].astype(str), y=df_annual["revenue"],
            name="Revenue", marker_color=[ACCENT, TEAL, AMBER],
            text=df_annual["revenue"].apply(lambda x: f"${x/1e3:.0f}K"),
            textposition="outside", textfont=dict(size=10)
        ), secondary_y=False)
        fig.add_trace(go.Scatter(
            x=df_annual["YEAR_ID"].astype(str), y=df_annual["growth"],
            name="Growth %", line=dict(color=GREEN, width=2.5),
            mode="lines+markers", marker=dict(size=8, color=GREEN),
            yaxis="y2"
        ), secondary_y=True)
        fig.update_layout(paper_bgcolor=PAPER_BG, plot_bgcolor=CHART_BG,
                          font=dict(family="DM Sans", color=FONT_COLOR),
                          height=320, margin=dict(l=16,r=16,t=48,b=16),
                          legend=dict(bgcolor="rgba(0,0,0,0)"),
                          xaxis=dict(gridcolor=GRID_COLOR),
                          yaxis=dict(gridcolor=GRID_COLOR),
                          yaxis2=dict(gridcolor="rgba(0,0,0,0)", ticksuffix="%"))
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-header">Monthly Seasonality Heatmap</div>', unsafe_allow_html=True)
        df_heat = df_all.groupby(["YEAR_ID","MONTH_ID"])["SALES"].sum().reset_index()
        df_pivot = df_heat.pivot(index="YEAR_ID", columns="MONTH_ID", values="SALES").fillna(0)
        month_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        fig = go.Figure(go.Heatmap(
            z=df_pivot.values,
            x=[month_labels[i-1] for i in df_pivot.columns],
            y=df_pivot.index.astype(str),
            colorscale=[[0,"#0D1421"],[0.3,"#1E3A5F"],[0.7,ACCENT],[1,"#BEE3F8"]],
            text=[[f"${v/1e3:.0f}K" for v in row] for row in df_pivot.values],
            texttemplate="%{text}",
            textfont=dict(size=10),
            showscale=False
        ))
        chart_layout(fig, height=320)
        st.plotly_chart(fig, use_container_width=True)

    # AI Insights
    st.markdown('<div class="section-header">📌 Analyst Insights</div>', unsafe_allow_html=True)
    best_month_idx = df_all.groupby("MONTH_ID")["SALES"].sum().idxmax()
    best_month_name = pd.to_datetime(str(best_month_idx), format="%m").strftime("%B")
    best_year = int(df_all.groupby("YEAR_ID")["SALES"].sum().idxmax())
    best_product = df_all.groupby("PRODUCTLINE")["SALES"].sum().idxmax()

    st.markdown(f"""
    <div class="insight-card success">
        📈 <strong>Peak Performance:</strong> {best_month_name} is consistently the strongest revenue month across all years,
        with {best_year} being the highest-performing year overall.
    </div>
    <div class="insight-card">
        📦 <strong>Product Dominance:</strong> {best_product} leads all product lines in revenue generation.
        Consider expanding inventory and marketing spend in this category.
    </div>
    <div class="insight-card warning">
        ⚠️ <strong>Seasonality Risk:</strong> Revenue shows high concentration in Q4 (Oct–Nov).
        Developing Q2 promotions could smooth revenue distribution and reduce quarterly volatility.
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# TAB 5 — DEAL ANALYSIS
# ════════════════════════════════════════════════════════════
with tab5:
    col1, col2, col3 = st.columns(3)

    df_deal_full = df.groupby("DEALSIZE").agg(
        revenue=("SALES","sum"),
        profit=("PROFIT","sum"),
        orders=("ORDERNUMBER","count"),
        avg_value=("SALES","mean"),
        customers=("CUSTOMERNAME","nunique")
    ).reset_index()

    deal_colors = {"Small": ACCENT, "Medium": TEAL, "Large": AMBER}

    for i, (_, row) in enumerate(df_deal_full.iterrows()):
        with [col1, col2, col3][i % 3]:
            margin = row["profit"] / row["revenue"] * 100
            color  = deal_colors.get(row["DEALSIZE"], ACCENT)
            st.markdown(f"""
            <div class="kpi-card" style="border-bottom: 3px solid {color}; margin-bottom: 16px;">
                <div class="kpi-label">{row['DEALSIZE']} Deals</div>
                <div class="kpi-value">${row['revenue']/1e3:.0f}K</div>
                <div style="margin-top:12px; display:grid; grid-template-columns:1fr 1fr; gap:8px;">
                    <div>
                        <div style="font-size:10px;color:#475569;">Orders</div>
                        <div style="font-size:14px;font-weight:600;color:#CBD5E0;">{int(row['orders']):,}</div>
                    </div>
                    <div>
                        <div style="font-size:10px;color:#475569;">Avg Value</div>
                        <div style="font-size:14px;font-weight:600;color:#CBD5E0;">${row['avg_value']:,.0f}</div>
                    </div>
                    <div>
                        <div style="font-size:10px;color:#475569;">Margin</div>
                        <div style="font-size:14px;font-weight:600;color:{color};">{margin:.1f}%</div>
                    </div>
                    <div>
                        <div style="font-size:10px;color:#475569;">Customers</div>
                        <div style="font-size:14px;font-weight:600;color:#CBD5E0;">{int(row['customers'])}</div>
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">Deal Size Mix by Year</div>', unsafe_allow_html=True)
        df_deal_yr = df_all.groupby(["YEAR_ID","DEALSIZE"])["SALES"].sum().reset_index()
        fig = px.bar(df_deal_yr, x="YEAR_ID", y="SALES", color="DEALSIZE",
                     barmode="group",
                     color_discrete_map=deal_colors,
                     text_auto=False)
        fig.update_traces(texttemplate="$%{y:.0f}", textposition="outside")
        chart_layout(fig, height=340)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown('<div class="section-header">Deal Size by Product Line</div>', unsafe_allow_html=True)
        df_deal_prod = df.groupby(["PRODUCTLINE","DEALSIZE"])["SALES"].sum().reset_index()
        fig = px.bar(df_deal_prod, x="PRODUCTLINE", y="SALES", color="DEALSIZE",
                     barmode="stack", color_discrete_map=deal_colors)
        fig.update_xaxes(tickangle=30, tickfont=dict(size=10))
        chart_layout(fig, height=340)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-header">Deal Conversion Funnel</div>', unsafe_allow_html=True)
    df_status = df.groupby("STATUS")["SALES"].sum().reset_index().sort_values("SALES", ascending=False)
    fig = go.Figure(go.Funnel(
        y=df_status["STATUS"],
        x=df_status["SALES"],
        textinfo="value+percent initial",
        marker=dict(color=[ACCENT, TEAL, AMBER, GREEN, RED, PURPLE][:len(df_status)]),
        textfont=dict(size=12)
    ))
    chart_layout(fig, height=320)
    st.plotly_chart(fig, use_container_width=True)

# ── Footer ───────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div class="footer">
    KPI Intelligence Center &nbsp;·&nbsp; Built by Samuel Oyedokun &nbsp;·&nbsp; 
    Powered by Streamlit & Plotly &nbsp;·&nbsp; Data: 2003–2005 Sales Records
</div>
""", unsafe_allow_html=True)