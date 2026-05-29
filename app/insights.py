def generate_insights(
    dataset_type,
    df
):

    insights = []

    # ======================
    # SALES INSIGHTS
    # ======================

    if dataset_type == "sales":

        top_region = (

            df.groupby(
                "Region"
            )["Revenue"]
            .sum()
            .idxmax()

        )

        top_product = (

            df.groupby(
                "Product"
            )["Revenue"]
            .sum()
            .idxmax()

        )

        revenue = (
            df["Revenue"]
            .sum()
        )

        profit = (
            df["Profit"]
            .sum()
        )

        margin = (
            (profit / revenue) * 100
            if revenue > 0
            else 0
        )

        insights.append(

            f"Top revenue region is {top_region}."

        )

        insights.append(

            f"Best performing product is {top_product}."

        )

        insights.append(

            f"Overall profit margin is {margin:.2f}%."
        )

    # ======================
    # INVOICE INSIGHTS
    # ======================

    elif dataset_type == "invoice":

        top_vendor = (

            df.groupby(
                "Vendor"
            )["Total"]
            .sum()
            .idxmax()

        )

        total_spend = (
            df["Total"]
            .sum()
        )

        insights.append(

            f"Highest spending vendor is {top_vendor}."
        )

        insights.append(

            f"Total vendor spend is ${total_spend:,.2f}."
        )

    # ======================
    # LEAD INSIGHTS
    # ======================

    elif dataset_type == "lead":

        top_city = (

            df["City"]
            .value_counts()
            .idxmax()

        )

        insights.append(

            f"Most leads are located in {top_city}."
        )

        insights.append(

            f"Lead database contains {len(df)} records."
        )

    return insights