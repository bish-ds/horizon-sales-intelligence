import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set page configuration
st.set_page_config(
    page_title="Horizon Sales Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Inter & Outfit fonts and apply custom styling (no empty lines to prevent markdown parsing leakage)
st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet"><style>.stApp {background-color: #0B0F19 !important;color: #F8FAFC !important;}html, body, [class*="css"] {font-family: 'Inter', sans-serif;}h1, h2, h3, h4, h5, h6 {font-family: 'Outfit', sans-serif;font-weight: 700;color: #F8FAFC !important;}[data-testid="stSidebar"] {background-color: #030712 !important;border-right: 1px solid rgba(148, 163, 184, 0.08) !important;}[data-testid="stSidebar"] hr {border-color: rgba(148, 163, 184, 0.1) !important;}[data-testid="stVerticalBlockBorderOnly"] {border-radius: 16px !important;border: 1px solid rgba(148, 163, 184, 0.1) !important;padding: 24px !important;background-color: rgba(17, 24, 39, 0.5) !important;box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2) !important;transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);}[data-testid="stVerticalBlockBorderOnly"]:hover {transform: translateY(-3px);border-color: rgba(59, 130, 246, 0.3) !important;box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.4) !important;background-color: rgba(17, 24, 39, 0.6) !important;}div[data-testid="stMetric"] {background-color: rgba(17, 24, 39, 0.5) !important;border: 1px solid rgba(148, 163, 184, 0.1) !important;padding: 15px !important;border-radius: 12px !important;}div[data-testid="stMetric"] label {color: #94A3B8 !important;}div[data-testid="stMetric"] div[data-testid="stMetricValue"] {color: #F8FAFC !important;}</style>""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    # Load the exported EDA dataset using an absolute path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "Sales_data(EDA Exported).csv")
    df = pd.read_csv(file_path)
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar: Render a premium SVG logo instead of an external image
st.sidebar.markdown("""
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 5px;">
    <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" style="border-radius: 10px;">
        <rect width="40" height="40" rx="10" fill="url(#paint0_linear)"/>
        <path d="M12 28V18M20 28V12M28 28V22" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M10 14L16 10L24 16L30 8" stroke="#60A5FA" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        <defs>
            <linearGradient id="paint0_linear" x1="0" y1="0" x2="40" y2="40" gradientUnits="userSpaceOnUse">
                <stop stop-color="#3B82F6"/>
                <stop offset="1" stop-color="#8B5CF6"/>
            </linearGradient>
        </defs>
    </svg>
    <div>
        <h2 style='margin: 0; font-size: 22px; line-height: 1.1; color: #F8FAFC;'>Horizon</h2>
        <p style='margin: 0; font-size: 12px; opacity: 0.7; color: #94A3B8;'>Sales Intelligence</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown("<h3 style='font-size: 16px; color: #F8FAFC; margin-bottom: 10px;'>🎛️ Filters</h3>", unsafe_allow_html=True)
selected_region = st.sidebar.multiselect("Select Region", options=df['us_region'].dropna().unique(), default=df['us_region'].dropna().unique())
selected_channel = st.sidebar.multiselect("Select Channel", options=df['channel'].dropna().unique(), default=df['channel'].dropna().unique())

filtered_df = df[
    (df['us_region'].isin(selected_region)) &
    (df['channel'].isin(selected_channel))
]

# Title Header (Clean and professional, no emojis)
st.markdown("<h1 style='font-size: 38px; margin-bottom: 5px; color: #F8FAFC;'>Horizon Sales Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 16px; opacity: 0.8; margin-bottom: 30px; color: #94A3B8;'>Analyzing Acme Co.'s sales data to optimize pricing, promotions, and market expansion.</p>", unsafe_allow_html=True)

# KPI Cards generator
def kpi_card(title, value, gradient_from, gradient_to, icon):
    html = f"""
    <div style="
        background: linear-gradient(135deg, {gradient_from} 0%, {gradient_to} 100%);
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.15);
        color: white;
        font-family: 'Inter', sans-serif;
        position: relative;
        overflow: hidden;
        margin-bottom: 15px;
        min-height: 120px;
    ">
        <div style="position: absolute; right: -5px; bottom: -15px; font-size: 70px; opacity: 0.12; user-select: none;">
            {icon}
        </div>
        <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1.5px; opacity: 0.85; font-weight: 600;">{title}</div>
        <div style="font-size: 1.9rem; font-weight: 800; margin-top: 8px; line-height: 1.2; letter-spacing: -0.5px;">{value}</div>
    </div>
    """
    return html

# Metrics Calculation
revenue = filtered_df['revenue'].sum()
profit = filtered_df['profit'].sum()
orders = filtered_df['order_number'].nunique()
margin = (profit / revenue * 100) if revenue > 0 else 0

# KPI row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(kpi_card("Total Revenue", f"${revenue:,.0f}", "#0F172A", "#1D4ED8", "💵"), unsafe_allow_html=True)
with col2:
    st.markdown(kpi_card("Total Profit", f"${profit:,.0f}", "#064E3B", "#059669", "📈"), unsafe_allow_html=True)
with col3:
    st.markdown(kpi_card("Total Orders", f"{orders:,}", "#4C1D95", "#7C3AED", "🛒"), unsafe_allow_html=True)
with col4:
    st.markdown(kpi_card("Avg Profit Margin", f"{margin:.1f}%", "#78350F", "#D97706", "📊"), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Helper function to apply dark-theme compatible styling to Plotly charts
def style_chart(fig):
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10),
        font=dict(family="Inter, sans-serif", size=11, color="#94A3B8"),
        xaxis=dict(
            showgrid=False,
            color="#64748B",
            tickfont=dict(size=10)
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(148, 163, 184, 0.08)",
            color="#64748B",
            tickfont=dict(size=10)
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=10, color="#94A3B8")
        )
    )

# Charts Section
col_left, col_right = st.columns(2)

with col_left:
    with st.container(border=True):
        st.markdown("<h3 style='font-size: 18px; margin-bottom: 15px; color: #F8FAFC;'>🗺️ Revenue by Region</h3>", unsafe_allow_html=True)
        region_data = filtered_df.groupby('us_region')['revenue'].sum().reset_index().sort_values('revenue', ascending=False)
        fig_region = px.bar(
            region_data,
            x='us_region', y='revenue',
            labels={'us_region': 'Region', 'revenue': 'Revenue ($)'},
            color='revenue',
            color_continuous_scale=['#1E3A8A', '#3B82F6']
        )
        style_chart(fig_region)
        fig_region.update_coloraxes(showscale=False)
        fig_region.update_traces(marker=dict(line=dict(width=0)))
        st.plotly_chart(fig_region, use_container_width=True)

with col_right:
    with st.container(border=True):
        st.markdown("<h3 style='font-size: 18px; margin-bottom: 15px; color: #F8FAFC;'>📈 Sales Trend Over Time</h3>", unsafe_allow_html=True)
        monthly_sales = filtered_df.groupby(filtered_df['order_date'].dt.to_period("M"))['revenue'].sum().reset_index()
        monthly_sales['order_date'] = monthly_sales['order_date'].astype(str)
        fig_trend = px.area(
            monthly_sales, x='order_date', y='revenue',
            labels={'order_date': 'Month', 'revenue': 'Revenue ($)'}
        )
        style_chart(fig_trend)
        fig_trend.update_traces(
            line=dict(color='#3B82F6', width=3),
            fillcolor='rgba(59, 130, 246, 0.1)'
        )
        st.plotly_chart(fig_trend, use_container_width=True)

col_bottom_left, col_bottom_right = st.columns(2)

with col_bottom_left:
    with st.container(border=True):
        st.markdown("<h3 style='font-size: 18px; margin-bottom: 15px; color: #F8FAFC;'>🍰 Profit Contribution by Channel</h3>", unsafe_allow_html=True)
        channel_data = filtered_df.groupby('channel')['profit'].sum().reset_index()
        fig_channel = px.pie(
            channel_data,
            names='channel', values='profit',
            hole=0.5,
            color_discrete_sequence=['#3B82F6', '#10B981', '#F59E0B', '#8B5CF6']
        )
        style_chart(fig_channel)
        fig_channel.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            marker=dict(line=dict(color='#0B0F19', width=2))
        )
        st.plotly_chart(fig_channel, use_container_width=True)

with col_bottom_right:
    with st.container(border=True):
        st.markdown("<h3 style='font-size: 18px; margin-bottom: 15px; color: #F8FAFC;'>🏆 Top 10 Products by Revenue</h3>", unsafe_allow_html=True)
        top_products = filtered_df.groupby('product_name')['revenue'].sum().reset_index().nlargest(10, 'revenue')
        fig_products = px.bar(
            top_products, x='revenue', y='product_name', orientation='h',
            labels={'revenue': 'Revenue ($)', 'product_name': 'Product'},
            color='revenue',
            color_continuous_scale=['#7C3AED', '#A78BFA']
        )
        style_chart(fig_products)
        fig_products.update_coloraxes(showscale=False)
        fig_products.update_layout(yaxis={'categoryorder': 'total ascending'})
        fig_products.update_traces(marker=dict(line=dict(width=0)))
        st.plotly_chart(fig_products, use_container_width=True)

st.markdown("<br><hr style='border: 1px solid rgba(148, 163, 184, 0.08);'><br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; opacity: 0.6; font-size: 13px; font-family: Inter, sans-serif; padding-bottom: 30px; color: #94A3B8;'>"
    "Horizon USA Sales Intelligence Hub • Built with Python & Streamlit • Data range: 2014-2018"
    "</div>",
    unsafe_allow_html=True
)
