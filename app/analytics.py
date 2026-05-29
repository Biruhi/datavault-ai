import pandas as pd


def generate_analytics(df):

    revenue = (
        df["Revenue"]
        .sum()
    )

    profit = (
        df["Profit"]
        .sum()
    )

    orders = len(df)

    avg_order = (
        revenue / orders
        if orders > 0
        else 0
    )

    margin = (
        (profit / revenue) * 100
        if revenue > 0
        else 0
    )

    return {

        "Revenue":
        round(
            revenue,
            2
        ),

        "Profit":
        round(
            profit,
            2
        ),

        "Orders":
        orders,

        "Average Order":
        round(
            avg_order,
            2
        ),

        "Margin":
        round(
            margin,
            2
        )
    }