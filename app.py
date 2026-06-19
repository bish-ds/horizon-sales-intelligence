import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Horizon Sales Intelligence",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for aesthetic improvements
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #1e3a8a;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    # Load the exported EDA dataset
    df = pd.read_csv("Sales_data(EDA Exported).csv")
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar for navigation & filtering
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3308/3308395.png", width=100)
st.sidebar.title("Horizon")
st.sidebar.subheader("Sales Intelligence")
st.sidebar.markdown("---")

st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect("Select Region", options=df['us_region'].dropna().unique(), default=df['us_region'].dropna().unique())
selected_channel = st.sidebar.multiselect("Select Channel", options=df['channel'].dropna().unique(), default=df['channel'].dropna().unique())

filtered_df = df[
    (df['us_region'].isin(selected_region)) &
    (df['channel'].isin(selected_channel))
]

# Main Dashboard Header
st.title("📈 USA Regional Sales Dashboard")
st.markdown("Analyze Acme Co.’s sales data to identify key revenue and profit drivers.")

# Top Level Metrics
revenue = filtered_df['revenue'].sum()
profit = filtered_df['profit'].sum()
orders = filtered_df['order_number'].nunique()
margin = (profit / revenue * 100) if revenue > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${revenue:,.0f}")
col2.metric("Total Profit", f"${profit:,.0f}")
col3.metric("Total Orders", f"{orders:,}")
col4.metric("Avg Profit Margin", f"{margin:.1f}%")

st.markdown("---")

# Charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Revenue by Region")
    fig_region = px.bar(
        filtered_df.groupby('us_region')['revenue'].sum().reset_index().sort_values('revenue', ascending=False),
        x='us_region', y='revenue',
        color='revenue', color_continuous_scale='Blues',
        labels={'us_region': 'Region', 'revenue': 'Revenue ($)'}
    )
    fig_region.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_region, use_container_width=True)

with col_right:
    st.subheader("Sales Trend Over Time")
    monthly_sales = filtered_df.groupby(filtered_df['order_date'].dt.to_period("M"))['revenue'].sum().reset_index()
    monthly_sales['order_date'] = monthly_sales['order_date'].astype(str)
    fig_trend = px.line(
        monthly_sales, x='order_date', y='revenue',
        markers=True, line_shape='spline',
        labels={'order_date': 'Month', 'revenue': 'Revenue ($)'}
    )
    fig_trend.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_trend, use_container_width=True)

st.markdown("---")

col_bottom_left, col_bottom_right = st.columns(2)

with col_bottom_left:
    st.subheader("Profit Margin by Channel")
    fig_channel = px.pie(
        filtered_df.groupby('channel')['profit'].sum().reset_index(),
        names='channel', values='profit',
        hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_channel, use_container_width=True)

with col_bottom_right:
    st.subheader("Top 10 Products by Revenue")
    top_products = filtered_df.groupby('product_name')['revenue'].sum().reset_index().nlargest(10, 'revenue')
    fig_products = px.bar(
        top_products, x='revenue', y='product_name', orientation='h',
        color='revenue', color_continuous_scale='Purples'
    )
    fig_products.update_layout(yaxis={'categoryorder': 'total ascending'}, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_products, use_container_width=True)

st.markdown("---")
st.markdown("Powered by **Horizon Analytics** | Data sourced from Acme Co. 2014-2018")
