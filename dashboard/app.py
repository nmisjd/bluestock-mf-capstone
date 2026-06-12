import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: #1E88E5;
}

[data-testid="metric-container"] {
    background-color: #262730;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #1E88E5;
}
</style>
""", unsafe_allow_html=True)
# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

perf_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_scheme_performance.csv"
)

tx_df = pd.read_csv(
    BASE_DIR / "data" / "processed" / "clean_transactions.csv"
)

portfolio_df = pd.read_csv(
    BASE_DIR / "data" / "raw" / "09_portfolio_holdings.csv"
)

# ==========================================
# TITLE
# ==========================================

st.title("📈 Mutual Fund Analytics Dashboard")
st.markdown("### Bluestock Fintech Capstone Project")

# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.header("Dashboard Filters")

selected_risk = st.sidebar.multiselect(
    "Risk Grade",
    sorted(perf_df["risk_grade"].dropna().unique()),
    default=list(sorted(perf_df["risk_grade"].dropna().unique()))
)

selected_category = st.sidebar.multiselect(
    "Category",
    sorted(perf_df["category"].dropna().unique()),
    default=list(sorted(perf_df["category"].dropna().unique()))
)

filtered_df = perf_df[
    (perf_df["risk_grade"].isin(selected_risk)) &
    (perf_df["category"].isin(selected_category))
]

# ==========================================
# TABS
# ==========================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Overview",
        "🏆 Fund Analytics",
        "👥 Investor Analytics",
        "📦 Portfolio Analytics"
    ]
)

# ==========================================
# TAB 1 - OVERVIEW
# ==========================================

with tab1:

    st.subheader("Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Average 1Y Return",
        f"{filtered_df['return_1yr_pct'].mean():.2f}%"
    )

    col2.metric(
        "Average Sharpe Ratio",
        f"{filtered_df['sharpe_ratio'].mean():.2f}"
    )

    col3.metric(
        "Highest AUM",
        f"₹ {filtered_df['aum_crore'].max():,.0f} Cr"
    )

    col4.metric(
        "Funds Analyzed",
        len(filtered_df)
    )

    st.divider()

    st.subheader("Risk vs Return Analysis")

    fig = px.scatter(
        filtered_df,
        x="std_dev_ann_pct",
        y="return_3yr_pct",
        color="risk_grade",
        size="aum_crore",
        hover_name="scheme_name",
        title="Risk vs Return Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Top 10 Performing Funds")

    top_funds = (
        filtered_df
        .sort_values(
            "return_3yr_pct",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_funds[
            [
                "scheme_name",
                "fund_house",
                "return_3yr_pct",
                "sharpe_ratio",
                "risk_grade"
            ]
        ],
        use_container_width=True
    )

# ==========================================
# TAB 2 - FUND ANALYTICS
# ==========================================

with tab2:

    st.subheader("Fund Screener")

    selected_fund = st.selectbox(
        "Select Fund",
        sorted(perf_df["scheme_name"].unique())
    )

    fund = perf_df[
        perf_df["scheme_name"] == selected_fund
    ]

    st.dataframe(
        fund,
        use_container_width=True
    )

    st.divider()

    st.subheader("Top Funds by Sharpe Ratio")

    sharpe_df = (
        filtered_df
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(10)
    )

    fig2 = px.bar(
        sharpe_df,
        x="sharpe_ratio",
        y="scheme_name",
        orientation="h",
        title="Top Funds by Sharpe Ratio"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ==========================================
# TAB 3 - INVESTOR ANALYTICS
# ==========================================

with tab3:

    colA, colB = st.columns(2)

    with colA:

        gender_fig = px.pie(
            tx_df,
            names="gender",
            title="Gender Distribution"
        )

        st.plotly_chart(
            gender_fig,
            use_container_width=True
        )

    with colB:

        city_fig = px.pie(
            tx_df,
            names="city_tier",
            title="City Tier Distribution"
        )

        st.plotly_chart(
            city_fig,
            use_container_width=True
        )

    st.divider()

    age_fig = px.histogram(
        tx_df,
        x="age_group",
        title="Investor Age Group Distribution"
    )

    st.plotly_chart(
        age_fig,
        use_container_width=True
    )

    st.divider()

    state_df = (
        tx_df.groupby("state")
        .size()
        .reset_index(name="transactions")
        .sort_values(
            "transactions",
            ascending=False
        )
        .head(15)
    )

    state_fig = px.bar(
        state_df,
        x="state",
        y="transactions",
        title="Top States by Transactions"
    )

    st.plotly_chart(
        state_fig,
        use_container_width=True
    )

# ==========================================
# TAB 4 - PORTFOLIO ANALYTICS
# ==========================================

with tab4:

    st.subheader("Sector Allocation")

    sector_alloc = (
        portfolio_df
        .groupby("sector")["weight_pct"]
        .sum()
        .reset_index()
    )

    sector_fig = px.pie(
        sector_alloc,
        names="sector",
        values="weight_pct",
        title="Sector Allocation"
    )

    st.plotly_chart(
        sector_fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Top Holdings")

    top_holdings = (
        portfolio_df
        .sort_values(
            "market_value_cr",
            ascending=False
        )
        .head(15)
    )

    holdings_fig = px.bar(
        top_holdings,
        x="stock_name",
        y="market_value_cr",
        color="sector",
        title="Top Holdings by Market Value"
    )

    st.plotly_chart(
        holdings_fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Top Holdings Table")

    st.dataframe(
        top_holdings[
            [
                "stock_name",
                "sector",
                "market_value_cr",
                "weight_pct"
            ]
        ],
        use_container_width=True
    )

# ==========================================
# DOWNLOAD SECTION
# ==========================================

st.divider()

csv = filtered_df.to_csv(index=False)

st.download_button(
    "⬇ Download Filtered Fund Data",
    csv,
    file_name="fund_analysis.csv",
    mime="text/csv"
)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")
st.markdown(
    """
    **Mutual Fund Analytics Platform**  
    Bluestock Data Analyst Internship Capstone Project  
    Developed by Sajid Ahmed
    """
)