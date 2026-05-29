import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import pandas as pd
import plotly.express as px

from app.data_loader import (
    load_data
)

from app.file_detector import (
    detect_file_type
)

from app.sales_analyzer import (
    analyze_sales
)

from app.invoice_analyzer import (
    analyze_invoices
)

from app.lead_analyzer import (
    analyze_leads
)

from app.analytics import (
    generate_analytics
)

from app.insights import (
    generate_insights
)

from app.forecast import (
    forecast_revenue
)

from app.executive_dashboard import (
    build_executive_summary
)

from app.exporter import (
    export_csv,
    export_excel
)

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="DataVault AI",
    layout="wide"
)

st.title(
    "📊 DataVault AI"
)

st.markdown(
    """
    Upload Sales, Invoice, or Lead datasets
    and automatically generate analytics,
    dashboards, exports, and AI insights.
    """
)

# ==================================
# FILE UPLOAD
# ==================================

uploaded_file = st.file_uploader(
    "Upload CSV or XLSX",
    type=[
        "csv",
        "xlsx"
    ]
)

# ==================================
# PROCESS FILE
# ==================================

if uploaded_file:

    df = load_data(
        uploaded_file
    )

    dataset_type = (
        detect_file_type(
            df
        )
    )

    st.success(
        f"Detected Dataset: {dataset_type.upper()}"
    )


    summary = (
        build_executive_summary(
            dataset_type,
            df
        )
    )

    st.subheader(
        "🏢 Executive Overview"
    )

    cols = st.columns(
        len(summary)
    )

    for i, (
        key,
        value
    ) in enumerate(
        summary.items()
    ):

        if isinstance(
            value,
            float
        ):

            cols[i].metric(
                key,
                f"${value:,.2f}"
            )

        else:

            cols[i].metric(
                key,
                value
            )

    # ==================================
    # SALES DASHBOARD
    # ==================================

    if dataset_type == "sales":

        analytics = (
            generate_analytics(
                df
            )
        )

        st.subheader(
            "📈 Executive Dashboard"
        )

        col1, col2, col3, col4, col5 = (
            st.columns(5)
        )

        col1.metric(
            "Revenue",
            f"${analytics['Revenue']:,.2f}"
        )

        col2.metric(
            "Profit",
            f"${analytics['Profit']:,.2f}"
        )

        col3.metric(
            "Orders",
            analytics["Orders"]
        )

        col4.metric(
            "Avg Order",
            f"${analytics['Average Order']:,.2f}"
        )

        col5.metric(
            "Margin %",
            f"{analytics['Margin']}%"
        )

        st.subheader(
            "📋 Sales Records"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        # ======================
        # REVENUE BY REGION
        # ======================

        st.subheader(
            "🌍 Revenue by Region"
        )

        region_df = (
            df.groupby(
                "Region",
                as_index=False
            )["Revenue"]
            .sum()
        )

        region_chart = px.bar(
            region_df,
            x="Region",
            y="Revenue",
            title="Revenue by Region"
        )

        st.plotly_chart(
            region_chart,
            use_container_width=True
        )

        # ======================
        # FORECASTING
        # ======================

        forecast = (
            forecast_revenue(
                df
            )
        )

        if forecast:

            st.subheader(
                "🔮 Revenue Forecast"
            )

            st.metric(

                "Predicted Next Revenue",

                f"${forecast['Predicted Revenue']:,.2f}"

            )

            revenue_trend = (

                df.groupby(
                    "Date",
                    as_index=False
                )["Revenue"]
                .sum()

            )

            trend_chart = px.line(

                revenue_trend,

                x="Date",

                y="Revenue",

                title=
                "Revenue Trend"

            )

            st.plotly_chart(

                trend_chart,

                use_container_width=True

            )

        # ======================
        # TOP PRODUCTS
        # ======================

        st.subheader(
            "🏆 Top Products"
        )

        product_df = (
            df.groupby(
                "Product",
                as_index=False
            )["Revenue"]
            .sum()
            .sort_values(
                "Revenue",
                ascending=False
            )
            .head(10)
        )

        product_chart = px.bar(
            product_df,
            x="Product",
            y="Revenue",
            title="Top Products"
        )

        st.plotly_chart(
            product_chart,
            use_container_width=True
        )

        # ======================
        # PROFIT BY CATEGORY
        # ======================

        st.subheader(
            "💰 Profit by Category"
        )

        category_df = (
            df.groupby(
                "Category",
                as_index=False
            )["Profit"]
            .sum()
        )

        category_chart = px.pie(
            category_df,
            names="Category",
            values="Profit",
            title="Profit by Category"
        )

        st.plotly_chart(
            category_chart,
            use_container_width=True
        )

    # ==================================
    # INVOICE DASHBOARD
    # ==================================

    elif dataset_type == "invoice":

        metrics = (
            analyze_invoices(
                df
            )
        )

        st.subheader(
            "🧾 Invoice Dashboard"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Invoices",
            metrics["Invoices"]
        )

        col2.metric(
            "Vendors",
            metrics["Vendors"]
        )

        col3.metric(
            "Total Spend",
            f"${metrics['Total Spend']:,.2f}"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        vendor_df = (
            df.groupby(
                "Vendor",
                as_index=False
            )["Total"]
            .sum()
        )

        vendor_chart = px.bar(
            vendor_df,
            x="Vendor",
            y="Total",
            title="Spend by Vendor"
        )

        st.plotly_chart(
            vendor_chart,
            use_container_width=True
        )

    # ==================================
    # LEAD DASHBOARD
    # ==================================

    elif dataset_type == "lead":

        metrics = (
            analyze_leads(
                df
            )
        )

        st.subheader(
            "🎯 Lead Dashboard"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Companies",
            metrics["Companies"]
        )

        col2.metric(
            "Cities",
            metrics["Cities"]
        )

        col3.metric(
            "Emails",
            metrics["Emails"]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        city_df = (
            df["City"]
            .value_counts()
            .reset_index()
        )

        city_df.columns = [
            "City",
            "Count"
        ]

        city_chart = px.bar(
            city_df,
            x="City",
            y="Count",
            title="Leads by City"
        )

        st.plotly_chart(
            city_chart,
            use_container_width=True
        )

    else:

        st.warning(
            "Dataset type not recognized."
        )

    # ==================================
    # AI INSIGHTS
    # ==================================

    st.subheader(
        "🤖 AI Insights"
    )

    insights = generate_insights(
        dataset_type,
        df
    )

    for insight in insights:

        st.info(
            insight
        )

    # ==================================
    # EXPORTS
    # ==================================

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    csv_path = (
        "outputs/report.csv"
    )

    excel_path = (
        "outputs/report.xlsx"
    )

    export_csv(
        df,
        csv_path
    )

    export_excel(
        df,
        excel_path
    )

    st.subheader(
        "⬇ Downloads"
    )

    col1, col2 = st.columns(2)

    with col1:

        with open(
            csv_path,
            "rb"
        ) as file:

            st.download_button(
                "Download CSV",
                file,
                file_name="report.csv"
            )

    with col2:

        with open(
            excel_path,
            "rb"
        ) as file:

            st.download_button(
                "Download Excel",
                file,
                file_name="report.xlsx"
            )